# global
# import ivy
import numpy as np
from hypothesis import given, strategies as st


# local
import ivy_tests.test_ivy.helpers as helpers
import ivy.functional.backends.torch as ivy_torch


# noinspection DuplicatedCode
@st.composite
def _arrays_idx_n_dtypes(draw):
    num_dims = draw(st.shared(st.integers(1, 4), key="num_dims"))
    num_arrays = draw(st.shared(st.integers(2, 4), key="num_arrays"))
    common_shape = draw(
        helpers.lists(
            arg=st.integers(2, 3), min_size=num_dims - 1, max_size=num_dims - 1
        )
    )
    unique_idx = draw(helpers.integers(min_value=0, max_value=num_dims - 1))
    unique_dims = draw(
        helpers.lists(arg=st.integers(2, 3), min_size=num_arrays, max_size=num_arrays)
    )
    xs = list()
    available_dtypes = tuple(
        set(ivy_np.valid_float_dtypes).intersection(ivy_tests.valid_float_dtypes)
    )
    input_dtypes = draw(
        helpers.array_dtypes(available_dtypes=available_dtypes, shared_dtype=True)
    )
    for ud, dt in zip(unique_dims, input_dtypes):
        x = draw(
            helpers.array_values(
                shape=common_shape[:unique_idx] + [ud] + common_shape[unique_idx:],
                dtype=dt,
            )
        )
        xs.append(x)
    return xs, input_dtypes, unique_idx


# utilities
@given(
    xs_n_input_dtypes_n_unique_idx=_arrays_idx_n_dtypes(),
    as_variable=helpers.array_bools(),
    num_positional_args=helpers.num_positional_args(
        fn_name="ivy.functional.frontends.torch.result_type"
    ),
    native_array=helpers.array_bools(),
)
def test_torch_result_type(
    xs_n_input_dtypes_n_unique_idx,
    as_variable,
    num_positional_args,
    native_array,
    fw,
):
    xs, input_dtypes, unique_idx = xs_n_input_dtypes_n_unique_idx
    xs = [np.asarray(x, dtype=dt) for x, dt in zip(xs, input_dtypes)]
    helpers.test_frontend_function(
        input_dtypes=input_dtypes,
        as_variable_flags=as_variable,
        with_out=False,
        num_positional_args=num_positional_args,
        native_array_flags=native_array,
        fw=fw,
        frontend="torch",
        fn_name="result_type",
        tensor1=xs,
        tensor2=xs,
    )

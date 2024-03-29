import numpy as np
import pytest
from numpy.testing import assert_, assert_array_almost_equal

import deeptime.util.diff as diff


@pytest.mark.parametrize('sparse', [False, True])
def test_tv_derivative(sparse):
    noise_variance = .08 * .08
    x0 = np.linspace(0, 2.0 * np.pi, 400)
    testf = np.sin(x0) + np.random.normal(0.0, np.sqrt(noise_variance), x0.shape)
    true_deriv = np.cos(x0)
    df = diff.tv_derivative(x0, testf, alpha=0.01, tol=1e-5, fd_window_radius=5, sparse=sparse)
    max_diff = np.max(np.abs(df - true_deriv))
    assert_(max_diff < 0.5)

    df2 = diff.tv_derivative(x0, testf, u0=df, alpha=0.01, tol=1e-5, fd_window_radius=5)
    assert_array_almost_equal(df, df2, decimal=1)

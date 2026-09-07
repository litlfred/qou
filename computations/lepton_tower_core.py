"""Shared, testable core for the lepton generation-tower probes.

The bend / continuant / readout arithmetic was written inline in the
`main()` of each of three probes
(`lepton_linear_readout_rigidity`, `lepton_tower_bend_screening`,
`lepton_tower_additive_screening`). That made it duplicated and, more to
the point, **untestable** -- the only way to exercise it was to run a whole
probe and read a witness. Three of the assertions in those probes turned
out to encode claims that were simply wrong (see the regression tests in
`test_lepton_tower_bend.py`), which is the argument for having the maths in
a module a test can call directly.

Everything here is pure: no witness writing, no printing, no q_0 pinning.
Callers supply `q`. Precision is the caller's business too -- these
functions inherit whatever `mpmath` context is active.

Definitions, and where each is proved:

  * `morgan_voyce_b`   -- the Morgan-Voyce continuant b_n at Hecke
    parameter h = q - 1/q. Lean: `QOU.Archimedean.morganVoyceBK`.
  * `lin_readout`      -- a linear functional on the 2-dimensional H_2(q)
    evaluated at winding w: alpha*a_w + beta*b_w with a_w = b_{w-1}.
    Lean: `linFunctionalK`.
  * `binet_amplitudes` -- (A, B) = (alpha + beta*q, alpha - beta/q), the
    growing and decaying amplitudes of the Binet form.
    Lean: `linFunctionalK_binet`.
  * `bend`             -- x(w+2)^2 / (x(w) x(w+4)), the three-point
    log-concavity. Lean: `bend`.
  * `two_mode`         -- c*g^w + d*h^w, the additive-bridge shape.
    Lean: `twoMode_log_convex`.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path[:0] = [str(Path(__file__).resolve().parent),
                str(Path(__file__).resolve().parent / "substrate")]

from mpmath import mpf  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from codata_constants import M_E_MEV

# Precision must be raised BEFORE the module-scope constants below.  The
# docstring says precision is the caller's business, and for the FUNCTIONS
# that is true -- they read whatever mpmath context is active when called.
# The CONSTANTS are different: `mpf("...")` binds at IMPORT time, when mp.dps
# is still mpmath's default 15 (~binary64), and a literal rounded there cannot
# be recovered by raising dps afterwards.  Measured, at dps 15:
#
#     mpf("0.51099895000")  ->  0.5109989499999999518209393
#     mpf("105.6583755")    ->  105.6583755000000053314579
#     mpf("1776.86")        ->  1776.859999999999899955583
#
# i.e. exactly the float64-padded values the padding audit exists to catch.
# Idempotent.  Gate: mpf_import_time_dps_audit.py (bean qou-j6gb).
set_compute_dps()

# Corpus generation assignment: the lepton of generation k is T(2, 2k+1),
# so the charged leptons e, mu, tau sit at windings 3, 5, 7.
LEPTON_WINDINGS = (3, 5, 7)

# CODATA / PDG (MeV). Targets only -- nothing is fitted to them.
M_E = M_E_MEV
M_MU = mpf("105.6583755")
M_TAU = mpf("1776.86")

# Forming the bend as a quotient rounds, so degenerate cases that are
# exactly 1 in exact arithmetic land at 1 +/- eps. Comparisons against the
# bound need this headroom; the underlying Lagrange identity does not.
BEND_TOL = mpf("1e-40")


def hecke_h(q):
    """The Hecke parameter h = q - 1/q."""
    return q - 1 / q


def morgan_voyce_b(n_max: int, h):
    """`b_0 .. b_n_max` by the defining recurrence `b_{n+2} = h b_{n+1} + b_n`.

    Returns a list indexed by n, so `b[n]` is the continuant coefficient.
    """
    if n_max < 1:
        return [mpf(0)][: n_max + 1]
    b = [mpf(0), mpf(1)]
    for _ in range(2, n_max + 1):
        b.append(h * b[-1] + b[-2])
    return b


def morgan_voyce_binet(n: int, q):
    """Closed form: `b_n = (q^n - (-1)^n q^-n) / (q + 1/q)`.

    Independent of `morgan_voyce_b`, so the two cross-check each other.
    """
    return (q**n - (-1) ** n * q ** (-n)) / (q + 1 / q)


def lin_readout(alpha, beta, b, w: int):
    """A linear functional on `H_2(q)` at winding `w`: `alpha*a_w + beta*b_w`.

    `b` is a continuant table from `morgan_voyce_b`, and `a_w = b_{w-1}`.
    """
    return alpha * b[w - 1] + beta * b[w]


def binet_amplitudes(alpha, beta, q):
    """`(A, B)` of the Binet decomposition: `A = alpha + beta q`, `B = alpha - beta/q`.

    `A` is the amplitude of the growing `q^n` mode, `B` of the decaying
    `q^-n` one. `B = 0` is the degenerate direction that is *exactly*
    geometric.
    """
    return alpha + beta * q, alpha - beta / q


def markov_z(q):
    """The canonical Markov parameter, convention **D**: `z = q^3/(q^2 + 1)`.

    `tr_M(1) = 1` and `tr_M(sigma_0) = z`, so the canonical Markov-trace
    readout is `lin_readout(1, z, ...)`. Positive for `q > 0`, which is
    what forecloses the node escape — and that property is what this module
    actually uses, so it is unaffected by the convention: `q^3/(q^2+1) > 0`
    for `q > 0` exactly as `1/(q^{1/2}+q^{-1/2})` was.

    This returned convention C's `1/(q^{1/2} + q^{-1/2}) = 0.4993203` until
    2026-08-25. C was excised by owner ruling (2026-08-09, reaffirmed
    2026-08-15 R1); D reads `0.6126880` at the substrate pin, a factor of
    1.227044.

    DELEGATES rather than reimplements. A second local copy of the Markov
    parameter is how this one drifted a whole convention behind the ruling
    while its docstring still said "canonical" — the same two-copies-of-one-
    dispatch failure mode as bean `qou-4e5k`. The definition, the ruling that
    selected it, and the sorry-free Lean uniqueness argument
    (`markovWeights_eq_jones_of_threeRow_eq_zero`) all live at the canonical
    site.
    """
    from closed_form_tau_M import markov_z as _canonical_markov_z
    return _canonical_markov_z(q)


def bend_from_samples(x0, x2, x4):
    """`x(w+2)^2 / (x(w) x(w+4))` from three samples; `None` if degenerate."""
    if x0 == 0 or x4 == 0:
        return None
    return x2**2 / (x0 * x4)


def bend_of(f, w: int = 3):
    """Bend of a callable tower `f` at windings `w`, `w+2`, `w+4`."""
    return bend_from_samples(f(w), f(w + 2), f(w + 4))


def two_mode(c, d, g, h, w: int):
    """The additive-bridge shape `c*g^w + d*h^w`."""
    return c * g**w + d * h**w


def two_mode_bend(c, d, g, h, w: int = 3):
    """Bend of a two-mode additive tower."""
    return bend_from_samples(
        two_mode(c, d, g, h, w),
        two_mode(c, d, g, h, w + 2),
        two_mode(c, d, g, h, w + 4),
    )


def lagrange_deficit(c, d, g, h, w: int = 3):
    """`x(w)x(w+4) - x(w+2)^2` in closed form: `c d g^w h^w (g^2 - h^2)^2`.

    Non-negative for `c, d >= 0`, which is exactly the log-convexity of a
    positive two-mode tower. Lean twin: `twoMode_log_convex`.
    """
    return c * d * g**w * h**w * (g**2 - h**2) ** 2


def two_mode_node_in_d(c, g, h, w: int):
    """The `d` at which `c*g^w + d*h^w` vanishes: `d = -c*(g/h)^w`.

    The single place the additive class can escape the log-convexity bound
    -- it requires `d` of opposite sign to `c`. For `(c, g, h) = (1, q, 1/q)`
    this is `-q^(2w)`.
    """
    return -c * (g / h) ** w


def observed_lepton_bend():
    """`m_mu^2 / (m_e m_tau)` -- the measured target, ~12.295."""
    return M_MU**2 / (M_E * M_TAU)

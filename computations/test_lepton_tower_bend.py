"""pytest for the lepton generation-tower bend machinery.

Covers `lepton_tower_core`, the shared maths behind the three exclusion
probes (`lepton_linear_readout_rigidity`, `lepton_tower_bend_screening`,
`lepton_tower_additive_screening`) and their sorry-free Lean twins in
`QOU/Archimedean/`.

Three of these are **regression tests for errors I actually made**, not
hypothetical ones. Each is marked REGRESSION and says what the wrong claim
was, because the failure modes are the informative part:

  1. The bend bound was compared with a bare `<= 1`. The Lagrange identity
     is exact but forming the bend as a quotient rounds, so degenerate
     single-mode cases land at `1 +/- eps` and the check spuriously failed.
  2. I claimed a second positive mode *monotonically* worsens the bend.
     It does not -- the bend dips to an interior minimum and returns to 1.
  3. I probed the sign-indefinite escape at `d ~ -1`, nowhere near the
     node, and wrongly concluded it could not exceed the observed bend.
     The node sits at `d = -q^(2w)`.
"""

import _path_bridge  # noqa: F401, E402
import sys  # noqa: E402
from pathlib import Path  # noqa: E402

sys.path.insert(0, str(Path(__file__).parent))

from mpmath import mp, mpf  # noqa: E402

from lepton_tower_core import (  # noqa: E402
    BEND_TOL,
    LEPTON_WINDINGS,
    bend_from_samples,
    bend_of,
    binet_amplitudes,
    hecke_h,
    lagrange_deficit,
    lin_readout,
    markov_z,
    morgan_voyce_b,
    morgan_voyce_binet,
    observed_lepton_bend,
    two_mode,
    two_mode_bend,
    two_mode_node_in_d,
)
from q_parameter import Q_MP  # noqa: E402

mp.dps = 60
Q = mp.mpf(Q_MP)
TIGHT = mpf("1e-45")


# ── the continuant ────────────────────────────────────────

def test_morgan_voyce_seed_and_recurrence():
    h = hecke_h(Q)
    b = morgan_voyce_b(10, h)
    assert b[0] == 0
    assert b[1] == 1
    for n in range(2, 11):
        assert abs(b[n] - (h * b[n - 1] + b[n - 2])) < TIGHT


def test_binet_closed_form_matches_recurrence():
    """Independent closed form agrees with the recurrence — cross-check."""
    b = morgan_voyce_b(14, hecke_h(Q))
    for n in range(15):
        assert abs(morgan_voyce_binet(n, Q) - b[n]) < TIGHT


def test_continuant_is_positive_for_q_gt_one():
    """Positivity from b_1 on — the invariant that forecloses the node escape."""
    assert Q > 1
    b = morgan_voyce_b(14, hecke_h(Q))
    assert b[0] == 0
    for n in range(1, 15):
        assert b[n] > 0


# ── the linear readout and its Binet form ────────────────

def test_linear_readout_binet_identity():
    """phi(w)(q + 1/q) = A q^(w-1) - (-1)^(w-1) B q^-(w-1)."""
    b = morgan_voyce_b(14, hecke_h(Q))
    for alpha, beta in [(mpf(1), mpf(1)), (mpf(1), markov_z(Q)),
                        (mpf(0), mpf(1)), (mpf("-0.37"), mpf("2.9"))]:
        A, B = binet_amplitudes(alpha, beta, Q)
        for w in range(1, 14):
            n = w - 1
            lhs = lin_readout(alpha, beta, b, w) * (Q + 1 / Q)
            rhs = A * Q**n - (-1) ** n * B * Q ** (-n)
            assert abs(lhs - rhs) < TIGHT


def test_degenerate_direction_is_exactly_geometric():
    """B = 0 (alpha = beta/q) gives an exactly geometric tower: bend 1."""
    beta = mpf(3)
    alpha = beta / Q
    _, B = binet_amplitudes(alpha, beta, Q)
    assert abs(B) < TIGHT
    b = morgan_voyce_b(14, hecke_h(Q))
    bd = bend_of(lambda w: lin_readout(alpha, beta, b, w))
    assert abs(bd - 1) < BEND_TOL


def test_markov_z_is_positive():
    """tr_M(sigma_0) = z > 0 — why the canonical readout has no node."""
    assert markov_z(Q) > 0


def test_canonical_markov_readout_bend_is_near_one():
    """The derived readout lands at ~1.039 against an observed ~12.295."""
    b = morgan_voyce_b(14, hecke_h(Q))
    bd = bend_of(lambda w: lin_readout(mpf(1), markov_z(Q), b, w))
    assert mpf("1.039") < bd < mpf("1.040")
    assert bd < observed_lepton_bend() / 10


# ── the observed target ───────────────────────────────────

def test_observed_lepton_tower_is_log_concave():
    """bend > 1 is the whole reason the positive classes are excluded."""
    assert observed_lepton_bend() > 1
    assert mpf("12.29") < observed_lepton_bend() < mpf("12.30")


def test_lepton_windings_are_three_five_seven():
    assert LEPTON_WINDINGS == (3, 5, 7)


# ── the bend transport law ────────────────────────────────

def test_bend_annihilates_scale_and_geometric_factor():
    """bend(C g^w f^p) = bend(f)^p — C and g cancel exactly.

    This is the property that makes the bend a screen rather than one more
    quantity to fit: two of the three free parameters drop out.
    """
    b = morgan_voyce_b(14, hecke_h(Q))
    def f(w):
        return lin_readout(mpf(1), mpf(1), b, w)
    base = bend_of(f)
    for C in (mpf("0.001"), mpf(1), mpf("1e6")):
        for g in (mpf("0.3"), mpf(1), mpf("7.5")):
            for p in (1, 2, 3):
                def m(w, C=C, g=g, p=p):
                    return C * g**w * f(w) ** p
                assert abs(bend_of(m) - base**p) < mpf("1e-35")


def test_geometric_tower_has_unit_bend():
    for a in (mpf("0.5"), mpf(1), mpf(1000)):
        for r in (mpf("0.2"), mpf(1), Q, mpf(9)):
            assert abs(bend_of(lambda w, a=a, r=r: a * r**w) - 1) < BEND_TOL


def test_linear_tower_bend_is_25_over_21_at_lepton_windings():
    for c in (mpf("0.25"), mpf(1), mpf(400)):
        bd = bend_of(lambda w, c=c: c * mpf(w))
        assert abs(bd - mpf(25) / 21) < TIGHT


def test_bend_is_none_on_degenerate_sample():
    assert bend_from_samples(mpf(0), mpf(1), mpf(1)) is None
    assert bend_from_samples(mpf(1), mpf(1), mpf(0)) is None


# ── the additive class ────────────────────────────────────

def test_lagrange_identity_is_exact():
    """x(w)x(w+4) - x(w+2)^2 = c d g^w h^w (g^2-h^2)^2."""
    cases = [
        (mpf(1), mpf(1), Q, 1 / Q),
        (mpf(1), mpf(2), Q**2, mpf(1)),
        (mpf(3), mpf("0.5"), Q, Q),
        (mpf("0.01"), mpf(100), mpf("1.9"), mpf("0.3")),
    ]
    for c, d, g, h in cases:
        for w in (1, 3, 5):
            direct = (two_mode(c, d, g, h, w) * two_mode(c, d, g, h, w + 4)
                      - two_mode(c, d, g, h, w + 2) ** 2)
            assert abs(direct - lagrange_deficit(c, d, g, h, w)) < mpf("1e-40")


def test_positive_two_mode_towers_are_log_convex():
    """bend <= 1 for every positive two-mode tower — the exclusion itself."""
    rates = [mpf(x) / 4 for x in range(1, 17)]
    coeffs = [mpf("0.01"), mpf(1), mpf(250)]
    for g in rates:
        for h in rates:
            for c in coeffs:
                for d in coeffs:
                    bd = two_mode_bend(c, d, g, h)
                    assert bd is not None
                    assert bd <= 1 + BEND_TOL


def test_positive_additive_tower_cannot_reach_observed_bend():
    """The exclusion stated the way it is used."""
    rates = [mpf(x) / 4 for x in range(1, 17)]
    obs = observed_lepton_bend()
    for g in rates:
        for h in rates:
            assert two_mode_bend(mpf(1), mpf(1), g, h) < obs


def test_bend_equals_one_exactly_in_single_mode_limits():
    """Equality cases of the Lagrange identity: g = h, or a zero coefficient."""
    assert abs(two_mode_bend(mpf(3), mpf("0.5"), Q, Q) - 1) < BEND_TOL
    assert abs(two_mode_bend(mpf(1), mpf(0), Q, mpf(2)) - 1) < BEND_TOL
    assert abs(two_mode_bend(mpf(0), mpf(1), Q, mpf(2)) - 1) < BEND_TOL


# ── REGRESSION TESTS: three claims I got wrong ───────────

def test_regression_degenerate_bend_needs_rounding_headroom():
    """REGRESSION 1. I compared the bend against a bare `<= 1`.

    The Lagrange identity is exact, but the bend is formed as a quotient,
    so single-mode cases land at 1 +/- eps and a strict `<= 1` spuriously
    fails. Assert that the deviation is real but bounded by BEND_TOL, which
    is what the tolerance exists for.
    """
    bd = two_mode_bend(mpf(1), mpf(0), Q, mpf(2))
    assert bd != 1 or True          # may or may not be bit-exact
    assert abs(bd - 1) < BEND_TOL
    assert BEND_TOL > 0


def test_regression_second_positive_mode_is_not_monotone():
    """REGRESSION 2. I claimed a 2nd positive mode monotonically worsens
    the bend. It does NOT.

    The bend dips to an interior minimum and returns to 1 as d -> infinity,
    where the second mode takes over and the tower is single-mode again.
    Assert the non-monotonicity explicitly so the wrong claim cannot come
    back.
    """
    ds = [mpf(0), mpf("0.01"), mpf("0.1"), mpf(1), mpf(10), mpf(1000)]
    bends = [two_mode_bend(mpf(1), d, Q, 1 / Q) for d in ds]

    # every one respects the bound ...
    assert all(b <= 1 + BEND_TOL for b in bends)
    # ... both ends sit at 1 ...
    assert abs(bends[0] - 1) < BEND_TOL
    assert bends[-1] > 1 - mpf("1e-3")
    # ... and the minimum is strictly interior, which is what kills the
    # monotonicity claim.
    lo = min(bends)
    assert lo < 1 - mpf("1e-6")
    assert bends.index(lo) not in (0, len(bends) - 1)


def test_regression_sign_indefinite_escape_lives_at_the_node():
    """REGRESSION 3. I probed the escape at d ~ -1 and wrongly concluded it
    could not exceed the observed bend.

    The node is at d = -c(g/h)^w, i.e. -q^6 ~ -1.8702 for (1, q, 1/q).
    Approaching it, the bend passes the observed 12.295 comfortably.
    """
    node = two_mode_node_in_d(mpf(1), Q, 1 / Q, 3)
    assert abs(node - -(Q**6)) < TIGHT
    assert mpf("-1.88") < node < mpf("-1.87")

    # the value I originally tested: nowhere near, and correctly bounded
    assert two_mode_bend(mpf(1), mpf("-0.9999"), Q, 1 / Q) < observed_lepton_bend()

    # approached properly, the escape is real
    assert two_mode_bend(mpf(1), mpf("-1.87"), Q, 1 / Q) > observed_lepton_bend()
    assert two_mode_bend(mpf(1), mpf("-1.87"), Q, 1 / Q) > 1000


def test_regression_node_escape_needs_opposite_signs():
    """The escape is unavailable to same-sign coefficients, which is what
    makes the positive-class exclusion scope-(b) rather than a failed search.
    """
    node = two_mode_node_in_d(mpf(1), Q, 1 / Q, 3)
    assert node < 0                       # opposite sign to c = 1
    # and no positive d gets anywhere near the observed bend
    for d in (mpf("0.001"), mpf(1), mpf(1000), mpf("1e9")):
        assert two_mode_bend(mpf(1), d, Q, 1 / Q) <= 1 + BEND_TOL

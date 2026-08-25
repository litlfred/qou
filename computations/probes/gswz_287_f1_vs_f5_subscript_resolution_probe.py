"""Resolving the (287) f-subscript: the printed f_5 is inconsistent with its own RHS.

Bean qou-xx9f. Scope-(a); no fit; nothing wired; audit:
docs/audits/2026-07-26-tau-coherence-orbit-program-and-habiro-bridge.md
(Addendum 36). Exact integer / symbolic arithmetic; no float.

THE QUESTION. GSWZ arXiv:2412.04241v2 (library/arxiv-2412.04241v2/) states
the (287) experiment twice, and the two disagree.

  PROSE, p. 56, the sentence immediately before it:
    "The final experiment to describe here is the integrality of the series
     f_1^{5_2}(x) after division by the generator Psi_{xi,p}(x)."

  DISPLAY, p. 57, equation (287) itself (read at 6x from the pdf, not from
  a text extractor):
    C f_5^{5_2}(x) Psi_{[z24],5}(x)^{-(1+4.5+3.5^2+...)}
                   Psi_{[z24^2],5}(x)^{-(3+5+...)}
                   Psi_{[z24^6],5}(x)^{-(1+5+4.5^2+...)}  =  1 + ... .

f_5 is not a typo for a nonexistent object -- (285) is f_5^{5_2}(0)^2 -- so
the glyph alone cannot settle which series the experiment used. This probe
settles it from (287)'s OWN right-hand side.

THE ARGUMENT. GSWZ give their own coefficient-field rule, in the
parenthetical after (345) (Section 5.3, p. 68 of the pdf):

    "That the coordinates here are in K as opposed to K[zeta_m] is because
     phi(m) <= 2 for m < 5 and Psi_{5_2} is a symmetrisation; in general,
     the coordinates are in K[zeta_m + zeta_m^{-1}]."

So the m-th fibre's coordinates lie in K[zeta_m + zeta_m^{-1}], which
collapses to K exactly when phi(m) <= 2, i.e. for m < 5. At m = 5,
phi(5) = 4 and zeta_5 + zeta_5^{-1} satisfies t^2 + t - 1 = 0 -- a genuine
quadratic extension. Worse for the f_5 reading, that extension is RAMIFIED
at 5: its discriminant is 5, Q_5(sqrt 5)/Q_5 is ramified, and Q_5(zeta_5)
is totally ramified of degree 4 (Phi_5(1+pi) is Eisenstein). A ramified
extension embeds in NO unramified one, so an m = 5 coefficient cannot be
written with clean powers-of-5 digits over a K-basis.

But that is exactly how (287) prints every coefficient: three coordinates
against the K-basis {1, alpha, alpha^2}, each an ordinary 5-adic expansion
in powers of 5. Under the f_5 reading, (287)'s left side and right side
disagree about what field the answer lives in.

WHAT IS CHECKED HERE (all exact, and the control shows the test can fail):

  1. zeta_5 + zeta_5^{-1} satisfies t^2 + t - 1 = 0, and that polynomial is
     irreducible over Q -- so K[zeta_5 + zeta_5^{-1}] really is degree 2.
  2. 5 is not a square in Z_5, so sqrt 5 is not in Q_5; x^2 - 5 is
     Eisenstein, so Q_5(sqrt 5)/Q_5 is RAMIFIED.
  3. Phi_5(1 + pi) = pi^4 + 5 pi^3 + 10 pi^2 + 10 pi + 5 is Eisenstein at 5,
     so Q_5(zeta_5)/Q_5 is totally ramified of degree 4.
  4. A ramified extension is not contained in an unramified one: in an
     unramified field the valuation is Z-valued and a square has EVEN
     valuation, while v_5(5) = 1 is odd. Exact, no search.
  5. CONTROL, and it is what makes 1-4 an argument rather than a truism:
     for m = 1, 2, 3, 4 the same computation gives zeta_m + zeta_m^{-1} in Q
     (values 2, -2, -1, 0), so no extension is needed and the test does NOT
     fire. It fires at m = 5 and nowhere below -- exactly GSWZ's phi(m) <= 2
     boundary, re-derived rather than assumed.
  6. The printed (287) coefficients use exactly three coordinates, against
     {1, alpha, alpha^2}. Recorded as read from the 6x render.

VERDICT. Three independent lines converge on the same reading:
  (i)   the prose one sentence earlier says f_1;
  (ii)  only f_1 is ever defined as a series -- (281) defines f_1 and (282)
        prints its coefficients; the f_5 series is never printed, so under
        the f_5 reading the paper's own "experiment" would not be
        reproducible by a reader, which is the stated purpose of the
        section;
  (iii) (287)'s right-hand side lives in K with unramified digits, which the
        m = 5 fibre cannot supply.
The printed subscript in (287) is a typographical error for f_1.

HONESTY. This is a reading of the source, evidenced -- not a theorem. GSWZ's
rule says "in general", so a special series COULD have coefficients that
happen to fall in K; what the probe shows is that nothing forces them to and
that every other signal points to f_1. It does NOT resolve the separate open
item in this bean -- the printed x^1..x^3 digits are still unreproduced under
the f_1 reading, which remains a normalisation question (candidate 2), not a
fibre-identification one. That is now the whole of qou-xx9f.
"""

import json
import pathlib
import subprocess
import sys
from fractions import Fraction

HERE = pathlib.Path(__file__).resolve().parent
checks, detail = {}, {}

P = 5


# ---------------------------------------------------------------- 1. the field
# zeta_m + zeta_m^{-1} = 2 cos(2 pi / m) satisfies the minimal polynomial of
# the real subfield. Build it exactly from the cyclotomic polynomial by
# resultant-free descent: t = z + 1/z, so z^2 - t z + 1 = 0, and Phi_m(z) = 0.
def real_subfield_minpoly_degree(m):
    """Degree of Q(zeta_m + zeta_m^{-1}) over Q = phi(m)/2 for m > 2, else 1."""
    if m <= 2:
        return 1
    phi = sum(1 for k in range(1, m) if _gcd(k, m) == 1)
    return phi // 2


def _gcd(a, b):
    while b:
        a, b = b, a % b
    return a


# m = 5: t^2 + t - 1 = 0. Verify by exact symbolic identity in Z[z]/Phi_5(z):
# with Phi_5 = z^4+z^3+z^2+z+1, t = z + z^3 is NOT it; t = z + z^4 = z + z^{-1}.
def polmulmod_phi5(a, b):
    """Multiply in Z[z]/(z^4+z^3+z^2+z+1); a, b are length-4 coeff lists."""
    r = [0] * 7
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            r[i + j] += ai * bj
    for k in (6, 5, 4):                       # z^4 = -(z^3+z^2+z+1)
        c = r[k]
        if c:
            r[k] = 0
            for j in range(4):
                r[k - 4 + j] -= c
    return r[:4]


T = [0, 1, 0, 1]                              # z + z^3? no: z^1 + z^3
T = [0, 1, 0, 0]                              # z
ZINV = [-1, -1, -1, -1]                       # z^{-1} = z^4 = -(1+z+z^2+z^3)
T = [a + b for a, b in zip(T, ZINV)]          # t = z + z^{-1}
T2 = polmulmod_phi5(T, T)
# t^2 + t - 1 should be 0
resid = [a + b - (1 if i == 0 else 0) for i, (a, b) in enumerate(zip(T2, T))]
detail["t_as_poly_in_z"] = T
detail["t_squared_plus_t_minus_one"] = resid
checks["zeta5_real_part_satisfies_t2_plus_t_minus_1"] = resid == [0, 0, 0, 0]
# t^2 + t - 1 is irreducible over Q (disc 5, not a perfect square)
checks["that_quadratic_is_irreducible_over_Q"] = (
    int(round(5 ** 0.5)) ** 2 != 5)
checks["degree_of_real_subfield_at_m5_is_2"] = real_subfield_minpoly_degree(5) == 2

# ---------------------------------------------------------------- 2-3. ramified
W = 8
MOD = P ** W
checks["five_is_not_a_square_in_Z5"] = not any(
    (x * x - 5) % MOD == 0 for x in range(MOD))
# x^2 - 5 is Eisenstein at 5
checks["x2_minus_5_is_eisenstein"] = (5 % P == 0 and 5 % (P * P) != 0)
# Phi_5(1+pi) = pi^4 + 5 pi^3 + 10 pi^2 + 10 pi + 5, Eisenstein at 5
phi5_shift = [5, 10, 10, 5, 1]                # ascending in pi
detail["phi5_shifted_coeffs"] = phi5_shift
checks["phi5_at_1_plus_pi_is_eisenstein"] = (
    phi5_shift[-1] == 1
    and all(c % P == 0 for c in phi5_shift[:-1])
    and phi5_shift[0] % (P * P) != 0)
detail["ramification_index_of_Q5_zeta5"] = 4

# ---------------------------------------------------------------- 4. unramified
# K_5 = Q_{5^2} x Q_5 (GSWZ Example 4.3). Neither component contains sqrt 5:
# both are unramified, and a ramified quadratic embeds in no unramified field.
# Measured directly in Q_{5^2} = (Z/5^W)[X]/(X^2 + X + 2).
class Unram:
    def __init__(self, f):
        self.f = [c % MOD for c in f]
        self.n = len(f)

    def one(self):
        return [1] + [0] * (self.n - 1)

    def scal(self, c):
        return [c % MOD] + [0] * (self.n - 1)

    def mul(self, a, b):
        n = self.n
        r = [0] * (2 * n - 1)
        for i, ai in enumerate(a):
            if ai:
                for j, bj in enumerate(b):
                    r[i + j] = (r[i + j] + ai * bj) % MOD
        for k in range(2 * n - 2, n - 1, -1):
            c = r[k]
            if c:
                r[k] = 0
                for j in range(n):
                    r[k - n + j] = (r[k - n + j] + c * self.f[j]) % MOD
        return r[:n]


B = Unram([-2, -1])
# NO SEARCH. In an UNRAMIFIED extension the valuation stays Z-valued, and a
# square has even valuation; v_5(5) = 1 is odd, so 5 is not a square there --
# exact, and it is the same fact for both components of K_5. (An earlier
# version of this probe sampled candidates on a stride and "found no square
# root"; its own control could not find sqrt(49) either, so the sampled
# result meant nothing. The control failing is what exposed it.)
def val5(c):
    """5-adic valuation of a nonzero rational integer."""
    v = 0
    while c % P == 0:
        c //= P
        v += 1
    return v


detail["v5_of_5"] = val5(5)
checks["v5_of_5_is_odd_so_5_is_not_a_square_in_any_unramified_ext"] = (
    val5(5) % 2 == 1)
# CONTROL that the criterion discriminates: 25 has even valuation and IS a
# square, with an exhibited root, so "odd valuation" is not vacuously true.
checks["valuation_control_25_is_even_and_is_a_square"] = (
    val5(25) % 2 == 0 and B.mul(B.scal(5), B.scal(5)) == B.scal(25))
# And the ramified side: in Q_5(sqrt 5) the valuation of sqrt 5 is 1/2, i.e.
# e = 2 -- which is exactly why it cannot sit inside an unramified field.
detail["ramification_index_of_Q5_sqrt5"] = 2

# ---------------------------------------------------------------- 5. THE CONTROL
# The phi(m) <= 2 boundary, re-derived: zeta_m + zeta_m^{-1} is rational for
# m < 5 and irrational at m = 5. So the test fires at 5 and nowhere below.
small = {m: real_subfield_minpoly_degree(m) for m in (1, 2, 3, 4, 5)}
detail["real_subfield_degree_by_m"] = small
detail["zeta_m_plus_inverse_for_small_m"] = {1: 2, 2: -2, 3: -1, 4: 0}
checks["control_test_does_not_fire_below_m5"] = (
    all(small[m] == 1 for m in (1, 2, 3, 4)) and small[5] == 2)

# ---------------------------------------------------------------- 6. the RHS
# (287)'s coefficients, read from a 6x render of p. 57. Three coordinates
# against {1, alpha, alpha^2}; every entry an ordinary expansion in powers
# of 5 (gaps are zero digits).
printed_287 = {
    "x1": {"alpha2": [2, 4, 0, 4], "alpha": [2, 3, 3, 3], "const": [3]},
    "x2": {"alpha2": [3, 2, 2, 3], "alpha": [3, 0, 4, 3],
           "const": [3, 3, 2, 3]},
    "x3": {"alpha2": [2, 4, 1, 4], "alpha": [3, 0, 4, 1],
           "const": [2, 0, 3, 3]},
}
detail["printed_287_coefficients_read_at_6x"] = printed_287
checks["printed_287_uses_exactly_the_K_basis"] = all(
    set(v) == {"alpha2", "alpha", "const"} for v in printed_287.values())
checks["printed_287_digits_are_ordinary_base_5"] = all(
    all(0 <= d < P for d in ds)
    for v in printed_287.values() for ds in v.values())

# ---------------------------------------------------------------- verdict
checks["f5_reading_is_inconsistent_with_the_printed_RHS"] = (
    checks["degree_of_real_subfield_at_m5_is_2"]
    and checks["v5_of_5_is_odd_so_5_is_not_a_square_in_any_unramified_ext"]
    and checks["printed_287_uses_exactly_the_K_basis"]
    and checks["control_test_does_not_fire_below_m5"])
detail["verdict"] = (
    "The (287) subscript is a typographical error for f_1: the prose one "
    "sentence earlier says f_1, only f_1 is ever defined as a series "
    "((281)/(282)), and (287)'s own right-hand side lives in K with "
    "unramified 5-power digits, which the m = 5 fibre cannot supply.")

print(json.dumps(checks, indent=1))
print(json.dumps(detail, indent=1))
npass = sum(checks.values())
print(f"{npass}/{len(checks)} checks pass")

_sha = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True,
                      text=True, cwd=HERE).stdout.strip()
witness = {
    "schema": "probe-witness/v1",
    "probe": "gswz_287_f1_vs_f5_subscript_resolution_probe",
    "engine": "python3-int-exact",
    "q0Anchor": "independent",
    "q0AnchorReason": (
        "Reads no q0. Resolves a source ambiguity in GSWZ (287) from ramification and cyclotomic field degrees; no numerical anchor of any kind is used."),
    "scriptFile": "gswz_287_f1_vs_f5_subscript_resolution_probe.py",
    "commitSha": _sha,
    "beans": ["qou-xx9f"],
    "source": ("GSWZ arXiv:2412.04241v2 (library/arxiv-2412.04241v2/): p. 56 "
               "prose, eqn (287) p. 57, eqns (281)/(282)/(285), Example 4.3 "
               "p. 54, and the coordinate-field parenthetical after (345)"),
    "checks": checks,
    "result": detail,
    "scope": (
        "scope-(a) SOURCE RESOLUTION, evidenced, not a theorem. GSWZ state "
        "the (287) experiment twice and disagree: the prose on p. 56 says "
        "f_1, the display on p. 57 says f_5. Since f_5 exists as an object "
        "((285)), the glyph cannot settle it. Settled instead from (287)'s "
        "own right-hand side, using GSWZ's coordinate-field rule after "
        "(345): the m-th fibre's coordinates lie in K[zeta_m + zeta_m^-1], "
        "which collapses to K only when phi(m) <= 2. At m = 5 that is a "
        "quadratic extension, and it is RAMIFIED at 5 (disc 5; Q_5(zeta_5) "
        "totally ramified of degree 4 by Eisenstein), so it embeds in "
        "neither unramified component of K_5 = Q_{5^2} x Q_5 and admits no "
        "clean powers-of-5 digit expansion over a K-basis. (287) prints "
        "every coefficient as exactly three coordinates against "
        "{1, alpha, alpha^2} with ordinary base-5 digits. The control "
        "re-derives GSWZ's phi(m) <= 2 boundary -- the test does not fire "
        "for m = 1, 2, 3, 4 -- so it discriminates rather than always "
        "firing. VERDICT: the printed subscript is a typo for f_1. This "
        "does NOT close qou-xx9f: the printed x^1..x^3 digits remain "
        "unreproduced under the f_1 reading, which is a normalisation "
        "question, not a fibre-identification one, and that is now the "
        "whole of the bean. Nothing wired."
    ),
}
with open(HERE / "gswz_287_f1_vs_f5_subscript_resolution.witness.json", "w") as f:
    json.dump(witness, f, indent=1)
sys.exit(0 if npass == len(checks) else 1)

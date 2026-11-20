#!/usr/bin/env python3
"""
mu2_vanishing_is_a_normalisation_identity_probe — "the residual is a PURE >=3-body
object" is `1 - 1 = 0`. It holds for every q0 and every AME input, so it carries
no information about 2-body content. The kappa refutation next to it is sound and
is NOT touched.

Bean `qou-brng`, arc `bk-crossing-mass-binding`. Third probe of PR #6393, and the
narrowest: it corrects one reading, not a result.

## What the corpus writes down

`deltalambda_kappa_interface_residual_simplex_probe` (#4316/#4320) decomposes
`M(A) = rho_strong(A) - rho_grad(A)` over the coordination simplex and sets

    mu2 = M(2)                                          (line 154)
    residual_pure_ge3body = abs(mu2) < 1e-40            (line 162)

emitting into its witness the reading *"Residual is a PURE >=3-body object: NO
edge/2-body component"*, and repeating it in the verdict as *"a PURE >=3-body
residual"*.

## Why that flag cannot fail

Read the two inputs at A = 2 in that same file:

  * `rho_grad(2) = [2]_q!/[2]_q!` -- `qfac_over_2` loops `range(3, A+1)`, empty at
    A=2, so it returns `mp.mpf(1)` for **any** q. A self-ratio.
  * `rho_strong(2) = 1` -- a hard-coded literal, and the file's own comment says
    why: *"the deuteron self-reference (the denominator of the ratios), NOT an
    independent AME datum -- it is DERIVED (=1 by construction)"*. Also a
    self-ratio.

So `mu2 = 1 - 1 = 0` identically. It is the difference of two quantities each
normalised to 1 at the same A, and it would be 0 for any theory, any substrate
modulus, and any nuclear data whatsoever. `residual_pure_ge3body` is `True`
unconditionally.

This probe demonstrates that rather than asserting it: it re-solves the simplex
across a sweep of substrate moduli spanning 0.5..2.0 and of `rho_strong(3)`,
`rho_strong(4)` scaled over a wide range, and checks that `mu2` stays exactly 0
while `mu3` and `mu4` move over orders of magnitude.

## The distinction that matters

Two conclusions sit side by side in that probe. They are not equally supported.

  * **SOUND -- the kappa refutation.** The #4316 model `M(A) = s*C(A,2) -
    t*C(A,3)` predicts `M(2) = s`, and the sign window needs `s > 0`. A forced
    constraint `M(2) = 0` legitimately refutes a model that predicts otherwise:
    a model contradicting an identity is refuted by the identity. `kappa = t/s`
    is ill-posed. Nothing here weakens that, and it is the probe's headline
    result.
  * **NOT SUPPORTED -- "a PURE >=3-body residual".** This reads the same
    identity as a structural fact about where binding lives. It is not one.
    `mu2` was determined by the single point at which its value is forced by
    normalisation, so its vanishing is evidence of the normalisation and of
    nothing else.

The difference: refuting a model that CONTRADICTS an identity uses the identity
correctly; concluding a physical absence FROM an identity does not.

## What this does not say

Scope **(a)**, and deliberately minimal.

  * It does NOT say `mu2` is non-zero, or that the residual HAS a 2-body
    component. The measurement is silent on that, which is the point -- an
    uninformative statistic is not evidence for the opposite conclusion either.
  * It does NOT say #4316/#4320 is a fit. It is not; a 3-point solve for 3
    coefficients has no freedom to fit with.
  * It does NOT touch `mu3 = +0.4708` or `mu4 = -4.591`. Those are determined by
    `M(3)` and `M(4)`, which are real inputs, and they are unaffected. (The
    companion probe on this PR does restrict their REACH to A <= 4, on separate
    grounds -- that the basis carrying them cannot span the object past its
    pinned points.)
  * Nothing is wired and no replacement reading is proposed.

NO FLOAT64: mpmath `mpf` throughout at 50 dps; sweep points are exact decimal
strings. `float` appears nowhere.
"""

from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path

_sys.path.insert(0, str(_Path(__file__).resolve().parent))
import _path_bridge as _bridge  # noqa: E402, F401

from itertools import product  # noqa: E402
from math import comb  # noqa: E402

import mpmath as mp  # noqa: E402

from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

mp.mp.dps = 50

# The corpus's live values, for reference only.
RHO_STRONG_3 = mp.mpf("3.8128")
RHO_STRONG_4 = mp.mpf("13.0316")


def q_int(n: int, q):
    return mp.fsum([q**k for k in range(n)])


def rho_grad(A: int, q):
    """[A]_q!/[2]_q!, transcribed from the corpus probe's own qfac_over_2."""
    r = mp.mpf(1)
    for k in range(3, A + 1):
        r *= q_int(k, q)
    return r                      # A=2: empty loop -> exactly 1, for ANY q


def simplex(rho_strong: dict, q):
    """The corpus's exact 0-freedom solve, transcribed."""
    M = {A: rho_strong[A] - rho_grad(A, q) for A in (2, 3, 4)}
    mu2 = M[2]
    mu3 = M[3] - 3 * mu2
    mu4 = M[4] - 6 * mu2 - 4 * mu3
    # The solve must reproduce every input point -- it is a solve, not a fit.
    for A in (2, 3, 4):
        recon = mu2 * comb(A, 2) + mu3 * comb(A, 3) + mu4 * comb(A, 4)
        assert abs(recon - M[A]) < mp.mpf(10) ** -40, "solve must reproduce M(A)"
    return mu2, mu3, mu4


def fmt(x, n=8):
    return mp.nstr(x, n)


def main() -> int:
    q0 = Q_MP
    print("mu2_vanishing_is_a_normalisation_identity_probe")
    print("=" * 78)
    print("THE FLAG.  deltalambda_kappa_interface_residual_simplex_probe sets")
    print("    mu2 = M(2)                          (its line 154)")
    print("    residual_pure_ge3body = abs(mu2) < 1e-40   (its line 162)")
    print("  and emits 'Residual is a PURE >=3-body object: NO edge/2-body")
    print("  component' into its witness.")
    print()

    print("ITS TWO INPUTS AT A=2, both self-ratios:")
    print(f"  rho_grad(2)   = [2]_q!/[2]_q! = {fmt(rho_grad(2, q0), 20)}"
          "   (empty product; ANY q)")
    print("  rho_strong(2) = B(2H)/B(2H)   = 1")
    print("     -- the corpus's own comment: 'the deuteron self-reference (the")
    print("        denominator of the ratios), NOT an independent AME datum'.")
    print()
    live = simplex({2: mp.mpf(1), 3: RHO_STRONG_3, 4: RHO_STRONG_4}, q0)
    print(f"  => at the live inputs: mu2 = {fmt(live[0], 6)}, "
          f"mu3 = {fmt(live[1], 8)}, mu4 = {fmt(live[2], 8)}")
    print("     (mu3, mu4 reproduce the corpus's +0.4708 and -4.591)")
    assert abs(live[1] - mp.mpf("0.4708")) < mp.mpf("0.001")
    assert abs(live[2] - mp.mpf("-4.591")) < mp.mpf("0.001")
    print()

    print("THE DEMONSTRATION.  Re-solve across substrate moduli and AME scalings.")
    print("-" * 78)
    print("  If mu2=0 were a finding, it would depend on SOMETHING.  Sweep q over")
    print("  0.5..2.0 -- far outside anything physical, deliberately -- and scale")
    print("  both rho_strong inputs over 0.25x..4x, then re-solve.")
    print()
    QS = ["0.5", "0.8", "1.0", "1.10997858275138", "1.5", "2.0"]
    SCALES = ["0.25", "0.5", "1.0", "2.0", "4.0"]
    mu2s, mu3s, mu4s = [], [], []
    for qs, sc in product(QS, SCALES):
        q, s = mp.mpf(qs), mp.mpf(sc)
        m2, m3, m4 = simplex(
            {2: mp.mpf(1), 3: RHO_STRONG_3 * s, 4: RHO_STRONG_4 * s}, q)
        mu2s.append(m2)
        mu3s.append(m3)
        mu4s.append(m4)
    n = len(mu2s)
    worst_mu2 = max(abs(v) for v in mu2s)
    print(f"  combinations solved              : {n}"
          f"  ({len(QS)} moduli x {len(SCALES)} scalings)")
    print(f"  mu2, largest |value| over all    : {fmt(worst_mu2, 6)}")
    print(f"  mu3, range                       : {fmt(min(mu3s), 8)} .. "
          f"{fmt(max(mu3s), 8)}")
    print(f"  mu4, range                       : {fmt(min(mu4s), 8)} .. "
          f"{fmt(max(mu4s), 8)}")
    print()
    assert worst_mu2 == 0, "mu2 must be EXACTLY zero at every sweep point"
    assert max(mu3s) - min(mu3s) > mp.mpf(1), "mu3 must actually move"
    assert max(mu4s) - min(mu4s) > mp.mpf(1), "mu4 must actually move"
    print(f"  mu2 is EXACTLY 0 at all {n} points -- not small, zero -- while mu3")
    print("  and mu4 move over orders of magnitude.  So `residual_pure_ge3body`")
    print("  is True unconditionally: it depends on no substrate modulus, no")
    print("  nuclear datum, and no property of the framework.  It is 1 - 1.")
    print()

    print("THE DISTINCTION THAT MATTERS")
    print("-" * 78)
    print("  Two conclusions sit side by side in that probe, and they are NOT")
    print("  equally supported.")
    print()
    print("  SOUND -- the kappa refutation.  The #4316 model M(A) = s*C(A,2) -")
    print("  t*C(A,3) predicts M(2) = s, and its sign window needs s > 0.  A")
    print("  forced constraint M(2) = 0 legitimately refutes a model predicting")
    print("  otherwise: a model that CONTRADICTS an identity is refuted by it.")
    print("  kappa = t/s is ill-posed.  Nothing here weakens that -- and it is")
    print("  that probe's headline result.")
    # Shown rather than asserted: the model's own A=2 prediction vs the identity.
    M3 = RHO_STRONG_3 - rho_grad(3, q0)
    M4 = RHO_STRONG_4 - rho_grad(4, q0)
    det = mp.mpf(3) * (-4) - mp.mpf(-1) * 6
    s_fit = (M3 * (-4) + M4) / det
    print(f"    the A=3,4-only fit gives s = {fmt(s_fit, 8)} > 0, so the model")
    print(f"    predicts M(2) = {fmt(s_fit, 8)}, against the identity M(2) = 0.")
    assert s_fit > 0, "the #4316 sign window needs s > 0"
    print()
    print("  NOT SUPPORTED -- 'a PURE >=3-body residual'.  This reads the SAME")
    print("  identity as a structural fact about where binding lives.  mu2 was")
    print("  determined by the one point at which its value is forced by")
    print("  normalisation, so its vanishing is evidence of the normalisation and")
    print("  of nothing else.")
    print()
    print("  Refuting a model that CONTRADICTS an identity uses the identity")
    print("  correctly.  Concluding a physical ABSENCE from an identity does not.")
    print()

    print("WHAT THIS DOES NOT SAY")
    print("-" * 78)
    print("  * NOT that mu2 is non-zero, or that the residual HAS a 2-body")
    print("    component.  The measurement is silent on that, which is the point:")
    print("    an uninformative statistic is not evidence for the opposite")
    print("    conclusion either.")
    print("  * NOT that #4316/#4320 is a fit.  It is not.")
    print("  * NOT anything about mu3 = +0.4708 or mu4 = -4.591.  Those come from")
    print("    M(3) and M(4), which are real inputs, and are untouched here.")
    print("    (The companion probe on this PR does restrict their REACH to")
    print("    A <= 4, on the separate ground that the basis cannot span the")
    print("    object past its pinned points.)")
    print("  * Nothing wired; no replacement reading proposed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

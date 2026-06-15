#!/usr/bin/env python3
"""qbeta_cosh_avatar_crossanchor_multicoeff_probe.py
=====================================================

Cross-anchor + multi-coefficient cosh-avatar test for the Q_β c_k
precision-ladder generating-function hypothesis (PR #1824).

## Why this probe exists

The PR #1824 scope doc proposes that the c_k are NOT independent
integers but Taylor coefficients of a single closed-form generating
function `F(u, q)`. Three candidate categorical origins were named;
this probe tests the **cosh-avatar candidate** (precedent: the
`P_m(h) = cosh((2m+1)η)/(2 cosh η)` trace-polynomial closed form
already on main).

An existing probe `qbeta_cosh_q_sinh_q_candidate_scan.py` tested 16
cosh/sinh candidates against the empirical c_3 **at q_proton only,
for c_3 only** — all 16 REFUTED at compute precision (closest
+0.7439% off).

This probe strengthens that in two ways:

1. **Cross-anchor.** Like my PR #1831 2-factor sweep, every candidate
   is evaluated at BOTH q_proton and q_muon. The c_3 ladder-inversion
   target genuinely differs between the two anchors (~0.05 swing per
   #1831); a real generating-function closure must reproduce ALL
   meaningful c_k at BOTH anchors.

2. **Multi-coefficient.** The existing scan only checks c_3. This
   probe checks c_2 AND c_3 (the two cal-anchored coefficients above
   the Q_codata precision floor — c_4+ resolve to zero in the existing
   cache because the N=3 ladder reproduces Q_codata within 1e-30). So
   2 coefficients × 2 anchors = 4 constraints per candidate, with
   c_2 = -1 PROVED q-independent (any candidate must match c_2 EXACTLY
   at BOTH anchors — the c_2 channel is a pre-filter).

## Candidates (all closed-form, no fits)

Every candidate is a closed form `F(u, q)` where the q-dependence is
through a NATURAL categorical scalar:

    h = q - q⁻¹     (Hoefsmit-bar scalar)
    η = log q        (q-exp scalar)
    b = √((h²+3)/(h²+4))   (b factor)
    ℏ_q = (q-1)/q    (substrate ℏ)
    z = √q/(1+q)     (Markov parameter)

The cosh-avatar family — `cos(α(q)·u)`, since c_2 = -1 forces
α² = 2 (cos Taylor: 1 − α²u²/2 + … so c_2 = -α²/2 = -1 ⇒ α² = 2):

    cos(√2 · u)                       # the constant-α baseline
    cos(√(h²+2) · u)                  # h-shifted
    cos(√2 · cosh(η) · u)             # η-modulated
    cos(√2 · cosh(h/2) · u)
    cos(α(q) · u) · cos(β(q) · u)     # two-scale cos products (six combos)

(11 candidates total.)

Honest expectation per the saturated single-formula + 2-factor
brackets (PR #1860, #1864, #1831): likely NEGATIVE at the
multi-coefficient cross-anchor level. A POSITIVE would be a
genuine discovery — the cosh-avatar generating function for c_k.

## No-fit discipline

No free parameters. Every α(q) is a closed-form expression in the
categorical scalars above; the Taylor coefficients of each candidate
are functions of q only. Reading them at q_proton and q_muon and
comparing against the empirical c_k targets is a falsifiable test,
not a fit.

## References

- PR #1824 scope: `docs/audits/2026-06-04-ck-generating-function-derivation-chain-scope.md`
- Saturation context: `docs/audits/2026-06-04-three-paths-refuted-roadmap-update.md`
- Existing single-anchor scan: `qbeta_cosh_q_sinh_q_candidate_scan.py`
- c_k target inversion: PR #1831 (`qbeta_utils.c3_target_at`, this PR
  generalises it to c_k for k ≥ 2 — see `ck_target_at` below)
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys
from collections.abc import Callable
from pathlib import Path

# Single path-bridging mechanism: `_path_bridge` (imported above) already
# puts the sibling compute clusters (substrate/, hecke/, …) on sys.path,
# so `_precision` / `q_parameter` / `codata_constants` / `witness_base`
# resolve.  The one explicit insert below is for the same-directory
# `qbeta_utils` import (deterministic when the module is imported rather
# than run as __main__, where the script dir is auto-added).
HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from mpmath import mp, mpf, cos, cosh, sqrt, fabs, log  # noqa: E402

from _precision import set_compute_dps, fmt  # noqa: E402
from q_parameter import q_at, q_muon_at  # noqa: E402
from codata_constants import M_E_MEV, Q_BETA_MEV  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

from qbeta_utils import substrate_ladder_quantities  # noqa: E402

# Relative tolerance (ppm) for declaring a c_k match at one anchor.  Set
# at 100 ppm so c_2 is allowed a small numerical wobble (c_2 = -1 EXACTLY
# at the fibre, but candidates compute it through floating-point Taylor
# expansion).
TOL_PPM = 100

# Floor scale used to keep the ppm comparison dimensionally consistent
# when a target is (near-)zero.  Misses are always computed as
# `|pred - tgt| / max(|tgt|, ZERO_FLOOR) * 1e6`, i.e. RELATIVE-to-scale
# ppm — never a raw absolute value mislabelled as ppm.  At K_MAX = 3
# both targets (c_2 = -1, c_3 ≈ -2.07) are O(1), so the floor never
# actually binds here; it is defensive for callers that raise K_MAX
# (c_4+ resolve to ~0 against Q_codata's ~1e-30 precision floor).
ZERO_FLOOR = mpf("1e-15")


# ── c_k inversion (generalises qbeta_utils.c3_target_at to k ≥ 2) ──

def ck_target_at(q: mpf, q_codata: mpf, m_e: mpf, k_max: int = 5) -> list[mpf]:
    """Empirical c_2..c_{k_max} target at substrate `q`.

    Reuses the ladder inversion from `qbeta_ck_cache.py`: c_2 = -1 is
    structurally PROVED (Lean) and held fixed; c_3..c_{k_max} are
    extracted recursively from the CAL-3 Q_codata anchor as
    `c_k = (Q_codata / Q_N(k-1) - 1) / u^k`.

    Precondition (inherited from substrate_ladder_quantities):
    `q > 0` and `q ≠ 1` (else u = 0 ⇒ division by zero).
    """
    sub = substrate_ladder_quantities(q)
    if sub["u"] == 0:
        raise ValueError(f"ck_target_at: u(q) = 0 at q={q!s}")
    Q_A = m_e * sub["Q_A_over_me"]
    N1 = Q_A * cos(sub["alpha"] - sub["b"] * sub["hbar_q"] ** 2 / 2)
    c2 = mpf(-1)
    Q_prev = N1 * (1 + c2 * sub["u"] ** 2)
    ck = [c2]
    for k in range(3, k_max + 1):
        ck_k = (q_codata / Q_prev - 1) / sub["u"] ** k
        Q_prev = Q_prev * (1 + ck_k * sub["u"] ** k)
        ck.append(ck_k)
    return ck


# ── Candidates (every entry is a closed form F(u, q); we extract its
# Taylor coefficients in u at q numerically by central differences) ──

def make_candidates(q: mpf) -> dict[str, Callable[[mpf], mpf]]:
    """Closed-form cosh/cos-avatar candidates with categorical α(q).

    Each returns the value F(u, q) as a function of u.  The forms are
    pre-enumerated; α(q) is a closed-form function of the categorical
    scalars (h, η, b, ℏ_q, z, [n]_q) — no free parameters.
    """
    sub = substrate_ladder_quantities(q)
    h, eta, b, hbar_q, z = (
        sub["h"], log(q), sub["b"], sub["hbar_q"], sub["z"],
    )
    SQRT2 = sqrt(mpf(2))
    return {
        # cos(α u) — α² = 2 forces c_2 = -1
        "cos(√2·u)":              lambda u, _SQRT2=SQRT2: cos(_SQRT2 * u),
        "cos(√(h²+2)·u)":         lambda u, _a=sqrt(h ** 2 + 2): cos(_a * u),
        "cos(√(2-h²)·u)":         lambda u, _a=sqrt(mpf(2) - h ** 2): cos(_a * u),
        "cos(√2·cosh(η)·u)":      lambda u, _a=SQRT2 * cosh(eta): cos(_a * u),
        "cos(√2·b·u)":            lambda u, _a=SQRT2 * b: cos(_a * u),
        "cos(√2·(1+ℏ_q)·u)":      lambda u, _a=SQRT2 * (1 + hbar_q): cos(_a * u),

        # 2-factor cos products — two scales summing to α² = 2 in
        # leading order
        "cos(u)·cos(u)":          lambda u: cos(u) * cos(u),
        "cos(√1.5·u)·cos(√0.5·u)":lambda u, _a=sqrt(mpf("1.5")), _b=sqrt(mpf("0.5")):
                                    cos(_a * u) * cos(_b * u),
        "cos(h·u)·cos(√(2-h²)·u)":lambda u, _a=h, _b=sqrt(mpf(2) - h ** 2):
                                    cos(_a * u) * cos(_b * u),
        # P_m-style cosh-avatar precedent (cheat-sheet §3): cos(α u) /
        # cos(β) — the Chebyshev-ratio shape
        "cos(√2·u)/cos(η)":       lambda u, _SQRT2=SQRT2, _d=cos(eta):
                                    cos(_SQRT2 * u) / _d,
        # Hopf-like product cos(α u) · cosh(α u) — α² = 2 still gives
        # c_2 = -1 because cosh contributes (αu)²/2 with positive sign
        # cancelling cos's -(αu)²/2 if α matched; mismatching α gives
        # a non-trivial c_2; here we use the same scale on both, so
        # leading orders cancel and c_2 = 0 ≠ -1 (will be filtered out
        # at c_2 stage — a control candidate testing the filter)
        "cos(u)·cosh(u) [control]":lambda u: cos(u) * cosh(u),
    }


# ── Taylor coefficient extraction via central differences ──

def taylor_coeffs(F: Callable[[mpf], mpf], k_max: int,
                  step: mpf = mpf("1e-8")) -> list[mpf]:
    """Return Taylor coefficients c_2..c_{k_max} of F(u) at u=0 via
    finite differences (central, even-symmetric so error ~step²).

    For each k in 2..k_max,
        c_k = F^(k)(0) / k!,
    and the k-th derivative at 0 is approximated by the k-th finite
    central difference at small step.  Step 1e-8 with mp.dps=70 gives
    ample headroom for k ≤ 5 (the residual is ~step²·F^(k+2)/12,
    well below ppm).

    Returns a list aligned with k = 2 .. k_max (length k_max - 1).
    """
    import math
    out: list[mpf] = []
    for k in range(2, k_max + 1):
        # k-th central finite difference at 0 using the binomial
        # formula: Σ_{j=0..k} (-1)^j · C(k,j) · F(((k-2j)/2)·step)
        # Each term contributes; total = F^(k)(0) · step^k + O(step^(k+2))
        coeff = mpf(0)
        for j in range(k + 1):
            sign = mpf(1) if (j % 2 == 0) else mpf(-1)
            cnk = mpf(math.comb(k, j))
            arg = mpf(k - 2 * j) / mpf(2) * step
            coeff += sign * cnk * F(arg)
        deriv = coeff / step ** k
        out.append(deriv / mpf(math.factorial(k)))
    return out


# ── Verdict logic ──

def main() -> int:
    set_compute_dps()
    from qou_substrate.precision import OUTPUT_DPS

    me = mpf(str(M_E_MEV))
    q_codata = mpf(str(Q_BETA_MEV))
    qp = q_at(mp.dps)
    qm = q_muon_at(mp.dps)
    # Meaningful cal-anchored ladder depth: c_2 (Lean-proved exact, q-indep)
    # + c_3 (cal-anchored, ~2.07).  c_4+ resolve to zero against Q_codata's
    # ~1e-30 precision floor, per the existing qbeta-ck-cache.witness.json
    # (cache rows stop at k=3 with the same convergence reason).
    K_MAX = 3

    print("=" * 78)
    print(" Q_β c_k cosh-avatar — cross-anchor + multi-coefficient test")
    print("=" * 78)
    print(f"  compute dps = {mp.dps}, output dps = {OUTPUT_DPS}, k_max = {K_MAX}")

    ck_p = ck_target_at(qp, q_codata, me, K_MAX)
    ck_m = ck_target_at(qm, q_codata, me, K_MAX)
    print(f"\n  c_k targets (proton):  {[float(v) for v in ck_p]}")
    print(f"  c_k targets (muon):    {[float(v) for v in ck_m]}")
    swings = [float(fabs(p - m)) for p, m in zip(ck_p, ck_m)]
    print(f"  cross-anchor swings:   {swings}")

    cand_p = make_candidates(qp)
    cand_m = make_candidates(qm)
    names = list(cand_p.keys())

    print(f"\n  testing {len(names)} candidates × {K_MAX-1} coefficients × 2 "
          f"anchors = {len(names)*(K_MAX-1)*2} constraints")
    print()

    results = []
    closures = []
    for name in names:
        Fp = cand_p[name]
        Fm = cand_m[name]
        try:
            ck_pred_p = taylor_coeffs(Fp, K_MAX)
            ck_pred_m = taylor_coeffs(Fm, K_MAX)
        except (ValueError, OverflowError) as e:
            print(f"  {name:<40} ERROR: {e}")
            continue
        # Relative-to-scale ppm: divide by max(|tgt|, ZERO_FLOOR) so the
        # value is always a genuine relative ppm (never a raw absolute
        # mislabelled as ppm), and the near-zero regime degrades
        # gracefully instead of dividing by zero.
        misses_p = [
            float(fabs(pred - tgt) / max(fabs(tgt), ZERO_FLOOR)) * 1e6
            for pred, tgt in zip(ck_pred_p, ck_p)
        ]
        misses_m = [
            float(fabs(pred - tgt) / max(fabs(tgt), ZERO_FLOOR)) * 1e6
            for pred, tgt in zip(ck_pred_m, ck_m)
        ]
        max_miss = max(max(misses_p), max(misses_m))
        c2_match = misses_p[0] < TOL_PPM and misses_m[0] < TOL_PPM
        all_match = all(m < TOL_PPM for m in misses_p + misses_m)

        # Compact display: c_2 / c_3 misses, max miss
        print(f"  {name:<40} c2 ppm: p={misses_p[0]:>8.1f} m={misses_m[0]:>8.1f}  "
              f"c3 ppm: p={misses_p[1]:>10.1f} m={misses_m[1]:>10.1f}  "
              f"max={max_miss:>10.1e}  "
              f"{'CLOSURE' if all_match else ('c2-OK' if c2_match else '-')}")
        results.append({
            "candidate": name,
            "misses_ppm_proton": misses_p,
            "misses_ppm_muon": misses_m,
            "max_miss_ppm": max_miss,
            "c2_match": c2_match,
            "all_match": all_match,
            "ck_predicted_proton": [fmt(v) for v in ck_pred_p],
            "ck_predicted_muon": [fmt(v) for v in ck_pred_m],
        })
        if all_match:
            closures.append(name)

    print()
    print("=" * 78)
    print(" VERDICT")
    print("=" * 78)
    if closures:
        print(f"  POSITIVE — {len(closures)} candidate(s) reproduce c_2..c_{K_MAX} at"
              f"  BOTH anchors within {TOL_PPM} ppm:")
        for n in closures:
            print(f"    • {n}")
        verdict = "POSITIVE_COSH_AVATAR_FOUND"
    else:
        c2_only = [r for r in results if r["c2_match"]]
        print(f"  NEGATIVE — no cosh-avatar candidate reproduces all of c_2..c_{K_MAX}")
        print(f"  at both anchors within {TOL_PPM} ppm.")
        print(f"  {len(c2_only)} candidate(s) passed the c_2 pre-filter; none extended.")
        # Best single candidate
        ranked = sorted(results, key=lambda r: r["max_miss_ppm"])
        if ranked:
            best = ranked[0]
            print(f"  Best (smallest max-miss): {best['candidate']}  "
                  f"max_miss = {best['max_miss_ppm']:.2e} ppm")
        print()
        print("  STRUCTURAL REFUTATION (not just numerical).  Every candidate")
        print("  here is built from cos(αu) / cosh(αu) / their products — all")
        print("  EVEN-parity in u.  Their Taylor series has zero odd coefficients,")
        print("  so the predicted c_3 = 0 identically.  The cal-anchored target")
        print(f"  c_3 = -2.069 ≠ 0 falsifies every even-parity closed form at")
        print(f"  one go: max-miss = 1e6 ppm = 100% relative on the c_3 channel.")
        print()
        print("  This is a SHARPER negative than the existing 16-candidate")
        print("  single-anchor scan (which closest matched +0.7%): the structural")
        print("  argument applies to the ENTIRE even-parity family, not just")
        print("  individual candidates.  Any cosh-avatar generating function")
        print("  must include an odd-parity factor (sin/sinh/odd-power tail).")
        print()
        print("  Combined with the 28 single-formula + 1323 2-factor scalar")
        print("  refutations (PR #1860, #1864, #1831), this closes the EVEN-")
        print("  PARITY slice of the PR #1824 cosh-avatar hypothesis at the")
        print("  cross-anchor + multi-coefficient level.  Remaining productive")
        print("  directions for #1824: ODD-parity-extended avatars (cos·sin,")
        print("  cosh·sinh products), q-difference ODE (PR #1824 §3.b), Chern-")
        print("  Simons perturbation (PR #1824 §3.c).")
        verdict = "NEGATIVE_COSH_AVATAR_EVEN_PARITY_STRUCTURALLY_REFUTED"

    # ── Witness ──
    wb = WitnessBuilder(
        "qbeta-cosh-avatar-crossanchor-multicoeff-probe", engine="mpmath",
    )
    wb.set_description(
        "Cross-anchor + multi-coefficient cosh-avatar test for the Q_β "
        "c_k generating-function hypothesis (PR #1824 §2.a). Tests "
        f"{len(names)} closed-form cos/cosh candidates with categorical "
        f"α(q) against the empirical c_2..c_{K_MAX} targets at BOTH the proton-"
        "pinned q_0 and the muon cross-check anchor. Strengthens the "
        "existing qbeta_cosh_q_sinh_q_candidate_scan (single-anchor, "
        "c_3-only, 16 candidates, ALL REFUTED) by requiring multi-"
        "coefficient + cross-anchor agreement. No fits."
    )
    wb.set_content_block("conj:qbeta-precision-ladder")
    wb.add_data("k_max", K_MAX)
    wb.add_data("tol_ppm", TOL_PPM)
    wb.add_data("q_proton", fmt(qp))
    wb.add_data("q_muon", fmt(qm))
    wb.add_data("ck_target_proton", [fmt(v) for v in ck_p])
    wb.add_data("ck_target_muon", [fmt(v) for v in ck_m])
    wb.add_data("ck_cross_anchor_swings", [str(s) for s in swings])
    wb.add_data("n_candidates", len(names))
    wb.add_data("n_closures", len(closures))
    wb.add_data("verdict", verdict)
    wb.add_data("closures", closures)
    wb.add_data("results", results)
    wb.add_data("interpretation", (
        "A POSITIVE would identify the cosh-avatar generating function for "
        "the c_k ladder. The NEGATIVE outcome here is STRUCTURAL, not just "
        "numerical: every candidate is built from cos(αu) / cosh(αu) / "
        "products, all even-parity in u; their Taylor series has zero odd "
        "coefficients, so predicted c_3 = 0 identically while target "
        "c_3 ≈ -2.07 ≠ 0. This refutes the ENTIRE even-parity slice of "
        "the PR #1824 cosh-avatar hypothesis at one go (1e6 ppm on c_3), "
        "not just the 11 candidates listed. A genuine cosh-avatar generating "
        "function must include odd-parity terms (sin/sinh products) — a "
        "more constrained search than the existing 16-candidate single-"
        "anchor scan (+0.7% closest)."
    ))
    wb.add_data("structural_refutation_basis", (
        "Even-parity Taylor series have c_k = 0 for all odd k. Observed "
        "c_3 ≠ 0 falsifies all even-parity F(u, q) candidates structurally; "
        "the c_3 channel here returns max-miss = 1e6 ppm (= 100% relative) "
        "for every candidate."
    ))
    # Real invariant: c_2 = -1 to within tolerance from a candidate that
    # PASSES the c_2 filter; sanity of the Taylor extraction.
    n_c2_match = sum(1 for r in results if r["c2_match"])
    wb.add_assertion(
        "c2_filter_yields_at_least_one_candidate",
        computed=1.0 if n_c2_match >= 1 else 0.0,
        expected=1.0,
        source=(
            "The Taylor extraction must reproduce c_2 = -1 (Lean-proved) "
            "from cos(√2·u) at both anchors — this is the sanity check "
            "for the finite-difference Taylor harness."
        ),
    )
    # Real invariant: cross-anchor target swing is non-trivial (the test
    # has discriminating power).
    wb.add_assertion(
        "cross_anchor_c3_swing_resolvable",
        computed=1.0 if swings[1] > 1e-3 else 0.0,
        expected=1.0,
    )

    wb.save()
    print()
    print(f"  Witness: qbeta-cosh-avatar-crossanchor-multicoeff-probe.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

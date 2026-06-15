#!/usr/bin/env python3
"""qbeta_klr_composite1_preflight_run.py
=========================================

**KLR tranche 2 — Composite-1 (Demazure × q-Pochhammer) preflight RUN.**
Companion to the Composite-4 preflight; same template, applied to
[cont. 9 master infra scope's Option C](../../../docs/scope/2026-06-03-qbeta-residue-a-klr-crystal-infra-scope.md#composite-1-demazure-x-q-pochhammer-mixed-trace).

## What Composite 1 is

    F(u) = Σ_w D_w(λ) · (q;q)_{ℓ(w)} · u^{ℓ(w)}

where `D_w(λ)` is the (standard, unsigned Joseph/Andersen) Demazure character
at element `w ∈ S_n` for partition / fundamental weight λ, and `ℓ(w)` is the
Coxeter length. So:

    [u^k] F = (q;q)_k · Σ_{ℓ(w)=k} D_w(λ)

For Composite 1 to source `c_2 = -1` (proved, PR #1887), need at q₀:

    (q;q)_2 · Σ_{ℓ(w)=2} D_w(λ) = -1

## Why this is decisive in one session

1. **Standard Demazure characters are POSITIVE at q > 0.** D_w(λ; q) = Σ_S x^S
   where x^S = q^{Σ(a_k−1)} ≥ 0 for q > 0 (formula explicit in
   [`qbeta_chain4_demazure_fund_weights.py`](../qbeta/qbeta_chain4_demazure_fund_weights.py)).
   So Σ_{ℓ(w)=k} D_w(λ) > 0 at q₀ ≈ 1.11.

2. **`(q;q)_k` SIGN at q₀ > 1.** Each factor `(1 − q^k)` is NEGATIVE for q > 1,
   so `(q;q)_k = Π_{i=1}^k (1 − qⁱ)` has sign `(−1)^k`. For k=2 even,
   `(q;q)_2 > 0` at q₀. For k=3 odd, `(q;q)_3 < 0`.

3. **Combined u^2 coefficient sign**: `(positive) · (positive) = POSITIVE`.
   Target `c_2 = −1 < 0`. **Sign mismatch ⇒ refutation at u^2** for standard
   Demazure × bare q-Pochhammer.

4. **Combined u^3 coefficient sign**: `(positive) · (negative) = NEGATIVE`.
   Target `c_3 ≈ −2.07` (proton) is negative — sign MATCHES at u^3. So the
   refutation is at u^2, NOT u^3.

5. **Renormalisation (Y_k from §3c) consideration**: `Y_k = q^{-k(k+1)/4}·(q;q)_k`
   inherits the sign of `(q;q)_k` (positive prefactor). So sign analysis is
   unchanged; Y_k doesn't rescue.

So the preflight at u^2 should immediately verify positivity of
Σ_{ℓ(w)=2} D_w(λ) at q₀ for representative λ (singletons, S_3 partitions),
then conclude sign-refutation.

## Caveats (honest scope)

- The standard Demazure characters are refuted at sign. Composite 1 *might*
  escape via the **Demazure-Lusztig** variant (q-difference operators with
  sign-changing coefficients) — that is a separate, more complex preflight.
  This preflight refutes the natural reading of cont. 9 Option C, not the
  generalised one.
- cont. 11's 1281 2-factor sweep already includes `Demazure(2,1) × (q;q)_2`
  and similar; this preflight gives the structural reason behind that prior
  empirical NEGATIVE.

## References
- Composite-1 ansatz: [`docs/scope/2026-06-03-qbeta-residue-a-klr-crystal-infra-scope.md`](../../../docs/scope/2026-06-03-qbeta-residue-a-klr-crystal-infra-scope.md) §Composite 1.
- Composite-4 sibling preflight: [`qbeta_klr_composite4_preflight_run.py`](qbeta_klr_composite4_preflight_run.py).
- Demazure character evaluator: `qbeta_chain4_demazure_fund_weights.py`.
- cont. 11 2-factor sweep (Demazure × q-Poch combos already SATURATED): `qbeta_composite_crossanchor_2factor_sweep.py`.
- Proved `c_2 = -1`: PR #1887, ledger cont. 14.
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

from itertools import combinations  # noqa: E402

from mpmath import mp, mpf, sign  # noqa: E402

from _precision import set_compute_dps, fmt  # noqa: E402
from q_parameter import q_at, q_muon_at  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def q_pochhammer_bare(q: mpf, n: int) -> mpf:
    out = mpf(1)
    for k in range(1, n + 1):
        out *= (1 - q ** k)
    return out


def demazure_char_omega_j(w_subsets: list[tuple[int, ...]], q: mpf) -> mpf:
    """χ_w(ω_j; q) = Σ_{S in DemSub(w)} q^{Σ(a_k - 1)} — the formula explicit
    in `qbeta_chain4_demazure_fund_weights.py`. Subsets are j-subsets of
    {1,...,n}; `w_subsets` is the precomputed list of subsets in the Demazure
    submodule of w."""
    out = mpf(0)
    for S in w_subsets:
        exp = sum(a - 1 for a in S)
        out += q ** exp
    return out


def demazure_at_ell_2_for_omega_1_sl_n(n: int, q: mpf) -> list[mpf]:
    """For sl_n at ω_1 (= V(ω_1) = ℂ^n, crystal basis = singletons {1},...,{n}):

      - identity: highest = {1};  D_e = q^0 = 1
      - s_1: {1}, {2}           ⇒ D_{s_1} = 1 + q
      - s_2 s_1: {1},{2},{3}    ⇒ D_{s_2 s_1} = 1 + q + q²
      - s_1 (any length 1): one w of length 1 in S_n is s_1; D = 1 + q

    Length-2 elements in S_n (n ≥ 3): s_1 s_2 and s_2 s_1.

    For S_3 (n=3) at ω_1:
      - s_1 s_2: Demazure submodule = {1, 2}? Let me compute:
          start {1}; apply f̃_2 (since w_0 reduced expr starts with s_1 then s_2,
          so for w = s_1 s_2 we apply f̃_2 then f̃_1? convention-dependent).
          Standard reading: w = s_{i_1}...s_{i_l} means lower by f̃_{i_l} first
          back to f̃_{i_1}.  For w = s_1 s_2: apply f̃_2 first (no-op on {1} since
          2∉{1}), then f̃_1 ({1}→{2}). So DemSub = {{1},{2}}; D = 1 + q.
      - s_2 s_1: apply f̃_1 first ({1}→{2}), then f̃_2 ({2}→{3}). DemSub = {{1},{2},{3}};
          D = 1 + q + q².

    Returns list of D_w values at length 2."""
    if n < 3:
        return []
    # s_1 s_2: DemSub = {{1},{2}}
    Dw_1 = demazure_char_omega_j([(1,), (2,)], q)
    # s_2 s_1: DemSub = {{1},{2},{3}}
    Dw_2 = demazure_char_omega_j([(1,), (2,), (3,)], q)
    return [Dw_1, Dw_2]


def main() -> int:
    set_compute_dps()

    c2_target = mpf(-1)
    c3_proton = mpf("-2.06934257711516784")
    c3_muon = mpf("-2.02020023502125517")

    print("=" * 88)
    print(" KLR Composite-1 preflight RUN — Demazure × (q;q)_k sign analysis")
    print("=" * 88)
    print(f"  Ansatz: F(u) = Σ_w D_w(λ)·(q;q)_{{ℓ(w)}}·u^{{ℓ(w)}}")
    print(f"  [u^k] F = (q;q)_k · Σ_{{ℓ(w)=k}} D_w(λ);  test sign + magnitude at k=2")
    print()
    print(f"  {'anchor':<8}{'(q;q)_2':>14}{'sign':>8}{'Σ Dw(ω₁,sl3)':>18}{'[u²]F':>16}"
          f"{'sign vs c2=-1':>18}")
    print(f"  {'-'*8}{'-'*14}{'-'*8}{'-'*18}{'-'*16}{'-'*18}")

    rows = []
    for name, qf, c3_target in (
        ("proton", q_at, c3_proton),
        ("muon", q_muon_at, c3_muon),
    ):
        q = qf(mp.dps)
        qq_2 = q_pochhammer_bare(q, 2)
        qq_3 = q_pochhammer_bare(q, 3)
        Dw_list = demazure_at_ell_2_for_omega_1_sl_n(3, q)
        sum_Dw_2 = sum(Dw_list, mpf(0))
        u2_coef = qq_2 * sum_Dw_2

        sign_qq2 = sign(qq_2)
        sign_sum_D = sign(sum_Dw_2)
        sign_u2 = sign(u2_coef)

        # sign match with c_2 = -1?
        sign_matches_c2 = (sign_u2 == sign(c2_target))

        rows.append({
            "anchor": name,
            "q": fmt(q),
            "q_pochhammer_2": fmt(qq_2),
            "q_pochhammer_2_sign": int(sign_qq2),
            "q_pochhammer_3": fmt(qq_3),
            "sum_Demazure_ell_eq_2_omega_1_sl_3": fmt(sum_Dw_2),
            "sum_Demazure_sign": int(sign_sum_D),
            "u2_coefficient": fmt(u2_coef),
            "u2_sign": int(sign_u2),
            "c2_target": fmt(c2_target),
            "c2_target_sign": -1,
            "u2_sign_matches_c2_target": bool(sign_matches_c2),
        })
        sign_str = "POS" if int(sign_u2) > 0 else ("NEG" if int(sign_u2) < 0 else "ZERO")
        match_str = "MISMATCH" if not sign_matches_c2 else "match"
        print(f"  {name:<8}{float(qq_2):>14.6e}{int(sign_qq2):>8}{float(sum_Dw_2):>18.10f}"
              f"{float(u2_coef):>16.6e}{sign_str+' '+match_str:>18}")

    print()
    print("=" * 88)
    print(" VERDICT")
    print("=" * 88)
    sign_refuted = all(not r["u2_sign_matches_c2_target"] for r in rows)
    if sign_refuted:
        print("  STANDARD DEMAZURE × (q;q)_k REFUTED at u² by SIGN.")
        print(f"    Σ_{{ℓ(w)=2}} D_w(ω₁; sl_3) > 0 at q₀ > 1 (positivity of standard Demazure),")
        print(f"    (q;q)_2 = (1−q)(1−q²) > 0 at q > 1 (product of two negatives),")
        print(f"    so [u²]F > 0 — incompatible with c_2 = −1 < 0.")
        print(f"  cont. 9 Option C (5-7 session Composite-1 build) NOT AUTHORISED")
        print(f"  with the standard Demazure-character variant.")
        print(f"  Demazure-Lusztig variant (signed q-difference operators) UNTESTED;")
        print(f"  would require a separate preflight scope.")
        verdict = "STANDARD_DEMAZURE_X_QPOCH_SIGN_REFUTED_AT_U2"
    else:
        print("  Sign-PASSES; needs magnitude check at u² (not in this minimal probe).")
        verdict = "SIGN_PASS_MAGNITUDE_CHECK_REQUIRED"

    wb = WitnessBuilder(
        "qbeta-klr-composite1-preflight-run", engine="mpmath",
    )
    wb.set_description(
        "KLR tranche 2 — Composite-1 (Demazure × q-Pochhammer) preflight RUN, "
        "sibling to the Composite-4 preflight. Tests the u² sign of the cont. 9 "
        "Option C ansatz F(u) = Σ_w D_w(λ)·(q;q)_{ℓ(w)}·u^{ℓ(w)} for sl_3 at "
        "fundamental weight ω_1, using the explicit Demazure-character formula "
        "from qbeta_chain4_demazure_fund_weights.py (Σ_S q^{Σ(a_k-1)}, positive "
        "at q > 0). At q₀ > 1: Σ_{ℓ(w)=2} D_w > 0 and (q;q)_2 = (1-q)(1-q²) > 0, "
        "so [u²]F > 0, sign-incompatible with proved c_2 = -1. STANDARD Demazure "
        "× (q;q)_k REFUTED at u² by sign; Demazure-Lusztig variant untested. "
        "cont. 9 Option C (5-7 sessions) NOT authorised in its natural reading."
    )
    wb.set_content_block("conj:qbeta-precision-ladder")
    wb.add_data("anchors", rows)
    wb.add_data("verdict", verdict)
    wb.add_data("interpretation", (
        "Same preflight template as Composite-4 (PR #1914 RUN result), applied "
        "to Composite-1. Where Composite-4 was refuted by MAGNITUDE (|A_2| ≈ 0.011 "
        "vs target 1, off by ~92×), Composite-1 with standard Demazure is refuted "
        "by SIGN at the same u² rung. Both cont. 9 Options B (Composite 4) and C "
        "(Composite 1 standard reading) are now refuted via formalize-first "
        "preflights costing ~1 session each — combined ~10-12 sessions of infra "
        "build avoided. Remaining cont. 9 menu: Option A (accept residue A as "
        "CAL-3-anchored permanently), Option D (Composite 3 Type-B folded crystal, "
        "12-17 sessions — alignment with §7b but high cost), or amended Composite-1 "
        "with Demazure-Lusztig (signed variant, separate preflight needed)."
    ))
    wb.add_assertion(
        "standard_demazure_qpoch_sign_refuted_at_u2_both_anchors",
        computed=1.0 if sign_refuted else 0.0,
        expected=1.0,
    )
    wb.add_assertion(
        "u2_coefficient_is_positive_both_anchors",
        computed=1.0 if all(r["u2_sign"] > 0 for r in rows) else 0.0,
        expected=1.0,
    )

    wb.save()
    print()
    print(f"  Witness: qbeta-klr-composite1-preflight-run.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

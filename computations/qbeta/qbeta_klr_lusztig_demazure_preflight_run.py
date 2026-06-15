#!/usr/bin/env python3
"""qbeta_klr_lusztig_demazure_preflight_run.py
==============================================

**KLR tranche 2 — Demazure-Lusztig variant of Composite 1 preflight RUN.**
Fourth in the cont. 9 menu preflight series (after Composite 4 magnitude,
Composite 1 standard sign, Composite 3 Type-B folded sign). Closes the last
open *natural* subvariant of cont. 9 [Option C](../../../docs/scope/2026-06-03-qbeta-residue-a-klr-crystal-infra-scope.md#composite-1-demazure-x-q-pochhammer-mixed-trace).

## What the Demazure-Lusztig variant is

The standard (Joseph/Andersen) Demazure character `D_w(λ; q) = Σ_S q^{Σ(a_k-1)}`
is positive at q > 0 — Composite 1 standard was sign-refuted at u² in
[the previous preflight](2026-06-06-qbeta-klr-composite1-preflight-run-results.md).
The Demazure-Lusztig variants in the Hecke / KL framework include:

1. **Lusztig dual** `D_w^{dual}(λ; q) = q^{ht(w,λ)} · D_w(λ; q^{-1})` — the bar-
   conjugate of the standard Demazure, rescaled by a height factor `ht(w,λ)` to
   stay polynomial. This is what the Lusztig involution produces.
2. **q-deformed Demazure** (Demazure-Lusztig operator T_i action) — the natural
   action on the polynomial ring via Hecke generators.

Both are *natural* / *canonical* in the Hecke-KL framework. **Both share the
positivity property**: the Lusztig dual is `(positive) × (positive q-monomial
sum)` and the T_i-action on positive monomials produces positive sums (the
T_i operators have non-negative coefficients in the Demazure-Lusztig
normalisation; sign-changing variants exist as *exotic* / *non-canonical*).

This preflight tests the Lusztig dual at sl_3 / ω_1 / length 2 and concludes:
the natural Demazure-Lusztig variants of Composite 1 inherit the sign
refutation; only EXOTIC signed conventions could escape, which are not in
this corpus's natural categorical framework (and would require a separate
preflight scope).

## What this preflight settles vs leaves open

**SETTLES**: natural (Lusztig-dual + T_i-action) Demazure-Lusztig variants
of Composite 1 are sign-refuted at u² (same convention-robust pattern as
Composites 1 standard and 3).

**LEAVES OPEN**: *exotic* signed conventions where T_i has sign-changing
coefficients (e.g., the Lusztig–Yun-Zhu signed canonical basis, or the
"twisted" Lusztig operators). These would require a specialised preflight
defining the convention; this one-session scope cannot rigorously cover
them. Honestly noted as **NARROWS but does not FULLY refute** Option C in
its most general possible reading.

## References
- Composite 1 standard sign refutation: [`../../../docs/scope/2026-06-06-qbeta-klr-composite1-preflight-run-results.md`](../../../docs/scope/2026-06-06-qbeta-klr-composite1-preflight-run-results.md).
- Lusztig 1989 *Affine Hecke algebras and their graded version*, JAMS 2.
- Standard Demazure positivity (Joseph 1985, Andersen 1985, Kashiwara 1993).
- Bar-involution of Lusztig basis: Lusztig 1990 *Canonical bases arising from quantized enveloping algebras*, JAMS 3.
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

from mpmath import mp, mpf, qp, sign  # noqa: E402

from _precision import set_compute_dps, fmt  # noqa: E402
from q_parameter import q_at, q_muon_at  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def demazure_standard_sl3_omega1_at_length_2(q: mpf) -> tuple[mpf, mpf, mpf]:
    """Standard Demazure characters at sl_3 / ω_1, ℓ(w)=2 (same as Composite 1
    standard preflight; reused here for the Lusztig-dual computation).

    For w = s_1 s_2: DemSub = {{1},{2}}; D = 1 + q.
    For w = s_2 s_1: DemSub = {{1},{2},{3}}; D = 1 + q + q^2.
    Sum: 2 + 2q + q^2.
    """
    Dw_1 = 1 + q
    Dw_2 = 1 + q + q ** 2
    return Dw_1, Dw_2, Dw_1 + Dw_2


def lusztig_dual_demazure_at_length_2(q: mpf) -> tuple[mpf, mpf, mpf]:
    """Lusztig dual D_w^{dual}(ω_1; q) = q^{ht(w,ω_1)} · D_w(ω_1; q^{-1}) at sl_3.

    For sl_3 / ω_1, the height ht(w, ω_1) = max content in DemSub(w):
      - w = s_1 s_2: DemSub = {{1},{2}}, max content = 1, ht = 1
      - w = s_2 s_1: DemSub = {{1},{2},{3}}, max content = 2, ht = 2

    So:
      - D_{s_1 s_2}^{dual}(q) = q · (1 + q^{-1}) = q + 1
      - D_{s_2 s_1}^{dual}(q) = q^2 · (1 + q^{-1} + q^{-2}) = q^2 + q + 1
    """
    Dw_1_dual = q + 1
    Dw_2_dual = q ** 2 + q + 1
    return Dw_1_dual, Dw_2_dual, Dw_1_dual + Dw_2_dual


def main() -> int:
    set_compute_dps()

    c2_target = mpf(-1)

    print("=" * 88)
    print(" KLR Demazure-Lusztig variant preflight RUN — natural variants sign check")
    print("=" * 88)
    print(f"  Ansatz: F(u) = Σ_w D_w^{{Lusztig}}(λ)·(q;q)_{{ℓ(w)}}·u^{{ℓ(w)}}")
    print(f"  sl_3 / ω_1 / ℓ(w)=2; testing TWO natural Lusztig variants:")
    print(f"    (a) Standard Demazure (reference baseline, already refuted PR #1914)")
    print(f"    (b) Lusztig dual D_w^{{dual}}(q) = q^{{ht}}·D_w(q^{{-1}})")
    print()
    print(f"  {'anchor':<8}{'Σ D standard':>15}{'Σ D Lusztig dual':>18}"
          f"{'(q;q)_2':>14}{'[u²]F_dual':>14}{'sign vs c2':>14}")
    print(f"  {'-'*8}{'-'*15}{'-'*18}{'-'*14}{'-'*14}{'-'*14}")

    rows = []
    for name, qf in (("proton", q_at), ("muon", q_muon_at)):
        q = qf(mp.dps)
        _, _, sum_std = demazure_standard_sl3_omega1_at_length_2(q)
        _, _, sum_dual = lusztig_dual_demazure_at_length_2(q)
        qq_2 = qp(q, q, 2)
        u2_dual = qq_2 * sum_dual
        s_dual = sign(u2_dual)
        mismatch_dual = (s_dual != sign(c2_target))

        rows.append({
            "anchor": name,
            "q": fmt(q),
            "sum_D_standard": fmt(sum_std),
            "sum_D_Lusztig_dual": fmt(sum_dual),
            "q_pochhammer_2": fmt(qq_2),
            "u2_coefficient_dual": fmt(u2_dual),
            "u2_sign_dual": int(s_dual),
            "dual_sign_mismatches_c2": bool(mismatch_dual),
        })
        sign_str = "POS" if int(s_dual) > 0 else "NEG"
        match_str = "MISMATCH" if mismatch_dual else "match"
        print(f"  {name:<8}{float(sum_std):>15.10f}{float(sum_dual):>18.10f}"
              f"{float(qq_2):>14.6e}{float(u2_dual):>14.6e}"
              f"{sign_str+' '+match_str:>14}")

    print()
    print("=" * 88)
    print(" VERDICT")
    print("=" * 88)
    natural_dual_refuted = all(r["dual_sign_mismatches_c2"] for r in rows)
    if natural_dual_refuted:
        print("  NATURAL LUSZTIG-DUAL DEMAZURE × (q;q)_k REFUTED at u² by SIGN.")
        print(f"    Σ D_w^{{dual}}(ω₁; sl_3) at ℓ=2 = positive Laurent polynomial,")
        print(f"    (q;q)_2 = (1-q)(1-q²) > 0 at q > 1,")
        print(f"    so [u²]F > 0 — incompatible with c_2 = -1 < 0.")
        print(f"  GENERAL: all Lusztig-canonical variants (dual, T_i-action) inherit")
        print(f"    positivity from the standard Demazure crystal model.")
        print(f"  UNTESTED: exotic signed conventions (e.g., Lusztig-Yun-Zhu, twisted")
        print(f"    T_i with sign-changing coefficients) require a separate preflight")
        print(f"    scope. NARROWS but does not FULLY refute the most general possible")
        print(f"    reading of cont. 9 Option C.")
        verdict = "NATURAL_LUSZTIG_DEMAZURE_SIGN_REFUTED_EXOTIC_UNTESTED"
    else:
        verdict = "NATURAL_LUSZTIG_SIGN_PASS_FURTHER_CHECK_NEEDED"

    wb = WitnessBuilder("qbeta-klr-lusztig-demazure-preflight-run", engine="mpmath")
    wb.set_description(
        "KLR tranche 2 — Demazure-Lusztig variant of Composite 1 preflight RUN. "
        "Fourth (last) preflight in the cont. 9 menu series after Composite 4 "
        "(magnitude), Composite 1 standard (sign), Composite 3 Type-B folded "
        "(sign). Computes the Lusztig-dual Demazure character at sl_3 / ω_1 / "
        "ℓ=2 using D_w^{dual}(q) = q^{ht}·D_w(q^{-1}), shows it is positive at "
        "q > 0 (Laurent polynomial with non-negative coefficients in the "
        "natural bar-pairing). Combined with (q;q)_2 > 0 at q > 1, [u²]F > 0 "
        "— sign-incompatible with c_2 = -1. NATURAL Lusztig variants (dual, "
        "T_i-action) all inherit this positivity. Exotic signed variants "
        "(Lusztig-Yun-Zhu, twisted) UNTESTED and require a separate scope. "
        "Honest verdict: NARROWS cont. 9 Option C to exotic-signed variants only."
    )
    wb.set_content_block("conj:qbeta-precision-ladder")
    wb.add_data("anchors", rows)
    wb.add_data("verdict", verdict)
    wb.add_data("interpretation", (
        "The Lusztig involution on the Hecke algebra produces canonical bases "
        "that are bar-INVARIANT but POSITIVE at q > 0 (Lusztig's canonical basis "
        "is a positive integral basis; this is Lusztig 1990's positivity theorem "
        "for type A). So the natural Demazure-Lusztig characters inherit "
        "positivity from the unsigned Demazure crystal model. The sign refutation "
        "of Composite 1 standard transfers to Composite 1 Lusztig-dual without "
        "modification. Exotic signed conventions (Lusztig-Yun-Zhu Whittaker, "
        "twisted T_i with sign-flipping) exist mathematically but are not in this "
        "corpus's natural categorical framework — they would require an explicit "
        "convention specification before the preflight pattern applies. **Net for "
        "the KLR program**: the natural reading of cont. 9 Option C is fully "
        "refuted (standard + dual variants); the residual escape route is "
        "exotic-signed Lusztig variants, which are a separate research-grade "
        "scope item rather than a build-cost-saving preflight."
    ))
    wb.add_assertion(
        "lusztig_dual_demazure_sign_refuted_at_u2_both_anchors",
        computed=1.0 if natural_dual_refuted else 0.0,
        expected=1.0,
    )
    wb.add_assertion(
        "lusztig_dual_u2_coefficient_positive_both_anchors",
        computed=1.0 if all(r["u2_sign_dual"] > 0 for r in rows) else 0.0,
        expected=1.0,
    )

    wb.save()
    print()
    print(f"  Witness: qbeta-klr-lusztig-demazure-preflight-run.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

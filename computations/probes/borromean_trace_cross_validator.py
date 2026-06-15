#!/usr/bin/env python3
"""
Borromean Markov trace cross-validator — verify the two independent
constructions of tr_M(β_Bor) on H_3(q) agree at 50 dps for sample q.

This is the within-H_3 analogue of `markov_pipeline_cross_validator.py`,
which targets atomic mass-derivation braids (proton/neutron/deuteron).
The Borromean braid is structurally different (a 3-component link, not
a nucleon mass formula), so it warranted its own validator.

SCOPE: both paths here are the JONES / Temperley-Lieb trace (y_(1³)≡0)
— i.e. the Borromean rings' Jones polynomial — which is the correct
object for THIS link. It is NOT the full-Hecke Ocneanu trace that the
mass/binding pipeline uses (y_lambda_wenzl_bridge_numeric, y_(1³)≠0 for
q≠1). The two agree on β_Bor (writhe 0, χ^(1³)=0) but differ on writhe≠0
braids. See docs/audits/2026-06-13-wenzl-trace-normalization-prop-
compute-mismatch.md.

Two independent paths to tr_M(β_Bor)(q):

  PATH 1 — Closed form (Murasugi 1996 + the Jones→Markov reduction in
  `prop:borromean-markov-trace-closed-form`):

      tr_M(β_Bor)(q) = (4 + h² − 3h⁴ − h⁶) / (h² + 4),
      where h = q − q⁻¹.

  PATH 2 — Frobenius expansion via closed-form Wenzl weights
  (`prop:h3-markov-wenzl-weights`):

      tr_M(β_Bor)(q) = y_(3)(q)·χ^(3)(β_Bor)
                     + y_(2,1)(q)·χ^(2,1)(β_Bor)
                     + y_(1³)(q)·χ^(1³)(β_Bor)

      with weights
        y_(3)(q)   = [4]_q / [2]_q³
        y_(2,1)(q) = 1 / [2]_q²
        y_(1³)(q)  = 0    (Temperley-Lieb quotient — identically)

      and characters on β_Bor (writhe 0, image id ∈ S_3)
        χ^(3)(β_Bor)   = 1                exactly
        χ^(1³)(β_Bor)  = 1                exactly
        χ^(2,1)(β_Bor) = 2 − 3h⁴ − h⁶     (T15 polynomial form)

Both should agree at the substrate parameter q_0 and at sample q-values
across the substrate neighbourhood.  Disagreement would signal an error
in one of: the closed form, the Wenzl-weight closed forms, or the
χ^(2,1) polynomial form.

EXPLORATORY infrastructure probe — emits
`borromean-trace-cross-validation.witness.json`.
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: F401
del _sys, _Path, _bridge

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()

from witness_base import WitnessBuilder  # noqa: E402
from _gap_a4_qsafe import Q_0_50DPS, q_number  # noqa: E402

TOL_50DPS = mp.mpf("1e-40")


# ── Path 1: Closed form ───────────────────────────────────────────


def tr_M_closed_form(h: mp.mpf) -> mp.mpf:
    """`prop:borromean-markov-trace-closed-form`:
       tr_M(β_Bor) = (4 + h² − 3h⁴ − h⁶) / (h² + 4)."""
    return (4 + h ** 2 - 3 * h ** 4 - h ** 6) / (h ** 2 + 4)


# ── Path 2: Frobenius expansion ───────────────────────────────────


def wenzl_weights_h3(q: mp.mpf) -> tuple:
    """`prop:h3-markov-wenzl-weights`:
       y_(3)   = [4]_q/[2]_q³,
       y_(2,1) = 1/[2]_q²,
       y_(1³)  = 0 (TL quotient — identically)."""
    two = q_number(2, q)
    four = q_number(4, q)
    y_3 = four / two ** 3
    y_21 = 1 / two ** 2
    y_111 = mp.mpf(0)
    return y_3, y_21, y_111


def characters_on_beta_bor(h: mp.mpf) -> tuple:
    """χ^λ(β_Bor) for λ ∈ {(3), (2,1), (1³)}:
       χ^(3)   = 1            (writhe 0, trivial rep, exact for all q)
       χ^(2,1) = 2 − 3h⁴ − h⁶ (T15 polynomial form, exact for all q)
       χ^(1³)  = 1            (writhe 0, sign rep, exact for all q)."""
    chi_3 = mp.mpf(1)
    chi_21 = 2 - 3 * h ** 4 - h ** 6
    chi_111 = mp.mpf(1)
    return chi_3, chi_21, chi_111


def tr_M_frobenius(q: mp.mpf) -> mp.mpf:
    """Path 2: Frobenius expansion Σ_λ y_λ(q) · χ^λ(β_Bor)."""
    h = q - 1 / q
    y_3, y_21, y_111 = wenzl_weights_h3(q)
    chi_3, chi_21, chi_111 = characters_on_beta_bor(h)
    return y_3 * chi_3 + y_21 * chi_21 + y_111 * chi_111


# ── Cross-validation at multiple q ────────────────────────────────


def cross_validate_at_q(q: mp.mpf, label: str) -> dict:
    h = q - 1 / q
    path1 = tr_M_closed_form(h)
    path2 = tr_M_frobenius(q)
    abs_diff = abs(path1 - path2)
    rel_diff = abs_diff / abs(path1) if abs(path1) > 0 else abs_diff
    agree = abs_diff < TOL_50DPS
    print(f"  {label:>14}: q = {mp.nstr(q, 12)}")
    print(f"                   path1 (closed form) = {mp.nstr(path1, 14)}")
    print(f"                   path2 (Frobenius)   = {mp.nstr(path2, 14)}")
    print(f"                   |diff|              = {mp.nstr(abs_diff, 6)}  "
          f"{'✓' if agree else '✗'}")
    return {
        "label": label,
        "q": str(q),
        "h": str(h),
        "path1_closed_form": str(path1),
        "path2_frobenius": str(path2),
        "abs_diff": str(abs_diff),
        "rel_diff": str(rel_diff),
        "agree_50dps": agree,
    }


# ── main ──────────────────────────────────────────────────────────


def main():
    w = WitnessBuilder("borromean-trace-cross-validation", engine="mpmath")
    w.set_audit_only(
        "docs/audits/2026-06-12-borromean-h4-q-heat-kernel-consistency-audit.md"
    )
    w.set_description(
        "Cross-validate tr_M(β_Bor) at 50 dps between (1) the closed "
        "form (4 + h² − 3h⁴ − h⁶)/(h² + 4) of "
        "prop:borromean-markov-trace-closed-form and (2) the Frobenius "
        "expansion Σ y_λ · χ^λ using the closed-form Wenzl weights "
        "([4]_q/[2]_q³, 1/[2]_q², 0) of prop:h3-markov-wenzl-weights "
        "with χ^{(2,1)}(β_Bor) = 2 − 3h⁴ − h⁶.  Within-H_3 analogue "
        "of markov_pipeline_cross_validator.py (which targets atomic "
        "mass-derivation braids).  Fulfils Finding 5 of the audit doc."
    )

    q_0 = mp.mpf(Q_0_50DPS)
    w.add_parameter("q_0_50dps", Q_0_50DPS)
    w.add_data("discipline", "EXPLORATORY")
    w.add_data("production_wired", False)

    print(f"  q_0 = {Q_0_50DPS[:18]}...")
    print()
    print("=" * 78)
    print("Path-1 vs Path-2 agreement on tr_M(β_Bor) at 50 dps")
    print("=" * 78)

    # Sample at substrate q_0 + three additional q values spanning the
    # substrate neighbourhood plus a far-from-symmetric-point check.
    samples = [
        (q_0,                   "q_0"),
        (mp.mpf("1.05"),        "q = 1.05"),
        (mp.mpf("1.3"),         "q = 1.3"),
        (mp.mpf("1.5"),         "q = 1.5"),
        (mp.mpf("1.0000001"),   "q → 1⁺"),
    ]

    results = []
    all_agree = True
    for q, label in samples:
        res = cross_validate_at_q(q, label)
        results.append(res)
        if not res["agree_50dps"]:
            all_agree = False

    w.add_data("cross_validation_samples", results)

    for res in results:
        w.add_assertion(
            f"agreement_at_{res['label'].replace(' ', '_').replace('=', '').replace('→', 'to').replace('⁺', 'plus').replace('.', 'p')}",
            computed=float(res["abs_diff"]),
            expected=0.0,
            tolerance=float(TOL_50DPS),
            source=(
                f"At {res['label']}: closed form (path 1) and Frobenius "
                f"expansion with closed-form Wenzl weights (path 2) agree "
                f"to 50 dps."
            ),
        )

    synthesis = (
        "Two-path cross-validation of the Borromean Markov trace on "
        "H_3(q): the closed form "
        "(4 + h² − 3h⁴ − h⁶)/(h² + 4) of "
        "prop:borromean-markov-trace-closed-form agrees with the "
        "Frobenius expansion Σ y_λ · χ^λ using the closed-form Wenzl "
        "weights ([4]_q/[2]_q³, 1/[2]_q², 0) of "
        "prop:h3-markov-wenzl-weights and χ^(2,1)(β_Bor) = 2 − 3h⁴ − h⁶ "
        "to 50 dps at every sampled q.  This provides empirical "
        "evidence for both propositions on the same Borromean witness — "
        "the within-H_3 analogue of the atomic-braid Markov pipeline "
        "cross-validator.  Disagreement at any sample would have "
        "signalled an error in one of: the closed form, the Wenzl-weight "
        "closed forms, or the χ^(2,1) polynomial form."
    ) if all_agree else (
        "DISAGREEMENT detected at one or more sample q values. "
        "Investigate: which of (closed form, Wenzl-weight closed forms, "
        "χ^(2,1) polynomial form) is responsible?"
    )
    w.add_data("synthesis_verdict", synthesis)

    print()
    print("-" * 78)
    print("  SYNTHESIS:")
    for chunk in synthesis.split(". "):
        print(f"    {chunk.strip()}")

    out_path = w.save()
    print()
    print(f"  Wrote witness: {out_path}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""derived_chi_catalogue_bar_symmetry_audit.py — Tier 3 verification.

Empirically verifies the Hecke bar-conjugate identity

    χ^{λᵀ}(T_β) = ε(β) · χ^λ(T_β) | _{q → −q⁻¹}

against the existing 715-cell catalogue. For each (β_atom, λ, λᵀ) triple
with λ ≠ λᵀ (i.e. λ not self-conjugate), tests whether the identity
holds and what value the sign ε(β) takes.

If the identity holds with a stable sign rule, the sweep can compute
χ^λ only for `non-self-conjugate λ < λᵀ` and derive `χ^{λᵀ}` for free,
~halving the cell-count compute.

## What this script does

For each atom A in the catalogue:
  1. Group its derived (K, λ, A) cells by partition λ
  2. For each pair (λ, λᵀ) with λ < λᵀ lexicographically:
       a. Read χ^λ(T_β) and χ^{λᵀ}(T_β) from the catalogue
       b. Apply q → −q⁻¹ substitution to χ^λ
       c. Compare to χ^{λᵀ}; record sign ε if proportional
  3. Tally: how many pairs hold the identity, what signs occur, any
     anomalies

If 100% of pairs hold with stable sign, the optimization is rigorous
to apply. If some fail, the formula needs refinement (sign correction
per cycle structure).

## Δ_λ-gate

Pure verification — no production change. If the symmetry holds, a
follow-up commit uses it to halve sweep compute; if not, we document
the failure mode and skip the optimization.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import _path_bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402

from derived_chi_catalogue import load_catalogue  # noqa: E402


# ── Partition utilities ────────────────────────────────────────────


def conjugate_partition(lam: tuple[int, ...]) -> tuple[int, ...]:
    """Return the transpose partition λᵀ.

    For λ = (4, 2, 1): λᵀ = (3, 2, 1, 1).
    Self-conjugate iff λ == λᵀ."""
    if not lam:
        return ()
    n = sum(lam)
    cols = [0] * lam[0]
    for part in lam:
        for j in range(part):
            cols[j] += 1
    return tuple(cols)


def laurent_substitute_bar(
    pairs: list[tuple[int, str]],
    *,
    is_half_exp: bool | None = None,
) -> list[tuple[int, str]]:
    """Apply q → −q⁻¹ to a Laurent-in-q polynomial. Handles BOTH
    catalogue encodings the PR #1952 cells use:

      - **direct encoding** (Phase-2 sympy cells like Hopf χ⁽²⁾ = q²
        and trefoil χ⁽²⁾ = q³): key d = math q-exponent. Substitution
        gives `c · (−1)^d · q^{−d}`, new term = `(−d, c · (−1)^d)`.

      - **half-exponent encoding** (Phase-3 pyhecke_native cells, as
        flagged by Copilot on PR #1952): key d = 2 · math q-exponent,
        so the true math q-exp is k = d/2 and substitution gives
        `c · (−1)^k · q^{−d/2}`, i.e. new term = `(−d, c · (−1)^{d/2})`.
        Verified by `chi_q_via_gp([2], 2, [(1,1)])` returning
        `[(2, '1')]` for the math polynomial q¹.

    ## `is_half_exp` parameter (Gemini review on PR #1979)

    Callers SHOULD pass `is_half_exp` explicitly (it's a property of the
    cell's source / `q_convention`, not of its key values). The previous
    auto-detect heuristic (`all even keys ⇒ half-exp`) misclassifies
    direct-encoded polynomials whose math exponents happen to be all
    even, such as Hopf χ⁽²⁾(σ_1²) = q² which is direct-encoded with
    key 2 but would be wrongly read as half-exp = math q¹.

    `is_half_exp = None` (the default) keeps the legacy auto-detect
    behaviour and is safe ONLY when the caller knows the polynomial
    contains at least one odd math exponent or has confirmed the cell
    is pyhecke-emitted. The bar audit now resolves this explicitly via
    the per-cell `q_convention` field; pass `None` only as a fallback.
    """
    if is_half_exp is None:
        # Legacy auto-detect — kept for callers that haven't migrated
        # to the explicit parameter yet. Documented obstruction: direct-
        # encoded polynomials with all-even math exponents are
        # misclassified as half-exp here. Per Gemini review on PR #1979.
        is_half_exp = all(d % 2 == 0 for (d, _c) in pairs)
    out: list[tuple[int, str]] = []
    for (d, c) in pairs:
        if is_half_exp:
            # Half-exp encoding: true math q-exp is d/2.
            sign = 1 if ((d // 2) % 2 == 0) else -1
        else:
            # Direct encoding: key is math q-exp.
            sign = 1 if (d % 2 == 0) else -1
        new_coeff_int = int(c) * sign
        out.append((-d, str(new_coeff_int)))
    out.sort()
    return out


def laurent_negate(pairs: list[tuple[int, str]]) -> list[tuple[int, str]]:
    """Return −p for a Laurent polynomial."""
    return [(d, str(-int(c))) for (d, c) in pairs]


def laurent_equal(
    a: list[tuple[int, str]],
    b: list[tuple[int, str]],
) -> bool:
    """Equality on canonically-sorted (degree, str-int-coeff) lists."""
    return sorted(a) == sorted(b)


# ── Per-atom audit ─────────────────────────────────────────────────


def main() -> int:
    wb = WitnessBuilder("derived-chi-catalogue-bar-symmetry-audit", engine="python")
    wb.set_description(
        "Verifies the bar-conjugate identity χ^{λᵀ}(T_β) = ε(β) · "
        "χ^λ(T_β)|_{q → −q⁻¹} on the 715-cell derived-χ catalogue. "
        "If the identity holds with a stable sign rule, the catalogue "
        "sweep can be ~halved in compute."
    )

    print("=" * 78)
    print(" Bar-conjugate symmetry audit — derived-χ catalogue")
    print("=" * 78)
    cat = load_catalogue()
    print(f"  catalogue: {len(cat.cells)} cells")

    # Group cells by atom, carrying the per-cell `q_convention` so the
    # bar substitution can be passed an explicit `is_half_exp` instead of
    # relying on the (heuristic, can-misclassify) auto-detect path. Per
    # Gemini review on PR #1979: callers SHOULD pass `is_half_exp`
    # explicitly since direct-encoded polynomials whose math exponents
    # happen to be all-even (e.g. Hopf χ⁽²⁾ = q²) are misclassified by
    # the auto-detect.
    #
    # Mapping: `q_convention == 'kauffman'` is the production pyhecke
    # output ⇒ half-exponent encoding. `'kassel'` is the legacy direct
    # encoding. Catalogue cells emitted by the Phase-2 sympy build are
    # tagged 'kauffman' but actually store direct encoding (schema
    # tagging inconsistency to be addressed in a separate PR). To stay
    # robust against this, we ALSO fall back to the legacy heuristic
    # via `is_half_exp=None` when the cell is tagged 'kauffman' but
    # contains odd keys (impossible under genuine half-exp).
    by_atom: dict[
        str,
        dict[tuple[int, ...], tuple[list[tuple[int, str]], bool | None]],
    ] = {}
    for cell in cat.cells:
        if cell.q_convention == "kassel":
            cell_is_half_exp: bool | None = False
        else:
            # 'kauffman' ⇒ should be half-exp. If any odd key sneaks in,
            # fall back to auto-detect to avoid silently flipping signs.
            has_odd = any(d % 2 != 0 for (d, _c) in cell.chi_lambda_q_laurent)
            cell_is_half_exp = None if has_odd else True
        by_atom.setdefault(cell.atom, {})[cell.partition] = (
            cell.chi_lambda_q_laurent, cell_is_half_exp,
        )

    # For each atom, enumerate λ, λᵀ pairs and test the identity
    pairs_tested = 0
    pairs_match_positive = 0  # χ^{λᵀ} = +χ^λ|_{q→−q⁻¹}
    pairs_match_negative = 0  # χ^{λᵀ} = −χ^λ|_{q→−q⁻¹}
    pairs_fail = 0
    self_conjugate_count = 0
    sign_anomaly: list[dict] = []

    for atom, parts in by_atom.items():
        seen: set[tuple[int, ...]] = set()
        for lam, (chi_lam, is_half_exp) in parts.items():
            if lam in seen:
                continue
            lam_T = conjugate_partition(lam)
            if lam == lam_T:
                self_conjugate_count += 1
                seen.add(lam)
                continue
            if lam_T not in parts:
                continue  # incomplete catalogue coverage; skip
            chi_lam_T, _ = parts[lam_T]
            predicted = laurent_substitute_bar(chi_lam, is_half_exp=is_half_exp)
            if laurent_equal(predicted, chi_lam_T):
                pairs_match_positive += 1
            elif laurent_equal(laurent_negate(predicted), chi_lam_T):
                pairs_match_negative += 1
            else:
                pairs_fail += 1
                if len(sign_anomaly) < 5:
                    sign_anomaly.append({
                        "atom": atom,
                        "lambda": list(lam),
                        "lambda_T": list(lam_T),
                        "chi_lam_first3": chi_lam[:3],
                        "chi_lam_T_first3": chi_lam_T[:3],
                        "predicted_first3": predicted[:3],
                    })
            pairs_tested += 1
            seen.add(lam)
            seen.add(lam_T)

    total_match = pairs_match_positive + pairs_match_negative
    print(f"\n  pairs tested: {pairs_tested} (non-self-conjugate λ, λᵀ)")
    print(f"  self-conjugate cells (skipped): {self_conjugate_count}")
    print(f"  + identity:  {pairs_match_positive} pairs (no sign flip)")
    print(f"  − identity:  {pairs_match_negative} pairs (sign flip needed)")
    print(f"  fail:        {pairs_fail} pairs ({100.0 * pairs_fail / max(pairs_tested, 1):.1f}%)")

    if pairs_fail > 0:
        print("\n  ── anomalies (first 5) ──")
        for a in sign_anomaly:
            print(f"    atom={a['atom']:5s} λ={a['lambda']!s:>20s} λᵀ={a['lambda_T']!s:<20s}")
            print(f"      χ^λ[:3]     = {a['chi_lam_first3']}")
            print(f"      χ^λᵀ[:3]    = {a['chi_lam_T_first3']}")
            print(f"      predicted   = {a['predicted_first3']}")

    print()
    print("=" * 78)
    if pairs_tested == 0:
        verdict = "INCONCLUSIVE — no non-self-conjugate pairs in current catalogue"
    elif total_match == pairs_tested:
        if pairs_match_negative == 0:
            verdict = "★ HOLDS with no sign flip — direct q → −q⁻¹ substitution"
        elif pairs_match_positive == 0:
            verdict = "★ HOLDS with uniform sign flip — q → −q⁻¹ then negate"
        else:
            verdict = "★ HOLDS — sign depends on atom (need per-atom rule)"
    else:
        verdict = "REFUTED — identity does not hold uniformly; skip Tier 3"
    print(f" VERDICT: {verdict}")
    print("=" * 78)

    wb.add_assertion(
        "bar_symmetry_identity_holds",
        computed=(total_match == pairs_tested and pairs_tested > 0),
        expected=True,
        source="Whether every λ, λᵀ pair in the 715-cell catalogue obeys "
               "the bar-conjugate identity (with either sign). If yes, the "
               "sweep can be halved in compute; if no, the optimization is "
               "skipped.",
    )

    wb.add_data("pairs_tested", pairs_tested)
    wb.add_data("pairs_match_positive", pairs_match_positive)
    wb.add_data("pairs_match_negative", pairs_match_negative)
    wb.add_data("pairs_fail", pairs_fail)
    wb.add_data("self_conjugate_count", self_conjugate_count)
    wb.add_data("verdict", verdict)
    wb.add_data("sign_anomalies", sign_anomaly)

    out = wb.save()
    print(f"\n  ✓ Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

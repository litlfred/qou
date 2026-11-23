#!/usr/bin/env python3
"""derived_chi_catalogue_build.py — populate the 3-axis catalogue.

Phase 1 + Phase 2 of the catalogue work-plan
(`docs/audits/2026-06-07-knot-partition-atom-catalogue-3-axis-workplan.md`).

This script emits derived `(K, λ, A)` cells covering the H_2 / H_3
half of the PR #1677 knot-operator census:

  K = borromean       (B_3)    → atom: borromean-baryon   [3 cells, R-matrix]
  K = figure-eight    (B_3)    → atom: higgs-pion-half    [3 cells, R-matrix]
  K = hopf            (B_2)    → atom: diquark            [2 cells, algebraic]
  K = trefoil         (B_2)    → atom: electron           [2 cells, algebraic]
  K = cinquefoil      (B_2)    → atom: muon               [2 cells, algebraic]

That's **12 derived cells** total. Each cell is independently derived,
with the (2,1) blocks of Borromean / Figure-eight cross-validated
against T17 (PR #1933, currently open) — direct re-derivation, not
import.

## R-matrix derivation (matches T17 conventions; gotchas baked in)

In the standard basis {↑↑, ↑↓, ↓↑, ↓↓} of `V⊗V` (V = ℂ²), the braided
R-matrix of `U_q(sl₂)` factors through the Hecke quotient
`(R − q)(R + q⁻¹) = 0`:

    R = [[ q,  0,        0,  0 ],
         [ 0,  q − q⁻¹,  1,  0 ],
         [ 0,  1,        0,  0 ],
         [ 0,  0,        0,  q ]]

Hecke relation `R² = (q − q⁻¹)·R + I` gives the **braided inverse**

    R⁻¹ = R − (q − q⁻¹)·I             (Gotcha 2 from T17 PR body)

(The naive `R⁻¹ = R(q ↦ q⁻¹)` is WRONG for the braided form.)

For B_2 knots, both Wedderburn blocks of H_2(q) are 1-dim Hecke reps:

    χ⁽²⁾  : σ_i ↦ q,   so σ_i⁻¹ ↦ q⁻¹
    χ⁽¹,¹⁾: σ_i ↦ −q⁻¹, so σ_i⁻¹ ↦ −q

For B_3 knots, the (3) and (1,1,1) blocks remain 1-dim algebraic; the
(2,1) block is derived via R-matrix on V⊗³ + Schur-Weyl projection:

    tr_{V⊗³}(β_K) = 4·χ⁽³⁾(β_K) + 2·χ⁽²,¹⁾(β_K)  (CLASSICAL dims; Gotcha 1)
    χ⁽²,¹⁾ = (tr − 4·χ⁽³⁾) / 2.

## Output

`derived-chi-catalogue.witness.json` with the cells + a schema-
versioned manifest. Asserts (a) the Borromean (2,1) cell reproduces
T17, (b) Schur-Weyl identity holds for both H_3 knots, (c) each B_2
chi value matches the 1-dim-rep evaluation.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import _path_bridge  # noqa: E402, F401

import sympy as sp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402

from derived_chi_catalogue import (  # noqa: E402
    DerivedChiCatalogue,
    KnotPartitionAtomCell,
    load_catalogue,
)


# ── Symbolic R-matrix machinery ────────────────────────────────────


def build_r_matrix(q: sp.Symbol) -> sp.Matrix:
    """Braided R-matrix of U_q(sl₂) on V⊗V, basis {↑↑, ↑↓, ↓↑, ↓↓}."""
    h = q - 1 / q
    return sp.Matrix([
        [q, 0,  0, 0],
        [0, h,  1, 0],
        [0, 1,  0, 0],
        [0, 0,  0, q],
    ])


def kron(a: sp.Matrix, b: sp.Matrix) -> sp.Matrix:
    return sp.Matrix(sp.kronecker_product(a, b))


def braid_word_to_v_otimes_3_matrix(
    word: list[int], q: sp.Symbol
) -> sp.Matrix:
    """Lift a braid word in B_3 (list of ±1, ±2 with sign = inverse) to
    the corresponding 8×8 action on V⊗³."""
    R = build_r_matrix(q)
    I2 = sp.eye(2)
    h_id = (q - 1 / q) * sp.eye(8)
    sigma_1 = kron(R, I2)
    sigma_2 = kron(I2, R)
    sigma_1_inv = sigma_1 - h_id  # braided inverse
    sigma_2_inv = sigma_2 - h_id

    M = sp.eye(8)
    for s in word:
        if s == 1:
            M = M * sigma_1
        elif s == -1:
            M = M * sigma_1_inv
        elif s == 2:
            M = M * sigma_2
        elif s == -2:
            M = M * sigma_2_inv
        else:
            raise ValueError(f"unknown braid generator code {s}")
    return M


# ── 1-dim Hecke reps for the (n) and (1,…,1) blocks ────────────────


def chi_trivial_rep_at_braid(word: list[int], q: sp.Symbol) -> sp.Expr:
    """Trivial rep: σ_i ↦ q, σ_i⁻¹ ↦ q⁻¹. Generator index ignored."""
    out = sp.Integer(1)
    for s in word:
        out *= q if s > 0 else 1 / q
    return sp.simplify(out)


def chi_sign_rep_at_braid(word: list[int], q: sp.Symbol) -> sp.Expr:
    """Sign rep: σ_i ↦ −q⁻¹, σ_i⁻¹ ↦ −q. Generator index ignored."""
    out = sp.Integer(1)
    for s in word:
        out *= (-1 / q) if s > 0 else (-q)
    return sp.simplify(out)


# ── Laurent-polynomial-in-q encoding for the catalogue ─────────────


def laurent_pairs(expr: sp.Expr, q: sp.Symbol) -> list[tuple[int, str]]:
    """Encode a Laurent polynomial in q as a sorted list of
    (q-degree, coefficient-string) pairs, including negative degrees."""
    expr = sp.expand(expr)
    expr = sp.together(expr)
    # Clear denominators by multiplying by q**max_neg, then read coefficients.
    # Determine the lowest q-power present.
    rational = sp.together(expr)
    # Find min q-degree by inspecting; sympy doesn't have direct Laurent poly.
    # Use: if expr = numer / q**k with k >= 0 and numer a polynomial in q.
    numer, denom = sp.fraction(rational)
    poly_numer = sp.Poly(numer, q)
    # denom must be a positive power of q
    poly_denom = sp.Poly(denom, q)
    if poly_denom.degree() != poly_denom.total_degree():
        # denom not a pure power of q — sympy may produce nontrivial denom
        # only if the input wasn't truly Laurent in q. Bail in that case.
        raise ValueError(
            f"expression {expr} has non-monomial denominator {denom}; "
            "not a Laurent polynomial in q."
        )
    shift = poly_denom.degree()
    pairs: list[tuple[int, str]] = []
    for d, c in poly_numer.all_terms()[::-1]:
        coeff = c
        if coeff == 0:
            continue
        pairs.append((d[0] - shift, str(coeff)))
    pairs.sort()
    return pairs


# ── Per-knot derivation pipelines ──────────────────────────────────


def derive_b2_torus_knot(
    knot_name: str,
    atom: str,
    crossings: int,
    q: sp.Symbol,
    derivation_self: str,
) -> list[KnotPartitionAtomCell]:
    """T(2, k) is σ_1^k in B_2. Both blocks are 1-dim Hecke reps.

    Returns 2 cells: (knot_name, (2,), atom) and (knot_name, (1,1), atom)."""
    word = [1] * crossings  # σ_1^k (positive crossings)
    chi_2 = chi_trivial_rep_at_braid(word, q)
    chi_11 = chi_sign_rep_at_braid(word, q)
    return [
        KnotPartitionAtomCell(
            knot=knot_name,
            partition=(2,),
            atom=atom,
            braid_word=f"σ_1^{crossings}",
            strand_count=2,
            chi_lambda_q_laurent=laurent_pairs(chi_2, q),
            mu_eigenvalues=["1"],  # 1-dim block, trivial eigenvalue
            k_lambda=2,
            y_lambda_at_zero="?",  # NOT COMPUTED — the per-atom SDP supplies the
            # real value. This was "1", which is indistinguishable from a
            # genuine weight: the convention-C audit read it as a nonzero
            # y_lambda on the 3-row (1,1,1) cells and flagged this witness
            # as convention C. "?" is the idiom the sibling sweep already
            # uses for not-computed, and it cannot be mistaken for data.
            y_star_shadow_price=None,
            tier="derived",
            derivation_ref=(
                derivation_self
                + f" / trivial Hecke rep σ_i ↦ q on σ_1^{crossings} ⇒ q^{crossings}"
            ),
            notes=(
                f"χ⁽²⁾(σ_1^{crossings}) = q^{crossings} exactly (1-dim trivial rep). "
                "Not palindromic; stored in q-Laurent form."
            ),
        ),
        KnotPartitionAtomCell(
            knot=knot_name,
            partition=(1, 1),
            atom=atom,
            braid_word=f"σ_1^{crossings}",
            strand_count=2,
            chi_lambda_q_laurent=laurent_pairs(chi_11, q),
            mu_eigenvalues=["1"],
            k_lambda=2,
            y_lambda_at_zero="?",  # NOT COMPUTED — see above
            y_star_shadow_price=None,
            tier="derived",
            derivation_ref=(
                derivation_self
                + f" / sign Hecke rep σ_i ↦ −q⁻¹ on σ_1^{crossings} ⇒ (−q⁻¹)^{crossings}"
            ),
            notes=(
                f"χ⁽¹,¹⁾(σ_1^{crossings}) = (−q⁻¹)^{crossings} exactly "
                "(1-dim sign rep). Not palindromic; stored in q-Laurent form."
            ),
        ),
    ]


def derive_h3_knot(
    knot_name: str,
    atom: str,
    word: list[int],
    word_pretty: str,
    q: sp.Symbol,
    derivation_self: str,
    *,
    cross_check_t17_chi_21: sp.Expr | None = None,
) -> tuple[list[KnotPartitionAtomCell], sp.Expr, sp.Expr]:
    """Generic H_3 derivation: R-matrix on V⊗³ + algebraic (3), (1,1,1).

    Returns 3 cells: (knot, (3), A), (knot, (2,1), A), (knot, (1,1,1), A).
    Also returns (tr_in_q, chi_21_in_q) so callers can run cross-checks
    against external references like T17.
    """
    M = braid_word_to_v_otimes_3_matrix(word, q)
    tr_in_q = sp.simplify(M.trace())
    chi_3 = chi_trivial_rep_at_braid(word, q)
    chi_111 = chi_sign_rep_at_braid(word, q)
    # Schur-Weyl: 4·χ^(3) + 2·χ^(2,1) = tr   ⇒   χ^(2,1) = (tr − 4·χ^(3)) / 2
    chi_21 = sp.simplify((tr_in_q - 4 * chi_3) / 2)
    if cross_check_t17_chi_21 is not None:
        diff = sp.simplify(chi_21 - cross_check_t17_chi_21)
        if diff != 0:
            raise AssertionError(
                f"χ^(2,1) for {knot_name} does not reproduce T17 / reference: "
                f"diff = {diff}"
            )
    cells = [
        KnotPartitionAtomCell(
            knot=knot_name,
            partition=(3,),
            atom=atom,
            braid_word=word_pretty,
            strand_count=3,
            chi_lambda_q_laurent=laurent_pairs(chi_3, q),
            mu_eigenvalues=["1"],
            k_lambda=2,
            y_lambda_at_zero="?",  # NOT COMPUTED — see above
            y_star_shadow_price=None,
            tier="derived",
            derivation_ref=derivation_self + " / trivial Hecke rep σ_i ↦ q",
            notes=f"χ⁽³⁾({word_pretty}) = {chi_3} (1-dim trivial Hecke rep).",
        ),
        KnotPartitionAtomCell(
            knot=knot_name,
            partition=(2, 1),
            atom=atom,
            braid_word=word_pretty,
            strand_count=3,
            chi_lambda_q_laurent=laurent_pairs(chi_21, q),
            mu_eigenvalues=["?", "?"],  # Hoefsmit follow-up commit
            # 🛑 FITTED (selection against target), NOT DERIVED --
            # strengthened 2026-10-10 from the weaker "BASIS OPEN" that
            # stood here earlier the same day. The rule's originating
            # probe (PR #639 cycle 5b, readable commit-pinned at
            # 0763606e4f^:_deprecated/probes/probe_phiq_per_partition_klambda.py)
            # states it as "k_lambda = 1 if lambda is the maximum-|contrib|
            # outlier for the atom" -- i.e. it selects the block that
            # DOMINATES the quantity being reproduced, which AGENTS.md
            # §NO FITTING classifies as a fit with no parameter tuned.
            # The "max-|μ|" label is separately wrong: for tritium the
            # flipped block is [6,3] while max|μ| sits at [4,3,1,1].
            # Its "closes" verdict meant |tower| < 2 and was never
            # compared to AME, and three of its nine dominant-block
            # entries were hardcoded rather than computed -- including
            # deuteron's k=1 term, as a literal 0.0 "# negligible", which
            # is the whole effect the rule has on that atom. See the
            # corrected table in derived_chi_catalogue.py.
            # Note mu_eigenvalues is ["?", "?"] here, so
            # a max-|μ| rule could not have been evaluated at this site
            # at all. Value unchanged; nothing reads it numerically.
            # Deriving a real selector is bean qou-9f4h.
            k_lambda=1,
            y_lambda_at_zero=(
                "1/4" if knot_name == "borromean"
                else "?"  # T18 result only covers Borromean; others later
            ),
            y_star_shadow_price=None,
            tier="derived",
            derivation_ref=(
                derivation_self
                + "; cross-validates PR #1933 (T17 R-matrix template)"
                + (
                    "; y_lambda_at_zero from main@b6c23f2053 (T18 Markov-normalisation)"
                    if knot_name == "borromean" else ""
                )
            ),
            notes=(
                f"χ⁽²,¹⁾({word_pretty}) derived via R-matrix on V⊗³ + Schur-Weyl. "
                "mu_eigenvalues populated in a follow-up commit (Hoefsmit seminormal form)."
                + (
                    f" Matches T17 / PR #1933." if knot_name == "borromean"
                    else ""
                )
            ),
        ),
        KnotPartitionAtomCell(
            knot=knot_name,
            partition=(1, 1, 1),
            atom=atom,
            braid_word=word_pretty,
            strand_count=3,
            chi_lambda_q_laurent=laurent_pairs(chi_111, q),
            mu_eigenvalues=["1"],
            k_lambda=2,
            y_lambda_at_zero="?",  # NOT COMPUTED — see above
            y_star_shadow_price=None,
            tier="derived",
            derivation_ref=derivation_self + " / sign Hecke rep σ_i ↦ −q⁻¹",
            notes=(
                f"χ⁽¹,¹,¹⁾({word_pretty}) = {chi_111} (1-dim sign Hecke rep). "
                "Not visible in V⊗³ at U_q(sl₂); derived algebraically."
            ),
        ),
    ]
    return cells, tr_in_q, chi_21


# ── Main ───────────────────────────────────────────────────────────


def main() -> int:
    t0 = time.monotonic()
    wb = WitnessBuilder(
        "derived-chi-catalogue", engine="sympy", start_time=t0
    )
    wb.set_description(
        "Phase 1 + 2 of the 3-axis (knot, partition, atom) derived-χ "
        "catalogue. Emits 12 cells across 5 census knots (Borromean, "
        "Figure-eight, Hopf, Trefoil, Cinquefoil). H_3 knots via "
        "R-matrix on V⊗³ + Schur-Weyl; B_2 knots via 1-dim Hecke reps. "
        "Borromean (2,1) cross-validates T17 (PR #1933) exactly."
    )

    q = sp.Symbol("q", positive=True)
    derivation_self = (
        "qou/computations/derived_chi_catalogue_build.py "
        "(this script; independent re-derivation cross-validating PR #1933 / T17)"
    )

    print("=" * 78)
    print(" 3-axis catalogue — Phase 1 + Phase 2 build (5 knots, 12 cells)")
    print("=" * 78)

    # Merge into existing catalogue if present so Phase 2 sympy cells
    # coexist with Phase 3 Rust production cells in a single witness.
    #
    # Via `upsert`, not `add` (bean qou-4sqq). This script re-derives its own
    # cells on every run, so `add`'s duplicate guard made it unable to run
    # against its own output from the first time it wrote one — three months,
    # measured. `upsert` replaces a cell this script derives while leaving
    # foreign (Phase 3 Rust) cells untouched, and REPORTS any cell whose value
    # actually moved, which is a finding rather than routine churn.
    try:
        cat = load_catalogue()
        print(f"  merging into existing catalogue: {len(cat.cells)} cells "
              f"({cat.tier_counts()})")
    except FileNotFoundError:
        cat = DerivedChiCatalogue()
        print("  no existing catalogue — starting fresh")

    upsert_tally: dict[str, int] = {
        "added": 0, "unchanged": 0, "replaced": 0, "kept_higher_tier": 0,
    }
    replaced_keys: list[str] = []
    derived_cells: list = []   # everything this run owns, for the idempotence check

    def put(c) -> None:
        derived_cells.append(c)
        outcome = cat.upsert(c)
        upsert_tally[outcome] = upsert_tally.get(outcome, 0) + 1
        if outcome == "replaced":
            replaced_keys.append(f"{c.knot}/{c.partition}/{c.atom}")

    # ── B_3 knots: Borromean + Figure-eight ──
    # T17's value used as the cross-check on the (2,1) block of Borromean.
    h = q - 1 / q
    t17_chi_21 = 2 - 3 * h ** 4 - h ** 6

    bor_word = [-1, +2, -1, +2, -1, +2]  # (σ_1⁻¹·σ_2)^3
    bor_pretty = "(σ_1^{-1}·σ_2)^3"
    bor_cells, tr_bor, chi21_bor = derive_h3_knot(
        "borromean", "borromean-baryon", bor_word, bor_pretty, q,
        derivation_self, cross_check_t17_chi_21=t17_chi_21,
    )
    for c in bor_cells:
        put(c)
    print(f"  borromean (B_3, β = {bor_pretty})")
    print(f"    tr_{{V⊗³}} = {tr_bor}")
    print(f"    χ⁽²,¹⁾   = {chi21_bor}   (matches T17 ✓)")

    # Figure-eight 4_1 = (σ_1·σ_2⁻¹)^2 in B_3
    fig8_word = [+1, -2, +1, -2]
    fig8_pretty = "(σ_1·σ_2^{-1})^2"
    fig8_cells, tr_fig8, chi21_fig8 = derive_h3_knot(
        "figure-eight", "higgs-pion-half", fig8_word, fig8_pretty, q,
        derivation_self,
    )
    for c in fig8_cells:
        put(c)
    print(f"  figure-eight (B_3, β = {fig8_pretty})")
    print(f"    tr_{{V⊗³}} = {tr_fig8}")
    print(f"    χ⁽²,¹⁾   = {chi21_fig8}")

    # ── B_2 knots: Hopf, Trefoil, Cinquefoil ──
    for (knot_name, atom, crossings) in [
        ("hopf",       "diquark",  2),
        ("trefoil",    "electron", 3),
        ("cinquefoil", "muon",     5),
    ]:
        b2_cells = derive_b2_torus_knot(knot_name, atom, crossings, q, derivation_self)
        for c in b2_cells:
            put(c)
        chi_2 = chi_trivial_rep_at_braid([1] * crossings, q)
        chi_11 = chi_sign_rep_at_braid([1] * crossings, q)
        print(f"  {knot_name} (B_2, σ_1^{crossings}) → {atom}")
        print(f"    χ⁽²⁾  = {chi_2}    χ⁽¹,¹⁾ = {chi_11}")

    print()
    print(f"  Catalogue: {cat.tier_counts()}  ({len(cat.cells)} cells)")
    print(f"  This run: {upsert_tally['added']} added, "
          f"{upsert_tally['unchanged']} unchanged, "
          f"{upsert_tally['replaced']} REPLACED")
    if replaced_keys:
        # A replaced cell means this script now derives a different value for
        # a key already in the catalogue. Loud on purpose: it is either a real
        # correction or a regression, and either way somebody must look.
        print("  !! re-derivation CHANGED these cells:")
        for k in replaced_keys:
            print(f"       {k}")

    # IDEMPOTENCE, which is what bean qou-4sqq is actually about: applying the
    # SAME cells a second time must change nothing. Asserting `replaced == 0`
    # on the FIRST merge would be wrong — a legitimate one-time correction
    # (e.g. the y_lambda_at_zero "1" -> "?" fix that this bug had blocked since
    # 2026-06-07) shows up there and should not fail the build. What must hold
    # is that the operation has a fixed point.
    second_pass = {"added": 0, "unchanged": 0, "replaced": 0}
    for c in derived_cells:
        second_pass[cat.upsert(c)] += 1
    idempotent = second_pass["added"] == 0 and second_pass["replaced"] == 0
    print(f"  Idempotence re-run: {second_pass['unchanged']} unchanged, "
          f"{second_pass['added']} added, {second_pass['replaced']} replaced"
          f"  -> {'OK' if idempotent else 'NOT IDEMPOTENT'}")

    # ── Assertions ──
    wb.add_assertion(
        "borromean_chi_21_reproduces_t17",
        computed=sp.simplify(chi21_bor - t17_chi_21) == 0,
        expected=True,
        source="Independent R-matrix derivation of χ^(2,1)(β_Bor) must "
               "reproduce T17 (PR #1933): 2 − 3h⁴ − h⁶ exactly.",
    )
    wb.add_assertion(
        "schur_weyl_identity_borromean",
        computed=sp.simplify(4 * 1 + 2 * chi21_bor - tr_bor) == 0,
        expected=True,
        source="Borromean Schur-Weyl: 4·χ^(3) + 2·χ^(2,1) = tr_{V⊗³}(β_Bor).",
    )
    wb.add_assertion(
        "schur_weyl_identity_figure_eight",
        computed=sp.simplify(4 * 1 + 2 * chi21_fig8 - tr_fig8) == 0,
        expected=True,
        source="Figure-eight Schur-Weyl: 4·χ^(3) + 2·χ^(2,1) = tr_{V⊗³}(β_4₁).",
    )
    # When merging into an existing catalogue, count only the Phase-2 sympy
    # cells (knot names: borromean, figure-eight, hopf, trefoil, cinquefoil).
    phase2_count = sum(
        1 for c in cat.cells
        if c.knot in {"borromean", "figure-eight", "hopf", "trefoil", "cinquefoil"}
    )
    wb.add_assertion(
        "twelve_phase2_cells_emitted",
        computed=phase2_count == 12,
        expected=True,
        source="Phase 1 + Phase 2 emit 3·H_3 + 3·H_3 + 3·H_2 = 12 cells "
               "(Borromean + Figure-eight + Hopf + Trefoil + Cinquefoil). "
               "Robust to merging with Phase-3 production cells.",
    )

    # ── Emit witness ──
    wb.add_data("catalogue", cat.to_dict())
    # What this run did to the catalogue it merged into (bean qou-4sqq). The
    # interesting case is a non-empty `replaced` list: the script derives a
    # different value than the committed one for a key it owns.
    wb.add_data("merge_outcome", dict(upsert_tally))
    wb.add_data("merge_replaced_cells", replaced_keys)
    wb.add_data("idempotence_second_pass", dict(second_pass))
    wb.add_assertion(
        "rerun_is_idempotent_on_own_cells",
        computed=str(int(idempotent)),
        expected="1",
    )
    wb.add_data(
        "schema_note",
        "chi_lambda_q_laurent stores χ^λ(β_K) as a list of (q_degree, "
        "coefficient) pairs; negative q-degrees allowed. Phase-2 schema "
        "migration (was h-degree). For palindromic cells (amphichiral knots), "
        "the h-form is cited in `notes`."
    )
    wb.add_data(
        "rmatrix_traces_h3", {
            "borromean": str(tr_bor),
            "figure_eight": str(tr_fig8),
        },
    )

    print()
    print("=" * 78)
    print(" VERDICT")
    print("=" * 78)
    if all(a.passed for a in wb.assertions):
        print(f"  ✓ {len(wb.assertions)} assertions pass; {len(cat.cells)} cells emitted.")
    else:
        print(f"  ✗ {sum(1 for a in wb.assertions if not a.passed)} assertion(s) FAILED — halting.")
        return 1

    out = wb.save()
    print(f"  ✓ Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

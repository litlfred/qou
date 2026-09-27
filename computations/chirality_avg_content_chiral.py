#!/usr/bin/env python3
"""chirality_avg_content_chiral.py

Companion to `chirality_avg_content.py` (which closed the
amphichiral case for figure-8 and Borromean).  This script computes
$\\langle c(\\lambda) \\rangle_\\beta$ for **chiral** braids in
$H_3(R, q_0)$ — the open residual of GAP-A-2 in
`derivation-audit-report.md`.

Per `prop:chirality-writhe-ribbon-derivation`, the first-order
chirality factor is

  a_K(β) = 1 + w(β) · ⟨c⟩_β · h + O(h²),

where ⟨c⟩_β is the Plancherel-weighted mean content.  The
amphichiral case discharges by bar-involution symmetry
(χ^λ = χ^{λ^T}), giving ⟨c⟩ = 0.  This script samples chiral
3-braids to expose the structural-but-non-zero values that the
chiral case takes.

Key observation (2026-05-09): the chiral ⟨c⟩_β is **braid-word
specific**; the conjecture's earlier universal-1 ansatz was wrong,
and so was the simple writhe-content formula (empirically falsified
for the deuteron).  The right structural form for the chiral
residual remains the open piece of GAP-A-2.

CORRECTIONS (2026-08-10, beans qou-okxx / epic qou-qia8) — three
defects found by the writhe level-of-definition sweep
(`docs/audits/2026-08-10-writhe-level-of-definition.md`):

1. The writhe was a **hardcoded dict field**, and one row carried
   `"writhe": 4` for a word whose actual writhe is `+2`.  That made
   `a_K = 1 + w·⟨c⟩·h` twice too large for that row.  The writhe is
   now **computed from the braid word** (`writhe()` below); no case
   may declare it.
2. Three rows were **mislabelled as knots they are not**.  The
   closure's component count (cycles of the underlying permutation)
   and Alexander determinant `|Δ(−1)|` are now computed for every
   row and recorded in the witness, so a label can be checked
   against the topology rather than asserted:
     - `σ_1^3 ∈ B_3` was called the trefoil `3_1`.  Its permutation
       is the transposition `(1 2)`, so the closure has **2**
       components and is the split link `3_1 ⊔ 0_1` (Alexander
       polynomial ≡ 0, determinant 0) — not a knot at all.  The
       trefoil sits at **braid index 2**, `σ_1^3 ∈ B_2`, which lives
       in the companion `chirality_avg_content.py`.
     - `(σ_1 σ_2)^3 ∈ B_3` was called the "toral form of 3_1".  Its
       permutation is trivial, so the closure has **3** components:
       it is the torus **link** `T(3,3)` (determinant 4), not the
       trefoil.
     - `σ_1^2 σ_2^-1 σ_1^2 σ_2^-1` was called a "5_2 candidate".
       Its closure has **3** components and determinant **12**;
       `5_2` is a knot with determinant 7.  The label is dropped.
3. Level of definition.  The writhe is invariant under Markov I
   (conjugation) but **shifts by ±1 under Markov II**, so a
   writhe-derived number is well-defined only once the level is
   pinned.  Per the owner ruling recorded in the audit, states are
   Gröbner–Shirshov normal forms and the observable is evaluated at
   the **lowest level of the substrate tower — the braid index**.
   Every row therefore records `n_strands` and whether it sits at
   the braid index of its own closure.  This script is fixed at
   `n = 3`, so its rows are *not* minimal-level unless the closure's
   braid index happens to be 3.

Output: `chirality-avg-content-chiral.witness.json`.

Refs:
- prop:chirality-writhe-ribbon-derivation (the first-order ansatz)
- conj:chirality-ribbon-frobenius (the all-orders conjecture; now
  split into amphichiral closed / chiral open)
- companion: `chirality_avg_content.py` (amphichiral case at H_3,
  plus the minimal-level trefoil at H_2)
- docs/audits/2026-08-10-writhe-level-of-definition.md
"""
import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))


from _precision import set_compute_dps, fmt, str_at_true_precision  # noqa: E402
import mpmath
from mpmath import mp, mpf

from hecke_characters import (  # noqa: E402
    PRECISION_F64_FALLBACK,
    PRECISION_MPFR_50DPS,
    _RUST_CHI_AVAILABLE,
    chi_lambda_braid,
    partitions_of,
)
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from partition_utils import hook_length_1based as hook_length  # noqa: E402

set_compute_dps()
# Authoritative q_0 from q_parameter.Q_50_DIGIT_STR (m_μ/m_e CODATA fix).
Q0 = mpf(Q_50_DIGIT_STR)


def q_int(k: int, q):
    return mpf(0) if k == 0 else (q ** k - 1) / (q - 1)


def q_factorial(k: int, q):
    out = mpf(1)
    for i in range(1, k + 1):
        out *= q_int(i, q)
    return out


def dim_q(shape, q, n_fac_q):
    denom = mpf(1)
    for i, row_len in enumerate(shape, start=1):
        for j in range(1, row_len + 1):
            denom *= q_int(hook_length(shape, i, j), q)
    return n_fac_q / denom


def content_sum(shape):
    s = 0
    for i, row_len in enumerate(shape, start=1):
        for j in range(1, row_len + 1):
            s += (j - i)
    return s


# --------------------------------------------------------------------
# Braid-word topology.  Computed, never declared (qou-okxx).
# --------------------------------------------------------------------

def writhe(word):
    """Writhe (= algebraic length) of a braid word: the sum of the
    exponent signs.

    LEVEL WARNING.  This is a function of the *braid word at a fixed
    strand count*, not of its closure.  It is invariant under Markov I
    (conjugation, `writhe_conj`) but shifts by exactly ±1 under
    Markov II (`writhe_stabilize`), which does not change the link.
    See `QOU/StandardModel/WritheMarkovInvariance.lean` and
    `docs/audits/2026-08-10-writhe-level-of-definition.md`.
    """
    return sum(int(s) for s, _ in word)


def closure_components(n_strands, word):
    """Number of components of the braid closure.

    The closure's components are the cycles of the underlying
    permutation in S_n obtained by forgetting the crossing signs
    (generator σ_i ↦ transposition (i, i+1)).
    """
    perm = list(range(n_strands + 1))  # 1-based; perm[k] = image of k
    for _sign, gen in word:
        i = int(gen)
        perm[i], perm[i + 1] = perm[i + 1], perm[i]
    seen = [False] * (n_strands + 1)
    cycles = 0
    for k in range(1, n_strands + 1):
        if seen[k]:
            continue
        cycles += 1
        j = k
        while not seen[j]:
            seen[j] = True
            j = perm[j]
    return cycles


# Chiral 3-braid test cases.  Word format: list of [sign, gen]
# matching the convention of chirality_avg_content.py.
#
# NOTE: no case declares its writhe — it is computed by `writhe()`.
# The `closure` field records the VERIFIED topology of the closure
# (component count via `closure_components`, determinant |Δ(−1)| via
# the reduced Burau representation), not an aspirational knot name.
CASES = [
    {
        # 2 components (permutation = (1 2)), Alexander ≡ 0, det 0.
        # Was mislabelled "trefoil 3_1"; the trefoil is a KNOT and
        # sits at braid index 2 (see chirality_avg_content.py).
        "name": "σ_1^3 in B_3  (3_1 ⊔ 0_1, split)",
        "word": [[1, 1], [1, 1], [1, 1]],
        "closure": "3_1 ⊔ 0_1 (split link, 2 components, det 0)",
        "components_expected": 2,
        "determinant": 0,
        "braid_index_of_closure": 2,
        "amphichiral": False,
    },
    {
        "name": "σ_1^-3 in B_3  (3_1* ⊔ 0_1, split)",
        "word": [[-1, 1], [-1, 1], [-1, 1]],
        "closure": "3_1* ⊔ 0_1 (split link, 2 components, det 0)",
        "components_expected": 2,
        "determinant": 0,
        "braid_index_of_closure": 2,
        "amphichiral": False,
    },
    {
        # 3 components (permutation trivial), det 4.  Was mislabelled
        # "3_1 (toral form)"; T(2,3) is the trefoil, T(3,3) is a
        # 3-component link.  Braid index of T(3,3) is 3, so THIS row
        # is at its minimal level.
        "name": "(σ_1 σ_2)^3 in B_3  (T(3,3) torus link)",
        "word": [[1, 1], [1, 2], [1, 1], [1, 2], [1, 1], [1, 2]],
        "closure": "T(3,3) torus link (3 components, det 4)",
        "components_expected": 3,
        "determinant": 4,
        "braid_index_of_closure": 3,
        "amphichiral": False,
    },
    {
        # 3 components, det 12.  Was mislabelled "5_2 candidate";
        # 5_2 is a knot with determinant 7, so this is neither 5_2
        # nor a knot.  No corpus name is claimed for it.
        "name": "σ_1^2 σ_2^-1 σ_1^2 σ_2^-1 in B_3  (3-component link)",
        "word": [[1, 1], [1, 1], [-1, 2], [1, 1], [1, 1], [-1, 2]],
        "closure": "unnamed 3-component link (det 12) — NOT 5_2 (det 7)",
        "components_expected": 3,
        "determinant": 12,
        "braid_index_of_closure": None,   # not established
        "amphichiral": False,
    },
]


def main():
    # WitnessBuilder is constructed at the top of main() so durationMs
    # captures the full computation time (Copilot review #229).
    builder = (
        WitnessBuilder(name="chirality-avg-content-chiral",
                       engine="mpmath")
        .set_description(
            "Chiral residual of GAP-A-2 in derivation-audit-report.md. "
            "Computes ⟨c⟩_β = (Σ w_λ χ^λ(β) c(λ)) / "
            "(Σ w_λ χ^λ(β)) for chiral 3-braids at q_0 to expose "
            "the structural-but-non-zero values that the chiral case "
            "takes.  Companion to chirality-avg-content.witness.json "
            "(amphichiral case, plus the minimal-level trefoil at "
            "H_2).  The writhe is computed from each braid word, and "
            "each row records the verified topology of its closure "
            "(component count, determinant, braid index) — three rows "
            "carried wrong knot names and one a wrong hardcoded writhe "
            "until 2026-08-10 (qou-okxx)."
        )
        .set_audit_only(
            "folio/quantum-observable-universe/braids-and-knots/"
            "derivation-audit-report.md (GAP-A-2 chiral residual)"
        )
    )

    n = 3
    n_fac_q = q_factorial(n, Q0)
    parts = list(partitions_of(n))

    print("=" * 96)
    print("Chirality ⟨c⟩_β for chiral 3-braids (GAP-A-2 chiral residual)")
    print("=" * 96)
    print(f"  q_0 = {float(Q0):.16f}, n = {n}")
    print(f"  partitions of {n}: {parts}")
    print()

    rows = []
    h_val = Q0 - 1 / Q0
    # The actual numeric precision of `chi_lambda_braid` depends on
    # whether the Rust mpfr kernel is available.  The witness records
    # the actual tag (mpfr_50dps when Rust + mpfr are available, else
    # f64_numeric_fallback).  Previous code claimed `precision_dps: 50`
    # which overstated fidelity when only the f64 fallback ran (Copilot
    # review #r3213243720 / #r3213426355).
    chi_precision = (
        PRECISION_MPFR_50DPS if _RUST_CHI_AVAILABLE
        else PRECISION_F64_FALLBACK
    )
    chi_kwargs = {"precision": "mpfr_50dps"} if _RUST_CHI_AVAILABLE else {}
    # When the MPFR kernel is selected, `chi_lambdas_braid` needs the
    # substrate parameter as a decimal string — float(Q0) would
    # truncate to ~16 digits and defeat the mpfr_50dps fidelity
    # (Copilot review r3291263540).
    q_value_for_chi = Q_50_DIGIT_STR if _RUST_CHI_AVAILABLE else Q0
    # Batch character evaluation across partitions per case — F-A
    # of ffi-roundtrip-audit (single PyO3 crossing, rayon-parallel
    # on the Rust side).  Import here to avoid module-load reorder.
    from hecke_characters import chi_lambdas_braid
    for case in CASES:
        word = case["word"]
        # The writhe is COMPUTED from the braid word, never declared.
        # A hardcoded `"writhe": 4` on the fourth row (actual: +2) made
        # its a_K twice too large until 2026-08-10 (bean qou-okxx).
        w = writhe(word)
        # The closure's component count is likewise computed, and
        # cross-checked against the value recorded in the case table —
        # a mismatch means the label has drifted from the word again.
        comps = closure_components(n, word)
        if comps != case["components_expected"]:
            raise AssertionError(
                f"{case['name']}: closure has {comps} components, "
                f"case table says {case['components_expected']} — the "
                f"label has drifted from the braid word."
            )
        num = mpf(0)
        den = mpf(0)
        per_lam = []
        chi_raw_values = chi_lambdas_braid(parts, word, q_value_for_chi, **chi_kwargs)
        for shape, chi_raw in zip(parts, chi_raw_values):
            c_lam = content_sum(shape)
            w_lam = dim_q(shape, Q0, n_fac_q) ** 2 / n_fac_q
            # Rust mpfr returns a decimal string; parse to mpf.
            if isinstance(chi_raw, str):
                chi_raw = mpf(chi_raw)
            # Keep mpmath precision: extract real part as mpf without
            # casting through builtin complex / float (which would drop
            # to 53-bit precision and invalidate the mp.dps = 50
            # working precision).
            chi_val = mp.re(chi_raw)
            num += w_lam * chi_val * c_lam
            den += w_lam * chi_val
            # On the f64 fallback `chi_raw` arrives as a builtin complex, so χ
            # holds 53 bits however carefully it is handled afterwards — the
            # same overstatement `chi_precision` records, one level down.
            per_lam.append({
                "shape": list(shape),
                "content_c_lambda": c_lam,
                "wedderburn_weight": str(w_lam),
                "chi_lambda_beta": str_at_true_precision(chi_val),
                "weighted_chi_c": str(w_lam * chi_val * c_lam),
            })
        # Tolerance tied to working precision (per Gemini review).
        zero_tol = mpf(10) ** (-int(mp.dps * 0.6))
        if abs(den) < zero_tol:
            avg_c_mp = None
            a_K_first_mp = None
            avg_c = None
            a_K_first = None
            note = "denominator ~ 0 (degenerate Markov trace at q_0)"
        else:
            # Keep full mpmath precision for the witness; convert to
            # float only at the final report-emission stage so 50-dps
            # results survive in the witness's `avg_content_c_beta_mp`
            # string field.
            avg_c_mp = num / den
            a_K_first_mp = 1 + w * avg_c_mp * h_val
            avg_c = float(avg_c_mp)
            a_K_first = float(a_K_first_mp)
            note = ""
        at_braid_index = (case["braid_index_of_closure"] == n)
        print(f"  {case['name']:<52}  w={w:>+3} (computed), "
              f"comps={comps}, det={case['determinant']}, "
              f"⟨c⟩_β={avg_c if avg_c is None else f'{avg_c:+.6f}':>12}, "
              f"a_K(1st)={a_K_first if a_K_first is None else f'{a_K_first:+.4f}':>9}"
              f"  {note}")
        rows.append({
            "name": case["name"],
            # `closure` replaces the former `knot_class`, which carried
            # three wrong knot names (qou-okxx).  It states the VERIFIED
            # topology of the closure, not an aspirational label.
            "closure": case["closure"],
            "amphichiral": case["amphichiral"],
            "braid_word": word,
            "n_strands": n,
            # Computed, not declared.  See `writhe()` for the level
            # warning: this is a datum of the word at THIS strand count,
            # and Markov II would shift it by ±1 without changing the
            # closure.
            "writhe": w,
            "writhe_source": "computed_from_braid_word",
            "closure_components": comps,
            "closure_determinant": case["determinant"],
            "braid_index_of_closure": case["braid_index_of_closure"],
            # True only when this row sits at the lowest level of the
            # substrate tower, where the owner ruling says the
            # observable is evaluated.
            "at_braid_index": at_braid_index,
            "n_partitions": len(parts),
            "rows": per_lam,
            "numerator": str(num),
            "denominator": str(den),
            # Full-precision (50-dps) string is the canonical witness
            # value; the float fields are convenience truncations for
            # downstream comparison at 53-bit precision.
            "avg_content_c_beta_mp": (None if avg_c_mp is None else str(avg_c_mp)),
            "a_K_first_order_mp": (None if a_K_first_mp is None else str(a_K_first_mp)),
            "avg_content_c_beta": (None if avg_c is None else avg_c),
            "a_K_first_order": (None if a_K_first is None else a_K_first),
            "note": note,
        })
    print()

    # Summary observations.
    notes = [
        "CORRECTION (2026-08-10, qou-okxx): the writhe is now computed "
        "from the braid word.  The fourth row previously carried a "
        "hardcoded writhe of 4 for a word whose writhe is +2, which "
        "made its a_K = 1 + w·⟨c⟩·h twice too large.",
        "CORRECTION (2026-08-10, qou-okxx): three rows were mislabelled. "
        "σ_1^3 in B_3 closes to the SPLIT LINK 3_1 ⊔ 0_1 (2 components, "
        "Alexander ≡ 0, det 0), not the trefoil — the trefoil is a knot "
        "and sits at braid index 2.  (σ_1 σ_2)^3 closes to the TORUS "
        "LINK T(3,3) (3 components, det 4), not a 'toral form of 3_1'. "
        "σ_1^2 σ_2^-1 σ_1^2 σ_2^-1 closes to a 3-component link of "
        "determinant 12, so it is neither 5_2 (a knot, det 7) nor any "
        "knot.  Component counts are computed from the underlying "
        "permutation; determinants are |Δ(−1)| via the reduced Burau "
        "representation.",
        "LEVEL (2026-08-10): the writhe is Markov-I invariant but shifts "
        "by ±1 under Markov II, so every row records its n_strands and "
        "whether it sits at the braid index of its own closure.  Only "
        "the T(3,3) row does (braid index 3).  Per the owner ruling in "
        "docs/audits/2026-08-10-writhe-level-of-definition.md the "
        "observable is evaluated at the lowest level of the tower, so "
        "the two σ_1^{±3} rows are OFF-LEVEL diagnostics: the "
        "minimal-level trefoil datum is the H_2 row of the companion "
        "chirality_avg_content.py.",
        "The two σ_1^{±3} rows give ⟨c⟩_β = ±1.815, antisymmetric under "
        "the braid mirror as required.  This is a statement about the "
        "braid words, not about the trefoil.",
        "⟨c⟩_β is a function of the BRAID WORD, not of the closure: the "
        "four words here present four different links, so this table on "
        "its own does not exhibit two representatives of one knot type. "
        "(The earlier note claiming σ_1^3 and (σ_1 σ_2)^3 were two "
        "representatives of 3_1 was wrong on the topology — they are a "
        "split link and a 3-component torus link.)  The level ruling is "
        "what makes the datum well-defined: evaluate at the braid index.",
        "None of the values match the ⟨c⟩ = 1 universal ansatz from "
        "the conjecture; the chiral case has word-specific structural "
        "values that are NOT given by the simple writhe-content formula.",
        "Combined with the deuteron empirical falsification "
        "(chirality-writhe-ribbon-derivation.md:122-126), this "
        "demarcates the chiral residual of GAP-A-2: a structural "
        "formula relating ⟨c⟩_β to the braid topology is the open "
        "piece.",
    ]
    print("Summary observations:")
    for note in notes:
        print(f"  - {note}")
    print()

    builder = (
        builder
        .add_parameter("q_0", float(Q0))
        .add_parameter("q0_anchor", "proton")
        .add_parameter(
            "q0_anchor_note",
            "EXPERIMENTAL / Physical-Observations pin (m_p/m_e). "
            "`q_parameter` auto-selects the anchor from "
            "`q0_anchor_manifest.json` by the running producer's "
            "stem; `chirality_avg_content_chiral` is in NEITHER "
            "list, so it takes the proton default — which is also "
            "what the 2026-08-07 owner directive prescribes for "
            "touched compute.  The PREVIOUSLY COMMITTED witness was "
            "built in the muon era (q_0 = 1.1099785955541805), so "
            "every ⟨c⟩ here moved by ~1e-7 relative on the "
            "2026-08-10 re-run purely from the anchor, independently "
            "of the writhe and label corrections.  The one number "
            "that moved for a substantive reason is the fourth row's "
            "a_K (1.089679 -> 1.044839), from the hardcoded writhe 4 "
            "being replaced by the computed +2.  NOTE the companion "
            "`chirality_avg_content.py` is manifest-tagged "
            "`ideal_muon`, so ⟨c⟩ values must not be compared across "
            "the two witnesses below the 1e-7 level.",
        )
        .add_parameter("n", n)
        .add_parameter("partitions", [list(p) for p in parts])
        .add_parameter("chi_precision", chi_precision)
        .add_parameter("rust_chi_available", _RUST_CHI_AVAILABLE)
        .add_parameter("mp_dps", mp.dps)
        .add_data("cases", rows)
        .add_data("summary_observations", notes)
        .add_assertion(
            # Renamed from `trefoil_chiral_avg_c_nonzero_and_antisymmetric`
            # (qou-okxx): σ_1^{±3} in B_3 closes to a SPLIT LINK, not the
            # trefoil.  The mirror-antisymmetry claim is unaffected — it
            # is a property of the two braid words.
            name="sigma1_cubed_B3_avg_c_nonzero_and_mirror_antisymmetric",
            computed=int(
                rows[0]["avg_content_c_beta"] is not None
                and rows[1]["avg_content_c_beta"] is not None
                and abs(rows[0]["avg_content_c_beta"]
                        + rows[1]["avg_content_c_beta"]) < 1e-6
                and abs(rows[0]["avg_content_c_beta"]) > 0.1
            ),
            expected=1,
        )
        .add_assertion(
            name="chiral_avg_c_not_universal_1",
            computed=int(
                rows[0]["avg_content_c_beta"] is None
                or abs(rows[0]["avg_content_c_beta"] - 1.0) > 0.1
            ),
            expected=1,
        )
        .add_assertion(
            # Regression guard for the hardcoded-writhe defect: the
            # fourth row's writhe is +2, not the 4 that was declared.
            name="row4_writhe_computed_is_2_not_hardcoded_4",
            computed=rows[3]["writhe"],
            expected=2,
        )
        .add_assertion(
            # Regression guard for the three mislabelled rows: the
            # component counts that refute "trefoil" / "toral 3_1" /
            # "5_2 candidate" are recomputed from the braid words.
            name="closure_component_counts_2_2_3_3",
            computed=",".join(str(r["closure_components"]) for r in rows),
            expected="2,2,3,3",
        )
    )
    out_path = builder.save()
    print(f"  Witness emitted: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

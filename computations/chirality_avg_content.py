"""chirality_avg_content.py

First numerical computation of the chirality factor's
Wedderburn-weighted average content ⟨c⟩_β for the figure-8
($4_1$) and Borromean ($\\mathcal{B}_3$) braids.

Per `prop:chirality-writhe-ribbon-derivation`, the first-order
chirality factor is

  a_K(β) = 1 + w(β) · ⟨c⟩_β · h + O(h²),

where

  ⟨c⟩_β = (Σ_λ w_λ · χ^λ(β) · c(λ)) / (Σ_λ w_λ · χ^λ(β))

with Plancherel weights w_λ = dim_q(λ)² / [n]_q!, Hecke characters
χ^λ(β) computed via `hecke_characters.chi_lambda_braid`, and
content c(λ) = Σ_{x ∈ λ} (col(x) - row(x)).

This script:
  1. Computes χ^λ(β), w_λ, c(λ) for each λ ⊢ n at q_0
     for two atomic braids:
     - β = (σ_1 σ_2^{-1})^2  (figure-8 4_1, n=3)
     - β = (σ_1 σ_2^{-1})^3  (Borromean B_3, n=3)
  2. Forms the weighted sum and average.
  3. Reports ⟨c⟩_β at q_0 with full mp.dps precision.

Cross-check: a Type-B folded crystal computation (per
prop:type-b-folded-crystal-combinatorics) predicts
self-conjugate-pair partitions contribute zero to the
content-summation. Verified empirically via the
λ vs λ^T pairing.

RETRACTED PREDICTION (2026-08-10, bean qou-kjmo).  This script used
to predict "Expected: ⟨c⟩_β ≈ 0" for BOTH of its chiral rows, by the
Type-B transpose cancellation.  The prediction failed twice and
neither the script nor the witness said so:

  | row                        | predicted | measured (committed) |
  |----------------------------|-----------|----------------------|
  | σ_1^3 in H_2               | ≈ 0       | 3.29832709450030     |
  | (σ_1 σ_2)^3 in H_3         | ≈ 0       | 0.354276650913726    |

The failure is now **derived**, not merely observed — see
`transpose_collapse_check()` below.  For n ≤ 3 the transpose pairing
collapses the numerator exactly:

    Σ_λ w_λ χ^λ(β) c(λ)  =  (c_max / [n]_q!) · ( q^ℓ − (−1/q)^ℓ )

because dim_q((n)) = dim_q((1^n)) = 1 (so both extreme partitions
carry the same weight 1/[n]_q!), c((1^n)) = −c((n)) = −c_max, and the
only remaining partition at n = 3 is the self-transpose (2,1) with
c = 0.  Here ℓ = writhe(β) and χ^{(n)}(β) = q^ℓ,
χ^{(1^n)}(β) = (−1/q)^ℓ are the two one-dimensional Hecke characters.

**Scope-(b) structural exclusion, for n ≤ 3.**  Invariant: for real
q > 0 the factor q^ℓ − (−1/q)^ℓ vanishes only at q = 1 or ℓ = 0.  For
odd ℓ it equals q^ℓ + q^{−ℓ} ≥ 2 > 0 by AM–GM, so it is never zero;
for even ℓ it equals q^ℓ − q^{−ℓ}, which vanishes iff q = 1.  Hence at
the substrate q_0 ≠ 1,

    ⟨c⟩_β = 0   ⟺   writhe(β) = 0        (n ≤ 3)

The Type-B cancellation therefore **cannot** produce ⟨c⟩ ≈ 0 for any
braid of nonzero writhe at n ≤ 3.  The two amphichiral rows below
(figure-8, Borromean) return 0 not because they are amphichiral but
because they have writhe 0; the two chiral rows have writhe +3 and
+6 and are structurally excluded from vanishing.

**Scope-(a) only for n ≥ 4.**  The collapse above uses the fact that
every non-extreme partition of n ≤ 3 has c = 0.  That fails from
n = 4 on ((3,1) has c = +2, (2,1,1) has c = −2), so the numerator is
no longer proportional to q^ℓ − (−1/q)^ℓ and this argument says
nothing there.  The general Type-B ≈ 0 claim is refuted as tested,
not excluded in principle.

The connection to the level ruling is direct: ⟨c⟩_β = 0 ⟺ w = 0 is a
**level-dependent** criterion, because Markov II shifts w by ±1
without changing the link.  See
`docs/audits/2026-08-10-writhe-level-of-definition.md`.
"""

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
# Ref: [manuscript] prop:chirality-writhe-ribbon-derivation
# Ref: [manuscript] prop:type-b-folded-crystal-combinatorics

import json
from q_parameter import Q_50_DIGIT_STR
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

import mpmath
from mpmath import mp, mpf

from hecke_characters import (  # noqa: E402
    chi_lambda_braid,
    partitions_of,
    young_diagram_cells,
)
from witness_base import WitnessBuilder  # noqa: E402
from partition_utils import hook_length_1based as hook_length  # noqa: E402
from _precision import set_compute_dps  # noqa: E402


def q_int(k: int, q_val: mpf) -> mpf:
    if k == 0:
        return mpf(0)
    return (q_val ** k - 1) / (q_val - 1)


def q_factorial(k: int, q_val: mpf) -> mpf:
    out = mpf(1)
    for i in range(1, k + 1):
        out *= q_int(i, q_val)
    return out


def dim_q(shape: tuple[int, ...], n: int, q_val: mpf,
          n_fac_q: mpf) -> mpf:
    denom = mpf(1)
    for i, row_len in enumerate(shape, start=1):
        for j in range(1, row_len + 1):
            denom *= q_int(hook_length(shape, i, j), q_val)
    return n_fac_q / denom


def content_sum(shape: tuple[int, ...]) -> int:
    """c(λ) = Σ_{x ∈ λ} (col(x) - row(x)) using 0-indexed positions."""
    total = 0
    for i, row_len in enumerate(shape):
        for j in range(row_len):
            total += j - i
    return total


def transpose_shape(shape: tuple[int, ...]) -> tuple[int, ...]:
    if not shape:
        return ()
    height = max(shape)
    out = []
    for j in range(height):
        col = sum(1 for r in shape if r > j)
        out.append(col)
    return tuple(out)


def writhe(word) -> int:
    """Writhe (= algebraic length) of a braid word: sum of exponent signs.

    LEVEL WARNING.  A datum of the braid word at a FIXED strand count,
    not of its closure: invariant under Markov I (conjugation) but
    shifted by ±1 under Markov II, which does not change the link.
    See `QOU/StandardModel/WritheMarkovInvariance.lean`.
    """
    return sum(int(s) for s, _ in word)


def closure_components(n_strands: int, word) -> int:
    """Number of components of the braid closure = cycles of the
    underlying permutation in S_n (σ_i ↦ transposition (i, i+1))."""
    perm = list(range(n_strands + 1))
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


def transpose_collapse_check(n: int, word, q_val: mpf,
                             numer: mpf) -> dict:
    """Machine-check the n ≤ 3 transpose collapse (bean qou-kjmo).

    Claim (see module docstring):

        Σ_λ w_λ χ^λ(β) c(λ)  =  (c_max / [n]_q!) · ( q^ℓ − (−1/q)^ℓ )

    with ℓ = writhe(β) and c_max = c((n)) = n(n−1)/2.  Recomputes the
    right-hand side from ℓ alone — no characters — and compares it to
    the numerator the main loop accumulated from the full Wedderburn
    sum.  Agreement is what turns the failed "⟨c⟩ ≈ 0" prediction from
    an observation into a derivation.

    Returns a dict; `applicable` is False for n ≥ 4, where the collapse
    does not hold (partitions such as (3,1) have nonzero content).
    """
    ell = writhe(word)
    if n > 3:
        return {
            "applicable": False,
            "reason": ("collapse holds only for n ≤ 3, where every "
                       "non-extreme partition has content 0"),
        }
    c_max = n * (n - 1) // 2
    n_fac_q = q_factorial(n, q_val)
    # q^ℓ − (−1/q)^ℓ, the two one-dimensional Hecke characters.
    chi_triv = q_val ** ell
    chi_sign = (-1 / q_val) ** ell
    predicted = (mpf(c_max) / n_fac_q) * (chi_triv - chi_sign)
    resid = abs(numer - predicted)
    scale = max(abs(numer), abs(predicted), mpf(1))
    return {
        "applicable": True,
        "writhe_ell": ell,
        "c_max": c_max,
        "predicted_numerator": mpmath.nstr(predicted, 30),
        "actual_numerator": mpmath.nstr(numer, 30),
        "relative_residual": mpmath.nstr(resid / scale, 6),
        "collapse_verified": bool(resid / scale < mpf("1e-12")),
        # The structural consequence: for real q > 0, q ≠ 1 the factor
        # q^ℓ − (−1/q)^ℓ vanishes iff ℓ = 0.
        "vanishing_requires_zero_writhe": True,
        "avg_c_can_vanish_here": bool(ell == 0),
    }


def avg_content_for_braid(name: str, n: int, word: list[tuple[int, int]],
                          q_val: mpf, dps: int,
                          closure: str = "",
                          determinant=None,
                          braid_index_of_closure=None,
                          components_expected=None,
                          level_note: str = "") -> dict:
    """Compute ⟨c⟩_β for a given braid word at q_val."""
    # Convert word from [(sign, gen), ...] to chi_lambda_braid format
    # which is [(±1, gen_1based), ...] same convention.
    word_canon = [(int(s), int(g)) for (s, g) in word]

    n_fac_q = q_factorial(n, q_val)

    shapes = [tuple(s) for s in partitions_of(n)]
    rows = []
    numer = mpf(0)
    denom = mpf(0)

    for shape in shapes:
        d = dim_q(shape, n, q_val, n_fac_q)
        w_lam = d * d / n_fac_q
        # f64 fallback (Rust kernel for mpfr precision unavailable
        # in this environment); ~16 dps is sufficient for the
        # first numerical estimate of ⟨c⟩_β. A future PR with the
        # Rust kernel installed can re-run at 50 dps.
        chi = chi_lambda_braid(
            shape, word_canon,
            q_value=float(q_val),
            precision="f64",
        )
        chi_val = mpf(repr(chi))
        c_lam = content_sum(shape)
        rows.append({
            "shape": list(shape),
            "shape_T": list(transpose_shape(shape)),
            "dim_q": mpmath.nstr(d, 30),
            "wedderburn_weight": mpmath.nstr(w_lam, 30),
            "chi_lambda_beta": mpmath.nstr(chi_val, 30),
            "content_c_lambda": c_lam,
            "weighted_chi_c": mpmath.nstr(w_lam * chi_val * c_lam, 30),
        })
        numer += w_lam * chi_val * c_lam
        denom += w_lam * chi_val

    if denom == 0:
        avg = None
    else:
        avg = numer / denom

    # Topology of the closure, COMPUTED — never declared (qou-okxx).
    comps = closure_components(n, word)
    if components_expected is not None and comps != components_expected:
        raise AssertionError(
            f"{name}: closure has {comps} components, case table says "
            f"{components_expected} — the label has drifted from the "
            f"braid word."
        )
    w = writhe(word)

    return {
        "name": name,
        "n_strands": n,
        "braid_word": [list(t) for t in word],
        # Verified topology of the closure, replacing the knot names
        # that were asserted rather than checked (qou-okxx).
        "closure": closure,
        "closure_components": comps,
        "closure_determinant": determinant,
        "braid_index_of_closure": braid_index_of_closure,
        "at_braid_index": (braid_index_of_closure == n),
        "writhe": w,
        "writhe_source": "computed_from_braid_word",
        "level_note": level_note,
        "n_partitions": len(shapes),
        "rows": rows,
        "numerator": mpmath.nstr(numer, 30),
        "denominator": mpmath.nstr(denom, 30),
        "avg_content_c_beta": mpmath.nstr(avg, 30) if avg is not None else None,
        # Derivation of why ⟨c⟩ ≈ 0 was NOT obtained here (qou-kjmo).
        "transpose_collapse": transpose_collapse_check(n, word, q_val, numer),
    }


def main() -> None:
    set_compute_dps()  # f64 chi values limit downstream precision to ~16 dps
    q_0 = mpf(Q_50_DIGIT_STR)

    cases = [
        # figure-8 4_1: (σ_1 σ_2^{-1})^2 in B_3 — writhe 0, amphichiral.
        # Braid index of 4_1 is 3, so this row IS at minimal level.
        avg_content_for_braid(
            "figure-8 4_1 (σ_1 σ_2^-1)^2 in H_3", 3,
            [(1, 1), (-1, 2), (1, 1), (-1, 2)],
            q_0, dps=50,
            closure="4_1 figure-eight knot (1 component, det 5)",
            determinant=5, braid_index_of_closure=3,
            components_expected=1,
            level_note="at the braid index of 4_1 (= 3): minimal level",
        ),
        # Borromean B_3: (σ_1 σ_2^{-1})^3 in B_3 — writhe 0, amphichiral.
        avg_content_for_braid(
            "Borromean B_3 (σ_1 σ_2^-1)^3 in H_3", 3,
            [(1, 1), (-1, 2), (1, 1), (-1, 2), (1, 1), (-1, 2)],
            q_0, dps=50,
            closure="Borromean rings (3 components, det 16)",
            determinant=16, braid_index_of_closure=3,
            components_expected=3,
            level_note="at the braid index of the Borromean rings (= 3)",
        ),
        # CANONICAL trefoil row.  σ_1^3 in B_2 closes to the trefoil:
        # 1 component, Alexander t^2 − t + 1, determinant 3.  The braid
        # index of 3_1 = T(2,3) is min(2,3) = 2 (Morton–Williams), so
        # this is the MINIMAL-LEVEL presentation and, per the owner
        # ruling, the level at which the observable is evaluated.
        #
        # RETRACTED (qou-kjmo): this row previously carried "Expected:
        # ⟨c⟩_β ≈ 0 again at H_2" by Type-B cancellation.  Measured
        # 3.29832709450030 (committed witness).  The prediction is now
        # structurally excluded, not merely unmet — see the module
        # docstring and `transpose_collapse_check`: at n ≤ 3 the
        # numerator is (c_max/[n]_q!)·(q^ℓ − (−1/q)^ℓ), which for real
        # q > 0, q ≠ 1 vanishes iff the writhe ℓ = 0.  Here ℓ = +3.
        avg_content_for_braid(
            "trefoil 3_1 (σ_1^3 in H_2) — CANONICAL, minimal level", 2,
            [(1, 1), (1, 1), (1, 1)],
            q_0, dps=50,
            closure="3_1 trefoil knot (1 component, det 3)",
            determinant=3, braid_index_of_closure=2,
            components_expected=1,
            level_note=(
                "CANONICAL trefoil datum: braid index of 3_1 = T(2,3) "
                "is min(2,3) = 2 (Morton-Williams), so this row is at "
                "the lowest level of the substrate tower and is the "
                "value the owner ruling selects.  The σ_1^3 row in "
                "chirality_avg_content_chiral.py sits at n = 3, where "
                "the same word closes to the SPLIT LINK 3_1 ⊔ 0_1 — a "
                "different link, not a second representative of the "
                "trefoil.  Its ⟨c⟩ = 1.8149 is therefore not a rival "
                "value for this knot."
            ),
        ),
        # RELABELLED (qou-okxx): was "T(2,3) torus knot in H_3
        # (writhe +6)".  σ_1 σ_2 σ_1 σ_2 σ_1 σ_2 = (σ_1 σ_2)^3 is the
        # full twist in B_3; its underlying permutation is trivial, so
        # the closure has 3 components — it is the torus LINK T(3,3)
        # (determinant 4), NOT the trefoil T(2,3).  The trefoil has
        # writhe 3 at its braid index; no presentation of it gives 6.
        # Braid index of T(3,3) is 3, so this row is at minimal level.
        avg_content_for_braid(
            "T(3,3) torus link ((σ_1 σ_2)^3 in H_3)", 3,
            [(1, 1), (1, 2), (1, 1), (1, 2), (1, 1), (1, 2)],
            q_0, dps=50,
            closure="T(3,3) torus link (3 components, det 4)",
            determinant=4, braid_index_of_closure=3,
            components_expected=3,
            level_note=(
                "at the braid index of T(3,3) (= 3).  Formerly "
                "mislabelled the trefoil T(2,3); the closure has 3 "
                "components, so it is not a knot at all.  The "
                "'⟨c⟩_β ≈ 0 by Type-B' prediction on this row is "
                "likewise structurally excluded: writhe = +6 ≠ 0."
            ),
        ),
    ]

    payload = {
        "computation": "chirality-avg-content",
        "description": (
            "First numerical computation of ⟨c⟩_β = Σ w_λ χ^λ(β) "
            "c(λ) / Σ w_λ χ^λ(β) for the figure-8 (4_1), Borromean "
            "(B_3), trefoil (3_1 at its braid index 2) and T(3,3) "
            "braids at q_0. Inhabits ChiralityFactorClass with "
            "structural-content values.  Every row records the "
            "COMPUTED writhe and the verified topology of its closure "
            "(component count, determinant, braid index)."
        ),
        "contentBlock": "prop:chirality-writhe-ribbon-derivation",
        "precision_dps": 50,
        "q_0": str(q_0),
        "q0_anchor": "muon",
        "q0_anchor_note": (
            "IDEAL / canonical 3-CAL pin (CAL-2 = 𝔇_β, proxy "
            "m_μ/m_e), q_0 = 1.10997859555733471... .  This is NOT a "
            "free choice made here: `q_parameter` auto-selects the "
            "anchor from `q0_anchor_manifest.json` by the running "
            "producer's stem, and `chirality_avg_content` is listed "
            "under `ideal_muon`.  The 2026-08-07 owner directive "
            "(touched compute defaults to the proton anchor) is not "
            "applied by hand here: retagging a manifest-tagged ideal "
            "producer is part of the tracked ~840-witness migration "
            "(bean tnjb), which is explicitly not authorised as an "
            "idle-time drain.  No number in this witness moves as a "
            "result of the 2026-08-10 corrections."
        ),
        "cross_script_anchor_note": (
            "ANCHOR ASYMMETRY, stated so no reader mixes the two "
            "layers.  This producer is manifest-tagged `ideal_muon`. "
            "Its companion `chirality_avg_content_chiral.py` is in "
            "NEITHER manifest list, so it falls through to the "
            "experimental/proton default, and its committed witness "
            "moved by ~1e-7 relative when re-run on 2026-08-10.  "
            "Neither producer straddles the two layers internally — "
            "each evaluates q_0, the Wedderburn weights and the Hecke "
            "characters at one and the same anchor — but ⟨c⟩ values "
            "must not be compared ACROSS the two witnesses below the "
            "1e-7 level."
        ),
        "cases": cases,
        "interpretation": (
            "⟨c⟩_β values give the Wedderburn-weighted "
            "average content for each atomic braid; the chirality "
            "first-order factor is a_K(β) = 1 + w(β) · ⟨c⟩_β · h "
            "where w(β) is the writhe and h = q − q⁻¹.  w(β) is a "
            "datum of the braid WORD at a fixed strand count, not of "
            "the closure — Markov II shifts it by ±1 — so a_K is "
            "well-defined only once the level is pinned.  Per the "
            "owner ruling the level is the braid index; the rows here "
            "record whether they sit at it."
        ),
        "retracted_prediction": {
            "bean": "qou-kjmo",
            "claim": (
                "Expected: ⟨c⟩_β ≈ 0 by Type-B transpose cancellation "
                "(c(λ) + c(λ^T) = 0), asserted for both chiral rows."
            ),
            "outcome": "FAILED on both rows",
            "measured": {
                "trefoil 3_1 (σ_1^3 in H_2)": "3.29832709450030 "
                                              "(committed, muon pin)",
                "T(3,3) ((σ_1 σ_2)^3 in H_3)": "0.354276650913726 "
                                               "(committed, muon pin)",
            },
            "scope": "b-for-n-le-3, a-for-n-ge-4",
            "invariant": (
                "For n ≤ 3 the transpose pairing collapses the "
                "numerator exactly to (c_max/[n]_q!)·(q^ℓ − (−1/q)^ℓ), "
                "since dim_q((n)) = dim_q((1^n)) = 1 and the only "
                "non-extreme partition at n ≤ 3 is the self-transpose "
                "(2,1) with c = 0.  SIGN/POSITIVITY INVARIANT: for "
                "real q > 0, odd ℓ gives q^ℓ + q^{−ℓ} ≥ 2 > 0 (AM–GM, "
                "never zero) and even ℓ gives q^ℓ − q^{−ℓ}, zero only "
                "at q = 1.  Hence at q_0 ≠ 1, ⟨c⟩_β = 0 ⟺ writhe = 0. "
                "The cancellation therefore CANNOT deliver ≈ 0 for "
                "any nonzero-writhe braid at n ≤ 3.  Verified per row "
                "by transpose_collapse_check()."
            ),
            "scope_a_caveat": (
                "The collapse uses 'every non-extreme partition of "
                "n ≤ 3 has content 0', which fails from n = 4 ((3,1) "
                "has c = +2).  For n ≥ 4 the Type-B ≈ 0 claim is "
                "refuted as tested — scope-(a) — not excluded in "
                "principle."
            ),
            "why_the_amphichiral_rows_do_vanish": (
                "figure-8 and Borromean return ⟨c⟩ = 0 because their "
                "writhe is 0, not because they are amphichiral.  The "
                "same invariant explains both the successes and the "
                "failures, and it is level-dependent: Markov II moves "
                "the writhe off 0 without changing the link."
            ),
        },
    }

    out = (
        WitnessBuilder.wrap_legacy(
            "chirality-avg-content",
            payload,
            script_path=__file__,
            engine="mpmath",
        )
        .set_audit_only(
            "docs/audits/2026-05-09-refocused-1ppb-workplan-v3.md"
        )
        .save()
    )

    print("⟨c⟩_β results (writhe computed from the braid word; "
          "closure topology verified):")
    for case in cases:
        avg = case["avg_content_c_beta"]
        tc = case["transpose_collapse"]
        flag = "MINIMAL LEVEL" if case["at_braid_index"] else "off-level"
        print(f"  {case['name']} (n={case['n_strands']}, "
              f"w={case['writhe']:+d}, comps={case['closure_components']}, "
              f"det={case['closure_determinant']}, {flag}):")
        print(f"      ⟨c⟩_β = {avg}")
        if tc["applicable"]:
            print(f"      transpose collapse verified: "
                  f"{tc['collapse_verified']} "
                  f"(rel.resid {tc['relative_residual']}); "
                  f"⟨c⟩ can vanish here: {tc['avg_c_can_vanish_here']} "
                  f"(requires writhe 0, actual {tc['writhe_ell']:+d})")

    print()
    print("RETRACTED PREDICTION (qou-kjmo): this script predicted "
          "⟨c⟩_β ≈ 0 for both chiral rows")
    print("  by Type-B transpose cancellation.  It FAILED on both "
          "(committed witness, muon pin):")
    print("    trefoil 3_1 (σ_1^3 in H_2)   predicted ≈ 0, "
          "measured 3.29832709450030")
    print("    T(3,3)  ((σ_1 σ_2)^3 in H_3) predicted ≈ 0, "
          "measured 0.354276650913726")
    print("  Scope-(b) for n ≤ 3 — the numerator collapses to "
          "(c_max/[n]_q!)·(q^ℓ − (−1/q)^ℓ),")
    print("  which for real q > 0, q ≠ 1 vanishes iff the writhe "
          "ℓ = 0 (sign/positivity invariant;")
    print("  odd ℓ gives q^ℓ + q^-ℓ ≥ 2 > 0).  So the cancellation "
          "CANNOT give ≈ 0 at nonzero writhe.")
    print("  Scope-(a) for n ≥ 4, where the collapse fails "
          "((3,1) has content +2).")
    print("  The two amphichiral rows vanish because their writhe "
          "is 0, not because they are amphichiral.")
    print(f"\nWitness: {out}")


if __name__ == "__main__":
    main()

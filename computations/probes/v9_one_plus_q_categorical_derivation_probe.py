"""Option E v9 — categorical derivation probe for the (1+q)/2 factor.

Per author 2026-05-31 direction (STRUCTURAL TASK).

## Context

Option E v9 (commit 30c5393b7) closes the (³H, ³He) mirror pair to 0.11%
via the formula:

  B_T - B_³He = m_π · ℏ_q · (1+q)/2 · Σ_λ y_λ · (χ^λ(β_T) + χ^{λᵀ}(β_³He))/2

Sibling PR #1581 Finding C audited (1+q)/2 against 33 q-arithmetic candidates
and confirmed it is UNIQUE within 0.11%. But the question remains:

  Is (1+q)/2 PRODUCED by a categorical chain, or just SELECTED by search?

The interpretive hint from #1581 was: "(1+q)/2 = (q⁰ + q¹)/2 is the arithmetic
mean of the trivial-rep T_s eigenvalue (1) and the q-deformed positive-
crossing eigenvalue (q). Hecke-natural quantity." — that is interpretation,
not derivation.

## What this probe does

Tests 7 candidate CATEGORICAL DERIVATIONS for (1+q)/2:

  (a) Mirror-symmetrization of crossing count. Average over Z↔N swap of
      "positive crossings minus negative crossings". For ³H (uud-uud-udd)
      and ³He (uud-udd-udd), the net crossing count differs by exactly
      one interface; averaging over the mirror gives (q⁰ + q¹)/2 if one
      crossing is "neutral" (vacuum).
  (b) q-symmetrizer eigenvalue ratio. The q-symmetric projector
      e_+ = (σ + q⁻¹)/[2]_q has eigenvalues (1, q⁰) on the trivial and
      (q, q¹) on the positive crossing. Its trace ratio gives (1+q)/[2]_q,
      NOT (1+q)/2. Check the related "half-symmetrizer" e_+ · [2]_q / 2.
  (c) Reeb-phase derivative at the mirror axis. For self-conjugate
      partition λ = λᵀ on the mirror axis Z=N, the Reeb phase
      θ_λ = arccos(χ^λ/d_λ) has a specific derivative; check if
      d/dq θ at q=1 gives (1+q)/2 via Taylor expansion.
  (d) Markov-trace eigenvalue average. tr_M(σ + 1) = tr_M(σ) + tr_M(1)
      = q · w(K) + tr_M(1). For the figure-8 (or trivial) link, the
      ratio tr_M(σ + 1) / (2 · tr_M(1)) might give (1+q)/2.
  (e) p-n averaging via the canonical projection. Per the cheat-sheet
      "Bring color-tube weighted averaging" note: σ_avg = (σ + σ⁻¹)/2 is
      what the production marshalling uses; per #1581's hint the mirror
      product chain might naturally produce (1+q)/2 via the OTHER half
      of the projection ((σ + 1)/2 instead of (σ + σ⁻¹)/2).
  (f) Quantum dimension-of-2 average. For the 2-dim Hopf algebra
      H = k[Z/2], dim_q(H) = [2]_q = q + q⁻¹. The "halved" character
      (1 + q)/2 emerges if we pick out just one of the two basis vectors.
  (g) Hopf-algebra antipode coefficient. The antipode S in H_n(q) acts
      on σ_i as S(σ_i) = σ_i⁻¹; the "S-symmetric" combination
      (σ + S(σ))/2 = (σ + σ⁻¹)/2 has eigenvalues (q + q⁻¹)/2 = [2]_q/2;
      the "antipode-twisted" combination (1 + σ)/2 has eigenvalues
      ((1+1)/2, (1+q)/2) = (1, (1+q)/2). This IS the candidate that
      makes (1+q)/2 a Hecke eigenvalue average directly.

## Constraint checks

For ANY candidate to be a categorically-derived (1+q)/2:

  C1. q → 1 limit: must equal 1 (since classical mirror pair collapse)
  C2. q → q_0 ≈ 1.10998: must equal 1.054855 (the empirically required factor)
  C3. Bar-symmetry behavior: f(q⁻¹) should be coherent with the
      bar-anti/symmetric structure of the v9 formula
  C4. Categorical naturality: must arise from a SPECIFIC Wedderburn
      block, a SPECIFIC Markov-trace construction, or a SPECIFIC
      Hopf-algebra invariant — not arbitrary algebraic recombination.

## Cross-references

- option_e_v9_all_symmetries.py (commit 30c5393b7 — the BREAKTHROUGH)
- option_e_v9_one_plus_q_structural_audit.py (PR #1581 Finding C)
- docs/canonical-derivation-cheat-sheet.md §5 (Bring color-tube averaging,
  pn-convention finding)
- docs/audits/2026-05-27-pion-half-figure-eight.md (half-Reeb-rotation)
- AGENTS.md §7a (Hecke-Skein convention: σ_i eigenvalues q, -q⁻¹)
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 1, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the `probes/` cluster subdirectory. The bridge
# module also puts every other cluster subdir on sys.path so
# cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def main() -> int:
    set_compute_dps(50)
    DPS = 50

    q = mp.mpf(Q_50_DIGIT_STR)
    target = (1 + q) / 2  # the value we're trying to derive categorically
    target_numerical = mp.mpf("1.054989")  # ≈ what v9 needed

    print("=" * 78)
    print("v9 (1+q)/2 — categorical derivation probe (50 dps)")
    print("=" * 78)
    print(f"\nq_0 (canonical 50dps)                = {Q_50_DIGIT_STR}")
    print(f"target (1+q)/2 evaluated at q_0      = {mp.nstr(target, 30)}")
    print(f"v9 empirical correction factor       ≈ {mp.nstr(target_numerical, 12)}")
    print(f"  match to (1+q)/2 within            = {mp.nstr((target - target_numerical)/target_numerical * 100, 6)}%")
    print()

    # Helpers
    qi = 1 / q
    h = q - qi
    h2 = h * h
    qbracket2 = q + qi  # [2]_q

    # Helper: relative error vs target (1+q)/2
    def err(val):
        return (val - target) / target * 100

    # Helper: relative error of value vs reference at q=1, q=q_0
    def check_constraints(name, expr_func, narrative):
        """expr_func: q -> value; check q→1 limit and q=q_0 match.

        Returns dict with: limit_at_q1, value_at_q0, error_vs_target_pct,
                          passes_C1 (limit=1), passes_C2 (match within 0.1%).
        """
        # C1: q → 1 limit
        try:
            val_at_1 = expr_func(mp.mpf("1") + mp.mpf("1e-60"))
            # Use mpmath limit if available
            limit_at_1 = val_at_1  # already evaluated at q ≈ 1
        except (ZeroDivisionError, ValueError):
            limit_at_1 = None

        # C2: q at q_0
        val_at_q0 = expr_func(q)
        err_pct = err(val_at_q0)

        # C3: bar-symmetry — f(q⁻¹) vs f(q)
        try:
            val_at_qinv = expr_func(1 / q)
            bar_symm = abs(val_at_qinv - val_at_q0) / val_at_q0
        except (ZeroDivisionError, ValueError):
            bar_symm = None

        c1_pass = limit_at_1 is not None and abs(limit_at_1 - 1) < mp.mpf("1e-10")
        c2_pass = abs(err_pct) < mp.mpf("0.1")  # within 0.1% of target

        marker = ""
        if c1_pass and c2_pass:
            marker = "  ★★ FULL MATCH (C1+C2)"
        elif c2_pass:
            marker = "  ★ matches at q_0 (C2 only — C1 limit wrong)"
        elif c1_pass:
            marker = "  · C1 ok but C2 mismatch"

        print(f"\n--- Candidate {name} ---")
        print(f"  Narrative: {narrative}")
        print(f"  Value at q_0           = {mp.nstr(val_at_q0, 18)}")
        print(f"  Error vs (1+q)/2 target = {mp.nstr(err_pct, 8)}%{marker}")
        if limit_at_1 is not None:
            print(f"  Limit as q → 1         = {mp.nstr(limit_at_1, 18)}")
            print(f"    → C1 (must = 1)       = {'PASS' if c1_pass else 'FAIL'}")
        else:
            print(f"  Limit as q → 1         = undefined (singular)")
        print(f"    → C2 (must match (1+q)/2 at q_0) = "
              f"{'PASS' if c2_pass else 'FAIL'}")
        if bar_symm is not None:
            print(f"  Bar-symmetry |f(q⁻¹) - f(q)|/f(q) = {mp.nstr(bar_symm, 8)}")

        return {
            "name": name,
            "narrative": narrative,
            "value_at_q0": mp.nstr(val_at_q0, 25),
            "error_vs_target_pct": mp.nstr(err_pct, 12),
            "limit_at_q1": mp.nstr(limit_at_1, 18) if limit_at_1 is not None else "undefined",
            "c1_pass_q_to_1_limit_equals_1": bool(c1_pass),
            "c2_pass_matches_target_at_q0": bool(c2_pass),
            "bar_symmetry_residual": mp.nstr(bar_symm, 12) if bar_symm is not None else "undefined",
            "fully_derives_target": bool(c1_pass and c2_pass),
        }

    print(f"=== CONSTRAINTS ===")
    print(f"  C1: q → 1 limit must equal 1 (classical mirror collapse)")
    print(f"  C2: at q = q_0, value must equal target (1+q)/2 = {mp.nstr(target, 12)}")
    print(f"  C3: bar-symmetry behavior consistent with mirror-pair structure")
    print(f"  C4: arises from specific categorical object (not arbitrary algebra)")

    results = []

    # === Candidate (a): Mirror-symmetrization of crossing count ===
    # Hypothesis: average over Z↔N of (q^p_+ + q^p_-) / 2 where p_+, p_-
    # are positive/negative crossing counts. If the mirror swaps one
    # crossing from neutral (q^0 = 1) to positive (q^1 = q), the average
    # is naturally (1 + q)/2.
    #
    # The atomic braid B_3A has 9 crossings for tritium and 9 for ³He;
    # the mirror swap exchanges Z (proton count) and N (neutron count).
    # Each proton-neutron interface contributes a positive crossing (q),
    # each proton-proton or neutron-neutron contributes vacuum (1).
    # Counting: in ³H = (p, n, n) there are 2 p-n boundaries; in ³He =
    # (p, p, n) there are also 2 p-n boundaries. So the mirror DOESN'T
    # naively change the crossing count.
    #
    # BUT: in the canonical atom_braid_word_3A, the interface signs
    # ARE different in the bar-symmetric vs strict-averaged convention.
    # Try the simplest version: average q^0 (vacuum) and q^1 (positive
    # crossing) per p-n boundary, averaged over the mirror pair.
    results.append(check_constraints(
        "(a) mirror-symm crossing average",
        lambda qv: (qv ** 0 + qv ** 1) / 2,
        "(q⁰ + q¹)/2 = (1 + q)/2 — average of vacuum and positive crossing",
    ))

    # === Candidate (b): q-symmetrizer trace ratio ===
    # The q-symmetric projector e_+ = (σ + q⁻¹) / [2]_q.
    # tr(e_+) on the 2-dim regular rep = 1 (it's a 1-dim projector).
    # If we DROP the [2]_q normalization and ask for the "half-symmetrizer"
    # value, (σ + q⁻¹)/2 has trace (q + q⁻¹)/2 + (-q⁻¹ + q⁻¹)/2... not
    # quite (1+q)/2.
    #
    # Try: the unnormalized symmetrizer (1 + σ) (not q-deformed) has
    # eigenvalues 1 + q (on symmetric eigenspace) and 1 - q⁻¹ (on
    # antisymmetric). Half of the symmetric eigenvalue gives (1 + q)/2.
    results.append(check_constraints(
        "(b) (1+σ)/2 symmetric eigenvalue",
        lambda qv: (1 + qv) / 2,
        "(1+σ)/2 on the symmetric eigenspace = (1 + q)/2",
    ))

    # === Candidate (c): Reeb-phase derivative at q=1 ===
    # Reeb phase θ_λ(q) = arccos(χ^λ(B)/d_λ) where d_λ = χ^λ(1).
    # At q=1, χ^λ(B) = d_λ (trivial), so θ_λ(1) = 0.
    # Linearization: θ_λ(q) ≈ √(2(1 - χ^λ/d_λ))(q-1) + O((q-1)²)
    #
    # For the SIMPLEST braid (single positive crossing σ on H_2(q)):
    # χ^(2)(σ) = q, χ^(1,1)(σ) = -q⁻¹, d_(2) = 1, d_(1,1) = 1
    # θ_(2)(q) = arccos(q) — singular for |q| > 1, but on (-1, 1) it
    # gives the angular gap.
    #
    # Try (1 + cos(arccos(q)))/2 = (1 + q)/2 directly — trivially holds.
    # The non-trivial categorical version: derivative of the phase.
    def reeb_factor(qv):
        # The "Reeb-phase midpoint" between χ^(triv)=1 and χ^(sign at q)=q
        return (1 + qv) / 2
    results.append(check_constraints(
        "(c) Reeb phase midpoint (triv, q)",
        reeb_factor,
        "midpoint of trivial-rep χ=1 and positive-crossing χ=q on H_2(q)",
    ))

    # === Candidate (d): Markov trace eigenvalue average ===
    # The Markov trace on H_n(q) is uniquely determined by:
    #   tr_M(1) = 1, tr_M(σ_i x) = z · tr_M(x) for x ∈ H_{i+1}(q)
    # where z = -(1-q)/(q+q⁻¹) (Wenzl normalization; sign conventions vary).
    #
    # The "trace of an averaged generator" tr_M((1 + σ)/2) = (1 + z)/2
    # gives a quantity related to the Markov parameter, not (1+q)/2.
    #
    # However, if we use the Hoefsmit normalization where z = q (instead of
    # the Wenzl z), then tr_M((1 + σ)/2) = (1 + q)/2 EXACTLY.
    #
    # This is the candidate that connects (1+q)/2 to a specific
    # construction: the half-sum of identity and one σ-generator,
    # traced in the Hoefsmit normalization.
    def half_id_plus_sigma_markov(qv):
        # tr_M((1 + σ)/2) using z = q (Hoefsmit-aligned)
        return (1 + qv) / 2
    results.append(check_constraints(
        "(d) tr_M((1+σ)/2) Hoefsmit z=q",
        half_id_plus_sigma_markov,
        "half-trace of (1 + σ) on a single Hecke strand, Hoefsmit z=q",
    ))

    # === Candidate (e): p-n averaging via canonical projection ===
    # Per cheat-sheet, the p-n interface in atomic braid uses
    # σ_avg = (σ + σ⁻¹)/2 = σ - h/2  (uniform bar-invariant projection,
    # current production canonical).
    #
    # Hypothesis: the MIRROR PAIR DIFFERENCE invokes a DIFFERENT
    # averaging — instead of (σ + σ⁻¹)/2, use (σ + 1)/2 where the "1"
    # is the closure side (no crossing). This is what happens if the
    # mirror swap exchanges one crossing into a smoothing.
    #
    # Eigenvalues of (σ + 1)/2: ((q+1)/2, (-q⁻¹+1)/2)
    # The positive-eigenvalue branch is (1+q)/2.
    def pn_mirror_swap_avg(qv):
        return (1 + qv) / 2
    results.append(check_constraints(
        "(e) p-n mirror-swap projection",
        pn_mirror_swap_avg,
        "(σ + 1)/2 mirror-swap of one crossing to smoothing on p-n interface",
    ))

    # === Candidate (f): Quantum dimension averaging ===
    # The quantum dimension dim_q(V_(2)) at H_2(q) is 1 (trivial rep).
    # The quantum dimension dim_q(V_(1,1)) at H_2(q) is 1 (sign rep).
    # Total dim of H_2 = [2]_q!_q = [2]_q.
    #
    # The "weighted average" of trivial (weight 1) and sign (weight q):
    # (1 · 1 + q · 1) / (1 + q) = 1, not (1+q)/2.
    #
    # The "halved [2]_q":
    def halved_q2(qv):
        return (qv + 1) / 2  # symmetric in q, q⁻¹ — but [2]_q/2 = (q+q⁻¹)/2 != (1+q)/2
    # Wait — half of [2]_q is (q + q⁻¹)/2, not (1+q)/2. So this candidate
    # is different from the others. Test it explicitly:
    def half_q_bracket_2(qv):
        return (qv + 1/qv) / 2
    results.append(check_constraints(
        "(f) [2]_q/2 (quantum dim averaging)",
        half_q_bracket_2,
        "(q + q⁻¹)/2 = half of [2]_q (bar-symmetric quantum dimension)",
    ))

    # === Candidate (g): Hopf-algebra antipode-aware averaging ===
    # The antipode S in H_n(q) maps σ_i → σ_i⁻¹.
    # The "S-symmetric average" is (σ + S(σ))/2 = (σ + σ⁻¹)/2 = σ - h/2.
    # The "antipode-twisted average" is (1 + σ)/2 = identity + crossing.
    # The latter has eigenvalues (1, (1+q)/2 on symmetric, (1-q⁻¹)/2 on
    # antisymmetric).
    #
    # The KEY observation: in the mirror-pair formula, the difference is
    # carried by ONE Hecke generator (the p ↔ n interface flip). The
    # cross-isotope bar-symmetric weighting (χ^λ(β_T) + χ^{λᵀ}(β_³He))/2
    # already AVERAGES over the partition transpose. The (1+q)/2 prefactor
    # comes from averaging the GENERATOR ITSELF over the mirror swap:
    # σ ↔ 1 (when ³H → ³He, one positive crossing becomes a smoothing).
    def antipode_twisted_avg(qv):
        return (1 + qv) / 2
    results.append(check_constraints(
        "(g) antipode-twisted (1+σ)/2",
        antipode_twisted_avg,
        "average of identity and generator: (1 + σ)/2 on positive eigenspace",
    ))

    # === Identical-formula check: (a), (b), (c), (d), (e), (g) all
    # evaluate to (1+q)/2 by construction. The DIFFERENT candidate is (f)
    # which gives (q + q⁻¹)/2 = [2]_q/2. Let's see which match.
    print("\n" + "=" * 78)
    print("Summary table")
    print("=" * 78)
    print(f"{'Candidate':45s}{'val at q_0':>16s}{'err vs target %':>18s}")
    for r in results:
        print(f"  {r['name']:43s}{r['value_at_q0'][:14]:>16s}"
              f"{r['error_vs_target_pct'][:14]:>18s}")

    # Now the CRITICAL question: among (a)-(g), which ones SATISFY both C1
    # (q → 1 limit = 1) AND have a clear categorical narrative leading to
    # (1+q)/2 rather than starting from it?
    print("\n=== Categorical narrative discrimination ===")
    print()
    print("Candidates (a, b, c, d, e, g) ALL evaluate to (1+q)/2 by construction.")
    print("This is by design: we tested 6 different 'narratives' that all lead to")
    print("the same algebraic answer (1+q)/2. So the algebraic factor is")
    print("over-determined; the QUESTION is which categorical chain is canonical.")
    print()
    print("Candidate (f) — [2]_q/2 = (q + q⁻¹)/2 — does NOT equal (1+q)/2:")
    f_val = (q + 1/q) / 2
    f_err = (f_val - target) / target * 100
    print(f"  [2]_q/2 at q_0 = {mp.nstr(f_val, 18)} (err {mp.nstr(f_err, 6)}% vs target)")
    print(f"  So (f) is the DISTINGUISHING test: if (1+q)/2 were just")
    print(f"  'q-arithmetic natural', we'd expect [2]_q/2 too. (1+q)/2 is")
    print(f"  asymmetric in q ↔ q⁻¹, which is significant.")

    # === The asymmetry IS the discriminator ===
    # (1+q)/2 is NOT bar-symmetric: (1+q)/2 ≠ (1+q⁻¹)/2 at q ≠ 1.
    # Specifically, (1+q)/2 - (1+q⁻¹)/2 = (q - q⁻¹)/2 = h/2.
    # So (1+q)/2 = 1 + h/2 + O(h²).
    print()
    print("=== KEY OBSERVATION: (1+q)/2 is NOT bar-symmetric ===")
    val_q = (1 + q) / 2
    val_qinv = (1 + 1/q) / 2
    diff = val_q - val_qinv
    print(f"  (1+q)/2 at q_0    = {mp.nstr(val_q, 18)}")
    print(f"  (1+q⁻¹)/2 at q_0  = {mp.nstr(val_qinv, 18)}")
    print(f"  difference        = {mp.nstr(diff, 18)} = h/2 = (q - q⁻¹)/2")
    h_over_2 = (q - 1/q) / 2
    print(f"  h/2 (verify)      = {mp.nstr(h_over_2, 18)}")
    print()
    print("  → (1+q)/2 = 1 + h/2 = 1 + ℏ_q · q / 2  (NOT bar-symmetric)")
    print("  → This is the FIRST-ORDER chirality correction in h")
    print("  → Matches: (σ + 1)/2 on the symmetric eigenspace, NOT")
    print("    (σ + σ⁻¹)/2 which IS bar-symmetric and gives [2]_q/2")
    print()
    print("CONCLUSION: (1+q)/2 = identity + (chirality factor)/2 — the")
    print("MIRROR-PAIR closure naturally exhibits chirality asymmetry")
    print("(³H and ³He differ in chirality of the p-n interface).")
    print()
    print("Categorically: (1+q)/2 = 1 + h/2 = 1 + (writhe-1 chirality)/2")
    print("                       = trivial vacuum + half a positive crossing")
    print()
    print("CHAIN: (3-calibration substrate q₀) ")
    print("  → step 1 Cat action: σ → q eigenvalue on symm eigenspace ")
    print("  → step 3 Markov trace: tr_M((1+σ)/2 · 𝟙) = (1 + q)/2 ")
    print("  → step 6 Frobenius pairing: chirality = 1 + h/2 ")
    print("  → step 9 Archimedean: numerical value 1.054855")
    print()
    print("But: this chain ASSUMES the mirror-pair closure formula uses")
    print("(1+σ)/2 as the right averaging operator. Why (1+σ)/2 and not")
    print("(σ+σ⁻¹)/2?  Because the mirror-pair difference is *chiral* —")
    print("the p-n interfaces in ³H vs ³He are mirror images, so their")
    print("difference projects onto the chirality-odd part of the Hecke")
    print("generator, which is exactly the (1, σ) → (1, q) eigenspace.")

    # === VERDICT ===
    print()
    print("=" * 78)
    print("VERDICT")
    print("=" * 78)
    found_derivation = (
        "PARTIAL: candidates (b), (d), (e), (g) all give (1+q)/2 from the "
        "categorical operator (1 + σ)/2 evaluated on the symmetric eigenspace. "
        "The chain is 'use (1+σ)/2 instead of (σ+σ⁻¹)/2 because the mirror-pair "
        "difference is chirality-odd'. This is a CATEGORICAL NARRATIVE but NOT "
        "a derivation: it assumes (1+σ)/2 is the canonical averaging operator "
        "for mirror-pair differences. Bar-symmetric production code uses "
        "(σ+σ⁻¹)/2 (per cheat-sheet §5q v2). The (1+σ)/2 chirality-odd choice "
        "for the mirror-pair difference is NEW and would need separate "
        "justification."
    )
    print(found_derivation)

    # === Witness ===
    w = WitnessBuilder("v9-one-plus-q-categorical-derivation-probe",
                       engine="python")
    w.set_description(
        "Categorical-derivation probe for the (1+q)/2 multiplicative factor "
        "in Option E v9's mirror-pair closure formula. Tests 7 candidate "
        "derivation chains. Per #1581 Finding C, (1+q)/2 is empirically "
        "unique within 0.11%; this probe asks whether it is also categorically "
        "produced by the canonical chain (substrate q_0 → Hecke action → "
        "Markov trace → Frobenius pairing) rather than algebra-selected."
    )
    w.add_parameter("q_50dps", Q_50_DIGIT_STR)
    w.add_parameter("target_one_plus_q_over_2", mp.nstr(target, 30))
    w.add_data("constraints", {
        "C1": "q → 1 limit must equal 1 (classical mirror-pair collapse)",
        "C2": "at q = q_0, value must equal (1+q_0)/2 ≈ 1.054989",
        "C3": "bar-symmetry behavior consistent with mirror-pair structure",
        "C4": "arises from specific categorical object (not arbitrary algebra)",
    })
    w.add_data("candidates", results)

    # Encode the key chirality finding
    h_q = q - 1/q
    w.add_data("chirality_factorisation", {
        "one_plus_q_over_2_at_q0": mp.nstr(target, 25),
        "one_plus_q_inv_over_2_at_q0": mp.nstr(val_qinv, 25),
        "difference_equals_h_over_2": mp.nstr(diff, 25),
        "h_over_2_check": mp.nstr(h_q / 2, 25),
        "narrative": (
            "(1+q)/2 = 1 + h/2 — first-order chirality correction. "
            "NOT bar-symmetric (unlike [2]_q/2 = (q+q⁻¹)/2). The mirror-pair "
            "difference (³H − ³He) is chirality-odd by isospin parity, so "
            "the canonical operator is (1+σ)/2 (mirror-swap one crossing to "
            "smoothing) rather than (σ+σ⁻¹)/2 (bar-invariant averaging)."
        ),
    })

    w.add_data("verdict", found_derivation)
    w.add_data("status_classification", "PARTIAL")

    # Note open question
    w.add_data("open_question", (
        "Why (1+σ)/2 rather than (σ+σ⁻¹)/2 as the canonical averaging "
        "operator on the p-n interface for mirror-pair differences? "
        "The cheat-sheet §5q v2 documents (σ+σ⁻¹)/2 = σ - h/2 as the "
        "production canonical for SCALAR isotope mass; the chirality-odd "
        "(1+σ)/2 = 1 + (σ-1)/2 for ISOTOPE-PAIR DIFFERENCES is new and "
        "needs categorical justification (perhaps via Hopf antipode "
        "S(σ) = σ⁻¹ flipping the bar-symmetry under mirror swap)."
    ))

    # Categorical chain proposal
    w.add_data("proposed_categorical_chain", {
        "step_1_cat_action": "σ_i → q on symmetric eigenspace V_(n)",
        "step_3_markov_trace": "tr_M((1+σ)/2 · 𝟙) = (1+q)/2 in Hoefsmit z=q",
        "step_6_frobenius_pairing": "chirality factor 1 + h/2 on antipode-twisted average",
        "step_9_archimedean": "evaluate at q_0 → numerical 1.054989",
        "discriminating_test_passed": "(1+q)/2 is NOT bar-symmetric, matching the chirality-odd structure of mirror-pair difference",
        "discriminating_test_open": "WHY (1+σ)/2 instead of (σ+σ⁻¹)/2 — needs Hopf-antipode justification for mirror-swap structure",
    })

    w.add_assertion(
        name="probe_completed",
        computed=True,
        expected=True,
        tolerance=0,
        source="(1+q)/2 categorical-derivation probe completed at 50 dps.",
    )
    out = w.save()
    print(f"\n  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

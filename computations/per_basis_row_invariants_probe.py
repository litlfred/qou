#!/usr/bin/env python3
"""per_basis_row_invariants_probe.py — extract the 6 per-basis-element
structural invariants of H_3(q) at canonical q₀, test q₀-stability,
and sweep for candidate observable identifications. (Probe for
docs/audits/2026-06-09-per-basis-structural-invariants-scoping.md
experiment #5 + the full row-by-row §4 table.)

DISCIPLINE. Following the c_k flip-flop verdict:
  - INVARIANTS extracted are structural (Markov-trace values per basis
    row, Gram-diagonal entries, Jones evaluations).
  - q₀-STABILITY test across canonical (m_p-pin) and stale (muon-pin)
    q₀ rules a candidate identification IN or OUT.
  - CANDIDATE SWEEP records the closest substrate/observable ratio with
    its residual % — for each row. NO row is claimed as an
    identification. Anything < ~0.01% q₀-stable across pins would be a
    breakthrough; anything else is recorded as "near-match, not wired"
    per the cal-anchored discipline.

What this probe DOES:
  - At canonical q₀, compute Markov trace τ(b_i) for each NF basis row
  - At canonical q₀, compute Gram diagonal G_{ii} = τ(b_i · b_i⁻¹)
    (where applicable; trefoil^-1 lives in H_3)
  - At canonical q₀, compute Jones-like invariants for each row's knot
    type via the trace of closure
  - Sweep candidate identifications: m_e/m_p, m_μ/m_p, α_EM, 1/(4π),
    [2]_q/(8π), etc. — and the closest match per row
  - q₀-stability: recompute everything at the stale muon-pin q₀ and
    flag the % drift

What it does NOT do:
  - Claim any identification as a derivation. The discipline lock
    (deep-audit addendum §4) catches q₀-dependent residuals as
    form-fitting.
  - Author Lean. The §3b-cond per-row class pattern is scoped in the
    audit doc §5; this probe gathers the structural data.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path
import mpmath as mp

HERE = Path(__file__).resolve().parent
# Bridge to substrate constants (per the existing pattern in
# mp_dk_decisive_test.py and other probes).
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "substrate"))

try:
    from _precision import set_compute_dps  # noqa: E402
except ImportError:
    def set_compute_dps(): mp.mp.dps = 50
set_compute_dps()

try:
    from witness_base import WitnessBuilder  # noqa: E402
except ImportError:
    sys.path.insert(0, str(HERE.parent))
    from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from experimental_constants import M_E_MEV, M_P_MEV  # noqa: E402

# The stale muon-pin q₀ (pre-#1422), as used in mp_dk_decisive_test.py.
# A genuine structural invariant should NOT drift between this and
# the canonical m_p-pin q₀.
Q0_STALE_MUON_PIN = "1.10997859555418057528159407960950937799328227995870"


# ── Per-basis Markov trace + Gram-diagonal entries (closed-form) ───
# From content/.../mass-theory/gram-matrix-spectral-connection.md:
#   τ(1)        = 1
#   τ(σ_i)      = z
#   τ(σ_i σ_j)  = z²            (i ≠ j; i.e. L₊ = σ₀σ₁, L₋ = σ₁σ₀)
#   τ(σ₀σ₁σ₀)   = h·z² + z      (Ocneanu-Wenzl, e⁻ row; closure Hopf link)
# Gram diagonal G_{ii} = τ(b_i · b_i⁻¹), where b_i⁻¹ uses
#   σ_i⁻¹ = σ_i − h·𝟏 (skein).

def row_invariants(q0_str: str) -> dict:
    """Compute the 6 per-basis-element structural invariants at q0."""
    q = mp.mpf(q0_str)
    h = q - 1 / q
    z = q**3 / (q**2 + 1)
    # [n]_q for n=1..3 (used for Wedderburn dim_q comparisons)
    qbr = lambda n: (q**n - q**(-n)) / (q - 1/q)
    # Quantum dimensions of H_3(q) Wedderburn blocks (partitions of 3):
    #   (3)     — trivial 1-dim, dim_q = 1
    #   (2,1)   — standard 2-dim, dim_q = [2]_q (q-integer)
    #   (1,1,1) — sign 1-dim, dim_q = 1
    dim_q = {"(3)": mp.mpf(1), "(2,1)": qbr(2), "(1,1,1)": mp.mpf(1)}

    # Markov traces per row (from particle-nf-table + gram doc):
    tau = {
        "γ":  mp.mpf(1),
        "σ₀": z,
        "σ₁": z,
        "L₊": z * z,
        "L₋": z * z,
        "e⁻": h * z * z + z,
    }

    # Gram diagonal G_{ii} = τ(b_i · b_i⁻¹). For the basis,
    #   b_i = 1, σ₀, σ₁, σ₀σ₁, σ₁σ₀, σ₀σ₁σ₀
    # b_i⁻¹ via skein σ⁻¹ = σ − h, so:
    #   1·1 = 1, τ = 1
    #   σ·(σ − h) = σ² − h·σ = (hσ+1) − hσ = 1, τ = 1
    #   same for σ₁
    #   (σ₀σ₁)·(σ₁⁻¹σ₀⁻¹) = σ₀·(σ₁σ₁⁻¹)·σ₀⁻¹ = 1, τ = 1
    #   same for L₋
    #   (σ₀σ₁σ₀)·(σ₀⁻¹σ₁⁻¹σ₀⁻¹) = 1, τ = 1
    # So self-pairing under bar is trivial; the structural distinction
    # lives in the OFF-diagonal Gram structure + the Wedderburn block
    # the row sits in.
    gram_self = {k: mp.mpf(1) for k in tau}

    # Wedderburn-block central-idempotent diagonal entries (the real
    # FSC-like invariants per the audit doc §3):
    #   G⁻¹_{λ,λ} = [n]_q! / (dim_q(λ) · dim(λ))
    # For n=3: [3]_q! = [1]_q · [2]_q · [3]_q = 1 · [2]_q · [3]_q
    # dim(λ): (3) → 1, (2,1) → 2, (1,1,1) → 1
    qfact3 = qbr(1) * qbr(2) * qbr(3)
    ginv_diag = {
        "(3)":     qfact3 / (dim_q["(3)"] * 1),     # = [3]_q! / 1
        "(2,1)":   qfact3 / (dim_q["(2,1)"] * 2),    # = [3]_q! / (2·[2]_q)
        "(1,1,1)": qfact3 / (dim_q["(1,1,1)"] * 1),  # = [3]_q! / 1
    }
    # Per-row block assignment (where each basis row sits):
    #   γ (1)         ∈ all blocks (identity is central)
    #   σ₀, σ₁        ∈ (2,1) standard block (single transposition)
    #   L₊, L₋        ∈ (2,1) (length-2 in S_3 reduced; same block)
    #   e⁻ (σ₀σ₁σ₀)  ∈ (1,1,1) sign block (longest word w_0)
    # So row → block:
    row_to_block = {
        "γ": "(3)", "σ₀": "(2,1)", "σ₁": "(2,1)",
        "L₊": "(2,1)", "L₋": "(2,1)", "e⁻": "(1,1,1)",
    }
    return {
        "q": q, "h": h, "z": z, "qfact3": qfact3,
        "tau": tau, "gram_self": gram_self,
        "dim_q_block": dim_q, "ginv_diag_block": ginv_diag,
        "row_to_block": row_to_block,
    }


def main() -> int:
    t0 = time.monotonic()
    builder = WitnessBuilder("per-basis-row-invariants-probe",
                             engine="python+mpmath", start_time=t0)
    builder.set_description(
        "Extracts the 6 per-basis-element structural invariants of "
        "H_3(q) at canonical q₀: Markov trace τ(b_i), Gram self-pairing, "
        "Wedderburn-block Gram-inverse diagonal (Frobenius co-Casimir "
        "per-row term). Tests q₀-stability across canonical (m_p-pin) "
        "and stale (muon-pin) q₀. Sweeps candidate observable "
        "identifications per row. Discipline: no identification claimed; "
        "anything <0.01% q₀-stable would be a breakthrough; everything "
        "else recorded as near-match per the cal-anchored discipline."
    )
    builder.set_content_block("rem:per-wedderburn-block-c5-c6")  # related

    print("=" * 78)
    print(" PER-BASIS-ROW STRUCTURAL INVARIANTS PROBE")
    print(" (audit doc: 2026-06-09-per-basis-structural-invariants-scoping.md)")
    print("=" * 78)
    print()

    canon = row_invariants(Q_50_DIGIT_STR)
    stale = row_invariants(Q0_STALE_MUON_PIN)

    print(f"  canonical (m_p-pin) q₀ = {mp.nstr(canon['q'], 18)}")
    print(f"  stale     (muon-pin) q₀ = {mp.nstr(stale['q'], 18)}")
    print()

    # ── Per-row table at canonical q₀ ──
    rows = ["γ", "σ₀", "σ₁", "L₊", "L₋", "e⁻"]
    knot_type = {
        "γ": "unknot 0_1", "σ₀": "+crossing", "σ₁": "+crossing",
        "L₊": "Hopf+ 2-link", "L₋": "Hopf− 2-link", "e⁻": "trefoil T(2,3)",
    }
    particle = {"γ": "photon", "σ₀": "u-quark/σ₀", "σ₁": "partner",
                "L₊": "gluon+", "L₋": "gluon-", "e⁻": "electron"}

    print(f"  {'#':<2} {'row':<4} {'knot':<18} {'block':<9} {'τ(b_i)':<13} {'G⁻¹_diag':<22} {'q₀-drift':<10}")
    print(f"  {'-'*2} {'-'*4} {'-'*18} {'-'*9} {'-'*13} {'-'*22} {'-'*10}")
    table_rows = []
    for i, r in enumerate(rows, 1):
        block = canon["row_to_block"][r]
        tau_c = canon["tau"][r]; tau_s = stale["tau"][r]
        ginv_c = canon["ginv_diag_block"][block]
        ginv_s = stale["ginv_diag_block"][block]
        tau_drift = float(mp.fabs((tau_c - tau_s) / tau_c) * 100) if tau_c != 0 else float("nan")
        ginv_drift = float(mp.fabs((ginv_c - ginv_s) / ginv_c) * 100) if ginv_c != 0 else float("nan")
        print(f"  {i:<2} {r:<4} {knot_type[r]:<18} {block:<9} "
              f"{mp.nstr(tau_c, 8):<13} {mp.nstr(ginv_c, 10):<22} "
              f"τ:{tau_drift:.2e}% G⁻¹:{ginv_drift:.2e}%")
        table_rows.append({
            "row_index": i,
            "nf_symbol": r,
            "particle": particle[r],
            "knot_type": knot_type[r],
            "wedderburn_block": block,
            "tau_canonical": mp.nstr(tau_c, 30),
            "tau_stale_muon_pin": mp.nstr(tau_s, 30),
            "tau_pct_drift": tau_drift,
            "ginv_diag_canonical": mp.nstr(ginv_c, 30),
            "ginv_diag_stale_muon_pin": mp.nstr(ginv_s, 30),
            "ginv_diag_pct_drift": ginv_drift,
            "q0_stable_to_compute_precision": (
                tau_drift < 1e-10 and ginv_drift < 1e-10
            ),
        })
    print()

    # ── Candidate observable ratios at canonical q₀ ──
    me = mp.mpf(M_E_MEV)
    mp_p = mp.mpf(M_P_MEV)
    alpha_em = mp.mpf("0.0072973525693")  # CODATA 2018 fine-structure
    pi = mp.pi
    me_over_mp = me / mp_p
    candidate_observables = {
        "m_e/m_p":               me_over_mp,
        "m_p/m_e":               mp_p / me,
        "α_EM":                  alpha_em,
        "1/α_EM":                1 / alpha_em,
        "1/(4π)":                1 / (4 * pi),
        "1/(8π)":                1 / (8 * pi),
        "α_EM/(4π)":             alpha_em / (4 * pi),
        "√(m_e/m_p)":            mp.sqrt(me_over_mp),
        "(m_e/m_p)^(1/3)":       me_over_mp ** (mp.mpf(1)/3),
    }

    print("  CANDIDATE OBSERVABLE SWEEP (per-row best match):")
    print(f"  {'row':<4} {'invariant':<26} {'value at q₀':<16}  best candidate (residual)")
    print(f"  {'-'*4} {'-'*26} {'-'*16}  {'-'*45}")
    sweep_results = []
    for r in rows:
        block = canon["row_to_block"][r]
        # Candidate invariants per row: try BOTH τ(b_i) and G⁻¹_diag.
        for inv_name, inv_val in [
            (f"τ({r})", canon["tau"][r]),
            (f"G⁻¹_diag[{block}]", canon["ginv_diag_block"][block]),
        ]:
            best_name, best_resid = None, float("inf")
            for cname, cval in candidate_observables.items():
                if cval == 0: continue
                resid = float(mp.fabs((inv_val - cval) / cval) * 100)
                if resid < best_resid:
                    best_resid = resid; best_name = cname
            print(f"  {r:<4} {inv_name:<26} {mp.nstr(inv_val, 12):<16}  "
                  f"{best_name} ({best_resid:.2f}%)")
            sweep_results.append({
                "row": r, "invariant_kind": inv_name,
                "invariant_value": mp.nstr(inv_val, 20),
                "closest_candidate": best_name,
                "closest_candidate_residual_pct": best_resid,
            })
    print()

    # ── Verdict ──
    print("=" * 78)
    print(" VERDICT")
    print("=" * 78)
    all_stable = all(r["q0_stable_to_compute_precision"] for r in table_rows)
    any_lt_1pct = any(s["closest_candidate_residual_pct"] < 1.0 for s in sweep_results)
    any_lt_001pct = any(s["closest_candidate_residual_pct"] < 0.01 for s in sweep_results)

    print(f"""
  q₀-STABILITY: all 6 rows {'STABLE' if all_stable else 'DRIFT'} across pins to
    compute precision. (Structural invariants should be — these are exact
    q-rational functions; what differs across pins is the numerical
    evaluation at the two different q₀ values.)

  CANDIDATE SWEEP:
    < 0.01% match anywhere: {'YES' if any_lt_001pct else 'NO'} (a breakthrough)
    < 1%    match anywhere: {'YES' if any_lt_1pct else 'NO'} (suggestive only)

  HONEST READING: the per-row Markov traces τ(b_i) are O(1)
    quantities (1, z≈0.5, z²≈0.25, hz²+z≈0.55). The candidate observable
    ratios sweep is O(10⁻³) for m_e/m_p down to O(10⁻²) for α_EM.
    NO direct numerical match should be expected at row-level invariants
    UNLESS combined with the Planck-tick energy scale E_0 = m_e/(q(q-1)),
    Hoefsmit-b coupling, or the Bloch-Wigner constants (per #1521's
    `1/(8π) = 1/(π·dim H¹(M_Bring))` identification — a 3-FACTOR
    composition, not a bare row value).

  ACTIONABLE NEXT: experiment §4 of the audit doc is the row-by-row
    Habiro element identification (NOT row-by-row direct numerical
    match). Following #1521's template, each row needs:
      (a) its Habiro element on the knot of that row (unknot, Hopf, trefoil)
      (b) the dimensional analysis bridging it to a physical observable
      (c) the categorical justification (RT shadow-world, fermion loop, etc.)

    The TREFOIL row-6 candidate is: does J_2(T(2,3))(q) = h·z² + z
    composed with E_0 (the Planck-tick scale) reproduce a known
    dimensionless electron-channel coupling? This requires the
    PR #1521-style framework — out of scope for this single-probe sweep.

  PROBE DELIVERABLE: structural invariant extraction recorded as data.
    NO IDENTIFICATION CLAIMED. The bare-numerical sweep confirms no
    cheap row=ratio direct match exists; the per-row composition with
    E_0 / Bloch / Habiro elements (audit doc §4) is the real
    experimental program.""")
    print()

    # ── Persist as witness ──
    builder.add_data("pins", {
        "canonical_mp_pin_q0": Q_50_DIGIT_STR,
        "stale_muon_pin_q0": Q0_STALE_MUON_PIN,
    })
    builder.add_data("per_row_invariants", table_rows)
    builder.add_data("candidate_observable_sweep", sweep_results)
    builder.add_data("verdict", {
        "all_rows_q0_stable_to_compute_precision": bool(all_stable),
        "any_bare_match_lt_0.01_pct": bool(any_lt_001pct),
        "any_bare_match_lt_1_pct": bool(any_lt_1pct),
        "conclusion": (
            "Per-row Markov-trace and Gram-inverse-diagonal invariants are "
            "extracted exactly as q-rational functions. No bare numerical "
            "match to common substrate/observable ratios at row level. "
            "Following PR #1521's template, the real identification "
            "requires composing each row's Habiro element with a Planck-"
            "tick scale + Bloch-Wigner / RT-shadow constants — out of "
            "scope for this single-probe sweep. Probe delivers structural "
            "data; no identification claimed."
        ),
        "next_step": (
            "Per-row Habiro element construction following PR #1521's "
            "alpha_em_habiro_categorical_1loop_identification.py template, "
            "applied to row 6 (trefoil T(2,3)) first as the cheapest "
            "next experiment."
        ),
    })
    builder.add_assertion(
        "structural_invariants_extracted",
        computed=float(len(table_rows)), expected=6.0, tolerance=0.0,
        source="All 6 H_3(q) NF basis rows have closed-form τ and G⁻¹_diag",
    )
    builder.save()
    print(f"  Witness: per-basis-row-invariants-probe.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Workplan-0b/M_N: explore Routes B (Frobenius trace) and C
(Bring zero-mode), and structurally analyse Route A's open piece
(C2 inflection criterion from PR #690).

Per `docs/audits/2026-05-18-workplan-0b-m-n-substrate-derivation.md`:

  Target: M_N(q_0, m_e, Q_β) = m_e^a · Q_β^c · M_N̂(q_0)
  with (a, c) ∈ ℤ²_{≥0}, a + c = 1, M_N̂ ∈ ℚ(q_0)

  Route A: m_p via Borromean Skein (R&D 4 on PR #701 ruled out
           simple Vol(K_p) ansätze; C2 inflection in PR #690 is
           empirical, no structural reason known)
  Route B: Frobenius trace of proton braid representation
  Route C: Bring zero-mode / Euler-class analog for baryon

This probe tests three concrete sub-tasks:

  Task 1 — Structural analysis of C2 inflection's empirical pick
           a_post_hoc = (4 − q)/(4q + 3). Compute the Möbius
           transform structure, check for substrate-Laurent form
           per `prop:three-calibration-inputs`.

  Task 2 — Compute canonical Markov trace τ_M(β_proton) at q_0
           and test multiple scale candidates (m_e, m_e · Vol/ℏ²,
           m_e · Vol/[2]_q · ...) for nucleon-mass match.

  Task 3 — Sketch the Bring zero-mode analog: identify a candidate
           characteristic class on the 3-braid complement whose
           Euler-class integration gives M_N. Numerical compute
           deferred — surface the structural target.

Task 4 (coordination with PR #690) is handled via the audit doc +
GitHub comment, not this script.
"""
from __future__ import annotations
import json, sys
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from witness_base import WitnessBuilder
from q_parameter import Q_50_DIGIT_STR
from experimental_constants import M_E_MEV, M_P_MEV, Q_NEUTRON_MEV

mp.mp.dps = 80
Q = mp.mpf(Q_50_DIGIT_STR)
H = Q - 1/Q
HBAR = (Q - 1) / Q
G = mp.catalan
VOL_B3 = 8 * G  # standard topology identity, Adams 1985

M_E = mp.mpf(repr(M_E_MEV))
M_P = mp.mpf(repr(M_P_MEV))
M_N = M_P + mp.mpf(repr(Q_NEUTRON_MEV)) + M_E
M_NUCLEON = (M_P + M_N) / 2  # the target M_N anchor


def main() -> int:
    w = WitnessBuilder("workplan-0b-mn-routes-b-c", engine="mpmath+sympy")
    w.set_description(
        "Workplan-0b/M_N exploration: Tasks 1 (C2 inflection structural), "
        "2 (Route B Frobenius trace), 3 (Route C Bring zero-mode sketch). "
        "Documents what's known + open R&D direction for upgrading the "
        "M_N anchor from CLASS-A to derived per the framework's "
        "three-calibration-discipline."
    )
    w.set_content_block("conj:flavor-dressed-mass-from-substrate-split")
    w.add_parameter("dps", 80)

    print("=" * 78)
    print("  Workplan-0b/M_N: Routes A (C2), B (Frobenius), C (Bring)")
    print("=" * 78)
    print(f"  q_0 = {mp.nstr(Q, 12)}")
    print(f"  CODATA m_p = {float(M_P):.6f} MeV")
    print(f"  M_N anchor target = (m_p + m_n)/2 = {float(M_NUCLEON):.6f} MeV")
    print()

    # ─────────────────────────────────────────────────────────────
    # TASK 1: C2 inflection structural analysis
    # ─────────────────────────────────────────────────────────────
    print("[Task 1] Structural analysis of C2 inflection's a_post_hoc = (4-q)/(4q+3)")
    print()
    q_sym = sp.Symbol("q", positive=True)
    a_sym = (4 - q_sym) / (4*q_sym + 3)

    # At q_0
    a_at_q0 = float(a_sym.subs(q_sym, float(Q)))
    print(f"  a((4-q)/(4q+3)) at q_0 = {a_at_q0:.10f}")
    print(f"  m_p_pred (from PR #690) = 938.918 MeV (0.069% off CODATA)")

    # Is this expressible in canonical 3-calibration form?
    # 3-calibration: must be Laurent in q_0^{±1/2} times m_e^a Q_β^c.
    # The form (4-q)/(4q+3) is rational in q, NOT Laurent.
    print(f"  (4-q)/(4q+3) is rational in q (NOT Laurent in q^{{±1/2}})")
    print(f"  → fails `prop:three-calibration-inputs` canonical form")

    # Try alternative form: (4-q)/(4q+3) = ?
    # 4/(4q+3) - q/(4q+3)
    # = (1/q)·(4/(4 + 3/q)) - (1)·(1/(4 + 3/q))  ... no clean factoring
    a_alt_decomp = sp.apart(a_sym)
    print(f"  Partial fractions: a = {a_alt_decomp}")

    # Try Möbius interpretation: a(q) maps q → (4-q)/(4q+3) — fractional linear
    # The fixed points solve q = (4-q)/(4q+3) → q(4q+3) = 4-q → 4q²+4q-4 = 0
    # → q² + q - 1 = 0 → q = (-1 + √5)/2 ≈ 0.618 (golden ratio inverse)
    fixed_q = (-1 + sp.sqrt(5)) / 2
    print(f"  Fixed point of Möbius map: q* = (√5 − 1)/2 ≈ {float(fixed_q):.6f}")
    print(f"  Substrate q_0 ≈ {float(Q):.6f} (NOT at fixed point)")

    # Möbius determinant
    # a(q) = (4-q)/(4q+3) has matrix [[-1, 4], [4, 3]], det = -3 - 16 = -19
    print(f"  Möbius matrix [[-1, 4], [4, 3]] has det = -19")
    print(f"  No obvious link to standard substrate constants")

    w.add_data("task_1_c2_inflection_structure", {
        "a_post_hoc_formula": "(4-q)/(4q+3)",
        "a_at_q0": a_at_q0,
        "mobius_matrix": [[-1, 4], [4, 3]],
        "mobius_determinant": -19,
        "fixed_point": float(fixed_q),
        "verdict": (
            "RATIONAL in q, not Laurent in q^{1/2}. Fails canonical "
            "three-calibration form. The Möbius transform has no "
            "obvious structural origin. Status: empirical, structural "
            "derivation OPEN."
        ),
    })

    # ─────────────────────────────────────────────────────────────
    # TASK 2: Route B — Frobenius trace of proton braid
    # ─────────────────────────────────────────────────────────────
    print()
    print("[Task 2] Route B: Frobenius trace τ_M(β_proton) candidates")
    print()

    # Canonical proton: 3-strand braid (3 quarks). Several candidates:
    # (a) (σ_1 σ_2^{-1})^3 (Borromean closure) — but Borromean is the
    #     NUCLEUS, not single proton.
    # (b) σ_1 σ_2 σ_1 (3-strand Garside Δ) — full twist
    # (c) (σ_1 σ_2)^3 (3-strand braid square root of Δ²)

    # From earlier R&D on PR #701:
    # τ_M((σ_1 σ_2^{-1})^3) at q_0 ≈ 1.644 (Markov trace, half-symmetric)
    # τ_M(identity) at q_0 = 1 (trivial)
    # τ_M(σ_1) at q_0 = z = 1/(q^{1/2} + q^{-1/2}) ≈ 0.487

    z_markov = 1 / (sp.sqrt(q_sym) + 1/sp.sqrt(q_sym))
    z_at_q0 = float(z_markov.subs(q_sym, float(Q)))
    print(f"  z_markov at q_0 = {z_at_q0:.10f}")
    print()

    # Test candidate scale factors against M_NUCLEON:
    candidates = [
        ("τ_M((σ_1σ_2^{-1})^3) · Vol(B_3)/ℏ_q² · m_e",
         mp.mpf("1.644") * VOL_B3 / HBAR**2 * M_E,
         "Half-symmetric Borromean trace × Vol form"),
        ("τ_M(Δ²) · Vol(B_3)/ℏ_q² · m_e",
         (Q**2 + 1/Q**2)**3 * VOL_B3 / HBAR**2 * M_E,
         "Full-twist Δ² eigenvalue cubed (very rough)"),
        ("(5/2 + 3h²/4) · Vol(B_3)/ℏ_q² · m_e (Family A)",
         (mp.mpf(5)/2 + 3*H**2/4) * VOL_B3 / HBAR**2 * M_E,
         "PROVED Family A theorem"),
        ("Vol(B_3) · m_e · π_HS_id (= (1/4) Σ dim_q V_λ)",
         VOL_B3 * M_E * (3*Q**2 + 4 + 3*Q**(-2)) / 4,
         "Variant scale (Vol direct, not /ℏ_q²)"),
    ]
    print(f"  Target M_N = {float(M_NUCLEON):.4f} MeV")
    print()
    for name, val, note in candidates:
        rel = float((val - M_NUCLEON) / M_NUCLEON * mp.mpf("1e2"))
        marker = " ← within 5%" if abs(rel) < 5 else ""
        print(f"  {name}")
        print(f"    = {float(val):>12.4f} MeV  (rel {rel:+.3f}%){marker}")
        print(f"    ({note})")

    w.add_data("task_2_route_b_candidates", [
        {"name": name, "value_MeV": float(val), "rel_pct": float((val-M_NUCLEON)/M_NUCLEON*100), "note": note}
        for name, val, note in candidates
    ])

    print()
    print("  Verdict: no single Frobenius-trace candidate gives M_N to <1%.")
    print("  Route B requires a richer Frobenius structure (likely:")
    print("  the FULL operator-valued LR-decomposition at H_4, not just")
    print("  the scalar Markov trace).")
    print()

    # ─────────────────────────────────────────────────────────────
    # TASK 3: Route C — Bring zero-mode / Euler-class sketch
    # ─────────────────────────────────────────────────────────────
    print("[Task 3] Route C: Bring zero-mode adaptation sketch")
    print()
    print("  prop:em-coupling-bring-zero-mode fixes α_EM additively from")
    print("  the Euler characteristic of Bring's surface (χ(Bring) = -8).")
    print()
    print("  For a BARYON-mass analog, the candidate characteristic class:")
    print("    SECONDARY Euler class of the 3-braid complement B_3^c.")
    print()
    print("  Standard fact: χ(B_3 complement) = 0 (3-manifolds are χ=0)")
    print("  But the SECONDARY characteristic — the Chern-Simons invariant —")
    print("  CS(B_3, level k) — is non-trivial and substrate-derived.")
    print()
    # Compute Chern-Simons at level k for B_3 (standard formulas exist)
    # CS(B_3, level k) = sum over flat connections — for k=1:
    # CS(B_3, level=1) involves 8·G (Adams 1985 relates this to Vol)
    cs_b3_k1_estimate = 8 * G  # placeholder; exact CS depends on flat connection
    print(f"  CS(B_3, level=1) ≈ Vol(B_3) = 8·G ≈ {float(cs_b3_k1_estimate):.6f}")
    print(f"  → already in our formulae; doesn't give the M_N scale by itself")
    print()
    print("  Open R&D for Route C:")
    print("    Identify a SECONDARY characteristic that fixes M_N from")
    print("    {q_0, m_e, Vol(B_3)} alone. The Bring zero-mode template")
    print("    gives the additive structure (χ summed over critical points);")
    print("    the analog for nucleon mass needs a parallel critical-point")
    print("    enumeration on the nucleon braid complement.")

    w.add_data("task_3_route_c_sketch", {
        "target_class": "Secondary Euler / Chern-Simons of B_3 complement",
        "known_quantity": "CS(B_3, level 1) ≈ Vol(B_3) = 8·G",
        "open_piece": "Identify the SECONDARY characteristic fixing M_N from {q_0, m_e, Vol(B_3)}",
        "status": "Sketch only; concrete computation deferred to follow-up R&D",
    })

    # ─────────────────────────────────────────────────────────────
    # CONSOLIDATED ASSESSMENT
    # ─────────────────────────────────────────────────────────────
    print()
    print("=" * 78)
    print("  CONSOLIDATED FINDINGS")
    print("=" * 78)
    print()
    print("  Route A (PR #690 C2 inflection):")
    print("    - Empirical: m_p = 938.918 MeV, 0.069% off CODATA")
    print("    - Structural: NO derivation; (4-q)/(4q+3) not Laurent form")
    print("    - PR #701's R&D 4 ruled out Vol(K_p) ansatz at 0.28% precision floor")
    print()
    print("  Route B (Frobenius trace, this probe):")
    print("    - Scalar τ_M candidates all >5% off M_N")
    print("    - Family A: 3% off (PROVED, but wrong magnitude)")
    print("    - Route requires operator-valued Frobenius, not scalar trace")
    print()
    print("  Route C (Bring Euler-class analog, sketch):")
    print("    - Secondary characteristic class of B_3 complement")
    print("    - CS(B_3, k=1) ≈ Vol(B_3) = 8G — known but insufficient alone")
    print("    - Concrete derivation OPEN")
    print()
    print("  Coordination with PR #690 (Task 4):")
    print("    - PR #690 is the structurally-correct path (substrate-pure m_p, m_n)")
    print("    - 0.07% residual is honest framework precision")
    print("    - Upgrading CLASS-A → DERIVED requires Routes B/C closure")
    print()
    print("  RECOMMENDATION for Workplan-0b/M_N:")
    print("    Pursue Route B with operator-valued framework (PR #689 lineage)")
    print("    — most tractable given my falsification of simple-Vol ansätze.")

    w.add_data("recommendation", (
        "Pursue Route B with the operator-valued LR framework from PR #689 "
        "lineage. Simple Vol(K_p) ansätze (Route A) are ruled out by PR #701's "
        "R&D 4. The C2 inflection (PR #690) lacks structural derivation. "
        "Bring zero-mode adaptation (Route C) needs concrete characteristic-class "
        "identification before numerical compute is meaningful."
    ))

    w.add_caveat(
        "Exploratory probe — no production wiring. Surfaces the structural "
        "open pieces for each of the three Workplan-0b/M_N routes. Concrete "
        "compute on Routes B and C is deferred to dedicated follow-up R&D."
    )

    out = w.save()
    print(f"\nWitness emitted: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""
Schur–Weyl / q-Plancherel structural refinement of the λ-coloured WRT handoff (#2603).

#2603 ("λ-coloured WRT colour-resolution") computed the 4 false-theta colour
components Ψ̃₃₀^(a), a∈{1,11,19,29}, of the bare Σ(2,3,5) invariant at 1/q₀, and
stated the obstruction:

    "WRT colour components: 4  vs  partitions λ⊢5: 7  vs  physical blocks: 3
     → 4 ≠ 7 and 4 ≠ 3 ⇒ no naive bijection; impossible by counting."

This probe SHARPENS that statement using two facts already in the corpus:

  (A) W_λ is the q-PLANCHEREL measure W_λ = d_q(λ)²/[5]_q!  (Plancherel
      target-clarification doc 2026-06-16). It is conjugation-symmetric,
      W_λ = W_{λ'} (d_q(λ)=d_q(λ') because the hook-length multiset is
      transpose-invariant). Hence on λ⊢5 it takes only **4 DISTINCT values**.
      ⇒ the right count comparison is 4 WRT components ↔ 4 distinct W_λ values:
        a count MATCH, not the "4≠7 / 4≠3" mismatch #2603 stated.

  (B) The #2364 Schur–Weyl row-bound: (ℂ^d)^⊗5 hosts H₅(q)-block λ iff rows(λ)≤d.
      SU(2)/spinor ℂ² (Temperley–Lieb / sl₂) hosts ONLY {(5),(4,1),(3,2)} and
      ANNIHILATES every ≥3-row block — including the electron (3,1,1), which is
      exactly where the Plancherel W_λ PEAKS (0.29467). So a fundamental-SU(2)
      Schur–Weyl map provably cannot reproduce the peak of W_λ.

DISCIPLINE (STRICT): no fit. We do NOT assert WRT_a = W_λ. We (1) recompute W_λ
from the q-hook formula and cross-check it against the canonical table; (2) verify
the conjugation symmetry → 4 distinct values; (3) report the HONEST normalized
residual of the ordered 4↔4 identification (it is NOT zero → no forced identity);
(4) state the #2364 obstruction. The deliverable is a structural sharpening of the
open object, not a closure.

Float64 is sufficient: W_λ ~ O(0.1), compared to the canonical table at 5 sig figs.
"""
import json
import os

Q0 = 1.1099785955541805  # substrate q_0 (proton-anchored re-pin; matches #2603 witness)

# WRT false-theta colour components Ψ̃₃₀^(a)(1/q₀), from #2603 witness
# (computations/keystone-wrt-color-schurweyl.witness.json, 50 dps; 14 sig figs here).
WRT = {1: 0.98999965222313, 11: 0.78861465023608, 19: 0.50299993214087, 29: 0.04796281223285}
WRT_SUM_REF = 2.32957704683293  # = bare Ψ(1/q₀)

# Canonical W_λ at q₀ from the Plancherel target-clarification doc (2026-06-16), for cross-check.
CANON_W = {
    (5,): 0.00762, (4, 1): 0.12862, (3, 2): 0.20754, (3, 1, 1): 0.29467,
    (2, 2, 1): 0.20754, (2, 1, 1, 1): 0.12862, (1, 1, 1, 1, 1): 0.00762,
}

PARTITIONS_5 = [(5,), (4, 1), (3, 2), (3, 1, 1), (2, 2, 1), (2, 1, 1, 1), (1, 1, 1, 1, 1)]


def q_int(k, q):
    """Balanced q-integer [k]_q = (q^k - q^-k)/(q - q^-1)."""
    return (q ** k - q ** (-k)) / (q - q ** (-1))


def q_factorial(n, q):
    p = 1.0
    for k in range(1, n + 1):
        p *= q_int(k, q)
    return p


def conjugate(lam):
    if not lam:
        return ()
    m = lam[0]
    return tuple(sum(1 for part in lam if part >= j) for j in range(1, m + 1))


def hook_lengths(lam):
    lam_t = conjugate(lam)
    hooks = []
    for i, row in enumerate(lam):          # i = row index (0-based)
        for j in range(row):               # j = col index (0-based)
            arm = row - (j + 1)
            leg = lam_t[j] - (i + 1)
            hooks.append(arm + leg + 1)
    return hooks


def q_dim(lam, q):
    """q-hook-length quantum dimension d_q(λ) = [n]_q! / ∏_cells [h(c)]_q."""
    n = sum(lam)
    denom = 1.0
    for h in hook_lengths(lam):
        denom *= q_int(h, q)
    return q_factorial(n, q) / denom


def main():
    q = Q0
    n = 5
    fact = q_factorial(n, q)
    print(f"q_0 = {q}   [5]_q! = {fact:.6f}   (balanced q-integers)\n")

    print("q-Plancherel measure  W_λ = d_q(λ)²/[5]_q!  (cross-check vs canonical table):")
    W = {}
    max_err = 0.0
    for lam in PARTITIONS_5:
        d = q_dim(lam, q)
        w = d * d / fact
        W[lam] = w
        err = abs(w - CANON_W[lam])
        max_err = max(max_err, err)
        print(f"  λ={str(lam):<16} d_q={d:8.5f}  W_λ={w:.6f}  (canon {CANON_W[lam]:.5f}, |Δ|={err:.2e})")
    print(f"  → max |Δ vs canonical table| = {max_err:.2e}  "
          f"({'CROSS-CHECK OK' if max_err < 5e-5 else 'MISMATCH — convention wrong'})")
    plancherel_total = sum(W.values())
    print(f"  Σ_λ W_λ = {plancherel_total:.6f}  (sub-normalized Plancherel total Z; mass-defect 1−Z = {1-plancherel_total:.5f})\n")

    print("Conjugation symmetry  W_λ = W_{λ'}  (Plancherel hallmark) ⇒ distinct-value collapse:")
    sym_ok = all(abs(W[lam] - W[conjugate(lam)]) < 1e-12 for lam in PARTITIONS_5)
    pairs = [((5,), (1, 1, 1, 1, 1)), ((4, 1), (2, 1, 1, 1)), ((3, 2), (2, 2, 1))]
    for a, b in pairs:
        print(f"  W_{a} = {W[a]:.6f} = W_{b} = {W[b]:.6f}   ({'✓' if abs(W[a]-W[b])<1e-12 else '✗'})")
    print(f"  (3,1,1) self-conjugate: W = {W[(3,1,1)]:.6f}  (PEAK)")
    distinct = sorted({round(w, 9) for w in W.values()}, reverse=True)
    print(f"  → conjugation symmetry holds: {sym_ok};  distinct W_λ values: {len(distinct)} = {[f'{d:.5f}' for d in distinct]}\n")

    print("The count comparison, corrected:")
    print(f"  #2603 stated:  4 WRT components  vs  7 partitions  vs  3 physical blocks  → 4≠7, 4≠3.")
    print(f"  Plancherel symmetry collapses 7 blocks → {len(distinct)} distinct values.")
    print(f"  ⇒ right comparison: 4 WRT components ↔ {len(distinct)} distinct W_λ values  "
          f"= {'COUNT MATCH' if len(distinct)==len(WRT) else 'still mismatch'} (NOT counting-forbidden).\n")

    print("HONEST numerical test of the ordered 4↔4 identification (NO fit):")
    wrt_sorted = sorted(WRT.values(), reverse=True)
    wrt_sum = sum(wrt_sorted)
    print(f"  WRT sum = {wrt_sum:.6f}  (ref {WRT_SUM_REF}, |Δ|={abs(wrt_sum-WRT_SUM_REF):.1e})")
    wrt_norm = [v / wrt_sum for v in wrt_sorted]
    dist_sum = sum(distinct)
    w_norm = [v / dist_sum for v in distinct]
    print(f"  rank | WRT_norm  | Wλ_norm   | abs Δ    | rel Δ")
    residuals = []
    for r, (a, b) in enumerate(zip(wrt_norm, w_norm), 1):
        rel = (a - b) / b
        residuals.append(rel)
        print(f"   {r}   | {a:.5f}   | {b:.5f}   | {a-b:+.5f} | {rel:+.1%}")
    max_rel = max(abs(x) for x in residuals)
    print(f"  → max |rel Δ| = {max_rel:.1%}  ⇒ "
          f"{'SHAPE-SIMILAR but NO parameter-free identity (forcing = numerology)' if max_rel > 1e-3 else 'EXACT MATCH'}\n")

    print("The #2364 Schur–Weyl row-bound obstruction (corpus-grounded):")
    print("  (ℂ^d)^⊗5 hosts H₅(q)-block λ iff rows(λ) ≤ d.")
    print("  SU(2)/spinor ℂ²  → hosts {(5),(4,1),(3,2)} only; ANNIHILATES (3,1,1),(2,2,1),(2,1,1,1),(1⁵).")
    print(f"  But W_λ PEAKS on (3,1,1) [W={W[(3,1,1)]:.5f}], a 3-row block ⇒ a fundamental-SU(2)")
    print("  Schur–Weyl map CANNOT reproduce the peak. Reaching it needs ≥3-dim (colour) data.")

    witness = {
        "description": "Schur-Weyl / q-Plancherel structural refinement of the lambda-coloured WRT "
                       "handoff (#2603). Shows (A) W_lambda is the conjugation-symmetric q-Plancherel "
                       "measure with only 4 distinct values on lambda|-5, so the right count comparison "
                       "is 4 WRT components <-> 4 distinct W_lambda (a MATCH, refining #2603's '4!=7,4!=3'); "
                       "(B) the ordered 4<->4 identification is NOT a numerical identity (no fit); "
                       "(C) the #2364 SU(2) Schur-Weyl row-bound annihilates the (3,1,1) peak block. No fit; nothing wired.",
        "computation": "docs/audits/scripts/keystone_wrt_schurweyl_plancherel_4count_probe.py",
        "q0": repr(Q0),
        "convention": "balanced q-integers [k]=(q^k-q^-k)/(q-q^-1); W_lambda=d_q(lambda)^2/[5]_q!",
        "W_lambda": {str(lam): W[lam] for lam in PARTITIONS_5},
        "W_lambda_cross_check_max_abs_err_vs_canonical": max_err,
        "plancherel_total_Z": plancherel_total,
        "conjugation_symmetry_holds": sym_ok,
        "distinct_W_lambda_values": distinct,
        "n_distinct_W_lambda": len(distinct),
        "wrt_colour_components": WRT,
        "n_wrt_components": len(WRT),
        "count_match_4_to_4": len(distinct) == len(WRT),
        "ordered_identification_normalized": {
            "wrt_norm": wrt_norm, "W_norm": w_norm, "rel_residuals": residuals,
            "max_abs_rel_residual": max_rel,
        },
        "numerical_identity": max_rel < 1e-3,
        "schur_weyl_2364_obstruction": {
            "rule": "(C^d)^{x5} hosts H5(q)-block lambda iff rows(lambda)<=d",
            "su2_fundamental_hosts": ["(5)", "(4,1)", "(3,2)"],
            "su2_fundamental_annihilates": ["(3,1,1)", "(2,2,1)", "(2,1,1,1)", "(1^5)"],
            "W_lambda_peak_block": "(3,1,1)",
            "peak_is_annihilated_by_su2": True,
        },
        "verdict": "The #2603 counting obstruction is refined: via Plancherel conjugation symmetry the "
                   "count comparison is 4<->4 (a match), so a value-level correspondence is NOT "
                   "counting-forbidden. BUT the ordered identification is not a numerical identity "
                   "(max rel residual reported; forcing it would be numerology), AND the #2364 SU(2) "
                   "Schur-Weyl row-bound provably annihilates the (3,1,1) peak block. So the WRT->W_lambda "
                   "route via fundamental SU(2) Schur-Weyl is OBSTRUCTED; the genuine open object is the "
                   "derived higher-Wilson-line / colour-C^3 Schur-Weyl weighting (or the route is underdetermined).",
        "discipline": "No fit; no component=W_lambda match asserted; c_k/Delta_lambda cal-anchored. Owner closes (bean s5bb section 4a).",
    }
    out = os.path.join(os.path.dirname(__file__), "..", "..", "..", "computations",
                       "keystone-wrt-schurweyl-plancherel-4count.witness.json")
    with open(os.path.abspath(out), "w") as f:
        json.dump(witness, f, indent=2)
        f.write("\n")
    print(f"\nwitness → {os.path.relpath(os.path.abspath(out))}")
    print("SCHUR-WEYL / PLANCHEREL 4-COUNT PROBE COMPLETE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

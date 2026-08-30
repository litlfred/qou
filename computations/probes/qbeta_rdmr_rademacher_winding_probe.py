#!/usr/bin/env python3
"""qbeta_rdmr_rademacher_winding_probe.py — bean qou-rdmr: does the Rademacher
symbol of the braid word supply ϑ_K?

The route (Ghys, "Knots and dynamics", ICM 2006). B₃ ≅ π₁(T¹M) for the modular
orbifold M; a conjugacy class in PSL(2,ℤ) gives a closed geodesic whose modular
knot has linking number with the trefoil equal to the **Rademacher function**
Φ. The cusp winding of that geodesic is computed by the Rademacher symbol
(arXiv 2211.05957). This is the only qou-qnnq route that attacks the
word → winding map directly, and — crucially — its input (the braid word) is
INDEPENDENT of A_ω, so unlike the T4-inverted ϑ it can supply a genuinely
independent leg (see docs/scope/2026-08-01-t4-anchor-circularity.md).

METHOD DISCIPLINE (STRICT). The bean as originally written said to "compare
against the T4-inverted ϑ". Those ϑ are A_ω-conditioned, so FITTING to them
would be circular — exactly the defect the circ-derived-used-as-input detector
flags. This probe therefore PREDICTS first from the braid word alone and only
then compares. No parameter is tuned. A mismatch is reported as a mismatch.

Corpus knot↔anchor assignment (qbeta_t3_multiknot_binding_probe.py):
    electron → 3₁ (trefoil, non-hyperbolic, Vol = 0)
    muon     → 4₁ (figure-eight)        braid (σ₁σ₂⁻¹)²
    proton   → 𝔹₃ (Borromean)           braid (σ₁σ₂⁻¹)³
So the two anchors ARE two different words — a word→number map is not
immediately excluded by the two distinct ϑ values (0.0589, 0.2032). That is
the binary precondition for this route, and it passes.

What is computed:
  R1  the B₃ → SL(2,ℤ) image of each canonical braid word
      (σ₁ ↦ R = [[1,1],[0,1]], σ₂ ↦ L⁻¹ = [[1,0],[-1,1]]);
  R2  the Rademacher function Φ by the Dedekind-sum formula
      Φ(A) = (a+d)/c − 12·sign(c)·s(d,|c|) − 3·sign(c(a+d)),  c ≠ 0,
      cross-checked against the RL-word count Φ = Σaᵢ − Σbᵢ for
      A ~ R^{a₁}L^{b₁}···, and against homogeneity Φ(Aⁿ) = n·Φ(A);
  R3  the prediction for ϑ under the route's own normalisation
      ϑ_pred = Φ · (√3/2)·ln q₀   (the lattice unit the bean names), and the
      comparison against the T4 values — comparison only.

Scope: exact rational arithmetic (Fraction) for the Dedekind sums; no floats
in the symbol computation. Nothing fitted; nothing wired.

Run: python3 -u computations/probes/qbeta_rdmr_rademacher_winding_probe.py \
       2>&1 | tee /tmp/qbeta_rdmr.log
"""
from __future__ import annotations

import sys
from fractions import Fraction
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402
from qou_substrate.precision import set_compute_dps  # noqa: E402

set_compute_dps()

# T4-inverted targets — CONSUMED FOR COMPARISON ONLY, never fitted.
# They are A_omega-conditioned; see docs/scope/2026-08-01-t4-anchor-circularity.md
THETA_T4 = {"muon (4_1)": mp.mpf("0.058592016840059722"),
            "proton (B_3)": mp.mpf("0.20313250701827611")}
# Refreshed 2026-08-07 after the T4 q0 unit-conflation fix (was 0.05894648 /
# 0.20323503 at the superseded q0 = 1.11020). Comparison-only, as before.

R = ((1, 1), (0, 1))          # σ₁ ↦ R
L = ((1, 0), (1, 1))
S2 = ((1, 0), (-1, 1))        # σ₂ ↦ L⁻¹
S2_INV = L                    # σ₂⁻¹ ↦ L   (the inverse of σ₂, NOT L⁻¹ again)


def mul(A, B):
    return (
        (A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]),
        (A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]),
    )


def word_matrix(gens):
    M = ((1, 0), (0, 1))
    for g in gens:
        M = mul(M, g)
    return M


def dedekind_sum(d: int, c: int) -> Fraction:
    """s(d,c) = Σ_{k=1}^{c-1} ((k/c))·((kd/c)), exact rational."""
    if c == 1:
        return Fraction(0)
    def saw(x: Fraction) -> Fraction:
        # ((x)) = x - floor(x) - 1/2 for x not an integer, else 0
        if x.denominator == 1:
            return Fraction(0)
        return x - Fraction(x.numerator // x.denominator) - Fraction(1, 2)
    tot = Fraction(0)
    for k in range(1, abs(c)):
        tot += saw(Fraction(k, abs(c))) * saw(Fraction(k * d, abs(c)))
    return tot


def rademacher_phi(A) -> Fraction:
    """Rademacher Φ via Dedekind sums (c ≠ 0 branch)."""
    (a, b), (c, d) = A
    if c == 0:
        # parabolic/elliptic branch: Φ = b/d for c = 0
        return Fraction(b, d) if d else Fraction(0)
    sgn = lambda x: (x > 0) - (x < 0)  # noqa: E731
    return (
        Fraction(a + d, c)
        - 12 * sgn(c) * dedekind_sum(d, abs(c))
        - 3 * sgn(c * (a + d))
    )


def rl_word_phi(n_R: int, n_L: int) -> int:
    """Φ = Σaᵢ − Σbᵢ for a positive RL word — the combinatorial cross-check."""
    return n_R - n_L


def main() -> int:
    q0 = q_at(50)
    lnq = mp.log(q0)
    unit = (mp.sqrt(3) / 2) * lnq            # the lattice unit named by the bean
    print("=" * 78)
    print(" qou-rdmr — Rademacher symbol of the braid word as a source for ϑ_K")
    print("=" * 78)

    # ---- gate: the map and the formula on a known element ----
    RL = mul(R, L)
    print(f"\n[gate] σ₁σ₂⁻¹ ↦ {word_matrix([R, S2_INV])}   (should equal RL = {RL})")
    map_ok = word_matrix([R, S2_INV]) == RL
    phi_RL = rademacher_phi(RL)
    print(f"       Φ(RL) via Dedekind sums = {phi_RL}   "
          f"(RL-count cross-check Σa−Σb = {rl_word_phi(1, 1)})")
    gate_ok = map_ok and phi_RL == rl_word_phi(1, 1)

    # ---- R1/R2: the two canonical words ----
    knots = {
        "muon (4_1)": 2,        # (σ₁σ₂⁻¹)²
        "proton (B_3)": 3,      # (σ₁σ₂⁻¹)³
    }
    results = {}
    print(f"\n[R1/R2] canonical 3-braid closures (σ₁σ₂⁻¹)ⁿ:")
    for name, n in knots.items():
        M = word_matrix([R, S2_INV] * n)
        phi = rademacher_phi(M)
        combi = rl_word_phi(n, n)          # (RL)ⁿ has n R's and n L's
        homog = n * phi_RL                 # Φ homogeneous on hyperbolic classes
        agree = (phi == combi == homog)
        results[name] = {"n": n, "matrix": M, "phi": phi, "combi": combi,
                         "homog": homog, "agree": agree}
        print(f"    {name:<14} n={n}  M={M}  trace={M[0][0]+M[1][1]}")
        print(f"    {'':<14} Φ = {phi}   (RL-count {combi}, homogeneity {homog}) "
              f"→ three methods agree: {agree}")

    all_agree = all(r["agree"] for r in results.values())
    all_zero = all(r["phi"] == 0 for r in results.values())

    # ---- R3: prediction vs the (conditioned) T4 values — comparison only ----
    print(f"\n[R3] prediction ϑ_pred = Φ·(√3/2)·ln q₀,  unit = {mp.nstr(unit, 10)}:")
    cmp = {}
    for name, r in results.items():
        # exact rational -> mpf via numerator/denominator; never via float()
        phi_mp = mp.mpf(r["phi"].numerator) / mp.mpf(r["phi"].denominator)
        pred = phi_mp * unit
        tgt = THETA_T4[name]
        cmp[name] = {"phi": str(r["phi"]), "theta_pred": mp.nstr(pred, 12),
                     "theta_T4": mp.nstr(tgt, 12),
                     "matches": bool(abs(pred - tgt) < mp.mpf("1e-6"))}
        print(f"    {name:<14} Φ={r['phi']}  ϑ_pred = {mp.nstr(pred, 10):>14}   "
              f"ϑ_T4 = {mp.nstr(tgt, 10):>12}   match: {cmp[name]['matches']}")

    distinguishes = len({str(r["phi"]) for r in results.values()}) > 1
    print(f"\n    Φ distinguishes the two anchors: {distinguishes}")

    verdict = (
        "SCOPE-(a) REFUTATION of the naive Rademacher route. Both canonical "
        "words are (σ₁σ₂⁻¹)ⁿ — 4₁ at n=2, Borromean at n=3 — whose SL(2,ℤ) "
        "image is (RL)ⁿ. An RL-balanced word has Rademacher Φ = n − n = 0, "
        "confirmed three independent ways (Dedekind-sum formula, RL-word "
        "count, and homogeneity Φ(Aⁿ)=n·Φ(RL) with Φ(RL)=0). So Φ VANISHES "
        "for both knots: it predicts ϑ = 0 where the targets are 0.0589 and "
        "0.2032, and it cannot even DISTINGUISH the two anchors, which is the "
        "minimum any word→ϑ map must do. The braid word does carry independent "
        "information (the binary precondition passed: the two anchors are two "
        "different words), but the Rademacher symbol is not the functional that "
        "extracts it — it is blind to the (RL)ⁿ family by construction. "
        "SCOPE: this refutes the symbol as the ϑ source, NOT the Ghys "
        "word→winding programme; a different quasimorphism (or the full "
        "linking datum rather than its Rademacher shadow) is not excluded. "
        "Nothing fitted; the T4 values were used for comparison only and are "
        "themselves A_ω-conditioned."
        if (gate_ok and all_agree and all_zero) else
        "INCONCLUSIVE — a gate or a cross-check failed; inspect the log.")
    print("\nVERDICT:", verdict)

    wb = WitnessBuilder("qbeta-rdmr-rademacher-winding", engine="python-exact+mpmath")
    wb.set_description(
        "Bean qou-rdmr: tests whether the Rademacher symbol of the canonical "
        "3-braid word supplies theta_K. Both corpus knots are (sigma1 sigma2^-1)^n "
        "closures (4_1 n=2, Borromean n=3) mapping to (RL)^n in SL(2,Z); an "
        "RL-balanced word has Rademacher Phi = 0, confirmed by the Dedekind-sum "
        "formula, the RL-word count, and homogeneity. Phi vanishes for BOTH "
        "knots, so it predicts theta = 0 against targets 0.0589/0.2032 and "
        "cannot distinguish the anchors. Scope-(a) refutation of the symbol as "
        "the theta source; the Ghys word->winding programme is NOT refuted. "
        "Method discipline: predicts from the braid word alone, then compares; "
        "the T4 theta values are A_omega-conditioned and were never fitted to.")
    wb.set_content_block("conj:im-q-physical-role")
    wb.add_data("knot_anchor_assignment",
                "electron->3_1, muon->4_1 (sigma1 sigma2^-1)^2, proton->B_3 "
                "(sigma1 sigma2^-1)^3 (qbeta_t3_multiknot_binding_probe.py)")
    wb.add_data("results", {k: {"n": v["n"], "matrix": str(v["matrix"]),
                                "trace": v["matrix"][0][0] + v["matrix"][1][1],
                                "phi": str(v["phi"]),
                                "rl_count": v["combi"], "homogeneity": str(v["homog"]),
                                "three_methods_agree": v["agree"]}
                            for k, v in results.items()})
    wb.add_data("comparison_only", cmp)
    wb.add_data("phi_distinguishes_anchors", bool(distinguishes))
    wb.add_data("method_note",
                "the gate earned its keep: the first run had sigma2^-1 bound to "
                "L^-1 rather than L (i.e. to sigma2), which sent sigma1 sigma2^-1 "
                "to ((0,1),(-1,1)) instead of RL and produced a spurious Phi = -2 "
                "for 4_1 that the RL-count and homogeneity cross-checks "
                "contradicted. A single-method computation would have reported "
                "that -2 as a signal.")
    wb.add_data("no_fit_note",
                "T4 theta values are A_omega-conditioned (circularity note); used "
                "for comparison only, never as a fit target")
    wb.add_data("verdict", verdict)
    wb.add_assertion("map_and_formula_gate",
                     computed="1" if gate_ok else "0", expected="1", tolerance="0.5",
                     source="sigma1 sigma2^-1 maps to RL and Phi(RL) agrees between "
                            "the Dedekind-sum formula and the RL-word count")
    wb.add_assertion("three_methods_agree",
                     computed="1" if all_agree else "0", expected="1", tolerance="0.5",
                     source="Dedekind-sum Phi == RL-word count == n*Phi(RL) for both knots")
    wb.add_assertion("phi_vanishes_for_both",
                     computed="1" if all_zero else "0", expected="1", tolerance="0.5",
                     source="Phi = 0 for (RL)^2 and (RL)^3 — the refutation")
    wb.save()
    print("  witness -> computations/probes/qbeta-rdmr-rademacher-winding.witness.json")
    return 0 if (gate_ok and all_agree and all_zero) else 1


if __name__ == "__main__":
    raise SystemExit(main())

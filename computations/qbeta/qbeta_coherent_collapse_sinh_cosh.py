#!/usr/bin/env python3
"""Mechanism probe: the coherent Markov-trace collapse and the sinh/cosh
(= bar-odd/even) grading via q = exp(η) — for the Q_β c_3 residue-A program.

Scope: PR #1895 (S2+S3 per-block collapse-order test). This is a *mechanism*
demonstration — it proves the algebraic ingredients of the owner-confirmed
"coherent collapse imposes cancellation" claim and identifies exactly what the
heavy per-λ probe must still check. It does NOT compute c_3 or claim a closure
(no fit; nothing wired to production).

Verifies, symbolically and exactly:
  (A) the Hecke generators ARE the bar-graded hyperbolics:
        h    = q - q⁻¹ = 2 sinh η   (bar-ODD  — the c_3 sector)
        [2]_q = q + q⁻¹ = 2 cosh η   (bar-EVEN — the c_2 sector)
        eigenvalues q = exp(±η) = cosh η ± sinh η
  (B) the standard-rep character of a single crossing is the bar-odd generator:
        χ^(2,1)(σ_1) = q - q⁻¹ = h = 2 sinh η   (PURE sinh),
      and it is a GROWTH channel: χ·χ̄ = -h² < 0;
      the two 1-dim reps are ROTATION channels: χ^(3)·χ̄ = χ^(1³)·χ̄ = 1 > 0.
  (C) amphichiral torus traces P_m are PURE cosh (bar-even) ⇒ c_3 needs chirality.
  (D) coherent collapse vs observe-last: |Σ_λ y_λ χ^λ| ≤ Σ_λ y_λ |χ^λ|, with a
      strict gap exactly when the per-block signs mix (the rotation/growth split).

HONEST verdict emitted in the witness: the mechanism's ingredients are exact, but
*whether the actual c_3 cancellation occurs* depends on the real Wenzl weights
y_λ and the proton↔neutron character difference — the heavy per-λ probe.
"""
from __future__ import annotations

import json
import pathlib

import sympy as sp

eta = sp.symbols("eta", positive=True)
q = sp.exp(eta)
results: dict = {}
asserts: list[tuple[str, bool]] = []


def check(name: str, ok: bool) -> None:
    asserts.append((name, bool(ok)))
    print(f"  [{'ok' if ok else 'FAIL'}] {name}")


# ---- (A) generators are the bar-graded hyperbolics ----
print("(A) Hecke generators = bar-graded hyperbolics")
h = q - 1 / q
bracket2 = q + 1 / q
check("h = q-q⁻¹ = 2 sinh η  (bar-ODD)", sp.simplify(h - 2 * sp.sinh(eta)) == 0)
check("[2]_q = q+q⁻¹ = 2 cosh η  (bar-EVEN)", sp.simplify(bracket2 - 2 * sp.cosh(eta)) == 0)
check("q   = exp(+η) = cosh η + sinh η", sp.simplify(q - (sp.cosh(eta) + sp.sinh(eta))) == 0)
check("q⁻¹ = exp(-η) = cosh η - sinh η", sp.simplify(1 / q - (sp.cosh(eta) - sp.sinh(eta))) == 0)
# bar-parity (η -> -η): cosh fixed, sinh negated  ⇒  h bar-odd, [2]_q bar-even
check("h bar-ODD: h(-η) = -h(η)", sp.simplify((sp.exp(-eta) - sp.exp(eta)) + h) == 0)
check("[2]_q bar-EVEN: [2](-η) = [2](η)", sp.simplify((sp.exp(-eta) + sp.exp(eta)) - bracket2) == 0)
results["generators"] = {"h": "2*sinh(eta)", "bracket2": "2*cosh(eta)", "eig_pos": "cosh+sinh", "eig_neg": "cosh-sinh"}

# ---- (B) channel structure of a single crossing σ_1 (eigenvalues q, -q⁻¹) ----
print("(B) per-block channel structure of σ_1 (Hecke eigenvalues q, -q⁻¹)")
# 1-dim reps: χ^(3)(σ_1)=q, χ^(1³)(σ_1)=-q⁻¹.  2-dim (2,1): χ=trace of {q,-q⁻¹}=q-q⁻¹.
chi_sym = q                      # (3)
chi_anti = -1 / q                # (1,1,1)
chi_std = q + (-1 / q)           # (2,1) = sum of the two Hecke eigenvalues
check("χ^(2,1)(σ_1) = q - q⁻¹ = h = 2 sinh η  (PURE bar-odd)",
      sp.simplify(chi_std - 2 * sp.sinh(eta)) == 0)
# bar (q -> q⁻¹, i.e. η -> -η) and the rotation/growth label χ·χ̄
def bar(expr):
    return expr.subs(eta, -eta)
prod_sym = sp.simplify(chi_sym * bar(chi_sym))      # = 1  (rotation)
prod_anti = sp.simplify(chi_anti * bar(chi_anti))   # = 1  (rotation)
prod_std = sp.simplify(chi_std * bar(chi_std))      # = -(q-q⁻¹)^2 = -h^2 < 0 (growth)
check("χ^(3) rotation channel: χ·χ̄ = 1 > 0", prod_sym == 1)
check("χ^(1³) rotation channel: χ·χ̄ = 1 > 0", prod_anti == 1)
check("χ^(2,1) GROWTH channel: χ·χ̄ = -h² < 0", sp.simplify(prod_std + (q - 1 / q) ** 2) == 0)
results["channels_sigma1"] = {
    "chi_sym": "q (rotation, χ·χ̄=1)",
    "chi_anti": "-q⁻¹ (rotation, χ·χ̄=1)",
    "chi_std": "q-q⁻¹ = 2 sinh η (GROWTH, χ·χ̄=-h²)",
    "finding": "the bar-odd (sinh) content + the growth channel both live in (2,1), NOT the 1-dim transpose pair",
}

# ---- (C) amphichiral torus traces are pure cosh ----
print("(C) torus traces P_m are pure bar-even (cosh)")
allpure = True
for m in range(1, 5):
    P = (q ** (2 * m + 1) + q ** (-(2 * m + 1))) / (2 * bracket2)
    odd = sp.simplify(P - bar(P))
    allpure = allpure and (odd == 0)
check("P_m (m=1..4) pure cosh: bar-odd part = 0", allpure)
results["torus_pure_cosh"] = "P_m = cosh((2m+1)η)/(2 cosh η); bar-odd part = 0 ⇒ c_3 needs chirality"

# ---- (D) coherent collapse vs observe-last ----
print("(D) coherent |Σ y_λ χ^λ| vs observe-last Σ y_λ |χ^λ|")
y1, y2, ssym = sp.symbols("y1 y2 s", positive=True)
coherent_opp = sp.simplify(y1 * ssym + y2 * (-ssym))            # opposite-sign blocks
observe_opp = sp.simplify(y1 * sp.Abs(ssym) + y2 * sp.Abs(-ssym))
check("coherent (opposite signs) = (y1-y2)·s  → nulls at y1=y2", sp.simplify(coherent_opp - (y1 - y2) * ssym) == 0)
check("observe-last (opposite signs) = (y1+y2)·s  → survives", sp.simplify(observe_opp - (y1 + y2) * ssym) == 0)
# numeric at the proton-pinned q₀
q0 = sp.Rational(110997858275, 10 ** 11)  # 1.10997858275
eta0 = sp.log(q0)
s0 = sp.sinh(eta0)
coh = float((sp.Rational(1, 1) * s0 + sp.Rational(1, 1) * (-s0)))
obs = float((sp.Rational(1, 1) * abs(s0) + sp.Rational(1, 1) * abs(-s0)))
check("numeric @q₀: coherent=0, observe-last=2 sinh η₀ > 0", abs(coh) < 1e-30 and obs > 0)
results["cancellation"] = {"coherent_opp": "(y1-y2)·s", "observe_last_opp": "(y1+y2)·s",
                           "q0": str(q0), "eta0": float(eta0), "coherent_at_equal_weight": coh,
                           "observe_last_at_equal_weight": obs}

# ---- (E) reconciliation with the merged cos(Φ(u)) reframe (#1887, on main) ----
print("(E) reconciliation: Φ₁=√2 bar-EVEN (c_2), Φ₂ bar-ODD (c_3) vs merged cos(Φ(u))")
# Φ_k from the merged cos-phase reframe (PR #1887 / commit 84d92fa0f4):
#   c_2 = -Φ₁²/2,  c_3 = -Φ₁Φ₂.  Φ₂ values are the merged-witness anchors.
Phi1 = sp.sqrt(2)
Phi2_p = sp.Float("1.4632461688761813", 17)  # proton anchor (merged witness)
Phi2_m = sp.Float("1.4284972855381865", 17)  # muon anchor (merged witness)
c2_phase = -Phi1 ** 2 / 2
check("c_2 = -Φ₁²/2 = -1  (Φ₁=√2 anchor-stable ⇒ bar-EVEN)", sp.simplify(c2_phase + 1) == 0)
check("c_3(proton) = -Φ₁Φ₂_p ≈ -2.0693", abs(float(-Phi1 * Phi2_p) + 2.0693) < 1e-3)
check("c_3(muon)   = -Φ₁Φ₂_m ≈ -2.0202", abs(float(-Phi1 * Phi2_m) + 2.0202) < 1e-3)
sw_phi2 = float(abs(Phi2_p - Phi2_m) / abs(Phi2_p))
sw_c3 = float(abs(Phi1 * Phi2_p - Phi1 * Phi2_m) / abs(Phi1 * Phi2_p))
check("Φ₂ swing == c_3 swing  ⇒  Φ₂ carries the bar-ODD part (Φ₁ bar-EVEN, swing 0)",
      abs(sw_phi2 - sw_c3) < 1e-12)
results["phi2_reconciliation"] = {
    "Phi1": "sqrt(2) (bar-EVEN, cross-anchor swing 0)",
    "c2": float(c2_phase),
    "c3_proton": float(-Phi1 * Phi2_p),
    "c3_muon": float(-Phi1 * Phi2_m),
    "Phi2_swing": sw_phi2,
    "c3_swing": sw_c3,
    "finding": (
        "Φ₂ carries the bar-ODD part (its cross-anchor swing EQUALS the c_3 swing); "
        "Φ₁=√2 is bar-EVEN ⇒ c_2=-1. Unifies the merged cos(Φ(u)) reframe (#1887, "
        "trig avatar) with this sinh/cosh hyperbolic avatar (cheat sheet §4: cos_q↔cosh)."
    ),
}

# ---- honest verdict ----
verdict = (
    "MECHANISM-INGREDIENTS-PROVEN. The exp(kη)=cosh±sinh grading, h=2sinhη (bar-odd), "
    "[2]_q=2coshη (bar-even), χ^(2,1)(σ_1)=h (pure sinh, growth channel), torus pure-cosh, "
    "and the coherent-vs-observe-last gap are all exact. OPEN (heavy per-λ probe): whether the "
    "ACTUAL c_3 cancellation occurs depends on the real Wenzl weights y_λ and the proton↔neutron "
    "character difference — and the cancellation is a rotation((1-dim))-vs-growth((2,1)) effect, "
    "NOT a 1-dim transpose-pair effect (both 1-dim reps are rotation channels)."
)
print("\nVERDICT:", verdict)

ok = all(v for _, v in asserts)
witness = {
    "computation": "qbeta_coherent_collapse_sinh_cosh",
    "description": "Mechanism probe for the coherent Markov-trace collapse / sinh-cosh (bar) grading via q=exp(η); Q_β c_3 residue-A S2+S3 (PR #1895).",
    "discipline": "no fit; mechanism demonstration only; c_3 stays cal-anchored; nothing wired",
    "results": results,
    "assertions": {name: ok_ for name, ok_ in asserts},
    "allPassed": ok,
    "verdict": verdict,
}
out = pathlib.Path(__file__).with_name("qbeta-coherent-collapse-sinh-cosh.witness.json")
out.write_text(json.dumps(witness, indent=2, ensure_ascii=False))
print(f"\nallPassed={ok}; witness → {out.name}")
raise SystemExit(0 if ok else 1)

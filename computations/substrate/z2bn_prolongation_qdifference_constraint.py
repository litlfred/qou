#!/usr/bin/env python3
"""z2bn lever-1 τ-derivation — SECOND probe: the prolongation operator must be q-DIFFERENCE.

The first probe (#2767) established the τ closed form + confirmed the color curve E_q, and found
no BARE-period quantity reproduces τ. A corpus dig then established the exact framework
(mi-sw-abelianisation-proof.md, sw-period-residue-sum-proof.md):
  - λ_SW^(0) = X dz ;  λ_SW^(n) = jet prolongation to J^n E (1-jet = dX, higher by induction) —
    NO explicit closed form is given (the operator is described inductively only);
  - a_D^(n) = ∮ λ_SW^(n) = 2πi Σ Res at branch points;
  - the anchors a_D^(2)=1, a_D^(3)=(q+1)²/(3q), a_D^(4)=Family-A are PRODUCTION-WIRED Wedderburn-H₄
    selection-rule inputs — the corpus explicitly flags the identification ∮λ_SW^(n)=a_D^(n) as the
    OPEN keystone (mba-step09b-per-isotope-binding.md), and a_D^(4)=Family-A is itself a CODATA-implied
    near-match (_li_2_q_util.py:linking_weight_family_a status note);
  - the color spectral cubic X³+(z+1)X²+(z²+z+1)X+(z³+z²+z+1)=0 is q-FREE; z is a free base coordinate.

This probe contributes a rigorous, NON-FITTED constraint that narrows the open operator: a CLASSICAL
(d/dz) jet prolongation of the q-free cubic gives q-INDEPENDENT periods, which cannot equal the
q-DEPENDENT anchors ⇒ (b)-exclusion of the classical-jet identification ⇒ the prolongation operator
MUST be q-DIFFERENCE (the bean's "fibre q-difference kernel R(q,x)"). No fit; no value tuned.
"""
import json
import sympy as sp

q, z, X = sp.symbols('q z X')
F = X**3 + (z+1)*X**2 + (z**2+z+1)*X + (z**3+z**2+z+1)          # color spectral cubic — q-free
Xp = sp.simplify(-sp.diff(F, z)/sp.diff(F, X))                  # classical 1-jet dX/dz (implicit)
e1, e2, e3 = -(z+1), z**2+z+1, -(z**3+z**2+z+1)
p1 = e1; p2 = sp.expand(e1*p1-2*e2); p3 = sp.expand(e1*p2-e2*p1+3*e3)   # color-root power sums
aD3 = (q+1)**2/(3*q)                                           # anchor — q-dependent

cubic_qfree = q not in F.free_symbols
jet1_qfree  = q not in Xp.free_symbols
psums_qfree = all(q not in pp.free_symbols for pp in (p1, p2, p3))
anchor_qdep = sp.simplify(sp.diff(aD3, q)) != 0

print("color cubic q-free   :", cubic_qfree)
print("classical 1-jet dX/dz:", Xp, " | q-free:", jet1_qfree)
print("power sums           : p1=%s p2=%s p3=%s | q-free: %s" % (p1, p2, p3, psums_qfree))
print("anchor a_D^(3)=(q+1)²/(3q) q-dependent:", anchor_qdep)

verdict = (
    "(b)-EXCLUSION of the CLASSICAL-jet identification a_D^(n)=∮λ_SW^(n): the color spectral cubic, "
    "its classical jets (d/dz), and all color-root power sums are q-FREE polynomials in z, so any "
    "∮ over q-free cycles is q-INDEPENDENT — but a_D^(3)=(q+1)²/(3q) is q-DEPENDENT. Invariant cited: "
    "q-independence of classical-jet periods vs q-dependence of the anchor. Therefore the prolongation "
    "operator is NOT a classical jet; it MUST be a q-DIFFERENCE operator (the fibre q-difference kernel "
    "R(q,x) of the z2bn bean). The q-difference class is NOT excluded — it is the surviving/indicated "
    "direction. The explicit q-difference prolongation (and thus the residue derivation of the anchors) "
    "remains the open keystone; the anchors stay wired Wedderburn-H₄ inputs (a_D^(4)=Family-A flagged a "
    "CODATA near-match). No fit; nothing tuned."
)
out = {
  "description": ("z2bn lever-1 τ-derivation second probe: rigorous q-type-consistency constraint that "
                  "the λ_SW prolongation operator must be q-difference, not a classical jet."),
  "color_cubic": "X^3+(z+1)X^2+(z^2+z+1)X+(z^3+z^2+z+1) (q-free)",
  "classical_1_jet_dX_dz": str(Xp),
  "color_root_power_sums": {"p1": str(p1), "p2": str(p2), "p3": str(p3)},
  "q_free": {"cubic": bool(cubic_qfree), "classical_jet": bool(jet1_qfree), "power_sums": bool(psums_qfree)},
  "anchor_a_D3": "(q+1)^2/(3q)", "anchor_q_dependent": bool(anchor_qdep),
  "lambda_sw_prolongation_status": ("inductive only (1-jet=dX, higher by induction); NO explicit "
                                     "closed form in corpus — cannot integrate directly yet"),
  "anchors_status": ("production-wired Wedderburn-H4 inputs; identification ∮λ_SW^(n)=a_D^(n) is the "
                     "OPEN keystone; a_D^(4)=Family-A is a CODATA-implied near-match"),
  "verdict": verdict,
}
wpath = "computations/substrate/z2bn-prolongation-qdifference-constraint.witness.json"
with open(wpath, "w") as fh:
    json.dump(out, fh, indent=2, ensure_ascii=False)
print("\nwitness ->", wpath)

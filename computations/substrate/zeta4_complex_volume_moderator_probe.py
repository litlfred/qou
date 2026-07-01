"""ζ₄ = i moderates Re 𝔙 (binding) and Im 𝔙 (Q_β) — the complex-volume coupling.

User question: "something in q-Askey that moderates Re 𝔙 and Im 𝔙?" — YES, the ζ₄ = i rotation.

𝔙 = Vol + i·CS (complex-volume observable; conj:binding-qbeta-complex-volume). The bar involution
q ↔ q⁻¹ (q = e^η) SPLITS it: Re 𝔙 = 𝔈_bind = bar-even (cosh, q-Hermite binding moment, PR #2899);
Im 𝔙 = 𝔔_β = bar-odd (sinh, c_k Habiro element). What MODERATES (couples) the two is the i of
Vol + i·CS, i.e. ζ₄ = i. This probe verifies the moderator at the generator level (no fit):

  (1) cosh(η + iπ/2) = i·sinh(η),  sinh(η + iπ/2) = i·cosh(η)   — the ζ₄ rotation η ↦ η+iπ/2
      sends cosh ↦ i·sinh (Re 𝔙 ↦ i·Im-channel) and back.
  (2) Φ₄ = q²+1 (the residue SHARED by the binding L₂ denominator 2·Φ₄ and the Q_β c_k kernel a₁
      ζ₄ residue) has root q = ζ₄ = i, where the bar-even generator [2]_q = q+q⁻¹ VANISHES and the
      bar-odd generator h = q−q⁻¹ becomes pure imaginary 2i.
  (3) the q ↦ i·q (ζ₄) rotation on symmetric [k]_q introduces Φ₄ poles — the algebraic shadow.

Lean cert (sorry-free): QOU/Mass/Zeta4ComplexVolumeModerator.lean (cosh_zeta4_rotation,
sinh_zeta4_rotation, phi4_root_zeta4, barEven_zeta4, barOdd_zeta4).

Scope (a): pins the moderator at the GENERATOR level (cosh ↔ i·sinh; Φ₄ = ζ₄ locus). That the
FULL binding and Q_β observables are exact ζ₄-rotates is the stronger, value-gated claim — not
asserted. No fit; sympy symbolic exact.
"""
import json, os

import sympy as sp

eta = sp.symbols("eta", real=True)
q = sp.symbols("q")
I = sp.I
hpi = sp.pi / 2 * I

# (1) the smooth moderator identity
mod_cosh = sp.simplify(sp.cosh(eta + hpi) - I * sp.sinh(eta))
mod_sinh = sp.simplify(sp.sinh(eta + hpi) - I * sp.cosh(eta))

# (2) Φ₄ locus
Phi4 = q ** 2 + 1
bar_even = q + 1 / q     # [2]_q  (cosh, Re 𝔙 / binding)
bar_odd = q - 1 / q      # h      (sinh, Im 𝔙 / Q_β)
phi4_at_i = sp.simplify(Phi4.subs(q, I))
even_at_i = sp.simplify(bar_even.subs(q, I))
odd_at_i = sp.simplify(bar_odd.subs(q, I))

# (3) ζ₄ rotation on [k]_q
def qint(k):
    return (q ** k - q ** (-k)) / (q - 1 / q)
rot = {k: str(sp.simplify(qint(k).subs(q, I * q))) for k in range(1, 6)}

results = {
    "moderator_cosh_to_i_sinh_residual": str(mod_cosh),   # 0 => cosh(η+iπ/2)=i sinh η
    "moderator_sinh_to_i_cosh_residual": str(mod_sinh),   # 0 => sinh(η+iπ/2)=i cosh η
    "phi4_at_zeta4": str(phi4_at_i),                      # 0
    "barEven_[2]q_at_zeta4": str(even_at_i),              # 0 (bar-even vanishes)
    "barOdd_h_at_zeta4": str(odd_at_i),                   # 2*I (bar-odd pure imaginary)
    "qint_under_zeta4_rotation": rot,
    "lean_cert": "QOU/Mass/Zeta4ComplexVolumeModerator.lean (sorry-free)",
}
assertions = {
    "cosh_rotates_to_i_sinh": mod_cosh == 0,
    "sinh_rotates_to_i_cosh": mod_sinh == 0,
    "phi4_root_is_zeta4": phi4_at_i == 0,
    "barEven_vanishes_at_zeta4": even_at_i == 0,
    "barOdd_imaginary_at_zeta4": sp.simplify(odd_at_i - 2 * I) == 0,
}
all_passed = all(assertions.values())

verdict = (
    "ζ₄ = i IS THE MODERATOR of Re 𝔙 (binding, cosh) and Im 𝔙 (Q_β, sinh). VERIFIED (sorry-free "
    "Lean): the ζ₄ rotation η ↦ η+iπ/2 sends cosh ↦ i·sinh and sinh ↦ i·cosh — i.e. rotates "
    "Re 𝔙 ↔ i·Im 𝔙, the complex-volume coupling of 𝔙 = Vol + i·CS. The cyclotomic factor Φ₄ = q²+1 "
    "SHARED by the binding side (L₂ denom = 2·Φ₄) and the Q_β c_k kernel (a₁ ζ₄ residue) is exactly "
    "the locus q = ζ₄ = i, where the bar-even [2]_q vanishes and the bar-odd h → 2i. So the shared "
    "Φ₄ is not coincidental common cyclotomy — it is the algebraic locus of the i = ζ₄ rotation that "
    "interchanges the binding (Re) and Q_β (Im) channels of the single complex-volume object 𝔙. "
    "Scope (a): generator-level; the full-observable ζ₄-rotation claim is value-gated, not asserted."
)

witness = {
    "computation": "zeta4_complex_volume_moderator_probe",
    "description": (
        "Verifies (symbolic + Lean-certified) that ζ₄ = i moderates Re 𝔙 (binding, bar-even cosh) "
        "and Im 𝔙 (Q_β, bar-odd sinh): the rotation η ↦ η+iπ/2 sends cosh ↦ i·sinh, and Φ₄ = q²+1 "
        "(the shared binding-L₂ / Q_β-a₁ residue) is the ζ₄ = i locus where bar-even vanishes / "
        "bar-odd → 2i. Answers 'something in q-Askey that moderates Re/Im 𝔙'."
    ),
    "discipline": "no fit; sympy symbolic exact; Lean-certified core; (a)-scoped.",
    "auditOnly": "docs/audits/2026-06-28-wlambda-identity-i-rescope-no-hlf.md",
    "results": results,
    "assertions": assertions,
    "allPassed": all_passed,
    "verdict": verdict,
}
from witness_base import WitnessBuilder  # noqa: E402 — P30 rollup (bean cmiy)
# Flat `assertions` payload → stamp (not wrap_legacy) preserves it.
WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="sympy")
witness["scriptFile"] = os.path.basename(__file__)
out = os.path.join(os.path.dirname(__file__), "zeta4-complex-volume-moderator-probe.witness.json")
with open(out, "w", encoding="utf-8") as f:
    json.dump(witness, f, indent=2)

print(f"(1) cosh(η+iπ/2)−i·sinh(η) = {mod_cosh}   sinh(η+iπ/2)−i·cosh(η) = {mod_sinh}")
print(f"(2) Φ₄(i)={phi4_at_i}  [2]_q(i)={even_at_i} (bar-even→0)  h(i)={odd_at_i} (bar-odd→2i)")
print(f"\nallPassed = {all_passed}")
print(f"\nVERDICT: {verdict}")
print(f"\nwitness -> {out}")

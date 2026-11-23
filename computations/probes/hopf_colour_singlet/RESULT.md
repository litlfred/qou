# Result: Hopf colour singlet probe (2026-11-22)

Pre-registration: `PREREGISTRATION.md`. Producer: `singlet_eigen_probe.py` (exact sympy over ℚ(q), ~0.4 s, stdout only, no witness).

All five pre-registered checks PASS.

1. Jimbo Ř for gl₃ is Hecke on V⊗V: (Ř − q)(Ř + q⁻¹) = 0.
2. Braid relation holds on V⊗³.
3. ker(Ř₁₂ + q⁻¹) ∩ ker(Ř₂₃ + q⁻¹) has dimension exactly 1.
4. At q = 1 the vector is the classical ε.
5. Weight (1,1,1), support on the 6 permutations.

Singlet vector:

ε_q = e123 − q⁻¹e132 − q⁻¹e213 + q⁻²e231 + q⁻²e312 − q⁻³e321.

So both braid generators act on the singlet by −q⁻¹. This verifies exactly the input
that `HopfColourTensorBraid.singlet_rescale` takes as a hypothesis (previously cited to
Jimbo / Kassel). Still cited, not computed here: that U_q(gl₃) commutes with Ř_c, so the
singlet line is a U_q(gl₃)-submodule.

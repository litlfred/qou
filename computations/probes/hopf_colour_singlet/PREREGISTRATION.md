# Pre-registration: Jimbo Ř on the gl₃ colour singlet (2026-11-22)

Written before running `singlet_eigen_probe.py`. Exact arithmetic over ℚ(q), sympy.

**Object.** V = ℂ³, Jimbo's U_q(gl₃) braiding
Ř = Σ_i q E_ii⊗E_ii + Σ_{i≠j} E_ji⊗E_ij + (q − q⁻¹) Σ_{i<j} E_jj⊗E_ii,
acting on V⊗V⊗V as Ř₁₂ = Ř⊗1, Ř₂₃ = 1⊗Ř.

**Predictions (each a pass/fail check, no tolerance).**
1. Ř satisfies (Ř − q)(Ř + q⁻¹) = 0 on V⊗V.
2. Ř₁₂Ř₂₃Ř₁₂ = Ř₂₃Ř₁₂Ř₂₃ on V⊗3.
3. The joint eigenspace ker(Ř₁₂ + q⁻¹) ∩ ker(Ř₂₃ + q⁻¹) in V⊗3 has dimension exactly 1
   over ℚ(q) (the q-antisymmetric singlet ε_q).
4. At q = 1 that vector specialises to the classical ε (signs of permutations, up to scale).
5. Its U_q(gl₃) weight is (1,1,1): only basis vectors e_a⊗e_b⊗e_c with {a,b,c} = {1,2,3} occur.

**What this settles.** The input cited (Jimbo / Kassel) in
`HopfColourTensorBraid.lean`: on the colour singlet the colour factor Ř_c acts by −q⁻¹.
If 3 fails, the singlet reduction X = −q⁻¹·b in that file has no carrier and the
tensor-route conclusion is withdrawn.

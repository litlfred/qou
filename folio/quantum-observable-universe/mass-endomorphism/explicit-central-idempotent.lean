import QOU.MassEndomorphism.MurphyLagrangeCentralIdempotents

set_option autoImplicit false

/-!
# Explicit central primitive idempotents in `H_n(q)` via Murphy elements

Companion sibling specialization for `prop:explicit-central-idempotent`, forwarding to the
all-`n` multiplicative Murphy–Lagrange construction in
`QOU.MassEndomorphism.MurphyLagrangeCentralIdempotents`:

- `murphyHeckeCentralIdem_sum_eq_one` (`∑_λ e_λ = 1` in `Hecke K q q⁻¹ n`),
- `murphyHeckeCentralIdem_mul` (`e_λ * e_μ = δ_{λ,μ} e_λ`),
- `murphyHeckeCentralIdem_idem` (`e_λ * e_λ = e_λ`),
- `murphyHeckeCentralIdem_comm` (`e_λ * x = x * e_λ` for all `x ∈ Hecke K q q⁻¹ n`).
-/

namespace QOU.MassEndomorphism.ExplicitCentralIdempotentSibling

open QOU.SchurWeyl
open QOU.MassEndomorphism.MurphyLagrangeCentralIdempotents

-- Ref: [murphy1981]
-- Ref: [dipper-james1986]
-- Ref: [ram1997]
/-- Unconditional four-strand (`H_4(q)`, `n = 3`) specialization of
`murphyHeckeCentralIdem`: for every partition `lam : Partition 4` (including `(2, 2)`),
`murphyHeckeCentralIdem q 3 lam` is a central idempotent in `Hecke K q q⁻¹ 3`. -/
theorem explicit_central_idempotent_h4 {K : Type*} [Field K] [CharZero K]
    (q : K) (hq0 : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q)
    (lam : Partition 4) :
    murphyHeckeCentralIdem q 3 lam * murphyHeckeCentralIdem q 3 lam =
      murphyHeckeCentralIdem q 3 lam ∧
    ∀ x : Hecke K q q⁻¹ 3,
      murphyHeckeCentralIdem q 3 lam * x = x * murphyHeckeCentralIdem q 3 lam :=
  ⟨murphyHeckeCentralIdem_idem q hq0 hq2 3 lam,
   murphyHeckeCentralIdem_comm q hq0 hq2 3 lam⟩

end QOU.MassEndomorphism.ExplicitCentralIdempotentSibling

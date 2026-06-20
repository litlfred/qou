/-!
# QOU.AppendixSurreals.WenzlPositivityImpliesSubstratePositivity

**Sibling-resolution stub** for content block
[`conj:wenzl-positivity-implies-substrate-positivity`](wenzl-positivity-implies-substrate-positivity.md):
*Wenzl positivity at q_0 implies substrate C*-Frobenius positivity*.

The §3b-cond class axiomatisation lives here. The class instance is
the **conjectural witness** (sorry = conjecture per AGENTS.md §3b),
not a missing proof. The class bridges the downstream
`OSReflectionPositivity` typeclass and a future
`WenzlPositivityAt(q_0)` typeclass on the upstream side — granting
this instance, OS reflection positivity reduces to Wenzl's classical
positivity theorem for Rep(U_q(sl_2)) at q_0 ∈ R_{>1}.

-- Ref: [manuscript] quantum-observable-universe/appendix-surreals/wenzl-positivity-implies-substrate-positivity.ts
-- Ref: [wenzl1988] Wenzl, "Hecke algebras of type A_n and subfactors," Invent. Math. 92 (1988)
-/

namespace QOU.AppendixSurreals

/-- **CONJECTURE.** Wenzl positivity of Rep(U_q(sl_2)) at q = q_0
    ∈ R_{>1} implies the substrate C*-Frobenius positivity axiom
    needed by `OSReflectionPositivity`. -/
class WenzlPositivityImpliesSubstratePositivity where
  /-- The bridge claim: Wenzl-positivity of Rep(U_q(sl_2)) at q_0
      ∈ R_{>1} implies substrate C*-Frobenius positivity (Müger /
      BKLR sense) of the QOU Frobenius–Hopf substrate. The class
      instance is the §3b-cond conjectural witness. -/
  -- Ref: [manuscript] conj:wenzl-positivity-implies-substrate-positivity
  holds : Prop

end QOU.AppendixSurreals

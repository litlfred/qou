import Mathlib.Tactic

/-!
# QOU.Archimedean.TypedGarsideElement

**Canonical declaration** for content block at
[`quantum-observable-universe/particle-interactions/typed-garside-element.ts`](quantum-observable-universe/particle-interactions/typed-garside-element.ts).

Formalises the manuscript **definition** of the typed Garside element
`𝒢(t₀,…,t_{A-1}) ∈ H_A(q)`: the Garside staircase of typed crossings, one
`C(t_j, t_{ℓ+1}; σ_j) = σ_j + d(t_j, t_{ℓ+1})` per nucleon pair. The
structure below pins the concrete crossing-coefficient table `d` and the
`binom(A, 2)` factor count. (§7c: archimedean over `ℝ` — `d` uses
`q − q⁻¹`.)
-/

namespace QOU.Archimedean

/-- Nucleon type: proton `p` or neutron `n`. -/
inductive Nucleon
  | p
  | n
deriving DecidableEq

/-- Data for the typed Garside element `𝒢(t₀,…,t_{A-1})`.

    A `definition` carrier: the substrate parameter `q`, the typed-crossing
    coefficient table `d`, its four defining values (manuscript
    `d(p,p)=0`, `d(n,n)=-(q-q⁻¹)`, `d(p,n)=d(n,p)=-½(q-q⁻¹)`), the nucleon
    count `A`, and the crossing-factor count `= binom(A,2)` (one factor per
    nucleon pair). -/
structure TypedGarsideElement where
  /-- Substrate parameter `q`. -/
  q : ℝ
  /-- Typed-crossing coefficient `d(f_i, f_j)` in `C = σ + d`. -/
  d : Nucleon → Nucleon → ℝ
  /-- `d(p,p) = 0`. -/
  d_pp : d Nucleon.p Nucleon.p = 0
  /-- `d(n,n) = -(q − q⁻¹)`. -/
  d_nn : d Nucleon.n Nucleon.n = -(q - q⁻¹)
  /-- `d(p,n) = -½(q − q⁻¹)`. -/
  d_pn : d Nucleon.p Nucleon.n = -(1 / 2) * (q - q⁻¹)
  /-- `d(n,p) = -½(q − q⁻¹)`. -/
  d_np : d Nucleon.n Nucleon.p = -(1 / 2) * (q - q⁻¹)
  /-- Nucleon count `A = Z + N`. -/
  A : ℕ
  /-- Number of crossing factors in the staircase. -/
  numFactors : ℕ
  /-- The staircase has one factor per nucleon pair: `binom(A, 2)`. -/
  numFactors_eq : numFactors = A.choose 2

-- Ref: [leitner2026] quantum-observable-universe/particle-interactions/typed-garside-element.ts

/-- The typed-crossing coefficient is symmetric on a mixed proton–neutron
    pair (manuscript: `d(p,n) = d(n,p)`). -/
theorem d_mixed_symm (G : TypedGarsideElement) :
    G.d Nucleon.p Nucleon.n = G.d Nucleon.n Nucleon.p := by
  rw [G.d_pn, G.d_np]

/-- A single nucleon carries no crossing factors (`binom(1,2) = 0`). -/
theorem numFactors_one
    (G : TypedGarsideElement) (h : G.A = 1) : G.numFactors = 0 := by
  rw [G.numFactors_eq, h]
  decide

end QOU.Archimedean

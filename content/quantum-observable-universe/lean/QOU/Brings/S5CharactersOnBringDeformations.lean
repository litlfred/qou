import Mathlib.Data.Fin.VecNotation

/-!
# `S_5` on the deformations of Bring's curve — the character arithmetic

The first-order deformation space `H¹(T_C)` of Bring's curve `C = Σ₄` is a
representation of its automorphism group `S₅`.  Two content blocks state its
decomposition, `H¹(T_C) ≅ [4,1] ⊕ [3,2]`, and draw consequences from it: no
`S₅`-invariant deformation (rigidity), no invariant symplectic form on the
deformation space, and a one-dimensional space of equivariant "actions"
`V₄ ⊗ [3,2] → [3,2]`.

This file proves the **arithmetic half** of those statements by kernel
evaluation, from the character table of `S₅` taken as input:

* `charTable` — the seven irreducible characters of `S₅` on its seven
  conjugacy classes, in the order `1⁵, 2·1³, 2²·1, 3·1², 3·2, 4·1, 5`, with
  class sizes `1, 10, 15, 20, 20, 30, 24` (Fulton–Harris, *Representation
  Theory*, §2.3; James–Kerber, *The Representation Theory of the Symmetric
  Group*).  It is a **definition with a citation, not a theorem**: nothing in
  this file derives the table.  `charTable_orthonormal` checks that the
  input is at least an orthonormal system for the class-weighted inner
  product, which any character table must be.
* The symmetric and exterior powers are computed by the power-sum formulas
  `2·χ_{Sym²}(g) = χ(g)² + χ(g²)`, `2·χ_{Λ²}(g) = χ(g)² − χ(g²)`,
  `6·χ_{Sym³}(g) = χ(g)³ + 3χ(g)χ(g²) + 2χ(g³)`.  To stay in `ℤ` and avoid
  division, the file works with the **scaled** characters `2·χ_{Sym²}`,
  `2·χ_{Λ²}`, `6·χ_{Sym³}` throughout, and every multiplicity statement is
  scaled accordingly: `inner (2·χ) ψ = 240` means `⟨χ, ψ⟩ = 1`.
* `h1TangentSix` is `6·χ_{H¹(T_C)}` computed by the complete-intersection
  route, `H¹(T_C) = H⁰(N_C) − 𝔰𝔩(V₄)` with `N_C = 𝒪_C(2) ⊕ 𝒪_C(3)`; the
  **geometric** inputs of that route (the normal-bundle splitting,
  `H⁰(T_C) = 0`, `H¹(T_{ℙ³}|_C) = 0`) are theorems of algebraic geometry
  cited in the content block, not formalised here.

Every theorem below is a closed equality in `ℤ` and is discharged by
`decide`; this is a genuinely finite computation, not a laundering of a
structural claim (AGENTS.md §Strict Lean Discipline, item 6).

Companion probe (same numbers, exact `Fraction` arithmetic, plus a brute-force
check of the power-sum formulas over all 120 permutations):
`computations/audits/bring_h1_tangent_ci_route_and_v4_on_32_probe.py`.
-/

namespace QOU.Brings.S5Char

/-- Class sizes of `S₅` in the order `1⁵, 2·1³, 2²·1, 3·1², 3·2, 4·1, 5`. -/
def classSize : Fin 7 → ℤ := ![1, 10, 15, 20, 20, 30, 24]

/-- The class of `g²` for `g` in each class: `(2·1³)² = 1⁵`, `(2²·1)² = 1⁵`,
`(3·2)² = 3·1²`, `(4·1)² = 2²·1`, and the odd-order classes are fixed. -/
def sq : Fin 7 → Fin 7 := ![0, 0, 0, 3, 3, 2, 6]

/-- The class of `g³`: `(3·1²)³ = 1⁵`, `(3·2)³ = 2·1³`, and the classes of
order prime to `3` are fixed. -/
def cube : Fin 7 → Fin 7 := ![0, 1, 2, 0, 1, 5, 6]

/-- `120 · ⟨χ, ψ⟩ = Σ_classes |class| · χ · ψ`  (characters are real, so no
conjugation is needed). -/
def inner (χ ψ : Fin 7 → ℤ) : ℤ :=
  classSize 0 * χ 0 * ψ 0 + classSize 1 * χ 1 * ψ 1 + classSize 2 * χ 2 * ψ 2 +
  classSize 3 * χ 3 * ψ 3 + classSize 4 * χ 4 * ψ 4 + classSize 5 * χ 5 * ψ 5 +
  classSize 6 * χ 6 * ψ 6

/-- The character table of `S₅` — **input, cited** (Fulton–Harris §2.3). -/
def chiTriv : Fin 7 → ℤ := ![1, 1, 1, 1, 1, 1, 1]
def chiSign : Fin 7 → ℤ := ![1, -1, 1, 1, -1, -1, 1]
/-- `[4,1]`, the standard representation `V₄ = {Σ xᵢ = 0} ⊂ k⁵`. -/
def chiStd : Fin 7 → ℤ := ![4, 2, 0, 1, -1, 0, -1]
def chi2111 : Fin 7 → ℤ := ![4, -2, 0, 1, 1, 0, -1]
/-- `[3,2]`, five-dimensional. -/
def chi32 : Fin 7 → ℤ := ![5, 1, 1, -1, 1, -1, 0]
def chi221 : Fin 7 → ℤ := ![5, -1, 1, -1, -1, 1, 0]
def chi311 : Fin 7 → ℤ := ![6, 0, -2, 0, 0, 0, 1]

/-- The input table is orthonormal for `inner / 120` — the minimal sanity
check that these seven vectors could be a character table at all. -/
theorem charTable_orthonormal :
    inner chiTriv chiTriv = 120 ∧ inner chiSign chiSign = 120 ∧
    inner chiStd chiStd = 120 ∧ inner chi2111 chi2111 = 120 ∧
    inner chi32 chi32 = 120 ∧ inner chi221 chi221 = 120 ∧
    inner chi311 chi311 = 120 ∧
    inner chiTriv chiSign = 0 ∧ inner chiTriv chiStd = 0 ∧ inner chiTriv chi2111 = 0 ∧
    inner chiTriv chi32 = 0 ∧ inner chiTriv chi221 = 0 ∧ inner chiTriv chi311 = 0 ∧
    inner chiSign chiStd = 0 ∧ inner chiSign chi2111 = 0 ∧ inner chiSign chi32 = 0 ∧
    inner chiSign chi221 = 0 ∧ inner chiSign chi311 = 0 ∧
    inner chiStd chi2111 = 0 ∧ inner chiStd chi32 = 0 ∧ inner chiStd chi221 = 0 ∧
    inner chiStd chi311 = 0 ∧
    inner chi2111 chi32 = 0 ∧ inner chi2111 chi221 = 0 ∧ inner chi2111 chi311 = 0 ∧
    inner chi32 chi221 = 0 ∧ inner chi32 chi311 = 0 ∧ inner chi221 chi311 = 0 := by
  decide

/-- `2 · χ_{Sym² W}` from `χ_W`. -/
def sym2Twice (χ : Fin 7 → ℤ) : Fin 7 → ℤ := fun i => χ i * χ i + χ (sq i)
/-- `2 · χ_{Λ² W}` from `χ_W`. -/
def alt2Twice (χ : Fin 7 → ℤ) : Fin 7 → ℤ := fun i => χ i * χ i - χ (sq i)
/-- `6 · χ_{Sym³ W}` from `χ_W`. -/
def sym3Six (χ : Fin 7 → ℤ) : Fin 7 → ℤ :=
  fun i => χ i * χ i * χ i + 3 * χ i * χ (sq i) + 2 * χ (cube i)
/-- `χ_{W ⊗ W'}`. -/
def tensor (χ ψ : Fin 7 → ℤ) : Fin 7 → ℤ := fun i => χ i * ψ i

/-- `Sym² V₄ = [5] ⊕ [4,1] ⊕ [3,2]` (all statements scaled by 2). -/
theorem sym2_std :
    inner (sym2Twice chiStd) chiTriv = 240 ∧ inner (sym2Twice chiStd) chiStd = 240 ∧
    inner (sym2Twice chiStd) chi32 = 240 ∧ inner (sym2Twice chiStd) chiSign = 0 ∧
    inner (sym2Twice chiStd) chi2111 = 0 ∧ inner (sym2Twice chiStd) chi221 = 0 ∧
    inner (sym2Twice chiStd) chi311 = 0 ∧ sym2Twice chiStd 0 = 20 := by
  decide

/-- `Λ² V₄ = [3,1,1]` is irreducible: no `S₅`-invariant symplectic form on `V₄`. -/
theorem alt2_std :
    inner (alt2Twice chiStd) chi311 = 240 ∧ inner (alt2Twice chiStd) chiTriv = 0 ∧
    inner (alt2Twice chiStd) chiSign = 0 ∧ inner (alt2Twice chiStd) chiStd = 0 ∧
    inner (alt2Twice chiStd) chi2111 = 0 ∧ inner (alt2Twice chiStd) chi32 = 0 ∧
    inner (alt2Twice chiStd) chi221 = 0 ∧ alt2Twice chiStd 0 = 12 := by
  decide

/-- `Sym³ V₄ = [5] ⊕ 2[4,1] ⊕ [3,2] ⊕ [3,1,1]` (scaled by 6). -/
theorem sym3_std :
    inner (sym3Six chiStd) chiTriv = 720 ∧ inner (sym3Six chiStd) chiStd = 1440 ∧
    inner (sym3Six chiStd) chi32 = 720 ∧ inner (sym3Six chiStd) chi311 = 720 ∧
    inner (sym3Six chiStd) chiSign = 0 ∧ inner (sym3Six chiStd) chi2111 = 0 ∧
    inner (sym3Six chiStd) chi221 = 0 ∧ sym3Six chiStd 0 = 120 := by
  decide

/-- The identity that makes the complete-intersection route agree with the
Serre–Noether route: `Sym³ V₄ ≅ V₄ ⊗ V₄ ⊕ V₄`, as characters (scaled by 6). -/
theorem sym3_eq_tensor_add_std :
    ∀ i, sym3Six chiStd i = 6 * (tensor chiStd chiStd i + chiStd i) := by
  decide

/-- `6 · χ_{H¹(T_C)}` by the complete-intersection route:
`H¹(T_C) = [Sym² V − 1] + [Sym³ V − 1 − V] − [V ⊗ V − 1]`. -/
def h1TangentSix : Fin 7 → ℤ := fun i =>
  3 * sym2Twice chiStd i - 6 + (sym3Six chiStd i - 6 - 6 * chiStd i)
    - (6 * tensor chiStd chiStd i - 6)

/-- **`H¹(T_C) ≅ [4,1] ⊕ [3,2]`**, of dimension `9 = 3g − 3`, with no trivial
and no sign summand: Bring's curve has no `S₅`-invariant first-order
deformation. -/
theorem h1Tangent_decomposition :
    inner h1TangentSix chiStd = 720 ∧ inner h1TangentSix chi32 = 720 ∧
    inner h1TangentSix chiTriv = 0 ∧ inner h1TangentSix chiSign = 0 ∧
    inner h1TangentSix chi2111 = 0 ∧ inner h1TangentSix chi221 = 0 ∧
    inner h1TangentSix chi311 = 0 ∧ h1TangentSix 0 = 54 := by
  decide

/-- The Serre–Noether route gives the same virtual character:
`6 · (Sym² V₄ − 1) = h1TangentSix` on every class. -/
theorem h1Tangent_eq_noether :
    ∀ i, h1TangentSix i = 3 * sym2Twice chiStd i - 6 := by
  decide

/-- `V₄ ⊗ [3,2] = [4,1] ⊕ [3,2] ⊕ [3,1,1] ⊕ [2,2,1]`: in particular
`Hom_{S₅}(V₄ ⊗ [3,2], [3,2])` and `Hom_{S₅}(V₄ ⊗ [3,2], V₄)` are each
**one-dimensional** — `V₄` acts on the five-space equivariantly in exactly one
way up to scale, and pairs with it into itself in exactly one way. -/
theorem std_tensor_32 :
    inner (tensor chiStd chi32) chiStd = 120 ∧ inner (tensor chiStd chi32) chi32 = 120 ∧
    inner (tensor chiStd chi32) chi311 = 120 ∧ inner (tensor chiStd chi32) chi221 = 120 ∧
    inner (tensor chiStd chi32) chiTriv = 0 ∧ inner (tensor chiStd chi32) chiSign = 0 ∧
    inner (tensor chiStd chi32) chi2111 = 0 := by
  decide

/-- `Sym² [3,2]` has exactly one invariant (the symmetric self-duality form on
the block) and `Λ² [3,2]` has none: no invariant symplectic form on `[3,2]`. -/
theorem forms_on_32 :
    inner (sym2Twice chi32) chiTriv = 240 ∧ inner (alt2Twice chi32) chiTriv = 0 := by
  decide

/-- `χ_{H¹(T_C)}` itself.  `h1TangentSix` is divisible by `6` on every class
(`six_mul_h1Tangent` certifies it), so this is an honest character, and the
symmetric/exterior-square formulas — which are not linear in `χ` — can be
applied to it directly. -/
def h1Tangent : Fin 7 → ℤ := fun i => h1TangentSix i / 6

theorem six_mul_h1Tangent : ∀ i, 6 * h1Tangent i = h1TangentSix i := by
  decide

/-- On the whole nine-dimensional deformation space: two invariant symmetric
forms (one per summand) and **no** invariant alternating form — there is no
`S₅`-invariant symplectic structure on `H¹(T_C)`.  (`sym2Twice`/`alt2Twice`
are the characters of `Sym²`/`Λ²` scaled by 2, so `480 = 2 · 120 · 2`.) -/
theorem forms_on_h1Tangent :
    h1Tangent 0 = 9 ∧
    inner (sym2Twice h1Tangent) chiTriv = 480 ∧
    inner (alt2Twice h1Tangent) chiTriv = 0 := by
  decide

/-- The `S₅`-invariants of the Hochschild (co)homology of the base curve, via
HKR and Serre duality (`H⁰(K) = V₄`, `H¹(𝒪) = V₄`, `H¹(K) = 𝟙 = H⁰(𝒪)`,
`H⁰(T) = 0`): invariants live only in `HH₀ = H⁰(𝒪) ⊕ H¹(K)` (dimension 2)
and `HH⁰ = H⁰(𝒪)` (dimension 1); `HH₁ = H⁰(K)`, `HH₋₁ = H¹(𝒪)`,
`HH¹ = H¹(𝒪)` and `HH² = H¹(T)` have none.  Scaled by 6 where `h1TangentSix`
enters. -/
theorem hochschild_invariants_of_base :
    inner chiStd chiTriv = 0 ∧                       -- HH₁, HH₋₁, HH¹ : no invariant
    inner (fun i => chiTriv i + chiTriv i) chiTriv = 240 ∧   -- HH₀ : two invariants
    inner chiTriv chiTriv = 120 ∧                     -- HH⁰ : one invariant
    inner h1TangentSix chiTriv = 0 := by              -- HH² : no invariant
  decide

/-- The alternating sums: over the invariant homology, `2 − 0 − 0 = χ(ℙ¹)`;
over the full homology, `2 − 4 − 4 = −6 = χ_eu(Σ₄)`. -/
theorem euler_characteristics :
    (2 : ℤ) - 0 - 0 = 2 ∧ (2 : ℤ) - chiStd 0 - chiStd 0 = -6 := by
  decide

end QOU.Brings.S5Char

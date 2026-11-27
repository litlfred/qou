import QOU.BraidsAndKnots.RationalAssociator.AssociatorTower
import QOU.BraidsAndKnots.RationalAssociator.HexagonUniversal
import HeckeTemperleyLieb.QuasiYangBaxterFromHexagon

/-!
# The quasi-Yang–Baxter equation for the rational associator tower

Bean `qou-3fdg` (stage 5 of the rational-associator plan, epic `qou-dk7p`).

`HeckeTemperleyLieb.QuasiYangBaxterFromHexagon.quasiYBE_of_hexagon` proves the quasi-Yang–Baxter
equation in `(A ⊗ A) ⊗ A` from a coproduct `Δ`, an element `R`, quasi-cocommutativity and the
hexagon `(Δ ⊗ id)(R) = P · R₁₃ · Q · R₂₃ · Φ`. The rational associators of this directory live in
a different place: they are polynomials `Φ ∈ ℚ⟨X, Y⟩` whose hexagon holds in the universal
truncated algebra `U4 N` (`AssocU4`). This file connects the two.

**Which reading.** A concrete quasi-triangular instance `(A, Δ, R)` over `ℚ` needs a realisation
`t_ij ↦ h Ω_ij` of the Drinfeld–Kohno algebra by a Casimir tensor in `U(𝔤)^{⊗3}[h]/(h^N)`. That
realisation (invariance of `Ω`, hence the Drinfeld–Kohno relations among the `Ω_ij`) is not in
this repository. So the deliverable here is reading (b): the universal statement in `U4 N`, plus
the transport to every realisation.

* `quasiYBE_of_hexagons`: in any `ℚ`-algebra, for a `DK3` family `(a, b, c) = (t₁₂, t₁₃, t₂₃)`,
  the hexagons of `φ` at `(a, b, c)` and at the leg-swapped family `(a, c, b)` imply

    `e(t₁₂) φ(t₁₃,t₁₂) e(t₁₃) φ(t₂₃,t₁₃) e(t₂₃) φ(t₁₂,t₂₃)
       = φ(t₂₃,t₁₂) e(t₂₃) φ(t₁₃,t₂₃) e(t₁₃) φ(t₁₂,t₁₃) e(t₁₂)`,

  with `e(x) = E(x)`. With `R_ij = e(t_ij)`, `Φ₁₂₃ = φ(t₁₂, t₂₃)` and the leg-permuted associators
  `Φ₃₁₂ = φ(t₁₃, t₁₂)`, `Φ₁₃₂⁻¹ = φ(t₂₃, t₁₃)` (by (5.12)), `Φ₃₂₁ = φ(t₂₃, t₁₂)`,
  `Φ₂₃₁⁻¹ = φ(t₁₃, t₂₃)`, `Φ₂₁₃ = φ(t₁₂, t₁₃)`, this is the quasi-Yang–Baxter equation
  `R₁₂ Φ₃₁₂ R₁₃ Φ₁₃₂⁻¹ R₂₃ Φ = Φ₃₂₁ R₂₃ Φ₂₃₁⁻¹ R₁₃ Φ₂₁₃ R₁₂`. The proof is the same one-line
  argument as `quasiYBE_of_hexagon`: both sides equal `e(t₁₂) e(t₁₃ + t₂₃)`, and `t₁₂` commutes
  with `t₁₃ + t₂₃`. Quasi-cocommutativity is replaced by that Drinfeld–Kohno relation.
* `quasiYBE_U4`, `quasiYBE_of_assocU4`: in `U4 N`, the hexagon at the universal family alone
  suffices; the swapped hexagon is its image under `hexagon_of_universal`.
* `quasiYBE_compatible_of_tower`: the compatible rational tower of `AssociatorTower.lean`
  satisfies the quasi-Yang–Baxter equation in `U4 N` for every `N ≥ 2`, conditional on the
  named `K`-associator tower hypothesis.
* `quasiYBE_of_realization`: for any `ℚ`-algebra `A` and algebra map `ρ : U4 N → (A ⊗ A) ⊗ A`
  carrying `e(t₁₂), e(t₁₃), e(t₂₃)` to `R₁₂, R₁₃, R₂₃`, the quasi-Yang–Baxter equation holds in
  `(A ⊗ A) ⊗ A` with the `ρ`-images of the rational associators. No coproduct is needed.
* `hexagon_of_realization`, `quasiYBE_of_hexagon_realization`: if moreover
  `ρ(e(t₁₃ + t₂₃)) = (Δ ⊗ id)(R)`, the hypothesis `hhex` of `quasiYBE_of_hexagon` holds with
  `P, Q, Φ` the `ρ`-images of `φ(t₁₃,t₁₂)`, `φ(t₂₃,t₁₃)`, `φ(t₁₂,t₂₃)`, and that theorem applies.

The braid relation `σ₁σ₂σ₁ = σ₂σ₁σ₂` for `σ₁ = s₁₂R₁₂`, `σ₂ = Φ⁻¹s₂₃R₂₃Φ` is equivalent to the
quasi-Yang–Baxter equation after moving the permutations to one side; that rewriting needs the
semidirect product with `S₃` and is not done here. Nothing analytic is used.
-/

namespace QOU.BraidsAndKnots.RationalAssociator

open QOU.HeckeTemperleyLieb.QuasiYangBaxterFromHexagon

/-! ### The universal statement in any `ℚ`-algebra -/

section General

variable {R : Type*} [Ring R] [Algebra ℚ R]

omit [Algebra ℚ R] in
/-- The leg swap `1 ↔ 2` preserves the Drinfeld–Kohno relations on three strands:
`(t₁₂, t₁₃, t₂₃) ↦ (t₁₂, t₂₃, t₁₃)`. -/
theorem DK3.legSwap12 {a b c : R} (h : DK3 a b c) : DK3 a c b := by
  refine ⟨?_, ?_, ?_⟩
  · rw [add_comm]; exact h.n12_3
  · exact h.n23_1
  · exact h.n13_2

/-- **Quasi-Yang–Baxter from the two hexagons.** For a `DK3` family `(a, b, c) = (t₁₂, t₁₃, t₂₃)`
in a `ℚ`-algebra, if `φ` satisfies the hexagon (exponential `E`) at `(a, b, c)` and at the
leg-swapped family `(a, c, b)`, then

  `e(a) · φ(b,a) e(b) φ(c,b) e(c) φ(a,c) = φ(c,a) e(c) φ(b,c) e(b) φ(a,b) · e(a)`,

where `e(x) = eval x 0 E`. -/
theorem quasiYBE_of_hexagons (φ E : FreeAlgebra ℚ (Fin 2)) {a b c : R} (h : DK3 a b c)
    (hex : Hexagon φ E a b c) (hexs : Hexagon φ E a c b) :
    eval a 0 E * (eval b a φ * eval b 0 E * eval c b φ * eval c 0 E * eval a c φ) =
      eval c a φ * eval c 0 E * eval b c φ * eval b 0 E * eval a b φ * eval a 0 E := by
  unfold Hexagon at hex hexs
  rw [← hex, ← hexs, add_comm c b]
  have hc : Commute (eval (b + c) 0 E) a :=
    commute_eval h.n12_3.symm (Commute.zero_left a) E
  exact (commute_eval hc.symm (Commute.zero_left _) E).eq

end General

/-! ### In the universal truncated algebra `U4 N` -/

section U4

variable {N : ℕ}

/-- `(t₁₂, t₁₃, t₂₃)` of `U4 N` as a `DK3` family. -/
theorem dk3_U4 (N : ℕ) : DK3 (t N 0) (t N 1) (t N 3) := (dk4 N).d4

/-- **The quasi-Yang–Baxter equation in `U4 N` from the universal hexagon.** If `φ` satisfies the
hexagon with exponential `E` at the universal three-strand family of `U4 N`, then

  `e(t₁₂) φ(t₁₃,t₁₂) e(t₁₃) φ(t₂₃,t₁₃) e(t₂₃) φ(t₁₂,t₂₃)
     = φ(t₂₃,t₁₂) e(t₂₃) φ(t₁₃,t₂₃) e(t₁₃) φ(t₁₂,t₁₃) e(t₁₂)`

in `U4 N`. -/
theorem quasiYBE_U4 (φ E : FreeAlgebra ℚ (Fin 2)) (hφ : Hexagon φ E (t N 0) (t N 1) (t N 3)) :
    eval (t N 0) 0 E * (eval (t N 1) (t N 0) φ * eval (t N 1) 0 E * eval (t N 3) (t N 1) φ *
        eval (t N 3) 0 E * eval (t N 0) (t N 3) φ) =
      eval (t N 3) (t N 0) φ * eval (t N 3) 0 E * eval (t N 1) (t N 3) φ * eval (t N 1) 0 E *
        eval (t N 0) (t N 1) φ * eval (t N 0) 0 E := by
  have hs : Hexagon φ E (t N 0) (t N 3) (t N 1) :=
    hexagon_of_universal φ E hφ (dk3_U4 N).legSwap12 (t_mem_Fil_one 0) (t_mem_Fil_one 3)
      (t_mem_Fil_one 1)
  exact quasiYBE_of_hexagons φ E (dk3_U4 N) hφ hs

/-- **Every rational associator in `U4 N` satisfies the quasi-Yang–Baxter equation there.** -/
theorem quasiYBE_of_assocU4 {E Φ : FreeAlgebra ℚ (Fin 2)} (hΦ : AssocU4 N E Φ) :
    eval (t N 0) 0 E * (eval (t N 1) (t N 0) Φ * eval (t N 1) 0 E * eval (t N 3) (t N 1) Φ *
        eval (t N 3) 0 E * eval (t N 0) (t N 3) Φ) =
      eval (t N 3) (t N 0) Φ * eval (t N 3) 0 E * eval (t N 1) (t N 3) Φ * eval (t N 1) 0 E *
        eval (t N 0) (t N 1) Φ * eval (t N 0) 0 E :=
  quasiYBE_U4 Φ E hΦ.hex

end U4

/-! ### The compatible rational tower -/

section Tower

variable {K : Type*} [Field K] [Algebra ℚ K]

/-- **The compatible rational tower satisfies the quasi-Yang–Baxter equation at every level.**
Conditional on a compatible tower of group-like `K`-associators for `E`
(`CompatibleGroupLikeKAssociatorTower`, the named analytic input), there is one sequence
`Φ : ℕ → ℚ⟨X, Y⟩` with compatible truncations (`Φ (N + 1) − Φ N ∈ FF N`), each `Φ N` a
group-like associator in `U4 N`, and each `Φ N` satisfying the quasi-Yang–Baxter equation in
`U4 N`. -/
theorem quasiYBE_compatible_of_tower {E : FreeAlgebra ℚ (Fin 2)}
    (hE : FreeAlgebra.algebraMapInv E = 1) (hT : CompatibleGroupLikeKAssociatorTower K E) :
    ∃ Φ : ℕ → FreeAlgebra ℚ (Fin 2),
      (∀ N, 2 ≤ N → AssocU4 N E (Φ N) ∧ GL N (Φ N) ∧
        eval (t N 0) 0 E * (eval (t N 1) (t N 0) (Φ N) * eval (t N 1) 0 E *
            eval (t N 3) (t N 1) (Φ N) * eval (t N 3) 0 E * eval (t N 0) (t N 3) (Φ N)) =
          eval (t N 3) (t N 0) (Φ N) * eval (t N 3) 0 E * eval (t N 1) (t N 3) (Φ N) *
            eval (t N 1) 0 E * eval (t N 0) (t N 1) (Φ N) * eval (t N 0) 0 E) ∧
      ∀ N, 1 ≤ N → Φ (N + 1) - Φ N ∈ FF N := by
  obtain ⟨Φ, hA, hC⟩ := rational_associator_compatible_of_tower hE hT
  exact ⟨Φ, fun N hN => ⟨(hA N hN).1, (hA N hN).2, quasiYBE_of_assocU4 (hA N hN).1⟩, hC⟩

end Tower

/-! ### Transport to `(A ⊗ A) ⊗ A` -/

section Realization

open scoped TensorProduct

variable {N : ℕ} {A : Type*} [Ring A] [Algebra ℚ A]

/-- **Quasi-Yang–Baxter in `(A ⊗ A) ⊗ A` from a realisation of `U4 N`.** Let `ρ : U4 N → (A ⊗ A) ⊗ A`
be a `ℚ`-algebra map carrying `e(t₁₂), e(t₁₃), e(t₂₃)` to `R₁₂, R₁₃, R₂₃`. If `Φ` is a rational
associator in `U4 N`, then with `P = ρ φ(t₁₃,t₁₂)`, `Q = ρ φ(t₂₃,t₁₃)`, `Φ₁₂₃ = ρ φ(t₁₂,t₂₃)` and
`P' = ρ φ(t₂₃,t₁₂)`, `Q' = ρ φ(t₁₃,t₂₃)`, `Φ₂₁₃ = ρ φ(t₁₂,t₁₃)`:

  `R₁₂ · P R₁₃ Q R₂₃ Φ₁₂₃ = P' R₂₃ Q' R₁₃ Φ₂₁₃ · R₁₂`. -/
theorem quasiYBE_of_realization {E Φ : FreeAlgebra ℚ (Fin 2)} (hΦ : AssocU4 N E Φ)
    (ρ : U4 N →ₐ[ℚ] (A ⊗[ℚ] A) ⊗[ℚ] A) (R : A ⊗[ℚ] A)
    (h12 : ρ (eval (t N 0) 0 E) = leg12 R) (h13 : ρ (eval (t N 1) 0 E) = leg13 R)
    (h23 : ρ (eval (t N 3) 0 E) = leg23 R) :
    leg12 R * (ρ (eval (t N 1) (t N 0) Φ) * leg13 R * ρ (eval (t N 3) (t N 1) Φ) * leg23 R *
        ρ (eval (t N 0) (t N 3) Φ)) =
      ρ (eval (t N 3) (t N 0) Φ) * leg23 R * ρ (eval (t N 1) (t N 3) Φ) * leg13 R *
        ρ (eval (t N 0) (t N 1) Φ) * leg12 R := by
  have key := congrArg ρ (quasiYBE_of_assocU4 hΦ)
  simp only [map_mul, h12, h13, h23] at key
  exact key

/-- **The hexagon hypothesis of `quasiYBE_of_hexagon` from a rational associator.** If a
`ℚ`-algebra map `ρ : U4 N → (A ⊗ A) ⊗ A` carries `e(t₁₃ + t₂₃), e(t₁₃), e(t₂₃)` to
`(Δ ⊗ id)(R), R₁₃, R₂₃`, then every rational associator `Φ` in `U4 N` gives
`(Δ ⊗ id)(R) = P · R₁₃ · Q · R₂₃ · Φ₁₂₃` with `P, Q, Φ₁₂₃` the `ρ`-images of
`φ(t₁₃,t₁₂), φ(t₂₃,t₁₃), φ(t₁₂,t₂₃)`. -/
theorem hexagon_of_realization {E Φ : FreeAlgebra ℚ (Fin 2)} (hΦ : AssocU4 N E Φ)
    (ρ : U4 N →ₐ[ℚ] (A ⊗[ℚ] A) ⊗[ℚ] A) (Δ : A →ₐ[ℚ] A ⊗[ℚ] A) (R : A ⊗[ℚ] A)
    (hΔ : ρ (eval (t N 1 + t N 3) 0 E) = Algebra.TensorProduct.map Δ (AlgHom.id ℚ A) R)
    (h13 : ρ (eval (t N 1) 0 E) = leg13 R) (h23 : ρ (eval (t N 3) 0 E) = leg23 R) :
    Algebra.TensorProduct.map Δ (AlgHom.id ℚ A) R =
      ρ (eval (t N 1) (t N 0) Φ) * leg13 R * ρ (eval (t N 3) (t N 1) Φ) * leg23 R *
        ρ (eval (t N 0) (t N 3) Φ) := by
  have key := congrArg ρ hΦ.hex
  simp only [map_mul, h13, h23, hΔ] at key
  exact key

/-- **`quasiYBE_of_hexagon` applied to a rational associator.** Under quasi-cocommutativity of
`(Δ, R)` and a realisation `ρ` as in `hexagon_of_realization`, the conclusion of
`quasiYBE_of_hexagon` holds with `P, Q, Φ₁₂₃` the `ρ`-images of the rational associator. -/
theorem quasiYBE_of_hexagon_realization {E Φ : FreeAlgebra ℚ (Fin 2)} (hΦ : AssocU4 N E Φ)
    (ρ : U4 N →ₐ[ℚ] (A ⊗[ℚ] A) ⊗[ℚ] A) (Δ : A →ₐ[ℚ] A ⊗[ℚ] A) (R : A ⊗[ℚ] A)
    (hR : ∀ a, Algebra.TensorProduct.comm ℚ A A (Δ a) * R = R * Δ a)
    (hΔ : ρ (eval (t N 1 + t N 3) 0 E) = Algebra.TensorProduct.map Δ (AlgHom.id ℚ A) R)
    (h13 : ρ (eval (t N 1) 0 E) = leg13 R) (h23 : ρ (eval (t N 3) 0 E) = leg23 R) :
    leg12 R * (ρ (eval (t N 1) (t N 0) Φ) * leg13 R * ρ (eval (t N 3) (t N 1) Φ) * leg23 R *
        ρ (eval (t N 0) (t N 3) Φ)) =
      tau12 (ρ (eval (t N 1) (t N 0) Φ)) * leg23 R * tau12 (ρ (eval (t N 3) (t N 1) Φ)) *
        leg13 R * tau12 (ρ (eval (t N 0) (t N 3) Φ)) * leg12 R :=
  quasiYBE_of_hexagon Δ R hR _ _ _ (hexagon_of_realization hΦ ρ Δ R hΔ h13 h23)

end Realization

end QOU.BraidsAndKnots.RationalAssociator

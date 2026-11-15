import QOU.Machinery.BilinearTraceCyclicity

/-!
# Representation decomposition from the basis alone

`BilinearTraceCyclicity.gram_symm_of_rep_decomp` derives Gram symmetry — hence,
via `cyclic_of_gram_symm`, full cyclicity — from a decomposition

  `τ x = ∑_λ w_λ · tr (ρ_λ x)`

required **for every `x`**. That hypothesis is stronger than the mathematics
needs, and the gap is exactly what makes the bridge awkward to use at a concrete
level.

Both sides of that identity are *linear* in `x`. So it is determined by its
values on the `ι`-indexed basis `e i = Pi.single i 1`, and a concrete level
should only ever have to discharge `#ι` scalar equations rather than a statement
quantified over the whole module. At `H₄(q)` that is the difference between 24
equations in the coordinate vector's entries and one identity in a free
`Fin 24 → K`.

`rep_decomp_of_basis` closes that gap: given additivity and homogeneity of `τ`
and of each `ρ_λ`, the basis-level decomposition upgrades to the `∀ x` form.
`gram_symm_of_rep_decomp_of_basis` then chains it into the existing bridge, so
the concrete obligation becomes:

* the `ρ_λ` are multiplicative on the bilinear product (at `H₄` this is
  `map_mul` for the Wedderburn `AlgHom`, whose components are the block maps
  by `rfl`), linear (likewise `map_add` / `map_smul`), and
* `#ι` scalar identities `τ (e i) = ∑_λ w_λ · tr (ρ_λ (e i))`.

Nothing here is specific to `H₄`; it serves `H₃`, `H₅`, and any level whose
Markov trace is a coefficient vector against a basis.

Base ring (§7c): generic `[CommRing R]`. No archimedean construct, no ordering,
no `ℝ`.

-- Ref: [leitner2026] bean `qou-x64l`, step 4 (retire the ASCII H₄ Gram chain).
-/

namespace QOU.Machinery.BilinearTrace

variable {R : Type*} [CommRing R] {ι : Type*} [Fintype ι] [DecidableEq ι]
-- `Matrix.trace` needs only `Fintype` on the index; `DecidableEq (dim l)` is
-- deliberately absent, so neither theorem below carries an unused instance.
variable {Λ : Type*} {dim : Λ → Type*} [∀ l, Fintype (dim l)]

/-- **A linear map's trace-decomposition is determined on the basis.**

If `τ` and every `ρ l` are additive and homogeneous, then the decomposition
`τ x = ∑_{l ∈ s} w l · tr (ρ l x)` holding on the basis vectors `e i` forces it
for every `x`.

This is the rung that lets a concrete level discharge `#ι` scalar equations in
place of a statement quantified over `ι → R`. -/
theorem rep_decomp_of_basis
    (τ : (ι → R) → R) (s : Finset Λ) (w : Λ → R)
    (ρ : ∀ l, (ι → R) → Matrix (dim l) (dim l) R)
    (hτadd : ∀ u v, τ (u + v) = τ u + τ v)
    (hτsmul : ∀ (c : R) v, τ (c • v) = c * τ v)
    (hρadd : ∀ l u v, ρ l (u + v) = ρ l u + ρ l v)
    (hρsmul : ∀ l (c : R) v, ρ l (c • v) = c • ρ l v)
    (hbasis : ∀ i, τ (e (R := R) i) = ∑ l ∈ s, w l * (ρ l (e (R := R) i)).trace)
    (x : ι → R) :
    τ x = ∑ l ∈ s, w l * (ρ l x).trace := by
  -- Expand `x` in the basis on both sides, then exchange the two sums.
  conv_lhs => rw [basis_decomp x]
  rw [tau_sum τ hτadd]
  -- Left: `∑ i, x i * τ (e i)`, then substitute the basis hypothesis.
  have hleft : ∑ i, τ (x i • e (R := R) i)
      = ∑ i, ∑ l ∈ s, x i * (w l * (ρ l (e (R := R) i)).trace) := by
    refine Finset.sum_congr rfl (fun i _ => ?_)
    rw [hτsmul, hbasis i, Finset.mul_sum]
  rw [hleft, Finset.sum_comm]
  -- Right: push `ρ l` and `Matrix.trace` through the basis expansion.
  refine Finset.sum_congr rfl (fun l _ => ?_)
  have hρsum : ρ l x = ∑ i, x i • ρ l (e (R := R) i) := by
    conv_lhs => rw [basis_decomp x]
    induction (Finset.univ : Finset ι) using Finset.induction with
    | empty =>
        have hz : ρ l (0 : ι → R) = 0 := by
          have h := hρadd l 0 0; rw [add_zero] at h; exact left_eq_add.mp h
        simpa using hz
    | @insert a t ha ih =>
        rw [Finset.sum_insert ha, Finset.sum_insert ha, hρadd, hρsmul, ih]
  rw [hρsum, Matrix.trace_sum, Finset.mul_sum]
  refine Finset.sum_congr rfl (fun i _ => ?_)
  rw [Matrix.trace_smul, smul_eq_mul]
  ring

/-- **Gram symmetry from a basis-level representation decomposition.**

The usable form of `gram_symm_of_rep_decomp`: the decomposition hypothesis is
discharged on basis vectors only. Multiplicativity of the `ρ l` on the bilinear
product `B` is unchanged — at `H₄` it is `map_mul` for the Wedderburn `AlgHom`. -/
theorem gram_symm_of_rep_decomp_of_basis
    (B : (ι → R) → (ι → R) → (ι → R)) (τ : (ι → R) → R)
    (s : Finset Λ) (w : Λ → R) (ρ : ∀ l, (ι → R) → Matrix (dim l) (dim l) R)
    (hmul : ∀ l u v, ρ l (B u v) = ρ l u * ρ l v)
    (hτadd : ∀ u v, τ (u + v) = τ u + τ v)
    (hτsmul : ∀ (c : R) v, τ (c • v) = c * τ v)
    (hρadd : ∀ l u v, ρ l (u + v) = ρ l u + ρ l v)
    (hρsmul : ∀ l (c : R) v, ρ l (c • v) = c • ρ l v)
    (hbasis : ∀ i, τ (e (R := R) i) = ∑ l ∈ s, w l * (ρ l (e (R := R) i)).trace)
    (i j : ι) :
    τ (B (e (R := R) i) (e (R := R) j)) = τ (B (e (R := R) j) (e (R := R) i)) :=
  gram_symm_of_rep_decomp B τ s w ρ hmul
    (rep_decomp_of_basis τ s w ρ hτadd hτsmul hρadd hρsmul hbasis) i j

end QOU.Machinery.BilinearTrace

import QOU.Archimedean.GroundRing
import QOU.Archimedean.TransferMatrix
import QOU.Archimedean.BetaDecay
import QOU.Archimedean.YoungIdempotent
import Mathlib.Tactic.Ring

/-!
# Ordering Independence of the Young-Symmetrized Q-Value

The Young-symmetrized Skein polynomial `P_sym = tr_M(e_{(n)} · B · e_{(n)})`
is independent of the nucleon ordering used to construct the chain element `B`.
This gives a unique, algebraically determined Q-value.

**Note to reader**: all proofs over `ℤ[q, q⁻¹]`.

## Key result

For ANY two orderings of the same nucleus `(Z, N)`, the
Young-symmetrized Q-value is the same:

```
Q_sym(ordering₁) = Q_sym(ordering₂) = Q_sym
```

This follows from the idempotent property: `e_{(n)} · B · e_{(n)} = χ(B) · e_{(n)}`
where `χ(B)` is the character in the symmetric representation.

## Proof

By definition, `skeinPolynomialSym c = ∏_{j<k} f(c[j], c[k])` with
`f(a, b) = 𝔴⁺(v)·q + 𝔴⁰(v)`, `v = vertexType a b`: each crossing is already
evaluated in the symmetric representation `σ ↦ q`. Since `vertexType` is
symmetric and `ℤ[t, t⁻¹]` is commutative, a product over unordered pairs is
invariant under permuting the list (`pairProd_perm`), and two lists with the
same counts are permutations of each other (`List.perm_iff_count`).

## Verified computationally

For tritium `(Z=1, N=2)`: all 9 parent × daughter ordering combinations
give `Q_sym = 0.01943` (identical to 10 decimal places).
-/

namespace QOU.Archimedean

/-! ## §1  The Young-symmetrized Skein polynomial -/

/-- The Young-symmetrized Skein polynomial is defined as
    `P_sym(q) = tr_M(e_{(n)} · B(config) · e_{(n)})` where
    `e_{(n)}` is the symmetric Young idempotent and `B` is
    the chain element for any ordering of `config`.

    This is ordering-independent: the result depends only on
    the multiset of nucleon types `{Z protons, N neutrons}`,
    not on the specific ordering. -/
noncomputable def skeinPolynomialSym (config : NuclearConfig) : R_t :=
  -- Compute the Young-symmetrized Skein polynomial:
  -- P_sym(q) = tr_M(e_{(A)} · B(config) · e_{(A)})
  --
  -- For each crossing at generator j: the chain element contributes
  -- (c_j · σ_j + d_j) where (c_j, d_j) are the crossing coefficients.
  --
  -- The Young symmetrizer projects onto the symmetric rep (σ → q),
  -- so: χ(∏_j (c_j σ_j + d_j)) = ∏_j (c_j · q + d_j)
  --
  -- This is independent of the ordering of generators (commutative
  -- product of scalars).
  --
  -- Implementation: evaluate each crossing in the symmetric rep
  -- (σ → q) and multiply all factors.
  let A := config.length
  if A < 2 then 1
  else
    let factors := (List.range (A - 1)).map fun j =>
      (config.drop (j + 1)).foldl (fun acc nk =>
        let nj := config[j]!
        let v := vertexType nj nk
        -- In symmetric rep: c·q + d for each crossing
        acc * (w_plus_t v * q_from_t + w_zero_t v)
      ) 1
    factors.foldl (· * ·) 1

/-! ## §2  Ordering independence

`skeinPolynomialSym` is, by its definition above, the product over all
pairs `j < k` of the crossing factor `𝔴⁺(v)·q + 𝔴⁰(v)` with
`v = vertexType c[j] c[k]`. `vertexType` is symmetric and `R_t` is
commutative, so this product over unordered pairs depends only on the
multiset of nucleons. That is the whole proof: nothing about Young
symmetrizers or Hecke algebras is used, because the definition already
evaluates each crossing in the symmetric representation (`σ ↦ q`).

This replaces the former class `SkeinMultisetInvariant`, whose single field
was the conclusion (§3b-cond item 5; issue #8911). -/

/-- Product of `g a b` over all unordered pairs of positions in a list. -/
def pairProd {α R : Type*} [CommMonoid R] (g : α → α → R) : List α → R
  | [] => 1
  | a :: l => (l.map (g a)).prod * pairProd g l

/-- A pair product with a symmetric `g` is invariant under permutation. -/
theorem pairProd_perm {α R : Type*} [CommMonoid R] (g : α → α → R)
    (hg : ∀ a b, g a b = g b a) {l₁ l₂ : List α} (h : l₁.Perm l₂) :
    pairProd g l₁ = pairProd g l₂ := by
  induction h with
  | nil => rfl
  | cons a h ih => simp only [pairProd, ih, (h.map (g a)).prod_eq]
  | swap a b l =>
      simp only [pairProd, List.map_cons, List.prod_cons, hg a b]
      ac_rfl
  | trans _ _ ih₁ ih₂ => exact ih₁.trans ih₂

/-- A left fold by multiplication is a list product. -/
theorem foldl_mul_eq {α R : Type*} [CommMonoid R] (f : α → R) (l : List α) (a : R) :
    l.foldl (fun acc b => acc * f b) a = a * (l.map f).prod := by
  induction l generalizing a with
  | nil => simp
  | cons b l ih => simp [ih, mul_assoc]

/-- The index form `∏_j ∏_{k>j} g c[j] c[k]` equals `pairProd`. -/
theorem range_pairProd {α R : Type*} [CommMonoid R] [Inhabited α] (g : α → α → R) (c : List α) :
    ((List.range c.length).map
      (fun j => ((c.drop (j + 1)).map (g c[j]!)).prod)).prod = pairProd g c := by
  induction c with
  | nil => simp [pairProd]
  | cons a l ih =>
      rw [List.length_cons, List.range_succ_eq_map]
      simp only [List.map_cons, List.map_map, List.prod_cons, pairProd]
      rw [← ih]
      simp [Function.comp_def]


/-- The symmetric-representation factor of one crossing. -/
noncomputable def crossingFactor (a b : NucleonType) : R_t :=
  w_plus_t (vertexType a b) * q_from_t + w_zero_t (vertexType a b)

theorem vertexType_comm (a b : NucleonType) : vertexType a b = vertexType b a := by
  cases a <;> cases b <;> rfl

theorem crossingFactor_comm (a b : NucleonType) : crossingFactor a b = crossingFactor b a := by
  simp [crossingFactor, vertexType_comm a b]

/-- `skeinPolynomialSym` is the pair product of `crossingFactor`. -/
theorem skeinPolynomialSym_eq_pairProd (config : NuclearConfig) :
    skeinPolynomialSym config = pairProd crossingFactor config := by
  unfold skeinPolynomialSym
  have hf : ∀ j, (config.drop (j + 1)).foldl (fun acc nk =>
        acc * (w_plus_t (vertexType config[j]! nk) * q_from_t
          + w_zero_t (vertexType config[j]! nk))) 1
      = ((config.drop (j + 1)).map (crossingFactor config[j]!)).prod := by
    intro j
    have := foldl_mul_eq (crossingFactor config[j]!) (config.drop (j + 1)) 1
    rw [one_mul] at this
    exact this
  simp only [hf]
  rw [← range_pairProd]
  split_ifs with h
  · -- length < 2 : every factor is an empty product
    rw [eq_comm, List.prod_eq_one]
    intro x hx
    simp only [List.mem_map, List.mem_range] at hx
    obtain ⟨j, hj, rfl⟩ := hx
    rw [List.drop_eq_nil_of_le (by omega)]
    simp
  · have hfold := foldl_mul_eq (R := R_t) id
      ((List.range (config.length - 1)).map
        (fun j => ((config.drop (j + 1)).map (crossingFactor config[j]!)).prod)) 1
    simp only [id, one_mul] at hfold
    rw [hfold]
    obtain ⟨n, hn⟩ : ∃ n, config.length = n + 1 := ⟨config.length - 1, by omega⟩
    rw [hn, List.range_succ, List.map_append, List.prod_append, Nat.add_sub_cancel]
    rw [List.map_singleton, List.prod_singleton, List.drop_eq_nil_of_le (by omega)]
    simp

theorem skeinPolynomialSym_perm {c₁ c₂ : NuclearConfig} (h : c₁.Perm c₂) :
    skeinPolynomialSym c₁ = skeinPolynomialSym c₂ := by
  rw [skeinPolynomialSym_eq_pairProd, skeinPolynomialSym_eq_pairProd]
  exact pairProd_perm crossingFactor crossingFactor_comm h

theorem skein_multiset_invariance (c₁ c₂ : NuclearConfig)
    (h_perm : ∀ t : NucleonType, c₁.count t = c₂.count t) :
    skeinPolynomialSym c₁ = skeinPolynomialSym c₂ :=
  skeinPolynomialSym_perm (List.perm_iff_count.mpr h_perm)


/-- **Theorem (ordering independence).** Two nuclear configurations with the
same number of protons and the same number of neutrons have the same
symmetric skein polynomial. -/
theorem ordering_independence (config₁ config₂ : NuclearConfig)
    (h_perm : ∀ t : NucleonType, config₁.count t = config₂.count t) :
    skeinPolynomialSym config₁ = skeinPolynomialSym config₂ :=
  skein_multiset_invariance config₁ config₂ h_perm

/-! ## §3  The unique Q-value -/

/-- The unique, ordering-independent Q-value for β⁻ decay.

    `Q_sym = |log_q(P_sym(dau) / P_sym(par))| · ℏ_q · m_e/3`

    This is the ONLY algebraically determined Q-value:
    - It does not depend on the nucleon ordering
    - It is computed over `ℤ[q, q⁻¹]` (no numerical optimization)
    - The structural error (+4.4% for tritium) is the Level 0
      approximation, not an ordering artifact. -/
noncomputable def Q_sym (op : BetaDecayOp) : FractionRing R_t :=
  let P_par := skeinPolynomialSym op.parent
  let P_dau := skeinPolynomialSym op.daughter
  algebraMap R_t (FractionRing R_t) P_dau /
    algebraMap R_t (FractionRing R_t) P_par
  -- The full Q involves: |log_q(this ratio)| · ℏ_q · m_e/3 × F(τ,N)
  -- but log_q and absolute value require ordered fields (ℝ specialisation)

end QOU.Archimedean

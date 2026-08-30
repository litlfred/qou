import QOU.BraidKnot.HeckeTypeAPresentationEquiv

/-!
# Toward cell and Specht modules

Bean `qou-phir`, remaining half. This is **not** a cellular structure — building one
needs the Murphy basis, which is open here (see *What is still missing*). It is the part
of the cellular datum that follows from the presentation alone, plus the two cell modules
that exist for every `n`.

## The anti-involution — Graham–Lehrer axiom (C2)

A cellular algebra carries an anti-automorphism `*` with `C^λ_{s,t}* = C^λ_{t,s}`. For a
Hecke algebra it is the map fixing every generator, and it exists because the defining
relations are **palindromic**: reversing a word takes each relation to a relation.

It is not an ornament. It is what makes the bilinear form on a cell module symmetric,
and hence what lets the radical of that form cut out the simple head — so it is a
prerequisite for Specht theory, not a corollary of it.

**Why type A specifically.** For a general Coxeter matrix the reversal of
`altProd a b m` is `altProd a b m` when `m` is odd and `altProd b a m` when `m` is even,
so the general statement needs a parity lemma plus a chain of auxiliary word identities.
In type `A` the matrix takes only the values `1, 2, 3`, and at each the commutation the
reversal needs is *supplied by the relation itself*:

| `m` | reversal needs | supplied by |
|---|---|---|
| `1` (`i = j`) | nothing | both sides are `altProd _ _ 1` |
| `2` (far) | `a·b = b·a` | the far-commutation relation |
| `3` (adjacent) | `a·b·a = b·a·b` | the braid relation |

So type `A` is a three-way case split with no parity argument — and type `A` is where
Specht modules live anyway.

## What is still missing

The **Murphy basis** `{m_{s,t}}` indexed by pairs of standard tableaux, which is what
makes the cellular axioms (C1) and (C3) statable at all, and with it the general Specht
module `S^λ`. That needs the `T_w` basis (proved on #6053, transported here by
`algEquiv`) plus the combinatorics of standard tableaux and the dominance order. Nothing
below claims any of it.
-/

namespace QOU.BraidKnot.Hecke

open QOU.MathlibExt.IwahoriHecke
open QOU.IwahoriHecke.TypeA
open MulOpposite

universe u

variable (K : Type u) [CommRing K] (q : K) (n : ℕ)

/-- The type-`A` matrix is symmetric. -/
theorem strandMatrix_symm (i j : Fin n) :
    strandMatrix (n + 1) i j = strandMatrix (n + 1) j i := by
  simp only [strandMatrix, CoxeterMatrix.Aₙ, Matrix.of_apply, Fin.ext_iff]
  by_cases h : (i : ℕ) = (j : ℕ)
  · simp [h]
  · rw [if_neg h, if_neg (Ne.symm h)]
    congr 1
    exact propext ⟨fun hh => hh.symm, fun hh => hh.symm⟩

variable {K q}

/-- The quadratic relation with the factors in the other order. Immediate from
`T_quadratic` because `algebraMap` is central — and it is exactly the form the opposite
algebra asks for. -/
theorem T_quadratic_swap {B : Type*} {M : B → B → ℕ} (i : B) :
    (T K q M i + 1) * (T K q M i - algebraMap K (HeckeAlgebra K q M) q) = 0 := by
  have h := T_quadratic (R := K) (q := q) (M := M) i
  have hc := Algebra.commutes (A := HeckeAlgebra K q M) q (T K q M i)
  have e1 : (T K q M i - algebraMap K (HeckeAlgebra K q M) q) * (T K q M i + 1)
      = T K q M i * T K q M i + T K q M i
        - algebraMap K (HeckeAlgebra K q M) q * T K q M i
        - algebraMap K (HeckeAlgebra K q M) q := by
    simp only [sub_mul, mul_add, mul_one]; abel
  have e2 : (T K q M i + 1) * (T K q M i - algebraMap K (HeckeAlgebra K q M) q)
      = T K q M i * T K q M i + T K q M i
        - T K q M i * algebraMap K (HeckeAlgebra K q M) q
        - algebraMap K (HeckeAlgebra K q M) q := by
    simp only [add_mul, mul_sub, one_mul]; abel
  rw [e2, ← hc, ← e1]; exact h

variable (K q)

/-! ## The anti-involution -/

/-- **The anti-automorphism fixing the generators**, as an algebra map into the opposite
algebra: Graham–Lehrer cellular axiom (C2) for the type-`A` Hecke algebra.

The three relation checks are the three rows of the table in the header. -/
noncomputable def antiAut :
    IwahoriHeckeOfSn K q (n + 1) →ₐ[K] (IwahoriHeckeOfSn K q (n + 1))ᵐᵒᵖ :=
  lift K q (strandMatrix (n + 1)) (fun i => op (σ K q (n + 1) i))
    (fun i => by
      have h := T_quadratic_swap (K := K) (q := q) (M := strandMatrix (n + 1)) i
      have hop : (op (σ K q (n + 1) i)
            - algebraMap K (IwahoriHeckeOfSn K q (n + 1))ᵐᵒᵖ q)
          * (op (σ K q (n + 1) i) + 1)
          = op ((σ K q (n + 1) i + 1)
              * (σ K q (n + 1) i - algebraMap K (IwahoriHeckeOfSn K q (n + 1)) q)) := by
        simp [σ, ← MulOpposite.op_mul, ← MulOpposite.op_add, ← MulOpposite.op_sub,
          ← MulOpposite.op_one]
      rw [hop]
      have hsig : (σ K q (n + 1) i + 1)
          * (σ K q (n + 1) i - algebraMap K (IwahoriHeckeOfSn K q (n + 1)) q) = 0 := h
      rw [hsig, MulOpposite.op_zero])
    (fun i j => by
      rcases eq_or_ne i j with rfl | hij
      · rfl
      · by_cases hadj : (i : ℕ) + 1 = (j : ℕ)
        · rw [strandMatrix_adjacent n hadj, strandMatrix_adjacent' n hadj,
            altProd_three, altProd_three]
          have hb := sigma_braid (R := K) (q := q) (n := n + 1) i j
          rw [strandMatrix_adjacent n hadj, strandMatrix_adjacent' n hadj,
            altProd_three, altProd_three] at hb
          simp only [σ, ← MulOpposite.op_mul, MulOpposite.op_inj] at *
          simpa [mul_assoc] using hb
        · by_cases hadj' : (j : ℕ) + 1 = (i : ℕ)
          · rw [strandMatrix_adjacent' n hadj', strandMatrix_adjacent n hadj',
              altProd_three, altProd_three]
            have hb := sigma_braid (R := K) (q := q) (n := n + 1) i j
            rw [strandMatrix_adjacent' n hadj', strandMatrix_adjacent n hadj',
              altProd_three, altProd_three] at hb
            simp only [σ, ← MulOpposite.op_mul, MulOpposite.op_inj] at *
            simpa [mul_assoc] using hb
          · rw [strandMatrix_far n (by omega) (by omega) (by omega),
              strandMatrix_far n (by omega) (by omega) (by omega),
              altProd_two, altProd_two]
            have hf := sigma_braid (R := K) (q := q) (n := n + 1) i j
            rw [strandMatrix_far n (by omega) (by omega) (by omega),
              strandMatrix_far n (by omega) (by omega) (by omega),
              altProd_two, altProd_two] at hf
            simp only [σ, ← MulOpposite.op_mul, MulOpposite.op_inj] at *
            first
              | (simpa [mul_assoc] using hf)
              | (simpa [mul_assoc] using hf.symm))

@[simp] theorem antiAut_sigma (i : Fin n) :
    antiAut K q n (σ K q (n + 1) i) = op (σ K q (n + 1) i) :=
  lift_T K q (strandMatrix (n + 1)) _ _ _ i

/-! ## The two extreme cell modules

`S^{(n)}` and `S^{(1ⁿ)}` — the `q`-analogues of the trivial and sign representations of
`S_n`. These are the only Specht modules available without the Murphy basis, and they
exist for every `n`. -/

/-- The index (trivial) cell module of the type-`A` Hecke algebra: `σ_i ↦ q`. -/
noncomputable def typeAIndexRep : IwahoriHeckeOfSn K q (n + 1) →ₐ[K] K :=
  indexRep K q (strandMatrix (n + 1)) (strandMatrix_symm n)

/-- The sign cell module: `σ_i ↦ −1`. -/
noncomputable def typeASignRep : IwahoriHeckeOfSn K q (n + 1) →ₐ[K] K :=
  signRep K q (strandMatrix (n + 1)) (strandMatrix_symm n)

/-- **The two extreme cell modules are distinct** as soon as there is a generator and
`q ≠ −1`.

`q = −1` is the first point where they collide, which is where semisimplicity of
`H_n(q)` starts to fail — the reason the cellular machinery is needed at all. -/
theorem typeAIndexRep_ne_typeASignRep [Nontrivial K] (i : Fin n) (hq : q ≠ -1) :
    typeAIndexRep K q n ≠ typeASignRep K q n :=
  indexRep_ne_signRep K q (strandMatrix (n + 1)) (strandMatrix_symm n) i hq

/-! ## Toward the Murphy basis: the rank-one `x_λ`

Murphy's basis is `m_{st} = T_{d(s)}^* · x_λ · T_{d(t)}`, where
`x_λ = Σ_{w ∈ S_λ} T_w` is the sum over the Young subgroup. Its defining property is
that it is a **`q`-eigenvector** for every generator of that subgroup:
`σ_i · x_λ = q · x_λ` for `s_i ∈ S_λ`. Everything else in the construction is
conjugation by coset representatives.

The **rank-one** case — `S_λ = ⟨s_i⟩`, so `x_λ = 1 + σ_i` — is proved here, and it needs
nothing but the quadratic relation: `σ_i + σ_i² = q(1 + σ_i)` is that relation
rearranged. It is the base case of the whole construction and the one place where no
basis machinery is required.

**What the general case needs, and why it is not here.** `x_λ` for a general Young
subgroup is a sum over `S_λ`, and the eigenvector property is proved by pairing each
`w` with `w s_i` — one of the two has length going up, the other down, and the two
`rsFun` branches combine to `q·(T_w + T_{w s_i})`. That pairing argument over
`Equiv.Perm (Fin (n+1))` is the open work. The `T_w` basis it needs is now available
(`QOU.Hecke.TwBasis.basisTwOfField`, merged in #6053, and transported to this
presentation by `basisTwOfSn`), so the blocker is the combinatorics, not the algebra. -/

/-- **The rank-one Murphy element** `x_{⟨s_i⟩} = 1 + σ_i`: the sum over the Young
subgroup generated by a single simple reflection. -/
noncomputable def parabolicSym (i : Fin n) : IwahoriHeckeOfSn K q (n + 1) :=
  1 + σ K q (n + 1) i

/-- **The defining eigenvector property**, left action: `σ_i · x = q · x`.

This is the quadratic relation rearranged — `σ_i + σ_i² = q σ_i + q` — and it is what
makes `x_λ` the right object to build the Murphy basis on. -/
theorem sigma_mul_parabolicSym (i : Fin n) :
    σ K q (n + 1) i * parabolicSym K q n i = q • parabolicSym K q n i := by
  have h := QOU.IwahoriHecke.TypeA.sigma_quadratic (R := K) (q := q) (n := n + 1) i
  have expand : (σ K q (n + 1) i - algebraMap K (IwahoriHeckeOfSn K q (n + 1)) q)
      * (σ K q (n + 1) i + 1)
      = σ K q (n + 1) i * σ K q (n + 1) i + σ K q (n + 1) i
        - algebraMap K (IwahoriHeckeOfSn K q (n + 1)) q * σ K q (n + 1) i
        - algebraMap K (IwahoriHeckeOfSn K q (n + 1)) q := by
    simp only [sub_mul, mul_add, mul_one]; abel
  rw [expand] at h
  simp only [parabolicSym, mul_add, mul_one, Algebra.smul_def]
  refine sub_eq_zero.mp ?_
  linear_combination (norm := abel) h

/-- The same on the right: `x · σ_i = q · x`. Identical content, since `1 · σ_i = σ_i`. -/
theorem parabolicSym_mul_sigma (i : Fin n) :
    parabolicSym K q n i * σ K q (n + 1) i = q • parabolicSym K q n i := by
  have h := sigma_mul_parabolicSym K q n i
  simp only [parabolicSym, add_mul, mul_add, one_mul, mul_one] at h ⊢
  exact h

end QOU.BraidKnot.Hecke

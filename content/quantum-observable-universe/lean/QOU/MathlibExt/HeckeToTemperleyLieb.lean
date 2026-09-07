import Mathlib.Tactic.NoncommRing
import Mathlib.RingTheory.TwoSidedIdeal.Kernel
import QOU.MathlibExt.IwahoriHeckeAlgebra
import QOU.MathlibExt.TemperleyLiebAlgebra

/-!
# `H_n(q) ↠ TL_n(δ)` — the Temperley–Lieb quotient map, as an algebra hom

**Bean `qou-cds1`.** `rem:hecke-radical-is-temperley-lieb` says, and has said
throughout, that **no formalised statement of `H_n(q)/rad ≅ TL_n(q)` exists.**
This file does not supply the isomorphism. It supplies the **surjection**, which
is the half that needs no semisimplicity input:

> there is a surjective `R`-algebra map `H_n(q) ↠ TL_n(δ)`,

reducing the isomorphism to a single question — *is its kernel the trace
radical?* That question is stated at the end, and not answered.

## Why this needed no new infrastructure

Both algebras were already presented in this corpus as `RingQuot`s of a free
algebra **with their universal properties proved** (`lift` / `hom_ext` /
`exists_unique_lift`, in `IwahoriHecke` and in `TemperleyLieb`). So the map is
built by `lift`, and the entire content is checking that one family in `TL`
satisfies the two Hecke relations.

## The normalisation, and why `v` rather than `√q`

`IwahoriHecke` is in the **Iwahori** normalisation `(T_i − q)(T_i + 1) = 0`;
`TemperleyLieb` carries the **balanced** relations `e_i² = δ e_i`,
`e_i e_j e_i = e_i`. Those do not match under any shift `T_i ↦ a − e_i`: the
quadratic relation then forces `δ = q + 1` and the braid relation forces
`δ = q + q⁻¹`, and the two agree only at `q = 1`. The fix is the standard one,
carrying the square root as primitive datum:

    T_i  ↦  v·e_i − 1 ,      with   v·δ = v² + 1 ,   q = v² .

Read at `v = q^{1/2}` that is `δ = v + v⁻¹`, the usual loop parameter. **But no
inverse and no square root appears anywhere below.** The hypothesis is the
polynomial identity `v * δ = v ^ 2 + 1`, meaningful over any commutative ring —
so §7c holds without effort: nothing is stated over `ℝ`, nothing needs `0 < q`,
and `v` is not required to be a unit until surjectivity, where it genuinely is.

That is not mere convenience. `Real.sqrt q` would drag a purely algebraic
statement across the substrate→archimedean wall for no reason, and the
`√q`-vs-`q` distinction is exactly the convention-C/D confusion this corpus has
spent months draining.

## The shape of the proof, which is smaller than expected

The two relation checks are **ring identities about two elements**, with no
reference to `algebraMap`, centrality, or the ambient algebra. They are proved
that way in §Abstract below and then instantiated once. The braid check is the
surprise: writing `u_i = v·e_i`, the hypotheses are `u² = Q·u + u` and
`u_i u_j u_i = Q·u_i`, and both sides of the braid relation reduce to

    −u_i u_j − u_j u_i + u_i + u_j − 1 ,

in which **`Q` does not appear at all.** So the braid relation needs no
compatibility between `q` and `δ` beyond what the loop relation already forces,
and the proof needs no commutation hypothesis on `Q`. The `v·δ = v² + 1`
condition enters only through the loop relation.

-- Ref: [jones1985] https://doi.org/10.2307/1971403 — the Temperley–Lieb
-- quotient of the Hecke algebra and the Markov trace that detects it.
-/

namespace QOU.MathlibExt.HeckeToTemperleyLieb

open QOU.MathlibExt.TemperleyLieb (TemperleyLiebAlgebra e e_sq e_adjacent e_farCommute)
open QOU.MathlibExt.IwahoriHecke (HeckeAlgebra T altProd)

/-! ## The diagram hypothesis -/

/-- **Type-A compatibility between a Coxeter matrix and an adjacency predicate.**

`IwahoriHecke` is indexed by a Coxeter matrix `M`; `TemperleyLieb` by an
adjacency predicate `Adj`. This says they describe the same diagram: `3` on
adjacent pairs (the braid relation), `2` on distinct non-adjacent ones
(commutation), `1` on the diagonal.

A structure rather than four loose hypotheses because all of them are needed
together at every use, and because `adj_irrefl` is the one that is easy to
forget — without it `M i i` would have to be both `1` and `3`. -/
structure IsTypeADiagram {B : Type*} (M : B → B → ℕ) (Adj : B → B → Prop) : Prop where
  /-- `M i i = 1`: a generator braids trivially with itself. -/
  diag : ∀ i, M i i = 1
  /-- Adjacent generators satisfy the length-3 braid relation. -/
  adj : ∀ i j, Adj i j → M i j = 3
  /-- Distinct non-adjacent generators commute. -/
  far : ∀ i j, i ≠ j → ¬ Adj i j → M i j = 2
  /-- Adjacency is irreflexive. -/
  adj_irrefl : ∀ i, ¬ Adj i i
  /-- Adjacency is symmetric. -/
  adj_symm : ∀ i j, Adj i j → Adj j i

/-! ## Abstract — the two relation checks as ring identities -/

section Abstract

variable {A : Type*} [Ring A]

/-- **The Iwahori quadratic relation, abstractly.**

If `u * u = Q * u + u` then `x := u − 1` satisfies `(x − Q)(x + 1) = 0`.

No hypothesis on `Q` at all — not centrality, not invertibility. The relation is
`(u − 1 − Q) * u = u*u − u − Q*u`, and the assumption is exactly what makes that
vanish. -/
theorem quadratic_of_sq {u Q : A} (hu : u * u = Q * u + u) :
    (u - 1 - Q) * ((u - 1) + 1) = 0 := by
  have h : (u - 1 - Q) * ((u - 1) + 1) = u * u - u - Q * u := by noncomm_ring
  rw [h, hu]
  abel

/-- **The length-3 braid relation, abstractly.**

Given the loop relation for each of `u₁, u₂` and the two adjacency relations
`u₁u₂u₁ = Q·u₁`, `u₂u₁u₂ = Q·u₂`, the shifted elements `u − 1` braid.

**`Q` cancels.** Both sides reduce to `−u₁u₂ − u₂u₁ + u₁ + u₂ − 1`, so the
identity holds for *any* `Q` satisfying those hypotheses, with no centrality and
no relation between `Q` and a loop parameter. That is why the substitution works
at all: the braid relation is not an extra constraint on `δ` once the loop
relation is imposed on the rescaled generator. -/
theorem braid3_of {u₁ u₂ Q : A}
    (h₁ : u₁ * u₁ = Q * u₁ + u₁) (h₂ : u₂ * u₂ = Q * u₂ + u₂)
    (h₁₂ : u₁ * u₂ * u₁ = Q * u₁) (h₂₁ : u₂ * u₁ * u₂ = Q * u₂) :
    (u₁ - 1) * ((u₂ - 1) * (u₁ - 1)) = (u₂ - 1) * ((u₁ - 1) * (u₂ - 1)) := by
  have e₁ : (u₁ - 1) * ((u₂ - 1) * (u₁ - 1))
      = u₁ * u₂ * u₁ - u₁ * u₂ - u₁ * u₁ + u₁ - u₂ * u₁ + u₂ + u₁ - 1 := by noncomm_ring
  have e₂ : (u₂ - 1) * ((u₁ - 1) * (u₂ - 1))
      = u₂ * u₁ * u₂ - u₂ * u₁ - u₂ * u₂ + u₂ - u₁ * u₂ + u₁ + u₂ - 1 := by noncomm_ring
  rw [e₁, e₂, h₁₂, h₂₁, h₁, h₂]
  abel

/-- **Commutation is inherited by the shift.** -/
theorem commute_of {u₁ u₂ : A} (h : u₁ * u₂ = u₂ * u₁) :
    (u₁ - 1) * (u₂ - 1) = (u₂ - 1) * (u₁ - 1) := by
  have e₁ : (u₁ - 1) * (u₂ - 1) = u₁ * u₂ - u₁ - u₂ + 1 := by noncomm_ring
  have e₂ : (u₂ - 1) * (u₁ - 1) = u₂ * u₁ - u₂ - u₁ + 1 := by noncomm_ring
  rw [e₁, e₂, h]
  abel

end Abstract

/-! ## Instantiation in `TL`

Written with the scalar action `•` rather than `algebraMap _ * _`. That is not
cosmetic: the three relations all need the scalar moved past a generator, and
`algebraMap R A v * e i * (algebraMap R A v * e j)` cannot be reassociated into
`algebraMap R A v * algebraMap R A v * (e i * e j)` by `noncomm_ring` — the second
scalar is trapped between two generators and only *centrality* frees it. In `•`
form that step is `smul_mul_smul_comm`, a single rewrite. -/

section TL

variable {R : Type*} [CommRing R] {B : Type*}

variable (v δ : R) (Adj : B → B → Prop)

/-- **The rescaled Temperley–Lieb generator** `u_i = v · e_i`.

Rescaling by `v` moves the loop parameter from `δ` to `v·δ = v² + 1 = q + 1`, the
Iwahori-normalised value, and moves the adjacency relation from
`e_i e_j e_i = e_i` to `u_i u_j u_i = q·u_i`. Those two shifts are exactly what
reconciles the two files' conventions; see the header. -/
noncomputable def u (i : B) : TemperleyLiebAlgebra R δ Adj := v • e R δ Adj i

variable {v δ Adj}

/-- `e_i² = δ • e_i`, the loop relation in `•` form. -/
theorem e_sq_smul (i : B) :
    e R δ Adj i * e R δ Adj i = δ • e R δ Adj i := by
  rw [e_sq, Algebra.smul_def]

/-- **The loop relation on `u`**: `u_i² = q·u_i + u_i`, with `q = v²`.

This is the only place `v·δ = v² + 1` is used. -/
theorem u_sq (hδ : v * δ = v ^ 2 + 1) (i : B) :
    u v δ Adj i * u v δ Adj i
      = algebraMap R (TemperleyLiebAlgebra R δ Adj) (v ^ 2) * u v δ Adj i
        + u v δ Adj i := by
  simp only [u, ← Algebra.smul_def, smul_mul_smul_comm, e_sq_smul, smul_smul,
    ← add_smul]
  congr 1
  linear_combination v * hδ

/-- **The adjacency relation on `u`**: `u_i u_j u_i = q·u_i` with `q = v²`.

No hypothesis on `δ` is needed — the `v³` on the left meets `v² · v` on the
right. That is the abstract lemma's "`Q` cancels" made concrete. -/
theorem u_adj {i j : B} (hij : Adj i j) :
    u v δ Adj i * u v δ Adj j * u v δ Adj i
      = algebraMap R (TemperleyLiebAlgebra R δ Adj) (v ^ 2) * u v δ Adj i := by
  have hadj := e_adjacent (R := R) (δ := δ) hij
  simp only [u, ← Algebra.smul_def, smul_mul_smul_comm, smul_smul, hadj]
  congr 1
  ring

/-- **Non-adjacent `u`'s commute**, inherited from `e_farCommute`. -/
theorem u_comm {i j : B} (hij : ¬ Adj i j) :
    u v δ Adj i * u v δ Adj j = u v δ Adj j * u v δ Adj i := by
  have hfar := e_farCommute (R := R) (δ := δ) hij
  simp only [u, smul_mul_smul_comm, hfar]

end TL

/-! ## The map -/

section Hom

variable {R : Type*} [CommRing R] {B : Type*}
variable {v δ : R} {M : B → B → ℕ} {Adj : B → B → Prop}

/-- **The Temperley–Lieb quotient map** `H_n(v²) →ₐ[R] TL_n(δ)`, `T_i ↦ v·e_i − 1`.

Built by `IwahoriHecke.lift`, so the two obligations are exactly the Hecke
relations, discharged by `quadratic_of_sq` and `braid3_of` / `commute_of`. -/
noncomputable def heckeToTL (hδ : v * δ = v ^ 2 + 1) (hd : IsTypeADiagram M Adj) :
    HeckeAlgebra R (v ^ 2) M →ₐ[R] TemperleyLiebAlgebra R δ Adj :=
  IwahoriHecke.lift R (v ^ 2) M (fun i => u v δ Adj i - 1)
    (fun i => quadratic_of_sq (u_sq hδ i))
    (fun i j => by
      by_cases hij : i = j
      · subst hij
        rw [hd.diag i]
      · by_cases hadj : Adj i j
        · rw [hd.adj i j hadj, hd.adj j i (hd.adj_symm i j hadj)]
          rw [IwahoriHecke.altProd_three, IwahoriHecke.altProd_three]
          exact braid3_of (u_sq hδ i) (u_sq hδ j) (u_adj hadj)
            (u_adj (hd.adj_symm i j hadj))
        · have hji : ¬ Adj j i := fun h => hadj (hd.adj_symm j i h)
          rw [hd.far i j hij hadj, hd.far j i (Ne.symm hij) hji]
          rw [IwahoriHecke.altProd_two, IwahoriHecke.altProd_two]
          exact commute_of (u_comm hadj))

@[simp] theorem heckeToTL_T (hδ : v * δ = v ^ 2 + 1) (hd : IsTypeADiagram M Adj) (i : B) :
    heckeToTL hδ hd (T R (v ^ 2) M i) = u v δ Adj i - 1 :=
  IwahoriHecke.lift_T R (v ^ 2) M _ _ _ i

end Hom

/-! ## Surjectivity -/

section Surjective

variable {R : Type*} [CommRing R] {B : Type*} {δ : R} {Adj : B → B → Prop}

/-- **`TL` is generated by its `e_i`.**

`RingQuot.mkAlgHom` is surjective and `FreeAlgebra` is generated by `ι`, so the
image of the generators generates. Stated here rather than in
`TemperleyLiebAlgebra` only because that is where it was first needed; it is a
fact about the presentation, not about this map. -/
theorem adjoin_range_e_eq_top :
    Algebra.adjoin R (Set.range (e R δ Adj))
      = (⊤ : Subalgebra R (TemperleyLiebAlgebra R δ Adj)) := by
  set S := Algebra.adjoin R (Set.range (e R δ Adj)) with hS
  refine top_unique fun x hx => ?_
  clear hx
  obtain ⟨y, rfl⟩ :=
    RingQuot.mkAlgHom_surjective R (QOU.MathlibExt.TemperleyLieb.Rel R δ Adj) x
  induction y with
  | grade0 r =>
      rw [AlgHom.commutes]
      exact S.algebraMap_mem _
  | add a b ha hb => rw [map_add]; exact S.add_mem ha hb
  | mul a b ha hb => rw [map_mul]; exact S.mul_mem ha hb
  | grade1 i => exact Algebra.subset_adjoin (Set.mem_range_self i)

variable {v : R} {M : B → B → ℕ}

/-- **The map is surjective**, given a right inverse `w` for `v`.

`v` must be a unit and this is the one place it is needed: `e_i` is recovered as
`w · (T_i + 1)`, so without an inverse for `v` the generators need not be in the
image at all. Everything above holds over any commutative ring. -/
theorem heckeToTL_surjective (hδ : v * δ = v ^ 2 + 1) (hd : IsTypeADiagram M Adj)
    {w : R} (hw : v * w = 1) :
    Function.Surjective (heckeToTL hδ hd) := by
  have htop : (⊤ : Subalgebra R (TemperleyLiebAlgebra R δ Adj))
      ≤ (heckeToTL hδ hd).range := by
    rw [← adjoin_range_e_eq_top]
    apply Algebra.adjoin_le
    rintro _ ⟨i, rfl⟩
    refine ⟨algebraMap R (HeckeAlgebra R (v ^ 2) M) w * (T R (v ^ 2) M i + 1), ?_⟩
    show (heckeToTL hδ hd) (algebraMap R (HeckeAlgebra R (v ^ 2) M) w
        * (T R (v ^ 2) M i + 1)) = e R δ Adj i
    have h1 : (heckeToTL hδ hd) (algebraMap R (HeckeAlgebra R (v ^ 2) M) w
        * (T R (v ^ 2) M i + 1))
        = algebraMap R (TemperleyLiebAlgebra R δ Adj) w
          * ((heckeToTL hδ hd) (T R (v ^ 2) M i) + 1) := by
      simp [map_mul, map_add, map_one, AlgHom.commutes]
    rw [h1, heckeToTL_T, sub_add_cancel, u, ← Algebra.smul_def, smul_smul,
      mul_comm w v, hw, one_smul]
  intro x
  exact htop (Algebra.mem_top)

end Surjective

/-! ## Non-vacuity — the diagram hypothesis is satisfiable

Everything above takes `IsTypeADiagram M Adj` as a hypothesis. If no pair
`(M, Adj)` satisfied it, every theorem in this file would be vacuously true and
the surjection would be about nothing. It is satisfied by the linear type-A
diagram on `Fin n`, which is the case the mass channel uses at `n = 3A`. -/

section NonVacuous

open QOU.MathlibExt.TemperleyLieb (adjFin adjFin_symm adjFin_irrefl)

/-- The type-A Coxeter matrix of the linear diagram on `Fin n`: `1` on the
diagonal, `3` on adjacent pairs, `2` elsewhere. -/
def coxeterFin {n : ℕ} (i j : Fin n) : ℕ :=
  if i = j then 1 else if adjFin i j then 3 else 2

/-- **The hypothesis is inhabited.** So the surjection theorem is a statement
about a nonempty class, not a vacuous implication. -/
theorem isTypeADiagram_coxeterFin {n : ℕ} :
    IsTypeADiagram (coxeterFin (n := n)) adjFin where
  diag i := by simp [coxeterFin]
  adj i j h := by
    have hne : i ≠ j := by rintro rfl; exact adjFin_irrefl i h
    simp [coxeterFin, hne, h]
  far i j hij h := by simp [coxeterFin, hij, h]
  adj_irrefl i := adjFin_irrefl i
  adj_symm _ _ h := adjFin_symm.mp h

end NonVacuous

/-! ## The kernel, and exactly what is still open -/

section Kernel

variable {R : Type*} [CommRing R] {B : Type*}
variable {v δ : R} {M : B → B → ℕ} {Adj : B → B → Prop}

/-- **The Temperley–Lieb ideal** — the kernel of the quotient map, as a
two-sided ideal.

`TwoSidedIdeal`, not `Ideal`: Mathlib's `Ideal` is `Submodule R R` and is the
*commutative* notion, while `HeckeAlgebra` is not commutative. That distinction
is why the first-isomorphism step below is stated as an open engineering item
rather than proved.

This is a definition and asserts nothing about what the ideal is. It exists so
that the open question can be *written down*. -/
noncomputable def tlKernel (hδ : v * δ = v ^ 2 + 1) (hd : IsTypeADiagram M Adj) :
    TwoSidedIdeal (HeckeAlgebra R (v ^ 2) M) :=
  TwoSidedIdeal.ker (heckeToTL hδ hd).toRingHom

/-- **The Temperley–Lieb relator lies in the kernel.**

`U_i := T_i + 1` maps to `u_i = v·e_i`, and the extra relation cutting `TL` out
of `H` is `U_i U_j U_i = q·U_i` for adjacent `i, j` — which in `H` is a genuine
relation only modulo the ideal. This exhibits that relator as an explicit
element of `tlKernel`, so the ideal is not merely named: it visibly contains
what it is supposed to contain.

It does **not** show the relators generate it. That is the `⊆` half of the open
question below, and the easier half. -/
theorem tlRelator_mem_ker (hδ : v * δ = v ^ 2 + 1) (hd : IsTypeADiagram M Adj)
    {i j : B} (hij : Adj i j) :
    heckeToTL hδ hd
        ((T R (v ^ 2) M i + 1) * (T R (v ^ 2) M j + 1) * (T R (v ^ 2) M i + 1)
          - algebraMap R (HeckeAlgebra R (v ^ 2) M) (v ^ 2) * (T R (v ^ 2) M i + 1))
      = 0 := by
  have hT : ∀ k : B, heckeToTL hδ hd (T R (v ^ 2) M k + 1) = u v δ Adj k := by
    intro k
    rw [map_add, map_one, heckeToTL_T, sub_add_cancel]
  rw [map_sub, map_mul, map_mul, map_mul, AlgHom.commutes, hT, hT]
  rw [u_adj hij, sub_self]

end Kernel

/-!
## 🛑 What remains open, stated precisely

The paper's claim is `H_n(q)/rad ≅ TL_n(q)`, where `rad` is the null space of
the Markov trace — `QOU.QBeta.TemperleyLiebTower.traceRadical`, already proved a
two-sided ideal there (`traceRadical_two_sided`). Against that, this file
supplies a surjection `H_n(v²) ↠ TL_n(δ)` and names its kernel. **Two things
stand between that and the claim, and they are of very different kinds.**

**(1) Mathematics — the ideal is not identified.**

> **Open.** `tlKernel hδ hd = traceRadical tr_M`, for the convention-D Markov
> trace on `H_n(q)`.

`⊆` is a computation: the relator of `tlRelator_mem_ker` generates the kernel
(itself unproved here) and the trace kills it. `⊇` says the trace sees
*everything* outside the ideal — semisimplicity of `TL_n(δ)` at the relevant
`δ`, i.e. exactly the Wedderburn input this file was built to avoid needing. The
corpus has the positivity half of that (`TemperleyLiebTower.yw_pos`,
`terms_zero_of_weighted_sum_zero`) and does not have the block decomposition it
would be applied to.

**(2) Engineering — the first isomorphism theorem is missing for this setting.**
Even granting (1), turning "surjective with kernel `I`" into "`H/I ≅ TL`" needs
a first isomorphism theorem for **noncommutative** rings. Mathlib's
`Ideal.quotientKerAlgEquivOfSurjective` is stated for `Ideal`, which is
`Submodule R R` and therefore the commutative notion; the noncommutative
`TwoSidedIdeal` has `ker` (used above) but no quotient-equivalence under any
`quotientKerEquivOfSurjective`-shaped name — checked across `TwoSidedIdeal/` and
`RingTheory/Congruence/`. So that step is `RingCon` plumbing, not mathematics,
and it is **not** done here rather than being done badly.

Nothing above asserts either item. **No class, axiom or `sorry` stands in for
them**: `tlKernel` is a definition, `tlRelator_mem_ker` is a theorem about it,
and both open items appear only in this comment. A conditional class asserting
the ideal equality would satisfy the propagation audit while adding no
mathematics, which §"Axiomatization is NOT a Proof" forbids.

## What this file does NOT claim

* **Not** that `H_n(q)/rad ≅ TL_n(q)`, for the two reasons above.
* **Not** that the relators generate `tlKernel` — only that one of them is in it.
* **Not** anything about braid groups, diagram bases, or `dim TL_n = catalan n`.
  `B` here is an arbitrary index type with an adjacency predicate; specialising
  to `Fin (n-1)` with `TemperleyLieb.adjFin` is immediate but is not done,
  because nothing above needs it.
* **Not** that `heckeToTL` is injective anywhere. It is not, whenever the kernel
  is nonzero — which is the point of its being a quotient map.
-/

end QOU.MathlibExt.HeckeToTemperleyLieb

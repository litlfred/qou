import QOU.SchurWeyl.HeckeInclusion
import Mathlib.Algebra.Algebra.Bilinear
import Mathlib.LinearAlgebra.Dimension.StrongRankCondition
import Mathlib.LinearAlgebra.Dimension.Constructions
import Mathlib.LinearAlgebra.Dimension.Finrank

/-!
# QOU.SchurWeyl.HeckeCoset — the coset spanning bound `dim H_{n+1}(q) ≤ (n+1)!` (bean `qou-uoal`)

The Iwahori–Hecke basis theorem `dim_K H_n(q) = n!` has two halves; this file
establishes the **spanning half** in general `n` (upper bound), via the tower
coset decomposition.  With the QOU indexing `Hecke K q qi n = H_{n+1}(q)`
(the algebra on `n` generators `σ_0,…,σ_{n-1}`), the statement proved here is

  `Module.finrank K (Hecke K q qi n) ≤ (n+1)!`.

## Strategy — coset decomposition of the tower

`H_{n+1}(q) = ⨁_{k} H_n(q) · r_k` over the `n+2` (classically `n+2 = [H_{n+2}:H_{n+1}]`)
coset representatives

  `r_0 = 1,  r_j = σ_n σ_{n-1} ⋯ σ_{n-j+1}   (j = 1,…,n+1)`,

i.e. `r_j` is the descending product of the top `j` generators.  **Right**
multiplication by any generator preserves the subspace `Σ_k ι(H_n)·r_k`
(`ι = heckeIncl`, the tower inclusion `H_n ↪ H_{n+1}`), so that subspace is a
right ideal containing `1`, hence all of `H_{n+1}`.  Iterating gives a spanning
family indexed by `cosetIndex n` of cardinality `(n+1)!`.

**Handedness.**  The family carries the subalgebra on the *left* (`ι(H_n)·r_j`),
so the induction must be taken on the *right* — right multiplication acts on the
`r_j` factor, where the Hecke relations apply.  An earlier left-handed version of
the closure lemma left the top generator open as a `sorry`, because
`σ_n · ι(w) · r_j` offers no relation with which to move `σ_n` past the opaque
`ι(w)`.  On the correct side the same statement is a four-case computation; see
`span_mul_gen_mem`.  Nothing deeper was needed (bean `qou-j6f9`).

## What is delivered here

* `descProd m j` — the descending product `σ_m σ_{m-1} ⋯ σ_{m-j+1}` of length `j`
  in `H_{m+1}(q) = Hecke K q qi (m+1)` (the coset representative `r_j`).
* `descProd_mul_σ_of_add_lt` / `_of_add_eq` / `_of_add_eq_succ` / `_of_le_add` —
  the **four cases of the bubble**: `r_j σ_i` equals `σ_i r_j` (far commutation),
  `r_{j+1}` (lengthening), `(q-qi)·r_j + (q·qi)·r_{j-1}` (quadratic), or
  `σ_{i-1} r_j` (braid), selected by comparing `i + j` with `m`.  All sorry-free.
* `cosetIndex m`, `cosetFam m` — the recursively-built spanning family and its
  finite index type, with `Fintype.card (cosetIndex m) = (m+1)!`
  (`card_cosetIndex`, sorry-free).
* `one_mem_span_cosetFam` — `1` is in the span of the family (sorry-free).
* `finrank_le_card_of_span` — the generic finite-spanning ⇒ `finrank ≤ card`
  reduction (sorry-free).
* `incl_mul_descProd_mem` — coset absorption: `ι(w)·r_k` stays in the span.
* `span_mul_gen_mem` — **right**-multiplication by a generator preserves the
  span (sorry-free).  This is the general-`n` form of the twelve explicit
  `HeckeDim3.gen_mul_mem` reductions at `n = 3`.
* `span_cosetFam_eq_top` — the spanning statement, from `span_mul_gen_mem` via
  the adjoin = span-of-submonoid route (`Submonoid.closure_induction_right`).
* `finrank_le_factorial` — the headline bound `finrank K (Hecke K q qi n) ≤ (n+1)!`,
  proved from `span_cosetFam_eq_top`.  **Sorry-free**; `#print axioms` gives
  `[propext, Classical.choice, Quot.sound]`.

The whole file is sorry-free: this settles the **spanning half** of the
Iwahori–Hecke basis theorem in general `n`.  The complementary
linear-independence half (`dim ≥ n!`) is *not* claimed here — at `n = 3` it is
`HeckeDim3Indep`.

Base ring: generic `[CommRing K]` for the algebraic data; `[Nontrivial K]` only
for the `finrank` bound (`StrongRankCondition`), per §7c.

LaTeX label: `prop:hecke-coset-spanning-bound`

Refs:
- [mathas1999] *Iwahori–Hecke Algebras and Schur Algebras of the Symmetric
  Group*, Ch. 1 (the `T_w` standard basis, `w ∈ S_n`),
  https://doi.org/10.1090/ulect/015
- [geckpfeiffer2000] Geck–Pfeiffer, *Characters of Finite Coxeter Groups and
  Iwahori–Hecke Algebras*, §4.4 (coset representatives / reduced words),
  https://doi.org/10.1093/oso/9780198502500.001.0001
-/

namespace QOU.SchurWeyl

open Hecke HeckeInclusion

namespace HeckeCoset

variable {K : Type*} [CommRing K] {q qi : K}

/-! ## Coset representatives: the descending products `r_j = σ_m ⋯ σ_{m-j+1}` -/

/-- The descending product `descProd m j = σ_m σ_{m-1} ⋯ σ_{m-j+1}` of the top
`j` generators of `H_{m+1}(q) = Hecke K q qi (m+1)` (length `j`; `descProd m 0 = 1`).
This is the coset representative `r_j` in the decomposition
`H_{m+1} = Σ_j ι(H_m)·r_j`.  The generator index `m - j` (truncated subtraction)
is always `< m + 1`, so no bound hypothesis is needed. -/
noncomputable def descProd (m : ℕ) : ℕ → Hecke K q qi (m + 1)
  | 0 => 1
  | (j + 1) => descProd m j * σ K q qi (m + 1) ⟨m - j, by omega⟩

@[simp] theorem descProd_zero (m : ℕ) : descProd (K := K) (q := q) (qi := qi) m 0 = 1 := rfl

theorem descProd_succ (m j : ℕ) :
    descProd (K := K) (q := q) (qi := qi) m (j + 1)
      = descProd m j * σ K q qi (m + 1) ⟨m - j, by omega⟩ := rfl

/-! ## Right multiplication of a coset representative by a generator

These four lemmas are the entire content of the coset "bubble".  Writing
`r_j = descProd m j = σ_m σ_{m-1} ⋯ σ_{m-j+1}` (so `r_j` occupies generator
indices `[m-j+1, m]`, and `r_0 = 1`), the product `r_j σ_i` re-expresses as

| case | condition | `r_j · σ_i` |
|---|---|---|
| far commutation | `i + j + 1 ≤ m` | `σ_i · r_j` |
| lengthening | `i + j = m` | `r_{j+1}` |
| quadratic | `i + j = m + 1` | `(q-qi)·r_j + (q·qi)·r_{j-1}` |
| braid | `m + 2 ≤ i + j` | `σ_{i-1} · r_j` |

In every case the result is `(a generator, or a scalar) · r_k` — i.e. it lands
back in `Σ_k ι(H_m)·r_k`, which is exactly what closes the span argument.

**Handedness is the crux.** The spanning family is `ι(H_m)·r_j`, with the
subalgebra on the **left**; so it is *right* multiplication by a generator that
re-enters the family, and the induction must be taken on the right
(`Submonoid.closure_induction_right`).  Left multiplication by the top generator
does *not* reduce this way — `σ_m · ι(w) · r_j` offers no way to move `σ_m` past
`ι(w)` — which is why the left-handed formulation of this lemma looked like the
deep half of the basis theorem.
-/

/-- **Far commutation** (`i + j + 1 ≤ m`): `σ_i` sits at least two below every
factor of `r_j`, so it commutes past the whole descending product. -/
theorem descProd_mul_σ_of_add_lt (m : ℕ) (i : Fin (m + 1)) :
    ∀ j : ℕ, (i : ℕ) + j + 1 ≤ m →
      descProd (K := K) (q := q) (qi := qi) m j * σ K q qi (m + 1) i
        = σ K q qi (m + 1) i * descProd m j
  | 0, _ => by rw [descProd_zero, one_mul, mul_one]
  | (j + 1), h => by
      have hc : σ K q qi (m + 1) ⟨m - j, by first | omega | (simp only []; omega)⟩ * σ K q qi (m + 1) i
          = σ K q qi (m + 1) i * σ K q qi (m + 1) ⟨m - j, by first | omega | (simp only []; omega)⟩ :=
        σ_commute K q qi (m + 1) ⟨m - j, by first | omega | (simp only []; omega)⟩ i (by first | omega | (simp only []; omega))
      rw [descProd_succ, mul_assoc, hc, ← mul_assoc,
        descProd_mul_σ_of_add_lt m i j (by first | omega | (simp only []; omega)), mul_assoc]

/-- **Lengthening** (`i + j = m`): appending `σ_i` to `r_j` is exactly the
recursive step defining `r_{j+1}`. -/
theorem descProd_mul_σ_of_add_eq (m j : ℕ) (i : Fin (m + 1)) (h : (i : ℕ) + j = m) :
    descProd (K := K) (q := q) (qi := qi) m j * σ K q qi (m + 1) i = descProd m (j + 1) := by
  rw [descProd_succ]
  congr 2
  exact Fin.ext (by first | omega | (simp only []; omega))

/-- **Quadratic** (`i + j = m + 1`, `j ≥ 1`): `σ_i` is the *last* factor of `r_j`,
so `r_j σ_i = r_{j-1} σ_i²`, and the Hecke quadratic relation splits it into
`r_j` and `r_{j-1}`. -/
theorem descProd_mul_σ_of_add_eq_succ (m j : ℕ) (i : Fin (m + 1))
    (hj : 1 ≤ j) (h : (i : ℕ) + j = m + 1) :
    descProd (K := K) (q := q) (qi := qi) m j * σ K q qi (m + 1) i
      = (q - qi) • descProd m j + (q * qi) • descProd m (j - 1) := by
  obtain ⟨j', rfl⟩ : ∃ j', j = j' + 1 := ⟨j - 1, by first | omega | (simp only []; omega)⟩
  have hi : (⟨m - j', by first | omega | (simp only []; omega)⟩ : Fin (m + 1)) = i :=
    Fin.ext (by first | omega | (simp only []; omega))
  have hstep : descProd (K := K) (q := q) (qi := qi) m (j' + 1)
      = descProd m j' * σ K q qi (m + 1) i := by rw [descProd_succ, hi]
  rw [hstep, mul_assoc, σ_quadratic, mul_add, mul_smul_comm, mul_smul_comm, mul_one,
    ← hstep]
  simp

/-- **Braid** (`m + 2 ≤ i + j`): `σ_i` lies strictly inside `r_j`, and the
Yang–Baxter move plus far commutation pull `σ_{i-1}` out on the left. -/
theorem descProd_mul_σ_of_le_add (m : ℕ) :
    ∀ (j : ℕ) (i : Fin (m + 1)), j ≤ m + 1 → m + 2 ≤ (i : ℕ) + j →
      descProd (K := K) (q := q) (qi := qi) m j * σ K q qi (m + 1) i
        = σ K q qi (m + 1) ⟨(i : ℕ) - 1, by first | omega | (simp only []; omega)⟩ * descProd m j
  | 0, i, _, h => by exact absurd h (by first | omega | (simp only []; omega))
  | (j + 1), i, hjm, h => by
      -- Under the length bound, the hypothesis forces `i ≥ 1`.
      have hilt : (i : ℕ) < m + 1 := i.isLt
      have hi1 : 1 ≤ (i : ℕ) := by omega
      rcases Nat.lt_or_ge ((i : ℕ) + (j + 1)) (m + 3) with hA | hB
      · -- `i + j = m + 1`: `σ_{i-1}` is the new last factor, `σ_i` the previous one.
        have hj1 : 1 ≤ j := by omega
        obtain ⟨j', rfl⟩ : ∃ j', j = j' + 1 := ⟨j - 1, by first | omega | (simp only []; omega)⟩
        have ha : (⟨m - (j' + 1), by first | omega | (simp only []; omega)⟩ : Fin (m + 1))
            = (⟨(i : ℕ) - 1, by first | omega | (simp only []; omega)⟩ : Fin (m + 1)) := Fin.ext (by first | omega | (simp only []; omega))
        have hb : (⟨m - j', by first | omega | (simp only []; omega)⟩ : Fin (m + 1)) = i := Fin.ext (by first | omega | (simp only []; omega))
        -- `r_{j'+2} = r_{j'} · σ_i · σ_{i-1}`
        have hexp : descProd (K := K) (q := q) (qi := qi) m (j' + 1 + 1)
            = descProd m j' * σ K q qi (m + 1) i
                * σ K q qi (m + 1) ⟨(i : ℕ) - 1, by first | omega | (simp only []; omega)⟩ := by
          rw [descProd_succ, ha, descProd_succ, hb]
        -- Yang–Baxter at `i-1`: `σ_{i-1} σ_i σ_{i-1} = σ_i σ_{i-1} σ_i`.
        have hbraid : σ K q qi (m + 1) i * σ K q qi (m + 1) ⟨(i : ℕ) - 1, by first | omega | (simp only []; omega)⟩
              * σ K q qi (m + 1) i
            = σ K q qi (m + 1) ⟨(i : ℕ) - 1, by first | omega | (simp only []; omega)⟩ * σ K q qi (m + 1) i
              * σ K q qi (m + 1) ⟨(i : ℕ) - 1, by first | omega | (simp only []; omega)⟩ := by
          have hbr := σ_braid K q qi (m + 1) (⟨(i : ℕ) - 1, by first | omega | (simp only []; omega)⟩ : Fin (m + 1))
            (by first | omega | (simp only []; omega))
          have hai : (⟨((⟨(i : ℕ) - 1, by first | omega | (simp only []; omega)⟩ : Fin (m + 1)) : ℕ) + 1, by first | omega | (simp only []; omega)⟩
              : Fin (m + 1)) = i := Fin.ext (by first | omega | (simp only []; omega))
          rw [hai] at hbr
          exact hbr.symm
        -- `σ_{i-1}` commutes past `r_{j'}` (all its indices are `≥ i+1`).
        have hcomm : descProd (K := K) (q := q) (qi := qi) m j'
              * σ K q qi (m + 1) ⟨(i : ℕ) - 1, by first | omega | (simp only []; omega)⟩
            = σ K q qi (m + 1) ⟨(i : ℕ) - 1, by first | omega | (simp only []; omega)⟩ * descProd m j' :=
          descProd_mul_σ_of_add_lt m ⟨(i : ℕ) - 1, by first | omega | (simp only []; omega)⟩ j' (by first | omega | (simp only []; omega))
        calc descProd (K := K) (q := q) (qi := qi) m (j' + 1 + 1) * σ K q qi (m + 1) i
            = descProd m j' * (σ K q qi (m + 1) i
                * σ K q qi (m + 1) ⟨(i : ℕ) - 1, by first | omega | (simp only []; omega)⟩
                * σ K q qi (m + 1) i) := by rw [hexp]; noncomm_ring
          _ = descProd m j' * (σ K q qi (m + 1) ⟨(i : ℕ) - 1, by first | omega | (simp only []; omega)⟩
                * σ K q qi (m + 1) i
                * σ K q qi (m + 1) ⟨(i : ℕ) - 1, by first | omega | (simp only []; omega)⟩) := by rw [hbraid]
          _ = (descProd m j' * σ K q qi (m + 1) ⟨(i : ℕ) - 1, by first | omega | (simp only []; omega)⟩)
                * σ K q qi (m + 1) i
                * σ K q qi (m + 1) ⟨(i : ℕ) - 1, by first | omega | (simp only []; omega)⟩ := by noncomm_ring
          _ = σ K q qi (m + 1) ⟨(i : ℕ) - 1, by first | omega | (simp only []; omega)⟩
                * (descProd m j' * σ K q qi (m + 1) i)
                * σ K q qi (m + 1) ⟨(i : ℕ) - 1, by first | omega | (simp only []; omega)⟩ := by rw [hcomm]; noncomm_ring
          _ = σ K q qi (m + 1) ⟨(i : ℕ) - 1, by first | omega | (simp only []; omega)⟩ * descProd m (j' + 1)
                * σ K q qi (m + 1) ⟨(i : ℕ) - 1, by first | omega | (simp only []; omega)⟩ := by
              rw [descProd_mul_σ_of_add_eq m j' i (by first | omega | (simp only []; omega))]
          _ = σ K q qi (m + 1) ⟨(i : ℕ) - 1, by first | omega | (simp only []; omega)⟩ * descProd m (j' + 1 + 1) := by
              rw [mul_assoc, descProd_mul_σ_of_add_eq m (j' + 1)
                (⟨(i : ℕ) - 1, by first | omega | (simp only []; omega)⟩ : Fin (m + 1)) (by first | omega | (simp only []; omega))]
      · -- `i + j ≥ m + 2`: `σ_i` commutes with the new last factor; recurse.
        have hc : σ K q qi (m + 1) i * σ K q qi (m + 1) ⟨m - j, by first | omega | (simp only []; omega)⟩
            = σ K q qi (m + 1) ⟨m - j, by first | omega | (simp only []; omega)⟩ * σ K q qi (m + 1) i :=
          σ_commute K q qi (m + 1) i ⟨m - j, by first | omega | (simp only []; omega)⟩
            (by first | omega | (simp only []; omega))
        rw [descProd_succ, mul_assoc, ← hc, ← mul_assoc,
          descProd_mul_σ_of_le_add m j i (by first | omega | (simp only []; omega)) (by first | omega | (simp only []; omega)), mul_assoc, ← descProd_succ]

/-! ## The recursively-built spanning family and its index type -/

/-- The finite index type of the coset spanning family of `Hecke K q qi m`.
`cosetIndex 0 = Unit`; `cosetIndex (m+1) = cosetIndex m × Fin (m+2)` — one factor
`Fin (m+2)` for the `m+2` coset representatives added at each tower step.
`Fintype.card (cosetIndex m) = (m+1)!`. -/
def cosetIndex : ℕ → Type
  | 0 => Unit
  | (m + 1) => cosetIndex m × Fin (m + 2)

instance instFintypeCosetIndex : (m : ℕ) → Fintype (cosetIndex m)
  | 0 => (inferInstance : Fintype Unit)
  | (m + 1) =>
      letI := instFintypeCosetIndex m
      (inferInstance : Fintype (cosetIndex m × Fin (m + 2)))

/-- `Fintype.card (cosetIndex m) = (m+1)!` — the family has `(m+1)!` elements. -/
theorem card_cosetIndex : (m : ℕ) → Fintype.card (cosetIndex m) = (m + 1).factorial
  | 0 => rfl
  | (m + 1) => by
      have e : cosetIndex (m + 1) ≃ cosetIndex m × Fin (m + 2) := Equiv.refl _
      rw [Fintype.card_congr e, Fintype.card_prod, Fintype.card_fin, card_cosetIndex m,
        Nat.factorial_succ (m + 1)]
      ring

/-- The coset spanning family `cosetFam m : cosetIndex m → Hecke K q qi m`.
`cosetFam 0 () = 1`; `cosetFam (m+1) (b, j) = ι(cosetFam m b) · r_j`, where
`ι = heckeIncl` is the tower inclusion and `r_j = descProd m j`. -/
noncomputable def cosetFam : (m : ℕ) → cosetIndex m → Hecke K q qi m
  | 0, _ => 1
  | (m + 1), p => heckeIncl K q qi m (cosetFam m p.1) * descProd m p.2.val

theorem cosetFam_succ (m : ℕ) (p : cosetIndex (m + 1)) :
    cosetFam (K := K) (q := q) (qi := qi) (m + 1) p
      = heckeIncl K q qi m (cosetFam m p.1) * descProd m p.2.val := rfl

/-! ## `finrank ≤ card` from a finite spanning set (sorry-free reduction) -/

/-- Generic reduction: a finite set spanning `⊤` bounds the finrank by its card. -/
theorem finrank_le_card_of_span [Nontrivial K] {A : Type*} [AddCommGroup A]
    [Module K A] (s : Finset A) (hs : Submodule.span K (s : Set A) = ⊤) :
    Module.finrank K A ≤ s.card := by
  have h1 := finrank_span_le_card (R := K) (s : Set A)
  rw [hs, finrank_top] at h1
  simpa using h1

/-- `1` lies in the span of the coset family (sorry-free, by induction on `m`).
Base: `cosetFam 0 () = 1`.  Step: `1 = ι(1)·r_0 = ι(cosetFam m b₁)·descProd m 0`
where `b₁` witnesses `1 ∈ span (range (cosetFam m))`; since `heckeIncl` is an
algebra map and `descProd m 0 = 1`, the image of `1` is `1`. -/
theorem one_mem_span_cosetFam :
    (m : ℕ) → (1 : Hecke K q qi m) ∈ Submodule.span K (Set.range (cosetFam m))
  | 0 => Submodule.subset_span ⟨(), rfl⟩
  | (m + 1) => by
      -- `1 = heckeIncl 1 = heckeIncl 1 · r_0`; push `1 ∈ span (range (cosetFam m))`
      -- through the (linear) tower inclusion, which lands each family element at
      -- coset index `(b, 0)`.
      have ih := one_mem_span_cosetFam m
      have hmap : (Submodule.span K (Set.range (cosetFam m))).map
            (heckeIncl K q qi m).toLinearMap
          ≤ Submodule.span K (Set.range (cosetFam (m + 1))) := by
        rw [Submodule.map_span, Submodule.span_le]
        rintro _ ⟨_, ⟨b, rfl⟩, rfl⟩
        apply Submodule.subset_span
        refine ⟨(b, (0 : Fin (m + 2))), ?_⟩
        simp [cosetFam, AlgHom.toLinearMap_apply]
      have h1 : (1 : Hecke K q qi (m + 1)) = (heckeIncl K q qi m).toLinearMap 1 := by simp
      rw [h1]
      exact hmap (Submodule.mem_map_of_mem ih)

/-! ## The spanning statement (crux) and the headline finrank bound -/

/-- **Coset absorption.**  For any `w` in the span of the level-`m` family and any
coset index `k`, the product `ι(w)·r_k` lies in the span of the level-`(m+1)`
family (it *is* a family element when `w` is one). -/
theorem incl_mul_descProd_mem (m : ℕ) (k : Fin (m + 2)) {w : Hecke K q qi m}
    (hw : w ∈ Submodule.span K (Set.range (cosetFam m : cosetIndex m → Hecke K q qi m))) :
    heckeIncl K q qi m w * descProd m (k : ℕ)
      ∈ Submodule.span K
        (Set.range (cosetFam (m + 1) : cosetIndex (m + 1) → Hecke K q qi (m + 1))) := by
  have hMj : (Submodule.span K
        (Set.range (cosetFam m : cosetIndex m → Hecke K q qi m))).map
        ((LinearMap.mulRight K (descProd m (k : ℕ))).comp (heckeIncl K q qi m).toLinearMap)
      ≤ Submodule.span K
        (Set.range (cosetFam (m + 1) : cosetIndex (m + 1) → Hecke K q qi (m + 1))) := by
    rw [Submodule.map_span, Submodule.span_le]
    rintro _ ⟨_, ⟨d, rfl⟩, rfl⟩
    apply Submodule.subset_span
    exact ⟨(d, k), by
      simp [cosetFam, LinearMap.mulRight_apply, LinearMap.comp_apply,
        AlgHom.toLinearMap_apply]⟩
  have hres := hMj (Submodule.mem_map_of_mem hw)
  simpa [LinearMap.mulRight_apply, LinearMap.comp_apply, AlgHom.toLinearMap_apply] using hres

/-- **The coset-span closure lemma (the crux) — right-handed.**  *Right*
multiplication by any generator `σ_i` of `H_{m+1}(q) = Hecke K q qi m` preserves
the `K`-span of the coset family `cosetFam m`.

This is the general-`n` form of the twelve explicit `HeckeDim3.gen_mul_mem`
reductions at `n = 3`, and it is **sorry-free**: each family element
`ι(w)·r_j` meets `σ_i` in exactly one of the four cases of the bubble
(`descProd_mul_σ_of_add_lt` / `_of_add_eq` / `_of_add_eq_succ` / `_of_le_add`,
selected by comparing `i + j` with `m`), and every case returns either a family
element or `ι(w·σ_k)·r_j` with the level-`m` statement available by recursion.

**Why right and not left.**  The family is `ι(H_m)·r_j`, with the subalgebra on
the *left*.  Right multiplication therefore acts on the `r_j` factor, where the
Hecke relations apply; left multiplication by the top generator would have to
move `σ_m` past the opaque `ι(w)`, which no relation does.  Taking the induction
on the correct side is what turns this from "the deep half of the basis theorem"
into a four-case computation. -/
theorem span_mul_gen_mem :
    ∀ (m : ℕ) (i : Fin m) (b : Hecke K q qi m),
      b ∈ Submodule.span K (Set.range (cosetFam m : cosetIndex m → Hecke K q qi m)) →
      b * σ K q qi m i
        ∈ Submodule.span K (Set.range (cosetFam m : cosetIndex m → Hecke K q qi m))
  | 0, i, _, _ => i.elim0
  | (m + 1), i, b, hb => by
      have key : (Submodule.span K
            (Set.range (cosetFam (m + 1) : cosetIndex (m + 1) → Hecke K q qi (m + 1)))).map
            (LinearMap.mulRight K (σ K q qi (m + 1) i))
          ≤ Submodule.span K
            (Set.range (cosetFam (m + 1) : cosetIndex (m + 1) → Hecke K q qi (m + 1))) := by
        rw [Submodule.map_span, Submodule.span_le]
        rintro _ ⟨_, ⟨c, rfl⟩, rfl⟩
        rw [LinearMap.mulRight_apply, cosetFam_succ, mul_assoc]
        have hjlt : (c.2 : ℕ) < m + 2 := c.2.isLt
        have hilt : (i : ℕ) < m + 1 := i.isLt
        have hwmem : cosetFam m c.1 ∈ Submodule.span K
            (Set.range (cosetFam m : cosetIndex m → Hecke K q qi m)) :=
          Submodule.subset_span ⟨c.1, rfl⟩
        rcases lt_trichotomy ((i : ℕ) + (c.2 : ℕ)) m with hlt | heq | hgt
        · -- far commutation: `r_j σ_i = σ_i r_j`, and `σ_i = ι(σ_i)`
          have hi' : (i : ℕ) < m := by omega
          have hσ : heckeIncl K q qi m (σ K q qi m ⟨(i : ℕ), hi'⟩) = σ K q qi (m + 1) i := by
            rw [heckeIncl_σ]; congr 1
          rw [descProd_mul_σ_of_add_lt m i (c.2 : ℕ) (by omega), ← mul_assoc, ← hσ, ← map_mul]
          exact incl_mul_descProd_mem m c.2 (span_mul_gen_mem m ⟨(i : ℕ), hi'⟩ _ hwmem)
        · -- lengthening: `r_j σ_i = r_{j+1}`
          rw [descProd_mul_σ_of_add_eq m (c.2 : ℕ) i heq]
          have hk : ((c.2 : ℕ) + 1) < m + 2 := by omega
          have hcast : descProd (K := K) (q := q) (qi := qi) m ((c.2 : ℕ) + 1)
              = descProd m ((⟨(c.2 : ℕ) + 1, hk⟩ : Fin (m + 2)) : ℕ) := rfl
          rw [hcast]
          exact incl_mul_descProd_mem m ⟨(c.2 : ℕ) + 1, hk⟩ hwmem
        · rcases eq_or_lt_of_le (Nat.succ_le_of_lt hgt) with heq2 | hgt2
          · -- quadratic: `r_j σ_i = (q-qi)·r_j + (q·qi)·r_{j-1}`
            have hj1 : 1 ≤ (c.2 : ℕ) := by omega
            rw [descProd_mul_σ_of_add_eq_succ m (c.2 : ℕ) i hj1 (by omega), mul_add,
              mul_smul_comm, mul_smul_comm]
            refine Submodule.add_mem _ (Submodule.smul_mem _ _ ?_) (Submodule.smul_mem _ _ ?_)
            · exact incl_mul_descProd_mem m c.2 hwmem
            · have hk : ((c.2 : ℕ) - 1) < m + 2 := by omega
              have hcast : descProd (K := K) (q := q) (qi := qi) m ((c.2 : ℕ) - 1)
                  = descProd m ((⟨(c.2 : ℕ) - 1, hk⟩ : Fin (m + 2)) : ℕ) := rfl
              rw [hcast]
              exact incl_mul_descProd_mem m ⟨(c.2 : ℕ) - 1, hk⟩ hwmem
          · -- braid: `r_j σ_i = σ_{i-1} r_j`, and `σ_{i-1} = ι(σ_{i-1})`
            have hi' : (i : ℕ) - 1 < m := by omega
            have hσ : heckeIncl K q qi m (σ K q qi m ⟨(i : ℕ) - 1, hi'⟩)
                = σ K q qi (m + 1) ⟨(i : ℕ) - 1, by omega⟩ := by
              rw [heckeIncl_σ]; congr 1
            rw [descProd_mul_σ_of_le_add m (c.2 : ℕ) i (by omega) (by omega), ← mul_assoc,
              ← hσ, ← map_mul]
            exact incl_mul_descProd_mem m c.2 (span_mul_gen_mem m ⟨(i : ℕ) - 1, hi'⟩ _ hwmem)
      exact key (Submodule.mem_map_of_mem hb)

/-- **The coset family spans `H_{m+1}(q)`** (`span = ⊤`), from the right-handed
closure lemma `span_mul_gen_mem` via the adjoin-equals-span-of-submonoid route
(exactly as `HeckeDim3.span_sixWords_eq_top` at `n = 3`, but inducting on the
right). -/
theorem span_cosetFam_eq_top (m : ℕ) :
    Submodule.span K (Set.range (cosetFam m : cosetIndex m → Hecke K q qi m)) = ⊤ := by
  rw [eq_top_iff]
  rintro x -
  have hx : x ∈ Algebra.adjoin K (Set.range (σ K q qi m)) := by
    rw [adjoin_range_σ_eq_top]; trivial
  have hspan : x ∈ Submodule.span K
      (↑(Submonoid.closure (Set.range (σ K q qi m))) : Set (Hecke K q qi m)) := by
    rw [← Algebra.adjoin_eq_span]; exact hx
  refine Submodule.span_le.mpr ?_ hspan
  intro y hy
  induction hy using Submonoid.closure_induction_right with
  | one => exact one_mem_span_cosetFam m
  | mul_right a _ b hb ih =>
      obtain ⟨i, rfl⟩ := hb
      exact span_mul_gen_mem m i a ih

/-- **The headline coset spanning bound** `dim_K H_{m+1}(q) ≤ (m+1)!`
(`Hecke K q qi m = H_{m+1}(q)`), proved from `span_cosetFam_eq_top` and the
family-cardinality count `card_cosetIndex`. -/
theorem finrank_le_factorial [Nontrivial K] (m : ℕ) :
    Module.finrank K (Hecke K q qi m) ≤ (m + 1).factorial := by
  classical
  have hspans : Submodule.span K
      ((Finset.univ.image (cosetFam m) : Finset (Hecke K q qi m)) : Set (Hecke K q qi m)) = ⊤ := by
    rw [Finset.coe_image, Finset.coe_univ, Set.image_univ]
    exact span_cosetFam_eq_top m
  calc Module.finrank K (Hecke K q qi m)
      ≤ (Finset.univ.image (cosetFam m)).card := finrank_le_card_of_span _ hspans
    _ ≤ (Finset.univ : Finset (cosetIndex m)).card := Finset.card_image_le
    _ = Fintype.card (cosetIndex m) := Finset.card_univ
    _ = (m + 1).factorial := card_cosetIndex m

end HeckeCoset

end QOU.SchurWeyl

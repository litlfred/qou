import Mathlib.LinearAlgebra.Basis.Basic
import Mathlib.LinearAlgebra.Dimension.StrongRankCondition
import Mathlib.LinearAlgebra.Finsupp.VectorSpace
import Mathlib.Data.Fintype.EquivFin
import Mathlib.Data.Fintype.OfMap
import Mathlib.Data.Finset.Max
import QOU.BraidKnot.StandardYoungTableau
import QOU.BraidKnot.Specht
import Mathlib.Tactic.Group

/-!
# QOU.BraidKnot.SpechtStandardBasisCore — brick-4 definitions + the order-agnostic core

**Definitions-and-lower-machinery half** of brick 4's standard-basis theorem for
Specht modules (`dim_k S^μ = #SYT(μ)`, Sagan, *The Symmetric Group*, Thm 2.5.2).

This module holds **all the brick-4 objects and every lemma that does not itself
depend on the dominance/triangular core** — the SYT→tableau conversion, the
standard polytabloids, the abstract `Triangular` lever, the corestriction
reduction, and the spanning half (with its single honest straightening stub).

It sits **below** the two independence cores (`SpechtDominanceCore`,
`SpechtTriangularCore`), which import it read-only. The triangular-dependent
capstone declarations (`standardPolytabloid_triangular` — now **proved** by
consuming `SpechtTriangularCore.standardPolytabloid_triangular'` — plus
`standardPolytabloid_linearIndependent`, `standardBasis`,
`specht_finrank_eq_numSYT`) live **above** those cores, in
`QOU.BraidKnot.SpechtStandardBasis`.

Everything here is declared in the `QOU.BraidKnot.SpechtStandardBasis`
namespace (unchanged), so downstream references (`SpechtStandardBasis.sytToTableau`,
`.cellLabel`, `.standardPolytabloid`, `.leadTab`, `.Triangular`,
`.linearIndependent_corestrict_iff`, `.standardPolytabloid_span`, …) resolve exactly
as before — `SpechtStandardBasis` re-exports this file by importing it.

So the opaque dimension identity `dim = numSYT` becomes a clean map:
*"it is a basis question — linear independence + spanning, both classically
cited, everything else machine-checked."*

## sorry-free ↔ stubbed map

| Declaration | Status |
|---|---|
| `cellLabel`, `cellLabel_injective` | **sorry-free** (injectivity of `T.entry` via `inj_on`) |
| `instFintypeStandardYoungTableau` | **sorry-free** (`Fintype` of an SYT via `Fintype.ofInjective`) |
| `sytToTableau` | **sorry-free** (the bijective filling `Fin n ≃ μ.cells`) |
| `standardPolytabloid` | **sorry-free** (definition) |
| `standardPolytabloid_mem` | **sorry-free** (lands in `S^μ`) |
| `standardPolytabloidS` (corestriction) | **sorry-free** |
| `standardPolytabloid_linearIndependent` | **STUB** `sorry` — `-- Ref: [sagan2001]` Thm 2.5.2 |
| `colStab_smul_self`, `polytabloid_colStab_smul` (column-antisymmetry) | **sorry-free** |
| `domCount'`, `domWeight`, `domBound`, `domCount'_le`, `domWeight_le` (the dominance measure) | **sorry-free** |
| `straightening_step_colMax` (Garnir core, **column-maximal case**) | **STUB** `sorry` — `-- Ref: [sagan2001]` §2.6 |
| `straightening_step` (Garnir straightening core) | **sorry-free MODULO `straightening_step_colMax`** (column-sort dichotomy: the `domWeight`-raising branch is proved outright via `polytabloid_colStab_smul`) |
| `standardPolytabloid_straightening` | **sorry-free MODULO `straightening_step_colMax`** (well-founded induction on the dominance weight) |
| `standardPolytabloid_span` | **sorry-free MODULO `straightening_step_colMax`** (Garnir relations) |
| `standardBasis` | **sorry-free MODULO the two stubs** (`Basis.mk` wiring) |
| `specht_finrank_eq_numSYT` | **sorry-free MODULO the two stubs** (the reduction) |

The reduction (`standardBasis` + `specht_finrank_eq_numSYT`) is **genuinely
sorry-free**: its only `sorry`-tainted inputs are the two named classical facts
(`standardPolytabloid_linearIndependent`, and — via
`standardPolytabloid_straightening` and `straightening_step` — the single Garnir
core `straightening_step_colMax`). The
SYT→tableau conversion **and** the `Fintype` instance brick 1 left open are
*both* proved sorry-free here.

**Spanning half — reduction (this file, §3b).** The former single spanning stub
`standardPolytabloid_straightening` (every polytabloid `e_t` lies in the span of
the *standard* polytabloids) is now **proved sorry-free by well-founded induction**
on a self-contained dominance weight (`domWeight`, a strictly-monotone ℕ-valued
linear extension of Sagan's dominance order, defined locally because this file sits
*below* `SpechtDominanceCore` in the import graph), reducing the whole spanning
half to a **single** sharper combinatorial core, `straightening_step`: a
*non-standard* polytabloid is a `k`-combination of polytabloids of strictly
dominance-greater (`domWeight`-greater) tabloids (Sagan §2.6 Garnir relations).

That core is itself now **proved sorry-free MODULO a still-sharper residual**,
`straightening_step_colMax`, via a **column-sort dichotomy** on whether some column
permutation `σ ∈ C_t` strictly raises `domWeight`. The `domWeight`-raising branch is
discharged outright by the column-antisymmetry lemma `polytabloid_colStab_smul`
(`e_{σ·t} = sgn(σ)·e_t` for `σ ∈ C_t`, proved sorry-free here): since `sgn(σ)² = 1`,
`e_t = sgn(σ)·e_{σ·t}`, a one-term combination whose single term is strictly
`domWeight`-greater by the branch hypothesis. What remains is only the
**column-maximal** branch (no `σ ∈ C_t` raises `domWeight`, so the column-sort is
exhausted): the genuine Garnir coset-sum at a row descent, isolated as the residual
`straightening_step_colMax` with the sharpening hypothesis that `t` is
column-dominance-maximal.

## References
- [sagan2001] Sagan, *The Symmetric Group*, §2.5 (the standard basis, Thm 2.5.2;
  independence via the dominance/last-letter order, spanning via Garnir
  relations).
- [james1984representation] James, *The Representation Theory of the Symmetric
  Groups* (Specht modules, the standard basis theorem).
- [fulton1997] Fulton, *Young Tableaux* (tableaux / tabloids, standard fillings).
-/

open scoped BigOperators

namespace QOU.BraidKnot.SpechtStandardBasis

open QOU.BraidKnot
open QOU.BraidKnot.Specht

variable {k : Type} [Field k] [CharZero k]
variable {μ : YoungDiagram}

/-! ## 1. SYT → general tableau conversion (sorry-free)

A standard Young tableau `T` assigns to each cell `(i, j) ∈ μ` a label
`T.entry i j < μ.card`, *injectively* (`T.inj_on`). Reading this off as a map
`μ.cells → Fin (μ.card)` gives an injection between two finite types of equal
cardinality (`Fintype.card μ.cells = μ.cells.card = μ.card`), hence a bijection.
Inverting it yields the general (bijective) tableau `Fin (nOf μ) ≃ μ.cells` that
brick 2 consumes. -/

/-- The label that a standard tableau `T` assigns to a cell, as an element of
`Fin (μ.card) = Fin (nOf μ)`. The bound is exactly `T.lt_card`. -/
def cellLabel (T : StandardYoungTableau μ) : μ.cells → Fin (nOf μ) :=
  fun c => ⟨T.entry c.1.1 c.1.2, T.lt_card c.1.1 c.1.2 ((YoungDiagram.mem_cells _).1 c.2)⟩

/-- `cellLabel T` is injective: distinct cells carry distinct labels (`T.inj_on`). -/
theorem cellLabel_injective (T : StandardYoungTableau μ) :
    Function.Injective (cellLabel T) := by
  rintro ⟨⟨i, j⟩, hc⟩ ⟨⟨i', j'⟩, hc'⟩ h
  have hmem : (i, j) ∈ μ := (YoungDiagram.mem_cells _).1 hc
  have hmem' : (i', j') ∈ μ := (YoungDiagram.mem_cells _).1 hc'
  have hval : T.entry i j = T.entry i' j' := by
    simpa [cellLabel, Fin.ext_iff] using h
  obtain ⟨hi, hj⟩ := T.inj_on i j i' j' hmem hmem' hval
  subst hi; subst hj; rfl

/-- **`Fintype (StandardYoungTableau μ)`** — the instance brick 1 left open.

An SYT is determined by its values on `μ.cells` (off-cell entries are pinned to
`0` by `zero_off`, and the bounds/strictness fields are `Prop`s). The map
`T ↦ (the restricted entry function on cells)` into the *finite* function space
`μ.cells → Fin (μ.card)` is injective, so `Fintype.ofInjective` supplies the
instance. (Two SYTs agreeing on every cell are equal: on-cells by the agreement,
off-cells by `zero_off` — discharged via the `@[ext]` lemma.)

This is a **bonus**: the headline `specht_finrank_eq_numSYT` uses
`Module.finrank_eq_nat_card_basis` (which needs no `Fintype` on the index), so
it does not depend on this instance. Provided here to close brick 1's open
instance sorry-free. -/
noncomputable instance instFintypeStandardYoungTableau :
    Fintype (StandardYoungTableau μ) :=
  Fintype.ofInjective (β := μ.cells → Fin (nOf μ)) cellLabel <| by
    intro T T' h
    ext i j
    by_cases hij : (i, j) ∈ μ
    · -- on a cell: the labels agree, so the entries agree
      have hc : (i, j) ∈ μ.cells := (YoungDiagram.mem_cells _).2 hij
      have := congrFun h ⟨(i, j), hc⟩
      simpa [cellLabel, Fin.ext_iff] using this
    · -- off a cell: both pinned to 0 by `zero_off`
      rw [T.zero_off i j hij, T'.zero_off i j hij]

/-- `cellLabel T` is bijective: an injection between two finite types of equal
cardinality (`card μ.cells = μ.cells.card = μ.card = nOf μ`). -/
theorem cellLabel_bijective (T : StandardYoungTableau μ) :
    Function.Bijective (cellLabel T) := by
  rw [Fintype.bijective_iff_injective_and_card]
  refine ⟨cellLabel_injective T, ?_⟩
  rw [Fintype.card_coe, Fintype.card_fin]

/-- **SYT → general tableau** (sorry-free). The bijective filling
`Fin (nOf μ) ≃ μ.cells` reading off `T.entry`: label `l ↦` the unique cell whose
entry is `l`. Built by inverting the bijection `cellLabel T : μ.cells ≃ Fin n`. -/
noncomputable def sytToTableau (T : StandardYoungTableau μ) : Specht.Tableau μ :=
  (Equiv.ofBijective (cellLabel T) (cellLabel_bijective T)).symm

/-! ## 2. Standard polytabloids (sorry-free definitions) -/

/-- The **standard polytabloid** `e_T = e_{sytToTableau T} ∈ M^μ` of a standard
Young tableau `T`. These are the candidate basis vectors of `S^μ`. -/
noncomputable def standardPolytabloid (T : StandardYoungTableau μ) :
    Specht.Mtab (k := k) μ :=
  Specht.polytabloid (k := k) (sytToTableau T)

omit [CharZero k] in
/-- Every standard polytabloid lies in the Specht module (it is a polytabloid). -/
theorem standardPolytabloid_mem (T : StandardYoungTableau μ) :
    standardPolytabloid (k := k) T ∈ Specht.SpechtSubmodule (k := k) μ :=
  Specht.polytabloid_mem_specht (k := k) (sytToTableau T)

/-- The standard polytabloid **corestricted** to `S^μ` (i.e. valued in the
submodule `Specht.SpechtSubmodule μ`), using `standardPolytabloid_mem`. This is
the family `Basis.mk` builds a basis from. -/
noncomputable def standardPolytabloidS (T : StandardYoungTableau μ) :
    Specht.SpechtSubmodule (k := k) μ :=
  ⟨standardPolytabloid (k := k) T, standardPolytabloid_mem (k := k) T⟩

/-! ## 3. The two genuine content obligations

The linear-independence half (§3a) is **reduced**, sorry-free, to a single
combinatorial core (`standardPolytabloid_triangular`) via a locally-proved
triangular-independence lever; the spanning half (§3b) remains one honest stub. -/

/-! ### 3a. Linear independence — reduced to Sagan's dominance lemma

The classical independence argument is *unitriangularity in the dominance order*:
`e_T = ±{T} + (dominated terms)`, so the standard polytabloids form a triangular
family over the tabloid basis and are therefore independent. The "triangular ⇒
independent" lever is **absent from the pinned Mathlib** (its only such machinery is
Gram–Schmidt-specific, requiring an inner-product space), so we supply it locally,
sorry-free, and reduce the obligation to exactly Sagan's dominance lemma. -/

/-- The triangular hypothesis bundle (upper-bound form), over any `CommRing`:
`lead` injective, the diagonal coefficient `(v i)(lead i)` a unit, and `lead i` an
upper bound of `supp (v i)`. -/
structure Triangular {ι : Type*} {α : Type*} {R : Type*} [LinearOrder α] [CommRing R]
    (v : ι → (α →₀ R)) (lead : ι → α) : Prop where
  /-- distinct vectors have distinct leading indices -/
  lead_inj : Function.Injective lead
  /-- the diagonal coefficient is a unit -/
  diag_unit : ∀ i, IsUnit ((v i) (lead i))
  /-- `lead i` is an upper bound of `supp (v i)` -/
  supp_le : ∀ i, ∀ a ∈ (v i).support, a ≤ lead i

/-- **Triangular-independence lever** — the lemma the pinned Mathlib lacks, supplied
sorry-free. A triangular `Finsupp` family (injective leading map, unit diagonal,
support bounded above by the leading index) is linearly independent. Maximal-leading-
index argument; works over any `CommRing`. A natural Mathlib-upstream candidate. -/
theorem Triangular.linearIndependent {ι : Type*} {α : Type*} {R : Type*}
    [LinearOrder α] [CommRing R] {v : ι → (α →₀ R)} {lead : ι → α}
    (h : Triangular v lead) : LinearIndependent R v := by
  classical
  rw [linearIndependent_iff']
  intro s g hsum
  by_contra hne
  push_neg at hne
  obtain ⟨i, hiS, hgi⟩ := hne
  set T : Finset ι := s.filter (fun i => g i ≠ 0) with hT
  have hiT : i ∈ T := by rw [hT]; simp [hiS, hgi]
  obtain ⟨i₀, hi₀T, hi₀max⟩ := T.exists_max_image lead ⟨i, hiT⟩
  have hg0 : g i₀ ≠ 0 := by rw [hT] at hi₀T; exact (Finset.mem_filter.mp hi₀T).2
  have hi₀S : i₀ ∈ s := by rw [hT] at hi₀T; exact (Finset.mem_filter.mp hi₀T).1
  have hpt : (∑ j ∈ s, g j • v j) (lead i₀) = 0 := by rw [hsum]; rfl
  rw [Finsupp.finset_sum_apply] at hpt
  have hterm : ∀ j, (g j • v j) (lead i₀) = g j * (v j) (lead i₀) := by
    intro j; rw [Finsupp.smul_apply, smul_eq_mul]
  simp_rw [hterm] at hpt
  have hzero : ∀ j ∈ s, j ≠ i₀ → g j * (v j) (lead i₀) = 0 := by
    intro j hjS hji₀
    by_cases hgj : g j = 0
    · rw [hgj, zero_mul]
    · have hjT : j ∈ T := by rw [hT]; simp [hjS, hgj]
      have hlt : lead j < lead i₀ :=
        lt_of_le_of_ne (hi₀max j hjT) (fun heq => hji₀ (h.lead_inj heq))
      have : (v j) (lead i₀) = 0 :=
        Finsupp.notMem_support_iff.mp
          (fun hmem => absurd (h.supp_le j (lead i₀) hmem) (not_le.mpr hlt))
      rw [this, mul_zero]
  rw [Finset.sum_eq_single i₀ (fun j hjS hji₀ => hzero j hjS hji₀)
      (fun hi₀notS => absurd hi₀S hi₀notS)] at hpt
  refine hg0 ?_
  rcases (h.diag_unit i₀).exists_right_inv with ⟨c, hc⟩
  have hcalc := congrArg (· * c) hpt
  simp only [zero_mul] at hcalc
  rwa [mul_assoc, hc, mul_one] at hcalc

/-- The concrete **leading-tabloid map** `lead T = {sytToTableau T}` (the row-class of
`T`'s own filling) — the leading tabloid of `e_T`. Sorry-free. -/
noncomputable def leadTab (T : StandardYoungTableau μ) : Specht.Tabloid μ :=
  Specht.Tabloid.mk (sytToTableau T)

omit [CharZero k] in
/-- `(S^μ).subtype ∘ standardPolytabloidS = standardPolytabloid` (definitional). -/
theorem subtype_comp_standardPolytabloidS :
    (Specht.SpechtSubmodule (k := k) μ).subtype ∘ standardPolytabloidS (k := k) (μ := μ)
      = standardPolytabloid (k := k) (μ := μ) := by
  funext T; rfl

omit [CharZero k] in
/-- **Corestriction reflects independence**: independence of `standardPolytabloidS`
(in `S^μ`) ⟺ independence of `standardPolytabloid` (in `M^μ`), since the `S^μ`
inclusion has trivial kernel. Sorry-free. -/
theorem linearIndependent_corestrict_iff :
    LinearIndependent k (standardPolytabloidS (k := k) (μ := μ))
      ↔ LinearIndependent k (standardPolytabloid (k := k) (μ := μ)) := by
  have hker : LinearMap.ker (Specht.SpechtSubmodule (k := k) μ).subtype = ⊥ :=
    Submodule.ker_subtype _
  have key := LinearMap.linearIndependent_iff
      (Specht.SpechtSubmodule (k := k) μ).subtype hker
      (v := standardPolytabloidS (k := k) (μ := μ))
  rw [subtype_comp_standardPolytabloidS] at key
  exact key.symm

/-! ### 3b. Spanning (single honest stub)

(The triangular-dependent `standardPolytabloid_triangular` — now proved — and
`standardPolytabloid_linearIndependent` live in `SpechtStandardBasis`, above the
independence cores.) -/

/-! #### The column-antisymmetry lemma (`e_{σ·t} = sgn(σ)·e_t`, sorry-free)

The first ingredient of Sagan's §2.6 straightening algorithm: a column
permutation `σ ∈ C_t` acts on the polytabloid by its sign. This is the
"column-sort" reduction — every `e_t` equals `±e_{column-sorted t}`. -/

/-- For `σ ∈ C_t`, the column stabilizer is `σ`-invariant: `C_{σ·t} = C_t`.
(`colPattern (σ·t) = σ · colPattern t = colPattern t` since `σ ∈ C_t`.) -/
theorem colStab_smul_self (t : Specht.Tableau μ) {σ : Equiv.Perm (Fin (Specht.nOf μ))}
    (hσ : σ ∈ Specht.colStab t) : Specht.colStab (σ • t) = Specht.colStab t := by
  unfold Specht.colStab
  rw [Specht.colPattern_smul, Specht.mem_colStab.mp hσ]

omit [CharZero k] in
/-- **Column-antisymmetry (sorry-free).** A column permutation `σ ∈ C_t` acts on
the polytabloid by its sign: `e_{σ·t} = sgn(σ)·e_t`. The sum over `C_{σ·t} = C_t`
is reindexed `ρ ↦ ρσ` (right multiplication by `σ ∈ C_t`), using
`sgn(ρσ) = sgn(ρ)sgn(σ)`, `ρ·(σ·t) = (ρσ)·t`, and `sgn(σ)² = 1`. This is the
column-sort step of Sagan §2.6: every polytabloid equals `±` its
column-standardised representative. -/
theorem polytabloid_colStab_smul (t : Specht.Tableau μ)
    {σ : Equiv.Perm (Fin (Specht.nOf μ))} (hσ : σ ∈ Specht.colStab t) :
    Specht.polytabloid (k := k) (σ • t)
      = (Equiv.Perm.sign σ : ℤ) • Specht.polytabloid (k := k) t := by
  classical
  have hEq : Specht.colStab (σ • t) = Specht.colStab t := colStab_smul_self t hσ
  have hs2 : (Equiv.Perm.sign σ : ℤ) * (Equiv.Perm.sign σ : ℤ) = 1 := by
    rcases Int.units_eq_one_or (Equiv.Perm.sign σ) with h | h <;> rw [h] <;> decide
  rw [Specht.polytabloid, Specht.polytabloid, Finset.smul_sum]
  refine Finset.sum_bij'
    (i := fun (ρ : Specht.colStab (σ • t)) _ =>
      (⟨(ρ : Equiv.Perm (Fin (Specht.nOf μ))) * σ, ?_⟩ : Specht.colStab t))
    (j := fun (π : Specht.colStab t) _ =>
      (⟨(π : Equiv.Perm (Fin (Specht.nOf μ))) * σ⁻¹, ?_⟩ : Specht.colStab (σ • t)))
    ?_ ?_ ?_ ?_ ?_
  · exact Subgroup.mul_mem _ (hEq ▸ ρ.2) hσ
  · exact hEq.symm ▸ Subgroup.mul_mem _ π.2 (Subgroup.inv_mem _ hσ)
  · intro ρ _; exact Finset.mem_univ _
  · intro π _; exact Finset.mem_univ _
  · intro ρ _; apply Subtype.ext; simp [mul_assoc]
  · intro π _; apply Subtype.ext; simp [mul_assoc]
  · intro ρ _
    have e1 : (ρ : Equiv.Perm (Fin (Specht.nOf μ))) • (σ • t)
        = ((ρ : Equiv.Perm (Fin (Specht.nOf μ))) * σ) • t := (mul_smul _ _ _).symm
    show (Equiv.Perm.sign (ρ : Equiv.Perm (Fin (Specht.nOf μ))) : ℤ)
          • Specht.Mtab.of (k := k) ((ρ : Equiv.Perm (Fin (Specht.nOf μ))) • (σ • t))
      = (Equiv.Perm.sign σ : ℤ) • ((Equiv.Perm.sign
            ((ρ : Equiv.Perm (Fin (Specht.nOf μ))) * σ) : ℤ)
          • Specht.Mtab.of (k := k) (((ρ : Equiv.Perm (Fin (Specht.nOf μ))) * σ) • t))
    rw [e1, ← mul_smul]
    congr 1
    rw [map_mul]
    push_cast
    have : (Equiv.Perm.sign σ : ℤ)
        * ((Equiv.Perm.sign (ρ : Equiv.Perm (Fin (Specht.nOf μ))) : ℤ) * (Equiv.Perm.sign σ : ℤ))
      = (Equiv.Perm.sign (ρ : Equiv.Perm (Fin (Specht.nOf μ))) : ℤ)
        * ((Equiv.Perm.sign σ : ℤ) * (Equiv.Perm.sign σ : ℤ)) := by ring
    rw [this, hs2, mul_one]

omit [CharZero k] in
/-- **Garnir annihilation — algebraic core (sorry-free).** The sign-reversing
involution at the heart of every Garnir relation. If `τ` is an involution
(`τ*τ = 1`) of sign `-1` lying in the *row* stabiliser of `t` (so `τ` fixes the
tabloid `{t}`), and `G` is a finite set of permutations closed under right
multiplication by `τ`, then the signed sum of basis tabloids
`∑_{g∈G} sgn(g)·{g·t}` vanishes: pairing `g ↔ gτ` cancels terms, because
`{gτ·t} = {g·t}` (`τ` fixes the row pattern) while `sgn(gτ) = -sgn(g)`.
This is the Mathlib-side realisation of "the full column antisymmetriser of a
Garnir set annihilates the tabloid" (Sagan §2.6). It is the algebraic ingredient
the column-maximal Garnir core (`straightening_step_colMax`, still `sorry`)
consumes; the three pieces still missing on top of it — the coset→polytabloid
antisymmetriser bridge (needs `CharZero k`), the Garnir-set/row-descent existence
for a column-maximal non-standard tableau, and the dominance strict-increase —
are recorded in the module docstring. -/
-- Ref: [sagan2001] Sagan, *The Symmetric Group*, §2.6 (Garnir relations).
theorem mtab_sum_sign_smul_of_eq_zero (t : Specht.Tableau μ)
    (G : Finset (Equiv.Perm (Fin (Specht.nOf μ))))
    (τ : Equiv.Perm (Fin (Specht.nOf μ)))
    (hτ2 : τ * τ = 1) (hτsign : Equiv.Perm.sign τ = -1)
    (hτrow : τ ∈ Specht.rowStab t)
    (hGclosed : ∀ g ∈ G, g * τ ∈ G) :
    ∑ g ∈ G, (Equiv.Perm.sign g : ℤ) • Specht.Mtab.of (k := k) (g • t) = 0 := by
  classical
  -- `τ` fixes the tabloid of `t`: `{τ·t} = {t}`.
  have hrow : Specht.Tabloid.mk (τ • t) = Specht.Tabloid.mk t :=
    Quotient.sound (by
      show Specht.rowPattern (τ • t) = Specht.rowPattern t
      rw [Specht.rowPattern_smul]; exact Specht.mem_rowStab.mp hτrow)
  -- Hence `of ((g*τ)·t) = of (g·t)` for every `g`.
  have hofeq : ∀ g : Equiv.Perm (Fin (Specht.nOf μ)),
      Specht.Mtab.of (k := k) ((g * τ) • t) = Specht.Mtab.of (k := k) (g • t) := by
    intro g
    have hmk : Specht.Tabloid.mk ((g * τ) • t) = Specht.Tabloid.mk (g • t) := by
      rw [mul_smul, ← Specht.Tabloid.smul_mk g (τ • t), hrow, Specht.Tabloid.smul_mk]
    simp only [Specht.Mtab.of, hmk]
  -- Sign is reversed by right-multiplication with `τ`.
  have hs : ∀ g : Equiv.Perm (Fin (Specht.nOf μ)),
      (Equiv.Perm.sign (g * τ) : ℤ) = -(Equiv.Perm.sign g : ℤ) := by
    intro g; rw [map_mul, hτsign]; simp
  refine Finset.sum_involution (fun g _ => g * τ) ?_ ?_ ?_ ?_
  · -- paired terms cancel
    intro g _
    rw [hofeq g, hs g, neg_smul]
    abel
  · -- involution is fixed-point free (τ ≠ 1), so the `f a ≠ 0 → …` premise is free
    intro g _ _ hgg
    have hτ1 : τ = 1 := by
      have hg1 : g * τ = g * 1 := by rw [mul_one]; exact hgg
      exact mul_left_cancel hg1
    rw [hτ1, map_one] at hτsign
    exact absurd hτsign (by decide)
  · -- closed under the involution
    intro g hg; exact hGclosed g hg
  · -- it is an involution
    intro g _; show (g * τ) * τ = g
    rw [mul_assoc, hτ2, mul_one]

omit [CharZero k] in
/-- **Column-stabiliser conjugation.** `ρ ∈ C_{σ·t} ↔ σ⁻¹ρσ ∈ C_t` — the column
stabiliser transforms by conjugation under the `Sₙ` action, since
`colPattern (σ·t) = σ · colPattern t`. -/
theorem mem_colStab_smul (σ : Equiv.Perm (Fin (Specht.nOf μ))) (t : Specht.Tableau μ)
    (ρ : Equiv.Perm (Fin (Specht.nOf μ))) :
    ρ ∈ Specht.colStab (σ • t) ↔ σ⁻¹ * ρ * σ ∈ Specht.colStab t := by
  rw [Specht.mem_colStab, Specht.mem_colStab, Specht.colPattern_smul]
  constructor
  · intro h
    rw [mul_smul, mul_smul, h, ← mul_smul, inv_mul_cancel, one_smul]
  · intro h
    rw [← mul_smul]
    have hrw : ρ * σ = σ * (σ⁻¹ * ρ * σ) := by group
    rw [hrw, mul_smul, h]

omit [CharZero k] in
/-- **Polytabloid equivariance (sorry-free).** The polytabloid is `Sₙ`-equivariant:
`e_{σ·t} = σ · e_t`, i.e. acting on the tableau by `σ` equals acting on the
polytabloid by the module representation `Mtab.rep`. Reindex the column-stabiliser
sum by the conjugation `π ↦ σπσ⁻¹` (bijecting `C_t ≅ C_{σ·t}`, preserving sign,
and sending `σ·(π·t)` to `(σπσ⁻¹)·(σ·t)`). -/
theorem polytabloid_rep_smul (σ : Equiv.Perm (Fin (Specht.nOf μ))) (t : Specht.Tableau μ) :
    Specht.polytabloid (k := k) (σ • t)
      = Specht.Mtab.rep μ σ (Specht.polytabloid (k := k) t) := by
  classical
  rw [Specht.polytabloid, Specht.polytabloid, map_sum]
  refine Finset.sum_bij'
    (i := fun (ρ : Specht.colStab (σ • t)) _ =>
      (⟨σ⁻¹ * (ρ : Equiv.Perm (Fin (Specht.nOf μ))) * σ,
        (mem_colStab_smul σ t _).mp ρ.2⟩ : Specht.colStab t))
    (j := fun (π : Specht.colStab t) _ =>
      (⟨σ * (π : Equiv.Perm (Fin (Specht.nOf μ))) * σ⁻¹, ?_⟩ : Specht.colStab (σ • t)))
    ?_ ?_ ?_ ?_ ?_
  · -- `σπσ⁻¹ ∈ C_{σ·t}`
    rw [mem_colStab_smul]
    have : σ⁻¹ * (σ * (π : Equiv.Perm (Fin (Specht.nOf μ))) * σ⁻¹) * σ
        = (π : Equiv.Perm (Fin (Specht.nOf μ))) := by group
    rw [this]; exact π.2
  · intro ρ _; exact Finset.mem_univ _
  · intro π _; exact Finset.mem_univ _
  · -- left inverse `j (i ρ) = ρ`
    intro ρ _; apply Subtype.ext
    show σ * (σ⁻¹ * (ρ : Equiv.Perm (Fin (Specht.nOf μ))) * σ) * σ⁻¹ = ρ
    group
  · -- right inverse `i (j π) = π`
    intro π _; apply Subtype.ext
    show σ⁻¹ * (σ * (π : Equiv.Perm (Fin (Specht.nOf μ))) * σ⁻¹) * σ = π
    group
  · -- term equality
    intro ρ _
    rw [map_zsmul, Specht.Mtab.rep_of]
    congr 1
    · -- sign: `sgn ρ = sgn (σ⁻¹ρσ)`
      have : Equiv.Perm.sign (σ⁻¹ * (ρ : Equiv.Perm (Fin (Specht.nOf μ))) * σ)
          = Equiv.Perm.sign (ρ : Equiv.Perm (Fin (Specht.nOf μ))) := by
        rw [map_mul, map_mul, map_inv, mul_right_comm, inv_mul_cancel, one_mul]
      rw [this]
    · -- tabloid: `ρ • σ • t = σ • (σ⁻¹ρσ) • t`
      show Specht.Mtab.of (k := k) ((ρ : Equiv.Perm (Fin (Specht.nOf μ))) • σ • t)
        = Specht.Mtab.of (k := k)
            (σ • (σ⁻¹ * (ρ : Equiv.Perm (Fin (Specht.nOf μ))) * σ) • t)
      congr 1
      rw [← mul_smul, ← mul_smul, ← mul_assoc, ← mul_assoc, mul_inv_cancel,
        one_mul, mul_smul]

omit [CharZero k] in
/-- **Polytabloid is a sign-eigenvector of its column stabiliser (sorry-free).**
For `σ ∈ C_t`, the representation acts on `e_t` by the sign character:
`σ · e_t = sgn(σ) · e_t`. Immediate from equivariance
(`polytabloid_rep_smul`: `e_{σ·t} = σ · e_t`) composed with column-antisymmetry
(`polytabloid_colStab_smul`: `e_{σ·t} = sgn(σ) · e_t` for `σ ∈ C_t`). This is the
eigenvector property the Garnir antisymmetriser bridge consumes. -/
theorem rep_polytabloid_of_mem_colStab (t : Specht.Tableau μ)
    {σ : Equiv.Perm (Fin (Specht.nOf μ))} (hσ : σ ∈ Specht.colStab t) :
    Specht.Mtab.rep μ σ (Specht.polytabloid (k := k) t)
      = (Equiv.Perm.sign σ : ℤ) • Specht.polytabloid (k := k) t := by
  rw [← polytabloid_rep_smul, polytabloid_colStab_smul t hσ]

omit [CharZero k] in
/-- **Antisymmetriser eigenvalue (sorry-free).** Summing the signed group action
over any finite set `H` of column-stabiliser elements collapses to `|H| · e_t`:
`∑_{ρ∈H} sgn(ρ) · (ρ · e_t) = |H| · e_t`, because each term is
`sgn(ρ)·sgn(ρ)·e_t = e_t` by the sign-eigenvector property (`sgn(ρ)² = 1`). This
is the `α · e_t = |S_A×S_B| · e_t` step of the Garnir coset→polytabloid bridge
(here for an arbitrary `H ⊆ C_t`, of which `S_A×S_B` is the relevant instance). -/
theorem sum_sign_rep_polytabloid (t : Specht.Tableau μ)
    (H : Finset (Equiv.Perm (Fin (Specht.nOf μ))))
    (hH : ∀ ρ ∈ H, ρ ∈ Specht.colStab t) :
    ∑ ρ ∈ H, (Equiv.Perm.sign ρ : ℤ) •
        Specht.Mtab.rep μ ρ (Specht.polytabloid (k := k) t)
      = H.card • Specht.polytabloid (k := k) t := by
  classical
  have hterm : ∀ ρ ∈ H, (Equiv.Perm.sign ρ : ℤ) •
      Specht.Mtab.rep μ ρ (Specht.polytabloid (k := k) t)
        = Specht.polytabloid (k := k) t := by
    intro ρ hρ
    rw [rep_polytabloid_of_mem_colStab t (hH ρ hρ), smul_smul]
    have hs2 : (Equiv.Perm.sign ρ : ℤ) * (Equiv.Perm.sign ρ : ℤ) = 1 := by
      rcases Int.units_eq_one_or (Equiv.Perm.sign ρ) with h | h <;> rw [h] <;> decide
    rw [hs2, one_smul]
  rw [Finset.sum_congr rfl hterm, Finset.sum_const]

omit [CharZero k] in
/-- **Polytabloid-level Garnir annihilation (sorry-free).** The `rep`-level analog
of `mtab_sum_sign_smul_of_eq_zero`: if a `sign(-1)` involution `τ` *fixes the
polytabloid* (`τ · e_t = e_t`) and `G` is right-`τ`-closed, the signed group-action
sum vanishes, `∑_{g∈G} sgn(g) · (g · e_t) = 0`. Same sign-reversing-involution
pairing `g ↔ gτ`: `rep(gτ)(e_t) = rep(g)(rep(τ)(e_t)) = rep(g)(e_t)` while
`sgn(gτ) = -sgn(g)`. Once a row descent supplies such a `τ` (fixing `e_t` because
it lies in a row after the Garnir swap), this is the Garnir relation
`g_{A,B} · e_t = 0` at the polytabloid level. -/
theorem sum_sign_rep_eq_zero_of_fixed (t : Specht.Tableau μ)
    (G : Finset (Equiv.Perm (Fin (Specht.nOf μ))))
    (τ : Equiv.Perm (Fin (Specht.nOf μ)))
    (hτ2 : τ * τ = 1) (hτsign : Equiv.Perm.sign τ = -1)
    (hτfix : Specht.Mtab.rep μ τ (Specht.polytabloid (k := k) t)
      = Specht.polytabloid (k := k) t)
    (hGclosed : ∀ g ∈ G, g * τ ∈ G) :
    ∑ g ∈ G, (Equiv.Perm.sign g : ℤ) •
        Specht.Mtab.rep μ g (Specht.polytabloid (k := k) t) = 0 := by
  classical
  have hfix : ∀ g : Equiv.Perm (Fin (Specht.nOf μ)),
      Specht.Mtab.rep μ (g * τ) (Specht.polytabloid (k := k) t)
        = Specht.Mtab.rep μ g (Specht.polytabloid (k := k) t) := by
    intro g
    rw [map_mul]
    exact congrArg (Specht.Mtab.rep μ g) hτfix
  have hs : ∀ g : Equiv.Perm (Fin (Specht.nOf μ)),
      (Equiv.Perm.sign (g * τ) : ℤ) = -(Equiv.Perm.sign g : ℤ) := by
    intro g; rw [map_mul, hτsign]; simp
  refine Finset.sum_involution (fun g _ => g * τ) ?_ ?_ ?_ ?_
  · intro g _
    rw [hfix g, hs g, neg_smul]; abel
  · intro g _ _ hgg
    have hτ1 : τ = 1 := by
      have hg1 : g * τ = g * 1 := by rw [mul_one]; exact hgg
      exact mul_left_cancel hg1
    rw [hτ1, map_one] at hτsign; exact absurd hτsign (by decide)
  · intro g hg; exact hGclosed g hg
  · intro g _; show (g * τ) * τ = g; rw [mul_assoc, hτ2, mul_one]

/-! #### The self-contained dominance weight (sorry-free)

The straightening induction needs a well-founded measure that strictly increases
under a Garnir step. Because this file sits **below** `SpechtDominanceCore` in the
import graph, we cannot reuse that module's `domRel`; instead we define, locally
and self-containedly, a strictly-monotone ℕ-valued *linear extension* of the
dominance order — the total of all clamped dominance counts `domCount' f i m`
(`= #{l : (l:ℕ) < m ∧ f l ≤ i}`, "how many of the `m` smallest labels lie in rows
`≤ i`"), summed over `i, m ∈ [0, n]`. A tabloid strictly dominating another has
this total strictly larger, so it is a valid well-founded measure. All ℕ-valued
(§7c-clean: no `ℝ`, no ordering on `q`). -/

/-- The **dominance count** of a row pattern `f` (self-contained, local to this
file): `domCount' f i m = #{l : (l:ℕ) < m ∧ f l ≤ i}`. -/
def domCount' (f : Fin (Specht.nOf μ) → ℕ) (i m : ℕ) : ℕ :=
  (Finset.univ.filter (fun l : Fin (Specht.nOf μ) => (l : ℕ) < m ∧ f l ≤ i)).card

/-- The **dominance weight** of a tableau: the total of all clamped dominance
counts of its row pattern. A strictly-monotone linear extension of the dominance
order (a Garnir straightening step strictly increases it), hence a valid
well-founded measure for the straightening induction. -/
def domWeight (t : Specht.Tableau μ) : ℕ :=
  ∑ i ∈ Finset.range (Specht.nOf μ + 1), ∑ m ∈ Finset.range (Specht.nOf μ + 1),
    domCount' (Specht.rowPattern t) i m

/-- A fixed ceiling for `domWeight` (used to run the strong induction on the
decreasing measure `domBound μ - domWeight t`). -/
def domBound (μ : YoungDiagram) : ℕ :=
  (Specht.nOf μ + 1) * ((Specht.nOf μ + 1) * Specht.nOf μ)

/-- Each dominance count is bounded by `n = nOf μ` (a filtered subset of the
`n`-element label set). -/
theorem domCount'_le (f : Fin (Specht.nOf μ) → ℕ) (i m : ℕ) :
    domCount' (μ := μ) f i m ≤ Specht.nOf μ := by
  unfold domCount'
  refine le_trans (Finset.card_filter_le _ _) ?_
  rw [Finset.card_univ, Fintype.card_fin]

/-- `domWeight t ≤ domBound μ` (sum of `(n+1)²` counts, each `≤ n`). -/
theorem domWeight_le (t : Specht.Tableau μ) : domWeight t ≤ domBound μ := by
  unfold domWeight domBound
  calc ∑ i ∈ Finset.range (Specht.nOf μ + 1), ∑ m ∈ Finset.range (Specht.nOf μ + 1),
          domCount' (Specht.rowPattern t) i m
      ≤ ∑ _i ∈ Finset.range (Specht.nOf μ + 1), ∑ _m ∈ Finset.range (Specht.nOf μ + 1),
          Specht.nOf μ := by
        refine Finset.sum_le_sum (fun i _ => ?_)
        refine Finset.sum_le_sum (fun m _ => ?_)
        exact domCount'_le _ i m
    _ = (Specht.nOf μ + 1) * ((Specht.nOf μ + 1) * Specht.nOf μ) := by
        simp [Finset.sum_const, Finset.card_range, Nat.mul_comm, Nat.mul_left_comm]

/-! #### The single residual straightening core + the induction skeleton -/

omit [CharZero k] in
/-- **STUB — the residual straightening core, SHARPENED to the column-maximal case
(Sagan §2.6 Garnir relations).**
A polytabloid `e_t` that is *not itself* a standard polytabloid **and** whose tableau
`t` is already **column-(dominance-)maximal** — no column permutation `σ ∈ C_t`
strictly raises the dominance measure `domWeight` (hypothesis `hmax`) — is a
`k`-linear combination of polytabloids of **strictly `domWeight`-greater** tabloids.

This is the *irreducible* combinatorial heart of the straightening algorithm with the
**column-sort already exhausted**: because `hmax` says no column permutation can raise
`domWeight` further, the column-antisymmetry lever `polytabloid_colStab_smul` (proved
above) is spent, and closing this requires a genuine **Garnir coset-sum identity at a
row descent** (Sagan §2.6), whose non-identity coset terms are `±e_{π•t}` with
`domWeight (π•t) > domWeight t`. The general `straightening_step` (below) reduces to
this case sorry-free by splitting on whether a `domWeight`-raising column permutation
exists.

`hmax` is a genuine restriction (a column-maximal `t` is column-standard up to the
row order), so this is an honest sub-case, cited but not vacuous: for a column-maximal
non-standard `t` a row descent between adjacent columns exists and the Garnir relation
yields strictly dominance-greater — hence strictly `domWeight`-greater — terms. -/
theorem straightening_step_colMax (t : Specht.Tableau μ)
    (h : Specht.polytabloid (k := k) t ∉ Set.range (standardPolytabloid (k := k) (μ := μ)))
    (hmax : ∀ σ : Specht.colStab t,
      domWeight ((σ : Equiv.Perm (Fin (Specht.nOf μ))) • t) ≤ domWeight t) :
    ∃ (s : Finset (Specht.Tableau μ)) (c : Specht.Tableau μ → k),
      (∀ t' ∈ s, domWeight t < domWeight t') ∧
      Specht.polytabloid (k := k) t = ∑ t' ∈ s, c t' • Specht.polytabloid (k := k) t' := by
  -- Ref: [sagan2001] §2.6 (Garnir relations / straightening algorithm). See also
  -- [james1984representation] §8. With the column-sort exhausted (`hmax`: `t` is
  -- column-dominance-maximal), the residual is a pure Garnir coset-sum identity at a
  -- row descent, whose non-identity terms are polytabloids of strictly
  -- dominance-greater (hence `domWeight`-greater) tabloids.
  sorry

omit [CharZero k] in
/-- **Straightening step (Sagan §2.6) — reduced sorry-free to the column-maximal core.**
A polytabloid `e_t` that is *not itself* a standard polytabloid is a `k`-linear
combination of polytabloids of **strictly dominance-greater** tabloids (encoded by the
strictly-monotone measure `domWeight`). From this core, the full spanning half
(`standardPolytabloid_straightening`) follows sorry-free by well-founded induction on
`domBound μ - domWeight t`.

**Reduction (sorry-free half).** Split on whether some column permutation `σ ∈ C_t`
strictly raises `domWeight`:

* **Column-raising** (`∃ σ ∈ C_t, domWeight t < domWeight (σ•t)`) — handled here
  outright by the column-antisymmetry lever `polytabloid_colStab_smul`: since
  `e_{σ•t} = sgn(σ)·e_t` and `sgn(σ)² = 1`, we get `e_t = sgn(σ)·e_{σ•t}`, a
  one-term combination over `{σ•t}`, and `domWeight t < domWeight (σ•t)` is exactly
  the branch hypothesis. No dominance theory needed.
* **Column-maximal** (no such `σ`) — delegated to `straightening_step_colMax`, the
  single sharpened Garnir residual, which now carries the extra hypothesis `hmax`
  that no column permutation raises `domWeight`. -/
theorem straightening_step (t : Specht.Tableau μ)
    (h : Specht.polytabloid (k := k) t ∉ Set.range (standardPolytabloid (k := k) (μ := μ))) :
    ∃ (s : Finset (Specht.Tableau μ)) (c : Specht.Tableau μ → k),
      (∀ t' ∈ s, domWeight t < domWeight t') ∧
      Specht.polytabloid (k := k) t = ∑ t' ∈ s, c t' • Specht.polytabloid (k := k) t' := by
  classical
  by_cases hraise : ∃ σ : Specht.colStab t,
      domWeight t < domWeight ((σ : Equiv.Perm (Fin (Specht.nOf μ))) • t)
  · -- Column-raising case: fully proved via column-antisymmetry.
    obtain ⟨σ, hσ⟩ := hraise
    set σ0 : Equiv.Perm (Fin (Specht.nOf μ)) := (σ : Equiv.Perm (Fin (Specht.nOf μ))) with hσ0
    have hmem : σ0 ∈ Specht.colStab t := σ.property
    have hpc : Specht.polytabloid (k := k) (σ0 • t)
        = (Equiv.Perm.sign σ0 : ℤ) • Specht.polytabloid (k := k) t :=
      polytabloid_colStab_smul (k := k) t hmem
    have hs2 : (Equiv.Perm.sign σ0 : ℤ) * (Equiv.Perm.sign σ0 : ℤ) = 1 := by
      rcases Int.units_eq_one_or (Equiv.Perm.sign σ0) with h1 | h1 <;> rw [h1] <;> decide
    refine ⟨{σ0 • t}, fun _ => ((Equiv.Perm.sign σ0 : ℤ) : k), ?_, ?_⟩
    · intro t' ht'
      rw [Finset.mem_singleton] at ht'; subst ht'; exact hσ
    · rw [Finset.sum_singleton, hpc,
          ← Int.cast_smul_eq_zsmul k (Equiv.Perm.sign σ0 : ℤ) (Specht.polytabloid (k := k) t),
          smul_smul, ← Int.cast_mul, hs2, Int.cast_one, one_smul]
  · -- Column-maximal case: delegated to the sharpened Garnir residual.
    push_neg at hraise
    exact straightening_step_colMax (k := k) t h hraise

omit [CharZero k] in
/-- **Spanning half — now proved sorry-free MODULO the single core
`straightening_step`.** Every polytabloid `e_t` (arbitrary tableau `t`) lies in the
span of the *standard* polytabloids, by well-founded (strong) induction on the
measure `domBound μ - domWeight t`: if `e_t` is already a standard polytabloid it is
in the spanning set; otherwise `straightening_step` rewrites it over tabloids of
strictly greater `domWeight` (strictly smaller measure), each in the span by the
induction hypothesis, and the span is closed under `k`-linear combinations. -/
theorem standardPolytabloid_straightening :
    ∀ t : Specht.Tableau μ,
      Specht.polytabloid (k := k) t ∈
        Submodule.span k (Set.range (standardPolytabloid (k := k) (μ := μ))) := by
  intro t
  generalize hg : domBound μ - domWeight t = g
  induction g using Nat.strong_induction_on generalizing t with
  | _ g IH =>
    by_cases hr : Specht.polytabloid (k := k) t ∈
        Set.range (standardPolytabloid (k := k) (μ := μ))
    · exact Submodule.subset_span hr
    · obtain ⟨s, c, hgt, heq⟩ := straightening_step (k := k) t hr
      rw [heq]
      refine Submodule.sum_mem _ (fun t' ht' => ?_)
      refine Submodule.smul_mem _ _ ?_
      have hlt : domWeight t < domWeight t' := hgt t' ht'
      have hb : domWeight t' ≤ domBound μ := domWeight_le t'
      exact IH (domBound μ - domWeight t') (by omega) t' rfl

omit [CharZero k] in
/-- **M^μ-level span identity.** The standard polytabloids span exactly `S^μ`
inside `M^μ`. (≤): each standard polytabloid is a polytabloid (`standardPolytabloid_mem`);
(≥): the straightening core. Sorry-free modulo `standardPolytabloid_straightening`. -/
theorem standardPolytabloid_span_eq_specht :
    Submodule.span k (Set.range (standardPolytabloid (k := k) (μ := μ)))
      = Specht.SpechtSubmodule (k := k) μ := by
  apply le_antisymm
  · rw [Submodule.span_le]
    rintro _ ⟨T, rfl⟩
    exact standardPolytabloid_mem (k := k) T
  · rw [Specht.SpechtSubmodule, Submodule.span_le, Set.range_subset_iff]
    exact standardPolytabloid_straightening (k := k) (μ := μ)

omit [CharZero k] in
/-- **Content obligation 2/2 — spanning**, now derived **sorry-free modulo the single
core** `standardPolytabloid_straightening` (the M^μ span identity + the corestriction
to `⊤` in `S^μ` are discharged here). Keeps the original name/signature for `Basis.mk`. -/
theorem standardPolytabloid_span :
    Submodule.span k (Set.range (standardPolytabloidS (k := k) (μ := μ))) = ⊤ := by
  apply Submodule.map_injective_of_injective
    (Submodule.injective_subtype (Specht.SpechtSubmodule (k := k) μ))
  rw [Submodule.map_subtype_top, Submodule.map_span, ← Set.range_comp,
      subtype_comp_standardPolytabloidS]
  exact standardPolytabloid_span_eq_specht (k := k) (μ := μ)

end QOU.BraidKnot.SpechtStandardBasis

import QOU.Mathlib.PagedSpectralSequence
import Mathlib.LinearAlgebra.Quotient.Basic
import Mathlib.LinearAlgebra.FiniteDimensional.Defs
import Mathlib.Tactic

/-!
# QOU.Mathlib.EulerCharacteristic — why `Δ_λ` is proved and its magnitude is not

Bean `qou-fngs`, LES/spectral arc. `PagedSpectralSequence.lean` made collapse
mean something. This file proves the one thing a spectral sequence gives you
*without* collapse, and thereby explains a standing asymmetry in the corpus.

## The asymmetry

`Δ_λ = (−1)^{n(λ)} · dim V_λ` is settled, while the magnitude it is built from
— the `r* ≈ 1.585` scaling of `dim V_λ` itself — is open. That is not an
accident of effort. It is the difference between an Euler characteristic and a
graded piece, and this file is that difference stated as two theorems about the
same object:

* `eulerChar_bump_eq` — the **alternating sum** of page ranks over a window is
  unchanged by page-turning. No collapse hypothesis, no filtration analysis;
  the correction terms cancel against each other.
* `finrank_bump_eq_iff` — an **individual** page rank is unchanged exactly when
  the differentials into and out of that cell both vanish.

So an index of `Δ_λ`'s shape is page-independent for free, and can therefore be
computed on whichever page is accessible; a single `dim V_λ` is page-independent
only under a vanishing statement nobody has, which is precisely the missing
collapse. `Δ_λ` being available while `dim V_λ` is not is the expected
situation, not a gap in the argument for `Δ_λ`.

## The mechanism

Total degree `p + q` grades each page, and `d_r : E_r^{p,q} → E_r^{p+r,q-r+1}`
raises it by exactly one (`deg_next`) — so every page is a cochain complex in
this grading and page-turning is passage to cohomology. Rank–nullity plus
quotient additivity give the local accounting (`finrank_bump_add`):

    rk E_{r+1}^c + rk (im d_c) + rk (im d_{prev c}) = rk E_r^c

The two correction terms sit in adjacent total degrees, so under the sign
`(−1)^{p+q}` they enter with opposite signs. Reindexing the second along the
bijection `prev` (`sum_sgn_imRank_prev`) turns it into minus the first, and they
cancel. That cancellation is the whole of Euler–Poincaré.

## Why a field, and why that is not a §7c violation

Ranks are `Module.finrank` over a field `K` with finite-dimensional pages.
That is a genuine restriction — `R_q = ℤ[q, q⁻¹]` is not a field and its
modules have no such dimension — and it is deliberate rather than sloppy: the
statement being explained, `Δ_λ = (−1)^{n(λ)} dim V_λ`, is a dimension of a
representation, so a field is where it lives. `K` is an arbitrary field, not
`ℝ`, so nothing archimedean is smuggled in.

## What this does not do

It does not iterate to `E_∞`. Iterating needs the support hypothesis at every
page, which is the boundedness condition of a convergent spectral sequence;
supplying that for the Gröbner filtration is the same missing work
`BarGradedCollapse` leaves open. One step is proved here, and one step is what
the asymmetry above needs.

-- Ref: [leitner2026] quantum-observable-universe/eightfold-way
-/

namespace QOU.Mathlib.EulerCharacteristic

open QOU.Mathlib.SpectralSequence QOU.Mathlib.PagedSpectralSequence

universe u v

/-! ### Total degree, its sign, and the `prev`/`next` bijection -/

/-- Total degree `p + q`. `CellIndex`'s own docstring names `q` the
    "total-complement degree" for exactly this sum. -/
def CellIndex.deg (c : CellIndex) : ℤ := c.p + c.q

/-- **The differential raises total degree by one.** This is what makes each
    page a cochain complex in the total grading, and it is the reason the two
    correction terms below carry opposite signs. -/
@[simp] theorem deg_next (c : CellIndex) :
    CellIndex.deg (CellIndex.next c) = CellIndex.deg c + 1 := by
  simp only [CellIndex.deg, CellIndex.next]
  ring

@[simp] theorem deg_prev (c : CellIndex) :
    CellIndex.deg (CellIndex.prev c) = CellIndex.deg c - 1 := by
  simp only [CellIndex.deg, CellIndex.prev]
  ring

/-- Page-turning keeps the bidegree, hence the total degree and its sign. -/
@[simp] theorem deg_bump (c : CellIndex) :
    CellIndex.deg (CellIndex.bump c) = CellIndex.deg c := rfl

/-- `prev` inverts `next` on the other side. `PagedSpectralSequence` has
    `next_prev`; this is what makes `prev` **injective**, which is what the sum
    reindexing needs. -/
theorem prev_next (c : CellIndex) : CellIndex.prev (CellIndex.next c) = c := by
  obtain ⟨r, p, q⟩ := c
  have h1 : p + (r : ℤ) - (r : ℤ) = p := by ring
  have h2 : q - (r : ℤ) + 1 + (r : ℤ) - 1 = q := by ring
  simp [CellIndex.next, CellIndex.prev, h1, h2]

theorem prev_injective : Function.Injective CellIndex.prev :=
  Function.LeftInverse.injective next_prev

instance : DecidableEq CellIndex := fun a b => by
  obtain ⟨r₁, p₁, q₁⟩ := a
  obtain ⟨r₂, p₂, q₂⟩ := b
  simp only [CellIndex.mk.injEq]
  infer_instance

/-- `(−1)^{p+q}`, the total-degree sign. -/
def sgn (c : CellIndex) : ℤ := ((Int.negOnePow (CellIndex.deg c) : ℤˣ) : ℤ)

/-- The sign flips along the differential — the source of the cancellation. -/
theorem sgn_next (c : CellIndex) : sgn (CellIndex.next c) = -sgn c := by
  simp [sgn, Int.negOnePow_succ]

@[simp] theorem sgn_bump (c : CellIndex) : sgn (CellIndex.bump c) = sgn c := by
  simp [sgn]

/-! ### The incoming differential really does land in the kernel -/

variable {R : Type u} [CommRing R] {page : CellIndex → Type v}
    [∀ c, AddCommGroup (page c)] [∀ c, Module R (page c)]

@[simp] theorem reindex_rfl {c : CellIndex} :
    reindex (R := R) (page := page) (rfl : c = c) = LinearEquiv.refl R (page c) := rfl

/-- **`d ∘ d = 0`, transported.** `PagedSS.d_comp_d` is stated at
    `next (prev c)`, which is `c` only propositionally, so the fact that the
    incoming image lies in `ker d_c` needs the transport spelt out. Stating it
    with the equation `h` as a hypothesis lets `subst` do the work. -/
theorem range_transport_le_ker {b c : CellIndex} (h : CellIndex.next b = c)
    (S : PagedSS R page) :
    LinearMap.range ((reindex (R := R) (page := page) h).toLinearMap.comp (S.d b))
      ≤ LinearMap.ker (S.d c) := by
  subst h
  intro y hy
  obtain ⟨x, rfl⟩ := hy
  simpa using LinearMap.congr_fun (S.d_comp_d b) x

/-! ### Ranks

    Dimensions need a field; see the module docstring on why that is the right
    home for a statement about `dim V_λ`. -/

variable {K : Type u} [Field K] {pageK : CellIndex → Type v}
    [∀ c, AddCommGroup (pageK c)] [∀ c, Module K (pageK c)]
    [∀ c, FiniteDimensional K (pageK c)]

/-- Rank of the image of the differential **out of** `c`. The two corrections in
    `finrank_bump_add` are both of this form, at adjacent cells. -/
noncomputable def imRank (S : PagedSS K pageK) (c : CellIndex) : ℕ :=
  Module.finrank K (LinearMap.range (S.d c))

/-- The incoming subobject has the rank of the incoming image: the `comap` along
    `(ker d_c).subtype` is an isomorphism onto it because `d ∘ d = 0` puts that
    image inside the kernel, and `reindex` is an isomorphism. -/
theorem finrank_incoming (S : PagedSS K pageK) (c : CellIndex) :
    Module.finrank K (incoming S.d c) = imRank S (CellIndex.prev c) := by
  have hle := range_transport_le_ker (next_prev c) S
  have h1 : Module.finrank K (incoming S.d c)
      = Module.finrank K
          (LinearMap.range
            ((reindex (R := K) (page := pageK) (next_prev c)).toLinearMap.comp
              (S.d (CellIndex.prev c)))) :=
    (Submodule.comapSubtypeEquivOfLe hle).finrank_eq
  rw [h1, LinearMap.range_comp]
  exact (Submodule.equivMapOfInjective _
    (reindex (R := K) (page := pageK) (next_prev c)).injective _).symm.finrank_eq

/-- **The local rank identity.**

    Turning the page costs exactly the two differentials adjacent to the cell:
    the one out of it (whose kernel it passes to) and the one into it (whose
    image it quotients by).

    Stated additively because `ℕ` subtraction is a trap. -/
theorem finrank_bump_add (S : PagedSS K pageK) (c : CellIndex) :
    Module.finrank K (pageK (CellIndex.bump c)) + imRank S c
        + imRank S (CellIndex.prev c)
      = Module.finrank K (pageK c) := by
  have h1 : Module.finrank K (pageK (CellIndex.bump c))
      = Module.finrank K ((LinearMap.ker (S.d c)) ⧸ incoming S.d c) :=
    (S.turn c).finrank_eq
  have h2 : Module.finrank K ((LinearMap.ker (S.d c)) ⧸ incoming S.d c)
        + Module.finrank K (incoming S.d c)
      = Module.finrank K (LinearMap.ker (S.d c)) :=
    Submodule.finrank_quotient_add_finrank _
  have h3 : Module.finrank K (incoming S.d c) = imRank S (CellIndex.prev c) :=
    finrank_incoming S c
  have h4 : Module.finrank K (LinearMap.range (S.d c))
        + Module.finrank K (LinearMap.ker (S.d c))
      = Module.finrank K (pageK c) :=
    LinearMap.finrank_range_add_finrank_ker _
  have h5 : imRank S c = Module.finrank K (LinearMap.range (S.d c)) := rfl
  omega

/-- **An individual page rank is page-independent exactly under vanishing.**

    Half of the asymmetry this file exists to state: `dim E_r^c` survives
    page-turning only when both adjacent differentials die at `c`. That is a
    collapse statement, and it is what the corpus does not have for the Gröbner
    filtration — hence no `dim V_λ`. Contrast `eulerChar_bump_eq`. -/
theorem finrank_bump_eq_iff (S : PagedSS K pageK) (c : CellIndex) :
    Module.finrank K (pageK (CellIndex.bump c)) = Module.finrank K (pageK c)
      ↔ imRank S c = 0 ∧ imRank S (CellIndex.prev c) = 0 := by
  have := finrank_bump_add S c
  omega

/-- Consistency with `PagedSpectralSequence`: collapse gives an isomorphism, and
    an isomorphism gives equal ranks — the forward direction of
    `finrank_bump_eq_iff` reached the other way. -/
theorem finrank_bump_of_collapse (S : PagedSS K pageK) (r₀ : ℕ)
    (hcol : Collapses S r₀) (c : CellIndex) (hc : r₀ ≤ c.r) :
    Module.finrank K (pageK (CellIndex.bump c)) = Module.finrank K (pageK c) :=
  (page_stabilises_of_collapse S r₀ hcol c hc).some.finrank_eq

/-! ### The Euler characteristic -/

/-- Signed rank sum over a finite window of cells. -/
noncomputable def eulerChar (s : Finset CellIndex) (f : CellIndex → ℕ) : ℤ :=
  ∑ c ∈ s, sgn c * (f c : ℤ)

/-- **The cancellation.** Reindexed along `prev`, the incoming corrections are
    exactly minus the outgoing ones.

    `hsupp` is the finite-window hypothesis: every cell carrying a nonzero
    differential image lies in the window together with its target. Some such
    hypothesis is unavoidable — without it the sums are over infinitely many
    cells — and this is the weakest form that makes the reindexing legitimate. -/
theorem sum_sgn_imRank_prev (S : PagedSS K pageK) (s : Finset CellIndex)
    (hsupp : ∀ c, imRank S c ≠ 0 → c ∈ s ∧ CellIndex.next c ∈ s) :
    ∑ c ∈ s, sgn c * (imRank S (CellIndex.prev c) : ℤ)
      = -∑ c ∈ s, sgn c * (imRank S c : ℤ) := by
  classical
  set t : Finset CellIndex := s ∪ s.image CellIndex.prev with ht
  -- reindex the incoming sum onto the shifted window
  have ha : ∑ b ∈ s.image CellIndex.prev, sgn (CellIndex.next b) * (imRank S b : ℤ)
      = ∑ c ∈ s, sgn c * (imRank S (CellIndex.prev c) : ℤ) := by
    rw [Finset.sum_image prev_injective.injOn]
    refine Finset.sum_congr rfl fun c _ => ?_
    rw [next_prev]
  -- the shifted window and the original agree, because both extend to `t`
  have hsub₁ : s.image CellIndex.prev ⊆ t := Finset.subset_union_right
  have hsub₂ : s ⊆ t := Finset.subset_union_left
  have hb : ∑ b ∈ s.image CellIndex.prev, sgn b * (imRank S b : ℤ)
      = ∑ b ∈ t, sgn b * (imRank S b : ℤ) := by
    refine Finset.sum_subset hsub₁ fun b _ hbn => ?_
    have : imRank S b = 0 := by
      by_contra hne
      obtain ⟨_, hnext⟩ := hsupp b hne
      exact hbn (Finset.mem_image.2 ⟨CellIndex.next b, hnext, prev_next b⟩)
    simp [this]
  have hc : ∑ c ∈ s, sgn c * (imRank S c : ℤ) = ∑ c ∈ t, sgn c * (imRank S c : ℤ) := by
    refine Finset.sum_subset hsub₂ fun c _ hcn => ?_
    have : imRank S c = 0 := by
      by_contra hne
      exact hcn (hsupp c hne).1
    simp [this]
  calc ∑ c ∈ s, sgn c * (imRank S (CellIndex.prev c) : ℤ)
      = ∑ b ∈ s.image CellIndex.prev, sgn (CellIndex.next b) * (imRank S b : ℤ) := ha.symm
    _ = ∑ b ∈ s.image CellIndex.prev, -(sgn b * (imRank S b : ℤ)) := by
        refine Finset.sum_congr rfl fun b _ => ?_
        rw [sgn_next]; ring
    _ = -∑ b ∈ s.image CellIndex.prev, sgn b * (imRank S b : ℤ) := by
        rw [Finset.sum_neg_distrib]
    _ = -∑ c ∈ s, sgn c * (imRank S c : ℤ) := by rw [hb, hc]

/-- **Euler characteristic is page-independent.**

    The alternating sum of page ranks over a window is unchanged by turning the
    page — with **no collapse hypothesis**. The window hypothesis `hsupp` is
    about where the differential is nonzero, not about it vanishing.

    This is the other half of the asymmetry. An index of the shape
    `Δ_λ = (−1)^{n(λ)} dim V_λ` is a term of such a sum, so it can be evaluated
    on whichever page is accessible; the individual `dim V_λ` cannot
    (`finrank_bump_eq_iff`). -/
theorem eulerChar_bump_eq (S : PagedSS K pageK) (s : Finset CellIndex)
    (hsupp : ∀ c, imRank S c ≠ 0 → c ∈ s ∧ CellIndex.next c ∈ s) :
    eulerChar s (fun c => Module.finrank K (pageK (CellIndex.bump c)))
      = eulerChar s (fun c => Module.finrank K (pageK c)) := by
  have key : ∀ c : CellIndex,
      sgn c * (Module.finrank K (pageK (CellIndex.bump c)) : ℤ)
        = sgn c * (Module.finrank K (pageK c) : ℤ)
          - sgn c * (imRank S c : ℤ) - sgn c * (imRank S (CellIndex.prev c) : ℤ) := by
    intro c
    have h := finrank_bump_add S c
    have : (Module.finrank K (pageK (CellIndex.bump c)) : ℤ)
        = (Module.finrank K (pageK c) : ℤ) - (imRank S c : ℤ)
          - (imRank S (CellIndex.prev c) : ℤ) := by omega
    rw [this]; ring
  simp only [eulerChar, key, Finset.sum_sub_distrib]
  rw [sum_sgn_imRank_prev S s hsupp]
  ring

end QOU.Mathlib.EulerCharacteristic

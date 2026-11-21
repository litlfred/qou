import QOU.Mathlib.SpectralCollapseCriteria

/-!
# QOU.Mathlib.ConcentratedColumnCollapse — the collapse the mass formula actually uses

Bean `qou-fngs`.  `QOU/Mathlib/SpectralCollapseCriteria.lean` proves that bounded
support forces collapse, and `legacyOfPaged` turns a collapsing `PagedSS` into the
`[GBFiltrationCollapsesAtE2 R]` hypothesis downstream theorems take.  **Neither had
ever been applied**: measured on `origin/main`, every occurrence of `PagedSS` in the
corpus is a *hypothesis* `S : PagedSS …` and not one declaration constructs one, so
the only discharge of `GBFiltrationCollapsesAtE2` remained `canonicalTrivial`, whose
witness is `PUnit`.

This module supplies the missing side: the page family the corpus's own mass-formula
proof describes, and the discharge that follows from it.

## What `conj:phi-q-categorical-truncation` asks for

Step 1 of that proof (`mass-theory/phi-q-categorical-truncation-proof.md`) reads

```
E_∞^{p,*} = Z(A) = ⊕_{λ ⊢ n} R · e_λ   for p = 0,
            0                            for p ≥ 1.
```

That is **concentration in the `p = 0` column**, and it is a statement about the
filtration degree `p`, not about the page index `r`.  So it is exactly the `N = 0`
case of `collapses_of_bounded_support`, and `collapses_two_of_bounded_support`
already covers `N ≤ 1`.  The E₂ collapse the mass formula needs is therefore
**derivable from the concentration hypothesis it already states**, for *any*
differential the family admits.

## The `k` in `k⋆` is a different filtration, and this is worth stating plainly

The bean records the conclusion *"the mass formula needs the specific `k⋆`, so it
needs E₂, not merely 'some page'"*, with `E₂` said to be *"what fixes `k⋆` to be the
max GB-depth rather than something larger"*.  That reads the two indices as one, and
they are not:

* `p` is the **Hochschild / filtration degree** — the column index of the spectral
  sequence, and the index `CellIndex.p` carries here.  Collapse is a statement about
  differentials between columns.
* `k` is the **GB-depth of a partition**, which Step 3 uses to stratify
  `Z(A) = ⊕_{k = 0}^{k⋆} Z^{(k)}(A)`.  That is a decomposition *inside* the single
  surviving column `E_∞^{0,*}`; it indexes no page and no column.

`k⋆` is finite for the reason Step 3 gives — `k⋆ := max_{λ ∈ supp(T_w)} depth_GB(λ)`
is a maximum over a finite support — and the spectral sequence plays no part in
fixing it.  So collapse at E₂ neither implies nor is implied by the value of `k⋆`;
what collapse buys the proof is Step 1's `E_∞^{p,*} = 0` for `p ≥ 1`, and nothing
more.  Keeping the two apart is what makes the E₂ claim reachable at all: as a
statement about `p` it is the `N = 0` window, which is provable.

## What is still assumed, and it is the whole of it

The **concentration** itself.  Nothing here shows that the Gröbner-filtration
spectral sequence of `H_n(R, q)` is concentrated in the `p = 0` column; that is the
content of `S-GB-spectral-collapse` and it remains an assertion.  What is no longer
assumed is the step *from* concentration *to* collapse, and the discharge below
takes the real page family rather than `PUnit`.

-- Ref: [leitner2026] quantum-observable-universe/mass-theory
-/

namespace QOU.Mathlib.ConcentratedColumnCollapse

open QOU.Mathlib.SpectralSequence
open QOU.Mathlib.PagedSpectralSequence
open QOU.Mathlib.SpectralCollapseCriteria

universe u

variable (R : Type u) [CommRing R] (M : Type u) [AddCommGroup M] [Module R M]

/-- **Pages concentrated in the `p = 0` column**: the module `M` there, the zero
module everywhere else.

Carried as a `Submodule`-valued family rather than an `if … then M else PUnit`, so
that the `AddCommGroup` and `Module R` instances are the *uniform* submodule ones.
The `if` version needs an instance defined by case split, and the two splits then
have to agree definitionally for every lemma that mentions both. -/
def ConcentratedPage (c : CellIndex) : Type u :=
  ((if c.p = 0 then (⊤ : Submodule R M) else ⊥) : Submodule R M)

instance instAddCommGroupConcentratedPage (c : CellIndex) :
    AddCommGroup (ConcentratedPage R M c) :=
  inferInstanceAs (AddCommGroup ((if c.p = 0 then (⊤ : Submodule R M) else ⊥) :
    Submodule R M))

instance instModuleConcentratedPage (c : CellIndex) :
    Module R (ConcentratedPage R M c) :=
  inferInstanceAs (Module R ((if c.p = 0 then (⊤ : Submodule R M) else ⊥) :
    Submodule R M))

/-- Off the `p = 0` column the page is the zero module.

This is the only property of the family the collapse argument uses. -/
theorem subsingleton_of_p_ne_zero {c : CellIndex} (h : c.p ≠ 0) :
    Subsingleton (ConcentratedPage R M c) := by
  constructor
  rintro ⟨x, hx⟩ ⟨y, hy⟩
  simp only [if_neg h, Submodule.mem_bot] at hx hy
  subst hx; subst hy; rfl

/-- **The `p = 0` column is genuinely `M`.**

Recorded so that the family cannot be mistaken for a dressed-up `PUnit`: the
surviving column is the whole module — `Z(A)` in the intended reading — not a
placeholder. -/
noncomputable def columnEquiv {c : CellIndex} (h : c.p = 0) :
    ConcentratedPage R M c ≃ₗ[R] M :=
  (LinearEquiv.ofEq _ _ (by simp only [if_pos h])).trans
    Submodule.topEquiv

/-- **Concentration forces collapse at E₂.**

For *every* differential this page family admits — the statement quantifies over
`S`, and its proof never looks at `S.d`.  The `r = 0` and `r = 1` differentials are
unconstrained; collapse asks only about `r ≥ 2`, and there the shift `p ↦ p + r`
already leaves the window.

This is Step 1 of `conj:phi-q-categorical-truncation` turned from an assertion into
a consequence of the concentration that step states. -/
theorem concentrated_collapses (S : PagedSS R (ConcentratedPage R M)) :
    Collapses S 2 := by
  refine collapses_two_of_bounded_support S 0 (by norm_num) ?_
  intro c hc
  refine subsingleton_of_p_ne_zero R M ?_
  rcases hc with h | h <;> omega

/-- **The discharge, from a real page family.**

`legacyOfPaged` has existed since 2026-08-24 and had no argument to be applied to.
This is the first `GBFiltrationCollapsesAtE2` in the corpus whose witness is neither
`PUnit` nor an assumption: the pages are `M` on the surviving column, and the
collapse is derived from the support rather than built into the model. -/
def gbCollapsesOfConcentrated (S : PagedSS R (ConcentratedPage R M)) :
    GBFiltrationCollapsesAtE2 R :=
  legacyOfPaged S (concentrated_collapses R M S)

/-! ### Inhabitation, as a theorem rather than a named model

    `QOU/Mathlib/PagedSpectralSequence.lean` declines to ship a trivial witness, and
    gives the reason: a named trivial model is a thing downstream code reaches for,
    and in `QOU/Mathlib/SpectralSequence.lean` one was reached for and then cited as
    though the substrate axiom had been discharged.

    The same reasoning applies here, but the opposite question also needs an answer:
    a structure nothing can inhabit makes every theorem about it vacuous, and that is
    precisely the defect this module was written to measure.  So inhabitation is
    recorded as an existence **theorem** — enough to show the tower is not empty,
    with no name for a downstream citation to point at. -/

/-- **The page family is inhabitable.**

Witnessed by the zero differential, whose page-turning isomorphism is the identity
composite `E_{r+1} ≅ ker 0 ⧸ im 0 = ⊤ ⧸ ⊥`.

The witness is *not* what makes `concentrated_collapses` true — that theorem
quantifies over every `S` and never inspects `S.d`.  This only rules out the reading
under which the results above are about an empty type. -/
theorem nonempty_pagedSS_concentrated :
    Nonempty (PagedSS R (ConcentratedPage R M)) := by
  refine ⟨{ d := fun _ => 0, d_comp_d := fun _ => LinearMap.comp_zero _,
            turn := fun c => ?_ }⟩
  -- `page` is fixed by unification with the goal here, which is why the
  -- `incoming = ⊥` obligation is deferred into `refine` rather than stated as a
  -- standalone `have`: outside the goal its page family is a metavariable.
  have hker : LinearMap.ker (0 : ConcentratedPage R M c →ₗ[R]
      ConcentratedPage R M (CellIndex.next c)) = ⊤ := LinearMap.ker_zero
  refine ((Submodule.topEquiv (R := R) (M := ConcentratedPage R M c)).symm.trans
    (LinearEquiv.ofEq _ _ hker.symm)).trans (Submodule.quotEquivOfEqBot _ ?_).symm
  simp only [incoming, LinearMap.comp_zero, LinearMap.range_zero,
    Submodule.comap_bot, Submodule.ker_subtype]

end QOU.Mathlib.ConcentratedColumnCollapse

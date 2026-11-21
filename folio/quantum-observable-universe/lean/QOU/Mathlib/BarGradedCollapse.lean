import QOU.Mathlib.PagedSpectralSequence
import Mathlib.Tactic

/-!
# QOU.Mathlib.BarGradedCollapse — collapse *proved* from a parity grading

Bean `qou-fngs`, continuing the arc. `PagedSpectralSequence.lean` made
`Collapses` mean something; this file gives the first way to **prove** it
instead of assuming it.

## The argument the corpus already has, one level up

`QOU/QBeta/ZBarParity.lean` works at the **scalar** level. Under the fibre bar
involution `q ↦ q⁻¹` it proves `z` is exactly bar-even, `κ_{(2,1)}` exactly
bar-odd, and — the load-bearing step — `bar_even_ne_bar_odd_of_ne_zero`: an
even scalar cannot equal a nonzero odd one, in characteristic `≠ 2`. That is
the `c₃`-odd exclusion (`ck_a1_bar_odd_of_c3_odd`).

Read structurally, that is a **ℤ/2 grading**, and the exclusion is the most
classical reason a spectral sequence degenerates: a differential that must
shift parity, landing where the parity is wrong, is zero *because of the
grading* — no computation, no filtration analysis.

What was missing is the lift from scalars to **maps between modules**. That is
this file:

* `eq_zero_of_even_and_odd` — an element both even and odd is zero, given
  2-torsion-freeness (the module form of `bar_even_and_odd_two_mul_eq_zero`);
* `map_eq_zero_of_parity_mismatch` — a bar-**equivariant** map from a purely
  even module to a purely odd one is the zero map;
* `collapses_of_parity_mismatch` — hence a `PagedSS` whose differentials run
  even → odd from page `r₀` on **collapses at `r₀`**.

The third is a collapse theorem with a proof. `GBFiltrationCollapsesAtE2`
asserted the same shape and was discharged by `PUnit`.

## What is assumed, and it is not hidden

The parity data is a hypothesis: someone must exhibit the involution and show
the pages are purely even / purely odd. That is real mathematical work and this
file does not do it for the Gröbner filtration. What it removes is the step
where collapse itself was assumed — given the grading, collapse now follows.

2-torsion-freeness is carried explicitly rather than assumed via a field, so
the result is available over `R_q = ℤ[q, q⁻¹]`, where the corpus actually
works, and not only after specialising to `ℝ`.

-- Ref: [leitner2026] quantum-observable-universe/qbeta
-/

namespace QOU.Mathlib.BarGradedCollapse

open QOU.Mathlib.SpectralSequence QOU.Mathlib.PagedSpectralSequence

universe u v

variable {R : Type u} [CommRing R]

/-- A **bar involution** on an `R`-module: an `R`-linear map squaring to the
    identity. The fibre involution `q ↦ q⁻¹` of `ZBarParity` induces one on
    every module the corpus grades by it. -/
structure BarInvolution (M : Type v) [AddCommGroup M] [Module R M] where
  /-- The involution. -/
  bar : M →ₗ[R] M
  /-- It squares to the identity. -/
  bar_bar : ∀ x, bar (bar x) = x

variable {M N : Type v} [AddCommGroup M] [Module R M] [AddCommGroup N] [Module R N]

/-- `x` is bar-**even**: fixed by the involution. -/
def IsEven (b : BarInvolution (R := R) M) (x : M) : Prop := b.bar x = x

/-- `x` is bar-**odd**: negated by the involution. -/
def IsOdd (b : BarInvolution (R := R) M) (x : M) : Prop := b.bar x = -x

/-- **Even and odd meet only at zero** — the module form of
    `ZBarParity.bar_even_and_odd_two_mul_eq_zero`.

    2-torsion-freeness is a hypothesis rather than a field assumption, so this
    is usable over `R_q = ℤ[q, q⁻¹]` and not only after specialising to `ℝ`. -/
theorem eq_zero_of_even_and_odd (b : BarInvolution (R := R) M) {x : M}
    (he : IsEven b x) (ho : IsOdd b x)
    (htors : ∀ y : M, y + y = 0 → y = 0) : x = 0 := by
  unfold IsEven at he
  unfold IsOdd at ho
  have hx : x = -x := he.symm.trans ho
  refine htors x ?_
  nth_rewrite 2 [hx]
  simp

/-- **A parity-mismatched equivariant map is zero.**

    If `f` intertwines the two involutions, the source is purely even and the
    target purely odd, then every `f x` is both even (transported from the
    source) and odd (by the target's grading) — hence zero.

    This is `ZBarParity`'s exclusion applied to a map rather than a scalar, and
    it is what makes a grading force a differential to vanish. -/
theorem map_eq_zero_of_parity_mismatch
    (bM : BarInvolution (R := R) M) (bN : BarInvolution (R := R) N)
    (f : M →ₗ[R] N)
    (hequiv : ∀ x, bN.bar (f x) = f (bM.bar x))
    (heven : ∀ x : M, IsEven bM x)
    (hodd : ∀ y : N, IsOdd bN y)
    (htors : ∀ y : N, y + y = 0 → y = 0) :
    f = 0 := by
  ext x
  refine eq_zero_of_even_and_odd bN ?_ (hodd _) htors
  show bN.bar (f x) = f x
  rw [hequiv x, heven x]

/-- **Collapse, proved from the grading.**

    A `PagedSS` carrying a bar involution on every page, whose differentials
    are equivariant and run purely-even → purely-odd from page `r₀` on,
    collapses at `r₀`.

    Nothing is assumed about the filtration; the grading does the work. Compare
    `GBFiltrationCollapsesAtE2`, which asserted the conclusion and was
    discharged by a `PUnit` model — see
    `SpectralSequence.collapse_is_definitional`. -/
theorem collapses_of_parity_mismatch {page : CellIndex → Type v}
    [∀ c, AddCommGroup (page c)] [∀ c, Module R (page c)]
    (S : PagedSS R page) (r₀ : ℕ)
    (b : ∀ c, BarInvolution (R := R) (page c))
    (hequiv : ∀ c x, (b (CellIndex.next c)).bar (S.d c x) = S.d c ((b c).bar x))
    (heven : ∀ c, r₀ ≤ c.r → ∀ x : page c, IsEven (b c) x)
    (hodd : ∀ c, r₀ ≤ c.r → ∀ y : page (CellIndex.next c), IsOdd (b _) y)
    (htors : ∀ c, ∀ y : page c, y + y = 0 → y = 0) :
    Collapses S r₀ := by
  intro c hc
  exact map_eq_zero_of_parity_mismatch (b c) (b (CellIndex.next c)) (S.d c)
    (hequiv c) (heven c hc) (hodd c hc) (htors _)

/-- **The payoff, chained.** A parity-graded spectral sequence stabilises: from
    page `r₀` on, the next page is isomorphic to this one.

    This is the statement the substrate axiom `S-GB-spectral-collapse` wants,
    now reachable from a grading rather than posited. Supplying the grading for
    the Gröbner filtration is the remaining work. -/
theorem page_stabilises_of_parity {page : CellIndex → Type v}
    [∀ c, AddCommGroup (page c)] [∀ c, Module R (page c)]
    (S : PagedSS R page) (r₀ : ℕ)
    (b : ∀ c, BarInvolution (R := R) (page c))
    (hequiv : ∀ c x, (b (CellIndex.next c)).bar (S.d c x) = S.d c ((b c).bar x))
    (heven : ∀ c, r₀ ≤ c.r → ∀ x : page c, IsEven (b c) x)
    (hodd : ∀ c, r₀ ≤ c.r → ∀ y : page (CellIndex.next c), IsOdd (b _) y)
    (htors : ∀ c, ∀ y : page c, y + y = 0 → y = 0)
    (c : CellIndex) (hc : r₀ ≤ c.r) :
    Nonempty (page (CellIndex.bump c) ≃ₗ[R] page c) :=
  page_stabilises_of_collapse S r₀
    (collapses_of_parity_mismatch S r₀ b hequiv heven hodd htors) c hc

end QOU.Mathlib.BarGradedCollapse

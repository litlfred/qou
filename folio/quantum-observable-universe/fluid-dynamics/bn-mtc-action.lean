import Mathlib.CategoryTheory.Monoidal.Braided.Basic
import Mathlib.CategoryTheory.Endomorphism


/-!
# QOU.bnAction

Categorical braiding on 𝐕⊗𝐕 induces a B_n representation on 𝐕^⊗n
that does not factor through the symmetric-group quotient, because
the observable MTC braiding is non-symmetric on some simple.

LaTeX label: `prop:bn-mtc-action`

**Ground ring**: `ℂ` (categorical; non-computational).

## Why the non-symmetry is a hypothesis rather than an instance

The natural home for the non-symmetry witness is the field
`ObservableMTC.braiding_nonsymmetric` of `def:observable-mtc`. This
file cannot reach it: content-block siblings live outside the Lake
globs (`globs = ["QOU", "QOU.+"]`), so a sibling cannot import a
sibling. The previous version wrote `[MTC : ObservableMTC C]` anyway,
which `autoImplicit` silently turned into an auto-bound variable and
the elaborator then rejected —

    invalid binder annotation, type is not a class instance ?m.5

That version also had a second defect the compile error was hiding: it
concluded `∃ V, (β_ V V).hom ≫ (β_ V V).hom ≠ 𝟙 (V ⊗ V)` and proved it
by `MTC.braiding_nonsymmetric`, i.e. it restated a **field of the
definition** and projected it out. That is the self-assuming shape
AGENTS.md §3b-cond item 5 forbids, and it is not the `.md` claim: the
`.md` claims the representation *does not factor through* `B_n ↠ S_n`.

So the non-symmetry now enters as an explicit hypothesis `hV` — the
defining property of an observable MTC, supplied by the caller — and
the theorem **derives** the non-factoring from it.
-/

set_option autoImplicit false

namespace QOU

open CategoryTheory MonoidalCategory BraidedCategory

/-- **No factorisation through a quotient that kills the generator's
    order.**

    If `π : B →* S` sends `σ` to an element squaring to `1`, while
    `ρ : B →* G` sends `σ` to an element whose square is not `1`, then
    `ρ` cannot be written as `φ ∘ π`.

    This is the group-theoretic content of the proposition, stated
    without reference to braids: `π` is `B_n ↠ S_n`, `σ` is a braid
    generator `σ_i` (whose image is a transposition, hence an
    involution), and `ρ` is the categorical representation. -/
theorem not_factorsThrough_of_sq_ne_one
    {B S G : Type*} [Group B] [Group S] [Group G]
    (π : B →* S) (ρ : B →* G) (σ : B)
    (hπ : π σ ^ 2 = 1) (hρ : ρ σ ^ 2 ≠ 1) :
    ¬ ∃ φ : S →* G, ρ = φ.comp π := by
  rintro ⟨φ, rfl⟩
  exact hρ (by rw [MonoidHom.comp_apply, ← map_pow, hπ, map_one])

/-- A non-symmetric braiding on `V` is an element of `Aut (V ⊗ V)`
    whose square is not the identity.  This is the bridge from the
    categorical statement `c ∘ c ≠ id` to the group statement
    `x ^ 2 ≠ 1` that `not_factorsThrough_of_sq_ne_one` consumes. -/
theorem braiding_sq_ne_one
    {C : Type*} [Category C] [MonoidalCategory C] [BraidedCategory C]
    (V : C) (hV : (β_ V V).hom ≫ (β_ V V).hom ≠ 𝟙 (V ⊗ V)) :
    (show Aut (V ⊗ V) from β_ V V) ^ 2 ≠ 1 := by
  intro h
  rw [pow_two] at h
  -- `(f * g).hom = g.hom ≫ f.hom` and `(1 : Aut X).hom = 𝟙 X` are both
  -- `rfl` for `Aut`, so the categorical equation is the group one.
  exact hV (congrArg Iso.hom h)

/-- **The braid representation does not factor through `S_n`**
    (`prop:bn-mtc-action`).

    Let `C` be braided monoidal and let `V` be an object on which the
    braiding is non-symmetric — the defining property of a simple in an
    observable MTC (`def:observable-mtc`, field
    `braiding_nonsymmetric`), supplied here as `hV` because a
    content-block sibling cannot import a sibling.

    Let `π : B →* S` be any quotient sending the braid generator `σ` to
    an involution — this is exactly `B_n ↠ S_n`, under which `σ_i` maps
    to the transposition `(i, i+1)`.

    Then no representation `ρ` sending `σ` to the braiding factors
    through `π`.  This is the `.md` claim; it is *derived* from `hV`
    rather than projected out of it.

    **Scope, stated so it is not overread.**  This is the statement at
    the `V ⊗ V` level — equivalently `n = 2`, where the `.md`'s
    `ρ_n(σ_i)` is the bare braiding.  The general-`n` form quantifies
    over `Aut (V^{⊗ n})` with `ρ_n(σ_i) = id^{⊗(i-1)} ⊗ c_{V,V} ⊗
    id^{⊗(n-i-1)}`, and needs the tensor-power construction plus the
    fact that whiskering an automorphism preserves "square ≠ 1"; that
    is not built here.  The obstruction argument itself is already
    general: `not_factorsThrough_of_sq_ne_one` is stated for arbitrary
    groups and consumes only `ρ σ ^ 2 ≠ 1`, so extending to general `n`
    is supplying that hypothesis for the whiskered braiding, not
    redoing the argument.

    LaTeX: `\label{prop:bn-mtc-action}`
    Ref: [kitaev2006] https://doi.org/10.1016/j.aop.2005.10.005
    Ref: [moore-seiberg1989] https://doi.org/10.1007/BF01238857 -/
theorem bnAction
    {C : Type*} [Category C] [MonoidalCategory C] [BraidedCategory C]
    {B S : Type*} [Group B] [Group S]
    (V : C) (hV : (β_ V V).hom ≫ (β_ V V).hom ≠ 𝟙 (V ⊗ V))
    (π : B →* S) (σ : B) (hπ : π σ ^ 2 = 1)
    (ρ : B →* Aut (V ⊗ V)) (hρσ : ρ σ = (show Aut (V ⊗ V) from β_ V V)) :
    ¬ ∃ φ : S →* Aut (V ⊗ V), ρ = φ.comp π :=
  not_factorsThrough_of_sq_ne_one π ρ σ hπ
    (by rw [hρσ]; exact braiding_sq_ne_one V hV)

end QOU

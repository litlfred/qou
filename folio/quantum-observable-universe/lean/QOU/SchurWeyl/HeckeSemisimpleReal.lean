import QOU.SchurWeyl.HeckeSemisimpleGeneral

/-!
# QOU.SchurWeyl.HeckeSemisimpleReal — the `ℝ` specialisations of the semisimplicity result

Split out of `QOU/SchurWeyl/HeckeSemisimpleGeneral.lean` (bean `qou-j377`).

That file is now generic: `isSemisimpleRing_hecke_generic` holds over any
`[Field K] [CharZero K]` with `q` not a root of unity.  What is collected here is everything
that is genuinely about `ℝ`:

* `isSemisimpleRing_hecke` — the same statement in the hypothesis shape the substrate uses,
  `q ≠ 0` and `q ^ 2 ≠ 1`.  **Over `ℝ`, and only over `ℝ`, that pair already says `q` is not
  a root of unity** (`GenericParameter.ofSqNeOne`); over a general field it fails at a
  primitive fourth root of unity, which is why the generic statement carries the criterion
  directly rather than this pair.
* `isSemisimpleRing_hecke_of_one_lt`, `wenzlCriterion_of_one_lt`,
  `semisimple_of_one_lt_unconditional` — the `1 < q` forms, which are ordered-field
  statements by construction.

§7c asks that a generic development and its archimedean specialisation not share a file, and
here the split also marks exactly where the mathematics changes.
-/

namespace QOU.SchurWeyl

/-- **The `ℝ` specialisation**, in the hypothesis shape the substrate uses.

Over `ℝ` — and only over `ℝ` — `q ≠ 0` together with `q ^ 2 ≠ 1` already says `q` is not a
root of unity, which is what `QOU.SchurWeyl.GenericParameter.ofSqNeOne` supplies.  Over a
general field that implication fails at a primitive fourth root of unity, so the generic
statement above carries the criterion directly. -/
theorem isSemisimpleRing_hecke (q : ℝ) (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (n : ℕ) :
    IsSemisimpleRing (Hecke ℝ q q⁻¹ n) :=
  isSemisimpleRing_hecke_generic q hq0 (QOU.SchurWeyl.GenericParameter.ofSqNeOne hq0 hq2) n

/-- **The substrate discharges semisimplicity at every rank (sorry-free).**

    For any real `q > 1` — in particular the substrate `q₀ ≈ 1.10998` —
    `QOU.SchurWeyl.Hecke ℝ q q⁻¹ n` is semisimple at every rank.  This is the
    shape in which the substrate parameter discharges the semisimplicity leg of
    the `P ≠ NP`-in-QOU counting argument, with no cited class and no `sorry`.

    The carrier is named explicitly rather than called "the Iwahori–Hecke
    algebra", because this file's scope section distinguishes it from
    `QOU.Hecke.IwahoriHecke`, and the informal name would read as a claim about
    that one. -/
theorem isSemisimpleRing_hecke_of_one_lt {q : ℝ} (hq : 1 < q) (n : ℕ) :
    IsSemisimpleRing (Hecke ℝ q q⁻¹ n) := by
  refine isSemisimpleRing_hecke q (by positivity) ?_ n
  have h1 : 1 < q ^ 2 := by nlinarith
  exact ne_of_gt h1

/-! ## Discharging the cited `WenzlCriterion`

`QOU.Information.PNeqNpEquivalence.WenzlCriterion` is a hypothesis class — its
own docstring says "hypothesis class, not a theorem of this development" — and
it had **no instance anywhere in the corpus**.  Everything downstream of
`semisimple_of_one_lt` was therefore conditional on an assumption with no known
model.  It has one now. -/

/-- **A model for the cited `WenzlCriterion` (sorry-free).**

    For any real `q > 1`, the criterion holds with `semisimple n` instantiated
    as actual semisimplicity of the rank-`n` algebra.  This is what the class
    was asking for and had never been supplied.

    The `WenzlGeneric` hypothesis is not used: over `ℝ`, `1 < q` already gives
    semisimplicity outright, so the criterion is satisfied a fortiori.  Note
    that a *blanket* instance quantified over all `q` would be **false** as the
    class is stated — `WenzlGeneric 0 n` holds vacuously (`0 ^ k = 0 ≠ 1`)
    while `q = 0` is degenerate — which is why this is a theorem taking `hq`,
    not an `instance`. -/
theorem wenzlCriterion_of_one_lt {q : ℝ} (hq : 1 < q) :
    QOU.Information.WenzlCriterion q
      (fun n => IsSemisimpleRing (Hecke ℝ q q⁻¹ n)) :=
  ⟨fun n _ => isSemisimpleRing_hecke_of_one_lt hq n⟩

/-- **`semisimple_of_one_lt`, with the criterion discharged (sorry-free).**

    The composition: no cited class remains between `1 < q` and semisimplicity
    at every rank.

    Scope, so this is not over-read: semisimplicity is a magnitude-axis fact.
    Nothing here bears on the `P ≠ NP` wall, and the counting-to-decision
    transfer is untouched. -/
theorem semisimple_of_one_lt_unconditional {q : ℝ} (hq : 1 < q) (n : ℕ) :
    IsSemisimpleRing (Hecke ℝ q q⁻¹ n) :=
  haveI := wenzlCriterion_of_one_lt hq
  QOU.Information.semisimple_of_one_lt
    (ss := fun n => IsSemisimpleRing (Hecke ℝ q q⁻¹ n)) hq n

end QOU.SchurWeyl

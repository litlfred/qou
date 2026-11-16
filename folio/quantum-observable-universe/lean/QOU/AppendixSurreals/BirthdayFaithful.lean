/-
  The birthday axioms constrain only from above — and the missing lower bound, as an
  opt-in mixin whose independence is proved rather than asserted.

  Bean `qou-bday`.  Reads on from `qou-hypr`.

  ═══ THE PROBLEM, IN ONE LINE ═══

  `QOU/AppendixSurreals/HyperrealLimitTransfer.lean` proves that

      flatBirthday x := if x = 0 then 0 else 1

  — a **two-valued** function — satisfies **all six** birthday axioms of `SurrealField`.
  So those axioms do not characterise Conway's birthday.

  ═══ WHAT THAT COSTS, STATED SHARPLY ═══

  `flatBirthday ≤ 1` everywhere.  Therefore:

  > **No lower bound on birthday is derivable from the current axioms.**  Any statement
  > of the form `birthday x ≥ f x` with `f` unbounded is refuted by the flat model.

  Upper bounds are unaffected — which is exactly why the bounds the appendix actually
  proves survive.  They are all upper bounds, and correspondingly weak.  §1 below makes
  that concrete: `birthday (n : K) ≤ n` is already a **theorem** from the existing axioms,
  by induction on `birthday_one` and `birthday_add_le`.  The matching `≥` is what is
  missing, and it is missing because nothing in the axiom set can supply it.

  ═══ THE FIX, AND WHY IT IS OPT-IN ═══

  §2 adds `BirthdayFaithful` — a **mixin**, not a change to `SurrealField` — carrying the
  one equation `birthday (n : K) = n`.  Opt-in for three reasons:

  * `SurrealField` is used across ~38 modules; strengthening it in place would force every
    one of them to supply the new field, and most do not care about birthdays at all;
  * a mixin makes the dependency *visible*: a theorem that needs real birthday content
    says so in its hypotheses, and one that does not, does not;
  * the corpus already demonstrates this pattern — `BlowupCalculus.lean`'s `BlowupField`
    is declared over the plain ordered-field classes rather than over `SurrealField`.

  §3 proves the mixin is a **genuine** strengthening: `flatBirthday` fails it, so
  `BirthdayFaithful` is not derivable from the six existing axioms.  That is the point of
  this module — the claim "this kills the flat model" is a theorem here, not a remark.

  ⚠ **Not claimed:** that `BirthdayFaithful` is *sufficient* to pin down Conway's
  birthday.  It rules out the flat model; it does not rule out every degenerate model.
  Whether the axiom set is now categorical is open and is not addressed.

  -- Ref: [conway1976] Ch. 0
  -- Ref: [gonshor1986]
-/
import QOU.AppendixSurreals.HyperrealLimitTransfer

namespace QOU.AppendixSurreals

open SurrealField

universe u

/-! ## §1 — the upper bound is already a theorem

`birthday (n : K) ≤ n` follows from `birthday_one` and `birthday_add_le` alone.  Stating
it makes the asymmetry visible: the axioms give the `≤` and nothing gives the `≥`. -/

variable {K : Type u} [SurrealField K]

/-- **`birthday (n : K) ≤ n`, from the existing axioms.**

Induction: `birthday (n+1) ≤ birthday n ♯ birthday 1 = birthday n ♯ 1 = succ (birthday n)`,
and `succ` is monotone.  Nothing here needs a new axiom — which is the point. -/
theorem birthday_natCast_le : ∀ n : ℕ, birthday ((n : ℕ) : K) ≤ (n : Ordinal)
  | 0 => by simpa using le_of_eq (birthday_zero (K := K))
  | (n + 1) => by
      have hstep : birthday (((n : ℕ) : K) + 1)
          ≤ Ordinal.nadd (birthday ((n : ℕ) : K)) (birthday (1 : K)) :=
        birthday_add_le _ _
      rw [birthday_one] at hstep
      rw [Ordinal.nadd_one] at hstep
      have hmono : Order.succ (birthday ((n : ℕ) : K)) ≤ Order.succ (n : Ordinal) :=
        Order.succ_le_succ (birthday_natCast_le n)
      have : birthday (((n : ℕ) : K) + 1) ≤ Order.succ (n : Ordinal) := hstep.trans hmono
      simpa [Ordinal.natCast_succ] using this

/-! ## §2 — the missing lower bound, as an opt-in mixin -/

/-- **`BirthdayFaithful`** — the one equation the six `SurrealField` axioms cannot supply:
the natural numbers are born on the day their value names.

A **mixin**, deliberately.  `SurrealField` is used across ~38 modules and most of them do
not reason about birthdays; requiring this of all of them would be noise.  Carrying it
separately also makes the dependency legible — a result that needs genuine birthday
content takes `[BirthdayFaithful K]`, and one that does not, does not.

Combined with `birthday_natCast_le` (§1, which needs no mixin) this pins `birthday n`
exactly; the mixin supplies only the half that was missing. -/
class BirthdayFaithful (K : Type u) [SurrealField K] where
  /-- Conway: the natural number `n` is born on day `n`. -/
  birthday_natCast : ∀ n : ℕ, birthday ((n : ℕ) : K) = (n : Ordinal)

/-- With the mixin, the two halves meet: the bound of §1 is attained. -/
theorem birthday_natCast_eq [BirthdayFaithful K] (n : ℕ) :
    birthday ((n : ℕ) : K) = (n : Ordinal) :=
  BirthdayFaithful.birthday_natCast n

/-! ## §3 — the mixin is a GENUINE strengthening

If `BirthdayFaithful` followed from the six existing axioms it would be satisfied by every
model of them, including the flat one.  It is not. -/

/-- **The flat model fails the mixin**, at `n = 2`.

`flatBirthday` assigns `1` to every nonzero element, so `flatBirthday (2 : ℝ*) = 1 ≠ 2`.
Since `flatBirthday` *does* satisfy all six birthday axioms
(`HyperrealLimitTransfer.surrealFieldHyperreal`), this shows `BirthdayFaithful` is **not
derivable** from them. -/
theorem flatBirthday_not_faithful :
    ¬ (∀ n : ℕ, HyperrealTransfer.flatBirthday ((n : ℕ) : ℝ*) = (n : Ordinal)) := by
  intro h
  have h2 := h 2
  rw [show ((2 : ℕ) : ℝ*) = (2 : ℝ*) by norm_num] at h2
  rw [HyperrealTransfer.flatBirthday_two] at h2
  -- `1 = 2` in `Ordinal` is false.
  have : (1 : Ordinal) ≠ ((2 : ℕ) : Ordinal) := by
    norm_num
  exact this h2

/-- **Summary, as a single statement.**  The six birthday axioms are satisfiable together
with the *negation* of the mixin — witnessed by `flatBirthday` on `ℝ*` — so the mixin adds
strictly new content. -/
theorem birthdayFaithful_independent_of_surrealField_axioms :
    (∃ _ : SurrealField.{0, 0} ℝ*, True)
      ∧ ¬ (∀ n : ℕ, HyperrealTransfer.flatBirthday ((n : ℕ) : ℝ*) = (n : Ordinal)) :=
  ⟨⟨HyperrealTransfer.surrealFieldHyperreal, trivial⟩, flatBirthday_not_faithful⟩

/-- **Independence, with the two halves actually joined.**

⚠ The conjunction above is **weaker than its name**, and the gap is easy to miss. Its first
conjunct says *some* `SurrealField` structure exists on `ℝ*`; its second says `flatBirthday`
fails the mixin. Nothing in the statement says these concern the **same** structure — read
literally it would be satisfied by an unrelated witness for each half, which is not
independence.

This is the honest form: **one** structure, satisfying all six axioms, whose *own* birthday
fails the mixin. It is what the earlier docstring already claimed ("witnessed by
`flatBirthday` on `ℝ*`") and what the conjunction did not say.

The proof is unchanged because `surrealFieldHyperreal.birthday` **is** `flatBirthday` by
definition — so the content was always there, and only the statement was loose. That is
precisely why it was worth tightening rather than leaving as a comment: a reader checking
the theorem, not the field assignment, could not have known. -/
theorem birthdayFaithful_independent_witnessed :
    ∃ S : SurrealField.{0, 0} ℝ*,
      ¬ (∀ n : ℕ, S.birthday ((n : ℕ) : ℝ*) = (n : Ordinal)) :=
  ⟨HyperrealTransfer.surrealFieldHyperreal, flatBirthday_not_faithful⟩

/-! ## §4 — `StrictBirthdayHierarchy` and exclusion of every finite-bounded birthday model

`BirthdayFaithful` not only excludes the two-valued `flatBirthday ≤ 1` model, it enforces a
strictly increasing ordinal hierarchy on the natural numbers `0 < 1 < 2 < ⋯ < n < ⋯` and
therefore rules out **every** finite-bounded birthday assignment `birthday x ≤ B` (`B : ℕ`). -/

/-- Alias emphasizing that `[BirthdayFaithful K]` equips `K` with a strict, unbounded ordinal
birthday hierarchy on `(n : K)` (`bday`). -/
abbrev StrictBirthdayHierarchy (K : Type u) [SurrealField K] := BirthdayFaithful K

/-- Under `[BirthdayFaithful K]`, the map `n ↦ birthday (n : K)` is strictly monotone. -/
theorem birthday_natCast_strictMono [BirthdayFaithful K] {m n : ℕ} (hmn : m < n) :
    birthday ((m : ℕ) : K) < birthday ((n : ℕ) : K) := by
  rw [birthday_natCast_eq, birthday_natCast_eq]
  exact Nat.cast_lt.mpr hmn

/-- Under `[BirthdayFaithful K]`, birthdays are unbounded across the finite ordinals:
for every `N : ℕ` there exists `x : K` with `(N : Ordinal) ≤ birthday x`. -/
theorem birthday_unbounded_of_faithful [BirthdayFaithful K] (N : ℕ) :
    ∃ x : K, (N : Ordinal) ≤ birthday x := by
  refine ⟨((N : ℕ) : K), ?_⟩
  rw [birthday_natCast_eq]

/-- Under `[BirthdayFaithful K]`, no finite ordinal `B : ℕ` can bound `birthday x` for all
`x : K` (ruling out not only the 2-valued `flatBirthday ≤ 1` model, but every `B`-bounded
model). -/
theorem no_finite_birthday_bound_of_faithful [BirthdayFaithful K] (B : ℕ) :
    ¬ (∀ x : K, birthday x ≤ (B : Ordinal)) := by
  intro hB
  have hlt : birthday ((B : ℕ) : K) < birthday (((B + 1 : ℕ) : K)) :=
    birthday_natCast_strictMono (Nat.lt_succ_self B)
  rw [birthday_natCast_eq] at hlt
  exact not_le_of_gt hlt (hB (((B + 1 : ℕ) : K)))

end QOU.AppendixSurreals

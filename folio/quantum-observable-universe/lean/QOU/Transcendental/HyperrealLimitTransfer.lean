/-
  `conj:surreal-limit-transfer` at the hyperreals — what discharges, and what the
  attempt to discharge it reveals about `SurrealField` itself.

  Bean `qou-hypr`.  Reads on from bean `qou-thmb`.

  **Transcendental subgraph (moved 2026-11-27, bean `qou-134z`).** This module
  is the analytic half of the surreal limit transfer: the ultrapower `ℝ*` and
  `Filter.Tendsto`. It lives behind the boundary `QOU/Transcendental/`. The
  limit theorems the corpus needs (uniqueness, comparison, squeeze) no longer
  depend on it: they are order algebra on located cuts in `QOU.Core.CutLimit`.

  ═══ WHAT BEAN `hypr` CLAIMED, AND WHY IT WAS WRONG ═══

  Bean `hypr` argued that `SurrealField ℝ*` "looks close to free" because
  `SurrealField` *extends* `Field K, LinearOrder K, IsStrictOrderedRing K` and `ℝ*`
  has all three.  **That argument was written from the `extends` clause alone and
  never read the rest of the class.**  `SurrealField` also demands Conway's

      birthday : K → Ordinal

  with six axioms (`birthday_zero`, `birthday_one`, `birthday_neg`,
  `birthday_add_le`, `birthday_avg_le`, `birthday_ofReal_le_omega`), plus
  `omegaSurreal`.  Mathlib's `Hyperreal` has no birthday function, Mathlib's
  `Surreal` has no birthday function, and (checked 2026-08-09) **no `SurrealField`
  instance exists anywhere in this corpus** — this file's `def` is the first.

  ═══ THE PART THAT IS UNCONDITIONALLY TRUE (§1) ═══

  Every *analytic* claim bean `hypr` wanted is a theorem about `ℝ*` and needs no
  surreal structure at all.  §1 proves the whole limit-transfer content directly:
  `ofSeq` for the ω-evaluation, `Hyperreal.st` for the standard part, and

  * `st_ofSeq_of_tendstoReal` — limits are computed by `st ∘ ofSeq`;
  * `ofSeq_le_ofSeq_of_eventuallyLE` — eventual domination transfers to `ℝ*`;
  * `tendstoReal_le_of_eventuallyLE'` — the limit-comparison inequality, routed
    through one hyperreal inequality at `ω`.

  These are `SurrealField`-free, `birthday`-free, and instance-free.  If you want
  the mathematics of `conj:surreal-limit-transfer`, it is §1 and it is proved.

  ═══ THE PART THAT IS A DEFECT REPORT (§2) ═══

  Can the *class* be discharged too?  Yes — and the way it discharges is the
  finding.  `flatBirthday x := if x = 0 then 0 else 1` — a **two-valued** function,
  visibly not Conway's birthday — satisfies **all six birthday axioms**
  (`flatBirthday_*` below, each proved).  So:

  > The `birthday` axioms in `QOU/AppendixSurreals/Basic.lean` do not characterise
  > Conway's birthday.  They admit a model in which every nonzero element is born
  > on day 1.  Any theorem proved *from those axioms alone* is therefore true of
  > that model too, and says nothing specific about birthdays.

  `birthday_avg_le` in particular — documented in `Basic.lean` as "exactly Conway's
  `{L | R}` recipe" and "genuinely independent of `birthday_add_le`" — is satisfied
  here for the degenerate reason that its right-hand side is `≥ 1` and its left-hand
  side is `≤ 1`.  It constrains nothing under a bounded birthday.

  ⚠ `surrealFieldHyperreal` is therefore a **`def`, never a global `instance`**:
  registering it globally would apply every `BirthdayField`-generic theorem to `ℝ*`
  under a birthday that is not Conway's.

  **Resolved 2026-11-27 (owner ruling "Split into base + Conway class").**  The class is
  now three: `SurrealBase` (ordered field ⊇ ℝ with ω, no birthday), `BirthdayField` (the
  six upper-bound axioms) and `SurrealField` (adds `birthday_natCast` and Conway
  simplicity).  `ℝ*` is a global `SurrealBase` instance (`surrealBaseHyperreal`), the
  flat structure is a `BirthdayField` but not a `SurrealField`.  Whether *some other*
  birthday on `ℝ*` makes it a `SurrealField` is not addressed (under CH, `ℝ*` is an
  `η₁` real-closed field of size `ℵ₁`, which suggests it may be; nothing here uses that).

  ═══ WHAT §3 THEN GETS ═══

  Under that local instance, `SurrealLimitTransfer ℝ*` is constructed with every
  field a real Mathlib theorem — none of them mentions `birthday`.  That is the
  precise sense in which the conjecture discharges: **its content is birthday-free,
  and it was stated over a carrier that is not.**  The honest fix is to weaken the
  class's carrier (see the follow-on recorded in bean `hypr`), not to promote this
  instance.

  ═══ ⚠ THE LIMITATION, UNCHANGED FROM BEANS `hypr` AND `thmb` ═══

  `Hyperreal.isSt_ofSeq_iff_tendsto : IsSt (ofSeq f) r ↔ Tendsto f (hyperfilter ℕ) (𝓝 r)`,
  and `Nat.hyperfilter_le_atTop` makes hyperfilter convergence **strictly weaker**
  than `atTop` convergence.  Only `Tendsto atTop → IsSt` is available
  (`isSt_of_tendsto`); the converse is false.  So everything here *pushes* real
  limits into `ℝ*`.  Nothing here discharges a `Tendsto … atTop` goal by a
  standard-part computation — `IsSt (ofSeq f) r` is `f(ω) ≈ r` for one specific `ω`,
  not "for every infinite hypernatural", which is what a genuine NSA limit argument
  needs and which Mathlib does not package.  **Surreal/standard-part machinery does
  not replace the ε–δ arguments in this corpus.**

  -- Ref: [robinson1966] §3.2
  -- Ref: [conway1976] Ch. 0 (birthday)
-/
import QOU.Observations.SurrealLimitTransfer
import Mathlib.Analysis.Real.Hyperreal

namespace QOU.AppendixSurreals.HyperrealTransfer

open QOU.AppendixSurreals

/-! ## §0 — the ε–N form is Mathlib's `Tendsto`

`TendstoReal` is `SurrealLimitTransfer.lean`'s self-contained ε–N convergence,
written to keep topology out of the surreal kernel.  It is `Tendsto _ atTop (𝓝 _)`. -/

/-- The kernel's ε–N convergence implies Mathlib's `Tendsto … atTop (𝓝 L)`. -/
theorem tendsto_atTop_of_tendstoReal {a : ℕ → ℝ} {L : ℝ} (h : TendstoReal a L) :
    Filter.Tendsto a Filter.atTop (nhds L) := by
  rw [Metric.tendsto_atTop]
  intro ε hε
  obtain ⟨N, hN⟩ := h ε hε
  exact ⟨N, fun n hn => by rw [Real.dist_eq]; exact hN n hn⟩

/-! ## §1 — the limit-transfer content at `ℝ*`, unconditionally

No `SurrealField`, no `birthday`, no instance, no conjecture class.  This section is
the mathematics bean `hypr` was after. -/

/-- The ω-evaluation of a convergent sequence has the limit as its standard part —
in Mathlib's `IsSt` form. -/
theorem isSt_ofSeq_of_tendstoReal {a : ℕ → ℝ} {L : ℝ} (h : TendstoReal a L) :
    Hyperreal.IsSt (Hyperreal.ofSeq a) L :=
  Hyperreal.isSt_of_tendsto (tendsto_atTop_of_tendstoReal h)

/-- **Limits are computed by `st ∘ ofSeq`.**  The unconditional `ℝ*` form of
`standardPart_evalOmega_of_tendstoReal`. -/
theorem st_ofSeq_of_tendstoReal {a : ℕ → ℝ} {L : ℝ} (h : TendstoReal a L) :
    Hyperreal.st (Hyperreal.ofSeq a) = L :=
  (isSt_ofSeq_of_tendstoReal h).st_eq

/-- **Eventual domination transfers to the hyperreal order.**  This is the one step
that uses `Nat.hyperfilter_le_atTop`, and it uses it in the *only* direction that is
available. -/
theorem ofSeq_le_ofSeq_of_eventuallyLE {a b : ℕ → ℝ} (h : EventuallyLE a b) :
    Hyperreal.ofSeq a ≤ Hyperreal.ofSeq b := by
  obtain ⟨N, hN⟩ := h
  exact Filter.Germ.coe_le.2
    (Nat.hyperfilter_le_atTop (Filter.eventually_atTop.2 ⟨N, hN⟩))

/-- **Limit comparison through the hyperreal order**, unconditionally.

The whole argument is routed through a single inequality at `ω` plus the
monotonicity of the standard part — the "inequality → nonstandard statement → real
inequality" round trip, with no conjecture class in the statement.

(The strict-inequality collapse is visible here too: `ofSeq a < ofSeq b` is perfectly
compatible with `L = M`, which is why only `≤` survives.) -/
theorem tendstoReal_le_of_eventuallyLE' {a b : ℕ → ℝ} {L M : ℝ}
    (ha : TendstoReal a L) (hb : TendstoReal b M) (hab : EventuallyLE a b) :
    L ≤ M :=
  (isSt_ofSeq_of_tendstoReal ha).le (isSt_ofSeq_of_tendstoReal hb)
    (ofSeq_le_ofSeq_of_eventuallyLE hab)

/-! ## §2 — the birthday axioms admit a two-valued model

Everything in this section is about `QOU/AppendixSurreals/Basic.lean`'s axioms, not
about the hyperreals.  `ℝ*` is used only because it supplies the *other* thing
`SurrealField` needs and `ℝ` cannot: an element above every natural number
(`omegaSurreal_gt_natCast` is false in any archimedean field, so `ℝ` itself is not a
counter-model and the axiom does do that much work). -/

/-- The real embedding `ℝ →+* ℝ*`. -/
noncomputable def hyperrealOfReal : ℝ →+* ℝ* where
  toFun r := (r : ℝ*)
  map_one' := Hyperreal.coe_one
  map_mul' := Hyperreal.coe_mul
  map_zero' := Hyperreal.coe_zero
  map_add' := Hyperreal.coe_add

theorem hyperrealOfReal_strictMono : StrictMono hyperrealOfReal :=
  fun _ _ h => Hyperreal.coe_lt_coe.2 h

open scoped Classical in
/-- **The two-valued candidate birthday**: everything nonzero is born on day 1.

This is transparently *not* Conway's birthday — under Conway, `birthday 2 = 2`,
`birthday (1/2) = 2`, `birthday ω = ω`.  The point of the lemmas below is that
`Basic.lean`'s axioms cannot tell the difference. -/
noncomputable def flatBirthday (x : ℝ*) : Ordinal.{0} := if x = 0 then 0 else 1

/-- `flatBirthday` is bounded by `1` — the fact every axiom below leans on. -/
theorem flatBirthday_le_one (x : ℝ*) : flatBirthday x ≤ 1 := by
  unfold flatBirthday
  split
  · exact Ordinal.zero_le 1
  · exact le_refl 1

theorem flatBirthday_zero : flatBirthday 0 = 0 := by simp [flatBirthday]

theorem flatBirthday_one : flatBirthday 1 = 1 := by simp [flatBirthday]

/-! ### `flatBirthday` is provably not Conway's birthday

Two witnesses, so the claim is a theorem rather than a reading of the definition.
Conway gives `birthday 2 = 2` and `birthday ω = ω`; `flatBirthday` gives `1` for both,
and `1 < ω`. -/

/-- Conway: `birthday 2 = 2`.  Here: `1`. -/
theorem flatBirthday_two : flatBirthday 2 = 1 := by
  simp [flatBirthday]

/-- Conway: `birthday ω = ω`.  Here: `1`, and `1 ≠ ω`. -/
theorem flatBirthday_omega : flatBirthday Hyperreal.omega = 1 := by
  simp [flatBirthday, Hyperreal.omega_ne_zero]

/-- **The two-valued model is not Conway's birthday**, stated as an inequality that
does not depend on knowing `flatBirthday`'s definition: an element strictly above every
natural number is assigned a birthday strictly below `ω`. -/
theorem flatBirthday_omega_lt_omega0 :
    flatBirthday Hyperreal.omega < Ordinal.omega0 := by
  rw [flatBirthday_omega]
  exact Ordinal.one_lt_omega0

theorem flatBirthday_neg (x : ℝ*) : flatBirthday (-x) = flatBirthday x := by
  simp [flatBirthday, neg_eq_zero]

/-- `1 ≤ flatBirthday x ♯ flatBirthday y` whenever `x` and `y` are not both zero. -/
theorem one_le_nadd_flatBirthday {x y : ℝ*} (h : x ≠ 0 ∨ y ≠ 0) :
    (1 : Ordinal) ≤ Ordinal.nadd (flatBirthday x) (flatBirthday y) := by
  rcases h with hx | hy
  · have : flatBirthday x = 1 := by simp [flatBirthday, hx]
    calc (1 : Ordinal) = flatBirthday x := this.symm
      _ ≤ Ordinal.nadd (flatBirthday x) (flatBirthday y) := Ordinal.le_self_nadd
  · have : flatBirthday y = 1 := by simp [flatBirthday, hy]
    calc (1 : Ordinal) = flatBirthday y := this.symm
      _ ≤ Ordinal.nadd (flatBirthday y) (flatBirthday x) := Ordinal.le_self_nadd
      _ = Ordinal.nadd (flatBirthday x) (flatBirthday y) := Ordinal.nadd_comm _ _

/-- **`birthday_add_le` holds.**  The only case with any content is `x + y ≠ 0`, and
there at least one of `x, y` is nonzero, so the right-hand side is already `≥ 1`. -/
theorem flatBirthday_add_le (x y : ℝ*) :
    flatBirthday (x + y) ≤ Ordinal.nadd (flatBirthday x) (flatBirthday y) := by
  by_cases hxy : x + y = 0
  · rw [hxy, flatBirthday_zero]; exact Ordinal.zero_le _
  · have hne : x ≠ 0 ∨ y ≠ 0 := by
      by_contra hc
      push_neg at hc
      exact hxy (by rw [hc.1, hc.2, add_zero])
    exact (flatBirthday_le_one _).trans (one_le_nadd_flatBirthday hne)

/-- **`birthday_avg_le` holds — and holds vacuously.**

`Basic.lean` documents this axiom as "exactly Conway's `{L | R}` recipe" and as
"genuinely independent of `birthday_add_le`".  Under a birthday bounded by `1` the
right-hand side is `≥ 0 + 1 = 1` no matter what, so the axiom constrains nothing.
That is the sharpest form of the defect: the axiom carrying the most design
commentary in `Basic.lean` is the one this model satisfies with the least effort. -/
theorem flatBirthday_avg_le (x y : ℝ*) :
    flatBirthday ((x + y) / 2)
      ≤ Ordinal.nadd (flatBirthday x) (flatBirthday y) + 1 := by
  refine (flatBirthday_le_one _).trans ?_
  calc (1 : Ordinal) = 0 + 1 := (zero_add 1).symm
    _ ≤ Ordinal.nadd (flatBirthday x) (flatBirthday y) + 1 :=
        add_le_add_right (Ordinal.zero_le _) 1

/-- **`birthday_ofReal_le_omega` holds**, for the same bounded-by-`1` reason. -/
theorem flatBirthday_ofReal_le_omega (r : ℝ) :
    flatBirthday (hyperrealOfReal r) ≤ Ordinal.omega0 :=
  (flatBirthday_le_one _).trans (le_of_lt Ordinal.one_lt_omega0)

theorem omega_gt_natCast (n : ℕ) : (n : ℝ*) < Hyperreal.omega := by
  have h : ((n : ℝ) : ℝ*) < Hyperreal.omega := Hyperreal.infinitePos_omega (n : ℝ)
  exact_mod_cast h

/-- **`ℝ*` is a `SurrealBase`.**  An ordered field extending `ℝ` with `ω` above every
natural number — and nothing about birthdays, so this *is* a global instance: every
`SurrealBase`-generic theorem (infinitesimals, standard part, limit transfer) is true of
`ℝ*`.  Owner ruling 2026-11-27, "Split into base + Conway class". -/
noncomputable instance surrealBaseHyperreal : SurrealBase.{0} ℝ* where
  __ := (inferInstance : Field ℝ*)
  __ := (inferInstance : LinearOrder ℝ*)
  __ := (inferInstance : IsStrictOrderedRing ℝ*)
  ofReal := hyperrealOfReal
  ofReal_strictMono := hyperrealOfReal_strictMono
  omegaSurreal := Hyperreal.omega
  omegaSurreal_gt_natCast := omega_gt_natCast

/-- **The independence witness.**  `ℝ*` with `flatBirthday` satisfies every axiom of
`BirthdayField`, with a birthday that is not Conway's.  This structure is not a
`SurrealField`: its birthday fails both `birthday_natCast` and `simplicity` (`BirthdayFaithful.lean`).

⚠ **`def`, deliberately not `instance`.**  A global instance would make every
`BirthdayField`-generic theorem apply to `ℝ*` under a two-valued birthday. -/
noncomputable def surrealFieldHyperreal : BirthdayField.{0, 0} ℝ* where
  toSurrealBase := surrealBaseHyperreal
  birthday := flatBirthday
  birthday_zero := flatBirthday_zero
  birthday_one := flatBirthday_one
  birthday_neg := flatBirthday_neg
  birthday_add_le := flatBirthday_add_le
  birthday_avg_le := flatBirthday_avg_le
  birthday_ofReal_le_omega := flatBirthday_ofReal_le_omega

/-! ## §3 — `SurrealLimitTransfer ℝ*` under the local instance

Every field below is a Mathlib theorem and **none of them mentions `birthday`**.  That
is the whole point: the conjecture's content is birthday-free, and it was stated over a
carrier that is not. -/

section LocalWitness

/-- `IsClose` at `ℝ*` is exactly Mathlib's `IsSt`.  This is the bridge lemma, and it
is the reason §3 is cheap: `IsInfinitesimal (x - ofReal r)` unfolds to
`∀ ε > 0, |x - r| < ε`, which is `Hyperreal.isSt_iff_abs_sub_lt_delta`. -/
theorem isClose_iff_isSt (x : ℝ*) (r : ℝ) :
    IsClose x (SurrealField.ofReal r) ↔ Hyperreal.IsSt x r := by
  rw [Hyperreal.isSt_iff_abs_sub_lt_delta]
  rfl

/-- **`SurrealLimitTransfer ℝ*`.**  Since 2026-11-27 the class sits on the birthday-free
`SurrealBase`, so this is an honest model of it at `ℝ*`; it says nothing about `𝐍𝐨`,
which is why it stays a `def` (the class remains the conjecture for Conway's numbers). -/
noncomputable def surrealLimitTransferHyperreal : SurrealLimitTransfer ℝ* where
  evalOmega := Hyperreal.ofSeq
  evalOmega_const _ := rfl
  evalOmega_add _ _ := rfl
  evalOmega_mul _ _ := rfl
  evalOmega_le_of_eventuallyLE _ _ h := ofSeq_le_ofSeq_of_eventuallyLE h
  evalOmega_isClose_of_tendstoReal a L h :=
    (isClose_iff_isSt (Hyperreal.ofSeq a) L).2 (isSt_ofSeq_of_tendstoReal h)

end LocalWitness

end QOU.AppendixSurreals.HyperrealTransfer

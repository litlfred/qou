import QOU.Observations.BirthdayFaithful
import QOU.Transcendental.HyperrealLimitTransfer

/-!
# A faithful but non-simple birthday on `ℝ*` (beans `hypr`, `qou-dx7g`)

`HyperrealLimitTransfer.surrealFieldHyperreal` puts a `BirthdayField` structure on `ℝ*`
whose birthday is the two-valued `flatBirthday`. `BirthdayFaithful.lean` adds two
opt-in mixins, `BirthdayFaithful` (`birthday n = n`) and `ConwaySimplicity`, and proves
each independent of the six `BirthdayField` axioms by that flat model.

This module gives a second structure on `ℝ*`, `surrealFieldHyperrealDyadic`, whose
birthday is

* `⌈|r|⌉₊ + e(r)` on a standard dyadic rational `r`, where `e(r)` is the least `k` with
  `r · 2^k ∈ ℤ`;
* `ω` everywhere else (non-dyadic standard reals, and every nonstandard element).

Proved here, sorry-free:

* it satisfies all six `BirthdayField` birthday axioms;
* it **is** `BirthdayFaithful` (`birthday n = n` for every natural `n`);
* it supports `SurrealLimitTransfer ℝ*` (`surrealLimitTransferHyperrealDyadic`), rebasing
  `HyperrealTransfer.surrealLimitTransferHyperreal` off the degenerate two-valued
  `flatBirthday` onto a `BirthdayFaithful` carrier;
* it **fails** `ConwaySimplicity`, at `x = ω`, `z = ω + 1`: both are born on day `ω`,
  and every element born earlier is a standard real lying below both.

Consequence (`birthdayFaithful_not_imp_conwaySimplicity`): **`BirthdayFaithful` does not
imply `ConwaySimplicity`**, even together with the six axioms. A theorem that uses only
`BirthdayFaithful` is therefore still not specific to Conway's birthday.

How close this is to Conway (a remark, not used in any proof): a non-integer dyadic
`x = m/2^k` (reduced, `k ≥ 1`) is born on day `⌊|x|⌋ + 1 + k = ⌈|x|⌉ + k` in Conway's
construction, and an integer `n` on day `|n|`, so on the dyadic rationals this birthday
**is** Conway's. Non-dyadic reals, `ω` and `1/ω` are born on day `ω` in Conway's
construction too. The two differ only on elements Conway gives a birthday above `ω`,
such as `ω + 1`, and that is exactly where simplicity fails below.

⚠ `def`, not `instance`, for the same reason as `surrealFieldHyperreal`: a global
instance would make every `BirthdayField`-generic theorem apply to `ℝ*` silently.
-/

namespace QOU.AppendixSurreals.DyadicBirthday

open scoped Classical

/-! ## §1 — dyadic rationals and their 2-adic exponent, on `ℝ` -/

/-- `r` is a dyadic rational: `r · 2^k` is an integer for some `k`. -/
def IsDyadic (r : ℝ) : Prop := ∃ k : ℕ, ∃ m : ℤ, r * 2 ^ k = m

/-- The least `k` with `r · 2^k ∈ ℤ` (and `0` off the dyadics). -/
noncomputable def dyExp (r : ℝ) : ℕ :=
  if h : IsDyadic r then Nat.find h else 0

theorem dyExp_spec {r : ℝ} (h : IsDyadic r) : ∃ m : ℤ, r * 2 ^ dyExp r = m := by
  rw [dyExp, dif_pos h]; exact Nat.find_spec h

theorem dyExp_le {r : ℝ} {k : ℕ} {m : ℤ} (hk : r * 2 ^ k = m) : dyExp r ≤ k := by
  have h : IsDyadic r := ⟨k, m, hk⟩
  rw [dyExp, dif_pos h]; exact Nat.find_min' h ⟨m, hk⟩

/-- Raising the exponent keeps `r · 2^k` an integer. -/
theorem mul_pow_int_of_le {r : ℝ} {a b : ℕ} {m : ℤ} (hm : r * 2 ^ a = m) (hab : a ≤ b) :
    ∃ n : ℤ, r * 2 ^ b = n := by
  refine ⟨m * 2 ^ (b - a), ?_⟩
  have : (2 : ℝ) ^ b = 2 ^ a * 2 ^ (b - a) := by
    rw [← pow_add, Nat.add_sub_cancel' hab]
  rw [this, ← mul_assoc, hm]; push_cast; ring

/-- `e(r + s) ≤ max (e r) (e s)`, and the sum is dyadic. -/
theorem add_spec {r s : ℝ} (hr : IsDyadic r) (hs : IsDyadic s) :
    ∃ n : ℤ, (r + s) * 2 ^ max (dyExp r) (dyExp s) = n := by
  obtain ⟨m₁, h₁⟩ := dyExp_spec hr
  obtain ⟨m₂, h₂⟩ := dyExp_spec hs
  obtain ⟨n₁, g₁⟩ := mul_pow_int_of_le h₁ (le_max_left (dyExp r) (dyExp s))
  obtain ⟨n₂, g₂⟩ := mul_pow_int_of_le h₂ (le_max_right (dyExp r) (dyExp s))
  exact ⟨n₁ + n₂, by rw [add_mul, g₁, g₂]; push_cast; ring⟩

theorem isDyadic_add {r s : ℝ} (hr : IsDyadic r) (hs : IsDyadic s) : IsDyadic (r + s) :=
  let ⟨n, hn⟩ := add_spec hr hs; ⟨_, n, hn⟩

theorem dyExp_add_le {r s : ℝ} (hr : IsDyadic r) (hs : IsDyadic s) :
    dyExp (r + s) ≤ max (dyExp r) (dyExp s) :=
  let ⟨_, hn⟩ := add_spec hr hs; dyExp_le hn

theorem avg_spec {r s : ℝ} (hr : IsDyadic r) (hs : IsDyadic s) :
    ∃ n : ℤ, ((r + s) / 2) * 2 ^ (max (dyExp r) (dyExp s) + 1) = n := by
  obtain ⟨n, hn⟩ := add_spec hr hs
  exact ⟨n, by rw [pow_succ, ← hn]; field_simp⟩

theorem isDyadic_avg {r s : ℝ} (hr : IsDyadic r) (hs : IsDyadic s) :
    IsDyadic ((r + s) / 2) :=
  let ⟨n, hn⟩ := avg_spec hr hs; ⟨_, n, hn⟩

theorem dyExp_avg_le {r s : ℝ} (hr : IsDyadic r) (hs : IsDyadic s) :
    dyExp ((r + s) / 2) ≤ max (dyExp r) (dyExp s) + 1 :=
  let ⟨_, hn⟩ := avg_spec hr hs; dyExp_le hn

theorem isDyadic_neg {r : ℝ} (hr : IsDyadic r) : IsDyadic (-r) :=
  let ⟨k, m, h⟩ := hr; ⟨k, -m, by rw [neg_mul, h]; push_cast; ring⟩

theorem dyExp_neg (r : ℝ) : dyExp (-r) = dyExp r := by
  by_cases hr : IsDyadic r
  · apply le_antisymm
    · obtain ⟨m, hm⟩ := dyExp_spec hr
      exact dyExp_le (m := -m) (by rw [Int.cast_neg, ← hm]; ring)
    · obtain ⟨m, hm⟩ := dyExp_spec (isDyadic_neg hr)
      exact dyExp_le (m := -m) (by rw [Int.cast_neg, ← hm]; ring)
  · have hnr : ¬ IsDyadic (-r) := fun h => hr (by simpa using isDyadic_neg h)
    rw [dyExp, dif_neg hnr, dyExp, dif_neg hr]

theorem isDyadic_natCast (n : ℕ) : IsDyadic (n : ℝ) := ⟨0, n, by simp⟩

theorem dyExp_natCast (n : ℕ) : dyExp (n : ℝ) = 0 :=
  Nat.le_zero.mp (dyExp_le (k := 0) (m := n) (by simp))

/-! ## §2 — the real-valued day `⌈|r|⌉₊ + e(r)` and its two inequalities -/

/-- The day assigned to a standard dyadic rational. -/
noncomputable def realDay (r : ℝ) : ℕ := ⌈|r|⌉₊ + dyExp r

theorem realDay_add_le {r s : ℝ} (hr : IsDyadic r) (hs : IsDyadic s) :
    realDay (r + s) ≤ realDay r + realDay s := by
  have h1 : ⌈|r + s|⌉₊ ≤ ⌈|r|⌉₊ + ⌈|s|⌉₊ :=
    (Nat.ceil_mono (abs_add_le r s)).trans (Nat.ceil_add_le _ _)
  have h2 := dyExp_add_le hr hs
  have h3 : max (dyExp r) (dyExp s) ≤ dyExp r + dyExp s := max_le_add_of_nonneg
    (Nat.zero_le _) (Nat.zero_le _)
  unfold realDay; omega

theorem realDay_avg_le {r s : ℝ} (hr : IsDyadic r) (hs : IsDyadic s) :
    realDay ((r + s) / 2) ≤ realDay r + realDay s + 1 := by
  have habs : |(r + s) / 2| ≤ |r| + |s| := by
    rw [abs_div, abs_two]
    have := abs_add_le r s
    have h0 : 0 ≤ |r + s| := abs_nonneg _
    linarith
  have h1 : ⌈|(r + s) / 2|⌉₊ ≤ ⌈|r|⌉₊ + ⌈|s|⌉₊ :=
    (Nat.ceil_mono habs).trans (Nat.ceil_add_le _ _)
  have h2 := dyExp_avg_le hr hs
  have h3 : max (dyExp r) (dyExp s) ≤ dyExp r + dyExp s := max_le_add_of_nonneg
    (Nat.zero_le _) (Nat.zero_le _)
  unfold realDay; omega

theorem realDay_neg (r : ℝ) : realDay (-r) = realDay r := by
  simp [realDay, abs_neg, dyExp_neg]

theorem realDay_natCast (n : ℕ) : realDay (n : ℝ) = n := by
  simp [realDay, dyExp_natCast]

/-! ## §3 — the birthday on `ℝ*` -/

/-- `x` is (the image of) a standard dyadic rational. -/
def StdDyadic (x : ℝ*) : Prop := ∃ r : ℝ, (r : ℝ*) = x ∧ IsDyadic r

/-- The dyadic birthday on `ℝ*`: `realDay r` at a standard dyadic `r`, `ω` elsewhere. -/
noncomputable def dyBirthday (x : ℝ*) : Ordinal.{0} :=
  if h : StdDyadic x then ((realDay h.choose : ℕ) : Ordinal) else Ordinal.omega0

theorem dyBirthday_coe {r : ℝ} (hr : IsDyadic r) :
    dyBirthday (r : ℝ*) = ((realDay r : ℕ) : Ordinal) := by
  have h : StdDyadic (r : ℝ*) := ⟨r, rfl, hr⟩
  rw [dyBirthday, dif_pos h]
  have : h.choose = r := Hyperreal.coe_eq_coe.mp h.choose_spec.1
  rw [this]

theorem dyBirthday_of_not {x : ℝ*} (h : ¬ StdDyadic x) : dyBirthday x = Ordinal.omega0 := by
  rw [dyBirthday, dif_neg h]

theorem dyBirthday_le_omega (x : ℝ*) : dyBirthday x ≤ Ordinal.omega0 := by
  by_cases h : StdDyadic x
  · rw [dyBirthday, dif_pos h]; exact (Ordinal.nat_lt_omega0 _).le
  · rw [dyBirthday_of_not h]

/-- Natural sum of two finite days is their sum. -/
theorem nadd_natCast (a b : ℕ) :
    Ordinal.nadd (a : Ordinal) (b : Ordinal) = ((a + b : ℕ) : Ordinal) := by
  rw [Ordinal.nadd_nat]; push_cast; rfl

theorem omega_le_nadd_of_not {x y : ℝ*} (h : ¬ (StdDyadic x ∧ StdDyadic y)) :
    Ordinal.omega0 ≤ Ordinal.nadd (dyBirthday x) (dyBirthday y) := by
  rcases not_and_or.mp h with hx | hy
  · rw [dyBirthday_of_not hx]; exact Ordinal.le_self_nadd
  · rw [dyBirthday_of_not hy]; exact Ordinal.le_nadd_self

theorem dyBirthday_zero : dyBirthday 0 = 0 := by
  have h := dyBirthday_coe (isDyadic_natCast 0)
  rw [realDay_natCast] at h
  simpa using h

theorem dyBirthday_one : dyBirthday 1 = 1 := by
  have h := dyBirthday_coe (isDyadic_natCast 1)
  rw [realDay_natCast] at h
  simpa using h

theorem stdDyadic_neg {x : ℝ*} (h : StdDyadic x) : StdDyadic (-x) :=
  let ⟨r, hr, hd⟩ := h; ⟨-r, by rw [← hr]; push_cast; rfl, isDyadic_neg hd⟩

theorem dyBirthday_neg (x : ℝ*) : dyBirthday (-x) = dyBirthday x := by
  by_cases h : StdDyadic x
  · obtain ⟨r, rfl, hd⟩ := h
    have : (-(r : ℝ*)) = ((-r : ℝ) : ℝ*) := by push_cast; rfl
    rw [this, dyBirthday_coe (isDyadic_neg hd), dyBirthday_coe hd, realDay_neg]
  · have hn : ¬ StdDyadic (-x) := fun hn => h (by simpa using stdDyadic_neg hn)
    rw [dyBirthday_of_not h, dyBirthday_of_not hn]

theorem dyBirthday_add_le (x y : ℝ*) :
    dyBirthday (x + y) ≤ Ordinal.nadd (dyBirthday x) (dyBirthday y) := by
  by_cases h : StdDyadic x ∧ StdDyadic y
  · obtain ⟨⟨r, rfl, hr⟩, ⟨s, rfl, hs⟩⟩ := h
    have : (r : ℝ*) + (s : ℝ*) = ((r + s : ℝ) : ℝ*) := by push_cast; rfl
    rw [this, dyBirthday_coe (isDyadic_add hr hs), dyBirthday_coe hr, dyBirthday_coe hs,
      nadd_natCast]
    exact_mod_cast realDay_add_le hr hs
  · exact (dyBirthday_le_omega _).trans (omega_le_nadd_of_not h)

theorem dyBirthday_avg_le (x y : ℝ*) :
    dyBirthday ((x + y) / 2) ≤ Ordinal.nadd (dyBirthday x) (dyBirthday y) + 1 := by
  by_cases h : StdDyadic x ∧ StdDyadic y
  · obtain ⟨⟨r, rfl, hr⟩, ⟨s, rfl, hs⟩⟩ := h
    have : ((r : ℝ*) + (s : ℝ*)) / 2 = (((r + s) / 2 : ℝ) : ℝ*) := by push_cast; rfl
    rw [this, dyBirthday_coe (isDyadic_avg hr hs), dyBirthday_coe hr, dyBirthday_coe hs,
      nadd_natCast]
    exact_mod_cast realDay_avg_le hr hs
  · exact (dyBirthday_le_omega _).trans
      ((omega_le_nadd_of_not h).trans (Order.le_succ _ |>.trans_eq (Order.succ_eq_add_one _)))

theorem dyBirthday_ofReal_le_omega (r : ℝ) :
    dyBirthday (HyperrealTransfer.hyperrealOfReal r) ≤ Ordinal.omega0 :=
  dyBirthday_le_omega _

/-- **The dyadic structure.** `ℝ*` with the same field, order, `ofReal` and `ω` as
`surrealFieldHyperreal`, and the dyadic birthday. A `def`, not an `instance`. -/
noncomputable def surrealFieldHyperrealDyadic : BirthdayField.{0, 0} ℝ* where
  toSurrealBase := HyperrealTransfer.surrealBaseHyperreal
  birthday := dyBirthday
  birthday_zero := dyBirthday_zero
  birthday_one := dyBirthday_one
  birthday_neg := dyBirthday_neg
  birthday_add_le := dyBirthday_add_le
  birthday_avg_le := dyBirthday_avg_le
  birthday_ofReal_le_omega := dyBirthday_ofReal_le_omega

/-! ## §4 — faithful, and not simple -/

/-- The dyadic birthday gives every natural `n` the day `n`. -/
theorem dyBirthday_natCast (n : ℕ) : dyBirthday ((n : ℕ) : ℝ*) = (n : Ordinal) := by
  have h := dyBirthday_coe (isDyadic_natCast n)
  rw [realDay_natCast] at h
  have hc : (((n : ℝ)) : ℝ*) = ((n : ℕ) : ℝ*) := rfl
  rwa [hc] at h

/-- **`BirthdayFaithful` holds** for the dyadic structure. -/
noncomputable def birthdayFaithfulDyadic :
    @BirthdayFaithful ℝ* surrealFieldHyperrealDyadic :=
  @BirthdayFaithful.mk ℝ* surrealFieldHyperrealDyadic dyBirthday_natCast

/-- A standard real is below `ω` and below `ω + 1`. -/
theorem coe_lt_omega (r : ℝ) : (r : ℝ*) < Hyperreal.omega :=
  Hyperreal.infinitePos_omega r

/-- `ω` is not a standard dyadic (it is not standard at all). -/
theorem not_stdDyadic_omega : ¬ StdDyadic Hyperreal.omega := by
  rintro ⟨r, hr, -⟩
  have := coe_lt_omega r
  rw [hr] at this
  exact lt_irrefl _ this

theorem not_stdDyadic_omega_add_one : ¬ StdDyadic (Hyperreal.omega + 1) := by
  rintro ⟨r, hr, -⟩
  have h := coe_lt_omega (r - 1)
  have : (((r - 1 : ℝ)) : ℝ*) = Hyperreal.omega := by
    push_cast; rw [hr]; ring
  rw [this] at h
  exact lt_irrefl _ h

/-- **The dyadic birthday fails Conway simplicity**, at `x = ω`, `z = ω + 1`. Both are
born on day `ω`; every element born earlier is a standard dyadic, hence below both. -/
theorem dyBirthday_not_simple :
    ¬ (∀ x z : ℝ*, x ≠ z →
        (∀ y : ℝ*, dyBirthday y < dyBirthday x → (y < x ↔ y < z)) →
        dyBirthday x < dyBirthday z) := by
  intro h
  have hne : Hyperreal.omega ≠ Hyperreal.omega + 1 := by
    intro e; have := congrArg (· - Hyperreal.omega) e; simp at this
  have key := h Hyperreal.omega (Hyperreal.omega + 1) hne (by
    intro y hy
    rw [dyBirthday_of_not not_stdDyadic_omega] at hy
    have hstd : StdDyadic y := by
      by_contra hn; rw [dyBirthday_of_not hn] at hy; exact lt_irrefl _ hy
    obtain ⟨r, rfl, -⟩ := hstd
    have h1 := coe_lt_omega r
    have h2 : (r : ℝ*) < Hyperreal.omega + 1 := h1.trans (lt_add_one _)
    exact ⟨fun _ => h2, fun _ => h1⟩)
  rw [dyBirthday_of_not not_stdDyadic_omega,
    dyBirthday_of_not not_stdDyadic_omega_add_one] at key
  exact lt_irrefl _ key

/-- **`BirthdayFaithful` does not imply `ConwaySimplicity`.** One `BirthdayField`
structure on `ℝ*` whose own birthday satisfies the first mixin and fails the second. -/
theorem birthdayFaithful_not_imp_conwaySimplicity :
    ∃ S : BirthdayField.{0, 0} ℝ*,
      (∀ n : ℕ, S.birthday ((n : ℕ) : ℝ*) = (n : Ordinal)) ∧ ¬ @ConwaySimplicity ℝ* S :=
  ⟨surrealFieldHyperrealDyadic, dyBirthday_natCast,
    fun h => dyBirthday_not_simple h.simplicity⟩

/-! ## §5 — `SurrealLimitTransfer ℝ*` rebased onto the faithful dyadic structure (`hypr`) -/

section DyadicLimitTransfer

attribute [local instance] surrealFieldHyperrealDyadic

/-- Under `surrealFieldHyperrealDyadic`, `IsClose` to an embedded standard real `r` is
definitionally Mathlib's `Hyperreal.IsSt`. -/
theorem isClose_iff_isSt_dyadic (x : ℝ*) (r : ℝ) :
    IsClose x (SurrealField.ofReal r) ↔ Hyperreal.IsSt x r := by
  rw [Hyperreal.isSt_iff_abs_sub_lt_delta]
  rfl

/-- **`SurrealLimitTransfer ℝ*` on the `BirthdayFaithful` dyadic structure (`hypr`).**
Rebases `HyperrealTransfer.surrealLimitTransferHyperreal` off the two-valued `flatBirthday`
onto `surrealFieldHyperrealDyadic`. Kept as a `def` (never a global `instance`) per
AGENTS.md Rule 13a so `SurrealLimitTransfer` remains an uninstantiated conjecture class for
Conway's `𝐍𝐨`. -/
noncomputable def surrealLimitTransferHyperrealDyadic : SurrealLimitTransfer ℝ* where
  evalOmega := Hyperreal.ofSeq
  evalOmega_const _ := rfl
  evalOmega_add _ _ := rfl
  evalOmega_mul _ _ := rfl
  evalOmega_le_of_eventuallyLE _ _ h := HyperrealTransfer.ofSeq_le_ofSeq_of_eventuallyLE h
  evalOmega_isClose_of_tendstoReal a L h :=
    (isClose_iff_isSt_dyadic (Hyperreal.ofSeq a) L).2
      (HyperrealTransfer.isSt_ofSeq_of_tendstoReal h)

end DyadicLimitTransfer

/-- **Combined witness on `ℝ*` (`hypr`, `qou-dx7g`).** One `BirthdayField` structure on `ℝ*`
(`surrealFieldHyperrealDyadic`) simultaneously satisfies `BirthdayFaithful` and
`SurrealLimitTransfer` while failing `ConwaySimplicity`. -/
theorem faithful_limitTransfer_not_simple_witnessed :
    ∃ S : BirthdayField.{0, 0} ℝ*,
      Nonempty (@BirthdayFaithful ℝ* S) ∧
        Nonempty (@SurrealLimitTransfer ℝ* S.toSurrealBase) ∧
        ¬ @ConwaySimplicity ℝ* S :=
  ⟨surrealFieldHyperrealDyadic, ⟨birthdayFaithfulDyadic⟩,
    ⟨surrealLimitTransferHyperrealDyadic⟩, fun h => dyBirthday_not_simple h.simplicity⟩

end QOU.AppendixSurreals.DyadicBirthday

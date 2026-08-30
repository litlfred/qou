/-
# The parameter selection: turning an infinite supply of approximations into `Γ_m`'s growth clause

Every other stage of the arc is proved.  What is left is the step that makes Roth's theorem a
statement about *finitely many* solutions rather than a contradiction from assumed data: given
infinitely many good rational approximations to `α`, choose `m` of them whose heights grow fast
enough that `Γ_m`'s clauses hold.

## Why this is the piece that is not bookkeeping

Everything else in the arc composes hypotheses that a caller supplies.  This one *constructs* the
data, and it is the only place where the hypothesis "infinitely many solutions" is consumed.  The
construction is a recursion — pick a denominator past a threshold, raise it to a power, pick
another past *that* — and the recursion is where the "sufficiently large" in the informal proof
actually lives.

## The shape `Γ_m` wants

`rothGammaFull_of_heights` asks for `H j ^ (2q) ≤ H k ^ p` on consecutive indices.  Choosing the
next height beyond `H j ^ (2q)` gives `H j ^ (2q) ≤ H k`, and `H k ≤ H k ^ p` because `p ≥ 1` and
`H k ≥ 2` — so the growth function to iterate is exactly `x ↦ x ^ (2q)`, with the floor `2` carried
along to keep `two_le` true.  The `max` in `growSeq` is what carries it: without it the second
height could be chosen below the floor whenever `f` happened to return something small, and
`two_le` would fail on every index but the first.

## What this does not do

It selects heights and proves the growth clause.  It does not choose `ε`, `δ`, `m` or the degrees
— `rothDegrees` already determines the degrees from the heights, and `slack_pos` already says what
`ε`, `δ` and `m` must satisfy.  Assembling those choices with this selection into the final
statement is the remaining step.
-/
import QOU.Mathlib.RothGammaProducer

namespace MvPolynomial

section Selection

variable {S : Set ℕ}

/-- **The greedy fast-growing selection.**  Each term is chosen from the supply beyond both the
floor `N₀` and the growth function applied to its predecessor. -/
noncomputable def growSeq (hS : ∀ N, ∃ q ∈ S, N ≤ q) (f : ℕ → ℕ) (N₀ : ℕ) : ℕ → ℕ
  | 0 => Classical.choose (hS N₀)
  | (n + 1) => Classical.choose (hS (max N₀ (f (growSeq hS f N₀ n))))

theorem growSeq_mem (hS : ∀ N, ∃ q ∈ S, N ≤ q) (f : ℕ → ℕ) (N₀ : ℕ) :
    ∀ n, growSeq hS f N₀ n ∈ S
  | 0 => (Classical.choose_spec (hS N₀)).1
  | (n + 1) => (Classical.choose_spec (hS (max N₀ (f (growSeq hS f N₀ n))))).1

/-- The floor is respected at every index — this is what keeps `Γ_m`'s `two_le` clause true past
the first term. -/
theorem le_growSeq (hS : ∀ N, ∃ q ∈ S, N ≤ q) (f : ℕ → ℕ) (N₀ : ℕ) :
    ∀ n, N₀ ≤ growSeq hS f N₀ n
  | 0 => (Classical.choose_spec (hS N₀)).2
  | (n + 1) =>
      le_trans (le_max_left N₀ (f (growSeq hS f N₀ n)))
        (Classical.choose_spec (hS (max N₀ (f (growSeq hS f N₀ n))))).2

/-- Each term outruns the growth function applied to its predecessor. -/
theorem growSeq_succ (hS : ∀ N, ∃ q ∈ S, N ≤ q) (f : ℕ → ℕ) (N₀ : ℕ) (n : ℕ) :
    f (growSeq hS f N₀ n) ≤ growSeq hS f N₀ (n + 1) :=
  le_trans (le_max_right N₀ (f (growSeq hS f N₀ n)))
    (Classical.choose_spec (hS (max N₀ (f (growSeq hS f N₀ n))))).2

/-- **The greedy sequence is monotone.**  Each term is at least its predecessor's `k`-th power,
and the floor keeps every term at least `1`, so a `k ≥ 1` growth function cannot decrease.

Needed because `sum_rothDegrees_le` bounds `Σ r_h` using the *smallest* height, and "smallest"
is only `H₀` if the heights increase. -/
theorem growSeq_mono (hS : ∀ N, ∃ q ∈ S, N ≤ q) {k : ℕ} (hk : 1 ≤ k) {N₀ : ℕ} (hN₀ : 1 ≤ N₀) :
    Monotone (growSeq hS (fun x => x ^ k) N₀) := by
  refine monotone_nat_of_le_succ (fun n => ?_)
  have h1 : 1 ≤ growSeq hS (fun x => x ^ k) N₀ n := le_trans hN₀ (le_growSeq hS _ N₀ n)
  have h2 : growSeq hS (fun x => x ^ k) N₀ n ≤ (growSeq hS (fun x => x ^ k) N₀ n) ^ k :=
    Nat.le_self_pow (by omega) _
  exact le_trans h2 (growSeq_succ hS (fun x => x ^ k) N₀ n)

/-- **Two of `Γ_m`'s clauses, from an unbounded supply.**  Given infinitely many admissible
heights, `m` of them can be chosen from the supply, all beyond an arbitrary floor `N₀`, with
`H j ^ (2q) ≤ H k ^ p` on consecutive indices.

That is `rothGammaFull_of_heights`'s `hgrow` and `hH` at once — and taking `N₀ := 2 ^ F` also gives
its `floor` clause, which is why the floor is a parameter rather than the constant `2`.  Clause 3
is the one that bites hardest (`RothRealLadder`'s witness needed `H = 1024` at `m = 2` because of
it), so having it fall out of the same construction is worth the generality. -/
theorem exists_heights_growing (hS : ∀ N, ∃ q ∈ S, N ≤ q) (m p q : ℕ) (hp : 0 < p) (hq : 0 < q)
    (N₀ : ℕ) (hN₀ : 2 ≤ N₀) :
    ∃ H : Fin m → ℕ, (∀ h, H h ∈ S) ∧ (∀ h, N₀ ≤ H h) ∧ (∀ h, 2 ≤ H h) ∧
      (∀ j k : Fin m, (j : ℕ) ≤ (k : ℕ) → H j ≤ H k) ∧
      ∀ j k : Fin m, (j : ℕ) + 1 = (k : ℕ) → H j ^ (2 * q) ≤ H k ^ p := by
  classical
  refine ⟨fun h => growSeq hS (fun x => x ^ (2 * q)) N₀ (h : ℕ),
    fun h => growSeq_mem hS _ N₀ _, fun h => le_growSeq hS _ N₀ _,
    fun h => le_trans hN₀ (le_growSeq hS _ N₀ _),
    fun j k hjk => growSeq_mono hS (by omega) (by omega) hjk, fun j k hjk => ?_⟩
  have hstep : (growSeq hS (fun x => x ^ (2 * q)) N₀ (j : ℕ)) ^ (2 * q)
      ≤ growSeq hS (fun x => x ^ (2 * q)) N₀ ((j : ℕ) + 1) :=
    growSeq_succ hS (fun x => x ^ (2 * q)) N₀ (j : ℕ)
  rw [hjk] at hstep
  refine le_trans hstep ?_
  exact Nat.le_self_pow hp.ne' _

/-- **The floor clause too.**  At `N₀ = 2 ^ F` the selected heights also satisfy
`rothGammaFull_of_heights`'s `hfloor`. -/
theorem exists_heights_growing_floor (hS : ∀ N, ∃ q ∈ S, N ≤ q) (m p q F : ℕ) (hp : 0 < p)
    (hq : 0 < q) (T : ℕ) (hF : 1 ≤ F) :
    ∃ H : Fin m → ℕ, (∀ h, H h ∈ S) ∧ (∀ h, 2 ≤ H h) ∧
      (∀ h, T ≤ H h) ∧
      (∀ j : Fin m, (j : ℕ) = 0 → (2 : ℤ) ^ F ≤ (H j : ℤ)) ∧
      (∀ j k : Fin m, (j : ℕ) ≤ (k : ℕ) → H j ≤ H k) ∧
      ∀ j k : Fin m, (j : ℕ) + 1 = (k : ℕ) → H j ^ (2 * q) ≤ H k ^ p := by
  have h2F : 2 ≤ max (2 ^ F) T := by
    refine le_trans ?_ (le_max_left _ _)
    calc (2 : ℕ) = 2 ^ 1 := (pow_one 2).symm
      _ ≤ 2 ^ F := Nat.pow_le_pow_right (by norm_num) hF
  obtain ⟨H, hmem, hfloor, h2, hmono, hgrow⟩ :=
    exists_heights_growing hS m p q hp hq (max (2 ^ F) T) h2F
  refine ⟨H, hmem, h2, fun h => le_trans (le_max_right _ _) (hfloor h), fun j _ => ?_,
    hmono, hgrow⟩
  have := le_trans (le_max_left (2 ^ F) T) (hfloor j)
  exact_mod_cast this

end Selection

section Degrees

/-! ## `N` after the heights: `Γ_m`'s `hlarge`

The dependency runs one way.  `hlarge` constrains `N` *relative to the already-chosen heights*, so
it is discharged after the selection, not before — and there is no circularity in it at all.
`hbound` is the one that looks circular; see the bean.
-/

/-- **`N` large relative to the heights gives `Γ_m`'s `hlarge`.**  `(H h)^{p+2q} ≤ N` for every
`h` is the whole condition, and `p ≥ 1` does the rest. -/
theorem hlarge_of_pow_le {m : ℕ} (H : Fin m → ℕ) (N : ℕ) (hN : N ≠ 0) (hH : ∀ h, 2 ≤ H h)
    (p q : ℕ) (hp : 0 < p) (hpow : ∀ h, (H h) ^ (p + 2 * q) ≤ N) :
    ∀ h : Fin m, p + 2 * q ≤ p * rothDegrees H N h := by
  intro h
  have hb : 1 < H h := lt_of_lt_of_le one_lt_two (hH h)
  have hlog : p + 2 * q ≤ Nat.log (H h) N := (Nat.le_log_iff_pow_le hb hN).mpr (hpow h)
  have hd : Nat.log (H h) N ≤ rothDegrees H N h := by
    rw [rothDegrees]
    split_ifs
    · exact le_rfl
    · exact Nat.le_succ _
  calc p + 2 * q ≤ Nat.log (H h) N := hlog
    _ ≤ rothDegrees H N h := hd
    _ = 1 * rothDegrees H N h := (one_mul _).symm
    _ ≤ p * rothDegrees H N h := Nat.mul_le_mul_right _ hp

/-- **And such an `N` exists.**  Constructed from the heights, which is the point: the order is
heights → `N` → degrees, never the other way. -/
theorem exists_pow_le {m : ℕ} (H : Fin m → ℕ) (hH : ∀ h, 2 ≤ H h) (k : ℕ) :
    ∃ N : ℕ, N ≠ 0 ∧ ∀ h, (H h) ^ k ≤ N := by
  classical
  have hpos : ∀ h : Fin m, 1 ≤ H h := fun h => le_trans one_le_two (hH h)
  refine ⟨(∏ h, H h) ^ k, pow_ne_zero _ ?_, fun h => ?_⟩
  · exact Finset.prod_ne_zero_iff.mpr (fun h _ => by have := hH h; omega)
  · exact Nat.pow_le_pow_left
      (Finset.single_le_prod' (fun i _ => hpos i) (Finset.mem_univ h)) k

/-! ## Is `hbound` circular?  No — and this is the lemma that says why

`Γ_m`'s last clause is `b ^ (m q) ≤ H₀ ^ (r₀ p)` where `b` is the auxiliary polynomial's height
bound, `⌈siegelHeight r α μ⌉`.  It reads as circular: `b` depends on `r`, `r = rothDegrees H N`
depends on `H₀`, and `H₀` is what the clause constrains.

It is not, and the reason is a *cancellation*.  Note first, from the types, that
`siegelHeight r α μ` depends on `H` **only through `r`** — so raising `H₀` while holding `r` fixed
leaves `b` alone and raises the right-hand side, which is `hbound_mono` below.  That is the move
the informal proof makes when it says "choose `q₁` large".

Holding `r` fixed while raising `H₀` means raising `N` too, and the asymptotics are what make it
work.  Writing `log` for real logarithms: `r₀·log H₀ ≈ log N`, so the right side is `≈ p·log N`.
On the left, `log b ≈ ρ·log(#box · ‖A‖)` with `ρ = #E/(#box − #E)`, and both `#box` and `‖A‖` grow
like `exp(c·∑_h r_h)` while `∑_h r_h ≈ log N · ∑_h 1/log H_h`.  So the left side is
`≈ m q ρ c · log N · ∑_h 1/log H_h`, **`log N` cancels**, and since the growth clause makes `H₀`
the smallest height, `∑_h 1/log H_h ≤ m/log H₀`.  The clause reduces to a condition on `H₀`
alone: `log H₀ ≳ m² q ρ c / p`.

⚠ That cancellation is an asymptotic argument, not yet formalised.  `hbound_mono` is the part that
is, and it is the part the non-circularity actually rests on; the rest is an estimate on `#box`
and `‖A‖` that this arc has not written down.  Recorded so the gap is visible rather than implied
by the surrounding lemmas being proved.
-/

/-- **Raising `H j` never hurts `Γ_m`'s height clause**, with the degrees held fixed.  This is the
formal content of "choose `q₁` large": the clause is monotone in the height, and `b` does not move
when `r` does not.

No sign condition on `b` is needed — I wrote `0 ≤ b` and the linter reported it unused, which is
right: only the *base* `H j` has to be non-negative, and it is a natural number.  The stronger
statement is kept. -/
theorem hbound_mono {m : ℕ} {b : ℤ} (H H' : Fin m → ℕ) (d : Fin m → ℕ) (p q : ℕ)
    (j : Fin m) (hle : H j ≤ H' j)
    (h : b ^ (m * q) ≤ (H j : ℤ) ^ (d j * p)) :
    b ^ (m * q) ≤ (H' j : ℤ) ^ (d j * p) := by
  refine le_trans h (pow_le_pow_left₀ (Int.natCast_nonneg _) ?_ _)
  exact_mod_cast hle

end Degrees

section Assembly

/-! ## The selection assembled: four of `Γ_m`'s six inputs, from the supply alone

`rothGammaFull_of_heights` takes six inputs.  Two are free of the selection — `hfloorExp` is a
numeric condition on `F` alone, and `hbound` is the height clause the previous section analysed.
The other four all come from the supply, and `exists_heights_and_N` produces them together with
the data they are about.

The order is forced and is the content: heights first (the growth recursion), then `N` from the
heights, then the degrees from both.  Nothing here can be reordered.
-/

/-- **The data, and four of `Γ_m`'s inputs.**  From an unbounded supply of admissible heights:
`m` of them, a threshold `N`, and the growth, floor, `two_le` and `hlarge` clauses. -/
theorem exists_heights_and_N {S : Set ℕ} (hS : ∀ N, ∃ q ∈ S, N ≤ q) (m p q F : ℕ)
    (hp : 0 < p) (hq : 0 < q) (T k : ℕ) (hF : 1 ≤ F) :
    ∃ (H : Fin m → ℕ) (N : ℕ), (∀ h, H h ∈ S) ∧ (∀ h, 2 ≤ H h) ∧ N ≠ 0 ∧ (∀ h, T ≤ H h) ∧
      (∀ j : Fin m, (j : ℕ) = 0 → (2 : ℤ) ^ F ≤ (H j : ℤ)) ∧
      (∀ j k : Fin m, (j : ℕ) ≤ (k : ℕ) → H j ≤ H k) ∧
      (∀ j k : Fin m, (j : ℕ) + 1 = (k : ℕ) → H j ^ (2 * q) ≤ H k ^ p) ∧
      (∀ h : Fin m, p + 2 * q ≤ p * rothDegrees H N h) ∧
      (∀ h : Fin m, (H h) ^ k ≤ N) := by
  obtain ⟨H, hmem, h2, hT, hfloor, hmono, hgrow⟩ :=
    exists_heights_growing_floor hS m p q F hp hq T hF
  obtain ⟨N, hN, hpow⟩ := exists_pow_le H h2 (max (p + 2 * q) k)
  have hH1 : ∀ h : Fin m, 1 ≤ H h := fun h => le_trans one_le_two (h2 h)
  have hp2q : ∀ h, (H h) ^ (p + 2 * q) ≤ N := fun h =>
    le_trans (Nat.pow_le_pow_right (hH1 h) (le_max_left _ _)) (hpow h)
  have hk : ∀ h, (H h) ^ k ≤ N := fun h =>
    le_trans (Nat.pow_le_pow_right (hH1 h) (le_max_right _ _)) (hpow h)
  exact ⟨H, N, hmem, h2, hN, hT, hfloor, hmono, hgrow,
    hlarge_of_pow_le H N hN h2 p q hp hp2q, hk⟩

/-- **`Γ_m` from the supply, modulo the height clause.**  There are heights in the supply and a
threshold `N` such that *if* the auxiliary polynomial's height bound `b` satisfies `Γ_m`'s last
clause for them, then all seven clauses hold.

The implication is the honest shape.  `hbound` is a statement *about the produced data*, so it
cannot be a hypothesis of the existential — and quantifying it over all possible `H`, `N` would
demand far more than the argument needs.  `hbound_mono` is what makes the implication
dischargeable: the clause improves as `H₀` grows, and the supply is unbounded.

⚠ `b` is a **function** of the produced data, not a constant.  It was a constant in the first
draft, and that version cannot be used: the `b` this is actually applied at is
`⌈siegelHeight (rothDegrees H N) α μ⌉`, which depends on the `H` and `N` the theorem itself
produces.  A constant `b` cannot be instantiated with it, so the "honest shape" was still the
wrong one — honest about `hbound` and wrong about `b`. -/
theorem exists_rothGammaFull_of_supply {S : Set ℕ} (hS : ∀ N, ∃ q ∈ S, N ≤ q)
    (m p q F : ℕ) (bOf : (Fin m → ℕ) → ℕ → ℤ) (hp : 0 < p) (hq : 0 < q) (T k : ℕ) (hF : 1 ≤ F)
    (hfloorExp : q * ((m - 1) * m * (2 * m + 1)) ≤ F * p) :
    ∃ (H : Fin m → ℕ) (N : ℕ), (∀ h, H h ∈ S) ∧ N ≠ 0 ∧ (∀ h, 2 ≤ H h) ∧ (∀ h, T ≤ H h) ∧
      (∀ j k : Fin m, (j : ℕ) ≤ (k : ℕ) → H j ≤ H k) ∧
      (∀ h : Fin m, p + 2 * q ≤ p * rothDegrees H N h) ∧
      (∀ h : Fin m, (H h) ^ k ≤ N) ∧
      ((∀ j : Fin m, (j : ℕ) = 0 →
          (bOf H N) ^ (m * q) ≤ (H j : ℤ) ^ (rothDegrees H N j * p)) →
        RothGammaFull (Equiv.refl (Fin m)) p q F (rothDegrees H N)
          (fun j => (H j : ℤ)) (bOf H N)) := by
  obtain ⟨H, N, hmem, h2, hN, hT, hfloor, hmono, hgrow, hlarge, hk⟩ :=
    exists_heights_and_N hS m p q F hp hq T k hF
  exact ⟨H, N, hmem, hN, h2, hT, hmono, hlarge, hk, fun hbound =>
    rothGammaFull_of_heights H hp hN h2 hgrow hlarge hfloorExp hfloor hbound⟩

/-- **The selection machinery is applicable.**  Every hypothesis of
`exists_rothGammaFull_of_supply` is discharged at `m = 2`, `p = q = 1`, `F = 10`, `b = 1` — the
parameters `RothRealLadder`'s own witness uses — over the unbounded supply `Set.univ`.

`hfloorExp` is the clause that pins `F`: at `m = 2` it reads `1·(1·2·5) ≤ F·1`, so `F = 10` is the
smallest that works, which is the same arithmetic that forced `H = 1024` in the earlier witness.
The two are the same constraint seen from opposite ends. -/
theorem exists_rothGammaFull_of_supply_witness :
    ∃ (H : Fin 2 → ℕ) (N : ℕ), (∀ h, H h ∈ (Set.univ : Set ℕ)) ∧ N ≠ 0 ∧ (∀ h, 2 ≤ H h) ∧
      (∀ h, 5 ≤ H h) ∧
      (∀ j k : Fin 2, (j : ℕ) ≤ (k : ℕ) → H j ≤ H k) ∧
      (∀ h : Fin 2, 1 + 2 * 1 ≤ 1 * rothDegrees H N h) ∧
      (∀ h : Fin 2, (H h) ^ 7 ≤ N) ∧
      ((∀ j : Fin 2, (j : ℕ) = 0 →
          (1 : ℤ) ^ (2 * 1) ≤ (H j : ℤ) ^ (rothDegrees H N j * 1)) →
        RothGammaFull (Equiv.refl (Fin 2)) 1 1 10 (rothDegrees H N)
          (fun j => (H j : ℤ)) 1) :=
  exists_rothGammaFull_of_supply (S := (Set.univ : Set ℕ))
    (fun N => ⟨N, Set.mem_univ N, le_rfl⟩) 2 1 1 10 (fun _ _ => 1) one_pos one_pos 5 7
    (by norm_num) (by norm_num)

/-- **`Σ r_h` in terms of the smallest height.**  `Σ_h rothDegrees H N h ≤ m·(log_b N + 1)` for any
`b` below every height — because `Nat.log` is antitone in its base, so the smallest height gives
the largest degree.

This is the concrete form of the asymptotic `Σ r_h ≈ log N · Σ_h 1/log H_h ≤ m·log N/log H₀` that
`hbound`'s cancellation runs on: it puts `Σ r_h` under `m·log_{H₀} N`, so the left side of the
height clause grows like `N^{c·m/log H₀}` against a right side of `N^p`. -/
theorem sum_rothDegrees_le {m : ℕ} (H : Fin m → ℕ) (N b : ℕ) (hb : 1 < b)
    (hle : ∀ h, b ≤ H h) :
    ∑ h, rothDegrees H N h ≤ m * (Nat.log b N + 1) := by
  classical
  calc ∑ h, rothDegrees H N h ≤ ∑ _h : Fin m, (Nat.log b N + 1) := by
        refine Finset.sum_le_sum (fun h _ => ?_)
        have hstep : Nat.log (H h) N ≤ Nat.log b N := Nat.log_anti_left hb (hle h)
        rw [rothDegrees]
        split_ifs
        · omega
        · omega
    _ = m * (Nat.log b N + 1) := by
        rw [Finset.sum_const, Finset.card_univ, Fintype.card_fin, smul_eq_mul]

end Assembly

end MvPolynomial

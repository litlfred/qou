import Mathlib.Tactic
import QOU.BraidKnot.BraidGroupNStrand

set_option autoImplicit false

/-!
# QOU.Knot.BraidClosure — the closure permutation and its component count

Bean `qou-e6db`, step 1. `QOU.Knot.MFWSkeinInduction` states the MFW window in
terms of three integers: the strand count `n`, the writhe `e`, and the number of
**closure components** `c`. Of those, `n` and `e` already existed
(`QOU.BraidKnot.BraidWord.writhe`); `c` did not exist anywhere in the tree, so
nothing could connect a braid word to the window it is supposed to satisfy.

This file supplies it. A braid word induces a permutation of the strand
endpoints — each crossing swaps two adjacent positions, regardless of its sign —
and the closure's components are exactly that permutation's orbits.

**Built on the existing type, deliberately.** `BraidWord` is defined **nine
times** across this Lean tree (`PhotonThreading`, four separate `StandardModel`
files, two `Archimedean` files, `BraidKnot.BraidGroupNStrand`,
`BraidKnot.BraidWordBasisGram`, and `KnotTheory`), with `writhe` defined at
least five times — four of them character-identical. A tenth definition would
make that worse. `BraidKnot.BraidGroupNStrand.BraidWord` is used here because it
is the only one indexed by the strand count `n` and carrying the crossing sign,
which is precisely what MFW needs. The fragmentation is recorded in `qou-e6db`;
it is an obstacle to HOMFLY-in-Lean, not something this file fixes.
-/

namespace QOU.Knot.BraidClosure

open QOU.BraidKnot

variable {n : ℕ}

/-- The lower of the two strand positions a generator `σ_i` acts on. -/
def loIdx (i : Fin (n - 1)) : Fin n := ⟨i.val, by have := i.isLt; omega⟩

/-- The upper of the two strand positions a generator `σ_i` acts on. -/
def hiIdx (i : Fin (n - 1)) : Fin n := ⟨i.val + 1, by have := i.isLt; omega⟩

theorem loIdx_ne_hiIdx (i : Fin (n - 1)) : loIdx i ≠ hiIdx i := by
  simp [loIdx, hiIdx, Fin.ext_iff]

/-- The transposition a crossing induces on strand positions.

**The sign is irrelevant here** — `σ_i` and `σ_i⁻¹` cross the same two strands
and so induce the same permutation. That is why the closure component count `c`
is insensitive to crossing changes, which is exactly what makes it a usable
invariant in the skein induction: switching a crossing moves `e` but fixes `c`.
-/
def crossingSwap (c : BraidCrossing n) : Equiv.Perm (Fin n) :=
  Equiv.swap (loIdx c.gen) (hiIdx c.gen)

/-- The permutation of strand endpoints induced by a braid word. Its orbits are
the components of the Markov closure. -/
def closurePerm : BraidWord n → Equiv.Perm (Fin n)
  | [] => 1
  | c :: w => crossingSwap c * closurePerm w

@[simp] theorem closurePerm_nil : closurePerm ([] : BraidWord n) = 1 := rfl

@[simp] theorem closurePerm_cons (c : BraidCrossing n) (w : BraidWord n) :
    closurePerm (c :: w) = crossingSwap c * closurePerm w := rfl

theorem closurePerm_append (v w : BraidWord n) :
    closurePerm (v ++ w) = closurePerm v * closurePerm w := by
  induction v with
  | nil => simp
  | cons c v ih => simp [ih, mul_assoc]

/-- The writhe is additive over concatenation — the other half of what the
skein induction needs, since stacking braids adds their crossing signs. -/
theorem writhe_append (v w : BraidWord n) :
    BraidWord.writhe (v ++ w) = BraidWord.writhe v + BraidWord.writhe w := by
  induction v with
  | nil => simp
  | cons c v ih => simp [ih]; ring

/-- **The number of closure components.** Orbits of `closurePerm`: each
nontrivial cycle is one component, and each fixed point is a component of its
own (a strand that closes up alone). -/
noncomputable def components (w : BraidWord n) : ℕ :=
  (closurePerm w).cycleType.card + (n - (closurePerm w).support.card)

/-- The identity braid closes to `n` disjoint circles — the `n`-component
unlink. This is the `c = n` corner the window arithmetic pins down. -/
@[simp] theorem components_nil : components ([] : BraidWord n) = n := by
  simp [components]

/-- **The base corner, connected.** For the empty word the writhe is `0` and the
component count is `n`, so `MFWSkeinInduction.DescendingWrithe n c e` holds with
`c = n`, `e = 0` — matching `descending_trivial_perm_writhe_zero`, which
previously had no braid word to be about. -/
theorem descendingWrithe_nil :
    BraidWord.writhe ([] : BraidWord n) = 0 ∧
      components ([] : BraidWord n) = n := by
  constructor
  · simp
  · simp

/-! ### Non-vacuity: the definitions compute the right numbers

A definition that type-checks can still be wrong. These pin `closurePerm` and
`components` to cases whose answers are known independently. -/

/-- On two strands there is only one generator, so any crossing swaps `0` and
`1`. (`Fin (2 - 1)` needs the subtraction reduced by hand — instance search will
not find `Subsingleton` through it.) -/
theorem closurePerm_two (c : BraidCrossing 2) :
    closurePerm [c] = Equiv.swap (0 : Fin 2) 1 := by
  -- `c.gen : Fin (2 - 1)`, so `simp` already knows its value is `0`; no
  -- separate `c.gen.val = 0` hypothesis is needed.
  have h0 : loIdx c.gen = (0 : Fin 2) := by apply Fin.ext; simp [loIdx]
  have h1 : hiIdx c.gen = (1 : Fin 2) := by apply Fin.ext; simp [hiIdx]
  simp [closurePerm, crossingSwap, h0, h1]

/-- **One crossing on two strands closes to the unknot: `c = 1`, not 2.** The
two strands are joined into a single circle. This is the smallest case where
`components` could have been off by one, and it is not. -/
theorem components_two_one_crossing (c : BraidCrossing 2) :
    components [c] = 1 := by
  have hne : (0 : Fin 2) ≠ 1 := by decide
  have hcyc : (Equiv.swap (0 : Fin 2) 1).cycleType
      = {(Equiv.swap (0 : Fin 2) 1).support.card} :=
    (Equiv.Perm.isCycle_swap hne).cycleType
  simp [components, closurePerm_two c, hcyc]

/-- Two crossings on two strands cancel in the *permutation* (though not in the
writhe), so the closure has two components again — the 2-component unlink.
Together with the previous lemma this shows `components` tracks the parity of
the crossing count, as it must. -/
theorem components_two_two_crossings (c d : BraidCrossing 2) :
    components [c, d] = 2 := by
  have hcd : c.gen = d.gen := by
    have h1 := c.gen.isLt
    have h2 := d.gen.isLt
    apply Fin.ext
    omega
  have hone : closurePerm [c, d] = 1 := by
    simp [closurePerm, crossingSwap, hcd, Equiv.swap_mul_self]
  simp [components, hone]

/-! ### The skein moves, on actual braid words

`MFWSkeinInduction.mfw_step` takes the window shifts as arithmetic hypotheses:
switching moves `e ↦ e - 2`, smoothing moves `e ↦ e - 1`, and both keep `n`.
Nothing so far proved that a braid word *realises* those shifts, nor that `c`
behaves as the induction needs. These lemmas supply exactly that. -/

/-- Flip a crossing's sign — the skein "switch". -/
def flipSign (c : BraidCrossing n) : BraidCrossing n :=
  { c with positive := !c.positive }

@[simp] theorem crossingSwap_flipSign (c : BraidCrossing n) :
    crossingSwap (flipSign c) = crossingSwap c := rfl

/-- **Switching a crossing does not move the permutation** — hence not `c`
either. This is the half of the skein step that makes the induction work: `e`
moves while `c` and `n` stay put, so the window slides without changing width. -/
theorem closurePerm_switch (v w : BraidWord n) (c : BraidCrossing n) :
    closurePerm (v ++ flipSign c :: w) = closurePerm (v ++ c :: w) := by
  simp [closurePerm_append]

theorem components_switch (v w : BraidWord n) (c : BraidCrossing n) :
    components (v ++ flipSign c :: w) = components (v ++ c :: w) := by
  simp [components, closurePerm_switch]

/-- **Switching moves the writhe by exactly 2**, in the direction set by the
crossing's original sign — the `e ↦ e - 2` of `mfw_step`. -/
theorem writhe_switch (v w : BraidWord n) (c : BraidCrossing n) :
    BraidWord.writhe (v ++ flipSign c :: w)
      = BraidWord.writhe (v ++ c :: w) - 2 * (if c.positive then 1 else -1) := by
  simp only [writhe_append, BraidWord.writhe_cons, flipSign]
  cases hc : c.positive <;> simp <;> ring

/-- **Smoothing removes the crossing**, so the permutation loses exactly that
transposition. Since multiplying by a transposition changes the orbit count by
one, this is where `c` moves — the other half of the skein step. -/
theorem closurePerm_smooth (v w : BraidWord n) (c : BraidCrossing n) :
    closurePerm (v ++ c :: w)
      = closurePerm v * crossingSwap c * closurePerm w := by
  simp [closurePerm_append, mul_assoc]

/-- **Smoothing moves the writhe by exactly 1** — the `e ↦ e - 1` of
`mfw_step`. -/
theorem writhe_smooth (v w : BraidWord n) (c : BraidCrossing n) :
    BraidWord.writhe (v ++ c :: w)
      = BraidWord.writhe (v ++ w) + (if c.positive then 1 else -1) := by
  simp only [writhe_append, BraidWord.writhe_cons]
  ring

/-! ### Parity — why `|e| ≤ n - c` is a *same-parity* statement

The exhaustive measurement behind `MFWSkeinInduction`'s base case found `|e|` and
`n - c` always sharing a parity, with the bound tight whenever they agree. That
is not a coincidence of small cases: it follows from the sign homomorphism,
because each crossing contributes exactly one transposition. -/

/-- **The closure permutation's sign is `(-1)` to the crossing count.** Each
crossing is one transposition, whatever its sign — the same sign-blindness that
makes `c` invariant under switching. -/
theorem sign_closurePerm (w : BraidWord n) :
    Equiv.Perm.sign (closurePerm w) = (-1) ^ w.length := by
  induction w with
  | nil => simp
  | cons c w ih =>
      rw [closurePerm_cons, map_mul, ih, crossingSwap,
          Equiv.Perm.sign_swap (loIdx_ne_hiIdx c.gen), List.length_cons,
          pow_succ]
      exact (mul_comm _ _)

/-- The crossing count and the cycle data agree in parity — the sign identity
read through `Equiv.Perm.sign_of_cycleType`. Since `cycleType.sum` is the
support size and `cycleType.card` the number of nontrivial cycles, this is the
parity half of "one transposition changes the orbit count by one". -/
theorem length_parity_cycleType (w : BraidWord n) :
    (-1 : ℤˣ) ^ w.length
      = (-1) ^ ((closurePerm w).cycleType.sum
          + (closurePerm w).cycleType.card) := by
  rw [← sign_closurePerm, Equiv.Perm.sign_of_cycleType]

/-- **The writhe has the parity of the crossing count** — each crossing
contributes `±1`, and both are odd. -/
theorem writhe_sub_length_even (w : BraidWord n) :
    Even (BraidWord.writhe w - (w.length : ℤ)) := by
  induction w with
  | nil => simp
  | cons c w ih =>
      obtain ⟨k, hk⟩ := ih
      refine ⟨k + (if c.positive then 0 else -1), ?_⟩
      rw [BraidWord.writhe_cons, List.length_cons]
      push_cast
      cases c.positive <;> simp_all <;> linarith

/-- `(-1)^a = (-1)^b` in `ℤˣ` forces `a` and `b` to share a parity. -/
private theorem neg_one_pow_parity {a b : ℕ} (h : (-1 : ℤˣ) ^ a = (-1) ^ b) :
    a % 2 = b % 2 := by
  rcases Nat.even_or_odd a with ha | ha <;> rcases Nat.even_or_odd b with hb | hb
  · rw [Nat.even_iff.mp ha, Nat.even_iff.mp hb]
  · rw [ha.neg_one_pow, hb.neg_one_pow] at h; exact absurd h (by decide)
  · rw [ha.neg_one_pow, hb.neg_one_pow] at h; exact absurd h (by decide)
  · rw [Nat.odd_iff.mp ha, Nat.odd_iff.mp hb]

/-- **The writhe's parity is fixed by the closure permutation's cycle data.**

This is the parity constraint that makes `|e| ≤ n - c` a *same-parity, smaller
magnitude* statement rather than a bare inequality — the structure the base-case
measurement found (tight exactly when the parities allow) and which no argument
in the corpus had yet supplied. Stated against `cycleType` rather than `n - c`
to avoid truncated `ℕ` subtraction; see the note below for what that costs. -/
theorem writhe_parity_cycleType (w : BraidWord n) :
    Even (BraidWord.writhe w
      - (((closurePerm w).cycleType.sum + (closurePerm w).cycleType.card : ℕ) : ℤ)) := by
  have hpar : w.length % 2
      = ((closurePerm w).cycleType.sum + (closurePerm w).cycleType.card) % 2 :=
    neg_one_pow_parity (length_parity_cycleType w)
  obtain ⟨k, hk⟩ := writhe_sub_length_even w
  have hlen : Even ((w.length : ℤ)
      - (((closurePerm w).cycleType.sum + (closurePerm w).cycleType.card : ℕ) : ℤ)) := by
    rw [Int.even_sub, Int.even_coe_nat, Int.even_coe_nat, Nat.even_iff, Nat.even_iff, hpar]
  obtain ⟨m, hm⟩ := hlen
  exact ⟨k + m, by linarith⟩

end QOU.Knot.BraidClosure

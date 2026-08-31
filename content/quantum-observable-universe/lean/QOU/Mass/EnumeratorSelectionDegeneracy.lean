/-
# The binding-K enumerator's selection criterion cannot pick a binding carrier

`qou-brng` asked for a carrier selection principle that is not minimality. There
already is one — `binding_k_enumerator.py` ranks by Frobenius residual — and this
file is why it does not work. Three independent defects, each fatal on its own,
all readable off the enumerator's **own recorded output** in
`computations/_deprecated/binding-k-enumerator.witness.json`.

## 🛑 First, correcting a correction of mine

The merged `CarrierCrossingQuantisation` header says the corpus's principle is
Frobenius-residual minimisation, not minimality, and that reading
`bindingKMinimalLength` as the criterion is what makes minimality look
load-bearing. **The first half is right about the code and wrong about the
corpus.** The `sort` key is indeed `(PSD-feasible, residual, length)` — but the
`bindingKWord = [3,3]` on the Lean instances was taken from the witness's
`min_length_psd_feasible_candidates` list, **not** from the residual-ranked
`psd_feasible_top_k`. So the recorded carrier *is* the min-length pick after
all; what is not minimality is the code's sort. Both halves matter and I
previously stated only one.

## Defect 1 — the residual's top pick is a SELF-CROSSING

With `constituent_offsets = [0,3,6]` in `B₉`, nucleon `k` occupies strands
`3k+1 … 3k+3`, and `σ_i` joins strands `i, i+1`. So `σ_i` is an **interface**
(inter-component) generator exactly when `i` is a multiple of `3`
(`interface_iff_three_dvd`) — that is, `σ₃` and `σ₆` alone. Every one of
`σ₄, σ₅, σ₇, σ₈` joins two strands **inside one nucleon**.

The enumerator's `inter_nucleon_generators_extended` for `A = 3` is
`[3,-3,4,-4,5,-5,6,-6,7,-7,8,-8]` — **8 of its 12 entries are intra-nucleon**,
and the field name says otherwise.

Consequence, recorded: for **both** `³H` and `³He` the residual-ranked top two
are `[-8,-8]` and `[-5,-5]`, i.e. `σ₈⁻²` and `σ₅⁻²` — self-crossings inside
nucleons 3 and 2. A carrier built from them has **zero** inter-component
crossings, so `countChannel = 0` (`selfCrossing_countChannel_eq_zero`) and it
binds nothing at all. The criterion's winner is not a weak carrier; it is not a
carrier.

## Defect 2 — the top-2 ordering is float64 noise between exactly-equal candidates

Recorded residuals, `³H`:

    [-8,-8]   0.9321237012643592     <- rank 1
    [-5,-5]   0.9321237012643594     <- rank 2
    [-3,-3]   0.9339216957602768
    [-6,-6]   0.9339216957602768

`σ₅` and `σ₈` are the *same* generator of two different nucleon blocks, so by
the construction's block symmetry their residuals are **equal**. The recorded
difference is `2.220e-16` — two ULP at `0.93`, where `float64` eps is
`1.11e-16`. The rank-1 slot is therefore decided by rounding, not by
mathematics. The same 2-ULP split appears for `[-4,-4]` vs `[-7,-7]` and for
`[7,7]` vs `[4,4]`.

This is the failure mode AGENTS.md's NO-FLOAT64 rule names outright: *"agreement
at 1e-16 in float64 is the floor of the arithmetic, not evidence about the
mathematics"* — here used not to claim an agreement but, worse, to **break a
tie** and thereby choose the answer.

## Defect 3 — the two genuine interfaces are exactly degenerate

`[-3,-3]` and `[-6,-6]` record the **identical** residual
`0.9339216957602768`, to every digit. So even restricted to the real interface
generators the criterion cannot tell the `1|2` interface from the `2|3` one. A
principle that is degenerate on the only two candidates that could bind is not
selecting; it is tying.

## What this closes, and what it opens

**Closes:** extending `L_K_max` was my proposed next step and it is **futile**.
The search was never truncation-limited in the way that matters — a longer
search re-ranks by a criterion that (1) prefers non-carriers, (2) breaks ties in
rounding error, and (3) is degenerate on the interfaces. Fixing the length bound
without fixing the criterion searches a larger space with the same broken
comparator.

**Opens:** the criterion is repairable and the repairs are named. Restrict the
generator set to genuine interfaces (`i` a multiple of `3`); carry the residual
in `mpmath.mpf` rather than `float64` so the comparisons mean something; and
break the remaining `1|2`-vs-`2|3` degeneracy with something other than the
trace residual, since that symmetry is exact.

Note also that the corpus's own canonical `A = 3` carrier, the Borromean `L6a4`,
is **not reachable** from `⟨σ₃, σ₆⟩` at all: those two generators are distant
(`|3-6| ≥ 2`) hence commute, so the subgroup is free abelian and every word
reduces to `σ₃^a σ₆^b`, whose pairwise linking numbers are `a/2`, `b/2`, `0`.
Brunnian forces `a = b = 0`, the trivial carrier
(`commuting_interfaces_brunnian_trivial`). The Borromean braid `(σ₁σ₂⁻¹)³` needs
**adjacent** generators. So on the minimal set the enumerator could never have
found the corpus's own answer, at any length.

## Scope

Scope **(b)** on the enumerator's selection criterion *as implemented*, with the
invariants named: the block arithmetic of `constituent_offsets` (defects 1, 3)
and `float64` ULP spacing (defect 2). Scope **(a)** on the *idea* of
residual-based selection, which is untested — no repaired criterion has been
run, and nothing here says one would fail.

Ground ring `ℕ` for the block arithmetic; the `countChannel` statement is
`ℝ` (§7c) matching `BrunnianBindingChannel`.

Beans `qou-brng`.
-/
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

namespace QOU.Mass.EnumeratorSelectionDegeneracy

/-! ## 1. Which generators are interfaces -/

/-- The nucleon block containing strand `s`, for nucleons of three strands each
laid out at `constituent_offsets = [0, 3, 6, …]`: strands `1,2,3` are nucleon 0,
strands `4,5,6` nucleon 1, and so on. -/
def blockOf (s : ℕ) : ℕ := (s - 1) / 3

/-- `σ_i` joins strands `i` and `i+1`; it is an **interface** generator when
those two strands lie in different nucleons. -/
def IsInterface (i : ℕ) : Prop := blockOf i ≠ blockOf (i + 1)

/-- **Interfaces are exactly the multiples of three.** So in `B₉` with three
nucleons, `σ₃` and `σ₆` are the only inter-component generators, and
`σ₄, σ₅, σ₇, σ₈` are all intra-nucleon self-crossings. -/
theorem interface_iff_three_dvd (i : ℕ) (hi : 1 ≤ i) :
    IsInterface i ↔ i % 3 = 0 := by
  unfold IsInterface blockOf
  omega

/-- The four generators the enumerator's `..._extended` list adds beyond `σ₃`
and `σ₆` are **not** interfaces, so the field name is wrong about two thirds of
its entries. -/
theorem extended_generators_are_intra :
    ¬ IsInterface 4 ∧ ¬ IsInterface 5 ∧ ¬ IsInterface 7 ∧ ¬ IsInterface 8 := by
  refine ⟨?_, ?_, ?_, ?_⟩ <;>
    · rw [interface_iff_three_dvd _ (by norm_num)]; decide

/-- And `σ₃`, `σ₆` are. -/
theorem three_six_are_interfaces : IsInterface 3 ∧ IsInterface 6 := by
  constructor <;> · rw [interface_iff_three_dvd _ (by norm_num)]

/-! ## 2. A self-crossing carrier binds nothing -/

/-- The unsigned count channel, as in `BrunnianBindingChannel.countChannel`:
`½(n₊ + n₋)(q − q⁻¹)`, whose `n₊`, `n₋` are **inter-component** crossings. -/
noncomputable def countChannel (np nn : ℕ) (q : ℝ) : ℝ :=
  ((np : ℝ) + (nn : ℝ)) * (q - q⁻¹) / 2

/-- **A carrier built only from intra-nucleon generators contributes no binding.**
It has no inter-component crossings, so both counts are zero and the channel
vanishes identically — for every `q`, so no anchor or convention rescues it.
This is what the enumerator's rank-1 candidate `σ₈⁻²` is. -/
theorem selfCrossing_countChannel_eq_zero (q : ℝ) : countChannel 0 0 q = 0 := by
  unfold countChannel; ring

/-- Restated as the acceptance test it fails: a carrier is admissible only if its
count channel is non-zero somewhere, and a self-crossing carrier never is. -/
theorem selfCrossing_not_admissible :
    ¬ ∃ q : ℝ, countChannel 0 0 q ≠ 0 := by
  rintro ⟨q, hq⟩
  exact hq (selfCrossing_countChannel_eq_zero q)

/-! ## 3. The minimal interface set cannot carry a Brunnian link -/

/-- Pairwise linking numbers of a carrier `σ₃^a σ₆^b` in `B₉`, doubled to stay in
`ℤ`: the `1|2` pair sees only the `σ₃` letters, the `2|3` pair only the `σ₆`
letters, and the `1|3` pair sees neither. -/
def twoLk (a b : ℤ) : ℤ × ℤ × ℤ := (a, b, 0)

/-- **On the minimal interface set the only Brunnian carrier is trivial.**
`σ₃` and `σ₆` are distant (`|3 - 6| ≥ 2`) hence commute, so `⟨σ₃, σ₆⟩` is free
abelian and every word reduces to `σ₃^a σ₆^b`. Brunnian means every pairwise
linking number vanishes, which forces `a = b = 0`.

So no amount of extra word length produces a Brunnian carrier here — the
obstruction is the generator set, not the length bound. The corpus's own
canonical `A = 3` carrier, the Borromean `(σ₁σ₂⁻¹)³`, needs **adjacent**
generators and is therefore outside this subgroup entirely. -/
theorem commuting_interfaces_brunnian_trivial (a b : ℤ)
    (h : twoLk a b = (0, 0, 0)) : a = 0 ∧ b = 0 := by
  unfold twoLk at h
  exact ⟨(Prod.mk.injEq .. ▸ h).1, by simpa using congrArg (Prod.fst ∘ Prod.snd) h⟩

end QOU.Mass.EnumeratorSelectionDegeneracy

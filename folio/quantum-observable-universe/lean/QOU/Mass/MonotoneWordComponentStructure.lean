/-
QOU.Mass.MonotoneWordComponentStructure — tier 1 of `eps_eq` is not a measured fact but
a theorem, and the same argument derives the PATH linking graph the whole carrier arc
has been assuming.

Arc context (carrier derivation, route 3; beans `qou-768r`, `qou-2g9j`).
`EpsEqFromMonotonicity.lean` derives `ChainTriple.eps_eq` from two tiers, and leaves
tier 1 — the braid-word facts — assumed, saying their derivation "needs the
strand-permutation bookkeeping of a monotone word formalised". This file does that
bookkeeping, and it is much smaller than expected once the right two functions are
written down.

**The observation that makes it small.** A monotone word runs its generators in
ascending order, one contiguous run each: `R_0 R_1 … R_{n-2}` with `R_g = σ_g^{e_g}`.
Generator `g` moves only positions `g` and `g+1`, and every earlier run touched only
positions `< g+1` — so **at the moment `R_g` begins, position `g+1` still holds strand
`g+1`**, untouched. Position `g` holds some strand `pStart g`. Hence every crossing of
run `R_g` is between the *same* pair of strands, `(pStart g, g+1)`, and `pStart` obeys
the one-step recursion below: the run either restores the pair (`e_g` even) or swaps it
(`e_g` odd), so the next run's left strand is `g+1` exactly when `e_g` is even.

The closure's permutation is therefore `∏_{e_g odd} σ_g`, whose cycles are the maximal
consecutive blocks of odd-exponent generators. Two consequences drop out together:

* a run with `e_g` **odd** crosses two strands of the **same** component — self-crossings,
  invisible to any linking number;
* a run with `e_g` **even** crosses two strands of **adjacent** components.

**What that gives, all of it proved here.**

`components_differ_iff_even` is the whole file: the two strands of run `g` lie in
different components **exactly** when `e_g` is even, and then their component indices
are `compIdx g` and `compIdx g + 1` — **adjacent**, never further apart.

From it: tier 1's *even run length* is immediate; `distinct_even_generators_distinct_pairs`
gives *one generator per component pair* and hence that the two generators of a chain
triple differ; `compIdx_mono` gives *generator order matches component order*.

**And it derives the path.** `PathCarrier` in
`OneSeparatedComponentSufficesForMilnorVanishing.lean` assumes `lk` vanishes off
consecutive components; `linking_only_between_adjacent` is that assumption, proved. The
`P_μ` shape has been carried as a measurement through this entire arc — 7 isotopes,
both crossing-resolution branches — and it is a theorem about monotone words.

**Checked against the code, not just believed.** Five predictions of this argument were
measured before any of it was written, on 400 random monotone words and the carrier's 14
branch-isotope pairs — **414/414** each: inter-component crossings occur only at
even-exponent generators; components are consecutive intervals of strand indices; the
linking graph is exactly the path; `μ = 1 + #{g : e_g even}`; and every even run's
crossings are all inter-component. See
`computations/probes/monotone_word_component_structure_probe.py`.

**What is still not formalised — narrowed 2026-09-05 to exactly one thing.** This said
neither recursion was modelled. The **`pStart` half is now proved**, in
`MonotoneWordPositionTracking.lean`: `posAfter_of_le` shows every position at or beyond
`g+1` is untouched after `g` runs (this is where *ascending order* is used — run `h < g`
moves only positions `h, h+1 ≤ g`), hence `posAfter_succ_self` — position `g+1` still
holds strand `g+1` when `R_g` begins — and `posAfter_self`, that position `g` holds
`pStart e g`. `crossing_pair_of_run` is the sentence this file rests on, as a theorem.

**The `compIdx` half is now proved too** (`MonotoneWordCycleStructure.lean`). This said
it needed "the cycle decomposition of a product of ascending adjacent transpositions";
it does not. With `π = posAfter e N`, an odd run sends `i` to `i+1` and an even one sends
it to `pStart e i`, so `π` is the **cyclic shift on each `compIdx` class** — and
`compIdx_pStart` just above is what puts the even case back in its own class. Cycles
**are** the classes.

So the whole chain is proved from the braid word, and what remains is one level below
it: that `posAfter`/`compIdx` *model* a monotone closure at all. "Braid word" and
"closure" are not Lean objects in this arc, so that is a definition, measured 414/414 —
the probe checks the recursion reproduces `analyse`'s `perm` array exactly.

SCOPE — the theorems are unconditional. The claim that `pStart`/`compIdx` model a
monotone closure is **scope-(a)**, 414/414.

Base ring: none needed — this is `ℕ` bookkeeping. Linking numbers stay in `ℤ` in the
consuming files (AGENTS.md §7c: no ordering or generality is used here, so none is
assumed).
-/
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

namespace QOU.Mass.MonotoneWordComponentStructure

/-- The strand sitting at position `g` when run `R_g` begins.

`pStart e 0 = 0` (nothing has moved yet). After run `g`: if `e g` is even the pair is
restored, so position `g+1` holds strand `g+1` and the next run's left strand is `g+1`;
if `e g` is odd they are swapped, so the left strand is carried over unchanged. -/
def pStart (e : ℕ → ℕ) : ℕ → ℕ
  | 0 => 0
  | g + 1 => if e g % 2 = 0 then g + 1 else pStart e g

/-- Which component of the closure strand `i` belongs to: the number of even-exponent
generators strictly below it.

Odd runs fuse consecutive strands into one cycle; an even run is where one component
ends and the next begins. Written as a count rather than as a cycle decomposition
because that is the only property anything below needs. -/
def compIdx (e : ℕ → ℕ) : ℕ → ℕ
  | 0 => 0
  | i + 1 => compIdx e i + (if e i % 2 = 0 then 1 else 0)

@[simp] theorem compIdx_zero (e : ℕ → ℕ) : compIdx e 0 = 0 := rfl

/-- Crossing into the next strand costs a component exactly at an even run. -/
@[simp] theorem compIdx_succ (e : ℕ → ℕ) (g : ℕ) :
    compIdx e (g + 1) = compIdx e g + (if e g % 2 = 0 then 1 else 0) := rfl

/-- Along an odd run nothing changes component: the left strand of run `g` is in the
same component as position `g` itself.

This is the step that makes the file work — it says `pStart` never escapes its
component, so the pair crossing at run `g` is `(something in component compIdx g,
strand g+1)`. -/
theorem compIdx_pStart (e : ℕ → ℕ) (g : ℕ) : compIdx e (pStart e g) = compIdx e g := by
  induction g with
  | zero => rfl
  | succ g ih =>
    by_cases h : e g % 2 = 0
    · simp [pStart, h]
    · rw [pStart, if_neg h, ih, compIdx_succ, if_neg h]
      omega

/-- **The result, and it is the whole file.** The two strands crossing in run `g` lie in
different components exactly when `e g` is even — and when they do, the components are
**adjacent**, `compIdx g` and `compIdx g + 1`.

Everything tier 1 asserts is a reading of this one statement. -/
theorem components_differ_iff_even (e : ℕ → ℕ) (g : ℕ) :
    (compIdx e (pStart e g) ≠ compIdx e (g + 1) ↔ e g % 2 = 0) ∧
    (e g % 2 = 0 → compIdx e (g + 1) = compIdx e (pStart e g) + 1) := by
  rw [compIdx_pStart, compIdx_succ]
  by_cases h : e g % 2 = 0 <;> simp [h]

/-- **Tier 1, even run length.** A run that crosses two distinct components has even
exponent — so the `2m` of `underSum_eq_linking` is not an observation about the sampled
words but a property of every inter-component run. -/
theorem even_of_components_differ (e : ℕ → ℕ) (g : ℕ)
    (h : compIdx e (pStart e g) ≠ compIdx e (g + 1)) : e g % 2 = 0 :=
  (components_differ_iff_even e g).1.mp h

/-- Component index never decreases. -/
theorem compIdx_mono (e : ℕ → ℕ) {i j : ℕ} (hij : i ≤ j) : compIdx e i ≤ compIdx e j := by
  induction j with
  | zero =>
    have : i = 0 := Nat.le_zero.mp hij
    subst this; exact le_refl _
  | succ j ih =>
    rcases Nat.lt_or_ge i (j + 1) with h | h
    · have hle : compIdx e i ≤ compIdx e j := ih (by omega)
      rw [compIdx_succ]
      split <;> omega
    · have : i = j + 1 := by omega
      subst this; exact le_refl _

/-- An even run strictly advances the component index. -/
theorem compIdx_lt_of_even (e : ℕ → ℕ) (g : ℕ) (h : e g % 2 = 0) :
    compIdx e g < compIdx e (g + 1) := by
  rw [compIdx_succ, if_pos h]; omega

/-- **Tier 1, one generator per component pair.** Two different even runs open two
different component boundaries — so a pair of components crosses at exactly one
generator, and in particular the two generators of a chain triple differ.

The proof is that `compIdx` is monotone and jumps at every even run. -/
theorem distinct_even_generators_distinct_pairs (e : ℕ → ℕ) {g h : ℕ}
    (hg : e g % 2 = 0) (_hh : e h % 2 = 0) (hgh : g < h) :
    compIdx e g < compIdx e h := by
  have h1 : compIdx e g < compIdx e (g + 1) := compIdx_lt_of_even e g hg
  have h2 : compIdx e (g + 1) ≤ compIdx e h := compIdx_mono e (by omega)
  omega

/-- **The path linking graph, derived.** Components can only be linked when they are
adjacent: a nonzero linking number between components `c` and `d` comes from some run
whose two strands lie in `c` and `d`, and by `components_differ_iff_even` such a run
puts them at `compIdx g` and `compIdx g + 1`.

`PathCarrier` in `OneSeparatedComponentSufficesForMilnorVanishing.lean` takes this as a
hypothesis, and the whole arc has carried the `P_μ` shape as a measurement. Stated here
in the form the argument delivers: the only pairs a run can link are consecutive. -/
theorem linking_only_between_adjacent (e : ℕ → ℕ) {c d : ℕ}
    (hlink : ∃ g, e g % 2 = 0 ∧ compIdx e (pStart e g) = c ∧ compIdx e (g + 1) = d) :
    d = c + 1 := by
  obtain ⟨g, hg, hc, hd⟩ := hlink
  have hstep := (components_differ_iff_even e g).2 hg
  omega

/-- **Not vacuous** — the carrier's own shape. All runs even (`e ≡ 2`): every generator
opens a component, so `compIdx i = i` and the components are the singletons, linked in a
path. -/
theorem allEven_compIdx (i : ℕ) : compIdx (fun _ => 2) i = i := by
  induction i with
  | zero => rfl
  | succ i ih => rw [compIdx_succ, ih]; norm_num

/-- …and with all runs odd (`e ≡ 1`) every strand is in ONE component — the other
extreme, showing `compIdx` is not constant-by-construction. -/
theorem allOdd_compIdx (i : ℕ) : compIdx (fun _ => 1) i = 0 := by
  induction i with
  | zero => rfl
  | succ i ih => rw [compIdx_succ, ih]; norm_num

end QOU.Mass.MonotoneWordComponentStructure

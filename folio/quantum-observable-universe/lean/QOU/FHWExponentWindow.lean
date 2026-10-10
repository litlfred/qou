import QOU.MobiusMutualChannel
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.SpecialFunctions.Log.Basic

/-!
# QOU.FHWExponentWindow

**Two independent selection principles for the kernel exponent agree, and they
agree at a single point.**

## The question this settles

`QOU/MobiusMutualChannel.lean` §7 proved that Möbius invariance against the
arclength density forces the kernel `f(d) = f(1)/d²` — exponent exactly `−2`.
A fair objection to that result is that it merely *re-derives a convention*:
the inverse square was the modelling choice all along, so a criterion selecting
it could be a criterion reverse-engineered to select it.

The literature answers half of that, and the honest half is smaller than it
first looks — see the two 🛑 sections below before citing this file. Bryson–Freedman–He–Wang (Bull. AMS **28** (1993) 99–103,
`library/arxiv-math-9301212v1/`) treat `−2` explicitly as **a choice among
candidates**, and pin it only to an interval. In their words:

> "Note that there are competing candidates for the exponent `= −2` in the
> definition of `E`; for example, the Newtonian potential in `ℝ³` has exponent
> `= −1`. When the exponent is strictly larger than `−3`, finite values are
> obtained for smooth simple loops. Exponents smaller or equal to `−2` yield
> energies which blow up as a simple loop `γ` begins to acquire a double point,
> thus creating an infinite energy barrier to a change of topology. Such a
> barrier would not exist for the Newtonian potential."

So their two requirements bracket the exponent:

* **finiteness** on smooth simple loops needs `e > −3`;
* the **topological barrier** — infinite energy cost to change knot type —
  needs `e ≤ −2`.

Their window is therefore `(−3, −2]`, a continuum. It does **not** single out
`−2`; the Newtonian `−1` is excluded, but `−2.5` is not.

**§7's criterion does single it out, and it picks the endpoint.** That is the
content here: two criteria with nothing to do with each other — one conformal,
one topological — intersect in exactly one exponent.

## What is proved, and what is cited

**PROVED (sorry-free, from §7):** `mobiusInvariant_rpow_exponent_eq_neg_two`.
If the power law `d ↦ d^e` is Möbius invariant against arclength, then
`e = −2`. No window is assumed; this is §7 specialised to power laws and then
solved for the exponent.

**PROVED:** `neg_two_mem_bfhwWindow`, so the intersection statement is not
vacuous, and `bfhw_window_mobius_unique`, the intersection itself.

## 🛑 What BFHW actually supply, corrected after reading the surrounding page

An earlier draft of this file said the two window facts "are analytic results of
[bryson-freedman-he-wang1993]". **That is wrong on both halves and is corrected
here rather than shipped.**

*It is not a theorem of theirs.* The passage is an **unnumbered remark**, sitting
between the statement of Theorem E and the proof of Theorem A — it carries no
proof in that document.

*It is not theirs to prove.* The remark **defers**, verbatim: *"We refer to
[O1–O3] for detailed discussions."* Those are O'Hara — `[O1]` *Energy of a knot*
(Topology 30, 1991, held at `library/1-s20-0040938391900102-main/`), `[O2]`
*Family of energy functionals of knots* (Topology Appl.), `[O3]` *Energy
functionals of knots* (World Scientific). **`[O2]` and `[O3]` are where the
exponent range lives, and the corpus holds NEITHER** — checked by title across
every `library/*/structure.json`. So `BFHWWindow` records a claim whose proof is
in neither this file nor any held document.

## 🛑 And the result here is not news to BFHW — they assert it

The same remark closes: *"Similarity and Möbius invariance are, **of course**,
special to the exponent −2."*

So the *statement* `mobiusInvariant_rpow_exponent_eq_neg_two` establishes was
regarded as evident in 1993. This file does not discover it. What it does is
narrower and still worth having:

* it **proves** what they assert without proof, sorry-free, from the invariance
  hypothesis alone;
* it proves **uniqueness** — BFHW say invariance is "special to" `−2`, which is
  a statement that `−2` has the property; the theorem here is that `−2` is the
  **only** exponent that does.

Do not describe this file as showing that the exponent was open, or as settling
a question BFHW left open. They left the *modelling* choice open among candidate
knot energies while treating the Möbius characterisation as obvious. Those are
different things and the distinction is the honest one.

**NOT CLAIMED:** that any of this applies to the *mutual* channel's magnitude.
BFHW's Theorem D (`2πc([γ]) + 4 ≤ E(γ)`) is about the **self** energy of a
single closed curve; `qou-o6ml` route 2 owns the pairwise term, and the bound
does not transfer to it. What transfers is the **exponent** question, which is
a statement about the kernel and is shared by both channels.

## References

- [bryson-freedman-he-wang1993] Bull. AMS 28(1), 1993, 99–103 —
  `library/arxiv-math-9301212v1/`
- [ohara1991] https://doi.org/10.1016/0040-9383(91)90010-2
-/

namespace QOU.FHWExponentWindow

open QOU.MobiusMutualChannel

/-- **The BFHW admissible window**, as *cited* from Bull. AMS 28 (1993) 99–103.

    `e > −3` is their finiteness condition on smooth simple loops; `e ≤ −2` is
    their infinite-energy-barrier condition. This predicate **records** the two
    claims so the intersection below can be stated; it does not derive them. -/
def BFHWWindow (e : ℝ) : Prop := -3 < e ∧ e ≤ -2

/-- `−2` lies in the BFHW window — the window is inhabited at the endpoint, so
    the uniqueness statement below is not vacuously true. -/
theorem neg_two_mem_bfhwWindow : BFHWWindow (-2) := by
  constructor <;> norm_num

/-- The window is a genuine interval, not a point: `−5/2` is admissible to BFHW
    and is **not** `−2`.

    This is the load-bearing non-degeneracy check. Without it, "Möbius
    invariance picks out the endpoint" would be empty — the endpoint might be
    the only thing there. -/
theorem bfhwWindow_not_singleton :
    ∃ e : ℝ, BFHWWindow e ∧ e ≠ -2 := by
  refine ⟨-5/2, ⟨by norm_num, by norm_num⟩, by norm_num⟩

/-- **The Newtonian exponent is excluded by BFHW**, as their remark says — a
    sanity check that the window encodes what the paper claims. -/
theorem neg_one_not_mem_bfhwWindow : ¬ BFHWWindow (-1) := by
  rintro ⟨-, h⟩; norm_num at h

/-- **Möbius invariance forces the exponent to be exactly `−2`.**

    §7 of `MobiusMutualChannel` gives `f d = f 1 / d ^ 2` for any Möbius
    invariant kernel. Specialising to the power law `f d = d ^ e` and evaluating
    at `d = 2` gives `2 ^ e = 2 ^ (−2)`; taking logarithms and cancelling
    `log 2 ≠ 0` yields the exponent.

    Note what is *not* assumed: no window, no finiteness, no barrier. The
    conformal symmetry alone determines the exponent. -/
theorem mobiusInvariant_rpow_exponent_eq_neg_two
    {e : ℝ} (h : MobiusInvariantKernel (fun d => d ^ e)) : e = -2 := by
  -- `x ^ (-2 : ℝ) = 1 / x ^ 2` for positive `x`, via the integer cast.
  have hrpow : ∀ x : ℝ, 0 < x → x ^ (-2 : ℝ) = 1 / x ^ 2 := by
    intro x hx
    rw [show (-2 : ℝ) = ((-2 : ℤ) : ℝ) by norm_num, Real.rpow_intCast]
    simp
    norm_cast
  -- §7 at `d = 2`, with `1 ^ e = 1`.
  have hkey := mobiusInvariant_forces_inverse_square h (show (0 : ℝ) < 2 by norm_num)
  simp only [Real.one_rpow] at hkey
  -- `hkey : (2:ℝ) ^ e = 1 / 2 ^ 2`; rewrite the right side back to an rpow.
  rw [← hrpow 2 (by norm_num)] at hkey
  -- Take logs and cancel `log 2 ≠ 0`.
  have hlog := congrArg Real.log hkey
  rw [Real.log_rpow (by norm_num : (0:ℝ) < 2),
      Real.log_rpow (by norm_num : (0:ℝ) < 2)] at hlog
  exact mul_right_cancel₀ (ne_of_gt (Real.log_pos (by norm_num))) hlog

/-- **THE RESULT: the two criteria intersect in exactly one exponent.**

    An exponent that is admissible to BFHW *and* Möbius invariant is `−2`, and
    `−2` is admissible — so the conformal criterion selects precisely the
    endpoint of the topological window.

    Two things make this more than a restatement. The window is a genuine
    interval (`bfhwWindow_not_singleton`), so the endpoint is not the only
    candidate on offer. And the two criteria are independent in origin: BFHW's
    comes from finiteness and an energy barrier to changing knot type, §7's from
    invariance under inversions. Neither was derived from the other, and the
    corpus holds the paper that states the first. -/
theorem bfhw_window_mobius_unique
    {e : ℝ} (_hw : BFHWWindow e) (hm : MobiusInvariantKernel (fun d => d ^ e)) :
    e = -2 :=
  mobiusInvariant_rpow_exponent_eq_neg_two hm

/-- The converse half: `−2` really does satisfy both criteria, so the
    intersection is the nonempty set `{−2}` rather than empty. -/
theorem neg_two_satisfies_both :
    BFHWWindow (-2) ∧ MobiusInvariantKernel (fun d => d ^ (-2 : ℝ)) := by
  refine ⟨neg_two_mem_bfhwWindow, ?_⟩
  have hrpow : ∀ x : ℝ, 0 < x → x ^ (-2 : ℝ) = 1 / x ^ 2 := by
    intro x hx
    rw [show (-2 : ℝ) = ((-2 : ℤ) : ℝ) by norm_num, Real.rpow_intCast]
    simp
    norm_cast
  intro d da db hd hda hdb
  have hq : (0:ℝ) < d / (da * db) := by positivity
  simp only [hrpow _ hq, hrpow _ hd]
  have hd' : d ≠ 0 := ne_of_gt hd
  have hda' : da ≠ 0 := ne_of_gt hda
  have hdb' : db ≠ 0 := ne_of_gt hdb
  field_simp

end QOU.FHWExponentWindow

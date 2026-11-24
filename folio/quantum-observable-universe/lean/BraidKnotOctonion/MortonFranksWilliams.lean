import Mathlib.Tactic.Linarith

set_option autoImplicit false

/-!
# QOU.Knot.MortonFranksWilliams — the MFW pair, and what it bounds

Bean `qou-dr8m`. The Morton–Franks–Williams inequalities bound the braid index
of a link below, from the `v`-degrees of its HOMFLY polynomial. HOMFLY is the
Ocneanu/Markov trace on the Iwahori–Hecke tower — the corpus's own object — so
this is the natural route to a **derived** braid index, replacing the
literature-recalled value `braid index(6₁) = 4` that `qou-xpgq` flagged as
unverified and load-bearing. (`qou-xpgq` lives on the unmerged branch of
PR #5294, so `beans show qou-xpgq` returns nothing until that lands — its PR
body carries the flag verbatim: "`6₁`'s braid index is **not** verified against
any in-repo source".)

## The statement being formalised

With the HOMFLY skein `v⁻¹P(L₊) − vP(L₋) = zP(L₀)`, `P(unknot) = 1`, and
`β ∈ B_n` a braid with exponent sum (writhe) `e` whose closure is `L`:

    (1)   e − n + 1  ≤  mindeg_v P_L
    (2)                 maxdeg_v P_L  ≤  e + n − 1

**These two are the HYPOTHESES here, carried by `MFWWitness`, and they are NOT
proved.** Proving them requires HOMFLY's well-definedness, i.e. Markov
invariance of the Ocneanu trace on the `Hₙ` tower, plus a degree argument —
research-scale, and tracked separately. Everything below is *derived* from the
pair, sorry-free, and the file asserts nothing about any actual knot.

This is the §3b-cond conditional pattern used honestly: the structure carries
the **inputs**, the theorems **derive** the conclusions. It is deliberately NOT
a class carrying `braid index ≥ …` as a field, which would be the
"axiomatisation is not a proof" failure — the bound is computed here, not
assumed.

## What is derived

* `spread_le_two_mul_sub_two` — subtracting (1) from (2) **cancels the writhe**
  `e`, which is the crux: `e` is not a link invariant, the degrees are.
* `braid_bound` — hence `spread + 2 ≤ 2n`, the MFW lower bound on the braid
  index, in a division-free form.
* `no_representative_of_spread_gt` — the contrapositive, which is the form that
  actually rules a strand number out.
* `selfLinking_le` — reading (1) ALONE bounds the **self-linking number**
  `sl = e − n` above: `sl ≤ mindeg_v P − 1`. The HOMFLY sharpening of
  Bennequin. So one trace bounds a minimum below and a maximum above.
* `writhe_bounds` — adding (1) and (2) instead constrains the writhe at fixed
  `n` (stated as two inequalities to avoid an `abs` import).

## And why the braid index is a MINIMUM and never a maximum

`Markov.stab` (stabilisation `β ↦ βσₙ^{±1}`, closure unchanged) makes the set of
representable strand numbers **upward closed**, hence unbounded above:
`rep_unbounded`. So `max` is `∞` for every link and carries no information —
the minimum is the only invariant of the two. That asymmetry is structural, and
it is proved here rather than asserted.

## References

- [morton1988] H. R. Morton, *Seifert circles and knot polynomials*. https://doi.org/10.1017/S0305004100064057
- [franks-williams1987] J. Franks, R. F. Williams, *Braids and the Jones polynomial*. https://doi.org/10.1090/S0002-9947-1987-0896009-2
- [leitner2026] `QOU/KnotTheory/JonesPolynomial.lean` (the Markov-trace idiom this follows).
-/

namespace QOU.Knot.MortonFranksWilliams

/-- The MFW input for one braid representative: `n` strands, writhe `e`, and
the `v`-degree window `[dmin, dmax]` of the link's HOMFLY polynomial, together
with **the two MFW inequalities as hypotheses**. Nothing here is proved; see
the module docstring. -/
structure MFWWitness where
  /-- number of strands of the braid representative -/
  n : ℤ
  /-- exponent sum (writhe) of the braid word -/
  e : ℤ
  /-- `mindeg_v` of the HOMFLY polynomial of the closure -/
  dmin : ℤ
  /-- `maxdeg_v` of the HOMFLY polynomial of the closure -/
  dmax : ℤ
  /-- a braid has at least one strand -/
  one_le_n : 1 ≤ n
  /-- MFW (1) -/
  mfw_lower : e - n + 1 ≤ dmin
  /-- MFW (2) -/
  mfw_upper : dmax ≤ e + n - 1
  /-- the degree window is non-empty (`mindeg ≤ maxdeg` for a nonzero HOMFLY).
  Needed for `writhe_bounds`; NOT derivable from the MFW pair alone, so it is
  carried explicitly rather than quietly assumed. -/
  dmin_le_dmax : dmin ≤ dmax

namespace MFWWitness

variable (w : MFWWitness)

/-- **The crux: subtracting the two inequalities cancels the writhe.** `e` is
not a link invariant while the degree window is, so only the difference is
usable. -/
theorem spread_le_two_mul_sub_two : w.dmax - w.dmin ≤ 2 * w.n - 2 := by
  have h1 := w.mfw_lower
  have h2 := w.mfw_upper
  linarith

/-- **The MFW lower bound on the braid index**, division-free: any strand
number admitting a representative satisfies `spread + 2 ≤ 2n`. -/
theorem braid_bound : (w.dmax - w.dmin) + 2 ≤ 2 * w.n := by
  have := w.spread_le_two_mul_sub_two
  linarith

/-- **Reading MFW (1) alone bounds a MAXIMUM.** The self-linking number of the
transverse representative is `sl = e − n`; the same trace that bounds the braid
index below bounds `sl` above. This is the HOMFLY sharpening of Bennequin's
`sl ≤ 2g − 1`. -/
theorem selfLinking_le : w.e - w.n ≤ w.dmin - 1 := by
  have := w.mfw_lower
  linarith

/-- Adding (1) and (2) instead constrains the **writhe** at fixed `n`. Stated as
a two-sided pair rather than with `|·|` to keep the import surface minimal. -/
theorem writhe_bounds :
    2 * w.e - 2 * w.n + 2 ≤ w.dmin + w.dmax ∧
    w.dmin + w.dmax ≤ 2 * w.e + 2 * w.n - 2 := by
  have h1 := w.mfw_lower
  have h2 := w.mfw_upper
  have h3 := w.dmin_le_dmax
  constructor <;> linarith

end MFWWitness

/-- **The contrapositive — the form that actually rules a strand number out.**
If the HOMFLY degree spread is too wide for `n` strands, then no braid on `n`
strands closes to that link. This is how MFW is used in practice. -/
theorem no_representative_of_spread_gt
    (n dmin dmax : ℤ) (h : 2 * n < (dmax - dmin) + 2) :
    ¬ ∃ w : MFWWitness, w.n = n ∧ w.dmin = dmin ∧ w.dmax = dmax := by
  rintro ⟨w, rfl, rfl, rfl⟩
  exact absurd w.braid_bound (by linarith)

/-! ## Why the braid index is a minimum and never a maximum -/

/-- Markov stabilisation `β ↦ β·σₙ^{±1}` leaves the closure unchanged while
adding a strand. Carried as a hypothesis on an abstract representability
predicate: `Rep n` reads "some braid on `n` strands closes to this link". -/
class Markov (Rep : ℕ → Prop) : Prop where
  /-- stabilisation adds a strand without changing the closure -/
  stab : ∀ n, Rep n → Rep (n + 1)

variable {Rep : ℕ → Prop}

/-- Representability is **upward closed** under stabilisation. -/
theorem rep_upward [Markov Rep] {n : ℕ} (hn : Rep n) : ∀ m, n ≤ m → Rep m := by
  intro m hm
  induction m, hm using Nat.le_induction with
  | base => exact hn
  | succ k _ ih => exact Markov.stab k ih

/-- **Hence there is no maximal braid index**: the representable strand numbers
are unbounded above, so `max` is `∞` for every link and carries no information.
The braid index is a MINIMUM precisely because this maximum is degenerate. -/
theorem rep_unbounded [Markov Rep] {n : ℕ} (hn : Rep n) :
    ¬ ∃ M, ∀ m, Rep m → m ≤ M := by
  rintro ⟨M, hM⟩
  have : Rep (max n M + 1) := rep_upward hn _ (by omega)
  have := hM _ this
  omega

/-! ## Worked instance: the knot `6₁`

The four numbers below are **measured**, not recalled:
[`computations/homfly_braid_index_mfw.py`](../../../../../../computations/homfly_braid_index_mfw.py)
computes the exact two-variable HOMFLY of a braid closure by
descending-diagram skein recursion in integer Laurent arithmetic, and reads
`dmin`/`dmax` off it. The producer is gated on textbook HOMFLY for five links,
on the Conway specialisation `P(v=1, z) = ∇(z)` for seven knots, and on
agreement with the tabulated braid index for the six knots other than `6₁`.

`e = 1` is the writhe of the 4-strand word `[1,1,2,-1,-3,2,-3]`, whose closure
SnapPy identifies as `6₁`/`m032`. That word is what supplies the **upper**
bound; it is a computed fact about a diagram, so it is cited here rather than
proved. What Lean adds is the **lower** bound and its consequence — and note
that with `spread = 6` and `n = 4` both MFW inequalities are equalities, so the
witness is tight on both sides. This replaces the literature-recalled
`braid index(6₁) = 4` that `qou-xpgq` flagged as unverified and load-bearing.
-/

/-- The measured MFW input for `6₁`: HOMFLY `v`-degree window `[-2, 4]`, and the
4-strand representative of writhe `1`. -/
def sixOne : MFWWitness where
  n := 4
  e := 1
  dmin := -2
  dmax := 4
  one_le_n := by norm_num
  mfw_lower := by norm_num
  mfw_upper := by norm_num
  dmin_le_dmax := by norm_num

/-- The MFW window for `6₁` is **tight on both sides**: the derived bound
`spread + 2 ≤ 2n` holds with equality at `n = 4`. -/
theorem sixOne_tight : (sixOne.dmax - sixOne.dmin) + 2 = 2 * sixOne.n := by
  norm_num [sixOne]

/-- **No 3-strand braid closes to a link with `6₁`'s HOMFLY degree window.**
This is the step that separates `4` from `3`. Among the *tabulated* knots the
producer checks, none tests that separation — `3₁`, `4₁`, `5₁`, `5₂`, `6₂`, `6₃`
all have braid index `2` or `3` — so the discrimination is exercised
independently by `torusFourFive` below rather than only on the knot under
test. -/
theorem sixOne_not_three_strand :
    ¬ ∃ w : MFWWitness, w.n = 3 ∧ w.dmin = -2 ∧ w.dmax = 4 :=
  no_representative_of_spread_gt 3 (-2) 4 (by norm_num)

/-- **Every representative of `6₁` needs at least 4 strands.** Together with the
computed 4-strand closure cited above, the braid index of `6₁` is exactly `4`. -/
theorem sixOne_four_le_strands (w : MFWWitness)
    (hmin : w.dmin = -2) (hmax : w.dmax = 4) : 4 ≤ w.n := by
  have := w.braid_bound
  rw [hmin, hmax] at this
  linarith

/-! ### An independent knot at braid index 4

`6₁` is the knot under test, so a separation theorem stated only about it
cannot show that the machinery *can* separate `4` from `3` — it could be
reading its own input back. `T(4,5)`, the closure of `(σ₁σ₂σ₃)⁵`, supplies
that independently: its braid index is `min(p, q) = 4` by a theorem (MFW is
sharp on torus knots), not by a knot table, and the measured HOMFLY window is
`[12, 18]`, again spread `6`.
-/

/-- The measured MFW input for the torus knot `T(4,5)`: HOMFLY `v`-degree
window `[12, 18]` on the 4-strand word `(σ₁σ₂σ₃)⁵`, writhe `15`. -/
def torusFourFive : MFWWitness where
  n := 4
  e := 15
  dmin := 12
  dmax := 18
  one_le_n := by norm_num
  mfw_lower := by norm_num
  mfw_upper := by norm_num
  dmin_le_dmax := by norm_num

/-- `T(4,5)`'s window is tight on both sides, exactly as `6₁`'s is. -/
theorem torusFourFive_tight :
    (torusFourFive.dmax - torusFourFive.dmin) + 2 = 2 * torusFourFive.n := by
  norm_num [torusFourFive]

/-- **The separation is not special to `6₁`.** No 3-strand braid closes to a
link with `T(4,5)`'s degree window either, so the bound genuinely distinguishes
`4` from `3` on a knot whose braid index is fixed by a theorem rather than by
the computation under test. -/
theorem torusFourFive_not_three_strand :
    ¬ ∃ w : MFWWitness, w.n = 3 ∧ w.dmin = 12 ∧ w.dmax = 18 :=
  no_representative_of_spread_gt 3 12 18 (by norm_num)

/-- The two witnesses have **equal spread but disjoint degree windows** —
`[-2, 4]` against `[12, 18]`. MFW reads only the spread, which is why both
give `4` while the polynomials themselves are nothing alike. -/
theorem sixOne_torusFourFive_same_spread :
    sixOne.dmax - sixOne.dmin = torusFourFive.dmax - torusFourFive.dmin := by
  norm_num [sixOne, torusFourFive]

end QOU.Knot.MortonFranksWilliams

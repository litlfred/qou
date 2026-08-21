import Mathlib.Tactic.Linarith

set_option autoImplicit false

/-!
# QOU.Knot.MortonFranksWilliams — the MFW pair, and what it bounds

Bean `qou-dr8m`. The Morton–Franks–Williams inequalities bound the braid index
of a link below, from the `v`-degrees of its HOMFLY polynomial. HOMFLY is the
Ocneanu/Markov trace on the Iwahori–Hecke tower — the corpus's own object — so
this is the natural route to a **derived** braid index, replacing the
literature-recalled value `braid index(6₁) = 4` that `qou-xpgq` flagged as
unverified and load-bearing.

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
- [manuscript] `QOU/KnotTheory/JonesPolynomial.lean` (the Markov-trace idiom this follows).
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

end QOU.Knot.MortonFranksWilliams

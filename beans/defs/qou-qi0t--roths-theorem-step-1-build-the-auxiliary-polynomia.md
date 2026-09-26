---
# qou-qi0t
title: 'Roth''s theorem step 1: build the auxiliary polynomial, and thereby audit Gamma_m'
status: completed
type: task
priority: normal
created_at: 2026-08-29T19:34:44Z
updated_at: 2026-08-30T03:17:38Z
---

Roth's Lemma is proved (qou-4lbh) but Gamma_m has never been PRODUCED -- only transported (rename_equiv), descended (rothGammaFull_descend), or hand-built at m=2. Its seven clauses have never been discharged from a Diophantine setup at m >= 3. Mathlib has the engine: NumberTheory/SiegelsLemma.lean (exists_ne_zero_int_vec_norm_le) and NumberField/House.lean. The work is the wiring: encode 'P vanishes to index >= mu at (alpha,...,alpha)' as a linear system over Z in P's coefficients, count equations against unknowns, apply Siegel, and read off the height bound. Treat it as an AUDIT of RothGammaFull, not as construction: if Gamma_m is misstated, index_le_rothBound is a true theorem about the wrong hypothesis -- which is exactly what correction 18 was. Child of qou-br3w.

## The audit ran first, and `Γ_m` survived it

Before touching Siegel's lemma I built the **producer** — the thing that had never existed — and
the seven clauses came out jointly satisfiable. `QOU/Mathlib/RothGammaProducer.lean`:

* `rothDegrees H N` — Mahler's normalisation `r_h·log H_h ≈ const`, written with `Nat.log` and
  never leaving `ℕ`, because every clause of `Γ_m` is multiplicative.
* `rothGammaFull_of_heights` — **the first production of `Γ_m` in the arc.** Clauses 1 and 2 come
  out of the normalisation; 3a, 3b and 4 are conditions on `F` and `b`, which the construction
  does not choose and so must be supplied.
* `gamma_three` — `Γ_3` at `t = 1/2`, produced, not hand-built.
* `roth_three` — Roth's Lemma applied to it. Both sides discharged.

### Two things the construction settles

**The floor/ceiling split is load-bearing.** `d h := Nat.log (H h) N` at `h = 0` and
`Nat.log (H h) N + 1` elsewhere. That puts `H₀^{d₀} ≤ N < H_k^{d_k}`, which is clause 2 — "the
first `K^s` is the smallest" — *on the nose*. A uniform choice puts every `H_h^{d_h}` in
`(N, N·H_h]` and orders none of them, so the clause simply fails to follow. I did not anticipate
this; it fell out of trying to prove clause 2 and failing.

**"Choose `r₁` sufficiently large" is `p·d_j ≥ p + 2q`.** Growth needs a rounding margin, taken
here as `H_j^{2q} ≤ H_k^p` (the factor `2`), and then the clause holds exactly when the degrees
clear that finite bound. Roth's asymptotic side condition is a two-term arithmetic inequality.

### The numbers are forced, and they are enormous

Clause 3a is `q·(m−1)m(2m+1) ≤ F·p`, so at `m = 3, t = 1/2` it reads `84 ≤ F`, and clause 3b
then demands `2^84 ≤ H₁`. With the growth hypothesis the heights are `(2^84, 2^336, 2^1344)`,
`N = 2^6720`, `d = (80, 21, 6)`. ⚠ `d` decreases while `H^d` increases
(`2^6720 < 2^7056 < 2^8064`) — clauses 1 and 2 pulling opposite ways and both holding. That is
the joint satisfiability that had never been exhibited above `m = 2`.

### What the closed loop does NOT show

`roth_three` gives `Θ ≤ 13/2^{1/4} ≈ 10.9` at `m = 3`. But `Θ_m ≤ m` holds outright
(`IsRothTheta.le_card`), so **the trivial bound is 3 and Roth's Lemma here is weaker**. It has to
be: the strength is asymptotic in `t`, and `t = 1/2` is nowhere near the regime. The witness
establishes that the machine runs end to end on data it produced itself — not that the number is
useful at these parameters. Only the first was missing, and it is worth not conflating them.

## Remaining

The audit is clean, so the construction work stands as scoped: encode "P vanishes to index ≥ μ
at `(α,…,α)`" as a linear system over `ℤ`, count equations against unknowns, apply
`Mathlib.NumberTheory.SiegelsLemma.exists_ne_zero_int_vec_norm_le`, and read off `a`. The
producer now says exactly what that construction must deliver: heights with `H_j^{2q} ≤ H_k^p`,
a scale `N`, degrees clearing `p·d_j ≥ p + 2q`, and an `F` meeting clause 3a.

## The system, and the counting

`QOU/Mathlib/RothAuxiliaryPolynomial.lean` — 14 declarations, all axiom-clean.

**Mathlib supplies more of the engine than expected.**
`NumberTheory.NumberField.House.exists_ne_zero_int_vec_house_le` is Siegel's lemma **over a
number field**, with the `house` bound already proved. So the equations may keep their
`ℚ(α)` coefficients; the expansion in a `ℚ`-basis that I had scoped as work is not needed.

### Part 1 — the index condition is a linear system

`le_index_iff_coeff_eq_zero` turns `c ≤ index d α P` into "every translate-coefficient of
weight below `c` vanishes"; `coeff_translate_eq_sum` shows each is linear in `P`'s coefficients
with matrix `translateMatrix α i n := coeff i (translate α (monomial n 1))`.

⚠ Defining the matrix that way rather than by the closed form
`∏_h binom(n_h,i_h)·α_h^{n_h−i_h}` is deliberate: the closed form is a multivariate binomial
theorem, `RothIndex` records that `coeff_translate` does not exist at this Mathlib pin, and the
**system does not need it** — only the `house` bound does.

### Part 2 — the counting, done exactly

`sum_centredWeight_sq` computes the second moment **exactly**: cross terms vanish, only the `m`
diagonal terms survive. Built from the one-coordinate moments (`0` and `(r+1)(r+2)/(12r)`) and
two product-space lemmas (`sum_piFinset_single`, `sum_piFinset_pair_eq_zero`).
`card_centredWeight_le` is Chebyshev: at most `m/(4λ²)` of the box lies `λ` below the mean.

⚠⚠ **The cross terms are load-bearing, and I checked this before writing them.** Cauchy–Schwarz
on `(∑_h u_h)² ≤ m·∑_h u_h²` bounds the variance by `m²/4` instead of `m/4`. With Roth's
`λ = εm` that turns the conclusion from `1/(4ε²m)` into `1/(4ε²)` — a constant, with no `m` left
to grow. Since the whole argument is "take `m` large enough that `deg α/(4ε²m) < 1`", the
cheaper inequality does not weaken the result, it **destroys** it. Two hours of Finset
manipulation bought by five minutes of arithmetic.

⚠ `card_centredWeight_le` needs `0 ≤ lam` and is **false without it** — at negative `lam` the
filter is weaker than the square bound it is compared against. `nlinarith` refused the step,
which is the cheapest a statement-stronger-than-the-truth defect has ever been caught in this
arc: no reading, no counterexample construction, just a tactic declining.

### Remaining

1. the `house` bound on `translateMatrix` — this one does need the closed form;
2. the bridge from `Fin m → ℕ` (the counting) to `σ →₀ ℕ` (the arc's `index`);
3. equations-vs-unknowns: `deg α` equations per vanishing condition, against `∏(r_h+1)`
   unknowns, then `exists_ne_zero_int_vec_house_le`.

(2) is plumbing. (1) is a real lemma. (3) is where `m` gets chosen, and the counting above is
what makes the choice possible.

## Part 3 — the system is underdetermined, and `deg α` is not in the count

`card_lt_card_idxBox_of_eps`: at index threshold `m(½ − ε)` the vanishing conditions are strictly
fewer than the coefficients as soon as **`m > 1/(4ε²)`**. That is Roth's "take `m` sufficiently
large" with the bound explicit, and it is what the variance computation bought — the threshold
scales with `m` while the standard deviation scales with `√m`.

### The degree cancels out of the counting

I expected `deg α` to appear: classically each `K`-linear equation is `deg α` equations over `ℚ`,
so the count should read `deg α · #conditions < #unknowns`. It does not.
`exists_ne_zero_int_vec_house_le` takes `p < q` with `p`, `q` the **`K`-counts** and discharges
the `ℚ`-counts `p·h`, `q·h` internally (`h = finrank ℚ K`); since `p·h < q·h ⟺ p < q`, the degree
cancels.

⚠ This is a simplification of the **counting**, not of the theorem. `deg α` re-enters through the
`house` bound on the matrix entries, which is still missing. Worth stating precisely because
"the degree dropped out" is the kind of observation that reads as a discovery and is usually a
misreading — here it is a fact about where Mathlib draws the interface, and it moves work rather
than removing it.

### A number I did not assert

The `ε = ¼, m = 5` witness has a box of `2⁵ = 32` points (`card_idxBox_five_witness`, checked)
and a filtered set of six. The **six is a hand count and the build has no opinion about it** —
`decide` stalls on the filter's `Decidable` instance, which goes through `Rat.instDecidableLe`
and `Fintype.piFinset` and does not reduce. Recorded in the docstring as unverified rather than
stated flatly. Corrections 17 and 24 in this arc were both docstring numbers nothing checked.

## Remaining, re-ranked

1. **the `house` bound on `translateMatrix`** — needs the multivariate binomial closed form, and
   is where `deg α` actually enters. Now the only mathematical gap.
2. the `Fin m → ℕ` ↔ `σ →₀ ℕ` bridge — plumbing.
3. the application of Siegel, now that `p < q` is available.

## Part 4 — the matrix entries are small, and the engine was measured

`seminorm_translateMatrix_le`: `f (translateMatrix α i n) ≤ (2B)^{|n|}` where `|n|` is the total
degree and `B` bounds `f ∘ α`.

**Proved without the closed form.** Peel one variable occurrence at a time from
`monomial n 1 = X_j · monomial n' 1`; each step multiplies by a single linear factor
`X_j + C α_j` and costs a factor `2B` — the `2` from its two terms, the `B` from the constant
one. `coeff_X_mul'` does the peeling. The multivariate binomial theorem is never needed, which
retires the item I had ranked as "a real lemma" last turn.

### The engine: measured, not assumed

Last turn I recorded that Mathlib "supplies the engine". It does — but not in this build:

| module | transitive cone | unbuilt | verdict |
|---|---|---|---|
| `NumberTheory.SiegelsLemma` (over `ℤ`) | 1955 | **3** | built in ~30 s, verified usable |
| `NumberTheory.NumberField.House` (over `K`) | 3322 | **470** | expensive |

`Int.Matrix.exists_ne_zero_int_vec_norm_le` now type-checks at this pin (needs
`attribute [local instance] Matrix.seminormedAddCommGroup` and `open Matrix`).

⚠ `.lake` is a build artifact — a fresh container has neither, and reproducing needs
`lake build Mathlib.NumberTheory.SiegelsLemma`.

⚠ "Mathlib has it" and "this project can use it" are different claims, and I made the first
while meaning the second. The measurement took one script.

### The fork, stated rather than taken

The `ℤ` engine is free but needs the `ℚ(α) → ℚ`-basis expansion of the equations — precisely
what `House` exists to do. So: a 470-module Mathlib build, against re-deriving the integral-basis
bookkeeping. Neither is obviously right.

The Part 4 bound is written to survive either: it holds for **any** submultiplicative seminorm,
so it instantiates at `house` the moment that module is built, and at `|·|` on `ℤ` today
(`abs_translateMatrix_le`). That was the reason for the generality, not a preference for it.

## Remaining

1. **the fork above** — decide, or build `House` in the background and keep both open;
2. the `Fin m → ℕ` ↔ `σ →₀ ℕ` bridge — plumbing;
3. the Siegel application itself.

All four inputs Siegel needs now exist: the system (Part 1), its size (Parts 2–3), and the
entry bound (Part 4).

## Part 5, the house bound — and a measurement I got wrong by 20×

**Part 5, the bridge.** `Finsupp.equivFunOnFinite` carries `Fin m → ℕ` (the counting) to `σ →₀ ℕ`
(what `index` speaks), and the two weights differ by exactly the mean:
`centredWeight r (equivFunOnFinite i) = idxWeight r i − m/2`. Endpoint:
`fintypeCard_idxWeight_lt` — `Fintype.card` of the equation subtype below `Fintype.card` of the
unknown subtype, i.e. **`p < q` in the exact form Siegel asks for**.

**The house bound.** `house_translateMatrix_le` (`QOU/Mathlib/RothHouseBound.lean`) instantiates
Part 4's seminorm bound at `house`. First try, no new proof — which is what the generality was
for.

### ⚠⚠ The correction

Last commit I recorded that `House` was **470 of 3322** transitive imports from the built
closure, and framed the next step as a **fork**: that build against re-deriving the
integral-basis bookkeeping by hand.

**Both numbers were wrong and there was no fork.** `House` took **40 modules and about four
minutes** (`3390 → 3430` oleans). `SiegelsLemma` was `3`, which the estimate did get right.

Cause: the import-cone script matched `^import` with `re.MULTILINE` over whole files, so it
collected `import` lines inside docstrings and comments; once the root module `Mathlib` came in
that way the cone inflated toward all of Mathlib. The first run read only the first 20 kB per
file, which hid most of the damage.

**What makes this worth recording rather than just fixing.** The arc has now hit the same shape
three times in three guises:

* a **weaker true theorem** (correction 24) — invisible to build, axioms, and witnesses;
* a **hypothesis nobody discharges** (correction 25) — indistinguishable from a false one;
* an **unvalidated measurement** (here) — indistinguishable from a measured one.

And the check that would have caught this one was free: the script produced two numbers, `3` and
`470`. I verified the `3` in thirty seconds and extrapolated the `470`. **Validating a tool on
the case whose answer you already know is not the same as validating it** — the cheap case is
exactly the one a bug is least likely to disturb.

The wrong figure was published in a commit message and a docstring; the docstring is corrected in
place and `RothHouseBound`'s header carries the full account.

## Remaining

Only the Siegel application itself. All four of its inputs now exist and are checked:

| input | where |
|---|---|
| the system | `le_index_iff_coeff_eq_zero`, `coeff_translate_eq_sum` |
| `p < q` | `fintypeCard_idxWeight_lt` |
| entry bound (`house`) | `house_translateMatrix_le` |
| the engine | `exists_ne_zero_int_vec_house_le`, built and verified |

## From a solution to the polynomial — `QOU/Mathlib/RothAuxiliaryConstruction.lean`

`exists_ofBox_of_solution`: a coefficient vector that is non-zero on the box and kills every
vanishing condition of weight below `μ` **is** an auxiliary polynomial — degree bound, index
bound, and coefficients read off. Siegel supplies exactly such a vector, so what remains between
here and the auxiliary polynomial is the call itself.

### Three things that had to be proved rather than assumed

I expected this to be plumbing. Three pieces were not.

* **`translate` is natural in the coefficient ring** (`map_translate`). The polynomial must be
  built over `𝓞 K` — Siegel needs algebraic *integer* entries — while `index` is read over `K`.
  Without naturality those are unrelated statements. With it, `index_map` says the index does not
  notice the change of ring. This was the caveat I flagged last turn as "where the defect hides";
  it was real, and it cost an induction over `MvPolynomial`.
* **Outside the box the translate has no coefficients**
  (`coeff_translate_eq_zero_of_notMem`). The system is indexed by the box, but
  `le_index_iff_coeff_eq_zero` quantifies over **all** multi-indices of low weight — and there
  are such indices outside the box (`i h > r h` costs only `> 1` of weight, and the threshold is
  near `m/2`). They cost nothing only because translation preserves every `degreeOf`
  (`degreeOf_translate_eq` — proved long ago for another purpose). Had that failed, the system
  would have been genuinely infinite.
* **The sum runs over the box, not the support** (`coeff_translate_ofBox`).
  `coeff_translate_eq_sum` sums over `P.support`, which is what a polynomial gives you; a matrix
  row needs a *fixed* index set. Extending is free because the extra coefficients vanish, but the
  two are not the same sum and Siegel only accepts the second.

The module deliberately does **not** import `RothHouseBound`, so the construction stays usable
without the number-field dependency.

## Remaining

Only the Siegel call: build the matrix `a i n := translateMatrix α i n` over `𝓞 K` on the two
subtypes, discharge `a ≠ 0` (the `(0,0)` entry is `1`) and `0 < p` (the zero multi-index is an
equation when `ε ≤ ½`), and feed `fintypeCard_idxWeight_lt` and `house_translateMatrix_le`.

## Summary of Changes — the auxiliary polynomial exists

`MvPolynomial.exists_auxiliary_polynomial` (`QOU/Mathlib/RothAuxiliary.lean`):

> Given degrees `r`, algebraic integers `α`, and `ε` with `0 < ε ≤ ½` and `m > 1/(4ε²)`, there is
> a non-zero `P ∈ 𝓞 K[x₁,…,x_m]` with `degreeOf h P ≤ r h`, index at least `m(½ − ε)` at
> `(α₁,…,α_m)`, and every coefficient of house at most Siegel's bound.

No `sorry`; `[propext, Classical.choice, Quot.sound]`. Step 1 of `qou-br3w` is done.

### Three things this turn found by *applying* what was already proved

1. **`ε ≤ ½` is load-bearing and is not implied by the counting hypothesis.** Siegel needs
   `0 < p`, and the zero multi-index is an equation exactly when `m(½ − ε) ≥ 0`. The counting
   hypothesis `1 < 4ε²m` does not give it — `ε = 10, m = 1` satisfies it while making the
   threshold negative and the equation set empty. Free in Roth's regime, but it had to be found.
   I flagged it as a question at the end of last turn and it turned out to be real.

2. **`exists_ofBox_of_solution` carried an unusable instance binder.** It was declared
   `[DecidableEq σ]` where `σ` is the *section* variable and does not occur in the statement —
   so the instance was unresolvable and the lemma **could not be applied at all**. It compiled,
   `#print axioms` was clean, and it had no witness. Found the moment something tried to use it.
   ⚠ This is correction 9's shape once more, in its purest form yet: not a false hypothesis, an
   *unsatisfiable elaboration obligation*. The fix was deleting six characters.

3. **Siegel's height bound is stated with a `private` constant.** `c₁` in Mathlib's `House.lean`
   is `private def`, so the bound in `exists_ne_zero_int_vec_house_le`'s conclusion cannot be
   named downstream in the ordinary way. `open private c₁ from …` reaches it, and
   `auxHeightBound` gives it a name. Without that the height clause would have had to be dropped,
   or weakened to `∃ C, ∀ n, house ≤ C` — which is **contentless**, since a finite coefficient set
   always has such a `C`. Worth naming as a Mathlib API limitation rather than working around
   silently.

### Follow-on for `qou-br3w`

Step 1 of five is complete. Remaining: the index *lower* bound at the rational point (step 2,
partial — `RothHeightBound` has the one-variable case), the contradiction and parameter
bookkeeping (step 4), and `¬LiouvilleWith` (step 5). Step 3, Roth's Lemma, was `qou-4lbh`.

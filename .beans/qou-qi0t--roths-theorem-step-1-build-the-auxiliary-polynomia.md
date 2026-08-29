---
# qou-qi0t
title: 'Roth''s theorem step 1: build the auxiliary polynomial, and thereby audit Gamma_m'
status: in-progress
type: task
priority: normal
created_at: 2026-08-29T19:34:44Z
updated_at: 2026-08-29T19:41:08Z
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

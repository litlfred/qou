# The last surviving reading of `J^•` is excluded too — for every `n`, and no shift repairs it

Bean `qou-wjbd`, continuing `wpdb`. Third pass on the word-depth ↔
partition-depth bridge, after
[`2026-08-16-word-depth-vs-partition-depth-bridge-is-unstated`](2026-08-16-word-depth-vs-partition-depth-bridge-is-unstated.md)
(the identification is unstated) and
[`2026-08-16-three-gb-filtrations-one-name`](2026-08-16-three-gb-filtrations-one-name.md)
(`J^•` names three inequivalent objects; two are excluded).

**Result: the third is excluded as well, for every `n ≥ 2`, and the obvious
repair — a re-indexing — provably cannot work.** An honest negative; nothing is
closed.

## What I inherited, and the one thing in it that was too optimistic

The second audit measured the surviving **Coxeter-length** reading
`F_ℓ = span{T_w : ℓ(w) ≤ ℓ}` against the partition side and reported

| `n` | verdict |
|---|---|
| 2, 3 | **fails** |
| 4–7 | **holds** |

concluding that the exclusion "holds from `n = 4` up, so it is not an exclusion
of the identification in general."

> ### 🔻 That "holds" was a weak test passing, not the identification holding
>
> The condition tested was
>
> $$\#\{\lambda \vdash n : \mathrm{gbDepth}(\lambda) = k\} \;\leq\; \#\{w \in S_n : \ell(w) = k\}$$
>
> i.e. the partition strata against `gr_k` of the **whole algebra**. But
> `Z^{(k)}` is not a graded piece of the whole algebra. It is a graded piece of
> the filtration *induced on the centre*, `(Z ∩ F_k)/(Z ∩ F_{k-1})`, whose
> dimension is `dim(Z ∩ F_k) − dim(Z ∩ F_{k-1})` — generally far smaller than
> `#{w : ℓ(w) = k}`. Bounding by the ambient `gr_k` is sound but very lossy: at
> `n = 6` it compares against `{1, 5, 14, 29, 49, 71, 90, 101, …}` when the true
> graded dimensions are `{1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 3, 2, 1}`.
>
> Computing the actual dimension turns a one-sided **necessary condition** into
> an **equality test**, and the equality fails at every `n` tested. So the
> reading was never viable at `n = 4–7`; the earlier pass simply could not see
> it through that bound. Not a retraction of anything asserted — the ≤ test and
> its verdicts are correct as stated — but the *reading* of "holds" as
> "survives" was too generous, and it is the reason this front looked open for
> ten days.

## 1. Degree `0`: the identification is off by a shift, for **every** candidate `J^•`

This one needs no computation and is independent of which filtration `J^•`
turns out to be.

Let `F_•` be any filtration of `H_n(R, q)` by `R`-submodules with `F_{-1} = 0`
and `1 ∈ F_0` — a property every reading in the corpus has (`F_0 = R·T_e` for
the Coxeter reading; `J^0 = A` for the ideal-power one). Then

$$Z^{(0)} \;=\; (Z \cap F_0)/(Z \cap F_{-1}) \;=\; Z \cap F_0 \;\ni\; 1 \;\neq\; 0 .$$

Meanwhile the partition side's degree-`0` stratum is **empty**: `gbDepth λ =
λ₁ + λ'₁ − 1 ≥ 1` for every nonempty diagram. So

$$Z^{(0)} \;\neq\; \mathrm{span}\{e_\lambda : \mathrm{gbDepth}(\lambda) = 0\} \;=\; 0 .$$

**Scope (b) — structural exclusion.** The invariant cited is the pair *"the unit
is central and lies in filtration degree `0`"* and *"`gbDepth` is positive"*, the
latter Lean-proved sorry-free as
[`QOU.BraidKnot.gbDepth_pos`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/CentreGradingObstruction.lean).

The six sites write the identification **unshifted**, and
`phi-q-categorical-truncation-proof` writes the sum starting at `k = 0`
explicitly. So this alone refutes the literal statement. The natural response is
that the indexing is off by a constant — which §3 addresses.

## 2. The sharp measurement

[`centre_length_filtration_vs_gbdepth.py`](scripts/centre_length_filtration_vs_gbdepth.py)
builds `H_n(q)` in the `T_w` basis (AGENTS.md §7a convention,
`σ² = (q − q⁻¹)σ + 1`), solves `T_{s_i} x = x T_{s_i}` for the centre, and
intersects with each `F_k`.

**Arithmetic is exact throughout — no floating point anywhere.** Three
independent exact backends agree: `Fraction` over `ℚ` with `q` specialised,
`𝔽_p` with `p = 2⁶¹ − 1`, and fully symbolic `ℚ(q)` via sympy for `n ≤ 4`.
`dim Z = p(n)` at every sample, which certifies the specialisations generic for
the full commutator matrix. And specialising `q` can only *lower* the rank, so
every reported `dim(Z ∩ F_k)` is an **upper bound** on the generic-`q` value —
which is the direction every exclusion below needs, so no genericity has to be
assumed anywhere.

| `n` | `p(n)` | `gbDepth` strata `N_k` | `dim Z^{(k)}` (Coxeter) | word support | partition support |
|---|---|---|---|---|---|
| 2 | 2 | `{2:2}` | `[1,1]` | `{0,1}` | `{2}` |
| 3 | 3 | `{3:3}` | `[1,0,1,1]` | `{0,2,3}` | `{3}` |
| 4 | 5 | `{3:1, 4:4}` | `[1,0,0,0,1,2,1]` | `{0,4,5,6}` | `{3,4}` |
| 5 | 7 | `{4:2, 5:5}` | `[1,0,0,0,0,0,1,1,1,2,1]` | `{0,6,7,8,9,10}` | `{4,5}` |
| 6 | 11 | `{4:2, 5:3, 6:6}` | `[1,0,0,0,0,0,0,0,1,1,1,0,1,3,2,1]` | `{0,8,9,10,12,13,14,15}` | `{4,5,6}` |

The two sides do not match at any `n`, and the mismatch is not marginal: the
word side spreads over `ℓ(w₀) + 1 = n(n−1)/2 + 1` degrees (quadratic in `n`)
while the partition side occupies `n − m_n + 1` (linear). At `n = 6` that is 16
against 3. At `n = 6` the two dimension **multisets** already differ —
`{1,1,1,1,1,1,2,3}` against `{2,3,6}` — so not even an arbitrary permutation of
the index set matches, let alone an order-preserving one.

## 3. No shift repairs it, for every `n ≥ 3`

The table is a finite check. The following argument is not, and it is the real
result.

**Lemma 1.** `Z ∩ F_0 = R·1`, so `dim Z^{(0)} = 1`. Immediate: `F_0 = R·T_e =
R·1`, and `1` is central.

**Lemma 2.** For `n ≥ 3`, `Z ∩ F_1 = R·1`, so `dim Z^{(1)} = 0`.
*Proof.* Let `x = a₀ + Σᵢ aᵢ T_{sᵢ}` be central. The `a₀` term commutes. For
`|i − j| ≥ 2` the generators commute and `ℓ(sᵢsⱼ) = 2`, so `T_{sᵢ}T_{sⱼ} =
T_{sᵢsⱼ} = T_{sⱼsᵢ} = T_{sⱼ}T_{sᵢ}` and that pair contributes nothing. For
`|i − j| = 1` the elements `sᵢsⱼ` and `sⱼsᵢ` are **distinct** of length `2`, so
the coefficient of `T_{sᵢsⱼ}` in
`[x, T_{sⱼ}] = Σᵢ aᵢ(T_{sᵢ}T_{sⱼ} − T_{sⱼ}T_{sᵢ})` is exactly `aᵢ`. Centrality
forces `aᵢ = 0` for every `i` adjacent to some `j` — which is every `i` once
`n ≥ 3`. ∎ (Confirmed against the exact linear algebra at `n = 3…6`.)

**Lemma 3.** The `gbDepth` spectrum is the **contiguous** interval `[m_n, n]`,
every value attained.
*Proof.* `gbDepth λ = λ₁ + λ'₁ − 1`, so depth `d` is attained iff there are
`r, s ≥ 1` with `r + s = d + 1`, `rs ≥ n` (the `r × s` box must hold `n` cells)
and `r + s − 1 ≤ n` (the corner hook must fit). The largest product with
`r + s = d + 1` is `⌊(d+1)²/4⌋`, monotone in `d`; so if `d = m_n` is attainable
then so is every `d ∈ [m_n, n]`, and `d = n` is attained by the single row
`[n]`. ∎ (Verified for all `n ≤ 40`.)

**Theorem.** For `n ≥ 3` there is no shift `c` with
`dim Z^{(k)} = #{λ ⊢ n : gbDepth λ = k + c}` for all `k`.
*Proof.* By Lemmas 1 and 2 the word-side sequence is nonzero at `0`, zero at
`1`, and — since it totals `dim Z = p(n) ≥ 3` — nonzero somewhere above `1`. Its
support therefore has an **interior gap**. By Lemma 3 the partition-side support
has none. A shift is an order isomorphism of the index set, so it transports
gap-freeness; no `c` exists. ∎
(`n = 2` is excluded separately by the table: `[1,1]` against `{2:2}`.)

Formalised sorry-free as
[`QOU.BraidKnot.shift_cannot_fill_a_gap`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/CentreGradingObstruction.lean),
with the `n = 4` instance as `coxeter_reading_excluded_at_four`. `#print axioms`
on all five declarations returns only `propext` / `Quot.sound` /
`Classical.choice` — no `sorryAx`, no custom axiom. The algebra-side inputs
(Lemmas 1–2 and the measured `n = 4` sequence) are carried as **hypotheses**,
because `H_n(q)` and its centre are not Lean objects in this tree; the theorem
derives the exclusion from them rather than asserting it.

**Scope (b) — structural exclusion**, with the invariant cited: *the `gbDepth`
spectrum is gap-free (Lemma 3) while the centre meets `F_1` in a line only
(Lemma 2)*. Both are proved, not probed.

## 4. What this does **not** exclude — read this before citing the above

**It is not a proof that the identification is false in the abstract.** A
filtration inducing the `gbDepth` grading on the centre exists trivially —
filter by the Wedderburn blocks themselves, `F_k := ⊕_{gbDepth λ ≤ k} R·e_λ`.
What is excluded is that **any of the three things the corpus calls `J^•`** is
such a filtration. Stating it the other way round would be exactly the
over-claim AGENTS.md's scope-(a)/(b) rule exists to prevent.

**It does not touch any mass or binding number.** `J^•` enters the downstream
chain as an *indexing* — which body order an `a_D^{(n)}` belongs to, which
stratum a projector lands in — not as a magnitude. Unaffected: the Wedderburn
decomposition, the Markov trace, `tr_M`, `y_λ`, the idempotents themselves,
`gbDepth` as a definition, and `prop:gb-spectral-sequence`.

**It does not refute `prop:curvature-rank-gb-stratification`'s statement.** The
proposition is about words and may well be true of words. What fails is reading
a *partition* grading off it.

## 5. Where this leaves the consumer sites

The dilemma the second audit posed — *either* the identification means
compatibility with the length filtration (excluded at `n ≤ 3`) *or* the citation
does no work — now collapses. The first branch is excluded at **every** `n`. So:

**the citation does no work, at all six sites.** That is the finding.

The repair splits in two, and the split is worth making because one half needs
no conditionality at all:

**Class A — the site only needs the grading as a *definition*.** `Z = ⊕_λ R·e_λ`
is the Wedderburn decomposition; bucketing the blocks by `gbDepth λ` is a free
construction requiring no proposition, and `k⋆(T_w) := max{gbDepth λ : λ ∈
supp(T_w)}` is defined from the *partition* support, not from any word rank.
Sites whose downstream use is only "the centre splits into depth strata and
there are projectors onto them" are **sound as mathematics** and need only to
stop citing the word proposition. No conjecture, no §3b propagation. On
inspection `prf:phi-q-categorical-truncation` looks like this — but note its
truncation claim is then carried by the partition support alone, and
`gbDepth_const_on_H3` already showed that support is *constant* at `n = 3`, so
the claim is vacuous at the single-nucleon case whichever way this is resolved.

**Class B — the site needs genuine compatibility with the word filtration.**
`prop:jet-prefix-gb-filtration` defines `β_k^{GS} := σ_{k-3}(T_w) ∈
J^{k-3}(q)/J^{k-2}(q)`; `prf:unified-curvature-rank-mass-formula` says "by
curvature-rank stratification, `e_λ` has GB-depth `depth(λ)`". These *are* the
identification. They should be re-scoped as conditional on a named conjecture —
and the conjecture should record that **all three candidate readings of `J^•`
are now excluded**, so it is not merely open but currently without a candidate
construction. Whoever names it should not present it as a routine gap.

**Recommendation, and it is a judgement rather than a finding:** re-scope Class
B as conditional; repair Class A by re-citing rather than by adding a
conditional. Do **not** do it as a blanket edit — the six sites cite the
proposition for different things, and mechanical editing across sites whose uses
differ is how this defect got in. This pass deliberately does not rewrite them;
it updates the banners that point at the earlier audits so they no longer say
"unstated" when the sharper finding is "excluded".

## 6. What remains open

The bridge itself. Concretely: **is there a filtration of `H_n(q)`, definable
from the Gröbner–Shirshov rewriting data, whose induced grading on the centre is
the `gbDepth` grading?** The three readings in the corpus are not it. Whether
some fourth object is, nobody has tested — and §1 says whatever it is, its
degree-`0` piece is the line spanned by the unit, so it can match the partition
side only after a shift, and §3 says the shift has to move a *gap-free* spectrum
onto a sequence whose first two entries are `1, 0`. Any candidate must therefore
either fail to be an algebra filtration, or place a second central element in
`F_1` — and Lemma 2 shows the Coxeter one cannot.

That is a sharper obstruction than the one this bean started with, and it is
still an obstruction, not a closure.

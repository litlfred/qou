---
# qou-2ss0
title: 'b3Agg''s sign IS the origin-secant gap: an exact iff replacing two one-way convexity implications, and the fit trap that follows'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-13T07:58:29Z
updated_at: 2026-11-17T07:28:00Z
parent: qou-v2om
---

## Result (2026-09-13) — the convexity route analysed; convexity is the WRONG invariant

`qou-q8vl` lists "the convexity route, which is unanalysed here" as its one open
sub-item. Analysed. Lean `QOU/MassTheory/B3AggSecantCharacterisation.lean`
(10 decls, lean-direct `-DautoImplicit=false -s 65536` **exit 0**, no warnings;
`#print axioms` on all 8 theorems: **no sorryAx**, only propext / Classical.choice
/ Quot.sound).

### The identity

With `s x = Φ x / x` the origin-secant slope, for `g != 0`

    b3Agg Φ g  =  Φ(3g) − 3 Φ(g)  =  3g · ( s(3g) − s(g) )

exactly (`b3Agg_eq_secant_gap`, by `field_simp`). Hence for `g > 0`

    0 ≤ b3Agg Φ g   ↔   s(g) ≤ s(3g)        (`b3Agg_nonneg_iff_secant_le`)
    0 < b3Agg Φ g   ↔   s(g) < s(3g)        (`b3Agg_pos_iff_secant_lt`)
    b3Agg Φ g = 0   ↔   s(g) = s(3g)        (`b3Agg_eq_zero_iff_secant_eq`)

**These are iffs.** `AggregatorConvexityDichotomy` has three one-way
implications; this replaces them with the condition they were approximating.

### Finding 1 — convexity is sufficient and STRICTLY UNNECESSARY

`convexOn_sufficient_not_necessary` exhibits `Φ x = x³ − x²`: passes through the
origin, **not** `ConvexOn ℝ (Ici 0)` (it is concave near the origin, `Φ'' = 6x−2
< 0` for `x < 1/3`; the witness is that the midpoint of `[0,1/3]` sits strictly
above the chord, `Φ(1/6) = −5/216` against `−8/216`), and yet
`b3Agg Φ 1 = 18 > 0`.

So **a search for `b₃ > 0` restricted to convex aggregators is searching a
strict subset.** Global convexity is a condition at every pair of points; what
`b₃ > 0` requires is that ONE secant slope not drop across ONE fixed scale
ratio. That is a real narrowing of the open search, and it is the opposite of
what the one-line "convexity route" framing suggests.

### Finding 2 — and the route carries a fit trap, now stated as a theorem

Because the characterisation is an **iff**, the aggregator's secant behaviour
across `(g, 3g)` and the sign of `b₃` are the *same proposition*, not two facts
that could corroborate each other (`sign_carries_no_information_beyond_the_secant`).
Choosing `Φ` so that `b₃ > 0` is therefore the assumption rewritten, not evidence
for it. Under §"NO FITTING, EXCEPT CAL-1/2/3" that is **selection against the
target** in the directive's own terms: an *object* is chosen, no continuous
parameter is tuned, and the measured sign is reproduced by construction.

**The convexity route is a derivation route only if the secant condition is
derived from something that does not already know `b₃`.** Otherwise it is the
answer restated. That is the thing to check before anyone spends a tranche on it.

### Scope and what is NOT claimed

Scope (a). No aggregator is proposed, no magnitude is touched, and the
production assembly is undisturbed — `B = −α log(...)` is concave, so `b₃ ≤ 0`
there by the existing `b3Agg_nonpos_of_concaveOn`, unchanged. This narrows and
classifies the search; it derives no replacement. `qou-q8vl`'s OTHER open item —
a third bond family breaking pn-averaging or interface affineness — is untouched.

No `q`, no Markov parameter, no anchor, no CODATA value, no numeral outside the
witness polynomial. Nothing here can go stale under the convention-D migration.


## 🛑 CORRECTION 2026-09-13 — I asked the owner for a paper the corpus already HOLDS and already CITES

I told the owner, twice, that Groeneveld (1962) — the alternating-sign theorem
the whole `b₃ < 0` negative rests on — is "**NOT** in `library/`", and asked for
a PDF. **Both halves were wrong**, and the second is worse than the first.

**Held.** Measured on `library/*/sections/`: `Groeneveld` **2 documents**,
`Ursell` **6**, `Mayer` **39**, `Ruelle` **12**, `Penrose` **19**, `lattice gas`
**4**, `fugacity` **10**. `library/s10955-022-02992-6/` is **Jansen & Kolesnikov
(2022), *Cluster Expansions: Necessary and Sufficient Convergence Conditions*,
J. Stat. Phys.**, whose §3.1 states the *"well-known alternating sign property of
the Ursell function"* with the explicit sign
`(−1)^(r + Σ(|Vᵢ|−1)) = (−1)^k` and proves it as Corollary 3.3.

**And cited.** `QOU/MassTheory/UrsellPartitionFunctionB3.lean` line 21 names
`(Jansen–Kolesnikov, library/s10955-022-02992-6/, p. 5)` and line 73 carries
`-- Ref: [jansen2022cluster] https://doi.org/10.1007/s10955-022-02992-6`. The key
is in `content/schema/references.ts`; `BondArcTheorems.lean` cites it too. **The
b₃ Lean is properly sourced and always was.**

### How I got it wrong — it is the documented trap, verbatim

I ran **tier 1 only**. `INDEX.md` returns **0** for `Groeneveld`, `Ursell`,
`Ruelle`, `lattice gas` and `fugacity` while `sections/` returns 2, 6, 12, 4 and
10. AGENTS.md §corpus-grep path 5 says exactly this: *"a clean tier-1 scan is
evidence about the index, not about the library"*, and records that the index
silently went **33 real documents** stale once before. I quoted that rule to the
owner earlier in the same session and then did not apply it.

**Cheapest fix for the next agent: never conclude "not held" from `INDEX.md`.**
Run `grep -rli <topic> library/*/sections/` before saying it. It costs one
command.

## SIXTH name-collision, for `qou-r44k`

`alternating sign` → **alternating sign MATRICES**. Of the four documents
matching it, `1-s20-s009731651830061x-main` (Fischer, *Constant term formulas
for refined enumerations of Gog and Magog trapezoids*) supplies **21** of the
section hits and has nothing to do with Ursell functions; `arxiv-math-9909027v1`
is Jones, *Planar Algebras I*. So a grep for the phrase that names this bean's
own load-bearing theorem lands mostly on combinatorics of ASMs. Same class as
the five already recorded, found inside my own search path.


## 2026-09-13 — the SCALING route, from the owner's upload, and it is the shape a derivation would have

The owner uploaded `arXiv:2311.05446v3` (Aishwarya–Rotem, *New Brunn–Minkowski
and functional inequalities via convexity of entropy*). Its Brunn–Minkowski
results hold for log-concave measures with a **p-homogeneous potential** — and
that hypothesis SHAPE is what matters here, not the inequalities.

`sign_carries_no_information_beyond_the_secant` says the convexity route is a
derivation only if the secant condition comes from something that does not
already know `b₃`. **Scaling is such a something.** A homogeneity degree is
fixed by how the assembly law behaves under rescaling the bond weight; it is not
a curvature picked to fix a sign.

Four new theorems (lean-direct exit 0, all four `#print axioms` clean):

    b3Agg_of_scales                    Φ(3g) = c·Φ(g)  ⇒  b₃ = (c − 3)·Φ(g)
    b3Agg_pos_iff_scale_gt_three       with Φ(g) > 0:   b₃ > 0  ↔  c > 3
    b3Agg_eq_zero_iff_scale_eq_three                     b₃ = 0  ↔  c = 3
    b3Agg_pos_iff_exponent_gt_one      Φ(3g) = 3^p·Φ(g): b₃ > 0  ↔  p > 1

The first three need **no convexity, no differentiability and no hypothesis on
`Φ` anywhere else** — strictly more general than the power law, since `c` is any
scaling factor. Verified in exact `Decimal` at `p = 0.5, 1, 1.5, 2, 3` against
the direct cumulant before the Lean was written; all five agree exactly, signs
`−, 0, +, +, +`.

### Why this is the useful reformulation

**`p = 1` is additive superposition and gives exactly zero** — the affine
boundary `b3Agg_linear_eq_zero` is the linear instance of. **`p < 1`, where a
concave law such as a logarithm sits, gives a negative cumulant.** So the open
question moves from

  *"why should the aggregator curve upward?"*   (a curvature — the fit trap)

to

  *"is the assembly law SUPERLINEAR in the bond count, and why?"*   (a scaling)

That second question is about how the law responds to rescaling, which the
framework can in principle settle **without reference to the measured sign**.
It is the first formulation of this open item that is not circular by
construction.

**NOT claimed:** that the framework's assembly IS superlinear, that `p > 1`, or
any value of `p`. Scope (a). No aggregator is proposed and the magnitude is
untouched. Asserting `p > 1` because it yields `b₃ > 0` would be the same
selection-against-target this file exists to name — the requirement is a derived
scaling degree, not a chosen one.


## 2026-09-13 — `qou-q8vl`'s SECOND escape route is narrower than it was stated

`qou-q8vl` records the open escape for a third bond family as: *"it must break
the AVERAGING of the pn letter, or break AFFINENESS of the interface law."*
**The second half is too weak.** Measured, then proved.

`QOU/MassTheory/InterfaceMonotoneBlocksSignMixed.lean` (12 decls, lean-direct
exit 0, `#print axioms` clean — and the three order-core theorems depend on
**no axioms at all**).

### What actually blocks the pattern

Affineness is not the invariant. **Monotonicity is.** If `f` is monotone in
*either* direction and `c` lies between `a` and `b`, then `f c` cannot strictly
exceed both `f a` and `f b` — no linearity, no continuity, no algebra. The
hypothesis is an order property and each proof is one `lt_of_lt_of_le` against
`lt_irrefl`.

Checked in exact `Fraction` before the Lean, at `a, c, b = 0, 1, 2`:

    affine increasing   3x+5      c strict max?  NO
    affine decreasing  -3x+5      c strict max?  NO
    monotone NON-affine  x³       c strict max?  NO   <-- the point
    antitone NON-affine -x³       c strict max?  NO
    NON-monotone       1-(x-1)²   c strict max?  YES  <-- only escape

`PnBetweennessBlocksSignMixed.pn_not_strict_max` is the `f = (z + ·)` instance
of `pn_not_strict_max_of_monotone`.

### Consequence for the open search — this is the usable part

**A third bond family that merely abandons affineness gains nothing.** A cubic
interface law `d ↦ d³` is as blocked as `d ↦ z + d`. The escape requires a
**non-monotone** law, a strictly stronger demand over a much smaller space.

So the cheap filter, before any number is computed: *is the candidate law
monotone?* If yes, the sign-mixed pattern is already excluded and the
construction is dead. That turns a vague "break affineness" into a
one-line test.

`hump_realises_strict_max` / `nonmonotone_escape_exists` show the narrowing is
**sharp** rather than a disguised impossibility — the downward parabola
`1 − (d−1)²` does put the middle strictly above both endpoints. So monotonicity
is exactly the invariant, not a sufficient condition standing in for something
weaker.

### Scope

Scope (b); the invariant is order-preservation, an identity rather than a
measurement. **NOT claimed:** that a non-monotone interface law exists in the
framework, is derivable, or is physical. Physically it would mean a larger letter
offset *decreasing* the bond factor over some range and increasing it over
another; whether the framework admits that is open and untouched here.
`qou-q8vl`'s *first* escape — breaking the pn averaging — is also untouched.


## 2026-09-13 — the THIRD escape is NOT loose, and I nearly claimed it was

Two of `qou-q8vl`'s hypotheses turned out stronger than needed — aggregator
**convexity** weakens to a two-point secant condition, interface **affineness**
weakens to monotonicity. I pattern-matched and went looking for the same gain in
the third, that the pn letter is a strict convex **combination**, expecting it to
weaken to mere **betweenness**.

**The arithmetic refused it, before any Lean was written.** Over an ordered field
the two are the SAME condition: any `c` strictly between `a` and `b` is
`combo w a b` with the weight read off as `w = (b−c)/(b−a) ∈ (0,1)`, exactly.
My probe looked like it showed a gap only because the value I picked to be
"between but not a combination" (`d_pn = 7` against `0, 10`) **is** a combination,
at `w = 3/10`.

Proved rather than left as a remark, so the tightness is on record:

    combo_of_between   a < c < b            →  ∃ w ∈ (0,1), combo w a b = c
    between_of_combo   w ∈ (0,1)            →  a < combo w a b < b
    between_iff_combo  (a < c ∧ c < b)      ↔  ∃ w ∈ (0,1), combo w a b = c

lean-direct exit 0; `#print axioms` clean on all three.

### Consequence — the escape analysis is now COMPLETE

| hypothesis | status |
|---|---|
| aggregator **convexity** | weakens → secant monotonicity across one scale ratio |
| interface **affineness** | weakens → order-monotonicity |
| pn **averaging** | **already tight** — no sharpening exists |

So the full characterisation of what a third bond family must do is:

  **`d_pn` must lie OUTSIDE the interval spanned by `d_pp` and `d_nn`,
   OR the interface law must be NON-MONOTONE.**

Nothing weaker will do, and those are the only two doors. That closes
`qou-q8vl`'s open-escape question as a question — it does not derive a family
through either door, and neither door is shown to be reachable in the framework.

**Method note worth keeping.** The pattern "the corpus stated a sufficient
condition where a weaker one is the real invariant" held twice and then failed.
Two instances is not a rule. The check that caught it cost one `Fraction`
computation against a would-be counterexample; the claim would have cost a
retraction.


## LANDED 2026-09-13 on `main` (merge `3cb26d4b9f8`) — and the arc grew a second file

This bean's Result section above covers the **convexity/secant** half. The same
arc also produced `QOU/MassTheory/InterfaceMonotoneBlocksSignMixed.lean`, which
answers the OTHER half of `qou-q8vl`'s escape question.

### `qou-q8vl` asked for two doors; both are now measured

That bean records the escape for a third bond family as *"break the AVERAGING of
the pn letter, or break AFFINENESS of the interface law."*

**Affineness is not the invariant — MONOTONICITY is.** A monotone interface law
in EITHER direction keeps the middle value in the middle
(`not_strict_max_of_monotone`; the proof is one `lt_of_lt_of_le` against
`lt_irrefl`, and the three order-core theorems depend on **no axioms at all**).
Checked in exact `Fraction` before formalising:

| law | middle is strict max? |
|---|---|
| affine, increasing or decreasing | no |
| **monotone non-affine (`x³`)** | **no** |
| **non-monotone (`1 − (x−1)²`)** | **yes** — the only escape |

So a family that merely abandons affineness gains **nothing**.
`nonmonotone_escape_exists` shows the narrowing is **sharp**, not a disguised
impossibility.

**Averaging, by contrast, is already tight — and I expected otherwise.** I
pattern-matched the first two weakenings (convexity → secant monotonicity,
affineness → order-monotonicity) and predicted a third, averaging → mere
betweenness. **Exact `Fraction` arithmetic refused it.** Over an ordered field
the two are the SAME condition: `between_iff_combo`, with the weight read off
explicitly as `w = (b−c)/(b−a)`. My probe looked like it showed a gap only
because `d_pn = 7` against `(0, 10)` *is* a combination, at `w = 3/10`.

### Net, and what stays OPEN

> A third bond family must put **`d_pn` outside the interval spanned by `d_pp`
> and `d_nn`**, or use a **non-monotone interface law**. Nothing weaker will do;
> those are the only two doors.

This closes `qou-q8vl`'s escape question **as a question**. It derives no family
through either door and shows neither reachable in the framework — so the open
mathematics (does `b₃ > 0` happen; the extensive term of `qou-brng`) is
untouched. **Left in-progress deliberately** per AGENTS.md §13a: the subject is
an open conjecture, and recording that it is open is not closing it.

Also §7c: `check-sidecars.sh` flagged this file "MIXED generic + archimedean"
before commit; the `hump` witness did not need `ℝ` and was made generic over an
ordered field. The preflight caught it, not review.


## 2026-09-13 — the non-monotone door, and what actually blocks the affine one

Chased the one escape `InterfaceMonotoneBlocksSignMixed` leaves open. Seven new
sorry-free declarations in that file (`lean`-direct exit 0, **zero warnings**,
`#print axioms` clean).

**A gap in my own earlier work.** `pn_not_strict_max_of_monotone` and
`signMixed_impossible_of_monotone` assume `Monotone`, so a **decreasing**
interface law was never covered — although `not_strict_max_of_antitone` was
sitting in `OrderCore` unused. Both antitone halves added.

**The structural reason `μ = z + d` is blocked.** The interface factor is a
Markov trace ratio `μ(x) = tr_M(W·x)/tr_M(W)` at fixed `W`, and the numerator is
**linear in `x`**. So along any *affine* path in the algebra `x(t) = x₀ + t·x₁`
the law is affine in `t`; an affine law is monotone or antitone by the sign of
its slope, hence blocked **either way**. `μ = z + d` *is* that affine path.

So the escape must **leave the affine family, not merely the affine formula** —
which is a sharper statement than "be non-monotone", and it is checkable without
computing a bond value.

**The framework does admit such a family, and the corpus already measured it.**
The file header said *"whether the framework admits such a thing is open and is
not addressed here"*. `m ↦ σ^m` is not an affine path (a product, not a sum), and
its interface factor is measured non-monotone in `m`: `μ > 1` at
`m = 2, 4, 5, 6, 7, 8` and **not** at `m = 3`
(`stacked_interface_writhe_normalised_probe.py`, via
[`2026-09-12-b3-sign-one-root-and-the-insufficient-escape.md`](docs/audits/2026-09-12-b3-sign-one-root-and-the-insufficient-escape.md)
§6(b)). Over a threshold at 2 and 4 but not 3 is not monotone.

**This selects nothing.** Naming the family occupying the door is structural;
picking an `m` because it yields `b₃ > 0` is selection against the target
(§NO FITTING), and `qou-kj4v` records that running backwards for `σ²`. Under
`qou-ales` the braid word is selected by γγ + the confinement SDP, and **that
derivation is what stays open.** Scope (a); no family derived through the door.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-13 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## 2026-11-15 — re-scoped by the γγ rule

The owner ruled that the γγ selection rule also covers the nuclear bond letters. Any number in this bean computed on the single-crossing interface letters of `atom_braid_word_3A` (`d_k`, `μ_e`, the chain law `∏(z_D + d_k)`, the `b₃` magnitudes −1.2277 / −0.7973 MeV, or a sign map on that word) is now a record of a superseded word, not a current result. Lean results stated for generic bond weights are unaffected. The redo waits on a γγ-selected word per nucleus (PR #7876). Record: `docs/audits/2026-11-15-gg-rule-rescopes-old-letter-binding.md`. The bean stays open.

## Round 62 Update (PR #8255)
- Formalized in PR https://github.com/litlfred/qou/pull/8255 (head `b4ec4b15ca43f486c66d8f53b0eeb216293fc6aa`, Commit 1 `c715790dad2efe16f1713c8a17825e912524e641`, `scriptHash: e2eb499467fc`).

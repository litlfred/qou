---
# qou-rstq
title: 'ROAST QUEUE: every open 5₂ claim needing adversarial review, with what specifically to attack'
status: in-progress
type: task
priority: high
tags:
    - qbeta
    - 5two
    - review
    - roast
    - reorg-2026-10-04
created_at: 2026-08-07T22:05:00Z
updated_at: 2026-10-04T15:15:05Z
parent: b9cj
---


## Purpose

The 5₂ chain now spans six beans and two Lean files, and **most of it is
verified-not-proved**. This is the index of what is still open, and — more
usefully — **what specifically to attack in each**. A reviewer should be able to
start here.

**Standing status: sum rule verified to 80 dps, unproved.**

## The chain, and where each link actually stands

| link | bean | status | roast target |
|---|---|---|---|
| transport `x=1 → x=−1` | `qou-trns` | branch **pinned**; envelope **true but unformalized** | the envelope theorem is confirmed *numerically* only |
| cyclotomic identity | `qou-8v3k` | reduction, not proof | the `S(x) = S(1) − log²x` integration |
| rationality | `qou-b7cy` | proved **on paper**, via Borel | not formalizable — see `qou-mlbg` |
| numerators `(17,5,−1)` | `qou-fivt` | **derived**, Lean-checked | rests entirely on `qou-rhyp`'s nine hypotheses |
| the nine hypotheses | `qou-rhyp` | **all unproved** | five-term is the real one |
| complex `Li₂` | `qou-clx8`, `qou-ph1k`, `qou-gkco` | open | statement verified true; proof open |

## What to attack, concretely

1. **`qou-rhyp`, the five-term instances.** Everything downstream is a
   `linear_combination` over these. If any of `hA`, `hB`, `hC` is not a genuine
   five-term instance — wrong argument, wrong branch — the whole derivation
   collapses. They were checked numerically to `1e-40`; check the *algebra* of
   the arguments independently.
2. **`qou-trns`, the envelope step.** Confirmed by finite differences, which is
   evidence, not proof. The IFT hypothesis (`min |disc| = 0.348`) was measured on
   a sampled arc — a finer sweep could in principle find a near-collision.
3. **`qou-b7cy`'s "rationality is PROVED".** True modulo Borel's theorem, which
   `qou-mlbg` shows is nowhere near Mathlib. Read that claim as *proved on paper,
   unformalizable*, and check nothing downstream silently upgrades it.
4. **Route 8's `k = 0`.** Now pinned by `g(1) = 0` rather than local constancy —
   stronger, but still assumes continuity of the root branches, which rests on the
   same discriminant sampling as (2).

## ⚠ The recurring failure mode in this work — check for it first

**Principal-vs-continuous `Log` has produced a spurious `2π` three separate
times** (`qou-trns`). Every one looked like a real discrepancy. If a probe here
reports a mismatch that is a multiple of `2π` or `π²`, suspect the branch
convention **before** suspecting the mathematics.

Related, from `qou-b7cy`: a per-embedding formula `V − L(ξ) = iπ·log[(1−w)/w]`
was tried and **is false** — it fails at two of three embeddings while the *sum*
is exact. Sum-level agreement does not imply term-level correctness.

## Known dead ends — do not re-run

* **PSLQ over `[L1, L(w₂), L(q), L(r), L(s)]`** returns `[−4,4,−3,4,3]`, which is
  a linear consequence of the targets and carries **no** information (`qou-fivt`).
* **The Galois/Möbius `T`-orbit** (`1/wₖ = 1 − w_{k+1}`) is real structure, but the
  orbit sum is **irrational** — the 3-cycle alone yields nothing (`qou-fivt`).
* **The `ℂ/2π²ℤ` modulus hypothesis** — refuted; the branch shift is a multiple of
  both moduli (`qou-r7ml`).
* **GGM / GGMW** contain no saddle-sum; `Σⱼ Vⱼ` appears nowhere (`qou-g2wr`).
* **"Formalize Borel first"** is a multi-year programme, not a plan (`qou-mlbg`).

## Two errors formalisation caught that numerics did not

Worth remembering when judging how much to trust the probes:

1. The certificate's **R-labels were permuted** against its coefficients — exact
   rational arithmetic confirmed a *rank* statement blind to which row was which.
2. The **divided form is false in characteristic 7**; `ring` refused it and
   `char_seven_forces` now proves the hypotheses force `3·L1 = 0` there.

## Also open, lower priority

* `qou-mfst` — `lake-manifest.json` still lists `«doc-gen4»` after `qou-dg4x`
  commented the `require` out. Harmless, deliberate, tracked.

## Refs

* parent `qou-0yqu`; PRs #4658 (merged), #4701

---

## 2026-08-07 — critical-path clarification, and a correction to `qou-mlbg`

**The `B₂`-Fourier fact is NOT on the critical path.** Worth stating, because two
beans describe it as the thing to attack first.

Route 10 framed the sum rule as a distribution relation
`Re[2L(wₖ)+L(−wₖ)] = (7/2)·Re Li₂(ζ₇^k) + π²/4`, which needs
`Re Li₂(ζ₇^k) = π²B₂(k/7)`. **Route 11 supersedes that framing**: it derives the
numerators from the five-term relation directly, never touching `Li₂` at roots of
unity. So the `B₂` fact is *explanatory* — it says why the numerators are a
Bernoulli polynomial — and **load-bearing for nothing**.

Prioritise `qou-rhyp` (the nine hypotheses) over the `B₂` half. `qou-fivt`'s
"Next: derive the `Re Li₂(ζ₇^k)` half first" predates Route 11 and is now the
wrong advice.

**Separately — `qou-mlbg` has been corrected.** Its zero-counts stand, but the
conclusion drawn from them was too broad: Mathlib *does* carry the `B₂` Fourier
fact, as `hasSum_one_div_nat_pow_mul_cos` in `NumberTheory/ZetaValues.lean`
(at `k = 1` the constants collapse to exactly `π²`). **The survey searched for the
objects it would have named — `Polylog`, `dilog`, `Rogers` — and missed the
content sitting under a different one.**

**Roast target added:** re-run that survey's logic against the *other* gaps before
concluding anything is absent. Specifically, `qou-rhyp`'s inversion and Landen
extensions were called "not in Mathlib" on the same reasoning that just failed
once. That reasoning is now suspect. Mathlib genuinely has no `Li₂`, so those two
probably *are* absent — but "probably" is exactly the word the earlier survey did
not use, and should have.

---

## 2026-08-07 — ROAST ITEM 1 DISCHARGED, and two new items

### Item 1 (the five-term instances) — closed

> "If any of `hA`, `hB`, `hC` is not a genuine five-term instance — wrong
> argument, wrong branch — the whole derivation collapses. They were checked
> numerically to `1e-40`; **check the *algebra* of the arguments independently**."

Done, twice and independently:

* `computations/probes/qbeta_5two_route14_fiveterm_arguments_exact_probe.py` —
  **exact arithmetic** in `ℚ(w)`, `w³ = 2w² + w − 1`, `fractions.Fraction` in the
  power basis. No floating point anywhere in the argument matching, so a
  near-miss cannot pass. 6 gates, all pass.
* `QOU/QBeta/FiveTwoFiveTermArguments.lean` — the same six identities in Lean,
  over any `Field`, sorry-free, axioms `[propext, Classical.choice, Quot.sound]`
  (three need only `propext, Quot.sound`; `ne_zero_of_hs` only `propext`).

**All three are genuine.** The relation's last three arguments are determined as
rational functions of `(x,y)`, and they match the hypotheses' arguments
identically:

| | instance | last three arguments |
|---|---|---|
| `hA` | **diagonal**, `x = y = w₂` | `{1−q, r, r}` |
| `hB` | `x = 1−w₂`, `y = q` | `{1−q, 1−s, w₂}` |
| `hC` | `x = w₂`, `y = s` | `{1−w₂, 1−s, 1−r}` |

Three findings worth keeping:

1. **`hA` is the diagonal instance**, which is why it has coefficients `(2,−1,−2)`
   rather than the five-term's `(1,1,−1,−1,−1)` — two arguments coincide. Its
   identification `w₂² = 1−q` is **exactly `bloch_key`**, already sorry-free in
   `FiveTwoCyclotomicBloch.lean`.
2. **`bloch_key` appears twice.** It also fixes `hC`'s last argument (`arg_C2`).
   The identity that made the Bloch element `2[w] + [−w]` work is the same one
   that makes the five-term arguments close up. Stated as `bloch_key'` so the
   connection is a `linear_combination`, not a comment.
3. **Three of the six identities need nothing at all** — `arg_A2`, `arg_B1`,
   `arg_C1` hold for every `x`. Only `arg_A1`, `arg_B2`, `arg_C2` use the cubic.
   The denominators `1 − xy` collapse (to `q` for `hB`, to `x` for `hC`), which is
   why two of the five arguments come out with no denominator left.

In the generator `x = w₂` the whole dictionary is `q = 1/(2−x)`, `r = x/(x+1)`,
`s = (1−x)/x` — worth knowing, since `w₂ = σ(w₁)` is also a root of the same
cubic and everything is simpler there.

### 🔥 New roast items

4. **The extended Rogers `L` is a *choice*.** `qou-rhyp` now shows `hinv1` and
   `hlan1` were **false** for a Rogers `L` built on the corpus `LiTwo` (junk
   values off `[−1,1]`), and repairs them by *defining* the extension. The
   piecewise function is **not proved equal** to the analytic continuation of
   `Li₂`; agreement is checked at six points. Attack that gap — it is the one
   this lane created rather than inherited.
5. **48% of the QOU Lean library is never compiled** (`qou-orph`, measured:
   761/1598). Every "sorry-free, axioms audited" claim in this lane — including
   the file merged in #4658 — rested on hand-run targeted builds, not on
   anything the repo maintains. Three modules are now wired into `QOU.lean`;
   758 are not. **Do not read any axiom audit in this repo as a maintained
   property until that is fixed.**

### Where the chain now stands

| link | status |
|---|---|
| five-term **instances** | ✅ **proved genuine**, exactly + in Lean |
| five-term **relation** (Abel) | ❌ the one open analytic input to the numerators |
| inversion / Landen | ✅ by construction (`FiveTwoRogersExtend`) |
| reflection | proof written, build unfinished |
| transport `x=1 → x=−1` | envelope true but unformalized (`qou-trns`) |
| extension = analytic continuation | ❌ **new gap**, item 4 above |

**Standing status, unchanged: the 5₂ sum rule is verified to 80 dps, unproved.**

---

## 2026-08-08 — roast item 4 refined, and a correction to how I framed it

### Correction: the corpus DOES have a complex dilogarithm

When Route 15 reduced roast item 4 to "`Li₂` inversion and `Li₂` Landen", I wrote
that neither is in Mathlib and implied there was nothing to build on. The Mathlib
half is right. The implication is **wrong**:

`QOU/MathlibExt/ComplexDilogarithm.lean` already has, sorry-free —

* `cLiTwo` by its power series, with `cLiTwo_analyticOnNhd` on the unit ball;
* `cLiTwo_eq_intervalIntegral` — the integral representation on the disc;
* `cLiTwoExt y := −∫₀¹ log(1 − yz)/z dz`, **defined for every `y`** (junk-valued
  where the integrand is not integrable, per Mathlib convention);
* `cLiTwoExt_eq_cLiTwo` on the disc, plus the integrability lemmas.

**This is the second time in this lane that a "we don't have X" conclusion came
from searching for a name rather than a statement** — the first was
`hasSum_one_div_nat_pow_mul_cos` in `qou-mlbg`. The lesson did not stick the
first time. Before writing "the corpus has no …", grep the corpus.

### The refinement: item 4's two halves are NOT equally hard

Roast item 4 needs `extend` identified with `Re` of the analytic Rogers `L` at
`w₁ = +2.2470` (inversion branch) and `−w₁ = −2.2470` (Landen branch). Those are
in different situations:

* **Landen half, `x < 0`.** `−w₁` is far from the cut `[1,∞)`, the defining
  integral converges, and `cLiTwoExt` is *already the right object there*. What
  is missing is the Landen identity itself.
* **Inversion half, `x > 1`.** `w₁` lies **on** the cut. `cLiTwoExt` is not the
  right object at a point of `[1,∞)` — one needs `Re` of the boundary value,
  which is well defined precisely because the discontinuity across the cut is
  `2πi·log x`, i.e. **purely imaginary**. That fact is what the whole lane's
  "take real parts" convention rests on, and it has never been stated anywhere.

So the inversion half carries an extra step nobody had written down. **Do not
plan item 4 as one job.**

### `ComplexDilogarithm.lean` is itself orphaned

It is **not** imported from `QOU.lean`, so `lake build` never compiles it —
a ~500-line sorry-free complex dilogarithm that nothing in the repo checks.
Exactly `qou-orph`'s thesis, in the file this lane most depends on.

### A near-miss worth recording

`grep -c "sorry" ComplexDilogarithm.lean` returns **3**, and all three are in the
module docstring, in prose asserting the file *is* sorry-free. I nearly recorded
"3 sorries" as a defect. **A count is not a finding until you have looked at the
lines.**

---

## 2026-08-08 — ROAST ITEM 2 RESOLVED, and it found a real defect

Item 2 read:

> "`qou-trns`, the envelope step. Confirmed by finite differences, which is
> evidence, not proof. The IFT hypothesis (`min |disc| = 0.348`) was measured on
> a sampled arc — **a finer sweep could in principle find a near-collision**."

It is not a near-collision. **The discriminant vanishes exactly on the arc**, at
`θ = 137.9206708879635°`, where two of the three `y`-branches meet
(`y₂ = y₃ = −1.13224188…`). `min |disc| = 0`, not `0.348`.

Proof needs no numerics: `disc` is palindromic, so `disc(x)/x⁴ = Q(x + 1/x)` with
`Q(u) = u⁴ − 6u³ + 7u² + 6u − 31`; points of `|x| = 1` are real `u ∈ [−2,2]`; and
`Q(−2) = +49`, `Q(−1) = −23` in integers, so IVT gives a root. Full record in
`qou-trns` and `qbeta_5two_route16_discriminant_vanishes_probe.py`.

**This reopens `qou-trns` sub-gap 1** (`k = 0` was "PINNED"; its continuity step
is false) and falsifies the envelope theorem's IFT hypothesis.

### The methodological point — this is the fourth of a kind

`0.348` was a **grid minimum reported as a true minimum**. Refining the scan
gives 0.068, then 0.0068, then 0. Of a piece with the other measurement failures
this lane has logged:

1. a probe whose printed verdict its own data contradicted;
2. principal-vs-continuous `log`, **four** times;
3. `grep -c "sorry"` returning 3 for a file whose three hits were docstring prose
   asserting it *is* sorry-free;
4. **this one** — a sampled extremum quoted as an exact one.

All four share a shape: **a number was produced by a procedure, and then quoted
without the procedure.** When a bean states a constant, it should state how it
was obtained, so the next reader can see what would falsify it.

### Roast target added

**Every remaining numerically-obtained constant in this lane is suspect until
its procedure is stated.** In particular `qou-8v3k` and `qou-trns` both quote
`min |disc| = 0.348`; both are now wrong. Sweep for others.

---

## 2026-08-08 — a claim of mine, corrected by the literature

I wrote, in the item-4 refinement above, that the purely-imaginary jump of `Li₂`
across the cut `[1,∞)` "underpins this lane's whole 'take real parts' convention
and **is written down nowhere**."

**It is written down.** Zagier, *The Dilogarithm Function*, Ch. I §3:

> "The function `Li₂(z)`, extended as above to `ℂ ∖ [1,∞)`, **jumps by
> `2πi·log|z|`** as `z` crosses the cut."

Standard, and the lane should cite it rather than treat it as folklore. The
*refinement* stands — item 4's two halves really are unequal, and the inversion
half really does need the boundary value — but the missing ingredient is a
citation, not a discovery.

**And the bigger one:** the level-7 ladder is **Watson (1937)** (Kirillov §1.2.2).
`qou-fivt` and `qou-abel` are annotated. The Lean work is a formalization of a
classical identity family; the derivation route (five-term rather than
duplication) and the formalization itself are what is new. Presenting the
numerators as "DERIVED" carried an implication of novelty that is withdrawn.

**Roast target added:** sweep this lane for other claims of the form "not in the
literature" / "written down nowhere" / "new". Two have now failed —
`hasSum_one_div_nat_pow_mul_cos` in Mathlib (`qou-mlbg`), and this. The lane has
a pattern of asserting absence without searching.

---

## 2026-08-08 — item 4 attacked: `extend` IS `Re L`, measured; Landen's core proved

Route 33 (`qbeta_5two_route33_extend_identification_probe.py`, 6 gates, 50 dps) +
`QOU/MathlibExt/ComplexDilogarithmLanden.lean` (4 theorems, sorry-free, lake
green).

### Why this became the sharpest item

Route 32 reduced the 5₂ sum rule to the level-7 bridge, which rests on Lean's
`extended_sum` — stated for the **piecewise** `extend`, while the bridge computes
with the **analytic** Rogers `L`. Item 4 is now the last non-transport link, and
everything around it is proved.

### Measured

`extend (π²/6) rogersL x = Re L_analytic(x)` to **1e-50**, at the six arguments
`extended_sum` actually uses — the level-7 orbit `{1/(1−x), x, (x−1)/x}` and its
negatives — and across all three regimes on 81-point sweeps.

### Proved this round

The **analytic core of the Landen leg**:

    d/dz [ Li₂(z) + Li₂(z/(z−1)) + ½·log(1−z)² ] = 0     (`hasDerivAt_landenCombo`)

The three derivatives are `−log(1−z)/z`, `−log(1−z)/(z(z−1))`, `log(1−z)/(z−1)`,
and they cancel because `−1/z − 1/(z(z−1)) + 1/(z−1) = 0` identically. The branch
condition is isolated as `1 − z ∈ slitPlane` and **shown load-bearing** (G6): at
`z = 3` the step `log(1 − z/(z−1)) = −log(1−z)` fails by exactly `2πi`.

This is precisely what `ComplexDilogarithm.lean` lists as *not* provided: "the
inversion formula … Note this is **false** for `cLiTwo` at `‖z‖ > 1`".

### What is still missing, per regime (G5)

| regime | status |
|---|---|
| `0 ≤ x ≤ 1` | **nothing** — `cLiTwo_ofReal` already bridges the corpus's `LiTwo` |
| `x < 0` (Landen) | analytic core **proved**; remaining: the base value `Li₂(−1) = −π²/12` |
| `x > 1` (inversion) | **harder, not attempted** — see below |

The Landen base value is one special value, and the corpus's
`rogersL_reflection` already supplies the partner `rogersL(½) = π²/12` at the
natural base point `z = −1`. Mathlib has `hasSum_zeta_two` (`π²/6`) but no
alternating analogue, so it is not free.

**The inversion leg is the sharper obstacle.** `x > 1` lies *on* `cLiTwoExt`'s
cut — `notCut = {w | Im w ≠ 0 ∨ Re w < 1}` excludes it — so it needs a
**boundary value from off the cut**, not merely a constant of integration. That
is new analytic infrastructure. Exactly **one** of the six arguments is in that
regime (`w₁ = 2.24698`, the same value that falsified `hinv1`), and it cannot be
avoided.

**The 5₂ sum rule remains verified to 80 dps, unproved.**

### 2026-08-08 (later) — the Landen base value, and a Mathlib gap filled

`QOU/MathlibExt/AlternatingZetaTwo.lean` + `QOU/Archimedean/LiTwoNegOne.lean`
(3 theorems, sorry-free, lake green).

Route 33 G4 named `Li₂(−1) = −π²/12` as the single value standing between
`hasDerivAt_landenCombo` and Landen. It is now proved.

**The Mathlib gap.** Mathlib has `hasSum_zeta_two` (`Σ 1/n² = π²/6`) but **no
alternating analogue**. `hasSum_alternating_zeta_two` supplies it, by splitting
the index into even and odd:

* odd index gives `Σ 1/(2k+2)² = ¼·Σ 1/(k+1)² = π²/24`;
* hence even index gives `Σ 1/(2k+1)² = π²/6 − π²/24 = π²/8`;
* the alternating series has the same two pieces with the even one negated, so
  it sums to `−π²/8 + π²/24 = −π²/12`.

That file imports **only Mathlib**, so it can go upstream unchanged — the same
discipline `ComplexDilogarithm.lean` follows. `LiTwo_neg_one` and
`cLiTwo_neg_one` are the corpus-side corollaries, the latter through
`cLiTwo_ofReal`.

**Two probe claims corrected in the same commit.** Route 33's G4 said "Lean does
NOT have this yet" and G5 said the Landen leg still needed the base value. Both
became false the moment this landed, and both are now rewritten to say so
explicitly rather than quietly. That is the third time in this branch a probe
claim has had to be corrected because the work moved past it.

**Item 4 status now:**

| regime | status |
|---|---|
| `0 ≤ x ≤ 1` | done (`cLiTwo_ofReal`) |
| `x < 0` (Landen) | analytic core **proved**, base value **proved**; remaining: only the zero-derivative-to-identity connectedness step |
| `x > 1` (inversion) | **the real obstacle** — on `cLiTwoExt`'s cut, needs boundary values, new infrastructure |

**The 5₂ sum rule remains verified to 80 dps, unproved.**

### 2026-08-08 (later still) — the boundary infrastructure, and the base value in the form Landen consumes

`QOU/MathlibExt/ComplexDilogarithmBoundary.lean` (2 theorems) +
`cLiTwoExt_neg_one` in `QOU/Archimedean/LiTwoNegOne.lean`. Sorry-free, lake
green.

**The gap that was hiding.** `LiTwo_neg_one` gave `Li₂(−1) = −π²/12` for the
*series*. But `hasDerivAt_landenCombo` is about `cLiTwoExt`, and
`cLiTwoExt_eq_cLiTwo` holds only on the **open** disc — while `−1` sits on the
boundary. Every base point worth using for a dilogarithm identity is on that
boundary (`−1` for Landen, `1` for reflection), so the open-disc statement is
exactly one point short wherever it is needed.

**What was built**, stated for *every* boundary point off the cut rather than
for `−1`:

    ‖y‖ ≤ 1  and  y ∉ [1,∞)   ⟹   cLiTwoExt y = cLiTwo y

Three ingredients, no new estimates:

* `continuousOn_cLiTwo_closedBall` — the series is dominated on the **closed**
  disc by `1/(k+1)²`, summable via `summable_one_div_succ_sq`, so
  `continuousOn_tsum` applies. The Weierstrass M-test, and the only place the
  boundary is touched.
* `cLiTwoExt` is continuous at `y` because it is analytic on `ℂ ∖ [1,∞)` —
  `analyticOnNhd_cLiTwoExt`, the theorem `ComplexDilogarithm.lean` flags as its
  own missing piece.
* they agree on the open disc, whose closure contains `y`, so the
  within-neighbourhood filter is `NeBot` and the limits must agree.

⚠ **It does not reach `[1,∞)`.** That boundary is *on* the cut, `cLiTwoExt` is
not defined there, and no continuity argument in that file applies to it. This
is stated in the module docstring rather than left implicit, because the
inversion leg is exactly what needs it.

**Item 4 status:**

| regime | status |
|---|---|
| `0 ≤ x ≤ 1` | done |
| `x < 0` (Landen) | analytic core proved, base value proved **in the form the argument consumes**; remaining: the zero-derivative-to-identity connectedness step |
| `x > 1` (inversion) | **unchanged — the real obstacle**, and now precisely bounded: it is the one thing the new boundary theorem deliberately cannot reach |

**The 5₂ sum rule remains verified to 80 dps, unproved.**

---

## 2026-08-08 — ITEM 4: the Landen regime is CLOSED. One argument left, in one regime.

Two theorems, both sorry-free, both `lake`-verified, both axioms
`[propext, Classical.choice, Quot.sound]`:

```
QOU/MathlibExt/ComplexDilogarithmLanden.lean   (PR #4776)
  landenCombo_ofReal_eq_zero : ∀ {t : ℝ}, t < 0 → landenCombo (t : ℂ) = 0
      i.e.  Li₂(t) + Li₂(t/(t−1)) + ½·log(1−t)² = 0

QOU/QBeta/FiveTwoExtendIdentification.lean     (PR #4701)
  extend_eq_re_cRogersL_of_neg : ∀ {x : ℝ}, x < 0 →
      extend (π²/6) rogersL x = (cLiTwoExt x + log x · log(1−x) / 2).re
```

The second is the one this item actually asked for, in the `x < 0` regime.

### The base point is why this closed now and not earlier

The zero derivative was already proved (Route 33 G3). What was missing was the
constant, and the obvious base point `z = −1` needs `Li₂(½) = π²/12 − ½·log 2²`
— **not in Mathlib**. Pinning at the *limit* `z → 0⁻` instead needs no special
value at all: every term vanishes there. `Ico t 0` already excludes the one
point where the derivative hypotheses fail, so the endpoint costs only a
continuity lemma. Route 34 G3 checks the economy is real (each of the three
pieces at `−1` is individually nonzero), not a stylistic preference.

### Status per argument, which is now the honest unit

`extended_sum` uses six arguments. **Five are proved:**

| arguments | regime | status |
|---|---|---|
| two in `[0,1]` | identity | done — `extend` is `f`, `cLiTwo_ofReal` bridges |
| three negative | Landen | **done, this round** |
| `w₁ = 2.24698` | inversion | **open — the whole of what remains** |

So item 4 is **not closed**; it is reduced from "two of three regimes open" to
**one argument in one regime**. That is the right way to state it, and the
per-argument table should replace the per-regime one in future reports.

### What the inversion leg needs, unchanged

`x > 1` lies **on** `cLiTwoExt`'s cut (`notCut` excludes real `x ≥ 1`), so it
needs a genuine **boundary value** from off the cut — not a constant of
integration. `ComplexDilogarithmBoundary` reaches the closed unit ball off the
cut and deliberately stops short of `[1,∞)`; its docstring says so. Route 34 G5
checks adversarially that the Landen theorem does **not** silently cover
`t = 2.24698`: the combination is visibly nonzero there. A proof that appeared
to reach it would be wrong.

### A fourth sighting of `−t` on log's cut, harmless this time

`log x` carries an `iπ` for `x < 0`, and it drops out of the real part — but
because its partner factor `log(1−x)` is **real**, not because the cut was
avoided. Corrections 5 and 6 in #4701 and the level-7 bridge's `arg(−t) = π`
were the other three. Recorded in the module docstring rather than passed over,
since the first three were all missed on the way past.

**The 5₂ sum rule remains verified to 80 dps, unproved.**


---

## 2026-08-08 — ITEM 4 IS CLOSED

    extend_eq_re_cRogersL (hx0 : x ≠ 0) (hx1 : x ≠ 1) :
      extend (π²/6) rogersL x = Re (cLiTwoExt x + log x · log(1−x) / 2)

`QOU/QBeta/FiveTwoExtendIdentification.lean`, sorry-free, `lake`-verified,
axioms `[propext, Classical.choice, Quot.sound]`. All three regimes; all six
arguments `extended_sum` uses, none of which is `0` or `1`.

The per-argument table that replaced the per-regime one is now uniformly done:

| arguments | regime | status |
|---|---|---|
| two in `[0,1]` | identity | done |
| three negative | Landen | done |
| `w₁ = 2.24698` | inversion | **done** |

Supporting work landed in `QOU/MathlibExt/ComplexDilogarithmOnCut.lean`
(integrability on the cut, continuity on the cut, the on-cut derivative,
`cLiTwoExt 1 = π²/6`, the inversion identity) and
`QOU/MathlibExt/ComplexDilogarithmLanden.lean` (Landen's identity, constant
included). See `qou-invr` for the route and for the three predictions this lane
made about it that were wrong.

**⚠ What item 4 was and was not.** It was one input to the level-7 bridge — the
link letting `extended_sum` (about the piecewise `extend`) talk to the bridge
(which computes with the analytic `Re L`). Closing it does **not** close the sum
rule, does not touch Gap A (`qou-glbl`), and does not perform the assembly
(`qou-asem`) it unblocks.

**The 5₂ sum rule remains verified to 80 dps, unproved.**

## Round 72 Progress (PR #8491)
- De-vacuified and proved genuine Lean 4.24.0 theorems in PR `litlfred/qou#8491` (C1 `0a93eba0e8b5b8ee92b4af6972a325d2dc1a28fd`, C2 `a9b922df9d2baa717878dbac10e60b5a5c341c6e`, 80-dps mpmath witness verified, 0 static audit findings).

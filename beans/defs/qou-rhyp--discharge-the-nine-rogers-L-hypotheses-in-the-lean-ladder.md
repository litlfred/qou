---
# qou-rhyp
title: Discharge the nine Rogers-L hypotheses in FiveTwoLevelSevenLadder (reflection / inversion / Landen / five-term)
status: completed
type: task
priority: high
tags:
    - qbeta
    - dilogarithm
    - 5two
    - lean
    - mathlib-gap
created_at: 2026-08-07T22:05:00Z
updated_at: 2026-09-26T11:07:05Z
parent: qou-0yqu
---


## Why this bean exists

`QOU/QBeta/FiveTwoLevelSevenLadder.lean` proves the three level-7 numerators
**from nine hypotheses**, with `L` abstract. Those hypotheses were, until now,
only prose inside `qou-fivt` — not a tracked gap. They are the concrete remaining
Lean work, so they get their own bean.

**All nine are verified true** against the real Rogers `L` at the actual `wₖ`
(residuals `≤ 3.4e-41`), so none is vacuous. What is missing is *proof*.

## The nine, grouped by difficulty

### 1. Reflection ×4 — **should be nearly free, do this first**

`hrw`, `hrq`, `hrr`, `hrs`: `L(1−x) = L1 − L x`.

The corpus already has, **sorry-free**, in `QOU/Archimedean/DilogReflection.lean`:

```lean
theorem LiTwo_reflection' (x : ℝ) (hx0 : 0 < x) (hx1 : x < 1) :
    LiTwo x + LiTwo (1 - x) = Real.pi ^ 2 / 6 - Real.log x * Real.log (1 - x)
```

With Rogers `L(x) := LiTwo x + log x · log(1−x)/2` the two `½ log log` terms add to
a full `log x · log(1−x)`, which **exactly cancels** the correction term:

    L(x) + L(1−x) = LiTwo x + LiTwo(1−x) + log x·log(1−x) = π²/6

So Rogers reflection follows from `LiTwo_reflection'` by `linear_combination`,
after rewriting `1 − (1 − x) = x`. All four points lie in `(0,1)`
(`w₂, q, r, s` and their reflections), so the side conditions hold.
**Note `LiTwo` lives in namespace `QOU.QPochhammer`,** not `QOU.Archimedean`.

### 2. Inversion ×1 and Landen ×3 — real analysis, not yet in the corpus

`hinv1`: `L x + L(1/x) = 2·L1` for `x > 1`.
`hlan1/2/3`: `L x + L(x/(x−1)) = 0` for `x < 0`.

Verified on **generic** points (`qou-fivt`, gate G1), not just our `wₖ` — so they
are the standard extensions, not coincidences. Neither is in Mathlib (see
`qou-mlbg`: Mathlib has no `Li₂` at all). Each is a one-variable identity
provable the same way `LiTwo_reflection'` is — constancy of a derivative — so the
corpus's existing proof is the template.

### 3. The five-term relation ×3 — the real work

`hA`, `hB`, `hC` are instances of

    L(x) + L(y) − L(xy) − L(x(1−y)/(1−xy)) − L(y(1−x)/(1−xy)) = 0

with all arguments in `(0,1)`. This is the one genuinely substantial item. It is
classical (Abel), and it is the single input the whole Route-11 derivation rests
on.

## ⚠ Queued for roasting

* **The four reflection instances** claim their arguments lie in `(0,1)`. That is
  true for `w₂, q, r, s` numerically — but the Lean statement does **not** carry
  the side conditions, because `L` is abstract. When `L` is instantiated with the
  concrete Rogers `L`, those `0 < x < 1` obligations appear and must be
  discharged. **Do not assume they come for free.**
* `hinv1` bundles inversion *with* the algebraic accident `1/w₁ = 1 − w₂`. If
  someone instantiates it carelessly they will prove inversion at the wrong
  point. Keep the two facts separate when discharging.

## Refs

* `QOU/QBeta/FiveTwoLevelSevenLadder.lean` — the four theorems taking these hypotheses
* `QOU/Archimedean/DilogReflection.lean` — `LiTwo_reflection'`, the template and the input
* `qou-fivt` (Routes 10–11), `qou-mlbg` (Mathlib has no `Li₂`)

---

## ⚠ CORRECTION 2026-08-07 — item 2 was wrong, and two of the hypotheses are FALSE

**`QOU/QBeta/FiveTwoRogersExtend.lean`** (sorry-free, axioms
`[propext, Classical.choice, Quot.sound]`) + probe
`qbeta_5two_route13_rogers_extension_probe.py` (8 gates, 60 dps, all pass).

### What section 2 above said, and why it is wrong

> "Inversion ×1 and Landen ×3 — real analysis, not yet in the corpus. […] Each is
> a one-variable identity provable the same way `LiTwo_reflection'` is — so the
> corpus's existing proof is the template."

**Wrong in both directions.** Two of the four are not hard; they are **false**.
The other two are not analysis; they are free.

The corpus's dilogarithm is a bare power series
(`DilogarithmArchimedeanLimit.lean:63`), summable exactly on `[−1,1]`. Off that
interval Lean's `tsum` returns its **junk value `0`**
(`tsum_eq_zero_of_not_summable`), and `Real.log` is **even**
(`Real.log_neg_eq_log`). So a Rogers `L` built on `LiTwo` equals
`log|x|·log|1−x|/2` for `|x| > 1` — not the dilogarithm.

The ladder's `w₁` is the root `2.2469796…` of `w³−2w²−w+1`. So `hinv1` is
evaluated at `w₁ > 1` and `hlan1` at `−w₁ < −1` — **both in the junk region**:

| hypothesis | argument | residual |
|---|---|---|
| `hinv1` | `w₁ = +2.24698` | **−2.4543** |
| `hlan1` | `−w₁ = −2.24698` | **+1.5692** |
| `hlan2`, `hlan3`, 4× reflection | all in `[−1,1]` | `< 1e-40` ✓ |

The failure is exactly localised to the two arguments that leave the disc.

### The repair is definitional, not analytic

The extended real Rogers dilogarithm (Zagier, *The dilogarithm function*, §I.3)
is **defined** off `[0,1]` by `L x := 2·L1 − L(1/x)` for `x > 1` and
`L x := −L(x/(x−1))` for `x < 0`. `FiveTwoRogersExtend.extend` does exactly
that, generic in `f` and `c`, so inversion and Landen hold **by construction**:

* `extend_inversion` / `extend_inv_eq` — `hinv1`
* `extend_landen` / `extend_landen_eq` — `hlan1`, `hlan2`, `hlan3`
* `extend_reflection` / `extend_reflection_eq` — transports reflection across
* `inv_mem_unit`, `landen_mem_unit` — why the branches close up: `1/x` and
  `x/(x−1)` land in `[0,1]` for **every** `x > 1` resp. `x < 0`

No dilogarithm appears, so the file builds off basic Mathlib order/field lemmas
and does **not** wait on the `DilogReflection` cone.

### What the repair costs — say it plainly

The Lean object is now a **piecewise function**, *not* proved equal to the
analytic continuation of `Li₂`. Gate G7 checks the two agree at all six points in
play (`±w₁, ±w₂, ±w₃`, residuals `< 1e-40`), and G8 checks the numerators
`(17,5,−1)/7·L1` and the sum `3L1 = π²/2` come out of the extension alone. That
is **evidence, not identification**. Anyone wanting the analytic identification
must prove it separately — and that is a new gap, recorded here rather than
quietly assumed away.

### Why no earlier probe caught it

`qbeta_5two_route11_fiveterm_certificate_probe.py` evaluated the same targets
with mpmath's `polylog` — the genuine analytic continuation with principal
branches — and got the right answer. **It was testing the mathematics; the Lean
file encodes the semantics. Both were right on their own terms; the gap was
between them.** Route 11's probe even flagged the extension formulas as
"verified on generic points here, not derived" — the flag was right, the reason
was not the one given.

### Also: the count in this bean's title is wrong

`numerators_original_form` takes **twelve** hypotheses, not nine: 4 reflection
(`hrw hrq hrr hrs`), 4 reduction (`hinv1 hlan1 hlan2 hlan3`), 1 renaming
(`hsw3`), 3 five-term (`hA hB hC`). The title's "nine" predates the file.

### Where this leaves the bean

| group | count | status |
|---|---|---|
| reduction — inversion + Landen | 4 | **DONE**, by construction |
| renaming `hsw3` | 1 | trivial (`s := −w₃`) |
| reflection | 4 | proof written (`FiveTwoRogersReflection.lean`); **build not yet finished** |
| five-term `hA`, `hB`, `hC` | 3 | **OPEN — the only real remaining input** |

**Standing status unchanged: the 5₂ sum rule is verified to 80 dps, unproved.**

### 🔥 Queued for roasting

* **The extension is a *choice*.** It is the standard one, but the ladder's
  conclusion is only about the sum rule if the extension is the function the
  sum rule is about. G7 is six data points, not a theorem. Attack this first.
* **`extend` is generic in `f`** — which means `extend_inversion` says nothing
  about dilogarithms and cannot be misread as saying so. Check that no
  downstream file quietly upgrades it.
* **The same junk-value question applies to every other corpus use of `LiTwo`
  off `[−1,1]`.** This lane found it; nobody has swept the rest.

---

## 2026-08-07 (later) — the five-term instances are PROVED genuine, and the gap Route 13 created is closed on paper

### Roast item 1 (`qou-rstq`) — discharged

`hA`, `hB`, `hC` **are** genuine five-term instances. Checked twice, independently:

* **exact arithmetic** in `ℚ(w)` — `qbeta_5two_route14_fiveterm_arguments_exact_probe.py`,
  `fractions.Fraction` in the power basis, no floating point in the matching;
* **Lean** — `QOU/QBeta/FiveTwoFiveTermArguments.lean`, over any `Field`,
  sorry-free, ten theorems.

| | instance | last three arguments |
|---|---|---|
| `hA` | **diagonal**, `x = y = w₂` | `{1−q, r, r}` |
| `hB` | `x = 1−w₂`, `y = q` | `{1−q, 1−s, w₂}` |
| `hC` | `x = w₂`, `y = s` | `{1−w₂, 1−s, 1−r}` |

`hA` being *diagonal* is what explains its coefficients `(2,−1,−2)` instead of
the five-term's `(1,1,−1,−1,−1)` — two of the five arguments coincide. Its
identification `w₂² = 1−q` **is `bloch_key`**, and `bloch_key` shows up a second
time fixing `hC`'s last argument. Three of the six identities need nothing at all.

Also: `arg_B2`/`arg_C2` were first stated with `x ≠ 1`; they do not need it,
because `s·x = 1−x` already forces `x ≠ 0` (at `x = 0` it reads `0 = 1`).

### Roast item 4 — the gap Route 13 created — closed on paper

Route 13 repaired `hinv1`/`hlan1` by *defining* the extension, and flagged the
cost: the Lean object is piecewise, not proved equal to the analytic
continuation, with agreement checked at only six points.

`qbeta_5two_route15_extension_is_continuation_probe.py` shows the agreement is
**identical, not coincidental** — confirmed at generic arguments from `1.000001`
to `1e6` and `−1e-6` to `−1e6` — and gives a two-line derivation per branch:

* `x > 1`: Euler inversion + principal `log(−x) = log x + iπ`, on real parts.
* `x < 0`: Landen, using `1 − x/(x−1) = 1/(1−x)`.

Both collapse exactly. **`extend` IS `Re` of the principal-branch analytic
Rogers `L`.**

### Where the work actually went — it did not vanish

**It moved down one level.** This bean originally owed "inversion ×1 and Landen
×3" for Rogers `L`. Those are now free by construction. But identifying `extend`
with the analytic continuation owes **`Li₂` inversion and `Li₂` Landen** — the
same two classical facts, one level down, and Mathlib has no `Li₂` at all
(`qou-mlbg`).

That is a smaller and far better-defined debt than four unproved hypotheses. It
is still a debt. **Nothing downstream should read `extend` as "the dilogarithm".**

### A gate that caught its own author

`qbeta_5two_route15`'s first G5 tested `|ext(1+1e-10) − L1| < 1e-9` and **failed
at 1.25e-9**. The mathematics was fine — near `x = 1` the residual is
`O(ε log ε)`, so at `ε = 1e-10` it is `~1e-9` *by construction*. A seam is a
limit statement and has to be gated as one; G5 now tests monotone decrease. Worth
recording next to the branch-trap note: **a failing gate is not evidence of a
failing theorem until you have checked the gate.**

### Current state of the twelve hypotheses

| group | count | status |
|---|---|---|
| inversion + Landen | 4 | ✅ by construction (`FiveTwoRogersExtend`) |
| renaming `hsw3` | 1 | trivial |
| reflection | 4 | proof written; build still unfinished |
| five-term `hA`,`hB`,`hC` | 3 | ✅ **proved to be genuine instances**; the relation itself ❌ |

**The one open analytic input to the numerators is Abel's five-term relation.**
**Standing status unchanged: the 5₂ sum rule is verified to 80 dps, unproved.**

---

## 2026-08-07 (end of session) — reflection BUILT; only Abel's relation is left

`FiveTwoRogersReflection.lean` has compiled. The `⚠ NOT YET BUILT` header it
carried is gone, and its theorems are audited:

```
rogersL_reflection    [propext, Classical.choice, Quot.sound]
rogersL_one_sub       [propext, Classical.choice, Quot.sound]
hasDerivAt_rogersL    [propext, Classical.choice, Quot.sound]
rogersL_deriv_symm    [propext, Classical.choice, Quot.sound]
```

No `sorryAx` anywhere in the chain, which also certifies `LiTwo_reflection'`
beneath it.

**What killed the first two build attempts was not the mathematics.** The file
failed at job 3177/3177 with `Unknown identifier 'LiTwo_reflection''` — a
**namespace error**. `LiTwo` is declared in `QOU.QPochhammer`, but
`LiTwo_reflection'` and the `hasDerivAt_*` lemmas are in `QOU.Archimedean`
(`DilogReflection.lean` itself does `open QOU.QPochhammer`). The file's own
comment said "note `LiTwo` lives in `QOU.QPochhammer`, not `QOU.Archimedean`" —
correct about `LiTwo`, and exactly the wrong lesson to draw about the theorem.
Both `open`s are needed; that is now in the file.

Cost: two ~45-minute builds of a 3177-job Mathlib cone to surface a one-line
fix. **When a file's only novel content is a `linear_combination` off an existing
lemma, check the identifier resolves before starting the cone.**

### New: `hasDerivAt_rogersL`

    L'(x) = -(log(1-x)/x + log x/(1-x))/2   on (0,1)

A product rule off `hasDerivAt_LiTwo` and `hasDerivAt_log_mul_log_one_sub`, both
already sorry-free. This is the analytic ingredient any proof of the five-term
relation starts from, so it is the first real step toward the one remaining gap.
`rogersL_deriv_symm` records that the derivative is symmetric under `x ↦ 1 - x`
— which is *why* reflection holds. It needs no hypotheses at all; the first draft
carried `0 < x < 1` by reflex and the linter caught them unused. **Second time
this session a side condition was added by reflex and turned out unnecessary**
(the first was `x ≠ 1` in `FiveTwoFiveTermArguments`).

### The twelve hypotheses, final state

| group | count | status |
|---|---|---|
| inversion + Landen | 4 | ✅ by construction (`FiveTwoRogersExtend`) |
| renaming `hsw3` | 1 | ✅ trivial |
| reflection | 4 | ✅ **proved and built** (`FiveTwoRogersReflection`) |
| five-term `hA`,`hB`,`hC` | 3 | ✅ **proved to follow from Abel** (`FiveTwoFiveTermArguments`) |

**Eleven of twelve are discharged. The level-7 numerators now rest on exactly one
unproved input: Abel's five-term relation on `(0,1)`.**

That is the whole remaining gap on this branch of the chain. It does not close
the sum rule — `qou-trns`'s transport is still unformalized, and `extend` is
still not identified with the analytic continuation in Lean (`qou-rstq` item 4,
closed on paper by Route 15 but not in Lean).

**Standing status, unchanged all session: the 5₂ sum rule is verified to 80 dps,
unproved.**

---

## 2026-08-08 — CLOSED: all twelve discharged

| group | count | where |
|---|---|---|
| inversion + Landen | 4 | `FiveTwoRogersExtend` — by construction |
| renaming `hsw3` | 1 | trivial |
| reflection | 4 | `FiveTwoRogersReflection.rogersL_reflection` |
| five-term `hA`,`hB`,`hC` | 3 | `FiveTwoFiveTermArguments` + `FiveTwoAbelFiveTerm` |

`numerators_of_abel` is unconditional as `numerators_of_root`. The bean's
original framing — "nine hypotheses, reflection nearly free, inversion/Landen
standard analysis, five-term the real work" — was wrong in two places, both
recorded above: there are **twelve**, and two of the inversion/Landen four were
**false**, not hard.

**The 5₂ sum rule remains verified to 80 dps, unproved.** This bean was never
the sum rule; it was the ladder's hypotheses, and those are done.

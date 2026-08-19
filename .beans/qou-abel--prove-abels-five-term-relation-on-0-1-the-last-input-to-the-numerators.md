---
# qou-abel
title: "Prove Abel's five-term relation on (0,1) — the LAST open input to the level-7 numerators"
status: completed
type: task
priority: high
tags:
    - qbeta
    - dilogarithm
    - 5two
    - lean
    - mathlib-gap
created_at: 2026-08-08T00:20:00Z
updated_at: 2026-08-08T00:20:00Z
parent: 0yqu
---


## Why this bean exists

`qou-rhyp` closed eleven of the twelve hypotheses
`FiveTwoLevelSevenLadder.numerators_original_form` takes. **This is the twelfth**,
and it now carries the whole branch on its own, so it gets its own bean rather
than staying a bullet inside a bean about something else.

## The statement

For `x, y ∈ (0,1)` with the Rogers `L`:

    L x + L y - L (x·y) - L (x(1-y)/(1-x·y)) - L (y(1-x)/(1-x·y)) = 0

Classical — Abel, 1830 — and **not in Mathlib**, which has no `Li₂` at all
(`qou-mlbg`).

## What is already in place

Everything else on this branch:

| piece | where |
|---|---|
| `L` on `[0,1]`, from the corpus `LiTwo` | `FiveTwoRogersReflection.rogersL` |
| reflection `L(1-x) = L1 - L x` | `FiveTwoRogersReflection.rogersL_reflection` ✅ built |
| **`L'(x) = -(log(1-x)/x + log x/(1-x))/2`** | `FiveTwoRogersReflection.hasDerivAt_rogersL` ✅ built |
| extension off `[0,1]`, inversion + Landen free | `FiveTwoRogersExtend` ✅ |
| `hA`,`hB`,`hC` are five-term instances | `FiveTwoFiveTermArguments.arg_*` ✅ |
| five-term ⟹ `hA`,`hB`,`hC` | `FiveTwoFiveTermArguments.h*_of_five_term` ✅ |
| **Abel + reflection ⟹ numerators `(17,5,-1)`** | `FiveTwoFiveTermArguments.numerators_of_abel` ✅ |

So `numerators_of_abel` is already written and sorry-free. **Discharging this
bean turns it into an unconditional theorem about the corpus's `LiTwo`.**

## The proof, and why the corpus is unusually well set up for it

The standard argument, which is exactly the shape
`QOU/Archimedean/DilogReflection.lean` already uses for `LiTwo_reflection'`:

1. Fix `y ∈ (0,1)`. Let `F(x)` be the left-hand side.
2. Show `F'(x) = 0` on `(0,1)`.
3. Show `F(x) → 0` as `x → 0⁺`.

Step 3 is easy: `L 0 = 0`, `x·y → 0`, `x(1-y)/(1-xy) → 0`, and
`y(1-x)/(1-xy) → y`, so `F → L y - L y = 0`.

**Step 2 is the work**, and it is where `hasDerivAt_rogersL` earns its place: the
three composite terms need the chain rule with rational inner functions, then the
resulting identity among `log`s of rational functions of `(x,y)` needs
`Real.log_mul` / `Real.log_div` with positivity side conditions at each split.
That last part — not the calculus — is the bulk of the Lean effort.

`LiTwo_reflection'` is the template for the whole shape (derivative vanishes,
boundary limit, conclude), and it is already sorry-free, so this is a known-good
pattern in this corpus rather than a new one.

## Scope check — what this does NOT close

Discharging this does **not** prove the 5₂ sum rule. Two other links remain:

* `qou-trns` — the transport `x = 1 → x = -1`: envelope theorem confirmed
  numerically, **not formalized**.
* `qou-rstq` item 4 — `extend` is not identified with the analytic continuation
  *in Lean*. Route 15 closed it **on paper** (probe
  `qbeta_5two_route15_extension_is_continuation_probe.py`), reducing it to `Li₂`
  inversion and `Li₂` Landen. Both classical, neither in Mathlib.

**The 5₂ sum rule is verified to 80 dps, unproved.**

## ⚠ Queued for roasting

* **Do not state the relation with unrestricted `∀ x y`.** It is false outside
  the region where the arguments stay in `(0,1)` — the extended `L` picks up
  `π²/6` corrections. `numerators_of_abel` deliberately takes the three
  instances separately, with their arguments written out, so a careless `∀`
  version cannot slip in underneath it.
* **Check the three instances' arguments really are in `(0,1)`** before using a
  restricted statement. They are (`w₂ = 0.5550`, `q = 0.6920`, `r = 0.3569`,
  `s = 0.8019`, and the derived ones), but that is a numerical fact about roots
  of a cubic and will need `nlinarith`-style bounds in Lean, which nobody has
  written yet. **That is a hidden sub-gap** — flagged here so it is not
  discovered late.
* The `log` side conditions in step 2 are where a wrong branch would hide.
  Principal-vs-real `log` has produced a spurious result **four** times in this
  lane (`qou-rstq`). Everything here is real-valued on `(0,1)`, which is exactly
  the situation where it is easy to stop checking.

## Refs

* `qou-rhyp` (the other eleven), `qou-fivt` (Routes 10–11), `qou-mlbg` (no `Li₂`
  in Mathlib), `qou-rstq` (roast queue), parent `qou-0yqu`
* `QOU/QBeta/FiveTwoFiveTermArguments.lean`, `QOU/QBeta/FiveTwoRogersReflection.lean`
* PRs #4658 (merged), #4701

---

## 2026-08-08 — PROVED

`QOU/QBeta/FiveTwoAbelFiveTerm.lean`, sorry-free:

```lean
theorem rogersL_fiveTerm {x y : ℝ} (hx0 : 0 < x) (hx1 : x < 1) (hy0 : 0 < y) (hy1 : y < 1) :
    rogersL x + rogersL y - rogersL (x * y)
      - rogersL (x * (1 - y) / (1 - x * y))
      - rogersL (y * (1 - x) / (1 - x * y)) = 0
```

Axioms `[propext, Classical.choice, Quot.sound]`, and the whole chain beneath it
is clean — `hasDerivAt_rogersL`, `LiTwo_reflection'` included. `lake build`
green. Cross-checked numerically at 25 `(x,y)` pairs, worst residual `1.6e-40`.

`L` is the corpus's own `rogersL`, built on `LiTwo`. Non-vacuous: on `(0,1)` the
power series converges, so `rogersL` there **is** the real Rogers dilogarithm —
unlike off `[−1,1]`, where Route 13 showed it is junk.

### How it went

Exactly the shape predicted: fix `y`, kill the derivative, evaluate at `x → 0⁺`.

**The derivative step compiled first try**, which is worth explaining rather than
being pleased about. All the content sits in four log-splitting lemmas
(`log_inner_left` and friends), which use `1 - x(1-y)/(1-xy) = (1-x)/(1-xy)` and
its mirror. Once those are in place, `-2·F'(x)` is a *linear form* in
`log x, log(1-x), log y, log(1-y), log(1-xy)` whose five coefficients each vanish
as rational functions — so the last step really is `field_simp; ring`. The
difficulty was never the calculus; it was arranging for the logs to split, which
is where every positivity side condition lives.

Three things that did cost iterations, all mechanical:

* `field_simp` normalises `1 - x*y` to `1 - y*x` in one orientation and not the
  other, so a hypothesis stated as `1 - x * y ≠ 0` silently failed to apply.
  Fixed by supplying both orientations.
* `positivity` is structural — it cannot use `0 < x` from the context — so
  `Real.log_div (by positivity)` failed where `ne_of_gt (mul_pos hx0 _)` works.
* Two more hypotheses added by reflex and unused: `hy0` in `one_sub_mul_pos`
  (`x·y < x < 1` needs only `y < 1`) and in `tendsto_inner_right_zero`.
  **Third and fourth instances this session.**

### What is NOT closed

The remaining step to make `numerators_of_abel` unconditional is the sub-gap this
bean already flagged: the three instances' arguments must be shown to lie in
`(0,1)`, which needs bounds on the root — specifically `1/2 < w₂ < 1`, since
`s = (1-x)/x < 1` fails without it. That is `nlinarith` plus an IVT existence
argument, and it is not written.

**The 5₂ sum rule remains verified to 80 dps, unproved.** `qou-trns`'s transport
is still unformalized and `extend` is still not identified with the analytic
continuation in Lean.

---

## 2026-08-08 (later) — the sub-gap is closed too; the numerators are UNCONDITIONAL

The bound this bean flagged in advance is written:

```lean
theorem numerators_of_root {x : ℝ} (hx : x ^ 3 - 2 * x ^ 2 - x + 1 = 0)
    (hlo : 1 / 2 < x) (hhi : x < 1) :
    (7 * (2 * (π^2/6) + 2 * rogersL x - rogersL (1 / (2 - x))) = 17 * (π^2/6))
      ∧ (7 * (2 * rogersL x - rogersL (x / (x + 1))) = 5 * (π^2/6))
      ∧ (7 * (-(2 * (π^2/6)) + 2 * rogersL x + rogersL ((1 - x) / x)) = -(π^2/6))
```

**No hypothesis about `L` remains.** Abel is `rogersL_fiveTerm`, reflection is
`rogersL_one_sub`, both proved. Sorry-free, standard axioms, `lake` green.

And it is not vacuous:

```lean
theorem exists_root_in_Ioo : ∃ x : ℝ, x ^ 3 - 2 * x ^ 2 - x + 1 = 0 ∧ 1 / 2 < x ∧ x < 1
```

by IVT — `f(1/2) = 1/8 > 0`, `f(1) = -1 < 0`. Cross-checked numerically at the
root `0.55495813208737119142`; all three residuals `< 5e-40`.

`1/2 < x` earns its place exactly where predicted: `s = (1-x)/x < 1` is false
without it, and `s` is `hC`'s second argument.

### Small note worth keeping

`positivity` failed on `0 < (1-x)/x` while succeeding on `0 < 1/(2-x)` two lines
earlier. Not a quirk: `positivity` tries `assumption` on atoms, and `0 < 2 - x`
was in context while `0 < 1 - x` was not. Adding the missing `have` fixed it.
**When `positivity` fails on one of several similar goals, look for the missing
hypothesis rather than reaching for a different tactic.**

### Where this leaves the chain

The level-7 numerators `(17, 5, -1)` are now **proved in Lean, unconditionally,
for the corpus's own dilogarithm**, from the cubic and a root bound.

That is one link. The 5₂ sum rule needs two more, both still open:

* `qou-trns` — the transport `x = 1 → x = -1`, envelope theorem unformalized;
* `qou-rstq` item 4 — `extend` identified with the analytic continuation *in
  Lean* (closed on paper by Route 15; needs `Li₂` inversion and `Li₂` Landen).

**The 5₂ sum rule remains verified to 80 dps, unproved.**

---

## 2026-08-08 — CLOSED

`rogersL_fiveTerm` (Abel on `(0,1)`), `numerators_of_root` (the numerators,
unconditional), `exists_root_in_Ioo` (non-vacuity), `extended_targets` and
`extended_sum` — all in `QOU/QBeta/FiveTwoAbelFiveTerm.lean`, all sorry-free on
`[propext, Classical.choice, Quot.sound]`, `lake build` green.

The sub-gap this bean flagged in advance — the `(0,1)` membership of the three
instances' arguments — is closed too, and `1/2 < x` earned its place exactly
where predicted (`s = (1-x)/x < 1` fails without it).

**Nothing here is left open.** What the chain still needs is in `qou-trns` and
`qou-rstq` item 4, neither of which is about the five-term relation.

---

## ⚠ 2026-08-08 — the level-7 ladder is CLASSICAL. Watson (1937).

Literature arrived (`library/arxiv-hep-th-9408113v2/9408113v2.pdf` — Kirillov, *Dilogarithm identities*,
hep-th/9408113). **§1.2.2 gives Watson's relations**, and they are this lane's.

Kirillov: let `α, −β, −1/γ` be the roots of `x³ + 2x² − x − 1 = 0`, with
`α = ½sec(2π/7)`, `β = ½sec(π/7)`, `γ = 2cos(3π/7)`. Then

    L(α) − L(α²) = (1/7)·L(1)
    2L(β) + L(β²) = (10/7)·L(1)
    2L(γ) + L(γ²) = (8/7)·L(1)

Under `x ↦ −x` his cubic **is** `x³ − 2x² − x + 1`, ours, and

    α = −w₃,   β = w₂,   γ = 1/w₁

verified to `1e-30` (`qbeta_5two_route18_watson_classical_probe.py`, 6 gates).

**So `numerators_of_root` formalizes a known identity family.** The
`(17, 5, −1)/7` are different combinations of the same `L`-values in the same
field `ℚ(ζ₇)⁺`, with the same denominator 7. This bean, and the commits behind
it, presented the numerators as "DERIVED" with a tacit implication of novelty.
**That implication was wrong and is withdrawn.**

### What remains this lane's

* **The route.** Kirillov proves accessibility from the **duplication formula**;
  this lane derived it from the **five-term relation**. Genuinely different.
* **The formalization.** Watson, Loxton, Lewin, Kirillov and Zagier all work on
  paper. `rogersL_fiveTerm`, `numerators_of_root`, `extended_sum` are sorry-free
  Lean, which the literature does not provide.

Both are worth having. Neither is a new theorem.

### Two further confirmations from Zagier (`library/the-dilogarithm-function-*.pdf`)

* **`FiveTwoRogersExtend.extend` is Zagier's definition verbatim** — `L(0)=0`,
  `L(1)=π²/6`, `L(x)=2L(1)−L(1/x)` for `x>1`, `L(x)=−L(x/(x−1))` for `x<0`.
  Route 13's repair was the standard one; now checked against the source rather
  than from memory.
* **`hasDerivAt_rogersL` is Zagier's `L′(x)` verbatim**, and he names exactly
  that formula as the route to "these and all other functional equations" —
  which is how Abel was proved here. The method was right for the documented
  reason.

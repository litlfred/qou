---
# qou-abel
title: "Prove Abel's five-term relation on (0,1) — the LAST open input to the level-7 numerators"
status: todo
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

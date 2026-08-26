---
# qou-cdqu
title: chi-sym-alt-closed-form.lean models 3 letter types; atom_braid_word_3A emits 4
status: todo
type: task
created_at: 2026-08-26T17:01:42Z
updated_at: 2026-08-26T17:01:42Z
---

[`content/quantum-observable-universe/braids-and-knots/chi-sym-alt-closed-form.lean`](../content/quantum-observable-universe/braids-and-knots/chi-sym-alt-closed-form.lean)
formalises

    χ_sym(β)·χ_alt(β) = (-1)^{#β} · (1 + H_A²/4)^{nUd β}

over an alphabet of exactly three letters:

```lean
inductive FactorType
  | sigma           -- (c=1, d=0)
  | sigmaInv        -- (c=1, d=-H_A)
  | udHalf          -- (c=1, d=-H_A/2)
```

**`atom_braid_word_3A` emits a fourth.** Measured on ⁴He (47 letters): 23 `σ`,
15 `σ⁻¹`, 8 at `d = -h/2`, and **one** at `d = -h(1/2 - δ/4)` — the
colour-weighted p-n interface, `δ = flavor_split_subleading(q₀) ≈ 0.001376`.
There is exactly one per atom regardless of A, because the pp interface is a
plain `σ` and the nn a plain `σ⁻¹` (already isospin-distinct by chirality).

So `chiPairProduct_eq` is **sorry-free and true**, about a **colour-blind**
alphabet — not about the word the corpus actually builds. This is not a proof
defect; it is a scope gap between the formal statement and its intended subject,
and nothing in the file says so.

### It is not academic — it is a measured 5.11e-9

Carrying the p-n letter as itself, `f_ud^(2A) · f_pn` instead of
`f_ud^(2A+1)`, takes `chi_sym_alt_closed_form`'s residual from **5.1139e-9 to
1.2e-14** (the float64 floor of the inputs). Fixed on the Python side in
`6dd79a2a9`; the Lean still states only the colour-blind form.

The mechanism is worth carrying into the Lean: `f(d) = d² - 1 + d·h` has
`f'(d) = 2d + h`, which **vanishes identically at `d = -h/2`**. The `udHalf`
letter sits at a stationary point of the per-factor product, so the colour
perturbation costs *second* order — `Δd/d = 6.9e-4` gives `Δf = (Δd)² = 5.17e-9`.
That is a clean, provable statement and it is the reason the gap stayed hidden.

### Scope

- `FactorType` gains a `pnColor` constructor carrying its `d`.
- `chiPairPerFactor` extends to it: `d² - 1 + d·H_A`, no special case needed.
- `chiPairProduct_eq` generalises to `(-1)^{#β} · (1 + H_A²/4)^{nUd β} · Π f_pn`.
  With exactly one such letter it is `… · f_pn`.
- The stationarity lemma `∀ h, (deriv f)(-h/2) = 0` is a one-liner and is the
  substantive content.
- The `.md` sibling and `rem:chi-sym-alt-closed-form` need the same correction;
  `docs/chi-sym-alt-theorem.md` is cited as the `-- Ref:` and states the
  colour-blind form.

### Not done here

Content-block + Lean change, and PR #5833 is already large. Also worth deciding
first whether the corpus wants the colour-blind form kept as the headline (it is
the simpler statement and is exactly true for `pn_convention="strict_averaged"`)
with the colour-weighted one as a corollary, or the reverse. That is an
expository call, not a measurement.

---
# qou-cdqu
title: chi-sym-alt-closed-form.lean models 3 letter types; atom_braid_word_3A emits 4
status: completed
type: task
priority: normal
created_at: 2026-08-26T17:01:42Z
updated_at: 2026-08-26T18:15:32Z
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


## Closed 2026-08-26 (PR #5833, commits `f9799f9a2`, `09a5d5bbb`)

Additive throughout — nothing that was proved changed.

### The fix

A **new** inductive `ColourFactorType` rather than a fourth constructor on
`FactorType`, which would have cost `FactorType` its `DecidableEq` to a
real-valued field. With it: `chiPairPerFactorC`, `chiPairProductC`, `nUdC`,
`nBlind`, `nPn`, `pnProduct`, and

```
chiPairProductC H_A w = (-1)^{nBlind w} · (1 + H_A²/4)^{nUdC w} · pnProduct H_A w
```

The **weighted form is the theorem** and the colour-blind one its `δ = 0`
corollary (`chiPairProductC_delta_zero`). That is the only direction that
exists: setting `δ = 0` collapses weighted → blind, while the blind form has
already discarded `δ`. It also matches R3 (owner ruling 2026-08-15) making
`bring_color_weighted` canonical — the blind form is exact for
`strict_averaged`, which R3 rules non-canonical.

### The substantive lemma, and the owner's improvement to it

The stationarity of the `ud` letter, first as

```
f(d) − f(−H_A/2) = (d + H_A/2)²        [ℝ, `ring`]
```

then — on the owner's question, *"can we rewrite identity so 2 is not in
denom?"* — in the strictly better division-free form:

```
4·(d² − 1 + d·H_A) = (2d + H_A)² − H_A² − 4        [any CommRing, `ring`]
```

Three things this bought:

1. **No `Field`, no `CharZero`, no `2 ≠ 0`.** My first generic version carried
   `[Field R] [CharZero R]` purely so `field_simp` could clear a denominator
   that did not need to be there. §7c asks for the weakest typeclass; this is
   it.
2. **It states the content better.** All the `d`-dependence sits inside a
   *perfect square* in the offset `2d + H_A`, vanishing exactly at `2d = −H_A`.
   "The ud letter is a stationary point" and "the offset enters squared" are the
   same fact; this form makes the second manifest with no derivatives, no
   division, and no distinguished point.
3. **The characteristic-2 caveat disappears rather than being worked around.**
   The divided form is genuinely *false* in char 2 (`H_A/2` undefined). This one
   degenerates to `0 = 0` — the honest answer: no stationary point exists there,
   and the statement claims none.

Measured consequence, unchanged: predicted `5.11397e-9` from this identity
alone against `5.11395e-9` measured on all four atoms.

### Verified

`lean`-direct **exit 0** (~6 s) against the real import cone;
`#print axioms` on all six new declarations → `[propext, Classical.choice,
Quot.sound]`, **no `sorryAx`**. `check-sidecars.sh` clean. Render preflight on
the `.md` clean (22 `$$`, braces balanced, no `\operatorname`).

### Doc annotated, not rewritten

`docs/chi-sym-alt-theorem.md` — the `-- Ref:` this file cites — has a scope
banner and two inline corrections. Its Step 4 asserted the p-n boundary "uses
(1, −H_A/2) = ud-half", which is where the entire `2A+1` derivation comes from
and is true only in the colour-blind convention. The derivation is correct under
its own assumption; it simply never stated the assumption.

### Two things found while doing it, NOT fixed — worth a follow-up

- **`chi-sym-alt-closed-form.lean` has no `.md` or `.ts` sibling.** It is an
  orphan Lean file in a content chapter directory, so it has no `.qa.json` and
  nothing but an agent ever checks it — exactly the case AGENTS.md §"QA is
  agent-owned" names. `check-sidecars.sh` agrees: *"library Lean … no sidecar"*.
- **`chi_sym_alt_closed_form.py` sets `set_content_block("rem:chi-sym-alt-closed-form")`
  and that block does not exist anywhere in `content/`.** Dangling reference.

Both are small, both are content-structure rather than mathematics, and neither
was in this bean's scope.



## Correction 2026-08-26 — the float64 tail item is RETRACTED

This bean's closing item repeated the claim that both ⁴He braid constructors emit
float64 offsets. It is false and is retracted in full on `qou-oppb`:
`atom_braid_word_3A` is exact (relative error 0.0 at 60 dps against the closed
form), the float64 belonged only to a since-deleted local rebuild, and
`he4_braid_canonical` now delegates so there is one constructor. The 1.2e-14
residual quoted above is the character accumulation's own, not a floor set by the
offsets.

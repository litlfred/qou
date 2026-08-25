---
# qou-x20w
title: Generalise OmegaOrder to a separate exponent group, and populate it from Mathlib HahnSeries
status: completed
type: task
priority: normal
created_at: 2026-08-16T13:47:01Z
updated_at: 2026-08-21T17:00:42Z
---


## DONE 2026-08-16 — the class is generalised and populated

Branch `claude/omegaorder-exponent-group-2026-08-16`. Approved by the owner
after #5244 recorded the obstruction. `OmegaOrder` now has a **real model**.

### What changed

`Asymptotics.lean` — two conservative weakenings:

- **exponents move to their own `Γ`.** Previously `Ow : K → WithTop K`, which is
  right for `𝐍𝐨` (closed under `ω`-exponentiation) but self-referential, and it
  is why the class had no instance anywhere: Mathlib's leading-exponent
  valuation is `HahnSeries.orderTop : HahnSeries Γ R → WithTop Γ` with `Γ`
  separate, and nothing bridged the two. Take `Γ := K` to recover the old
  reading.
- **the base weakens** from `[SurrealField K]` to `[CommRing K]` plus an algebra
  over an **abstract scalar ring `S`**. The scaling axiom was phrased with
  `SurrealField.ofReal`; nothing about a leading-exponent valuation needs the
  scalars to be the reals.

`HahnOmegaOrder.lean` (new) — the model, `Ow := HahnSeries.orderTop` over a
domain. `SpectralNormalForm.lean` — updated to `[OmegaOrder K ℝ Γ]`.

### What had to be proved

Mathlib gives multiplicativity of `orderTop` only as the **inequality**
`orderTop_add_le_mul`. `Ow_mul` is an equality, so `orderTop_mul` derives it
from `HahnSeries.order_mul` (the equality on the un-topped `order`, needing both
factors non-zero and `R` a domain) plus the two zero cases. The domain
hypothesis earns its place twice: once for `order_mul`, once so `x * y ≠ 0`
follows and the `⊤` bookkeeping matches.

### The §7c trap this walked into, and why the escape is better mathematics

First cut used `[CommRing K] [Algebra ℝ K]`. That made `check-wall-side` **FAIL**
both `Asymptotics` and `HahnOmegaOrder`: the mixed-regime rule fires on
`CommRing` (an `ALGEBRAIC_LEAN_RE` marker) coexisting with `ℝ`. Verified it was
my regression, not pre-existing, by re-running against a stashed tree.

The acknowledgement escape was unavailable — the checker reads the note from a
block's `.md`/`.ts`, **never** from the `.lean` docstring, and these are library
files with no sibling block. So there was nowhere to put an acknowledgement.

Abstracting the scalar ring to `S` fixes the gate **and** is the better
statement: the axiom is about scalars from the base having order zero, which has
nothing to do with the reals. Surreal callers instantiate `S := ℝ`. Both files
now PASS. Worth remembering: when the mixed-regime rule fires on a library file,
the escape hatch does not exist, so the ℝ has to actually go.

### Verification

- Whole umbrella: `lean-direct-cone -k QOU` → **1097 modules, err = 0**. The
  signature change broke no consumer. (Only `Asymptotics` and
  `SpectralNormalForm` used the class as a typeclass; `KernelGrowthBound` and
  `LocalInfinitesimalField` mention it in prose only.)
- `#print axioms` on `orderTop_mul` and `hahnOmegaOrder`:
  `[propext, Classical.choice, Quot.sound]`. No `sorryAx`.
- `check-base-ring` PASS ×3; `check-wall-side` PASS ×3; both
  `lean-content-siblings` local gates exit 0; orphan gate exit 0;
  `run-validate` exit 0.

### What this settles, and what it does not

**Settles:** `OmegaOrder`'s four axioms are jointly consistent, over a carrier
with genuine non-archimedean content (`HahnSeries ℤ ℝ` has elements of every
integer order) rather than a degenerate one. Every `[OmegaOrder]`-conditional
result now rests on a class that is known satisfiable.

**Does not settle:** `SpectralNormalForm` is still unwitnessed. It additionally
needs `IsInfinitesimal`/`IsFinite`, hence `[SurrealField K]`, and `SurrealField`
demands `omegaSurreal` exceeding every natural — so the Hahn model does not
qualify and no archimedean carrier can. The gap is now **one** construction
(a non-archimedean ordered field carrying both a birthday function and a
leading-exponent valuation) rather than two, and its header says so.

`hahnOmegaOrder` is deliberately a `def`, **not** a global `instance` —
registering it would let resolution silently pick the Hahn valuation for an
unrelated `K`, which is the same shape of accident as the fabricated instances
`qou-ffwk` is about.

## Summary of Changes — closed 2026-08-21 (owner instruction)

Closed on explicit owner instruction; AGENTS.md §4a reserves closure for a human
and this records that it was one.

**Delivered** (PR #5255, merged):

- `OmegaOrder` generalised twice over — exponents moved to their own parameter
  `Γ`, and the base weakened from `[SurrealField K]` to `[CommRing K]` plus an
  algebra over an abstract scalar ring `S`. Taking `Γ := K` and `S := ℝ`
  recovers the original surreal reading, so no caller lost anything.
- `HahnOmegaOrder.lean` (new) — the model, `Ow := HahnSeries.orderTop` over a
  domain. `orderTop_mul` proved from `HahnSeries.order_mul` plus the two zero
  cases, because Mathlib only ships the inequality.
- `SpectralNormalForm` updated to the new signature.

**The point:** the class had **no instance anywhere**, so every
`[OmegaOrder]`-conditional result rested on something never shown consistent.
It now has a model over a carrier with genuine non-archimedean content.

**Verified:** whole umbrella `lean-direct-cone -k QOU` → **1097 modules,
err = 0**; sorry-free; base-ring and wall-side PASS on all three files; siblings,
orphan and validate gates clean.

**Left open, deliberately, and now the only remaining piece:**
`SpectralNormalForm` is still unwitnessed. It additionally needs
`IsInfinitesimal`/`IsFinite`, hence `[SurrealField K]`, and `SurrealField`
demands `omegaSurreal` exceeding every natural — so the Hahn model cannot serve
and no archimedean carrier can. That gap is **one** construction (a
non-archimedean ordered field carrying both a birthday function and a
leading-exponent valuation) rather than the two it was before, and
`Asymptotics.lean`'s history note records the build order for it.

`hahnOmegaOrder` is a `def`, **not** a global `instance` — registering it would
let resolution silently pick the Hahn valuation for an unrelated `K`, the same
shape of accident `qou-ffwk` exists to remove.

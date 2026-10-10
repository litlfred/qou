---
# qou-nmib
title: Formalize H3 Delta baryon map and Wigner SU(2) gap resolution
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - 8f-lean
created_at: 2026-07-20T00:46:28Z
updated_at: 2026-10-10T08:24:45Z
parent: qou-8lxd
---

## Body written 2026-10-10 — this bean was TITLE-ONLY from 2026-07-20

Two items packed into one title, and **measuring them splits the bean**: one
half is largely already done, the other is gated by the arc's own blocker — but
only partly, and the part that is not gated is startable now.

## Half B first — "Wigner `SU(2)` gap resolution" looks LARGELY DONE

Two substantive Lean carriers exist on the live tree, neither of them a stub:

- `folio/.../lean/QOU/BraidsAndKnots/WignerSU4FromSpinIsospin.lean` — the D11
  carrier for `conj:wigner-su4-from-spin-isospin`, i.e. `SU(4) = SU(2)_S ×
  SU(2)_I` as the combined classical limit of the spin `SO(3)` fibre action
  (D10) and the canonical isospin `ℤ/2` swap (D9). `class
  WignerSU4FromSpinIsospin` at line 100, **no instance provided** (the honest
  open state, §3b), plus `wignerSU4_occupancy_via_plancherel` and — good
  discipline worth not losing — a **`_refutable` / `_satisfiable` pair** at
  lines 139 and 152, which is what distinguishes a content-bearing class from
  one that is vacuously unsatisfiable.
- `folio/.../lean/QOU/Mass/WignerSU4RowBoundInactive.lean` — the row-cap side:
  `rows`, `rows_le`, `SU4Admissible p := rows p ≤ 4`,
  `su4_inactive_of_le_four`, `su4_filter_eq_univ`, `su4_restricted_sum_eq`,
  `su4_no_magic_enhancement`, and `su4_active_at_five` as the non-vacuity
  witness (the bound bites only from `n = 5`).

**That file's own docstring records a trap worth carrying forward**: its two
content-bearing fields once asserted `E_gate = E_0 · log(1/W_λ)` **for all
reals with no hypothesis relating them**, so instantiating `E_gate := 1`,
`E_0 := 0` made `¬ Nonempty …` provable — the class had no instance *and could
not have one*. Repaired on an owner ruling, along with a `.ts` ref that pointed
at a different, vacuous `holds : Prop` stub.

**So half B is probably a verify-and-close, not a formalisation.** What it needs
is someone to state what "the gap" was and check it against these two files. Do
that before writing any new Lean here.

## Half A — "`H₃` Delta baryon map" — and it SPLITS by dimension

The content side exists: `prop:borromean-decuplet`
(`folio/quantum-observable-universe/eightfold-way/borromean-decuplet-derivation.md`)
tabulates `Δ⁺⁺ (uuu)`, `Δ⁺ (uud)`, `Δ⁰ (udd)`, `Δ⁻ (ddd)` with `I₃` and
strangeness, alongside `Ω⁻ (sss)`. Its `lean.ref` is
`qou:QOU.Eightfold.RowCapObstruction.eightfold_channels_at_three` — i.e. it
points at the **obstruction**, not at a `Δ` map. There is no `Delta baryon` /
`DeltaBaryon` / `delta_baryon` declaration anywhere in the Lean tree (measured).

**The split, and it is the useful part of this bean.** Symmetric three-index
representations have `dim Sym³(k^N) = C(N+2, 3)`:

| `N` | `dim Sym³` | multiplet |
|---:|---:|---|
| 2 | **4** | the `Δ(1232)` isospin quartet `Δ⁺⁺, Δ⁺, Δ⁰, Δ⁻` |
| 3 | **10** | the full flavour `SU(3)` decuplet (adds `Σ*, Ξ*, Ω⁻`) |

So:

- **The `Δ` quartet alone needs only `N = 2`** and is therefore **not** gated by
  `qou-j3w6`. It is `Sym³` of the existing fundamental, a finite construction,
  and is startable today.
- **The full decuplet needs `N = 3`** — `Ω⁻ (sss)` is strange, so it cannot
  exist at `N = 2` — and is gated by `qou-j3w6`. The block's own line 12 names
  `Δ⁺⁺(uuu)`, `Δ⁻(ddd)` and `Ω⁻(sss)` in one breath, which is how the two
  scopes got bundled.
- **And `RowCapObstruction.lean` already proves the gated half is blocked**, not
  merely unstarted: at `N = 2` the alternating channel `dim V_(1³) = C(N,3)`
  **vanishes**, so there is no singlet, hence no `8 ⊕ 1` and no `η′`, for
  **any** `q`. Scope-(b), invariant cited (the Schur-Weyl row cap).

## Options

1. **Split this bean in three** — (a) verify-and-close half B against the two
   existing files; (b) formalise the `Δ` isospin quartet as `Sym³` at `N = 2`,
   ungated; (c) the full decuplet, `blocked-by qou-j3w6`. Cost: three beans, no
   content change. **Recommended (agent judgement)** — it is the same fix
   `qou-6766` needed, and (b) is the only genuinely startable piece here.
2. **Do (a) only** and leave the rest as one bean. Cheapest; leaves a bundle.
3. **Block the whole bean on `qou-j3w6`.** Wrong, and recorded as wrong so
   nobody does it: it would park the `N = 2` quartet, which the gate does not
   touch.
4. **Nothing.**

**Default if unanswered: (4).** The bean stays a two-item title that cannot be
claimed, which is why it has not moved since 2026-07-20.

**Blast radius:** `prop:borromean-decuplet`, `conj:wigner-su4-from-spin-isospin`,
`QOU/BraidsAndKnots/WignerSU4FromSpinIsospin.lean`,
`QOU/Mass/WignerSU4RowBoundInactive.lean`,
`QOU/Eightfold/RowCapObstruction.lean`. No compute, no witness.

---
# qou-nmib
title: 'Delta(1232) quartet at N=2: the I_3 labelling is DONE and sorry-free; open only on a wiring decision (no content block cites QOU/EightfoldWay/)'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - 8f-lean
created_at: 2026-07-20T00:46:28Z
updated_at: 2026-10-10T10:47:33Z
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


## Split enacted 2026-10-10 — this bean is now the UNGATED `Δ`-quartet half only

Option 1 of the options above, enacted. Retitled, and the other two halves moved
out so each can be claimed:

| half | bean | state |
|---|---|---|
| `Δ(1232)` isospin quartet, `Sym³` at `N = 2`, `dim = 4` | **this bean** | **startable today — the one genuinely ungated Lean item on the `8f-lean` front** |
| "Wigner `SU(2)` gap resolution" | **`qou-x0th`** | probably a verify-and-close against two existing sorry-free files |
| full flavour-`SU(3)` decuplet, `dim = 10`, needs `N = 3` | **`qou-3oi0`** | `blocked-by qou-j3w6` |

**Scope of this bean, stated so it does not re-absorb the other two.** Formalise
`Sym³` of the existing `N = 2` fundamental and the map onto the four quartet
states `Δ⁺⁺, Δ⁺, Δ⁰, Δ⁻` indexed by `I₃ ∈ {+3/2, +1/2, −1/2, −3/2}`. The
dimension is `C(N+2,3) = C(4,3) = 4` at `N = 2`, which is a finite computation.
**Do not touch `Ω⁻`, `Σ*` or `Ξ*`** — they are strange, need `N = 3`, and belong
to `qou-3oi0`.

Content side already exists: `prop:borromean-decuplet` tabulates all four quartet
states with `I₃` and strangeness.

**Watch the base ring (§7c).** `Sym³` over a generic `{R : Type*} [CommRing R]`
is the right signature; there is no archimedean construct in a dimension count,
so do not specialise to `ℝ`.


## 2026-10-10 — LEAN HALF DONE. Stays open on a wiring decision, not on mathematics.

Worked. The corpus-grep answered half of it before any Lean was written, which is
the headline.

### Already existed — do not re-derive it

`folio/quantum-observable-universe/lean/QOU/EightfoldWay/SymmetricChannelDimension.lean`
(163 lines before this change, sorry-free) already proves the dimension content,
and proves it **properly**:

```
finrank_homogeneousSubmodule :
  Module.finrank K (homogeneousSubmodule (Fin N) K n) = (N + n - 1).choose n
```

general in `N`, `n` and the base ring, via an explicit `Equiv` from the weight
diagram to `Sym (Fin N) n` and Mathlib's `Sym.card_sym_eq_choose`, with
`quadruplet_dim = 4` (**the Δ quartet, N = 2**) and `decuplet_dim = 10` as `rfl`
consequences, plus `decuplet_ne_quadruplet` as an explicit anti-fit guard.

**This file is the standard the arc should be held to**, and it is worth saying
next to `qou-x0th`: real Mathlib imports, a real `Equiv`, real `Module.finrank`,
numerals as consequences of a general theorem. Compare `S5SO3FiberAction.lean`
(same arc) — zero imports, `decide` over hardcoded tables, one theorem that is
`1 ≠ 2`.

### What was missing is exactly what this bean named: the I₃ map

A dimension count does not say the four states **are** the isospin quartet. Six
declarations added, sorry-free, axioms `[propext, Classical.choice, Quot.sound]`:

| declaration | content |
|---|---|
| `coordSum_of_mem` | `degree = n ⟹ n_u + n_d = n`, via `Finsupp.degree_eq_sum` |
| `twoI3` | `2I₃ = n_u − n_d`, doubled to stay in `ℤ` (no division, no `ℝ`) |
| `quartetPoint` / `_mem` | the explicit point `u^(3−k) d^k`, shown to lie in the diagram |
| `twoI3_quartetPoint` | `2I₃ = 3 − 2k` — the ladder is **attained** |
| `twoI3_mem_ladder` | every point carries one of `3, 1, −1, −3` — **closed** |
| `twoI3_odd` | `2I₃` is odd everywhere — the half-integral/fermionic fact |
| `twoI3_injOn` | distinct points ⟹ distinct `I₃` — the label is **faithful** |

Attained + closed make the value set exactly those four. `injOn` is what upgrades
`quadruplet_dim`'s 4 from "four basis vectors" to "four isospin-labelled states",
which is the bean's actual ask.

**Negative-controlled**, since this bean sits beside `qou-x0th`, where the
complaint was precisely that theorems were not falsifiable. Two wrong versions
were written and confirmed to FAIL: the integer-weight ladder `{2, 0, −2}` at
degree 3 (`omega` fails on all four branches), and `twoI3_odd` restated at degree
2 (fails — oddness is genuinely degree-dependent, not an artifact of the
encoding). A first attempt at the controls errored on an unbound `n` under
`autoImplicit=false`; **that was my harness and was nearly reported as the
result**, which is the `hadron_knot_table` trap one level down.

### Scope held at N = 2

The new section's docstring **states and does not prove** that at three flavours
`I₃` alone is not faithful (strangeness is an independent coordinate). That is
`qou-3oi0`, is gated on `qou-j3w6`, and is deliberately not touched.

### Verification

- `lean` direct, `-DautoImplicit=false -s 65536`: **exit 0**, 7.2 s.
- `scripts/lean-library-sweep.py --only-exact`: **1 ok, 0 RED**.
- `scripts/check-sidecars.sh`: `[library Lean — no ℝ, generic OK]` (§7c).
- `#print axioms` on all six plus `quadruplet_dim`: **no `sorryAx`**.
- Zero `native_decide`, zero `sorry` in the file.

### Why this bean STAYS OPEN — and it is not the mathematics

`QOU/EightfoldWay/` holds two substantive sorry-free modules (this one and
`MesonOctetTracelessSplit`) and **neither is imported in `QOU.lean`**, whose 931
imports are all `QOU.Eightfold.*` — singular, a live 45-module directory sitting
beside a near-twin.

**They ARE built**, so "orphan" is wrong about the build: the paper lakefile's
`globs = ["QOU", "QOU.+"]` were widened for exactly this (bean `qou-rc7b`, whose
comment records that 785 of 1655 modules were previously never compiled). What is
true, and is what matters, is that **no content block carries a `lean.ref` to
either module**. A sorry-free derivation that no block cites does not reach the
paper.

**That is a content decision and so is the owner's**: `prop:borromean-decuplet`
currently points its `lean.ref` at
`QOU.Eightfold.RowCapObstruction.eightfold_channels_at_three` — the *obstruction*
— which is arguably the honest current state and may be deliberate. Pointing a
block at `quadruplet_dim` instead, or adding a block for the quartet, changes
what a proposition claims. Not chosen here.

**Default if unanswered: nothing changes.** The theorems stay built and
uncited; no number moves anywhere.

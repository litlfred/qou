# GAP-4 is #3551 (same max-contact principle, α-level); GAP-3 (derived R(q,x)) is the frontier

**Date:** 2026-07-11
**Branch:** `claude/gap4-alpha-bridge-gap3-frontier-2026-07-11`
**Beans:** `qou-3lsb` (GAP-4), `qou-6poy` (GAP-3). **Type:** synthesis / anti-duplication bridge
(docs + beans only, no compute).

## Why this is a bridge, not a probe

GAP-2b (#3638) redirected the many-body binding term from the nucleon level to the **α-cluster
level**. Corpus-grep before writing a GAP-4 probe surfaced that the α-cluster contact structure is
**already computed** — the anti-duplication discipline working as intended (cf. #3585). This note
connects GAP-2b's nucleon-side finding to the existing α-level result and localizes what actually
remains.

## GAP-4 is already resolved by #3551 (same principle, one scale up)

`bk_alpha_geometry_selection.py` + the merged PR #3551 read the binding of α-conjugate nuclei as

  `B(nα) = n_α·B(⁴He) + N_contacts·b_αα`,

with `N_contacts` the **max-contact** edge count of the α-cluster (deltahedra exact for n_α ≤ 6),
and test that the geometry is **selected by contact-maximization** — the *identical* variational
max-contact principle as GAP-1 (#3630), evaluated one scale up (α's instead of nucleons). The α-α
bond count is the same deltahedral `3n−6` formula: ⁸Be (2α) 1 bond, ¹²C (3α) 3, ¹⁶O (4α) 6,
²⁰Ne (5α) 9, ²⁴Mg (6α) 12.

**So the QOU binding closure has a two-scale max-contact structure, now established from both ends:**

| scale | unit | edge count | who |
|---|---|---|---|
| nucleon | nucleon (unit sphere) | max-contact `3A−6` | GAP-1 (#3630) |
| α-cluster | α particle | max-contact `3n_α−6` | #3551 |

GAP-2b's key evidence — the Li many-body residual is **constant** (~8 MeV, CV 6%) while the nucleon
count grows — is exactly what the α-cluster level predicts: ⁵Li/⁶Li/⁷Li = α + valence share one
α-core, so their residual is α-core-fixed, not nucleon-count-scaling. The nucleon-side decoupling
(GAP-2b) and the α-side contact model (#3551) are the **same fact from two directions**.

## What actually remains in GAP-4 (narrowed)

1. **The ²⁰Ne one-bond DOF** — ²⁰Ne is under-bound by ~1 contact (its known prolate α+¹⁶O
   structure is *not* a maximal-contact cluster). `bk_alpha_geometry_selection.py` surfaces this
   as a genuine deviation, not a fit knob. Halo/cluster nuclei below max-contact (the original
   GAP-4 statement) are this class.
2. **`b_αα` is empirical** (≈2.4 MeV, the Hafstad–Teller value, pinned from ¹²C/¹⁶O). Deriving it
   from the substrate is a genuine open item — but it is the α-level analogue of the nucleon-level
   per-bond `b*` (#3545 Part 12, the connected `tr_M` / centered Gram norm), so the derivation
   route is the **same** object one scale up.

Because GAP-4's core is #3551, bean `qou-3lsb` is marked **resolved-by-#3551**, with the two items
above as its narrowed remainder (kept open; `b_αα` derivation is the substantive one).

## GAP-3 is the genuine frontier (derived R(q,x))

With GAP-1 (2-body, derived), GAP-2 (3-body = irreducible, localized), GAP-2b (many-body =
α-cluster), and GAP-4 (= #3551) all resolved or bridged, the single genuinely-open research-grade
leg is **GAP-3: the derived q-difference kernel `R(q,x)`** that produces the per-order weights
`wₙ` without a fit. #3545 Part 3 established no parameter-free constant-ratio kernel reaches 5%
(a tuned one is the banned 7th ansatz); the honest target is `R(q,x)` derived from the **fibre
root-of-unity singularity structure of `λ_SW`** — the s5-so3 keystone / Habiro-ring territory
(`docs/coordination/s5-so3-keystone.md`), now ungated (#3607). This is a multi-session
formalize-first effort, not a single probe: the invariant `R` must reproduce is the `D(m)` Habiro
tower (#3545 Part 2, `(q−1)²·Φ_cyclotomic` leading structure).

**Net:** the binding-closure gap map (#3620) is now — nucleon 2-body ✓ (GAP-1), 3-body localized
✓ (GAP-2/2b), α-cluster many-body ✓ (GAP-4 = #3551); the frontier is the **single** derived-`R(q,x)`
weight kernel (GAP-3), and the per-bond/per-α-bond strengths (`b*`, `b_αα`) as its two-scale
substrate targets.

## Discipline

Docs/beans only. No compute (the α-level compute is #3551; duplicating it would violate
anti-duplication). No fit, no wiring. Scope-(a) synthesis.

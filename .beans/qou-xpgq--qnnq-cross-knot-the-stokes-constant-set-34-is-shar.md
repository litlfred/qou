---
# qou-xpgq
title: 'qnnq cross-knot: the Stokes constant set {3,4} is SHARED by 4_1 and 5_2 — prunes crossing-number / #connections / block-size as its index; braid-index (Hecke H_3 Wedderburn) survives; 6_1 predicts {5,10} vs R1''s {5}'
status: in-progress
type: task
priority: normal
created_at: 2026-08-19T19:47:35Z
updated_at: 2026-08-19T19:48:17Z
---

## Finding (scope-(a), probe exit 0, 7/7)

`computations/probes/qbeta_qnnq_stokes_constant_set_crossknot_probe.py`

4₁ and 5₂ carry the **same** GGM Stokes-factorization constant set `{3,4}`
while differing in every other candidate driver:

| driver | 4₁ | 5₂ | same? |
|---|---|---|---|
| crossing number | 4 | 5 | NO |
| #bdry-parabolic connections | 3 | 4 | NO |
| geometric block size | 2×2 | 3×3 | NO |
| **braid index** | **3** | **3** | **YES** |
| Stokes constant set | {3,4} | {3,4} | YES |

Sources (both committed, not re-derived): `aomega-qzero-dt-count.witness.json`
(4₁, Lean-proved q→0 anchor) and `qbeta-g3-5two-stokes-sandwich.witness.json`
(5₂, exact against GGM's printed (96/97) factorization, constants {3,4}; the
`−9` entry is `3·3`, a composite of the product, not an elementary constant).

**What this prunes.** The corpus flagged "braid index 3 / crossing number 4"
as an untested coincidence-trap pair (2026-08-02 symmetry-constant-target
audit §3). The 5₂ point separates them: crossing number goes 4→5 while the
constant set does not move, so **crossing number cannot index {3,4}**. Same
argument prunes #connections (3→4) and block size (2→3) *as the index of the
constant set* — this does NOT touch R1's live `DT_max = #connections` handle,
which is a different quantity.

**What survives (CANDIDATE, not derived).** A braid-index-indexed reading:
the Wedderburn pair of `H_n` at the braid index,
`(#blocks, Σ_λ dim V_λ) = (p(n), I(n))` with `I(n)` the involution count
(Frobenius–Schur; verified from hook lengths in the probe). `n=3 → (3,4)`.

**Discriminating prediction on the corpus's own missing datum.** `qou-btvl`
records 6₁'s independent resurgence DT count as *the* missing third-knot test
point. 6₁ has braid index 4, #connections 5:
- R1 (#connections) predicts a **5**
- Wedderburn candidate predicts the pair **{5, 10}**

The **10** is the discriminator; R1 does not produce it.

## Discipline

Two knots of equal braid index do **not** force a rule. The AGENTS.md bar is
"across knots AND structurally forced" — the *forced* half is absent, so
`{3,4}` is **not** declared derived and **qou-qnnq stays open**. Nothing
wired, no fit, no c_k touched, no tier change. All arithmetic exact integer.

Incidental: `precision-gates.sh --changed` is green, and its no-free-parameter
certificate reports exactly one untraceable literal on the canonical
prediction path — `A_omega = 3` at `qbeta_t4_stokes3_crux_probe.py:60`, i.e.
this very open leg.

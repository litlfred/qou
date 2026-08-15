---
# qou-xu5t
title: 'MISLABEL: strand-twist ''4 of 10,000 survive'' has zero selectivity - forced by 1x2x2x1 composition counts'
status: completed
type: task
priority: normal
created_at: 2026-08-08T13:03:41Z
updated_at: 2026-08-14T18:49:15Z
---

Found by the SM/eightfold epistemic accounting,
`docs/audits/2026-08-08-sm-eightfold-epistemic-accounting.md` §5.1
(Finding 5, material/presentation). **This is the one materially misleading
number in either chapter.**

**Claim as presented (3 sites):** *"of 10,000 helon-style assignments, only 4
survive the spectrum + nucleon-GMN battery"*, with the `u`-quark twist
`{0,1,1}` and electron twist `{-1,-1,-1}` **"uniquely determined"**.
- `content/quantum-observable-universe/eightfold-way/flavor-charge-assignments.md:57-66`
- `content/quantum-observable-universe/eightfold-way/eightfold-open-problems.md:70-74`
- `content/quantum-observable-universe/appendix-standard-model/sm-open-problems.md:11`

**The result is forced arithmetic with zero selectivity content.** The
battery's constraint is the helon normalisation `Q_twist = totalTwist/3`
(`computations/strand_twist_y_battery.py:10`), i.e. `totalTwist = 3Q` per
flavour. Multiset counts of 3 draws from `{-1,0,+1}` by sum:

```
T:      -3  -2  -1   0  +1  +2  +3
count:   1   1   2   2   2   1   1      (total 10 = the witness's
                                         search_space.multisets_per_flavour)
```

Required `T = 3Q`: `u→+2`, `d→-1`, `ν→0`, `e→-3`. Surviving options per
flavour: `1 × 2 × 2 × 1 = 4`.

**Reproduced element-for-element** against
`computations/strand-twist-y-battery.witness.json`
`.data.survivors.per_flavour_multisets`:

| flavour | required T | enumeration | witness |
|---|---|---|---|
| u | +2 | `[(0,1,1)]` unique | `[[0,1,1]]` ✓ |
| d | -1 | `[(-1,-1,1),(-1,0,0)]` | 2 opts, first `[-1,-1,1]` ✓ |
| ν | 0 | `[(-1,0,1),(0,0,0)]` | 2 opts, first `[-1,0,1]` ✓ |
| e | -3 | `[(-1,-1,-1)]` unique | `[[-1,-1,-1]]` ✓ |

**Three consequences.**
1. `10,000` is `10⁴` — the **unconstrained** product across 4 flavours. The
   constraint **factorises per flavour**, so quoting "4 of 10,000" presents a
   factorised constraint as a global search and reads as ~2500× selectivity
   where there is none.
2. The "uniquely determined" `u` and `e` multisets are **compositional
   accidents**: `T=+2` and `T=-3` each admit exactly one multiset of three
   draws from `{-1,0,+1}`. That is a fact about compositions, not about the
   framework's braid words. `d`, `ν` are 2-fold for the same reason.
3. The target was the input: the spectrum condition *requires* reproducing the
   known SM first-generation hypercharges, and the `Z₆` block
   (`witness.data.z6.sm_table_ok`, all `True`) checks that the **SM table**
   satisfies `Z₆` (a known Baez–Huerta fact), not that the survivors do
   anything.

**The tier label is NOT wrong — do not escalate this to a fit accusation.**
The witness `description` says "EXPLORATORY"; `flavor-charge-assignments.md`
says the multisets are "enumerated, **not derived** from the framework's braid
words, so the conjecture remains open"; `eightfold-open-problems.md:75-77`
names the derivation gap precisely. Nothing is wired to production. The defect
is purely **presentation**: the numbers carry an evidential charge the
computation does not support.

**Suggested fix (content edit, 3 sites, needs sidecar + render-QA):** replace
"of 10,000 … only 4 survive" with the per-flavour factorisation — e.g. "the
normalisation `Q_twist = T/3` fixes `totalTwist = 3Q` per flavour; the
residual freedom is the number of twist multisets realising each `T`
(`1 × 2 × 2 × 1 = 4`), a composition count rather than a selectivity result."
Drop or requalify "uniquely determined".

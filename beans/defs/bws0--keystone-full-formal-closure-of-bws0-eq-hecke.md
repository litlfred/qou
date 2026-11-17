---
# bws0
title: 'Keystone: full formal closure of bwS0_eq_hecke (the loc_matches gate)'
status: in-progress
pr: 8283
type: feature
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-07-27T00:30:00Z
updated_at: 2026-10-04T15:10:39Z
parent: b9cj
---

Full formal closure of `bwS0_eq_hecke` (`KeystoneVerlindeSMatrixBridge.BWVacuumRowIsHecke`) —
the single open conjecture that `loc_matches` (the W_λ keystone / Subgoal-2, m_p·m_μ) reduces to:
the Chern–Simons/WRT gauge vacuum row `bwS0(λ)` equals the Hecke modular datum `d_q(λ)/√(Σ d_q²)`
at real q>1.

**Strategy (PR #4365):** reduce the conjecture to named/cited inputs via interpolation rigidity,
then discharge each input as far as honest. `bwS0_eq_hecke` is NOT provable outright (it rests on
the TQFT identification WRT = BW-localization, a physics input — §Axiomatization-is-NOT-a-Proof);
the goal is to isolate the irreducible content and Lean-prove everything else.

Decomposition (see child task beans bwsa–bwse):
- rigidity engine + distinct root points — DONE (bwsa)
- root realization + value-map continuation — DONE (bwsb, #4365)
- WRT=modular-data agreement across enough roots — OPEN (bwsc)
- bwS0 bounded-degree (Habiro rigidity) — OPEN (bwsd)
- WRT=BW-localization identification — irreducible cited input (bwse)

Closure = bwsc + bwsd landed; then bwse is the one remaining *cited* (not derived) hinge.


---

## Decomposition corrected 2026-09-03 — the residual is two chips, not three

The list above still reads:

```
• WRT=modular-data agreement across enough roots — OPEN (bwsc)
• bwS0 bounded-degree (Habiro rigidity)          — OPEN (bwsd)
```

**`bwsd` is not open.** It was dissolved on 2026-08-01 (PR #4402): `KeystoneHabiroInfiniteRigidity.eq_of_habiro_root_agreement` uses the infinite fibre-root family, so agreement at all roots forces equality with no degree bound at all. Its own bean says so; only its title (which still ends "(OPEN)") and this list disagree. The residual is:

```
• bwsc — WRT = modular-data agreement            OPEN
• bwse — WRT = BW-localization identification    irreducible cited input, not to be "proved"
```

### And bwsc's price is lower than this ledger records (PR #6459)

`bwsc` set the obligation at level `N >= 7` from *"max mark-6 => degree 5 in t"*. The mark-6 block is `d((3,1,1)) = [5] + 1 = t^4 - 3t^2 + 2` — the A5-split `3 + 3'` signature — **not** `[6] = t^5 - 4t^3 + 3t`. Both equal `6` at `t = 2`, which is what the mark names; the degrees are `4` and `5`. Max degree over the four blocks is `4`, so five points suffice and **level 6** closes the `n = 5` case.

So the closure condition in this bean's last line — *"Closure = bwsc + bwsd landed; then bwse is the one remaining cited hinge"* — should read: **closure = bwsc landed** (at level 6, or via the all-roots family with no degree hypothesis), then `bwse`.

Neither correction touches the open content. `bwsc` is still the WRT agreement itself, of which `KeystoneLRAmplitudeReal` (#4365) supplies the `Sigma(2,3,5)` slice; `bwse` is still a physics input that `AGENTS.md §Axiomatization-is-NOT-a-Proof` forbids laundering into a derivation.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-03 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Round 56 Implementation Progress (PR #8283)
- **Status:** `in-progress` (per no-unilateral-closure policy)
- **PR:** https://github.com/litlfred/qou/pull/8283 (head `f53a095b5ee34373c44ef4b0b400e85b12af4c1c`, Commit 1 `0e2f86d58bac8f2f07854f3515aabf15d9779cd3`)
- **Lean 4 Module & Theorems:** `QOU/AlphaEM/MellorMelvinModDeltaAndBws0DegreeFourClosure.lean` (`bws0_mark6_a5_split_degree_four_vs_degree_five`)
- **80-dps Witness:** `computations/probes/round56-mellor-melvin-bws0-stokes-dt-qholonomic.witness.json` (`scriptHash: d98411981e4d`, `allPassed: true`, `0` raw `float64`)

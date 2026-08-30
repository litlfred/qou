---
# qou-u6cz
title: 'GAP: qbeta-ck-basis-constrained-pslq.witness.json is STALE and asserts allPassed:true for a chain that now FAILS'
status: todo
type: task
created_at: 2026-08-15T15:14:19Z
updated_at: 2026-08-15T15:14:19Z
---


## Finding

Re-running `computations/probes/qbeta_ck_basis_constrained_pslq.py` **unmodified,
at its committed source**, against current `main` reproduces neither the committed
witness nor its own assertion:

| field | committed witness | re-run today |
|---|---|---|
| `c3_reproduced_canonical` | `-2.02018812814143945582016855395` | `-974.382476607697851630950275826` |
| assertion `extraction_chain_reproduces_cache_c3` `computed` | `1.583530407934892e-30` | `972.3622884795565` |
| assertion `passed` | `true` | **`false`** |
| `allPassed` | `true` | **`false`** |
| `sigma_Q_rel_needed_for_minimal_budget` | `7.88e-16` | `3.8e-13` |

The script is **pure** — `Q0_CANONICAL`, `M_E_MEV`, `Q_BETA_CODATA_MEV` and
`C3_EMP_CACHE` are all hardcoded `mp.mpf` literals and `ladder_chain` is closed-form
arithmetic — so identical source must give identical output. The producer therefore
changed after the witness was written (witness `scriptCommitSha e6abd349`,
`computedAt 2026-07-11`) and was never re-run. The Stage-1 verdict
(`ENTROPY-BLOCKED`) is unchanged, but it is now reached through a
`c_3` that is ~500× off the cache value it claims to reproduce.

## Not a simple z-convention swap

Tested five candidate `z` at the canonical q₀ against the committed target
`c_3 = -2.0201881…`; none is close:

| z | value | c_3 | \|Δ\| |
|---|---|---|---|
| `q³/(q²+1)` (convention D — current source) | 0.612688 | −974.382 | 972.4 |
| `q²/(q²+1)` | 0.551982 | −482.107 | 480.1 |
| `q/(q²+1)` | 0.497291 | +17.472 | 19.5 |
| `1/(q²+1)` | 0.448018 | +513.137 | 515.2 |
| `q³/(q⁴+1)` | 0.543120 | −404.772 | 402.8 |

So `alpha` / `Q_N1` / `Q_A` structure moved, not just `z`.

## Disposition

Belongs to the Q_β trace-convention front (**PR #5111**, bean `qou-b3nk` —
"settle or register disputed"), NOT to a drive-by witness refresh. Do **not**
regenerate this witness to make it green: `allPassed:false` is the honest current
state, and committing it silently would land a red assertion whose cause is an
unsettled convention.

Blocks `qou-s6b9` (the `Vol(4_1)=2*Lambda(pi/3)` key mislabel at line 313 — a
correct rename that cannot land until this witness can be regenerated validly).

Found while completing the Vol(4₁) drain in PR #5119.

---

## 2026-08-30 — the "Not a simple z-convention swap" section is WRONG (bean `qou-l2we`)

It **was** a simple z-convention swap. The five candidate `z` tested above are
all *rational* functions of q; convention C itself — `z = sqrt(q)/(1+q)`, the one
form carrying a square root — was never tried. It reproduces the committed target
exactly:

    z = sqrt(q)/(1+q)   ->  c_3 = -2.02018812814143945582   |delta| ~ 1e-30

which is the committed assertion's own `computed: 1.583530407934892e-30`. So
`alpha`/`Q_N1`/`Q_A` did NOT move — only `z` did, from C to D, in
`ladder_chain`. Same defect `qbeta_ck_cache.py` carried until `a340f7c87`.

This matters because the disposition above routes the bean to the Q_β
trace-convention front (PR #5111 / `qou-b3nk`) on the strength of that wrong
premise.

**Not reopened as a z-swap, though**: the owner ruling is to **excise convention
C**, so the probe was fixed by REMOVING the frame rather than picking one — its
entropy verdict never needed a Markov `z` (`u = b·hbar_q^2` contains none). See
`qou-l2we` for the resolution and the retired assertion.

Status left as-is — not this bean's owner. The parts of it that still stand:
`allPassed:false` was the honest state, and it must not be made green by
retuning. It was not: a false assertion was retired and a frame-immunity
assertion proved in its place.

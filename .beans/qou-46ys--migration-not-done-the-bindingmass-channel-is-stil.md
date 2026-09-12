---
# qou-46ys
title: 'MIGRATION NOT DONE: the binding/mass channel is still convention C while the decay channel is on D'
status: todo
type: task
priority: high
created_at: 2026-09-12T19:04:20Z
updated_at: 2026-09-12T19:06:21Z
---

**What is wrong.** The owner ruled convention D canonical on 2026-08-15 and
excised C. The **decay** channel has been migrated (`z_D` now scores Q_β). The
**binding / mass** channel has not, and says so in its own source.

**Primary evidence, not inference.**
[`computations/gap_a3_overshoot_robustness_check.py`](../computations/gap_a3_overshoot_robustness_check.py)
lines 52-67, its own comments, twice:

> `TRM` is CONVENTION C. `TRM["D"] = 0.38835725751524` is the convention-C
> deuteron `|tr_M|`; under the canonical convention D the same quantity is
> [different] … Convention C was excised 2026-08-09 … **Re-deriving is
> authorial work** and is [not done here]

and at line 67: *"tr_M(β_K) from the #2635 run (`y_lambda_at` q₀ + `chi_all_lambda`)
— **CONVENTION C**"*.

**Why this is the most exposed channel, measured.** `z` is not a separate knob —
**it *is* the `y_λ`**, at step ⑥ of the canonical chain (the Frobenius pairing
`tr_M = Σ_λ y_λ χ_λ`). Binding is the *same* pairing,
`B(K) = m_e · Σ_λ y_λ χ^λ Δ_λ` over partitions of `n = 3A`, and convention D sets
`y_λ = 0` for every `ℓ(λ) ≥ 3`:

| A | n = 3A | partitions | ≤2 rows | **killed** | fraction of dim kept |
|---|---|---|---|---|---|
| 1 | 3 | 3 | 2 | 1 | 83.3 % |
| 2 | 6 | 11 | 4 | 7 | 18.3 % |
| 3 | 9 | 30 | 5 | 25 | 1.34 % |
| 4 | 12 | 77 | 7 | 70 | **0.0434 %** |
| 5 | 15 | 176 | 8 | 168 | **7.41e-6** |

At ⁴He, D keeps **7 of 77 blocks**. So the open binding-magnitude problem — the
"separate super-pairwise additive extensive object" of the `Δ_λ` gate — is being
attacked with weights that under the canonical convention are almost all zero,
while the code computing them is still on C. **No bean recorded that before this
one.** (The `Δ_λ` half is settled and unaffected:
`Δ_λ = (−1)^{n(λ)}·dim V_λ`, sorry-free, general `n`.)

**Normalisation is NOT the issue** — `Σ_λ y_λ f^λ = 1.0` exactly under D at
n = 3, 6, 9, 12 (`qbeta_zd_gap_anatomy_probe`, worst |·−1| < 1e-50). Do not spend
a session on that hypothesis; it is refuted.

**Scope of the work, and it is real.** The file itself calls re-deriving
"authorial work" — a `z`-swap is *not* valid (`QOU.QBeta.decayLadder_zC_threeRow_ne_zero`,
sorry-free, makes the C-frame ladder and the three-row forcing mutually
exclusive). So this is a re-derivation, not a substitution.

**Two acceptable outcomes, and the cheap one is legitimate:**
1. Re-derive the binding `tr_M` under D. Large, authorial.
2. **Scope every figure the binding channel publishes as C-conditional**, the way
   the `c_k` ladder already is. Cheap, honest, and it stops the straddle being
   invisible — which is the actual present harm.

Nobody owns this. Full analysis:
`docs/audits/2026-09-12-zd-gap-anatomy-and-three-undone-migrations.md` §4 and §5(b).

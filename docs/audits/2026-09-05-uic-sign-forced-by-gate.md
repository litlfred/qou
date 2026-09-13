# The wrong sign is forced by the Pass-2 gate, not by the nucleus

**Date:** 2026-09-05 · **Bean:** `qou-sv7h` · **Scope:** (a)

> ## 🛑 RETRACTED IN PART, 2026-09-12 — the title claim is refuted
>
> **Bean `qou-21oc`; PR #7253.** The gate this document says forces the sign has
> been **removed** from `unified_iterative_correction` (owner ruling, after its
> complementary-slackness justification was refuted sorry-free in
> `QOU.MassTheory.UICGateNotFromComplementarySlackness`, PR #7251). If the sign
> were *forced by* the gate, removing the gate would have to be able to change
> it. **It does not.** Re-measured over the same terms with no sign filter
> (`uic_sign_forced_by_gate_probe`, 7/7):
>
> | atom | gated sum | **ungated sum** | ratio |
> |---|---|---|---|
> | ²H | −1.3656848 | **−2.251132** | 0.607 |
> | ³H | −0.97040895 | **−1.8036172** | 0.538 |
> | ³He | −0.80794043 | **−1.7465929** | 0.463 |
> | ⁴He | −0.80209171 | **−1.3701187** | 0.585 |
> | ⁶Li | −1.0769706 | **−1.9696784** | 0.547 |
>
> **Those five are this probe's own reconstruction** — partitions with `k ≤ 6`
> only, read from the partition table with one kernel call each and no per-step
> accumulation, and ordered `["p"]*Z + ["n"]*N` rather than the producer's
> alternating ground state. At ²H (where the orderings coincide) `−2.251132`
> matches the producer's `k_exact = 6` return `−2.251131977321312` to 8 s.f.; at
> ⁴He they differ by 5.39 %. Do not quote them as producer returns.
>
> Through the **producer** itself, tier-labelled because it is not a small knob
> (²H ungated spans 43× across the tiers):
>
> | `k_exact` | ²H gated → ungated | ⁴He gated → ungated |
> |---|---|---|
> | 4 | `−0.0896 → −0.4122` | `−0.0806 → −0.2742` |
> | 6 | `−1.3657 → −2.2511` | `−0.8387 → −1.4482` |
> | **11 = production default** | `−9.1477 → −17.6908` | `−8.2016 → −15.9927` |
>
> Every ungated total is negative and **larger in magnitude**, so dropping the
> gate moves *away* from AME (²H: `+2.2246 MeV`) at every tier.
>
> **What survives:** steps **1** and **3** — `C_λ ≥ 0` on all 682 partitions,
> and `|Tr| ≥ d` in 3.4 % of `Tr ≤ 0` against 34.1 % of `Tr > 0`. Together they
> establish a **bias**: the gated subset is more negative than the slack one.
> **Step 2's inference from that bias to "B < 0 is FORCED" does not follow** and
> is withdrawn. Read "forces" as "biases" throughout below.
>
> **The A-independence section is downgraded from explanation to correlation.**
> The gated-set size is near-constant across A — but `where_the_a_dependence_is_lost_probe`
> Layer 3 finds the **raw, pre-gate** ratio already flat (1.25 / 1.16 / 1.09 at
> k = 5 / 7 / 9), so the gate is not the cause there either.
>
> Nothing measured here is wrong; one inference drawn from it was.

`815b2a46a0` measured four wrong-signed atoms and stated the gap: *"nothing here
says WHY the sign is wrong — that is the physics question this measurement opens
and does not answer."* The answer is in the LP gate rather than in the physics.

## The argument, in three measured steps

After Pass 2, `unified_iterative_correction` returns

```
B = Σ over GATED λ of  C_λ · ( ln|Tr M_λ(A)| − ln d_λ )
```

**1. `C_λ ≥ 0` for every partition.** Each factor of
`C_λ = m_e · H_q(λ) · y_λ · ρ_λ(s_*)` is separately non-negative — in particular
`y_λ = w_λ/d_λ − y_0` with `y_0 = min_λ(w_λ/d_λ)`, so `y_λ ≥ 0` **by
construction**. Measured: **0 of 682** partitions carry a negative scale.

**2. Pass 2 keeps exactly the partitions with final trace ≤ 0** and zeroes the
rest, on a complementary-slackness reading (`y_λ > 0` only where the Frobenius
constraint is tight).

**3. A trace ≤ 0 almost never has `|Tr| ≥ d`; a positive trace often does.**
Pooled over five atoms × 28 partitions:

| final trace | `\|Tr\| ≥ d` | fraction |
|---|---|---|
| `Tr > 0` | 28 of 82 | **34.1 %** |
| `Tr ≤ 0` | 2 of 58 | **3.4 %** |

A **10× asymmetry**, and it is structural rather than accidental: `Tr(I) = d > 0`,
so reaching `Tr ≥ +d` only needs the spectrum to stay aligned with the identity,
while reaching `Tr ≤ −d` needs it to overshoot through zero **and** align
coherently in the negative direction.

**Therefore** `ln(|Tr|/d) < 0` on essentially the whole gated set, every term is
a non-negative scale times a negative log, and **`B < 0` is forced — for any
nucleus.**

Per atom, at k_max = 6:

| atom | A | gated negative | slack negative | gated sum |
|---|---|---|---|---|
| ²H | 2 | **15/15** | 8/13 | −1.3657 |
| ³H | 3 | **9/9** | 13/19 | −0.9704 |
| ³He | 3 | **9/9** | 13/19 | −0.8079 |
| ⁴He | 4 | **9/10** | 12/18 | −0.8021 |
| ⁶Li | 6 | **14/15** | 8/13 | −1.0770 |

## It explains the A-independence too

`qou-sv7h` measured −7.271 / −7.742 / −7.456 / −6.829 while AME spans **12.7×**,
and could not account for it. The gated-set size across A = 2..6 is
**[15, 9, 9, 10, 15]** — roughly constant. The gate selects a nearly fixed-size
set of cancelling partitions whose log-ratios sit in a similar range whatever A
is, so **the output is a property of the gate's selection, not of the nucleus.**
Sign and A-independence have one cause.

## The tension this exposes, flagged not decided

Pass 2's own docstring derives the gate from complementary slackness. For a
constraint `tr ≥ 0`, *tight* means `tr = 0` — but the code admits **all**
`tr ≤ 0`, and a strictly negative trace is **infeasible** for that constraint,
not tight. Meanwhile the contribution `∝ ln|tr|` **diverges to −∞ as `tr → 0`**,
i.e. exactly at the partitions complementary slackness says should contribute.

Those two readings cannot both be right, and resolving it needs the primal LP,
which is not in `hecke_core_legacy.py`. Recorded as a question for whoever owns
`prop:mass-coefficient-shadow-price`.

## What is not claimed

That the gate is wrong — only that it is the mechanism. That the correct formula
is X. And **not** that the accumulator diverges: it does not, per
[`2026-09-05-uic-a1-vanishing-trace.md`](2026-09-05-uic-a1-vanishing-trace.md),
which retracts an earlier claim of mine that it does.

The table above is a direct-from-kernel reconstruction at k_max = 6 over 28
partitions; it does not reproduce the production accumulator's absolute values
(deuterium −1.366 here against production −7.271), because it omits the
q-Gaussian tier and the exact/gaussian split. It is evidence about **which
partitions carry the sign**, which is invariant to that truncation.

Reproduce: [`computations/probes/uic_sign_forced_by_gate_probe.py`](../../computations/probes/uic_sign_forced_by_gate_probe.py) — 5/5 checks.

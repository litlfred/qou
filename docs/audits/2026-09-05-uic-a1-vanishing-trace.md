# The A=1 Markov trace is zero — and the accumulator survives it. Dropping it does not.

**Date:** 2026-09-05 · **Bean:** `qou-sv7h` · **Scope:** (a)

> ## ⚠ RETRACTION — this document's first version said term 1 DIVERGES. It does not.
>
> The first version of this audit, of
> [`uic_a1_vanishing_trace_probe.py`](../../computations/probes/uic_a1_vanishing_trace_probe.py),
> of commit `2cb02fb644` and of PR #6746 concluded that
> `unified_iterative_correction` is divergent and that this explained the wrong
> sign. **That was wrong.**
>
> It was drawn from the PER-STEP decomposition, where `(2,1)` shows a `−117`
> delta at A=1, without checking that the A=2 step carries `+115` and that the
> accumulator telescopes. Measured on the returned value, bit-identical at three
> precisions:
>
> | kernel dps | `uic(1,1)`, k_max=5 |
> |---|---|
> | 50 | −0.7335499391634978 |
> | 100 | −0.7335499391634978 |
> | 150 | −0.7335499391634978 |
>
> **The sign is not explained by a divergence, and the sign question is still
> open.** What survives is below, and one part of it inverts a proposed fix.

## What is true, and measured

**1. The per-partition scale is non-negative**, every factor separately.
`C_λ = m_e · H_q(λ) · y_λ · ρ_λ(s_*)`, with `y_λ = w_λ/d_λ − y_0` and
`y_0 = min_λ(w_λ/d_λ)` — so `y_λ ≥ 0` **by construction**, and the code's closed
form `1/[k]_q!` **is** that minimum at every k = 2..11 (rel < 1e-12). Measured:
`q_hook ≤ 0` in **0 of 682**; `C_λ < −1e-12` in **0 of 682**. The 28 exact zeros
are the min-attaining `(k)`/`(1^k)` pairs.

**2. At A=1 the `(2,1)` Markov trace is exactly zero.** `|Tr|` falls without
bound as the arithmetic improves — 5.08e-21 (dps 20) → 2.67e-51 (50) →
3.93e-62 (100), 41 decades — and `log_norm` stays 0, so nothing compensates.
A census over k ≤ 5 across both deuterium steps finds **exactly one** such
(partition, step) pair in 34.

**3. And it cancels.** The accumulator telescopes:
`Σ_k (log_cur_k − log_prev_k) = log_final − ln d_λ`, so the divergent
intermediate appears once with each sign.

## The consequence that matters: V1 is the divergent option

The natural-looking fix — *a single nucleon has zero binding, so the A=1 step
should not enter* — removes **one half of a cancelling pair**. Measured at
`(2,1)` for deuterium:

| dps | A=1 delta | A=2 delta | **V0** (keep) | **V1** (drop) |
|---|---|---|---|---|
| 50 | −117.1419 | +114.9436 | **−2.198292652** | +114.9436 |
| 100 | −142.0855 | +139.8872 | **−2.198292652** | +139.8872 |

Relative movement across that precision change: **V0 8.46e-51**, **V1 0.217**
and growing.

So the intuition is right about the physics and wrong about this arithmetic: the
A=1 step is **not an additive offset**, it is one term of an exact cancellation.
Removing it does not remove a spurious contribution — it uncovers a divergence.

## V2 — the free-nucleon reference — is finite, and is a real alternative

`_step_chain_generic(..., include_inter=False)` exists precisely to build "the
disconnected intra-nucleon braid segment used for the free-nucleon baseline",
and the intra block is the gluon-level content (`B₃ + quark + gluon`).

The accumulator's baseline is `L0 = ln(dim)` — the trace of the **empty braid**.
A free nucleon is not an empty braid. Replacing the reference with
`ln|Tr_free|` gives `ln(|Tr_bound| / |Tr_free|)`, which is stable at every
precision tested and shifts the value modestly: at `(2,1)`/deuterium, **−2.2254**
against V0's **−2.1983**.

Measured across five atoms at k_max = 6 (a truncated reconstruction, **not** the
production quantity — see caveat):

| atom | A | V0 as-is | V1 drop A=1 | V2 free-ref | AME |
|---|---|---|---|---|---|
| ²H | 2 | −1.366 | −0.282 | −0.531 | 2.225 |
| ³H | 3 | −0.970 | +14.398 | −0.262 | 8.482 |
| ³He | 3 | −0.808 | +14.561 | +0.059 | 7.718 |
| ⁴He | 4 | −0.802 | +0.237 | −0.423 | 28.296 |
| ⁶Li | 6 | −1.077 | +14.526 | −1.340 | 31.994 |

**None reproduces AME's extensivity.** V1's near-constant ≈ +14.5 is entirely
the divergent `(2,1)` term where the Pass-2 gate admits it (²H and ⁴He escape
only because the gate excludes it there) — i.e. it is the artefact, not a signal.

**Caveat, stated rather than buried:** this table is a direct-from-kernel
reconstruction at k_max = 6 over 28 partitions. It does not reproduce the
production accumulator (deuterium V0 here is −1.366 against the production
−7.271), because it omits the q-Gaussian tier and the exact/gaussian split. It
is evidence about the **relative structure** of the three baselines, not about
their absolute values.

## Two notes on method

**The per-step decomposition is not interpretable on its own.** Individual step
deltas are dominated by a ±117 artefact that cancels in the total, so any
diagnostic reading `per_step` sees numbers that mean nothing individually. They
are also computed with float64 `math.log`, so summing −117.14 and +114.94 to get
−2.198 spends ~3 significant digits.

**Two over-strict thresholds in this probe hid its own findings.** The vanishing
census was first written as "≥ 10 decades" and reported **zero** pairs — the
real drop is 9.56. The V0-stability check was first written as bit-equality and
**failed**, because V0 moves at 1e-51. Both are the class catalogued in
[`2026-08-15-detector-blindness-taxonomy.md`](2026-08-15-detector-blindness-taxonomy.md),
and in both cases the probe's own assertion is what caught it.

## What is still open

The wrong sign. This audit removes one candidate explanation (divergence),
refutes one proposed fix (V1), and shows a second (V2) to be finite but not
sign-correcting. It does not say what the correct formula is, and does not touch
the extensive-term question (`qou-brng`).

Reproduce: [`computations/probes/uic_a1_vanishing_trace_probe.py`](../../computations/probes/uic_a1_vanishing_trace_probe.py) — 9/9 checks.

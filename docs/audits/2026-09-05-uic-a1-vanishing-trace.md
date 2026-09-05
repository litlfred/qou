# Why `binding_energy` is negative: term 1 takes `ln` of a trace that is zero

**Date:** 2026-09-05 · **Bean:** `qou-sv7h` · **Scope:** (a) — identifies why the
computed number is negative; does not say what the correct formula is.

## The question this answers

`815b2a46a0` measured four wrong-signed atoms and stated the gap plainly:

> nothing here says WHY the sign is wrong — that is the physics question this
> measurement opens and does not answer.

The answer is arithmetic, not physics.

## The structure of term 1

`unified_iterative_correction` accumulates, per partition and per step,

```
B_λ = C_λ · ( ln|Tr M_λ^(0..A)| − ln d_λ )
C_λ = m_e · H_q(λ) · y_λ · ρ_λ(s_*)
```

Every factor of `C_λ` is separately non-negative, and this was measured rather
than assumed (682 partitions):

| factor | why ≥ 0 | measured |
|---|---|---|
| `m_e` | a mass | — |
| `H_q(λ) = ∏_x [h_x]_q` | q-integers are positive at q₀ > 1 | `q_hook ≤ 0` in **0** of 682 |
| `y_λ = w_λ/d_λ − y_0` | `y_0 = min_λ(w_λ/d_λ)`, so the difference is ≥ 0 **by construction** | the closed form `1/[k]_q!` **is** that minimum at every k = 2..11 (rel < 1e-12) |
| `ρ_λ(s_*) = 1/(μ_λ + s_*)` | `μ_λ = Σ_x [c(x)]_q²` is a sum of squares; `s_* = (q−1)/q > 0` | — |

`C_λ < −1e-12` in **0** of 682 partitions. 28 are exactly zero — precisely the
min-attaining `(k)` and `(1^k)` pairs, where `y_λ = 0`; they surface as ~1e-18
of float64 noise rather than as 0.

**So the sign of every contribution is the sign of its log-trace factor**, and
its magnitude is a non-negative multiple of it.

## The defect

At **A = 1** — a single nucleon, no bond — the Markov trace of the **(2,1)**
block is **exactly zero**. `ln|Tr|` is therefore `−∞`, and since `C_(2,1) > 0`,
term 1 is `−∞`.

Every finite value the function has returned is an artefact of where the
arithmetic underflowed. Measured by calling the Rust kernel on the identical
chain at increasing precision:

| kernel dps | \|Tr\| | ln\|Tr\| | `log_norm` |
|---|---|---|---|
| 20 | 5.08e-21 | −46.73 | 0.0 |
| 50 | 2.67e-51 | −116.45 | 0.0 |
| 100 | 3.93e-62 | −141.39 | 0.0 |

A genuine small number stabilises; this keeps falling — **41 decades** across
that range. `log_norm` is 0 throughout, so no rescale compensates: the reported
`log_trace` **is** `ln|Tr|`.

Feeding the chain's coefficients at full precision instead of their float64
values, the fall continues without plateau: 1e-51 → 1e-81 → 1e-121 → 1e-141.
The plateaus above are the *input* precision, not the trace.

## Why this explains what `qou-sv7h` measured

Three of that bean's observations follow with no new physics:

1. **Negative on both matrix families** (old braid-violating and corrected). A
   structural zero survives the correction — both families give a vanishing
   trace here.
2. **Nearly A-independent** (−7.271 / −7.742 / −7.456 / −6.829 while the target
   spans 12.7×). The A=1 step is present for *every* nucleus and contributes
   **84.7 %** of its own step; a divergent term that does not depend on the
   nucleus dominates.
3. **Neither a sign flip nor a constant rescale repairs it.** A divergence is
   not a mis-scaled binding.

## Scope, and what is not claimed

**The other traces are fine.** A census over every partition of k ≤ 5 across
both deuterium steps finds **exactly one** vanishing pair in 34; all others are
stable to < 3 decades under a 50 → 100 dps change. This is one identifiable
term, not a general breakdown — which is what makes it worth reporting and
fixable.

Not claimed: what the correct binding formula is. Not touched: the
extensive-term question (`qou-brng` / `aaa2ef9c51`), which concerns what should
be **added** once term 1 is well-defined. That work is now differently
positioned, though — `E = AME − B_pred` was fitted against a `B_pred` whose
value is set by precision, so the extracted `E ≈ 5.4 MeV × C(A,2)` inherits
that dependence.

## A note on the detector

The census threshold was first written as "≥ 10 decades" and reported **zero**
vanishing pairs. The real drop is 9.56 decades — the detector's own threshold
hid the finding it was written to catch. It is 3 decades now. Recorded because
this is the same class as the blind spots catalogued in
[`2026-08-15-detector-blindness-taxonomy.md`](2026-08-15-detector-blindness-taxonomy.md).

Reproduce: [`computations/probes/uic_a1_vanishing_trace_probe.py`](../../computations/probes/uic_a1_vanishing_trace_probe.py) — 6/6 checks.

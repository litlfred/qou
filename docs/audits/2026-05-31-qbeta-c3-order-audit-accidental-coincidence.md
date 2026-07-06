# Q_β c_3 order audit — the "−2" is an accidental cross-order coincidence

**Date:** 2026-05-31
**Probe:** [`qbeta_multiblock_order_audit.py`](../../computations/audits/qbeta_multiblock_order_audit.py)
→ `qbeta-multiblock-order-audit.witness.json`
**Goal arm:** 1ppQ-Q_β (`docs/coordination/1ppq-qbeta.md`)
**Probe claim:** `probe-qbeta-habiro-element-search` sub-attack — the
**symbolic q-difference solve** deferred by
`claude/qbeta-habiro-element-search-2026-05-31` (PR #1585) as
"needs dedicated session".
**Status:** characterization (no closure, no fitted form). Reinforces the
`probe-c3-q0-stability` **near-match** verdict with a *structural reason*.

---

## TL;DR

The per-Wedderburn-block contributions to `Δtr_M` live at order **√u**;
the ladder coefficient `c_3` lives at order **u³**. The value `−2` that
appears in both is **five ε-orders apart** (ε¹ vs ε⁶), in two different
objects. It is a **numerical coincidence, not a structural identity** —
which is the root cause of the four-session `c_3` wire/un-wire flip-flop.

## What was computed (all exact symbolic ε-series, no fitting)

With `u = b·ℏ²` (`b² = (h²+3)/(h²+4)`, `h = q−1/q`, `ℏ = (q−1)/q`) and the
exact per-block closed forms `f_λ(q)` from
`qbeta-per-block-paper-closed-forms.witness.json`:

| object | ε-series at q=1 | order in u |
|---|---|---|
| `u = b·ℏ²` | `(√3/2)·ε² − √3·ε³ + …` | — (defines u ~ ε²) |
| `f_(3)` | `−2ε − 3ε² + …` | **√u** (ε¹) |
| `f_(2,1)` | `−ε + ½ε² + …` | **√u** (ε¹) |
| `f_(1,1,1)` | `−2ε + 5ε² + …` | **√u** (ε¹) |
| `Δtr_M = Σ_λ f_λ` | `−5ε + …` | **√u** (ε¹) |
| ladder `c_3·u³` | (c_3 multiplies u³) | **u³** (ε⁶) |

The trivial block `(3)` and the sign block `(1,1,1)` each carry the `−2`
at order ε¹; block `(2,1)` carries `−1`. This reproduces the
bridge-narrowing structural fact ("c_3 ≈ −2 originates in the
trivial/sign blocks") — but now with the **order** made explicit.

## The accidental-coincidence finding

- The per-block `−2` is the **ε¹ (= u^{1/2})** coefficient of `Δtr_M`.
- The ladder `c_3 = −2` is the **u³ (= ε⁶)** coefficient of `Q_β/Q_base`.
- They are **5 ε-orders apart**, in two different objects.

Matching the value `−2` across these orders is a category error. Every
prior `c_3 = −2` identification (J_Hopf(q=1), J−ℏ_q², the deprecated
recursive pair-rules `c_k = J^a·K^b`) sets the **u³** coefficient equal to
a quantity that natively lives at order **√u** — so it is always a
near-match with a q₀-dependent residual. This is the mechanism behind the
**2.88 % cross-anchor swing** (−2.0097 muon-pin → −2.0693 m_p-pin).

## q₀-independence diagnostic (the falsifier)

The per-block leading coefficients `{−2, −1, −2}` are **fixed rationals** —
identical at the muon-pin and m_p-pin q₀ (swing = 0 to compute precision).
The empirical `c_3` swings 2.88 %. Therefore the swing **cannot** live in
the block structure; it lives entirely in the categorical map
`f: Δtr_M ↦ Q_β`.

## What this settles, and the sharpened open problem

| | status |
|---|---|
| per-block `Δtr_M` structure (`−2/−1/−2` at ε¹) | **proved, q₀-independent** |
| `c_3 = −2` as a ladder (u³) coefficient | **near-match** (now with a structural reason: wrong order) |
| categorical map `f: Δtr_M (√u) ↦ Q_β (c_3 at u³)` | **open** |

**The open problem is NOT "which near-match value for `c_3`"** (the
four-session trap). The value `−2` is settled as an accidental ε¹
coincidence. **The open problem is the map `f`** — a q-dependent
**scaling / eigenphase** that bridges order √u to order u³. This is the
same object the bridge-narrowing audit identified when it found "the
residual lives in SCALING (eigenphase), not Δ(net)". The Habiro element,
if it exists, is this scaling map — not a value for `c_3`.

## Discipline note

No fitted form is proposed (no 7th near-match candidate). Per the
AGENTS.md flip-flop framing and the `canonical-ck-tiered-not-binary`
qa-criterion, the result is reported **tiered**: proved block structure /
near-match `c_3` / open `f`-map. This probe is a *characterization that
prevents future flip-flops*, not a closure.

## Cross-references

- Coordination ledger: [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md)
- Bridge narrowing (6 ruled-out mechanisms): [`2026-05-31-qbeta-bridge-narrowing.md`](2026-05-31-qbeta-bridge-narrowing.md)
- Recursive pair-rules + Habiro PDE: [`2026-05-30-qbeta-recursive-pair-rules-and-habiro-pde.md`](2026-05-30-qbeta-recursive-pair-rules-and-habiro-pde.md)
- c_3 q₀-stability verdict (near-match): [`2026-05-31-qbeta-c3-q0-stability-verdict.md`](2026-05-31-qbeta-c3-q0-stability-verdict.md)
- Truncation-order canonical framing (Rule 4, tiered): [`2026-05-31-qbeta-ck-truncation-order-canonical-framing.md`](2026-05-31-qbeta-ck-truncation-order-canonical-framing.md)

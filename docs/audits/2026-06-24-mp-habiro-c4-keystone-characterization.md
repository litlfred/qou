# m_p term-6 Habiro residue `c_4` — keystone characterization

**Date:** 2026-06-24
**Beans:** `ovud` → `s5bb`
**Predecessor:** PR #2691 (proved F_Bor `/q³` exact; located the fit in `habiro_ratio`)
**Probe:** [`computations/mp_habiro_c4_keystone_probe.py`](../../computations/mp_habiro_c4_keystone_probe.py)
+ [`mp-habiro-c4-keystone-probe.witness.json`](../../computations/mp-habiro-c4-keystone-probe.witness.json)

## Goal

Give the s5-so3 keystone (`beans s5bb`) a precise **mass-sector** target,
with the same rigor the Q_β programme applies to its `c_k`. Formalize-first:
characterize the target and prune the easy classes before any wide search.

## Findings

### 1. `{46,4,29}` is a rounded-integer fit

Inverting the single-term model
`m_p_codata / m_p_{F_Bor only} = 1 + c_4·u⁴` (u = b·ℏ_q² ≈ 0.008517):

```
required c_4 = 46.0319    (NOT the integer 46)
```

The production "46" misses by **0.032 = 2.8× the proton-pin extraction
floor** (σ_c4 = 0.011). So "46" is a rounding of the true `46.03`.

### 2. Extraction floor — only `c_4` is data-determined

With m_p known to ~0.06 ppb (proton pin), `σ_c_k = σ_ratio / u^k`:

| k | σ_c_k (proton 0.06 ppb) | σ_c_k (formula 0.0004 ppb) |
|---|---|---|
| 4 | 0.011 | 7.6e-5 |
| 5 | 1.34 | 0.0089 |
| 6 | 157 | 1.05 |

So `c_5`, `c_6` are below the floor — the production `{4, 29}` at u⁵/u⁶ are
**cosmetic, not derived**. (Same structure as the Q_β ladder, where only
`c_2`, `c_3` are data-determined.)

### 3. Cross-anchor swing is small

`required c_4` at the proton pin (46.0319) vs the muon pin (46.0336) swings
**3.8e-5 (rel)** — small, because both mass-ratio anchors pin q_0 to nearly
the same value (the μ-p tension is large in σ but tiny in absolute q). The
target is a genuine real-q object `c_4 ≈ 46.03`, q-dependent.

### 4. Easy-class prune — no clean categorical hit

A small principled scan of 1–2 factor categorical objects
(`[n]_q!`, `[n]_q·[m]_q`, `tr_M(β_Bor)`-dressed products) finds **no clean
hit**; best `[7]_q·[6]_q` at 5.8% rel, `target/[7]_q = 6.037` (0.6% off) —
all ≫ the 0.011 floor. The target is not a simple categorical product,
consistent with the saturated Q_β `c_3` search (28 + 1281 candidates, all
NEGATIVE).

## Verdict (scope-limited, per AGENTS.md)

- (a) The production `{46,4,29}` is a **rounded-integer fit**; only `c_4`
  (= 46.03) is data-determined, and it is q-dependent, not the integer 46.
- (a) `c_4 = 46.03` is **not** a 1–2 factor categorical product (small scan
  NEGATIVE) — does not exclude a deeper Habiro-element source.
- The first-principles derivation of `c_4` is the **term-6 Habiro residue
  tail**, the same open Habiro-element problem as the Q_β `c_k` ladder.
  **Gated on the s5bb keystone.** A keystone closure that derives the Q_β
  `c_k` should derive this mass `c_4 = 46.03` too.

## Discipline

Exploratory probe. No production rewire, no fit added/removed, no registry
tier change, Δ_λ gate untouched. The production `habiro_ratio` stays as-is
pending the keystone; this audit only characterises its target honestly.

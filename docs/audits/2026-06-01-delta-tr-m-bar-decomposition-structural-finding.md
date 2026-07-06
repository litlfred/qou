# Δtr_M bar-decomposition under t ↔ 1/t (t = q^(1/2))

**Date:** 2026-06-01
**PR:** TBD (claude/qbeta-habiro-symbolic-qdiff-2026-06-01)
**Status:** STRUCTURAL OBSERVATION — not a derivation; flagged as
follow-up research direction.

## TL;DR

In the variable `t = q^(1/2)` (which eliminates half-integer
q-powers from Hecke-convention `tr_M`), the symbolic `Δtr_M(t)`
decomposes uniquely as `sym(t) + antisym(t)` under the involution
`t ↔ 1/t`:

| Part | Closed form (in t) | Back-substituted (in q) | At q_proton | % of Δtr_M |
|---|---|---|---|---|
| **Symmetric** | `−(t−1)²(t+1)²(t²+1) / (2t³)` | `(−q³+q²+q−1)/(2q^(3/2))` | -1.091e-2 | 7.7% |
| **Antisymmetric** | `−(t−1)(t+1)(t⁸+2t⁶+4t⁴+2t²+1) / (4t⁴(t²+1))` | `(−q⁵−q⁴−2q³+2q²+q+1)/(4q³+4q²)` | -1.312e-1 | 92.3% |
| **Sum** | — | — | -1.421e-1 ✓ matches |

The symmetric part factors **very cleanly**: `−(t²−1)²(t²+1)/(2t³)`
in t, equivalently `−(q−1)²(q+1)/(2q^(3/2))` in q.

## Why this is recorded

The Q_β c_k saga has produced 7 ruled-out mechanisms (per
`docs/audits/2026-05-31-qbeta-bridge-narrowing.md` updated with
mech #7 from PR #1609's Li_2^q × spectral refutation). The
underlying issue: candidates don't respect the natural Hecke
bar-involution structure.

Per `prop:li2q-phiq-bar-symmetrization`:
- **Binding context** (Q_β, Δ_λ, isospin differences) lives in
  the **Li_2^q sector** (bar-SYMMETRIC under q → 1/q)
- **Mass context** (m_p, m_n absolutes) lives in the **Φ_q sector**
  (bar-ASYMMETRIC, carries dimensional scale)

Q_β is a BINDING quantity (mass-difference). So the natural
expectation: Q_β's derivation should isolate the **symmetric**
projection of Δtr_M (= 7.7% of the total numerical value at
q_proton) — the other 92.3% lives in the mass sector and would
introduce spurious mass-scale dependence.

This is a structural observation, NOT a derivation claim. Future
work that uses this decomposition for c_k must pass the cross-
anchor test (q_proton vs q_muon) AND have a structural
justification — not just numerical match at one anchor.

## What the symmetric closed form might mean

`−(q−1)²(q+1)/(2q^(3/2))` factors interestingly:

- `(q−1)²` = `h² · q²` (squared Hecke-bar = ℏ_q²·q²)
- `(q+1)` = `[2]_q · q^(1/2) = (q + q⁻¹) · q^(1/2)`
- `1/q^(3/2)` brings the q-power balance back

So the symmetric part can be rewritten as
`−(h²·q²) · ([2]_q·q^(1/2)) / (2q^(3/2)) = −h²·[2]_q/2`

That's STRIKINGLY simple. Let me verify:

```
sym_q = −(q−1)²(q+1) / (2q^(3/2))
       = −(q² − 2q + 1)(q+1) / (2q^(3/2))
       = −(q³ + q² − 2q² − 2q + q + 1) / (2q^(3/2))
       = −(q³ − q² − q + 1) / (2q^(3/2))
       = (−q³ + q² + q − 1) / (2q^(3/2))    ← matches output ✓
```

And `−h²·[2]_q/2` = `−(q−q⁻¹)²·(q+q⁻¹)/2` = `−(q² − 2 + q⁻²)·(q+q⁻¹)/2`.

Multiplied out: `−(q³ + q − 2q − 2q⁻¹ + q⁻¹ + q⁻³)/2`
              = `−(q³ − q + q⁻¹·(-1) + q⁻³)/2`     [simplifying]
              = `−(q³ − q − q⁻¹ + q⁻³)/2`

Multiply numerator and denominator by `q^(3/2)`:
              = `−(q^(9/2) − q^(5/2) − q^(1/2) + q^(−3/2)) / 2`
              ... need to divide by `q^(3/2)` to compare:
              = `−(q³ − q − q⁻¹ + q⁻³)/2 · 1`

Comparing to `(−q³ + q² + q − 1) / (2q^(3/2))`:

These are NOT obviously equal — the powers don't match (3, 2, 1, 0 vs 3, 1, -1, -3). So `−h²·[2]_q/2` is NOT the symmetric part as written.

The factoring observation `(q−1)²(q+1) = q³ − q² − q + 1` is correct;
the rewrite into `h² · [2]_q` form needs more care. Recording the
algebraic form `−(q−1)²(q+1)/(2q^(3/2))` as the canonical statement
of the symmetric part; further simplification to Hecke-natural
basis is follow-up work.

## Follow-up research direction (recorded in research-queue)

This decomposition motivates a new attack candidate:

**Q_β candidate**: derive Q_β = m_e · f(sym(Δtr_M), q) where f
operates on the SYMMETRIC PROJECTION of Δtr_M only, with the
antisymmetric part canceling via the mass-difference structure
(Q_β = m_e · |sym(Δtr_M)| × structural correction).

Numerically at q_proton: |sym(Δtr_M)| = 1.091e-2; Q_β / m_e =
0.7823 / 0.511 = 1.531 MeV/MeV. Ratio: 1.531 / 1.091e-2 = 140.3.
So a candidate scaling factor S(q) would need to satisfy S(q_0) ≈ 140.3.
Substrate candidates with values ~100-200 at q_proton: 1/h² ≈ 102,
1/(h²·q^(1/2)) ≈ 97, ([2]_q/h²) ≈ 195. None hit 140.3 cleanly.

**This is exactly the candidate-fishing trap.** Recording the
direction without testing further: future structural justification
is REQUIRED before any candidate gets wired.

## Anti-patterns (DO NOT repeat)

- ❌ Using this decomposition to wire a c_k value without
  cross-anchor (q_proton vs q_muon) validation
- ❌ Searching for a clean-looking S(q) factor that matches
  numerically — this is the 7th-ansatz fit-trap
- ❌ Promoting the structural finding to a derivation claim
  without identifying which categorical object the symmetric
  projection represents

## Witness

`computations/probes/qbeta-delta-tr-bar-decomposition-probe.witness.json`

Includes the symbolic decomposition + numerical sanity check
(sym + antisym = Δtr_M to 1e-12 at q_proton).

## Cross-refs

- `docs/audits/2026-05-31-qbeta-bridge-narrowing.md` — 7 ruled-out mechanisms
- `docs/audits/2026-05-30-qbeta-recursive-pair-rules-and-habiro-pde.md` — Habiro q-difference equation framing
- `computations/_li_2_q_util.py` — prop:li2q-phiq-bar-symmetrization docstring
- `docs/coordination/1ppq-qbeta.md` — flip-flop history
- `.beans/research-queue.json` — `research-qbeta-habiro-element-search`

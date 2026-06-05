# GAP-A / Path B per-atom λ(K) — coordination ledger

> Sibling-axis ledger to [`1ppq-qbeta.md`](1ppq-qbeta.md). Tracks the
> Path B / per-atom λ(K) closure chain that closes [#1762](https://github.com/litlfred/qou/pull/1762)'s
> Option D from the mass / binding-energy side.

## Goal

Identify whether the per-atom Path B multiplier `λ(K)` in
`m(K) = m_e · Vol(K)/ℏ_q² · λ(K) + S(K)` is substrate-derivable, and if not,
which sub-leading `S(K)` form bridges the residual gap.

## Status — cont. 1 (2026-06-05)

**17 + 1 no-fit closures.** The Δ_λ-gate ansatz family is closed
(8 in the gate doc + #1860 Kashiwara × 5 + #1870 brane-tower × 5 = 18); the
GAP-A-4 §4 direction 3 (³He residual structural lead) closes negative
under cross-isotope extrapolation (#1883). The Phase-4 per-atom
amplitude `A(K)` remains substrate-derived to ≤ 2.5 %. The remaining
productive directions are #1876 §4-2 (additive `S(K)`) and §4-4
(per-knot `Vol(K)` convention re-examination).

| PR | Outcome | Net |
|---|---|---|
| [#1816](https://github.com/litlfred/qou/pull/1816) | merged | Option A diagnostic — light-series Vol(K) wired, RED gate confirmed |
| [#1841](https://github.com/litlfred/qou/pull/1841) | merged | Option B Bratteli induction REFUTED (3/3 sub-hypotheses) |
| [#1850](https://github.com/litlfred/qou/pull/1850) | merged | Markov trace stabilization axis REFUTED (z<1 obstruction + M1/M2) |
| [#1853](https://github.com/litlfred/qou/pull/1853) | merged | H₃→H₄ both axes refuted (consolidation) |
| [#1860](https://github.com/litlfred/qou/pull/1860) | merged | Option E Kashiwara Δ_λ — 5/5 candidates REFUTED |
| [#1822](https://github.com/litlfred/qou/pull/1822) | merged | qbeta rung-lifts (cross-axis tie) |
| [#1864](https://github.com/litlfred/qou/pull/1864) | merged | 3-paths-refuted roadmap consolidation (recommends "linking_weight_family_a is CODATA-implied near-match" framing) |
| [#1868](https://github.com/litlfred/qou/pull/1868) | merged | GAP-A-3 scope (brane-tower content channels) |
| [#1870](https://github.com/litlfred/qou/pull/1870) | merged | GAP-A-3 deuteron P_λ — 5/5 channels REFUTED |
| [#1872](https://github.com/litlfred/qou/pull/1872) | merged | GAP-A-4 Path B scope (L1/L2/L3 candidates) |
| [#1874](https://github.com/litlfred/qou/pull/1874) | merged | GAP-A-4 L1 light-series — L1a/b/c REFUTED (proton +2.89 % gap recovered) |
| [#1876](https://github.com/litlfred/qou/pull/1876) | merged | L1 retrospective (4 next-probe directions; #1882's ³He +0.70 % flagged) |
| [#1882](https://github.com/litlfred/qou/pull/1882) | merged | ³He L1b residual — `sqrt([3]_q/[2]_q)` +0.70 % filed as NUMEROLOGY |
| [#1883](https://github.com/litlfred/qou/pull/1883) | merged | Cross-isotope extrapolation REFUTED (>1000 % worst rel_err) → ³He numerology CONFIRMED |
| [#1886](https://github.com/litlfred/qou/pull/1886) | merged | T1 — additive `S(K)` sub-leading REFUTED under uniform-λ (100× swing across light series) |

## Cross-axis hub

The step-9 binding closure ledger
[`2026-06-05-step9-binding-closure.md`](2026-06-05-step9-binding-closure.md) (PR
[#1871](https://github.com/litlfred/qou/pull/1871), flag-bearer
`claude/confident-newton-R8lIx`) is the **adjacent-axis hub** for the
broader step-9 derivation gap. The two ledgers track related but distinct
questions:

| Ledger | Question | Axis |
|---|---|---|
| this (`gap-a-path-b-lambda.md`) | substrate-derivability of the per-atom `λ(K)` in Path B | per-atom mass multiplier |
| [`2026-06-05-step9-binding-closure.md`](2026-06-05-step9-binding-closure.md) | additive many-body binding series via SW-residue + q-difference | many-body binding closure |

The two intersect on: (a) the per-knot Vol(K) convention (T2 here ≡ C2 there), (b) the per-block-vs-global density gate (T3 here ≡ §4.B C1 there), (c) the bar-odd binding-difference observable (∼ L5 there; merged in #1871). My chain's negative results (`Δ_λ` Kashiwara, Markov stab, brane-tower content, L1 carrier-transplant) constrain their q-difference kernel `R(q,x)` derivation.

## Active sibling-axis coordination

- **[#1762](https://github.com/litlfred/qou/pull/1762)** (1ppQ roadmap) —
  parent. Roadmap-status comments posted at cont. 0 ([#1762-c.0](https://github.com/litlfred/qou/pull/1762#issuecomment-4626482823))
  and cont. 1 ([#1762-c.1](https://github.com/litlfred/qou/pull/1762#issuecomment-4632431195)).
- **[#1871](https://github.com/litlfred/qou/pull/1871)** (SU(2)/SO(3)
  per-block density) — same per-block-vs-global RED gate from the
  M=Vol×Density side. Coord posted; supports their "no production
  swap" decision.
- **[#1784](https://github.com/litlfred/qou/pull/1784)** (binding-link
  assignment heuristic) — Path C `atom→knot assignment` gate; same
  ³He atom is where #1883's numerology localised. Coord posted; their
  "Jones-via-Markov-derived link" is the cleanest productive next step.

## Discipline observations (from this chain)

1. **"Fix as numerology unless derivable" rule** (author, 2026-06-05) —
   a NEAR-MATCH (<5 %) with no categorical derivation is filed as
   coincidence pending derivation. Single-atom matches are
   numerology unless backed by cross-isotope structural rule.
2. **18 no-fit closures form a saturating chain** — no per-partition
   ansatz survives (single statistic, brane-tower content channel,
   induction, stabilization, Bratteli, Kashiwara crystal, etc.).
3. **Productive direction has shifted** from "derive per-partition
   Δ_λ" (closed) to "derive per-atom mass closure via Path B" (the
   `S(K)` sub-leading term + the `Vol(K)` convention question).

## Next concrete tasks on this ledger

| # | Task | Source |
|---|---|---|
| T1 | Probe #1876 §4 direction 2 — additive `S(K)` sub-leading form | [#1876](https://github.com/litlfred/qou/pull/1876) §4 |
| T2 | Probe #1876 §4 direction 4 — per-knot `Vol(K)` convention for compound atoms (cross-link with [#1871](https://github.com/litlfred/qou/pull/1871), [#1784](https://github.com/litlfred/qou/pull/1784)) | [#1876](https://github.com/litlfred/qou/pull/1876) §4 |
| T3 | Derive `λ(K)` from a Path B-specific formulation (NOT a Phase-4 transplant; per #1876 O2) | [#1876](https://github.com/litlfred/qou/pull/1876) O2 |

# Δ_λ co-Casimir ansatz — refutation formalized in Lean (2026-06-24)

**Branch:** `claude/vigilant-cannon-6pncqr` · **PR #2676**
**Status:** formalize-the-refutation. No new derivation; machine-checks an existing negative result. TIERED; nothing wired; `c_3`/Q_β/binding stay cal-anchored.

## Context

The per-isotope binding formula `B(K) = m_e · Σ_λ y_λ χ^λ Δ_λ` requires per-partition
`Δ_λ` values. Six closure ansätze have been refuted on the deuteron anchor (AGENTS.md
§"Precision goals" / "Δ_λ gate"): **Frobenius co-Casimir**, Demazure-fibre, LP-Plancherel,
LP-Frobenius, crystal-graph, augmented Markov. The standing gate rule —
**"do not propose a seventh fit-based ansatz"** — was enforced only by reviewer vigilance
(prose warnings in audit docs + AGENTS.md), not by any machine check.

This note records the first **machine-checked** member of that refutation set, per the
*formalize-the-refutation* discipline
([`compute-author.md §3.4`](../../.claude/skills/local/compute-author.md)): a refuted
ansatz becomes a sorry-free inequality so it cannot be silently re-proposed.

## What landed

[`QOU/BraidKnot/DeltaLambdaRefutation.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/DeltaLambdaRefutation.lean)
— three sorry-free `ℚ` lemmas, pinned to
[`rho-k-h3a-co-casimir.witness.json`](../../computations/rho-k-h3a-co-casimir.witness.json)
(50 dps, `allPassed: true`), 12-figure truncations (refutation margin ≈ 4.5×, so 12 figs
is far more than the inequality needs):

| lemma | statement | source field |
|---|---|---|
| `coCasimir_closureGap_eq` | `\|pred − target\| = closureGap` (ties the literals) | `closure_gap_LHS_minus_RHS = 4.49832…` |
| `coCasimir_refuted_deuteron` | `tol < \|pred − target\|` (gap ≈ 4.498 `m_e` units vs tol 1) | magnitude miss |
| `coCasimir_wrong_sign` | `0 < pred ∧ target < 0` (predicts `+0.145`, target `−4.353`) | wrong sign, irreparable by any `ρ > 0` |

The co-Casimir ansatz predicts a per-partition binding-density sum `+0.144959…` (`m_e`
units) where the empirical `−B_D/m_e` is `−4.353367…` — wrong sign, magnitude off ≈30×.

## Cross-references

- Conjecture this ansatz tried to close:
  [`conj:rho-prefactor-structural`](../../content/quantum-observable-universe/mass-theory/conj-rho-prefactor-structural.md)
  (GAP-A-4 — the structural `ρ` / `Δ_λ` rule).
- The six failed ansätze:
  [`2026-05-18-delta-lambda-gating-context.md`](2026-05-18-delta-lambda-gating-context.md) (Option B).
- Active **forward** three-lever Δ_λ work (this is the **backward** complement; no file overlap):
  [`2026-06-23-delta-lambda-three-lever-status.md`](2026-06-23-delta-lambda-three-lever-status.md)
  (#2612; beans `z2bn`/`w5tg`/`thb7`).

## Discipline

- Formalize-the-refutation per compute-author §3.4 — the witnessed disproof becomes a
  machine-checked `≠`, not a prose warning.
- No fit; nothing wired; no fourth calibration; the Δ_λ gate **remains open** (this neither
  closes nor reopens it — it hardens the "no 7th ansatz" rule).

## Follow-up

1. Promote to a content-block triple `lem:frobenius-cocasimir-refuted-deuteron` beside the
   GAP-A-4 conjecture (`.ts`/`.md`/`.lean`).
2. Add the remaining five refuted ansätze as `≠` lemmas as their clean witnessed numbers
   are surfaced (extend `DeltaLambdaRefutation.lean`).

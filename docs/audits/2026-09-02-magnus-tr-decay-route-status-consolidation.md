# tr-decay (qou-o6ov): route-status consolidation — every structural shortcut is dead; the core is one cancellation theorem

**Date:** 2026-09-02
**Directive (owner):** go on next after review of main.
**Scope:** scope-(a) consolidation + one new negative (conjugation symmetry); no MeV, no fit.
**Probe (new):** [`magnus_conjugation_symmetry_probe.py`](../../computations/deltalambda/magnus_conjugation_symmetry_probe.py)

## Purpose

`qou-o6ov` (prove `tr(ρ_λ Ω₂)` decays with `b(λ)`, to make the row-truncation rigorous) has
been attacked from ~10 directions this arc. This note consolidates **what is dead and why**, so
the next agent does not re-walk it, and states the one surviving open core. It is a TRAP-type
artifact: the measured negatives are the value.

## The established structure (all on main, verified)

- **Reduction to a single window** (#6311): the decay is per-window-local, `Ω₂ → ⁅A_a,A_{a+1}⁆`.
  Lean sorry-free (`omega2_reduces_to_adjacent`).
- **Localization to `‖⁅ρ,A_a⁆‖_F`** (#6339): Cauchy–Schwarz + Leibniz telescoping (Lean).
- **Endpoint is an exact zero** (#6387): the sign rep `(1ⁿ)` (b=max, dim 1) gives `tr=0`
  by commutativity. Lean sorry-free (`trace_rho_commutatorSum_eq_zero_of_commute`).
- **Alexander sector is `b=1`** (#6392): the peak is the reduced-Burau reflection rep
  `(n−1,1)`; the sign endpoint is information-free (writhe-only). The decay runs *away* from
  the Burau/Alexander sector.
- **Concentration:** `|c_λ| = y_λ|tr|` sits 86–92 % on `b=1` (A=3→4).

## Dead routes (each measured, not assumed)

| # | route | verdict | evidence |
|---|---|---|---|
| 1 | naive `\|tr\| ≤ q^L·dim` | **dead** | `Σ y·dim` tail plateaus at 0.5 (#6183/#6265) |
| 2 | operator-norm / submultiplicative telescoping | **dead** | local commutator `‖⁅σ_g,A_a⁆‖_F = Θ(√dim)` (plateau ≈1.5 to dim 7700), so the bound is only `O(dim)` (#6349) |
| 3 | support / active-tableau counting | **dead** | same as #2 — the local commutator support is `Θ(dim)`, not `o(dim)`; the decay is *not* a support collapse |
| 4 | Kerov–Olshanski shifted-symmetric bounded-degree | **dead** | `tr/dim` is not a low-degree polynomial in content power-sums (max rel resid 0.94, bean note 2026-08-30) |
| 5 | classical cluster / Penrose tree-graph (Procacci–Yuhjtman, Rebenko) | **template only** | commutative convergence-radius result; says nothing about cumulant sign (#6362) |
| 6 | non-commutative colored-Jones zeta (Garoufalidis–Le) | **right structure, wrong coordinates** | color-`N`/knot grading, not Hecke-irrep/shape-`b`; no plug-in bound (#6372) |
| 7 | **conjugation symmetry of the b-profile** | **refuted (new, this note)** | `tr(ρ_{λ'} Ω₂)/tr(ρ_λ Ω₂)` is messy, not `±1`/q-power (peak↔near-endpoint R=−0.0033 at A=3); the germ log-derivative breaks `q→−q⁻¹` |

## The one surviving open core

**Trace-orthogonality** (#6354): the CS slack `‖⁅ρ,A_a⁆‖_F·‖A_{a+1}‖_F / |t|` **grows** with
`b` (from ~3 to 10²–10³), so `|t|` decays faster than the commutator norm — i.e.
```
⟨ ⁅ρ_λ,A_a⁆ , A_{a+1} ⟩_Frobenius / dim_λ → 0   as b(λ) → ∞,
```
the projection of the word-commutator onto the fixed germ direction vanishes. This is a
genuine **sign/phase cancellation** (a matrix-element / overlap decay), and **all the
norm-, support-, and symmetry-based shortcuts above provably cannot reach it.** It is the
hard, multi-session theorem — the non-commutative cumulant object of #6372 (in the wrong
coordinates) is the nearest known machinery, and re-grading it by Hecke irrep is the open
research bridge.

## Practical consequence (what works today, un-rigorously)

Because `b=1` (reduced Burau) carries 86–92 % and is exactly computable, the row-truncation is
*effective in practice* (keep low `b`, error concentrated in a fast-decaying tail). What
remains open is upgrading that from a measured concentration to a **proved** tail bound — which
is blocked on the trace-orthogonality cancellation above, not on any of routes 1–7.

## Bottom line

Seven structural shortcuts to the tr-decay rate are now measured-dead or refuted (route 7 new
here). The decay is a genuine trace-level sign cancellation `⟨⁅ρ_λ,A_a⁆,A_{a+1}⟩/dim → 0`, with
a proved exact-zero endpoint (sign rep) and a Burau/Alexander peak at `b=1`. The rate itself is
the open theorem; the honest next step is the non-commutative-cumulant re-grading bridge
(#6372), a research program, not a lemma.

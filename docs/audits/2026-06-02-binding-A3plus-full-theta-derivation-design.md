# A≥3 absolute binding via full-order θ_λ — derivation campaign

**Date:** 2026-06-02
**Branch:** `claude/binding-A3plus-full-theta-derivation-2026-06-02`
**Advances toward (does NOT yet close):** A≥3-absolute Δ_λ gate (cheat-sheet line 411). The verdict doc records the current residuals (³He +17.4 %, T +39 %, ⁴He +2.7 % with cosh-growth, D scalar-path); closure requires the remaining levers listed at the end of this doc.

## What is open and what is closed

From [`docs/canonical-derivation-cheat-sheet.md`](../canonical-derivation-cheat-sheet.md) §9.3:

| Quantity | Status |
|---|---|
| **Deuteron absolute binding** | 🟢 **derived twice** — `m_e · Vol(𝓑₃) · Δtr` (+0.19%) and `μ₀ · ℏ_q · J_q²(j=1)` (−9%) |
| Mirror-pair **differences** (³H/³He, A=3) | 🟡 partial — signed structure real; best structural 2.52 %; published 0.11 % is a fitted `(1+q)/2` (CAL-4) near-match |
| **A≥3 absolute** binding (T, ³He, ⁴He) | 🔴 **the open gate** — `j=n/2` collapse of θ_λ saturates; needs **full per-rep θ_λ magnitude** (not the linear truncation) |

The deuteron is done. The **only** open gate at A≥3 is recovering the
`exp(Vol)` from the linearized `Δtr` per block — i.e. carrying the
per-rep q-Reeb phase `θ_λ` at **full (non-linearized) order** through
the GB-filtration / jet tower. Closing this single object closes
**both** the A≥3-absolute binding AND the mirror-difference magnitude
**with one non-fitted object** (line 414).

## The lever

Per cheat-sheet line 410, two independent deuteron derivations:

1. **Binding-endomorphism**: `B = m_e · Vol(𝓑₃) · Δtr`
2. **q-Hamiltonian rotational**: `B = μ₀ · ℏ_q · J_q²(j=n/2)`

Both substrate-derived; both saturate at A≥3 because the per-rep
phase decomposition collapses to a single channel (the highest-
weight `j=n/2` mode).  The "binding endomorphism analogy" audit
[`2026-05-28-binding-endomorphism-analogy.md`](2026-05-28-binding-endomorphism-analogy.md)
§"A≥3 derivation campaign" + [`2026-05-18-delta-lambda-gating-context.md`](2026-05-18-delta-lambda-gating-context.md)
trace the root cause: linear-truncation diagnosis (§259) +
volume-difference triple refutation at real q₀ (§273) +
complex-q / q-Reeb rotation as the extensive observable (§283).

The infrastructure for the lever has landed via sibling commits:
- `d59bcb79de` — θ_λ per-λ carry (full vector emitted, not collapsed)
- `5e388f598b` — full-order θ_λ probe (y_λ wrong-measure diagnosis)
- `d7c56c17e1` — binding measure search (`|content_λ|` best candidate
  for A-growth ratio match)
- `ba7af156cb` — per-block θ_λ carry on D/T/³He/⁴He (absolute open;
  signed difference structural)

[`binding-reeb-phase-decomposition.witness.json`](../../computations/binding-reeb-phase-decomposition.witness.json)
now carries the per-λ vector (`by_partition`):

```json
{
  "partition": [3, 2, 1], "dim": 16,
  "chi_free": "7.625…",   "chi_atom": "-1.972…",
  "r_free":   "0.476…",   "r_atom":   "-0.123…",
  "channel_free": "rotation", "channel_atom": "rotation",
  "theta_free_rad": "1.074…",
  "theta_atom_rad": "1.694…",
  "delta_theta_rad": "0.620…",
  "channel_flip": false
}
```

per partition, per atom (D, T, ³He, ⁴He).  The **growth channels**
(|r| > 1) are exactly where the highest-weight j=n/2 truncation
collapses extensive structure.  Full-order θ_λ on the growth
channels = arccosh(|r|) per cell, NOT just arccos(Re(r)).

## What this PR derives

For each atom K ∈ {T, ³He, ⁴He}:

1. **Load** per-λ θ_λ vector from
   `binding-reeb-phase-decomposition.witness.json::data.per_atom[K].by_partition`.
2. **Compute** full-order θ_λ — combining the rotation (arccos)
   AND growth (arccosh) contributions per partition.  No
   linearization; no truncation to j=n/2.
3. **Assemble** the binding via the canonical chain:
   `B(K) = m_e · F(θ_λ, K)` where `F` is the q-hyperbolic
   functor implied by cheat-sheet §9.2 ("density × volume").
   No new ansätze; no fits.
4. **Compare** to AME experimental.

If the full-order θ_λ closes A≥3 to within the L2-100× per-isotope
goals (see `docs/precision-goals.md`), **the Δ_λ gate is closed
across all A** via a single non-fitted object.

## Discipline

- **NOT a fit** — `F` is forced by the canonical chain (cheat sheet §9.2).
- **NOT a 7th ansatz** — `θ_λ` is derived at step 2 (Yekutieli
  boundary holonomy); this PR just stops the information loss
  that collapses θ_λ at the scalar-trace step.
- **NOT a new measure** — uses the per-block structure that was
  already there but discarded.

## Microcommit plan

1. **commit 1**: this design doc + scaffold script that loads the
   per-λ θ_λ data + computes full-order magnitude per partition.
2. **commit 2**: A≥3 first cut — `B(T) = m_e · Σ_λ y_λ · χ^λ ·
   full_θ_λ(T)` (matches deuteron baseline; check the form).
3. **commit 3**: A≥3 with growth-channel arccosh added (the
   extensive piece that's missing in linear Δtr).
4. **commit 4**: cross-validate on D (must reproduce the +0.19%
   match from the binding-endomorphism path).
5. **commit 5**: report per-atom verdict.

## Coordination

- **Parent: cheat sheet §9.3** + binding-endomorphism audit.
- **Adjacent: PR #1714** (KL scaffold) — *parked*; not on the
  critical path for this work but useful infrastructure for
  CLAUDE.md §7b shortcuts later.
- **Adjacent: PR #1719** (PROBE 4 closure) — *closed without
  merge*; refutation reference only.

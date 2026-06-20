# Substrate Fermi statistics + Q_β coordination — 2026-06-02

Branch: `claude/substrate-fermi-and-qbeta-coord-2026-06-01`

Per author 2026-06-02 "2 3" after PR #1671 merged (the campaign chain
canonical reference). Two items:

## Item I — Substrate Fermi statistics (open work from PR #1645)

PR #1654 Item B reframing identified the open multi-session derivation:
substrate-level implementation of QCD color-singlet (Fermi statistics
→ sign rep of S_3 on 3 color labels) + categorical Wedderburn
projection of EM coupling.

This branch's contribution: **first Lean scaffold** for the Fermi-
statistics implementation. Specifically:
  - `class ColorAntisymmetric` axiomatizing antisymmetry under S_3 action
  - Connection to `EmSignBlockCorrection` via Wedderburn projection
  - Multi-session work; this branch lands scaffolding only

## Item II — Q_β coordination push

Sibling work is heavily active on Q_β Habiro:
  - PR #1647 + 12 q-Laplacian commits
  - Mass-table sweep across 12 atoms
  - Φ_8 multiplicity scaling A−1 in mirror-pair Habiro
  - Wenzl tower FALSIFIED
  - ¹⁰C Habiro + mirror-pair refinements
  - 10-pair Φ_8 is PROTON-CONDITIONAL

PR #1671 added a light cross-reference audit
(`docs/audits/2026-06-01-qbeta-signblock-cross-reference.md`).
This branch's contribution: **deeper coordination probe** testing
whether the sign-channel × dim H_n pattern from m_p (PR #1645) and
Q_β c_3 (PR #1654 Item 3) generalizes across the sibling 12-atom
mass-table.

## Sibling coordination

Active siblings (last 24h):
  - `claude/inter-nucleon-linked-channel` — merged PR #1678 (inter-nucleon Hopf link)
  - `claude/research-precision-residual-probes-2026-06-01` — open
  - `claude/li2q-reality-gate-2026-06-01` — qLambert_single_term Lean
  - Multiple witness-refresh branches

This branch will:
  - **complement** Q_β work (NOT compete with Habiro identification)
  - Open a new dimension: sign-channel scaling across atoms

## Status

| Item | Tier | Status |
|---|---|---|
| I. Substrate Fermi statistics scaffold | DONE | `QOU.Substrate.ColorAntisymmetric` scaffolded — `signPlancherelWeight`, `FermiColorSinglet` class stub, `fermi_implies_signWeight_eq_one_sixth` conditional theorem |
| II. Q_β sign-channel × dim H_n cross-atom check | DONE | Coordination finding — dim H_(3A) (factorial) vs Φ_8 A-1 (linear) are DIFFERENT scalings; not competing |

## Findings summary

**Item I (Fermi scaffold):** First Lean module landing for the
substrate-level QCD color-singlet implementation. Includes:
  - `signPlancherelWeight (n : ℕ)` def + proof at n=3 returns 1/6
    (matches `ProtonMassEMSignBlock.plancherelSignH3`)
  - `class FermiColorSinglet` placeholder for the substrate
    categorification (NO INSTANCE — the class IS the conjecture per
    AGENTS.md §3b-cond)
  - `fermi_implies_signWeight_eq_one_sixth` conditional theorem
  - Open work documented in module docstring for future agents:
    (1) representation-theoretic 1-dim sign rep via Mathlib
    (2) S_3 transposition action `(-1)` formalization
    (3) categorical Wedderburn projection of EM coupling

**Item II (cross-atom Q_β):** Clear structural discrimination:
  - PR #1654 finding: c_3 = -2 = dim H_2 · σ_1(sign)|_{q=1}
    (H_2-Hopf-specific, 2-strand)
  - Sibling Φ_8 multiplicity A-1 scaling (mirror-pair Habiro, 3A-strand)
  - dim H_(3A) = (3A)! is FACTORIAL — grows from 720 (A=2) to 3.7e41 (A=12)
  - A-1 = LINEAR — grows from 1 to 11

These are vastly different scalings; the campaigns address different
observables. The dim H_n × σ_1(sign) pattern from PR #1654 is
**Hopf-link-specific** and does NOT generalize to the mass-table sweep.
The Φ_8 A-1 scaling is a separate categorical mechanism (Habiro
coefficient at higher A) and does NOT contradict PR #1654.

**Net coordination outcome:** the m_p sign-block campaign and the Q_β
Habiro campaign address **different categorical objects**:
  - m_p sign-block: Plancherel-weighted EM coupling at H_3 sign rep
  - Q_β Habiro: per-rung coefficient identification across mass-table

Both are legitimate; they don't compete and shouldn't be expected to
share a unified scaling.

## Cross-references

- merged [PR #1645](https://github.com/litlfred/qou/pull/1645) (sign-block hypothesis)
- merged [PR #1654](https://github.com/litlfred/qou/pull/1654) (template m_p-specific; Q_β partial)
- merged [PR #1671](https://github.com/litlfred/qou/pull/1671) (canonical reference)
- canonical reference: [`docs/audits/2026-06-01-sign-block-plancherel-campaign-canonical-reference.md`](../audits/2026-06-01-sign-block-plancherel-campaign-canonical-reference.md)
- Q_β cross-ref audit: [`docs/audits/2026-06-01-qbeta-signblock-cross-reference.md`](../audits/2026-06-01-qbeta-signblock-cross-reference.md)

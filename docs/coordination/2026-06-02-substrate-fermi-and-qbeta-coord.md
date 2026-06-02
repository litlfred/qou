# Substrate Fermi statistics + Q_β coordination — 2026-06-01

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
| I. Substrate Fermi statistics scaffold | TBD | pending |
| II. Q_β sign-channel × dim H_n cross-atom check | TBD | pending |

## Cross-references

- merged [PR #1645](https://github.com/litlfred/qou/pull/1645) (sign-block hypothesis)
- merged [PR #1654](https://github.com/litlfred/qou/pull/1654) (template m_p-specific; Q_β partial)
- merged [PR #1671](https://github.com/litlfred/qou/pull/1671) (canonical reference)
- canonical reference: [`docs/audits/2026-06-01-sign-block-plancherel-campaign-canonical-reference.md`](../audits/2026-06-01-sign-block-plancherel-campaign-canonical-reference.md)
- Q_β cross-ref audit: [`docs/audits/2026-06-01-qbeta-signblock-cross-reference.md`](../audits/2026-06-01-qbeta-signblock-cross-reference.md)

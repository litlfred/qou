# Sign-block / Plancherel template expansion — 2026-06-01

Branch: `claude/sign-block-template-expansion-2026-06-01`

Per author 2026-06-01 "1 2 3 4" — apply PR #1645's sign-block /
Plancherel structural template (P_λ = d²_λ/dim H_n) across all 4
remaining items:

## Items in this branch

### Item 1 — Δ_λ closure for binding energies (Option E)

Targets: d, T, ³He, ⁴He binding energies. Apply per-Wedderburn-block ×
Plancherel-weight to the binding-energy formula in the same spirit as
the m_p sign-block hypothesis.

Existing queue entries (already covering different angles):
- `research-one-plus-q-over-two-derivation`
- `research-multi-nucleon-interface-operator`
- `research-atom-to-knot-rule-A5plus`

### Item 2 — m_n / Δ_pn structural rewrite

PR #1645 confirmed X(q) = ℏ_q²·h_q·[2]_q refinement is NULL. The
formula needs a fresh categorical derivation, not refinement. The
flavor-split happens via Hecke σ_1 on a 2-strand sub-braid of H_n.
Apply the Plancherel-channel pattern: the σ_1 eigendecomposition is
(symmetric, antisymmetric) = ([2]_q, -1) eigenspaces. The flavor-split
should live at the SYMMETRIC channel (trivial rep of H_2).

### Item 3 — Sign-block template applied to Q_β + m_e atomic

Sibling work (PR #1647 merged + recent 12 commits) heavily covers Q_β
Habiro identification. Complement (not compete) by checking if the
Wedderburn-block × Plancherel weight pattern from PR #1645 ALSO closes
the Q_β c_3 = -2 finding at a 1-dim block of H_2 or H_3.

### Item 4 — Lean formalization deepening

Extend `ProtonMassEMSignBlock.lean` with:
- Lemma: Σ_λ (d²_λ/dim H_n) = 1 (Plancherel sum identity)
- Lemma: P_λ = 1/dim H_n at any 1-dim rep of H_n
- Connect to the Wedderburn-decomposition theorems available in
  Mathlib (if any)

## Sibling coordination

Recent sibling activity (last 24h):
- PR #1647 + 12 q-Laplacian/spectral-tower commits — overlap with Item 3
  (Q_β) potential; complement-only approach
- PR #1648 Lean import fix — orthogonal to ProtonMassEMSignBlock
- ⁷Li/⁷Be mirror + Q_β Habiro mass-table sweep (12 atoms) — orthogonal
  to Items 1, 2, 4

**Plan:** Items 4 → 2 → 3 → 1 in order (Lean fastest, m_n direct
continuation, Q_β light-touch coordination, Option E speculative).

## Status

| Item | Tier | Status |
|---|---|---|
| 1. Δ_λ Option E binding energies | TBD | pending (deferred) |
| 2. m_n / Δ_pn Plancherel-channel rewrite | TBD | pending |
| 3. Q_β template cross-application | TBD | pending (light coord) |
| 4. Lean deepening | TBD | pending (first) |

## Cross-references

- merged [PR #1581](https://github.com/litlfred/qou/pull/1581) (closed-route roundup)
- merged [PR #1617](https://github.com/litlfred/qou/pull/1617) (alt-geometries confirmed dim H_3 = 6)
- merged [PR #1629](https://github.com/litlfred/qou/pull/1629) (h⁴-residual PSLQ NULL)
- merged [PR #1645](https://github.com/litlfred/qou/pull/1645) (sign-block hypothesis + CODATA-floor finding)
- `QOU.Substrate.ProtonMassEMSignBlock` Lean class

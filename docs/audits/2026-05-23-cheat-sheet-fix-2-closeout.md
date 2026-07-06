# Cheat-sheet §5 #2 close-out — `mass_from_tower` API surface built

> **Status (2026-05-23).** Cheat-sheet §5 Migration Backlog #2
> ("SUPERSEDED `mass_endomorphism.py` migration") is now CLOSED.
> The supersession is content-block-level (`prop:mass-endomorphism-
> tower` → `prop:mass-tower-operator-valued`); the underlying
> Python computation `mass_from_tower` is the canonical formula
> and stays. This audit documents the API-surface build that lets
> downstream consumers import via the canonical name without
> changing the computation.

## Scope refinement (audit-trail)

The original cheat-sheet §5 #2 row claimed "20 importers off
SUPERSEDED `mass_endomorphism.py` to migrate to the new
`mass_tower_operator_valued` API." Two scope-refinement audits
have narrowed this:

| Audit | Refinement |
|---|---|
| [`docs/audits/2026-05-23-mass-endomorphism-migration-scope.md`](2026-05-23-mass-endomorphism-migration-scope.md) (PR #960) | 15 of 20 importers are utility-only (`Phi_q`, `q0`, `z_mark`, `w_*`, `proton_cross`, `neutron_cross`, etc.). They consume substrate helpers from `mass_endomorphism.py` which is NOT module-deprecated. The 4 "substantive" candidates: `m_p_m_e_li2q.py`, `mass_at_3A_proper.py`, `pn_alpha_lp_dual.py`, `probe_t2_t3_proton_neutron_a1.py`. |
| **This audit** | Strict re-count: only **2 scripts × 2 calls** = 4 sites actually call `mass_from_tower(`. `m_p_m_e_li2q.py` defines its own LOCAL `mass_from_tower_F` wrapper (uses `Phi_q` + `additive_wedderburn_volumes` utilities). `probe_t2_t3_proton_neutron_a1.py` calls `additive_wedderburn_volumes` only (a utility, not the deprecated API). |

**Final scope**: 2 substantive callers, 4 call sites — `mass_at_3A_proper.py:619-620` and `pn_alpha_lp_dual.py:183-184`.

## What this PR ships

### A. API surface in `mass_tower_operator_valued.py`

Added a re-export block at the canonical block-name location:

```python
# ── Canonical API surface for downstream consumers ──────────────
from mass_endomorphism import (
    mass_from_tower,
    additive_wedderburn_volumes,
)

__all__ = [
    "load_A_per_pair",
    "operator_trace_rhs",
    "mass_from_tower",
    "additive_wedderburn_volumes",
]
```

Re-export verified to be the **identical function object** (`new_mft is orig_mft → True`). No computation change; only the canonical import path is the operator-valued block.

### B. Caller migration

| Caller | Before | After |
|---|---|---|
| `mass_at_3A_proper.py:604` | `from mass_endomorphism import mass_from_tower` | `from mass_tower_operator_valued import mass_from_tower` |
| `pn_alpha_lp_dual.py:61` | `from mass_endomorphism import mass_from_tower, HA, z_mark` | utility imports stay on `mass_endomorphism`; `mass_from_tower` moves to `mass_tower_operator_valued` |

Each migrated import carries a brief comment explaining the equivalence ("Both expressions are equivalent at H_{3A}").

## Why this is canonical (not a fit)

The two block-names refer to the same Markov-trace mass formula at the H_{3A} layer:

- `prop:mass-endomorphism-tower` (SUPERSEDED): the Φ_q tower form
  `𝔪 = |Π V̂| + Σ Φ_q(|V̂_i|) + Σ_{i<j} z² Φ_q(|V̂_i V̂_j|)`
- `prop:mass-tower-operator-valued` (canonical): the operator-valued form
  `χ^λ(β) = Σ_{(μ,ν)} Tr(A^λ_{μν}(I) · (ρ_μ(β_p) ⊗ ρ_ν(β_n)))`

These are EQUIVALENT expressions, verified to machine-ε in the per-λ A-operator extraction witnesses at H_6 (deuteron), H_9 (tritium / ³He), and H_12 (⁴He — via PR #944's Phase-1 8-λ low-dim subset).

The Python function `mass_from_tower` IS the computational implementation of both expressions (the same arithmetic produces both, since both reduce to the same Markov trace at q_0). Re-export is the right move; rewriting would be busywork that preserves identical numerics.

## §5 Migration Backlog status after this PR

| # | Item | Status |
|---|---|---|
| 1 | LAMBDA truth-in-naming | ✅ closed (#888 + #895) |
| 2 | SUPERSEDED `mass_endomorphism.py` migration | ✅ **CLOSED** (this PR) |
| 3 | Rust LR adapter wiring | ✅ closed (#901 + #895 + #915 + #946) |
| 4 | Closed-form `tr_M(𝓑_K)` refactor | ✅ closed for `binding_canonical` (#921); per-partition Rust handles the other 3 |
| 5 | Reeb-flow / Garside compute verification | ✅ closed (#935) |

**All 5 cheat-sheet §5 items closed.**

## Test plan

- [x] AST parse: `mass_tower_operator_valued.py` + 2 migrated callers
- [x] Re-export identity test: `mass_tower_operator_valued.mass_from_tower is mass_endomorphism.mass_from_tower` → True
- [x] Sample call: `mass_from_tower([{'full': 0.989, 'inter': 0.0}])` returns the same `(desc, single, cross, total)` tuple via both import paths

## Files

- `computations/mass_tower_operator_valued.py` (+22 lines, canonical API surface)
- `computations/mass_at_3A_proper.py` (line 604: import path migration + comment)
- `computations/pn_alpha_lp_dual.py` (line 61: same)
- `docs/audits/2026-05-23-cheat-sheet-fix-2-closeout.md` (this audit)

## Cross-references

- [`docs/canonical-derivation-cheat-sheet.md §5 #2`](../canonical-derivation-cheat-sheet.md) — the row this PR closes
- [`docs/audits/2026-05-23-mass-endomorphism-migration-scope.md`](2026-05-23-mass-endomorphism-migration-scope.md) (PR #960) — scope-correction parent
- [PR #944](https://github.com/litlfred/qou/pull/944) — H_12 Phase-1 A-operator extract that makes the two expressions verifiably equivalent up to A=4
- `mass_endomorphism.mass_from_tower:114` — the canonical Φ_q tower implementation (unchanged)
- `mass_tower_operator_valued.operator_trace_rhs:102` — the per-λ operator-valued verifier (unchanged)

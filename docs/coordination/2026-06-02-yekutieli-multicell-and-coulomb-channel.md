# α_em multi-cell Yekutieli + substrate Coulomb channel — 2026-06-02

Branch: `claude/yekutieli-multicell-and-coulomb-channel-2026-06-02`

Per author 2026-06-02: revisit deriving α_em (the fine-structure
constant) from the canonical chain `categorical action → non-abelian
Stokes → Wedderburn`, via two specific routes the author flagged as
"I thought we did this":

  1. **Multi-cell summed Yekutieli** — non-abelian Stokes integral
     SUMMED over the 8-ideal-octahedron tessellation (prior probes
     used individual torus knots or per-cell, never the explicit sum)
  2. **Substrate Coulomb channel** — the sinh (Coulomb) channel of
     `prop:cosh-sinh-q-bridge` projected through Wedderburn

## Target structure (the genuinely-open pieces)

```
α_em⁻¹ = q·[9]_q·[10]_q   +  2/(3π)        +  [2]_q/(8π)·(1−h²α)  + O(α³)
         ↑ tree (Coulomb-     ↑ shift          ↑ 2-loop self-energy
           channel sinh)        (4.3 ppm)        (0.31 ppb residual)
       = 136.823            = +0.212207      = +0.000584
```

- **Tree term** `q·[9]_q·[10]_q` = 136.823 — ALREADY a Coulomb-channel
  (sinh = `[n]_q`) form per `prop:cosh-sinh-q-bridge`. This part is
  the existing `prop:em-coupling-bring-zero-mode`.
- **Shift** `2/(3π)` — believed to be Bring-surface Hodge / cohomology
  data (audit `em-coupling-bring-zero-mode.md`). The "3" candidate:
  N_cusps = 3 (Borromean is a 3-component link).
- **Self-energy** `[2]_q/(8π)·(1−h²α)` — the RT-2-loop EMPIRICAL target
  (PRs #1463/#1487/#1527/#1538/#1549). The "8" candidate: 8 ideal
  octahedra in the 𝓑_3 tessellation.

## Prior art (refuted / null)

| Probe | Verdict |
|---|---|
| `alpha_em_yekutieli_h2_extraction.py` (torus-knot product) | REFUTED — `q·tr_M(T(2,9))·tr_M(T(3,5))` = 0.8, not 137 |
| PR #1466 H_3 matter-insertion + Wedderburn | REFUTED −445% |
| PR #1471 Bring-surface integration | REFUTED −67% |
| sibling `yekutieli-A q-Lambert per-cell` | NULL |

These tried INDIVIDUAL cells / torus knots. The SUMMED multi-cell
form + the Coulomb-channel route are the two not-yet-cleanly-tested
variants.

## Status

| Item | Tier | Status |
|---|---|---|
| 1. Multi-cell summed Yekutieli (α_em shift) | TBD | pending |
| 2. Substrate Coulomb channel (α_em) | TBD | pending |

## Anti-pattern guards (per scaffolding audit 2026-06-01)

- ❌ NO fitted formula matching 2/(3π) or the self-energy numerically
  without a structural mechanism (8th-ansatz trap)
- ❌ Do NOT assume the 8 octahedra contribute equally — Borel descent
  may group them into unequal orbits
- ✓ DO report derive-or-refute honestly with a pre-stated failure sig

## Cross-references

- merged PR #1442 (m_K/m_π Bring-zero-mode closure — Coulomb-channel template)
- merged PR #1581 (m_p (α_em/π)/dim H_3)
- `prop:em-coupling-bring-zero-mode`, `prop:cosh-sinh-q-bridge`
- audit `2026-06-01-yekutieli-mp-substrate-derivation-scaffolding.md`
- `alpha_em_yekutieli_h2_extraction.py` (prior torus-knot refutation)

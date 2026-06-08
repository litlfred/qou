# QA proof-statement-integrity drain — fluid-dynamics non-NS slice

Branch: `claude/qa-backlog-proof-fluid-nonns-2026-06-08`
Pattern: merged PR #1984 (one slice = one PR).

## Blocks (all `proof-statement-integrity` = fail/critical, `True`-placeholder)

| Block | Mismatch | Plan |
|-------|----------|------|
| `discrete-vortex-spectrum` | `: True := trivial`, does not state q-Laplacian spectrum | encode eigenvalue spectrum claim as a context-class theorem |
| `core-levi-form` | `: True := trivial` (5 class hyps), no aspect-ratio/cond/5-equiv claim | encode condition-number = aspect-ratio² + 5-way equivalence |
| `helicity-conservation` | `: True := trivial`, no helicity-conservation claim | encode dH_q/dt = 0 + CWF decomposition |
| `kelvin-dispersion-derivation` | `: True := trivial`, no dispersion result | encode Δ_q(z^k) = -[k]_q² z^k eigenvalue + dispersion |
| `acoustic-horizon-conditions` | `: True := trivial`, no horizon claim | encode |v|=c_s horizon + transonic/non-degen/energy conditions |

NS blocks (ns-*/leray/q-bkm) deferred to sibling `serene-albattani`.

## Method
- Replace `True` tautology with abstract `class ...Context` bundling load-bearing
  claims as fields; theorems project the fields (the proven r-matrix/figure-eight pattern).
- Verify each via `QOU/_Scratch/<Name>.lean` harness + `lake build QOU._Scratch.<Name>`
  (content-block `.lean` not in QOU Lake graph). Remove `_Scratch` before commit.
- Re-rate via `qa-agent-write.ts --score`: integrity fail→pass + proof-rater-*.

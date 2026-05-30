# α_EM 1ppQ closure — coordination ledger

**Created:** 2026-05-30
**Owner branch:** `claude/alpha-em-yekutieli-h2-2026-05-30` → **PR #1444**
**Goal:** push the framework's FSC α_EM derivation toward CODATA experimental
precision (0.15 ppb); identify what the canonical α_EM categorical object
*is* and whether higher-order corrections close the residual.

## Headline result on PR #1444 (3 derive-or-refute probes)

| Layer | α⁻¹ | residual |
|---|---|---|
| Tree `q·[9]_q·[10]_q` (bare) | 136.8232 | −1553 ppm |
| **+Bring zero-mode shift `2/(3π)` at g=4** | **137.03543** | **−4.18 ppm** |
| +tentative `α/(4π)` (CODATA comparator) | 137.03601 | +57 ppb |

- **Yekutieli h² route refuted** — T(2,9) single-generator (CBH `[σ₁,σ₁]=0` trivial), T(3,5) closed-form Hecke trace exact at all orders (cube-root-of-unity on (2,1)).
- **Habiro / full-Jones refuted as alternative tree** — `[n]_q` is the q-quantum-DIMENSION, not the full Jones polynomial (off by 10⁶ ppm).
- **Bring zero-mode shift** (already in `prop:em-coupling-bring-zero-mode`) closes the tree 4 orders of magnitude. I had missed it earlier; corrected.

## Scope map

| PR | Branch | Status | Relationship |
|----|--------|--------|--------------|
| **#1444** (mine) | `alpha-em-yekutieli-h2-2026-05-30` | open | — |
| **#1442** | `meson-em-residual-alpha-em-2026-05-29` | **just merged** | **direct topical overlap (meson EM closure to 0.056 ppm)** — corrects my "α_EM blocks meson" framing |
| **#1443** | `author-hecke-branching-trace-decomp-2026-05-29` | open | topical: operator-valued LR branching parent of the per-rep `[n]_q` identification I rely on; **intent posted** |
| **#1431** | `a567-sdp-knot-rule-2026-05-29` | open | adjacent: SDP atom→knot rule for A∈{5,6,7}; **intent posted** earlier |
| #1440 | `charming-keller` | open | no overlap (compute infra: LP → Clarabel MPFR) |
| #1441 | `cosmetic-vhat-and-table-computation` | open | no overlap (cosmetic + schema) |

## Critical main movements integrated on rebase

- **#1442 merged** (`derive: full meson m_K²/m_π² closure to 0.056 ppm (sub-ppb)`) — directly closes the meson EM gap I was discussing via `(α_em/π)·m_π²·(1+ℏ_q)`. Means: **meson EM is closed structurally on main**, not blocked by α_em precision (consistent with my PR's correction, but ahead of my PR's framing).
- **`purge(SW): full Schur-Weyl purge + τ_M uniqueness Lean refactor`** (in #1442) — Schur–Weyl is gone from the framework. Matches the earlier exchange about whether SW would supply per-block angular momentum (deprecated, then purged). Removes one option from the binding A≥3 toolbox.
- `c731111`, `aebe42a`: q₀ cleanup / re-pin around `derivation_chain` — no impact on α_EM (Bring shift uses g=4 only, not q₀).

## Open / remaining

- **α/(4π) derived form** — the last 57 ppb. Candidate `1/(2π·[2]_q)` is 1.4% off — not it. Open research.
- **Connection to #1443** — operator-valued LR branching at trivial `I` and torus-knot braids should reproduce the per-rep `[n]_q` evaluation as a corollary.
- **CI failures on #1444** — `validate`, `content-pipeline` — same pre-existing main-level cluster as #1417 (PR adds zero TypeScript, only new probes); local e0 audit passes.

## Coordination actions taken

- Posted intent on **#1431** (a567 SDP): noted α_EM at 4 ppm no longer blocks downstream EM corrections; `[n]_q` is the q-dimension identification.
- Posted intent on **#1443** (operator-valued LR branching): flagged the topical link to my Probe 3 q-dimension identification.
- Did **not** post on #1442 (merged) per coordinate skill conventions.

## Next concrete (non-overlapping)

- If the α/(4π) derived form is needed: investigate whether the Bring zero-mode shift's `α/(4π)` partner comes from the *first* archimedean correction beyond the q→1 limit of the Bring zero-mode classes (likely a categorical Hodge-class computation).
- If the topical link to #1443 needs to be formalised: add a corollary to `prop:hecke-branching-trace-decomposition` recovering the q-dimension identification at `I=1` on torus-knot braids — but defer until owner reviews #1443.

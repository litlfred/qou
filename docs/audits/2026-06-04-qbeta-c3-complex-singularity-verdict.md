# c_3 complex-singularity probe — verdict

**Date:** 2026-06-04
**PR:** [#1821](https://github.com/litlfred/qou/pull/1821)
**Status:** DONE — feasibility/geometry result (NOT a closure)
**Plan:** [2026-06-04-qbeta-c3-complex-singularity-plan.md](2026-06-04-qbeta-c3-complex-singularity-plan.md)

## Result

Script:
[`qbeta_c3_complex_singularity_probe.py`](../../computations/qbeta/qbeta_c3_complex_singularity_probe.py)
· witness `qbeta-c3-complex-singularity-probe.witness.json`.

From the published anchors (`c_3(proton) = -2.0693`, `c_3(muon) = -2.0097`,
`Δq ≈ 1.28e-8` ⇒ 2.88% swing, `dc_3/dq ≈ 4.66e6`):

| quantity | value |
|---|---|
| nearest-singularity distance `b ≈ |c_3|/|dc_3/dq|` | **4.44e-7** |
| dist(q₀, nearest root of unity = ζ₁ = 1) = `|q₀ - 1|` | 0.10998 |
| ratio (RoU distance / b) | **2.47e5** |

## Two findings

1. **Complex-analytic framing — SUPPORTED.** `b ≈ 4.4e-7 ≪ 1`. As `b → 0`
   the implied derivative diverges, which is impossible for a smooth real-q
   function — so `c_3` is dominated by a singularity at distance `~b` from q₀
   and **cannot** be a smooth real-q `f(q)`. This independently confirms the
   cross-anchor rigidity falsification, and supports the fibre-level
   complex-analytic Habiro framing (AGENTS.md §"Im(q) at fibre vs observable
   level").

2. **Root-of-unity mechanism — REFUTED.** For real q₀ ≈ 1.11 (just outside the
   unit circle) the nearest root of unity is `ζ₁ = 1`, at distance
   `|q₀ - 1| ≈ 0.11`. That is **2.5e5× farther** than the singularity at `b`.
   Every other root of unity (ζ₂ = -1 at 2.11, ζ₆ = e^{iπ/3} at ~1.06, …) is
   farther still. So **root-of-unity evaluation cannot source the c_3
   hypersensitivity** — the specific RoU sub-hypothesis is refuted, while the
   broader complex-analytic framing stands.

## Interpretation

The singularity governing `c_3` is **near-real at q₀** (`b ~ 4e-7`), not on the
unit circle. This is consistent with the **residue-A simple pole at
u_substrate** (radius of convergence = u_substrate, PR #1713/#1727): q₀ sits
extremely close to the Q_β/Habiro singularity, which is exactly why `c_3` (a
high-order extracted ladder coefficient) is hyper-sensitive. The c_3
hypersensitivity and the residue-A precision ceiling (PR #1805) are two faces
of the **same near-q₀ singularity**.

## What this is and isn't

- **Is:** a geometry result pinning the nearest singularity to `b ~ 4e-7`,
  refuting both the real-q form (`b = 0`) and the root-of-unity mechanism,
  and unifying the c_3 swing with the residue-A pole.
- **Isn't:** a closure. It does **not** produce a categorical `c_3` formula.
  The genuine Habiro element remains the **open keystone** (registry §3/§5).

## Implication for the residue-A unblock

The genuine direction is a **near-real complex-analytic** object (the Q_β
Habiro element at its u_substrate singularity), **not** a root-of-unity
evaluation. Combined with the precision-ceiling verdict (PR #1805: A is ~4 sig
figs, gated on canonical c_11+), the productive next step is the **canonical
higher-order c_k extraction at the singularity**, which is owner-direction
research (registry §5; not an ansatz fit).

## Anti-pattern compliance

- ✅ Feasibility/geometry probe; explicitly NOT a closure (witness
  `is_closure: false`).
- ✅ TIERED honesty: supported (framing) / refuted (RoU mechanism) / open
  (the element).
- ✅ q₀ from canonical values; diagnostic-only; no production wiring.

## Cross-references

- c_3 real-q falsification: [2026-06-04-c3-habiro-3rung-crossanchor-rigidity-falsification.md](2026-06-04-c3-habiro-3rung-crossanchor-rigidity-falsification.md)
- residue-A precision ceiling: [2026-06-04-qbeta-residue-a-precision-ceiling-verdict.md](2026-06-04-qbeta-residue-a-precision-ceiling-verdict.md)
- canonical registry: [../coordination/ck-dk-canonical-registry.md](../coordination/ck-dk-canonical-registry.md)

# α_EM bean B3 — conformal inheritance: J ⟹ conformal class ⟹ Laplacian ⟹ a₀ (2026-07-18)

**Bean:** `qou-cncc` (B3) of the τ-correspondence proof plan (milestone
`qou-b5qg`). Upstream: B1 merged ([#3955](https://github.com/litlfred/qou/pull/3955),
fibre reality structure ρ), B2 shadow merged
([#3960](https://github.com/litlfred/qou/pull/3960), `shadow_unique` — the
ρ↔Hodge dictionary is FORCED at the degenerate locus).

**Probe:** [`computations/alpha_em/alpha_em_b3_conformal_inheritance_probe.py`](../../computations/alpha_em/alpha_em_b3_conformal_inheritance_probe.py)
→ [`alpha-em-b3-conformal-inheritance.witness.json`](../../computations/alpha_em/alpha-em-b3-conformal-inheritance.witness.json)
— 3/3 assertions PASS.

**Scope guard (STRICT):** scope-(a); derives no clause unconditionally; no
fit; nothing wired; `1/(8π)` stays a phase-4 identification (owner ruling
`dd55a5748`).

## The chain, per-step status

B3's job in the plan: connect the geometric object B2's lift lands on (the
complex structure `J` on the Bring side) to the analytic unit `a₀ = 1/(4π)`
that the per-loop conjecture's Clause A needs. The chain has three links:

| Link | Statement | Status |
|---|---|---|
| (i) | `J` ⟺ conformal class (+ orientation) on a surface | **standard** — a complex structure on a 2-manifold is exactly a conformal class with orientation (textbook; e.g. Jost, *Compact Riemann Surfaces*); cited, not re-proved |
| (ii) | conformal class + area ⟹ Laplacian ⟹ `Tr e^{tΔ} ~ Area/(4πt)`: the per-mode weight `a₀ = 1/(4π)` per unit area is **metric-independent** | **VERIFIED** here (V1/V2, below) |
| (iii) | IF the B2 functorial lift holds (τ carries the braiding's degenerate pair to `J` at the vertices) THEN the loop geometry inherits the conformal class `J` defines and with it the universal unit `a₀` | **CONDITIONAL** — stated, not derived; B2-lift open (Mathlib-gated), B4 open |

Net effect on the wall: **Clause A of the per-loop conjecture reduces to
(B2-lift) + (B4)** — the loop-universality clause is no longer an independent
open item; its only open inputs are the functorial lift (bean `qou-tq20`) and
the classical-limit normalization (bean `qou-1p06`).

## What was verified (V1–V3)

**V1 — a₀-universality across metric shapes.** For flat tori with Gram
matrices of very different shape — square, hexagonal, skew
`[[1,0.7],[0.7,2]]`, and a 9:1 anisotropic `diag(1,9)` — the exact lattice
heat trace satisfies

$$
\operatorname{Tr} e^{t\Delta_G} \cdot \frac{4\pi t}{\mathrm{Area}(G)} \to 1
$$

with the ratio equal to 1 to ≤ 10⁻⁶ already at `t = 10⁻³` for **all four**
shapes (square/hex/skew: 1.00000000; 9:1 anisotropic: 0.99999999). The
leading heat coefficient carries no metric data beyond the area: the
per-mode weight `1/(4π)` is universal.

**V2 — convergence is uniform-in-shape at the checked scales.** For the
worst-conditioned metric (9:1 anisotropic), the ratio at
`t = 10⁻², 3·10⁻³, 10⁻³` is `[1.00000000, 1.00000000, 0.99999999]`. On flat
metrics there is no curvature term, so the approach is exponential (the
dual-lattice term), not `O(t)` — already exact at these scales.

**V3 — consistency with the proved χ-side.** Sympy-exact: the merged GB Lean
identity `|χ|/(4·Area) = 1/(8π)` holds identically with
`Area = 2π·|χ|` (Gauss–Bonnet, curvature −1), and on Bring (`g = 4`):
`χ = −6`, `Area = 12π`, heat-trace constant `χ/6 = −1` (the merged
conjecture-statement value). The **same** universal `a₀` sits inside the
curved-side measure — V1's universality is exactly what makes the GB-side
coefficient `a₀` and not a metric-dependent weight.

## Honest scope

- Link (i) is a citation, not a new result.
- V1/V2 verify link (ii) **within the flat family** — the family where exact
  lattice sums exist. By the standard heat expansion, curvature corrections
  change subleading terms only (`t⁰` and beyond); the leading `a₀` term is
  the universal one on any closed surface. V3 checks the curved-side
  arithmetic consistency but is not an independent curved-side heat
  computation.
- Link (iii) is **conditional** — B3 does not derive Clause A
  unconditionally, does not derive the B2 lift, and leaves B4 open.
- Nothing is wired to production; no tier changes.

## Position in the proof plan

```
B1 (ρ reality structure)        MERGED #3955
B2 (functorial statement)       shadow MERGED #3960 (FORCED); lift OPEN (Mathlib-gated)
B3 (conformal inheritance)      THIS — chain delivered; Clause A = B2-lift + B4
B4 (classical-limit norm, KL)   OPEN — the hard analytic piece
B5 (assembly)                   blocked on B2-lift + B4
```

Next per the plan: **B4** (`qou-1p06`) — the classical-limit normalization
"q→1 one-loop total = a₀·α" via the KL/decategorification route (§7b item 2),
flagged the hardest brick.

# Δ_λ binding front — the single ≥4-body per-pair bond-magnitude scalar (session intent 2026-07-25)

**Goal.** Open the Δ_λ binding-closure front (owner: option 1 after the c₃ exclusion
capstone). Per the #4146 frontier: "the whole Δ_λ wall reduced to one value — the
deltalambda ≥4-body per-pair bond-magnitude scalar" (hand-off consumes #3802 + #3875);
and #4142: "Δ_λ magnitude reduced to a non-determinant graded-dimension object with a
two-sided bracket." The binding formula B(K)=m_e·Σ_λ y_λ χ^λ Δ_λ; sign + single-trace
magnitude are derived; the residual is this one per-pair bond scalar.

**Active-front awareness (coordinate, don't duplicate).** The covariance-kernel epic
`qou-x631` is actively working deltalambda on main (recent: "A2 — polynomial-positivity
reduction + 3 route-eliminations"). Parallel-exploration is permitted for OPEN research
(AGENTS.md), but the angle must be DISTINCT and coordinated. Scout the current x631
state + the two-sided bracket + #3802/#3875 FIRST.

**Discipline (STRICT).** The Δ_λ gate is "open for all" (2026-07-13) for *derivation*
routes, but the anti-fit / "no seventh fit-based ansatz" rule STANDS: a Δ_λ obtained by
inverting the AME anchors is a FIT, must be labelled one, and may not be wired as
canonical. The Lean-proved PROBE-4 KL-positivity prune stays pruned. Formalize-first
before any wide scan; scope-(a)/(b); nothing wired.

## Findings ledger

| # | date | angle | result | tier | artifacts |
|---|------|-------|--------|------|-----------|
| 1 | 2026-07-25 | **Single-knob two-anchor rigidity on the graded-dim upper bracket** (distinct from x631's partition-index covariance kernel; this is the per-**isotope** ρ_grad(A) over nucleon `A`). Formalize-first execution of **W5** (`qou-j5rx`, was todo): Lean-state the invariant any graded-dim family must satisfy. | **WALL (proved).** The single-parameter `q`-scaled coinvariant graded dimension `[A]_q!` **cannot** land both light-nucleus anchors `{ρ_strong(3)=3.8128, ρ_strong(4)=13.0316}`: (S) step-lock `[4]_q ≥ 4 > 3.418` (data step) for all `q≥1`; (M) both ρ_grad(3), ρ_grad(4) monotone ↑ in `q` (one knob, same direction); (N) reaching A=3 ⇒ A=4 overshoot (`3.8128·4 = 15.2512 > 13.0316`, margin 2.2196). Plus scope-(b) elimination of the SU(4) row-restriction damping (vacuous for A≤4). Search narrowed to genuinely **A-dependent** (non-single-knob) dampings. | scope-(b) proved invariant (S)/(M) [AME-independent] + scope-(a) comparison (N); **nothing wired, no fit** | Lean `JetFiltrationTwoAnchorNoGo.lean` (sorry-free, lean-direct exit 0); probe `deltalambda_graded_two_anchor_nogo_probe.py` (6/6, 60 dps); audit `docs/audits/2026-07-25-deltalambda-perpair-bond-scalar.md` |

**Verdict:** distinct-angle contribution is a **tighter WALL**, not a derivation and not a
fit — the `q`-knob cannot collapse the two-sided bracket to a point. Directs W5 to
A-locked parabolic/skew quotients of `[A]_q!` (truncation fixed by a stated principle,
not a fitted knob) or the Demazure sub-crystal (genuinely two-parameter). Coordinated
with `qou-x631` (no overlap — different leg).

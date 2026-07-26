# Δ_λ A-dependent damping — the route past the #4300 two-anchor no-go (session intent 2026-07-26)

**Goal.** Continue the Δ_λ binding front. #4300 (`a671b52f`) PROVED sorry-free a
scope-(b) no-go: the single-parameter q-scaled `[A]_q!` graded dimension cannot close
both light-nucleus anchors (step-lock `[4]_q≥4` + monotonicity + two-anchor no-go
`[3]_q≥3.8128 ⇒ [3]_q[4]_q>13.03`). So the closure needs a genuinely **A-dependent
damping** of `[A]_q!`. Two named routes:
1. An **A-locked parabolic/skew quotient** of `[A]_q!` by a STATED principle (the
   isotope coordination-graph / edge-set structure — NOT a per-A fit).
2. The **two-parameter Demazure sub-crystal** (§7b symmetric-crystal shortcut).

**Discipline (STRICT).** The A-dependence must come from a DERIVED principle, not a
per-A knob tuned to AME (that is the "seventh fit-based ansatz" the gate forbids;
inverting AME per-A is a FIT, labelled one, never wired). Formalize-first: state the
A-dependence principle as a Lean lemma before any wide scan. scope-(a)/(b); nothing
wired. PROBE-4 KL-positivity prune stays pruned.

**Coordinate.** x631 (covariance kernel over λ) + the B-tranche (#4283, module-map
sweep now complete/negative) are orthogonal to this A-over-nucleon leg. Scout the
jet-filtration audit §4 two-sided bracket + #3802/#3875 first; post intent.

---

## FINDING (2026-07-26) — WALL: both named damping routes excluded

**Verdict: WALL (scope-(b), pure-damping class excluded).** Both proposed routes
(a) A-locked parabolic/skew quotient and (b) Demazure sub-crystal are **dampings**
`D(A) ≤ 1`. At the **fixed canonical substrate** `q₀ ≈ 1.10998` the residual
`ρ_strong(A) − ρ_grad(A)` **changes sign**:

| A | `ρ_grad(A)(q₀)` | `ρ_strong(A)` | residual | needed `D(A)` |
|---|-----------------|---------------|----------|---------------|
| 3 | `[3]_{q₀}=3.3420` | 3.8128 | **+0.4708** (undershoot) | 1.1409 **(amplify)** |
| 4 | `[3][4]_{q₀}=15.7396` | 13.0316 | **−2.7080** (overshoot) | 0.8280 (damp) |

A damping supplies a non-positive correction at every A → cannot realise a sign
change → **no damping closes A=3** (which needs amplification). Generalises the
Demazure-only A=3 obstruction to the whole pure-damping class. Anchor-robust
(holds for raw AME 3.814/12.72 too).

- **Lean (sorry-free, `lean`-direct exit 0):** `QOU/MassTheory/DampingNonMonotoneWall.lean`
  — `damping_cannot_close_A3`, `substrate_A4_overshoots`, `damping_route_walled`.
- **Probe (6/6, exit 0):** `computations/deltalambda/deltalambda_damping_nonmonotone_wall_probe.py`.
- **Audit:** `docs/audits/2026-07-26-deltalambda-A-dependent-damping.md`.
- **PR:** #4307.

**Open target (NOT excluded, permanence).** `[A]_q!` stays a valid ingredient; the
correction is **additive + sign-changing in A** (a many-body term), not a
multiplicative suppression. Nothing wired; anchors are bounds only.

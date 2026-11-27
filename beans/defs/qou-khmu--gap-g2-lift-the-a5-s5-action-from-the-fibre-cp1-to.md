---
# qou-khmu
title: 'GAP G2: lift the A5/S5 action from the fibre CP1 to the base curve M0 (chi = -6 chain)'
status: todo
type: task
priority: high
tags:
    - bring-foundations
    - research
    - open-derivation
created_at: 2026-11-21T07:30:00Z
updated_at: 2026-11-22T21:59:12Z
parent: qou-6qbv
---
Created 2026-11-21 by W9 (session_01VQDpPcjxVSqN8ELUBjiBHk). The gap was named in `docs/audits/2026-11-17-bring-foundations-trace-sites-and-genus-attack.md` §3 and had no bean.

**Statement.** The corpus has A5 (and the EM involution in S5 \ A5) acting on the fibre P(V) ≅ CP¹ (`klein-bring-icosahedral-bridge`), not on the base curve M0. The genus-4 chain needs a faithful A5 action on M0, extending to S5.

**What is proved downstream.** Granted the lift and G3, the genus is 4 and χ = -6. This is sorry-free on main: `IrreducibleH1ForcesGenusFour`, `A5NoSixDim`, `RiemannHurwitzCellular`, `GenusFourFromGermStabilisers`, `GenusFourFromEquivariantMap`.

**Constraint (NO FITTING).** Every order-5 structure in the corpus is downstream of Bring (audit §2 item 4, qou-qhcr sessions of 2026-09-15). The lift must not be chosen because it yields 4.

**Open; do not close** (AGENTS.md §13a).

## 2026-11-22 applicability review (wave-2 sibling bring-riemann-gerbes, session_01Qmmkt7Jw9nSDCzSdsd8hLX)

APPLIES. Premises checked against owner-rulings.md on origin/main (all rows to 2026-11-22: photon with fixed constant 1, γγ linking neutrality, derived quark charges, potential-energy sign, m_p = m_n at q = 1, gluon open, electron σ₀σ₁σ₀ with T(2,n) as backup, S₅ two-test rule, T(A) tangent algebra) and git log on the Lean/content paths since the last update. Nothing landed on the fibre-to-base lift. Critical note: the anti-fit constraint in the body is the binding one; any lift chosen because it yields genus 4 is selection against the target. Open; stays open.

## 2026-11-22 tracker hygiene (qou-w3yy, owner-approved)

Parent set to `qou-6qbv`: old parent `qou-qhcr` is not an epic/milestone/feature; re-pointed to its nearest legal ancestor. No change to this bean's scope or status.

## 2026-11-27 — χ = −6 chain thread (session_01VQDpPbyS5NspZ1YQT2xsE6, PR #9726)

PR #9726 shows the chain needs, besides the cell structure, only G2 plus either (G3 + S₅) or the least-hyperbolic selection principle. So G2 is now the one structural input common to every route. Not attempted; still open.

## 2026-11-27 (χ = −6 chain thread, second pass): two explicit lifts, and what they do not decide
A lift of the A₅ action from the fibre P(V) ≅ ℂP¹ to a base curve is the same thing as an **A₅-equivariant branched cover M₀ → ℂP¹**, branched over a union of A₅-orbits (sizes 12, 20, 30, 60). Two classical ones:
- **Degree 2 over the 12-orbit** (icosahedron vertices): y² = f₁₂(x₀, x₁), Klein's degree-12 icosahedral form, in P(1,1,6). The binary icosahedral group acts on (x₀, x₁); −1 acts trivially in P(1,1,6), so A₅ acts. χ = 2·2 − 12 = −8, **genus 5** (hyperelliptic, Aut ⊇ A₅ × ℤ/2). This is the g = 5 member of the G3 window {4, 5}; S₅ removes it.
- **Degree 3 over the 12-orbit**: radial projection of the great dodecahedron {5, 5/2} (density 3, Coxeter *Regular Polytopes*). Each of the 12 vertices has a pentagram vertex figure, so local degree 2 there: R = 12, χ = 3·2 − 12 = −6, **genus 4**, A₅-quotient signature (0; 2,5,5). This is Bring's curve (the great dodecahedron is a regular map of type {5,5} on it, cf. PR #9726's probe).
**Scope (a) negative:** "lift with the least covering degree" selects degree 2 and genus 5, **not** Bring. So minimal degree is not the principle; degree 3 is what Bring needs, and nothing found forces 3. Not formalised (needs branched covers of ℂP¹). G2 stays open.

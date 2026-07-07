# Q_β and c₃ Synthesis: The Cosh-to-Cos Bridge and Fibre Swing

**Date:** 2026-07-07 · **Axis:** z→c_k f-map keystone · **Follows:** KC19, KC20, and the GS W2-Kill
· **Tier:** synthesis-plan

## 1. The Assembled Picture from Recent Landings

The recent integration of the `c_3` and `Q_β` PRs provides a complete portrait of the mismatch between the first-principles categorical growth and the observed decay ladder:

1. **The c₃ Swing and the Hopf Cubic (KC19 + KC20)**
   The odd-channel cubic $C_{Hopf}(y) = y^3 - 6y^2 + 10y - 6$ (sourced by the chiral Hopf link) has a negative discriminant, providing the required complex structure.
   At the shadow limit ($q=1$), it perfectly recovers the classical crossing weight $c_3(1) = -2$.
   However, at the physical substrate ($q_0$), $C_{Hopf}$ is anchor-rigid, while the physical $c_3$ exhibits a 2.375% swing between proton and muon anchors. Since $c_3$ is the $\mathcal{O}(u^3)$ coefficient of the crossing-weight departure $w(q)-1$, this swing must originate purely in the fibre structure of $w(q)$.

2. **The Categorical GS Net vs. The Observable Ladder (W2-Kill)**
   The full Gram-Schmidt (GS) augmentation perfectly reproduces the N=0 base amplitude $Q_A$ (W1 Pass).
   However, at higher orders, the GS net is *cosh-like* ($\sim 1 + \mathcal{O}(\hbar_q^2)$), directly conflicting with the *cos-like* structure of the production observable ladder $Q_{N1} = Q_A \cos(\alpha - b\hbar_q^2/2)$. The departure begins at $\mathcal{O}(u) = \mathcal{O}(\hbar_q^2)$.
   The first-principles categorical net describes growth; the decay observable describes a bounded, oscillatory ladder.

## 2. The Synthesized Objective: The Faddeev/Rogers Transformation

The central open problem is identifying the analytic continuation (or modular double transformation) that bridges these two regimes. The transformation must simultaneously achieve two things:
1. **The Sign Flip (cosh → cos):** Map the divergent, bar-even categorical growth (the $\cosh$-like GS net) to the bounded, bar-odd observable signature (the $\cos$-like ladder).
2. **The Fibre Swing:** Introduce the anchor-dependent swing into $c_3$, mapping the anchor-rigid evaluation of the chiral Hopf cubic into the 2.375% swinging observable coefficient.

This maps structurally to the known two-saddle geometry of the Faddeev modular quantum dilogarithm (or the Rogers dilogarithm on the torus).

## 3. Next Steps (Execution Plan)

1. **PyHecke Probe:** We will build a python script to probe the Faddeev/Rogers transformation on the GS net departure. Can we explicitly find a transformation mapping the GS $+ \frac{9}{8}\hbar_q^2$ departure to the negative cos-like ladder terms?
2. **Lean Formalization:** Formalize the structural precursor: proving that the odd-channel cubic has a negative discriminant (complex-conjugate roots) while the even channel ($4_1$ amphichiral) is real.

## Discipline
No new $c_k$ fits or values are introduced here. This synthesis formally rescopes the next mathematical effort towards the analytic continuation bridge, rather than attempting to coerce the GS net directly into the ladder form.

# q-NS: twisted transport, and why q-difference advection dissipates

Date: 2026-11-27. Bean `qou-q3dc` (gap), arc `qou-pa7n` (Part A, open). Lean:
`folio/quantum-observable-universe/lean/QOU/FluidDynamics/q_ns_twisted_transport.lean`.
The file is sorry-free, `lean -DautoImplicit=false -s 65536` exits 0, and its
axioms are `propext, Classical.choice, Quot.sound`. No empirical value enters
any proof.

## Question

`q_ns_triad_noncomm.lean` proved triad energy conservation for any linear
functional, given an **untwisted** divergence-free derivation. Is the q-NS
transport ∇_q an untwisted derivation on `O_q(SU(2))`?

## Corpus answer: no

At generic q the corpus builds the connection on Woronowicz's 3D calculus
(`ex:connection-su2`). Its vector fields obey a twisted Leibniz rule,
`X(fg) = Xf·θg + f·Xg`, where the twist θ is a torus automorphism. The
archimedean q-derivative is a q-difference operator, which is twisted in the
same way. So the untwisted theorem does not cover the corpus transport.

## What is proved (any algebra, any linear functional)

| Lean | Statement |
|---|---|
| `twisted_energy_budget` | X θ-twisted, φ∘X = 0 ⇒ `φ(Xu·u) + φ(u·Xu) = φ(Xu·(u − θu))` |
| `twisted_energy_budget_id` | θ = id gives conservation |
| `qDiff_leibniz`, `qDiff_div_free` | `D = (θ − id)/c` is θ-twisted, and divergence-free for a θ-invariant φ |
| `qDiff_energy_budget` | `φ(Du·u) + φ(u·Du) = −c·φ(Du·Du)` (an exact identity) |
| `qDiff_energy_budget_ne_zero` | explicit nonzero instance (ℚ × ℚ with the swap automorphism) |

## Reading (judgement, not a theorem)

A q-difference transport does not conserve the quadratic energy. It carries a
built-in dissipation term, `−c·φ((Du)²)`, that is first order in the step c.
For a positive state and a self-adjoint `Du`, that term has the sign of `−c`.
The Haar state is invariant under the torus automorphisms, so the hypothesis
`φ∘θ = φ` holds for torus twists on `O_q(SU(2))`. The file does not construct
the Haar state, positivity or the `*`-structure.

This changes what Part A is about. With twisted transport, the nonlinear term
can change the energy as well as move it between modes. Whether that change
regularises or destabilises as q → 1⁺ depends on the sign and size of c for
the actual vector fields of the 3D calculus. Those vector fields are not built
here.

## Not established

- That the corpus ∇_q on `O_q(SU(2))` is a q-difference operator. The corpus
  names the 3D calculus but does not define ∇_q on the noncommutative algebra.
- The sign of the dissipation on `O_q(SU(2))`.
- Part A.

## Update: orientation, the balanced difference, and the 3D-calculus twist

Three further results, all sorry-free (axioms: propext, Classical.choice,
Quot.sound), in the same file:

- `qDiff_neg`: the q-difference with step −c is minus the one with step c. So
  the sign of the dissipation term is set by the orientation of the difference
  (forward or backward), not by the algebra.
- `qCen_energy_conserving`: for an automorphism θ with φ∘θ = φ, the balanced
  difference (θ − θ⁻¹)/c, the operator behind the corpus's balanced q-integers,
  conserves the quadratic energy exactly, for every u and c.
- `theta3D`, `theta3D_energy`: the twist of Woronowicz's 3D calculus,
  (a, b, c, d) ↦ (q⁻²a, q⁴b, q⁻⁴c, q²d) (Hadfield–Krähmer, library
  `arxiv-math-0405249v5`), is the corpus torus automorphism
  `torusScaleAlgEquiv q (q⁻²) (q⁴)` on `OqSU2`. For any functional invariant
  under it, the one-sided budget is −c·φ(Du·Du) and the balanced budget is 0.

So whether q-NS transport on O_q(SU(2)) conserves or changes energy depends on
which difference the vector fields of the 3D calculus are. That is the next
open question. Haar invariance under θ is still a hypothesis, and positivity
and the *-structure are still not built.

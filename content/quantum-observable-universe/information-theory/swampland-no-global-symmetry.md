The observability axiom
([quantum observable universe](#def:quantum-observable-universe),
condition ii) requires
$$
  \mathrm{Hom}_{\mathbf{C}}(\mathbf{1}, \mathrm{Ad}(A)) = 0:
$$
the adjoint object carries no invariant section. This is the
categorical form of a foundational Swampland criterion.

**The Swampland statement.**
A consistent theory of quantum gravity admits no exact global symmetry
\cite{banks-seiberg2011}; in holographic settings this is established
rather than conjectural \cite{harlow-ooguri2021}. A global symmetry
would act on the matter content while commuting with every local
observable, leaving a sector that no measurement can reach.

**QOU translation.**
The vanishing $\mathrm{Hom}_{\mathbf{C}}(\mathbf{1}, \mathrm{Ad}(A)) = 0$
is the vanishing of the zeroth adjoint cohomology
$H^0_G(\mathrm{Ad}(A))$
([fibre functor rigidity](#rem:fibre-functor-rigidity)), and the Lie
algebra of $\mathrm{Aut}^{\otimes}(\tau)$ is exactly
$\mathrm{Hom}_{\mathbf{C}}(\mathbf{1}, \mathrm{Ad}(A))$. The axiom
therefore excludes any infinitesimal automorphism of the fibre functor
$\tau$ that acts trivially on every observable — precisely a decoupled
global symmetry. Every internal degree of freedom is gauge-accessible
to measurement.

**Scope.**
The correspondence is structural. The Swampland statement is a
constraint on dynamical gravity inferred from black-hole physics; here
the same exclusion is imposed as an axiom at the categorical level and
discharged in Lean as
$\mathrm{Subsingleton}\bigl((\mathbf{1}_{\mathbf{C}}) \to \mathrm{Ad}(A)\bigr)$.
We do not claim that the framework derives the no-global-symmetry
principle of quantum gravity; we observe that it internalises the same
content.

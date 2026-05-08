The [substrate parameter](#def:substrate-parameter) is defined over an
arbitrary base field $k$, so $q \in \mathrm{End}(\mathbf{1}) \cong k^\times$.
Nothing in the *algebraic* definition of $d_q$ requires $q$ to be real.
Over $k = \mathbb{C}$, write $q$ in polar form:

$$
  q =  |q|e^{i\varTheta}, \qquad |q| \geq 1,\quad \varTheta \in (-\pi, \pi].
$$

The deformed differential becomes

$$
  d_q =  |q|^{-1} e^{-i\varTheta}d
  +  \bigl(1 - |q|^{-1} e^{-i\varTheta}\bigr)\pi_V \circ d,
$$

and the quantum Planck constant generalises to

$$
  \hbar_q =  1 - q^{-1}
  =  1 - |q|^{-1} e^{-i\varTheta}.
$$

When $\varTheta \neq 0$, $\hbar_q$ acquires an imaginary part
$\mathrm{Im}(\hbar_q) = |q|^{-1}\sin\varTheta$, so the
$q$-equilibrium of the
[$q$-Laplacian](#rem:q-laplacian-interpretation) is no longer
self-adjoint — it mixes amplitudes with phases.

**Why observability forces $\varTheta = 0$.**
A [quantum observable universe](#def:quantum-observable-universe) carries
a dagger structure $\dagger$ and a fibre functor $\tau$ satisfying
positive-definiteness: $h_q(a^\dagger a) > 0$ for all $a \neq 0$.
For the Haar functional $h_q$ to be positive-definite, the inner product
$\langle \alpha, \beta \rangle_q = h_q(\alpha^\dagger \wedge_q \beta)$
on $\Omega^\bullet(A)$ must be Hermitian.  This requires $d_q^\dagger$
to be the formal adjoint of $d_q$, which holds if and only if

$$
  \overline{q^{-1}} = q^{-1},
$$

i.e. $q \in \mathbb{R}_{>0}$.  The positivity axiom $q \geq 1$ then
gives the Lean constraint `field_ge_one`.

**What the imaginary part would mean.**
If one relaxes the observability axiom — passing to the "pre-observable"
or algebraic sector — the phase $\varTheta$ has a geometric interpretation:

1. **Phase in crossing energy.** In the skein relation
   $qL_+ - q^{-1}L_- = (q - q^{-1})L_0$, complex $q$
   contributes a relative phase $e^{2i\varTheta}$ between over-
   and under-crossings.  This phase distinguishes a knot from
   its mirror image *continuously*, rather than by discrete
   crossing reversal.

2. **Continuous chirality.**  The operator
   $\sigma_\varTheta \colon q \mapsto |q|e^{i(\varTheta + \pi)}$
   acts as chirality reversal.  For real $q$ ($\varTheta = 0$),
   this is the discrete flip $q \mapsto -q$ (ill-defined for
   $q > 0$).  For complex $q$, chirality reversal becomes a
   continuous rotation in the $\varTheta$-circle, and the
   electron/positron distinction is a $\pi$-rotation rather
   than a discontinuous mirror.

3. **Non-Hermitian $q$-Laplacian.**  When $\varTheta \neq 0$,
   $\Delta_q$ has complex eigenvalues.  The real part still
   controls spatial diffusion, but the imaginary part generates
   a *probability current* along the Reeb fibre — a persistent
   phase rotation of the internal quantum state.

**Relation to root-of-unity specialisations.**  The
[$\mathrm{SU}(2)$ specialisation](#def:substrate-parameter) at
$q_0 = e^{\pi i / \kappa}$ has $|q_0| = 1$ and
$\varTheta = \pi / \kappa$ — it is genuinely complex.  This does not
contradict the observability constraint because root-of-unity
categories carry a *modified* trace (the quantum trace $\mathrm{tr}_q$)
that restores a non-degenerate pairing without requiring
positive-definiteness in the Hilbert-space sense.  The finite
modular tensor category at roots of unity is the prototype of a
"non-observable but algebraically consistent" sector.

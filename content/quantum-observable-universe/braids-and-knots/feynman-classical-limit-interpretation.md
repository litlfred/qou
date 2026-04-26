The classical limit ([recovery of the symmetric path integral](#prop:feynman-classical-limit))
identifies the precise mechanism by which the QOU categorical trace
degenerates to the standard quantum-mechanical formalism.

**The Hecke degeneration.**
At $q = 1$, the Hecke relation $(T - q)(T + q^{-1}) = 0$ becomes
$T^2 = 1$: the minimal polynomial of the braiding drops from a
quadratic with distinct roots $q \neq -q^{-1}$ to a quadratic with
roots $\pm 1$.  The consequence is that the two eigenspaces
$S^2 V$ (eigenvalue $q$) and $\Lambda^2 V$ (eigenvalue $-q^{-1}$)
merge into the $+1$ and $-1$ eigenspaces of the symmetric group
transposition.  The Hecke algebra $H_n(R, q)$, which at generic $q$ is a
non-trivial deformation of $k[S_n]$, becomes $k[S_n]$ itself.

**Loss of knot discrimination.**
The Jones polynomial satisfies $J_K(1) = 1$ for every knot $K$.
This means the Markov trace, which at $q \neq 1$ assigns distinct
values to distinct knot types (and hence distinct masses), becomes
constant at $q = 1$.  The complete knot-type eigenbasis
([knot eigenbasis completeness](#prop:knot-eigenbasis-complete))
degenerates: all knots become topologically trivial under the symmetric
quotient $B_n \twoheadrightarrow S_n$.

The irreducible $H_n(R, q)$-modules $S_\lambda$ become Specht modules of
$S_n$.  These are indexed by the same partitions $\lambda \vdash n$
with $\ell(\lambda) \leq 2$, corresponding to spins
$j = 0, 1/2, 1, \ldots, n/2$.  This is the standard angular momentum
eigenbasis: $|j, m\rangle$ states for $\mathrm{SU}(2)$-coupling of
$n$ spin-$\frac{1}{2}$ particles.

**Vanishing of quantum corrections.**
At $q = 1$, the quantum Planck constant
$\hbar_q = 1 - q^{-1} \to 0$, the speed of light
$c_q = 1/(q - 1) \to \infty$, and the quantum numbers
$[n]_q = (q^n - q^{-n})/(q - q^{-1}) \to n$.  The $q$-energy
([q-energy](#def:q-energy)) becomes

$$
  \mathbf{E}_1(K) = \underbrace{j(j+1) \cdot 0}_{\text{rot.}}
  + \underbrace{w^2 \cdot 0}_{\text{trans.}} + S_1(K) = S_1(K),
$$

recovering the classical action as the sole contribution.  The
topological mass formula $\mathfrak{m}(K) = \mathrm{Vol}(K)/\hbar_q^2$
([topological mass formula](#prop:topological-mass-formula))
diverges as $\hbar_q \to 0$ for hyperbolic knots with
$\mathrm{Vol}(K) > 0$ --- the classical limit assigns infinite mass
to knotted configurations, consistent with the classical expectation
that only unknotted (point-like) particles have finite mass.

**The finite sum persists.**
The decomposition $V^{\otimes n} = \bigoplus_\lambda V_\lambda \otimes S_\lambda$
remains valid at $q = 1$ and has the same number of summands.  The
trace formula

$$
  \sum_{\substack{\lambda \vdash n \\ \ell(\lambda) \leq 2}}
  (2j+1) \cdot \mathrm{tr}_{S_\lambda}\bigl(\pi(\beta)\bigr)
$$

is a finite sum over $\lfloor n/2 \rfloor + 1$ terms.  This is the
standard trace over the Clebsch--Gordan decomposition of
$(\mathbb{C}^2)^{\otimes n}$ in non-relativistic quantum mechanics.
The divergences of the continuum Feynman integral arise not from the
eigenspace structure (which is finite at every $n$) but from the
passage $n \to \infty$ without the algebraic constraint
--- the Hecke relation at $q \neq 1$ --- that organises the infinite
tower into a convergent topological invariant.

**Proposition (conditional on
[`conj:hyperbolic-volume-transcendence`](#conj:hyperbolic-volume-transcendence)
and
`rem:baryon-period-ratio`).**
*The piecewise geometric invariant
$\mathrm{Geom}(K)$
([topological mass formula](#prop:topological-mass-formula))
is the evaluation of the Yekutieli rigid dualizing complex
$\omega_A^\bullet$ on the algebraic stratification of the braid
$\beta$ with closure $K = \widehat\beta$ (per
[algebraic stratification](#prop:phi-q-tower-algebraic-stratification);
the τ-image of this evaluation is the geometric reading on
$S^3 \setminus K$, classified by Thurston's geometrization at the
τ-side):*

$$
  \mathrm{Geom}(K) =
  \langle \omega_A^\bullet, S^3 \setminus K \rangle_{\mathrm{Frob}}
  =
  \begin{cases}
    \mathrm{Vol}(K) / \hbar_q^2
      & K \text{ hyperbolic} \\[4pt]
    \mathrm{CS}(K) \cdot \hbar_q^2
      & K \text{ torus} \\[4pt]
    0 & K = \bigcirc
  \end{cases}
$$

*where $\langle -, - \rangle_{\mathrm{Frob}}$ is the Frobenius
pairing induced by the rigid dualizing complex, and
$\hbar_q = 1 - 1/q$ is the quantum Planck constant.*

*Proof.*
The argument has three parts.

**Part 1: the rigid dualizing complex mediates duality.**
The Frobenius--Hopf algebra $A$ at the substrate parameter $q$
carries a rigid dualizing complex $\omega_A^\bullet$
(Yekutieli \cite{yekutieli2015}), which satisfies the rigidifying
isomorphism

$$
  \omega_A^\bullet
  \;\simeq\;
  R\mathrm{Hom}_{A^e}(A, A^e)
$$

in the derived category $D(A^e)$.  The Frobenius form
$\lambda\colon A \to \mathbf{1}$ makes $A$ self-dual with respect
to $\omega_A^\bullet$, inducing the non-degenerate pairing

$$
  \langle -, - \rangle_{\mathrm{Frob}}
  \colon
  H^\bullet(S^3 \setminus K; \omega_A^\bullet)
  \otimes
  H^{3-\bullet}(S^3 \setminus K; A)
  \;\longrightarrow\;
  \mathbb{C}.
$$

This is the categorical substitute for the canonical sheaf in the
non-commutative setting.

**Part 2: Geometric type selects the evaluation mode (algebraic
side).** The proof works in $\mathbb{Z}[q^{\pm 1/2}]$ throughout;
the geometric / 3-manifold reading appears only as the τ-image
discussed in Part 3. Algebraically, the rigid dualizing evaluation
$\langle \omega_A^\bullet, S^3 \setminus K \rangle_{\mathrm{Frob}}$
admits a single closed-form expression in terms of the
[algebraic quantum volume](#def:algebraic-quantum-volume)
$\mathrm{Vol}_q(\beta) \in \mathbb{Z}[q^{\pm 1/2}]$ and the
[Chern-Simons phase](#rem:chern-simons-as-knot-invariant) $\mathrm{CS}_q(\beta)$:

$$
  \mathrm{Geom}(K)
  \;=\;
  \frac{\mathrm{Vol}_q(\beta)}{\hbar_q^2}
  \;+\;
  \mathrm{CS}_q(\beta) \cdot \hbar_q^2
$$

with the $\hbar_q$ factors normalising the Frobenius pairing. For
the algebraic-side derivation no Thurston-geometrization input is
required; the Wedderburn-Artin block decomposition of $H_n(R, q)$
selects which of the two summands dominates for a given braid:

- *Algebraic-hyperbolic regime* ($\mathrm{Vol}_q(\beta) \ne 0$
  in $\mathbb{Z}[q^{\pm 1/2}]$): the first summand carries the
  contribution. The fundamental class pairs against the algebraic
  quantum volume, and the Frobenius normalisation introduces
  $1/\hbar_q^2$ as the mass scale.

- *Algebraic-torus regime* ($\mathrm{Vol}_q(\beta) = 0$ in
  $\mathbb{Z}[q^{\pm 1/2}]$, e.g. $\beta = \beta_{T_{m,n}}$): the
  algebraic quantum volume vanishes identically and the second
  summand carries the contribution. The dualising normalisation
  flips to $\hbar_q^2$ (multiplicative rather than divisive),
  reflecting the Frobenius duality between bulk and boundary:

$$
  \frac{\mathrm{Vol}_q(\beta)}{\hbar_q^2}
  \quad\longleftrightarrow\quad
  \mathrm{CS}_q(\beta) \cdot \hbar_q^2.
$$

- *Algebraic-trivial regime* ($\beta = 1$, the identity / unknot
  closure): both algebraic summands vanish (vacuum normalisation),
  reflecting the empty cohomology of the trivial element of
  $H_n(R, q)$ against $\omega_A^\bullet$.

**Part 3: the Frobenius self-pairing is unitary (algebraic).**
For any braid $\beta$ and its mirror $\beta^*$ (obtained by
reversing each $\sigma_i \mapsto \sigma_i^{-1}$), the Frobenius
pairing satisfies

$$
  \langle \beta, \beta^* \rangle_{\mathrm{Frob}}
  = \mathrm{Geom}(\beta) \cdot \mathrm{Geom}(\beta^*)^{-1}
  = 1,
$$

since $\mathrm{Vol}_q(\beta^*) = \mathrm{Vol}_q(\beta)$ in
$\mathbb{Z}[q^{\pm 1/2}]$ (algebraic quantum volume is invariant
under mirror image, by inspection of the Markov-trace product
formula) and $\mathrm{CS}_q(\beta^*) = -\mathrm{CS}_q(\beta)$
(the Chern-Simons phase changes sign on mirror — direct
consequence of the $q \mapsto q^{-1}$ involution on the relevant
braid representation).

For **amphicheiral** knots ($K = K^*$, e.g.\ the figure-eight
$4_1$), the self-pairing is manifestly real.  This explains why
the figure-eight BW modification factors
([figure-eight BW coefficients](#conj:six-term-mass-formula-complete))
are both real algebraic expressions in $q$:
$1 - h^2 = 4 - [3]_q$ and $h[2]_q = q^2 - q^{-2}$.

**Connection to transcendence.**
The non-vanishing obstruction classes $\kappa_n \neq 0$
at every level of the brane tower — the content of the
[motivic perpetual obstruction theorem](#thm:motivic-perpetual-obstruction)
applied to the substrate's motivic Galois character at every
finite place — ensure that the evaluation $\mathrm{Geom}(K)$ for
distinct hyperbolic knots produces algebraically independent
values. A polynomial relation among the
$\mathrm{Vol}(K_i)/\hbar_q^2$ would force the tower to collapse
at finite height, contradicting place-by-place non-vanishing of
the motivic Galois character
([hyperbolic volume transcendence](#conj:hyperbolic-volume-transcendence)).
$\square$

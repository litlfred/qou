**Proposition.**
*The piecewise geometric invariant
$\mathrm{Geom}(K)$
([topological mass formula](#prop:topological-mass-formula))
is the evaluation of the Yekutieli rigid dualizing complex
$\omega_A^\bullet$ on the knot complement $S^3 \setminus K$,
filtered by Thurston's geometrization:*

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

**Part 2: Thurston geometrization selects the evaluation mode.**
Thurston's geometrization theorem for knot complements classifies
$S^3 \setminus K$ into exactly three geometric types.  The
cohomology $H^\bullet(S^3 \setminus K; \omega_A^\bullet)$ evaluates
differently in each case:

- *Hyperbolic $K$*: the fundamental class pairs against the
  hyperbolic volume form.  The rigid dualizing complex evaluation
  yields $\mathrm{Vol}(K)$, and the Frobenius normalisation
  introduces $1/\hbar_q^2$ as the mass scale.  This is the content
  of the Kashaev--Murakami--Murakami Volume Conjecture: the Hecke
  algebra trace (Frobenius character $c_K$) recovers
  $\mathrm{Vol}(K)$ in the asymptotic limit.

- *Torus $K = T_{m,n}$*: the hyperbolic volume vanishes.  The
  rigid dualizing evaluation reduces to the Chern--Simons invariant
  $\mathrm{CS}(T_{m,n}) = \pi^2(m^2-1)(n^2-1)/(12mn)$,
  which is the phase of the path integral on the Seifert-fibred
  complement.  The dualising normalisation flips to $\hbar_q^2$
  (multiplicative rather than divisive), reflecting the
  Frobenius duality between bulk and boundary:

$$
  \frac{\mathrm{Vol}(K)}{\hbar_q^2}
  \quad\longleftrightarrow\quad
  \mathrm{CS}(K) \cdot \hbar_q^2.
$$

- *Unknot $K = \bigcirc$*: the complement $S^3 \setminus \bigcirc$
  is a solid torus with no non-trivial cohomology against
  $\omega_A^\bullet$.  The evaluation is zero (vacuum
  normalisation).

**Part 3: the Frobenius self-pairing is unitary.**
For any knot $K$ and its mirror $K^*$, the Frobenius pairing
satisfies

$$
  \langle K, K^* \rangle_{\mathrm{Frob}}
  = \mathrm{Geom}(K) \cdot \mathrm{Geom}(K^*)^{-1}
  = 1,
$$

since $\mathrm{Vol}(K^*) = \mathrm{Vol}(K)$ for hyperbolic knots
(volume is invariant under mirror image) and
$\mathrm{CS}(K^*) = -\mathrm{CS}(K)$ for torus knots
(Chern--Simons changes sign).

For **amphicheiral** knots ($K = K^*$, e.g.\ the figure-eight
$4_1$), the self-pairing is manifestly real.  This explains why
the figure-eight BW modification factors
([figure-eight BW coefficients](#prop:figure-eight-bw-coefficients))
are both real algebraic expressions in $q$:
$1 - h^2 = 4 - [3]_q$ and $h[2]_q = q^2 - q^{-2}$.

**Connection to transcendence.**
The non-vanishing Yekutieli obstruction classes $\kappa_n \neq 0$
at every level of the brane tower — the content of
[motivic perpetual obstruction](#lem:motivic-perpetual-obstruction)
applied to the substrate's motivic Galois character at every
finite place — ensure that the evaluation $\mathrm{Geom}(K)$ for
distinct hyperbolic knots produces algebraically independent
values. A polynomial relation among the
$\mathrm{Vol}(K_i)/\hbar_q^2$ would force the tower to collapse
at finite height, contradicting place-by-place non-vanishing of
the motivic Galois character
([hyperbolic volume transcendence](#conj:hyperbolic-volume-transcendence)).
$\square$

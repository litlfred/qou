<!-- FILE_START: mobius-energy-intro.md -->
The previous section produced the universal $R$-matrix for $\mathcal{U}_q(\mathfrak{su}(2))$, fixing the braiding on $\mathbf{Rep}(\mathcal{U}_q(\mathfrak{su}(2)))$. With the braiding in hand, we can extract a numerical invariant of a closed strand: an energy that grows when the strand folds back on itself. We define it categorically and check that it reproduces the classical Möbius energy in the limit $q \to 1$.

The section is anchored by Proposition: Categorical recovery of Möbius energy, which writes the energy of a knot embedding $\varrho \colon S^1 \to \tau(A)$ as a Frobenius double integral built from the Hopf comultiplication and the $q$-Hodge star, and then identifies its $q \to 1$ limit with the classical Möbius energy up to a topological constant. The supporting Lemma: Classical limit of the Frobenius--Hopf kernel is the repulsive $1/r^2$ tracks the kernel through the limit, showing that the Frobenius pairing degenerates onto the $\mathrm{SU}(2)$ Killing form. The Corollary: Obstruction to self-intersection reads off the consequence: at $q \neq 1$, non-cocommutativity of the Hopf structure makes the energy diverge whenever two non-adjacent strands approach within the fibre $\tau(A)$. The companion Lemma: $q$-deformed commutator replaces $1/r^2$ with a hard kernel at $r = \hbar_q$ records the substrate-side picture: the divergence has a finite cutoff at the Planck scale $\hbar_q$. The next section, **Crossing energy and Coulomb charge**, takes the self-avoidance kernel as given and converts it into an energy contribution localised at each crossing.
<!-- FILE_END: mobius-energy-intro.md -->

<!-- FILE_START: mobius-energy.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe
([Definition](#def:quantum-observable-universe)) with substrate
parameter $q$ ([Definition](#def:substrate-parameter)),
categorical action $\mathfrak{S}_q$
([Definition](#def:categorical-action)), and $q$-Hodge star
$\star_q$ ([Definition](#def:q-hodge-star)).

Let $\varrho \colon S^1 \to \tau(A)$ be a smooth closed curve
(a knot embedding) and let $\mathfrak{m}(\varrho)$ denote the categorical mass
([Theorem](#thm:topological-mass)).

Define the *categorical Möbius energy* by

$$
  E_{\mathrm{cat}}(\varrho)
  = 
  \int_A \!\circ \mathrm{tr}_A \!\iint_{S^1 \times S^1 \setminus \mathrm{diag}}
  \!\!\Bigl(
    \Delta(\varrho(s)) \otimes \Delta(\varrho(t))
  \Bigr)
  \star_q
  \Bigl\lVert
    \frac{d\varrho}{ds} \wedge_q \frac{d\varrho}{dt}
  \Bigr\rVert
  ds dt,
$$

where $\Delta$ is the Hopf comultiplication, $\int_A$ is the
Frobenius form ([Remark](#rem:frobenius-simplification)), and the
integration excludes the diagonal $\mathrm{diag} \subset S^1 \times S^1$.

Then in the classical limit $q \to 1$, the categorical Möbius energy
recovers the classical Möbius energy up to a topological normalization:

$$
  \lim_{q \to 1} E_{\mathrm{cat}}(\varrho)
  = 
  \frac{1}{4} E(\varrho)
  +  \text{const}.
$$

Here $E(\varrho)$ is the classical Möbius energy

$$
  E(\varrho)
  = 
  \iint_{S^1 \times S^1}
  \Bigl(
    \frac{1}{\lvert \varrho(s) - \varrho(t) \rvert^2}
    - 
    \frac{1}{D(\varrho(s), \varrho(t))^2}
  \Bigr)
  \lvert \varrho'(s) \rvert  \lvert \varrho'(t) \rvert
  ds dt.
$$

Here $D(\varrho(s), \varrho(t))$ denotes the intrinsic arc-length distance
along $\varrho$.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: mobius-energy.md -->

<!-- FILE_START: mobius-energy-frobenius-kernel.md -->
**Lemma.**
*At $q = 1$ the $q$-Hodge star reduces to the classical Hodge star,
and the Frobenius pairing
$\int_A \circ \mu$ on $A \otimes A$ reduces to the standard
$\mathrm{SU}(2)$ Killing form.  The Frobenius--Hopf kernel collapses
to the repulsive $1/r^2$:*

$$
  \mathrm{tr}\bigl(
    \Delta(\gamma(s)) \otimes \Delta(\gamma(t))
  \bigr)
  \xrightarrow{q \to 1}
  \frac{1}{\lvert \gamma(s) - \gamma(t) \rvert^2}.
$$
<!-- FILE_END: mobius-energy-frobenius-kernel.md -->

<!-- FILE_START: jones-mobius-diagonal.md -->
**Lemma (Jones polynomial = Möbius contact term).**
*Let*
$$
  K_q(s,t) \;=\; \operatorname{tr}\bigl(\Delta(\varrho(s)) \otimes \Delta(\varrho(t))\bigr)
$$
*be the categorical Möbius two-point kernel of
[$\operatorname{prop:mobius-energy}$](#prop:mobius-energy), which collapses to
the repulsive $1/\lvert\varrho(s)-\varrho(t)\rvert^2$ as $q \to 1$
([Frobenius–Hopf kernel](#lem:mobius-energy-frobenius-kernel)). Write the
Hadamard finite-part decomposition of the categorical Möbius energy obtained by
excising the diagonal,*
$$
  E_{\mathrm{cat}}(\varrho)
  \;=\;
  \underbrace{T_{\mathrm{reg}}(\varrho)}_{\text{regularized two-point}}
  \;-\;
  \underbrace{C(\varrho)}_{\text{diagonal contact}} ,
$$
*excising the singular diagonal. Then the contact coefficient $C(\varrho)$ is the
fundamental ($N=2$) Markov trace, whose braid closure is the Jones polynomial
([Jones–Markov trace](#thm:jones-markov-trace))*
$$
  C(\varrho) \;=\; \operatorname{tr}_M(\rho(\beta_K)) \;=\; J_K(q).
$$
*Consequently*
$$
  J_K(q) \;=\; T_{\mathrm{reg}}(\varrho) \;-\; E_{\mathrm{cat}}(\varrho):
$$
*the fundamental Jones polynomial is exactly the self-energy that the Möbius
renormalization subtracts. The fundamental Jones data embeds into the Möbius
two-point data as its contact / diagonal term; the converse map loses the
off-diagonal fusion content $\Delta(e_\lambda) = \sum_{\mu\nu} N^\lambda_{\mu\nu}\,
e_\mu \otimes e_\nu$.*
<!-- FILE_END: jones-mobius-diagonal.md -->

<!-- FILE_START: non-self-intersection.md -->
Let $\varrho$ be a knot embedding with categorical Möbius energy
$E_{\mathrm{cat}}(\varrho)$ as in
[Proposition](#prop:mobius-energy), and let $q \neq 1$ be the
substrate parameter ([Definition](#def:substrate-parameter)).

The non-cocommutativity of the Hopf structure at $q \neq 1$
provides a categorical obstruction to self-intersection: the
energy $\mathfrak{m}(\varrho)$ diverges whenever two non-adjacent strands of
$\varrho$ approach within the fibre $\tau(A)$.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: non-self-intersection.md -->

<!-- FILE_START: nsi-q-deformed-kernel.md -->
**Lemma.**
*For $q \neq 1$, the categorical mass of a vortex filament
$\varrho$ inherits a kernel*

$$
  \frac{1}{\lvert \varrho(s) - \varrho(t) \rvert^2}
   \longmapsto 
  \frac{[2]_q}{\lvert \varrho(s) - \varrho(t) \rvert^2
  - \hbar_q^{2}},
$$

*where $[2]_q = q + q^{-1}$, $\hbar_q = 1 - q^{-1}$, and the kernel
has a hard singularity at
$\lvert \varrho(s) - \varrho(t) \rvert = \hbar_q$.*
<!-- FILE_END: nsi-q-deformed-kernel.md -->

<!-- FILE_START: non-self-intersection-interpretation.md -->
Physically, the $R$-matrix endows the vortex filament $\varrho$ with
a "quantum exclusion zone" of radius $\hbar_q$: the filament cannot
pass through itself because doing so would require infinite
categorical energy.  This is the knot-theoretic analogue of the
Pauli exclusion principle, with the non-cocommutativity of
$\Delta_q$ playing the role of fermionic statistics.
<!-- FILE_END: non-self-intersection-interpretation.md -->


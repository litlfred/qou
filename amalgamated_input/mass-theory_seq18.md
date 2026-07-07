<!-- FILE_START: vertex-factorisation-intro.md -->
The exceptional divisor of the previous section carries a Reeb bundle and vertex operators, but we have not yet shown that this local structure is the unique source of all the operator content the chapter uses. We close that gap now. Every vertex operator factors through the exceptional divisor; the resulting factorisation matches the Markov trace term by term, and the two structures together identify a Feynman path integral with a categorical trace.

The section opens with Proposition: Vertex operators factor through the exceptional divisor, the structural pivot: a vertex operator $V$ acting on the categorical state space is the composition of restriction to $E_p$ with the Reeb-bundle action. The Remark: Breit--Wheeler vertex makes the photon-polarisation content visible — the two photon helicity states are Hecke generators on $E_p$ — and the companion literature alignment ties the picture to Bilson--Thompson preons and photonic hopfions. The Theorem: Product factorization of the Markov trace reads off the consequence on traces: $\mathrm{tr}_M(V_1 \cdots V_n)$ splits as a product over vertices, and Proposition: Hecke generator as stochastic transition operator interprets each Hecke generator as the transition operator of a Markov chain on partitions, with Remark: Knot operations on Young diagrams under the Markov chain and Remark: Error bounds for the Markov chain recording the moves and fluctuations on the partition side.

The Feynman block is the heart of the section. Lemma: Eigenbasis decomposition for the Feynman amplitude reduces the amplitude to a sum over the Schur--Weyl eigenbasis; Lemma: Markov-weighted eigenbasis sum equals the Markov trace identifies the resulting sum with $\mathrm{tr}_M$ on $H_n(q)$; Lemma: Feynman amplitude collapses to the Markov trace carries out the collapse; and Proposition: Feynman transition amplitude as categorical trace wraps the identification in QOU language. The dictionary Remark: Dictionary: Feynman path integral $\leftrightarrow$ QOU categorical trace writes out the correspondence in full, and Proposition: Classical limit: recovery of the symmetric path integral, together with its interpretation remark, closes the loop by showing that the $q \to 1$ degeneration recovers the ordinary path integral. The next section takes the categorical trace machinery as given and assembles it into a single operator on the brane-tower state space.
<!-- FILE_END: vertex-factorisation-intro.md -->

<!-- FILE_START: vertex-is-exceptional-divisor.md -->
Let $(\mathbf{C}, \varTheta, G, \mathcal{S})$ be a QOU with
exceptional divisor $\mathcal{S}_p = \pi^{-1}(p) \cong \mathbb{P}^1(\mathbb{C})$
at a brane point $p$
([exceptional divisor](#def:exceptional-divisor)), and let
$\mathcal{R}_p$ denote the Reeb bundle over $\mathcal{S}_p$
([Reeb bundle](#def:reeb-bundle)). Then:

1. **Localisation.** Every Hecke generator $\sigma_i \in H_n(R, q)$
 acting on $V^{\otimes n}$ factors through the fibre functor
 restricted to $\mathcal{S}_p$. That is, the vertex operator
 $\sigma_i \colon V^{\otimes n} \to V^{\otimes n}$ is supported on
 $\mathcal{S}_p$ and acts as the identity on the base algebra $A_0$.

2. **Confinement.** Every Skein resolution
 $L_+ - L_- = (q - q^{-1})L_0$ is evaluated within the Reeb
 bundle $\mathcal{R}_p = S^3 \xrightarrow{\pi_H} \mathcal{S}_p$. The
 braid word $\beta \in B_n$ representing the interaction is
 evaluated as a Markov trace in $H_n(R, q)$ over $\mathcal{R}_p$,
 and the result projects to $A_0$ via the blow-down map $\pi$.

3. **Completeness.** Every interaction that changes quantum numbers
 at $p$ --- crossing change, pair creation, virtual exchange ---
 is realised by a finite braid word in $B_n$ whose Hecke image
 $\rho(\beta) \in H_n(R, q)$ acts within $\mathcal{R}_p$. No
 interaction requires data from outside the blow-up at $p$.
<!-- FILE_END: vertex-is-exceptional-divisor.md -->

<!-- FILE_START: six-operators-via-vertex-factorisation.md -->
[Vertex operators factor through the exceptional divisor](#prop:vertex-is-exceptional-divisor)
asserts a general factorisation: every Hecke generator
$\sigma_i$ acting on the categorical state space is supported on
$\mathcal{S}_p$, and every braid word $\beta \in B_n$ has a
Markov-trace image inside the Reeb bundle $\mathcal{R}_p$.  The
*proof* is a structural statement about localisation; it does not
exhibit specific factorisations.  The
[six canonical knot operators](#prop:six-canonical-knot-operators)
proposition fills that gap: the six elements of $S_3$ — under the
projection $B_3 \to S_3$ — supply the **named geometric
instances** of the vertex-factorisation claim, each with a fully
explicit Reeb-flow trajectory and boundary permutation.

**One-to-one dictionary.**

See [Table](#tbl:six-operators-via-vertex-factorisation-table-data).

**Contribution to the rest of the section.**  The
Markov-trace-product theorem
([product factorization of the Markov trace](#thm:markov-trace-product))
that follows now has six concrete worked cases against which to
sanity-check.  In particular: the Markov trace of a 3-cycle is
the trace on a torus knot, which by
[torus-knot zero volume via Reeb](#rem:torus-knot-zero-volume-via-reeb)
contributes zero hyperbolic volume; the Markov trace of the
Garside element is the trace on a non-torus braid whose
complement has a hyperbolic JSJ piece, per
[hyperbolic-knot positive volume via Reeb](#rem:hyperbolic-knot-positive-volume-via-reeb).
The vertex-factorisation claim is therefore not just structural —
it specialises to a verifiable geometric dictionary on a generating
set for the $S_3$ image of $B_3$, and the rest of the chapter
inherits that dictionary as the bridge between the algebraic
Hecke action and the JSJ-graded volume content.

**Limits of the bridge.**  The dictionary above is genuinely
exhaustive only for $S_3$.  Longer braid words in $B_n$ for
$n \geq 4$ produce knot trajectories that the six $S_3$
representatives only approximate locally; the general
factorisation in
[vertex is the exceptional divisor](#prop:vertex-is-exceptional-divisor)
remains the working statement for those cases.  The six rows
above are the **base case** of an induction on braid-word
length, not a complete enumeration of braid trajectories.
<!-- FILE_END: six-operators-via-vertex-factorisation.md -->

<!-- FILE_START: breit-wheeler-vertex.md -->
The **Breit--Wheeler process** $\gamma\gamma \to e^-e^+$ is the
creation of an electron--positron pair from two real photons.
In the QOU the entire vertex is encoded in the Iwahori--Hecke algebra
$H_n(R, q)$ acting on the exceptional divisor
$\mathcal{S}_p \cong \mathbb{P}^1(\mathbb{C})$
([exceptional divisor](#def:exceptional-divisor)).

## Polarisation states as Hecke generators

The exceptional divisor $\mathcal{S}_p$ is the $\mathbb{P}^1(\mathbb{C})$
fibre of the state bundle $\mathcal{S}$ at a brane point $p$.  Its
homogeneous coordinates $[v_1 : v_2]$ parametrise the two
independent polarisation directions of a spin-$1$ field residing at
$p$.  The Reeb bundle $\mathcal{R}_p = (S^3 \xrightarrow{\pi_H} S^2,
\xi_q)$ ([Reeb bundle](#def:reeb-bundle)) is the Hopf fibration over
$\mathcal{S}_p$; its $U(1)$ holonomy $e^{2\pi i/[2]_q}$, with
$[2]_q = q + q^{-1}$, is the $q$-deformed phase acquired by a
photon completing one full rotation in the polarisation sphere.

The two Hecke generators act on $\mathcal{S}_p$ as follows:

| Generator | Coordinate patch | Polarisation mode | Eigenvalues of $\sigma_i$ |
|-----------|-----------------|-------------------|----------------------|
| $\sigma_0$ | $v_2 \neq 0$ (affine chart $z = v_1/v_2$) | horizontal ($\leftrightarrow$) | $+q$ (left), $-q^{-1}$ (right) |
| $\sigma_1$ | $v_1 \neq 0$ (affine chart $w = v_2/v_1$) | vertical ($\updownarrow$) | $+q$ (left), $-q^{-1}$ (right) |

The Hecke relation $(\sigma_i - q)(\sigma_i + q^{-1}) = 0$ is therefore the
**photon helicity equation**: its two roots $+q$ and $-q^{-1}$ are
the left- and right-circular polarisation eigenvalues.  A linearly
polarised photon is a superposition of these two eigenstates, with
the polarisation angle $\psi$ encoded in the ratio $v_1/v_2 \in
\mathcal{S}_p$.

## The pair-creation vertex

The two-photon state $\gamma_1 \otimes \gamma_2$ is a word in
$H_n(R, q)$.  Three cases arise depending on the relative polarisation:

**Same generator (parallel polarisation).**
$$
  \sigma_i \cdot \sigma_i
  =  (q - q^{-1})\sigma_i + \mathbf{1}.
$$
The Hecke relation reduces the word to a dressed photon plus the
vacuum $\mathbf{1}$ (neutrino).  No pair is created: the energy
$2E_\gamma$ does not exceed the pair threshold because the two
photons share the same polarisation degree of freedom and their
net helicity vanishes only modulo the Hecke reduction, leaving
a lower-energy residue.

**Orthogonal generators (perpendicular polarisation).**
$$
  \sigma_0 \cdot \sigma_1 =  L_+
  \qquad (\text{Hopf link intermediate state}).
$$
The product is already irreducible: it is the normal-form basis
element $L_+$ (Hopf link), a two-strand entangled state.  Applying
one further $\sigma_0$ from the substrate (the Reeb direction) completes
the trefoil:
$$
  L_+ \cdot \sigma_0
  =  \sigma_0\sigma_1\sigma_0
  =  e^-.
$$
The positron $e^+$ is supplied by the mirror process
$\sigma_0^{-1}\sigma_1^{-1}\sigma_0^{-1}$ (all crossing signs
reversed, [antiparticle crossing reversal](#prop:antiparticle-crossing-reversal)).

The complete vertex is therefore:
$$
  \underbrace{\sigma_0}_{\gamma_1, \mathrm{horiz.}}
   \cdot 
  \underbrace{\sigma_1}_{\gamma_2, \mathrm{vert.}}
  \xrightarrow{\xi_q\text{-insertion}}
  \underbrace{\sigma_0\sigma_1\sigma_0}_{e^-}
  + 
  \underbrace{(\sigma_0\sigma_1\sigma_0)^\sigma}_{e^+}.
$$

The $\xi_q$-insertion is the action of the Reeb vector field
$\xi_q$ on the Reeb bundle $\mathcal{R}_p$: it supplies the third
crossing $\sigma_0$ from the contact structure of $S^3$, at a cost
of one unit of Reeb charge $1/[2]_q$.

## Polarisation selection rule

The vertex vanishes unless the two photons occupy **distinct**
polarisation patches of $\mathbb{P}^1(\mathbb{C})$.  Writing
$v_{e^-e^+} = (\sigma_0\sigma_1\sigma_0)\,(\sigma_0\sigma_1\sigma_0)^\sigma$
for the pair class and $\langle \cdot, \cdot \rangle_F$ for the
Frobenius pairing on $H_n(R, q)$:

$$
  \langle v_{e^-e^+}, \sigma_i\sigma_i \rangle_F =  0,
  \qquad
  \langle v_{e^-e^+}, \sigma_0\sigma_1 \rangle_F  \neq  0.
$$

This is the topological origin of the Breit--Wheeler polarisation
selection rule: parallel-polarised photons apply the Hecke
relation and return lower-energy states; only orthogonally
polarised photons produce the Hopf-link intermediate $L_+$ that
the substrate can complete into the $e^-e^+$ trefoil pair.
<!-- FILE_END: breit-wheeler-vertex.md -->

<!-- FILE_START: breit-wheeler-vertex-literature.md -->
The identification of $\sigma_0\sigma_1$ as the Hopf-link intermediate
that opens the trefoil channel ([Breit--Wheeler vertex](#rem:breit-wheeler-vertex))
places the QOU framework in direct contact with three established
strands of the literature on knotted matter and topological photonics.

## Braid--preon mapping (Bilson--Thompson)

The Bilson--Thompson topological preon model
\cite{bilsonthompson2005,bilsonthompson2007} maps Standard-Model
fermions to framed braids in $B_3$, with chirality (left- vs
The right-handed states) determined by the sign pattern of the crossings.
The $e^-/e^+$ pair in the QOU vertex
$$
  \sigma_0\sigma_1\sigma_0
  \quad\text{vs.}\quad
  \sigma_0^{-1}\sigma_1^{-1}\sigma_0^{-1}
$$
is the same construction: a three-strand braid whose chirality is
fixed by the global sign of the Hecke generators. The QOU
contribution is to identify $\sigma_0\sigma_1$ — and not the
individual generator $\sigma_0$ or $\sigma_1$ — as the topological
seed that breaks the parity-symmetric photon vacuum into the chiral
trefoil channel.

## Hecke asymmetry as topological parity violation

The Hecke deformation $q \neq q^{-1}$ asymmetrises over- and
under-crossings; this is the standard mechanism by which Iwahori--Hecke
representations of the braid group generate parity-violating anyon
statistics \cite{kauffman1991}. In the QOU Breit--Wheeler vertex the
two roots $+q,\,-q^{-1}$ of $(\sigma_i - q)(\sigma_i + q^{-1}) = 0$
are exactly the left- and right-circular polarisation eigenvalues, so
the Hecke relation _is_ the photon helicity equation. The same
algebraic asymmetry that drives anyonic parity violation drives the
left/right helicity splitting on the exceptional divisor
$\mathcal{S}_p \cong \mathbb{P}^1(\mathbb{C})$.

## Photonic hopfions

Recent experiments in structured light have realised three-dimensional
topological solitons of polarisation whose configuration maps to the
Hopf fibration \cite{sugic2021}. The topological charge (Hopf index)
of such a soliton _is_ its helicity. The QOU presentation of $L_+$
and $L_-$ as the positive and negative Hopf links generated by
$\sigma_0\sigma_1$ is the categorical analogue of these laboratory
photonic hopfions: in both settings the knot/link type is not a
secondary label on a separately defined helicity but the topological
object whose two oriented presentations _are_ the two helicity
states.

## Summary

The QOU Breit--Wheeler vertex bridges the braid--preon mapping of
\cite{bilsonthompson2005,bilsonthompson2007} with the Hecke-algebraic chirality of
\cite{kauffman1991} and the experimental photonic-hopfion programme of
\cite{sugic2021}: the coefficient of $\sigma_0\sigma_1$ in the
photon expansion is the topological switch that takes the parity-symmetric
vacuum into the chiral trefoil sector, and this switch is the same one
realised, at three different levels of abstraction, in all three lines
of work cited above.
<!-- FILE_END: breit-wheeler-vertex-literature.md -->

<!-- FILE_START: markov-trace-product.md -->
Let $\beta \in B_n$ be a braid on $n$ strands and let
$\rho(\beta) \in H_n(R, q)$ be its image under the Hecke quotient
([Jones--Markov trace](#thm:jones-markov-trace)).  After Hecke
reduction, the element $\rho(\beta)$ decomposes as a product of
**generator chains**: for each generator $\sigma_i$
($i = 0, \ldots, n-2$), the crossings at $\sigma_i$ reduce to a
linear combination $a_i \sigma_i + b_i$ with
$a_i, b_i \in \mathbb{Z}[q^{\pm 1}]$.

**Theorem.**  The Markov trace factors as a product over generators:

$$
  \mathrm{tr}_M\!\bigl(\rho(\beta)\bigr)
  = 
  \prod_{i=0}^{n-2} \hat{V}_i(q),
  \qquad
  \hat{V}_i(q) =  z \cdot a_i + b_i,
$$

where $z = 1/(q^{1/2} + q^{-1/2})$ is the Markov trace parameter.
Each $\hat{V}_i$ is the **vertex volume** at generator $\sigma_i$
--- the evaluation of the vertex operator $Y(\sigma_i, z_i)$ at
the $i$-th insertion point on the exceptional divisor
([vertex operator](#def:vertex-operator)).
<!-- FILE_END: markov-trace-product.md -->

<!-- FILE_START: markov-trace-product-interpretation.md -->
In the VOA formalism ([vertex operator](#def:vertex-operator)),
each vertex volume $\hat{V}_i$ is the **correlation function** of a
single vertex operator insertion:

$$
  \hat{V}_i(q) = 
  \bigl\langle Y(\sigma_i, z_i) \bigr\rangle_{\mathrm{Markov}}.
$$

The product formula is the **factorization of the $n$-point
correlation function** into one-point functions:

$$
  \bigl\langle Y(\sigma_0, z_0) \cdots Y(\sigma_{n-2}, z_{n-2})
  \bigr\rangle
  = 
  \prod_{i=0}^{n-2}
  \bigl\langle Y(\sigma_i, z_i) \bigr\rangle.
$$

This factorization is **not** an approximation --- it is an exact
consequence of the Markov property, which is the state-operator
correspondence of the VOA.  Each generator acts at a distinct
insertion point on $\mathcal{S}_p$, and the Markov property ensures that the
insertions are independent (they are at distinct points on
$\mathbb{P}^1(\mathbb{C})$, so their OPE is non-singular).

The degree bound $\deg P_\beta \leq n^2 - 1$ follows from the
conformal weight: each vertex volume has conformal weight
$\leq 2k_i + 1$ (where $k_i$ is the number of crossings at
$\sigma_i$), and the total conformal weight of the product is
bounded by $\sum_i (2k_i + 1) \leq (n-1)(n+1) = n^2 - 1$.

## The chain of invariant-preserving maps

$$
  \mathbb{Z}[B_n]
  \xrightarrow{\text{Hecke quotient}}
  H_n(R, q)
  \xrightarrow{\text{chain reduction}}
  \prod_{i} (a_i \sigma_i + b_i)
  \xrightarrow{\text{Markov trace}}
  \prod_{i} \hat{V}_i(q)
  = 
  P_\beta(q)
$$

Each step preserves the link invariant.  The polynomial
$P_\beta(q)$ is a well-defined invariant of the link
$\hat{\beta}$ --- it does not depend on the braid representative
or the reduction path.
<!-- FILE_END: markov-trace-product-interpretation.md -->

<!-- FILE_START: hecke-markov-transition.md -->
The algebraic machinery of the Hecke algebra $H_n(R, q)$ and the
Jones--Markov trace
([Jones--Markov trace](#thm:jones-markov-trace)) has a direct
probabilistic interpretation: **each Hecke generator $\sigma_i$ is a
stochastic transition operator**, and the product factorization
$\prod_i \hat{V}_i$
([product factorization](#thm:markov-trace-product)) is the
product of independent one-step expectations along a Markov chain.

## Statement

**Proposition.**
*Let $H_n(R, q)$ be the Iwahori--Hecke algebra with generators
$\sigma_1, \ldots, \sigma_{n-1}$ satisfying $(\sigma_i - q)(\sigma_i + q^{-1}) = 0$
([Hecke relation](#rem:hecke-algebra-from-braiding)).*

**(i) Spectral idempotents.**
*The orthogonal idempotents*

$$
  e_+^{(i)} = \frac{\sigma_i + q^{-1}}{q + q^{-1}},
  \qquad
  e_-^{(i)} = \frac{q - \sigma_i}{q + q^{-1}}
$$

*satisfy $e_+^{(i)} + e_-^{(i)} = 1$,
$(e_\pm^{(i)})^2 = e_\pm^{(i)}$,
$e_+^{(i)} e_-^{(i)} = 0$, and reconstruct the generator as
$\sigma_i = q \cdot e_+^{(i)} - q^{-1} \cdot e_-^{(i)}$.*

**(ii) Transition probabilities.**
*Define the symmetric and antisymmetric transition probabilities:*

$$
  p_+ = \frac{q}{q + q^{-1}} = \frac{q^2}{q^2 + 1},
  \qquad
  p_- = \frac{q^{-1}}{q + q^{-1}} = \frac{1}{q^2 + 1}.
$$

*Then $p_+ + p_- = 1$ and $p_+/p_- = q^2$.  The stochastic
transition operator at generator $i$ is*

$$
  K_i = p_+ \cdot \mathrm{id} + p_- \cdot s_i,
$$

*where $s_i$ is the adjacent transposition.  In the defining
representation on $\mathbb{C}[S_n]$, $K_i$ is a row-stochastic
matrix: at each crossing, the system stays in its current
configuration with probability $p_+$ or transposes the adjacent
pair with probability $p_-$.*

**(iii) Markov property as memorylessness.**
*The Markov trace property
$\mathrm{tr}_M(x \sigma_n^{\pm 1}) = z^{\pm 1}\mathrm{tr}_M(x)$
is equivalent to the statement that the transition at generator
$n$ depends only on the eigenvalue structure of $\sigma_n$, not on the
history $x \in H_{n-1}(q)$.  The expectation value of the $i$-th
crossing under $\mathrm{tr}_M$ is:*

$$
  \mathbb{E}[\hat{V}_i]
  = \mathrm{tr}_M(a_i \sigma_i + b_i)
  = z \cdot a_i + b_i
  = \hat{V}_i,
$$

*recovering the vertex volume
([product factorization](#thm:markov-trace-product)) as the
one-step conditional expectation.*

**(iv) Independence and factorization.**
*The product formula $\mathrm{tr}_M(\rho(\beta)) = \prod_i \hat{V}_i$
is the product of independent one-step expectations: each vertex
volume $\hat{V}_i$ is determined by the local crossing data
$(a_i, b_i)$ at generator $\sigma_i$, with no dependence on the
crossings at other generators.  This is a direct consequence of
memorylessness (iii).*

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: hecke-markov-transition.md -->

<!-- FILE_START: hecke-markov-interpretation.md -->
Every algebraic construction in the preceding sections has a
Markov chain counterpart
([Hecke transition operator](#prop:hecke-markov-transition)).
The two descriptions are the same mathematical object
viewed through different lenses: the Hecke algebra $H_n(R, q)$
is simultaneously an algebra of braid-group representations
and a space of stochastic transition operators.

## Overview: SYT paths on the Young graph

Fix an irrep $\lambda \vdash n$.  In the Hoefsmit seminormal
form ([Hoefsmit seminormal form](#prop:hoefsmit-seminormal-form)),
the irrep $\rho_\lambda \colon H_n(R, q) \to M_{d_\lambda}(R)$
is built on the basis of **standard Young tableaux** of shape
$\lambda$.  Each such tableau is a saturated chain

$$
  \varnothing = \lambda^{(0)} \nearrow \lambda^{(1)} \nearrow \cdots
    \nearrow \lambda^{(n)} = \lambda
$$

in the **Young graph** (Young lattice), where each step
$\lambda^{(k-1)} \nearrow \lambda^{(k)}$ adds a single box.
The space of all valid SYTs is therefore the space of all
length-$n$ paths from the empty diagram $\varnothing$ to
$\lambda$ on the Young graph, and it is this path space that
plays the role of the **discrete state space** of the chain.

The generator $\sigma_i \in B_n$ acts at step $i$ via the
Hecke-algebra image $\rho_\lambda(\sigma_i)$ (the same symbol
$\sigma_i$ is used for both the braid generator in $B_n$ and
its image in $H_n(R, q)$; context disambiguates), whose
matrix entries in the tableau basis are

$$
  \rho^\lambda_q(\sigma_i)_{T, T'}
  =
  \begin{cases}
    a_{\rho_i}(q) & T' = T, \\
    b(\rho_i, q) & T' = s_i \cdot T, \\
    0 & \text{otherwise},
  \end{cases}
  \qquad
  a_\rho(q) = \frac{q - q^{-1}}{1 - q^{-2\rho}},
  \quad
  b(\rho, q) = \sqrt{a_\rho(q)\,a_{-\rho}(q) + 1},
$$

where $\rho_i = c_T(i{+}1) - c_T(i)$ is the axial distance
between the cells carrying $i$ and $i{+}1$ in $T$
([Hoefsmit seminormal form](#prop:hoefsmit-seminormal-form)).
Every non-zero entry is an **explicit rational / radical
function of $q$**: this is a genuine quantum deformation of the
classical Young seminormal form, which is recovered at $q = 1$
by l'H\^{o}pital ($a_\rho(1) = 1/\rho$).  Because of this
$q$-deformation, the matrix $\rho^\lambda_q(\sigma_i)$ does
**not** contain classical probabilities: its entries are real
but can be negative, and they square to weights that sum to one
only after a Markov trace.  In the physicists' sense,
$\rho^\lambda_q(\sigma_i)$ is a matrix of **probability
amplitudes**, with $q$ playing the role of the deformation
parameter that distinguishes amplitudes from probabilities.

Two compatible pictures coexist on the same algebra:

1. **Amplitude picture.** On the SYT path space of irrep
   $\lambda$, amplitudes $\rho^\lambda(\sigma_i)_{T, T'}$
   evolve a complex state vector $\psi(T)$.  The Jones
   polynomial
   $J_L(q) = \mathrm{tr}_M(\rho(\beta_L))$
   ([Jones--Markov trace](#thm:jones-markov-trace)) is the
   closed-path sum of these amplitudes over all SYT paths,
   weighted by the Markov trace weights $w_\lambda$ — exactly
   the shape of a Feynman path integral.

2. **Probability picture.** Summing the amplitudes through
   the spectral idempotents
   $e_\pm^{(i)} = (\sigma_i + q^{-1})/(q + q^{-1})$,
   $(q - \sigma_i)/(q + q^{-1})$
   ([Hecke transition operator](#prop:hecke-markov-transition))
   yields the classical stochastic operator
   $K_i = p_+ \cdot \mathrm{id} + p_- \cdot s_i$ with
   $p_\pm = q^{\pm 1}/(q + q^{-1})$.  This $K_i$ is the
   row-stochastic Markov kernel targeting the Mallows
   measure \cite{diaconis-ram2000}.

The two pictures are related by the quadratic Hecke relation
$(\sigma_i - q)(\sigma_i + q^{-1}) = 0$: the amplitudes living on SYT
edges square, via the idempotents, to the symmetric /
antisymmetric Boltzmann weights of the classical chain.  SYT
paths on the Young graph are therefore the **quantum sample
space**, and the Markov chain of §2 is its classical shadow.

### Jucys--Murphy / SYT cell reindexing

In the same SYT basis, the Jucys--Murphy elements
$L_k = \sigma_{k-1}\cdots \sigma_1 \sigma_1 \cdots \sigma_{k-1}$ act diagonally
with eigenvalue $q^{2 c_T(k)}$, where $c_T(k)$ is the content
of the cell added at step $k$ of the tableau.  Because
$[L_i, L_j] = 0$, pairs of SYT cells are on equal footing with
no adjacent/far distinction; this is the representation-
theoretic origin of the uniform all-pairs coupling seen in the
mass-tower empirical probes on the
`claude/fix-partitions-shell-operator-TFznx` branch (see the
SYT/Jucys--Murphy reindexing of the mass-tower pair set
developed there).  The amplitude-to-probability passage above
is therefore also a passage from the **generator indexing** of
the chain to the **cell indexing** of the Young graph paths.

## Dictionary

See [Table](#tbl:hecke-markov-interpretation-table-data).

## Non-local correlations from local transitions

The memorylessness condition (iii) coexists with non-trivial
correlations.  In the Markov chain, each step depends only on
the current state, not the history.  Yet the braid relations
$\sigma_i \sigma_{i+1} \sigma_i = \sigma_{i+1} \sigma_i \sigma_{i+1}$ impose
**correlations between non-adjacent generators**: the outcome
at crossing $i$ constrains the outcomes at crossings $i \pm 1$
through the Yang--Baxter equation.

Correlations between distant crossings arise from the
algebraic structure of $H_n(R, q)$ --- the braid relations and
their representation theory --- not from step-to-step memory.
Each crossing is a **local, memoryless transition** whose
outcome is determined by the eigenvalue structure
$p_+, p_-$ alone.  The non-local correlations are
representation-theoretic: they are consequences of the
constraints that $H_n(R, q)$ imposes on any consistent
assignment of transition probabilities.

## Planck steps

Each step of the Markov chain is one Hecke evaluation --- one
braid crossing resolved into its symmetric or antisymmetric
channel.  In the Reeb flow picture
([information-theoretic time](#def:information-theoretic-time)),
this is one iteration of $f_q$ on the exceptional divisor,
i.e.\ one **Planck step**.

The per-step Shannon entropy $H(p_+, p_-)$ is bounded above
by $\ln 2$ (the fair-coin maximum at $q = 1$) and bounded
below by $0$ (the deterministic limit $q \to \infty$).  For
any $q > 1$, $p_+ > p_-$ and the entropy is strictly less than
$\ln 2$: the $q$-deformation away from the fair coin reduces
the information content per crossing.

## ASEP as the continuous-time limit

In the continuous-time limit, the Markov chain becomes the
**asymmetric simple exclusion process** (ASEP) with hopping
asymmetry $q$.  Bufetov \cite{bufetov2020} showed that the
ASEP generator is a sum of Hecke algebra elements:

$$
  \mathcal{L}_{\mathrm{ASEP}}
  =
  \sum_{i=1}^{n-1}
  \bigl(
    p_+ \cdot e_+^{(i)} + p_- \cdot e_-^{(i)} \cdot s_i
  \bigr),
$$

which is the generator built from the transition operators
$K_i$
([Hecke transition operator](#prop:hecke-markov-transition)).
The ASEP is integrable because it inherits the algebraic
structure of $H_n(R, q)$ and its quotient, the Temperley--Lieb
algebra.  The stationary distribution is the Mallows measure
$\pi(\sigma) \propto q^{\mathrm{inv}(\sigma)}$ --- the unique
probability measure on $S_n$ that weights each permutation
by $q$ raised to its number of inversions
\cite{diaconis-ram2000}.

## Corollaries

The product factorization
([product factorization](#thm:markov-trace-product)) is exact
because the crossings are independent (memoryless).  The Jones
polynomial is a link invariant because it is the partition
function of a well-defined stochastic process.  The transfer
matrix eigenvalues are $q$ and $-q^{-1}$ because these are
the Boltzmann weights of the two channels.

In the language of Diaconis--Ram \cite{diaconis-ram2000}, the
nuclear physics of the QOU is a systematic-scan Metropolis
algorithm on $S_n$: $n$ is the number of strands in the
nuclear braid word, $q$ is the substrate parameter, and the
target distribution is the Mallows measure
$\pi(\sigma) \propto q^{\mathrm{inv}(\sigma)}$.  Physical
observables --- mass, binding energy, decay rates --- are
expectations under this measure, computed via the Markov trace.
<!-- FILE_END: hecke-markov-interpretation.md -->

<!-- FILE_START: markov-lambda-knot-operations.md -->
> **SUPERSEDED-$\rho_q$ note .** Any use of the
> scalar substrate density $\rho_q = 1/\hbar_q^2$ in this block is the
> structurally-wrong leading-order ansatz per
> [`mass-endomorphism-tower.md` §SUPERSEDED](mass-endomorphism-tower.md);
> the canonical replacement is the operator-valued $A^\lambda_{\mu, \nu}(I)$
> graded expansion [`prop:rho-k-graded-expansion`](rho-k-graded-expansion.md).
> Full purge tracking: [`docs/audits/-superseded-rho-q-purge.md`](../../../docs/audits/-superseded-rho-q-purge.md).

The Markov chain
([Hecke transition operator](#prop:hecke-markov-transition)),
the knot-theoretic operations on a closed braid, and the
partition $\lambda \vdash n$ labelling an irrep of $H_n(R, q)$
are tied together by three explicit structural statements.
This remark records the three ties and the traffic between
$\lambda$-preserving and $\lambda$-changing moves.

## 1. $\lambda$-block decomposition (Wedderburn)

Semisimplicity of $H_n(R, q)$ (generic $q$) gives a decomposition

$$
  H_n(R, q)
  \;\cong\;
  \bigoplus_{\lambda \vdash n}
    \mathrm{End}_R(V_\lambda),
  \qquad
  \dim V_\lambda = d_\lambda = |\mathrm{SYT}(\lambda)|,
$$

The amplitude matrix of any braid $\beta \in B_n$ splits

$$
  \rho_q(\beta)
  \;=\;
  \bigoplus_{\lambda \vdash n} \rho^\lambda_q(\beta).
$$

**Consequence for the Markov chain.** Each $\lambda$ is a closed
sector with its own discrete state space $\mathrm{SYT}(\lambda)$
([SYT paths on the Young graph](#rem:hecke-markov-interpretation)).
Hecke-generator amplitudes
$\rho^\lambda_q(\sigma_i)$ never mix irreps: the chain on the
union of SYTs (over all shapes $\lambda \vdash n$) is a direct
sum of independent $\lambda$-chains.

## 2. Knot operations split into $\lambda$-preserving and $\lambda$-changing

The knot-theoretic operations on a closed braid are
**Reidemeister moves** and the equivalent **Markov moves** on
braids.  Each has a determinate action on $\lambda$:

| Operation | Algebraic form | Effect on $\lambda$ | Effect on the chain |
|:----------|:---------------|:-------------------|:--------------------|
| Braid relation (Reidemeister III) | $\sigma_i \sigma_{i+1} \sigma_i = \sigma_{i+1} \sigma_i \sigma_{i+1}$ | **fixes** $\lambda$ | Yang--Baxter inside one $\rho^\lambda_q$ block |
| Hecke quadratic (Reidemeister II) | $\sigma_i^2 = (q - q^{-1})\sigma_i + 1$ | **fixes** $\lambda$ | Two-channel skein: symmetric $q$ / antisymmetric $-q^{-1}$ eigenspace in $V_\lambda$ |
| Markov I --- conjugation | $\beta \mapsto \alpha \beta \alpha^{-1}$, $\alpha,\beta \in B_n$ | **fixes** every $\chi^\lambda_q$ | Class-function property of the trace; trajectory distribution unchanged |
| **Markov II** --- stabilization | $\beta \in B_n \mapsto \beta \sigma_n^{\pm 1} \in B_{n+1}$ | $\lambda \vdash n \;\to\; \mu \vdash n{+}1,\ \mu = \lambda + \square$ | **Young-graph edge**; trace weight rescales by $z^{\pm 1}$ |
| Reidemeister I (framing) | $\beta \mapsto \beta \sigma_n^{\pm 1}$ with framing compensation | $\lambda \nearrow \mu$ same as Markov II | Absorbed into stabilization with framing factor |

The point is the sharp dichotomy: **only Markov II crosses
$\lambda$-sectors**, and it does so exactly along **box-addition
edges of the Young graph**

$$
  \lambda \nearrow \mu
  \quad\Longleftrightarrow\quad
  \mu \setminus \lambda = \{\square\}.
$$

All other knot operations act inside a single irrep block.

### Markov II as a transition on the Young lattice

Stabilization therefore is **not** a step of the
within-$\lambda$ SYT chain; it is a step of a **second,
coarser Markov chain on partitions**:

$$
  \cdots \;\longrightarrow\;
  \lambda \vdash n
  \;\xrightarrow{\;z^{\pm 1}\;}\;
  \mu \vdash n{+}1
  \;\longrightarrow\; \cdots,
  \qquad
  \mu \supset \lambda,\ |\mu| = |\lambda| + 1.
$$

The transition rate along edge $\lambda \nearrow \mu$ is
proportional to the Ocneanu trace weight ratio
$w_\mu(q)/w_\lambda(q)$; at generic $q$ this is the
**$q$-Plancherel measure** on the Young lattice, matching the
growth process familiar from the Robinson--Schensted--Knuth
correspondence and the asymmetric simple exclusion process
\cite{diaconis-ram2000}.

## 3. Jones polynomial = Plancherel sum over $\lambda$

The factorisation of the Jones polynomial through irreps is

```tex
\begin{equation}\label{eq:jones-plancherel}
  J_L(q)
  \;=\;
  \mathrm{tr}_M\bigl(\rho_q(\beta_L)\bigr)
  \;=\;
  \sum_{\lambda \vdash n}
    w_\lambda(q) \,\chi^\lambda_q\bigl(\rho(\beta_L)\bigr),
\end{equation}
```

where $w_\lambda(q)$ is the Ocneanu weight
([Jones--Markov trace](#thm:jones-markov-trace)) and
$\chi^\lambda_q(\rho(\beta_L)) = \mathrm{tr}\,\rho^\lambda_q(\beta_L)$
is the irreducible $q$-character of the closed braid in the
$\lambda$-block.

In the Markov-chain language this is an explicit
**classical/quantum factorisation**:

- **Classical layer.**  The normalised weights
  $\pi_\lambda(q) = w_\lambda(q) / \sum_\mu w_\mu(q)$ form a
  probability measure on partitions $\lambda \vdash n$.  Markov
  II moves a sample along the Young graph according to this
  measure.
- **Quantum layer.**  Inside each sector, the character
  $\chi^\lambda_q(\rho(\beta_L))$ is a closed-path amplitude
  sum over $\mathrm{SYT}(\lambda)$ with matrix elements given
  by Hoefsmit seminormal form
  ([Hoefsmit seminormal form](#prop:hoefsmit-seminormal-form)).
  The chain here is an amplitude walk in $V_\lambda$, with
  entries that are rational functions of $q$ and can be
  negative.

The Jones polynomial is therefore the expectation of a
quantum-amplitude observable under a classical probability on
$\lambda$.  This is the precise sense in which
$\lambda$ is the **classical label** of the knot-theoretic
process and SYT paths are its **quantum trajectories**.

## Summary

- **Block-diagonality.**  Hecke generators act within a single
  $\lambda$-sector; the chain decomposes as
  $\bigoplus_\lambda$ independent SYT-chains.
- **Knot ops respect the blocks.**  Braid relations, Hecke
  quadratic, Reidemeister II/III, and Markov I all fix $\lambda$;
  only Markov II (stabilization) changes $\lambda$, and it does
  so by a single box addition --- a Young-graph edge.
- **Jones = Plancherel.**  The Jones polynomial is a sum over
  $\lambda$ of Ocneanu-weighted $q$-characters, exhibiting the
  classical-probability ($\lambda$) / quantum-amplitude (SYT)
  split at the level of the full link invariant.
<!-- FILE_END: markov-lambda-knot-operations.md -->

<!-- FILE_START: markov-chain-fluctuations.md -->
The two-chain decomposition
([knot operations and $\lambda$](#rem:markov-lambda-knot-operations))
--- an outer chain on partitions (stabilization / Markov II) and
an inner chain on SYTs (generators $\sigma_i$ inside $V_\lambda$) ---
has quantitative error bounds already established elsewhere in
the paper.  This remark matches each chain layer to its
controlling bound and flags a standard CLT framework that
**fails** in this paper's regime.

## Outer chain: $q$-Plancherel CLT (Féray--Méliot)

The outer chain samples $\lambda \vdash n$ under the normalised
Ocneanu weights $\pi_\lambda(q)$, which at generic $q$ are the
$q$-Plancherel measure on the Young lattice.  Fluctuations of
the jet-filtered invariant $a_k(\beta) \to a_\infty(\beta)$
around the dimension-weighted average are controlled by the
Féray--Méliot $q$-Plancherel CLT \cite{feray-meliot2012}:

$$
  \bigl\lvert a_k(\beta) - a_\infty(\beta) \bigr\rvert
  \;=\; O\!\bigl(k^{-1/2}\bigr),
$$

with explicit constants worked out in
[jet convergence](#conj:jet-convergence-classical-limit).
This is the standard Gaussian CLT rate transported to the
$q$-deformed Plancherel measure.

## Inner chain: Perron--Frobenius, not Bożejko--Speicher

The inner chain on $\mathrm{SYT}(\lambda)$ is the natural venue
for a $q$-Gaussian CLT in the sense of Bożejko--Speicher, since
the generators satisfy the $q$-commutation $\sigma_i \sigma_{i+1} \sigma_i =
\sigma_{i+1} \sigma_i \sigma_{i+1}$ with Hecke quadratic $(\sigma_i - q)(\sigma_i + q^{-1})
= 0$.  However, the Bożejko--Speicher noncommutative $q$-Gaussian
**does not apply** at the substrate value $q_0 \approx 1.11 > 1$:
the Touchard pair-partition moments
$T_n(q_0) = \sum_\pi q_0^{\mathrm{cr}(\pi)}$ grow super-exponentially
in $n$, so no well-defined $q$-Gaussian distribution exists.
This failure is documented in the computation layer
(the formal derivation), which selects the
**Perron--Frobenius dominant eigenvalue** proxy instead:

$$
  \log\bigl\lvert \mathrm{tr}\,\rho^\lambda_q(W_N) \bigr\rvert
  \;\approx\;
  \log d_q(\lambda) \,+\, N \cdot \log\lvert \mu_\lambda \rvert,
$$

where $\mu_\lambda$ is the spectral radius of a typical crossing
$c \sigma + d \cdot I$ in the $\lambda$-irrep.  This estimate is
valid for every $q > 0$ (pure Perron--Frobenius for positive
operators), with the rate controlled by the spectral gap
$\mu_\lambda - \mu_\lambda^{(2)}$ and exponential in $N$.

## Operational layer: geometric rate on physical predictions

The composite of outer and inner chains feeds into the
Wedderburn mass formula, whose empirical error on stable nuclei
satisfies

$$
  \frac{\bigl\lvert M_k(Z, N) - M_{\mathrm{obs}}(Z, N) \bigr\rvert}
       {M_{\mathrm{obs}}(Z, N)}
  \;\leq\; C \cdot r^{-(k-3)},
  \qquad C \approx 0.001,\ r \approx 4
$$

([Hecke convergence bound](#prop:hecke-convergence-bound)).
This geometric rate is faster than either layer in isolation and
reflects cancellation between inner and outer fluctuations in
the trace pairing; one Hecke level $\approx$ one QCD loop order.

## Summary

| Layer | Observable | Controlling bound | Rate |
|:---|:---|:---|:---|
| Outer ($\lambda \vdash n$) | $a_k \to a_\infty$ | Féray--Méliot $q$-Plancherel CLT | $O(k^{-1/2})$ |
| Inner ($\mathrm{SYT}(\lambda)$) | $\log\lvert\mathrm{tr}\,\rho^\lambda_q(W_N)\rvert$ | Perron--Frobenius spectral radius | $O(\mu_\lambda^{-N})$ remainder |
| Operational | $\lvert M_k - M_{\mathrm{obs}}\rvert/M_{\mathrm{obs}}$ | Wedderburn mass-formula error | $C \cdot r^{-(k-3)}$ |

**Caveat.** The natural candidate for an inner-chain CLT --- the
Bożejko--Speicher $q$-Gaussian --- **is not usable at $q_0 > 1$**.
Any approach that invokes a "$q$-Gaussian limit" for braid-word
observables at the physical substrate value is mis-applying the
framework.  The correct substitute is the Perron--Frobenius
dominant-eigenvalue estimate above.
<!-- FILE_END: markov-chain-fluctuations.md -->

<!-- FILE_START: q-gaussian-obstruction-at-q0.md -->
**Proposition (q-Gaussian obstruction at the substrate value).** *At the
substrate parameter $q_0 \approx 1.10998 > 1$, the Bożejko–Speicher
non-commutative $q$-Gaussian does not exist as a probability measure.
As a quantitative witness, the would-be even moments*
$$
  T_n(q_0) \;=\; \sum_{\pi \in \mathcal{P}_2(2n)} q_0^{\,\mathrm{cr}(\pi)}
$$
*(the sum over perfect matchings $\pi$ of $[2n]$, weighted by crossing number
$\mathrm{cr}(\pi)$) diverge super-exponentially in $n$.*
## Corollary

Braid-word fluctuation statistics at $q_0$ **cannot** be modelled by the BS
$q$-Gaussian. The convergent substitutes are the *inner* Perron–Frobenius
dominant eigenvalue (a deterministic law-of-large-numbers limit) and the
*outer* Féray–Méliot $q$-Plancherel CLT (a genuine Gaussian-fluctuation limit
on the partition chain). This is the rigorous backing for the framing in
[`rem:markov-chain-fluctuations`](#rem:markov-chain-fluctuations): any
"$q$-Gaussian limit" invoked for braid observables at $q_0$ is mis-applying
the $|q| \le 1$ Bożejko–Speicher theory.

## Lean formalization

The companion Lean `qGaussianObstructionAtQ0` states the obstruction and defers its proof via `sorry` (`-- Ref: [bozejko-speicher1991]`).

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: q-gaussian-obstruction-at-q0.md -->


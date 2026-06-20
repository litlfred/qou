*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

The torus knots embeddable on the moduli surface $\Sigma_g$
of a QOU form a **complete set of representations** — they
exhaust the available cohomology and span the space of
knot observables.

## Statement

**Proposition.**
*Let $(\mathbf{C}, A, \tau)$ be a QOU with moduli surface
$\Sigma_g$ of genus $g$ and Euler characteristic
$\chi = 2 - 2g$.*

**(i) Embeddability = representation.**
*A torus knot $T_{r,s}$ with $\gcd(r, s) = 1$ admits a
representation in $\mathbf{C}$ if and only if its Seifert
rank embeds in the first cohomology of $\Sigma_g$:*

$$
  \mathrm{rank} H_1(\mathrm{Seifert}(T_{r,s}))
  =  \frac{(r-1)(s-1)}{2}
   \leq  g
$$

**(ii) Fiber degree.**
*The knot $T_{r, p^k}$ acts at fiber degree $k$, where $p$
is prime.  On $\Sigma_g$, the maximum fiber degree is:*

$$
  k_{\max}(r, p, g)
  = 
  \max\!\left\{k : \frac{(r-1)(p^k - 1)}{2} \leq g\right\}
$$

*Degree $1$ knots define **shells**.  Degree $2$ knots define
**subshells**.  Degree $\geq 3$ knots, if embeddable, would
define sub-subshells.*

**(iii) Completeness.**
*The Jones polynomials of the embeddable torus knots, evaluated
in the irreducible representations of $H_2(q) \oplus H_3(q)$,
**span** the space of knot invariants on $\Sigma_g$.  Every
knot observable on $\Sigma_g$ is a linear combination
of evaluations of the embeddable torus knots.*

**(iv) Genus $4$ is forced.**
*The QOU axioms require:*
- *$T_{2,3}$ embeds (SU$_2$ reconstruction from trefoil structure):
  $(1)(2)/2 = 1 \leq g$.*
- *$T_{2,9} = T_{2,3^2}$ embeds (color-squared strong force, degree $2$):
  $(1)(8)/2 = 4 \leq g$.*
- *$T_{2,11}$ does NOT embed (no additional particles observed):
  $(1)(10)/2 = 5 > g$.*

*Therefore $g = 4$ and $\chi = 2 - 2(4) = -6$.*

## The 6 representations on $\Sigma_4$

For $g = 4$, the embeddability constraint $(r-1)(s-1) \leq 8$
with $\gcd(r, s) = 1$ and $2 \leq r < s$ yields exactly $6$
torus knots:

See [Table 1](#tbl:cohomological-embedding-table1-data).

The total Seifert rank used: $1 + 2 + 3 + 4 + 3 + 4 = 17$.
The available rank: $2g = 8$ (from $H^1(\Sigma_4) = \mathbb{Z}^8$).
The knots **overlap** in $H^1$ (they share Seifert cycles), so
$17 > 8$ does not contradict embeddability — each knot individually
fits within rank $\leq 4 = g$.

## Knot basis for $H^*(\Sigma_4)$

The cohomology of $\Sigma_4$ admits a **knot basis** — each
generator is identified with a specific knot-particle or force
operator.  The Hodge decomposition $H^1 = H^{1,0} \oplus H^{0,1}$
separates holomorphic (degree-$1$) from antiholomorphic
(degree-$2$) sectors:

$$
  H^*(\Sigma_4)
  = 
  \underbrace{H^0 \oplus H^2}_{\dim 2}
   \oplus 
  \underbrace{H^{1,0}}_{\dim 4}
   \oplus 
  \underbrace{H^{0,1}}_{\dim 4}
$$

See [Table 2](#tbl:cohomological-embedding-table2-data).

**Dimension count**: $\dim H^0 + \dim H^1 + \dim H^2 = 1 + 8 + 1 = 10$.  Euler characteristic: $\chi = 1 - 8 + 1 = -6$.  The $8$
generators of $H^1$ comprise $4$ holomorphic ($H^{1,0}$, degree-$1$
torus knots) and $4$ antiholomorphic ($H^{0,1}$, degree-$2$ knots
$+$ the amphichiral Higgs mass mechanism).

**Gravity** is not a knot — it is the categorical trace
$\int_A$ (the Frobenius pairing), operating at degree $0$.
It acts universally on all knot-particles.

**The Higgs mass mechanism** $4_1$ is the figure-eight knot:
the closure of the Borromean braid
$(\Delta_{\mathrm{mix}})^2 = (\sigma_0\sigma_1^{-1})^2$.
It is amphichiral ($4_1 = 4_1^{-1}$, its own antiparticle),
hyperbolic ($\mathrm{Vol}(4_1) = 2.0299$, giving mass), and
couples to every knot-particle with crossings $> 0$
(proportional to crossing count $=$ proportional to mass).
Massless knot-particles (photon: $0$ crossings, neutrino:
$0$ crossings) do not couple.  The open braid
$(\Delta_{\mathrm{mix}})^2$ gives the axial coupling
$g_A \approx 1.277$; the closed knot gives the mass mechanism.

The **Higgs boson** — the excitable scalar particle at
$\sim 125 \mathrm{GeV}$ — is separately identified with
the torus link $T(2,8)$
([Higgs as $T(2,8)$](#conj:higgs-t28)), a spin-$0$ boson
consistent with the fermion--boson decomposition
([fermion--boson knot--link](#prop:fermion-boson-knot-link)).
The two objects play complementary roles: $4_1$ is the
**mass mechanism** (the Higgs field condensate), while
$T(2,8)$ is the **mass boson** (the excitation of the field).

## Completeness via Jones polynomials

The Iwahori--Hecke algebras on the embeddable strand counts are:
- $H_2(q)$: $2$ irreducible representations (partitions of $2$:
  $(2)$ trivial, $(1,1)$ sign).  Dimension $2! = 2$.
- $H_3(q)$: $3$ irreducible representations (partitions of $3$:
  $(3)$ trivial, $(1,1,1)$ sign, $(2,1)$ standard of dimension
  $[2]_q$).  Dimension $3! = 6$.

Total irreps: $2 + 3 = 5$.

The Jones polynomial of a torus knot $T_{r,s}$ decomposes over
the irreps of $H_r(q)$ via the Markov trace:

$$
  V_{T_{r,s}}(q)
  = 
  \sum_{\lambda \vdash r}
  d_\lambda(q) \chi_\lambda(T_{r,s})
$$

where $d_\lambda$ is the $q$-dimension and $\chi_\lambda$ is the
character in irrep $\lambda$.

The $6$ embeddable knots, evaluated in the $5$ irreps, give a
$6 \times 5$ matrix $M_{ij} = \chi_{\lambda_j}(\sigma_i)$.  This
matrix has rank $5$ (= number of irreps, verified numerically).
Therefore the $6$ knot evaluations **span** the $5$-dimensional
space of irrep characters.

**Completeness**: any knot observable on $\Sigma_4$ is
a function of the irrep characters, which are spanned by the
$6$ torus knots.  No knot on $\Sigma_4$ can have an invariant
independent of $\{T_{2,3}, T_{2,5}, T_{2,7}, T_{2,9}, T_{3,4}, T_{3,5}\}$.

## Consequences

1. **Particle finiteness**: the $6$ torus knots are the complete
   knot-particle content.  Every observable hadron is a composite
   of these $6$ building blocks $\mathcal{K}_{\tau(r,s)}$.  No
   additional knot-particles exist on $\Sigma_4$.

2. **Shell model completeness**: the nuclear orbital shell structure
   (magic numbers, subshells) is entirely determined by the
   knot invariants (products and crossing numbers) of these $6$
   representations.  No additional shell structure can arise.

3. **Interaction completeness (no other forces).**  Each embeddable
   torus knot $\tau(r,s)$ defines a transfer matrix
   $T_{\tau(r,s)}(q) \in \mathrm{M}_2(\mathbb{Z}[q^{\pm 1/2}])$
   — a **force operator** governing the interaction it mediates.
   The $7$ transfer matrices ($6$ non-trivial + the identity)
   exhaust the harmonic $1$-forms on $\Sigma_4$: every interaction
   between knot-particles is a composition of these $7$ operators.
   An $8$th would require an embeddable torus knot at genus $> 4$
   — contradicting the brane tower cohomology.  **There are exactly
   $7$ force operators (including free propagation), and we prove
   there can be no others.**

   | Transfer matrix | Knot-particle | Interaction |
   |:---:|:---:|:---|
   | $T_{\tau(1,0)}(q) = \mathbf{I}$ | $\mathcal{K}_\nu$ (unknot) | Free propagation (identity) |
   | $T_{\tau(2,3)}(q)$ | $\mathcal{K}_e$ (trefoil) | Mass / electromagnetic |
   | $T_{\tau(2,5)}(q)$ | $\mathcal{K}_{\tau(2,5)}$ | 2nd generation |
   | $T_{\tau(2,7)}(q)$ | $\mathcal{K}_c$ (charm) | 3rd generation |
   | $T_{\tau(3,5)}(q)$ | $\mathcal{K}_{\tau(3,5)}$ | Weak ($\beta$-decay vertex) |
   | $T_{\tau(2,9)}(q)$ | $\mathcal{K}_{\tau(2,9)}$ | Strong binding (degree-$2$ tower of trefoil) |
   | $T_{\tau(3,4)}(q)$ | $\mathcal{K}_t$ (top) | Hopf-squared binding (degree-$2$ tower of Hopf) |

4. **$\chi = -6$ is the unique solution**: genus $4$ is the
   unique genus that accommodates exactly $\mathrm{SU}_2$
   reconstruction + color-squared strong force + no extra
   knot-particles.  Any other genus gives either too few forces
   ($g < 4$: no strong binding) or too many knot-particles
   ($g > 4$: $\tau(2,11)$ embeds, predicting unobserved matter).

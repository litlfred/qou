<!-- FILE_START: vertex-factorisation-feynman-intro.md -->
The preceding sub-section developed the vertex / Markov arc: the
vertex-as-exceptional-divisor + six operators via vertex
factorisation + Breit-Wheeler vertex + Markov-trace product + the
Hecke-Markov transition that anchors the factorisation. This
sub-section then identifies the same factorisation on the Feynman
side: the Feynman eigenbasis decomposition + trace collapse +
Feynman-Markov identification (the categorical-trace bridge) + the
Feynman-QOU dictionary + the classical limit. The two sub-sections
together provide both the vertex-algebra and the Feynman views of
the same exceptional-divisor structure.

The output is the Feynman eigenbasis decomposition with explicit categorical-trace evaluations; the next sub-section's archimedean-realisation Kashaev volume bridge consumes the Feynman trace collapse as its substrate-level input.
<!-- FILE_END: vertex-factorisation-feynman-intro.md -->

<!-- FILE_START: feynman-eigenbasis-decomposition.md -->
**Lemma.**
*Let $V$ be the fundamental representation of $\mathrm{SU}_q(2)$ with
$q$ not a root of unity, and let $\beta \in B_n$ be a braid acting on
$V^{\otimes n}$ via the braid group representation
$\rho_n \colon B_n \to \mathrm{Aut}(V^{\otimes n})$.  Then*

$$
  V^{\otimes n}
  \cong
  \bigoplus_{\substack{\lambda \vdash n \\ \ell(\lambda) \leq 2}}
  V_\lambda \otimes S_\lambda,
$$

*where $V_\lambda$ is the irreducible $\mathrm{SU}_q(2)$-module of spin
$j = (\lambda_1 - \lambda_2)/2$ and $S_\lambda$ is the irreducible
$H_n(R, q)$-module.  The braid $\beta$ acts on each $S_\lambda$ via
the quotient map $B_n \to H_n(R, q)$, and the number of summands is
$\lfloor n/2 \rfloor + 1$, which is finite for every $n$.*
<!-- FILE_END: feynman-eigenbasis-decomposition.md -->

<!-- FILE_START: feynman-trace-collapse.md -->
**Lemma.**
*Suppose $V_{\mathrm{phys}} = \varinjlim V^{\otimes n}$ admits the
complete eigenbasis of
([eigenbasis decomposition](#lem:feynman-eigenbasis-decomposition)).
Then the Feynman path integral*

$$
  \langle\psi_f|\psi_i\rangle
  =
  \int \mathcal{D}\phi\,e^{iS[\phi]/\hbar}
$$

*collapses to a finite weighted sum over the irreducible summands
$V_\lambda \otimes S_\lambda$.  No regularisation is needed, because
$V^{\otimes n}$ has finitely many irreducible summands by the
semisimplicity of $H_n(R, q)$ at non-root-of-unity $q$.*
<!-- FILE_END: feynman-trace-collapse.md -->

<!-- FILE_START: feynman-markov-identification.md -->
**Lemma.**
*Let $\beta \in B_n$ act on $V^{\otimes n}$ via $\rho_n$.  The
transition amplitude on the eigenbasis, defined as the Markov-weighted
sum of partial traces,*

$$
  \langle\psi_f|\psi_i\rangle_{\mathrm{eigenbasis}}
  :=
  \sum_{\substack{\lambda \vdash n \\ \ell(\lambda) \leq 2}}
  w_\lambda \cdot \mathrm{tr}_{S_\lambda}\bigl(\rho_n(\beta)\bigr),
$$

*equals the Jones--Markov trace
$\mathrm{tr}_M\bigl(\rho(\beta)\bigr)$ on $H_n(R, q)$, where the
Markov weights are
$w_\lambda = \dim_q(V_\lambda) \cdot \dim(S_\lambda) / \dim_q(V^{\otimes n})$.*
<!-- FILE_END: feynman-markov-identification.md -->

<!-- FILE_START: feynman-categorical-trace.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with
$\mathbf{C} = \mathbf{Rep}(\mathrm{SU}_q(2))$, $V$ the fundamental
representation, and $q$ not a root of unity.  Let
$\varrho \colon \mathbf{1} \to A$ be a closed cycle with braid
representative $\beta \in B_n$.

**Proposition.**
*The Feynman transition amplitude, evaluated on the knot-type
eigenbasis provided by the braided monoidal structure, equals the
Jones--Markov trace of the braid representation in the Hecke algebra:*

$$
  \langle\psi_f|\psi_i\rangle_{\mathrm{eigenbasis}}
  =
  \sum_{\substack{\lambda \vdash n \\ \ell(\lambda) \leq 2}}
  w_\lambda \cdot \mathrm{tr}_{S_\lambda}\bigl(\rho_n(\beta)\bigr)
  =
  \mathrm{tr}_M\bigl(\rho(\beta)\bigr),
$$

*where the sum is over partitions $\lambda$ of $n$ with at most two
parts, $w_\lambda$ are the Markov weights determined by the Markov
property $\mathrm{tr}_M(x \sigma_n^{\pm 1}) = z^{\pm 1}\mathrm{tr}_M(x)$
([Jones--Markov trace](#thm:jones-markov-trace)),
$\mathrm{tr}_{S_\lambda}$ is the trace on the irreducible
$H_n(R, q)$-module $S_\lambda$, and the right-hand side is the
Jones--Markov trace on $H_n(R, q)$.  The Markov weights satisfy
$w_\lambda = \dim_q(V_\lambda) \cdot \dim(S_\lambda) / \dim_q(V^{\otimes n})$,
where $\dim_q(V_\lambda) = [2j+1]_q$ is the quantum dimension of the
$\mathrm{SU}_q(2)$-module of spin $j = (\lambda_1 - \lambda_2)/2$.*

*In particular, the transition amplitude is a finite sum over
$\lfloor n/2 \rfloor + 1$ terms --- one for each irreducible summand
of $V^{\otimes n}$ --- and its absolute value equals the categorical
mass at a single brane level
([categorical mass as Markov trace](#prop:categorical-mass-markov)):*

$$
  \mathfrak{m}(\varrho)\big|_{\text{single level}}
  =
  \mathrm{tr}_M\bigl(\rho(\beta)\bigr)
  =
  \bigl|
  \langle\psi_f|\psi_i\rangle_{\mathrm{eigenbasis}}
  \bigr|.
$$
<!-- FILE_END: feynman-categorical-trace.md -->

<!-- FILE_START: feynman-qou-dictionary.md -->
The correspondence between the Feynman path integral formalism and the
QOU categorical trace is summarised in the following dictionary.  Each
row identifies a structural element of Feynman's formulation with its
QOU counterpart; the third column gives the content block where the
QOU object is defined.

See [Table](#tbl:feynman-qou-dictionary-table-data).

**Three finite computations of the path integral.**
The categorical trace admits three independent evaluation methods
--- analytic, algebraic, and computational --- each producing the
same finite answer without regularisation:

1. **Multiplicative integral** (analytic) \cite{yekutieli2015}:
   $\mathfrak{m} = \lVert\mathrm{MI}\int_\Sigma(\nabla_A q, L \wedge F^+)\rVert$.
   The surface $\Sigma$ is the disc swept by the photon threading
   through the hadron braid; the multiplicative integral accumulates
   the connection along this surface.

2. **Ribbon trace** (algebraic):
   $\mathfrak{m} = \lVert\mathrm{tr}_{\mathrm{ribbon}}(\rho(\beta))\rVert \cdot (q-1)^2$.
   The Reshetikhin--Turaev invariant evaluated in the ribbon category
   gives the crossing energy; the factor $(q-1)^2 = c_q^{-2}$ converts
   to mass.

3. **Gr\"obner--Shirshov reduction** (computational):
   $\mathfrak{m} = (q-1)^2 \sum_{\text{Hecke steps}} |c_w| \cdot |q - q^{-1}|$.
   Each Hecke step $\sigma_i^2 \to (q - q^{-1})\sigma_i + 1$ is a
   discrete contribution; the Yang--Baxter moves are free.  Confluence
   of the Gr\"obner--Shirshov basis ensures path independence (gauge
   invariance).

**Photon threading as insertion of a complete set of states.**
In the Feynman formalism, the propagator is computed by inserting a
complete set of intermediate states: $K(x_f, x_i; t) = \sum_n
\langle x_f | n \rangle \langle n | x_i \rangle e^{-iE_n t/\hbar}$.
The QOU analogue is the photon threading construction
([photon threading mass](#prop:photon-threading-mass)):
the photon strand $\gamma$ passes through the hadron braid
$\beta_{\mathfrak{H}}$, encountering each crossing in sequence.  Each
crossing contributes a Hecke step (eigenvalue insertion), and the total
threading cost is the mass.  The braid crossings play the role of
intermediate states; the Hecke relation $(T - q)(T + q^{-1}) = 0$
provides the eigenvalue decomposition at each insertion.
<!-- FILE_END: feynman-qou-dictionary.md -->

<!-- FILE_START: feynman-classical-limit.md -->
**Proposition (conditional on [`conj:classical-limit-stpart`](#conj:classical-limit-stpart) — classical limit).**
*In the $q \to 1$ limit of the categorical trace
([Feynman transition amplitude](#prop:feynman-categorical-trace)),
the following degenerations occur:*

1. **(Hecke $\to$ symmetric group.)**
   *The Hecke relation $(T - q)(T + q^{-1}) = 0$ becomes
   $(T - 1)(T + 1) = 0$, i.e.\ $T^2 = 1$.  The Iwahori--Hecke algebra
   $H_n(R, q)$ degenerates to the group algebra $k[S_n]$ of the symmetric
   group
   ([Hecke algebra from braiding](#rem:hecke-algebra-from-braiding)).*

2. **(Markov trace $\to$ flat character trace.)**
   *The Jones--Markov trace parameter
   $z = (q - 1)/(q^{1/2} + q^{-1/2})^2 \to 0$
   ([Jones--Markov trace](#thm:jones-markov-trace)),
   and the Markov trace $\mathrm{tr}_M$ on $H_n(R, q)$ degenerates to
   the augmentation map
   $\varepsilon \colon k[S_n] \to k$ sending every group element to $1$.*

3. **(Categorical action $\to$ classical action.)**
   *The categorical action
   $\mathfrak{S}_q(K) = \mathrm{tr}_M(\rho(\beta)) \to \mathfrak{S}_1(\beta)$, the
   character of the permutation $\pi(\beta) \in S_n$ obtained by
   imposing $\sigma_i^2 = 1$ on the braid word.  The $q$-energy
   reduces to $\mathfrak{E}_1 = \mathfrak{S}_1$ because the rotational and
   translational terms vanish with $\hbar_q = 1 - q^{-1} \to 0$
   ([$q$-energy](#def:q-energy)).*

4. **(Eigenbasis collapse.)**
   *The Jones polynomial $J_K(1) = 1$ for every knot $K$, so the
   Markov trace can no longer distinguish knot types.  The eigenspace
   decomposition $V^{\otimes n} \cong \bigoplus_\lambda V_\lambda \otimes S_\lambda$
   persists, but the $S_\lambda$ become Specht modules of $S_n$ ---
   the standard angular momentum eigenbasis of quantum mechanics.
   The quantum dimensions $[2j+1]_q$ become ordinary dimensions
   $2j+1$.*

5. **(Braiding $\to$ symmetric.)**
   *The braiding $c_{V,V}$ satisfies $c_{V,V}^2 = \mathrm{id}$, so
   the :refterm[monoidal category]{#monoidal-category} becomes symmetric.  The non-trivial
   knot structure that organises the sum at $q \neq 1$ collapses:
   all braid closures yield the unknot under the symmetric quotient.*

*In this limit, the finite categorical trace
$\sum_\lambda \dim_q(V_\lambda) \cdot \mathrm{tr}_{S_\lambda}(\rho(\beta))$
degenerates to the standard discrete trace
$\sum_\lambda (2j+1) \cdot \mathrm{tr}_{S_\lambda}(\pi(\beta))$
over the finite-dimensional angular momentum eigenbasis of the symmetric group.*

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: feynman-classical-limit.md -->

<!-- FILE_START: feynman-classical-limit-interpretation.md -->
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
  \mathfrak{E}_1(K) = \underbrace{j(j+1) \cdot 0}_{\text{rot.}}
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
<!-- FILE_END: feynman-classical-limit-interpretation.md -->


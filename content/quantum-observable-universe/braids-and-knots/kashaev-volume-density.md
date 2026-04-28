The topological mass formula
([topological mass formula](#prop:topological-mass-formula))

$$
  \mathfrak{m}(K) = \frac{\mathrm{Vol}(K)}{\hbar_q^{2}}
$$

is most naturally read as a **volume $\times$ density** product.  This
remark collects the three ingredients --- density $\rho_q$, topological
volume $\mathrm{Vol}(K)$, and the algebraic bridge provided by the
Kashaev limit --- into a single narrative that unifies the continuous
hyperbolic geometry of the mass endomorphism with the discrete Markov
trace over the Iwahori--Hecke algebra.

### Substrate density $\rho_q$

*Define the **substrate density** to be the inverse squared quantum
Planck constant*
([quantum Planck constant](#def:quantum-planck-constant)):

$$
  \rho_q
  \;:=\;
  \frac{1}{\hbar_q^{2}}
  \;=\;
  \frac{1}{(1 - q^{-1})^{2}}
  \;=\;
  \frac{q^{2}}{(q-1)^{2}}.
$$

Physically, $\rho_q$ is the **quantum drag density** imposed by the
substrate: the categorical cost, per unit of topological volume, of
transporting a closed vortex $\varrho \colon \mathbf{1} \to A$ through
the Frobenius--Hopf structure.  At the substrate value $q_0 \approx
1.10998$ ([substrate parameter](#def:substrate-parameter)) the density
is finite and greater than unity; in the classical
limit $q \to 1$ one has $\hbar_q \to 0$ and $\rho_q \to \infty$,
recovering the expected decoupling of mass from topology.

Rewriting the topological mass formula with $\rho_q$ made explicit:

$$
  \mathfrak{m}(K)
  \;=\;
  \underbrace{\mathrm{Vol}(K)}_{\text{topological volume}}
  \;\cdot\;
  \underbrace{\rho_q}_{\text{substrate density}}.
$$

Mass is volume weighted by the drag density of the substrate.  This
rewriting is an exact algebraic restatement of the proposition; the
$\approx$ sign only enters below, when the continuous $\mathrm{Vol}(K)$
is replaced by the Kashaev limit of Markov traces.

### The Kashaev bridge

The symbol $\mathrm{Vol}(K)$ appears on both sides of a philosophical
divide.  Read archimedeanly, $\mathrm{Vol}(K)$ is the hyperbolic volume
of the knot complement $S^{3} \setminus K$: a continuous real number
extracted from a Riemannian metric of constant negative curvature.  Read
algebraically --- in the register native to the Frobenius--Hopf axioms
--- $\mathrm{Vol}(K)$ is a shadow of a finite sequence of Hecke crossing
resolutions.  The Kashaev Volume Conjecture
\cite{kashaev1997, murakami-murakami2001} identifies the two:

$$
  \mathrm{Vol}(K)
  \;=\;
  2\pi\,\lim_{N \to \infty}
  \frac{\log\lvert J_{N}(K;\,e^{2\pi i/N})\rvert}{N},
$$

where $J_{N}(K; q)$ is the **$N$-coloured** Jones polynomial at $q$:
the Markov trace on the Hecke closure of $\beta_{K}$ with a
Jones--Wenzl projector $p_{N-1}$ inserted, equivalently the quantum
trace in the $N$-dimensional irreducible representation
$V_{N-1}$ of $U_{q}(\mathfrak{sl}_{2})$.  The standard Markov trace
$\mathrm{tr}_M$ recovers only the $N = 2$ case
([Jones--Markov trace](#thm:jones-markov-trace)); higher colourings
replace $\mathrm{tr}_M$ by the trace $\mathrm{tr}_M^{(N)}$ on the
$V_{N-1}$-coloured closure, and all three --- coloured trace,
categorical $\int_{A}$ on the $N$-th symmetric power, and
$J_{N}$ --- agree.  In the QOU setting the left-hand side is the
continuous holonomy term that appears in the archimedean proof of
the mass formula; the right-hand side is a limit of **coloured
Markov traces** in the Iwahori--Hecke algebra $H_{n}(q)$, each still
a categorical $\int_{A}$ evaluation, but on the Hecke image
$\rho(\beta_{K})$ composed with the projector $p_{N-1}$
([Jones--Markov trace](#thm:jones-markov-trace);
[Markov trace product](#thm:markov-trace-product)).

### Inverting the ontology

The Kashaev limit does more than relate two expressions for the same
number: it reverses the usual direction of abstraction.  In a
classically hyperbolic account, the volume is fundamental and the Jones
invariants are derivative asymptotic witnesses to it.  In the
non-archimedean, algebraically-native register of the QOU the roles
swap:

1. **The trace is fundamental.**  The categorical Haar morphism
   $\int_{A} \colon A \to \mathbf{1}$ and the categorical trace of
   $(\int_{A} \otimes \mathrm{id}) \circ \Delta \circ \varrho$ are
   finite, exact, and defined without recourse to a continuous manifold.
   Through the representation $\rho \colon B_{n} \to H_{n}(q)$ the
   fundamental-colour ($N = 2$) case coincides with the standard
   Markov trace $\mathrm{tr}_M$
   ([Jones--Markov trace](#thm:jones-markov-trace)); higher colours
   use the projector-inserted trace $\mathrm{tr}_M^{(N)}$, still
   defined purely inside $H_{n}(q)$.
2. **The coloured Jones polynomials are coloured Markov traces.**
   Each $J_{N}(K;\,e^{2\pi i/N})$ is a finite algebraic evaluation of
   $\mathrm{tr}_M^{(N)}$ on the Hecke image of the braid closure
   that represents $K$ --- equivalently, of the quantum trace in
   $V_{N-1}$.  The algebraic quantum volume
   $\mathrm{Vol}_{q}(\beta) \in \mathbb{Z}[q^{1/2}, q^{-1/2}]$
   ([algebraic quantum volume](#def:algebraic-quantum-volume)) collects
   these evaluations (across colours and roots of unity) into a
   single object, which embeds into the Habiro ring
   ([Habiro ring](#def:habiro-ring)).
3. **The hyperbolic volume is emergent.**  By the Kashaev conjecture,
   $\mathrm{Vol}(K)$ is the asymptotic coefficient of the logarithm of
   these coloured Markov traces as the colour $N \to \infty$.  It is
   the macroscopic shadow of an infinite family of finite algebraic
   measurements, not an input to them
   ([algebraic volume specialisation](#prop:algebraic-volume-specialization)).

What the archimedean observer calls "the continuous hyperbolic volume
of the knot complement" is, in the substrate, nothing more than the
accumulated **algebraic drag** generated as the state's representation
is transported by the comultiplication $\Delta$ and sorted by the
$R$-matrix into symmetric and antisymmetric eigenspaces.  Each crossing
contributes a rigidly determined quantum crossing weight
([crossing energy](#def:crossing-energy)) from the eigenvalues
$q$ and $-q^{-1}$ of $T$; the sum of these crossing weights, resolved
to Gröbner--Shirshov normal form
([nuclear normal form](#prop:nuclear-groebner-reduction)), is the
only physics in play.

### Consequences for the mass formula

Combining density and emergent volume, the mass of a knot-particle $K$
with braid representative $\beta_{K}$ admits the fully algebraic
expression

$$
  \mathfrak{m}(K)
  \;\approx\;
  \rho_{q}\;\cdot\;
  \Bigl[
    2\pi\,\lim_{N \to \infty}
    \frac{\log\lvert J_{N}(K;\,e^{2\pi i/N})\rvert}{N}
  \Bigr],
$$

where each $J_{N}(K;\,e^{2\pi i/N})$ is the coloured Markov trace
$\mathrm{tr}_M^{(N)}(\rho(\beta_{K}))$ at $q = e^{2\pi i/N}$ ---
still an entirely algebraic evaluation inside $H_{n}(q)$.

Three observations follow.

1. *No continuous input.*  Every quantity on the right-hand side is
   either a rational function of $q$ ($\rho_{q}$) or a coloured
   Markov trace in $H_{n}(q)$ evaluated at roots of unity
   ([Markov trace product](#thm:markov-trace-product)).  The hyperbolic
   volume enters only as the asymptotic coefficient, not as a separately
   posited datum.
2. *The substrate evaluation is finite.*  At $q = q_{0}$
   ([substrate parameter](#def:substrate-parameter)) the mass is
   computed directly from $\ln\lvert\mathrm{Vol}_{q_{0}}(\beta_{K})\rvert$
   ([algebraic quantum volume](#def:algebraic-quantum-volume))
   without passing to the Kashaev limit; the Kashaev identity calibrates
   the overall energy scale (route 2 of
   [algebraic volume specialisation](#prop:algebraic-volume-specialization))
   and fixes the coefficient relating $\rho_{q_{0}}$ to the dimensionful
   mass unit.
3. *Physical prediction vs.\ exact identity.*  The Volume--Density form
   is a derived approximation --- the $\approx$ is obligatory --- whose
   error term is controlled by the convergence rate of the Kashaev limit
   and by the higher-order corrections to the topological mass
   decomposition
   ([topological mass](#thm:topological-mass)).  The underlying
   categorical identity
   $\mathfrak{m}(\varrho) = \bigl\lVert \mathrm{tr}_{\mathrm{desc}}(\varrho) \bigr\rVert + \sum_{i} \bigl\lVert \mathrm{tr}_{\mathrm{trans}}(\varrho, p_{i}) \bigr\rVert$
   is exact.

In short: mass is volume times density; volume is the Kashaev shadow
of an infinite family of coloured Markov traces (each a categorical
$\int_{A}$ on the projector-inserted Hecke image); every step is
algebraic, and the appearance of continuous hyperbolic geometry in
the archimedean mass formula is an asymptotic artefact of the
quantum group at roots of unity, not a prerequisite of the
framework.

*Formal asymptotic content. The Kashaev limit $N \to \infty$ is the
[standard-part functor](#def:standard-part-functor) applied to the
coloured Hecke trace at $q = e^{2\pi i/N}$; the surreal reframing
of the volume conjecture is recorded in
[Kashaev as standard-part](#conj:kashaev-surreal), and the
asymptotic rate is catalogued in the
[body asymptotics catalog](#rem:body-asymptotics-catalog).*

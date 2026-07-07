<!-- FILE_START: intro-archimedean-realization-kashaev.md -->
The substrate-level knot category developed above takes value in
a generic categorical setting.  Crossing into the archimedean
realm requires a functor that lands in $\mathrm{Vec}_{\mathbb{C}}$;
this section constructs the archimedean realisation functor and
matches its output on knot complements to the Kashaev volume
conjecture, identifying the hyperbolic-volume invariant as the
archimedean shadow of the substrate-level Hecke-skein.

The arc splits in two.  The first half introduces the archimedean
realisation functor, proves it preserves the Hecke-skein relation,
and computes its value on torus knots (where the Kashaev volume
vanishes).  The second half tracks the convergence of the
substrate-level invariant to the hyperbolic volume as $q \to 1$,
identifying the categorical $\mathrm{Vol}_{\mathrm{hyp}}$ as the
limit of the Kashaev sum.

The arc closes with the archimedean-image table, the pre-tau vs post-tau distinction, and the volume-through-tau / volume-as-motivic-period identifications that pin the Kashaev volume conjecture's substrate-level interpretation.
<!-- FILE_END: intro-archimedean-realization-kashaev.md -->

<!-- FILE_START: archimedean-realization-functor.md -->
**Definition.**
*The **archimedean realization functor** of the QOU substrate is
the composite*

$$
  \mathcal{R}_{\mathrm{top}}
  \;:\;
  \widehat{\mathcal{M}}
  \;\xrightarrow{\;\;\chi_{\mathrm{top}}\;\;}\;
  \widehat{\mathcal{M}} \otimes_{K_0(\mathrm{Var})} \mathbb{Z}
  \;\xrightarrow{\;\;\pi_\infty\;\;}\;
  \mathbb{R}
$$

*sending the motivic class $[X]$ to its topological Euler
characteristic $\chi_{\mathrm{top}}(X)$ followed by the
**archimedean projection** $\pi_\infty \colon \mathbb{A} \to \mathbb{R}$
of the [adelic substrate](#def:adelic-substrate). The composite
$\mathcal{R}_{\mathrm{top}}$ is the topological realization of the
motivic measure: it maps motives to real-valued physical observables.*

**The two halves.**

1. **Realization of motives.** A motivic integral
   $\int_{\mathcal{L}(X)} d\mu \in \widehat{\mathcal{M}}$
   ([motivic mass measure](#def:motivic-mass-measure))
   is a class in the Grothendieck ring of varieties — a *geometric
   shape*, not a number. The topological realization
   $\chi_{\mathrm{top}}$ sends $[X]$ to $\chi(X) \in \mathbb{Z}$
   (Euler characteristic), or more refinedly to a Hodge-theoretic
   invariant such as a hyperbolic volume when $X$ has a hyperbolic
   structure on its smooth part.

2. **Adelic projection.** A laboratory measurement is an evaluation
   of an adelic observable at the archimedean place $\infty$:
   $\pi_\infty \colon \mathbb{A} \to \mathbb{R}$ discards the
   non-archimedean coordinates $\mathbb{Q}_p$ and keeps only the
   real component. Stability of the underlying state depends on
   the full adelic ring; the *measured value* depends only on
   $\pi_\infty$.

The physical observable extracted from a state with motivic
description $[X]$ is therefore

$$
  \mathrm{Obs}_{\mathbb{R}}(X)
  \;=\;
  \mathcal{R}_{\mathrm{top}}\!\left(
    \int_{\mathcal{L}(X)} d\mu
  \right)
  \;\in\;\mathbb{R}.
$$

**Identification with the QOU fibre functor.** The QOU fibre
functor $\tau \colon \mathbf{C} \to \mathbf{Arch}$
([spatial realization functor](#def:spatial-realization-functor))
realizes the categorical substrate in an archimedean target
$\mathbf{Arch}$. *On every motive that arises from QOU braid /
knot data, $\mathcal{R}_{\mathrm{top}}$ is exactly the
archimedean component of $\tau$:*

$$
  \mathcal{R}_{\mathrm{top}}
  \;=\;
  \tau_{\mathrm{arch}}
  \;:=\;
  \pi_\infty \circ \tau
  \quad\text{on } \widehat{\mathcal{M}}_{\mathrm{QOU}}
  \;\subseteq\; \widehat{\mathcal{M}}.
$$

The motivic measure $\mu$ in
[motivic mass measure](#def:motivic-mass-measure) prepares the
input — assembling local cyclotomic data into a class in
$\widehat{\mathcal{M}}$ — and $\mathcal{R}_{\mathrm{top}}$ is the
computation rule that $\tau$ uses to evaluate that class on the
archimedean place. There is no second functor: the *only* exit
from $\mathbf{C}$ to $\mathbb{R}$ is $\tau$, and
$\mathcal{R}_{\mathrm{top}}$ is just $\tau$'s name when restricted
to motivic inputs (see
[$\mathrm{Vol}(K)$ factors through $\tau$](#prop:vol-through-tau)).

Where $\tau$ also realizes objects (algebras, sheaves, connections)
that are not motives, $\mathcal{R}_{\mathrm{top}}$ extends $\tau$
to motivic inputs that lack a smooth realization (e.g. the
exceptional divisors of singular blow-ups in
[motivic mass measure](#def:motivic-mass-measure)) — but the two
agree on their common domain.

**Synthesis.** The QOU framework computes macroscopic observables
from discrete quantum data along a single chain:

$$
  \begin{array}{c}
   \text{local }q\text{-data at each prime }p
   \;\xrightarrow{\;\text{adelic stitch}\;}\;
   \mathbb{A}\text{-valued global state}
   \\[0.5ex]
   \;\xrightarrow{\;\int_{\mathcal{L}(X)} d\mu\;}\;
   \text{motivic class in }\widehat{\mathcal{M}}
   \\[0.5ex]
   \;\xrightarrow{\;\mathcal{R}_{\mathrm{top}} = \pi_\infty \circ \chi_{\mathrm{top}}\;}\;
   \mathrm{Obs}_\mathbb{R}\in\mathbb{R}.
  \end{array}
$$

No continuous differential equations are integrated; no Lebesgue
measure on a smooth manifold is assumed. Discrete categorical data
on the [arc space](#def:arc-space) of the substrate is assembled
adelically, integrated motivically, and projected archimedeanly
into the laboratory continuum. The Kashaev limit of the
[algebraic quantum volume](#def:algebraic-quantum-volume) is the
canonical instance of $\mathcal{R}_{\mathrm{top}}$ in action; see
[Kashaev limit as archimedean realization](#rem:kashaev-as-archimedean-realization).
<!-- FILE_END: archimedean-realization-functor.md -->

<!-- FILE_START: pre-tau-vs-post-tau.md -->
> **SUPERSEDED-$\rho_q$ note .** Any use of the
> scalar substrate density $\rho_q = 1/\hbar_q^2$ in this block is the
> structurally-wrong leading-order ansatz per
> [`mass-endomorphism-tower.md` §SUPERSEDED](mass-endomorphism-tower.md);
> the canonical replacement is the operator-valued $A^\lambda_{\mu, \nu}(I)$
> graded expansion [`prop:rho-k-graded-expansion`](rho-k-graded-expansion.md).
> Full purge tracking: [`docs/audits/-superseded-rho-q-purge.md`](../../../docs/audits/-superseded-rho-q-purge.md).

**Reading.** The encounter chapter is the place in the
manuscript where the Archimedean wall is most crossed by
accident. The hyperbolic-volume language and the
$q$-Pochhammer language *coincide* under
[$\tau_{\mathrm{arch}}$](#def:archimedean-realization-functor),
which can lead an author to write a derivation step in one
language while it logically belongs to the other. This remark
states the discipline once.

**The wall.** Every derivation step in the manuscript belongs
to exactly one of two registers:

| Register | Coefficient ring | Operative invariants | Examples |
|---------------|-------------------------------------------------------------------|---------------------------------------|---------------------------------------|
| **Pre-$\tau$** | $R = \mathbb{Z}[q^{\pm 1/2}, (q-q^{-1})^{-1}]$ (or its $z$-Habiro completion) | Hecke spectra; Markov traces; LP/SDP feasibility | Confinement SDP; Gröbner--Shirshov reductions |
| **Post-$\tau$** | $\mathbb{R}$ (or $\mathbb{C}$) via $\tau_{\mathrm{arch}}$ | Hyperbolic volumes; thimble depths; mass eigenvalues | Mostow rigidity; PL thimble flow; Bloch--Wigner $D(z)$ |

The functor $\tau_{\mathrm{arch}}$ is the **only** legal way to
cross from the left column to the right. Specifically:

* No derivation step on the left may use a value from the right
 (e.g. a hyperbolic volume) as input. Such values are *outputs*
 of $\tau_{\mathrm{arch}}$, not algebraic data.

* No derivation step on the right may claim algebraic-side
 identities (e.g. Hecke relations) — those hold in $R$ before
 $\tau_{\mathrm{arch}}$ is applied. After $\tau_{\mathrm{arch}}$
 one has only the realised real numbers.

* When a canonical equality bridges the two sides — e.g. the
 mass formula
 $\tau_{\mathrm{arch}}(\mathfrak{m}^{\mathrm{trans}}(\varrho_K))
  = \rho_q \cdot \mathrm{Vol}_{\mathrm{hyp}}(U \setminus K)$ — it
 is a statement *about the functor*, not a derivation step on
 either side alone. canonical comparisons of such bridges with
 experimental data must use $\approx$ unless an explicit error
 term is present.

**Motivic shorthand.** The cleanest algebraic-side home for
encounter data is the **$z$-Habiro completion**
$\hat{\mathbb{Z}}[q^{\pm 1}][z]_z$: it allows one to treat the
poles of the quantum dilogarithm $\Phi_q$ algebraically — as
quotients of cyclotomic ideals — rather than as divergent
analytic limits. Under $\tau_{\mathrm{arch}}$ these algebraic
poles realise as the cusps of the hyperbolic triangulation
([pole-to-cusp bijection](#conj:algebraic-geometric-dilog-equivalence)).

**Self-check.** When writing or reviewing an encounter-side
derivation, ask:

1. *Which column does my coefficient ring live in?*
2. *Have I used any data from the other column without going
 through $\tau_{\mathrm{arch}}$?*
3. *Are bridging equalities written with $\approx$ (or with an
 explicit error term)?*

If any answer is wrong, fix the derivation; do not hide the
crossing in prose.
<!-- FILE_END: pre-tau-vs-post-tau.md -->

<!-- FILE_START: vol-through-tau.md -->
**Proposition.**
*Let $(\mathbf{C}, A, \tau)$ be a QOU with fibre functor
$\tau \colon \mathbf{C} \to \mathbf{Arch}$ to the category of
archimedean realizations (smooth manifolds, real Hilbert spaces,
or any chosen archimedean target). For every braid
$\beta \in H_n(R, q)$, the real-valued knot volume $\mathrm{Vol}(K_\beta)$
of its closure factors strictly through $\tau$:*

$$
  \begin{tikzcd}[row sep=2.4em, column sep=4em]
    \mathrm{End}_{\mathbf{C}}(A^{\otimes n})
      \arrow[r, "\mathrm{tr}_M"]
      \arrow[d, "\tau_{\mathrm{arch}}"']
    & \mathbb{Z}[q^{1/2}, q^{-1/2}]
      \arrow[d, "\tau_{\mathrm{arch}}"]
    \\
    \tau(\mathrm{End}_{\mathbf{C}}(A^{\otimes n}))
      \arrow[r, "\mathrm{tr}_M^{\mathrm{arch}}"']
    & \mathbb{R}
  \end{tikzcd}
$$

*and there is no other archimedean route. Equivalently, the
diagram of QOU outputs commutes,*

$$
  \mathrm{Vol}(K_\beta)
  \;=\;
  \tau_{\mathrm{arch}}\bigl(\mathrm{Vol}_q(\beta)\bigr)
  \;=\;
  (\pi_\infty \circ \tau)\bigl(\mathrm{Vol}_q(\beta)\bigr),
$$

*where $\pi_\infty \colon \mathbb{A} \to \mathbb{R}$ is the
[adelic archimedean projection](#def:adelic-substrate) and
$\tau$ is the QOU fibre functor.*

**Identification.**
On the algebraic-quantum-volume part of $\mathrm{End}_{\mathbf{C}}(A^{\otimes n})$,
$\tau_{\mathrm{arch}}$ coincides with the
[archimedean realization functor](#def:archimedean-realization-functor)
$\mathcal{R}_{\mathrm{top}} = \pi_\infty \circ \chi_{\mathrm{top}}$.
Concretely:

$$
  \tau_{\mathrm{arch}}
  \;=\;
  \mathcal{R}_{\mathrm{top}}\big|_{\widehat{\mathcal{M}}_{\mathrm{Vol}}}
  \;=\;
  \mathcal{R}_{\mathrm{top}} \circ \mu,
$$

i.e. $\mathcal{R}_{\mathrm{top}}$ is just $\tau$'s archimedean
restriction, and $\mu$ is the
[motivic mass measure](#def:motivic-mass-measure) that prepares the
input. The fibre functor $\tau$ is the *only* exit from $\mathbf{C}$
to the laboratory continuum; the realization functor is its
canonical computation rule on quantum-volume motives.

**Sketch.**
$(\Rightarrow)$ Any composite $\mathbf{C} \to \mathbb{R}$ that
preserves tensor products and dualities of $\mathbf{C}$ and lands
in archimedean spaces is, by Tannaka–Krein duality / rigidity, a
fibre functor — hence $\tau$ up to natural isomorphism. The
$\tau$-image of $\mathrm{Vol}_q(\beta)$ is therefore the unique
archimedean output.

$(\Leftarrow)$ Given $\tau$, the composite $\tau \circ \mathrm{Vol}_q$
takes values in archimedean realizations of the trace of the
braid representation. Restriction to $\mathbb{R}$ via $\pi_\infty$
recovers exactly $\ln |\mathrm{Vol}_{q_0}(\beta)|$, the standard
formula
([algebraic quantum volume](#def:algebraic-quantum-volume)).

**Corollary.**
Any physical computation of a knot volume in QOU — Kashaev limit,
Bloch–Wigner dilogarithm, hyperbolic-volume formula
([$q$-Kashaev volume density](#rem:kashaev-volume-density),
[Kashaev as archimedean realization](#rem:kashaev-as-archimedean-realization))
— is the value of the same composite $\pi_\infty \circ \tau$.
There is no archimedean side-channel: every real-valued QOU
observable is the $\tau$-shadow of a categorical morphism.

## Lean formalization

The companion Lean `vol_through_tau_factors` currently encodes an existence stub (`∃ v, True`) pending a faithful statement; the sketch above is the intended content, deferred via `sorry` (`-- Ref: [kashaev1997]`, `[manuscript]`).
<!-- FILE_END: vol-through-tau.md -->

<!-- FILE_START: vol-as-motivic-period.md -->
**Reading.**
The hyperbolic volume $\mathrm{Vol}(S^3 \setminus K)$ of a hyperbolic
knot complement is a *motivic period* — specifically, the value of a
mixed-Tate motive under the **Bloch--Wigner regulator** $r_\infty$.
Under this reading, the
[archimedean realization functor](#def:archimedean-realization-functor)
is the period-evaluation map: it takes a class in the (quantum) Bloch
group and returns its archimedean image in $\mathbb{R}$.

**Period interpretation.**
A *period*, in the sense of Kontsevich--Zagier, is a complex number
expressible as the integral of an algebraic differential form over a
domain cut out by polynomial inequalities with rational coefficients.
For a hyperbolic knot complement triangulated with shape parameters
$z_1, \ldots, z_k \in \overline{\mathbb{Q}}$ satisfying Thurston's
gluing equations, the volume is

$$
  \mathrm{Vol}(S^3 \setminus K)
  \;=\;
  \sum_{i=1}^{k} D(z_i),
\qquad
D(z) := \operatorname{Im}\,\mathrm{Li}_2(z)
       + \log|z|\cdot\arg(1-z),
$$

where $D$ is the **Bloch--Wigner dilogarithm**. Each summand $D(z_i)$
is the period of an algebraic 1-form on $\mathbb{P}^1\setminus\{0,1,\infty\}$
integrated over a cycle determined by $z_i$, hence a period in the
Kontsevich--Zagier sense [`zagier1986`,`neumann-zagier1985`].

**Regulator interpretation.**
Equivalently, the shape parameters define a class
$[K] \in \mathcal{B}(\overline{\mathbb{Q}})$ in the (pre-)Bloch group,
and

$$
  \mathrm{Vol}(S^3 \setminus K)
  \;=\;
  r_\infty\bigl([K]\bigr),
$$

where $r_\infty : \mathcal{B}(\mathbb{C}) \to \mathbb{R}$ is the
archimedean Beilinson regulator restricted to the Bloch group. Under
this perspective, $\mathrm{Vol}(K)$ is exactly $K$-theoretic — the
image of an algebraic $K$-theory class under a transcendental
regulator.

**QOU placement.**
The
[archimedean realization functor](#def:archimedean-realization-functor)
already factorises as $\tau_{\mathrm{arch}} = \pi_\infty \circ \tau$
on motivic inputs and as $\pi_\infty \circ \chi_{\mathrm{top}}$ on
arc-space inputs. The Bloch--Wigner reading is the third equivalent
factorisation, restricted to inputs that come from
$\mathrm{Vol}_q$:

$$
  \tau_{\mathrm{arch}}\!
  \begin{pmatrix}
    \text{algebraic quantum volume}\\
    \mathrm{Vol}_q(\mathcal{B}_K) \in \mathbb{Z}[q^{\pm 1/2}]
  \end{pmatrix}
  \;=\;
  r_\infty\!\bigl([K]\bigr)
  \;=\;
  \mathrm{Vol}(S^3 \setminus K).
$$

The three pictures — adelic projection, Euler-characteristic
realization, Bloch--Wigner regulator — agree on this common domain.
Each is useful for a different formal manipulation:

* The **adelic** picture
 ([archimedean realization functor](#def:archimedean-realization-functor))
 is what controls the *categorical* compatibility ($\tau_{\mathrm{arch}}$
 factoring through the QOU fibre functor $\tau$).
* The **Euler-characteristic** picture
 ([motivic mass measure](#def:motivic-mass-measure)) governs the
 blow-up calculus for arc-space integrals.
* The **Bloch--Wigner / regulator** picture is the one that connects
 $\mathrm{Vol}_q$ to existing motivic-cohomology and quantum-topology
 literature (Kashaev, Murakami--Murakami, Garoufalidis--Zagier).

**Scope.**
This is an *interpretive remark*: it makes no new mathematical claim
beyond what is in
[$\mathrm{Vol}(K)$ factors through $\tau$](#prop:vol-through-tau).
It names the existing factorisation in motivic-period
language so that the
[Kashaev volume conjecture](#conj:kashaev-volume-conjecture) and the
archimedean remainder decay conjecture
can be cross-referenced with the regulator literature.
<!-- FILE_END: vol-as-motivic-period.md -->

<!-- FILE_START: kashaev-volume-density.md -->
> **SUPERSEDED-$\rho_q$ note .** Any use of the
> scalar substrate density $\rho_q = 1/\hbar_q^2$ in this block is the
> structurally-wrong leading-order ansatz per
> [`mass-endomorphism-tower.md` §SUPERSEDED](mass-endomorphism-tower.md);
> the canonical replacement is the operator-valued $A^\lambda_{\mu, \nu}(I)$
> graded expansion [`prop:rho-k-graded-expansion`](rho-k-graded-expansion.md).
> Full purge tracking: [`docs/audits/-superseded-rho-q-purge.md`](../../../docs/audits/-superseded-rho-q-purge.md).

The topological mass formula
([topological mass formula](#prop:topological-mass-formula))

$$
  \mathfrak{m}(K) = \frac{\mathrm{Vol}(K)}{\hbar_q^{2}}
$$

is most accordingly read as a **volume $\times$ density** product. This
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
the Frobenius--Hopf structure. At the substrate value $q_0 \approx
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

Mass is volume weighted by the drag density of the substrate. This
rewriting is an exact algebraic restatement of the proposition; the
$\approx$ sign only enters below, when the continuous $\mathrm{Vol}(K)$
is replaced by the Kashaev limit of Markov traces.

### The Kashaev bridge

The symbol $\mathrm{Vol}(K)$ appears on both sides of a philosophical
divide. Read archimedeanly, $\mathrm{Vol}(K)$ is the hyperbolic volume
of the knot complement $S^{3} \setminus K$: a continuous real number
extracted from a Riemannian metric of constant negative curvature. Read
algebraically --- in the register native to the Frobenius--Hopf axioms
--- $\mathrm{Vol}(K)$ is a shadow of a finite sequence of Hecke crossing
resolutions. The Kashaev Volume Conjecture
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
$V_{N-1}$ of $U_{q}(\mathfrak{sl}_{2})$. The standard Markov trace
$\mathrm{tr}_M$ recovers only the $N = 2$ case
([Jones--Markov trace](#thm:jones-markov-trace)); higher colourings
replace $\mathrm{tr}_M$ by the trace $\mathrm{tr}_M^{(N)}$ on the
$V_{N-1}$-coloured closure, and all three --- coloured trace,
categorical $\int_{A}$ on the $N$-th symmetric power, and
$J_{N}$ --- agree. In the QOU setting the left-hand side is the
continuous holonomy term that appears in the archimedean proof of
the mass formula; the right-hand side is a limit of **coloured
Markov traces** in the Iwahori--Hecke algebra $H_{n}(q)$, each still
a categorical $\int_{A}$ evaluation, but on the Hecke image
$\rho(\beta_{K})$ composed with the projector $p_{N-1}$
([Jones--Markov trace](#thm:jones-markov-trace);
[Markov trace product](#thm:markov-trace-product)).

### Inverting the ontology

The Kashaev limit does more than relate two expressions for the same
number: it reverses the usual direction of abstraction. In a
classically hyperbolic account, the volume is fundamental and the Jones
invariants are derivative asymptotic witnesses to it. In the
non-archimedean, algebraically-native register of the QOU the roles
swap:

1. **The trace is fundamental.** The categorical Haar morphism
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
 $V_{N-1}$. The algebraic quantum volume
 $\mathrm{Vol}_{q}(\beta) \in \mathbb{Z}[q^{1/2}, q^{-1/2}]$
 ([algebraic quantum volume](#def:algebraic-quantum-volume)) collects
 these evaluations (across colours and roots of unity) into a
 single object, which embeds into the Habiro ring
 ([Habiro ring](#def:habiro-ring)).
3. **The hyperbolic volume is emergent.** By the Kashaev conjecture,
 $\mathrm{Vol}(K)$ is the asymptotic coefficient of the logarithm of
 these coloured Markov traces as the colour $N \to \infty$. It is
 the macroscopic shadow of an infinite family of finite algebraic
 measurements, not an input to them
 (algebraic volume specialisation).

What the archimedean observer calls "the continuous hyperbolic volume
of the knot complement" is, in the substrate, nothing more than the
accumulated **algebraic drag** generated as the state's representation
is transported by the comultiplication $\Delta$ and sorted by the
$R$-matrix into symmetric and antisymmetric eigenspaces. Each crossing
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

1. *No continuous input.* Every quantity on the right-hand side is
 either a rational function of $q$ ($\rho_{q}$) or a coloured
 Markov trace in $H_{n}(q)$ evaluated at roots of unity
 ([Markov trace product](#thm:markov-trace-product)). The hyperbolic
 volume enters only as the asymptotic coefficient, not as a separately
 posited datum.
2. *The substrate evaluation is finite.* At $q = q_{0}$
 ([substrate parameter](#def:substrate-parameter)) the mass is
 computed directly from $\ln\lvert\mathrm{Vol}_{q_{0}}(\beta_{K})\rvert$
 ([algebraic quantum volume](#def:algebraic-quantum-volume))
 without passing to the Kashaev limit; the Kashaev identity calibrates
 the overall energy scale (route 2 of
 algebraic volume specialisation)
 and fixes the coefficient relating $\rho_{q_{0}}$ to the dimensionful
 mass unit.
3. *Physical prediction vs.\ exact identity.* The Volume--Density form
 is a derived approximation --- the $\approx$ is obligatory --- whose
 error term is controlled by the convergence rate of the Kashaev limit
 and by the higher-order corrections to the topological mass
 decomposition
 ([topological mass](#thm:topological-mass)). The underlying
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
<!-- FILE_END: kashaev-volume-density.md -->

<!-- FILE_START: kashaev-as-archimedean-realization.md -->
The Kashaev volume conjecture is exactly the
[archimedean realization functor](#def:archimedean-realization-functor)
applied to the [algebraic quantum volume](#def:algebraic-quantum-volume)
of a knot. This makes the conjecture's role inside QOU explicit: it
is not an external coincidence between quantum invariants and
hyperbolic geometry, it is the canonical instance of
$\mathcal{R}_{\mathrm{top}}$ on the brane substrate.

**Algebraic side (non-archimedean).** For a hyperbolic knot $K$
presented as the closure of a braid $\mathcal{B}_K$, the colored Jones
polynomial evaluated at the $N$-th root of unity
$q = \exp(2\pi i / N)$ is a discrete algebraic trace over the
local Hecke algebra $H_n(R, q)$
([Jones from Markov trace](#thm:jones-markov-trace)),

$$
  J_N(K)
  \;=\;
  \mathrm{tr}_M\bigl(\rho(\mathcal{B}_K)\bigr)
  \;\in\;\mathbb{Z}[q^{1/2}, q^{-1/2}]\big/\Phi_N(q),
$$

a purely $p$-adic / cyclotomic datum at the $N$-th place of the
[adelic substrate](#def:adelic-substrate). The
algebraic quantum volume $\mathrm{Vol}_q(\mathcal{B}_K)$ packages all
these local data into the global Habiro element.

**Archimedean realization via $\tau$.** Taking the asymptotic
limit $N \to \infty$ is the action of the QOU fibre functor $\tau$
restricted to its archimedean component
$\tau_{\mathrm{arch}} = \pi_\infty \circ \tau$: it discards the
cyclotomic / $p$-adic information and selects the $\mathbb{R}$
component of the adelic ring. The Kashaev–Murakami–Murakami theorem
states the resulting limit equals the hyperbolic volume of the
knot complement,

$$
  \mathrm{Vol}(S^3 \setminus K)
  \;=\;
  2\pi \cdot \lim_{N \to \infty}
  \frac{\log \lvert J_N(K)\rvert}{N}
  \;\in\;\mathbb{R}.
$$

This is precisely $\tau_{\mathrm{arch}}$ on the algebraic
quantum volume — equivalently $\mathcal{R}_{\mathrm{top}}$
applied to the same input
([Vol(K) factors through $\tau$](#prop:vol-through-tau)):

$$
  \mathrm{Vol}(S^3 \setminus K)
  \;=\;
  \tau_{\mathrm{arch}}\bigl(\mathrm{Vol}_q(\mathcal{B}_K)\bigr)
  \;=\;
  (\pi_\infty \circ \tau)\bigl(\mathrm{Vol}_q(\mathcal{B}_K)\bigr)
  \;=\;
  \mathcal{R}_{\mathrm{top}}\bigl(\mathrm{Vol}_q(\mathcal{B}_K)\bigr).
$$

The fibre-functor step $\tau$ is the hyperbolic realization
(Hodge realization at the cusp); $\pi_\infty$ is the
$N \to \infty$ asymptotic projection. $\tau$ is the *only*
archimedean route: there is no Kashaev limit independent of the
fibre functor.

**Physical interpretation.** Compare with
[$q$-Kashaev volume density](#rem:kashaev-volume-density): the
real-valued hyperbolic volume that emerges in the limit is the
inertial mass $\mathfrak{m}$ of the corresponding hadronic state.
The asymptotic limit and the laboratory measurement are the same
operation — both are $\pi_\infty$ — and the Volume Conjecture is
the consistency statement that QOU's archimedean realization of a
braid's motivic data agrees with the hyperbolic geometry of its
knot closure.

The Kashaev limit thus *is* the realization functor of QOU: not an
analogy, an identity.
<!-- FILE_END: kashaev-as-archimedean-realization.md -->

<!-- FILE_START: phi-q-piece.md -->
Let $\beta \in B_n$ be a braid with closure
$\widehat{\beta} = K \subset S^3$ and let
$\{\sigma_0, \dots, \sigma_{n-2}\}$ enumerate its crossings (one
per Hecke generator instance). For each subset
$S \subseteq \{0, \dots, n-2\}$, the **Φ$_q$-piece $K_S \subseteq S^3$**
is the link obtained from $\widehat{\beta}$ by replacing each crossing
$\sigma_i$ with $i \notin S$ by its $L_0$-smoothing (Kauffman skein
resolution [Kauffman bracket](#thm:jones-markov-trace)) while leaving
the crossings $\{\sigma_i : i \in S\}$ intact.

Concretely: let $\beta_S \in B_n$ denote the braid obtained from
$\beta$ by deleting (i.e., replacing by the identity strand) every
$\sigma_i$ with $i \notin S$ and keeping every $\sigma_i$ with $i \in S$.
Then

$$
  K_S \;:=\; \widehat{\beta_S}
  \;\subseteq\; S^3.
$$

The Φ$_q$ tower
([mass endomorphism tower](#prop:mass-endomorphism-tower))
indexes its summands by the *non-empty* subsets with
$\lvert S \rvert \leq 2$ — singletons and pairs — but the
construction above is well-defined for *every* $S$, including
$S = \emptyset$ (the trivial unlink) and $S = \{0, \dots, n-2\}$
(the original closure $K$). The full family $\{K_S\}_{S \subseteq
\{0,\dots,n-2\}}$ is what enjoys the structural properties below;
the truncation $\lvert S \rvert \leq 2$ is a property of the tower,
not of the Φ$_q$-piece itself.

The construction satisfies three structural properties:

1. **Functoriality.** $K_\emptyset$ is the trivial $n$-component
   unlink (no crossings remain); $K_{\{0,\dots,n-2\}} = K$ is the
   original closure.

2. **Subset compatibility.** For $S \subseteq T$ the link $K_S$ is
   obtained from $K_T$ by smoothing every crossing in $T \setminus S$,
   i.e., $K_S = (K_T)_S$.

3. **Categorical interpretation.** The same family $\{K_S\}_S$ is
   the geometric shadow of the Wedderburn-block stratification of the
   transient mass element
   ([categorical mass as Markov trace](#prop:categorical-mass-markov)):
   the spectral coordinate $\prod_{i \in S} \hat{V}_i$ on the algebraic
   side localises geometrically to the link $K_S$.

The piece $K_S$ is the geometric carrier of the per-$S$ summand
$\Phi_q\bigl(\bigl\lvert\prod_{i \in S} \hat{V}_i^{\mathrm{full}}\bigr\rvert\bigr)$
of the Φ$_q$ tower
([mass endomorphism tower](#prop:mass-endomorphism-tower)).
The empty piece $K_\emptyset$ is the descended (level-zero) carrier;
all other $K_S$ with $1 \leq \lvert S \rvert \leq 2$ are the transient
carriers.

The hyperbolic volume $\mathrm{Vol}_{\mathrm{hyp}}(S^3 \setminus K_S)$
of the piece is well-defined whenever the complement is hyperbolic;
when it is not (e.g., when $K_S$ is an unknot or torus link), the
piece contributes zero hyperbolic volume by convention. The Φ$_q$-piece
is the unit on which the archimedean realisation
([archimedean realization functor](#def:archimedean-realization-functor))
acts when restricted to the per-block summands of the tower.

### Motivic interpretation

In motivic language, $\Phi_q$ is the **Faddeev–Kashaev quantum
dilogarithm** [`faddeev1994`] — a $q$-deformation of the Bloch–Wigner
dilogarithm $D_2$ whose pentagon five-term relation is the defining
relation of the quantum Bloch group
([quantum Bloch group](#def:quantum-bloch-group)). The per-piece
summand $\Phi_q(\lvert V_S\rvert)$ is a class in the quantum Bloch
group $\mathfrak{B}(q)$, and the family $\{K_S\}_S$ is the geometric
stratification along which the regulator $\mathfrak{B}(q) \to \mathbb{R}$
decomposes. Recasting the Φ$_q$-piece as a quantum-dilog class fixes
its motivic type and makes the bridge to hyperbolic volume
([Φ$_q$–JSJ bridge](#rem:phi-q-tower-jsj-bridge)) a regulator
statement rather than a coincidence of two evaluation schemes.
<!-- FILE_END: phi-q-piece.md -->

<!-- FILE_START: phi-q-tower-algebraic-stratification.md -->
> **SUPERSEDED-$\rho_q$ note .** Any use of the
> scalar substrate density $\rho_q = 1/\hbar_q^2$ in this block is the
> structurally-wrong leading-order ansatz per
> [`mass-endomorphism-tower.md` §SUPERSEDED](mass-endomorphism-tower.md);
> the canonical replacement is the operator-valued $A^\lambda_{\mu, \nu}(I)$
> graded expansion [`prop:rho-k-graded-expansion`](rho-k-graded-expansion.md).
> Full purge tracking: [`docs/audits/-superseded-rho-q-purge.md`](../../../docs/audits/-superseded-rho-q-purge.md).

**Proposition (algebraic stratification of the Φ$_q$ tower).**
*Let $\beta \in B_n$ be a braid with crossings indexed by
$\{0, \ldots, n-2\}$. Let $H_n(R, q)$ be the Iwahori-Hecke algebra
with Markov trace $\mathrm{tr}_M$ and let $J^\bullet$ be the
Gröbner-Shirshov filtration on $H_n(R, q)$
([graded Markov trace](#prop:graded-markov-trace-from-gs-filtration)).
For each subset $S \subseteq \{0, \ldots, n-2\}$, let
$\beta_S \in B_n$ be the braid obtained from $\beta$ by smoothing
every crossing $i \notin S$ to the identity strand
([Φ$_q$-piece definition](#def:phi-q-piece)). The Φ$_q$-tower
admits a purely algebraic stratification by $|S|$:*

$$
  \mathfrak{m}(\varrho)
  \;=\;
  \underbrace{\bigl\| \mathrm{tr}_M(\rho(\beta_\emptyset))\bigr\|_F}_{\text{descended carrier}}
  \;+\;
  \sum_{|S| = 1} \Phi_q\bigl(\|\hat V_S\|_F\bigr)
  \;+\;
  \sum_{|S| = 2} z^{2} \Phi_q\bigl(\|\hat V_S\|_F\bigr)
$$

*where $\|\cdot\|_F$ denotes the **categorical Frobenius norm**
valued in $\mathbb{Z}[q^{\pm 1/2}]$ — **not** the Archimedean
absolute value — and each summand is an element of
$\mathbb{Z}[q^{\pm 1/2}]$ computed entirely within the Hecke
algebra. The stratification is
indexed by Hecke-tower :refterm[descent]{#descent} levels — singletons (level 1),
adjacent and non-adjacent pairs (level 2) — not by 3-manifold pieces.
Pentagon ascension ([mass endomorphism jet tower](#rem:mass-endomorphism-jet-tower))
guarantees that order-$\geq 3$ defects ascend to level-$(n+1)$
singletons or pairs in the jet tower; no triple or higher term
appears at any fixed level.*

## Content of this block

This is the **algebraic-side reformulation** that the audit's
GAP 8a calls for: every object on the right-hand side lives in
$\mathbb{Z}[q^{\pm 1/2}]$, and every step of the construction is a
Hecke-algebra operation (skein smoothing of a braid word, Markov
trace of an element of $H_n(R, q)$, Laurent expansion in $q^{1/2}$).
The norm $\|\cdot\|_F$ in the formula is the **Frobenius norm**
$\|x\|_F^2 := \langle x, x\rangle_F$, valued in the ground ring;
it is **not** the Archimedean absolute value.  Substitutions like
$q \mapsto q_0 \in \mathbb{R}$ are post-$\tau$ and not used in any
step of this proof.
Three-manifold language ($S^3$, knot complement, hyperbolic volume,
JSJ decomposition) does **not** appear on the algebraic side; it
enters only as the τ-image of the algebraic structure under
$\tau_{\mathrm{arch}}$
(Φ$_q$-tower JSJ archimedean bridge).

## The four levels of the algebraic stratification

|    Level | Index                    | Algebraic content                                                                          | $\mathbb{Z}[q^{\pm 1}]$-class                                                               |
| -------: | ------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------- |
|        0 | $S = \emptyset$          | $\beta_\emptyset$ = trivial $n$-strand identity; $\rho(\beta_\emptyset) = 1 \in H_n(R, q)$ | $\mathrm{tr}_M(1) = 1$                                                                      |
|        1 | $\lvert S \rvert = 1$    | $\beta_{\{i\}} = \sigma_i$; $\rho(\beta_{\{i\}}) \in H_n(R, q)$                            | $\hat V_i = z \cdot a_i + b_i$ ([algebraic quantum volume](#def:algebraic-quantum-volume)) |
|        2 | $\lvert S \rvert = 2$    | $\beta_{\{i, j\}} = \sigma_i \sigma_j$; $\rho(\beta_{\{i, j\}}) \in H_n(R, q)$             | $\hat V_i \hat V_j$ (commutative scalars in $\mathbb{Z}[q^{\pm 1}]$)                        |
| $\geq 3$ | $\lvert S \rvert \geq 3$ | absorbed into level $(n+1)$ via pentagon ascension                                         | n/a (does not appear at level $n$)                                                          |

Each level is a **GS-filtration piece** of $H_n(R, q)$: the
singletons $\sigma_i$ are at GS-degree 1, the pairs $\sigma_i \sigma_j$
at GS-degree 2, and so on. The descended (level-0) carrier is the
identity component, GS-degree 0. The truncation $\lvert S \rvert
\leq 2$ at any fixed jet level is the **categorical content** of
the mass-endomorphism formula
([mass endomorphism tower](#prop:mass-endomorphism-tower)), not a
3-manifold property.

## Significance

* **Discharges audit GAP 8a (wall risk).** The audit's worry was
  that the Φ$_q$-tower reformulation read as 3-manifold/topological.
  This proposition states the same content in pure Hecke-tower /
  GS-filtration language. The 3-manifold picture is the τ-image,
  not the derivation.

* **Decouples the algebraic engine from the JSJ identification.**
  The mass formula computes via algebraic stratification
  (Φ$_q(|\hat V_S|)$ as a Laurent polynomial); the JSJ
  identification of the τ-image is a separate conjecture
  (Φ$_q$-tower JSJ bridge)
  that *interprets* this algebraic structure on the geometric
  side. If the JSJ conjecture remains open, the algebraic mass
  formula is unaffected.

* **Provides the audit with a concrete Hecke-tower structure** for
  every block currently citing "JSJ pieces": replace
  `JSJ piece $P$` with `algebraic stratum $S \subseteq \{0, \ldots, n-2\}$`
  in the algebraic-side narrative; reserve the JSJ language for
  the τ-image discussion.
<!-- FILE_END: phi-q-tower-algebraic-stratification.md -->

<!-- FILE_START: kashaev-volume-conjecture.md -->
> **SUPERSEDED-$\rho_q$ note .** Any use of the
> scalar substrate density $\rho_q = 1/\hbar_q^2$ in this block is the
> structurally-wrong leading-order ansatz per
> [`mass-endomorphism-tower.md` §SUPERSEDED](mass-endomorphism-tower.md);
> the canonical replacement is the operator-valued $A^\lambda_{\mu, \nu}(I)$
> graded expansion [`prop:rho-k-graded-expansion`](rho-k-graded-expansion.md).
> Full purge tracking: [`docs/audits/-superseded-rho-q-purge.md`](../../../docs/audits/-superseded-rho-q-purge.md).

The **Kashaev volume conjecture (KVC)** asserts that, for every
hyperbolic knot $K \subseteq S^3$, the Kashaev limit of the colored
Jones polynomial computes the hyperbolic volume of the complement,

$$
  \mathrm{Vol}_{\mathrm{hyp}}(S^3 \setminus K)
  \;=\;
  2\pi \cdot \lim_{N \to \infty}
  \frac{\log \lvert J_N(K)\rvert}{N},
  \qquad
  J_N(K)\big\vert_{q = \exp(2\pi i / N)},
$$

with the convention that the right-hand side vanishes when $K$ is not
hyperbolic. KVC was conjectured by Kashaev [`kashaev1997`] and reformulated
in terms of the colored Jones polynomial by Murakami–Murakami
[`murakami-murakami2001`]. It is **open in general** (proved only for
specific families: the figure-eight knot, certain torus and pretzel
knots, etc.).

Inside QOU, KVC is the consistency statement that the archimedean
realisation functor $\tau_{\mathrm{arch}} = \pi_\infty \circ \tau$
([archimedean realization functor](#def:archimedean-realization-functor))
applied to the algebraic quantum volume
([algebraic quantum volume](#def:algebraic-quantum-volume))
recovers the hyperbolic volume; this is the content of the per-block
[Kashaev as archimedean realization](#rem:kashaev-as-archimedean-realization)
remark.

### Lean axiomatisation

Per `AGENTS.md` §3b ("Lean formalization of conjectures"), KVC is
encoded in Lean as a **typeclass**

```
class VolumeConjecture (q : ℝ) where
  hypVolume       : Braid → ℝ
  kashaevLimit    : Braid → ℝ
  kvc_holds       : ∀ β, hypVolume β = kashaevLimit β
  hypVolume_nonneg : ∀ β, 0 ≤ hypVolume β
```

The class fields encode the conjectural identification of hyperbolic
volume with the Kashaev limit. Any instance of `VolumeConjecture` is
**conjecture-bearing**: the `kvc_holds` field plays the role of
`sorry`, but as an axiomatised class field rather than a tactic
failure. Downstream results that depend on KVC take it as an
`[VolumeConjecture q]` typeclass argument and are then **fully
verified** by Lean — the only unproved input is the class instance.

This is the same pattern used for `MassEvaluation` in
[mass endomorphism tower](#prop:mass-endomorphism-tower): the
canonical computation is axiomatised so that the algebraic tower
identities are machine-checked.

### Rationale for a class rather than an axiom

Three reasons:

1. **Locality.** A typeclass instance can be supplied per knot family
   (figure-eight, torus, etc.) where KVC is actually proved; downstream
   theorems then specialise to verified ground.

2. **Compositionality.** A bridge theorem of the form
   $\Phi_q(V_S) = \rho_q \cdot \mathrm{Vol}(K_S)$ depends only on KVC
   restricted to $K_S$; the typeclass scope makes that dependency
   visible in the type signature.

3. **No global axiom pollution.** Mathlib's axiom audit
   (`#print axioms`) records typeclass dependencies but does not flag
   them as global axioms; the conditional nature of every downstream
   result is preserved.

The conjecture itself remains open at the level of $\pi_0$ —
no claim of proof is made by introducing the class.

### Motivic perspective

KVC is, in motivic language, a **regulator statement**: the
hyperbolic volume of $S^3 \setminus K$ is the image of a class in
the Bloch group $\mathcal{B}(\mathbb{C})$ under the Borel/Beilinson
regulator $r_\infty$, and the colored Jones polynomial at
$q = \exp(2\pi i / N)$ is the $q$-deformed avatar of that class
[`zagier1986`, `neumann-zagier1985`]. The QOU recasting frames
$\tau_{\mathrm{arch}} = \pi_\infty \circ \tau$ as the archimedean
realisation functor on the algebraic data $\Phi_q(\lvert V_S\rvert)$
— a class in the quantum Bloch group
([quantum Bloch group](#def:quantum-bloch-group)) — landing in
$\mathbb{R}$ as the hyperbolic volume of the corresponding
Φ$_q$-piece. KVC, in this presentation, is the assertion that the
$q$-deformed regulator agrees with the classical one in the Kashaev
limit.
<!-- FILE_END: kashaev-volume-conjecture.md -->

<!-- FILE_START: figure-8-archimedean-illustration.md -->
**Remark (figure-8 knot as the canonical algebraic / archimedean
example).**

The figure-8 knot $4_1$ is the smallest hyperbolic knot
[`thurston1978`] and serves as the cleanest illustration of the
dual existence forced by
[`prop:archimedean-functor-uniqueness`](#prop:archimedean-functor-uniqueness):
*algebraic / motivic in the substrate, transcendental in the
laboratory*.

**Embedding in Bring's surface.** The figure-8 knot embeds smoothly
into Bring's surface (genus $4$) as the amphichiral mass mechanism.
Its braid word $\sigma_1\sigma_2^{-1}\sigma_1\sigma_2^{-1}$ realises
on $4$ strands and the braid closure reproduces $4_1$ inside the
genus-$4$ handlebody. The amphichirality
$4_1 \cong 4_1^{\,\text{mirror}}$ — equivalently, invariance under
the bar involution $q \mapsto q^{-1}$ — is what selects the
figure-8 as a *mass* invariant rather than a chirality invariant.

**Pre-archimedean (substrate) representation.**
On the algebraic side, $4_1$ has a completely rigorous motivic
representation via its Hecke normal form. The
[algebraic quantum volume](#def:algebraic-quantum-volume) of $4_1$
is a finite product of Laurent polynomials,

$$
  \mathrm{Vol}_q(4_1)
  \;=\;
  \prod_{i=0}^{2} \hat{V}_i(q)
  \;\in\;
  \mathbb{Z}[q^{\pm 1/2}],
$$

with the $\hat{V}_i(q)$ explicitly determined by the four-strand
braid word above (cf.
[`thm:markov-trace-factorization`](#thm:markov-trace-factorization)).
At this level no $\pi$, no $\zeta$-values, no real-analytic
transcendentals appear: the entire object is a Laurent polynomial
in $q^{\pm 1/2}$ and lives strictly in the substrate ring $R$.

**Archimedean (laboratory) image.**
Apply the archimedean realization functor $\tau_{\text{arch}} =
\pi_\infty \circ \tau$
([archimedean realization functor](#def:archimedean-realization-functor)).
The image of $\mathrm{Vol}_q(4_1)$ under $\tau_{\text{arch}}$ in
the Faddeev-Kashaev quasi-classical limit is the *hyperbolic
volume* of the figure-8 knot complement
$S^3 \setminus 4_1$
([Kashaev volume conjecture](#conj:kashaev-volume-conjecture)),
which evaluates as the transcendental

$$
  \boxed{\;
    \mathrm{Vol}(4_1)
    \;=\;
    2\,D(\mathrm{e}^{i\pi/3})
    \;=\;
    2\,\mathrm{Cl}_2\!\left(\tfrac{\pi}{3}\right)
    \;\approx\;
    :val[Vol_4_1]{precision=6}\ldots
  \;}
$$

where $D$ is the Bloch-Wigner dilogarithm and $\mathrm{Cl}_2$ is
the Clausen function. The transcendence of $\mathrm{Cl}_2(\pi/3)$
is conjectural in number theory but the *form* of the answer is
forced by Bloch-Suslin pentagon-uniqueness: any archimedean
realization of the substrate's pentagon-coherent class must
factor through $D$, and the figure-8's three ideal-tetrahedron
triangulation pins down the specific shape parameter $z = e^{i\pi/3}$.

**The dichotomy in one line.**
The motivic side guarantees exact, $q$-rational algebraic
relationships governing particle interactions; $\tau_{\text{arch}}$
supplies the transcendental continuum required for geometric
measurement. Both pictures are needed:

| Side | Object for $4_1$ | Lives in | Role |
|---|---|---|---|
| Pre-archimedean | $\mathrm{Vol}_q(4_1) = \prod_i \hat{V}_i(q)$ | $\mathbb{Z}[q^{\pm 1/2}]$ | Exact algebraic identities, mass-formula state sum, Hecke trace |
| Archimedean | $\mathrm{Vol}(4_1) = 2\,\mathrm{Cl}_2(\pi/3)$ | $\mathbb{R}$ (transcendental) | Laboratory mass-scale, Higgs-like amphichiral mechanism |

The bridge between the two columns is uniquely determined by
[`prop:archimedean-functor-uniqueness`](#prop:archimedean-functor-uniqueness):
no other archimedean image is admissible.

**Cross-reference: $\alpha_{EM}$.** The same dichotomy underlies
the additive Bring zero-mode candidate
[`prop:em-coupling-bring-zero-mode`](#prop:em-coupling-bring-zero-mode):
the $\pi$ in $4_1$'s archimedean image
$2\,\mathrm{Cl}_2(\pi/3)$ and the $\pi$ in $1/\alpha_{EM}$'s
correction $2/(3\pi) = 2g/(4\pi(g-1))$ at $g=4$ share a single
provenance — the unique archimedean shadow of pentagon-coherent
substrate data on Bring's surface, factored through the
Bloch-Wigner dilogarithm. The exact algebraic values $:val[Vol_4_1]{precision=6}\ldots =
2\,\mathrm{Cl}_2(\pi/3)$ matches the standard hyperbolic
2-tetrahedra triangulation [`thurston1978`].
<!-- FILE_END: figure-8-archimedean-illustration.md -->

<!-- FILE_START: gb-depth-period-correspondence.md -->
**Conjecture (GS-depth $\leftrightarrow$ Goncharov period-depth correspondence).**

*Let $\mathcal{H}_q$ be the substrate convolution Hopf algebra
([Frobenius–Hopf substrate](#def:frobenius-hopf-substrate)) and let
$G(\mathcal{H}_q)$ be its sub-Hopf-algebra of grouplikes. Filter
$G(\mathcal{H}_q)$ by **iterated-integral depth**:*

$$
  G^{(0)} \;\subseteq\; G^{(1)} \;\subseteq\; G^{(2)} \;\subseteq\; \cdots,
  \qquad
  G^{(n)} \;:=\; \langle\, \exp_q,\, \log_q,\, \mathrm{Li}_2^q,\, \ldots,\, \mathrm{Li}_n^q \,\rangle.
$$

*Let $\tau_{\mathrm{arch}}$ be the archimedean realization functor
([archimedean realization](#def:archimedean-realization-functor)) and
let $\mathcal{P}_\bullet \subset \mathbb{R}$ be Goncharov's period
filtration on the algebra of (real) periods. Then:*

$$
  \boxed{\;\tau_{\mathrm{arch}}\!\left( G^{(n)}(\mathcal{H}_q) \right)
         \;\subseteq\; \mathcal{P}_n,\;}
$$

*and the inclusion is sharp at every depth — for each $n \geq 1$
there exists a grouplike $g \in G^{(n)} \setminus G^{(n-1)}$ whose
$\tau_{\mathrm{arch}}$-image generates a non-trivial class in
$\mathcal{P}_n / \mathcal{P}_{n-1}$.*

### Stratification dictionary

| Depth $n$ | Grouplike at depth $n$ | Goncharov class |
|---|---|---|
| 0 | $\exp_q$, scalars | algebraic numbers |
| 1 | $\log_q$ | $\log\alpha$, $\alpha \in \overline{\mathbb{Q}}$ (Baker class) |
| 2 | $\mathrm{Li}_2^q$ | hyperbolic 3-mfld volumes (Bloch–Wigner regulator) |
| $n$ | $\mathrm{Li}_n^q$ | weight-$n$ multiple polylogs (Goncharov motivic) |

### Structural content of the statement

The classical Mikusiński operational calculus on $C[0,\infty)$ takes
$f * g \mapsto \tilde f \cdot \tilde g$ under Laplace, turning ODEs
into algebra. The categorical analog already in this paper —
[`prop:categorical-laplace-unique`](#prop:categorical-laplace-unique),
[`q-resolvent`](#def:q-resolvent) — does exactly this for $\mathcal{H}_q$.
What it does *not* yet pin down is **which algebraic relations on
$\mathcal{H}_q$ survive $\tau_{\mathrm{arch}}$ and which do not**. The
present conjecture supplies the structural answer:

- A relation $R(g_1,\dots,g_m) = 0$ among grouplikes survives
  $\tau_{\mathrm{arch}}$ iff *all $g_i$ live in the same depth $G^{(n)}$
  and the relation is an algebraic identity in the cellular structure of
  $H_n(q)$* (provable over $\mathbb{Z}[q^{\pm 1}]$).
- A relation that crosses depth or invokes a transcendental
  identity among periods (e.g. the Bloch–Wigner 5-term relation,
  hyperbolic gluing equations) is an **archimedean accident** — it
  holds only in $\mathbb{R}$, not over $\mathcal{H}_q$ generically.

This is the wall-crossing criterion: depth determines what survives.

### Surreal envelope

Lift the standard-part map $\mathrm{std} \colon \mathbf{No} \to \mathbb{R}$
to the level of grouplikes. The depth filtration extends:

$$
  G^{(n)}(\mathcal{H}_q^{\,\mathbf{No}})
  \;\xrightarrow{\;\mathrm{std}\;}\;
  \mathcal{P}_n.
$$

Surreal infinitesimals $1/\omega^k$ sit at depth $k$ as *literal*
infinitesimal scaling factors — there is no recourse to distributions
or limits. The "delta at depth $n$" of graded Mikusiński is the
surreal element $1/\omega^n$, and $\mathrm{std}$ collapses each layer
to its archimedean image. This makes the *algebraic core survives*
mechanism ([algebraic core survives](#rem:algebraic-core-survives))
into a quantitative statement: it survives **at the depth at which it
lives**.

### Existing depth-2 evidence

The paper already records a depth-2 instance in
[`rem:figure-8-archimedean-illustration`](#rem:figure-8-archimedean-illustration):
the figure-8 knot, embedded in Bring's surface, has hyperbolic
volume $2\,\mathrm{Cl}_2(\pi/3) = 2\,\mathrm{Im}\,\mathrm{Li}_2(e^{i\pi/3})$.
One $\mathrm{Li}_2$ factor $\Rightarrow$ iterated-integral depth $2$,
matching the Bloch-regulator class of the archimedean image. See the
explicit canonical witness in
[`conj:bring-figure-eight-depth-2-witness`](#conj:bring-figure-eight-depth-2-witness).

### Discharge targets

**Open.** The conjecture is structural (no concrete computation
suffices to discharge it), but admits a clean reduction to known
period theory:

1. **Inclusion $\tau_{\mathrm{arch}}(G^{(n)}) \subseteq \mathcal{P}_n$:**
   reduces to showing $\tau_{\mathrm{arch}}$ commutes with iterated
   integration; for the categorical Laplace transform this is the
   monoidality result already proved
   ([`prop:categorical-laplace-unique`](#prop:categorical-laplace-unique)).
2. **Sharpness ($\mathcal{P}_n / \mathcal{P}_{n-1}$ non-trivial in
   image):** depth-2 case is the Bloch–Wigner regulator
   ([bloch2000], [suslin1991]) realised by hyperbolic 3-manifolds.
   Higher depths reduce to Goncharov's motivic-Galois action on
   multiple polylogs ([kontsevich1995], Goncharov 2001).

**Two related open questions:**

- *Cellular vs iterated-integral depth.* The cellular GB-depth on
  $Z(H_n(q))$ from
  [`prop:curvature-rank-gb-stratification`](#prop:curvature-rank-gb-stratification)
  (max hook of partition) is a **separate** filtration from the
  iterated-integral depth used here. Their precise relationship —
  e.g. whether amphichiral self-conjugate cells correspond to
  *even* iterated-integral depths — is open.
- *Graded Titchmarsh.* At which iterated-integral depth does the
  $*_q$-product on $\mathcal{H}_q$ first acquire zero divisors?
  This bounds where the graded field-of-fractions tower
  $\mathcal{M}_q^{(0)} \hookrightarrow \mathcal{M}_q^{(1)} \hookrightarrow \cdots$
  is well-defined, and feeds the operational-calculus mechanism
  per the Mikusiński (1959) construction.
<!-- FILE_END: gb-depth-period-correspondence.md -->

<!-- FILE_START: vc-as-depth-2-instance.md -->
**Remark (Volume Conjecture as the depth-2 instance of the GS $\leftrightarrow$
period correspondence).**

The Kashaev–Murakami–Murakami volume conjecture
([`conj:kashaev-volume-conjecture`](#conj:kashaev-volume-conjecture))
admits a clean structural reading inside the graded-Mikusiński
framework
([`conj:gb-depth-period-correspondence`](#conj:gb-depth-period-correspondence)):
*it is the depth-2 case.*

### One-line statement

$$
  \text{Volume Conjecture} \;\;\Longleftrightarrow\;\;
  \tau_{\mathrm{arch}}\!\left( G^{(2)}(\mathcal{H}_q) \right)
  \;\xrightarrow{\;\;}\;
  \mathcal{P}_2 \big/ \mathcal{P}_1
  \;=\; \{\text{hyperbolic 3-manifold volumes}\}.
$$

### Justification of the reading

The Volume Conjecture asserts that the asymptotic growth of the
coloured Jones polynomial $J_K^{(N)}(q)$ at $q = e^{2\pi i / N}$ as
$N \to \infty$ equals $\mathrm{Vol}(S^3 \setminus K)$. The
algebraic side ($J_K \in \mathbb{Z}[q^{\pm 1}]$) is field-polymorphic
and lives in the substrate
([`rem:algebraic-core-survives`](#rem:algebraic-core-survives)). The
geometric side is a real number, transcendental in general.

In graded-Mikusiński terms:

- $J_K^{(N)}$ is built by repeated application of the depth-2
  grouplike $\mathrm{Li}_2^q$ (Faddeev–Kashaev quantum-dilogarithm
  decomposition).
- The asymptotic limit at $q = e^{2\pi i / N}$, $N \to \infty$, is
  the archimedean realization $\tau_{\mathrm{arch}}$ followed by
  std-part on the surreal envelope.
- Single-$\mathrm{Li}_2$ factor $\Rightarrow$ iterated-integral
  depth 2 $\Rightarrow$ Goncharov period-class
  $\mathcal{P}_2 / \mathcal{P}_1$ (Bloch regulator
  $K_3^{\mathrm{ind}}(\overline{\mathbb{Q}}) \otimes \mathbb{Q}
  \to \mathbb{R} / \pi^2 \mathbb{Q}$).

The Volume Conjecture is therefore not a coincidence: hyperbolic
volumes appear at depth 2 because that is structurally where the
Bloch–Wigner regulator lives. Predicted at every depth $n$ is an
analogous statement: *colored quantum invariants built from
$\mathrm{Li}_n^q$ asymptote to weight-$n$ Goncharov periods.*

### Implications of accepting the keystone

The keystone correspondence does **not** prove the Volume Conjecture.
What it does is reduce the conjecture to two structurally smaller
claims:

1. *Categorical Laplace transport.* Show that the asymptotic at
   roots of unity coincides with the categorical Laplace transform
   of $\Phi_q$ followed by std-part — i.e. that the limiting
   procedure is intrinsically the Mikusiński transform applied
   stratum-by-stratum. Already partially in the paper via
   [`prop:categorical-laplace-unique`](#prop:categorical-laplace-unique).
2. *Sharpness at depth 2.* Show that the image of $G^{(2)}$ in
   $\mathcal{P}_2 / \mathcal{P}_1$ contains the Bloch–Wigner
   regulator class of every hyperbolic knot complement. This is the
   modern formulation of Bloch's 1978 conjecture and is a known
   target in motivic cohomology.

The framework thus does not eliminate the open problem — it places
it in its correct depth-graded category, where partial results
already exist (Murakami–Murakami 2001 for the figure-8;
Garoufalidis–Lê for torus knots; many others).

### Cross-reference

For an explicit depth-2 canonical witness on the figure-8 knot
embedded in Bring's genus-4 surface, see
[`conj:bring-figure-eight-depth-2-witness`](#conj:bring-figure-eight-depth-2-witness).
The 50-digit value $2\,\mathrm{Cl}_2(\pi/3) \approx :val[vol_4_1_decimal_50]{precision=6, witness=computations/hyperbolic-volumes.witness.json}\ldots$
is the Bloch regulator class incarnated as a hyperbolic volume.
<!-- FILE_END: vc-as-depth-2-instance.md -->

<!-- FILE_START: bring-figure-eight-depth-2-witness.md -->
**Conjecture (Bring figure-8 volume as depth-2 grouplike value;
50-digit canonical witness).**

*The hyperbolic volume of the figure-8 knot $4_1$ embedded in
Bring's genus-4 surface
([`rem:figure-8-archimedean-illustration`](#rem:figure-8-archimedean-illustration))
equals the standard-part of $2\,\mathrm{Im}\,\mathrm{Li}_2^q$ at the
regular-ideal-tetrahedron shape parameter $z = e^{i\pi/3}$ — the
depth-2 grouplike value predicted by
[`conj:gb-depth-period-correspondence`](#conj:gb-depth-period-correspondence):*

$$
  \mathrm{Vol}(S^3 \setminus 4_1)
  \;=\;
  \mathrm{std}\bigl( 2\,\mathrm{Im}\,\mathrm{Li}_2^q(e^{i\pi/3}) \bigr)
  \;=\;
  2\,\mathrm{Cl}_2\!\left(\tfrac{\pi}{3}\right).
$$

### canonical witness (50-digit precision)

Computed via `exact algebraic structures.polylog` at `mp.dps = 50` (formalism
the canonical formalism,
witness
[`gb-depth-period-bring-fig8.witness.json`](https://github.com/litlfred/qou/blob/main/computations/gb-depth-period-bring-fig8.witness.json)):

$$
  2\,\mathrm{Cl}_2(\pi/3)
  \;=\;
  2.029{,}883{,}212{,}819{,}307{,}250{,}042{,}405{,}108{,}549{,}040{,}571{,}883\ldots
$$

A SnapPy-precision sanity check via independent Clausen-series
partial sum (2 million terms) agrees to $\sim 13$ digits — the
working precision of SnapPy 3.3.2's verified hyperbolic structure.
The 50-digit value is the canonical algebraic computation.

### Depth correspondence

| Side | Object | Depth |
|---|---|---|
| Algebraic | $2\,\mathrm{Li}_2^q(e^{i\pi/3}) \in G^{(2)}(\mathcal{H}_q)$ | iterated-integral depth $= 2$ |
| Archimedean | $\mathrm{Vol}(4_1) \in \mathcal{P}_2 / \mathcal{P}_1$ | Goncharov period-depth $= 2$ |

A single $\mathrm{Li}_2$ factor on the algebraic side maps to a
single Bloch-regulator class on the geometric side: depth $2 = 2$
match, by construction of the Bloch–Wigner regulator
([bloch2000], [suslin1991]).

### Bring-specific significance

The figure-8 knot is the canonical knot-theoretic witness for
Bring's surface in this paper
([`def:brings-coordinate-ring`](#def:brings-coordinate-ring)). Its
4-strand braid word $\sigma_1\sigma_2^{-1}\sigma_1\sigma_2^{-1}$
realises inside the genus-4 handlebody, and amphichirality
$4_1 \cong 4_1^{\,\mathrm{mirror}}$ pins it as a *mass invariant*
rather than a chirality invariant. Two structural facts already in
the paper are consistent with the depth-2 reading:

- The $\pi$ in $\mathrm{Vol}(4_1) = 2\,\mathrm{Cl}_2(\pi/3)$ and the
  $\pi$ in the Bring zero-mode $\alpha_{EM}$ correction
  $2g/(4\pi(g-1))|_{g=4} = 2/(3\pi)$ share a single provenance — the
  unique archimedean shadow of pentagon-coherent substrate data on
  Bring's surface (cf.
  [`rem:figure-8-archimedean-illustration`](#rem:figure-8-archimedean-illustration)).
- Both factor through the Bloch–Wigner dilogarithm at a Bring shape
  parameter — exactly the depth-2 grouplike of $\mathcal{H}_q$.
### Cross-reference: deeper-depth Bring instances (open)

The keystone predicts analogous canonical witnesses at every depth:

| Depth | Bring object | Predicted std-image |
|---|---|---|
| 2 | figure-8 in genus-4 ($4_1$) | $2\,\mathrm{Cl}_2(\pi/3) \approx 2.02988\ldots$ (confirmed) |
| 3 | $\mathrm{Li}_3$ at $\zeta_5$ ($S_5$-natural Bring root of unity) | $\mathrm{Im}\,\mathrm{Li}_3(\zeta_5) \in \mathcal{P}_3/\mathcal{P}_2$ |
| $n$ | $\mathrm{Li}_n^q$ at the $S_5$-orbit of $\zeta_5$ | weight-$n$ Goncharov motivic period |

**Depth-2 ceiling for hyperbolic 3-manifold volumes.** *All* hyperbolic
3-manifold volumes (figure-8, Borromean rings = $8G$, Whitehead link,
$\ldots$) are depth-2 periods — one $\mathrm{Li}_2$ factor in their
Bloch–Wigner formula. Different knots correspond to different shape
parameters at the same depth. A genuine depth-3 witness therefore
requires either (a) a trilog $\mathrm{Li}_3$ at an algebraic argument,
(b) a Chern–Simons invariant (the depth-3 part of the complexified
volume $\mathrm{CS} + i\,\mathrm{Vol} \in \mathbb{C}/\pi^2\mathbb{Z}$),
or (c) a multiple zeta value such as $\zeta(3)$. The Bring-natural
choice is (a) at the primitive 5th root of unity $\zeta_5$ — see
[`conj:bring-trilog-depth-3-witness`](#conj:bring-trilog-depth-3-witness).
<!-- FILE_END: bring-figure-eight-depth-2-witness.md -->

<!-- FILE_START: kashaev-density-equals-sdp-multiplicity.md -->
**Conjecture (Rule 14 conditional adoption — owner authorised).**
Under the Kashaev volume conjecture
([`conj:kashaev-volume-conjecture`](#conj:kashaev-volume-conjecture))
applied to an atomic Hecke element $T_w$ with `Markov closure` knot/link
$K_w$, the multiplicative density prefactor
$\rho_F \in \mathbb{Z}_{>0}$ in the binding-energy formula

$$
  B_{\mathrm{pred}}(K_w)
  \;=\;
  \rho_F \cdot m_e \cdot \mathrm{Vol}_{\mathrm{hyp}}(K_w)
$$

equals the **joint-tower SDP Wedderburn multiplicity** $\nu_{\mathrm{SDP}}(K_w)$
of the canonical Hecke element $T_w$'s saturating SDP solution in the
$H_{n}(q)$ Wedderburn decomposition:

$$
  \rho_F  \;=\;  \nu_{\mathrm{SDP}}(K_w)
$$

per [`atom-knot-mass-derivation`](#prop:atom-knot-mass-derivation)
§Algorithm step 3 (the joint-tower SDP solve that produces
$\nu_{\mathrm{SDP}}$ as a non-negative integer multiplicity).

## Evidence (three confirmed atoms)

The identity is exact on the three SDP-confirmed
hyperbolic atoms (per
[`atom-knot-mass-derivation`](#prop:atom-knot-mass-derivation) line 265):

| Atom | $K_w$ | $\rho_F$ (legacy) | $\nu_{\mathrm{SDP}}$ |
|------|-------|-------------------|----------------------|
| ${}^{2}\mathrm{H}$ (D)  | knot $6_2$        | 1 | 1 |
| ${}^{3}\mathrm{H}$ (T)  | knot $8_{11}$     | 2 | 2 |
| ${}^{3}\mathrm{He}$     | link $L_{6a4}$    | 2 | 2 |

The ${}^{4}\mathrm{He}$ case uses the magic $A \cdot 8G$ closure rule rather than a
census knot, so its $\nu_{\mathrm{SDP}}$ value is **extrapolated**
($\rho_F = 2$ assumed); R&D follow-up is to extend the joint-tower
SDP solver to confirm $\nu_{\mathrm{SDP}}(⁴\mathrm{He}) = 2$.

## Categorical home (driver x of the 13-driver menu)

This identity falls under driver (x) **MacMahon-style
partition-algebra identities** of the canonical-derivation menu
([`docs/audits/-lambda-scale-canonical-unification.md`](../../docs/audits/-lambda-scale-canonical-unification.md)).
The Wedderburn multiplicity of $T_w$'s SDP solution is a
partition-algebra count: it is the dimension of the saturating
projection in the irreducible-block decomposition
$H_n(q) \cong \bigoplus_{\lambda \vdash n} \mathrm{End}(V_\lambda)$.
The agreement with the Kashaev density factor pulls
$\rho_F$ onto driver (x) and removes it from the Rule-14 escalation
queue.

## Conditional structure

The conjecture is **conditional on the joint-tower SDP completeness**:
i.e. the joint-tower SDP solver in
the canonical formalism
(when it lands; R&D in progress) gives a unique non-negative integer
$\nu_{\mathrm{SDP}}(K_w)$ for every bound-state knot $K_w$. Until R5-full
SDP ships, the identity is verified on three census atoms and
extrapolated to ${}^{4}\mathrm{He}$ with explicit caveat. The Lean class axiomatises

```lean
class KashaevDensityEqualsSDPMultiplicity
    (M : Type*) [BrCategory M] [Hecke M] [KashaevVolumeConjecture M] where
  /-- The joint-tower SDP multiplicity ν_SDP(K_w) of the canonical
      Hecke element T_w's saturating SDP solution. -/
  nu_sdp : ∀ (K : Knot), ℕ
  /-- ν_SDP equals the Kashaev density prefactor ρ_F. -/
  identity :
    ∀ (K : Knot),
      kashaev_density_prefactor K = nu_sdp K
```

per AGENTS.md §3b ("class is inhabited"); the only `sorry` is the
class instance, which closes when R5-full canonical knot solver
produces certified $\nu_{\mathrm{SDP}}$ values.

## Resolution of the Rule-14 escalation

Pre- the
the canonical formalism
formalism self-declared the density rule $\rho_F \in \{1, 2\}$ as
*"pending formal justification"* (line 23) — an open Rule-14
violation per the canonical-derivation discipline. With this
conjecture-conditional adoption, $\rho_F$ is:

1. **named canonically** (`nu_sdp` in the new code), connecting to the
   existing `ν_SDP` notation in
   [`atom-knot-mass-derivation`](#prop:atom-knot-mass-derivation);
2. **placed on the 13-driver menu** (driver x, MacMahon partition algebra);
3. **conditional on a class** that R5-full SDP will eventually
   inhabit — replacing the open-ended "pending formal justification"
   with an auditable conjecture-conditional dependency.

Owner authorised this adoption per Rule-14 procedure
, in response to
[`docs/audits/-rule14-kashaev-density.md`](../../docs/audits/-rule14-kashaev-density.md)
§Recommendation.

## Notation hazard resolved

Prior to this block, three distinct quantities used the symbol $\rho$
in QOU compute and content (per
[`atom-knot-mass-derivation`](#prop:atom-knot-mass-derivation) §Notation):

- $\nu_{\mathrm{SDP}}$ — integer Wedderburn multiplicity (this conjecture)
- $\rho_K$ — CODATA-fit density per knot
- $\rho_F$ — Kashaev prefactor in the formal derivation (unnamed, compute-only)

The renamed compute field (`rho_factor` $\to$ `nu_sdp` in
the canonical formalism
ATOM_ASSIGN) consolidates around the canonical $\nu_{\mathrm{SDP}}$ name,
removing the third unnamed $\rho$.

## Consumers

- the canonical formalism
  — ATOM_ASSIGN.`nu_sdp` field (renamed from `rho_factor` in the same
  PR that introduces this block)
- the canonical formalism
  — reads `nu_sdp` and emits `B_pred = nu_sdp · m_e · Vol(K)`
- [`atom-knot-mass-derivation`](#prop:atom-knot-mass-derivation)
  §Algorithm step 3 — supplies $\nu_{\mathrm{SDP}}$ via joint-tower SDP

## Open R&D

1. **Extend joint-tower SDP to ${}^{4}\mathrm{He}$** — confirm
   $\nu_{\mathrm{SDP}}(⁴\mathrm{He}) = 2$ explicitly (currently
   extrapolated from D/T/${}^{3}\mathrm{He}$ pattern).
2. **Extend joint-tower SDP to ${}^{5}\mathrm{Li}$, ${}^{6}\mathrm{Li}$, ${}^{7}\mathrm{Li}$** — the A$\in${5,6,7} gap
   per
   [`docs/audits/-a5-a7-isotope-wiring-gap.md`](../../docs/audits/-a5-a7-isotope-wiring-gap.md)
   needs $\nu_{\mathrm{SDP}}$ values; the wider atom$\to$knot census Rule-14
   escalation per
   [`docs/audits/-rule14-atom-knot-census.md`](../../docs/audits/-rule14-atom-knot-census.md)
   recommends waiting for R5-full SDP (owner-decided).
3. **Extend joint-tower SDP to α-cluster atoms (${}^{8}\mathrm{Be}$ and up)** — the
   α-cluster rule inherits $\rho_F = 2$ from ${}^{4}\mathrm{He}$; verifying
   $\nu_{\mathrm{SDP}} = 2$ across the α-cluster recursion would close
   the inheritance step.

## Cross-references

- Rule-14 escalation:
  [`docs/audits/-rule14-kashaev-density.md`](../../docs/audits/-rule14-kashaev-density.md)
- Sibling Rule-14 escalation (deferred to R5-full SDP):
  [`docs/audits/-rule14-atom-knot-census.md`](../../docs/audits/-rule14-atom-knot-census.md)
- 13-driver menu (driver x — MacMahon partition algebra):
  [`docs/audits/-lambda-scale-canonical-unification.md`](../../docs/audits/-lambda-scale-canonical-unification.md)
- Coordination ledger:
  [`docs/coordination/-post-1089-followups-ledger.md`](../../docs/coordination/-post-1089-followups-ledger.md)
- Underlying Kashaev volume conjecture:
  [`kashaev-volume-conjecture`](kashaev-volume-conjecture.md)
- $\nu_{\mathrm{SDP}}$ algorithmic definition:
  [`atom-knot-mass-derivation`](atom-knot-mass-derivation.md)
  §Algorithm step 3
<!-- FILE_END: kashaev-density-equals-sdp-multiplicity.md -->


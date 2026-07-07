<!-- FILE_START: q-special-functions-dilog-intro.md -->
The previous sub-section established the $q$-exponential and
$q$-logarithm (existence + uniqueness theorems, plus the $p$-adic
and finite-field obstructions to naïve specialisation). This
sub-section introduces the $q$-dilogarithm — the framework's
central transcendental object — with the existence + uniqueness
theorems and the SU(2) specialisation that anchors the
dilogarithm to a concrete structure. The closing
*generating-functions-solve-Reeb-flow* result ties the dilogarithm
back to the differential-structures Reeb derivation (preceding
section), completing the round trip from the differential
machinery to the central transcendental object.

The output is the $q$-dilogarithm $\mathrm{Li}_2^q$ as a morphism
in $\mathrm{End}_{\mathbf{C}}(A)$, together with its
$\mathrm{SU}(2)$ specialisation and the Reeb-flow PDE
characterisation that pins it.  The $q$-geometric-Langlands
chapter consumes $\mathrm{Li}_2^q$ as the depth-2 modular cocycle
underlying the spectral / automorphic pairing; the
mass-endomorphism chapter consumes it via the
quantum-dilogarithm contribution to the topological mass
integrand.
<!-- FILE_END: q-special-functions-dilog-intro.md -->

<!-- FILE_START: q-dilogarithm.md -->
The $q$-shuffle Hopf algebra $\mathcal{H}_q$
([$q$-exponential](#def:q-exponential),
[$q$-logarithm](#def:q-logarithm)) admits a canonical *level-2* element
obtained by iterating its primitive structure once. A
**level-$k$ primitive** of $\mathcal{H}_q$ is an element
$p_k \in \mathcal{H}_q^{\otimes k}$ satisfying the shuffle recursion

$$
  \Delta_q(p_k) \;=\; p_k \otimes 1 + 1 \otimes p_k + \sum_{i=1}^{k-1}
    p_i \otimes p_{k-i},
$$

with $p_0 = 1$ and $p_1 = \log_q$; the solution space at each level is
one-dimensional (up to primitives of lower levels). The
**$q$-dilogarithm** is the unique level-2 primitive

$$
  \mathrm{Li}_2^q \;\in\; \mathcal{H}_q^{\otimes 2}
$$

normalised by the five-term *pentagon* relation

$$
  \mathrm{Li}_2^q(y) + \mathrm{Li}_2^q(x)
  \;=\;
  \mathrm{Li}_2^q(xy) + \mathrm{Li}_2^q\!\left(\frac{x(1-y)}{1-xy}\right)
  + \mathrm{Li}_2^q\!\left(\frac{y(1-x)}{1-xy}\right),
$$

which pins $\mathrm{Li}_2^q$ up to a scalar.
<!-- FILE_END: q-dilogarithm.md -->

<!-- FILE_START: q-dilogarithm-pentagon-associator.md -->
The pentagon relation normalising the
([$q$-dilogarithm](#def:q-dilogarithm)) is the Hopf-algebraic avatar of
the *pentagon axiom* for the
:refterm[monoidal category]{#monoidal-category} $\mathbf{C}$: $\mathrm{Li}_2^q$
is the unique level-2 primitive compatible with the monoidal associator
$\alpha_{X,Y,Z}$.

```tex
\begin{equation}\label{eq:q-dilog-pentagon}
\begin{tikzcd}[row sep=2.5em, column sep=2em]
  (X \otimes Y) \otimes (Z \otimes W)
    \ar[r, "\alpha"]
    \ar[d, "\alpha \otimes \mathrm{id}"']
  &  X \otimes (Y \otimes (Z \otimes W))
    \ar[d, "\mathrm{id} \otimes \alpha"]
  \\
  ((X \otimes Y) \otimes Z) \otimes W
    \ar[r, "\alpha"']
  &  X \otimes ((Y \otimes Z) \otimes W)
\end{tikzcd}
\qquad
\leftrightarrow
\qquad
\mathrm{Li}_2^q\text{-pentagon}
\end{equation}
```
<!-- FILE_END: q-dilogarithm-pentagon-associator.md -->

<!-- FILE_START: q-dilogarithm-properties.md -->
The universal R-matrix of
$U_q(\mathfrak{sl}_2)$ admits the Faddeev--Kashaev factorisation

$$
  \mathcal{R} \;=\; q^{H \otimes H / 2}  \exp_q\!\bigl((q - q^{-1}) E \otimes F\bigr),
$$

and the *logarithm* of $\mathcal{R}$ is, at leading order in the
adjoint action, the $q$-dilogarithm. Hence $\mathrm{Li}_2^q$ is the
categorical *braiding potential*: its derivative along $E \otimes F$
recovers the braiding of two quantum-plane modules.
<!-- FILE_END: q-dilogarithm-properties.md -->

<!-- FILE_START: q-dilog-habiro-ring.md -->
**Base-ring independence.** Like $\exp_q$ and $\log_q$,
$\mathrm{Li}_2^q$ is defined abstractly as an iterated primitive of
$\mathcal{H}_q$ — its existence and uniqueness are Hopf-algebraic, not
analytic. Over $\mathbb{F}_p$ the pentagon identity is a polynomial
equation over the base ring, solvable as long as the denominators
$1 - xy, [n]_q$ do not vanish; outside those loci $\mathrm{Li}_2^q$
descends to a finite-field element.

**Native algebraic home: the Habiro ring.**
*The series $\mathrm{Li}_2^q(x) = \sum_{n \geq 1} x^n / (n\,[n]_q)$
has $q$-Pochhammer denominators (each $[n]_q$ is a cyclotomic
factor), so its formal-series coefficients lie in
$\mathbb{Z}[q^{\pm 1}, (q-q^{-1})^{-1}]$ and the partial sums are
coherent modulo $((q;q)_m)$ as $m \to \infty$. Thus
$\mathrm{Li}_2^q(x)$ is accordingly an element of the Habiro ring
$\widehat{\mathbb{Z}[q]}[\![x]\!]$
([Habiro ring](#def:habiro-ring)) of formal power series with
Habiro-completed coefficients. This is the algebraic home that
makes "evaluation at any root of unity" well-defined without
invoking $\mathbb{C}$: the projection $\widehat{\mathbb{Z}[q]} \to
\mathbb{Z}[q]/\Phi_N(q)$ at the $N$-th cyclotomic ideal sends
$\mathrm{Li}_2^q$ to its level-$N$ truncated dilogarithm,
recovering Kontsevich–Zagier mod-$p$ and the colored-Jones
asymptotic data without any analytic continuation.*
<!-- FILE_END: q-dilog-habiro-ring.md -->

<!-- FILE_START: q-dilog-three-contexts.md -->
**Three-context behaviour (downstream realisations).** The series
$\mathrm{Li}_2^q(x) = \sum x^n / (n [n]_q)$ carries an *extra* factor
of $n$ in the denominator, so its convergence in char $p$ and $p$-adic
settings is slightly worse than that of $\exp_q$:

* **$\mathbb{F}_p$.** Fails at $n = p$ (because $p = 0$) and at
 $n = \mathrm{ord}_{\mathbb{F}_p^\times}(q)$; replaced by the
 polynomial truncation $\mathrm{Li}_2^{q,(p)}(x) = \sum_{n=1}^{p-1} x^n / (n [n]_q)$,
 which retains the pentagon identity modulo $x^p = 0$. The
 **Kontsevich--Zagier mod $p$ dilogarithm** is the corresponding
 object at $q = 1$; $\mathrm{Li}_2^{q,(p)}$ is its $q$-deformation.
* **$\mathbb{Q}_p$.** For $q \in 1 + p\mathbb{Z}_p$ and
 $v_p(x) \ge 1$, converges with valuation
 $v_p(x^n / (n[n]_q)) \ge n - 2 v_p(n) - v_p(n!)/(p-1)$. The pentagon
 identity holds identically in $\mathbb{Q}_p[\![x,y]\!]$ restricted to
 $p\mathbb{Z}_p \times p\mathbb{Z}_p$. This is Coleman's $p$-adic
 dilogarithm in the $q$-deformed form.
* **$\mathbb{C}_p$.** Converges on $v_p(x) > 1/(p-1)$ (same radius as
 $\exp_q$; the extra $n$ in the denominator shifts the boundary
 slightly inward at the cutoff $n = p$ but does not change the
 asymptotic). Beyond the disc, $\mathrm{Li}_2^q$ extends to
 $\mathbb{C}_p$ via the pentagon identity and an Iwasawa-style branch
 choice.
<!-- FILE_END: q-dilog-three-contexts.md -->

<!-- FILE_START: q-dilog-archimedean.md -->
Over $\mathbb{C}$ the $q$-dilogarithm is
represented by the convergent series

$$
  \mathrm{Li}_2^q(x) \;=\; \sum_{n \ge 1} \frac{x^n}{n  [n]_q}
  \qquad (|x| < 1,  q \ne 1),
$$

sometimes called the *Kirillov dilogarithm*. At $q = 1$ this reduces
to the classical dilogarithm $\mathrm{Li}_2(x) = \sum x^n / n^2$.
<!-- FILE_END: q-dilog-archimedean.md -->

<!-- FILE_START: q-dilog-heat-partition.md -->
The Laplace transform
([categorical Laplace transform](#def:categorical-laplace)) of the
$q$-heat kernel ([Peter--Weyl heat kernel](#prop:q-heat-kernel-peter-weyl))
involves the resolvent $(\widehat{\Delta_q} + s)^{-1}$, whose
contour integral against the spectrum picks up a logarithmic branch
at each eigenvalue $\lambda_j(q)$. Summing these logarithms over
$j \in \widehat{G}$ produces a generating function that is
precisely the $q$-dilogarithm of $\exp(-s t_P(q))$. In short:
$\mathrm{Li}_2^q$ is the *partition function* of the $q$-heat flow,
and the pentagon identity is the monoidal compatibility of heat
flows on tensor-product state spaces.
<!-- FILE_END: q-dilog-heat-partition.md -->

<!-- FILE_START: q-dilog-physical-meaning.md -->
The $q$-dilogarithm is the generating
function for Bethe-ansatz energies in integrable lattice models
governed by $U_q(\mathfrak{sl}_2)$. In the QOU context, it
organises the one-loop correction to the Reeb-flow entropy on
the substrate — the leading non-trivial term in
$\log Z_q(\beta)$ past the classical and first quantum
($\hbar_q$) corrections.
<!-- FILE_END: q-dilog-physical-meaning.md -->

<!-- FILE_START: q-dilogarithm-exists.md -->
Over a base ring $R$ satisfying the hypotheses of
([existence of $\log_q$](#prop:q-logarithm-exists)), there exists a
level-2 iterated primitive $\mathrm{Li}_2^q \in \mathcal{H}_q^{\otimes 2}$
([$q$-dilogarithm](#def:q-dilogarithm)) satisfying the pentagon
identity.

Uniqueness is
([uniqueness of $q$-dilogarithm](#prop:q-dilogarithm-unique)).
<!-- FILE_END: q-dilogarithm-exists.md -->

<!-- FILE_START: q-dilogarithm-unique.md -->
The [$q$-dilogarithm](#def:q-dilogarithm) $\mathrm{Li}_2^q$, as a
level-2 iterated primitive normalised by the pentagon identity, is
unique up to scalar.  Any two solutions of the shuffle recursion
satisfying the pentagon identity differ by a level-1 primitive
(absorbed into the normalisation), hence coincide up to a fixed
scalar in $R$.
<!-- FILE_END: q-dilogarithm-unique.md -->

<!-- FILE_START: generating-functions-solve-reeb-flow.md -->
The three principal $q$-generating functions of the substrate —
the $q$-exponential, the $q$-dilogarithm, and the categorical
Fourier transform — are not just convenient combinatorial
objects.  They are the **exact algebraic solutions** to the three
characteristic flow equations on the Reeb bundle, evaluated
*before* the archimedean realisation.  This remark collects the
three identifications in one place and links them to the
algebraic-substrate framework
([vertex is the exceptional divisor](#prop:vertex-is-exceptional-divisor),
[Habiro ring](#def:habiro-ring)).

**1.  $\exp_q$ solves the base Reeb flow.**
The $q$-exponential $\exp_q(x) = \sum_{n \geq 0} x^n/[n]_q!$
([$q$-exponential](#def:q-exponential)) is the unique grouplike
satisfying $D_q \exp_q = \exp_q$
([$q$-exponential uniqueness](#prop:q-exponential-unique)).
Acting on a substrate coordinate $Z$ inside the Reeb bundle, this
identity is the formal solution of the base Reeb-flow equation
$L_{\xi_q} Z = J\,\hbar_q Z$: the categorical Reeb derivation
$\xi_q$ is exponentiated by $\exp_q$, producing the
one-parameter group $\phi^q_t$ that drives the
color-twist rotation
([$q$-Reeb flow on color coords](#def:q-reeb-flow-on-color-coords)).

**2.  Categorical Fourier diagonalises the $q$-heat equation.**
The $q$-heat equation $\partial_t u = -\Delta_q u$
([$q$-heat equation](#def:q-heat-equation)) governs the
diffusion-like dissipative shadow of the Reeb flow on
$\mathbf{Rep}(\mathrm{SU}_q(2))$.  The categorical Fourier
transform
([categorical Fourier transform](#def:categorical-fourier),
[categorical Fourier existence](#prop:categorical-fourier-exists))
diagonalises the $q$-Laplacian $\Delta_q$ on each Peter–Weyl
isotypic component $V_j$ with eigenvalue $\lambda_j(q)$, so the
$q$-heat equation reduces to a family of one-dimensional ODEs
$\partial_t \pi_j(u) = -\lambda_j(q) \pi_j(u)$ with closed-form
solution $\pi_j(u_0) e^{-\lambda_j(q) t}$.  The full evolution is
the eigenfunction expansion

$$
  u(t) \;=\; \sum_j e^{-\lambda_j(q) t}\,\pi_j(u_0).
$$

**3.  $\mathrm{Li}_2^q$ is the volumetric partition function.**
The $q$-dilogarithm $\mathrm{Li}_2^q(z) = \sum_{n \geq 1} z^n/(n[n]_q)$
([$q$-dilogarithm](#def:q-dilogarithm),
[$q$-dilogarithm uniqueness](#prop:q-dilogarithm-unique)) is the
formal antiderivative of $\log_q(1+t)/t$ in the Habiro completion.
It evaluates the *volumetric expansion* of the Reeb-heat flow: as
the trajectory traverses the divisor and the resolved defect
expands, the cumulative volume is

$$
  V(\beta) \;=\; -\mathrm{Li}_2^q(-V_0(\beta)),
$$

with $V_0$ the bare crossing volume of the braid $\beta$.  Under
the archimedean realisation functor $\tau_\infty \colon
\widehat{\mathbb{Z}[q]} \to \mathbb{C}[\![q-1]\!]$ — the $q \to 1$
limit along the real ray, which sends a Habiro-ring element to its
convergent analytic germ at $q = 1$ — this collapses to the Bloch–Wigner
dilogarithm
$D(z) = \Im\,\mathrm{Li}_2(z) + \arg(1-z)\log|z|$ that gives the
Thurston volume sum
([Thurston volume additivity](#prop:thurston-volume-additivity)).
The categorical $\mathrm{Li}_2^q$ is therefore the substrate-level
parent of every hyperbolic-volume computation in the paper:
$V_{\mathrm{hyp}}(K) = \tau_\infty \circ \mathrm{Li}_2^q$ of the
crossing chart.

**4.  Habiro ring as the algebraic home.**  All three generating
functions live in the Habiro ring
$\widehat{\mathbb{Z}[q]} = \varprojlim_n \mathbb{Z}[q]/((q;q)_n)$
([Habiro ring](#def:habiro-ring)) and its $z$-completion
([$z$-Habiro ring](#def:z-habiro-ring)).  This is what
"before the Archimedean wall" means concretely: the Reeb-flow
solutions are formal series with integer coefficients in $q$,
not $C^\infty$ functions of a real variable.  The wall is the
archimedean realisation functor $\tau_\infty$ above (the $q \to 1$
Taylor germ from $\widehat{\mathbb{Z}[q]}$ to the analytic
completion $\mathbb{C}[\![q-1]\!]$).  This local $q \to 1$
realisation is the archimedean-place shadow of the global adelic
realization functor $\mathcal{R}_{\mathrm{top}}$ developed in the
mass-theory chapter
(cf. [archimedean realization functor](#def:archimedean-realization-functor));
the two are not identified here.
The categorical Reeb-flow PDE has an *exact* algebraic solution
$\exp_q \cdot \mathrm{Li}_2^q \cdot \mathcal{F}_q$ in the Habiro
ring; its analytic shadow at $q \to 1$ is the convergent
power-series solution that classical PDE theory provides
*after* the realisation.

**Significance.**  This identification is the substantive
content of the "generating functions are the Reeb-flow
solutions" claim: it says the three principal special functions
of the framework are not chosen for combinatorial convenience —
they are the unique algebraic objects in the Habiro completion
satisfying the categorical evolution equations on
$\mathbf{Rep}(\mathrm{SU}_q(2))$ that the Reeb structure imposes.
Coupled with
[vertex is the exceptional divisor](#prop:vertex-is-exceptional-divisor)
(which restricts all interactions to the Reeb bundle), this
explains why the algebraic substrate of the paper consists of
exactly these three transforms.

**Lean synthesis class.**  The joint claim — that the three
solutions exist in a common Habiro completion and that their
archimedean shadows under $\tau_\infty$ are mutually compatible —
is captured by the Lean class `QOU.Habiro.HabiroFlowSolution`
(file `lean/QOU/Habiro/FlowSolution.lean`).  The per-function
fixed-point properties are already supplied by the existing
Lean developments
`QOU.QExponential`, `QOU.QDilogarithm`, and
`QOU.CategoricalFourier`
(structures, not typeclasses — the synthesis class does not
extend them, it bundles their proven content into a single
joint-existence claim).  This is a ansatz for the full
formalisation: the individual existence/uniqueness theorems are
already in scope, so any instance of
`HabiroFlowSolution` is conditional on the archimedean realisation
functor $\tau_\infty$ commuting with the three Habiro-ring
constructions (open conjecture; cf. the global adelic
[archimedean realization functor](#def:archimedean-realization-functor)
of the mass-theory chapter).
<!-- FILE_END: generating-functions-solve-reeb-flow.md -->

<!-- FILE_START: archimedean-realisation-volume-compatibility.md -->
Two archimedean realisations act on the substrate $q$-volume of a QOU
braid/knot, along *different* source and target types:

- the **local** archimedean realisation functor $\tau_\infty \colon
  \widehat{\mathbb{Z}[q]} \to \mathbb{C}[\![q-1]\!]$ (the $q \to 1$ Taylor
  germ), applied to the Habiro-ring volume
  $V(\beta) = -\mathrm{Li}_2^q(-V_0(\beta))$
  ([$q$-dilogarithm](#def:q-dilogarithm),
  [generating functions solve the Reeb flow](#rem:generating-functions-solve-reeb-flow));
- the **global** archimedean realization functor
  $\mathcal{R}_{\mathrm{top}} \colon \widehat{\mathcal{M}} \to \mathbb{R}$
  ([archimedean realization functor](#def:archimedean-realization-functor)),
  applied to the motivic volume class $\mu(\beta) \in \widehat{\mathcal{M}}$.

Because their types differ ($\widehat{\mathbb{Z}[q]} \to
\mathbb{C}[\![q-1]\!]$ versus $\widehat{\mathcal{M}} \to \mathbb{R}$), the
two functors are **not** equal as functors. The substantive claim is that
they agree *as real-valued volume observables* on the QOU volume classes.

**Conjecture.** *For every QOU braid $\beta$, the archimedean value of the
Habiro-ring volume under $\tau_\infty$ and the topological realization of the
motivic volume under $\mathcal{R}_{\mathrm{top}}$ coincide, and both equal the
Bloch–Wigner / Thurston hyperbolic volume of the associated hyperbolic piece:*

$$
  \mathrm{ev}_{q \to 1}\bigl(\tau_\infty(-\mathrm{Li}_2^q(-V_0(\beta)))\bigr)
  \;=\;
  \mathcal{R}_{\mathrm{top}}\bigl(\mu(\beta)\bigr)
  \;=\;
  V_{\mathrm{hyp}}(K_\beta),
$$

*naturally in $\beta$ — i.e. $\tau_\infty \circ (-\mathrm{Li}_2^q \circ (-V_0))$
and $\mathcal{R}_{\mathrm{top}} \circ \mu$ are the same map on the QOU volume
classes $\widehat{\mathcal{M}}_{\mathrm{QOU}}$.*

**Scaffolding (established).** Both maps are well defined: $\tau_\infty$ is the
Habiro $q \to 1$ evaluation, and $\mathcal{R}_{\mathrm{top}} = \pi_\infty \circ
\chi_{\mathrm{top}}$ is the composite realization. On the individual cases
already witnessed in the corpus — the figure-eight and trefoil complements —
both sides reduce to the same Bloch–Wigner sum
([Thurston volume additivity](#prop:thurston-volume-additivity)), so the
*scaffolding half* of the compatibility holds on those cases.

**Open (the conjecture proper).** The *general* naturality — that the identity
holds for **all** QOU braids simultaneously, as an equality of maps rather than
case-by-case numerology — is of Kashaev volume-conjecture strength and is not
proved here. It is the volume-observable face of the
`QOU.Habiro.HabiroFlowSolution` open conjecture flagged in
[generating functions solve the Reeb flow](#rem:generating-functions-solve-reeb-flow):
the assertion that $\tau_\infty$ commutes with the three Habiro-ring
constructions.
<!-- FILE_END: archimedean-realisation-volume-compatibility.md -->


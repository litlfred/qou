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
the archimedean realisation $\tau_\infty$ (the limit $q \to 1$
along the real ray) this collapses to the Bloch–Wigner
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
realisation functor $\tau$ from $\widehat{\mathbb{Z}[q]}$ to the
analytic completion $\mathbb{C}[\![q-1]\!]$
([archimedean realisation functor](#def:archimedean-realization-functor)).
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
`HabiroFlowSolution` is conditional on the realisation functor
$\tau_\infty$ commuting with the three Habiro-ring constructions
(open conjecture; see
[archimedean realisation functor](#def:archimedean-realization-functor)).

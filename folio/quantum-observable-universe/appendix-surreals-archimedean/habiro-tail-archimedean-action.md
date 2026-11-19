**Proposition (conditional on the standard dilogarithm functional equations).**
Let $S(q) = \sum_{n\ge 0} \prod_{j=1}^{n}(1-q^{j})(1-q^{-j})$ be the $4_1$
Kashaev–Habiro cyclotomic tail, evaluated at real $q = e^{t}$ (the archimedean
$\rho_\infty$ face). Then:

1. $S$ is **bar-even**: $S(q) = S(q^{-1})$, since each factor
   $(1-q^{j})(1-q^{-j})$ is invariant under $q \leftrightarrow q^{-1}$.
2. $S$ is an alternating asymptotic series with
   $(1-q^{j})(1-q^{-j}) = -4\sinh^{2}(jt/2)$; its optimal-truncation
   (minimal-term) resurgent action is
   $$
     A_0 \;=\; -4\int_{0}^{\ln\varphi}\ln\!\bigl(2\sinh s\bigr)\,ds \;=\; \frac{\pi^{2}}{5},
   $$
   where $\varphi = (1+\sqrt5)/2$ is the golden ratio and the minimal term sits
   at $\mathrm{arcsinh}(1/2) = \ln\varphi$.

The evaluation reduces to the golden-ratio Landen dilogarithm value
$\mathrm{Li}_2(\varphi^{-2}) = \pi^{2}/15 - \ln^{2}\varphi$, itself derived from
Euler reflection, duplication, and Landen's identity at the golden points
$\psi+\psi^{2}=1$, $1+\psi=\varphi$, $\psi/(1+\psi)=\psi^{2}$ (with
$\psi=\varphi^{-1}$). The analytic proofs of these $\mathbb{Q}(\sqrt5)$ dilogarithm
relations are given in \cite{hakimoglu-brown2025}.

**Two faces of the same quantum object.** The $4_1$ quantum dilogarithm admits two
distinct archimedean evaluations, which do not coincide:

| Face | Evaluation | Trace field | Resurgent action |
|------|-----------|-------------|------------------|
| Geometric / state-integral | Faddeev $\Phi_b$ at the modular-double parameter $b$ (root-of-unity / Kashaev) | $\mathbb{Q}(\sqrt{-3})$ | $\mathrm{Vol}(4_1)/\pi \approx 0.646$ |
| Archimedean $\rho_\infty$ | real-$q$ Habiro tail $S(q)$ | $\mathbb{Q}(\sqrt5)$ | $\pi^{2}/5 \approx 1.974$ |

The classical dilogarithm $\mathrm{Li}_2$ is the semiclassical ($b\to 0$) leading
term of $\Phi_b$ in both cases, but at different arguments — the geometric shape
$e^{i\pi/3}$ (giving $\mathrm{Vol}$, in $\mathbb{Q}(\sqrt{-3})$) versus the golden
ratio $\varphi^{-2}$ (giving $\pi^{2}/5$, in $\mathbb{Q}(\sqrt5)$). That the two
faces carry different actions in different number fields is the $\hbar
\leftrightarrow 2\pi i/N$ resummation wall made exact: the state-integral and
real-$q$ Habiro evaluations are related by resummation rather than by term-by-term
reparametrisation.

**Scope.** This is a rigorous statement about the archimedean $\rho_\infty$
(real-$q$) face. Because $S$ is bar-even, the $4_1$ Habiro tail carries no
bar-odd datum, consistent with $4_1$ amphichirality; the bar-odd (chiral)
resurgence relevant to the $Q_\beta$ odd channel must come from a chiral knot
such as $5_2$. Whether the real-$q$ face (as opposed to the geometric
state-integral face) is the observable $\rho_\infty$ evaluation for the
$Q_\beta$ channel is an open question; this proposition asserts only the
mathematical identity rather than an observable identification.

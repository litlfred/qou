**Archimedean specialisation.** **Conditional on the standard dilogarithm functional equations.**
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
$\mathrm{Li}_2(\varphi^{-2}) = \pi^{2}/15 - \ln^{2}\varphi$, one of the classical
closed-form values listed in \cite[§1]{zagier-dilogarithm}. It follows from
Euler reflection, duplication, and Landen's identity at the golden points
$\psi+\psi^{2}=1$, $1+\psi=\varphi$, $\psi/(1+\psi)=\psi^{2}$ (with
$\psi=\varphi^{-1}$). Those three functional equations are recalled in
\cite[§1.1]{hakimoglu-brown2025}, whose own golden-ratio result is a different
identity ($\pi^2/100$ as the real part of $\mathrm{Li}_2$ at a root of a quartic, §6).

**Two faces of the same quantum object.** The $4_1$ quantum dilogarithm admits two
distinct archimedean evaluations, which do not coincide:

| Face | Evaluation | Trace field | Resurgent action |
|------|-----------|-------------|------------------|
| Geometric / state-integral | Faddeev $\Phi_b$ at the aether $b$ (root-of-unity / Kashaev) | $\mathbb{Q}(\sqrt{-3})$ | $\mathrm{Vol}(4_1)/\pi \approx 0.646$ |
| Archimedean $\rho_\infty$ | real-$q$ Habiro tail $S(q)$ | $\mathbb{Q}(\sqrt5)$ | $\pi^{2}/5 \approx 1.974$ |

The classical dilogarithm $\mathrm{Li}_2$ is the semiclassical ($b\to 0$) leading
term of $\Phi_b$ in both cases, but at different arguments — the geometric shape
$e^{i\pi/3}$ (giving $\mathrm{Vol}$, in $\mathbb{Q}(\sqrt{-3})$) versus the golden
ratio $\varphi^{-2}$ (giving $\pi^{2}/5$, in $\mathbb{Q}(\sqrt5)$). That the two
faces carry different actions in different number fields is the $\hbar
\leftrightarrow 2\pi i/N$ resummation wall made exact: the state-integral and
real-$q$ Habiro evaluations are related by resummation, not by term-by-term
reparametrisation.

**Scope.** This is a rigorous statement about the archimedean $\rho_\infty$
(real-$q$) face. Because $S$ is bar-even, the $4_1$ Habiro tail carries no
bar-odd datum, consistent with $4_1$ amphichirality; the bar-odd (chiral)
resurgence relevant to the $Q_\beta$ odd channel must come from a chiral knot
such as $5_2$. Whether the real-$q$ face — as opposed to the geometric
state-integral face — is the physically relevant $\rho_\infty$ evaluation for the
$Q_\beta$ observable is an open question; this proposition asserts only the
mathematical identity, not a physical identification.

**Relation to the proved resurgence results.** The standard dictionary behind
item 2 runs from a Habiro-ring element $\Phi_K$ to the formal series
$F_K(x) = \Phi_K(e^{-1/x}) \in \mathbb{C}[[1/x]]$, its Borel transform $G_K$,
and the median resummation $S^{\mathrm{med}}_K$; the Costin--Garoufalidis
conjecture asks that $G_K$ be resurgent, that $S^{\mathrm{med}}_K$ be analytic on
$\mathrm{Re}\,x > 0$ with radial limits at $\tfrac{1}{2\pi i}\mathbb{Q}$, and that
those limits recover $\Phi_K$ at roots of unity \cite[§1, eqs. (1.3)--(1.8) and
Conj. 1.1]{crew2023}. Crew, Fantini, Goswami, Osburn and Wheeler prove the resurgence
and median-resummation statements for Habiro elements that come from radial limits
of partial theta series through a strange identity \cite[Thm. 1.2]{crew2023}, and
deduce the conjecture for the torus-knot families $T(2,2u+1)$ and $T(3,2^k)$
\cite[Cor. 1.5 and §3]{crew2023}. The hyperbolic knot $4_1$ is not in that class,
and the source supplies no strange identity for its tail, so the proved resurgence
does not transfer to item 2: the action $A_0 = \pi^2/5$ above is an
optimal-truncation statement about the real-$q$ series and is not a consequence of
\cite{crew2023}.

**The state-integral face in the literature.** The geometric face of the table is
treated on the $q$-difference side by Garoufalidis and Wheeler, who work out the
$4_1$ equation $tq\,f(qt;q) + (1-2t)\,f(t;q) + tq^{-1} f(q^{-1}t;q) = 0$ completely:
its solutions at $t = 0$ and $t = \infty$, their monodromy, residues and
determinants, the associated state integral, the $x$-deformation, and an analytic
lift of the colored Jones polynomial \cite[§1.5, Thm. 1.7, and \S§5.1--5.8]{garoufalidis-wheeler-modular}.
That treatment concerns the state-integral face only; it makes no statement about
the real-$q$ tail $S(q)$ of item 2.

**Extension across the double-twist family.** For the double-twist knots $K(m,-p)$
($m,p \ge 1$, with $K(1,-1) = 4_1$), the Lauridsen cyclotomic expansion and the
$q$-hypergeometric Kontsevich--Zagier / strongly-unimodal root-of-unity dualities
$F_{m,p}(\zeta_N) = U_{m,p}(-1;\zeta_N^{-1})$ and
$\mathcal{F}_{m,p}(\zeta_N) = \mathcal{U}_{m,p}(-1;\zeta_N^{-1})$ of Lovejoy and
Osburn \cite[Thms.~1.1--1.2, Cors.~1.3--1.4, eq.~(1.2)]{lovejoy-osburn} write the
real-$q$ Habiro tail as $\sum_{n\ge 0} C_{K(m,-p),n}(q)\prod_{j=1}^n (1-q^j)(1-q^{-j})$.
Under $q \mapsto q^{-1}$ the Gaussian $q$-binomial chains swap $m$ and $p$, giving
$C_{K(m,-p),n}(q^{-1}) = C_{K(p,-m),n}(q)$: bar-evenness therefore holds for the
entire amphichiral diagonal $K(m,-m)$ (including $8_3 = K(2,-2)$), whereas
off-diagonal knots such as $6_1 = K(1,-2)$ acquire a non-zero bar-odd part and
asymmetric $q > 1$ versus $q < 1$ optimal-truncation actions. Unlike bar-evenness,
the golden-ratio action $\pi^2/5$ is specific to the $m = p = 1$ base case where
$C_{K(1,-1),n}(q) = 1$: on the $q > 1$ ray of $K(2,-1) = 6_1^*$ (equivalently
$q < 1$ of $6_1$) the $q^{n_1^2 + n_1}$ weight shifts the dilogarithm saddle to
$\mathbb{Q}(\sqrt{2})$ at $e^{u^*} = 1 + 1/\sqrt{2}$, giving the exact octagonal
action $\pi^2/8$, whereas the $q > 1$ ray of $6_1$ ($A_0^+ \approx 1.6433$) and
the amphichiral knot $8_3 = K(2,-2)$ ($A_0 \approx 0.9913$, distinct from
$\mathrm{Vol}(8_3)/\pi \approx 1.6648$) are governed by a quartic inner saddle
whose optimal-truncation actions are $\mathbb{Q}$-linearly independent of $\pi^2$
up to norm $10^4$.

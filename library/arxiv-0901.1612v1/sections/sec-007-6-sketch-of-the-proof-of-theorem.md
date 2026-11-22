---
doc_id: arxiv-0901.1612v1
doc_title: "Triple linking numbers, ambiguous Hopf invariants and integral formulas for three-component links"
section_id: sec-007-6-sketch-of-the-proof-of-theorem
section_title: "Sketch of the proof of Theorem ??"
section_number: 6
pages: 17-18
source_pdf: 0901.1612v1.pdf
source_sha256: b4f3efcadd1e5caf
toc_source: outline
text_source: latex
latex_prose_ratio: 0.696
latex_coverage_ratio: 0.966
doc_brief: "Triple linking numbers, ambiguous Hopf invariants and integral formulas for three-component links — Three-component links in the 3-dimensional sphere were classi- fied up to link homotopy by John"
duplicate_of: "deturck-melvin-gluck-komendarczyk-shonkwiler-2008-triple-lin"
---
[]{#sec:thmB label="sec:thmB"} Let $L$ be a 3-component link in $S^3$ with pairwise linking numbers $p$, $q$ and $r$ all zero. We saw in Theorem [\[thm:A\]](#thm:A){reference-type="ref" reference="thm:A"} that these numbers are the degrees of the characteristic map $g_L: T^3 \to S^2$ on the 2-dimensional coordinate subtori. Thus $g_L$ is homotopic to a map which collapses the 2-skeleton of $T^3$, and so is in effect a map of $S^3 \to S^2$. The Hopf invariant of this map, which we will regard as the Hopf invariant of $g_L$, is equal to Pontryagin's $\nu$-invariant comparing $g_L$ to the constant map, and we will denote this by $\nu(g_L)$.

To calculate this Hopf invariant, we adapt J. H. C. Whitehead's integral formula for the Hopf invariant of a map from $S^3 \to S^2$ to the case of a map from $T^3 \to S^2$, and show how to make the calculation explicit.

Whitehead [@Whitehead] expressed the Hopf invariant of a map $f: S^3 \to S^2$ as follows. Let $\omega$ be the area 2-form on $S^2$, normalized so that $\int_{S^2} \omega = 1$. Then its pullback $f^* \omega$ is a closed 2-form on $S^3$ which is exact because $H^2(S^3; \mathbb R) = 0$. Hence $f^*\omega = d\alpha$ for some 1-form $\alpha$ on $S^3$, and Whitehead showed that $$\text{Hopf}(f) \ = \ \int_{S^3} \alpha \wedge f^*\omega,$$ the integral being independent of the choice of $\alpha$.

We recast Whitehead's formula in terms of vector fields by letting $V_f$ be the vector field on $S^3$ corresponding in the usual way to the 2-form $f^* \omega$. Then $V_f$ is divergence-free, since $f^* \omega$ is closed, and is in fact in the image of curl since $f^* \omega$ is exact. Thus $V_f = \nabla \times W$ for some vector field $W$ on $S^3$, and the integral formula for the Hopf invariant becomes $$\text{Hopf}(f) \ = \ \int_{S^3} W \,\,\raisebox{.2ex}{\text{\tiny\textbullet}}\,\,V_f \ d(\text{vol}),$$ independent of the choice of $W$.

To make Whitehead's formula more explicit, one needs a way to produce a vector field $W$ whose curl is $V_f$. On $\mathbb R^3$ this can be done by viewing $V_f$ as a flow of electric current and then calculating the corresponding magnetic field $\text{BS}(V_f)$ using the classical formula of Biot and Savart [@BiotSavart]: $$\text{BS}(V_f) \ = \ -\nabla \times \text{Gr}(V_f),$$ where $\text{Gr}$ is the Green's operator that inverts the vector Laplacian. Then by Ampère's Law, $\nabla \times \text{BS}(V_f) = V_f$.

The explicit formula for the Green's operator is well known on $\mathbb R^3$, namely convolution with the fundamental solution $\varphi(r) = -1/(4\pi r)$ of the scalar Laplacian, and hence $$\text{BS}(V_f)(y) \ = \ \int_{\mathbb R^3} V_f(x) \times \nabla_y\varphi\left(\|y-x\|\right)\ dx,$$ assuming that $V$ is compactly supported, to guarantee that the integral converges. The corresponding formula on $S^3$ was given by DeTurck and Gluck [@DeTurckGluck] and by Kuperberg [@Kuperberg].

We can summarize the calculation of the Hopf invariant in the single formula $$\text{Hopf}(f) \ = \ \int_{S^3} \text{BS}(V_f) \,\,\raisebox{.2ex}{\text{\tiny\textbullet}}\,\,V_f \ d(\text{vol})$$ which was Woltjer's original expression for the helicity of the vector field $V_f$.

A routine check shows that the above formula, with the integration over $T^3$ instead of $S^3$, yields the value of the Hopf invariant of the characteristic map $g_L: T^3\to S^2$. This provides a formula for Pontryagin's $\nu$-invariant, and portrays it as the helicity of the associated vector field $V_{g_L}$, which for simplicity we denote by $V_L$: $$\label{eqn:PontryaginHelicity}
    \nu(g_L) = \text{Hopf}(g_L) = \text{Hel}(V_L) = \int_{T^3} \text{BS}(V_L) \,\,\raisebox{.2ex}{\text{\tiny\textbullet}}\,\,V_L \ d(\text{vol}).
    \tag{$\ddag$}$$ A straightforward calculation shows that $$V_L \ = \ \frac{F_t \times F_u \,\,\raisebox{.2ex}{\text{\tiny\textbullet}}\,\,F}{4\pi \|F\|^3} \, {\partial}/{\partial s} + \frac{F_u \times F_s \,\,\raisebox{.2ex}{\text{\tiny\textbullet}}\,\,F}{4\pi \|F\|^3} \, {\partial}/{\partial t} + \frac{F_s \times F_t \,\,\raisebox{.2ex}{\text{\tiny\textbullet}}\,\,F}{4\pi \|F\|^3} \, {\partial}/{\partial u},$$ where $F: T^3 \to \mathbb R^3 - \{0\}$ is the map defined in Section [\[sec:characteristicmap\]](#sec:characteristicmap){reference-type="ref" reference="sec:characteristicmap"}, and where subscripts denote partial derivatives.

Therefore, to make the integral formula ([\[eqn:PontryaginHelicity\]](#eqn:PontryaginHelicity){reference-type="ref" reference="eqn:PontryaginHelicity"}) explicit, it remains to obtain an explicit formula for the Biot-Savart operator on the 3-torus. As in the case of $\mathbb R^3$, this depends on having an explicit formula for the fundamental solution of the scalar Laplacian.

## The fundamental solution of the Laplacian {#sub:fund_soln}

::: proposition
[]{#prop:fund_soln label="prop:fund_soln"} The fundamental solution of the scalar Laplacian on the 3-torus $T^3$ is given by the formula $$\varphi(x,y,z) \ = \ -\,\frac{1}{8\pi^3}\,\sum \, \frac{e^{i(\ell x+my+nz)}}{\ell^2+m^2+n^2}$$ where the sum is over all integers $\ell$, $m$ and $n$ $($positive and negative$)$ with the exception of $\ell=m=n=0$.
:::

Even though we have expressed $\varphi$ in terms of complex exponentials, the value of $\varphi$ is real for real values of $x$, $y$ and $z$ because of the symmetry of the coefficients, and can therefore also be expressed as a Fourier cosine series.

![Fundamental solution of the scalar Laplacian on the $2$-torus](fundsol3.pdf){#fig:fund_sol height="200pt"}

Figure [1](#fig:fund_sol){reference-type="ref" reference="fig:fund_sol"} shows the graph of the corresponding fundamental solution of the scalar Laplacian on the 2-torus $T^2$, displayed over the range $-3\pi \leq x, y \leq 3\pi$. If we think of the 2-torus as obtained from a square by identifying opposite sides, then this shows the function $\varphi$ to have a negative infinite minimum at the single vertex, two saddle points in the middle of the two edges, and a maximum in the middle of the square. Presumably the fundamental solution $\varphi$ on the 3-torus displays a corresponding Morse-like behavior.

## Completing the proof of Theorem [\[thm:B\]](#thm:B){reference-type="ref" reference="thm:B"} {#sub:ThmBCompleted}

Now we have an explicit formula for the fundamental solution $\varphi$ of the scalar Laplacian on the 3-torus $T^3$, and we know that both the scalar and vector Green's operators act by convolution with $\varphi$. In particular, if $V$ is a smooth vector field on $T^3$, then $\text{Gr}(V) = V * \varphi$, that is, $$\text{Gr}(V)(\tau) \ = \ \int_{T^3} V(\sigma) \varphi(\tau - \sigma) \ d\sigma.$$

To obtain the formula for the magnetic field $\text{BS}(V)$, we take the negative curl of the above formula and get $$\begin{aligned}
    \text{BS}(V)(\tau) \ = \ -\nabla_\tau \times \text{Gr}(V)(\tau) \ & = \ -\int_{T^3} \nabla_\tau \times \left(V(\sigma) \varphi(\tau - \sigma)\right)d\sigma \\
    & = \ \int_{T^3} V(\sigma) \times \nabla_\tau \varphi(\tau - \sigma) \ d\sigma.
\end{aligned}$$ Then the helicity of $V$ is given by $$\begin{aligned}
    \text{Hel}& (V) \ = \ \int_{T^3} V(\tau) \,\,\raisebox{.2ex}{\text{\tiny\textbullet}}\,\,\text{BS}(V)(\tau) \ d\tau \\
    & = \ \int_{T^3 \times T^3} V(\sigma) \times V(\tau) \,\,\raisebox{.2ex}{\text{\tiny\textbullet}}\,\,\nabla_\sigma \varphi(\sigma - \tau) \ d\sigma \, d\tau.
\end{aligned}$$

Applying this to the vector field $V_L$ associated with our 3-component link $L$, we get the desired formula for the Pontryagin invariant $\nu$ of $g_L$: $$\begin{aligned}
    \nu(g_L) \ &= \ \text{Hopf}(g_L) = \text{Hel}(V_L) = \int_{T^3} \text{BS}(V_L) \,\,\raisebox{.2ex}{\text{\tiny\textbullet}}\,\,V_L \ d(\text{vol}) \\
    &= \int_{T^3 \times T^3} V_L(\sigma) \times V_L(\tau) \,\,\raisebox{.2ex}{\text{\tiny\textbullet}}\,\,\nabla_\sigma \varphi(\sigma-\tau) \ d \sigma \, d \tau.
\end{aligned}$$

Hence by Theorem [\[thm:A\]](#thm:A){reference-type="ref" reference="thm:A"}, Milnor's $\mu$-invariant of the 3-component link $L$ is given by $$\mu(L) \ = \ \frac12\,\nu(g_L) \ = \ \frac12\, \int_{T^3 \times T^3} V_L(\sigma) \times V_L(\tau) \,\,\raisebox{.2ex}{\text{\tiny\textbullet}}\,\,\nabla_\sigma \varphi(\sigma-\tau) \ d\sigma \, d\tau,$$ completing the proof of Theorem [\[thm:B\]](#thm:B){reference-type="ref" reference="thm:B"}.

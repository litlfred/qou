---
doc_id: arxiv-1101.3374v1
doc_title: "Pontryagin invariants and integral formulas for Milnor's triple linking number"
section_id: sec-007-8-proof-of-theorem-formulas-1-and-2
section_title: "Proof of Theorem ??, formulas (1) and (2)"
section_number: 8
pages: 45-48
source_pdf: 1101.3374v1.pdf
source_sha256: 01d76c1d259c1d51
toc_source: outline
text_source: latex
latex_prose_ratio: 0.955
latex_coverage_ratio: 0.951
doc_brief: "Pontryagin invariants and integral formulas for Milnor's triple linking number — To each three-component link in the 3-sphere, we associate a geometrically natural characteristic map from the 3-torus"
---
[]{#sec:B label="sec:B"}

Theorem [\[thm:B\]](#thm:B){reference-type="ref" reference="thm:B"} provides three formulas for Milnor's $\mu$-invariant of a three-component link $L$ in $S^3$ whose pairwise linking numbers vanish:

$(1)$ (differential forms)  $\mu(L) \ = \ \displaystyle{\frac12\, \int_{T^3} \delta(\varphi*\omega_L) \wedge \omega_L}$

$(2)$ (vector fields)  $\mu(L) \ = \ \displaystyle{\frac12\, \int_{T^3\times T^3} \overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf v}}_L(\textup{\bf x}) \times \overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf v}}_L(\textup{\bf y}) \,\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}\,
\nabla_{\!\textup{\bf y}}\,\varphi\left(\textup{\bf x}- \textup{\bf y}\right)\ d\textup{\bf x}\, d\textup{\bf y}}$

$(3)$ (Fourier series)  $\mu(L) \ = \  \displaystyle{8\pi^3 \sum_{\textup{\bf n}\ne{\bf 0}} \textup{\bf a}_\textup{\bf n}\times \textup{\bf b}_\textup{\bf n}\,\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}\,\textup{\bf n}/|\textup{\bf n}|^2}$

The notation is explained in the introduction.

In the subsections that follow, we obtain explicit expressions for the characteristic $2\textup{-form}$ $\omega_L$ and vector field $\overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf v}}_L$, and for the fundamental solution $\varphi$ to the scalar Laplacian on $T^3$, and then establish formula (1) by making use of J. H. C. Whitehead's integral formula for the Hopf invariant. Then, we show how to obtain formula (2) from formula (1). Finally, in Section [\[sec:B\'\]](#sec:B'){reference-type="ref" reference="sec:B'"} we review the calculus of differential forms and Fourier analysis on $T^3$, in order to make explicit the role and form of $\varphi$ and obtain formula (3).

Recall the formula for the characteristic map $g_L\colon T^3\to S^2$ of the link $L$ given in Proposition [\[prop:char\]](#prop:char){reference-type="ref" reference="prop:char"}, $$g_L(s,t,u) \ = \ \frac{F(x,y,z)}{| F(x,y,z)|},$$ where $x=x(s)$, $y=y(t)$ and $z=z(u)$ parametrize the components of $L$, and where $F$ was given in Section [\[sec:characteristic\]](#sec:characteristic){reference-type="ref" reference="sec:characteristic"} as $$F(x,y,z) \ = \  (ix\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}y + iy\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}z + iz\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}x \ , \  jx\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}y + jy\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}z + jz\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}x \ , \  kx\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}y + ky\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}z + kz\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}x).$$ Here we view $x$, $y$ and $z$ as quaternions for the multiplication and as vectors in $\mathbb R^4$ when performing the dot product. For simplicity, we write $g_L=F/| F|$, suppressing the appearance of the evaluation map $e_L(s,t,u)=(x(s),y(t),z(u))$.

Again let $\omega$ be the Euclidean area 2-form on the unit 2-sphere $S^2\subset\mathbb R^3$, normalized so that the total area is 1 instead of $4\pi$. If $\textup{\bf p}$ is a point of $S^2$, and $\textup{\bf a}$ and $\textup{\bf b}$ are tangent vectors to $S^2$ at $\textup{\bf p}$, then $$\omega_{\textup{\bf p}}(\textup{\bf a},\textup{\bf b}) \ = \ \frac1{4\pi}(\textup{\bf a}\times\textup{\bf b})\,\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}\,\textup{\bf p}.$$ This 2-form $\omega$ on $S^2$ extends to a closed 2-form $\overline\omega$ in $\mathbb R^3-{\bf 0}$ given by $$\overline\omega_{\textup{\bf p}}(\textup{\bf a},\textup{\bf b}) \ = \ {(\textup{\bf a}\times\textup{\bf b})\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}\textup{\bf p}\over 4\pi|\textup{\bf p}|^3},$$ which is the pullback of $\omega$ from $S^2$ to $\mathbb R^3-{\bf 0}$ via the map $\textup{\bf p}\mapsto \textup{\bf p}/|\textup{\bf p}|$.

Hence the pullback $g_L^*\omega$ of $\omega$ from $S^2$ to $T^3$ via $g_L=F/| F|$ is the same as the pullback $F^*\overline\omega$ of $\overline\omega$ from $\mathbb R^3-{\bf 0}$ to $T^3$ via $F$.

Write $$g_L^*\omega \ = \ F^*\overline\omega 
\ = \ a(s,t,u)dt\wedge du+b(s,t,u)du\wedge ds+c(s,t,u)ds\wedge dt.$$ Then we have $$\aligned
a(s,t,u)& \ = \  F^*\overline\omega({\partial_t},{\partial_u}) \ = \  \overline\omega(F_*{\partial_t}, F_*{\partial_u}) \\
& \ = \ \overline\omega(F_t,F_u) \ = \  \frac{(F_t\times F_u)\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}F}{4\pi| F|^3},
\endaligned$$ and likewise for $b(s,t,u)$ and $c(s,t,u)$, where the subscripts on $F$ denote partial derivatives.

Therefore, the characteristic 2-form of the link $L$ is $$\omega_L \ = \  g_L^*\omega \ = \ 
\frac{F_t\times F_u\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}F}{4\pi| F|^3}  \, dt\wedge du
+\frac{F_u\times F_s\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}F}{4\pi| F|^3} \, du\wedge ds
+\frac{F_s\times F_t\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}F}{4\pi| F|^3} \, ds\wedge dt,$$ and its corresponding characteristic vector field is $$\overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf v}}_L \ = \ 
\frac{F_t\times F_u\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}F}{4\pi| F|^3} \, \partial_s
+\frac{F_u\times F_s\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}F}{4\pi| F|^3} \, \partial_t
+\frac{F_s\times F_t\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}F}{4\pi| F|^3} \, \partial_u.$$

Let $L$ be a three-component link in the 3-sphere $S^3$ with pairwise linking numbers $p$, $q$ and $r$ all zero. By the first part of Theorem [\[thm:A\]](#thm:A){reference-type="ref" reference="thm:A"} these numbers are the degrees of the characteristic map $g_L\colon T^3\to S^2$ on the $2$-dimensional coordinate subtori. Since these degrees are all zero, $g_L$ is homotopic to a map $g\colon T^3\to S^2$ which collapses the 2-skeleton of $T^3$ to a point: $$g_L\ \simeq \ g\colon T^3 \stackrel{\sigma}{\longrightarrow}S^3 \stackrel{f}{\longrightarrow}S^2,$$ where $\sigma$ is the collapsing map. By the second part of Theorem [\[thm:A\]](#thm:A){reference-type="ref" reference="thm:A"}, Milnor's $\mu$-invariant of $L$ is equal to half of Pontryagin's $\nu$-invariant $\nu(g_L)$ (comparing $g_L$ to the constant map $f_{000}$ as explained in Section [\[sec:pontryagin\]](#sec:pontryagin){reference-type="ref" reference="sec:pontryagin"}), which in turn is just the Hopf invariant of $f\colon S^3\to S^2$, $$\mu(L)\ = \ {1\over 2}\nu(g_L)\ = \ {1\over 2}\mathop{\rm Hopf}\nolimits(f).$$

We can thus use J. H. C. Whitehead's integral formula for the Hopf invariant as the first ingredient in our formula for the $\mu$ invariant. Starting from Hopf's definition of his invariant of a map $f\colon S^3\to S^2$ as the linking number between the inverse images of two regular values, Whitehead [@Whitehead] found an integral formula for $\mathop{\rm Hopf}\nolimits(f)$ as follows.

Let $\omega$ be the area 2-form on $S^2$, normalized so that $\int_{S^2}
\omega=1$. Its pullback $f^*\omega$ is a closed 2-form on $S^3$, which is exact because $H^2(S^3;\mathbb R)=0$. Hence $f^*\omega=d\alpha$ for some 1-form $\alpha$ on $S^3$, and Whitehead showed that the Hopf invariant of $f$ is given by the formula $$\mathop{\rm Hopf}\nolimits(f) \ = \ \int_{S^3}\alpha\wedge f^*\omega \ 
= \ \int_{S^3}\alpha\wedge d\alpha,$$ the value of the integral being independent of the choice of $\alpha$.

To make Whitehead's formula explicit requires a way to produce a 1-form $\alpha$ whose differential $d\alpha$ is a given 2-form $f^*\omega$ on $S^3$ which is known to be exact. We give an explicit formula for this in the Appendix, since it is not needed in the body of the paper. Instead, we are going to pull the whole situation back to $T^3$ and perform our calculations there.

In particular, the formula $$\mathop{\rm Hopf}\nolimits(f) \ = \  \int_{S^3}\alpha_0\wedge f^*\omega,$$ where $\alpha_0$ is any 1-form on $S^3$ such that $d\alpha_0=f^*\omega$, pulls back to the formula $$\nu(g_L)\ = \ \int_{T^3}\overline\alpha_0\wedge g^*\omega,$$ where $\overline\alpha_0$ is any 1-form on $T^3$ such that $d\overline\alpha_0 = g^*\omega$. One such choice of $\overline\alpha_0$ would be $\overline\alpha_0 = \sigma^*\alpha_0$, with $\alpha_0$ obtained as in the Appendix. However, since we don't have an explicit analytic formula for $\sigma$, and since the formula for $\alpha_0$ is complicated, we will pursue a slightly different approach.

Taking advantage of the fact that $g_L$ is homotopic to $g$, we also have $$\nu(g_L) \ = \  \int_{T^3}\alpha\wedge g_L^*\omega \ = \ \int_{T^3}\alpha\wedge \omega_L$$ for any $1$-form $\alpha$ on $T^3$ such that $d\alpha=\omega_L$. Therefore, what we really need is a canonical way to produce a $1$-form $\alpha$ on $T^3$ whose exterior derivative is the exact 2-form $\omega_L$. We will prove in Proposition [\[prop:alp\]](#prop:alp){reference-type="ref" reference="prop:alp"} that the $1$-form $$\alpha_L \ = \ \delta(\varphi* \omega_L)$$ has the desired property that $d\alpha_L=\omega_L$. Moreover, if $\widetilde\alpha$ is any other $1$-form such that $d\widetilde\alpha=\omega_L$, then $|\alpha_L| \le |\widetilde\alpha|$ in $L^2(T^3)$, with equality if and only if $\widetilde\alpha=\alpha_L$.

We thus obtain the explicit integral formula for Milnor's $\mu$-invariant of the three component link $L$: $$\mu(L) \ = \ {1\over 2}\nu(g_L) \ = \ {1\over 2}\int_{T^3}\delta(\varphi* \omega_L)\wedge\omega_L,$$ which is formula (1) of Theorem [\[thm:B\]](#thm:B){reference-type="ref" reference="thm:B"}.

The 1-form $\delta(\varphi* \omega_L)$ on $T^3$ which appears in formula (1) of Theorem [\[thm:B\]](#thm:B){reference-type="ref" reference="thm:B"} converts to the vector field $\nabla\times(\varphi* \overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf v}}_L)$, which can be regarded as the magnetic field on $T^3$ due to the current flow $\overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf v}}_L$. The customary minus sign here is now hidden in the definitions of the Laplacian and its inverse (Green's operator).

The integral formula for Milnor's $\mu$-invariant given in formula (1), $$\mu(L) \ = \ {1\over 2}\int_{T^3}\delta(\varphi* \omega_L)\wedge\omega_L\,,$$ then converts to the formula $$\mu(L) \ = \ {1\over 2}\int_{T^3}\left(\vphantom{x^2}\nabla\times(\varphi* \overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf v}}_L)\right)\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}\overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf v}}_L\,d\mathop{\rm vol}\nolimits$$ in the language of vector fields. To obtain formula (2) of Theorem [\[thm:B\]](#thm:B){reference-type="ref" reference="thm:B"}, we first expand out the convolution integral $$(\varphi* \overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf v}}_L)(\textup{\bf x}) \ = \ \int_{T^3}\overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf v}}_L(\textup{\bf y})\,\varphi(\textup{\bf x}-\textup{\bf y})\,d\textup{\bf y}.$$ Then we compute its curl: $$\begin{aligned}
\left(\vphantom{x^2}\nabla_{\!\textup{\bf x}}\times(\varphi* \overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf v}}_L)\right)(\textup{\bf x})
\ &= \  \int_{T^3}\nabla_{\!\textup{\bf x}}\times\left(\vphantom{x^2}\overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf v}}_L(\textup{\bf y})\,\varphi(\textup{\bf x}-\textup{\bf y})\right)\,d\textup{\bf y}\\
\ &= \  -\int_{T^3}\overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf v}}_L(\textup{\bf y})\times\nabla_{\!\textup{\bf x}}\,\varphi(\textup{\bf x}-\textup{\bf y})\,d\textup{\bf y}\,,
\end{aligned}$$ using the product formula $\nabla\times(f\overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf a}})=f(\nabla\times \overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf a}})-\overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf a}}\times\nabla f$. Note that $\nabla_{\!\textup{\bf x}}\times\overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf v}}_L(\textup{\bf y})={\bf 0}$ since, from the point of view of the variable $\textup{\bf x}$, the vector field $\overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf v}}_L(\textup{\bf y})$ is constant.

Inserting the expression for the curl of $\varphi*\overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf v}}_L$ into the formula for $\mu(L)$, we get $$\aligned
\mu(L)
&\ = \ -\frac12\int_{T^3\times T^3}\left(\vphantom{x^2}\overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf v}}_L(\textup{\bf y})\times\nabla_{\!\textup{\bf x}}\,\varphi(\textup{\bf x}-\textup{\bf y})\right)\,\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}\,
\overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf v}}_L(\textup{\bf x})\,d\textup{\bf x}\,d\textup{\bf y}\\
&\ = \ -\frac12\int_{T^3\times T^3}\overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf v}}_L(\textup{\bf x})\times\overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf v}}_L(\textup{\bf y})\,\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}\,\nabla_{\!\textup{\bf x}}\,\varphi(\textup{\bf x}-\textup{\bf y})\,d\textup{\bf x}\,d\textup{\bf y}\\
&\ = \ \frac12\int_{T^3\times T^3}\overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf v}}_L(\textup{\bf x})\times\overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf v}}_L(\textup{\bf y})\,\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}\,\nabla_{\!\textup{\bf y}}\,\varphi(\textup{\bf x}-\textup{\bf y})\,d\textup{\bf x}\,d\textup{\bf y}\,,
\endaligned$$ where at the last step we hid the minus sign by taking the gradient of $\varphi$ with respect to $\textup{\bf y}$ instead of $\textup{\bf x}$, and obtained formula (2) of Theorem [\[thm:B\]](#thm:B){reference-type="ref" reference="thm:B"}.

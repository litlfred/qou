---
doc_id: arxiv-1511.05628v1
doc_title: "QUANTUM MODULARITY AND COMPLEX CHERN-SIMONS THEORY"
section_id: sec-019-43-state-integrals
section_title: "State integrals"
section_number: 4.3
pages: 17-19
source_pdf: 1511.05628v1.pdf
source_sha256: 3b9da2994233882b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.961
latex_coverage_ratio: 0.978
doc_brief: "QUANTUM MODULARITY AND COMPLEX CHERN-SIMONS THEORY — The Quantum Modularity Conjecture of Zagier predicts the existence of a for- mal power series with arithmetically interesting coeﬃcients that"
---
Complex Chern-Simons theory has not yet been made mathematically rigorous as a full TQFT, in contrast to Chern-Simons theory with a compact gauge group [@Witten-jones] and the Reshetikhin-Turaev construction [@RT]. Nevertheless, there exist state-integral models, based on ideal triangulations, that provide a definition of complex Chern-Simons partition functions for a certain class of 3-manifolds [@D-levelk; @AK]. These state-integral models generalize earlier work [@Hikami; @DGLZ; @Dimofte-QRS; @AK-TQFT; @AK-new] that computed Chern-Simons partition functions at level $k=1$.

In the present paper, we use the asymptotic expansion of these state integrals in the limit $(t,\tilde t)\to(2k,0)$ to motivate the definition of the power series $\phi_{\gamma,\zeta}(\hbar)$ given in Section [\[sec.def\]](#sec.def){reference-type="ref" reference="sec.def"}.

Before we discuss the state-integral $\mathcal{Z}_\gamma$ associated to a Neumann-Zagier datum $\gamma$ of an ideal triangulation, it is worth mentioning that convergence of the state-integral requires certain positivity assumptions, which are satisfied when the ideal triangulation supports a strict angle structure. This is discussed at length in [@AK; @D-levelk]. In the rest of this section, we will assume that the background ideal triangulation admits such a structure. Although positivity is required for the convergence of the state-integral, the formula that we will obtain for its asymptotic expansion makes sense without any positivity assumptions.

It was shown in [@Dimofte-QRS; @DG] that a Neumann-Zagier datum $\gamma = (\mathbf A,\mathbf B,\nu,z,f,f'')$ with non-degenerate matrix $\mathbf B$ leads to a state-integral partition function for $\mathrm{SL}(2,\mathbb C)$ Chern-Simons at level $k=1$, given by

$$\begin{aligned}
\mathcal{Z}_\gamma&= \frac{1}{\sqrt{\det\mathbf B}}(i)^{f\mathbf B^{-1}\nu}
  e^{\frac1k(\frac\hbar8-\frac{\pi^2}{8\hbar})f\mathbf B^{-1}\nu} \int \frac{d^NZ}{
(-2\pi i \hbar)^{\frac N2}}e^{-\frac1{2k}(1+\frac{2\pi i}{\hbar})Z\mathbf B^{-1}\nu
+\frac1{2k\hbar}Z\mathbf B^{-1}\mathbf AZ} \prod_{i=1}^N\mathcal{Z}_\hbar[\Delta](Z_i) \,,
\label{SS1}
\end{aligned}$$

where the integral runs over some mid-dimensional contour in the space $\mathbb C^N$ parametrized by $Z=(Z_1,...,Z_N)$, and $\mathcal{Z}_\hbar[\Delta](Z_i)$ is a quantum dilogarithm function associated to every tetrahedron, given for $\Re(\hbar)<0$ by

$$\mathcal{Z}_\hbar[\Delta](Z_i) = \prod_{r=0}^\infty 
\frac{1-e^{(r+1)\hbar-Z_i}}{1-e^{r \frac{4\pi^2}{\hbar})
-\frac{2\pi i}{\hbar}Z_i}}  = \frac{(e^{Z_i+\hbar},
e^\hbar)_\infty}{(e^{\frac{2\pi i}{\hbar}Z_i},
e^{\frac{4\pi^2}{\hbar}})_\infty}\,.$$

This function has an asymptotic expansion as $\hbar\to 0$,

$$\begin{aligned}
\mathcal{Z}_\hbar[\Delta](Z_i) &\sim (e^{Z+\hbar},e^\hbar)_\infty \sim \exp\sum_{n=0}^\infty 
\frac{\hbar^{n-1}}{n!} B_n(1){\rm Li}_{2-n}(e^{-Z}) \\
& \hspace{.3in}  = \frac1\hbar {\rm Li}_2(e^{-Z}) + \frac12{\rm Li}_1(e^{-Z}) 
+ \frac\hbar{12}{\rm Li}_0(e^{-Z}) + \ldots\,.
\notag
\end{aligned}$$

Using ${\rm Li}_2(e^{-(Z^*+\delta Z)}) = {\rm Li}_2(e^{-Z^*}) 
+ \log(1-e^{-Z^*})\delta Z + ...$, it follows that at leading order in $\hbar$, the integrand of [\[SS1\]](#SS1){reference-type="eqref" reference="SS1"} has critical points at

$$\label{CScrit} 
\mathbf A Z^* +\mathbf B\log(1-e^{-Z^*}) = i\pi \nu\,,$$

which are a logarithmic version of the gluing equations. In particular, if $\gamma$ is a positive Neumann-Zagier datum, then the equations are satisfied by $Z^*_i=\log (z_i)$ for all $i=1,\dots,N$. By performing formal Gaussian integration around this "geometric" critical point, order by order in the formal parameter $\hbar$, we obtained in [@DG] a diagrammatic formula for the series $\phi_{K,1}(\hbar)$.

The actual contour of integration appropriate for [\[SS1\]](#SS1){reference-type="eqref" reference="SS1"} and its level-$k$ generalization has been carefully described in [@AK-TQFT; @D-levelk; @AK]. We emphasize, however, that in order to perform a formal perturbative expansion around a given critical point, a choice of contour is irrelevant.

The level-$k$ generalization of the state integral, as developed in [@D-levelk], reads

$$\begin{aligned}
\mathcal{Z}_\gamma^{(k)}&= \frac{1}{k^N\sqrt{\det\mathbf B}}\zeta^{\frac14f\mathbf B^{-1}\nu}
  e^{\frac1k(\frac\hbar8-\frac{\pi^2}{8\hbar})f\mathbf B^{-1}\nu}  \notag\\
  &\hspace{-.3cm}\times \hspace{-.2cm} \sum_{m\in(\mathbb Z/k\mathbb Z)^N} 
\int \frac{d^NZ}{(-2\pi i \hbar)^{\frac N2}}
(-\zeta^{\frac12})^{m\mathbf B^{-1}\mathbf A m} 
e^{-\frac1{2k}(1+\frac{2\pi i}{\hbar})Z\mathbf B^{-1}\nu+\frac1{2k\hbar}Z\mathbf B^{-1}\mathbf AZ} 
\prod_{i=1}^N \mathcal{Z}_\hbar^{(k)}[\Delta](Z_i,m_i)

\,,\hspace{-.5cm}\label{SSk}
\end{aligned}$$

where $\zeta=e^{\frac{2\pi i}{k}}$ as usual, and $(-\zeta^{\frac12})^C$ is understood as $e^{(\frac{i\pi}{k}-i\pi)C}$ for any $C$; and

$$\mathcal{Z}_\hbar^{(k)}[\Delta](Z_i,m_i)  = 
\frac{\big(\zeta^{m_i+1}e^{\frac\hbar k-\frac {Z_i}k};\zeta 
e^{\frac\hbar k}\big)_\infty}
{\big(\zeta^{-m_i}e^{-\frac{2\pi i}{k\hbar}{Z_i}};\zeta^{-1}
e^{\frac{4\pi^2}{k\hbar}}\big)_\infty}
\; =\hspace{-.2cm}
 \prod_{\mbox{$0\leq s,t< k \atop  s-t\,\equiv\, m_i\,(\text{mod}\,k)$}} 
\hspace{-.5cm}\mathcal{Z}_\hbar[\Delta]\Big(\frac {Z_i}k+ \hbar\frac s k 
+2\pi i \frac tk\Big)\,.$$

Recall some well-known facts about the asymptotic expansion of the quantum dilogarithm that can be found, for instance, in [@Za:dilogarithm Sec. II.D].

::: lemma
[]{#lem.AQDL label="lem.AQDL"} We have: $$\log \, (q x;q)_\infty = -\sum_{n=1}^\infty \frac{q^n x^n}{n(1-q^n)} \sim
\sum_{n=0}^\infty \hbar^{n-1} \frac{(-1)^n B_n}{n!} {\rm Li}_{2-n}(x)$$ when $q=e^\hbar$ and $\hbar \rightarrow 0$, where $B_n$ is the $n$-th Bernoulli number and ${\rm Li}_n(x)=\sum_{k=1}^\infty
x^k/n^k$ is the $n$-th polylogarithm. Since $x \partial_x {\rm Li}_{2-n}(x)={\rm Li}_{2-n-1}(x)$, it follows that $$\log \, (e^\hbar e^{-(u + w)}; e^\hbar)_\infty \sim 

\exp\left( \sum_{n,k=0}^\infty \hbar^{n-1} 
\frac{(-1)^{n+k} B_n}{n!k!} {\rm Li}_{2-n-k}(e^{-u})w^k
\right)$$
:::

The asymptotic expansion of $\mathcal{Z}_\hbar^{(k)}$ follows from its product representation,

$$\begin{aligned}
\label{psiexp}
\mathcal{Z}_\hbar^{(k)}[\Delta](Z_i,m_i)  &\sim \prod_{s=0}^{k-1} 
(\zeta^{m_i-s}e^{(1-\frac sk)\hbar-\frac1kZ_i};e^\hbar)_\infty  \notag \\ &
\sim \exp\sum_{n=0}^\infty\sum_{s=1}^{k} \frac{\hbar^{n-1}}{n!}B_n
\big(\tfrac sk\big) {\rm Li}_{2-n}(\zeta^{m_i+s}e^{-Z_i/k}) \\ 
& =  \exp\bigg[\frac1{k\,\hbar}{\rm Li}_2(e^{-Z_i}) - \sum_{s=1}^{k}
\Big(\frac12-\frac sk\Big){\rm Li}_1(\zeta^{m_i+s}e^{-Z_i/k}) + \ldots\bigg]\, \notag
\end{aligned}$$

(where we have substituted $s$ by $k-s$ in the second sum). Notably, the leading asymptotic $\frac1k{\rm Li}_2(e^{-Z_i})$ is independent of $m_i$. Indeed, this remains true for the entire integrand in [\[SSk\]](#SSk){reference-type="eqref" reference="SSk"}.

The critical points $Z^*$ of the integrand at order $\hbar^{-1}$ simply satisfy the standard gluing equation [\[CScrit\]](#CScrit){reference-type="eqref" reference="CScrit"}. Let us assume that the Neumann-Zagier has all $z_i$ strictly in the upper half-plane and focus on the geometric critical point $Z^* = \log(z)$. The value of the integrand at the critical point, at order $\hbar^{-1}$, then becomes (after some manipulation)

$$\exp\frac1 {k\,\hbar}\bigg[-\frac12(Z^*-i\pi f)\cdot((Z^*)''+i\pi f'') 
+ \sum_{i=1}^N {\rm Li}_2(e^{-Z_i^*})\bigg]\,, \label{CSvol}$$

where $(Z^*)'' = \log(1-e^{-Z^*}) = \log z''$. The quantity [\[CSvol\]](#CSvol){reference-type="eqref" reference="CSvol"} appears to agree with the complex hyperbolic volume of a manifold $M$ with Neumann-Zagier datum $\gamma$, modulo $\pi^2/6$ [@DG], though knowing this is unnecessary for obtaining the series $\phi_{\gamma,\zeta}$. On the other hand, it is crucial for our computation that the value at the leading-order saddle point is independent of $m$ --- so all terms in the sum over $m$ contribute equally to the higher-order asymptotics.

By using [\[psiexp\]](#psiexp){reference-type="eqref" reference="psiexp"}, or (better) the double series expansion around the critical point $Z^*$,

$$\mathcal{Z}_\hbar^{(k)}[\Delta](Z_i^*+\delta Z_i,m_i) \sim \exp \sum_{n=0}^\infty
\sum_{j=0}^\infty \frac{\hbar^{n-1}(-\delta Z_i)^j}{k^j\,n! j!} 
\sum_{s=1}^k B_n\big(\tfrac sk\big) {\rm Li}_{2-n-j}(\zeta^{m_i+s}e^{-Z_i^*/k})\,$$

a saddle-point approximation or formal Gaussian integration of [\[SSk\]](#SSk){reference-type="eqref" reference="SSk"} leads immediately to the definition of $\phi_{\gamma,\zeta}(\hbar)$ in Section [\[sec.def\]](#sec.def){reference-type="ref" reference="sec.def"}. Indeed, in the finite-dimensional Feynman calculus, the propagator $\Pi$ is the inverse of the Hessian matrix, appearing at order $\hbar^{-1}$ in the exponent of [\[SSk\]](#SSk){reference-type="eqref" reference="SSk"} as $\frac1k \delta Z\cdot(-\mathbf B^{-1}\mathbf A+\Delta_{(z^*)'})\cdot \delta Z$; while each vertex factor $\Gamma_i^{(j)}$ is the coefficient of $(\delta Z_i)^j$ in the exponent of [\[SSk\]](#SSk){reference-type="eqref" reference="SSk"}.

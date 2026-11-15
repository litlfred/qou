---
doc_id: arxiv-0903.2472v1
doc_title: "Exact Results for Perturbative Chern-Simons Theory with Complex Gauge Group"
section_id: sec-003-222-a-hierarchy-of-differential-equations
section_title: "A hierarchy of differential equations"
section_number: 2.2.2
pages: 20-23
source_pdf: 0903.2472v1.pdf
source_sha256: 637cfd1d4d833c02
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.929
latex_coverage_ratio: 0.979
doc_brief: "Exact Results for Perturbative Chern-Simons Theory with Complex Gauge Group — We develop several methods that allow us to compute all-loop partition functions in perturbative Chern-Simons theory with"
---
[]{#sec:hierarchy label="sec:hierarchy"}

The system of Schrödinger-like equations [\[almonz\]](#almonz){reference-type="eqref" reference="almonz"} determines the perturbative $G_{{\mathbb{C}}}$ invariant $Z^{(\alpha)} (M;\hbar,u)$ up to multiplication by an overall function of $\hbar$, which can be fixed by suitable boundary conditions.

In order to see in detail how the perturbative coefficients $S_n^{(\alpha)}(u)$ may be calculated and to avoid cluttering, let us assume that $r=1$. (A generalization to arbitrary values of $r$ is straightforward.) In this case, $A(l,m)$ is the so-called A-polynomial of $M$, originally introduced in [@cooper-1994], and the system [\[almonz\]](#almonz){reference-type="eqref" reference="almonz"} consists of a single equation $$\widehat{A} (\hat l, \hat m)\,Z^{(\alpha)} (M;\hbar,u) \;=\; 0\,.
\label{ahatcondition}$$ In the $u$-space representation the operator $\hat m = \exp (\hat u)$ acts on functions of $u$ simply via multiplication by $e^u$, whereas $\hat l = \exp (\hat v +i\pi)= \exp (\hbar\;{d \over du})$ acts as a "shift operator": $$\hat m f(u) \;=\; e^u f(u) \,,\qquad
\hat l f(u) \;=\; f(u + \hbar )\,.
\label{lmactonfofu}$$ In particular, the operators $\hat l$ and $\hat m$ obey the relation $$\hat l \hat m  \;=\; q^{{1 \over 2}} \hat m \hat l\,,$$ which follows directly from the commutation relation [\[uvcomm\]](#uvcomm){reference-type="eqref" reference="uvcomm"} for $\hat u$ and $\hat v$, with $$q \;=\; e^{2 \hbar}\;.$$

We would like to recast eq. [\[ahatcondition\]](#ahatcondition){reference-type="eqref" reference="ahatcondition"} as an infinite hierarchy of differential equations that can be solved recursively for the perturbative coefficients $S_n^{(\alpha)}(u)$. Just like its classical limit $A(l,m)$, the operator $\widehat{A} (\hat l, \hat m )$ is a polynomial in $\hat l$. Therefore, pushing all operators $\hat{l}$ to the right, we can write it as $$\widehat{A} (\hat{l},\hat{m}) \;=\; \sum_{j=0}^d a_j (\hat{m},\hbar)\,\hat{l}^j
\label{hatAcoeffs}$$ for some functions $a_j (m,\hbar)$ and some integer $d$. Using [\[lmactonfofu\]](#lmactonfofu){reference-type="eqref" reference="lmactonfofu"}, we can write eq. [\[ahatcondition\]](#ahatcondition){reference-type="eqref" reference="ahatcondition"} as $$\sum_{j=0}^d a_j(m,\hbar) Z^{(\alpha)} (M;\hbar,u + j \hbar ) \;=\; 0\,.
\label{reccompJN}$$ Then, substituting the general form [\[zzpert\]](#zzpert){reference-type="eqref" reference="zzpert"} of $Z^{(\alpha)} (M;\hbar,u)$, we obtain the equation $$\sum_{j=0}^d a_j(m,\hbar)
\exp \left[\frac{1}{\hbar} S_0^{(\alpha)} (u + j\hbar)
-\frac{1}{2} \delta^{(\alpha)} \log \hbar
+ \sum_{n=0}^{\infty} \hbar^n S_{n+1}^{(\alpha)} (u + j\hbar) \right] \;=\; 0\;.
\label{ASintermed}$$ Since $\delta^{(\alpha)}$ is independent of $u$, we can just factor out the $-\frac{1}{2}\delta^{(\alpha)} \log \hbar$ term and remove it from the exponent. Now we expand everything in $\hbar$. Let $$a_j (m,\hbar) \;=\; \sum_{p=0}^{\infty} a_{j,p} (m) \hbar^p \label{aj-hbar}$$ and $$\sum_{n=-1}^{\infty} \hbar^n S_{n+1} ( u + j \hbar)
\;=\; \sum_{r=-1}^{\infty} \sum_{m=-1}^r \frac{j^{r-m}}{(r-m)!} \hbar^r S_{m+1}^{(r-m)} (u)\,,
\label{Sn-hbar}$$ suppressing the index $\alpha$ to simplify notation. We can substitute [\[aj-hbar\]](#aj-hbar){reference-type="eqref" reference="aj-hbar"} and [\[Sn-hbar\]](#Sn-hbar){reference-type="eqref" reference="Sn-hbar"} into [\[ASintermed\]](#ASintermed){reference-type="eqref" reference="ASintermed"} and divide the entire expression by $\exp\hspace{-.05cm}\left(\,\sum_n \hbar^n S_{n+1}(u)\,\right)$. The hierarchy of equations then follows by expanding the exponential in the resulting expression as a series in $\hbar$ and requiring that the coefficient of every term in this series vanishes. The first four equations are shown in Table [\[tab:Seqns\]](#tab:Seqns){reference-type="ref" reference="tab:Seqns"}.

$$\begin{aligned}
\sum_{j=0}^d& e^{j S_0'} a_{j,0} = 0
        \\
\sum_{j=0}^d& e^{j S_0'}\biggl(a_{j,1} + a_{j,0}\bigl(\frac{1}{2}j^2S_0'' + j S_1'\bigr)\biggr) = 0
        \\
\sum_{j=0}^d& e^{j S_0'}\biggl(a_{j,2} + a_{j,1}\bigl(\frac{1}{2}j^2S_0'' + j S_1'\bigr) + a_{j,0}\biggl(\frac{1}{2}\bigl(\frac{1}{2}j^2S_0'' + j S_1'\bigr)^2
+ \frac{j^3}{6}S_0''' + \frac{j^2}{2} S_1'' + jS_2'\biggr)\biggr) = 0
        \\
\sum_{j=0}^d&  e^{j S_0'}\biggl(a_{j,3} + a_{j,2}\bigl(\frac{1}{2}j^2S_0'' + j S_1'\bigr) + a_{j,1}\biggl(\frac{1}{2}\bigl(\frac{1}{2}j^2S_0'' + j S_1'\bigr)^2
+ \frac{j^3}{6}S_0''' + \frac{j^2}{2} S_1'' + jS_2'\biggr)
        \\
&+ a_{j,0}\biggl(\frac{1}{6}\bigl(\frac{1}{2}j^2S_0'' + j S_1'\bigr)^3 + \bigl(\frac{1}{2}j^2S_0'' + j S_1'\bigr)\bigl(\frac{j^3}{6}S_0''' + \frac{j^2}{2} S_1'' + jS_2'\bigr)
        \\
&+ \frac{j^4}{24} S_0^{(4)} + \frac{j^3}{6}S_1''' + \frac{j^2}{2}S_2'' + jS_3'\biggr)\biggr) = 0 \\ \ldots
\end{aligned}$$

The equations in Table [\[tab:Seqns\]](#tab:Seqns){reference-type="ref" reference="tab:Seqns"} can be solved recursively for the $S_n(u)$'s, since each $S_n$ first appears in the $(n+1)^{{\rm st}}$ equation, differentiated only once. Indeed, after $S_0$ is obtained, the remaining equations feature the $S_{n\geq1}$ linearly the first time they occur, and so determine these coefficients uniquely up to an additive constant of integration.

The first equation, however, is somewhat special. Since $a_{j,0}(m)$ is precisely the coefficient of $l^j$ in the classical A-polynomial $A(l,m)$, we can rewrite this equation as $$A(e^{S_0'(u)},e^u)=0\,.$$ This is exactly the classical constraint $A (e^{v + i\pi} , e^u) = 0$ that defines the complex Lagrangian submanifold ${\cal L}$, with $S_0'(u) = v + i\pi$. Therefore, we can integrate along a branch $(l_\alpha=e^{v_\alpha+i\pi},m=e^u)$ of ${\cal L}$ to get the value of the classical Chern-Simons action [\[szero\]](#szero){reference-type="eqref" reference="szero"}, $$S_0^{(\alpha)}(u) = {\rm const} + \int^u \theta \vert_{{\cal L}}\,,
\label{szerowkb}$$ where $\theta \vert_{{\cal L}}$ denotes a restriction to ${\cal L}$ of the Liouville 1-form on ${{\cal M}}_{{\rm flat}}(G_{{\mathbb{C}}}, \Sigma)$, $$\theta = v du + i \pi du\,.
\label{liouvilleform}$$ The expression [\[szerowkb\]](#szerowkb){reference-type="eqref" reference="szerowkb"} is precisely the semi-classical approximation to the wave function $Z^{(\alpha)} (M;\hbar,u)$ supported on the Lagrangian submanifold ${\cal L}$, obtained in the WKB quantization of the classical phase space ${{\cal M}}_{{\rm flat}}(G_{{\mathbb{C}}}, \Sigma)$. By definition, the Liouville form $\theta$ (associated with a symplectic structure $\omega$) obeys $d \theta = i \hbar \omega$, and it is easy to check that this is indeed the case for the forms $\omega$ and $\theta$ on ${{\cal M}}_{{\rm flat}}(G_{{\mathbb{C}}}, \Sigma)$ given by eqs. [\[sympluv\]](#sympluv){reference-type="eqref" reference="sympluv"} and [\[liouvilleform\]](#liouvilleform){reference-type="eqref" reference="liouvilleform"}, respectively.

The semi-classical expression [\[szerowkb\]](#szerowkb){reference-type="eqref" reference="szerowkb"} gives the value of the classical Chern-Simons functional [\[szero\]](#szero){reference-type="eqref" reference="szero"} evaluated on a flat gauge connection ${\cal A}^{(\rho)}$, labeled by a homomorphism $\rho$. As we explained in [\[rhoviaua\]](#rhoviaua){reference-type="eqref" reference="rhoviaua"}, the dependence on $\rho$ is encoded in the dependence on a continuous holonomy parameter $u$, as well as a discrete parameter $\alpha$ that labels different solutions $v_{\alpha} (u)$ to $A (e^{v + i\pi} , e^u) = 0$, at a fixed value of $u$. In other words, $\alpha$ labels different branches of the Riemann surface $A(l,m) = 0$, regarded as a cover of the complex plane ${\mathbb{C}}$ parametrized by $m = e^u$, $$A (l_{\alpha} , m) = 0\,.
\label{abranches}$$ Since $A(l,m)$ is a polynomial in both $l$ and $m$, the set of values of $\alpha$ is finite (in fact, its cardinality is equal to the degree of $A(l,m)$ in $l$). Note, however, that for a given choice of $\alpha$ there are infinitely many ways to lift a solution $l_{\alpha} (u)$ to $v_{\alpha} (u)$; namely, one can add to $v_{\alpha} (u)$ any integer multiple of $2\pi i$. This ambiguity implies that the integral [\[szerowkb\]](#szerowkb){reference-type="eqref" reference="szerowkb"} is defined only up to integer multiples of $2 \pi i u$, $$S_0^{(\alpha)}(u) - {\rm const}
=  \int^u\log l_\alpha(u')\;du' = \int^u v_\alpha(u')\;du'
\;+\; i \pi u \qquad (\mbox{mod}\;2\pi i u)\;.
\label{S0_integral}$$ In practice, this ambiguity can always be fixed by imposing suitable boundary conditions on $S_0^{(\alpha)}(u)$, and it never affects the higher-order terms $S_n^{(\alpha)}(u)$. Therefore, since our main goal is to solve the *quantum* theory (to all orders in perturbation theory) we shall not worry about this ambiguity in the classical term. As we illustrate later (see Section [\[sec:figeightquant\]](#sec:figeightquant){reference-type="ref" reference="sec:figeightquant"}), it will always be easy to fix this ambiguity in concrete examples.

Before we proceed, let us remark that if $M$ is a hyperbolic 3-manifold with a single torus boundary $\Sigma = \partial M$ and ${\cal A}^{({\rm geom})}$ is the "geometric" flat $SL(2,{\mathbb{C}})$ connection associated with a hyperbolic metric on $M$ (not necessarily geodesically complete), then the integral [\[S0_integral\]](#S0_integral){reference-type="eqref" reference="S0_integral"} is essentially the complexified volume function, $i({\mbox{Vol\,}}(M;u) +i {\rm CS} (M;u))$, which combines the (real) hyperbolic volume and Chern-Simons invariants [^1]

of $M$. Specifically, the relation is [@gukov-2003; @nz-1985]: $$S_0^{({\rm geom})} (u)
= \frac{i}{2}\Big[ {\mbox{Vol\,}}(M;u) +  i {\rm CS} (M;u) \Big]
+ \,v_{{\rm geom}}(u)\,{\rm Re}\,(u) \,+\, i \pi u\,,
\label{S0_volume}$$ modulo the integration constant and multiples of $2\pi i u$.

[^1]: For example, imaginary $u$ parametrizes a conical singularity. See, *e.g.* [@thurston-1980; @nz-1985; @yoshida-1985] and our discussion in Section [\[sec:ideal\]](#sec:ideal){reference-type="ref" reference="sec:ideal"} for more detailed descriptions of ${\mbox{Vol\,}}(M;u)$ and ${\rm CS} (M;u)$. In part of the literature (*e.g.* in [@nz-1985]), the parameters $(u,v)$ are related to those used here by $2u_{\rm here}=u_{\rm there}$ and $2(v_{\rm here}+i\pi)=v_{\rm there}$. We include a shift of $i\pi$ in our definition of $v$ so that the complete hyperbolic structure arises at $(u,v)=(0,0)$.

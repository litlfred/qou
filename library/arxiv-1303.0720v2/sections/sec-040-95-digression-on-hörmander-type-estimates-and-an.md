---
doc_id: arxiv-1303.0720v2
doc_title: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS"
section_id: sec-040-95-digression-on-hörmander-type-estimates-and-an
section_title: "Digression on Hörmander-type estimates and an obstacle problem. We should like to"
section_number: 9.5
pages: 35-37
source_pdf: 1303.0720v2.pdf
source_sha256: 389ab465e81a0667
doc_brief: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS — We consider the q-analytic functions on a given planar domain Ω, square integrable with respect to a weight."
text_source: latex
latex_prose_ratio: 0.697
latex_coverage_ratio: 0.933
---
We should like to apply Proposition [\[prop-hormiter\]](#prop-hormiter){reference-type="ref" reference="prop-hormiter"} with $\phi:=mQ$. Then we need the assumptions of the proposition to be valid: $$\label{eq-9.4.1}
\varDelta Q>0\quad\text{and}\quad\frac{1}{2\varDelta Q}\varDelta\log\varDelta Q>-m
\quad\text{on}\,\,\,\Omega.$$ The latter criterion apparently gets easier to fulfill as $m$ grows. In the analytic case $q=1$ only the criterion $\Delta Q>0$ is needed, and in fact, it can be relaxed rather substantially (see [@ahm1] for the polynomial setting). Basically, what happens is that we may sometimes replace the potential $Q$ by its subharmonic minorant $\check Q$ given by $$\check Q(z):=\sup\big\{u(z):\,u\in\mathrm{Subh}(\Omega),\,\,\text{and}\,\,
u\le Q \,\,\text{on}\,\,\Omega\big\},$$ where $\mathrm{Subh}(\Omega)$ denotes the cone of subharmonic functions; see Theorem 4.1 [@ahm1] for details (in the polynomial setting). In principle, the Bergman kernel should be well approximated by the local Bergman kernel if $\check Q=Q$ in a neighborhood of the given point $z_0$. From the conceptual point of view, what is important is that for an analytic function $f$, the expression $\frac{1}{m}\log|f|$ is subharmonic (and in fact in the limit as $m$ grows to infinity we can approximate all subharmonic functions with expressions of this type). In our present bianalytic setting, $\frac{1}{m}\log|f|$ need not be subharmonic, but we still suspect that it approximately subharmonic for large $m$. So we expect that [\[eq-9.4.1\]](#eq-9.4.1){reference-type="eqref" reference="eq-9.4.1"} can be relaxed to $\check Q=Q$ near the point $z_0$ plus (if needed) some suitable replacement of the second (curvature type) criterion of [\[eq-9.4.1\]](#eq-9.4.1){reference-type="eqref" reference="eq-9.4.1"}.

## Analysis of the second term in the pointwise estimate II

As we apply Proposition [\[prop-hormiter\]](#prop-hormiter){reference-type="ref" reference="prop-hormiter"} to $\phi=mQ$, the result is the following.

::: prop
Let $\Omega$ be a domain in ${\mathbb C}$ and suppose $Q:\Omega\to{\mathbb R}$ is $C^4$-smooth with both $\varDelta Q>0$ on $\Omega$ and $$\kappa:=\sup_{\Omega}\frac{1}{2\varDelta Q}\varDelta
\log\frac{1}{\varDelta Q}<+\infty.$$ Assume that $f\in L^2_{\mathrm{loc}}(\Omega)$. Then there exists a (norm-minimal) solution $v_0$ to the problem $\bar\partial^2v_0=f$ with $$\int_{\Omega} |v_0|^2 \mathrm{e}^{-2mQ}\mathrm{d}A \le\frac{1}{4m(m-\kappa)}\int_{\Omega} |f|^2 
\frac{\mathrm{e}^{-2mQ}}{[\varDelta Q]^2}\mathrm{d}A,$$ provided that $m>\kappa$ and that the right-hand side is finite. []{#prop-hormiter2 label="prop-hormiter2"}
:::

We now apply the above proposition with $$\begin{gathered}
f(z):=\bar\partial_z^2[\chi_0(z)K^{\langle k\rangle}_{2,m}(z,w)]=
K^{\langle k\rangle}_{2,m}(z,w)\,\bar\partial^2\chi_0(z)+
2[\bar\partial\chi_0(z)][\bar\partial_zK^{\langle k\rangle}_{2,m}(z,w)]
\\
=\big\{\Lfun^{\langle2,k\rangle}(z,w)\,\bar\partial^2\chi_0(z)+
2[\bar\partial\chi_0(z)][\bar\partial_z\Lfun^{\langle2,k\rangle}(z,w)]\big\}
\mathrm{e}^{2mQ(z,w)},
\end{gathered}$$

and calculate that $$\begin{gathered}
|f(z)|\mathrm{e}^{-mQ(z)}\le\big\{|\bar\partial^2\chi_0(z)\Lfun^{\langle2,k\rangle}(z,w)|+
2|\bar\partial\chi_0(z)\bar\partial_w\Lfun^{\langle2,k\rangle}(z,w)|\big\}
\mathrm{e}^{m\mathop{\mathrm{Re}}[2Q(z,w)-Q(z)]}
\\
\le\big\{|\bar\partial^2\chi_0(z)\Lfun^{\langle2,k\rangle}(z,w)|+
2|\bar\partial\chi_0(z)\bar\partial_z\Lfun^{\langle2,k\rangle}(z,w)|\big\}
\mathrm{e}^{mQ(w)-\delta_0 m},
\end{gathered}$$ where as before $\delta_0=\frac{1}{18}r^2\epsilon_0$ and it is assumed that $w\in{\mathbb D}(z_0,\frac13r_0)$. Under the assumptions on $Q$ stated in Proposition [\[prop-hormiter2\]](#prop-hormiter2){reference-type="ref" reference="prop-hormiter2"}, we obtain from that proposition (recall the definition of [\[eq-defv0\]](#eq-defv0){reference-type="eqref" reference="eq-defv0"}) and the above calculation that $$\begin{gathered}
\big\|K^{\langle k\rangle}_{2,m}(\cdot,w) 
\chi_0-{\mathbf P}_{2,m}[K^{\langle k\rangle}_{2,m}(\cdot,w)\chi_0]\big\|_m
\\
\le \frac{[\epsilon_0]^{-1}}{2m^{1/2}(m-\kappa)^{1/2}}\mathrm{e}^{mQ(w)-\delta_0 m}
\big\{\|\bar\partial^2\chi_0\|_{L^2(\Omega)}
\,\|\Lfun^{\langle2,k\rangle}\|_{L^\infty({\mathbb D}(z_0,\frac34r)^2)}+
2\|\bar\partial\chi_0\|_{L^2(\Omega)}
\|\bar\partial_z\Lfun^{\langle2,k\rangle}\|_{L^\infty({\mathbb D}(z_0,\frac34r)^2)}\big\}
\\
=\mathrm{O}\bigg((m\epsilon_0)^{-1}\mathrm{e}^{mQ(w)-\delta_0 m}\big\{
r^{-1}\|\Lfun^{\langle2,k\rangle}\|_{L^\infty({\mathbb D}(z_0,\frac34r)^2)}+
\|\bar\partial_z\Lfun^{\langle2,k\rangle}\|_{L^\infty({\mathbb D}(z_0,\frac34r)^2)}\big\}\bigg),
\label{eq-9.6.1}
\end{gathered}$$ where the implied constant is absolute and $w\in{\mathbb D}(z_0,\frac13r_0)$, and we assume that $m\ge2\kappa$. If we accept a constant which depends on the triple $(Q,z_0,r)$, then we can simplify [\[eq-9.6.1\]](#eq-9.6.1){reference-type="eqref" reference="eq-9.6.1"} significantly: $$\big\|K^{\langle k\rangle}_{2,m}(\cdot,w) 
\chi_0-{\mathbf P}_{2,m}[K^{\langle k\rangle}_{2,m}(\cdot,w)\chi_0]\big\|_m
=\mathrm{O}(m\mathrm{e}^{mQ(w)-\delta_0 m}),
\label{eq-9.6.2}$$ because the two norms of $\Lfun^{\langle2,k\rangle}$ and $\bar\partial_z\Lfun^{\langle2,k\rangle}$ grow like $\mathrm{O}(m^2)$. Finally, we combine this norm estimate [\[eq-9.6.2\]](#eq-9.6.2){reference-type="eqref" reference="eq-9.6.2"} with control on the point evaluation at $z$ (see Proposition [\[pointwise2\]](#pointwise2){reference-type="ref" reference="pointwise2"}): $$\big|K^{\langle k\rangle}_{2,m}(z,w) 
\chi_0(z)-{\mathbf P}_{2,m}[K^{\langle k\rangle}_{2,m}(\cdot,w)\chi_0](z)\big|
=\mathrm{O}(m^{3/2}\mathrm{e}^{mQ(z)+mQ(w)-\delta_0 m}),\qquad z,w\in{\mathbb D}(z_0,\tfrac13r).
\label{eq-9.6.3}$$

## The pointwise distance to the weighted Bergman kernel

Here, we apply the estimates [\[eq-9.2.8\]](#eq-9.2.8){reference-type="eqref" reference="eq-9.2.8"} and [\[eq-9.6.3\]](#eq-9.6.3){reference-type="eqref" reference="eq-9.6.3"} with the (basic) estimate [\[glob1\]](#glob1){reference-type="eqref" reference="glob1"}. As before, the integer $k$ is fixed.

::: thm
[]{#thm-9.3 label="thm-9.3"} Let $\Omega$ be a domain in ${\mathbb C}$ and suppose $Q:\Omega\to{\mathbb R}$ is $C^4$-smooth with both $\varDelta Q>0$ on $\Omega$ and $$\kappa:=\sup_{\Omega}\frac{1}{2\varDelta Q}\varDelta
\log\frac{1}{\varDelta Q}<+\infty.$$ Assume moreover that $Q$ has the properties (A:i)--(A:iv) (see Subsection [\[subsec-assQ\]](#subsec-assQ){reference-type="ref" reference="subsec-assQ"}) on the disk ${\mathbb D}(z_0,r)\subset\Omega$. We fix an integer $k\ge0$ and assume that the approximate local Bergman kernel $K_{2,m}^{\langle k\rangle}(z,w)=\Lfun^{\langle2,k\rangle}\mathrm{e}^{2mQ(z,w)}$ extends to a separately bianalytic function of the variables $(z,\bar w)$ in the small bidisk ${\mathbb D}(z_0,r)\times{\mathbb D}(z_0,r)$. Then, for $m\ge\max\{2\kappa,1\}$, we have that $$K_{2,m}(z,w)=K^{\langle k\rangle}_{2,m}(z,w)+\mathrm{O}(m^{-k}\mathrm{e}^{mQ(z)+mQ(w)}),\qquad
z,w\in{\mathbb D}(z_0,\tfrac13r),$$ where the implied constant depends only on the triple $(Q,z_0,r)$.
:::

This means that the approximate kernel $K_{2,m}^{\langle k\rangle}$ is close to the true kernel $K_{2,m}$ locally near $z_0$.

::: proof
*Proof of Theorem [\[thm-9.3\]](#thm-9.3){reference-type="ref" reference="thm-9.3"}.* Since $\chi_0(z)=1$ for $z\in{\mathbb D}(z_0,\frac23r)$, the assertion follows from [\[eq-9.2.8\]](#eq-9.2.8){reference-type="eqref" reference="eq-9.2.8"} and [\[eq-9.6.3\]](#eq-9.6.3){reference-type="eqref" reference="eq-9.6.3"} once we observe that exponential decay is faster than power decay. ◻
:::

::: proof
*Proof of Theorem [\[blowupthm\]](#blowupthm){reference-type="ref" reference="blowupthm"}.* We express $\Lfun^{\langle 2,0\rangle}=m^2\Lfun^2_0+m\Lfun_1^2$ using the formulae obtained for $\Lfun^2_j$ for $j=0,1$ (see Remark [\[rem-AA\]](#rem-AA){reference-type="ref" reference="rem-AA"}). We also use that $2\mathop{\mathrm{Re}}Q(z,w)-Q(w)-Q(z)=-|w-z|^2\varDelta Q(z)+\mathrm{O}(|z-w|^3)$. The assertion follows after a number of tedious computations based on Taylor's formula. ◻
:::

::: rem
We have already obtained $K^{\langle k\rangle}_{2,m}$ explicitly for $k\le1$ and the assumptions made on $K^{\langle k\rangle}_{2,m}$ in the theorem are clearly fulfilled then. We believe that they are fulfilled for all other values of $k$ as well.
:::

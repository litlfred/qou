---
doc_id: arxiv-1106.2975v1
doc_title: "The Polyanalytic Ginibre Ensembles"
section_id: sec-004-5-reproducing-kernel-and-berezin-density-asympto
section_title: "Reproducing kernel and Berezin density asymptotics for a boundary point"
section_number: 5
pages: 23-30
source_pdf: 1106.2975v1.pdf
source_sha256: 7e966c7392b70ae0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.972
latex_coverage_ratio: 0.963
doc_brief: "The Polyanalytic Ginibre Ensembles — For integers n, q = 1, 2, 3, . . ., let Poln,q denote the C-linear space of polynomials in z and ¯z, of degree ≤n −1 in z and of degree ≤q −1 in ¯z."
---
In this section, we will calculate the limit of the blow-up berezin transform $\hat{\berd}^{\langle z\rangle}_{m,n,q}$ at a boundary point $z$, that is, $|z|=1$. There is no loss of generality to take $z=1$. Our strategy is to investigate the blow-up of the reproducing kernel of the space of analytic polynomials $\mathrm{Pol}_{m,n,1}$ (with $q=1$) first, and then use this information together with poly-Bargmann transform to lift the the asymptotics to the context of the general polyanalytic spaces $\mathrm{Pol}_{m,n,q}$.

The following improvement of the central limit theorem will be needed. Let $\mathrm{cdf}_X$ denote the cumulative distribution function of a real-valued random variable $X$ and let $$\mathrm{erf}(z) = \frac{1}{\sqrt{2 \pi}} 
\int_{- \infty}^z \mathrm e^{-\frac12t^2} {\mathrm d}t$$ be the error function. We shall write i.i.d. as shorthand for *independent identically distributed* in the context of random variables. The following result is from [@berry], [@esseen].

::: thm
Let $X_1, X_2, ...$ be i.i.d. real-valued random variables with $E(X_j)=0$, $E(X_j^2)=1$ and $E(|X_j|^3)=\rho<+\infty$ for all $j$. Also, let $Y_n = n^{-1/2}\sum_{j=1}^{n} X_j$. Then there exists an absolute constant $C$ such that $$\left| \mathrm{cdf}_{Y_n}(x) - \mathrm{erf}(x) \right| 
\leq \frac{C \rho}{\sqrt{n}}, \qquad x\in{\mathbb R}.$$
:::

The Berry-Esséen theorem gives the following asymptotics for the partial Taylor sums of the exponential function.

::: lem
[]{#erflemma label="erflemma"} We have $$\frac{E_{n-1}(x)}{\mathrm e^x} = \mathrm{erf}\bigg(\frac{n-x}{\sqrt{n}}\bigg) 
+ \mathrm{O}(n^{-1/2}),$$ as $n\to+\infty$, uniformly in $x\in[0,+\infty[$.
:::

::: proof
*Proof.* Let $X_1,...,X_n$ be independent exponentially distributed random variables on $[0,+\infty[$ with density $\mathrm e^{-x}$. It is well known that the sum $\sum_{j=1}^nX_j$ obeys a gamma distribution with the cumulative distribution function $1- \mathrm e^{-x}E_{n-1}(x)$. The random variables $X_1-1, ..., X_n-1$ all have zero mean and variance $1$, and the third moment is finite, so by the Berry-Esséen theorem, we have $$1-\mathrm e^{-x}E_{n-1}(x)=\text{cdf}_{\sum_{j=1}^n X_j}(x) 
=\mathrm{cdf}_{\frac{\sum_{j=1}^n X_j -n }{\sqrt{n}}}
\bigg(\frac{x-n}{\sqrt{n}}\bigg) 
=\mathrm{erf}\bigg(\frac{x-n}{\sqrt{n}}\bigg)+\mathrm{O}(n^{-1/2}),$$ where the "$\mathrm{O}$" term is uniform in $x$ as $n\to+\infty$. ◻
:::

This allows us to blow up the function $E_{n-1}(mz\bar w)$ when $z$ and $w$ are close to the point $1$ and $m,n\to+\infty$ with $n=m+\mathrm{O}(1)$.

::: lem
[]{#analyticbdrblowup label="analyticbdrblowup"} Fix a positive real $\varepsilon$. For complex $\xi,\eta\in{\mathbb C}$, we then have $$\frac{E_{n-1}\left(m(1+m^{-1/2}\xi)(1+ m^{-1/2}\bar{\eta})\right)}
{\mathrm e^{m+ \sqrt{m}(\xi+\bar\eta)}} = \mathrm e^{\xi\bar{\eta}}
\,\mathrm{erf}(-\xi- \bar\eta)+\mathrm{O}(m^{-\frac12+\varepsilon}),$$ as $m,n\to+\infty$ while $n=m+\mathrm{O}(1)$. Here, the "$\mathrm{O}$" expression on the right-hand side is uniform on compact subsets of ${\mathbb C}$.
:::

::: proof
*Proof.* If we put $$\zeta:=m(1+m^{-1/2}\xi)(1+m^{-1/2}\bar\eta)=m+m^{1/2}
(\xi+\bar\eta)+\xi\bar\eta,$$ then $$\frac{n-\zeta}{\sqrt{n}}=\frac{n-m-m^{1/2}(\xi+\bar\eta)-\xi\bar\eta}{\sqrt{n}}
=-\xi-\bar\eta+\mathrm{O}(m^{-1/2}),$$ where the "O" term is uniform on compact subsets. If we use that $E_{n-1}$ has only nonnegative Taylor coefficients, we get from Lemma [\[erflemma\]](#erflemma){reference-type="ref" reference="erflemma"} that $$\label{eq-t1}
\frac{|E_{n-1}(\zeta)|}{\mathrm e^{|\zeta|}}\le \frac{E_{n-1}(|\zeta|)}{\mathrm e^{|\zeta|}}
=\mathrm{erf}\bigg(\frac{n-|\zeta|}{\sqrt{n}}\bigg) 
+\mathrm{O}(n^{-1/2}),$$ with a uniform "O" term. So, for *real* $\xi,\eta$, we may deduce from [\[eq-t1\]](#eq-t1){reference-type="eqref" reference="eq-t1"} the assertion of the lemma with $\varepsilon=0$. For general complex $\xi,\eta$, we note that $$\begin{gathered}
|\zeta|=m\,|(1+m^{-1/2}\xi)(1+m^{-1/2}\bar\eta)|
\\
=m+m^{1/2}\operatorname{Re}[\xi+\eta]+
\operatorname{Re}\xi\operatorname{Re}\eta+\tfrac12(\operatorname{Im}\xi)^2+\tfrac12(\operatorname{Im}\eta)^2+\mathrm{O}(m^{-1/8})
\end{gathered}$$ uniformly in the domain where $\max\{|\xi|,|\eta|\}\le m^{1/8}$. As the right-hand side of [\[eq-t1\]](#eq-t1){reference-type="eqref" reference="eq-t1"} is $\le\frac32$ for big $n$, we see that $$\begin{gathered}
\Bigg|\frac{E_{n-1}\left(m(1+m^{-1/2}\xi)(1+ m^{-1/2}{\eta})\right)}
{\mathrm e^{m+ \sqrt{m}(\xi+\eta)+\xi\bar\eta}}\Bigg|
\le\frac32\mathrm e^{-(\operatorname{Im}\xi)(\operatorname{Im}\eta)+\tfrac12(\operatorname{Im}\xi)^2+\tfrac12(\operatorname{Im}\eta)^2+
\mathrm{O}(m^{-1/8})}
\\
\le2\mathrm e^{\frac12[\operatorname{Im}\xi-\operatorname{Im}\eta]^2} 
\end{gathered}$$ holds in the domain where $\max\{|\xi|,|\eta|\}\le m^{1/8}$, provided $m$ is big enough. We need to show that he difference $$F_{m,n}(\xi,\eta):=\frac{E_{n-1}\left(m(1+m^{-1/2}{\xi})
(1+m^{-1/2}\bar\eta)\right)}{\mathrm e^{m+ \sqrt{m}(\xi+\bar\eta)+\xi\bar\eta}} - 
\mathrm{erf}(-\xi-\bar\eta)$$ is of order $\mathrm{O}(m^{-1/2+\varepsilon})$ uniformly as $\xi,\eta$ remain confined to some compact subset of ${\mathbb C}$. We know that $F_{m,n}(\xi,\eta)=\mathrm{O}(m^{-1/2})$ uniformly when $\xi,\eta\in{\mathbb R}$ with confined to $\max\{|\xi|,|\eta|\}\le m^{1/8}$. In view of the calculation we just made, we also have a good uniform estimate of $F_{m,n}(\xi,\eta)$ when $\xi,\eta\in{\mathbb C}$ with $\max\{|\xi|,|\eta|\}\le m^{1/8}$. By employing a standard technique involving the subharmonicity of $\xi\mapsto\log|F_{m,n}(\xi,\eta)|$, and certain classical estimates of harmonic measure, we can show that $F_{m,n}(\xi,\eta)=\mathrm{O}(m^{\epsilon-1/2})$ holds uniformly when $\xi,\eta\in{\mathbb C}$ belong to a compact subset of ${\mathbb C}$, and in addition, $\eta\in{\mathbb R}$. Here, $\epsilon$ is a positive number which we can get as small as we like. A similar argument with $\eta$ in place $\xi$ worsens the control to $F_{m,n}(\xi,\eta)=\mathrm{O}(m^{2\epsilon-1/2})$, but now the control is uniform when both $\xi,\eta$ are both complex and confined to some compact subset. The proof is complete with $\varepsilon=2\epsilon$. ◻
:::

We shall identify both the right-hand and the left-hand side expressions appearing in Lemma [\[analyticbdrblowup\]](#analyticbdrblowup){reference-type="ref" reference="analyticbdrblowup"} with reproducing kernels of certain Hilbert spaces of entire functions. This will be the case $r=0$ of the proposition below.

Let us agree to identify $$L^2({\mathbb R}_-) =\{ f\in L^2(\mathbb{R}):\,\, f(x)=0 \,\,\text{ for }\,\, x>0\}.$$

::: prop
[]{#polybargmannkernel label="polybargmannkernel"} For $r=0,1,2,\ldots$, the function $$(\xi,\eta)\mapsto\frac{\mathrm e^{\xi\bar\eta}}{r! \sqrt{2 \pi}}
\int_{-\infty}^{-\xi-\bar\eta} H_r(t+\xi-\eta)
H_r(t+\bar\eta-\bar\xi)\mathrm e^{-\frac12t^2} {\mathrm d}t$$ is the reproducing kernel for the Hilbert space ${\mathbf B}_r[L^2({\mathbb R}_-)]\subset 
A^2_{1,r+1}({\mathbb C})$.
:::

::: proof
*Proof.* Let $M(\xi,\eta)=M_{\eta}(\xi)$ be the reproducing kernel for ${\mathbf B}_r[ L^2({\mathbb R}_-)]$. This kernel has $M_\eta\in{\mathbf B}_r[L^2({\mathbb R}_-)]$ and $$\begin{gathered}
\frac{1}{\sqrt{r!}(2\pi)^{1/4}} \int_{{\mathbb R}}f(t)H_r(t-\eta-\bar{\eta})
\mathrm e^{t\eta-\frac12\eta^2-\frac14t^2}{\mathrm d}t
= {\mathbf B}_r[f](\eta) \\
= \langle {\mathbf B}_r[f], M_{\eta} \rangle_{A^2_{1,r+1}({\mathbb C})} = 
\langle f, {\mathbf B}_r^{-1}[M_{\eta}] \rangle_{L^2({\mathbb R})} 
\end{gathered}$$ for all $\eta\in{\mathbb C}$ and all $f\in L^2({\mathbb R}_-)$, which allows us to conclude that $${\mathbf B}_r^{-1}[M_{\eta}](t)  
=(r!)^{-1/2}(2\pi)^{-1/4}1_{]-\infty,0]}(t)\, H_r(t-\eta-\bar{\eta})\,
\mathrm e^{t\bar\eta-\frac12\bar{\eta}^2-\frac14t^2}.$$ After applying the operator ${\mathbf B}_r$ to both sides, we see that (cf. Proposition [\[prop-Br\]](#prop-Br){reference-type="ref" reference="prop-Br"}) $$\begin{gathered}
 M_{\eta}(\xi) = \frac{1}{r!\sqrt{2\pi}} \int_{-\infty}^{0} 
H_r(t-\xi-\bar{\xi}) \mathrm e^{t \xi- \frac12\xi^2-\frac14 t^2} 
H_r(t-\eta-\bar{\eta}) \mathrm e^{t\bar{\eta}-\frac12\bar{\eta}^2-\frac14t^2} 
{\mathrm d}t 
\\
=\frac{\mathrm e^{\bar{\eta} \xi}}{r! \sqrt{2\pi}} 
\int_{-\infty}^{0} H_r(t-\xi-\bar{\xi}) 
H_r(t-\eta-\bar{\eta}) \mathrm e^{-\frac{1}{2}(t - \xi - \bar{\eta})^2} 
{\mathrm d}t 
\\
=\frac{\mathrm e^{\bar{\eta}\xi}}{r! \sqrt{2\pi}} \int_{-\infty}^{-\bar{\eta}-\xi} 
H_r(t + \bar{\eta} - \bar{\xi}) 
H_r(t+\xi-\eta) \mathrm e^{-\frac{1}{2}t^2} {\mathrm d}t. 
\end{gathered}$$ The proof is complete. ◻
:::

::: rem
The special case $r=0$ of the kernel in Proposition [\[polybargmannkernel\]](#polybargmannkernel){reference-type="ref" reference="polybargmannkernel"} is $\mathrm e^{\xi\bar\eta}\mathrm{erf}(-\xi-\bar\eta)$, which is what we have on the right-hand side in Lemma [\[analyticbdrblowup\]](#analyticbdrblowup){reference-type="ref" reference="analyticbdrblowup"}.
:::

We turn to the polyanalytic analogue of the left-hand side of Lemma [\[analyticbdrblowup\]](#analyticbdrblowup){reference-type="ref" reference="analyticbdrblowup"}.

::: defn
We introduce the *blow-up space at* $1$, $$\mathrm{Pol}^{\langle1\rangle}_{m,n,q} := 
\big\{\mathrm e^{-{m}^{1/2}\xi}p(1+m^{-1/2}\xi):\,\, p \in \mathrm{Pol}_{m,n,q} 
\big\},$$ which we equip with the norm $$\big\|\xi\mapsto \mathrm e^{-{m}^{1/2}\xi}p(1+m^{-1/2}\xi)
\big\|_{{{\delta\mathrm{Pol}}}^{\langle1\rangle}_{m,n,q}}:=m^{1/2}\mathrm e^{\frac12m}
\|p\|_{L^2({\mathbb C},\mathrm e^{-m|z|^2})}.$$ For $0\le r\le q-1$, we denote by ${\delta\mathrm{Pol}}^{\langle1\rangle}_{m,n,r+1}$ the subspace $${\delta\mathrm{Pol}}^{\langle1\rangle}_{m,n,r+1} := 
\big\{\mathrm e^{-{m}^{1/2}\xi}p(1+m^{-1/2}\xi):\,\, p \in {\delta\mathrm{Pol}}_{m,n,r+1} 
\big\},$$ equipped with the same norm.
:::

An elementary change of variables argument allows us to identify the norm on $\mathrm{Pol}^{\langle1\rangle}_{m,n,q}$ with that of $A^2_{m,q}({\mathbb C})$: $$\label{normidentity}
\big\|\xi\mapsto \mathrm e^{-{m}^{1/2}\xi}p(1+m^{-1/2}\xi)
\big\|_{\mathrm{Pol}^{\langle1\rangle}_{m,n,r+1}}=
\big\|\xi\mapsto \mathrm e^{-{m}^{1/2}\xi}p(1+m^{-1/2}\xi)
\big\|_{A^2_{1,r+1}({\mathbb C})}.$$ As a consequence, we may regard $\mathrm{Pol}^{\langle1\rangle}_{m,n,q}$ and ${{\delta\mathrm{Pol}}}^{\langle1\rangle}_{m,n,r+1}$ as norm closed subspaces of $A^2_{1,q}({\mathbb C})$. We may read off from the definition of the norm in ${{\delta\mathrm{Pol}}}^{\langle1\rangle}_{m,n,r+1}$ that the kernel on the left-hand side in Lemma [\[analyticbdrblowup\]](#analyticbdrblowup){reference-type="ref" reference="analyticbdrblowup"} is the reproducing kernel for the space $\mathrm{Pol}^{\langle1\rangle}_{m,n,1}$. So, Lemma [\[analyticbdrblowup\]](#analyticbdrblowup){reference-type="ref" reference="analyticbdrblowup"} can be understood as saying that $$\label{analytictildeconvergence}
K_{\mathrm{Pol}^{\langle1\rangle}_{m,n,1}}(\xi,\eta)= 
K_{{\mathbf B}_0[L^2({\mathbb R}_-)]}(\xi,\eta)+\mathrm{O}(m^{-\frac12+\varepsilon}),$$ where $K_{\mathrm{Pol}_{m,n,1}}$ and $K_{{\mathbf B}_0[L^2({\mathbb R}_-)]}$ denote the reproducing kernels of the spaces in the subscripts, and the bound is locally uniform on compact subsets. We want to generalize [\[analytictildeconvergence\]](#analytictildeconvergence){reference-type="eqref" reference="analytictildeconvergence"} beyond $r=0$. To this end, we make use of the operators ${\mathbf T}_{r}$.

::: prop
[]{#lem-T1 label="lem-T1"} For $r=1,2,3,\ldots$, we have that $$r^{-1/2}{\mathbf T}_{1}:\,{{\delta\mathrm{Pol}}}^{\langle1\rangle}_{m,n,r}\to
{{\delta\mathrm{Pol}}}^{\langle1\rangle}_{m,n,r+1}$$ is an isometric isomorphism.
:::

::: proof
*Proof.* From the isometry properties of ${\mathbf T}_{r-1}$ and ${\mathbf T}_{r}$ together with the semi-group property $r^{-1/2}{\mathbf T}_{1}\circ{\mathbf T}_{r-1}={\mathbf T}_{r}$, we get that $$r^{-1/2}{\mathbf T}_{1}:\,\delta A^2_{1,r}({\mathbb C})\to\delta A^2_{1,r+1}({\mathbb C})$$ is an isometric isomorphism. In view of [\[normidentity\]](#normidentity){reference-type="eqref" reference="normidentity"}, the isometry part of the assertion follows. It remains to show that the operator is onto. This is an algebraic exercise which we leave to the reader. ◻
:::

By iterating Proposition [\[lem-T1\]](#lem-T1){reference-type="ref" reference="lem-T1"}, we obtain the following.

::: cor
[]{#tildecor label="tildecor"} For $r=1,2,3\ldots$, we have that $${\mathbf T}_r:\mathrm{Pol}^{\langle1\rangle}_{m,n,1}\to
{\delta\mathrm{Pol}}^{\langle1\rangle}_{m,n,r+1}$$ is an isometric isomorphism.
:::

From Corollary [\[tildecor\]](#tildecor){reference-type="ref" reference="tildecor"} above, we get that $$\label{eq-kerneltop}
K_{{\delta\mathrm{Pol}}^{\langle1\rangle}_{m,n,r+1}}(\xi,\eta)=[{\mathbf T}_r]_\xi
[\bar{\mathbf T}_r]_\eta
\big(K_{\mathrm{Pol}^{\langle1\rangle}_{m,n,1}}(\xi,\eta)\big),$$ where the subscripts $z$ and $w$ are used to indicate that the operator is acting with respect to that variable, and the bar means complex conjugation of the operator. To be more precise, $$\bar{\mathbf T}_r[f](z):=\frac{1}{\sqrt{r!}} \mathrm e^{|z|^2}\,
\bar\partial_z^r\big\{f(z)\mathrm e^{-|z|^2}\big\}.$$ We would like to plug in the approximation [\[analytictildeconvergence\]](#analytictildeconvergence){reference-type="eqref" reference="analytictildeconvergence"} into [\[eq-kerneltop\]](#eq-kerneltop){reference-type="eqref" reference="eq-kerneltop"}. The operator ${\mathbf T}_r$ is a sum of certain polynomials in $\bar z$ of degree $\le r$ times the differential operator $\partial_z$ to powers $\le r$. The Cauchy integral formula allows us to control the size of the derivatives on a compact subset in terms of the size of the functions on a slightly bigger compact subset. This means that the approximation [\[analytictildeconvergence\]](#analytictildeconvergence){reference-type="eqref" reference="analytictildeconvergence"} carries over, and we find that $$\label{analytictildeconvergence2}
K_{{\delta\mathrm{Pol}}^{\langle1\rangle}_{m,n,r+1}}(\xi,\eta)= 
[{\mathbf T}_r]_\xi
[\bar{\mathbf T}_r]_\eta
\big(K_{{\mathbf B}_0[L^2({\mathbb R}_-)]}(\xi,\eta)\big)+\mathrm{O}(m^{-\frac12+\varepsilon}),$$ with uniform control on compact subsets. Next, as $$\mathrm{Pol}^{\langle1\rangle}_{m,n,q}=\bigoplus_{r=0}^{q-1}
{\delta\mathrm{Pol}}^{\langle1\rangle}_{m,n,r+1},$$ we get that $$\begin{gathered}
\label{analytictildeconvergence3}
K_{\mathrm{Pol}^{\langle1\rangle}_{m,n,q}}(\xi,\eta)=
\sum_{r=0}^{q-1}K_{{\delta\mathrm{Pol}}^{\langle1\rangle}_{m,n,r+1}}(\xi,\eta)
\\
=\sum_{r=0}^{q-1}[{\mathbf T}_r]_\xi[\bar{\mathbf T}_r]_\eta
\big(K_{{\mathbf B}_0[L^2({\mathbb R}_-)]}(\xi,\eta)\big)+\mathrm{O}(m^{-\frac12+\varepsilon}), 
\end{gathered}$$ again with uniform control on compact subsets. Next, it should be rather clear that $$[{\mathbf T}_r]_\xi[\bar{\mathbf T}_r]_\eta\big(K_{{\mathbf B}_0[L^2({\mathbb R}_-)]}(\xi,\eta)\big)$$ is the reproducing kernel for the space ${\mathbf T}_r{\mathbf B}_0[L^2({\mathbb R}_-)]={\mathbf B}_r
[L^2({\mathbb R}_-)]$, which was identified in terms of Hermite polynomials back in Proposition [\[polybargmannkernel\]](#polybargmannkernel){reference-type="ref" reference="polybargmannkernel"}. We write this down as a proposition.

::: prop
[]{#prop-5.9 label="prop-5.9"} Fix a positive real number $\varepsilon$. Then the reproducing kernel for $\mathrm{Pol}^{\langle1\rangle}_{m,n,q}$ has the following form: $$K_{\mathrm{Pol}^{\langle1\rangle}_{m,n,q}}(\xi,\eta)=
\sum_{r=0}^{q-1}\frac{\mathrm e^{\xi\bar\eta}}{r! \sqrt{2 \pi}}
\int_{-\infty}^{-\xi-\bar\eta} H_r(t+\xi-\eta)
H_r(t+\bar\eta-\bar\xi)\mathrm e^{-\frac12t^2} {\mathrm d}t+
\mathrm{O}(m^{-\frac12+\varepsilon}),$$ as $m,n\to+\infty$ while $n=m+\mathrm{O}(1)$, where the control is uniform on compact subsets.
:::

If we like, we may use the classical Christoffel-Darboux identity $$\label{eq-CD}
\sum_{r=0}^{q-1}\frac{1}{r!}H_r(x)H_r(y)=
\frac{H_q(x)H_{q-1}(y)-H_{q-1}(x)H_{q}(y)}{(q-1)!(x-y)}$$ to rewrite the above sum. Also, we should note that reproducing kernel for the blow-up space $\mathrm{Pol}^{\langle1\rangle}_{m,n,q}$ is connected with the reproducing kernel $K_{m,n,q}$ for $\mathrm{Pol}_{m,n,q}$ via the identity $$\label{eq-connect}
K_{\mathrm{Pol}^{\langle1\rangle}_{m,n,q}}(\xi,\eta)=
m^{-1}\mathrm e^{-m-m^{1/2}(\xi+\bar\eta)}K_{m,n,q}(1+m^{-1/2}\xi,1+m^{-1/2}\eta).$$

The $1$-point intensity function is $$K_{m,n,q}(z,z)\mathrm e^{-m|z|^2},$$ and the localized version with $z=1+m^{-1/2}\xi$ is $$U_{m,n,q}(\xi):=
m^{-1}K_{m,n,q}(1+m^{-1/2}\xi,1+m^{-1/2}\xi)\,\mathrm e^{-m|1+m^{-1/2}\xi|^2},$$ where we throw in a factor of $m^{-1}$ to compensate for the Jacobian. In view of [\[eq-connect\]](#eq-connect){reference-type="eqref" reference="eq-connect"} together with Proposition [\[prop-5.9\]](#prop-5.9){reference-type="ref" reference="prop-5.9"}, we obtain $$U_{m,n,q}(\xi)=\sum_{r=0}^{q-1}\frac{1}{r!\sqrt{2\pi}}\int_{-\infty}^{-2\operatorname{Re}\xi}
H_r(t)^2\mathrm e^{-\frac12t^2}{\mathrm d}t+\mathrm{O}(m^{-\frac12+\varepsilon}).$$ So, essentially, the $1$-point intensity function is determined by the density $$t\mapsto\sum_{r=0}^{q-1}\frac{1}{r!\sqrt{2\pi}}
H_r(t)^2\mathrm e^{-\frac12t^2},$$ which corresponds to filling the lowest energy eigenstates of the harmonic oscillator. By the Wigner semi-circle law, then, we get the approximation $$U_{m,n,q}(\xi)\approx
\frac{2q}{\pi}\int_{-1}^{-q^{-1/2}\operatorname{Re}\xi}\sqrt{1-\tau^2}{\mathrm d}\tau,$$ valid for big $m,n$ with $n=m+\mathrm{O}(1)$, and big $q$ (but much smaller than $m,n$). So, if we rescale to characteristic distance $q^{1/2}m^{-1/2}$ we find an interesting law in the limit.

The blow-up Berezin density at $1$ is given by $$\hat\berd^{\langle1\rangle}_{m,n,q}(\xi)=m^{-1}
\berd^{\langle1\rangle}_{m,n,q}(1+m^{-1/2}\xi)=m^{-1}
\mathrm e^{-m|1+m^{-1/2}\xi|^2}
\frac{|K_{m,n,q}(1+m^{-1/2}\xi,1)|^2}{K_{m,n,q}(1,1)}.$$ From [\[eq-connect\]](#eq-connect){reference-type="eqref" reference="eq-connect"}, we have that $$K_{\mathrm{Pol}^{\langle1\rangle}_{m,n,q}}(0,0)=
m^{-1}\mathrm e^{-m}K_{m,n,q}(1,1),$$ while Proposition [\[prop-5.9\]](#prop-5.9){reference-type="ref" reference="prop-5.9"} gives $$K_{\mathrm{Pol}^{\langle1\rangle}_{m,n,q}}(0,0)=
\sum_{r=0}^{q-1}\frac{1}{r! \sqrt{2 \pi}}
\int_{-\infty}^{0} H_r(t)^2\mathrm e^{-\frac12t^2} {\mathrm d}t+
\mathrm{O}(m^{-\frac12+\varepsilon}),$$ as $m,n\to+\infty$ with $n=m+\mathrm{O}(1)$. Now, as each Hermite polynomial $H_r$ is either even or odd, $$\int_{-\infty}^{0} H_r(t)^2\mathrm e^{-\frac12t^2} {\mathrm d}t=\frac{1}{2}
\int_{-\infty}^{+\infty} H_r(t)^2\mathrm e^{-\frac12t^2} {\mathrm d}t=
\frac{r!\sqrt{2\pi}}{2},$$ which leads to $$K_{\mathrm{Pol}^{\langle1\rangle}_{m,n,q}}(0,0)=
\frac{q}{2}+\mathrm{O}(m^{-\frac12+\varepsilon})$$ and $$K_{m,n,q}(1,1)=\tfrac12\,mq\mathrm e^m[1+\mathrm{O}(m^{-\frac12+\varepsilon})].$$ A similar calculation gives that $$\begin{gathered}
K_{m,n,q}(1+m^{-1/2}\xi,1)=m\mathrm e^{m+m^{1/2}\xi}
K_{\mathrm{Pol}^{\langle1\rangle}_{m,n,q}}(\xi,0)
\\
=m\mathrm e^{m+m^{1/2}\xi}\bigg\{
\sum_{r=0}^{q-1}\frac{1}{r! \sqrt{2 \pi}}
\int_{-\infty}^{-\xi} H_r(t+\xi)
H_r(t-\bar\xi)\mathrm e^{-\frac12t^2} {\mathrm d}t+
\mathrm{O}(m^{-\frac12+\varepsilon})\bigg\}.
\end{gathered}$$

Putting things together, we obtain the following asymptotics for the blow-up Berezin density.

::: thm
[]{#thm-5.10 label="thm-5.10"} Fix a positive real number $\varepsilon$. Then the blow-up Berezin density at $1$ has the following form: $$\hat\berd^{\langle1\rangle}_{m,n,q}(\xi)=
\frac{1}{\pi q}\bigg|\sum_{r=0}^{q-1}\frac{1}{r!}
\int_{-\infty}^{-\xi} H_r(t+\xi)
H_r(t-\bar\xi)\mathrm e^{-\frac12t^2} {\mathrm d}t\bigg|^2+
\mathrm{O}(m^{-\frac12+\varepsilon}),$$ as $m,n\to+\infty$ while $n=m+\mathrm{O}(1)$, where the control is uniform on compact subsets.
:::

::: rem
When we make some explicit calculations based on Theorem [\[thm-5.10\]](#thm-5.10){reference-type="ref" reference="thm-5.10"}, we see that the Fresnel zone pattern is less pronounced for a boundary point $z$.
:::

**Acknowledgements. We would like to thank Philip Kennerberg for sharing sharing his MATLAB-code and discussing the practicalities in simulating the process.**

---
doc_id: arxiv-math-0108215v1
doc_title: "arXiv:math/0108215v1 [math.GT] 30 Aug 2001"
section_id: sec-002-3-thick-knots-have-bounded-energy
section_title: "Thick knots have bounded energy"
section_number: 3
pages: 8-16
source_pdf: 0108215v1.pdf
source_sha256: 191784d2ccb3415a
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.949
latex_coverage_ratio: 0.628
doc_brief: "arXiv:math/0108215v1 [math.GT] 30 Aug 2001 — The M¨obius energy of a knot is an energy functional for smooth curves based on an idea of self-repelling."
---
In this section, we prove that the Möbius energy of a knot is bounded by the ropelength. Our goal is partly the theorem itself and partly the paradigm: any "energy" defined in terms of inverse-square distances should have an analogous bound, with the proof following this model.

::: thm
If $K$ is a smooth knot in $\Rset^3$ then $$E_{O4}(K) < 4.57\, E_L(K)^{4/3}.
\label{powbound}$$ []{#main label="main"}
:::

::: thm
If $K$ is a smooth knot in $\Rset^3$ then $$E_{O4}(K) \leq \frac{1}{4}E_L(K)^2 \;.
\label{quadbound}$$ []{#quadboundthm label="quadboundthm"}
:::

**Remark**  For short knots, the quadratic bound is better than the $4/3$ power bound. Comparing [\[powbound\]](#powbound){reference-type="eqref" reference="powbound"} to [\[quadbound\]](#quadbound){reference-type="eqref" reference="quadbound"}, we see that one needs ropelengths over $79$ before the advantage of the lower exponent is evident. If one uses the actual bound [\[finalbound\]](#finalbound){reference-type="eqref" reference="finalbound"} we obtain in the proof, which is a complicated expression dominated by a $4/3$ power term, then that bound is lower than [\[quadbound\]](#quadbound){reference-type="eqref" reference="quadbound"} for ropelengths $> 41$. Computer simulations suggest [@stasiakideal; @spatial] the only knots that can be realized with a ropelength $\leq 41$ are the unknot and the trefoil.

::: pf
We will obtain the quadratic bound en route to the $4/3$ power bound.

We follow an overall plan similar to [@BS2; @BS3], but introduce a limit process in the main argument. Since $E_{O4}$ and $E_L$ are both invariant under change of scale, we begin by rescaling $K$ to have thickness $R(K)=1$, so that $E_L(K)$ is just the total arclength of $K$, which we abbreviate $L$.

The energy $E_{O4}(K)$ is defined as a double-integral over $K
\times K$. We bound separately the integral over the portion of $K  \times K$ consisting of pairs $(x,y)$ with $\mathrm{arc}(x,y)
\leq \pi R(K) = \pi$, and the integral over the rest of $K
\times K$.

Let $$E_{\mathrm{prox}} = \int\nolimits_{x \in
K}\int\nolimits_{\mathrm{arc}(x,y) \leq \pi}
\frac{1}{|x-y|^2} - \frac{1}{\mathrm{arc}(x,y)^2}  
\;\;,$$ $$E_{\mathrm{dist}} = \int\nolimits_{x \in
K}\int\nolimits_{\mathrm{arc}(x,y) \geq \pi}
\frac{1}{|x-y|^2} \;\;,$$ and $$E_{\mathrm{reg}} = \int\nolimits_{x \in
K}\int\nolimits_{\mathrm{arc}(x,y) \geq \pi}
\frac{1}{\mathrm{arc}(x,y)^2}  
\;\;.$$

So we have $$E_{O4}=E_{\mathrm{prox}}+E_{\mathrm{dist}}-E_{\mathrm{reg}}\;.$$

By Lemma [\[prox\]](#prox){reference-type="ref" reference="prox"}, $$E_{\mathrm{prox}} \leq \frac{2}{\pi}\,L\;.
\label{eprox}$$ Also, by symmetry of the circle, $$E_{\mathrm{reg}}=
\int_{x \in K} \left(
2\int_{\pi}^{\frac{L}{2}}\frac{1}{t^2}\,\d t \right) \;\d
x\; = 
\;L\;\left( 2\int_{\pi}^{\frac{L}{2}}\frac{1}{t^2}\,\d t
\right) =
\frac{2}{\pi}\,L-4\;,
\label{ereg}$$ so $$\label{esummary}
E_{04} \leq E_{\mathrm{dist}}+4\;.$$

We now bound $E_{\mathrm{dist}}$. We shall bound the inner integral and then multiply by the length of $K$ to bound the energy. The inner integral, for each $x$, is $$I^x_{\mathrm{dist}}=\int\nolimits_{\mathrm{arc}(x,y)
\geq \pi}
\frac{1}{|x-y|^2}\;\;.$$

Here first is the quadratic bound.

By Lemma [\[distancebound\]](#distancebound){reference-type="ref" reference="distancebound"}, and our rescaling to $R(K)=1$, we have for each point $y \in K$, $$\mathrm{arc}(x,y) \geq \pi \Rightarrow |x-y|
\geq 2\;.$$ Thus, $$I_{\mathrm{dist}}^x\leq
\frac{1}{2^2}(L-2\pi)\;.$$ Multiplying by $L$, we get $$E_{\mathrm{dist}} \leq
\frac{1}{4}\,L^2-\frac{\pi}{2}\,L\;.
\label{edistquad}$$ Combine ([\[edistquad\]](#edistquad){reference-type="ref" reference="edistquad"}) with ([\[esummary\]](#esummary){reference-type="ref" reference="esummary"}) to complete a quadratic polynomial bound: $$\label{quadraticbound}
E_{O4}(K)
\leq \frac{1}{4}  L^2 - \frac{\pi}{2} L + 4\;.$$ Because $K$ is a smooth closed curve with maximum curvature $\leq 1$ (by Lemma [\[lsdr\]](#lsdr){reference-type="ref" reference="lsdr"} and the fact that we have normalized $K$ to have thickness radius = 1), the total curvature of $K$ is at most $L$. But by Fenchel's theorem, the total curvature of a closed curve is at least $2\pi$. Thus $L\geq 2\pi>8/\pi$, so the linear part of ([\[quadraticbound\]](#quadraticbound){reference-type="ref" reference="quadraticbound"}) is negative, and we have $$\label{finalquadraticbound}
E_{O4}(K)
\leq \frac{1}{4}  L^2\;.$$

We now develop the $4/3$ power bound. If $L<\frac{104}{3}+2\pi\approx 41$, i.e. $L-2\pi<\frac{4}{3}\left(3^3-1^3\right)$, then our proof stops here. The quadratic bound [\[quadbound\]](#quadbound){reference-type="eqref" reference="quadbound"} is valid and certainly $\eqref{quadbound} < \eqref{powbound}$, so [\[powbound\]](#powbound){reference-type="eqref" reference="powbound"} is valid as well. We continue under the assumption that $E_L(K)\geq \frac{104}{3}+2\pi$.

The first observation is that for any $\rho >0$, if $|x-y|\geq
\rho$, then the integrand $\frac{1}{|x-y|^2} \leq
\frac{1}{\rho^2}$. In obtaining the quadratic bound, we stopped here, allowing the idea that with respect to each point $x \in K$, the whole knot (except for the arc around $x$ of length $\pi$ in each direction) lies just at distance $2$ from $x$. But *the knot is thick* : a piece $w$ of $K$ of length $\ell(w)$ carries along with it a solid tube $W$ of volume $\pi
\ell(w)$ (we still are assuming $R(K)=1$). Furthermore, such a tube $W$ cannot intersect any other part of $K$ nor any of the rest of the tube around $K$. This restricts how much length of $K$ can be packed within any given distance from $x$.

Fix $x$ on $K$. Let $Y_{\mathrm{dist}}$ denote the set on which we integrate to compute $I_{\mathrm{dist}}^x$, that is $Y_{\mathrm{dist}}=\{y
\in K \,:\,\mathrm{arc}(x,y) \geq \pi\}$. The arclength of $Y_{\mathrm{dist}}$ is just $L-2 \pi$. Let $S(\rho,\sigma]$ denote the half-open spherical shell centered at $x$ with radius from $\rho$ to $\sigma$. Let $Y(\rho, \sigma]$ = $Y_{\mathrm{dist}}
\cap S(\rho, \sigma]$, a measurable set, and let $\ell (\rho,\sigma]$ denote its 1-dimensional measure, i.e. the measure of the length of $K$ lying in $S(\rho,\sigma]$. Let $T(\rho,\sigma]$ be the solid tube with axis $Y(\rho,\sigma]$, that is, the portion of the unit radius tube about $K$ consisting of disks centered at points $y\in Y(\rho,\sigma]$. The 3-dimensional measure, i.e. volume, of $T(\rho,\sigma]$ is $\pi \ell(\rho,\sigma]$. Define $S[\rho,\sigma]$, $Y[\rho,\sigma]$, $\ell[\rho,\sigma]$, and $T[\rho,\sigma]$ analogously. Note that $Y_{\mathrm{dist}} \subset S[2,L/2]$. The subset of $Y_{\mathrm{dist}}$ lying at distance exactly $2$ from $x$ plays a special role in the analysis, so we also define $S[2]$, $Y[2]$, $\ell[2]$, and $T[2]$.

Let $P=(\frac{3}{4}L-\frac{3\pi}{2}+1)^{1/3}-1$. The constant $P$ is the radius required so that a spherical shell from $r=1$ to $r=P+1$ has the same volume as a tube of radius $1$ about a set of length $L-2\pi$.

We bound the total amount of length that can lie in each spherical shell by a function $\ell^*$ (see [\[llessstar\]](#llessstar){reference-type="eqref" reference="llessstar"} below). Let $\ell^*[2]=\frac{4}{3}(3^3-1^3)=\frac{104}{3}$. For $2\leq a<b$, let $$\ell^*(a,b]=\frac{4}{3}\left( (\min\{b,P\}+1)^3 - (\min\{a,P\}+1)^3 
\right).$$ In particular, when $2\leq a<b\leq P$, this simplifies to $$\ell^*(a,b]=\frac{4}{3}\left( (b+1)^3 - (a+1)^3 \right).$$ Let $$\ell^*[2,b] = \ell^*[2] + \ell^*(2,b].$$ For $b\leq P$, $\ell^*[2,b]=\frac{4}{3}\left((b+1)^3-1^3\right)$. For $b>P$, notice that $\ell^*(2,b]=
\ell^*(2,P]$ so $\ell^*[2,b]=\ell^*[2,P]=L-2\pi$.

We now show that $$\label{llessstar}
\ell[2,r]\leq \ell^*[2,r] \text{ for all }2\leq r\;.$$ The tube $T[2,r]$ has volume $\pi\ell[2,r]$. But $T[2,r]$ lies entirely within $S[1,r+1]$, whose volume is $\frac{4}{3}\pi\left( (r+1)^3-1^3\right)$. Thus, when $2\leq r\leq P$, $$\begin{aligned}
\pi\ell[2,r]&\leq \frac{4}{3}\pi\left((r+1)^3-1^3\right)\\
&= \pi\ell^*[2,r].
\end{aligned}$$ If $r>P$, then $\ell^*[2,r]=\ell^*[2,P]=
L-2\pi\geq \ell[2,r]$. Thus, we have [\[llessstar\]](#llessstar){reference-type="eqref" reference="llessstar"}.

We next partition $Y_{\text{dist}}$ into sets $W_j$ whose distance to $x$ is controlled, and express $I^x_{\text{dist}}$ as the sum of the contributions from these sets.

Let $n\in\mathbb{N}$ and $\delta=\frac{P-2}{n}$. Then, $$\begin{aligned}
\ell^*[2,P]&=\ell^*[2] + \ell^*(2,2+\delta] + 
\ell^*(2+\delta,2+2\delta] + \cdots + 
\ell^*(P-\delta,P]\\
&=L-2\pi.
\end{aligned}$$

We define a sequence of sets $\{W_j\}$ using Lemma [\[ConstructWj\]](#ConstructWj){reference-type="ref" reference="ConstructWj"} as follows. Let $\nu_0=\ell^*[2]$ and $\nu_j=\ell^*(2+(j-1)\delta,2+j\delta]$ for $1\leq j\leq n$. Note that $\nu_n=\ell^*(2+(n-1)\delta,2+n\delta]=\ell^*(P-\delta,P]$. Since $\nu_0+\nu_1+\cdots+\nu_n=L-2\pi=\mu(Y_{\mathrm{dist}})$, by Lemma [\[ConstructWj\]](#ConstructWj){reference-type="ref" reference="ConstructWj"}, there exists a sequence $2\leq\rho_0\leq\rho_1\leq\cdots\leq\rho_n$ and a partition of $Y_\mathrm{dist}$ into measurable sets $W_0,\cdots,W_n$ such that: for $1\leq j\leq n$, we have $\mu(W_j)=\nu_j$ and $W_j\subseteq Y_\mathrm{dist}\cap S[\rho_{j-1},\rho_j]$; for $j=0$, we have $\mu(W_0)=\nu_0$ and $W_0\subseteq Y_\mathrm{dist}\cap S[2,\rho_0]$.

We want to know how far each $W_j$ is from $x$, so we next bound the radii $\rho_j$ (from below) in terms of $j$ and $\delta$. If $y\in W_0$, then $|x-y|\geq 2$ by Lemma [\[distancebound\]](#distancebound){reference-type="ref" reference="distancebound"}. For $1\leq j\leq n$, we claim $|x-y|>2+(j-1)\delta$ for all $y\in W_j$, except perhaps a set of measure $0$. Suppose $M$ is a non-zero measure subset of $W_1$ such that for all $y\in M$, we have $|x-y|\leq 2$. Then $W_0\cup M\subseteq Y[2]$ and $\ell[2]\geq \mu(W_0)+\mu(M)> \mu(W_0)=\ell^*[2]$, which contradicts [\[llessstar\]](#llessstar){reference-type="eqref" reference="llessstar"}. We continue using induction. Suppose for all $0\leq k< j\leq n$, we have $|x-y|> 2+(k-1)\delta$. Suppose $M$ is a non-zero measure subset of $W_j$ such that for all $y\in M$, we have $|x-y|\leq 2+(j-1)\delta$. Then $W_0\cup W_1\cup \cdots \cup W_{j-1} \cup M\subseteq Y[2,2+(j-1)\delta]$. Thus, $$\begin{aligned}
\pi \ell[2,2+(j-1)\delta] &\geq 
\mu(W_0)+\mu(W_1)+\cdots +\mu(W_{j-1})+\mu(M)\\
&> \mu(W_0)+\mu(W_1)+\cdots +\mu(W_{j-1})\\
&= \pi\left(\,
\ell^*[2]+\ell^*(2,2+\delta]+\cdots+\ell^*(2+(j-2)\delta,2+(j-1)\delta]
\,\right)\\
&= \pi\ell^*[2,2+(j-1)\delta],
\end{aligned}$$ which contradicts [\[llessstar\]](#llessstar){reference-type="eqref" reference="llessstar"}.

Since $Y_{\mathrm{dist}}=W_0\cup W_1\cup \cdots \cup W_n$, $$\begin{aligned}
I^x_{\mathrm{dist}} &= \int_{y\in W_0}\frac{1}{|x-y|^2} + 
\int_{y\in W_1}\frac{1}{|x-y|^2} + \cdots +
\int_{y\in W_n}\frac{1}{|x-y|^2}\nonumber \\
&< \frac{1}{2^2}\ell^*[2] + \frac{1}{2^2}\ell^*(2,2+\delta]+\cdots
+\frac{1}{(P-\delta)^2}\ell^*(P-\delta,P]\label{ixdistbound}.
\end{aligned}$$ The first term of [\[ixdistbound\]](#ixdistbound){reference-type="eqref" reference="ixdistbound"} is $\frac{104}{12}$. The rest is $$\begin{aligned}
& \sum_{j=1}^n \frac{1}{(2+(j-1)\delta)^2}\ell^*(2+(j-1)\delta,2+j\delta)
\text{\;, which equals}\\
& \sum_{j=1}^n \frac{1}{r_j^2}\left(4(r_j+1)^2\Delta r +
4(r_j+1)\Delta r^2 + \frac{4}{3}\Delta r^3\right),
\end{aligned}$$ where $r_j=2+(j-1)\delta$ and $\Delta r=\delta$. This is a Riemann sum for $\int_2^P\frac{4(r+1)^2}{r^2}\d r$ plus terms of higher order in $\Delta r$ whose contribution approaches $0$ as $\Delta r\to 0$. The bound [\[ixdistbound\]](#ixdistbound){reference-type="eqref" reference="ixdistbound"} holds for all choices of $n$, so as $n\to \infty$, we get $$\begin{aligned}
I^x_{\mathrm{dist}} 
&\leq \frac{104}{12}+\int_2^P \frac{4(r+1)^2}{r^2}\d r\\
&= \frac{8}{3}+4P-\frac{4}{P}+8\ln(P)-8\ln(2)\;.
\end{aligned}$$ We then multiply by $L$ to get $$\label{edistbound}
E_{\mathrm{dist}}\leq L
\left(\frac{8}{3}+4P-\frac{4}{P}+8\ln(P)-8\ln(2)\right).$$ Combining [\[esummary\]](#esummary){reference-type="eqref" reference="esummary"} with [\[edistbound\]](#edistbound){reference-type="eqref" reference="edistbound"} yields $$\label{finalbound}
E_{O4}(K)\leq L
\left(\frac{8}{3}+4P-\frac{4}{P}+8\ln(P)-8\ln(2)\right)+4\;.$$ We substitute $P=\left(\frac{3}{4}L-\frac{3\pi}{2}+1\right)^{1/3}-1$ to obtain our final bound.

This bound is messy, but on the order of $L^{4/3}$. We use a computer algebra system to plot the bound divided by $L^{4/3}$. The ratio achieves its maximum of $\approx 4.5626$ near $L=1115$. Thus, for all $L$ we have $$E_{O4}(K)\leq 4.57L^{4/3}.$$ 0◻
:::

For some values of $L$, in particular as $L$ gets very large, the coefficient $4.57$ can be further reduced. If $\frac{104}{3}+2\pi< L < 128$ or $L> 376,\!000$, we have $E_{O4}(K)\leq 4L^{4/3}$. As $L$ tends to infinity, the constant decreases to $3^{\frac{1}{3}}4^{\frac{2}{3}}\approx 3.63$.

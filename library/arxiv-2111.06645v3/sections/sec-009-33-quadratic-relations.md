---
doc_id: arxiv-2111.06645v3
doc_title: "Knots, Perturbative Series and Quantum Modularity"
section_id: sec-009-33-quadratic-relations
section_title: "Quadratic relations"
section_number: 3.3
pages: 18-20
source_pdf: 2111.06645v3.pdf
source_sha256: 2a4826bd1c2f0823
toc_source: outline
text_source: latex
latex_prose_ratio: 0.963
latex_coverage_ratio: 0.991
doc_brief: "Knots, Perturbative Series and Quantum Modularity — We introduce an invariant of a hyperbolic knot which is a map α 7→Φα(h) from Q/Z to matrices with entries in Q[[h]] and with rows and columns"
---
[]{#sub.quad label="sub.quad"}

The next interconnection among the power series associated to a given knot $K$ that we discover (experimentally, as always) from the examples is that they satisfy an unexpected quadratic relation, namely $$\label{quadrel}
\sum_{\sigma\in \mathcal{P}^{\text{red}}_K} \Phi^{(K,\sigma)}_\alpha(h) \Phi^{(K,\sigma)}_{-\alpha}(-h) = 0 .$$ Notice that this relation is non-trivial even at the level of its constant term, where it says, for example, that the value of the generalized Kashaev invariant $J^{(5_2,\sigma)}(\alpha)$ defined in the last subsection belongs to the kernel of the trace map from $\mathbb Q(\xi,\zeta_\alpha)$ to the trace field $\mathbb Q(\xi)$ of $5_2$ for every rational number $\alpha$. The special case of this when $\alpha=0$ was observed independently by Gang, Kim and Yoon [@torsion].

The relation [\[quadrel\]](#quadrel){reference-type="eqref" reference="quadrel"} is practically vacuous for the figure 8 knot, since in that case it follows immediately from the identity mentioned at the beginning of Section [\[sub.Formal\]](#sub.Formal){reference-type="ref" reference="sub.Formal"}. (Stated differently, if we multiply the series [\[as41\]](#as41){reference-type="eqref" reference="as41"} by its value at $-h$, we obtain an element of $\sqrt{-3}\mathbb Q\big[\big[h^2\big]\big]$, so that the trace down to $\mathbb Q$ vanishes, and similarly for [\[as41at5\]](#as41at5){reference-type="eqref" reference="as41at5"}.) But for the $5_2$ knot the identity is non-trivial even at $\alpha=0$, where [\[as52\]](#as52){reference-type="eqref" reference="as52"} gives $$\begin{aligned}
\Phi^{5_2}(h) \Phi^{5_2}(-h)
 ={}& \frac1{3\xi-2} + \frac{102\xi^2 - 183\xi + 135}{(3\xi-2)^7} h^2
\\
& - \frac{143543 \xi^2 - 252029 \xi + 190269}{4 (3\xi-2)^{13}} h^4+ \cdots
\end{aligned}$$ in which one can check that the three coefficients given, and in fact all coefficients up to order $h^{108}$, lie in the kernel of the trace map from $\mathbb Q(\xi)$ to $\mathbb Q$. Notice, by the way, that the series here has much simpler coefficients (specifically, much smaller denominators) than the individual factors as given by [\[as52\]](#as52){reference-type="eqref" reference="as52"}. This is a special case of a more general phenomenon that will be discussed in [@GSZ:habiro]. When we look at [\[quadrel\]](#quadrel){reference-type="eqref" reference="quadrel"} for this knot but other values of $\alpha$, the same thing happens: the $m$-th root of a unit in $\mathbb Q(\xi,\zeta_m)$ that is a common factor of each when $\alpha$ has denominator $m$ cancels when we multiply the series at $\alpha$ and $-\alpha$, and the series in $\mathbb Q(\xi,\zeta_m)[[h]]$ that we find, although it is no longer even when $\alpha$ is different from 0 or $1/2$, always has coefficients lying in the kernel of the trace map from $\mathbb Q(\xi,\zeta_m)$ to $\mathbb Q(\zeta_m)$.

The above illustrates the relation [\[quadrel\]](#quadrel){reference-type="eqref" reference="quadrel"} for our second simplest knot $5_2$. For our third standard example $K=(-2,3,7)$, this relation is even more surprising because now $\mathcal P_K$ has two Galois orbits, as discussed in Section [\[sec.Phi\]](#sec.Phi){reference-type="ref" reference="sec.Phi"}, and the quadratic relation relates them to one another. Specifically, if we consider separately the contributions from $\sigma_i$ for $1\le i\le 3$ and for $4\le i\le6$, then equation [\[Phi237.123\]](#Phi237.123){reference-type="eqref" reference="Phi237.123"} gives $$\begin{gathered}
 \sum_{j=1}^3 \Phi^{(K,\sigma_j)}(h) \Phi^{(K,\sigma_j)}(-h)\\
\qquad= \operatorname{Tr}_{\mathbb Q(\xi)/\mathbb Q}\left(\frac{\xi^2}{2 (3\xi-2)}
+ \frac{605\xi^2 - 1217 \xi +878}{2^4 (3\xi-2)^7} h^2 + \cdots\right) \\
 \qquad =\frac12+ 0 h^2  - \frac{13}{2^6} h^4
+ \frac{2987}{2^{11}\cdot3} h^6 + \frac{3517753}{2^{16}\cdot5} h^8  - 
 \frac{110362454561}{2^{19}\cdot3^3\cdot5\cdot7} h^{10} - \cdots
\end{gathered}$$ and equation [\[Phi237.456\]](#Phi237.456){reference-type="eqref" reference="Phi237.456"} gives $$\begin{aligned}
&\sum_{j=4}^6 \Phi^{(K,\sigma_j)}(h) \Phi^{(K,\sigma_j)}(-h)\\
&\qquad= \operatorname{Tr}_{\mathbb Q(\eta)/\mathbb Q}\left(\frac{\eta-2}{2\cdot7}
+ \frac{18811 \eta^2 -78046 \eta+ 67485}{2^8 \cdot 3 \cdot 7^4} h^2+ \cdots\right)\\
& \qquad =- \frac12 + 0 h^2 +\frac{13}{2^6} h^4
  - \frac{2987}{2^{11}\cdot3} h^6  - \frac{3517753}{2^{16}\cdot5} h^8 +
 \frac{110362454561}{2^{19}\cdot3^3\cdot5\cdot7} h^{10} + \cdots .
\end{aligned}$$ Each of these two series belongs to $\mathbb Q\big[\big[h^2\big]\big]$. Computing many more terms (we went up to $O\big(h^{38}\big)$), we find that their sum vanishes, confirming the quadratic relation in a very striking way and at the same time showing a subtle interdependence between the two cubic number fields associated to this knot. We note, however, that these are only two of the three number fields making up the algebra $\mathcal A_{(-2,3,7)} = \mathbb Q\times\mathbb Q(\xi)\times\mathbb Q(\eta)$ as defined in [\[AK\]](#AK){reference-type="eqref" reference="AK"}. We have not found *any* relation between the power series and the power series  for $\sigma\ne\sigma_0$. This is reflected in the fact that the summation in [\[quadrel\]](#quadrel){reference-type="eqref" reference="quadrel"} is over $\mathcal{P}^{\text{red}}_K$ and not over all of $\mathcal P_K$.

We end this subsection by mentioning that, as well as the quadratic relation [\[quadrel\]](#quadrel){reference-type="eqref" reference="quadrel"}, there are also *bilinear* expressions in the $\Phi^{(K,\sigma)}$ that are not zero, but (experimentally, and in some cases provably) are *convergent* rather than factorially divergent power series. This will be discussed briefly in Section [\[sub.holomorphic\]](#sub.holomorphic){reference-type="ref" reference="sub.holomorphic"} and in detail in the companion paper [@GZ:qseries]. Here we give only a numerical example. In Proposition [\[prop.W1\]](#prop.W1){reference-type="ref" reference="prop.W1"} below, we will give certain explicit bilinear combinations of the $\Phi$-series which we believe are the Taylor expansions of analytic functions and hence have a positive (and known) radius of convergence. In the simplest case (corresponding in the notation of Proposition [\[prop.W1\]](#prop.W1){reference-type="ref" reference="prop.W1"} to the $(\sigma_1,\sigma_1)$ component of the matrix , where $S=\bigl(\smallmatrix 0&-1\\1&0\endsmallmatrix\bigr)$ as usual, combined with [\[Orthogonality2\]](#Orthogonality2){reference-type="eqref" reference="Orthogonality2"}), this power series is given by $$\label{DefR}
{\rm e}^{-v(4_1)} \Phi(2 \pi {\rm i} x)\Phi\biggl(-\frac{2 \pi {\rm i} x}{1+x}\biggr)
 - {\rm e}^{v(4_1)} \Phi\biggl(\frac{2 \pi {\rm i} x}{1+x}\biggr)\Phi(-2 \pi {\rm i} x) ,$$ with $\Phi=\Phi^{(4_1)}_0$ as given in [\[as41\]](#as41){reference-type="eqref" reference="as41"}. The power series $\Phi$ has coefficients growing like $n!$ times an exponential function (the precise asymptotics will be described in the next subsection) and has 100th coefficient of the order of $10^{94}$, but the combination [\[DefR\]](#DefR){reference-type="eqref" reference="DefR"} has radius of convergence 1 and, for instance, 100th coefficient of order $10^{-3}$. Notice that if we replace all $\Phi$'s in [\[DefR\]](#DefR){reference-type="eqref" reference="DefR"} by the corresponding $\widehat\Phi$'s, then the prefactors ${\rm e}^{\pm v(4_1)}$ disappear.

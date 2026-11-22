---
doc_id: arxiv-0903.2472v1
doc_title: "Exact Results for Perturbative Chern-Simons Theory with Complex Gauge Group"
section_id: sec-013-421-quantization
section_title: "Quantization"
section_number: 4.2.1
pages: 51-52
source_pdf: 0903.2472v1.pdf
source_sha256: 637cfd1d4d833c02
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.915
latex_coverage_ratio: 0.993
doc_brief: "Exact Results for Perturbative Chern-Simons Theory with Complex Gauge Group — We develop several methods that allow us to compute all-loop partition functions in perturbative Chern-Simons theory with"
---
[]{#sec:figeightquant label="sec:figeightquant"}

In order to test the proposed state integral model [\[statesumdef\]](#statesumdef){reference-type="eqref" reference="statesumdef"}, we first compute the perturbative $SL(2,{\mathbb{C}})$ invariants of $M$ via quantization of ${{\cal M}}_{{\rm flat}}(G_{{\mathbb{C}}},\Sigma)$, as outlinted in Section [\[sec:quantization\]](#sec:quantization){reference-type="ref" reference="sec:quantization"}. Recall the expression [\[zpert\]](#zpert){reference-type="eqref" reference="zpert"} for the perturbative Chern-Simons partition function, $$Z^{(\alpha)} (M;\hbar,u) =
\exp\left( \frac{1}{\hbar} S_0^{(\alpha)} (u) - \frac{1}{2}\delta^{(\alpha)} \log \hbar
+ \sum_{n=0}^\infty S_{n+1}^{(\alpha)} (u) \hbar^n \right),$$ where for the figure-eight knot complement $\alpha \in \{{\rm geom},\,{\rm conj},\,{\rm abel}\}$, and, as explained *e.g.* in [@gukov-2003; @gukov-2006], $\delta^{(\alpha \neq {\rm abel})} = 0$.

In Section [\[sec:quantization\]](#sec:quantization){reference-type="ref" reference="sec:quantization"} we saw how quantization of the relation $A(l,m) = 0$ leads to the equation $$\widehat{A} (\hat l, \hat m ) ~Z^{(\alpha)} (M;\hbar,u) = 0\,,
\label{AZquantum}$$ which then determines the perturbative $G_{{\mathbb{C}}}$ invariant $Z^{(\alpha)} (M;\hbar,u)$. As explained earlier, *cf.* eqs. [\[aionp\]](#aionp){reference-type="eqref" reference="aionp"} and [\[almionp\]](#almionp){reference-type="eqref" reference="almionp"}, a simple way to find the operator $\widehat{A} (\hat l, \hat m )$ is to note that it also annihilates the polynomial invariants (of the knot $K$) computed by Chern-Simons theory with compact gauge group $G$. In the present case, $G = SU(2)$ and the equation [\[almionp\]](#almionp){reference-type="eqref" reference="almionp"} takes the form of a recursion relation on the set of colored Jones polynomials, $\{ J_n (K;q) \}$. Specifically, using the fact that $\hat l$ acts by shifting the value of the highest weight of the representation and writing $\widehat{A} (\hat{l},\hat{m}) = \sum_{j=0}^d a_j(\hat{m},q) \hat{l}^j$ as in [\[hatAcoeffs\]](#hatAcoeffs){reference-type="eqref" reference="hatAcoeffs"}, we obtain $$\sum_{j=0}^d a_j (q^{n/2}, q) J_{n+j} (K;q) = 0\,.$$ It is easy to verify that the colored Jones polynomials of the figure-eight knot indeed satisfy such a recursion relation, with the coefficients (see also[^1] [@garoufalidis-2004; @garoufalidis-2006]): $$\label{Aj}
\begin{align}
a_0(\hat{m},q) & = \frac{q\hat{m}^2}{(1+q\hat{m}^2)(-1+q\hat{m}^4)}\,, \\
a_1(\hat{m},q) & = \frac{1+(q^2-2q)\hat{m}^2-(q^3-q^2+q)\hat{m}^4-(2q^3-q^2)\hat{m}^6
+q^4\hat{m}^8}{q^{1/2}\hat{m}^2(1+q^2\hat{m}^2-q\hat{m}^4-q^3\hat{m}^6)}\,, \\
a_2(\hat{m},q) & = -\frac{1-(2q^2-q)\hat{m}^2-(q^5-q^4+q^3)\hat{m}^4+(q^7-2q^6)\hat{m}^6
+q^8\hat{m}^8}{q\hat{m}^2(1+q\hat{m}^2-q^5\hat{m}^4-q^6\hat{m}^6)}\,, \\
a_3(\hat{m},q) & = -\frac{q^4\hat{m}^2}{q^{1/2}(1+q^2\hat{m}^2)(-1+q^5\hat{m}^4)}\,.
\end{align}$$ Note that in the classical limit $q = e^{2\hbar} \to 1$, we have $$\widehat{A} (\hat{l},\hat{m}) ~~\underset{\hbar \to 0}{\longrightarrow}~~ \frac{A(l,m)}{m^2(m^2-1)(m^2+1)^2}\,.
\label{limit_hatA}$$ We could multiply all the $a_j$'s by the denominator of [\[limit_hatA\]](#limit_hatA){reference-type="eqref" reference="limit_hatA"} (or a $q$-deformation thereof) to obtain a more direct correspondence between $\widehat{A} (\hat{l},\hat{m})$ and $A(l,m)$, but this does not affect any of the following calculations.

To find the exact perturbative invariant $Z^{(\alpha)} (M;\hbar,u)$ for each $\alpha$, we reduce $\hat{m}$ to a classical variable $m$ (since in the $u$-space representation the operator $\hat{m}$ just acts via ordinary multiplication), expand each of the above $a_j$'s as $a_j(m,q) = \sum_{p=0}^\infty a_{j,p}(m)\hbar^p$, and substitute the $a_{j,p}$ into the hierarchy of differential equations derived in Section [\[sec:quantization\]](#sec:quantization){reference-type="ref" reference="sec:quantization"} and displayed in Table [\[tab:Seqns\]](#tab:Seqns){reference-type="ref" reference="tab:Seqns"}. The equations are then solved recursively on each branch $\alpha$ of the A-polynomial to determine the coefficients $S_n^{(\alpha)}(u)$.

[^1]: Note that [@garoufalidis-2004; @garoufalidis-2006] look at asymptotics of the colored Jones polynomial normalized by its value at the unknot, while the $SL(2,{\mathbb{C}})$ Chern-Simons partition function should agree with the unnormalized colored Jones polynomial. Hence, we must divide the expressions for $a_j$ there by $(m^2 q^{j/2} - q^{-j/2})$ to account for the difference, introducing a few factors of $q^{1/2}$ in our formulas.

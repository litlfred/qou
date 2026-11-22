---
doc_id: arxiv-2103.07383v1
doc_title: "On the Analyticity of Critical Points of the Generalized Integral Menger Curvature in the Hilbert Case"
section_id: sec-001-2-decomposition-of-the-first-variation
section_title: "Decomposition of the first variation"
section_number: 2
pages: 5-7
source_pdf: 2103.07383v1.pdf
source_sha256: 9dca35ea16490ad8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.974
latex_coverage_ratio: 0.992
doc_brief: "On the Analyticity of Critical Points of the Generalized Integral Menger Curvature in the Hilbert Case — We prove the analyticity of smooth critical points for generalized integral Menger cur- vature"
---
\label{sec:Decomposition}

Hermes was the first to derive Gateaux differentiability and a formula for the first variation of the integral Menger curvature $\mathcal{M}_p =  2^p \textnormal{intM}^{(p,p)} $ for $p\geq 2$ in his PhD thesis \cite[Theorem\,2.33, Remark\,2.35]{Hermes:2012:Menger}. In \cite[Theorem\,3]{BlattReiter:2015:Menger}, Blatt and Reiter extended this result to the generalized integral Menger curvature $\textnormal{intM}^{(p,q)}$ for the sub-critical range $p\in (\tfrac 23 q+1, q+\tfrac 23)$ and $q>1$. However, they approached the problem differently to Hermes by taking advantage of studying a certain subdomain of integration as well as using the newly discovered characterization of energy spaces developed in \cite[Theorem\,1.1]{Blatt:2013:NoteMenger} and \cite[Theorem\,1]{BlattReiter:2015:Menger}. The latter states that injective curves in $C^1(\R/\Z,\R^n)$ parametrized by arc-length have finite generalized integral Menger curvature iff they belong to the fractional Sobolev space $W^{(3p-2)/q-1,q} (\R/\Z, \R^n)$ \cite[Theorem 1]{BlattReiter:2015:Menger}. 

To summarize Blatt and Reiter's findings regarding the first variation of  the generalized integral Menger curvature $\textnormal{intM}^{(p,q)}$, cf. \cite[Theorem 3]{BlattReiter:2015:Menger}, they showed that it is continuously differentiable on the subspace of all regular embedded $W^{(3p-2)/q-1,q}$-curves. Furthermore, they gave an explicit formula for the first variation  of $\textnormal{intM}^{(p,q)}$ at  any arc-length parametrized embedded $\gamma \in W^{(3p-2)/q-1,q}(\R/\Z, \R^n)$ in direction $h \in W^{(3p-2)/q-1,q}(\R/\Z, \R^n)$.

In the following we will restrict ourselves to the non-degenerate, sub-critical range of generalized integral Menger curvature, i.e. $q=2$ and $p\in(\tfrac 73, \tfrac 83)$. In \cite{BlattReiter:2015:Menger} it has turned out to be helpful in that case to decompose its first variation  into a term of highest order and lower order terms in order to study the regularity of critical points.

Hence we start with recapitulating a decomposition of the first variation introduced in \cite[(4.2) and Lemma 4.2]{BlattReiter:2015:Menger}. 
Note that we abbreviate
\[
\difference{x,y} f  := f(u+x) - f(u+y) 
\]
and 
\[
D:= \set*[w \leq 1 + 2v, v \geq -1 + 2w]{(v,w) \in \left(-\tfrac 1 2,0\right) \times \left(0,\tfrac 1 2\right)}.
\]
\sloppy
We observe for any arc-length parametrized embedded $\gamma \in W^{\frac 32 p-2,2}(\R/\Z, \R^n)$ and $h \in W^{\frac 32 p-2,2}(\R/\Z, \R^n)$ that
\[
\label{eq:firstVariation}
\numberthis
\delta \Mpz (\gamma,h) = 12(\Qp(\gamma,h) + R^{(p)} (\gamma,h)),
\]
\fussy
where the main term is given by
\[
\Qp(\gamma,h) := \iiint_{\R/\Z \times D}  \frac {\left< \frac {\difference{w,0} \gamma} {w} - \frac {\difference{v,0} \gamma} {v}, \frac {\difference{w,0} h} {w} - \frac {\difference{v,0} h} {v} \right>} {\abs{v-w}^p \abs{v}^{p-2} \abs{w}^{p-2}} \d w \d v \d u.
\]

The remainder term can be expressed as following. 
\begin{lemma}[\protecting{\cite[Lemma 4.2]{BlattReiter:2015:Menger}}]
	\label{lemma:formRemainder}
	The term $R^{(p)} (\gamma,h)$ is a finite sum of terms of the form 
	\[
	\iiint\limits_{\mathbb R / \mathbb Z \times D} \idotsint\limits_{[0,1]^K} g^p(u,v,w;s_{1},\dots,s_{K-2}) \otimes h'(u+s_{K-1}v + s_K w) 
	\d\theta_{1}\cdots\d\theta_{K}\d v \d w \d u
	\numberthis
	\label{lemma:formRemainder:formula}
	\]
	where $\G : (0,\infty)^3 \rightarrow \mathbb R$ is an analytic function, $\otimes$ may denote any kind of product
	structure, such as cross product, dot product, scalar or matrix multiplication, $s_{j}\in\set{0,\theta_{j}}$ for $j=1,\dots,K$,
	\begin{multline*}
	g^p(u,v,w;s_{1},\dots,s_{K-2})=
	\G \left(\frac{|\T 0w|}{|w|}, \frac{|\T 0v|}{|v|}, \frac{|\T vw|}{|v-w|}\right) 
	\Gamma(u,v,w,s_{1},s_{2})\cdot{}\\
	{}\cdot\left( \bigotimes_{i=3}^{K_1} \dg(u+ s_i v) \right) \otimes \left(\bigotimes_{j=K_1}^{K_2} \dg(u + s_i w) \right) \otimes \left(\bigotimes_{j=K_2}^{K-2} \dg(u+v + s_i (w-v)) \right),
	\end{multline*}
	and
	$\Gamma(u,v,w,s_{1},s_{2})$ is a term of one of the four types
	\begin{align*}
	&\frac{\br{\gamma'(u+s_1 w) - \gamma'(u+s_1 v)}\otimes\br{\gamma'(u+s_2 w) - \gamma'(u+s_2 v)}}{|v|^{p-2} |w|^{p-2} |v-w|^{p}}, \\
	&\frac{|\gamma'(u+s_1 w) - \gamma'(u+s_2 w)|^2}{|v|^{p-2} |w|^{p-2} |v-w|^{p}}, \\ 
	& \frac{|\gamma'(u+s_1 v) - \gamma'(u+s_2 v)|^2}{|v|^{p-2} |w|^{p-2} |v-w|^{p}}, \\ 
	& \frac{|\gamma'(u+v + s_1 (w-v)) - \gamma'(u+v+s_2 (w-v))|^2}{|v|^{p-2} |w|^{p-2} |v-w|^{p}}.
	\end{align*}
\end{lemma}

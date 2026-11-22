---
doc_id: arxiv-1403.4021v2
doc_title: "MARKOV TRACES ON THE BIRMAN-WENZL-MURAKAMI ALGEBRAS"
section_id: sec-017-66-splittings
section_title: "Splittings"
section_number: 6.6
pages: 35-36
source_pdf: 1403.4021v2.pdf
source_sha256: 046d02411e0dc086
toc_source: outline
text_source: latex
latex_prose_ratio: 0.974
latex_coverage_ratio: 0.95
doc_brief: "MARKOV TRACES ON THE BIRMAN-WENZL-MURAKAMI ALGEBRAS — We classify the Markov traces factoring through the Birman-Wenzl-Murakami (BMW) algebras."
---
In this section we show that our extension of the BMW-algebra is not split
exactly in the two cases we are interested in.


\begin{prop} \label{propsplittingsBMW} Let $k$ be a field of characteristic $0$ and $\varphi: S^{\dagger\dagger}_{\pm} \to k$
a morphism of $\Q$-algebras. Then, for $n \geq 3$, the natural short exact sequence
$0 \to k C \to (F_n \otimes_A S^{\dagger\dagger}_{\pm} ) \otimes_{\varphi} k
\to (BMW_n^{\pm})\otimes S^{\dagger\dagger}_{\pm} ) \otimes_{\varphi} k \to 0$
splits iff $\varphi(Q)$ has a root in $k$, where
$$
Q(\la) = x^4(1+ u \tilde{\delta} + u^2 \tilde{\delta}) \in S^{\dagger\dagger}_{\pm} [\la].
$$
and $u = 2 \la a (a-x)x^{-2}$.
If this is the case, each one of the roots $\la$ provides a splitting $s_i \mapsto s_i + \la C$, and these
are the only two possible splittings. In particular, if $k$ is algebraically closed, then the short
exact sequence splits iff $\varphi((x-a)(x-2a)) \neq 0$, and it admits exactly one
splitting iff $\varphi(x+2a) = 0$.
\end{prop}

\begin{proof}
In the proof we work inside the specializations, and identify $x,a,\dots$ with their images under $\varphi$.
Let us assume that there is a splitting, given by $e_i \mapsto \check{e}_i$, $s_i \mapsto \check{s}_i$.
This splitting provides a splitting of the extension of the Temperley-Lieb subalgebra, and therefore,
by proposition \ref{propTLsplit},
one needs to have $x \neq a$, and $\check{e}_i = e_i - \frac{x}{2(a-x)} C$. We have $\check{s}_i = s_i + \la_i C$
for some $\la_i \in k$. Moreover, the equation $(s_i-a)(s_i^2-xs_i+1) = 0$ implies
that $s_i^{-1} = a s_i^2 -(ax+1)s_i + (x+a)$. Since this equation also holds for $\check{s}_i$,
we get $\check{s}_i^{-1}  = a \check{s}_i^2 -(ax+1)\check{s}_i + (x+a)$. Expanding $\check{s}_i = s_i + \la_i C$
we get $\check{s}_i^{-1} = s_i^{-1} + \la_i a (a-x) (1+2\la_i \tilde{\delta}/x^2) C$. From this we then get that the
equation $\check{e}_i = a\left( \frac{\check{s}_i + \check{s}_i^{-1}}{x} -1 \right)$
imposes $Q(\la_i) = 0$. We now consider the braid relation $ \check{s}_i \check{s}_j \check{s}_i =
\check{s}_j \check{s}_i \check{s}_j = 0$ when $|j-i| = 1$. We get
$\check{s}_i \check{s}_j \check{s}_i = s_i s_j s_i + (2 \la_i + \la_j)C + (\la_i^2 + 2 \la_i \la_j) C^2 + \la_i^2 \la_j C^3$
and therefore
$\check{s}_i \check{s}_j \check{s}_i - \check{s}_j \check{s}_i \check{s}_j$ is equal to
$$
(\la_i - \la_j)\left( 2 \frac{\tilde{\delta}}{x^2}(a-x) \la_i+a\right) \left( 2 \frac{\tilde{\delta}}{x^2}(a-x) \la_j+a\right) C.
$$
Therefore, either $\la_i = \la_j$, or $\tilde{\delta} \neq 0$ and one of the two values $\la_i$ or $\la_j$
is equal to $\la_0 = -ax^2/(2 \tilde{\delta}(a-x))$. Since $Q(\la_0) = x^4/\tilde{\delta}$ this is excluded hence
$\la_i = \la_j$. This proves that $\la_i$ is independent of $i$, hence the splitting has the form $\check{s}_i = s_i + \la C$
with $\la$ independent of $i$. It then remains to prove that this formula, with $\la$ a root of $Q$, provides a splitting.
The relation $\check{s}_i \check{s}_j = \check{s}_j \check{s}_i$ when $|j-i| \geq 2$
is clear, and therefore the only two relations that remain to be checked are $\check{e_i} \check{s}_j^{\eps} \check{e}_i = \check{e}_i$
for $|j-i| = 1$ and $\eps \in \{-1,1\}$. For this we first check that $\check{e}_i C = 0$ by direct computation. Then,
$\check{e}_i \check{s}_j \check{e}_i = \check{e}_i(s_j + \la C) \check{e}_i
= \check{e}_i s_j \check{e}_i + \la \check{e}_i C\check{e}_i 
= \check{e}_i s_j \check{e}_i + 0$ and, expanding $\check{e}_i = e_i - \frac{x}{2(a-x)} C$, we  get
$\check{e}_i \check{s}_j \check{e}_i =  \check{e}_i$. The case $\eps = -1$ is similar, and this concludes the proof.


\end{proof}


\begin{remark}
In cohomological terms, the non splitting in the cases $x=a$ and $x=2a$ provides a non-zero cohomology 2-class in the
Hochschild cohomology of these specializations of the BMW algebras with values in the one-dimensional bimodule
given by $s_i \mapsto a$ (which factorizes through $BMW_n^{\pm}$ in these cases). 
If $x\not\in \{a,2a,-2a \}$ and the sequence splits, necessarily in two different ways, then the two splittings
afford to distinct $BMW_n^{\pm}$-bimodule structures on $k$, namely $s_i C = C s_i = bC$
and $s_i C = C s_i = c C$.
\end{remark}


\begin{remark} \label{remarkretractTL} Another natural question is
for which specializations $\varphi : A \to k$ (with $k$ a field of characteristic $0$)
the natural morphism $\widetilde{TL}_n \otimes_{\varphi} k \to F_n \otimes_{\varphi} k$
admits a retraction. A straightforward computation shows that this holds if and only if
$\varphi(x+2a) = 0$ and that, in this case, there is exactly one retraction. It
is given by $e_i \mapsto e_i$, $s_i \mapsto -e_i-a$, $s_i^{-1} \mapsto -e_i - a$, $C \mapsto C$.
\end{remark}

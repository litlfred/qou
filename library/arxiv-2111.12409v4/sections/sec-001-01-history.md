---
doc_id: arxiv-2111.12409v4
doc_title: "On the generalisation of Roth’s theorem"
section_id: sec-001-01-history
section_title: "History"
section_number: 0.1
pages: 1-2
source_pdf: 2111.12409v4.pdf
source_sha256: 3f0b94ee06fe79bf
toc_source: outline
text_source: latex
latex_prose_ratio: 0.984
latex_coverage_ratio: 0.855
doc_brief: "On the generalisation of Roth’s theorem — We present two generalisations of Roth’s approximation theorem on proper adelic curves, assuming some technical conditions on the behavior of the logarithmic"
---
\label{hi}
The celebrated Roth's theorem proved in \cite{roth} asserts that the irrationality measure of a real algebraic number is $2$. An equivalent, but more detailed statement is the following:
\begin{thm}[Roth]
Let $\alpha$ be a real algebraic number and let $\varepsilon>0$ be a real number. Then there exists a real constant $C(\alpha,\varepsilon)>0$ such that for every pair of coprime integers $(p,q)$ with $q>C(\alpha,\varepsilon)$, it holds that:
$$
\left|\alpha-\frac{p}{q}\right|> q^{-2-\varepsilon}
$$
\end{thm}

The above statement can be  naturally generalised in different directions by considering a number field $K$ instead of $\mathbb Q$ and the simultaneous approximation of the elements $\alpha_1,\ldots,\alpha_n$ algebraic over  $K$ by an element of $K$ with respect to different valuations (see \cite[Chapter 7]{lang}). Actually, the statement proved in \cite[Chapter 7]{lang} holds for fields that are more general than  number fields.  At the moment we don't have an \emph{effective} version of Roth's theorem  (i.e. a bound for the constant $C(\alpha,\varepsilon)$, see \cite{C1}), but we have a \emph{quantitative}  version (i.e.  bounds, in terms of $\alpha$ and $\varepsilon$, on the number of good approximants  see  \cite{bom}, \cite{bom1}, \cite{ever}).

Let $k$ be a field of characteristic $0$ and let $\mathcal V_k$ be a  set in bijection with a family of absolute values of $k$. The bijection is denoted by $v\mapsto |\cdot|_v$, for any $v\in\mathcal V_k$ and we don't put any restriction on the cardinality of $\mathcal V_k$, therefore we recall that a sum  over an uncountable  set  is defined to be the supremum of the sums over all finite subsets. The couple  $(k,\mathcal V_k)$ \emph{satisfies the product formula} if  for any element $a\in k^\times$ the series $\sum_{v\in\mathcal V_k} \log|a|_v$ converges absolutely and moreover $\sum_{v\in\mathcal V_k} \log|a|_v=0$. In this setting one also has a natural notion of \emph{logarithmic height} for $a\in k^\times$:
$$h(a):=\sum_{v\in\mathcal V_K}\log^+|a|_v\,,$$
and we set $H(a):=e^{h(a)}$.  Roth's theorem was generalised by Corvaja in  \cite{C}   for any couple $(k,\mathcal V_k)$ satisfying the product formula:
\begin{thm}\cite[Corollaire 1]{C}.\label{CorCorv}
Assume that $(k,\mathcal V_k)$ satisfies the product formula. Let $\alpha_1,\ldots,\alpha_n$ be distinct elements algebraic on $k$, and let $|\cdot|_{v_1},\ldots,|\cdot|_{v_n}$ be distinct absolute values of $k$, with $v_1,\ldots, v_n\in \mathcal V_k$. For any $i=1,\ldots,n$ let's fix an appropriately  normalised extension of  $|\cdot|_{v_i}$ to $k(\alpha_i)$ (and by abuse of notation denote it with the same symbol $|\cdot|_{v_i}$). Then for any  $\varepsilon>0$ there exists a constant $C=C(\mathcal V_k,\alpha_1,\ldots,\alpha_n, v_1,\ldots, v_n,\varepsilon)>0$ such that for all $\beta\in k$ with $H(\beta)>C$ it holds that:
$$\sum^n_{i=1}\log|\alpha_i-\beta|_{v_i}>-(2+\varepsilon)h(\beta)\,.$$
\end{thm}
Notice that there are no further assumptions on the field $k$, which might be for instance a function field; therefore, theorem \ref{CorCorv} is a unifying result, as well as a generalisation of the classical Roth's theorem. Moreover, in the same paper Corvaja obtained also a quantitative version of Theorem \ref{CorCorv} (see \cite[Corollaire 3.7]{C}). 
 
An \emph{arithmetic function field},  is a  finitely generated field over $\mathbb Q$. The ``geometrisation'' of these fields in terms of Arakelov geometry is wonderfully explained in \cite{Mor}. Recently,  Vojta in \cite{vo} proved a version of Roth's theorem for arithmetic function fields with a big polarisation. For obvious reasons this can be considered as a ``higher dimensional'' generalisation of Roth's theorem.  We  conclude this short historic overview by explaining the statement of Vojta's  result. A big polarisation of an arithmetic function field  $K$  consists of a couple $(X,\overline{\mathcal L})$ where:
\begin{itemize}
\item[$(i)$]$X\to \spec\mathbb Z$ is a normal arithmetic variety whose function field is isomorphic to $K$.
\item[$(ii)$] Denote with $d$ the relative dimension of $X$ over  $\spec\mathbb Z$; then $\overline{\mathcal L}=\{\overline{\mathscr L}_1,\ldots\overline{\mathscr L}_d\}$  is a collection of hermitian, arithmetically nef and big line bundles.
\end{itemize}
Now  fix an arithmetic function field  $K$ with a big polarisation; then we can define a geometric height function $h_{\overline{\mathcal L}}$ for a prime divisor $Y$ as the Arakelov intersection number of the hermitian  line bundles $\overline{\mathscr L}_1,\ldots,\overline{\mathscr L}_d$ restricted to $Y$. We can now define a non-archimedean absolute value on $K$, associated to $Y$:
$$\vert a\vert_Y:=e^{-h_{\overline{\mathcal L}}(Y)\ord_Y(a)}\quad\forall a\in K\,.$$
Moreover, for any closed point $p
\in X_{\mathbb C}=X\times_{\spec\mathbb Z}\spec \mathbb C$ that doesn't come from the base change of a divisor on $X$ we have the following archimedean absolute value:
$$|a|_p:=\sqrt{a(p)\overline {a(p)}}\quad\forall a\in K\,.$$
By putting all together, we get a set of absolute values $M_K$ which turns out to be a measure space with a measure that we denote with $\mu$. The notion of  product formula holds true for the couple $(K, M_K)$ in the following form:
$$\int_{M_K}\log \vert a\vert_\nu d\mu(\nu)=0\,,\quad\forall a\in K^\times$$
Moreover there is a notion of height for any element of $a\in K^\times$:
$$
h_{K}(a):=\int_{M_K} \log^+|a|_{v}\, d\mu(v)\,.
$$
We set $H_K(a):=e^{h_{K}(a)}$. One of the $4$ equivalent versions of Vojta's generalisation of Roth's theorem is given below.
\begin{thm}\cite[Theorem 4.5]{vo}\label{vojta}
Consider a couple $(K,M_K)$ where $K$ is an arithmetic function field with a big polarisation such that $\overline{\mathscr L}_1=\ldots=\overline{\mathscr L}_d$, and $M_K$ is a set of absolute values as explained before. Let $S$ be a subset of $M_K$ of finite measure and fix some distinct elements $\alpha_1,\dots ,\alpha_n\in  K$. Then for any $\varepsilon>0$ and any $c\in\mathbb R$ there exists a real constant $C>0$ (depending on the fixed data) such that for any $\beta\in  K$  with  $h_{K}(\beta)>C$   
it holds that:
\begin{equation}\label{our_roth_encore}
\int_{S}\,\min_{1\le i\le n}\left(\log^-\vert \beta-\alpha_i\vert_\omega\right) d\mu(\omega)>-(2+\varepsilon)h_K(\beta)+c
\end{equation}
\end{thm}

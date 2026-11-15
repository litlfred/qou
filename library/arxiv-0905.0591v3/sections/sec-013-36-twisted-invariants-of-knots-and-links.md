---
doc_id: arxiv-0905.0591v3
doc_title: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS"
section_id: sec-013-36-twisted-invariants-of-knots-and-links
section_title: "Twisted invariants of knots and links"
section_number: 3.6
pages: 11-11
source_pdf: friedvidu1.pdf
source_sha256: cfeaf61f759a6af8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.958
latex_coverage_ratio: 1.0
doc_brief: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS — We give a short introduction to the theory of twisted Alexander polynomials of a 3–manifold associated to a representation of its fundamental group."
---
Let $L=L_1\cup\dots \cup L_m\subset S^3$ be an ordered oriented link.
Recall that given a representation $\gamma:\pi_1(S^3\setminus \nu L)\to \mbox{GL}(k,R)$ with $R$ a Noetherian UFD we can consider the
twisted Alexander polynomial $\Delta_L^\gamma$ as an element in the Laurent polynomial ring
$R[t_1^{\pm 1},\dots,t_m^{\pm 1}]$ and we
 write $\Delta^\gamma_{L,i}(t_1,\dots,t_m)=\Delta^\gamma_{L,i}\in R[t_1^{\pm 1},\dots,t_m^{\pm 1}]$.

 Given  $\epsilon_j \in \{ \pm 1\}$ for $j=1,\dots,m$ we denote by
$L^\epsilon$ the link $\epsilon_1 L_1,\dots,\epsilon_m  L_m$, i.e. the oriented link obtained from $L$ by reversing  the orientation
of all components with $\epsilon_j=-1$.

The following lemma is now an immediate consequence of the definitions:

\begin{lemma}\label{lem:reverse}
Given  $\epsilon_j \in \{ \pm 1\}$ for $j=1,\dots,m$ we have
\[ \Delta^\gamma_{L^\epsilon,i}(t_1,\dots,t_m)=\Delta^\gamma_{L,i}(t_1^{\epsilon_1},\dots,t_m^{\epsilon_m}).\]
\end{lemma}

We now turn to the study of twisted Alexander polynomials of sublinks.
Given a link $L=L_1\cup \dots L_{k-1}\cup L_k\subset S^3$ Torres \cite{To53} showed how to relate the
Alexander polynomials of $L$ and $L'=L_1\cup \dots L_{k-1}\subset S^3$. The following theorem of Morifuji \cite[Theorem~3.6]{Mo07} gives a generalization of the Torres condition to twisted Reidemeister torsion.

\begin{theorem}
Let $L=L_1\cup \dots L_{k-1}\cup L_k\subset S^3$ be a link. Write  $L'=L_1\cup \dots L_{k-1}\subset S^3$
and let $\gamma':\pi_1(S^3\setminus \nu L')\to \mbox{SL}(n,\mathbb{F})$ be a representation where $\mathbb{F}$ is a field.
Denote by $\gamma$ the representation $\pi_1(S^3\setminus \nu L)\to \pi_1(S^3\setminus \nu L')\to \mbox{SL}(n,\mathbb{F})$,
then
\[ \tau(L,\gamma)(t_1,\dots,t_{k-1},1) \doteq \left(T^n+\sum_{k=1}^{n-1}\epsilon_iT^i+(-1)^n\right)\cdot \tau(L',\gamma')(t_1,\dots,t_{k-1}) \]
where
\[ T\mathrel{\mathop:}=\prod_{i=1}^{k-1} t_i^{lk(L_i,L_k)} \]
and where $\epsilon_1,\dots,\epsilon_{n-1}$ are elements of $\mathbb{F}$.
\end{theorem}

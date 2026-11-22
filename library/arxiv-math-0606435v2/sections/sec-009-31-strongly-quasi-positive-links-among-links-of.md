---
doc_id: arxiv-math-0606435v2
doc_title: "arXiv:math/0606435v2 [math.GT] 10 Oct 2007"
section_id: sec-009-31-strongly-quasi-positive-links-among-links-of
section_title: "Strongly quasi-positive links among links of braid index 3"
section_number: 3.1
pages: 11-12
source_pdf: 0606435v2.pdf
source_sha256: 6dddaf838a19f0f5
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.93
latex_coverage_ratio: 0.953
doc_brief: "arXiv:math/0606435v2 [math.GT] 10 Oct 2007 — We show that 3-braid links with given (non-zero) Alexander or Jones polynomial are ﬁnitely many, and can be effectively determined."
---
Theorem \reference{thqp} follows relatively easily from
the work in \cite{3br}, but it is a good starting point for
the later more substantial arguments basing on Xu's form.

\proof[of theorem \reference{thqp}]
The inequalities of \eqref{mq} for the $v$-degree
of $P$ applied on a positive band representation show that,
with $P=P(L)$ and $\chi=\chi(L)$,
\begin{eqn}\label{x}
\md_vP\ge 1-\chi\,.
\end{eqn}
Because of \cite[proposition 21]{LickMil}, which now says
\begin{eqn}\label{p21}
P(v,v^{-1}-v)=1\,,
\end{eqn}
we have $\md_lP\le
\Md_zP$, and by \cite{3br} $\Md_zP=1-\chi$. So from \eqref{x}
we obtain 
\begin{eqn}\label{y}
\md_lP=1-\chi\,. 
\end{eqn}

It is known that the minimal degree term in $z$ of the skein polynomial
of a $n$-component link is divisible by $(v-v^{-1})^{n-1}$. (In
\cite{Kneissler} in fact all occurring terms are classified.) So
if $MWF (K)=1$, then $K$ is a knot. Now, the identity \eqref{p21}
implies that if $MWF=1$ for some knot $K$, then $P(K)=1$. For
any non-trivial knot $1-\chi=2g>0$, so for any non-trivial strongly
quasi-positive knot from \eqref{x} we have $\md_vP>0$, and so $P\ne 1$.

So a strongly quasi-positive link cannot have $P=1$, and always
$MWF\ge 2$.  
Therefore, when the braid index is 3, we have
$MWF\in \{2, 3\}$. Then \eqref{y} and the inequalities \eqref{mq}
for the $v$-degree of $P$ show that a 3-braid representation $\bt$
has exponent sum $[\bt]=3-\chi$, unless $MWF=2$ and $[\bt]=1-\chi$.

In former case, we can find a minimal genus band representation
from $\bt$ by Xu's algorithm \cite{Xu}, and this representation
must be positive. In latter case, we will have one negative band,
and have Xu's form $L^{-1}R$. Here $L$ and $R$ are positive words in
the letters $\sg_1,\sg_2,\sg_3=\sg_2\sg_1\sg_2^{-1}$ with $\sg_i$
followed by $\sg_i$ or $\sg_{i\bmod 3+1}$ (as described
in \S\reference{brt}), and $L$ is a single letter.

W.l.o.g. assume $L=\sg_3$. If the first or last letter in $R$
is a $\sg_3$ then we can cancel two bands, and have a positive
representation. If some $\sg_3$ occurs in $R$, then we can write
$L^{-1}R=\sg_3^{-1}\ap\sg_3\ap'$ where $\ap,\ap'$ are positive
band words. Such a representation is quasi-positive with a Seifert
ribbon \cite{Rudolph} of smaller genus. However, it is known that
for strongly quasi-positive links the genus and 4-genus coincide
(see for example \cite{posqp}). If $R$ has no $\sg_3$, then
we have up to cyclic letter permutation a braid of the form
$\sg_1^k\sg_2^l\sg_1^{-1}\sg_2^{-1}$ with $k\ge 0$, $l>0$. This
braid is easily seen to reduce to (a positive one on) two strands.
\qed

\begin{rem}\label{rqw}
It is not true that all 3-braids that have the skein polynomial of
$(2,n)$-torus links have positive 3-band representations. Birman's
\cite{Birman} construction (see definition \reference{DEFB} below)
yields examples like $12_{2037}$ in \cite{KnotScape} with one
negative band. This construction gives in fact all non-obvious
3-braid $MWF=2$ examples, a circumstance shown in \cite{ntriv} by
applying theorem \ref{thq} (and reportedly in previous unpublished
work of El-Rifai). The result is explained and used below in the
proof of theorem \reference{thJC}.
\end{rem}

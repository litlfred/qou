---
doc_id: arxiv-1309.0865v1
doc_title: "SOERGEL CALCULUS"
section_id: sec-036-63-double-leaves
section_title: "Double leaves"
section_number: 6.3
pages: 62-64
source_pdf: 1309.0865v1.pdf
source_sha256: e610a4fa938a7cc9
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.964
latex_coverage_ratio: 0.969
doc_brief: "SOERGEL CALCULUS — The monoidal category of Soergel bimodules is an incarnation of the Hecke category, a fundamental object in representation theory."
---
The previous section was essentially a discussion of maps $B_{\un{w}} \to Q_w$ for some $w$. Let us use this to discuss maps $B_{\un{w}} \to B_{\un{y}}$ for arbitrary expressions ${\un{w}}$ and ${\un{y}}$.

Consider a light leaves map $\LL_{{\un{x}},\eb} \co B_{\un{x}} \to B_{\un{w}}$ where ${\un{w}}$ is a rex for $w$. Flipping this diagram upside-down, we get a map $\oLL_{{\un{x}},\eb} \co
B_{\un{w}} \to B_{\un{x}}$. By the results of the previous section, $\oLL_{{\un{w}},\eb}$ behaves nicely after localization, giving a nonzero map $Q_{{\un{w}}} \to Q_\fb$ only when $\fb
\le \eb$. The coefficients appearing are not actually $p^\eb_\fb$, because the polynomials $\frac{1}{\a_s}$ should appear only in the projections maps from $B_{s,Q}$ to $Q$ or $Q_s$, not
in the inclusion maps. In the new formula for $p^\eb_\eb$, U0 and U1 will not contribute, and D0 and D1 will contribute $\frac{1}{\a_k}$. We leave the reader to check the details.
Regardless, the result is still invertible in $Q$ and the analogue of Corollary \ref{LLalocalbasis} holds.

Now let ${\un{x}}$ and ${\un{y}}$ be arbitrary sequences with subsequences $\eb$ and $\fb$ respectively, such that $({\un{x}},\eb)$ and $({\un{y}},\fb)$ both express $w$. Choose a rex ${\un{w}}$ for $w$, and
construct maps $\LL_{{\un{w}},\eb} \co B_{\un{w}} \to B_{\un{w}}$ and $\oLL_{{\un{y}},\fb} \co B_{\un{w}} \to B_{\un{y}}$. We define the corresponding \emph{double leaves map} to be the composition 
\[
\LLL_{w,\fb,\eb} \define \oLL_{{\un{y}},\fb} \circ \LL_{{\un{x}},\eb}.
\] 
After localization, we obtain a coefficient $p^{\fb,\eb}_{\fb',\eb'}$ given by the inclusion of each standard summand $Q_{\eb'}$ of $B_{\un{x}}$ and projection to each standard summand $Q_{\fb'}$ of ${\un{y}}$. We know several facts about these coefficients:

\begin{itemize} \item $p^{\fb,\eb}_{\fb',\eb'}=0$ unless $({\un{x}},\eb')$ and $({\un{y}},\fb')$ express the same element $v$.
\item $p^{\fb,\eb}_{\fb',\eb'}=0$ unless both $\eb'
\le \eb$ and $\fb' \le \fb$. In particular, this implies that the commonly expressed element $v$ must satisfy $v \le w$. We refer to this latter phenomenon as \emph{Bruhat
upper-triangularity}, a special kind of path dominance upper-triangularity.
\item When $v=w$, $\eb'=\eb$ and $\fb'=\fb$, the coefficient is nonzero and is a product of roots, obeying a
simple formula independent of the choice of $\LL$ maps. \end{itemize}

\begin{prop} Let $\LLL_{{\un{w}},{\un{y}}}$ contain one map $\LLL_{w,\fb,\eb}$ for each $w \in W$ and each pair of subsequences $({\un{x}},\eb)$ and $({\un{y}},\fb)$ expressing $w$. Then after localization, $\LLL_{{\un{w}},{\un{y}}}$ forms a basis of maps $B_{\un{w}} \to B_{\un{y}}$. In particular, the set $\LLL_{{\un{w}},{\un{y}}}$ is linearly independent. \label{LLLalocalbasis} \end{prop}

\begin{proof} After localization, the space of maps $B_{\un{w}} \to B_{\un{y}}$ is a direct sum of $\Hom(Q_\eb,Q_\fb)$ for each pair of subsequences. These terms have a partial order, and the
$\LLL$ maps satisfy upper-triangularity with respect to this partial order, with an invertible diagonal. \end{proof}

\begin{remark} In the definition of the double leaves basis we could have taken $\LL$ maps and rotated them 180 degrees, instead of flipping them. This would avoid some of the annoyances of the final
chapter, but would introduce its own annoyances. Most notably, rotation takes a map $B_{\un{w}} \to B_{\un{y}}$ and returns a map $B_{\o({\un{y}})} \to B_{\o({\un{w}})}$, where $\o$ denotes reversing the order of a
sequence. To define $\oLL$ using a rotated map, the target of the original map must be $B_{\o({\un{w}})}$, which is actually a rex for $w^{-1}$, and this requires additional bookkeeping.
Rotation will be more obviously useful in the final chapter. Note that both approaches are equally valid, although coming up with a change of basis matrix between them would be a combinatorial nightmare. Also, flipping a diagram vertically is more natural in terms of the cellular structure.\end{remark}

Let us now state some of our main results, which all assume Demazure Surjectivity:

\begin{thm} \label{homspacetheorem} The set $\LLL_{{\un{x}},{\un{y}}}$ forms a free $R$-basis for $\Hom(B_{\un{x}},B_{\un{y}})$ in $\DC$. \end{thm}

\begin{prop} \label{homspaceprop} The set $\LL_{{\un{x}},e}$ forms a free $R$-basis for $\Hom(B_{\un{x}},\1)$ in $\DC$. \end{prop}

\begin{cor} Hom spaces in $\DC$ are free graded $R$-modules. \end{cor}

\begin{remark} Proposition \ref{homspaceprop} is a special case of Theorem \ref{homspacetheorem}, because when ${\un{y}}=\emptyset$ we must have $w=e$, and $\oLL_{{\un{y}}}$ is the empty
diagram.\end{remark}

The final chapter of this paper contains an elementary diagrammatic (though unpleasant) proof of these results.  Of course it is enough to show that $\LLL$ spans, as we have already shown that this set is linearly independent over $R$. The reader is now equipped to read that chapter, which does not use anything beyond this
section.

We assume these three results for the rest of this chapter.

Because Theorem \ref{homspacetheorem} did not depend on the particular $\LL$ maps chosen, this implies that two different choices of $\LLL$ are pairwise dependent. It does \emph{not} imply
that two different choices of $\LL_{{\un{x}},w}$ are pairwise dependent, because the dependence relations may require lower terms.

\begin{ex} Let $s,t$ be the indices in type $A_2$. There are two choices for the map $\LL_{sts,111}$, as below. The difference between them is not an $\LL$ map, but it is an $\LLL$ map.
\igc{1}{LLvsLLnew} \end{ex}

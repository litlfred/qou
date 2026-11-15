---
doc_id: arxiv-1309.0865v1
doc_title: "SOERGEL CALCULUS"
section_id: sec-035-62-localizing-light-leaves
section_title: "Localizing light leaves"
section_number: 6.2
pages: 60-62
source_pdf: 1309.0865v1.pdf
source_sha256: e610a4fa938a7cc9
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.966
latex_coverage_ratio: 0.976
doc_brief: "SOERGEL CALCULUS — The monoidal category of Soergel bimodules is an incarnation of the Hecke category, a fundamental object in representation theory."
---
Let us fix a light leaves map $\LL_{{\un{x}},\eb}$, with $\eb$ expressing $w$. Let ${\un{w}}$ be the target of the map. Now consider what happens after the passage $\DC \to \Kar(\DC_Q)$. The target $B_{\un{w}}$ splits up into standard summands, with a unique summand isomorphic to $Q_w$. For each subsequence $\fb$ of ${\un{x}}$ which also expresses $w$ we have a summand $Q_\fb \sumset B_{\un{w}}$ isomorphic to $Q_w$, and this is sent by $\LL_{{\un{w}},\eb}$ into the unique summand $Q_w \sumset B_{\un{w}}$ with some coefficient $p^\eb_\fb \in Q$. For the conventions used to calculate this coefficient, see section \ref{subsec-compute}. A priori this coefficient depends on the choices made in the construction of $\LL_{{\un{w}},\eb}$.

\begin{prop}[Path Dominance Upper-triangularity] If $p^\eb_\fb \ne 0$ then $\fb \le \eb$ in the path dominance order. Moreover, $p^\eb_\eb$ is non-zero, and is a product of roots
independent of the choice of $\LL_{{\un{x}},\eb}$. \end{prop}

\begin{proof} Let us use the same notation as the previous section, so that $w_k$ is the element expressed by $({\un{w}}_{\le k},\eb_{\le k})$. We write $v_k$ for the corresponding element with $\eb$ replaced by $\fb$.

Remember that $\LL_{{\un{w}},\eb}$ is defined inductively, beginning with $\LL_k = \LL_{{\un{w}}_{\le k},\eb_{\le k}} \ot \1$. The target of $\LL_k$ is ${\un{w}}_k$, a rex for $w_k$, which only has
standard summands corresponding to elements $u \le w_k$. Therefore $\LL_k$ will clearly act as zero on $Q_{\fb_{\le k}}$ unless $v_k \le w_k$. Thus $\LL_{{\un{w}},\eb}$ will act as zero on
$Q_\fb$ unless $v_k \le w_k$ for every $k$, which is exactly the condition for $\fb \le \eb$ in the path dominance order. The upper-triangularity now follows.

We now turn to an explicit formula for $p^\eb_\eb$. For each $k \le \ell({\un{x}})$ define a root $\a_k$ as follows:
\begin{gather*}
  \a_k \define \begin{cases} w_{k-1}(\a_{{\un{x}}_k}) & \text{if $\eb_k$ is U0,} \\
-w_{k-1}(\a_{{\un{x}}_k}) & \text{if $\eb_k$ is D1,} \\
1 & \text{otherwise.}
\end{cases}
\end{gather*}
Note that $w_{k-1}(\a_{{\un{x}}_k})$ is the coefficient one obtains if one places $\a_{{\un{x}}_k}$ in the region just before ${\un{w}}_k$, as an element of $Q_\eb$,
and pulls it to the far left region. We claim that $p^\eb_\eb = \prod_{k=1}^{l({\un{x}})} \a_k$.

Consider what happens at the $k$-th step, when one includes from either $\1$ or $Q_s$ into $B_s$, and then follows $\phi_k$, the inductive part of an $\LL$ map (see figure
\ref{calculatingp}). First let us take care of all the cases when $\eb_k$ is 0. If $\eb_k$ is U0 then $\phi_k$ is a dot and the inclusion from $R$ is a dot, leaving us with a factor of $\a_s$ in that spot,
which we drag left to obtain $\a_k$. If $\eb_k$ is D0 then $\phi_k$ is a trivalent vertex; the dot from the inclusion pulls into the trivalent vertex, leaving nothing behind. What remains
is an $\LL$ map with all 0's removed (with a coefficient), so it is enough to check the formula when $\eb$ consists only of 1's.

Remember that bivalent vertices ``pull through" rex moves, as in relation \eqref{slidebivalentthru2m}. All that remains of the $\LL$ map is rex moves and caps. If $\eb_k$ is U1 then one
has a bivalent vertex as the inclusion map, which will eventually pull through braids and run into either a D1 or the top of the diagram. If it runs into the top, it will precisely cancel
the projection map on top, leaving no coefficient. If $\eb_k$ is D1 then the bivalent vertex meets a bivalent vertex from an earlier U1, and using relation \eqref{dashedcupscaps} we obtain
a factor of $-\a_s$, which pulls left to become $\a_k$, as in figure \ref{calculatingp}.

\begin{figure} \label{calculatingp} \caption{Calculating $p^\eb_\eb$} $\ig{1}{simplemap2} \qquad \ig{1}{wickedmap2} \qquad \ig{1}{wisemap2}$ \end{figure}

What we obtain is precisely the standard diagram representing the only map from $Q_{\eb}$ to $Q_{{\un{w}}}$, with a polynomial on the left equal to $\prod_{k=1}^{l({\un{w}})} \a_k$. \end{proof}

\begin{remark} Do not believe that just because $p^\eb_\eb$ did not depend on the choice of rex moves in the construction of $\LL_{{\un{w}},\eb}$, that no coefficients do. When $\fb < \eb$,
$p^\eb_\fb$ does depend on the rex moves chosen. Here is an example, where ${\un{w}}=(s,t,s,s,t,s)$ in type $A_2$, $\eb=(1,1,1,1,1,1)$ and $\fb=(0,0,0,0,0,0)$. \igc{1}{lowercoeffsdepend}
However, it is a priori clear that all coefficients $p_{\fb}^\eb$ are either products of $W$-conjugates of simple roots, or are zero. 
\end{remark}

\begin{cor} Fix an expression $\un{x}$ and let $\LL_{{\un{x}},w}$ be a set consisting of one light leaves map $\LL_{{\un{x}},\eb} \co B_{\un{x}} \to B_{\un{w}}$ for each subexpression $\eb$ expressing $w$. Now consider the maps $B_{\un{x},Q} \to Q_{w}$ in $\Kar(\DC_Q)$ obtained by postcomposing $\LL_{{\un{x}},\eb}$ with the projection $B_{\un{w},Q} \to Q_{w}$. These maps form a basis for $\Hom(B_{\un{w},Q}, Q_{w})$. Moreover, the original set $\LL_{{\un{x}},w}$ is linearly independent over $R$ as a subset of $\Hom(B_{\un{x}}, B_{\un{w}})$. \label{LLalocalbasis}\end{cor}

\begin{proof} The morphism space $B_{\un{w},Q} \to Q_{\un{w}}$ is the direct sum, for each $\fb$ expressing $w$, of the morphism space $Q_\fb \to Q_{\un{w}}$. The basis result now follows
from upper-triangularity, and the invertibility of the diagonal in $Q$. Linear independence follows immediately. \end{proof}

This corollary is essentially Libedinsky's theorem \cite{Lib}, and we have now presented a diagrammatic proof for it, entirely within the context of $\DC$ and $\DStd$ (i.e. without ever
using bimodules). As soon as one knows that the dimensions of $\Hom$ spaces is given by the standard pairing (as is the case for Soergel bimodules by \ref{SoergelThm2}) it follows by counting dimensions that the set $LL_{\un{w}, e}$ gives a  basis of $\Hom(B_{\un{w}}, R)$.

---
doc_id: arxiv-1412.4711v1
doc_title: "CHARACTER VARIETIES FOR SL(3, C): THE FIGURE EIGHT KNOT"
section_id: sec-002-11-representation-variety-and-character-variety
section_title: "Representation variety and character variety"
section_number: 1.1
pages: 3-4
source_pdf: 1412.4711v1.pdf
source_sha256: 4fb1d6ee062cca8c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.969
latex_coverage_ratio: 0.94
doc_brief: "CHARACTER VARIETIES FOR SL(3, C): THE FIGURE EIGHT KNOT — We give a description of several representation varieties of the fundamental group of the complement of the ﬁgure eight knot in PGL(3, C) or"
---
We begin by the most classical representation variety and character variety.

\newcommand{\Mon}{\mathrm{Mon}}

\begin{defn} 
We denote by $\Hom(\Gamma, G)$ the set of all morphisms
from $\Gamma$ to $G$. This space is called the \emph{representation variety}.

The \emph{monodromy variety}\footnote{Neither the name nor the notation is classical. The name has been so choosen because a geometric structure on a variety gives naturally, via the monodromy of the structure, an element in the monodromy variety.} $\Mon(\Gamma,G)$ is the quotient under the natural action by conjugation of $G$ :
$$\Mon(\Gamma,G)=\Hom(\Gamma,G)/G.$$
\end{defn}

Note that $\Hom(\Gamma,G)$ is an affine algebraic variety as $\Gamma$ is finitely presented and $G$ is affine  algebraic. Moreover the relators correspond to generators of the ideal defining the variety. Note however that $\Mon(\Gamma,G)$ is not an algebraic variety.


Though, the action of $G$ on itself by conjugation is an algebraic action.  Therefore it defines an algebraic action on $\Hom(\Gamma, G)$ which induces an
algebraic action on its regular functions.  We let $\bC[\Hom(\Gamma, G))]^{G}$ be the ring of invariant functions.
\begin{defn}
The \emph{character variety} is the algebraic quotient:
$$
X(  \Gamma, G)=\Hom(\Gamma, G)//G.
$$
It is the affine variety associated to the ring  $\bC[\Hom(\Gamma, G)]^{G}$ and comes together with the  regular map
$\Hom(\Gamma, G)\rightarrow  X(\Gamma, G)$ induced by the homomorphism 
$$
  \bC[X(  \Gamma, G)]=\bC[\Hom(\Gamma, G)]^{G} \rightarrow \bC[\Hom(\Gamma, G)]. 
$$
\end{defn}
\newcommand{\tr}{\mathrm{tr}}
The name of this variety comes from its links with the set of \emph{characters}, at least when $G=\SL(n,\bC)$ or $\PGL(n,\bC)$. 

When $G=\SL(n,\bC)$ traces of elements are well defined and one knows that there is a bijection between the character variety and the set of trace functions.

For the case $G=\PGL(n,\bC)$, let us remark that for an element $g$ in $\PGL(n,\bC)$, one may define its trace to the power $n$: choose a representant $\tilde g$ of $g$ which belongs to $\SL(n,\bC)$. Then we put: $\tr^n(g):=\tr^n(\tilde g)$. It does not depend on the choice of $\tilde g$.

\begin{defn} The character of $\rho\in\Hom(\Gamma,G)$ is the trace function
$\chi_\rho : \Gamma\rightarrow \bC$ defined by $\chi_\rho(\gamma)={\mbox{tr}}^n(\rho(\gamma))\ $. 
\end{defn}
 
Although we will not use it here, we believe that the map 
$$ 
X(  \Gamma, G)\rightarrow \{\textrm{characters of }\Gamma\} 
$$
induced by $\rho \mapsto \chi_\rho$ is a bijection. It is well-known for $n=2,\, 3$, see e.g. \cite{Lawton}.

Note that there is also a natural application from $\Mon(\Gamma,G)$ to $X(\Gamma,G)$ sending the class of a representation $\rho$ to $\chi_\rho$. This application is a surjection, but not an injection. It is not algebraic, as $\mathrm{Mon}(\Gamma,G)$ is not an algebraic variety.

---
doc_id: arxiv-1309.0865v1
doc_title: "SOERGEL CALCULUS"
section_id: sec-008-15-consequences-for-the-structure-of-soergel-bim
section_title: "Consequences for the structure of Soergel bimodules"
section_number: 1.5
pages: 11-13
source_pdf: 1309.0865v1.pdf
source_sha256: e610a4fa938a7cc9
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.987
latex_coverage_ratio: 0.97
doc_brief: "SOERGEL CALCULUS — The monoidal category of Soergel bimodules is an incarnation of the Hecke category, a fundamental object in representation theory."
---
Let $\DC$ denote the diagrammatic category defined by generators and relations in the previous section. In order to prove that this category is equivalent to $\BSBim$, we construct a basis
for morphisms in $\DC$, which is sent to a basis for morphisms in $\BSBim$. In \cite{Lib}, Libedinsky constructed a combinatorial basis for the morphism space between two Bott-Samelson
bimodules, which he called the \emph{light leaves} basis. His construction involves the technique of localization, which we will also explore diagrammatically in this paper.

Let $\un{x}$ be an expression and $\eb$ a subexpression expressing $w$. That is if $\un{x} = s_1 \dots s_m$ then $\eb$ is a sequence $\eb_1 \dots \eb_m$ of 0's and 1's such that $w = s_1^{\eb_1} \dots s_m^{\eb_m}$.
To this pair Libedinsky assigns a morphism $\LL_{\un{x},\eb} : B_{\un{x}} \to B_{\un{w}}$ where $\un{w}$ is a reduced expression for $w$. Libedinsky's definition of $\LL_{\un{x}, \eb}$ is inductive and at each step may involve a choice of reduced expression and as well as a sequence of braid relations to reach such an expression. So, though beautiful, it is highly non-canonical. We  translate Libedinsky's construction into our diagrammatic language, in which case a light leaf morphism can be thought of as a kind of rhombus (see section \ref{sec-LLL})
\[
\begin{array}{c}
\begin{tikzpicture}[scale=0.7]
\draw (-0.3,-2) -- (-2,-2) -- (-1,0) -- (-0.3,0);
\draw (0.3,-2) -- (2,-2) -- (1,0) -- (0.3,0);
\node (top) at (0,0) {$\un{w}$};
\node (mid) at (0,-1) {$\LL_{\un{x}, \eb}$};
\node (bot) at (0,-2) {$\un{x}$};
\end{tikzpicture}
\end{array}
\]
where the upper expression is always reduced.

Now let $\un{x}$ and $\un{y}$ be fixed expressions. 
Following Libedinsky, we introduce the \emph{double leaves} morphism
\[
\LLL_{w,\eb,\fb} \define 
\begin{array}{c}
\begin{tikzpicture}[scale=0.7]
\draw (-0.3,-2) -- (-2,-2) -- (-1,0) -- (-0.3,0);
\draw (0.3,-2) -- (2,-2) -- (1,0) -- (0.3,0);
\draw (-0.3,2) -- (-2,2) -- (-1,0) -- (-0.3,0);
\draw (0.3,2) -- (2,2) -- (1,0) -- (0.3,0);
\node (top) at (0,2) {$\un{y}$};
\node (mid) at (0,1) {$\oLL_{\un{y}, \fb}$};
\node (top) at (0,0) {$\un{w}$};
\node (mid) at (0,-1) {$\LL_{\un{x}, \eb}$};
\node (bot) at (0,-2) {$\un{x}$};
\end{tikzpicture}
\end{array}
\]
where $\oLL_{\un{y}, \fb}$ denotes the vertical flip of a light leaf morphism, and $\eb$ (resp. $\fb$) is a subexpression of $\un{x}$ (resp. $\un{y}$) which expresses $w$. Hence $\LLL_{w,\eb,\fb}$ is a morphism $B_{\un{x}} \to B_{\un{y}}$. Consider the set
\[
\LLL_{\un{x}, \un{y}} \define \bigcup_{w \in W} \{ \LLL_{w,\eb,\fb} \; | \; \eb \in M(\un{x}, w), \fb \in M(\un{y}, w)\}
\]
where, $M(\un{x}, w)$ denotes the set of subexpressions of $\un{x}$ expressing $w$. Our main theorem is then the following:

\begin{thm} $\LLL_{\un{x},\un{y}}$ is an $R$-basis for $\Hom_{\DC}(B_{\un{x}}, B_{\un{y}})$. \end{thm}

The proof of this theorem is pure diagrammatic algebra. Unfortunately it is quite convoluted. It has the following consequences:
\begin{enumerate}
\item Under very general assumptions one has a functor $\DC \to \SBim$ (we defined this functor earlier under the assumption that $2$ was invertible).  If the category of Soergel bimodules is well-behaved (i.e. if the Soergel Categorification Theorem holds) then this functor is an equivalence of monoidal categories.
\item Soergel bimodules play an important role in modular representation theory \cite{Soergel, FiebigJAMS}.
Here it is desirable to have versions over fields of positive characteristic and local rings. One can define the diagrammatic category over very general rings. For example, if $W$ is crystallographic then one can define the diagrammatic category over $\ZM$. Over a complete local ring the indecomposable objects in the diagrammatic category are parametrized (up to shift) by $W$, and the split Grothendieck group always categorifies the Hecke algebra. This gives a new proof of Soergel's Categorification Theorem whenever Soergel bimodules are well-behaved, and suggests that the diagrammatic category is the correct replacement when they are not.
\item The category of Bott-Samelson bimodules is a cellular category, with cells parametrized by $w \in W$, and with cellular basis given by a fixed choice of light leaves morphisms. In particular, the endomorphism ring of any Bott-Samelson bimodule is a cellular algebra.
\end{enumerate}

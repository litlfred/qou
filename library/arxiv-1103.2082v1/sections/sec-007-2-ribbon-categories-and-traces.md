---
doc_id: arxiv-1103.2082v1
doc_title: "MODIFIED TRACES ON DELIGNE’S CATEGORY Rep(St)"
section_id: sec-007-2-ribbon-categories-and-traces
section_title: "Ribbon Categories and Traces"
section_number: 2
pages: 3-4
source_pdf: 1103.2082v1.pdf
source_sha256: 0ac5371486b38eac
toc_source: outline
text_source: latex
latex_prose_ratio: 0.961
latex_coverage_ratio: 0.984
---
\label{S:ribboncategories}   The authors of \cite{GKP} define modified trace functions for ideals in ribbon categories.  In this section we give a brief overview of this theory but refer the reader to the above paper for further details and proofs. 


\subsection{Ribbon Categories}\label{SS:ribboncats}  For notation and the general setup of ribbon categories our references are \cite{Tu} and \cite{Kas}.  A \emph{tensor category} $\cat$ is a category equipped with a covariant
bifunctor 
\[
\otimes :\cat \times \cat\rightarrow \cat
\]
called the tensor product, a unit object $\unit$, an associativity constraint, and left and
right unit constraints such that the Triangle and Pentagon Axioms hold (see \cite[XI.2]{Kas}).  In particular, for any $V$ in $\cat$, $\unit \otimes V$ and $V \otimes \unit$ are canonically isomorphic to $V$.

A \emph{braiding} on a tensor category $\cat$ consists of a family of isomorphisms 
\[
\{c_{V,W}: V \otimes W \rightarrow W\otimes V \},
\]
 defined for each pair of objects $V,W$ which satisfy the Hexagon Axiom \cite[XIII.1 (1.3-1.4)]{Kas} as well as the naturality condition expressed in the commutative diagram \cite[(XIII.1.2)]{Kas}.
We say a tensor category is \emph{braided} if it has a braiding.  We call the braiding \emph{symmetric} if 
\[
c_{W, V} \circ c_{V,W} = \Id_{V \otimes W}
\]
for all $V$ and $W$ in $\cat$.

A tensor category $\cat$ has \emph{duality} if for each object $V$ in $\cat$ there exits an object $V^{*}$ and coevaluation and evaluation morphisms\footnote{In \cite{GKP} these maps are denoted $b_{V}$ and $d_{V}$, respectively.} 
$$\coev_{V}: \unit \rightarrow V\otimes V^{*} \: \text{ and } \: \ev_{V}: V^{*}\otimes V \rightarrow \unit$$
satisfying relations \cite[XIV.2 (2.1)]{Kas}.

A \emph{twist} in a braided tensor category $\cat$ with duality is a family 
\[
\{ \theta_{V}:V\rightarrow V \}
\]
of natural isomorphisms defined for each object $V$ of $\cat$ satisfying relations \cite[(XIV.3.1-3.2)]{Kas}. Let us point out that the existence of twists is equivalent to having functorial isomorphisms $V \xrightarrow{\cong} V^{**}$ for all $V$ in $\cat$ (cf.\ \cite[Section 2.2]{BK}).

A \emph{ribbon category} is a braided tensor category with duality and twists.  A fundamental feature of ribbon categories is the fact that morphisms in the category can be represented diagrammatically and that isotopic diagrams correspond to equal morphisms.  For the sake of brevity, we do not give the graphical calculus here but encourage the interested reader to refer to \cite{Kas}. 

In a ribbon category it is convenient to also define the morphisms

\begin{equation*}
\coev'_{V} : \unit \to V^{*} \otimes V \text{ and } \ev'_{V}: V \otimes V^{*} \to \unit
\end{equation*}
which are given by
\begin{equation*}
\coev'_V =(\Id_{V^*}\otimes \theta_V) \circ c_{V,V^*} \circ \coev_{V}  \text{ and } \ev'_V  = \ev_{V} \circ c_{V,V^*} \circ (\theta_V\otimes \Id_{V^*}).
\end{equation*}
Finally, the \emph{ground ring} of a ribbon category $\cat$ is 
\[
K=\End_{\cat}(\unit ).
\]  We assume $K$ is a field, that the category is $K$-linear, and that the tensor product is bilinear. Later references to linearity will always be with respect to $K$.
Ultimately the ground ring will be a fixed field $F$ of characteristic zero and the categories in question will be $F$-linear.

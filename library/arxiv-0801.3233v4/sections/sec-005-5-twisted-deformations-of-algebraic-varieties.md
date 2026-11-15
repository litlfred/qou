---
doc_id: arxiv-0801.3233v4
doc_title: "Twisted Deformation Quantization of Algebraic Varieties (Survey)"
section_id: sec-005-5-twisted-deformations-of-algebraic-varieties
section_title: "Twisted Deformations of Algebraic Varieties"
section_number: 5
pages: 6-8
source_pdf: 0801.3233v4.pdf
source_sha256: d98f9d4a9ecb4c5e
toc_source: outline
text_source: latex
latex_prose_ratio: 0.984
latex_coverage_ratio: 0.985
doc_brief: "Twisted Deformation Quantization of Algebraic Varieties (Survey) — Let X be a smooth algebraic variety over a ﬁeld of characteristic 0. We introduce the notion of twisted associative (resp."
---
\label{sec:twdefs}

What can be done in general, when the variety $X$ is not affine? Can
we still make use of Theorem \ref{thm2}? 

In the paper \cite{Ko3} Kontsevich suggests that in general the 
deformation quantization of a Poisson bracket might have to be a 
{\em stack of algebroids}. This is a generalization of
the notion of sheaf of algebras. 

Actually stacks of algebroids appeared earlier, 
under the name {\em sheaves of twisted modules},
in the work of Kashiwara \cite{Ka}. See also \cite{DP}, \cite{PS},
\cite{KS1}, \cite{KS2}. 

I will use the term {\em twisted associative deformation},
and present an approach that treats the Poisson case as well. 
A similar point of view is taken in \cite{BGNT}. 

Here I will explain only a naive definition of twisted 
deformations. A more sophisticated definition, involving gerbes, 
may be found in Appendix D.
The fact that the two definitions agree follows from our work on
central extensions of gerbes and obstructions classes \cite{Ye5}.

Let $U \subset X$ be an affine open set, and let
$C := \Gamma(U, \mcal{O}_X)$. 
Suppose $A$ is an associative or Poisson deformation of the
$\K$-algebra $C$.
One may assume that 
$A = C[[\hbar]]$, and it is either endowed with a Poisson bracket
$\{ -,- \}$, or with a star product $\star$.  

In either case $A$ becomes a pronilpotent Lie algebra, and 
$\hbar A$ is a Lie subalgebra. In the Poisson
case the Lie bracket is $\{ -,- \}$, and in the associative case the
Lie bracket is the commutator
\[ [a,b] := a \star b - b \star a . \]
Let us denote the corresponding pronilpotent group by
\[ \opn{IG}(A) := \opn{exp}(\hbar A) , \]
and call it the {\em group of inner gauge transformations}
of $A$.

The group $\opn{IG}(A)$ acts on the deformation $A$ by gauge
equivalences. We denote this action by $\opn{ig}$. 
In the Poisson case the gauge
transformation $\opn{ig}(g)$, for $g \in \opn{IG}(A)$,
can be viewed as a formal hamiltonian flow. 
In the associative case the intrinsic exponential function
\[ \exp(a) =  \sum_{i \geq 0} \smfrac{1}{i!} \,
\underset{i}{\underbrace{ a \star \cdots \star a }} , \] 
for $a \in \hbar A$, allows us to identify the group $\opn{IG}(A)$
with the multiplicative subgroup 
\[ \{ g \in A \mid g \equiv 1 \opn{mod} \hbar \} . \]
Under this identification the operation $\opn{ig}(g)$ is just
conjugation by the invertible element $g$. 

The above can be sheafified: to a deformation $\mcal{A}$ of
$\mcal{O}_X$ we
assign the sheaf of groups $\opn{IG}(\mcal{A})$, etc.

Let us fix an affine open covering
$\{ U_0, \ldots, U_m \}$ of $X$. 
We write
\[ U_{i,j, \ldots} := U_i \cap U_j \cap \cdots . \]

\begin{dfn} \label{dfn1} 
A {\em twisted associative \tup{(}resp.\ Poisson\tup{)}
deformation} $\bsym{\mcal{A}}$ of $\mcal{O}_X$
consists of the following data: 
\begin{enumerate}
\item For any $i$, a deformation $\mcal{A}_i$ of $\mcal{O}_{U_i}$. 
\item For any $i < j$, a gauge equivalence
\[ g_{i,j} : \mcal{A}_i|_{U_{i,j}} \to \mcal{A}_j|_{U_{i,j}} .\] 
\item For any $i < j <k$, an element
\[ a_{i,j,k} \in \Gamma \bigl( U_{i,j,k}, \opn{IG}(\mcal{A}_i) \bigr)
. \]
\end{enumerate} 
The conditions are: 
\begin{enumerate}
\rmitem{i} For any $i <j <k$ one has
\[ g_{i,k}^{-1} \circ g_{j,k} \circ g_{i,j} = \opn{ig}(a_{i,j,k}^{-1})
. \]
\rmitem{ii} For any $i <j < k < l$ one has
\[ a_{i,j,l}^{-1} \cdot a_{i,k,l} \cdot a_{i,j,k} = 
g_{i,j}^{-1}(a_{j,k,l}^{}) . \]
\end{enumerate}
\end{dfn}

Condition (i) says that the $2$-cochain $\{ a_{i,j,k} \}$ 
measures the failure of the $1$-cochain $\{ g_{i,j} \}$ to be a
cocycle. This 
tells us whether the collection $\{ \mcal{A}_i \}$ of local
deformations can be glued into a global deformation of $\mcal{O}_X$. 

Condition (ii) -- usually called the tetrahedron equation -- says that
the $2$-cochain $\{ a_{i,j,k} \}$ satisfies a twisted cocycle condition. 

See Figure 1 for an illustration. 

\begin{figure}
\includegraphics[scale=0.4]{figure-1.jpg}
\caption{}
\end{figure}

\begin{exa} \label{exa:20}
If $\mcal{A}$ is a usual deformation of $\mcal{O}_X$, then we obtain
a twisted deformation $\bsym{\mcal{A}}$ by taking
$\mcal{A}_i : = \mcal{A}|_{U_i}$, $g_{i,j} := \bsym{1}$ and
$a_{i,j,k} := 1$.

In this way we can view usual deformations as twisted deformations. 
\end{exa}

There is a notion of {\em twisted gauge equivalence} 
$\bsym{\mcal{A}} \to \bsym{\mcal{A}'}$ between twisted
associative (resp.\ Poisson) deformations of $\mcal{O}_X$. 

Let $\bsym{\mcal{A}}$ be a twisted deformation.
We say $\bsym{\mcal{A}}$ is {\em really twisted} if
it is not twisted-equivalent to any usual deformation $\mcal{A}'$. 

\begin{exa} 
It is easy to construct an example of a commutative twisted associative
deformation $\bsym{\mcal{A}}$ of $\mcal{O}_X$ that is really
twisted. Take an algebraic variety $X$ with nonzero cohomology
class $c \in \mrm{H}^2(X, \mcal{O}_X)$. 
Let $\bsym{U}$ be an affine open covering of $X$, and let
$\{ c_{i, j, k} \}$ be a \v{C}ech $2$-cocycle representing $c$
on this covering. Now consider the data
$\bigl( \{ \mcal{A}_i \}, \{ g_{i, j} \}, \{ a_{i, j, k} \} \bigr)$
with $\mcal{A}_i := \mcal{O}_{U_i}[[\hbar]]$, 
$g_{i, j} := \bsym{1}$ and
\[ a_{i, j, k} := \opn{exp}(\hbar c_{i, j, k}) . \]
This twisted deformation $\bsym{\mcal{A}}$ has obstruction
class $c$ in the first order central extension (in the sense of \cite{Ye6}).
This implies that $\bsym{\mcal{A}}$ is really twisted. 
\end{exa}

\begin{rem} \label{rem1}
For a twisted associative deformation $\bsym{\mcal{A}}$
there is a well defined abelian category 
$\cat{Coh} \bsym{\mcal{A}}$ of ``coherent left
$\bsym{\mcal{A}}$-modules'', which is a deformation of the 
abelian category $\cat{Coh} \mcal{O}_X$. See the work of Lowen and
Van den Bergh \cite{LV}.

Indeed, there is a
geometric Morita theory, which says that twisted associative
deformations of $\mcal{O}_X$ are the same as deformations of 
$\cat{Coh} \mcal{O}_X$. This is explained in the last chapter of the book
\cite{KS1} by Kashiwara and Schapira.

We do not know of a similar interpretation of twisted Poisson
deformations. 
\end{rem}

---
doc_id: arxiv-math-0505170v2
doc_title: "AN AVERAGING PROCESS FOR UNIPOTENT GROUP ACTIONS"
section_id: sec-000-0-introduction
section_title: "Introduction"
section_number: 0
pages: 1-2
source_pdf: math0505170.pdf
source_sha256: 0846b74f9c7c55cb
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.893
---
Let $\K$ be a field of characteristic $0$. For any natural number
$q$ let $\K [t_0, \ldots, t_q]$ be the polynomial algebra, and let
$\bsym{\Delta}^q_{\K}$ be the {\em geometric 
$q$-dimensional simplex}
\[ \bsym{\Delta}^q_{\K} := \opn{Spec}
\K [t_0, \ldots, t_q] / (t_0 + \cdots + t_q - 1) . \] 
Our main result is the following theorem. 

\begin{thm} \label{thm0.1}
Let $G$ be a unipotent algebraic group over 
$\K$, let $X$ be a $\K$-scheme, let $Z$ be a $G$-torsor over $X$, 
and let $Y$ be any $X$-scheme. Suppose
$\bsym{f} = (f_0, \ldots, f_q)$ is a sequence of $X$-morphisms
$f_i : Y \to Z$. Then there is an $X$-morphism
\[ \opn{wav}_G(\bsym{f}) : \bsym{\Delta}^q_{\K} \times Y \to Z  \]
called the {\em weighted average}, such that 
the operation $\opn{wav}_G$ is 
symmetric, simplicial, functorial in the data $(G, X, Y, Z)$, 
and is the identity for $q = 0$. 
\end{thm}

``Symmetric'' means that $\opn{wav}_G$ is equivariant for the 
action of the permutation group of $\{0, \ldots, q \}$ on the 
sequence $\bsym{f}$ and the scheme $\bsym{\Delta}^q_{\K}$.
``Simplicial'' says that as $q$ varies
\[ \opn{wav}_G : \opn{Hom}_X(Y, Z)^{q+1} \to
\opn{Hom}_X(\bsym{\Delta}^q_{\K} \times Y, Z) \]
is a map of simplicial sets. ``Functorial in the data 
$(G, X, Y, Z)$'' means that e.g.\ given a morphism 
$h : Z \to Z'$ of $G$-torsors over $X$, one has
\[ h \circ \opn{wav}_G(\bsym{f}) = \opn{wav}_G(h \circ \bsym{f}), 
\]
where $h \circ \bsym{f}$ is the sequence
$(h \circ f_0, \ldots, h \circ f_q)$. 
Theorem \ref{thm0.1} is repeated, in full detail, as 
Theorem \ref{thm5.1}. 

Observe that when we restrict the morphism 
$\opn{wav}_G(\bsym{f})$ to each of the vertices of 
$\bsym{\Delta}^q_{\K}$ we recover the original morphisms 
$f_0, \ldots, f_q$. This is due to the simplicial property of 
$\opn{wav}_G$. Thus $\opn{wav}_G(\bsym{f})$ interpolates 
between $f_0, \ldots, f_q$. This is illustrated in Figure 
\ref{fig1}.

Here is a naive corollary of Theorem \ref{thm0.1},
which can further explain the result. Let us 
write $G(\K)$ for the group of $\K$-rational points of $G$. 
By a {\em weight sequence} in $\K$ we mean a sequence 
$\bsym{w} = (w_0, \ldots, w_q)$ of elements of $\K$ such that
$\sum w_i = 1$. 

\begin{cor} \label{cor0.1}
Let $G$ be a unipotent group over $\K$.
Suppose $Z$ is a set with $G(\K)$-action which is transitive and 
has trivial stabilizers. Let 
$\bsym{z} = (z_0, \ldots, z_q)$ be a sequence of points in $Z$ and 
let $\bsym{w}$ be a weight sequence in $\K$. Then there is a 
point 
$\opn{wav}_{G, \bsym{w}}(\bsym{z}) \in Z$
called the weighted average. 
The operation $\opn{wav}_{G}$
is symmetric, functorial, simplicial, 
and is the identity for $q = 0$. 
\end{cor}

The corollary is proved in Section 1. The idea is of course to 
take $Y = X := \opn{Spec} \K$ in the theorem, and to note that 
$\bsym{w}$ is a $\K$-rational point of $\bsym{\Delta}^q_{\K}$. 

Another consequence of Theorem \ref{thm0.1} is a new proof of the 
fact that a unipotent group in characteristic $0$ is special. See 
Remark \ref{rem1.1}. (This observation is due to Reichstein.)

Theorem \ref{thm0.1} was discovered in the course of research on 
deformation quantization in algebraic geometry \cite{Ye}, in 
which we tried to apply ideas of Kontsevich \cite{Ko}
to the algebraic context. Here is a brief outline. Suppose $X$ is 
a smooth $n$-dimensional $\K$-scheme. The coordinate bundle of $X$ 
\cite{GK, Ko} is an infinite dimensional bundle $Z \to X$ which 
parameterizes formal coordinate systems on $X$. The bundle $Z$ is 
a torsor under an affine group scheme 
$\mrm{GL}_{n, \K} \ltimes G$, where $G$ is pro-unipotent. One is 
interested in sections of the quotient bundle 
$\bar{Z} := Z / \mrm{GL}_{n, \K}$. If we are in the 
differentiable setup (i.e.\ $\K = \mbb{R}$ and $X$ is a 
$\mrm{C}^{\infty}$ manifold) then the fibers of $\bar{Z}$ are 
contractible (since they are isomorphic to $G(\mbb{R})$), 
and therefore global $\mrm{C}^{\infty}$ sections exist. 
However in the setup of algebraic geometry such an argument is 
invalid, and we were forced to seek an alternative approach.

Our solution was to use {\em simplicial sections} of $\bar{Z}$
(see Section 2, and especially Corollary \ref{cor2.1}). This 
approach was inspired by work of Bott \cite{Bo} on simplicial 
connections (cf.\ also \cite{HY}). 



\medskip \noindent
\textbf{Acknowledgments.} 
The author thanks David Kazhdan and Zinovy Reichstein for useful 
conversations. Also thanks to the referee for reading the paper 
carefully and suggesting a few improvements.

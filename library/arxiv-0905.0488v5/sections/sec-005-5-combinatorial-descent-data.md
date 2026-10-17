---
doc_id: arxiv-0905.0488v5
doc_title: "TWISTED DEFORMATION QUANTIZATION OF ALGEBRAIC VARIETIES"
section_id: sec-005-5-combinatorial-descent-data
section_title: "Combinatorial Descent Data"
section_number: 5
pages: 25-28
source_pdf: 0905.0488v5.pdf
source_sha256: fcf8dee7cd3849b9
toc_source: outline
text_source: latex
latex_prose_ratio: 0.981
latex_coverage_ratio: 0.969
doc_brief: "TWISTED DEFORMATION QUANTIZATION OF ALGEBRAIC VARIETIES — Let X be a smooth algebraic variety over a ﬁeld K containing the real numbers. We introduce the notion of twisted associative (resp."
---
\label{sec:cosim}

We begin with a quick review of cosimplicial theory. 
Let $\bsym{\Delta}$ denote the simplex category. The set
of objects of $\bsym{\Delta}$ is the set $\mbb{N}$ of natural
numbers. Given $p, q \in \mbb{N}$, the morphisms $\alpha : p \to q$
in $\bsym{\Delta}$ are the order preserving functions
$\alpha : \{ 0, \ldots, p \} \to \{ 0, \ldots, q \}$.
We denote this set of morphisms by
$\bsym{\Delta}^q_p$.
An element of $\bsym{\Delta}^q_p$ may be thought of as a sequence
$\bsym{i} = (i_0, \ldots, i_p)$ of integers with
$0 \leq i_0 \leq \cdots \leq i_p \leq q$. 
We call 
$\bsym{\Delta}^q := \{ \bsym{\Delta}^q_p \}_{p \in \mbb{N}}$
the $q$-dimensional combinatorial simplex, and an element
$\bsym{i} \in \bsym{\Delta}^q_p$ is a $p$-dimensional face of
$\bsym{\Delta}^q$. 

Let $\cat{C}$ be some category. A {\em cosimplicial object} in 
$\cat{C}$ is a functor $C : \bsym{\Delta} \to \cat{C}$.
We shall usually write $C^p := C(p) \in \opn{Ob} (\cat{C})$, and leave
the morphisms
$C(\alpha) : C(p) \to C(q)$, for $\alpha \in \bsym{\Delta}^q_p$,
implicit. Thus we shall refer to the cosimplicial object $C$ as
$\{ C^p \}_{p \in \mbb{N}}$.
The category of cosimplicial objects in $\cat{C}$, where the morphisms 
are natural transformations of functors 
$\bsym{\Delta} \to \cat{C}$, is denoted by 
$\bsym{\Delta}(\cat{C})$.

If $\cat{C}$ is a category of sets with structure (i.e.\ there is a
faithful functor $\cat{C} \to \cat{Set}$), then an object 
$C \in \opn{Ob}(\cat{C})$ has elements $c \in C$. 
Let $\{ C^p \}_{p \in \mbb{N}}$ be a cosimplicial object of $\cat{C}$. 
Given a face $\bsym{i} \in \bsym{\Delta}_p^q$
and an element $c \in C^p$, it will be convenient to write
\begin{equation} \label{eqn:101}
c_{\bsym{i}} := C(\bsym{i})(c) \in C^q .
\end{equation}
The picture to keep in mind is of ``the element $c$ pushed to the face
$\bsym{i}$ of the simplex $\bsym{\Delta}^q$''. 
See Figure \ref{fig:2} for an illustration.

We shall be interested in cosimplicial crossed groupoids, i.e.\ in objects of
the category $\bsym{\Delta}(\cat{CrGrpd})$. A cosimplicial crossed groupoid 
$G = \{ G^p \}_{p \in \mbb{N}}$
has in each simplicial dimension $p$ a crossed groupoid $G^p$. 
The morphisms $G(\bsym{i}) : G^p \to G^q$, 
for $\bsym{i} \in \bsym{\Delta}_p^q$, are implicit, and we use notation
(\ref{eqn:101}). 

Let us fix $p \in \N$. Then for any 
$\om \in \opn{Ob}(G^p)$ there is a group homomorphism  (the feedback)
$\opn{D} : G^p_2(\om) \to  G^p_1(\om)$.
And for every morphism $g : \om \to \om'$ in $G_1^p$ there is a group
isomorphism (the twisting)
\[ \opn{Ad}_{G^p_1 \curvearrowright G^p_{2}}(g) :
G^p_2(\om) \to G^p_2(\om') . \]
We shall often use the abbreviated expression
$\opn{Ad}(g)$ to mean both $\opn{Ad}_{G^p_1 \curvearrowright G^p_{2}}(g)$
and 
$\opn{Ad}_{G^p_1}(g)$; hopefully that will not cause confusion.

\begin{dfn} \label{dfn:101}
Let $G = \{ G^p \}_{p \in \mbb{N}}$ be a cosimplicial
crossed groupoid. A {\em combinatorial descent datum} in $G$
is a triple $(\om, g, a)$ of elements of the following sorts:
\begin{enumerate}
\rmitem{0}  $\om \in \opn{Ob}(G^0)$. 

\rmitem{1} $g \in G^1_1(\om_{(0)}, \om_{(1)})$, where 
$\om_{(0)}, \om_{(1)} \in \opn{Ob}(G^1)$ are the objects corresponding
to the vertices $(0)$ and $(1)$ in $\bsym{\Delta}^1$.

\rmitem{2} $a \in G^2_2(\om_{(0)})$, where 
$\om_{(0)} \in \opn{Ob}(G^2)$ is the object corresponding
to the vertex $(0)$ of $\bsym{\Delta}^2$.
\end{enumerate}

The conditions are as follows:
\begin{enumerate}
\rmitem{i} (Failure of $1$-cocycle) 
\[ g_{(0, 2)}^{-1} \circ g_{(1, 2)} \circ g_{(0, 1)} = \opn{D}(a) \]
in the group $G^2_1(\om_{(0)})$.
Here $\om_{(i)} \in \opn{Ob}(G^2)$ 
and $g_{(i, j)} \in G^2_1(\om_{(i)}, \om_{(j)})$ 
correspond to the faces $(i)$ and $(i, j)$ respectively of $\bsym{\Delta}^2$.

\rmitem{ii} (Twisted $2$-cocycle) 
\[ a_{(0, 1, 3)}^{-1} \circ a_{(0, 2, 3)} \circ 
a_{(0, 1, 2)} = 
\opn{Ad}(g_{(0, 1)}^{-1})(a_{(1, 2, 3)}) \]
in the group
$G^3_2(\om_{(0)})$.
Here $\om_{(i)} \in \opn{Ob}(G^3)$, 
$g_{(i, j)} \in G^3_1(\om_{(i)}, \om_{(j)})$ and
$a_{(i, j, k)} \in G^3_2(\om_{(i)})$
correspond to the faces $(i)$,  $(i, j)$ and $(i, j, k)$ respectively of
$\bsym{\Delta}^3$.
\end{enumerate}

We denote by $\opn{Desc}(G)$ the set of all
descent data in $G$. 
\end{dfn}

See Figure \ref{fig:2} for an illustration.

\begin{figure}
\begin{center}
\includegraphics[scale=0.6]{fig-2.pdf}

\caption{Illustration of a combinatorial descent datum $(\om, g, a)$ in the
cosimplicial crossed groupoid 
$G = \{ G^p \}_{p \in \mbb{N}}$.}
\label{fig:2}
\end{center}
\end{figure}

\begin{dfn} \label{dfn:100}
Let $(\om, g, a)$ and $(\om', g', a')$
be combinatorial descent data in the cosimplicial crossed groupoid 
$G$. A gauge transformation
$(\om, g, a) \to (\om', g', a')$ is a pair $(f, b)$ 
of elements of the following sorts:
\begin{enumerate}
\rmitem{0}  $f \in G^0_1(\om, \om')$.

\rmitem{1} $b \in G^1_2(\om_{(0)})$, where 
$\om_{(0)} \in \opn{Ob}(G^1)$ is the object corresponding
to the vertex $(0)$ in $\bsym{\Delta}^1$.
\end{enumerate}

These two conditions must hold:
\begin{enumerate}
\rmitem{i}  
\[ g'  = f_{(1)} \circ g \circ \opn{D}(b) \circ f_{(0)}^{-1} \]
in the set
$G^1_1(\om'_{(0)}, \om'_{(1)})$.

\rmitem{ii}
\[ a' =   
\opn{Ad}(f_{(0)}) \Bigl( b_{(0, 2)}^{-1} \circ a \circ 
\opn{Ad}(g_{(0, 1)}^{-1})(b_{(1, 2)}) \circ b_{(0, 1)} \Bigr) \]
in the group $G^2_2(\om'_{(0)})$.
\end{enumerate}
\end{dfn}

This is illustrated in Figure \ref{fig:3}.

\begin{figure}
\begin{center}
\includegraphics[scale=0.55]{fig-3.pdf}

\caption{Illustration of a gauge transformation 
$(f, b) : (\om, g, a) \to (\om', g', a')$
between descent data.}
\label{fig:3}
\end{center}
\end{figure}

The gauge transformations form an equivalence relation on the set
$\opn{Desc}(G)$; see \cite[Proposition 1.6]{Ye8}.
We call this relation {\em gauge equivalence}.

Let $\Phi : G \to H$ be a morphism of cosimplicial
crossed groupoids, i.e.\ a morphism in $\bsym{\Delta}(\cat{CrGrpd})$. 
Given a descent datum 
$(\om, g, a) \in \opn{Desc}(G)$, the triple 
$\Phi(\om, g, a) := (\Phi(\om), \Phi(g), \Phi(a))$
is a descent datum in $H$. The resulting function 
$\opn{Desc}(\Phi) : \opn{Desc}(G) \to \opn{Desc}(H)$
respects the gauge equivalence relations. 

\begin{dfn} \label{dfn:cosim.1}
For a cosimplicial crossed groupoid $G$ we write
\[ \ol{\opn{Desc}}(G) :=
\frac{ \opn{Desc}(G) } {\tup{ gauge equivalence}} . \]
For a morphism $\Phi : G \to H$
of cosimplicial crossed groupoids, we denote by 
\[ \ol{\opn{Desc}}(\Phi) : \ol{\opn{Desc}}(G) \to
\ol{\opn{Desc}}(H) \]
the induced function. 
\end{dfn}

\begin{dfn} \label{dfn:equiv-cosim.103}
A morphism $\Phi : G \to H$
of cosimplicial crossed groupoids is called a {\em weak equivalence} if in
every simplicial dimension $p$ the morphism of crossed groupoids
 $\Phi^p : G^p \to H^p$ is a weak equivalence (Definition
\ref{dfn:equiv-cosim.102}).
\end{dfn}

The next result is proved in the companion paper \cite{Ye8}.
An alternative proof (of a more general statement) can be found in M. Prasma's
paper \cite{Pr}. 

\begin{thm}[{Combinatorial Equivalence, \cite[Theorem 0.1]{Ye8}}]
\label{thm:100} 
Let $\Phi : G \to H$ be a weak equivalence between 
cosimplicial crossed groupoids. Then the function 
\[ \ol{\opn{Desc}}(\Phi) : \ol{\opn{Desc}}(G) \to
\ol{\opn{Desc}}(H) \]
from Definition \tup{\ref{dfn:cosim.1}} is bijective.
\end{thm}

\begin{rem} \label{rem:cosim.106}
If  we view the cosimplicial crossed groupoid as a cosimplicial simplicial set,
then the set of descent data  $\opn{Desc}(G)$ becomes the {\em total space} of
$G$. See \cite{BGNT2} and \cite{Pr}.

We discovered Theorem \ref{thm:100} while trying to understand, and possibly
improve, \cite[Proposition 3.3.1]{BGNT1} and the ideas in \cite{CH}. 
The precise relation to \cite[Proposition 3.3.1]{BGNT1} is explained in Remark
\ref{rem:Lie-desc.101}. As for \cite{CH}: there seems to be an implicit
assumption there that the nerve $\opn{N}(G)$ is a Reedy fibrant
cosimplicial simplicial set. This might not be true -- see \cite{Pr}.
\end{rem}

---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology"
section_id: sec-061-115-jsj-decomposition
section_title: "JSJ decomposition"
section_number: 11.5
pages: 372-377
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.735
latex_coverage_ratio: 0.986
doc_brief: "An Introduction to Geometric Topology — 86 sections: Front matter; Introduction; Part 1. Hyperbolic geometry"
---
In Chapter \ref{Three:topology:chapter} we cut every closed three-manifold along spheres, and it is now time to decompose it further along tori. 
This two-steps cutting operation is called the \emph{JSJ decomposition} of the manifold, after the names of Jaco, Shalen, and Johansson who discovered it in the mid 1970s.\index{JSJ decomposition}

The core of this decomposition is the existence of a canonical set of disjoint essential tori, unique up to isotopy. 


\subsection{Canonical torus decomposition}
Let $M$ be an orientable irreducible and $\partial$-irreducible compact 3-manifold with (possibly empty) boundary consisting of tori. How can we define a canonical set of disjoint essential tori in $M$? The answer is not obvious: for instance, if $M$ is a Seifert manifold, it may contain many vertical incompressible tori and there is no canonical way to choose among them.

We will soon see that the Seifert manifolds are in fact the only possible source of ambiguity. Let
$$S=T_1\sqcup \cdots \sqcup T_k$$ 
be a set of disjoint essential tori $T_i\subset \interior M$. 
We say that $S$ is a \emph{torus decomposition} of $M$ if it decomposes $M$ into blocks that are either:\index{torus decomposition} 
\begin{itemize}
\item torus (semi-)bundles,
\item Seifert manifolds, or
\item simple manifolds.
\end{itemize}

A torus decomposition is \emph{minimal} if no proper subset of $S$ is a torus decomposition. We prove here the following.

\begin{teo}[JSJ decomposition] \label{JSJ:teo}
Let  $M$ be an orientable irreducible and $\partial$-irreducible compact 3-manifold with (possibly empty) boundary consisting of tori. A minimal torus decomposition for $M$ exists and is unique up to isotopy.
\end{teo}

Such a minimal decomposition is called the \emph{canonical torus decomposition} or the \emph{JSJ decomposition} of $M$. The canonical torus decomposition may be empty: this holds precisely when $M$ is itself a torus (semi-)bundle, Seifert, or simple.

\begin{oss}
Torus (semi-)bundles are closed: therefore if $M$ is not itself a torus (semi-)bundle, the blocks of its canonical decomposition are either Seifert or simple.
\end{oss}


\subsection{Existence and uniqueness}
Let  $M$ be an orientable irreducible and $\partial$-irreducible compact 3-manifold with (possibly empty) boundary consisting of tori. We now prove Theorem \ref{JSJ:teo}. Let us start by showing existence.
\begin{prop}
The manifold $M$ has a torus decomposition.
\end{prop}
\begin{proof}
Let $T_1,\ldots, T_k$ be a maximal set of disjoint non-parallel essential tori in $M$, which exists by Corollary \ref{incompressible:cor}. We now prove that $S=T_1 \sqcup \cdots \sqcup T_k$ is a torus decomposition.

Suppose it is not: one block $N$ of the decomposition is neither a (semi-)bundle, nor Seifert, nor simple. The block $N$ is irreducible and $\partial$-irreducible since these properties are preserved after cutting along incompressible surfaces. Being not simple, it contains an essential annulus $A$ or an essential torus $T$. 

In the latter case we can add $T$ to the family $T_1,\ldots, T_k$ and get a contradiction since $S$ is maximal. In the former case Lemma \ref{only:annuli:lemma} applies and $N$ is Seifert.
\end{proof}

Since $M$ has a torus decomposition, it certainly has a minimal one. We now prove that it is unique.

\begin{prop} \label{minimal:torus:unique:prop}
The manifold $M$ has a unique minimal torus decomposition up to isotopy.
\end{prop}
\begin{proof}
Let $S = T_1\sqcup \cdots \sqcup T_k$ and $S' = T_1' \sqcup \cdots \sqcup T_{k'}'$ be two minimal torus decompositions for $M$. We minimise their transverse intersections, so that $S\cap S'$ consists of essential circles cutting some tori into annuli. 

Let $T_i'$ be decomposed into some annuli. 
Each such annulus is essential in $M\setminus S$, hence it is contained in some non-simple block, \emph{i.e.}~a Seifert one. It is contained there horizontally or vertically: in the former case, the block is $\big(D, (2,1), (2,1) \big)$, $S_*\timtil S^1$, or $A\times S^1$ with $S_*$ the M\"obius strip. The first two blocks are diffeomorphic, and by swapping the fibration the annulus becomes vertical. The third block $T\times I$ is excluded since $S$ is minimal.

Now all annuli in $T_i'$ are vertical. Two consequent vertical annuli are separated by some torus $T_j$; since the two annuli are fibered, the fibers of the two Seifert blocks incident to $T_j$ are isotopic: hence the two blocks glue to a bigger Seifert block and $T_j$ can be removed, a contradiction since $S$ is minimal.

We have shown that $S\cap S' = \emptyset$. If $T_i$ is parallel to $T_j'$ we superpose the two tori, cut $M$ along $T_i=T_j'$ and proceed by induction. Now we suppose by contradiction that there is no parallelism.

Every $T_i'$ is an essential vertical torus in a Seifert block of $M\setminus S$, and vice versa. This easily implies that all the blocks in $M\setminus S$, $M\setminus S'$, and all their intersections are Seifert! Pick one such intersection. It has a unique Seifert fibration, unless it is $K\timtil I$ which may fiber in two ways. Since $\partial (K\timtil I)$ is connected, one block is $K\timtil I$ itself and we change the fibration on this block if necessary. Now all intersections and all blocks have unique fibrations and they all glue to a Seifert fibration for $M$, a contradiction.
\end{proof}

The proof of Theorem \ref{JSJ:teo} is complete.

\begin{oss}
The sphere decomposition of Theorem \ref{prime:teo} and the torus decomposition of Theorem \ref{JSJ:teo} differ in two aspects: (i) the set of decomposing spheres is \emph{not} canonical up to isotopy, while the set of tori is; (ii) on the other hand, after cutting along the spheres and capping off we get a canonical set of prime manifolds, whereas if we cut along the tori we get some canonical manifolds with toric boundaries, but there is no canonical way to cap them off. 
\end{oss}


\subsection{Geometric decomposition} \label{geometric:decomposition:subsection}
The \emph{geometric decomposition} is a slight variation of the canonical torus decomposition that is more suited to the geometrisation perspective that we will encounter in the next chapters. It is constructed from the canonical torus decomposition $S$ for $M$ as follows. Whenever a block $N$ of the torus decomposition is diffeomorphic to $K\timtil I$,  
we substitute the torus $\partial N$ in $S$ with the core Klein bottle $K$ of $K\timtil I$. This substitution has the effect of deleting $N$ from the list of blocks of the decomposition.\index{geometric decomposition}

The geometric decomposition consists of incompressible tori and Klein bottles. One reason for preferring the geometric decomposition to the canonical torus one is that it contains no interval bundles and every Seifert block has a unique fibration up to isotopy (because we have eliminated the $K\timtil I$ blocks). In particular we get the following easy criterion, whose proof is straightforward. 
\begin{prop} \label{criterion:geometric:prop}
Let  $M$ be an orientable irreducible and $\partial$-irreducible compact 3-manifold with (possibly empty) boundary consisting of tori. 
A non-empty torus decomposition of $M$ is the geometric one if and only if:
\begin{itemize}
\item every block is simple or Seifert with $\chi<0$,
\item the fibrations of two adjacent Seifert blocks do not match.
\end{itemize}
\end{prop}

Another reason for preferring the geometric decomposition is that every Seifert block can be geometrised with finite volume, whereas $K\timtil I$ needs infinite volume (this will be shown in the next chapter). 

Geometric decompositions also behave well under finite coverings. Let $\tilde M \to M$ be a finite covering between two orientable irreducible and $\partial$-irreducible compact 3-manifolds with (possibly empty) boundary consisting of tori. 

\begin{prop} \label{JSJ:lifts:prop}
The geometric decomposition of $\tilde M$ is the counterimage of that of $M$.
\end{prop}
\begin{proof}
The criterion of Proposition \ref{criterion:geometric:prop} lifts from $M$ to $\tilde M$.
\end{proof}


\subsection{Graph manifolds}
Waldhausen introduced in the 1960s a simple but non-trivial class of three-manifolds using only two blocks. Here $D$ and $P$ are the disc and the pair-of-pants.

\begin{defn}
A \emph{graph manifold} is any orientable three-manifold that decomposes along disjoint tori into pieces diffeomorphic to $D\times S^1$ or $P\times S^1$.\index{graph manifold}
\end{defn}

One may describe any such manifold via a graph with vertices of valence 1 and 3 representing the blocks, and some appropriate $2\times 2$-matrices labelling the edges telling the way the two incident blocks are glued. As usual, different graphs may represent the same manifold. 

\begin{ex}
Let $M$ be an orientable three-manifold. The following are equivalent:
\begin{enumerate}
\item $M$ is a graph manifold,
\item $M=M_1\#\ldots \#M_h$ for some prime manifolds $M_i$ whose geometric decompositions consist of Seifert manifolds or torus (semi-)bundles.
\end{enumerate} 
\end{ex}
\begin{proof}[Hint]
Use Corollary~\ref{DF:Seifert:cor} and Proposition \ref{criterion:geometric:prop}. 
\end{proof}


\subsection{References}
Most of the arguments contained in this chapter are well-known to three-dimensional topologists and can be found in many books. A standard introduction to knots and links is Rolfsen \cite{Ro}, and much more on Dehn surgeries and their four-dimensional interpretations is contained in Gompf -- Stipsicz \cite{GS}. A proof of the JSJ decomposition can be found in Hatcher \cite{H}, the original papers of Jaco -- Shalen and Johannson are \cite{JS} and \cite{Jo}. Fomenko -- Matveev \cite{FM} contains a chapter devoted to graph manifolds; the original paper of Waldhausen is \cite{Wa}.


\chapter{The eight geometries} \label{eight:chapter}
We have concluded the previous chapter by defining a \emph{geometric decomposition} of three-manifolds along sphere and tori. The reason for using this terminology is the famous \emph{geometrisation conjecture}, proposed by Thurston in 1982 and proved by Perelman in 2003, which states that each of the blocks of the decomposition should be \emph{geometric}, in the sense that it may be equipped with a nice Riemannian metric.

There are eight nice Riemannian metrics available in dimension three. Three of them are the constant curvature ones (hyperbolic, elliptic, and flat), while the other five are some kind of (sometimes twisted) products of low-dimensional geometries. All these metrics are \emph{homogeneous}: distinct points have isometric neighbourhoods.

The Seifert manifolds studied in the previous chapters occupy precisely six of these eight geometries, and we analyse them in detail here.


\section{Introduction}
A connected Riemannian manifold $M$ is \emph{homogeneous} if for every $p,q\in M$ there is an isometry of $M$ sending $p$ to $q$, and is \emph{isotropic} if at each point $p$ every isometry of $T_pM$ is realised by an isometry of $M$. It is easy to prove that a complete isotropic manifold is also homogeneous and has constant sectional curvature: the fundamental examples of isotropic spaces are $S^n$, $\matR^n$, and $\matH^n$.\index{manifold!Riemannian manifold!homogeneous Riemannian manifold}\index{manifold!Riemannian manifold!isotropic Riemannian manifold}

The homogeneous condition alone (without isotropy) is more relaxed and produces manifolds that may not have constant sectional curvature.
We introduce in this chapter eight important homogeneous simply-connected complete Riemannian 3-manifolds:
$$S^3,\ \matR^3,\ \matH^3,\ S^2\times \matR,\ \matH^2\times \matR,\ \Nil,\ \Sol,\ \widetilde{\SL_2}.$$
The first three manifolds are also isotropic and have constant sectional curvature, the other five are not. 

Let $M$ be one of these eight model manifolds. We say that a Riemannian 3-manifold $N$ has a \emph{geometric structure modelled on $M$} if $N$ is locally isometric to $M$, that is if every point $p\in N$ has an open neighbourhood isometric to some open set in $M$. This implies that $N$ is \emph{locally homogeneous}: every two points $p,q\in N$ have isometric neighbourhoods $U(p) \isom U(q)$, both isometric to an $\varepsilon$-ball at any point of $M$.

If $N$ is complete, the developing map construction of Theorem \ref{simply:teo} applies also in this context and shows that $N = M/_\Gamma$ for some discrete group $\Gamma <\Iso(M)$ acting freely. \index{geometric structure}

\begin{table}
\begin{center}
\begin{tabular}{c||ccc}
       & \phantom{\Big|} $\chi>0$ & $\chi = 0$ & $\chi<0$ \\
 \hline \hline
 $e=0$ & \phantom{\Big|} $S^2 \times \matR$ & $\matR^3$ & $\matH^2 \times \matR$ \\
 $e\neq 0$ & \phantom{\big|} $S^3$ & $\Nil$ & $\widetilde {\SL_2}$
\end{tabular}
\vspace{.2 cm}
\nota{The closed manifolds modelled on six geometries are precisely the six commensurable classes of Seifert manifolds, distinguished by the numbers $e$ and $\chi$.}
\label{Seifert:geometry:table}
\end{center}
\end{table}

We now start a long journey through these eight geometries. The final goal of this chapter is to prove the following.

\begin{teo} \label{Seifert:geometrisation:teo}
A closed orientable 3-manifold has a geometric structure modelled on one of the following six geometries:
$$S^3,\ \matR^3,\ S^2\times \matR,\ \matH^2\times \matR,\ \Nil,\ \widetilde{\SL_2}$$
if and only if it is a Seifert manifold of the appropriate commensurability class, as prescribed by Table \ref{Seifert:geometry:table}. It has a $\Sol$ geometric structure if and only if it is a torus (semi-)bundle of Anosov type.
\end{teo}

It is a surprising (and maybe disappointing) fact that, despite its elegance and generality, the only known proof of this theorem available today works by investigating each geometry separately and carefully, often employing quite different techniques. We start with the elliptic case.

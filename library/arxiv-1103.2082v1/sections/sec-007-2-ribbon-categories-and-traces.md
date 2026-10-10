---
doc_id: arxiv-1103.2082v1
doc_title: "MODIFIED TRACES ON DELIGNE’S CATEGORY Rep(St)"
section_id: sec-007-2-ribbon-categories-and-traces
section_title: "Ribbon Categories and Traces"
section_number: 2
pages: 3-5
source_pdf: 1103.2082v1.pdf
source_sha256: 0ac5371486b38eac
text_source: latex
latex_prose_ratio: 0.664
latex_coverage_ratio: 0.964
doc_brief: "MODIFIED TRACES ON DELIGNE’S CATEGORY Rep(St) — Deligne has deﬁned a category which interpolates among the representations of the various symmetric groups."
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

\subsection{Ideals in $\cat$}\label{SS:ideals} There are two closely related notions of an ideal within a ribbon category.  The first we discuss is used in \cite{GKP} and defined via objects.  We discuss the second notion in Section~\ref{SS:homideals}.   Note that here and elsewhere if $f$ and $g$ are morphisms, then we write $fg$ for the composition $f \circ g$.

\begin{definition}\label{D:ideal} We say a full subcategory $\ideal$ of a ribbon category $\cat$ is an \emph{ideal} if the following two conditions are met:
\begin{enumerate}
\item  If $V$ is an object of $\ideal$ and $W$ is any object of $\cat$, then $V\otimes W$ is an object of $\ideal$.
\item  $\ideal$ is closed under retracts; that is, if $V$ is an object of $\ideal$, $W$ an object of $\cat$, and if there exists morphisms $f:W \rightarrow V$, $g:V\rightarrow W$ such that $gf=\Id_W$, then $W$ is an object of $\ideal$.
\end{enumerate}
\end{definition} Trivially, if $\ideal$ consists of just the zero object or $\ideal = \cat$, then $\ideal$ is an ideal of the category.  We say an ideal $\ideal$ is a \emph{proper} ideal if it contains a nonzero object and is not all of $\cat$.


\subsection{Traces in Ribbon Categories}\label{SS:traces} For any objects $V,W$ of $\cat$ and $f \in \End_{\cat}( V \otimes W)$, set
\begin{equation}\label{E:trL}
\tr_{L}(f)=(\ev_{V}\otimes \Id_{W})(\Id_{V^{*}}\otimes
f)(\coev'_{V}\otimes \Id_{W}) \in \End_{\cat}(W),
\end{equation} and
\begin{equation}\label{E:trR}
\tr_{R}(f)=(\Id_{V}\otimes \ev'_{W})  (f \otimes \Id_{W^{*}})
(\Id_{V}\otimes \coev _{W}) \in \End_{\cat}(V).
\end{equation}


\begin{definition}\label{D:trace}  If $\ideal$ is an ideal in $\cat$, then a \emph{trace on $\ideal$} is a family of linear functions
$$\mt = \{\mt_V:\End_\cat(V)\rightarrow K\}$$
where $V$ runs over all objects of $\ideal$ and such that following two conditions hold:
\begin{enumerate}
\item  If $U\in \ideal$ and $W\in \ob$ then for any $f\in \End_\cat(U\otimes W)$ we have
\begin{equation}\label{E:VW}
\mt_{U\otimes W}\left(f \right)=\mt_U \left( \tr_R(f)\right).
\end{equation}
\item  If $U,V\in \ideal$ then for any morphisms $f:V\rightarrow U $ and $g:U\rightarrow V$  in $\cat$ we have 
\begin{equation}\label{E:fggf}
\mt_V(g f)=\mt_U(f  g).
\end{equation} 
\end{enumerate}
\end{definition}
Using the trace on $\ideal$ introduced above, we define a modified
dimension function on objects in $\ideal$.  Namely, we define the \emph{modified dimension function} 
\[
\md_{\mt}: \operatorname{Ob}(\ideal ) \to  K
\] by the formula 
\[
\md_{\mt} (V) = \mt_{V}\left(\Id_{V} \right).
\]



\begin{example}\label{X:categoricaltrace}
If $\cat$ is a ribbon category, then $\cat$ itself is an ideal and the well known \emph{categorical trace} function
\[
\tr_{\cat}: \End_{\cat}(V) \to  K
\] given by 
\[
\tr_{\cat}(f) = \ev'_{V}  (f \otimes 1)  \coev_{V}
\] defines a trace on $\cat$.  The modified dimension function then coincides with the familiar \emph{categorical dimension} function.
\end{example}

The following theorem from \cite{GKP} gives a convenient way of creating ideals with traces.  Assume that $J$ in $\cat$ admits a linear map 
\[
\mt_{J}: \End_{\cat}(J) \to K
\] which satisfies 
\begin{equation*}
\mt_{J}\left( \tr_{L}(h) \right) = \mt_{J} \left( \tr_{R}(h)\right),
\end{equation*} for all $h \in \End_{\cat}(J\otimes J)$. 
Such a linear map is called an \emph{ambidextrous trace on $J$}. 

For an object $J$, let $\ideal_{J}$ denote the ideal whose objects are all objects which are retracts of $J \otimes X$ for some $X$ in $\cat$.
\begin{theorem}\label{T:ambitrace} If $J$ is an object of $\cat$ which admits an
  ambidextrous trace, then there is a unique trace on $\ideal_{J}$ determined
  by that ambidextrous trace.
\end{theorem} 


\subsection{Tensor Ideals in a Ribbon Category}\label{SS:homideals}
A somewhat different notion of ideal is used in \cite{CO1, CO2}.  As we need both, we define it here and discuss the relationship with the earlier definition.  To distinguish the two we call these tensor ideals.  They are defined via morphisms as follows.

\begin{definition}\label{D:Homideal}  A \emph{tensor ideal}, $J$, of $\cat$ is a family of subspaces 
\[
J(X,Y) \subseteq \Hom_{\cat}(X,Y)
\] for all pairs of objects $X,Y$ in $\cat$ subject to the following two conditions:
\begin{enumerate}
\item $ghk \in I(X,W)$ for each $k \in \Hom_{\cat}(X,Y)$, $h \in  J(Y,Z)$, and $g \in \Hom_{\cat}(Z,W)$.
\item $g\otimes \Id_{Z} \in J(X\otimes Z, Y\otimes Z)$ for every object $Z$ and every $g \in J(X,Y)$. 
\end{enumerate}
\end{definition} Trivially, for every pair of objects $X$ and $Y$ one can take $J(X,Y) =0$ and obtain a tensor ideal; similarly, for every pair of objects one can take $J(X,Y) = \Hom_{\cat}(X,Y)$.  A tensor ideal $J$ is called \emph{proper} if $J(X,Y)$ is a proper nonzero subspace of $\Hom_{\cat}(X,Y)$ for at least one pair of objects $X$ and $Y$ in $\cat$.

\subsection{}  If $\ideal$ is an ideal of $\cat$ in the sense of Definition~\ref{D:ideal}, then one can define subspaces 
\[
J(X,Y) = \left\{f \in \Hom_{\cat}(X,Y) \mid \text{there exists $Z$ in $\ideal$,  $g: X \to Z$, $h:Z \to Y$ so that $f=hg$} \right\}.
\]  Then $J$ forms a tensor ideal and we write $J(\ideal)$ for this tensor ideal.

Conversely, if $J$ is a tensor ideal, then one can define $\ideal$ to be the full subcategory consisting of 
all objects $V$ in $\cat$ such that $\Id_{V} \in J(V,V)$.  This is an ideal of $\cat$  and we write $\ideal (J)$ for this ideal.  

In the following lemma we record the basic properties relating these two notions of an ideal.  The proofs are elementary arguments using the definitions and previous parts of the lemma.

\begin{lemma}\label{L:ideals}  Let $\cat$ be a ribbon category.
\begin{enumerate}
\item If $\ideal$ is an ideal of $\cat$, then $\ideal = \ideal(J(\ideal))$.
\item If $J$ is a tensor ideal of $\cat$, then $J(\ideal(J)) \subseteq J$.  That is, 
\[
 J(\ideal(J))(X,Y) \subseteq J(X,Y) 
\]
for all pairs of objects $X,Y$.
\item The ideal $\ideal$ is the zero ideal if and only if $J(\ideal )$ is the zero tensor ideal.
\item The ideal $\ideal$ is the entire category $\cat$ if and only if 
\[
J(\ideal)(X,Y)=\Hom_{\cat}(X,Y)
\]
for all pairs of objects $X,Y$ in $\cat$. 
\item If $\cat$ has a unique proper tensor ideal, say $J$, and $\ideal$ is a proper ideal of $\cat$, then $\ideal$ is the unique proper ideal and $\ideal = \ideal (J)$.
\end{enumerate}
\end{lemma}  


\subsection{} A fundamental example of a tensor ideal is the so-called negligible morphisms.  Namely, let $\cat$ be a ribbon category and call a morphism $g: X \to Y$ \emph{negligible} if for all $h \in \Hom_{\cat}(Y,X)$, one has 
\[
\tr_{\cat}(gh) =0,
\] where $\tr_{\cat}$ denotes the categorical trace.  Setting $\mN(X,Y)$ to be the subspace of $\Hom_{\cat}(X,Y)$ of all negligible morphisms, one can check that $\mN$ is a tensor ideal. For short we call an object \emph{negligible} if it is an object in $\ideal (\mN )$.

When $t \in \Z_{\geq 0}$, $\mN$ is a proper tensor ideal of Deligne's category $\uRep(S_{t})$.  The quotient of $\uRep (S_{t})$ by this tensor ideal is equivalent to the category of finite dimensional representations over $F$ of the symmetric group $S_{t}$ (see \cite[Theorem 3.24]{CO1}).  It is in this sense that Deligne's category interpolates among the representations of the various symmetric groups.

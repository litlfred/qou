---
doc_id: arxiv-0905.0488v5
doc_title: "TWISTED DEFORMATION QUANTIZATION OF ALGEBRAIC VARIETIES"
section_id: sec-000-0-introduction
section_title: "Introduction"
section_number: 0
pages: 1-11
source_pdf: 0905.0488v5.pdf
source_sha256: fcf8dee7cd3849b9
toc_source: outline
text_source: latex
latex_prose_ratio: 0.995
latex_coverage_ratio: 0.972
doc_brief: "TWISTED DEFORMATION QUANTIZATION OF ALGEBRAIC VARIETIES — Let X be a smooth algebraic variety over a ﬁeld K containing the real numbers. We introduce the notion of twisted associative (resp."
---
\label{sec:Int}
\numberwithin{equation}{subsection}


\subsection{Deformation Quantization}
Let $\K$ be a field of characteristic $0$, and let $X$ be a
smooth algebraic variety over $\K$, with structure sheaf
$\mcal{O}_X$. Suppose $R$ is a {\em parameter algebra} over $\K$;
namely $R$ is a complete local noetherian commutative 
$\K$-algebra, with maximal ideal $\m$ and residue field $R / \m = \K$. 
The main example is $R = \K[[\hbar]]$, the formal power series ring in the
variable $\hbar$. An {\em associative $R$-deformation of $\mcal{O}_X$} is a
sheaf $\mcal{A}$ of flat $\m$-adically complete associative $R$-algebras on $X$,
with an isomorphism 
$\psi : \K \otimes_R \mcal{A} \iso \mcal{O}_X$, called an
augmentation. Similarly, a {\em Poisson $R$-deformation of $\mcal{O}_X$} is a
sheaf $\mcal{A}$ of flat $\m$-adically complete commutative Poisson $R$-algebras
on $X$, with an augmentation to $\mcal{O}_X$. 

Such deformations could be sheaf-theoretically trivial, meaning that
$\mcal{A} \cong$ \lb $R \hot \mcal{O}_X$, endowed
with either an associative multiplication (called a star product), or
a Poisson bracket. This is what happens in the differentiable setup
(i.e.\ when $X$ is a $\mrm{C}^{\infty}$ manifold and $\K = \R$). But in the
algebro-geometric setup the sheaf $\mcal{A}$ could be very complicated
-- indeed, all classical commutative deformations of $\mcal{O}_X$ are
special cases of both associative and Poisson deformations. 

Suppose $\mcal{A}$ and $\mcal{A}'$ are two $R$-deformations (of the same kind,
namely both are Poisson or associative). A {\em gauge transformation} 
$g : \mcal{A} \to \mcal{A}'$ is an isomorphism of sheaves of $R$-algebras
(Poisson or associative) that commutes with the augmentations to $\mcal{O}_X$.
If such a gauge transformation exists, then $\mcal{A}$ and $\mcal{A}'$ are said
to be {\em gauge equivalent}.

An $R$-deformation $\mcal{A}$ of $\mcal{O}_X$ determines a {\em first order
bracket} $\{ -,- \}_{\mcal{A}}$ on $\mcal{O}_X$. 
When $R = \K[[\hbar]]$ this is the usual induced Poisson bracket,
cf.\ \cite{Ye1}. For general $R$ see Definition \ref{dfn:20}.
It is important to note that the  first order bracket $\{ -,- \}_{\mcal{A}}$
is gauge invariant. 

\begin{exa} \label{exa:23}
Suppose $\{ -,- \}$ is a Poisson bracket on $\mcal{O}_X$. Consider the
commutative $\K[[\hbar]]$-algebra 
$\mcal{A} := \mcal{O}_X[[\hbar]] = \K[[\hbar]] \hot \OO_X$, endowed
with the Poisson bracket $\hbar \{ -,- \}$ and the obvious augmentation to 
$\mcal{O}_X$. We get a Poisson $\K[[\hbar]]$-deformation of $\mcal{O}_X$, and
the first order bracket is 
$\{ -,- \}_{\mcal{A}} = \{ -,- \}$.
\end{exa}

Let $\mcal{A}$ be a Poisson $R$-deformation of $\mcal{O}_X$.
A {\em deformation quantization} of $\mcal{A}$ is an associative
$R$-deformation $\mcal{B} = \opn{quant}(\mcal{A})$, such that 
$\{ -,- \}_{\mcal{B}}  = \{ -,- \}_{\mcal{A}}$.

In the fundamental paper \cite{Ko1}, M. Kontsevich proved that in the
$\mrm{C}^{\infty}$ setup, and for $R = \R[[\hbar]]$, every Poisson
$\R[[\hbar]]$-deformation $\mcal{A}$ can be quantized.
Moreover, Kontsevich proved that his  quantization  is canonical, 
and it induces a bijection between the set of gauge
equivalence classes of Poisson deformations, and the set of gauge
equivalence classes of associative deformations.
 
We proved an analogous result for {\em affine smooth
algebraic varieties} over a field $\K$ containing $\R$.
The method used in our paper \cite{Ye1}
was an adaptation of the ideas of Kontsevich from \cite{Ko1} to the
algebro-geometric setup. There were cohomological obstructions, indicating that 
the same result (namely \cite[Theorem 0.1]{Ye1}) would not hold for more
complicated smooth algebraic varieties. 


\subsection{Twisted Quantization: Overview}
In the paper \cite{Ko2}, Kontsevich suggested that on {\em any smooth algebraic
variety} $X$, every Poisson $R$-deformation $\mcal{A}$ of $\mcal{O}_X$ can be
quantized to a {\em stack of $R$-algebroids} $\gerbe{B}$ on $X$. 

The purpose of the present paper is more than just to provide a proof
of that assertion of Konstevich. 
We introduce the notions of {\em twisted Poisson $R$-deformation} and 
{\em twisted associative $R$-deformation} of $\mcal{O}_X$. 
These are stacky versions of the $R$-deformations discussed above. A 
twisted associative $R$-deformation is a refined variant of the {\em stack
of $R$-linear algebroids} from \cite{Ko2}, and is very similar to
the notion of {\em DQ algebroid} from \cite{KS2}. 
The concept of twisted Poisson deformation appears to be totally new (in
algebraic geometry, as well as in real differential and complex analytic
geometry). 

Our main result (the Twisted Quantization Theorem, number \ref{thm:14} below)
establishes a {\em twisted quantization} operation,
which is a canonical bijection between the set of twisted gauge equivalence
classes of twisted Poisson $R$-deformations of $\mcal{O}_X$, and the set of
twisted gauge equivalence classes of twisted associative $R$-deformations.
The proof of Theorem \ref{thm:14} requires many
intermediate results (in ring theory, algebraic geometry, cosimplicial
groupoids and $\mrm{L}_{\infty}$ morphisms), some of them of
independent interest. We present a few of these intermediate results below in
the Introduction. 
The Twisted Quantization Theorem raises a few questions that we find
intriguing; see end of Section \ref{sec:TDQ}.

We should mention that the first occurrence of twisted quantization was in
the paper \cite{Ka} of M. Kashiwara from 1996, that concerned contact 
manifolds. We discuss this work, and several other papers related to twisted
deformations, in Subsection \ref{subsec:discuss}. 



\subsection{Twisted Deformations} \label{subsec:tw.defs}
Let us now explain what are twisted deformations. 

We shall start with the concept of {\em crossed groupoid} (also known as a
crossed module over a groupoid, or a strict $2$-groupoid, cf.\ \cite{Ye7, Bw}).
This is a structure 
$\cat{P} = ( \cat{P}_1, \cat{P}_2, 
\opn{Ad}_{\cat{P}_1 \crvar \cat{P}_{2}}, \opn{D} )$
consisting of groupoids $\cat{P}_1$ and $\cat{P}_{2}$, such that 
$\opn{Ob}(\cat{P}_1) = \opn{Ob}(\cat{P}_2)$ and $\cat{P}_2$ is totally
disconnected; an action $\opn{Ad}_{\cat{P}_1 \crvar \cat{P}_{2}}$ of 
$\cat{P}_1$ on $\cat{P}_{2}$ called the {\em twisting}; and a morphism of
groupoids  (i.e.\  a functor) $\opn{D} : \cat{P}_{2} \to \cat{P}_{1}$ called the
{\em feedback}. There are conditions relating the twisting and the feedback; see
Definition \ref{dfn:cosim.101} for more details. 
We refer to the morphisms in the groupoid $\cat{P}_1$ as {\em $1$-morphisms}
of $\cat{P}$, or as {\em gauge transformations}. The morphisms in
$\cat{P}_2$ are called {\em $2$-morphisms}, or {\em inner gauge
transformations}. There is an obvious notion of morphism between crossed
groupoids.

Now let $X$ be a topological space. A {\em stack of crossed groupoids}
$\twocat{P}$ on $X$ is the geometrization of a crossed groupoid.
Thus for every open set $U \subset X$ we have a crossed groupoid
$\twocat{P}(U)$; and for every inclusion $V \subset U$ of open sets there is a
morphism of crossed groupoids
$\mrm{rest}^{}_{V / U} : \twocat{P}(U) \to \twocat{P}(V)$. 
We  assume that the restriction morphisms satisfy 
$\mrm{rest}^{}_{W / V} \circ \mrm{rest}^{}_{V / U} = \mrm{rest}^{}_{W / U}$
for a double inclusion $W \subset V \subset U$ of open sets of $X$.
We also assume that $\twocat{P}_1$ is a stack of groupoids (in the usual
sense), and for every local object 
$\mcal{A}$ of $\twocat{P}$ the presheaf of groups 
$\twocat{P}_2(\mcal{A})$ is a sheaf. 
See Definition \ref{dfn:200} for details.

For us there are two important stacks of crossed groupoids. 
Let $\K$ be a field of characteristic $0$,
$X$ an algebraic variety over $\K$, and $(R, \m)$ some parameter
algebra over $\K$  (these are the default assumptions for the rest of the
Introduction). First there is the stack
$\twocat{P} := \twocat{AssDef}(R, \mcal{O}_X)$ of associative $R$-deformations
of $\mcal{O}_X$, which assigns to each open set $U \subset X$ the set
$\twocat{P}(U) := \cat{AssDef}(R, \mcal{O}_U)$ of associative 
$R$-deformations of $\mcal{O}_U$. The $1$-morphisms in $\twocat{P}(U)$ are the
gauge transformations. The inner gauge group 
$\twocat{P}_2(U)(\mcal{A})$ of an 
object $\mcal{A} \in \opn{Ob}(\twocat{P}(U))$ is the
multiplicative group of elements of $\Gamma(U, \mcal{A})$ that are congruent to
$1$ modulo $\m$. The feedback $\opn{D}(a)$, for an element 
$a \in \twocat{P}_2(U)(\mcal{A})$, 
is the conjugation action of $a$ on $\mcal{A}|_U$.

The second stack of crossed groupoids is the stack
$\twocat{P} := \twocat{PoisDef}(R, \mcal{O}_X)$ of Poisson
$R$-deformations of $\OX$. It assigns to each open set $U \subset X$
the set $\twocat{P}(U) := \cat{PoisDef}(R, \mcal{O}_U)$ of Poisson
$R$-deformations of $\mcal{O}_U$. Again the $1$-morphisms are the gauge
transformations. The inner gauge group $\twocat{P}_2(U)(\mcal{A})$ of an
object $\mcal{A} \in \opn{Ob}(\twocat{P}(U))$
is $\Gamma(U, \opn{Exp}(\m \mcal{A}))$, 
where $\m \mcal{A}$ is viewed as a sheaf of pronilpotent Lie
algebras with the Poisson bracket. The action of $\twocat{P}_2(U)(\mcal{A})$  on
$\mcal{A}$ is by {\em formal hamiltonian flows}. 

Given a stack of crossed groupoids $\twocat{P}$ on $X$, we can
talk about {\em twisted objects of $\twocat{P}$}. Such a twisted object 
is a triple $(\gerbe{G}, \gerbe{A}, \opn{cp})$, consisting
of a gerbe $\gerbe{G}$ on $X$, called the {\em gauge gerbe}, with a morphism of
stacks of groupoids $\gerbe{A} : \gerbe{G} \to \twocat{P}_1$,
called the {\em representation}. 
This means that to every local object $i$ of 
$\gerbe{G}$ we assign a local object $\gerbe{A}(i)$ of $\twocat{P}$; and to
every local isomorphism $g : i \to j$ in $\gerbe{G}$ we assign a local 
$1$-isomorphism (i.e.\ a gauge transformation) 
$\gerbe{A}(g) : \gerbe{A}(i) \to \gerbe{A}(j)$ in $\twocat{P}_1$.
There is also an isomorphism of sheaves of groups
$\opn{cp} : \gerbe{G}(i) \to \twocat{P}_2(\gerbe{A}(i))$
for every local object $i$ of $\gerbe{G}$, called the {\em coupling
isomorphism}. All these data have to satisfy certain compatibilities -- 
see Definitions \ref{dfn:6} and \ref{dfn:11} for full details.
By slight abuse of language, we usually refer to the
twisted object $\gerbe{A}$ and its gauge gerbe $\gerbe{G}$.
An object $\gerbe{A}(i)$, for some local object $i$ of $\gerbe{G}$, is called a
{\em local object} of $\gerbe{A}$. 

In Examples \ref{exa:21} and \ref{exa:tw.sh.101} we explain how gerbes and
stacks of $R$-algebroids can be viewed as twisted objects, of the stacks of
crossed groupoids $\twocat{Grp}^{\times}(X)$ and  
$\twocat{Assoc}^{\times}(R, X)$ respectively. 

By definition a {\em twisted associative $R$-deformation of $\mcal{O}_X$} is a 
twisted object $\gerbe{A}$ of the stack of crossed groupoids
$\twocat{AssDef}(R, \mcal{O}_X)$.
Likewise, a {\em twisted Poisson $R$-deformation of
$\mcal{O}_X$} is a twisted object $\gerbe{A}$ of the stack  of crossed groupoids
$\twocat{PoisDef}(R, \mcal{O}_X)$.

The distinction between twisted associative $R$-deformations and DQ-algebroids
(in the sense of \cite{KS2}) is explained in Remark \ref{rem:6}.
As we said before, the concept of twisted Poisson deformation appears to be
completely new -- there does not seem to be any similar definition in the
literature. 



\subsection{Gauge Gerbes}
There is a benefit in working with gauge gerbes: it is easier
to study the combinatorial structure of a twisted deformation.
Indeed, let $\gerbe{A}$ be a twisted $R$-deformation of $\mcal{O}_X$, with 
gauge gerbe $\gerbe{G}$. The coupling isomorphism endows $\gerbe{G}$
with the $\m$-adic filtration, making it into a pronilpotent
gerbe (in the sense of \cite{Ye4}). Using the results from 
\cite{Ye4} on pronilpotent gerbes we obtain the next theorem
(repeated in a more general form as Theorem \ref{thm:6} in the body of
the paper): 

\begin{thm}[Total Trivialization] \label{thm:17}
Let $\K$ be a field of characteristic $0$, $X$ an algebraic variety over
$\K$, $\gerbe{A}$ a twisted associative or Poisson $R$-deformation of 
$\OX$, with gauge gerbe $\gerbe{G}$, and $U$ an open set in $X$
that satisfies 
$\opn{H}^1(U, \OX) = \opn{H}^2(U, \OX) = 0$
\tup{(}for instance an affine open set\tup{)}. 
Then the groupoid $\gerbe{G}(U)$ is nonempty and connected.
\end{thm}



\subsection{Combinatorial Descent} \label{subsec:combinat}
In this subsection we leave the geometry aside, to talk about {\em combinatorial
descent data}. We shall return to the geometry in Subsection
\ref{subsec:geodesc}. 

We are interested in {\em cosimplicial crossed groupoids}. 
A cosimplicial crossed group\-oid 
$G = \{ G^p \}_{p \in \N}$
is made up of a crossed groupoid 
$G^p = ( G^p_1, G^p_2, \opn{Ad}, \opn{D})$ 
for every $p$, and a morphism of crossed groupoids
$G(\al) : G^p \to G^q$
for every arrow $\al : p \to q$ in the simplex category $\bsym{\Delta}$.
The morphisms $G(\al)$ must satisfy the simplicial relations. 

Let $G = \{ G^p \}_{p \in \N}$
be a cosimplicial crossed groupoid. A {\em combinatorial descent datum} in
$G$ is a triple $(\om, g, a)$ consisting of elements of these sorts: 
$\om \in \opn{Ob}(G^0$),
$g \in G^1_1(\om_{(0)}, \om_{(1)})$
and 
$a \in G^2_2(\om_{(0)}, \om_{(0)})$.
These elements have to satisfy two conditions: ``failure of $1$-cocycle'' and 
``twisted $2$-cocycle''; see Definition \ref{dfn:101}. 
Here $\om_{(i)}$ is the object of the crossed groupoid $G^p$
corresponding to the vertex $(i)$ of the simplex $\bsym{\Delta}^p$, and
$G^p_p(\om_{(i)}, \om_{(j)})$ is the set of morphisms
$\om_{(i)} \to \om_{(j)}$ in the groupoid $G^p_p$. 

As we shall see in Subsection \ref{subsec:geodesc} below, combinatorial descent
data is an abstraction of the familiar descent data for gerbes.

Let us denote by $\opn{Desc}(G)$ the set of combinatorial descent data.
There is an equivalence relation on this set, called gauge equivalence (see
Definition \ref{dfn:100}), and we denote by 
$\ol{\opn{Desc}}(G)$ the quotient set. A morphism 
$\Phi : G \to H$ of cosimplicial crossed groupoids induces a
function 
$\ol{\opn{Desc}}(\Phi) : \ol{\opn{Desc}}(G) \to
\ol{\opn{Desc}}(H)$.
The notion of {\em weak equivalence} between cosimplicial crossed groupoids is
introduced in Definition \ref{dfn:equiv-cosim.103}. 
The next result is proved in the companion paper \cite{Ye8}.
See \cite{Pr} for an alternative proof. 

\begin{thm}[{Combinatorial Equivalence,  \cite[Theorem 0.1]{Ye8}}]
\label{thm:intro.100}
Let $\Phi : G \to H$ be a weak equivalence between 
cosimplicial crossed groupoids. Then the function 
\[ \ol{\opn{Desc}}(\Phi) : \ol{\opn{Desc}}(G) \to
\ol{\opn{Desc}}(H) \]
is bijective.
\end{thm}



\subsection{Lie Descent}
Let $\g = \bigoplus_{i \in \Z} \, \g^i$ be a {\em quantum type} DG Lie algebra
over $\K$,
namely $\g^i = 0$ for all $i < -1$. There is an induced
pronilpotent DG Lie $R$-algebra 
$\m \hot \g = \bigoplus_{i \in \Z} \, \m \hot \g^i$.
Following \cite{De} and \cite{Ge1} we consider the {\em Deligne crossed
groupoid} $\opn{Del}(\g, R)$ (better known as the Deligne $2$-groupoid). Recall
that the set of objects of 
$\opn{Del}(\g, R)$ is the set $\opn{MC}(\m \hot \g)$ of solutions of the
Maurer-Cartan equation. The $1$-morphisms in $\opn{Del}(\g, R)$ are the
elements of the gauge group $\opn{Exp}(\m \hot \g^0)$, and the 
$2$-morphisms in $\opn{Del}(\g, R)$ are the
elements of the groups $\opn{Exp}(\m \hot \g^{-1})_{\om}$, for 
$\om \in \opn{MC}(\m \hot \g)$. See Sections \ref{sec:defs-DG-Lie} and
\ref{sec:Lie-desc} for details. 

Now suppose $\g = \{ \g^p \}_{p \in \N}$ is a {\em cosimplicial quantum type DG
Lie algebra}. So in each simplicial dimension $p$ there is a quantum type DG Lie
algebra $\g^p = \bigoplus_{i \geq -1} \, \g^{p, i}$.
Since the Deligne crossed groupoid is functorial, we get a cosimplicial
crossed groupoid 
$\opn{Del}(\g, R) = \bigl\{ \opn{Del}(\g^p, R) 
\bigr\}_{p \in \N}$.
The combinatorial descent construction from Subsection \ref{subsec:combinat}
gives rise to the set of {\em Lie descent data} \lb
$\opn{Desc} \bigl( \opn{Del}(\g, R) \bigr)$,
and its quotient set (modulo gauge equivalence)
$\ol{\opn{Desc}} \bigl( \opn{Del}(\g, R) \bigr)$.

Suppose $\h =  \{ \h^p \}_{p \in \N}$ is another cosimplicial quantum type DG
Lie algebra. A cosimplicial
$\mrm{L}_{\infty}$ morphism $\Psi : \g \to \h$ 
is a collection $\Psi^p : \g^p \to \h^p$ of $\mrm{L}_{\infty}$ morphisms,
that respect the cosimplicial structures. We say that $\Psi$ is a cosimplicial
{\em $\mrm{L}_{\infty}$ quasi-isomorphism} if each $\Psi^p : \g^p \to \h^p$
is an $\mrm{L}_{\infty}$ quasi-isomorphism. 

\begin{thm}[Equivalence for Lie Descent] \label{thm:intro.103}
Let $\Psi : \g \to \h$ be a cosimplicial $\mrm{L}_{\infty}$ morphism between 
cosimplicial quantum type DG Lie algebras, and let 
$\nu : R \to S$ be a homomorphism between parameter algebras,
all over a field $\K$ of characteristic $0$. Then there is a function 
\[ \ol{\opn{Desc}} (\opn{Del})(\Psi, \nu)  : 
\ol{\opn{Desc}} ( \opn{Del}(\g, R) ) \to 
\ol{\opn{Desc}} ( \opn{Del}(\h, S) ) , \]
which is functorial in $\Psi$ and $\nu$.
Furthermore, if $\Psi$ is a cosimplicial  $\mrm{L}_{\infty}$ quasi-isomorphism
and $\nu$ is an isomorphism, then 
$\ol{\opn{Desc}} (\opn{Del})(\Psi, \nu)$ is bijective. 
\end{thm}

This is repeated with more details as Theorem \ref{thm:Lie-desc.101} in the body
of the paper. The proof uses Theorem
\ref{thm:intro.100}, and results from \cite{Ye7} on the Deligne crossed groupoid
and on the {\em bar-cobar construction} for DG Lie algebras.




\subsection{Geometric Descent} \label{subsec:geodesc}
Let 
$\twocat{P} = ( \twocat{P}_1, \twocat{P}_2, 
\opn{Ad}_{\twocat{P}_1 \crvar \twocat{P}_{2}}, \opn{D} )$
be some stack of crossed groupoids on a topological space
$X$. We denote the set of twisted objects of $\twocat{P}$ by
$\opn{TwOb}(\twocat{P})$. 
There is an intrinsic notion of twisted gauge equivalence between 
twisted objects (see Definition \ref{dfn:33}), and we denote the resulting set
of equivalence classes by 
$\ol{\opn{TwOb}}(\twocat{P})$. 

Let $\bsym{U} = \{ U_k \}_{k \in K}$  be an open covering of the space $X$.
For $k_0, \ldots, k_m \in K$ we write 
$U_{k_0, \ldots, k_m} := U_{k_0} \cap \cdots \cap U_{k_m}$.
A {\em geometric descent datum} for twisted objects of $\twocat{P}$, relative to
this covering, consists of a collection 
$\{ \mcal{A}_{k_0} \}_{k_0 \in K}$ of objects 
$\mcal{A}_{k_0} \in \opn{Ob}(\twocat{P}(U_{k_0}))$, a collection 
$\{ g_{k_0, k_1} \}$ of $1$-morphisms
\[ g_{k_0, k_1} : \mcal{A}_{k_0}|_{U_{k_0, k_1}} \iso 
\mcal{A}_{k_1}|_{U_{k_0, k_1}} \]
in $\twocat{P}_1(U_{k_0, k_1})$, and a collection
$\{ a_{k_0, k_1, k_2} \}$ of $2$-morphisms 
\[ a_{k_0, k_1, k_2} \in 
\twocat{P}_2(U_{k_0, k_1, k_2})(\mcal{A}_{k_0}|_{U_{k_0, k_1, k_2}}) . \]
The conditions are:
\[ g_{k_0, k_2}^{-1} \circ g_{k_1, k_2} \circ g_{k_0, k_1} =
\opn{D}(a_{k_0, k_1, k_2}) \]
as automorphisms of $\mcal{A}_{k_0}|_{U_{k_0, k_1, k_2}}$
in $\twocat{P}_1(U_{k_0, k_1, k_2})$, and 
\[ a_{k_0, k_1, k_3}^{-1} \cdot a_{k_0, k_2, k_3} \cdot 
a_{k_0, k_1, k_2} = 
\opn{Ad}_{\twocat{P}_1 \crvar \twocat{P}_{2}}(g_{k_0, k_1}^{-1})
(a_{k_1, k_2, k_3}) \]
in the group
$\twocat{P}_2(U_{k_0, \ldots, k_3})
(\mcal{A}_{k_0}|_{U_{k_0, \ldots, k_3}})$.

The above can be stated in terms of combinatorial descent (see Subsection
\ref{subsec:combinat}). 
For any open set $U \subset X$ we have a crossed groupoid
$\twocat{P}(U)$. Thus, given an open
covering $\bsym{U}$, the \v{C}ech construction gives rise to a cosimplicial
crossed groupoid $\opn{C}(\bsym{U}, \twocat{P})$. A geometric descent
datum is precisely an element of 
$\opn{Desc}(\opn{C}(\bsym{U}, \twocat{P}))$.

A consequence of Theorem \ref{thm:17} is this result (it is a combination of 
Corollary \ref{cor:4}, Theorem \ref{thm:glu.1}, Proposition
\ref{prop:bitorsors.6} and Proposition \ref{prop:206} in the body of the
paper): 

\begin{thm}[Decomposition] \label{thm:intro.101}
Let $\K$ be a field of characteristic $0$, $X$ a smooth algebraic variety
over $\K$, $R$ a parameter algebra over $\K$, and $\bsym{U}$ an
affine open covering of $X$. Denote by $\twocat{P}(R, X)$ either of the stacks
of crossed groupoids \lb $\twocat{AssDef}(R, \mcal{O}_X)$ or
$\twocat{PoisDef}(R, \mcal{O}_X)$. Then there is a bijection
\[ \ol{\opn{dec}} : 
\ol{\opn{TwOb}}  \bigl( \twocat{P}(R, X) \bigr) \iso
\ol{\opn{Desc}} \bigl( \opn{C} (\bsym{U}, \twocat{P}(R, X)) \bigr)  \]
called {\em decomposition}, which is functorial with respect to refinements
$\bsym{U}' \to \bsym{U}$ of affine open coverings, and with respect to
homomorphisms $R \to R'$ of parameter algebras.
\end{thm}

The ideas of geometric descent data and decomposition are not new; they appear
in most texts about gerbes (cf.\ \cite[Section IV.3.5]{Gi}, and also
\cite{Br, Ko2, BGNT1, DP1}). However, a result such
as Theorem \ref{thm:17} is usually not available, and the authors usually impose
something like Theorem \ref{thm:17} as a condition (explicitly or
implicitly), or else they are forced to deal with hypercoverings.

What Theorem \ref{thm:intro.101} says is that we can replace the study of
twisted deformations with that of geometric descent data. 



\subsection{DG Lie Algebras and Deformations} \label{subsec:geom}
On the smooth algebraic variety $X$ there are two important sheaves of DG Lie
algebras: the sheaf $\mcal{T}_{\mrm{poly}, X}$ of {\em polyderivations}, and the
sheaf $\mcal{D}_{\mrm{poly}, X}$ of {\em polydifferential operators}. 
Within $\mcal{D}_{\mrm{poly}, X}$ there is the subalgebra
$\mcal{D}_{\mrm{poly}, X}^{\mrm{nor}}$ 
of {\em normalized polydifferential operators}. 
The sheaves $\mcal{T}_{\mrm{poly}, X}$, $\mcal{D}_{\mrm{poly}, X}$ and
$\mcal{D}_{\mrm{poly}, X}^{\mrm{nor}}$
are quasi-coherent graded $\OX$-modules, and the inclusion 
$\mcal{D}_{\mrm{poly}, X}^{\mrm{nor}} \to \mcal{D}_{\mrm{poly}, X}$
is a quasi-isomorphism. 

\begin{thm}[{Geometrization, \cite[Theorem 0.1]{Ye9}}] \label{thm:120}
Let $\K$ be a field of characteristic $0$, $X$ a smooth algebraic variety
over $\K$, $R$ a parameter algebra over $\K$, 
and $U$ an affine open set in $X$.
There are equivalences of crossed groupoids
\[  \opn{geo} : \
\opn{Del} \bigl( \Gamma(U, \mcal{D}_{\mrm{poly}, X}^{\mrm{nor}}) , R \big)
\to \cat{AssDef}(R, \mcal{O}_U) \]
and
\[  \opn{geo} : \
\opn{Del} \bigl( \Gamma(U, \mcal{T}_{\mrm{poly}, X}) , R \big)
\to \cat{PoisDef}(R, \mcal{O}_U) \]
which we call {\em geometrization}. The equivalences  $\opn{geo}$
commute with homomorphisms $R \to R'$ of parameter algebras, and with inclusions
of affine open sets $U' \to U$.
\end{thm}

See Definition \ref{dfn:227} regarding equivalences of crossed groupoids.

In earlier versions of this paper the proof of Theorem \ref{thm:120} was
part of the material. However the paper got to be extremely long, and
hence we extracted all the material leading to Theorem
\ref{thm:120}, and made it into the new paper \cite{Ye9}. 
In terms of content, everything involving stacks remained in this paper, and
the rest was moved to \cite{Ye9}. 

The proof of Theorem \ref{thm:120}, in \cite{Ye9}, has several difficult
components. First there is the issue of $\m$-adically complete flat sheaves of
$R$-modules on the variety $X$, that required a lot of basic work 
(some of it in \cite{Ye5}). Regarding associative deformations, the
geometrization required a delicate analysis of sheaves of noncommutative rings 
on an algebraic variety, using {\em Ore localization}. The fact that the DG Lie
algebra $\mcal{D}_{\mrm{poly}, X}^{\mrm{nor}}$ controls  associative
deformations (without any differentiality restriction on these deformations!) 
is a new result. In our earlier paper \cite{Ye1} we had to put a local
differentiality condition on associative deformations (that we now know is
redundant). It is important to note that the corresponding statement 
for complex analytic manifolds is an open problem; see \cite[Remark 2.2.7]{KS2}.

Consider a finite affine open covering $\bsym{U}$ of $X$. The \v{C}ech
construction gives rise to the  cosimplicial quantum type DG Lie algebras
$\opn{C}(\bsym{U}, \mcal{T}_{\mrm{poly}, X})$ and 
$\opn{C}(\bsym{U}, \mcal{D}_{\mrm{poly}, X}^{\mrm{nor}})$. 
The combination of Theorems \ref{thm:120} and \ref{thm:intro.100} yields:

\begin{cor}[Geometrization of Descent Data] \label{cor:110}
Let $\K$ be a field of characteristic $0$, $X$ a smooth algebraic variety
over $\K$, $R$ a parameter algebra over $\K$, 
and $\bsym{U}$ a finite affine open covering of $X$.
There are bijections
\[  \ol{\opn{geo}} : 
\ol{\opn{Desc}} \bigl( \opn{Del} \bigl(
\mrm{C}(\bsym{U}, \mcal{D}_{\mrm{poly}, X}^{\mrm{nor}}) , R 
\bigr) \bigr)
\iso
\ol{\opn{Desc}} \bigl( \opn{C} \bigl(
\twocat{AssDef}(R, \mcal{O}_X) , \bsym{U} \bigr) \bigr) \]
and 
\[  \ol{\opn{geo}} : 
\ol{\opn{Desc}} \bigl( \opn{Del} \bigl(
\mrm{C}(\bsym{U}, \mcal{T}_{\mrm{poly}, X}) , R 
\bigr) \bigr)
\iso
\ol{\opn{Desc}} \bigl( \opn{C} \bigl(
\twocat{PoisDef}(R, \mcal{O}_X) , \bsym{U} \bigr) \bigr) . \]
The functions $\ol{\opn{geo}}$ respect homomorphisms
$R \to R'$ of parameter algebras, and 
refinements of coverings $\bsym{U}' \to \bsym{U}$.
\end{cor}

This is Theorem \ref{thm:11} in the body of the paper.

We know that $\mcal{T}_{\mrm{poly}, X}$ and 
$\mcal{D}_{\mrm{poly}, X}^{\mrm{nor}}$ are sheaves in the \'etale topology of
$X$. This, with Corollary \ref{cor:110} and  Theorem \ref{thm:intro.101}, imply
that 
$\ol{\opn{TwOb}}  \bigl( \twocat{P}(R, X) \bigr)$
is contravariant with respect to \'etale morphisms $X' \to X$.
The set $\ol{\opn{TwOb}}  \bigl( \twocat{P}(R, X) \bigr)$
is also covariant with respect to homomorphisms $R \to R'$ of parameter
algebras. See Theorem \ref{thm:7} for the precise statement.



\subsection{The Formality Morphism}
Given a finite affine open covering $\bsym{U}$ of $X$,
we can form the {\em mixed resolution} 
$\opn{Mix}_{\bsym{U}}(\mcal{M})$ of any 
quasi-coherent sheaf $\mcal{M}$. This resolution is functorial, and moreover 
the complex $\opn{Mix}_{\bsym{U}}(\mcal{M})$ is acyclic for the global sections
functor $\Gamma(X, -)$. 
Resolving the sheaves $\mcal{T}_{\mrm{poly}, X}$ and 
$\mcal{D}_{\mrm{poly}, X}$ we get sheaves of  DG Lie algebras 
$\opn{Mix}_{\bsym{U}}(\mcal{T}_{\mrm{poly}, X})$ and
$\opn{Mix}_{\bsym{U}}(\mcal{D}_{\mrm{poly}, X})$. 
See \cite[Proposition 6.3]{Ye1} for details.

Assume $\opn{dim} X = n$. An {\em \'etale coordinate system} on an open set 
$U \subset X$ is an \'etale morphism $s : U \to \mbf{A}^n_{\K}$. 
By {\em open covering with \'etale coordinates} of $X$ we mean 
a pair $(\bsym{U}, \bsym{s})$, consisting of an open covering
$\bsym{U} = \{ U_k \}$, together with a family $\bsym{s} = \{ s_k \}$ of 
\'etale coordinate systems $s_k : U_k \to \mbf{A}^n_{\K}$.

One of the main results of \cite{Ye1} is that there is an 
$\mrm{L}_{\infty}$ quasi-isomorphism
\[ \Psi_{\bsym{s}} = \{ \Psi_{\bsym{s}; i} \}_{i \geq 1} :
\opn{Mix}_{\bsym{U}}(\mcal{T}_{\mrm{poly}, X}) \to 
\opn{Mix}_{\bsym{U}}(\mcal{D}_{\mrm{poly}, X})  \]
between sheaves of DG Lie algebras on $X$. 
This is \cite[Theorem 0.2]{Ye1}, and it relies on the universal formality
morphism of Kontsevich from \cite{Ko1}. See \cite[Theorem 1.1]{VdB} for
another proof. In Theorem \ref{thm:13} in the body of the paper we expand
\cite[Theorem 0.2]{Ye1}. As a consequence we obtain the next theorem, which is
repeated, with more details, as Theorem \ref{thm:221}.

\begin{thm}[Cosimplicial Formality] \label{thm:22}
Assume the field $\K$ contains $\R$.
Let $X$ be a smooth algebraic variety over $\K$, and let
$(\bsym{U}, \bsym{s})$ be a finite affine open covering with
\'etale coordinates of $X$. Then there is a diagram
\[ \UseTips \xymatrix @C=12ex @R=5ex {
\mrm{C}(\bsym{U}, \mcal{T}_{\mrm{poly}, X})
\ar[d]
&
\mrm{C}(\bsym{U}, \mcal{D}_{\mrm{poly}, X}^{\mrm{nor}})
\ar[d]
\\
\mrm{C} \bigl( \bsym{U} , \opn{Mix}_{\bsym{U}}(\mcal{T}_{\mrm{poly}, X})
\bigr)
\ar[r]^{\mrm{C}(\bsym{U} , \Psi_{\bsym{s}})} 
&
\mrm{C} \bigl( \bsym{U} , \opn{Mix}_{\bsym{U}}(\mcal{D}_{\mrm{poly}, X})
\bigr) \ ,
} \]
where the objects are cosimplicial quantum type DG Lie algebras, the
vertical arrows are cosimplicial DG Lie quasi-isomorphisms, and the horizontal
arrow is a cosimplicial $\mrm{L}_{\infty}$ quasi-isomorphism. 
This diagram is independent \tup{(}up to cosimplicial quasi-isomorphism\tup{)}
of the covering $(\bsym{U}, \bsym{s})$, and respects \'etale morphisms 
$X' \to X$.
\end{thm}

The reason for the condition $\R \subset \K$ is because in \cite{Ye1}
we used the original universal quantization morphism of Konstevich \cite{Ko1}. 
See Remark \ref{rem:TDQ.101} for a discussion on how to relax this condition.



\subsection{The Twisted Quantization Theorem} \label{subsec:TDQ}
There is a notion of {\em twisted gauge equivalence} between  
twisted associative $R$-deformation of $\mcal{O}_X$; this is the same as the 
twisted gauge equivalence in 
$\opn{TwOb}(\twocat{P})$ for 
$\twocat{P} := \twocat{AssDef}(R, \mcal{O}_X)$.
Likewise for twisted Poisson deformations. 

A twisted deformation $\gerbe{A}$ induces a {\em first order bracket}
$\{ -,- \}_{\gerbe{A}}$ on $\mcal{O}_X$.
See Definition \ref{dfn:22}, or the text preceding Example \ref{exa:23} above.

Here is the main result of our paper:

\begin{thm}[Twisted Quantization] \label{thm:14}
Let $\K$ be a field containing the real numbers, let $R$ be a 
parameter $\K$-algebra, and let $X$ be a smooth algebraic variety over
$\K$. Then there is a bijection of sets
\[ \begin{aligned}
& \opn{tw{.}quant} : 
\frac{ \{ \tup{twisted Poisson $R$-deformations of 
$\mcal{O}_X$} \} }
{\tup{ twisted gauge equivalence}} \\[0.3em]
& \hspace{14ex} \xar{\ \cong \ }  \
\frac{ \{ \tup{twisted associative $R$-deformations of 
$\mcal{O}_X$} \} }
{\tup{ twisted gauge equivalence}}
\end{aligned} \] 
called {\em twisted quantization}. 
The bijection $\opn{tw{.}quant}$ preserves first order brackets, and commutes
with homomorphisms of parameter algebras $R \to R'$, and with  \'etale morphisms
of varieties $X' \to X$.
\end{thm}

This theorem is repeated in greater detail as Theorem \ref{thm:8}.
It is proved by assembling Theorem \ref{thm:intro.101}, Corollary
\ref{cor:110}, Theorem \ref{thm:22} and Theorem \ref{thm:intro.103}.
The roles of these results can be seen in the diagram in Figure 
\ref{fig:diagram}. 
Specifically, the  bijections $\ol{\opn{dec}}$ in the diagram are from 
Theorem \ref{thm:intro.101}; the  bijections $\ol{\opn{geo}}$ are from 
Corollary \ref{cor:110}; and the bijections 
$\ol{\opn{mix}}$ and $\ol{\Psi}_{\bsym{s}}$ are gotten by applying 
Theorem \ref{thm:intro.103} to the diagram of cosimplicial 
$\mrm{L}_{\infty}$ quasi-isomorphisms in Theorem \ref{thm:22}.

\begin{figure}
\[ \UseTips \xymatrix @C=5ex @R=5ex {
\ol{\opn{TwOb}} \bigl( \twocat{PoisDef}(R, \mcal{O}_X) \bigr)
\ar[d]_{\ol{\opn{dec}}}
\ar@{-->}[r]^{\opn{tw{.}quant}}
&
\ol{\opn{TwOb}} \bigl( \twocat{AssDef}(R, \mcal{O}_X) \bigr)
\ar[d]^{\ol{\opn{dec}}}
\\
\ol{\opn{Desc}} \bigl( 
\mrm{C}( \bsym{U}, \twocat{PoisDef}(R, \mcal{O}_X) ) \bigr)
&
\ol{\opn{Desc}} \bigl( 
\mrm{C}( \bsym{U}, \twocat{AssDef}(R, \mcal{O}_X) ) \bigr)
\\
\ol{\opn{Desc}}  \bigl( \opn{Del}
\bigl( \mrm{C}(\bsym{U}, \mcal{T}^{}_{\mrm{poly}, X}), R \bigr) \bigr)
\ar[u]^{\ol{\opn{geo}}}
\ar[d]_{\ol{\opn{mix}}}
&
\ol{\opn{Desc}} \bigl( \opn{Del} \bigr(
\mrm{C}(\bsym{U}, \mcal{D}^{\mrm{nor}}_{\mrm{poly}, X}) , R \bigr) \bigr)
\ar[u]_{\ol{\opn{geo}}}
\ar[d]^{\ol{\opn{mix}}}
\\
\ol{\opn{Desc}} \bigl( \opn{Del} \bigl(
\mrm{C}(\bsym{U}, \opn{Mix}_{\bsym{U}}(\mcal{T}_{\mrm{poly},X}) ), R \bigr)
\bigr)
\ar[r]^{\ol{\Psi}_{\bsym{s}}}
& 
\ol{\opn{Desc}} \bigl( \opn{Del} \bigl(
\mrm{C}(\bsym{U}, \opn{Mix}_{\bsym{U}}(\mcal{D}_{\mrm{poly}, X}) ), R \bigr)
\bigr)
} \]
\caption{Diagram of bijections in the proof of Theorem \ref{thm:14}.}
\label{fig:diagram}
\end{figure}

In Corollaries \ref{cor:TDQ.105} and \ref{cor:TDQ.102} we explain what happens
when some or all of the cohomology groups
$\mrm{H}^1(X, \mcal{O}_X)$, $\mrm{H}^2(X, \mcal{O}_X)$, 
$\mrm{H}^1(X, \mcal{T}_X)$ and $\mrm{H}^1(X, \mcal{D}_X)$
vanish.

A twisted $R$-deformation $\gerbe{A}$ of $\mcal{O}_X$ is said to be {\em really
twisted} if it has no global objects, namely if the groupoid $\gerbe{G}(X)$ is
empty (where $\gerbe{G}$ is the gauge gerbe of  $\gerbe{A}$).

Any deformation $\mcal{A}$ generates a twisted
deformation $\gerbe{A}$, and $\mcal{A}$ is a global object of
$\gerbe{A}$. See Example \ref{exa:19}. Any twisted deformation $\gerbe{A}$
that is not really twisted is of this form.

One consequence of Theorem \ref{thm:6} is that in the differentiable
setup (and $\K = \mbb{R}$) there are no really twisted
$R$-deformations. 
However, when $X$ is a complex analytic manifold (and $\K = \mbb{C}$),
there do exist really twisted $R$-deformations. Presumably our methods
(with minor adjustments) should work also for complex analytic
manifolds, and a result similar to Theorem \ref{thm:14} should hold.

Here is a question that we find intriguing. 

\begin{que}
Let $X$ be a Calabi-Yau surface, with symplectic Poisson bracket 
$\{ -,- \}$. Consider the Poisson $\K[[\hbar]]$-deformation 
$\mcal{A}$ of $\mcal{O}_X$ that we get from Example \ref{exa:23}, and the 
twisted Poisson deformation $\gerbe{A}$ generated by $\mcal{A}$.
Let $\gerbe{B} := \opn{tw{.}quant} (\gerbe{A})$,
which is a twisted associative $\K[[\hbar]]$-deformation 
of $\mcal{O}_X$, well-defined up to twisted gauge equivalence. Is
$\gerbe{B}$ really twisted? 
\end{que}

This question is repeated (with a few more details) at the end of Section
\ref{sec:TDQ}, along with a some other questions.



\subsection{Discussion of Related Work} \label{subsec:discuss}
We finish the introduction with a discussion of several related papers.
This is not an easy task, since these papers were written by people working in
several mathematical branches -- differential geometry, complex
analytic geometry, algebraic geometry and mathematical physics -- and the style
of writing varies accordingly.  

The impetus for our work was trying to understand the ideas 
proposed by Kontsevich in \cite{Ko2}. In that paper Kontsevich considered a
smooth algebraic variety $X$ over a field of characteristic $0$. He claimed
that any formal Poisson deformation of $\OO_X$ can be quantized to a stack of
algebroids. However there was only a hint of a proof in \cite{Ko2}, and there
was no statement regarding classification. We found this new idea of Kontsevich
extremely interesting, and wanted to prove it, and to expand it to a
precise classification statement (generalizing the affine case). We had several
conversations with Kontsevich, in which he offered some valuable suggestions,
that eventually led us to the concept of twisted Poisson deformation 
(see Subsection \ref{subsec:tw.defs}). The precise statement
about twisted deformation quantization of an
algebraic variety appears for the first time in this paper (this is 
Theorem \ref{thm:14}); and ours is the only paper that gives a complete proof
of this result. 

As we already mentioned, Kashiwara \cite{Ka} was the first to consider 
stacky quantizations. The situation in \cite{Ka} was this: $X$ is a complex
contact manifold, so
there is an open covering $X = \bigcup U_i$, where each $U_i$ is
isomorphic to an open submanifold of a projective cotangent bundle. Thus 
on $U_i$ there is a sheaf $\mcal{E}_i$ of microdifferential operators.
Kashiwara proved that even if the  $\mcal{E}_i$ cannot be glued into a
sheaf of rings, they can always be glued into a twisted sheaf (i.e.\
a stack of algebroids) $\gerbe{E}$. 

The paper \cite{KS2} by Kashiwara and P. Schapira discusses a variant 
of the stack of  microdifferential operators, that is called a {\em DQ
algebroid}. The description of a DQ algebroid $\gerbe{A}$ as a twisted object
is explained in Remark \ref{rem:6}.
There is some overlap regarding technical points between our paper and
\cite{KS2} (see Remark \ref{rem:221}, and the Introduction of \cite{Ye9}). 
The main thrust of \cite{KS2} is the study of the Hochschild homology sheaf 
associated to a symplectic DQ algebroid $\gerbe{A}$, and related 
characteristic classes. It does not contain any sort of twisted quantization
statement similar to our Theorem \ref{thm:14}.

P. Polesello and A. D'Agnolo  \cite{Po, DP1, DP2} studied twisted associative
deformations of complex manifolds, and quantizations of contact manifolds, in
the spirit of  \cite{Ka, KS2}. The relationship between \cite{DP2}
and our paper is mostly that in both papers heavy use is made of stacks of
crossed groupoids as a means of classifying twisted forms of stacks (as in
Theorem \ref{thm:intro.101} above). The paper \cite{Po} classifies twisted
associative deformations corresponding to a fixed  symplectic structure; there
is nothing in it resembling our Theorem \ref{thm:14}. One should also note (this
was pointed to us by Polesello) that the deformations in \cite{Po} and
\cite{KS2} are not augmented (see Remark \ref{rem:6}). 

E. Getzler wrote two papers \cite{Ge1, Ge2} on higher Deligne groupoids. 
The relevant results in \cite{Ge2}, and a certain difficulty in that paper, are
explained in Remark \ref{rem:Lie-desc.101}. 
For some time we had hoped to rely on Getzler's results for a proof of 
Theorem \ref{thm:intro.103} (at least for artinian parameter algebras), but we
could not find a satisfactory way to overcome the difficulty mentioned
in Remark \ref{rem:Lie-desc.101}. This is why we eventually provided our
own proof, that does not rely on Getzler's work.
 
P. Bressler, A. Gorokhovsky, R. Nest and B. Tsygan wrote a series of papers on
deformations of real and complex manifolds. In the paper \cite{BGNT1}
there is a discussion of cosimplicial DG Lie
algebras, with results similar to our Theorem \ref{thm:intro.103},
but only for DG Lie homomorphisms
$\g \to \h$ between cosimplicial DG Lie algebras (not $\mrm{L}_{\infty}$
morphisms), and only for artinian parameter algebras. 
Nonetheless several results in \cite{BGNT1} inspired us when we discovered
Theorems \ref{thm:intro.100} and \ref{thm:intro.103}.
Stacks -- in the true geometric sense -- do
not actually occur in \cite{BGNT1}; the authors only look at what we refer to
in Subsection \ref{subsec:geodesc} 
as geometric descent data. Also there is no twisted quantization result
similar to our Theorem \ref{thm:14}; in a large part of the paper
they only consider a particular symplectic Poisson bracket and study its
twisted associative quantizations. 

The paper \cite{BGNT2} considers twisted associative deformations
of twisted $\OO_X$-algebroids on a real or complex  manifold $X$. If we
understand correctly, the associative deformations considered in \cite{BGNT2}
are by definition locally differential, so the authors avoid touching
the hard technical issues lying behind our Theorem \ref{thm:120} 
(see discussion in Subsection \ref{subsec:geom}).
The paper \cite{BGNT2} does not contain a twisted quantization result
similar to our Theorem \ref{thm:14}. As far as we can tell one of the main
results there, namely \cite[Theorem 5.22]{BGNT2}, is analogous to our Corollary
\ref{cor:110} in the associative case. 

The third paper by this team of authors is \cite{BGNT3}. 
They consider several kinds of nerves (simplicial sets) associated with
$2$-groupoids, and prove these are homotopy equivalent. One of the methods used
in \cite{BGNT3} is nonabelian multiplicative integration of surfaces, as in our
paper \cite{Ye6}; indeed, they reproduce some of our results (with shorter
proofs in special cases). Among other things, it is claimed in \cite{BGNT3}
that the difficulty in \cite{Ge2} mentioned above can be settled (more on this
in Remark \ref{rem:Lie-desc.101}). 
It should be interesting to compare the results of \cite{BGNT3} to our Theorems 
\ref{thm:intro.100} and \ref{thm:intro.103}.

The fourth paper in this series is \cite{BGNT4}. Here they look at a 
$\mrm{C}^{\infty}$ manifold $X$ over $\K = \R$, with structure sheaf $\OO_{X}$. 
They start with a twist $\gerbe{B}_0$ of $\OO_{X}$, namely 
a stack of $\R$-algebroids $\gerbe{B}_0$ on $X$ that is locally equivalent to 
$\OO_{X}$. Such twists are classified by cohomology classes 
$[\phi] \in \opn{H}^3_{\mrm{dR}}(X)$.
Let $R$ be an artinian parameter $\R$-algebra with maximal ideal $\m$.  
Theorem 1.1 of \cite{BGNT4} says that associative 
$R$-deformations $\gerbe{B}$ of $\gerbe{B}_0$ are classified by 
the Deligne crossed groupoid of an $\mrm{L}_{\infty}$ algebra, 
whose underlying graded $\R$-module is 
$\Ga(X, \mcal{T}_{\mrm{poly}, X}) \ot \m$.
The binary operation is the usual one, but there is a ternary operation 
coming from a closed $3$-form $\phi$ on $X$ that represents the de Rham class 
$[\phi]$ of $\gerbe{B}_0$. This means that stacky associative $R$-deformations 
$\gerbe{B}$ correspond to $R$-linear $\phi$-Poisson structures on $X$, in the 
sense of Severa and Weinstein (cf.\ \cite{Se}). In this way
\cite[Theorem 1.1]{BGNT4} can be viewed as describing a twisted quantization 
operation.  However, the stackyness of an $R$-deformation $\gerbe{B}$ is the 
same as that of $\gerbe{B}_0 = \R \ot_{R} \gerbe{B}$. Thus this result is 
``perpendicular'' to our twisted quantization from Theorem \ref{thm:14}: for us 
the algebroid $\gerbe{B}_0$ is always trivial (i.e.\ $\gerbe{B}_0 = \OO_X$), and 
the stackyness is only in the $R$-linear deformation $\gerbe{B}$. 

The last paper to be discussed is \cite{CH}. The aim of that paper is
to prove a twisted deformation quantization like our Theorem \ref{thm:14}.
However in \cite{CH} the authors do not consider actual geometric twisted
deformations, but only the corresponding Lie descent
data. Thus they do not have any kind of geometrization result like our Corollary
\ref{cor:110}, nor a decomposition result like our Theorem 
\ref{thm:intro.101}. Their main result, \cite[Theorem 3.5]{CH}, 
seems to assert (in our notation, and when $X$ is a
smooth algebraic variety) that there is a bijection
\[ \ol{\opn{Desc}} \bigl( \opn{Del} \bigl(
\mrm{C}(\bsym{U}, \mcal{T}_{\mrm{poly}, X}) , \K[[\hbar]] 
\bigr) \bigr)
\ \cong \
\ol{\opn{Desc}} \bigl( \opn{Del} \bigl(
\mrm{C}(\bsym{U}, \mcal{D}_{\mrm{poly}, X}^{\mrm{nor}}) , \K[[\hbar]]  
\bigr) \bigr) . \]
Thus it is only a part of our Theorem \ref{thm:14} (the bottom half of the
diagram in Figure \ref{fig:diagram}).
We have some reservations regarding the validity of the proofs in \cite{CH},
for these reasons: 
the proofs in \cite{CH} are not all clear; delicate issues about pronilpotent
groupoids (such as those dealt with in the paper \cite{Ye7}) are ignored; and
there are some specific problems in homotopy theory (cf.\ Remarks
\ref{rem:cosim.106} and \ref{rem:Lie-desc.101}).

 


\medskip \noindent
\textbf{Acknowledgments.}
Work on this paper began together with Fredrick Leitner, and I wish to
thank him for his contributions. Many of the ideas in this paper are influenced
by the work of Maxim Kontsevich, and I am grateful to him for discussing this
material with me. Thanks also to Michael Artin, Pavel Etingof, Damien
Calaque, Michel Van den Bergh, Pierre Deligne, Lawrence Breen, Pierre Schapira,
Assaf Hasson, George Bergman, James Stasheff, Vladimir Hinich, Pietro
Polesello, Francois Petit and Matan Prasma for their assistance on various
aspects of this project. 
Finally I wish to thank the anonymous referee for reading the paper carefully 
and suggesting some further references.

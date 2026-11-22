---
doc_id: arxiv-0801.0083v4
doc_title: "CENTRAL EXTENSIONS OF GERBES"
section_id: sec-002-2-prestacks-on-a-topological-space
section_title: "Prestacks on a Topological Space"
section_number: 2
pages: 8-12
source_pdf: 0801.0083v4.pdf
source_sha256: 8e38b9e56d246709
toc_source: outline
text_source: latex
latex_prose_ratio: 0.995
latex_coverage_ratio: 0.965
doc_brief: "CENTRAL EXTENSIONS OF GERBES — We introduce the notion of central extension of gerbes on a topo- logical space X."
---
\label{sec:prest}

Let $X$ be a topological space. 
We need some notation for open coverings. Let $U \subset X$ be an open set, and
let $\bsym{U} = \{ U_k \}_{k \in K}$ be an open covering of $U$, i.e.\ 
$U = \bigcup_{k \in K} U_k$. Given 
$k_0, \ldots, k_m \in K$ we write
\[ U_{k_0, \ldots, k_m} := U_{i_0} \cap \cdots \cap U_{k_m} . \]

Let $\mcal{S}$ be a sheaf of sets on $X$. For an open set $U \subset X$ we
denote by 
$\mcal{S}(U) = \Gamma(U, \mcal{S})$
the set of sections of $\mcal{S}$ on $U$.

Recall that a {\em prestack} $\gerbe{G}$ on $X$
is the geometrization of the notion of category, 
in the same way that a presheaf of sets is the geometrization of the
notion of a set. Formally speaking a prestack $\gerbe{G}$ is a 
pseudofunctor
\[ \gerbe{G} 
= (\gerbe{G}_0, \gerbe{G}_1, \gerbe{G}_2) :
(\cat{Open} X)^{\mrm{op}} \to 
\bsym{\cat{Cat}} , \]
where $\cat{Open} X$ is the small category whose objects are the open sets 
$U \subset X$, and the morphisms $V \to U$ are the inclusions
$V \subset U$. However we shall make things more explicit here, and introduce
some notation, to emphasize the geometry. 

Thus a prestack $\gerbe{G}$ 
on $X$ has the following structure. 
For any open set $U \subset X$ there is a category
$\gerbe{G}(U) := \gerbe{G}_0(U)$. 
Elements of the set $\opn{Ob} \gerbe{G}(U)$ shall be denoted by
the letters $i, j$ etc.; this is because we want to view them as indices.
We write
\begin{equation}
\gerbe{G}(U)(i,j) := \opn{Hom}_{\gerbe{G}(U)} (i, j) , 
\end{equation}
the set of morphisms in the category $\gerbe{G}(U)$ from $i$ to $j$.

There are restriction functors ($1$-morphisms $\twocat{Cat}$)
\[ \opn{rest}^{\gerbe{G}}_{U_1 / U_0} := \gerbe{G}_1(U_1 \to
U_0) : \gerbe{G}(U_0) \to
\gerbe{G}(U_1) \] 
for any inclusion $U_1 \subset U_0$ of open sets. 
And there are composition isomorphisms ($2$-isomorphisms in
$\twocat{Cat}$)
\[ \gamma^{\gerbe{G}}_{U_2 / U_1 / U_0} := 
\gerbe{G}_2(U_2 \to U_1 \to U_0) 
: \opn{rest}^{\gerbe{G}}_{U_2 / U_1} \circ 
\opn{rest}^{\gerbe{G}}_{U_1 / U_0} \twoiso
\opn{rest}^{\gerbe{G}}_{U_2 / U_0} \]
for a double inclusion $U_2 \subset U_1 \subset U_0$. 
Condition (\ref{eqn:12}) now becomes 
\begin{equation} \label{eqn:6} 
\gamma^{\gerbe{G}}_{U_3 / U_2 / U_0} * 
\gamma^{\gerbe{G}}_{U_2 / U_1 / U_0} = 
\gamma^{\gerbe{G}}_{U_3 / U_1 / U_0} *
\gamma^{\gerbe{G}}_{U_3 / U_2 / U_1}
\end{equation}
for a triple inclusion $U_3 \subset U_2 \subset U_1 \subset U_0$. 
And there are corresponding conditions for $U \xar{=} U$.

As explained in Section \ref{sec.recall}, the set of prestacks on
$X$ has a structure of $2$-category, which we denote by
$\bsym{\cat{PreStack}}\, X$. Again, we want to be more specific. 
Suppose $\gerbe{G}$ and $\gerbe{H}$ are two prestacks on
$X$. A {\em morphism of prestacks}
$F : \gerbe{G} \to \gerbe{H}$
is a $1$-morphism between these pseudofunctors. Thus there is a
functor
\[ F(U) : \gerbe{G}(U) \to \gerbe{H}(U) \]
for any open set $U$, together with an isomorphism of functors
\[ \psi^F_{U_1 / U_0} : F(U_1) \circ 
\opn{rest}^{\gerbe{G}}_{U_1 / U_0} \twoiso 
\opn{rest}^{\gerbe{H}}_{U_1 / U_0} \circ \, F(U_0) \]
for any inclusion $U_1 \subset U_0$ of open sets. These isomorphisms
are required to satisfy condition 
\[ \psi^F_{U_2 / U_0} * \gamma^{\gerbe{G}}_{U_2 / U_1 / U_0} =
\gamma^{\gerbe{H}}_{U_2 / U_1 / U_0} * 
\psi^F_{U_2 / U_1}  * \psi^F_{U_1 / U_0} \]
for a double inclusion $U_2 \subset U_1 \subset U_0$.

The composition of morphisms of prestacks
$\gerbe{G} \xar{F} \gerbe{H} \xar{E} \gerbe{K}$
is denoted by $E \circ F$. 

Suppose $D, E, F : \gerbe{G} \to \gerbe{H}$
are morphisms between prestacks. We will denote $2$-morphisms between $E$
and $F$ by $\eta : E \twoto F$.
And the (vertical) composition with a $2$-morphism
$\zeta : D \twoto E$ is denoted by $\eta * \zeta : D \twoto F$. 

As in any $2$-category, we can say when a morphism of prestacks
$F : \gerbe{G} \to \gerbe{H}$ (i.e.\ a $1$-morphism
in $\bsym{\cat{PreStack}}\, X$) is an equivalence. 
This just means that there is a morphism of prestacks
$E : \gerbe{H} \to \gerbe{G}$,
and $2$-isomorphisms 
$E \circ F \twoiso \bsym{1}_{\gerbe{G}}$
and
$F \circ E \twoiso \bsym{1}_{\gerbe{H}}$. 
But here there is also a geometric characterization: $F$ is an equivalence if
and only if for any open set $U \subset X$ the functor
$F(U) : \gerbe{G}(U) \to \gerbe{H}(U)$
is an equivalence. 

Let $\gerbe{G}$ be a prestack on $X$. By a {\em subprestack} of $\gerbe{G}$ we
mean a prestack $\gerbe{N}$ such that $\gerbe{N}(U)$ is a subcategory of 
$\gerbe{G}(U)$ for every open set $U$, and such that the restriction functors
$\mrm{rest}^{\gerbe{N}}_{-/-}$ and the composition isomorphisms
$\gamma^{\gerbe{N}}_{- / - / -}$ are the same as those of $\gerbe{G}$.

Suppose $\gerbe{G}$ is a prestack on $X$. Take an open set $U \subset X$
and two objects $i, j \in \opn{Ob} \gerbe{G}(U)$. There is a
presheaf of sets $\gerbe{G}(i,j)$ on $U$, called the {\em presheaf of
morphisms}, defined as follows.
For an open set $V \subset U$ we define the set
\[ \gerbe{G}(i,j)(V) := 
\opn{Hom}_{\gerbe{G}(V)} \bigl( \mrm{rest}^{\gerbe{G}}_{V/U}(i),
\mrm{rest}^{\gerbe{G}}_{V/U}(j) \bigr) . \]
For an inclusion $V_1 \subset V_0 \subset U$ of open sets, the
restriction function 
\[ \mrm{rest}^{\gerbe{G}}(i,j)_{V_1 / V_0} :
\gerbe{G}(i,j)(V_0) \to \gerbe{G}(i,j)(V_1) \]
is the composed function
\[ \begin{aligned}
& \opn{Hom}_{\gerbe{G}(V_0)} \bigl(
\mrm{rest}^{\gerbe{G}}_{V_0/U}(i),
\mrm{rest}^{\gerbe{G}}_{V_0/U}(j) \bigr) \\
& \quad \xar{\mrm{rest}^{\gerbe{G}}_{V_1 / V_0}}
\opn{Hom}_{\gerbe{G}(V_0)} \bigl(
(\mrm{rest}^{\gerbe{G}}_{V_1/V_0} \circ
\mrm{rest}^{\gerbe{G}}_{V_0/U}) (i), 
(\mrm{rest}^{\gerbe{G}}_{V_1/V_0} \circ
\mrm{rest}^{\gerbe{G}}_{V_0/U}) (j) \bigr) \\
& \quad \xar{\gamma^{\gerbe{G}}_{V_1 / V_0 / U}}
\opn{Hom}_{\gerbe{G}(V_1)} \bigl(
\mrm{rest}^{\gerbe{G}}_{V_1/U}(i),
\mrm{rest}^{\gerbe{G}}_{V_1/U}(j) \bigr) . 
\end{aligned} \]
Condition (\ref{eqn:6}) ensures that
\[ \mrm{rest}^{\gerbe{G}}(i,j)_{V_2 / V_1} \circ
\mrm{rest}^{\gerbe{G}}(i,j)_{V_1 / V_0} =
\mrm{rest}^{\gerbe{G}}(i,j)_{V_2 / V_0} \]
for an inclusion 
$V_2 \subset V_1 \subset V_0 \subset U$.
Note that the set of sections of this presheaf is
\[ \Gamma(V, \gerbe{G}(i,j)) = \gerbe{G}(V)(i,j) . \]

{} From now on we shall usually write
$i|_V$ instead of $\mrm{rest}^{\gerbe{G}}_{V / U}(i)$, 
for a local object $i \in \opn{Ob} \gerbe{G}(U)$;
and $g|_{V_1}$ instead 
$\mrm{rest}^{\gerbe{G}}(i,j)_{V_1 / V_0}(g)$, for a local morphism 
$g \in \gerbe{G}(i,j)(V_0)$. Furthermore, 
we usually omit reference to the restriction
functors $\mrm{rest}^{\gerbe{G}}_{-/-}$ altogether.

Another convention that we shall adopt from here on is that we
denote the composition in the local categories
$\gerbe{G}(U)$ of a prestack $\gerbe{G}$ by ``$\circ$'', and not by 
``$*$'' as we did up to here.

Let $F : \gerbe{G} \to \gerbe{H}$ be a morphism of prestacks. 
One says that $F$ is a {\em weak equivalence} if it satisfies these conditions:
\begin{enumerate}
\rmitem{i} $F$ is {\em locally essentially surjective on objects}. This mean
that for any open set $U \subset X$,
object $j \in \opn{Ob} \gerbe{H}(U)$ and point $x \in U$, there is an open
set $V$ with $x \in V \subset U$, an object 
$i \in \opn{Ob} \gerbe{G}(V)$, and an isomorphism
$h : F(i) \iso j$ in $\gerbe{H}(V)$. 

\rmitem{ii} For any open set $U$ and $i, j \in \opn{Ob} \gerbe{G}(U)$ the
function
\[ F : \gerbe{G}(U)(i, j) \to \gerbe{H}(U) \bigl( F(i), F(j) \bigr) \]
is bijective. In other words, the functor
$F : \gerbe{G}(U) \to \gerbe{H}(U)$
is fully faithful. 
\end{enumerate}

A prestack $\gerbe{G}$ is called a {\em stack} if it satisfies 
these two conditions:
\begin{enumerate}
\rmitem{a} {\em Descent for morphisms}. This means that the presheaves of
morphisms $\gerbe{G}(i,j)$ are all sheaves. 

\rmitem{b} {\em Descent for objects}. This means 
that given an open set $U$, an open covering 
$U = \bigcup_{k \in K} U_k$, objects
$i_k \in \opn{Ob} \gerbe{G}(U_k)$, and isomorphisms
\[ g_{k_0, k_1} \in \gerbe{G}(U_{k_0, k_1})(i_{k_0}|_{U_{k_0, k_1}}, 
i_{k_1}|_{U_{k_0, k_1}}) \] 
that satisfy
\[ g_{k_1, k_2}|_{U_{k_0, k_1, k_2}} \circ 
g_{k_0, k_1}|_{U_{k_0, k_1, k_2}}  = g_{k_0, k_2}|_{U_{k_0, k_1, k_2}}  , \]
there exists an object
$i \in \gerbe{G}(U)$, 
and isomorphisms 
$g_k \in \gerbe{G}(U_{k})(i|_{U_{k}}, i_{k})$,
such that
\[ g_{k_0, k_1} \circ g_{k_0}|_{U_{k_0, k_1}}  = g_{k_1}|_{U_{k_0, k_1}} . \]
\end{enumerate}

Observe that by condition (a), the object $i \in \gerbe{G}(U)$ in condition (b)
is unique up to a unique isomorphism. A prestack $\gerbe{G}$ satisfying
condition (a) is sometimes called a {\em separated prestack}. 

We denote by $\bsym{\cat{Stack}}\, X$ the full sub $2$-category of
$\bsym{\cat{PreStack}}\, X$ gotten by taking all stacks, all
$1$-morphisms between them, and all $2$-morphisms between these
$1$-morphisms. 

It is not hard to see that a morphism of stacks $F : \gerbe{G} \to \gerbe{H}$ is
an equivalence if and only if it is a weak equivalence.

There is a {\em stackification} operation, which is analogous to sheafification:
to any prestack $\gerbe{G}$ one assigns a stack
$\til{\gerbe{G}}$, with a morphism of prestacks
$F : \gerbe{G} \to \til{\gerbe{G}}$.
These have the following universal property: given any stack 
$\gerbe{H}$ and morphism 
$E : \gerbe{G} \to \gerbe{H}$,
there is a morphism $\til{E} : \til{\gerbe{G}} \to \gerbe{H}$,
unique up to $2$-isomorphism, such that 
$E \twocong \til{E} \circ F$. 

Recall that a {\em groupoid} is a
category $\cat{G}$ in which all morphisms are isomorphisms. For an object $i$
the set $\cat{G}(i,i)$ is then a group. If the set 
$\cat{G}(i, j) \neq \emptyset$,
then it is a $\cat{G}(j, j)$-$\cat{G}(i, i)$-bitorsor. For 
$g \in \cat{G}(i, j)$ we denote by $\opn{Ad}(g)$ the group isomorphism 
$\cat{G}(i, i) \to \cat{G}(j, j)$ given by
$\opn{Ad}(g)(h) := g \circ h \circ g^{-1}$. 

By a {\em prestack of groupoids} on $X$ we mean a prestack 
$\gerbe{G}$ such that each of the categories $\gerbe{G}(U)$ is
a groupoid.
We denote by $\bsym{\cat{PreStGr}}\, X$
the full sub $2$-category of
$\bsym{\cat{PreStack}}\, X$ gotten by taking all prestacks of groupoids, all
$1$-morphisms between them, and all $2$-morphisms between these
$1$-morphisms. 
If $\gerbe{G}$ is a prestack of groupoids, then the associated stack
$\til{\gerbe{G}}$ is a stack of groupoids. 

We shall be interested in {\em gerbes}. 
A gerbe is a stack of groupoids $\gerbe{G}$ on $X$ that has these two
properties:
\begin{enumerate}
\rmitem{$\dag$} $\gerbe{G}$ is {\em locally nonempty}. What this means is
that any point $x \in X$ has an open neighborhood $U$ such that 
$\opn{Ob} \gerbe{G}(U) \neq \emptyset$. 

\rmitem{$\dag \dag$} $\gerbe{G}$ is {\em locally connected}. This
says that for any $i, j \in \opn{Ob} \gerbe{G}(U)$
and any $x \in X$, there is an open set $V$ such that $x \in V \subset U$ and
$\gerbe{G}(V)(i, j) \neq \emptyset$. 
\end{enumerate}

A gerbe $\gerbe{G}$ is called {\em trivial} if 
$\opn{Ob} \gerbe{G}(X) \neq \emptyset$.

Let $\mcal{G}$ be a sheaf of groups on $X$. By a {\em left
$\mcal{G}$-torsor} on
$X$ we mean a sheaf of sets $\mcal{S}$, with a left $\mcal{G}$-action, such
that $\mcal{S}$ is locally nonempty (i.e.\ each point $x \in X$ has an open
neighborhood $U$ such that $\mcal{S}(U) \neq \emptyset$), 
and for any $s \in \mcal{S}(U)$ the morphism of sheaves of sets
$\mcal{G}|_U \to \mcal{S}|_U$, $g \mapsto g \cdot s$, is an isomorphism. 
The torsor $\mcal{S}$ is trivial if $\mcal{S}(X) \neq \emptyset$. 

Suppose $\gerbe{G}$ is a gerbe on $X$. Given an open
set $U \subset X$ and $i \in \opn{Ob} \gerbe{G}(U)$, there is a sheaf of
groups $\gerbe{G}(i,i)$ on $U$. If $j \in \opn{Ob} \gerbe{G}(U)$
is some other object, then the sheaf of sets 
$\gerbe{G}(i,j)$ is a 
$\gerbe{G}(j,j)$-$\gerbe{G}(i,i)$-bitorsor. Namely, forgetting the
left action by $\gerbe{G}(j,j)$, the sheaf $\gerbe{G}(i,j)$ is a
right $\gerbe{G}(i,i)$-torsor; and vice versa.

We denote by $\bsym{\cat{Gerbe}}\, X$ the full sub-$2$-category of
$\bsym{\cat{PreStGr}}\, X$ gotten by taking all gerbes, all
$1$-morphisms between gerbes, and all $2$-morphisms between these $1$-morphisms.

Here are two prototypical examples of gerbes.

\begin{exa} \label{exa:15}
Let $\cat{I}$ be the groupoid with one object, say $0$, and with
$\cat{I}(0, 0) := \{ \bsym{1}_0 \}$, the trivial group.  
This groupoid is a terminal object in $\twocat{Cat}$, since any category
$\cat{C}$ admits exactly one functor $\cat{C} \to \cat{I}$. 

Now take a topological space $X$, and define a prestack $\gerbe{I}$ on it by
letting $\gerbe{I}(U) := \cat{I}$ for any open set $U$. 
Then $\gerbe{I}$ is a gerbe. The gerbe $\gerbe{I}$ is a terminal
object in $\bsym{\cat{PreStack}}\, X$. Indeed, given any prestack 
$\gerbe{G}$ on $X$ there is a unique morphism of prestacks
$\gerbe{G} \to \gerbe{I}$. We call $\gerbe{I}$ the {\em terminal gerbe}
(because the word ``trivial'' is over-used in this area).  
\end{exa}

\begin{exa} \label{exa:16}
Let $\mcal{G}$ be a sheaf of groups on $X$. For an open set $U$ let
$\cat{Tors}(\mcal{G}|_U)$ be the set of all left $\mcal{G}|_U$-torsors.
This is a groupoid. Given $V \subset U$ there is a functor
\[ \cat{Tors}(\mcal{G}|_U) \to \cat{Tors}(\mcal{G}|_V) , \]
namely $\mcal{S} \mapsto \mcal{S}|_V$. Thus we obtain a prestack of groupoids
$\twocat{Tors} \mcal{G}$ with
\[ (\twocat{Tors} \mcal{G})(U) := \cat{Tors}(\mcal{G}|_U) . \]
Since torsors are locally trivial it follows that 
$\twocat{Tors} \mcal{G}$ is a gerbe, called the {\em gerbe of
$\mcal{G}$-torsors}.
\end{exa}

\begin{rem}
A prestack of groupoids $\gerbe{G}$ is sometimes called a {\em
category fibered in groupoids} over $\cat{Open} X$. 
More precisely, given $\gerbe{G}$, we can construct a category
$\cat{G}$, together with a functor $\Phi : \cat{G} \to \cat{Open} X$
called the fiber functor. The set of objects of $\cat{G}$ is
\[ \opn{Ob} \cat{G} := 
\coprod_{U \in \cat{Open} X} \opn{Ob} \gerbe{G}(U) . \]
For objects $i \in \opn{Ob} \gerbe{G}(U)$ and
$j \in \opn{Ob} \gerbe{G}(V)$ one defines 
\[ \opn{Hom}_{\cat{G}}(i, j) := 
\opn{Hom}_{\gerbe{G}(U)}(i, j|_U) \]
if $U \subset V$; and 
$\opn{Hom}_{\cat{G}}(i, j) := \emptyset$ otherwise. 
The fiber functor $\Phi : \cat{G} \to \cat{Open} X$ is
$\Phi(i) := U$ for $i \in \opn{Ob} \gerbe{G}(U)$, and
$\Phi(g) := (U \to V)$ for 
$g \in \opn{Hom}_{\cat{G}}(i, j)$ as above.

Conversely, the prestack $\gerbe{G}$ can be recovered from the data
$\Phi : \cat{G} \to \cat{Open} X$.

For stacks of groupoids arising from moduli problems it is often more
natural to use the fibered category approach (cf.\ \cite{LMB}); but
for our applications in \cite{Ye}, the pseudofunctor approach is more
suitable.
\end{rem}

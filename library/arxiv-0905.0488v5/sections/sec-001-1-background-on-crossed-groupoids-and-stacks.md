---
doc_id: arxiv-0905.0488v5
doc_title: "TWISTED DEFORMATION QUANTIZATION OF ALGEBRAIC VARIETIES"
section_id: sec-001-1-background-on-crossed-groupoids-and-stacks
section_title: "Background on Crossed Groupoids and Stacks"
section_number: 1
pages: 11-15
source_pdf: 0905.0488v5.pdf
source_sha256: fcf8dee7cd3849b9
toc_source: outline
text_source: latex
latex_prose_ratio: 0.989
latex_coverage_ratio: 0.954
doc_brief: "TWISTED DEFORMATION QUANTIZATION OF ALGEBRAIC VARIETIES — Let X be a smooth algebraic variety over a ﬁeld K containing the real numbers. We introduce the notion of twisted associative (resp."
---
\label{sec:back}
\numberwithin{equation}{section}

In this paper we work a lot with stacks on topological spaces. The reader can
consult our earlier paper \cite{Ye4}, that contains a pretty detailed account
of $2$-categories, stacks and gerbes, with the same notation (Sections 1-2 of
that paper). 

Regarding set theoretic considerations, we employ Grothendieck universes. We 
consider a universe $\cat{U}$, that we call the small universe. Elements of
$\cat{U}$ are called small sets. By default all groups, rings etc.\ are small,
i.e.\ their underlying sets are small. And by default all categories $\cat{C}$
are $\cat{U}$-categories, i.e.\ $\opn{Ob}(\cat{C}) \subset \cat{U}$, and 
$\opn{Hom}_{\cat{C}}(i, j) \in \cat{U}$
for all $i, j \in \opn{Ob}(\cat{C})$.  Thus $\cat{Set}$, $\cat{Grp}$ etc.\
denote the categories of small sets, small groups etc., and they are
$\cat{U}$-categories. However some of the categories will be small categories;
a category $\cat{C}$ is small if $\opn{Ob}(\cat{C})$ is a small set.
There is also a universe $\cat{V}$, that we call the big universe, and 
$\cat{U}$ is an element of $\cat{V}$. Elements of $\cat{V}$ will be called big
sets. The $2$-category 
$\twocat{Cat}$ of all $\cat{U}$-categories is a $\cat{V}$-category (namely 
$\opn{Ob}(\twocat{Cat}) \subset \cat{V}$).  

Recall that a {\em groupoid} is a category in which all morphisms are
invertible. Given a groupoid $G$ and objects $i, j \in \opn{Ob}(G)$
we usually write
$G(i, j) := \opn{Hom}_{G}(i, j)$,
the set of morphisms from $i$ to $j$; and 
$G(i) := G(i, i)$, the automorphism group of the object $i$. 

\begin{dfn} \label{dfn:204}
Let $G$ be a groupoid.
\begin{enumerate}
\item Let $i, j \in \opn{Ob} (G)$ and $g \in G(i, j)$.  We define an isomorphism
of groups
\[ \opn{Ad}_{G}(g) : G(i) \iso G(j)  \]
by the formula
$\opn{Ad}_{G}(g)(h) := g \circ h \circ g^{-1}$
for $h \in G(i)$. 

\item The functor 
$\opn{Aut}_{G} : G \to \cat{Grp}$
is defined as follows: on objects $\opn{Aut}_{G}(i) := G(i)$, and on morphisms 
$\opn{Aut}_{G}(g) := \opn{Ad}_{G}(g)$. 

\item Let $H$ be another groupoid, and let $\Phi : G \to H$ be a functor. 
Define the natural transformation 
\[ \opn{Aut}_{\Phi} : \opn{Aut}_{G} \twoto \opn{Aut}_{H} \circ \, \Phi \]
of functors $G \to \cat{Grp}$ to be the group homomorphism
$\opn{Aut}_{\Phi} := \Phi : G(i) \to H(\Phi(i))$, for $i \in \opn{Ob}(G)$.
\end{enumerate} 
\end{dfn}

Suppose $G$ and $N$ are groupoids, such that 
$\opn{Ob}(N) = \opn{Ob}(G)$. 
An {\em action} $\Psi$ of $G$ on 
$N$ is a collection of group isomorphisms 
$\Psi(g) : N(i) \iso N(j)$
for all $i, j \in \opn{Ob}(G)$ and $g \in G(i, j)$, 
such that 
$\Psi(h \circ g) = \Psi(h) \circ \Psi(g)$
whenever $g$ and $h$ are composable, and 
$\Psi(1_i)$ is the identity automorphism of the group $N(i)$. 
The prototypical example is the action $\opn{Ad}_{G}$ of $G$ on itself. 

\begin{dfn} \label{dfn:cosim.101}
A {\em crossed groupoid} is a structure 
\[ G = 
( G_1, G_2, 
\opn{Ad}_{G_1 \crvar G_{2}}, \opn{D} ) \]
consisting of:
\begin{itemize}
\item Groupoids $G_1$ and $G_2$, such that 
$G_2$ is totally disconnected, and 
$\opn{Ob}(G_1) = \opn{Ob}(G_2)$. 
We write $\opn{Ob}(G) := \opn{Ob}(G_1)$. 

\item An action $\opn{Ad}_{G_1 \crvar G_{2}}$ of 
$G_1$ on $G_2$, called the {\em twisting}. 

\item A morphism of groupoids (i.e.\ a functor) 
$\opn{D} : G_2 \to G_1$
called the {\em feedback}, which is the identity on objects.
\end{itemize}

These are the conditions:
\begin{enumerate}
\rmitem{i} The morphism $\opn{D}$ is $G_1$-equivariant with respect to
the actions $\opn{Ad}_{G_1 \crvar G_{2}}$ and
$\opn{Ad}_{G_1}$. Namely 
\[ \opn{D}(\opn{Ad}_{G_1 \crvar G_{2}}(g)(a)) =
\opn{Ad}_{G_1}(g)(\opn{D}(a)) \]
in the group $G_1(j)$, for any $i, j \in \opn{Ob}(G)$, 
$g \in G_1(i, j)$ and $a \in G_2(i)$.

\rmitem{ii} For any $i \in \opn{Ob}(G)$ and 
$a \in G_2(i)$ there is equality
\[ \opn{Ad}_{G_1 \crvar G_{2}}(\opn{D}(a)) =
\opn{Ad}_{G_2(i)}(a) , \]
as automorphisms of the group $G_2(i)$.
\end{enumerate}
\end{dfn}

We sometimes refer to morphisms in the groupoid $G_1$ as {\em
$1$-morphisms}, and to the morphisms in $G_2$ as {\em
$2$-morphisms}. 

For later use we record the next facts (that are almost immediate from the
definitions). 

\begin{prop} \label{prop:200}
Let 
$G = ( G_1, G_2, \opn{Ad}_{G_1 \crvar G_{2}}, \opn{D} )$
be a crossed groupoid. 
\begin{enumerate}
\item For $i \in \opn{Ob}(G)$ let $\opn{IG}(i) := G_2(i)$, and for 
$g \in G_1(i, j)$ let 
$\opn{IG}(g) := \opn{Ad}_{G_1 \crvar G_{2}}(g)$. 
Then 
$\opn{IG} : G_1 \to \cat{Grp}$
is a functor. 

\item For $i \in \opn{Ob}(G)$ and $a \in \opn{IG}(i)$ let 
$\opn{ig}(a) := \opn{D}(a) \in G_1(i)$. Then 
$\opn{ig} : \opn{IG} \twoto \opn{Aut}_{G_1}$
is a natural transformation of functors $G_1 \to \cat{Grp}$. 

\item The data $( G_1, G_2, \opn{Ad}_{G_1 \crvar G_{2}}, \opn{D} )$
can be recovered from the groupoid $G_1$, the functor 
$\opn{IG} : G_1 \to \cat{Grp}$ and the 
 natural transformation 
$\opn{ig} : \opn{IG} \twoto \opn{Aut}_{G_1}$.
\end{enumerate}
\end{prop}

Proposition \ref{prop:200} suggests an alternative way to view the crossed 
groupoid $G = ( G_1, G_2, \opn{Ad}_{G_1 \crvar G_{2}}, \opn{D} )$.
We call $\opn{IG}(i) = G_2(i)$ the {\em inner gauge group} of the object $i$,
and its elements are also called {\em inner gauge transformations}. 
The group homomorphism 
$\opn{ig} = \opn{D} : \opn{IG}(i) \to G_1(i)$ is called the {\em inner action}. 
The morphisms in $G_1$ are also called {\em gauge transformations}. 
See Remark \ref{rem:cosim.101} regarding this point of view. 
Warning: the group
homomorphism $\opn{ig} = \opn{D}$
is usually not injective. 

Here are some examples of crossed groupoids.

\begin{exa} \label{exa:200}
Consider any groupoid $G_1$, and let $G_2$ be the totally disconnected
groupoid gotten from $G_1$ by removing all morphisms between distinct objects. 
(More generally one can take any normal subgroupoid $N \subset G_1$, in the
sense of \cite[Definition 3.1]{Ye4}, and define $G_2 := N$.)
Define the twisting  
$\opn{Ad}_{G_1 \crvar G_{2}} := {\opn{Ad}_{G_1}}|_{G_{2}}$,
and the feedback $\opn{D} : G_2 \to G_1$ is the inclusion. 
This is easily seen to be a crossed groupoid. 
\end{exa}

For a category $\cat{C}$ we denote by $\cat{C}^{\times}$ the subcategory having
all the objects of $\cat{C}$, and its morphisms are the isomorphisms of
$\cat{C}$. We call  $\cat{C}^{\times}$ the {\em groupoid of invertible
morphisms of $\cat{C}$}. 
Note that if $G$ is a groupoid, then any functor $G \to \cat{C}$ factors
through $\cat{C}^{\times}$.

\begin{exa} \label{exa:15}
Take the category $\cat{Grp}$ of small groups. We will make $\cat{Grp}^{\times}$
into a crossed groupoid  by introducing inner gauge groups. 
For a group $G$ let $\opn{IG}(G) := G$.
For a group isomorphism $\phi : G \to G'$ (i.e.\ for a morphism
$\phi \in \cat{Grp}^{\times}(G, G')$) we let 
$\opn{IG}(\phi) := \phi$. And for an element $g \in G$  we let
$\opn{ig}(g) := \opn{Ad}_G(g)$, i.e.\ conjugation.
Here the kernel of the homomorphism 
\[ \opn{ig} : \opn{IG}(G) = G = \cat{Grp}^{\times}_2(G)
\to \cat{Grp}^{\times}_1(G) = \opn{Aut}_{\cat{Grp}}(G) \]
is the center of the group $G$.
\end{exa}

\begin{exa} \label{exa:6}
Let $R$ be a commutative ring. Take the category $\cat{Assoc}(R)$
of associative unital $R$-algebras. Then $\cat{Assoc}^{\times}(R)$
is a crossed groupoid. 
The group of inner gauge transformations of an associative $R$-algebra $A$ is
the group $\opn{IG}(A) := A^{\times}$
of invertible elements. It is functorial, since a ring isomorphism 
$g : A \to A'$ sends invertible elements to invertible elements.
The inner action $\opn{ig}(a)$, for 
$a \in \opn{IG}(A)$, is conjugation by this invertible element, namely
$\opn{ig}(a)(a') = a \star a' \star a^{-1}$,
where $\star$ is the multiplication in $A$.
The conditions are very easy to verify.
\end{exa}

\begin{rem} \label{rem:cosim.101}
A crossed groupoid is better known as a 
{\em strict $2$-groupoid}, or a {\em crossed module over a groupoid}, or
as a {\em $2$-truncated crossed complex}; see \cite{Bw}. When
$\opn{Ob}(G)$ is a singleton then $G$ is just a crossed module. 
In earlier versions of this paper, and in \cite{Ye10}, we used the name 
{\em category with inner gauge groups}. A trace of this name remains
in the inner gauge groups $\opn{IG}$. 

We use different notation (fonts) for groupoids and crossed groupoids in this
paper, depending usually on their size. Thus $G$ will most likely be a small
groupoid, whereas $\cat{G}$ will be a big groupoid (i.e.\ a
$\cat{U}$-category).  

Traditionally papers used $2$-groupoid language to discuss descent (cf.\
\cite{BGNT1}). In this paper we realized that the crossed groupoid language is
more effective: geometric descent data comes naturally in terms of a
cosimplicial crossed groupoid (see Definition \ref{dfn:21}), and also the
Deligne construction (see Definition \ref{dfn:Lie-desc.101}) appears as a
crossed groupoid, so it is more natural to talk about the
{\em Deligne crossed groupoid}. 
\end{rem}

\begin{dfn}
Suppose 
$H = ( H_1, H_2, \opn{Ad}_{H_1 \crvar H_{2}}, \opn{D} )$ 
is another crossed groupoid. A {\em morphism of crossed groupoids}
$\Phi : G \to H$
is a pair of morphisms of groupoids 
$\Phi_p : G_p \to H_p$, $p = 1, 2$, that are equal on objects, 
and respect the twistings and the feedbacks. We denote by
$\cat{CrGrpd}$ the category consisting of crossed groupoids and morphisms
between them. 
\end{dfn}

\begin{dfn} \label{dfn:227}
A morphism of crossed groupoids $\Phi : G \to H$ is called an
{\em equivalence} if 
$\Phi_1 : G_1 \to H_1$ is an equivalence of groupoids, and for every
$i \in \opn{Ob}(G)$ the group homomorphism 
$\Phi_2 : G_2(i) \to H_2(\Phi_2(i))$ is bijective. 
\end{dfn}

Let $G$ be a crossed groupoid. We define the homotopy set 
$\bsym{\pi}_0(G) := \bsym{\pi}_0(G_1)$,
namely the set of isomorphism classes of objects of $G_1$.
The homotopy groups of $G$ are 
\[ \bsym{\pi}_1(G, i) := 
\opn{Coker} \bigl( \opn{D} : G_2(i) \to G_1(i) \bigr) \]
and
\[ \bsym{\pi}_2(G, i) := 
\opn{Ker} \bigl( \opn{D} : G_2(i) \to G_1(i) \bigr) \]
for $i \in \opn{Ob}(G)$.
The set $\bsym{\pi}_0(G)$ and the groups $\bsym{\pi}_p(G, i)$ are
functorial in $G$. 

\begin{dfn} \label{dfn:equiv-cosim.102}
A morphism of crossed groupoids $\Phi : G \to H$  
is called a {\em weak equivalence} if the function
$\bsym{\pi}_0(\Phi)  : \bsym{\pi}_0(G) \to \bsym{\pi}_0(H)$
is bijective, and the group homomorphisms
$\bsym{\pi}_p(\Phi, i) : \bsym{\pi}_p(G, i) \to \bsym{\pi}_p(H, \Phi(i))$
are bijective for all $i \in \opn{Ob}(G)$ and 
$p \in \{ 1, 2 \}$.
\end{dfn}

Of course if $\Phi$ is an equivalence then it is a weak equivalence.

\begin{dfn} \label{dfn:200}
Let $X$ be a topological space. A {\em stack of crossed groupoids} 
\[ \twocat{P} = ( \twocat{P}_1, \twocat{P}_2, 
\opn{Ad}_{\twocat{P}_1 \crvar \twocat{P}_{2}}, \opn{D} ) \]
on $X$ consists of a crossed groupoid 
\[ \twocat{P}(U) = \bigl( \twocat{P}_1(U), \twocat{P}_2(U), 
\opn{Ad}_{\twocat{P}_1(U) \crvar \twocat{P}_2(U)}, \opn{D} \bigr) \]
for every open set $U \subset X$, with a morphism of crossed
groupoids 
\[ \mrm{rest}^{}_{V / U} : \twocat{P}(U) \to \twocat{P}(V) , \]
called {\em restriction},
for every inclusion $V \subset U$ of open sets. 
The three conditions below have to hold:
\begin{enumerate}
\rmitem{i} The restriction morphisms satisfy 
$\mrm{rest}^{}_{W / V} \circ \mrm{rest}^{}_{V / U} = \mrm{rest}^{}_{W / U}$
for a double inclusion $W \subset V \subset U$ of open sets of $X$.

\rmitem{ii} The prestack of groupoids 
$\twocat{P}_1 : U \mapsto \twocat{P}_1(U)$
on $X$ is a stack. 

\rmitem{iii} For every open set $U$ and object 
$\mcal{A} \in \opn{Ob}(\twocat{P}(U))$, the presheaf of groups 
\[ \twocat{P}_2(\mcal{A}) : V \mapsto 
\twocat{P}_2(V)(\mrm{rest}^{}_{V / U}(\mcal{A}))  \]
on $U$ is a sheaf.  
\end{enumerate}
\end{dfn}

Condition (i) says that the stack $\twocat{P}_1$ is {\em split}, i.e.\ it is a
cat\'egorie fibr\'ee scind\'ee, in the sense of \cite{Gi}. 

\begin{dfn} \label{dfn:203}
Let $\twocat{P}$ be a stack of crossed groupoids on $X$.
\begin{enumerate}
\item An object $\mcal{A} \in \opn{Ob}(\twocat{P}(U))$, for some open set $U$,
is
called a {\em local object} of $\twocat{P}$.

\item Let $\mcal{A} \in \opn{Ob}(\twocat{P}(U))$,  and let $V \subset U$. 
We write $\mcal{A}|_V := \mrm{rest}^{}_{V / U} (\mcal{A})$.

\item Let $\mcal{A} \in \opn{Ob}(\twocat{P}(U))$ and
$\mcal{A}' \in \opn{Ob}(\twocat{P}(U'))$ 
be local objects of $\twocat{P}$, and let $V \subset U \cap U'$.
An element $g \in \twocat{P}_1(V)(\mcal{A}|_V, \mcal{A}'|_V)$
is called a {\em local $1$-morphism} of $\twocat{P}$; and 
an element $a \in \twocat{P}_2(V)(\mcal{A}|_V)$
is called a {\em local $2$-morphism} of $\twocat{P}$.

\item For a local object $\mcal{A}$ of $\twocat{P}$ we denote by
$\opn{IG}(\mcal{A})$ the sheaf of groups $\twocat{P}_2(\mcal{A})$
from condition (iii) in Definition \ref{dfn:200};
and we denote by 
$\opn{ig} : \opn{IG}(\mcal{A}) \to \twocat{P}_1(\mcal{A})$ 
the homomorphism of sheaves of groups induces by the feedbacks $\opn{D}$. 
\end{enumerate}
\end{dfn}

We denote by $\twocat{Grp}(X)$ the {\em stack of sheaves of groups} on $X$. 
It is the stack of categories that assigns
to each open set $U$ the category 
$\twocat{Grp}(X)(U) := \cat{Grp}(U)$
of sheaves of small groups on $U$. The restriction morphisms here are
restrictions of sheaves.

For any stack of groupoids $\twocat{P}$ on $X$ there is a functor of stacks 
$\opn{Aut}_{\twocat{P}} : \twocat{P} \to \twocat{Grp}(X)$,
which is the geometrization of Definition \ref{dfn:204}(2). 
Like Proposition \ref{prop:200} we have:

\begin{prop} \label{prop:201}
Let $\twocat{P}$ be a stack of crossed groupoids on $X$.
\begin{enumerate}
\item $\opn{IG} : \twocat{P}_1 \to \twocat{Grp}(X)$ is a functor of stacks 
on $X$.

\item $\opn{ig} : \opn{IG} \twoto \opn{Aut}_{\twocat{P}_1}$
is a natural transformation between functors of stacks
$\twocat{P}_1 \to \twocat{Grp}(X)$.

\item The data 
$( \twocat{P}_1, \twocat{P}_2, \opn{Ad}_{\twocat{P}_1 \crvar \twocat{P}_{2}},
\opn{D} )$
can be recovered from the stack of groupoids $\twocat{P}_1$, the functor of
stacks 
$\opn{IG} : \twocat{P}_1 \to \twocat{Grp}(X)$ and the natural transformation 
$\opn{ig} : \opn{IG} \twoto \opn{Aut}_{\twocat{P}_1}$.
\end{enumerate}
\end{prop}

\begin{proof}
Again this is immediate from the definitions, but here the details are of
course much more complicated than in Proposition \ref{prop:200}.
It is good to look up \cite[Section 2]{Ye4} for detailed definitions and
notation. 
\end{proof}

\begin{exa}
This is the geometric version of Example \ref{exa:200}.
Suppose $\gerbe{G}$ is a gerbe on $X$, and $\gerbe{N}$ is a normal subgroupoid
on $\gerbe{G}$, in the sense of \cite[Definition 3.6]{Ye4}.
Then there is a stack of crossed groupoids $\twocat{P}$ on $X$, with 
$\twocat{P}_1 := \gerbe{G}$, $\twocat{P}_2 := \gerbe{N}$,
$\opn{Ad}_{\twocat{P}_1 \crvar \twocat{P}_{2}} :=
{\opn{Ad}_{\gerbe{G}}}|_{\gerbe{N}}$,
and $\opn{D} : \twocat{P}_1 \to \twocat{P}_{2}$ is the inclusion. 
\end{exa}

\begin{exa} \label{exa:9}
This is the geometric version of Example \ref{exa:15}.
On any open set $U \subset X$ we have the crossed groupoid 
$\cat{Grp}^{\times}(U)$, in which the objects are the sheaves of groups
$\mcal{G}$ on $U$; the $1$-morphisms are the isomorphisms of sheaves of groups;
and the $2$-morphisms are the elements of $\Gamma(U, \mcal{G})$. 
The twisting and feedback are as in Example \ref{exa:15}.
As $U$ varies we obtain a stack of crossed groupoids
$\twocat{Grp}^{\times}(X)$.
\end{exa}

\begin{exa} \label{exa:10}
This is the geometric version of Example \ref{exa:6}.
Take a commutative ring $R$. For an open set
$U \subset X$ denote by $\cat{Assoc}(R, U)$ the category 
of sheaves of associative $R$-algebras on $U$. As $U$ varies we get 
$\twocat{Assoc}(R, X)$, the {\em stack of sheaves of associative $R$-algebras on
$X$}. Inside $\twocat{Assoc}(R, X)$ we have the stack of groupoids 
$\twocat{Assoc}^{\times}(R, U)$, in which we take only the invertible
morphisms. The latter can be made into a stack of crossed groupoids by taking
$\opn{IG}(\mcal{A}) := \mcal{A}^{\times}$, the sheaf of invertible elements. 
\end{exa}

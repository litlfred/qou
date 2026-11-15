---
doc_id: arxiv-0801.0083v4
doc_title: "CENTRAL EXTENSIONS OF GERBES"
section_id: sec-003-3-extensions-of-gerbes
section_title: "Extensions of Gerbes"
section_number: 3
pages: 12-19
source_pdf: 0801.0083v4.pdf
source_sha256: 8e38b9e56d246709
toc_source: outline
text_source: latex
latex_prose_ratio: 0.993
latex_coverage_ratio: 0.99
doc_brief: "CENTRAL EXTENSIONS OF GERBES — We introduce the notion of central extension of gerbes on a topo- logical space X."
---
\label{sec.ext}

We begin by taking certain basic notions about groups (such as normal subgroup
and center) and generalizing them to groupoids. 
As a matter of convenience we often refer to a functor 
$F : \cat{G} \to \cat{H}$ 
between groupoids as a morphism. (Indeed this is a $1$-morphism in the 
$2$-category $\twocat{Groupoid}$ of groupoids.)

\begin{dfn} \label{dfn:3}
Let $\cat{G}$ be a groupoid. A {\em normal subgroupoid} of $\cat{G}$ is a
subgroupoid $\cat{N}$ satisfying the following three conditions. 
\begin{enumerate}
\rmitem{i} $\opn{Ob} \cat{N} = \opn{Ob} \cat{G}$.
\rmitem{ii} For every $i, j \in \opn{Ob} \cat{G}$ and 
$g \in \cat{G}(i, j)$ there is equality
\[ \opn{Ad}(g) \bigl( \cat{N}(i, i) \bigr)  = \cat{N}(j, j) . \]

\rmitem{iii} $\cat{N}$ is totally disconnected, i.e.\ 
$\cat{N}(i, j) = \emptyset$ for $i \neq j$.
\end{enumerate}
\end{dfn}

In particular for every $i \in \opn{Ob} \cat{G}$ the
group $\cat{N}(i, i)$ is normal subgroup of the automorphism group 
$\cat{G}(i, i)$. 

Note that a normal subgroupoid $\cat{N}$ is the same as a collection 
$\{ N_i \}_{i \in \opn{Ob} \cat{G}}$ 
of subgroups $N_i \subset \cat{G}(i, i)$, satisfying the obvious variant of
condition (ii). 

The {\em trivial normal subgroupoid} of $\cat{G}$ is the normal subgroupoid
$\cat{N}$ for which all the groups $\cat{N}(i, i)$ are trivial; namely 
$\cat{N}(i, i) = \{ \bsym{1}_i \}$.

Let  $F : \cat{G} \to \cat{H}$ be a morphism of groupoids. 
For $i \in \opn{Ob} \cat{G}$ let
\[ \opn{Ker}(F)(i, i) := \opn{Ker} \bigl( F : \cat{G}(i,i) \to 
\cat{H} ( F(i), F(i) ) \bigr) . \]
This is a normal subgroup of $\cat{G}(i, i)$. 
Moreover, an easy calculation shows that the collection of subgroups 
$\{ \opn{Ker}(F)(i, i) \}_{i \in \opn{Ob} \cat{G}}$ 
is a normal subgroupoid of $\cat{G}$, which we denote by 
$\opn{Ker}(F)$. 

\begin{dfn}
Let $F : \cat{G} \to \cat{H}$ be a morphism of groupoids. We say that 
$F$ is a {\em weak epimorphism} if it satisfies these conditions:
\begin{enumerate}
\rmitem{i} $F$ is essentially surjective objects. Namely for any
$j \in \opn{Ob} \cat{H}$ there exists some $i \in \opn{Ob} \cat{G}$ such that
$\cat{H}(F(i), j) \neq \emptyset$.
\rmitem{ii} $F$ is surjective on sets of morphisms. This means that for any
$i, j \in \opn{Ob} \cat{G}$ the function
\[ F : \cat{G}(i, j) \to \cat{H} \bigl( F(i), F(j) \bigr) \]
is surjective.
\end{enumerate}
\end{dfn}

Observe that if $F : \cat{G} \to \cat{H}$ is a weak epimorphism whose kernel 
$\opn{Ker}(F)$ is the trivial normal subgroupoid of $\cat{G}$, then $F$ is an
equivalence.

\begin{dfn}
By an {\em extension of groupoids} we mean a diagram of morphisms of groupoids
\[ \cat{N} \xar{E} \cat{G} \xar{F} \cat{H} , \]
such that $F$ is a weak epimorphism,  
$\cat{N} = \opn{Ker}(F)$, and $E : \cat{N} \to \cat{G}$ is the inclusion.
\end{dfn}

By analogy with the case of groups we often write
\begin{equation} \label{eqn:20}
1 \to \cat{N} \to \cat{G} \xar{F} \cat{H} \to 1  
\end{equation}
for an extension of groupoids. But this is only a suggestive notation -- we do
not view the symbols ``$1$'' as groupoids. (We could, but then the first $1$
has to be replaced by the trivial normal subgroupoid of $\cat{G}$, and
the second $1$ by the terminal groupoid of Example \ref{exa:15}.)

Extensions of groupoids behave very much like extensions of groups. 
Suppose $\cat{G}$ is a groupoid and $\cat{N} \subset \cat{G}$ is a normal
subgroupoid. Then there is an extension of groupoids (\ref{eqn:20}). 
The groupoid $\cat{H}$ in this extension is unique up to equivalence.
One could choose $\cat{H}$ such that the function
$F : \opn{Ob} \cat{G} \to \opn{Ob} \cat{H}$ is bijective; and that would make 
$\cat{H}$ unique up to isomorphism.

Next suppose 
$F : \cat{G} \to \cat{H}$,
$F' : \cat{G}' \to \cat{H}'$ and 
$D : \cat{G} \to \cat{G}'$ are morphisms of groupoids, such that 
$D \bigl( \opn{Ker}(F) \bigr) \subset \opn{Ker}(F')$. 
Then there is a morphism of groupoids
$E : \cat{H} \to \cat{H}'$, unique up to $2$-isomorphism, such that the
diagram
\[ \UseTips \xymatrix @C=5ex @R=5ex {
\cat{G}
\ar[r]^{F}
\ar[d]_{D}
& 
\cat{H}
\ar[d]^{E}
\\
\cat{G}'
\ar[r]_{F'}
& 
\cat{H}'
}  \]
commutes up to $2$-isomorphism. 

Now consider a groupoid $\cat{G}$. 
For any $i \in \opn{Ob} \cat{G}$ we have the center
$\opn{Z}(\cat{G}(i, i))$ of the automorphism group
$\cat{G}(i, i)$. 
Given any pair of objects
$i, j \in \opn{Ob} \cat{G}$, and any isomorphism
$g \in \cat{G}(i, j)$, we have
\[ \opn{Ad}(g) \bigl( \opn{Z}(\cat{G}(i, i)) \bigr)  = 
\opn{Z}(\cat{G}(j, j)) . \]
Therefore the collection of subgroups 
$\{ \opn{Z}(\cat{G}(i, i)) \}_{i \in \opn{Ob} \cat{G}}$ 
is a normal subgroupoid of $\cat{G}$, 
which we denote by $\opn{Z}(\cat{G})$, and call the {\em center} of $\cat{G}$.

\begin{dfn}
\begin{enumerate}
\item  Let $\cat{G}$ be a groupoid. A {\em central subgroupoid} of
$\cat{G}$ is any normal subgroupoid $\cat{N}$ that is contained in
$\opn{Z}(\cat{G})$.
\item A {\em central extension of groupoids} is an extension of groupoids
(\ref{eqn:20}) such that $\cat{N}$ is a central subgroupoid of $\cat{G}$.
\end{enumerate}
\end{dfn}

Suppose $\cat{G}$ is a nonempty and connected groupoid, and 
$\cat{N}$ is a central subgroupoid of $\cat{G}$. 
Take any $i, j \in \opn{Ob} \cat{G}$ and
$g, g' \in \cat{G}(i, j)$. Then the group isomorphisms
\[ \opn{Ad}(g) , \opn{Ad}(g') : \cat{N}(i, i) \to \cat{N}(j, j) \]
are equal. In this way we can canonically identify the abelian groups 
$\cat{N}(i, i)$, for $i \in \opn{Ob} \cat{G}$, and view them as a single abelian
group.

When we are given a central extension of groupoids (\ref{eqn:20})
in which $\cat{G}$ is nonempty and connected, we can replace the 
central subgroupoid $\cat{N}$ by a single abelian group $N$ as explained above,
and the extension becomes
\[ 1 \to N \to \cat{G} \xar{F} \cat{H} \to 1 . \]

So far for the discrete situation; now we geometrize. 
Let $X$ be a topological space. 
Suppose $\gerbe{G}$ is a gerbe on $X$. 
By a local object $i$ of $\gerbe{G}$ we mean an object
$i \in \opn{Ob} \gerbe{G}(U)$ for some open set $U \subset X$. 
If $i, j$ are two local objects, defined on open sets $U, V$ respectively, then
by $\gerbe{G}(i,j)$ we mean the corresponding sheaf of isomorphisms on 
$U \cap V$. By a local isomorphism $g : i \iso j$
we mean an isomorphism 
$g \in \gerbe{G}(i,j)(W)$ for some open set 
$W \subset U \cap V$. 
Such $g$ gives rise to an isomorphism of sheaves of groups
\[ \opn{Ad}(g) : \gerbe{G}(i,i)|_W \iso \gerbe{G}(j,j)|_W . \]

\begin{dfn} \label{dfn.9}
Let $\gerbe{G}$ be a gerbe on $X$. A {\em normal subprestack of groupoids}
of $\gerbe{G}$ is a subprestack $\gerbe{N}$ of $\gerbe{G}$
with these two properties:
\begin{itemize}
\rmitem{i} For every open set $U$ the category 
$\gerbe{N}(U)$ is a normal subgroupoid of $\gerbe{G}(U)$
(see Definition \ref{dfn:3}). In particular
$\opn{Ob} \gerbe{N}(U) = \opn{Ob} \gerbe{G}(U)$, and
$\gerbe{N}(U)$ is totally disconnected. 

\rmitem{ii} For every local object $i$ of $\gerbe{N}$ the presheaf
$\gerbe{N}(i, i)$ is a sheaf. 
\end{itemize}

Since the full name is too long, we simply call such $\gerbe{N}$ a 
 {\em normal subgroupoid} of $\gerbe{G}$.
\end{dfn}

Here is what the definition amounts to. For every local object $i$ of 
$\gerbe{G}$ there is a subsheaf of groups 
$\gerbe{N}(i, i) \subset \gerbe{G}(i, i)$. The condition is that for any
local objects $i$ and $j$, and any local isomorphism 
$g : i \to j$, one has
\[ \opn{Ad}(g) \bigl( \gerbe{N}(i, i) \bigr) = \gerbe{N}(j, j) . \]

Warning: a normal subgroupoid of a gerbe is usually not a gerbe, nor even a
stack. 

\begin{prop} \label{prop:13}
Given a morphism of gerbes $F : \gerbe{G} \to \gerbe{H}$, there is a unique 
normal subgroupoid $\gerbe{N}$ of $\gerbe{G}$ such that 
\[ \gerbe{N}(U) = 
\opn{Ker} \bigl( F : \gerbe{G}(U) \to \gerbe{H}(U) \bigr) \]
for every open set $U$. 
\end{prop}

\begin{proof}
The formula defines a subprestack of groupoids $\gerbe{N}$ of $\gerbe{G}$.
We know that the groupoid $\gerbe{N}(U)$ is normal in $\gerbe{G}(U)$. 
And for any local object $i$ of $\gerbe{G}$ we have 
\[  \gerbe{N}(i, i) = \opn{Ker} \bigl( F : \gerbe{G}(i,i) \to 
\gerbe{H} \bigl( F(i), F(i) \bigr) \bigr)  \]
as presheaves, so $\gerbe{N}(i, i)$ a sheaf. 
\end{proof}

\begin{dfn}
The normal subgroupoid $\gerbe{N}$ in the proposition above is called the
{\em kernel} of $F$, and it is denoted by $\opn{Ker}(F)$
\end{dfn}

\begin{dfn}
Let $F : \gerbe{G} \to \gerbe{H}$ be a morphism of gerbes. We say that 
$F$ is a {\em weak epimorphism} if it satisfies these conditions:
\begin{enumerate}
\rmitem{i} $F$ is {\em locally essentially surjective on objects}. 
Recall that this says that for any open set $U \subset X$,
object $j \in \opn{Ob} \gerbe{H}(U)$ and point $x \in U$, there is an open
set $V$ with $x \in V \subset U$, an object 
$i \in \opn{Ob} \gerbe{G}(V)$, and an isomorphism
$h : F(i) \iso j$ in $\gerbe{H}(V)$. 

\rmitem{ii} $F$ is {\em surjective on isomorphism sheaves}. This says that for
any $i, j \in \opn{Ob} \gerbe{G}(U)$
the map of sheaves of sets
\[ F : \gerbe{G}(i, j) \to \gerbe{H}
\bigl( F(i), F(j) \bigr) \]
is surjective. 
\end{enumerate}
\end{dfn}

Note that if $F: \gerbe{G} \to \gerbe{H}$ is a weak epimorphism such that
$\opn{Ker}(F)$ is the trivial normal subgroupoid of $\gerbe{G}$, then 
$F$ is a weak equivalence, and hence it is an equivalence.

\begin{dfn} \label{dfn:1} 
An {\em extension of gerbes} is a diagram
\[  \gerbe{N} \xar{E} \gerbe{G} \xar{F} \gerbe{H}  \]
of morphisms in $\twocat{PreStGr} X$, such that $\gerbe{G}$ and $\gerbe{H}$
are gerbes, $F$ is a weak epimorphism,  
$\gerbe{N} = \opn{Ker}(F)$, and $E : \gerbe{N} \to \gerbe{G}$ is the inclusion.
\end{dfn}

We often use the notation of ``exact sequence''
\begin{equation} \label{eqn:21}
1 \to  \gerbe{N} \to \gerbe{G} \xar{F} \gerbe{H} \to 1  
\end{equation}
for an extension of gerbes. 

\begin{dfn} \label{dfn.5}
A {\em morphism of extensions of gerbes} is a diagram
\[ \UseTips \xymatrix @C=5ex @R=5ex {
\gerbe{N}
\ar[r]
\ar[d]
&
\gerbe{G}
\ar[r]^{F}
\ar[d]_{D}
& 
\gerbe{H}
\ar[d]_{E}
\\
\gerbe{N}'
\ar[r]
&
\gerbe{G}'
\ar[r]_{F'}
& 
\gerbe{H}'
}  \]
of morphisms in $\twocat{PreStGr} X$, 
where the rows are extensions of gerbes,
the  square on the right is commutative up to $2$-isomorphism,
and the square on the left is commutative.
We denote this morphism of extensions by $(D, E)$. 
\end{dfn}

\begin{thm} \label{thm:1} 
Let $\gerbe{G}$ be a gerbe on $X$, and let
$\gerbe{N}$ be a normal subgroupoid of $\gerbe{G}$. Then there exists
a gerbe $\gerbe{G} / \gerbe{N}$, 
and a morphism of gerbes
$F : \gerbe{G} \to \gerbe{G} / \gerbe{N}$,
with the following properties:
\begin{enumerate}
\rmitem{i} The diagram
\[ 1 \to  \gerbe{N} \to \gerbe{G} \xar{F}
\gerbe{G} / \gerbe{N} \to 1 \]
is an extension of gerbes.

\rmitem{ii} Suppose 
\[ 1 \to  \gerbe{N}' \to \gerbe{G}' \xar{F'}
\gerbe{H}' \to 1  \]
is an extension of gerbes, and 
$D : \gerbe{G} \to \gerbe{G}'$
is a morphism of gerbes, such that 
$D(\gerbe{N}) \subset \gerbe{N}'$. Then there is a 
morphism gerbes 
$E : \gerbe{G} / \gerbe{N} \to \gerbe{H}'$,
unique up to $2$-isomorphism, such that the diagram
\[ \UseTips \xymatrix @C=5ex @R=5ex {
1 
\ar[r]
&
\gerbe{N}
\ar[r]
\ar[d]
&
\gerbe{G}
\ar[r]^{F}
\ar[d]_{D}
& 
\gerbe{G} / \gerbe{N} 
\ar[r]
\ar[d]_{E}
& 
1
\\
1 
\ar[r]
&
\gerbe{N}'
\ar[r]
&
\gerbe{G}'
\ar[r]_{F'}
& 
\gerbe{H}'
\ar[r]
& 
1
}  \]
is a morphism of extensions.

\rmitem{iii} In the situation of property \tup{(ii)}, assume the morphism 
$D : \gerbe{G} \to \gerbe{G}'$ is an equivalence, and the sheaf
homomorphisms
\[ D : \gerbe{N}(i, i) \to \gerbe{N}' \bigl( F(i), F(i) \bigr) \]
are isomorphisms for all local objects $i$ of $\gerbe{G}$. Then $E$ is also an
equivalence.
\end{enumerate}
\end{thm}

Before giving the proof we need some preliminary work. 
Let $U \subset X$ be an open set, and let
$i, j \in \opn{Ob} \gerbe{G}(U)$. The sheaf of sets 
$\gerbe{G}(i, j)$ is a right $\gerbe{G}(i, i)$-torsor on $U$, and
hence it has a right action by the sheaf of groups
$\gerbe{N}(i, i)$. Let
$\bar{\gerbe{G}}(i, j)$ be the sheaf of sets on $U$ associated to the
presheaf
\[ V \mapsto \gerbe{G}(V)(i, j) \, / \, \gerbe{N}(V)(i, i) . \]
There is a surjective sheaf morphism
$\gerbe{G}(i, j) \to \bar{\gerbe{G}}(i, j)$.
If $i = j$ we get a sheaf of groups
$\bar{\gerbe{G}}(i, i)$.

\begin{lem} \label{lem.3} 
There is a unique structure of 
$\bar{\gerbe{G}}(j, j)$-$\bar{\gerbe{G}}(i, i)$-bitorsor
on $\bar{\gerbe{G}}(i, j)$, such that the surjection 
$\gerbe{G}(i, j) \to \bar{\gerbe{G}}(i, j)$ is 
$\gerbe{G}(j, j) \times \gerbe{G}(i, i)$ -equivariant.
\end{lem}

\begin{proof}
Uniqueness is clear. For existence, we have to exhibit a suitable action of the
sheaf of groups 
$\bar{\gerbe{G}}(j, j) \times \bar{\gerbe{G}}(i, i)$
on the sheaf of sets $\bar{\gerbe{G}}(i, j)$. Because of uniqueness, this
is a local question. 

Choose an open set $V \subset X$ that trivializes the bitorsor 
$\gerbe{G}(i, j)$; namely there is some
$g \in \gerbe{G}(i, j)(V)$. 
Then the left action of
$\gerbe{G}(j, j)|_{V}$ on $\gerbe{G}(i, j)|_{V}$
coincides with the right action of $\gerbe{G}(i, i)|_{V}$, via 
the isomorphism of sheaves of groups
\[ \opn{Ad}(g) : \gerbe{G}(i, i)|_{V} \iso 
\gerbe{G}(j, j)|_{V} . \]
Also we have a torsor isomorphism
\[ \gerbe{G}(i, i)|_{V} \iso \gerbe{G}(i, j)|_{V}, \
f \mapsto g \circ f . \]

Let $\bar{g} \in \bar{\gerbe{G}}(i, j)(V)$ be the image of $g$. 
We then have an isomorphism of sheaves of right
$\bar{\gerbe{G}}(i, i)|_V$-sets 
\[ \bar{\gerbe{G}}(i, i)|_{V} \iso \bar{\gerbe{G}}(i, j)|_{V}, \
\bar{f} \mapsto \bar{g} \circ \bar{f} . \]
It follows that $\bar{\gerbe{G}}(i, j)|_{V}$ is a right 
$\bar{\gerbe{G}}(i, i)|_V$-torsor.
On the other hand, the isomorphism $\opn{Ad}(g)$ induces an isomorphism
of sheaves of groups
\[ \phi : \bar{\gerbe{G}}(i, i)_V \iso
\bar{\gerbe{G}}(j, j)_V . \]
We conclude that 
$\bar{\gerbe{G}}(i, j)|_{V}$ is a 
$\bar{\gerbe{G}}(j, j)|_V$-$\bar{\gerbe{G}}(i, i)|_V$-bitorsor.
And for this bitorsor structure, the isomorphism of sheaves of groups is
$\phi = \opn{Ad}(\bar{g})$. An easy calculation shows that the surjection
$\gerbe{G}(i, j)|_V \to \bar{\gerbe{G}}(i, j)|_V$ is 
$\gerbe{G}(j, j)|_V \times \gerbe{G}(i, i)|_V$ -equivariant.
\end{proof}

\begin{proof}[Proof of the theorem]
The proof is divided into several steps. 

\medskip \noindent
(a) Define a prestack of groupoids $\bar{\gerbe{G}}$,
and a morphism $\gerbe{G} \to \bar{\gerbe{G}}$,
as follows.
For an open set $U \subset X$ the object set is
$\opn{Ob} \bar{\gerbe{G}}(U) := \opn{Ob} \gerbe{G}(U)$.
For a pair of objects $i, j \in \opn{Ob} \bar{\gerbe{G}}(U)$
let $\bar{\gerbe{G}}(i, j)$ be the sheaf of sets from Lemma \ref{lem.3},
and define 
$\bar{\gerbe{G}}(U)(i, j) := \Gamma(U, \bar{\gerbe{G}}(i, j))$.
Next let $\gerbe{G} / \gerbe{N}$ be the stack associated to 
$\bar{\gerbe{G}}$. So $\gerbe{G} / \gerbe{N}$ is a gerbe,
and there is a weak equivalence of prestacks
$\bar{\gerbe{G}} \to \gerbe{G} / \gerbe{N}$.
It is important to note that even though 
$\gerbe{G} / \gerbe{N}$ may have more local objects than
$\bar{\gerbe{G}}$, the isomorphism sheaves (for local objects of 
$\bar{\gerbe{G}}$) are unchanged. 

\medskip \noindent
(b) The morphism of gerbes 
$F : \gerbe{G} \to \gerbe{G} / \gerbe{N}$
we get from step (a) is a weak epimorphism, and its kernel in
$\gerbe{N}$. This proves property (i). 

\medskip \noindent
(c) In this step we prove the existence part of property (ii). 
Let us define a morphism of prestacks
$\bar{D} : \bar{\gerbe{G}} \to \gerbe{H}'$ as follows.
On objects $\bar{D}$ is just $F' \circ D$. 
And on isomorphisms, for local objects $i, j$ of 
$\bar{\gerbe{G}}$, we define
\[ \bar{D} : \bar{\gerbe{G}}(i, j) \to 
\gerbe{H}' \bigl( D(i), D(j) \bigr) \]
to be the unique $\gerbe{G}(i, i)$-equivariant sheaf morphism making
the diagram
\[ \UseTips \xymatrix @C=8ex @R=5ex {
\gerbe{G}(i, j)
\ar[r]
\ar[d]_{D}
&
\bar{\gerbe{G}}(i, j)
\ar[d]_{\bar{D}}
\\
\gerbe{G}' \bigl( D(i), D(j) \bigr)
\ar[r]^(0.5){F'}
&
\gerbe{H}' \bigl( \bar{D}(i), \bar{D}(j) \bigr)
}  \]
commute. 
Due to the universal property of stackification, $\bar{D}$ induces a
morphism of gerbes 
$E : \gerbe{G} / \gerbe{N} \to \gerbe{H}'$; and then 
$(D, E)$ is a morphism of extensions. 

\medskip \noindent
(d) Now we will prove that the morphism $E$ from step (c) is unique up to
$2$-isomorphism. Suppose 
$E' : \gerbe{G} / \gerbe{N} \to \gerbe{H}'$
is some other morphism such that $(D, E')$ is a morphism of extensions. 
By composing the canonical morphism 
$\bar{\gerbe{G}} \to \gerbe{G} / \gerbe{N}$ with $E'$, we
obtain a morphism
$\bar{D}' : \bar{\gerbe{G}} \to \gerbe{H}'$.
We are going to construct a $2$-isomorphism 
$\bar{\eta} : \bar{D} \twoiso \bar{D}'$.

For a local object 
$i \in \opn{Ob} \gerbe{G}(U) = \opn{Ob} \bar{\gerbe{G}}(U)$
let
$j := \bar{D}(i) \in \opn{Ob} \gerbe{H}'(U)$
and
$j' := \bar{D}'(i) \in \opn{Ob} \gerbe{H}'(U)$.
So $j = (F' \circ D)(i)$ and $j' = (E' \circ F)(i)$.
Take any $2$-isomorphism $\eta : E' \circ F \twoiso F' \circ D$.
Then $\eta$ induces a $2$-isomorphism
$\bar{\eta} : \bar{D} \twoiso \bar{D}'$,
which coincides with $\eta$ on objects of $\bar{\gerbe{G}}$,
and is the reduction of $\eta$ modulo 
$\gerbe{N}$ on isomorphisms in $\bar{\gerbe{G}}$.

Because $\gerbe{G} / \gerbe{N}$ is the stackification of 
$\bar{\gerbe{G}}$, and $E, E'$ are the stackifications of 
$\bar{D}, \bar{D}'$ respectively, $\bar{\eta}$ induces a $2$-isomorphism 
$E \twoiso E'$. 

\medskip \noindent
(e) Finally we shall prove property (iii). 
The morphism $\bar{D} : \bar{\gerbe{G}} \to \gerbe{H}'$
is locally surjective on objects. This is because $\bar{\gerbe{G}}$
and $\gerbe{G}$ have the same local objects; 
$\gerbe{G} \to \gerbe{G}'$ is locally bijective on objects; and
$\gerbe{G}' \to \gerbe{H}'$ is 
locally surjective on objects.

By construction, for any pair of local objects
$i, j$ of $\bar{\gerbe{G}}$ we have
\[ \bar{\gerbe{G}}(i, j) = \gerbe{G}(i, j) / \gerbe{N}(i, i) \]
as sheaves of sets. On the other hand
\[ D : \gerbe{N}(i, i) \to
\gerbe{N}' \bigl( D(i), D(i) \bigr) \]
is an isomorphism of sheaves of groups, and 
\[ D : \gerbe{G}(i, j) \to 
\gerbe{G}' \bigl( D(i), D(j) \bigr) \]
is an isomorphism of torsors. 
Since 
\[ \gerbe{H}' \bigl( E(i), E(j) \bigr) \cong
\gerbe{G}' \bigl( D(i), D(j) \bigr) / \gerbe{N}' \bigl( D(i), D(i) \bigr) \]
we see that $\bar{D} : \bar{\gerbe{G}} \to \gerbe{H}'$
is a weak equivalence. Therefore 
$E : \gerbe{G} / \gerbe{N} \to \gerbe{H}'$
is an equivalence.
\end{proof}

\begin{cor}
Suppose we are given extensions of gerbes
\[ 1 \to  \gerbe{N} \to \gerbe{G} \xar{F} \gerbe{H} \to 1 
\]
and
\[ 1 \to  \gerbe{N}' \to \gerbe{G}' \xar{F'} \gerbe{H}' \to 1
, \]
and a morphism of gerbes
$D : \gerbe{G} \to \gerbe{G}'$,
such that $D(\gerbe{N}) \subset \gerbe{N}'$. Then there is a 
morphism of gerbes $E : \gerbe{H} \to \gerbe{H}'$, 
unique up to $2$-isomorphism, such that the diagram
\[ \UseTips \xymatrix @C=5ex @R=5ex {
1 
\ar[r]
&
\gerbe{N}
\ar[r]
\ar[d]
&
\gerbe{G}
\ar[r]^{F}
\ar[d]_{D}
& 
\gerbe{H} 
\ar[r]
\ar[d]_{E}
& 
1
\\
1 
\ar[r]
&
\gerbe{N}'
\ar[r]
&
\gerbe{G}'
\ar[r]_{F'}
& 
\gerbe{H}'
\ar[r]
& 
1
}  \]
is a morphism of extensions.
\end{cor}

\begin{proof}
By the theorem we can replace $\gerbe{H}$ with the equivalent gerbe
$\gerbe{G} / \gerbe{N}$. Now we can use property (ii) of the
theorem.
\end{proof}


Given a sheaf of groups $\mcal{G}$ on $X$ and an 
open set $U \subset X$, we write
$\mcal{G}(U) := \Gamma(U, \mcal{G})$. The center of this group is denoted by
$\mrm{Z}(\mcal{G}(U))$. Since the center is not functorial, one has to be
careful what we mean by the center of the sheaf $\mcal{G}$. The correct
definition seems to be as follows. 

\begin{dfn}
Let $\mcal{G}$ be a sheaf of groups on $X$. The {\em center} of $\mcal{G}$ is
the sheaf of groups $\mrm{Z}(\mcal{G})$ whose group of sections on an open set
$U$ is
\[ \mrm{Z}(\mcal{G})(U) := 
\{ g \in \mcal{G}(U) \mid g|_V \in \mrm{Z}(\mcal{G}(V))
\text{ for any } V \subset U \} . \]
\end{dfn}

\begin{prop} \label{prop:14}
Given a gerbe $\gerbe{G}$, there is a unique 
normal subgroupoid $\gerbe{N}$ of $\gerbe{G}$ such that 
\[ \gerbe{N}(i, i) = \mrm{Z} \bigl( \gerbe{G}(i, i) \bigr) \]
for every local object $i$ of $\gerbe{G}$.
\end{prop}

The proof is like that of Proposition \ref{prop:13}.

\begin{dfn}
Let $\gerbe{G}$ be a gerbe. 
\begin{enumerate}
\item The normal subgroupoid $\gerbe{N}$ in Proposition \ref{prop:14} is
called the {\em center} of $\gerbe{G}$, and it is denoted by
$\opn{Z}(\gerbe{G})$.
\item A {\em central subgroupoid} of  $\gerbe{G}$ is a 
normal subgroupoid $\gerbe{N}$ of $\gerbe{G}$ that is contained in 
$\opn{Z}(\gerbe{G})$.
\end{enumerate}
\end{dfn}

\begin{prop} \label{prop:12}
Let $\gerbe{N}$ be a central subgroupoid of  $\gerbe{G}$. 
Then there is sheaf of abelian groups $\mcal{N}$, together with an 
isomorphism of sheaves of groups
\begin{equation} \label{eqn:23}
\chi_i : \mcal{N}|_U \to \gerbe{N}(i, i)
\end{equation}
for any open set $U$ and object $i \in \opn{Ob} \gerbe{G}(U)$,
satisfying this condition:
\begin{itemize}
\rmitem{$\diamondsuit$}
Given any $i \in \opn{Ob} \gerbe{G}(U)$,  $j \in \opn{Ob} \gerbe{G}(V)$, 
$W \subset U \cap V$, and $g \in \gerbe{G}(i, j)(W)$, one has
\[ \chi_j \circ \opn{Ad}(g) = \chi_j  \]
as sheaf homomorphisms 
$\mcal{N}|_W \to \mcal{G}(j, j)|_W$. 
\end{itemize}
The sheaf $\mcal{N}$ is unique up to a unique isomorphism.

Conversely, given a sheaf of abelian  groups $\mcal{N}$, together with a
collection of injective sheaf homomorphisms
\[ \chi_i : \mcal{N}|_U \to \opn{Z}(\gerbe{G}(i, i))  \]
for $i \in \opn{Ob} \gerbe{G}(U)$, 
that satisfy condition \tup{($\diamondsuit$)}, there exists a unique central
subgroupoid $\gerbe{N}$ of  $\gerbe{G}$ such that 
\tup{(\ref{eqn:23})} are isomorphisms.
\end{prop}

\begin{proof}
This is due to the local nature of gerbes; cf.\ part (a) of the proof of
Theorem \ref{thm:1}.
\end{proof}

The last proposition says that a central subgroupoid $\gerbe{N}$ of a gerbe
$\gerbe{G}$ can be viewed as a single sheaf of abelian groups.

Finally we can explain the title of the paper. 

\begin{dfn} \label{dfn:2}
A {\em central extension of gerbes} is an extension of gerbes 
\[  1 \to \gerbe{N} \xar{} \gerbe{G} \xar{F} \gerbe{H} \to 1  \]
such that $\gerbe{N}$ is a central subgroupoid of $\gerbe{G}$.
\end{dfn}

Using Proposition \ref{prop:12} to replace $\gerbe{N}$ with a 
sheaf of abelian groups $\mcal{N}$, we can rewrite this central extension as
\begin{equation} \label{eqn:27}
 1 \to \mcal{N} \xar{} \gerbe{G} \xar{F} \gerbe{H} \to 1 .
\end{equation}

Here are a couple of examples of central extensions of gerbes. The first is
somewhat tautological.

\begin{exa}
Suppose $\gerbe{N}$ is a central subgroupoid of a gerbe $\gerbe{G}$.
Then the extension of gerbes 
\[ 1 \to \gerbe{N} \to \gerbe{G} \xar{F} \gerbe{G} / \gerbe{N} \to 1  \]
from Theorem \ref{thm:1} is central.
\end{exa}

The next example was suggested to us by the referee.

\begin{exa} \label{exa:27}
Let 
\[ 1 \to \mcal{N} \to \mcal{G} \xar{F} \mcal{H} \to 1 \]
be a central extension of sheaves of groups on $X$. Given an open set $U$ 
and a $\mcal{G}|_U$-torsor $\mcal{S}$, let us denote by $F(\mcal{S})$ the
induced $\mcal{H}|_U$-torsor. This operation gives rise to a morphism of gerbes
\begin{equation} \label{eqn:24}
F : \twocat{Tors} \gerbe{G} \to \twocat{Tors} \gerbe{H} 
\end{equation}
(cf.\ Example \ref{exa:16}). Since locally any $\mcal{H}$-torsor is
trivial, it is locally induced from a $\mcal{G}$-torsor. This says that 
(\ref{eqn:24}) is locally essentially surjective on objects. 

Now for any $\mcal{G}$-torsor $\mcal{S}$, locally we have a (noncanonical)
isomorphism of sheaves of groups
\[ (\twocat{Tors} \gerbe{G})(\mcal{S}, \mcal{S}) \cong 
\mcal{G}^{\mrm{op}} . \]
Likewise for $\mcal{H}$-torsors. This implies that the 
morphism of gerbes (\ref{eqn:24}) is surjective on isomorphism sheaves, and
its kernel is a central subgroupoid of $\gerbe{G}$, isomorphic to
the sheaf $\mcal{N}$. In this way we get a  central extensions of gerbes
\begin{equation} \label{eqn:25}
1 \to \mcal{N} \to \twocat{Tors} \gerbe{G} \xar{F} \twocat{Tors} \gerbe{H}
\to 1  .
\end{equation}
\end{exa}

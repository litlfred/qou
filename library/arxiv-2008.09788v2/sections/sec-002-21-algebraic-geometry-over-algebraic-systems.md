---
doc_id: arxiv-2008.09788v2
doc_title: "NONSTANDARD ANALYSIS, DEFORMATION QUANTIZATION AND SOME LOGICAL ASPECTS OF (NON)COMMUTATIVE ALGEBRAIC GEOMETRY"
section_id: sec-002-21-algebraic-geometry-over-algebraic-systems
section_title: "Algebraic geometry over algebraic systems"
section_number: 2.1
pages: 5-13
source_pdf: 2008.09788v2.pdf
source_sha256: 460f4f5432cb1f0c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.965
latex_coverage_ratio: 0.954
doc_brief: "NONSTANDARD ANALYSIS, DEFORMATION QUANTIZATION AND SOME LOGICAL ASPECTS OF (NON)COMMUTATIVE ALGEBRAIC GEOMETRY — This paper surveys results related to well-known works of B. Plotkin and V."
---
\label{Pl}


\subsubsection{\bf Three versions of logical rigidity}\label{Equiv}

Questions we are going to illuminate in this section are concentrated around the interaction between algebra, logic, model theory and geometry.

The main question behind further considerations is as follows. Suppose we have two algebras equipped with a sort of logical description.

\begin{prm} When the coincidence of logical descriptions  provides an isomorphism between algebras in question?
\end{prm}

With this aim we consider different kinds of logical equivalences between algebras. Some of the notions we are dealing with are not formally defined in the text.
For  precise definitions and references  use \cite{Halmos}, \cite{MR}, \cite{Plotkin_UA-AL-Datab},  \cite{Plotkin_Haz}, \cite{Pl-St}, \cite{PlAlPl}, \cite{PlPl}.

\medskip

\subsubsection{\bf Between syntax and semantics.}\label{synsem}
By syntax we will mean a language intended to describe a certain subject area.
In syntax we ask questions, express hypotheses and formulate the results. In syntax we
also build chains of formal consequences. For our goals we use first-order languages or their fragments. Each language is
based on some finite set of variables that serve as the alphabet, and a number of rules that
allow us to build words based on this alphabet. In general, its signature includes Boolean
operations, quantifiers, constants, and also functional symbols and predicate symbols. The
latter ones are included in atomic formulas and, in fact, determine the face of a particular
language. Atomic formulas will be called words. Words together with logical operations
between them will be called formulas.

By semantics we understand the world of models, or in other words, the subject
area of our knowledge. This world exists by itself, and develops according to its laws.


Fix a variety of algebras $\Theta$. Let $W(X)$, $X=\{x_1, \ldots, x_n\}$ denote the finitely generated  free algebra in $\Theta$. By equations in $\Theta$ we mean expressions of the form $w\equiv w'$, where $w$, $w'$ are words in $W(X)$ for some $X$. This is our first syntactic object.  Next, let $ \tilde \Phi=(\Phi(X), X\in \Gamma)$ be the multi-sorted Halmos algebra of first order logical formulas based on atoms $w\equiv w'$, $w$, $w'$ in $W(X)$, see \cite{Pl-St}, \cite{Plotkin_AGinFOL}, \cite{PlPl}. There is a special procedure to construct such an algebraic object which plays  the same role with respect to First Order Logic as Boolean algebras do with respect to Propositional calculus. One can view elements of  $\tilde\Phi=(\Phi(X), X\in \Gamma)$ just as first order formulas over $w\equiv w'$.



Let $X=\{x_1, \ldots , x_n \}$ and let $H$ be an algebra in the variety $\Theta$. We have an affine space $H^X$ of points  $\mu : X \to H$. For every $\mu$ we have also the $n$-tuple $(a_1, \ldots , a_n) = \bar a$ with $a_i = \mu(x_i)$. For the given $\Theta$ we have the homomorphism $$\mu : W(X) \to H$$ and, hence, the affine space is viewed as the set of homomorphisms
$$\Hom(W(X),H).$$
The classical kernel $\Ker(\mu)$ corresponds to each point $\mu : W(X) \to H$. This is exactly the set of equations for which the  point $\mu$ is a solution. Every point $\mu$ has also the logical kernel $\LKer(\mu)$, see \cite{PlAlPl}, \cite{Plotkin_7_lec},  \cite{Plotkin_AGinFOL}. Logical kernel $\LKer(\mu)$ consists of all formulas $u \in \Phi(X)$ valid on the point $\mu$. This is always an ultrafilter in $\Phi(X)$.








So we define syntactic and semantic areas where logic and geometry operate, respectively. Connect them by a sort of Galois correspondence.

 Let $T$ be a system of equations in $W(X)$. The set $A$ in the affine space $\Hom(W(X),H)$ consisting of all solutions of the system $T$ corresponds  to $T$. Sets of such kind are called {\it algebraic sets}. Vice versa, given a set $A$ of points in the affine space consider all equations $T$ having $A$ as the set of solutions. Sets $T$ of such kind are called {\it closed congruences} over $W$.

 We can do the same correspondence with respect to arbitrary sets of formulas. Given a set $T$ of formulas in algebra of formulas (set of elements) $\Phi(X)$, consider the set $A$ in the affine space, such that every point of $A$ satisfies every formula of $\Phi$. Sets of such
kind are called {\it definable sets}. Points of $A$ are called solutions of the set of formulas $T$.  Conversely,  given a set $A$ of points in the affine space consider all formulas (elements) $T$ having $A$ as the set of solutions. Sets $T$ of such kind are {\it closed filters} in  $\Phi(X)$.

Let us formalize the Galois correspondence described above.



\subsubsection{\bf Galois correspondence in the Logical Geometry}\label{Galois}




Let us start with a particular case when the set of formulas $T$ in $\Phi(X)$ is a set of equations of the form $w=w'$, $w, w' \in W(X)$, $X \in \Gamma$.



 We set
$$
A = T'_H = \{ \mu : W(X) \to H \ | \  T \subset Ker(\mu)\}.
$$
Here $A$ is an {\it algebraic set} in $\Hom(W(X),H)$, determined by the set $T$.

Let, further, $A$ be a subset in $\Hom(W(X),H)$. We set
$$
T = A'_H = \bigcap_{\mu \in A} Ker(\mu).
$$
Congruences $T$ of such kind are called  $H$-closed in $W(X)$. We have also Galois-closures $T''_H$ and $A''_H$.

Let us pass to the general case of logical geometry. Let now $T$ be a set of arbitrary formulas in $\Phi(X)$. We set
$$
A = T^L_H = \{ \mu : W(X) \to H \ | \  T \subset \LKer(\mu)\}.
$$
We have also
$$
A = \bigcap_{u \in T} \Val^X_H(u).
$$
Here $A$ is called a {\it definable  set} in $\Hom(W(X),H)$, determined by the set $T$. 
 We use the term "definable" for $A$ of such kind, meaning that $A$ is defined by some set of formulas $T$.


For the set of points $A$  in $\Hom(W(X),H)$ we set
$$
T = A^L_H = \bigcap_{\mu \in A} \LKer(\mu).
$$




We have also 
$$
T = A^L_H = \{ u\in \Phi(X) \ |\  A \subset \Val^X_H(u)\}.
$$

 Here $T$ is a Boolean filter in $\Phi(X)$ determined by the set of points $A$. Filters of such kind are Galois-closed and we can define the Galois-closures of arbitrary sets $T$ in $\Phi(X)$ and $A$ in $\Hom(W(X),H)$ as $T^{LL}$ and $A^{LL}$.





\begin{rem} The principal role in all considerations plays the value homomorphism $\Val: \tilde\Phi\to \Hal_\Theta$, where $\Hal_\Theta$ is a special Halmos algebra associated with the vector space $\Hom(W(X),H)$, see \cite{Plotkin_AGinFOL}, \cite{PlPl}. Its meaning is to make the procedure of verification whether a point satisfies the formula a homomorphism.
\end{rem}


\subsubsection{\bf Logical similarities of algebras}\label{lodsym}

Now we are in a position to introduce several logical equivalences between algebras. Since
the Galois correspondence  yields the duality between syntactic and semantic objects, every definition of equivalence between algebras formulated in terms of formulas, that is logically, has its semantical counterpart, that is a geometric formulation, and vice versa.

All algebraic sets constitute a category with special rational maps as morphisms \cite{PlPl}. The same is true with respect to definable sets \cite{PlPl}. So, we can formulate logical closeness of algebras geometrically.

\begin{Def}\label{def:gsim} We call algebras $H_1$ and $H_2$  {\it geometrically similar} if the categories of algebraic sets $AG_\Theta(H_1)$ and $AG_\Theta(H_2)$ are isomorphic.
\end{Def}



By Galois duality  between closed congruences and algebraic sets,   $H_1$ and $H_2$ are  geometrically similar if and only if the corresponding   categories $C_\Theta(H_1)$ and $C_\Theta(H_2)$ of closed congruences over $W(X)$  are isomorphic.


\begin{Def}\label{def:lsim} We call algebras $H_1$ and $H_2$  {\it logically similar}, if the categories of definable sets $LG_\Theta(H_1)$ and $LG_\Theta(H_2)$ are isomorphic.
\end{Def}

By Galois duality  between closed filters in $\Phi(X)$  and definable  sets,   $H_1$ and $H_2$ are  logically similar if and only if the corresponding categories   $F_\Theta(H_1)$ and $F_\Theta(H_2)$ of closed filters in $F(X)$  are isomorphic.

We will be looking for conditions $\mathcal A$ on algebras $H_1$ and $H_2$ that provide geometrical or logical similarity.

Let two algebras $H_1$ and $H_2$ subject to some condition $\mathcal A$ be given.  Here $\mathcal A$ is any condition of logical or,  dually, geometrical character, formulated in terms of closed sets of formulas or definable sets.

\begin{Def}\label{def:lsim2} We call the condition $\mathcal A$ rigid (or $\mathcal A$-rigid)  if two algebras $H_1$ and $H_2$  subject to  $\mathcal A$ are isomorphic.
\end{Def}


\subsubsection{\bf Geometric equivalence of algebras}\label{gme}

\begin{Def}\label{def:AG} {
Algebras $H_1$ and $H_2$ are called AG-equivalent, if for every $X $ and every system of equations $T$   holds       $T''_{H_1}=T''_{H_2}$.}
\end{Def}
 AG-equivalent algebras are called also {\it  geometrically equivalent} algebras, see \cite{PlPl}, \cite{PlAlPl}, \cite{Plotkin_7_lec}. The closure $T''_{H}$ is called, sometimes, a {\it radical} of $T$ with respect to $H$. This is a normal subgroup and an ideal in cases of groups and associative (Lie) algebras, respectively.

 The meaning of Definition \ref{def:AG} is as follows. Two algebras $H_1$ and $H_2$ are AG-equivalent if they have the same solution sets with respect to any system of equations $T$.  We have the following criterion, see \cite{PlPl}.

 \begin{prop}\label{:AG}
If algeras $H_1$ and $H_2$ are AG-equivalent, then they are AG-similar.
\end{prop}

So, geometric equivalence of algebras provides their geometrical similarity. The next statement describes geometrically equivalent algebras.  Assume, for simplicity, that our algebras are geometrically noetherian (see \cite{Plotkin_7_lec}, \cite{MR}),  which means that every system of equations $T$ is equivalent to a finite subsystem $T'$ of $T$.  Then, see \cite{Plotkin_Gagta},

\begin{prop}\label{quasi1}
Geometrically noetherian algebras $H_1$ and $H_2$ are AG-equivalent if and only if they generate the same quasi-variety.
\end{prop}

Hence, two algebras $H_1$ and $H_2$ are AG-equivalent if and only if they have the same quasi-identities. If we drop the condition of geometrical noetherianity, then algebras $H_1$ and $H_2$ are AG-equivalent if they have the same infinitary quasi-identities.

Let $\Theta$ be the variety of all groups. Now the question of $AG$-rigidity for groups reduces to the question when two groups generating one and the same  quasi-variety are isomorphic. Of course the condition on groups to have one and the same quasi-identities is  very weak   and the  rigidity of such kind  can happen if  both groups belong to a very narrow class of groups. In general, such a condition does not seem sensible.

Geometrical equivalence of algebras gives a sufficient condition for $AG$-similarity. It turns out that for some varieties $\Theta$ this condition is also sufficient.

\begin{thm}{}\label{th:gsim}
Let $Var(H_1)=Var(H_2)=\Theta.$ Let $\Theta$ be one of the following varieties




\begin{itemize}
\item
$\Theta=Grp$, the variety of groups,
 \item
 $\Theta=Jord$, the variety of Jordan algebras,
 \item
 $\Theta=Semi$, the variety of semigroups,
 \item  $\Theta=Inv$, the variety of inverse semigroups,
 \item  $\Theta=\mathfrak N_d$, the variety of nilpotent groups of class $d$.
 \end{itemize}
 Categories $AG_\Theta(H_1)$ and $AG_\Theta(H_2)$ are
isomorphic if and only if the algebras $H_1$ and $H_2$ are
geometrically equivalent (see \cite{Formanek}) \cite{MSZ}, \cite{Ts4},
\cite{Ts2}).


\end{thm}

Let $\Theta^0$ be the category of all free algebras of the variety $\Theta$.  The following proposition is the main tool in the proof of Theorem \ref{th:gsim}.

\begin{prop}[\cite{Pl-Sib}]\label{prop:eq} If for the variety $\Theta$ every automorphism of the category $\Theta^0$ is inner,
then  two algebras $H_1$ and $H_2$ are geometrically similar if and only if they are geometrically equivalent.
\end{prop}



So, studying automorphisms of $\Theta^0$ plays a crucial role.  The latter problem is treated by means of Reduction Theorem (see \cite{Pl-St}, \cite{KLP}, \cite{MPP2}, \cite{PZ1}). This theorem reduces investigation of automorphisms of the whole category $\Theta^0$ of free in $\Theta$ algebras  to studying the  group $\Aut(\End(W(X)))$  associated with a single object $W(X)$ in $\Theta^0$. Here, $W(X)$ is a finitely generated free in $\Theta$ hopfian algebra, which generates the whole variety $\Theta$. In fact, if all automorphisms of the endomorphism semigroup of a free algebra $W(X)$ are close to being inner, then all automorphisms of $\Theta^0$ possess the same property. More precisely, denote by $Inn(\End(W(X)))$ the group of inner automorphisms of $\Aut(\End(W(X)))$. Then the group of outer automorphisms $\Aut(\End(W(X)))/Inn(\End(W(X)))$ measures, in some sense, the difference between the notions of geometric similarity and geometric equivalence.

\medskip

\subsubsection{\bf Elementary equivalence of algebras}\label{ee}

As we saw in the previous section $AG$-equivalence of algebraic sets  reduces to coincidence of  quasi-identities of algebras.  This is a weak invariant, a small part of elementary theory, and, of course, coincidence of quasi-identities does not imply isomorphism of algebras.  Hence $AG$-equivalence does not make much sense from the point of view of rigidity. Now we recall a more powerful  logical invariant of  algebras.

Given algebra $H$, its {\it elementary theory} $Th(H)$ is the set of all sentences (closed formulas) valid on $H$. We modify a bit this definition and adjust it to the Galois correspondence. Fix $X=\{x_1, \ldots, x_n\}$. Define $X$-elementary theory $Th^X(H)$ to be
  the  set of all  formulas $u \in \Phi(X)$ valid in every point of the affine space $\Hom(W(X),H)$. In general we have a multi-sorted representation of the elementary theory $$Th(H)=(Th^X(H), X \in \Gamma),$$
where $\Gamma$ is a  certain  system of sets.

\begin{Def}\label{elem}
Two algebras $H_1$ and $H_2$ are said to be {\it elementarily equivalent} if their elementary theories coincide.
\end{Def}

\begin{rem} From the geometric point of view this definition does not make difference between different points of the affine space. Given algebras $H_1$ and $H_2$,  we collect all together formulas valid in every point of the affine spaces $\Hom(W(X),H_1)$ and  $\Hom(W(X),H_2)$, and  declare algebras  $H_1$ and $H_2$ elementarily equivalent if these sets coincide.
\end{rem}

  Importance of the elementary classification of algebraic structures goes back
to the famous  works of A.Tarski and A.Malcev. The main problem is to figure out {\it what are the algebras elementarily equivalent to a given one.} Very often we fix a class of algebras $\mathcal C$ and ask what are the algebras elementarily equivalent to a given algebra inside the class $\mathcal C$. So, the rigidity question with respect to elementary equivalence looks as follows.




 \begin{prm}
  Let a class of algebras $\mathcal C$ and an algebra $H\in \mathcal C$ be given. Suppose that the elementary theories of algebras $H$ and $A\in \mathcal C$ coincide. Are they  {\it elementarily rigid}, that is,  are  $H$ and $A$  isomorphic?
 \end{prm}

\begin{rem}
What we call elementary rigidity has different names. This notion appeared in the papers by A. Nies \cite{Nies}  under the name of quasi definability of groups. The corresponding name used in \cite{ALM} is first order rigidity. For some reasons which will be clear in the next section we use another term.
\end{rem}



































In other words we ask for which algebras their logical characterization by means of the elementary theory is strong enough and define the algebra in the unique, up to an isomorphism, way?

 We restrict our attention to the case of groups, and, moreover, assume quite often that our groups are finitely generated.  Elementary rigidity of groups occurs not very often. Usually various extra conditions are needed. Here is the incomplete list of some known cases:

 \begin{thm}
 We will consider the following cases

 \begin{itemize}
 \item Finitely generated abelian groups are elementarily rigid in the class of such groups, see \cite{Szm}, \cite{EF}.
  \item Finitely generated torsion-free class 2 nilpotent groups are elementarily rigid in the class of finitely generated groups,  see \cite{Hirshon}, \cite{Oger} (this is wrong for such groups  of class 3 and for torsion groups of class 2, see \cite{Zilber1} ).
   \item If two finitely generated free nilpotent groups are elementarily equivalent, then they are isomorphic, that is a free finitely generated nilpotent group is elementarily rigid in the class of such groups,   see \cite{RSS}, \cite{Mal}.
   \item If two finitely generated free solvable groups are elementarily equivalent, then they are isomorphic, that is a free finitely generated solvable group is elementarily rigid in the class of such groups,   see \cite{RSS}, \cite{Mal}.
       \item Baumslag-Solitar group BS($1,n$) is elementarily rigid in the class of countable groups, see \cite{CKR}. General Baumslag-Solitar groups BS($m,n$) are elementarily rigid in the class of all Baumslag-Solitar groups, see  \cite{CKR}.
     \item Right-angled Coxeter group is elementarily rigid in the class of all right-angled Coxeter groups, see \cite{CK}.
      \item A good rigidity example is provided by profinite groups: if two finitely generated profinite groups are
elementarily equivalent (as abstract groups), then they are isomorphic \cite{JL}.
 \end{itemize}
  \end{thm}

 




Consider, separately, examples of elementary rigidity for linear groups. First of all, a group which is elementarily equivalent to a finitely generated linear group is a residually finite linear group \cite{Mal1}. The rigidity cases are collected in the following theorem.



 \begin{thm}
 We will consider the following cases.

 \begin{itemize}
 \item Historically, the first result was obtained by Malcev \cite{Mal2}. If two linear groups $GL_n(K)$ and  $GL_m(F)$, where $K$ and $F$ are    fields, are elementarily equivalent, then $n=m$ and the fields $K$ and $F$ are elementarily equivalent.
  \item This result was generalized to the wide class of Chevalley groups. Let $G_1=G_\pi(\Phi,R)$ and $G_2=G_\mu(\Psi,S)$ be two elementarily equivalent Chevalley groups. Here $\Phi$, $\Psi$ denote the root systems of rank $\geq 1$, $R$ and $S$ are local rings, and $\pi$, $\mu$ are weight lattices. Then root systems and weight lattices of $G_1$ and $G_2$ coincide, while the rings are elementarily equivalent. In other words Chevalley groups over local rings are elementarily rigid in the class of such groups modulo rigidity of the ground rings \cite{Bu}.
      \item Let $G_\pi(\Phi,K)$ be a simple Chevalley group over the algebraically closed field $K$. Then  $G_\pi(\Phi,K)$ is elementarily rigid in the class of all groups (cardinality is fixed). This result can be deduced from \cite{Zilber}. In fact, this is true for a much wider class of algebraic groups over algebraically closed fields and, modulo elementary equivalence of fields,  over arbitrary fields \cite{Zilber}.
   \item Any  irreducible non-uniform higher-rank characteristic zero
arithmetic lattice is elementarily rigid in the class of all groups, see \cite{ALM}. In particular, $SL_n(\mathbb Z)$, $n>2$ is elementarily rigid.
 \item Recently, the results of \cite{ALM} have been extended to a much more wide class of lattices, see \cite{AM}.
   \item Let $\mathcal O$ be the ring of integers of a number field, and let $n\geqslant 3$. Then every  group $G$ which is elementarily equivalent to $SL_n(\mathcal O)$ is isomorphic to $SL_n(\mathcal R)$, where the rings $\mathcal O$ and $\mathcal R$ are elementarily equivalent. In other words $SL_n(\mathcal O)$ is elementarily rigid in the class of all groups modulo elementary equivalence of rings. The similar results are valid with respect to $GL_n(\mathcal O)$ and  to the triangular group   $T_n(\mathcal O)$ \cite{SM}. These results intersect in part with the previous items, since  the ring $R=\mathbb Z$ is elementarily rigid in the class of all finitely generated rings \cite{Nies}, and thus  $SL_n(\mathbb Z)$ is elementarily rigid in the class of all finitely generated groups.
         \item  For the case of arbitrary Chevalley groups the results similar to  above cited are obtained in \cite{ST} by different machinery for a wide class of ground rings. Suppose  the Chevalley group $G=G(\Phi,R)$ of rank $\geqslant 2$ over the ring $R$ is given. Suppose that the ring $R$ is elementarily rigid in the class $\mathcal C$ of rings.  Then $G=G(\Phi,R)$ is elementarily rigid in the corresponding class $\mathcal C_1$ of groups  if $R$ is a field, $R$ is a local ring and $G$ is simply connected, $R$ is a Dedekind ring of  arithmetic type, that is the ring of $S$-integers of a number field, $R$ is Dedekind ring with at least 4 units and $G$ is adjoint. In particular, if  a ring of such kind is finitely generated then it gives rise to elementary rigidity of $G=G(\Phi,R)$ in the class of all finitely generated groups.
              If $R$ of such kind is not elementarily rigid then  $G=G(\Phi,R)$ is elementarily rigid in the class of all groups modulo elementary equivalence of rings.
 \end{itemize}
  \end{thm}

 Absolutely free groups lie on the other side of the scale of groups. It was Tarski who asked whether one can distinguish between finitely generated free groups by means of their elementary theories. This formidable  problem has been solved in affirmative, that is all free groups have one and the same elementary theory \cite{KM}, \cite{Se}. In fact, the variety of all groups is the only known variety of groups, such that a free in this variety finitely generated group is not rigid in the class of all such groups.

  \begin{prm} Construct a variety of groups different from the variety of all groups such that all free finitely generated groups in this variety have one and the same elementary theory.
  \end{prm}
















\subsubsection{\bf Logical equivalence of algebras}\label{leq}

In this Section we introduce the notion of logical equivalence of algebras which can be viewed as first order equivalence. We proceed following exactly the same scheme which was applied in Section \ref{gme} with respect to the definition of geometric equivalence of algebras.

Let $H_1$ and $H_2$ be two algebras.  We will be looking for semantic logical invariant of these algebras, that is compare the definable sets over $H_1$ and $H_2$. Recall that according to Definition \ref{def:lsim} two algebras $H_1$ and $H_2$ are {\it logically similar}, if the categories of definable sets $LG_\Theta(H_1)$ and $LG_\Theta(H_2)$ are isomorphic.

Using the duality provided by Galois correspondence from Section \ref{Galois} we  will raise logical similarity to the  level of syntax.
 The principal Definition \ref{def:LG} is the first order counterpart of  Definition \ref{def:AG}.

\begin{Def}\label{def:LG}
Algebras $H_1$ and $H_2$ are called LG-equivalent (aka logically equivalent), if for every $X $ and every set of formulas $T$ in $\Phi(X)$   the  equality $T^{LL}_{H_1}=T^{LL}_{H_2}$ holds .
\end{Def}

It is easy to see that  
\begin{prop}
 If algebras $H_1$ and $H_2$ are
$LG$-equivalent then they are elementarily equivalent.
\end{prop}

Now we want to understand what is the meaning of logical equivalence.

\begin{Def}\label{def:iso}
 Two algebras $H_1$ and $H_2$ are called \textit{$LG$-isotypic} if for every point $\mu:W(X)\to H_1$ there exists a point $\nu:W(X)\to H_2$ such that $\LKer(\mu)=\LKer(\nu)$ and, conversely, for every point $\nu:W(X)\to H_2$ there exists a point $\mu:W(X)\to H_1$ such that $\LKer(\nu)=\LKer(\mu)$.
\end{Def}

The meaning of  Definition \ref{def:iso} is the following. Two algebras are isotypic if the sets of realizable types over $H_1$ and $H_2$ coincide. So, by some abuse of language these algebras have the same logic of types. Some references for the notion of isotypic algebras are contained in \cite{Plotkin_M}, \cite{Plotkin_Gagta}, \cite{PlAlPl}, \cite{PlPl}, \cite{PZ}, \cite{Zhitom_types}. Note that the notion was introduced in \cite{PZ}, \cite{Plotkin_M} while \cite{PlPl} gives the most updated survey.

The main theorem is as follows, see \cite{Zhitom_types}.
\begin{thm}\label{thm:lgiso} 
Algebras $H_1$ and $H_2$ are $LG$-equivalent if and only if they are LG-isotypic.
\end{thm}

Now we are in a position to study   rigidity of algebras with respect to isotypicity property. It is clear, that since isotypicity is stronger than elementary equivalence, this phenomenon can occur quite often. Let us state this problem explicitly.



 \begin{prm}
Let a class of algebras $\mathcal C$ and an algebra $H\in \mathcal C$ be given. Suppose that algebras $H\in \mathcal C$ and $A\in \mathcal C$ are isotypic. Are they  {\it isotypically rigid}, that is are $H$ and $A$  isomorphic?
 \end{prm}

\begin{rem}
In many papers from the list above isotypically rigid algebras are called {\it logically separable} \cite{PlPl}, \cite{Plotkin_Gagta}, or {\it type definable} \cite{MRoman}. 
\end{rem}

 \begin{thm}\label{isor}
 We will consider the following cases of rigidity:

 \begin{itemize}
 \item Finitely generated free abelian groups are isotypically rigid in the class of all groups, see \cite{Zhitom_types}.
 \item Finitely generated  free nilpotent groups of  class at most $n$  are isotypically rigid in the class of all groups \cite{Zhitom_types}.
    \item  Finitely generated   metabelian  groups   are isotypically rigid in the class of all groups \cite{MRoman}.
 \item Finitely generated  virtually polycyclic groups are isotypically rigid in the class of all groups \cite{MRoman}.
   \item  Finitely generated  free solvable   groups of derived length $d > 1$    are isotypically rigid in the class of all groups \cite{MRoman}.
       \item All surface groups, which are not  non-orientable surface
groups of genus 1,2 or 3   are isotypically rigid in the class of all groups \cite{MRoman}.
  \item Finitely generated absolutely free groups  are isotypically rigid in the class of all groups,  see \cite{Sklinos_1} based on \cite{Pillay} (also follows from \cite{PerinSklinos}, \cite{Houcine}, \cite{Zhitom_types_1}).
      \item Finitely generated free  semigroups are isotypically rigid in the class of semigroups, see \cite{Zhitom_types}.
       \item Finitely generated free  inverse semigroups are isotypically rigid in the class of inverse semigroups, see \cite{Zhitom_types}.
      \item{} Finitely generated free associative algebras are isotypically rigid in the class of such algebras \cite{Zhitom_types_1}.
 \end{itemize}
  \end{thm}

  The number of examples can be continued to co-Hopf groups, some Burnside groups, etc.

In fact, using either logical equivalence of algebras, or what is the same, the isotypicity of algebras, we compare the possibilities of individual points in the affine space  to define the sets of formulas (in fact ultrafilters in $\Phi(X)$) which are valid in these points. Given a point $\mu$ in the affine space,  the collection of formulas valid on the point $\mu$ is {\it a type} of $\mu$. If these individual types are,  roughly speaking, the same for both algebras,  then these algebras are declared isotypic. Thus, for isotypic algebras  we compare  types of formulas realizable on these  algebras. Of course, this is significantly stronger than elementary equivalence, where the individuality of points disappeared and we compare only formulas valid in all points of the affine space.


The following principal problem was stated in \cite{PlPl} and is widely open.

\begin{prm}[Rigidity problem]
 Is it true that every two isotypic finitely generated groups are
isomorphic?
\end{prm}

We will finish with the one more tempting problem of the same spirit.


\begin{prm}\label{fields}
What are the isotypicity classes of fields? When  two isotypic fields are isomorphic?
\end{prm}

The elementary equivalence of fields was one of motivating engines for Tarski to develop the whole model-theoretic staff related to elementary equivalence. Problem \ref{fields}, in a sense,  takes us back to the origins of the theory.

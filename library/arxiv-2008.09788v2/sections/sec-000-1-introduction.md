---
doc_id: arxiv-2008.09788v2
doc_title: "NONSTANDARD ANALYSIS, DEFORMATION QUANTIZATION AND SOME LOGICAL ASPECTS OF (NON)COMMUTATIVE ALGEBRAIC GEOMETRY"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 2-5
source_pdf: 2008.09788v2.pdf
source_sha256: 460f4f5432cb1f0c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.984
latex_coverage_ratio: 0.975
doc_brief: "NONSTANDARD ANALYSIS, DEFORMATION QUANTIZATION AND SOME LOGICAL ASPECTS OF (NON)COMMUTATIVE ALGEBRAIC GEOMETRY — This paper surveys results related to well-known works of B. Plotkin and V."
---
\label{intro}
The connections between algebraic geometry and mathematical logic are extremely important.
First of all, notice a deep connection between algebra, category theory and model theory
 inspired by the results of Plotkin and his school
(see
\cite{Plotkin_UA-AL-Datab, Plotkin_Haz, Plotkin_7_lec, Plotkin_VarAlg-AlgVar, Pl-Sib}.
Note that this research is related to
 the one  of  most striking examples of interaction between model theory and geometry given by  solutions of the famous Tarskii's problem, see \cite{KM, Se}.
 Another outstanding  achievement is the theory of Zariski geometries developed by B.Zilber and E.Hrushovski \cite{HZ} and \cite{Z2,Z3}. In addition, the use of non-standard analysis has allowed progress in the theory of polynomial $64$ automorphisms. See the work of Belov and Kontsevich \cite{4,3}. For a detailed bibliography see \cite{b23}.




The foundations of algebraic geometry had an important part of the translation of topological and arithmetical properties into a purely algebraic language (\cite{Grothendieck}). 
Translation of the algebraic properties of a variety into the language of mathematical logic can be considered somehow in the spirit of this program.




 This short survey is related to ideas  contained in the 
 
 works of B. Plotkin and V. Remeslennikov and their followers. We assume that lots of questions  still require further illumination.

In particular, the following question is of interest: given two algebraic sets. Is there an algorithm for checking isomorphism? Similarly for birational equivalence. Is there a solution to the nesting problem of two varieties? For characteristics $0$, the answer is no \cite{Bel-Chil2}, but for a positive characteristic the answer is unknown.

On should mention a number of conjectures related to the theory of models and polynomial automorphisms expressed in the paper by Belov-Kontsevich \cite{4}. The investigations of the Plotkin school are far from completion, thus the relationship between the theory of medallions and the theory of categories is relevant.

 One of the goals of this paper is to narrow the gap and to draw attention to this topic. We deal with commutative and non-commutative algebraic geometry. The latter notion can be understood in several ways. There are many points of view on the subject. We touch universal algebraic geometry, some of its relations with reformational quantization and Gr\"obner basis in non-commutative situation.

The paper is organized as follows. {\bf Section \ref{mod-theor}} is devoted to {\bf various model-theoretical aspects and their applications}. More precisely, {\bf Section \ref{Pl}} deals with universal algebraic geometry and is focused around the interaction between algebra, logic, model theory and geometry. All these subjects are collected under the roof of the different kinds of logical rigidity of algebras. Under logical rigidity we mean some logical invariants of algebras whose coincidence gives rise to structural closeness of algebras in question. If such an invariant is strong enough then there is a solid ground to look for isomorphism of algebras whose logical invariants coincide.

We are comparing three types of logical description of algebras. Namely, we describe geometric equivalence of algebras, elementary equivalence of algebras and isotypicity of algebras. We look at these notions from the positions of universal algebraic geometry and logical geometry. This approach was developed by B. Plotkin and resulted in the consistent series of papers where algebraic logic, model theory, geometry and categories come together. In particular, an important role plays the study of automorphisms of categories of free algebras of the varieties. This question is highly related to description of such objects as $\Aut(\Aut)(A)$ and $\Aut(\End)(A)$, where $A$ is a free algebra in a variety.

We formulate the principal problems in this area and make a survey of the known results. Some of them are very recent while the others are quite classical. In any case we shall emphasize that we attract attention to the widely open important problem whether the finitely  generated isotypic groups are isomorphic.




The line started in  Section \ref{Pl} is continued in {\bf Section \ref{plot-prm}}.

 Problems related to universal algebraic geometry (i.e. algebraic geometry over algebraic systems) and
logical foundations of category theory gave rise to natural questions on automorphisms of categories and their auto-equivalences. The latter ones stimulate a new motivation to investigation of  semigroups of endomorphisms and groups of automorphisms of universal algebras (Plotkin's problem) (see \cite{Pl}).

Let $\Theta$ be a variety of linear algebras over a commutative-associative ring $K$ and $W=W(X)$ be a free algebra from $\Theta$  generated by a finite set $X$. Let
$H$ be an algebra from $\Theta$ and $AG_{\Theta}(H)$ be the
category of algebraic sets over $H$. Throughout the work, we refer to
\cite{b23, Pl-St} for definitions of the Universal Algebraic Geometry (UAG).

The category  $AG_{\Theta}(H)$ is considered as the logical invariant of an algebra $H$. By Definition \ref{def:gsim}, two algebras $H_{1}$ and $H_{2}$ are
geometrically similar if the categories $AG_{\Theta}(H_{1})$ and
$AG_{\Theta}(H_{2})$ are isomorphic.
It has been shown in \cite{Pl-St}, (cf., Proposition \ref{prop:eq}) that  geometrical similarity of algebras
is
determined by the structure of the group $\Aut(Theta^{0})$, where
$\Theta^{0}$ is the category of free finitely generated algebras
of $\Theta$.  The latter problem is treated by means of Reduction Theorem (see \cite{Pl-St}, \cite{KLP}, \cite{MPP2}, \cite{PZ1}). This theorem reduces investigation of automorphisms of the whole category $\Theta^0$ of free algebras in $\Theta$ to studying the  group $\Aut(\End(W(X)))$  associated with $W(X)$ in $\Theta^0$.

In Section \ref{plot-prm} we provide the reader with the results, describing $\Aut(\End(A))$, where $A$ is finitely generated free commutative or  associative algebra, over a field $K$. 

 
 


  We prove that the group $\Aut(\End(A))$ is generated by
semi-inner and mirror automorphisms of $\End(A)$ and the group
$\Aut(\mathcal{A}^{\circ})$ is generated by semi-inner and mirror
automorphisms of the category of free algebras $\mathcal{A}^{\circ}$.

 Earlier, the description of $\Aut(\mathcal{A}^{\circ})$  for the
 variety $\mathcal{A}$ of associative algebras over algebraically closed fields
 has been given in \cite{b19} and, over infinite fields, in \cite{b3}.
Also in the same works, the description of $\Aut(\End(W(x_{1},
x_{2})))$ has been obtained.

 Note that a description of the groups $\Aut(\End(W(X)))$ and $\Aut(\Theta^{\circ})$ for some other varieties
$\Theta$ has been given in \cite {b2, b3, b4, b8, b15, b16, b16a, b19,
b20, b21, MPP2, b27}.




A group of automorphisms of ind-schemes was computed in \cite{BEJ}. In investigating the Jacobian conjecture and automorphisms of the Weyl algebra, Plotkin's problem for symplectomorphisms is also extremely important. Such problems are associated with mathematical physics and the theory of $\mathcal{D}$-modules.





{\bf Section \ref{indep}} is devoted to {\bf  mathematical physics and model theory.}
This relation deals with nonstandard analysis.  We refer the reader to the review \cite{KanoveiLubec}.

The Belov--Kontsevich conjecture \cite{4}, sometimes Kanel-Belov--Kontsevich conjecture, dubbed $B{-}KKC_n$ for positive integer $n$, seeks to establish a canonical isomorphism between automorphism groups of algebras
\begin{equation*}
\Aut (A_{n,\mathbb{C}})\simeq \Aut(P_{n,\mathbb{C}}).
\end{equation*}
Here $A_{n,\mathbb{C}}$ is the $n$-th Weyl algebra over the complex field,
\begin{equation*}
A_{n,\mathbb{C}}=\mathbb{C}\langle x_1,\ldots,x_n,y_1,\ldots,y_n\rangle/(x_ix_j-x_jx_i,\; y_iy_j-y_jy_i,\; y_ix_j-x_jy_i-\delta_{ij}),
\end{equation*}
and $P_{n,\mathbb{C}}\simeq \mathbb{C}[z_1,\ldots,z_{2n}]$ is the commutative polynomial ring viewed as a $\mathbb{C}$-algebra and equipped with the standard Poisson bracket:
\begin{equation*}
\lbrace z_i,z_j\rbrace =\omega_{ij}\equiv \delta_{i,n+j}-\delta_{i+n,j}.
\end{equation*}
The automorphisms from $\Aut(P_{n,\mathbb{C}})$ preserve the Poisson bracket.


Let $\zeta_i,\;i=1,\ldots,2n$ denote the standard generators of the Weyl algebra (the images of $x_j,\;y_i$ under the canonical projection). The filtration by total degree on $A_{n,\mathbb{C}}$ induces a filtration on the automorphism group:
\begin{equation*}
\Aut^{\leq N}( A_{n,\mathbb{C}}):=\lbrace f\in\Aut(A_{n,\mathbb{C}})\;|\;\Deg f(\zeta_i),\;\Deg f^{-1}(\zeta_i)\leq N,\forall i=1,\ldots,2n\rbrace.
\end{equation*}
The obvious maps
\begin{equation*}
\Aut^{\leq N}( A_{n,\mathbb{C}})\rightarrow \Aut^{\leq N+1} (A_{n,\mathbb{C}})
\end{equation*}
are Zariski-closed embeddings, the entire group $\Aut (A_{n,\mathbb{C}})$ is a direct limit of the inductive system formed by $\Aut^{\leq N}$ together with these maps. The same can be said for the symplectomorphism group $\Aut(P_{n,\mathbb{C}})$.



The Belov--Kontsevich conjecture admits a stronger form, with $\mathbb{C}$ being replaced by the rational numbers. The latter conjecture will not be treated here in any way.


Since Makar-Limanov \cite{8}, \cite{9}, Jung \cite{6} and van der Kulk \cite{7}, the B-KK conjecture is known to be true for $n=1$. The proof is essentially a direct description of the automorphism groups. Such a direct approach however seems to be completely out of reach for all $n>1$. Nevertheless, at least one known candidate for isomorphism may be constructed in a rather straightforward fashion. The idea is to start with an arbitrary Weyl algebra automorphism, lift it after a shift by a certain automorphism of $\mathbb{C}$ to an automorphism of a larger algebra (of formal power series with powers taking values in the ring $^*\mathbb{Z}$ of hyperintegers) and then restrict to a subset of its center isomorphic to $\mathbb{C}[z_1,\ldots,z_{2n}]$.



This construction goes back to Tsuchimoto \cite{13}, who devised a morphism
 $\Aut (A_{n,\mathbb{C}})\rightarrow \Aut(P_{n,\mathbb{C}})$ in order to prove the stable equivalence between the Jacobian and the Dixmier conjectures. It was independently considered by Kontsevich and Kan\-el-Bel\-ov \cite{3}, who offered a shorter proof of the Poisson structure preservation which does not employ $p$-cur\-va\-tur\-es. It should be noted, however, that Tsuchimoto's thorough inquiry into $p$-cur\-va\-tur\-es has exposed a multitude of problems of independent interest, in which certain statements from the present paper might appear.



The construction we describe in detail in the following sections differs from that of Tsuchimoto in one aspect: an automorphism $f$ of the Weyl algebra may in effect undergo a shift by an automorphism of the base field $\gamma:\mathbb{C}\rightarrow\mathbb{C}$ prior to being lifted, and this extra procedure is homomorphic. Taking $\gamma$ to be the inverse nonstandard Frobenius automorphism (see below), we manage to get rid of the coefficients of the form $a^{[p]}$, with $[p]$ an infinite prime, in the resulting symplectomorphism. The key result here is that for a large subgroup of automorphisms, the so-called tame automorphisms, one can 
completely eliminate the dependence of the whole construction on the choice of the infinite prime $[p]$. Also, the resulting ind-group morphism $\phi_{[p]}$ is an isomorphism of the tame subgroups. In particular, for $n=1$ all automorphisms of $A_{1,\mathbb{C}}$ are tame (Makar-Limanov's theorem), and the map $\phi_{[p]}$ is the conjectured canonical isomorphism.



These observations motivate the question whether for any $n$ the group homomorphism $\phi_{[p]}$ is independent of infinite prime.




The next {\bf Section 3} makes emphasis on  {\bf algorithmic questions.}
First we dwell on 
 Non-Commutative Gr\"obner basis.
Questions of algorithmic decidability in algebraic structures have been studied since the 1940s.
In 1947 Markov \cite{Markov} and independently Post \cite{Post} proved that the word equality problem in finitely presented semigroups (and in algebras) cannot be algorithmically solved.
In 1952 Novikov constructed the first example of the group with unsolvable problem of word equality (see \cite{Novikov1} and \cite{Novikov2}).
In 1962 Shirshov proved solvability of the equality problem for Lie algebras with one relation
and raised a question about finitely defined Lie algebras \cite{Sh}.
In 1972 Bokut settled this problem.
In particular, he showed the existence of a finitely defined Lie algebra over an arbitrary field
with algorithmically unsolvable identity problem \cite{Bokut}.



Nevertheless, some problems become decidable if a finite Gr\"obner basis
defines a relations ideal. In this case it is easy to determine whether two elements of the algebra are equal or not (see \cite{Bergman2}).
In his work, D. Piontkovsky extended the concept of obstruction,
introduced by V. Latyshev (see \cite{Piont,Piont2,Piont3,Piont4}).
V.N. Latyshev raised the question concerning the existence
of an algorithm that can find out if a given element is either a zero divisor
 or a nilpotent element when the ideal of
relations in the algebra is defined by a finite Gr\"obner basis.

Similar questions for monomial automaton algebras can be solved.
In this case the existence of an algorithm for nilpotent element or a zero divisor was
proved by Kanel-Belov, Borisenko and Latyshev \cite{BBL}. Note that these algebras are not Noetherian and not weak Noetherian.
Iyudu showed that the element property of being one-sided zero divisor is recognizable
in the class of algebras with a one-sided limited processing (see \cite{Iudu}, \cite{IuduDisser}).
It also follows from a solvability of a linear recurrence relations system on a tree (see \cite{Belov}).



An example of an algebra with a finite Gr\"obner basis and algorithmically unsolvable problem
of zero divisor is constructed in \cite{IP}.

A notion of {\it Gr\"obner basis} (better to say {\it Gr\"obner-Shirshov basis})
first appeared in the context of noncommutative (and not Noetherian) algebra.

Note also that Poincar\'e-Birkhoff-Witt theorem can be canonically proved using Gr\"obner bases.
More detailed discussions of these questions see in \cite{Bokut}, \cite{Uf2}, \cite{BBL}.






To solve these two problems we simulate a universal Turing machine, each step of which corresponds to a multiplication from the left by a chosen letter.




The problem of the algorithmic decidability of the existence of an isomorphism between two algebraic varieties is extremely interesting and fundamental. A closely related problem is the embeddability problem. In the general form, it is formulated as follows.


{\bf Embeddability problem.}\ {\it  Let $\mathscr{A}$ and $\mathscr{B}$ be two algebraic varieties. Determine whether or not there exists an embedding of $\mathscr{A}$ in $\mathscr{B}$. Find an algorithm or prove its nonexistence.
}


In this paper, a negative solution to this problem is given even for affine varieties over an arbitrary field of characteristic zero whose coordinate rings are given by generators and defining relations.

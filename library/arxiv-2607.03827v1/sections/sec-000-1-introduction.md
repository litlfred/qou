---
doc_id: arxiv-2607.03827v1
doc_title: "Affine cellular algebras and asymptotic algebras"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-5
source_pdf: 2607.03827v1.pdf
source_sha256: 965d69603381942a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.967
latex_coverage_ratio: 0.986
doc_brief: "Affine cellular algebras and asymptotic algebras — The theory of affine cellular algebras A is extended to incorporate their asymptotic algebras ˆA, clarifying unexpected differences between"
---
The aim of this article is to clarify new and sometimes unexpected
structures of affine cellular algebras and properties of embeddings into
asymptotic algebras, to illustrate these structures and properties by examples
and to
put them into the context of algebraic Lie theory. This continues and builds
upon \cite{KXaffine} and \cite{CKLS}.

Plenty of finite dimensional algebras arising in algebraic Lie theory have
been shown to be cellular algebras. For instance, group algebras of symmetric
groups and their Hecke algebras as well as classical Schur algebras, blocks
of the Bernstein-Gelfand-Gelfand category $\mathcal O$ of semisimple complex
Lie algebras, Temperley Lieb algebras and Brauer algebras are widely studied
examples of cellular algebras, as defined by Graham and Lehrer
\cite{GrahamLehrer}. The definition in \cite{GrahamLehrer}
is using combinatorial properties of a cellular basis that
allows to define and investigate cell modules, which generalise Specht
modules, Weyl modules and Verma modules. A cellular structure allows to
parametrise simple modules in terms of a finite partially ordered set, and to
describe them in terms of linear algebra over a field that has been fixed
from the beginning. 

Subsequently, an equivalent definition of cellularity has been given
\cite{KXcellular} in
terms of a finite chain of  two-sided ideals -- indexed by the same finite
partially ordered set -- with subquotients being direct sums of cell modules.
This led to further ring theoretical and homological properties. The easiest
cellular algebras are split semisimple, more general quasi-hereditary ones
still have finite global dimension and going beyond these, one arrives at
infinite global dimension \cite{KXwhenis}.
In the semisimple or quasi-hereditary case,
subquotients of the cell chain all are idempotent ideals, while in the
non-quasi-hereditary situation some subquotients necessarily have square zero. 

To extend cellularity to not necessarily finite dimensional algebras, in
\cite{KXaffine} affine cellular algebras have been introduced,
and then plenty of algebras have been
shown to be affine cellular, for instance affine Hecke algebras,
KLR algebras, affine Schur algebras and affine Temperley-Lieb algebras.
Here, there is a common affine ground ring and the cell chain still is
finite, indexed by a finite partially ordered set as before. However,
each subquotient comes with its own affine commutative ring and the
subquotient is, as a non-unital algebra, a generalised matrix ring
(introduced by Brown \cite{Brown1955}) over this affine commutative algebra,
with matrix multiplication deformed by adding a fixed matrix as an
intermediate third factor into ordinary matrix multiplication;
this matrix is called swich matrix. Simple modules still are finite
dimensional (now over quotients of the affine rings modulo maximal ideals)
and they are classified by a spectrum, depending on the entries of
the swich matrices. Finite products
of matrix rings over affine commutative rings can
be seen as the analogues of semisimple cellular algebras, and subquotients of
cell ideals that are idempotent produce an analogue of a quasi-hereditary
situation; this motivated Kleshchev to define graded affine quasi-hereditary
algebras \cite{Kleshchev}. In the general situation there are many
other cases than idempotent subquotients or those squaring to zero. As we
will show, the situation is controlled by determinants of swich matrices
(not) being a zero-divisor in the affine commutative
rings of the subquotients. 

Our main focus is on a new ingredient of affine cell theory: Given an affine
cellular algebra A, there exists \cite{KXaffine} an algebra called asymptotic
algebra $\hat{A}$, that is a direct sum of matrix algebras over the
affine rings associated with the subquotients in the cell chain of A, and
by \cite{KXaffine}
there is an algebra homomorphism from A to $\hat{A}$. The subquotients of the
cell chain of A coincide as sets with the components of $\hat{A}$. If A is
finite dimensional cellular in the sense of \cite{GrahamLehrer},
the homomorphism can be
injective only when A is semisimple and coincides with $\hat{A}$, which has
the same dimension. In a different way,
Lusztig had defined in \cite{Lusztig2} asymptotic algebras for Hecke algebras
of finite or affine type over ground rings that are not fields, but for
instance Laurent polynomial rings over the integers. In Lusztig's work and
its applications, asymptotic algebras and embeddings of Hecke algebras into
their asymptotic algebras turned out to be very useful in various respects. 
The general theory of asymptotic algebras of affine cellular algebras has been
started in \cite{KXaffine} and continued in \cite{CKLS}. The current article
aims at extending and deepening this theory, at clarifying the situation in
various applications and at identifying Lusztig's asymptotic $\hat{A}$
with those defined in \cite{KXaffine} in relevant situations.
\medskip

The main results of the theory being developed can be stated informally as
follows: Let $A$ be an affine cellular algebra as defined in \cite{KXaffine},
with a fixed affine cell chain $0=J_0 \subset J_1 \subset J_2 \subset \dots
J_n=A$ and subquotients $J_j/J_{j-1}$ being generalised matrix algebras, where
the multiplication in $J_j/J_{j-1}$ is deformed by adding a fixed middle factor
$\psi^{(j)}$ called swich matrix. Let
$\hat{A}$ be the asymptotic algebra of $A$ and $\iota: A \rightarrow \hat{A}$.
\smallskip

Finite dimensional cellular algebras are either quasi-hereditary
(the desirable case with the best properties), equivalently of finite global
dimension (see \cite{KXwhenis}), or not quasi-hereditary and equivalently
of infinite global dimension. Being quasi-hereditary means that all swich
matrices are invertible, which means their determinants are invertible.
Otherwise, at least some swich matrices have zero determinants.
As we will see, for affine cellular algebras, the desirable case is that the swich matrices are not zero-divisors. 

Under this frequently satisfied assumption, the connection between the
affine cellular algebra $A$ and its asymptotic algebra $\hat{A}$ is
particularly close, as shown by Theorems A, B and C.

\begin{Theox}[special case of Theorem \ref{TheoremAtext}]
  \label{TheoremA}
  Suppose that no determinant of a swich matrix $\psi^{(j)}$
  (for $j = 1, \dots, n$) is a zero-divisor.
  Then there is an embedding $\theta: A \rightarrow \hat{A}$, which is
  explicitly given by the isomorphisms between the endomorphism rings of
  the subquotients ${(J_j/J_{j-1})}_A$ and the generalised matrix rings. 
\end{Theox}

\begin{Theox}[Theorem \ref{TheoremBtext}]
\label{TheoremB}
Suppose that no determinant of a swich matrix $\psi^{(j)}$ (for $j = 1, \dots, n$)
is a zero-divisor and all cell subquotients are idempotent ideals in the
quotient algebras of $A$ modulo lower affine cell ideals. Then the embedding
$\theta: A \rightarrow \hat{A}$ induces a fully
faithful functor from torsionless $\hat{A}$-modules to A-modules.
\end{Theox}

Using $\theta$ yields a K-theoretic consequence. 

\begin{Theox}[Theorem \ref{TheoremCtext}]
\label{TheoremC}
Suppose that no determinant of a swich matrix $\psi^{(j)}$ (for $j = 1, \dots, n$)
is a zero-divisor and all cell subquotients are idempotent ideals in the
quotient algebras of $A$ modulo lower affine cell ideals. Then the
embedding $\theta: A \rightarrow \hat{A}$ is a weakly spectrum preserving
morphism in the sense of Baum and Nistor \cite{BN}.
\end{Theox}

As a consequence, Baum and Nistor's results allow in particular to identify
periodic cyclic homology of the two algebras. 
\medskip

The cell modules of the affine cellular algebra $A$ are direct summands of the
regular $\hat{A}$-module. This is related with another feature of the
asymptotic algebra, and also of smaller analogues of $\hat{A}$. 

\begin{Theox}[Theorem \ref{TheoremDtext}]
\label{TheoremD}
Suppose that no determinant of a swich matrix $\psi^{(j)}$ (for $j = 1, \dots, n$)
is a zero-divisor and all cell subquotients are idempotent ideals in the
quotient algebras of $A$ modulo lower affine cell ideals.

(a) The asymptotic algebra $\hat{A}$ of $A$ can be constructed as
centraliser algebra of endomorphism rings of direct sums of a full set
of cell modules of $A$. In particular, there is
a double centraliser property between $A$ and its asymptotic algebra $\hat{A}$.

(b) The same properties are satisfied for all members of a family of
algebras also including $\hat{A}$ and constructed as centraliser algebras
of endomorphism rings of certain direct sums of cell modules of $A$. 
\end{Theox}

This construction of $\hat{A}$ is quite different from the definition of
asymptotic algebras in \cite{KXaffine}.
\medskip

In the finite dimensional cellular case, homomorphisms between cell modules
rarely are injective, there are no non-zero injective endomorphisms apart
from automorphisms, and if there are no non-zero homomorphisms between
different cell modules at all, the cellular algebra must be semisimple. In
stark contrast to that, for KLR algebras of Dynkin type (shown to be graded
affine quasi-hereditary by Kleshchev, Loubert and Miemietz \cite{KLM}),
Kleshchev and Steinberg \cite{KS} have shown that non-zero endomorphisms
of cell modules exist and always are injective, but
there are no non-zero homomorphisms between different cell modules.
It turns out that from the affine cellular perspective this is not at all
surprising. 

\begin{Theox}[special cases of Theorem \ref{determinante} and Corollary
  \ref{regular}]
\label{TheoremE}
Suppose that subquotients in the affine cell chain are idempotent, their affine commutative rings are integral
domains and the determinants of the swich matrices are non-zero. Then
non-zero endomorphisms of cell modules always are injective and there are
no non-zero homomorphisms between non-isomorphic cell modules.
\end{Theox}

In the final section of this article, we will be
turning to Lie theoretic examples, illustrating the situations occurring in the
new theory and also identifying our asymptotic algebras and the embedding
$\theta$ in various situations, including classical and affine Hecke
algebras studied by Lusztig \cite{Lusztig2}, (see also the book
\cite{GeckJacon}). We also give a worked out small example and
describe in detail the situation
of extended affine Hecke algebras of type $A$, which had been shown
to be affine cellular in \cite{KXaffine}.
Moreover we refer to  various useful methods to verify the assumptions (in
particular on the determinants of swich matrices) of our results above, for
instance a method developed by Mathas in \cite{Mathas} and using the existence
of Jucys-Murphy elements, which can be used to compute Gram determinants
(in our situation aka determinants of swich matrices), as well as $A$ and
$\hat{A}$ becoming isomorphic after extension of scalars (sometimes known as
Lusztig's isomorphism), and using properties of Kazhdan-Lusztig bases.

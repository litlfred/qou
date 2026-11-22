---
doc_id: arxiv-2202.06733v1
doc_title: "Received <day> <Month>, <year>"
section_id: sec-006-23-application-to-generators-of-su3
section_title: "Application to generators of SU(3)"
section_number: 2.3
pages: 3-5
source_pdf: 2202.06733v1.pdf
source_sha256: e670632090447f14
toc_source: outline
text_source: latex
latex_prose_ratio: 0.978
latex_coverage_ratio: 1.0
doc_brief: "Received <day> <Month>, <year> — Diﬀerent ways of representing the group 푆푈(3) within a Geometric Algebra approach are explored."
---
As discussed above, we now want to look at the characteristic multivectors for the case of the generators of the group $SU(3)$. There has been recent attention to $SU(3)$ in a Geometric Algebra context from the work by Martin Roelfs in his thesis, and he has translated some of this into a conventional {\em matrix} approach in the paper {\em `Geometric invariant decomposition of $SU(3)$'}\cite{roelfs2021geometric}. The specific GA results for an invariant commuting bivector decomposition of a generator of $SU(3)$ are given as an example in the recent paper by Roelfs and de Keninck {\em `Graded Symmetry Groups: Plane and Simple'}\cite{roelfs2021graded}.
This latter paper systematises the decomposition of rotors and bivectors, in a way which makes explicit, in higher dimensions, the methods sketched out in Hestenes \& Sobczyk\cite{hestenessobczyk}.

As a starting point on $SU(3)$ in the present paper, we want to show how the characteristic polynomial necessary to do the split of generators into commuting bivectors, arises in the characteristic multivector approach being pursued here.

So we now let the linear function $f(a)$ discussed in Sections~\ref{sect:char-mult} and \ref{sect:cay-ham}  be not a finite \alert{rotation}

\be
a \mapsto f(a)=R a \Rrev
\ee

as considered in \cite{lasenby-char-multi}, but the \alert{generator} of a finite rotation:

\be
a \mapsto f(a)=B\dt a
\ee

for the bivector $B$, which is related to $R$ by

\be
R=e^{-B/2}
\ee


We are going to work here (though not in the second part of the paper, where we will use quite different approaches) within the approach to unitary groups of the Doran et al.\ paper {\em `Lie Groups as Spin Groups'}\cite{doran1993lie}.

The essential point is that for $SU(3)$ we end up with a 6-dimensional algebra in which the action of a bivector generator $B$ on a vector $a$ is $B\dt a$, as above.
The bivector $B$ is not the most general possible within the 6-d algebra, which has 15 independent bivectors, but is picked out by commuting with $J$, the effective imaginary for the space, which if the 6 basis vectors are $\{e_1,e_2,e_3,f_1,f_2,f_3\}$, all mutually orthogonal and squaring to 1, is defined by

\be
J=e_1f_1+e_2f_2+e_3f_3
\ee


Enumerating the possibilities yields (up to normalisation) 9 bivectors, which we call:

\be
\begin{gathered}
E_{ij}= e_i e_j + f_i f_j,\quad i<j\\
F_{ij}= e_i f_j + e_j f_i,\quad i<j\\
J_i=e_i f_i, \quad i=1,2,3 \quad \text{(no sum)}
\end{gathered}
\label{eqn:generators}
\ee


Introducing the {\em commutator product} $A\crs B=\half(AB-BA)$ for two GA quantities $A$ and $B$, then the bivector generators picked out as satisfying $B\crs J=0$ define the unitary group. Those satisfying the additional constraint that $B\dt J=0$ then define the special unitary group (for which the generator matrices are traceless).

This condition reduces the 9 generators of equation (\ref{eqn:generators}) to 8 since each $J_i$ satisfies $J_i\dt J=-1$ meaning that only combinations of the $J_i$ of the form

\be
\alpha_1 J_1 + \alpha_2 J_2 +\alpha_3 J_3, \quad \text{where} \quad \alpha_1  + \alpha_2  +\alpha_3 = 0
\ee

can be used as a generator of $SU(3)$

So far this is all well understood from the perspective of the `Lie Groups as Spin groups' paper\cite{doran1993lie} and Chapter~11 of the Doran \& Lasenby book\cite{d2003geometric}. However, we now want to give some specific details for $SU(3)$ which go beyond the details presented in those, and then discuss the role of characteristic multivectors. We note that the approach being followed here as regards how the `Lie Groups as Spin groups' setup is implemented, differs somewhat from the Roelfs approach, in that here, as already described, we are taking the bivectors $B$ as operating upon a concrete vector $a$ in the 6d space. In the Roelfs approach, the bivector algebra is taken as being an abstract one, basically equivalent to the matrix algebra, where we do not need to think of it operating upon anything. Given that our $B$ operates via a `dot product' with a vector $a$, it is not immediately obvious that this action can be stripped off from $a$ itself, but the detailed correspondence of results (see below), plus a more detailed study of the approach (unpublished notes) suggests this is not a problem.

We can relate our generators to the Gell-Mann $SU(3)$ matrices, $\lambda_1, \ldots \lambda_8$ as follows:

\be
\begin{gathered}
\lambda_2=\half E_{12}, \quad \lambda_5=\half E_{13}, \quad \lambda_7=\half E_{23},\\
\lambda_1=\half F_{12}, \quad \lambda_4=\half F_{13}, \quad \lambda_6=\half F_{23},\\
\lambda_3=\half\left(J_1-J_2\right), \quad \lambda_8=\textstyle{\frac{\sqrt{3}}{6}}\left(J_1+J_2-2J_3\right)
\label{eqn:lambda-defs}
\end{gathered}
\ee

We have used equals signs here --- the important point is that the GA quantities on the left satisfy the same algebra as the Gell-Mann matrices.
Because they are GA quantities, however, interesting geometric structural relations come to light. E.g.\ an interesting relation is

\be
I\left(\lambda_i \wdg \lambda_j\right) = \textstyle{\frac{1}{6}} \delta_{ij} J - d_{ijk}\lambda_k
\ee

where $I$ is the pseudoscalar for the overall 6d space, and $d_{ijk}$ are the \alert{symmetric} structure constants of the $SU(3)$ algebra. We can see how \alert{duality} brings the exterior product of the $\lambda$'s back to representation in terms of bivectors.

We now get to the point we wish to emphasise here w.r.t.\ characteristic multivectors and the Cayley-Hamilton theorem. With $f(a)=B\dt a$, where $B$ is a generator bivector in $SU(3)$, we will now systematically find the full set of characteristic multivectors. The first is

\be
\partial_{(1)} f_{(1)} = \sum_{j=1}^m a^j b_j=a^j(B\dt a_j) =-a^j(a_j\dt B) = -\da(a\dt B)=-2B
\ee

Note the scalar part of this is the \alert{trace}, which is 0

For the next one we define some coefficients $B_i$ via

\be
B=B_i \lambda_i
\label{eqn:gen-su3-B}
\ee

where $i$ is summed over $1,\ldots,8$, and we will define the `length' of $B$ via

\be
|B|^2=B_i B_i
\ee

Then we get
\be
\partial_{(2)} f_{(2)} = 2B^2+\textstyle{\frac{3}{2}}|B|^2 = 2 B\wdg B +\half |B|^2
\ee

and the scalar invariant is the `length' of $B$, which makes sense

For the third one we have to introduce a bit more notation. This is in order to discuss the `determinant' of the transformation.  It is useful in the current context to define exactly what determinant we are talking about via the matrices. Thus let $\Lambda_i$, $i=1,\ldots ,8$ be the actual Gell-Mann matrices (ordinarily called $\lambda_i$!), and let us form, in matrix terms, the general generator

\be
M=B_i \Lambda_i = \left[\begin{array}{ccc}
B_3+\frac{B_8\sqrt{3}}{3} & B_1-B_2 j & B_4-B_5 j \\
B_1+B_2 j & -B_3+\frac{B_8 \sqrt{3}}{3} & B_6-B_7 j \\
B_4+B_5 j & B_6+B_7 j & -\frac{2 B_8 \sqrt{3}}{3}
\end{array}\right]
\ee

The determinant we are talking about is then $\det(M)$, which is real, so we can use it without having to worry about incorporating a scalar imaginary into our 6d formalism.

So for $r=3$ we find:

\be
\partial_{(3)} f_{(3)} = -\half |B|^2 B+\textstyle{\frac{1}{4}}\left(J+4I\right) \det(M)
\label{eqn:simp-deriv3}
\ee

which has grades 2 and 6.

For $r=4$ we find:

\be
\partial_{(4)} f_{(4)} = \half \det(M) IB +\textstyle{\frac{1}{16}}|B|^4
\ee

which has grades 0 and 4.

For $r=5$

\be
\partial_{(5)} f_{(5)} = \textstyle{\frac{1}{8}} \det(M) I(B\wdg B)
\ee

which is grade 2 only.

Finally, for $r=6$ we get:

\be
\partial_{(6)} f_{(6)} = \textstyle{\frac{1}{64}} \det^2(M)
\ee

i.e.\ grade 0 only. It is interesting that this `top level' characteristic multivector, which would normally return the determinant of the transformation (see Hestenes \& Sobczyk), here returns the determinant {\em squared}. We will shortly understand why this is.

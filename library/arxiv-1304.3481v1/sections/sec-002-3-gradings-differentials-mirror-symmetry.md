---
doc_id: arxiv-1304.3481v1
doc_title: "Quadruply-Graded Colored Homology of Knots"
section_id: sec-002-3-gradings-differentials-mirror-symmetry
section_title: "Gradings, Differentials, Mirror Symmetry"
section_number: 3
pages: 19-35
source_pdf: 1304.3481v1.pdf
source_sha256: d0840f2775c0f761
toc_source: outline
text_source: latex
latex_prose_ratio: 0.95
latex_coverage_ratio: 0.988
doc_brief: "Quadruply-Graded Colored Homology of Knots — We conjecture the existence of four independent gradings in the colored HOMFLY homology."
---
\label{sec:gradings}



\subsection{Introduction}
For any Young diagram $\lambda$, the $\lambda$-colored HOMFLY polynomial of a knot $K$, denoted $P^{\lambda}(K)(a,q)$, is a two-variable polynomial knot invariant whose $a=q^N$ one-variable specialization \eqref{PPN} equals the quantum knot invariant obtained by the representation $\lambda$ of the quantum $sl(N)$. Throughout the paper, $P^{\lambda}(K)$ denotes the reduced polynomial, i.e. it is normalized so that the value of the unknot is equal to 1.

We conjecture the existence of the homology theory $\CH^{\lambda}(K)$ categorifying the polynomials $P^{\lambda}(K)$, i.e. such that its graded Euler characteristic is equal to $P^{\lambda}(K)$. Although we do not give
the explicit definition of these homology theories, the insight from physics, representation theory and the double affine Hecke algebras (DAHAs) predict a very rich structure of differentials on $\CH^{\lambda}(K)$, together
with various symmetries of $\CH^{\lambda}(K)$. We focus on rectangular Young diagrams $\lambda$, i.e. Young diagrams which have the form of a rectangle with $R$ rows and $S$ columns, and which will be denoted $\lambda= R\times S$. This is a large class of representations, that includes as particular cases all symmetric representations ($R=1$) and antisymmetric ones ($S=1$).\footnote{Although many of the properties and results still hold for non-rectangular representations, there are certain subtleties in that case. We discuss this in section \ref{hooks}.}

Our main results for $\CH^{\lambda}(K)$ can be split in two groups, which match together perfectly.
First, we conjecture that certain, grading-independent structures exist and the following properties hold on $\CH^{\lambda}(K)$:
\begin{itemize}
\item $\CH^{\lambda}(K)$ is finite-dimensional.

\item There are two symmetries on $\CH^{\lambda}(K)$: one is the {\it mirror symmetry} that switches between $\lambda$ and its transpose partition $\lambda^t$:
\be
\CH^{\lambda}(K)\cong \CH^{\lambda^t}(K).
\ee
The other one is the {\it self-symmetry} on $\CH^{\lambda}(K)$.
While the mirror symmetry categorifies the known relation for the colored HOMFLY polynomials \eqref{PPmir}:
\be
P^{\lambda}(K)(a,q)=P^{\lambda^t}(K)(a,q^{-1}),
\ee
the self-symmetry is a completely new symmetry, that does not categorify any polynomial relation. It uses homological grading in a non-trivial way, and exists only on the homological level.

\item For every pair of non-negative integers $(n,m)$, such  that $n\ge R$ or $m\ge S$,\footnote{For other values of $m$ and $n$ the differentials may exist in the unreduced theory,
which we do not cover in details here.}
 there exists a collection of differentials $d_{n|m}$ on $\CH^{\lambda}(K)$, such that they pairwise anti-commute, and such that the homology of $\CH^{\lambda}(K)$ with respect to $d_{n|m}$ is
isomorphic to the homology $\CH^{sl(n|m),\lambda}(K)$ that categorifies the quantum invariant of a knot $K$
labeled by a representation $\lambda$ of $sl(n|m)$:
\be
H^*(\CH^{\lambda}(K),d_{n|m}) = \CH^{sl(n|m),\lambda}(K).
\ee
Introducing this two-parameter collection of differentials is one of the main goals
of the present paper\footnote{Although some of these operators were implicitly defined in \cite{G} for the uncolored homology, there relation to supergroups was not understood there.}. All previous results on the structural properties of the colored HOMFLY homologies (fundamental \cite{DGR} and symmetric ones  \cite{GS}) predicted only the existence of one-parameter family of anti-commuting differentials, with the parameter $N$ representing the rank of $sl(N)$ specializations.
As we shall explain, various reasons suggest that introduction of a two-parameter family associated with $sl(n|m)$ representations is a much more natural thing to do.

\item There exist {\it colored} differentials that change representations (colors). In other words, they allow passage from one homology theory $\CH^{\lambda}(K)$ to another one $\CH^{\mu}(K)$, for some Young diagram $\mu \subset \lambda$. More precisely, colored differential $d_{\lambda\to\mu}$ on $\CH^{\lambda}(K)$ has the property that the homology of $\CH^{\lambda}(K)$ with respect to $d_{\lambda\to\mu}$ is isomorphic to $\CH^{\mu}(K)$.







The main group of colored differentials, namely the group of $2(R+S-1)$ differentials,
is directly related to particular differentials $d_{n|m}$. More precisely, for every Young diagram $\mu$ that is obtained from $\lambda$ by removing either some of its rows or some of its columns,
there should be two different differentials of the form $d_{\lambda\to\mu}$ such that
\be\label{coliso}
H^*(\CH^{\lambda}(K),d_{\lambda\to\mu})=\CH^{\mu}(K).
\ee
They "lift" the relation  $\CH^{sl(n|m),\lambda}(K)\cong\CH^{sl(n|m),\mu}(K)$ coming from the isomorphism $\lambda \cong \mu$ as $sl(n|m)$ representations for appropriate values of $n$ and $m$, and we also denote such differential by $d^{col}_{n|m}$.  In other words, we have the following commutative diagram:

\begin{tabular}{ccc}
\quad\quad$\CH^{\lambda}(K)$ & $\xrightarrow{d_{\lambda\to \mu}\,\,\,\,(\mathrm{i.e.}\,\,\,\, d^{col}_{n|m})}$ & $\CH^{\mu}(K)$\cr
\quad\quad $\vline$ & & $\vline$ \cr
\quad\quad${\scriptstyle d_{n|m}}$ & & ${\scriptstyle d_{n|m}}$\cr
\quad\quad $\downarrow$ & & $\downarrow$ \cr
\quad\quad$\CH^{sl(n|m),\lambda}(K)$ & $\xrightarrow{\qquad \cong \qquad}$ & $\CH^{sl(n|m),\mu}(K)$
\end{tabular}

\noindent We note that on $\CH^{\lambda}(K)$ the differentials $d_{n|m}$ and $d^{col}_{n|m}$ share many similar properties. In particular, frequently the differential $d_{n|m}$ on $\CH^{\mu}(K)$ acts trivially, and then on $\CH^{\lambda}(K)$ the differentials $d_{n|m}$ and $d^{col}_{n|m}$ coincide.

\item For large classes of knots, including torus knots and two-bridge knots, the size of the homology $\CH^{\lambda}(K)$ is equal to the $|\lambda|$-th power of the dimension of $\CH^{\tableau1}(K)$. For an arbitrary knot $K$, such relation holds asymptotically  when $|\lambda|$ tends to infinity.

\end{itemize}

Our second major conjecture is that the colored HOMFLY homology $\CH^{\lambda}(K)$ of a knot $K$ is {\it quadruply-graded}. We  denote these four gradings by $a,q,t_{r},t_{c}$. Thus, apart from the $a$- and $q$-gradings associated to each generator, we also assign two homological $t$-gradings.
Any of the two $t$-gradings give a categorification of $P^{\lambda}(K)$, i.e. forgetting one of them gives triply-graded categorification of the colored HOMFLY-polynomial. In other words, if we denote the (four-variable) Poincar\'e polynomial of $\CH^{\lambda}(K)$ by $\CP^{\lambda}(K)(a,q,t_r,t_c)$, then we have
\be
\CP^{\lambda}(K) (a,q,t_{r}=-1,t_c=1) = \CP^{\lambda}(K) (a,q,t_r=1,t_{c}=-1) = P^{\lambda}(K)(a,q).
\ee




The appearance of the fourth grading is rather mysterious from the geometric point of view, but it seems to be inevitable. Let us list some of the evidences.
First of all, in the case of symmetric and anti-symmetric representations, the corresponding homology $\CH^{\lambda}(K)$ has been studied in the literature, and although the results in various papers are isomorphic, there are two different conventions for the homological $t$-gradings. The $t_r$-grading that we propose is the $t$-grading assigned to a generator of $\CH^{\lambda}(K)$
in the grading conventions of \cite{FGS2,GS}, whereas one can interpret $t_{c}$ as
the $t$-grading assigned to a generator of $\CH^{\lambda}(K)$ in grading conventions of \cite{AShakirov,DMMSS,DGR,GWalcher}.
As argued in \cite{GS}, the ``mirror symmetry'' --- the symmetry that relates the homology colored by a Young diagram and its transposed --- exchanges the two grading conventions. However, despite being very similar, one cannot pass from one convention to another by an explicit gradings transformation.
The solution that we propose is to keep track of both $t$-grading conventions together, and regard the homology $\CH^{\lambda}$ as
quadruply-graded theory, with four independent gradings $a,q,t_r$ and $t_c$.

The definite advantage of the quadruply-graded theory is that it makes
all of the structural properties and isomorphisms completely explicit. This cannot be achieved by a triply-graded theory: for example in the case of the symmetric representations (see \cite{GS}) only a few of the isomorphisms and symmetries could be made explicit.
In quadruply-graded theory $\CH^{\lambda}(K)$ one has completely explicit mirror symmetry and self-symmetry. Moreover, the
re-grading in all of the isomorphisms of colored differential (\ref{coliso})
can be made explicit, in all gradings. Finally, the exponential growth conjecture for the size of the colored homology becomes a totally refined exponential growth property of an appropriate three-variable Poincar\'e polynomial.
What is even more miraculous, is that all these symmetries, isomorphism re-gradings and exponential growth property have
rather simple and pleasant expressions. Moreover, all of them
become particularly elegant with the introduction of an auxiliary
grading, called the $Q$-grading, defined in a following simple way:
\be\label{Qgrad1}
Q=\frac{q+t_r-t_c}{R}.
\ee
This new grading, which can be considered as certain ``corrected'' $q$-grading,  cannot be seen on the decategorified, polynomial level, and as the formula indicates, both $t$-gradings are
needed for its definition. Therefore we need the quadruply-graded theory in order to have all explicit properties, and only a few of various symmetries and isomorphisms have polynomial counterparts at the decategorified level.

Finally, the symmetries get the nicest form when the homology is written in $(a,Q,t_r,t_c)$-gradings. Because of a linear relation between the gradings (\ref{Qgrad1}), this is just a simple re-grading of $\CH^{\lambda}(K)$. However, due to its importance, we give it a special name, $\tilde{\CH}^{\lambda}(K)$, and refer to it as the {\it tilde-version} of colored HOMFLY homology. Thus, it is given by:
\be
\tilde{\CH}^{\lambda}_{i,j,k,l}(K) \; := \; {\CH}^{\lambda}_{i,Rj-k+l,k,l}(K).
\ee
The only case when the two $t$-gradings coincide is the uncolored case, $\lambda=\tableau1$, and the resulting homology is
triply-graded in agreement with \cite{DGR}. In this case the $q$- and $Q$-gradings coincide, and the mirror symmetry and the self-symmetry are in fact the same symmetry.

Now we start with the detailed description of the structure of the quadruply-graded colored HOMFLY homology.



\subsection{Self-symmetry}
There are two remarkable symmetries in the colored homology when color is given by a rectangular Young diagram $\lambda$. The first one is self-symmetry on the homology ${\CH}^{\lambda}(K)$ and the second one is the mirror symmetry that relates the ${\CH}^{\lambda}(K)$ and ${\CH}^{\lambda^t}(K)$ homologies.

The main advantage of the $Q$-grading is that in the quadruple $(a,Q,t_r,t_c)$-grading both symmetries have a very simple and beautiful form. Thus, we present them in the corresponding tilde-version $\tilde{\CH}^{\lambda}(K)$.

\begin{conjecture}
The homology $\tilde{\CH}^{\lambda}(K)$ enjoys the following self-symmetry:
\be\label{selfsym}
{\boxed{\phantom{\int}\tilde{\CH}^\lambda_{i,j,k,l}(K) \cong  \tilde{\CH}^\lambda_{i,-j,k- Rj,l-Sj}(K).\phantom{\int}}}
\ee
\end{conjecture}

Moreover, we conjecture the existence of an involution $\Phi_{\lambda}:\CH^{\lambda}(K)\to\CH^{\lambda}(K)$
such that
$$(a,Q,t_r,t_c)[\Phi_{\lambda}(x)]=(a(x),-Q(x),t_{r}(x)-RQ(x),t_{c}(x)-SQ(x)).$$

Note that this symmetry does not descend to any relation on the colored HOMFLY polynomial (except in the uncolored case $\lambda=\tableau1$). In fact, due to a nontrivial presence of the $Q$-grading, it can be seen only on the quadruply-graded homology, and as to our knowledge, such symmetry has not been observed before.


For some knots, including torus knots (see below) we also conjecture that this involution comes from some version of the hard Lefshetz isomorphism. Namely, there exists an operator $L_{\lambda}:\CH^{\lambda}(K)\to\CH^{\lambda}(K)$
such that
\begin{equation}
\label{Llambda}
(a,q,Q,t_r,t_c)[L_{\lambda}]=(0,R+S,2,R,S),\quad \Phi_{\lambda}(x)=L_{\lambda}^{-Q(x)}.
\end{equation}
Note, according to the ``dictionary'' \eqref{aqtgradings} this operator is a bound state of $R+S$ D0-branes.


\subsection{Mirror symmetry}


Based on results for symmetric and anti-symmetric representations, it was conjectured \cite{GS} that colored HOMFLY homology enjoys mirror symmetry:
\begin{conjecture}(\cite{GS})\label{mirsymold}
For any knot, there exists an isomorphism (called {\it mirror symmetry}) between $\lambda$- and $\lambda^t$-colored HOMFLY homologies
preserving the $a$-grading and reversing the $q$-grading.
\end{conjecture}

However, to obtain the behavior of the $t$-gradings under this symmetry, one needs to introduce the fourth grading.
We are able to write an explicit formulas for the $t$-degrees change in the case of rectangular $\lambda$.
We start with a {\em different} conjectural symmetry between $\lambda$- and $\lambda^{t}$-colored homology.

\begin{conjecture}
In $(a,Q,t_{r},t_{c})$ gradings one has
\be\label{mirsym}
{\boxed{\phantom{\int}\tilde{\CH}^{\lambda^t}_{i,j,k,l} (K)\cong  \tilde{\CH}^\lambda_{i,j,l,k}(K).\phantom{\int}}}
\ee
\end{conjecture}

In order to obtain the explicit quadruply-graded version of the mirror symmetry from (\ref{mirsymold}), we combine self-symmetry (\ref{selfsym}) and mirror symmetry (\ref{mirsym}):

\begin{corollary}\label{mirsim}
In $(a,Q,t_{r},t_{c})$ gradings one has
\be\label{mirsymnew}
{\boxed{\phantom{\int}\tilde{\CH}^{\lambda^t}_{i,j,k,l}  (K)\cong  \tilde{\CH}^\lambda_{i,-j,l-Sj,k-Rj}(K).\phantom{\int}}}
\ee
\end{corollary}

The last equation enables one to write the explicit change of gradings in the mirror symmetry. Denote by $M_{\lambda}:\CH^{\lambda} \to \CH^{\lambda^t}$ the mirror symmetry isomorphism.
Consider the gradings of a generator $x$ in $\CH^{\lambda}$ theory and the gradings of the generator $M_{\lambda}(x)$ of $\CH^{\lambda^t}$, denoted by $(\hat{a},\hat{q},\hat{Q},\hat{t}_r,\hat{t}_c)$, where $\lambda$ is an $R\times S$ rectangular Young diagram and $\lambda^t$ is $S\times R$ rectangular Young diagram. They are related by the following transformation:
\begin{eqnarray*}
\hat{a} &=& a,~ \qquad \hat{q} = -q,~ \qquad \hat{Q}  =  -Q,\\
\hat{t}_r &=& t_c- S Q = (1+\frac{S}{R})t_c - \frac{S}{R} t_r - \frac{S}{R} q,\\
\hat{t}_c &=& t_r-  R Q = t_c- q.
\end{eqnarray*}

Since the mirror symmetry (\ref{mirsymnew}) inverts the $q$-grading, it ``categorifies'' the following relation between the colored HOMFLY polynomials:
\be
P^{\lambda}(K)(a,q)=P^{\lambda^t}(K)(a,q^{-1})
\ee
which is often attributed to level-rank duality.


\subsection{$sl(n|m)$ differentials}
\label{sec:supermn}

The homology $\CH^{\lambda}(K)$ comes with a large structure of pairwise anti-commuting differentials on it. We conjecture that there exists a differential for every pair of nonnegative integers $(n,m)$, such that $n\ge R$ or $m\ge S$. These differentials should be related to the homologies
corresponding to Lie superalgebras $sl(n|m)$ and representations labeled by Young diagram $\lambda$. The condition that $n\ge R$ or $m\ge S$ gives precisely those pairs $(n,m)$ for which the Lie superalgebra $sl(n|m)$ has an irreducible representation labeled by $\lambda$ (see Section  \ref{repsup}).
This generalizes the structure from \cite{DGR} and \cite{GS}, where the analogous differentials are labelled by a single integer $N$ and were related to the $sl(N)$ representations, i.e. $sl(N)$ specializations of the $\lambda$-colored HOMFLY polynomial. As we shall argue in this paper, the structure corresponding to Lie superalgebras is more natural, and the single parameter $N$ from \cite{DGR} and \cite{GS} is just a super-rank of a corresponding Lie superalgebra:
\be
N = n - m.
\ee

\vskip 0.3cm

This structure has appeared in the physics literature \cite{VafaUNM,WittenK} as a symmetry of brane/anti-brane systems,
which makes it especially easy to implement it in the brane system \eqref{theoryB} or, better yet, in the dual system \eqref{theoryA}
where the rank $N$ enters as the number of five-branes.

In this framework, replacing $sl(N)$ by a Lie superalgebra $sl(n|m)$ can be easily implemented by replacing $N$ five-brane
with a system of $n$ five-branes and $m$ anti-branes.

Another, more supersymmetric way to realize quantum and homological invariants of knots labeled by $sl(n|m)$ representations
is to consider $n$ five-branes supported on $\R \times W \times D$ exactly as in \eqref{theoryA} and introduce
$m$ new five-branes supported on $\R \times W \times D'$, such that $\C \cong D' \subset M_4$ and $D \cap D' = \{ 0 \}$,
\bea
\text{space-time} & : & \qquad \R \times T^* W \times M_4 \nonumber \\
n~\text{M5-branes} & : & \qquad \R \times W \times D \label{theoryAmn} \\
m~\text{M5-branes} & : &  \qquad \R \times W \times D' \nonumber
\eea
For instance, if $M_4 \cong \C^2$ is parametrized by coordinates $(z_1,z_2)$, then we can choose $D =\{ z_1 = 0 \}$ and $D' = \{ z_2 = 0 \}$.
Furthermore, identifying $M_4$ with the Taub-NUT space and reducing on the circle fiber takes us from M-theory
to type IIA string theory with a system of D4-branes and D6-branes shown in Figure \ref{fig:D4D6}.

\begin{figure}[htb]
\centering
\includegraphics[width=3.0in]{D4D6a}
\caption{In the approach of \cite{fiveknots}, homological invariants of knots labeled by representations of $sl(n|m)$
can be realized by a system of $n$ semi-infinite D4-branes ending on one side of the D6-brane and $m$ semi-infinite D4-branes ending on the other side of the D6-brane.}
\label{fig:D4D6}
\end{figure}

Then, as in \cite{fiveknots}, homological $sl(n|m)$ knot invariants can be obtained by ``counting''
solutions to the following partial differential equations on a 5-manifold $\R \times W \times \R_y$:
\begin{align}
F^+ - \frac{1 }{ 4} B \times B - \frac{1 }{ 2} D_y B & = 0 \notag \\
F_{y i} + D^{j} B_{j i} & = 0 \notag
\end{align}
with the prescribed behavior near the ``interface'' $y=0$:
$$
B \simeq \frac{B_0^{(\pm)} }{ y} \quad \text{as} \quad y \to \pm 0 \,.
$$
Here, $B$ is a section of $\Omega^{2,+} (\R \times W) \otimes {\rm ad} (E)$, so that
$$
(B \times B)_{ij} = \sum_{k} [B_{ik} , B_{jk}]
$$
Relegating further study of this physical system to a future work, we now return to the discussion of mathematical structures that we expect to see in such physical realizations of homological $sl(n|m)$ knot invariants.\\

\begin{conjecture}
For every pair of nonnegative integers $(n,m)$ such that $n\ge R$ or $m\ge S$ there exists a differential $d_{n|m}$ on the homology $\CH^{\lambda}(K)$, satisfying the following properties:

\begin{itemize}
\item {\bf Specialization:}
\be
(\CH^{\lambda}(K),d_{n|m})|_{a=q^{n-m}} \cong \CH^{sl(n|m),\lambda}(K).
\ee

\item  {\bf Anticommutativity:} All $d_{n|m}$ pairwise anti-commute.

\end{itemize}

\end{conjecture}

The homology theory $\CH^{sl(n|m),\lambda}(K)$  categorifies $(n-m)$-specialization of the $\lambda$-colored HOMFLY polynomial. In other words:
\be
\CP^{sl(n|m),\lambda}(K)(q,t=-1)=P^{\lambda}(K)(a=q^{n-m},q).
\ee
Although the right hand side of the above relation equals the quantum polynomial invariant associated with $sl(n|m)$ representations labeled by $\lambda$, it depends only on the super-rank of the Lie superalgebra. However, the homologies $\CH^{sl(n|m),\lambda}(K)$ for various pairs $(n,m)$ with fixed $n-m$ can in general be non-isomorphic. That is one of the reasons why we expect to have differentials parametrized by two integers instead of just one, as it was predicted for the fundamental representation \cite{DGR} and for the
symmetric representations \cite{GS}.

The main reason for the existence of such structure comes from the representation theory of the Lie superalgebras $sl(n|m)$. The condition that $n\ge R$ or $m\ge S$ gives precisely those pairs $(n,m)$ for which the Lie superalgebra $sl(n|m)$ has an irreducible representation labeled by $\lambda$. We denote the subset of the $(x,y)$ plane satisfying $x\ge 0$, $y\ge 0$ and $x\ge R$ or $y\ge S$ by $\Omega$. Then, the set of all admissible pairs $(n,m)$ for which we have a differential $d_{n|m}$ consists exactly of the points from $\Omega$ whose both coordinates are integers.

As for the degrees of the differentials $d_{n|m}$, we have the following:
\be
(a,q)[d_{n|m}]=(-2,2(n-m)),
\ee
in agreement with the specialization $a=q^{n-m}$. The $t_c$-degree is equal to
\be
t_c[d_{n|m}]=-2m-1.
\label{tcdegnm}
\ee
The $t_r$-degree is more subtle, and is given in the next section; in particular, it depends on $R$ and $S$.


In  the case of the fundamental \cite{DGR} and the symmetric representations \cite{GS}, the conjectured differentials $d_N$ were parametrized by a single integer $N$. It was argued that they correspond to the $sl(N)$ representations for $N>0$, while for the other values of $N$ there was no clear motivation. However, when observed from the $sl(n|m)$ point of view, they become much more natural: $d_N$ becomes in fact precisely the differential $d_{n|m}$, where $n$ and $m$ are uniquely determined by requiring that $N=n-m$ and such that $(n,m)$ lies on the boundary of $\Omega$,
see Figure \ref{fig:domain}.

\begin{figure}[htb]
\centering
\includegraphics[width=4.0in]{coloredD}
\caption{Domain $\Omega$ can be visualized as the complement of $\lambda^t$ in a positive quadrant of the $(n,m)$ plane.
Integer points on its boundary correspond to differentials $d_{n|m}$ or, equivalently, $d_N$ with $N=n-m$, among which three are special.
They correspond to the three corners of the domain $\Omega$ and are marked by red bullets.
The differentials for this examples are shown in Figure \ref{sunflower}.}
\label{fig:domain}
\end{figure}


In the case of the fundamental representation, the $t$-degrees of the differentials $d_N$ were defined in a rather artificial way.

By using 
the conventions from above, we get directly the desired degrees. (Note that in the fundamental representations the two $t$-gradings coincide: $t_r=t_c=t$.)
Indeed, for $N>0$, we have $d_N=d_{N|0}$, and therefore according to \eqref{tcdegnm} their $t$-degrees are equal to $-1$. For $N=0$, we have that $d_0=d_{1|1}$,  so the $t$-degree of $d_0$ equals $-3$, while for $N>0$, we have that $d_{-N}=d_{0|N}$, and so the $t$-degree of  $d_{-N}$ equals $-2N-1$, exactly as predicted in \cite{DGR}.


Although there are infinitely many integer pairs in $\Omega$, for a given knot $K$ only finitely many of the differentials $d_{n|m}$ can act non-trivially. Indeed, since $\CH^{\lambda}(K)$ is finite-dimensional and since $q(d_{n|m})=2(n-m)$ and $t_c(d_{n|m})=-2m-1$,
the differential $d_{n|m}$ becomes void on $\CH^{\lambda}(K)$ for sufficiently large values of $n$ or $m$. Thus we have:

\begin{conjecture}\label{con1}
For a knot $K$ and a rectangular Young diagram $\lambda$, we have
\begin{equation}\label{coneq1}
\CP^{sl(n|m),\lambda}(K)(q,t_r,t_c)=\CP^{\lambda}(K)(a=q^{n-m},q,t_r,t_c),
\end{equation}
when either $n$ or $m$ is sufficiently large.
\end{conjecture}


\subsection{Colored differentials}\label{coldif}

For every knot $K$, the homology theory $\CH^{\lambda}(K)$ comes with a remarkable structure of the so-called {\it colored} differentials that allow passage to homology theories $\CH^{\mu}(K)$ for various partitions $\mu \subset \lambda$. In other words, for certain such partitions $\mu$, there exists a differential $d$ on $\CH^{\lambda}(K)$ such that the homology with respect to this differential is isomorphic to $\CH^{\mu}(K)$, i.e.
\be\label{prob1}
H^*(\CH^{\lambda}(K),d) \cong \CH^{\mu}(K).
\ee
As we shall describe, the possible partitions $\mu$ will be the ones that can be obtained by removing either some rows or some columns from $\lambda$.
All these differentials are in fact ``lifting'' $sl(n|m)$ differentials $d_{n|m}$ for some specific values of $(n,m)$ that are on the boundary of the region $\Omega$, see Figure \ref{fig:domain}. These are precisely the pairs $(n,m)$ such that $\lambda\cong\mu$ as $sl(n|m)$ representations (see section \ref{repsup}). We denote the corresponding colored differential by $d^{col}_{n|m}$, and the ``lifting'' property is given by the following commutative triangle:

\begin{tabular}[c]{ccc}
\quad\quad\quad$\CH^{\lambda}(K)$ & $\xrightarrow{\quad d^{col}_{n|m}\quad}$ & $\CH^{\mu}(K)$\cr
\quad\quad\quad $\vline$ & & $\vline$ \cr
\quad\quad\quad${\scriptstyle d_{n|m}}$ & & ${\scriptstyle d_{n|m}}$\cr
\quad\quad\quad $\downarrow$ & & $\downarrow$ \cr
\quad\quad\quad$\CH^{sl(n|m),\lambda}(K)$ & $\xrightarrow{\qquad \cong \qquad}$ & $\CH^{sl(n|m),\mu}(K)$
\end{tabular}

\medskip
Here the arrow going from $\CH_1$ to $\CH_2$ labeled by $d$ means that a differential $d$ on $\CH_1$ is such that $H^*(\CH_1,d)\cong \CH_2$. In particular, note that the two differentials, both denoted $d_{n|m}$, are essentially different since they are defined on different homology theories. The differentials $d_{n|m}$ and $d^{col}_{n|m}$ are very similar, in particular, the four gradings of $d_{n|m}$ and $d^{col}_{n|m}$ are identical.

We show that for each rectangular diagram $\mu$ that is obtained from $\lambda$ by removing either some rows or some columns, there exist two different differentials on $\CH^{\lambda}$ realizing the isomorphism (\ref{prob1}). As we explained, all these colored differentials are of the form $d^{col}_{n|m}$. However, in order to clearly indicate the color-changing property of the
differential, we also label them by a superscript ``$\pm$'' as in $d^{\pm}_{\lambda\to\mu}$. One of them will be denoted as $d^{+}_{\lambda\to\mu}$: it has positive $Q$-degree (equal to $+2$), and we will be referred to as the {\em positive differential}. The second differential has negative $Q$-degree (equal to $-2$) and will be denoted by $d^{-}_{\lambda\to\mu}$.

We will show that $d^{+}_{\lambda\to\mu}$ and $d^{-}_{\lambda\to\mu}$ are exchanged by the involution $\Phi_{\lambda}$. In a particular case when $\mu=\emptyset$, the homology $\CH^{\mu}$ is one-dimensional and the corresponding colored differentials are called {\it canceling} differentials.
All these differentials are deep generalizations of the differentials $d_{1}$ and $d_{-1}$ in the uncolored theory \cite{DGR}, which can be considered as colored differentials to the trivial representation $ \emptyset$. Positive colored differentials can be seen as analogs of $d_1$ and negative colored differentials can be seen as analogs of $d_{-1}$.

Now, let us give a more precise definition of colored differentials, together with the explicit change of gradings in the isomorphism (\ref{prob1}). We note that the introduction of the fourth grading is again crucial: the $Q$-grading is indispensable for the explicit re-gradings. 

Let $\Sigma$ denote the $S$-invariant of a knot $K$, i.e. it is even integer such that the homology of the uncolored homology $\CH^{\tableau1}(K)$ with respect to the canceling differential $d_1$, which is one-dimensional, has $(\a,q,t_r,t_c)$-degree $(\Sigma,-\Sigma,0,0)$, see \cite{DGR,slice}.


\textbf{Positive row-removing differentials:} For any $0\le k< R$
there exists a ``row-removing differential'' $d^{+}_{R\times S\to k\times S}$ (which is in fact $d^{col}_{R+k|0}$) such that the homology
of $\CH^{R\times S}(K)$ with respect to it is isomorphic to $\CH^{k\times S}(K)$.
In particular, for $k=0$
the differential $d^{+}_{R\times S\to \emptyset}$ is canceling.
These differentials have the following degrees:
\be
(a,q,t_r,t_c)[d^{+}_{R\times S\to k\times S}]=(-2,2R+2k,-2k-1,-1).
\ee
Since $Q=\frac{q+t_r-t_c}{R}$, we have $Q[d^{+}_{R\times S\to k\times S}]=2.$
The explicit grading change in the corresponding isomorphism (\ref{prob1}) is as follows: let $x$ be a generator of $\CH^{k\times S}(K)$ with degree $(\a,Q,t_r,t_c,q)$. Then the degrees of the corresponding generator $\phi(x)$ of $H^*(\CH^{R\times S}(K),d^{+}_{R\times S\to k\times S})$, denoted  by $(\hat{\a},\hat{Q},\hat{t}_r,\hat{t}_c,\hat{q})$, are given by:
\begin{eqnarray*}
\hat{\a}=\a+S(R-k)\Sigma,\qquad\hat{Q}=Q-S(R-k)\Sigma,\\
\hat{t}_r=t_r+(R-k)Q + Sk(R-k) \Sigma,\\
\hat{t}_c=t_c,\qquad\hat{q}=q-S(R-k)(R+k)\Sigma.
\end{eqnarray*}

\textbf{Positive column-removing differentials: } For any $0\le l< S$
there exists a ``column-removing differential'' $d^{+}_{R\times S\to R\times l}$ (which is in fact $d^{col}_{R|l}$) such that the homology
of $\CH^{R\times S}(K)$ with respect to it is isomorphic to $\CH^{R\times l}(K)$.
In particular, for $l=0$
the differential $d^{+}_{R\times S\to \emptyset}$ is canceling and coincides with the canceling differential above.
These differentials have the following degrees:
$$(a,q,t_r,t_c)[d^{+}_{R\times S\to R\times l}]=(-2,2R-2l,-1,-2l-1).$$
One can check that $Q[d^{+}_{R\times S\to R\times l}]=2.$
 The grading change formulas have the form:
\begin{eqnarray*}
\hat{\a}=\a+R(S-l)\Sigma,\qquad \hat{Q}=Q-R(S-l)\Sigma,\\
\hat{t}_r=t_r,\qquad \hat{t}_c=t_c+(S-l)Q+Rl(S-l)\Sigma,\\
\hat{q}=q+(S-l)Q+R(S-l)(l-R)\Sigma.
\end{eqnarray*}


\textbf{Negative row-removing differentials: }
For any $0\le k< R$
there exists a ``row-removing differential'' $d^{-}_{R\times S\to k\times S}$ (which is in fact $d^{col}_{k|S}$) such that the homology
of $\CH^{R\times S}(K)$ with respect to it is isomorphic to $\CH^{k\times S}(K)$.
In particular, for $k=0$
the differential $d^{-}_{R\times S\to \emptyset}$ is canceling.
These differentials have the following degrees:
$$(a,q,t_r,t_c)[d^{-}_{R\times S\to k\times S}]=(-2,2k-2S,-2k-2R-1,-2S-1).$$
One can check that $Q[d^{-}_{R\times S\to k\times S}]=-2.$
The grading change formulas have the form:
\begin{eqnarray*}
\hat{\a}=\a+S(R-k)\Sigma,\quad \hat{Q}=Q+S(R-k)\Sigma,\\
\hat{t}_r=t_r+S(R-k)(R+k)\Sigma,\quad \hat{t}_c=t_c+S^2(R-k)\Sigma,\\
\hat{q}=q+kQ+S(R-k)(S-k)\Sigma.
\end{eqnarray*}

\textbf{Negative column-removing differentials: } For any $0\le l< S$
there exists a ``column-removing differential'' $d^{-}_{R\times S\to R\times l}$ (which is in fact $d^{col}_{0|S+l}$) such that the homology
of $\CH^{R\times S}(K)$ with respect to it is isomorphic to $\CH^{R\times l}(K)$.
In particular, for $l=0$
the differential $d^{-}_{R\times S\to \emptyset}$ is canceling and coincides with the canceling negative differential above.
These differentials have the following degrees:
$$(a,q,t_r,t_c)[d^{+}_{R\times S\to R\times l}]=(-2,-2l-2S,-2R-1,-2l-2S-1).$$
One can check that $Q[d^{+}_{R\times S\to R\times l}]=-2.$
The grading change formulas have the form:
\begin{eqnarray*}
\hat{\a}=\a+R(S-l)\Sigma,\quad \hat{Q}=Q+R(S-l)\Sigma,\\
\hat{t}_r=t_r+R^2(S-l)\Sigma,\quad \hat{t}_c=t_c+R(S-l)(S+l)\Sigma,\\
\hat{q}=q+R(S-l)(S+l)\Sigma.
\end{eqnarray*}


\begin{figure}
\begin{tikzpicture}

\draw (0,0) node {$\tableau{5 5 5 5}$};

\draw[->] (-0.5,0.5)--(-2.6,5.5);
\draw[->] (-0.55,0.4)--(-3.5,4.1);
\draw[->] (-0.6,0.3)--(-4,2.7);
\draw[->] (-0.65,0.2)--(-4.5,1.3);

\draw[->,very thick] (-0.75,0)--(-4.5,0);

\draw[->] (-0.7,-0.15)--(-4,-1.3);
\draw[->] (-0.63,-0.3)--(-3.5,-2.3);
\draw[->] (-0.55,-0.4)--(-2.75,-3.6);

\draw[->,very thick] (-0.1,-0.5)--(-0.7,-4.3);

\draw[->] (0.25,-0.5)--(1.6,-4);
\draw[->] (0.4,-0.4)--(2.6,-3);
\draw[->] (0.55,-0.3)--(3.5,-2.2);
\draw[->] (0.7,-0.2)--(4.2,-1.3);

\draw[->,very thick] (0.75,0)--(4.5,0);

\draw[->] (0.7,0.2)--(4,1.5);
\draw[->] (0.55,0.35)--(3.5,3.1);
\draw[->] (0.45,0.5)--(2.5,4.7);

\draw (-3,6) node {$\tableau{4 4 4 4}$};
\draw (-3.8, 4.5) node {$\tableau{3 3 3 3}$};
\draw (-4.3, 3) node {$\tableau{2 2 2 2}$};
\draw (-4.8,1.5) node {$\tableau{1 1 1 1}$};

\draw (-5,0) node {$\bullet$};

\draw (-4.8,-1.4) node{$\tableau{5}$};
\draw (-4.1,-2.5) node{$\tableau{5 5}$};
\draw (-3.2,-3.9) node{$\tableau{5 5 5}$};

\draw (-0.7,-4.8) node {$\tableau{5 5 5 5}$};

\draw (1.8,-4.5) node{$\tableau{4 4 4 4}$};
\draw (3,-3.5) node{$\tableau{3 3 3 3}$};
\draw (4,-2.5) node{$\tableau{2 2 2 2}$};
\draw (4.8,-1.5) node{$\tableau{1 1 1 1}$};

\draw (5,0) node {$\bullet$};

\draw (4.5,1.7) node {$\tableau{5}$};
\draw (4,3.4) node {$\tableau{5 5}$};
\draw (3,5.1) node {$\tableau{5 5 5}$};


\draw (-1.8,4.4) node {$d_{0|9}$};
\draw (-2.55,3.4) node {$d_{0|8}$};
\draw (-3.1,2.45) node {$d_{0|7}$};
\draw (-3.65,1.3) node {$d_{0|6}$};
\draw (-3.8,0.2) node {$d_{0|5}$};
\draw (-3.5,-0.2) node {{\tiny{CANCELING}}};
\draw (-3.7,-0.9) node {$d_{1|5}$};
\draw (-3.3,-1.8) node {$d_{2|5}$};
\draw (-2.7,-2.8) node {$d_{3|5}$};
\draw (-1.3,-3.5) node {$d^{col}_{4|5}=0$};
\draw (0.9,-3) node {$d_{4|4}$};
\draw (1.85,-2.5) node {$d_{4|3}$};
\draw (2.65,-1.9) node {$d_{4|2}$};
\draw (3.4,-1.23) node {$d_{4|1}$};
\draw (3.5,0.2) node {$d_{4|0}$};
\draw (3.2,-0.2) node {{\tiny{CANCELING}}};
\draw (3.15,1.4) node {$d_{5|0}$};
\draw (2.75,2.8) node {$d_{6|0}$};
\draw (1.7,3.8) node {$d_{7|0}$};

\end{tikzpicture}
\caption{Colored differentials for the $4\times 5$ rectangle.}
\label{sunflower}
\end{figure}



\vskip 0.25 cm

To explain better such a large structure of differentials, we present them in Figure \ref{sunflower}. This diagram represents the case of the representation labeled by the Young diagram
with $R=4$ rows and $S=5$ columns.
An arrow labelled by $d_{n|m}$ going from Young diagram $D_1$ to $D_2$ means that there exists a differential $d^{col}_{n|m}$ on $\CH^{D_1}(K)$ and  $\CH^{D_2}(K)$, such that

\be\label{glav}
H^*(\CH^{D_1}(K),d^{col}_{n|m}) \cong \CH^{D_2}(K).
\ee
There are three ''special" differentials which are represented by thick lines: two of them ($d^{col}_{4|0}$ and $d^{col}_{0|5}$) are canceling, i.e. the homology with respect to them is one-dimensional, and the third one  (the middle one) is  trivial  $d^{col}_{4|5}=0$.

In a general case of an arbitrary $R \times S$ rectangular Young diagram $\lambda$, the picture would be of the same form with $2R+2S-1$ differentials: written in a clockwise direction, they will  be $d_{R+i|0}$, with $i$ ranging $i=R-1,\ldots,0$, $d_{R|i}$, with $i$ ranging $i=0,\ldots,S$, $d_{i|S}$, with $i$ ranging $i=R-1,\ldots,0$, and $d_{0|S+i}$, with $i$ ranging $i=0,\ldots,S-1$, The canceling differentials will be the differentials $d_{R|0}$ and $d_{0|S}$, while the middle one would be $d_{R|S}$.\footnote{Although this middle colored differential $d^{col}_{R|S}$ is trivial, the $sl(R|S)$ colored differential $d_{R|S}$ is in general non-trivial and is related to knot Floer homology, in the same way as the differential $d_0$ in the uncolored case \cite{DGR}. We discuss these HFK-like differentials in Section \ref{sec:symant}.}

In the upper half of the diagram are the positive row- and negative column-removing differentials, with the row-removing ($d_{R+i|0}$ with $0\le i< R$) being in the upper right part and column-removing ($d_{0|S+i}$ with $0\le i< S$) being in the upper left part of the diagram.
The negative row- and positive column-removing differentials are in the lower half of the picture (below the canceling differentials).
The row-removing ones ($d_{i|S}$ with $0\le i<R$) are in the lower left part and column-removing ($d_{R|i}$ with $0\le i<S$) are in the lower right part of the diagram. The positive colored differentials are in the right half of the diagram, while the negative colored differentials are in the left half.\\

We conjecture that the collection of differentials is self-contained under the mirror symmetry and self-symmetry isomorphism. Namely,
Let $\lambda$ be a rectangular Young diagram and let $\mu$ be obtained from $\lambda$ by removal of some of the rows or columns. Then the following identities hold:
\begin{eqnarray}
\Phi_{\lambda}(d^{+}_{\lambda\to\mu}(x))&=&d^{-}_{\lambda\to\mu}(\Phi_{\lambda}(x)),\\
M_{\lambda}(d^{\pm}_{\lambda\to\mu}(x))&=&d^{\pm}_{\lambda^t\to\mu^t}(M_{\lambda}(x))).
\end{eqnarray}
The involution $\Phi$ provides an isomorphism
\be
H^{*}(\CH^{\lambda}(K),d^{+}_{\lambda\to\mu}(x)) \quad \stackrel{\Phi}{\longrightarrow} \quad H^{*}(\CH^{\lambda}(K),d^{-}_{\lambda\to\mu}(x)).
\ee


\subsection{Representation theory interpretation of the colored differentials}\label{repsup}

The main explanation for the existence of all these positive and negative colored differentials with the wanted behavior comes from the representation theory of $sl(n)$ and  $sl(n|m)$. We include the classical Lie algebra $sl(n)$ in the family of Lie superalgebras $sl(m|n)$, by identifying it with $sl(n|0)$.

Indeed, it is well-known that the irreducible polynomial representations of $sl(n)$ are labeled with the Young diagrams with at most $n$ rows. Moreover, some of these representations are isomorphic: namely, for every $k$ with $0\le k <R$, the representations labeled by the rectangular Young diagrams $R \times S$ and $k\times S$ are isomorphic as $sl(R+k)$-representations. This in turn implies that the doubly-graded homologies $\CH^{sl(R+k),R\times S}$ and $\CH^{sl(R+k),k\times S}$ categorifying respectively the quantum polynomial invariants $P^{sl(R+k),R\times S}(q)$ and $P^{sl(R+k),k\times S}(q)$, should be isomorphic. Finally, since $\CH^{sl(R+k),R\times S}$ is isomorphic to the homology of $\CH^{R\times S}$ with respect to the differential $d_{R+k|0}$, we obtain the explanation of the wanted behavior of the positive row-removing differentials.

As for the positive column-removing differentials one should look for the representations of the Lie superalgrebras $sl(n|m)$. There is an analogous theory
for the polynomial representations of $sl(n|m)$ \cite{br1,br2}, extending the classical case of $sl(n)$ algebras. This time, the irreducible representations are labeled by Young diagrams such that the $(n+1)$-st row contains at most $m$ boxes. Again, some of these representations are isomorphic: for every $k$ with $0\le k <S$ we have that the representations labeled by the rectangular Young diagrams $R\times S$ and $R\times k$ are isomorphic as $sl(R|k)$-representations.
Now one gets the homology theory corresponding to the $(sl(R|k), R\times S)$-representations as the homology of $\CH^{R\times S}$ with respect to $d_{R|k}$.
Hence, the above isomorphisms of the $sl(R|k)$-representations give rise to the positive column-removing differentials.

As for the negative differentials, they can be obtained in the same way as the positive differentials by using ``dual'' isomorphisms from above, combined with the mirror symmetry. Indeed, for two Young diagrams $\lambda$ and $\mu$ we have the following isomorphism of representations:
\be
\lambda \cong \mu, \quad\quad {\textrm{ as} }\quad  sl(n|m)\quad  {\textrm{ representations}},
\ee
if and only if
\be
\lambda^t \cong \mu^t, \quad\quad {\textrm{ as }}\quad sl(m|n) \quad {\textrm {representations}}.
\ee
In such way the existence of the negative row-removing differentials $d^{col}_{k|S}$ with $0\le k <R$ is a consequence of the isomorphism of $sl(k|S)$-representations corresponding to Young diagrams $R\times S$ and $k\times S$.
Finally, the existence of negative column-removing differentials $d^{col}_{0|S+k}$ with $0\le k <S$ follows from the isomorphism of $sl(0|S+k)$-representations corresponding to Young diagrams $R\times S$ and $R\times k$.


\subsection{Universal colored differentials}
\label{unicolor}

There exists yet another set of colored differentials on $\CH^{\lambda}(K)$ such that the homology with respect to any of them is isomorphic to $\CH^{\lambda'}(K)$ for some $\lambda'$ obtained from $\lambda$ by removing some of its rows or columns. The difference with respect to the differentials $d^{col}_{n|m}$ from above is that they are {\it universal} in the sense that their $\a$-degree is equal to 0.

Although the insights from the theory of deformations of potentials imply that such universal colored differentials should  exists for any row- or column-removal, we have managed to find explicitly such differentials only in the cases when $\lambda$ has two rows or two columns.

\begin{conjecture}\label{unicol}
Let $K$ be a knot.
Let $\lambda$ be $2 \times S$ rectangular diagram and let $\lambda'$ be $1\times S$ rectangular diagram. Then there exists a differential $d^{\uparrow}$ on  $\CH^{\lambda}(K)$ of $\a$-degree $0$, such that the homology of $\CH^{\lambda}(K)$ with respect to $d^{\uparrow}$ is isomorphic to $\CH^{\lambda'}(K)$.

Let $\mu$ be $R \times 2$ rectangular diagram and let $\mu'$ be $R\times 1$ rectangular diagram. Then their exists a differential $d^{\leftarrow}$ on $\CH^{\mu}(K)$ of $\a$-degree $0$ such that the homology of $\CH^{\mu}(K)$ with respect to $d^{\leftarrow}$ is isomorphic to $\CH^{\mu'}(K)$.
\end{conjecture}



To be more precise, we give  explicit values for the degrees of differentials $d^{\uparrow}$ and $d^{\leftarrow}$ and the degree changes in the isomorphisms of the Conjecture \ref{unicol}. We describe everything in the $(\a,Q,t_r,t_c,q)$-gradings.
The degrees of the differentials are given by:
\begin{eqnarray}
\deg d^{\uparrow}&=&(0,0,-2,0,2),\\
\deg d^{\leftarrow}&=&(0,0,0,2,2).
\end{eqnarray}
The first isomorphism from Conjecture \ref{unicol} gives:
\be\label{isom5}
H^*(\CH^{\lambda}(K),d^{\uparrow}) \cong \CH^{\lambda'}(K).
\ee
Let $x$ be a generator of $\CH^{\lambda'}(K)$ with degree $(\a,Q,t_r,t_c,q)$. Then the degrees of the corresponding generator $\phi(x)$ of $H^*(\CH^{\lambda}(K),d_N)$, denoted  by $(\hat{\a},\hat{Q},\hat{t}_r,\hat{t}_c,\hat{q})$, are given by:
\begin{eqnarray*}
\hat{\a}=2\a,\quad \hat{Q}=2Q,\quad \hat{t}_r=4t_r,\\
\hat{t}_c=2t_c,\quad \hat{q}=4q-2t_c.
\end{eqnarray*}
The second isomorphism from Conjecture \ref{unicol} gives:
\be\label{isom6}
H^*(\CH^{\mu}(K),d^{\leftarrow}) \cong \CH^{\mu'}(K).
\ee
Let $x$ be a generator of $\CH^{\mu'}(K)$ with degree $(\a,Q,t_r,t_c,q)$. Then the degrees of the corresponding generator $\phi(x)$ of $H^*(\CH^{\mu}(K),d_N)$, denoted  by $(\hat{\a},\hat{Q},\hat{t}_r,\hat{t}_c,\hat{q})$, are given by:
\begin{eqnarray*}
\hat{\a}=2\a,\quad \hat{Q}=2Q,\quad \hat{t}_r=2t_r,\\
\hat{t}_c=4t_c,\quad \hat{q}=2q+2t_c.
\end{eqnarray*}




\subsection{Refined exponential growth}

Now we are ready to formulate a quantitative refinement of the ``exponential growth conjecture'' from \cite{GS}.

\begin{conjecture}
Let $K$ be either two-bridge knot or a torus knot.
Let $\tilde{\CP}^{\lambda}(K)(a,Q,t_{r})$ denote the Poincar\'e polynomial (in $(a,Q,t_{r})$ gradings, i.e. after setting $t_c=1$) of $\tilde{\CH}^{\lambda}(K)$. Let $\tilde{\CP}^{\Lambda^{R}}(K)(a,Q,t_{r})$ denote the Poincar\'e polynomial of $\tilde{\CH}^{\Lambda^R}(K)$ ($R$-th antisymmetric colored homology).
Then the following relation holds:
\begin{equation}
\label{reduced refined exp growth}
\tilde \CP^{\lambda}(K)(a,Q,t_{r})=\left(\tilde \CP^{\Lambda^{R}}(K)(a,Q,t_{r})\right)^{S}.
\end{equation}
\end{conjecture}
By using the mirror symmetry and by switching $t_r \longleftrightarrow t_c$, we get the dual statement:

\begin{conjecture}
Let $K$ be either two-bridge knot or a torus knot.
Let $\tilde{\CP}^{\lambda}(K)(a,Q,t_{c})$ denote the Poincar\'e polynomial in $(a,Q,t_{c})$ gradings of $\tilde{\CH}^{\lambda}(K)$. Let $\tilde{\CP}^{S^{S}}(K)(a,Q,t_{c})$ denote the Poincar\'e polynomial of $\tilde{\CH}^{S^S}(K)$ ($S$-th symmetric colored homology).
Then the following relation holds:
\begin{equation}
\label{reduced refined exp growth dual}
\tilde{\CP}^{\lambda}(K)(a,Q,t_{c})=\left(\tilde{\CP}^{S^{S}}(K)(a,Q,t_{c})\right)^{R}.
\end{equation}
\end{conjecture}
\begin{corollary}
The dimensions of the ``rectangular homology groups'' satisfy the equation
\begin{equation}
\label{exp growth}
\dim \CH^{\lambda}(K)=\left(\dim \CH^{\tableau{1}}(K\right))^{|\lambda|}.
\end{equation}
Moreover, the similar statement holds in $(a,Q)$-gradings, i.e. with both $t_r$ and $t_c$ specialized to 1:
\begin{equation}
\label{a q exp growth}
\tilde{\CP}^{\lambda}(K)(a,Q)=\left(\tilde{\CP}^{\tableau{1}}(K)(a,Q)\right)^{|\lambda|}.
\end{equation}
\end{corollary}

\begin{corollary}
The Poincar\'e polynomial of the symmetric homology in $(a,Q,t_{r})$ gradings can be deduced from the uncolored
Poincar\'e polynomial (recall that $t_{r}=t_{c}=t$ for the uncolored homology):
\begin{equation}
\label{reduced refined exp growth for S}
\tilde{\CP}^{S^{r}}(K)(a,Q=q,t_{r}=t,t_c=1)=\left(\CP^{\tableau1}(K)(a,q,t)\right)^{r}.
\end{equation}
The Poincar\'e polynomial of the antisymmetric homology in $(a,Q,t_{c})$ gradings can be deduced from the uncolored
Poincar\'e polynomial:
\begin{equation}
\label{reduced refined exp growth for Lambda}
\tilde{\CP}^{\Lambda^{r}}(K)(a,Q=q,t_{r}=1,t_c=t)=\left(\CP^{\tableau1}(K)(a,q,t)\right)^{r}.
\end{equation}
\end{corollary}

Going back to original $q$-degrees, i.e. the ordinary version of the colored homology $\CH^{\lambda}(K)$, the above relations reduce to two-variable (in variables $a$ and $t$) exponential growths:
\be
{\CP}^{S^{r}}(K)(a,q=1,t_{r}=t,t_c=1)=\left(\CP^{\tableau1}(K)(a,q=1,t)\right)^{r},
\ee
and
\be
{\CP}^{\Lambda^{r}}(K)(a,q=1,t_{r}=1,t_c=t)=\left(\CP^{\tableau1}(K)(a,q=1,t)\right)^{r}.
\ee
Although such nice (and surprising) exponential growth properties should exist for large classes of knots, it is not expected that it should hold in general, i.e. for every knot. For example, the uncolored homology of the knot $9_{42}$ is 9-dimensional (see \cite{DGR}), its (triply-graded) $S^2$-colored homology is computed and the result has 401 generators. Therefore, we don't have any exponential growth property for it.\footnote{This could also be seen on the level of the $S^2$-colored HOMFLY polynomial of $9_{42}$. It has nonzero terms with $a$-degree $-6$, while the uncolored homology is concentrated in $a$-degrees -2,0 and 2. We thank Paul Wedrich for providing us with his computations of the colored HOMFLY polynomials.}
Nevertheless, such exponential growth property should hold in general but only asymptotically, as we briefly explain in the following subsection.


\subsection{Relation to the super-$A$-polynomial}

The exponential growth of the colored HOMFLY homology summarized
in \eqref{reduced refined exp growth}--\eqref{reduced refined exp growth for S}
nicely complements the results of \cite{FGS1,FGS2,Nawata},
where the large-$r$ limit of the $S^r$ homology was studied in detail.
In particular, it was conjectured in \cite{FGS2} that for an arbitrary knot $K$
the $S^r$-colored superpolynomials obey a recursion relation that comes from quantization of
an algebraic curve $A^{\text{super}} (x,y;a,t)=0$.
Specifically, this recursion relation has the following general form:
\be
\CP^{S^{r+n}} (K;a,q,t) + a_{n-1} \, \CP^{S^{r+n-1}} (K;a,q,t)
 + \ldots 
 + a_0 \, \CP^{S^{r}} (K;a,q,t) \; = \; 0
\label{QVCsuper}
\ee
and can be conveniently expressed in the operator form $\hat A^{\text{super}} \; \CP^{S^*} = 0$,
where the coefficients $a_i \equiv a_i (x, a, q, t)$ are rational functions of $a$, $q$, $t$, and $x \equiv q^{r}$.
To make contact with \eqref{a q exp growth}, we need to set $q=1$ which, by definition,
reduces the operator $\hat A^{\text{super}}$ 
to its characteristic polynomial, the super-$A$-polynomial $A^{\text{super}} (x, y; a,t)$.

Furthermore, since setting $q=1$ also implies $x=q^r=1$, we conclude that making contact with \eqref{a q exp growth}
involves comparison with the super-$A$-polynomial evaluated as $x=1$. Something very nice happens in this limit;
namely, in every example studied so far, all coefficients $a_i (x;a,t)$ of the super-$A$-polynomial
vanish, except for $a_{n-1}$. As a result, \eqref{QVCsuper} reduces to a much simpler recursion relation:
\be
\CP^{S^{r+n}} (K;a,q=1,t) \; + \; a_{n-1} (x=1, a, t) \, \CP^{S^{r+n-1}} (K;a,q=1,t) \; = \; 0 \,,

\ee
which indeed takes the form \eqref{a q exp growth}.
Specifically, it can be consistent with \eqref{a q exp growth}
if and only if $a_{n-1} (x=1, a, t) = \CP (K;a,q=1,t)$.
We conjecture that this is always the case, therefore, providing a bridge between our present work and \cite{FGS1,FGS2,Nawata}:

\begin{conjecture}
For any knot $K$, the following relation between the super-$A$-polynomial $A^{\text{super}} (x,y;a,t)$
and the (uncolored) superpolynomial holds:
\be
A^{\text{super}} (x=1,y;a,t) \; = \; y^k + y^{k-1} \, \CP (K;a,q=1,t) \,.
\ee
\end{conjecture}


\subsection{Symmetric and antisymmetric representations}\label{sec:symant}

In \cite{GS} the triply-graded colored HOMFLY homology for the symmetric and antisymmetric representations have been computed for plenty of knots. We obtain a quadruply-graded theory by adding a $t$-degree of the corresponding generator of the colored homology for the dual representation. The $t$-grading we used in \cite{GS} (and called ``old'') corresponds to $t_r$-grading in this paper. The other $t_c$-grading coincides with the $t$-grading used in \cite{AShakirov,DMMSS,DGR,GWalcher}. In the case of  the symmetric representations, we have two additional properties of the quadruply-graded colored homology: $\delta$-grading and HFK-like differential.
To every generator $x$ of $S^r$-colored quadruply-graded theory we can associate a $\delta$-grading by:
\be
\delta(x)=a(x)+\frac{q(x)}{2}-\frac{t_r(x)+t_c(x)}{2}=a(x)+\frac{Q(x)}{2}-t_r(x).
\ee

We call a knot $K$  $S^r$-thin if all generators of $\CH^{S^r}(K)$ have the same $\delta$-grading. In the uncolored case, $r=1$, this coincides with the definition of a thin knot. Also, in the uncolored case, the $\delta$-grading of all generators of a thin knot $K$ is equal to $\Sigma/2$, where $\Sigma$ is defined as in Section \ref{coldif}. We conjecture that every thin knot $K$ is also $S^r$-thin with the $\delta$-grading of all generators of $\CH^{S^r}(K)$ being equal to $r\Sigma/2$. We also conjecture that the refined exponential growth conjecture (\ref{reduced refined exp growth for S}) holds for all thin knots.


The action of the ``special'' differential $d_{1|r}$ on $S^r$-colored homology  is related to the action of the differential $d_{1|1}$ on the uncolored homology. The latter one is denoted $d_0$ in \cite{DGR} and it is conjectured that the homology $H^*(\CH^{\tableau 1}(K),d_0)$ is isomorphic to the knot Floer homology of $K$.
We conjecture the following isomorphism:
\be\label{HFKgrowth}
(\tilde{\CH}^{S^r}(K),d_{1|r})(a,Q=q,t_r=t,t_c=1)=\left(\CH^{\tableau 1}(K),d_{1|1})(a,q,t)\right)^r.
\ee
We note two things: first, the above property does not descend to any relation on the colored HOMFLY polynomial level, due to the non-trivial presence of the $Q$-grading. Secondly, both $d_{1|1}$ on $\CH^{\tableau 1}(K)$ and $d_{1|r}$ on $\CH^{S^r}(K)$
have non-zero $\delta$-grading and therefore act trivially on thin knots.  Hence, the relation (\ref{HFKgrowth}) in the case of thin knots becomes simply (\ref{reduced refined exp growth for S}).
However, once we pass to thick knots, in general the two relations are different, as we shall show in the example below for the (3,4)-torus knot.


\subsection{Rectangular vs. non-rectangular representations}\label{hooks}

What makes rectangular representations special?
Well, these are precisely representations, whose corresponding knot invariants obey Hirota equation.
Specifically, if $\lambda$ is a Young diagram of size $R \times S$, then the corresponding invariants $P^{\lambda} \equiv P_{R,S}$
obey recursion equations of the form
\be
P_{R,S}^2 \; = \; P_{R+1,S} \, P_{R-1,S} + P_{R,S+1} \, P_{R,S-1}
\label{Hirotaeq}
\ee
or
\be
P_{R,S} (u+1) \, P_{R,S} (u-1) \; = \; P_{R+1,S} (u) \, P_{R-1,S} (u) + P_{R,S+1} (u) \, P_{R,S-1} (u)
\label{Hirotaequ}
\ee
where $u$ is the spectral parameter. Both of these equations are variants of the familiar Hirota equation.
For instance, it is easy to verify that
\be
P_{R,S} (\unknot) \; = \; \prod_{i=1}^R \prod_{j=1}^S \frac{a q^{j-i} - a^{-1} q^{-j+i}}{q^{R+S-i-j+1} - q^{-(R+S-i-j+1)}}
\ee
satisfies \eqref{Hirotaeq}.

Another special property of the rectangular Young diagram, is that these are precisely the Young diagrams $\lambda$ such that for every Young diagram $\mu$, the Littlewood-Richardson coefficient $c_{\lambda,\lambda}^{\mu}$ is either 0 or 1. These in turn are precisely those $\lambda$ for which the two-variable HOMFLY polynomial $P^{\lambda}(K)(a,q)$ does not detect mutants (see \cite{MC}).

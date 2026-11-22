---
doc_id: arxiv-1304.3481v1
doc_title: "Quadruply-Graded Colored Homology of Knots"
section_id: sec-006-7-bottom-row-of-the-colored-homfly-homology
section_title: "``Bottom row'' of the colored HOMFLY homology"
section_number: 7
pages: 61-68
source_pdf: 1304.3481v1.pdf
source_sha256: d0840f2775c0f761
toc_source: outline
text_source: latex
latex_prose_ratio: 0.941
latex_coverage_ratio: 0.985
doc_brief: "Quadruply-Graded Colored Homology of Knots — We conjecture the existence of four independent gradings in the colored HOMFLY homology."
---
\label{sec:bottom}

In this part we wish to study the ``bottom row'' of the colored superpolynomial, defined as
\be
\CP^{\lambda}_{\text{bottom}} (q,t) \; : = \; \lim_{\a \to 0} \, \a^{\#} \, \CP^{\lambda} (\a,q,t) \,,
\label{bottomrow}
\ee
where $\a^{\#}$ denotes the appropriate power of $a$, such that the product $\a^{\#} \, \CP^{\lambda} (\a,q,t)$
contains only non-negative $a$-degrees starting from zero.


\subsection{Combinatorial interpretation for torus knots}
\label{sec:combbot}

First, let us recall the conjectural combinatorial description of the uncolored triply graded homology
for a $(p,q)$ torus knot \cite{G,GM,ORS}. Consider a $p\times q$ rectangle and a $NW-SE$ diagonal in it.

\begin{proposition}(\cite{G})
\label{prop:bottom1}
The dimension of the ``bottom row'' of the reduced uncolored homology equals to the number of lattice paths
in this rectangle strictly below the diagonal:
$$\dim \CH_{\text{bottom}} (T(p,q)) \; = \; c_{p,q}=\frac{(p+q-1)!}{p!q!}.$$
\end{proposition}

For example, if $q=p+1$, this dimension equals to the $p$-th Catalan number.

\begin{proposition}(\cite{G})
The dimension of the ``$k$-th row'' of the reduced uncolored homology equals to the number of lattice paths
below the diagonal with $k$ marked corners:
$$\dim \CH_{a=k} (T(p,q)) \; = \; \frac{(p+q-k-1)!}{ p\cdot q\cdot k!\cdot (p-k-1)!(q-k-1)!}.$$
\end{proposition}

A $q$-analogue of this formula was discussed in \cite[eq. (3.46)]{BEM}.
Both of these propositions motivate the following combinatorial construction,
completed in \cite{ORS} where it was matched to the algebro-geometric constructions of \cite{os}.

The basis in $\CH_{p,q}$ is enumerated by the lattice paths in the $p\times q$ rectangle with marked corners. To every such path we assign three gradings, where $a$-grading corresponds to the number of marked corners. Let us describe $q-$ and $t-$ gradings.
For simplicity, we will focus on the bottom row, considered in details in \cite{GM}. Corrections for the higher rows can be found in \cite{ORS}.

Let us interpret a lattice path as a Young diagram $D$. Consider the $\C^{*}\times \C^{*}$ action on the Hilbert scheme of
$N$ points on $\C^2$, and let us restrict it to a one-parameter subgroup $(t^p,t^q)$. One can check (see {\it e.g.} \cite{Nakajima})
that the action of this subgroup has isolated fixed points parametrized by the Young diagrams with $N$ boxes. Therefore the corresponding moment map is a Morse function on $\Hilb^{N}(\C^2)$, and its gradient flow induces the Bialynicki-Birula cell decomposition of the Hilbert scheme \cite{Nakajima,Elstro}. We are interested in the dimension of the cell $C_{D}$ labelled by the fixed point $D$, which is given by the following formula:
$$\dim C_{D}=|D|+h^{+}_{p/q}(D),$$
where
\begin{equation}
\label{hplus}
h^{+}_{p/q}(D)=\sharp\left\{c\in D~~ \vline~~ \frac{a(c)}{l(c)+1}\le \frac{p}{q}< \frac{a(c)+1}{l(c)}\right\}.
\end{equation}
Here $a(c)$ and $l(c)$ denote the arm and the leg of a cell $c$ in a diagram $D$:

\begin{tikzpicture}
\draw  (0,0)--(0,4)--(5,0)--(0,0);
\draw  (1.5,0.5)--(1.5,0.7)--(1.7,0.7)--(1.7,0.5)--(1.5,0.5);
\draw [thick] (0,3)--(0.5,3) -- (0.5,2) -- (2.3,2)--(2.3,1.3)--(3,1.3)--(3,0.5)--(4,0.5)--(4,0)--(0,0)--(0,3);
\draw [<->,>=stealth] (1.7,0.6) -- (3,0.6);
\draw [<->,>=stealth] (1.6,0.7) -- (1.6,2);
\draw (2.3,0.4) node {${a(c)}$};
\draw (1.3,1.3) node {${l(c)}$};
\draw (2.5,-0.2) node {$p$};
\draw (-0.2,2) node {$q$};
\draw [->,>=stealth] (2.6,-0.15) -- (5,-0.15);
\draw [->,>=stealth] (2.4,-0.15) -- (0,-0.15);
\draw [->,>=stealth] (-0.15,1.8) -- (-0.15,0);
\draw [->,>=stealth] (-0.15,2.2) -- (-0.15,4);
\end{tikzpicture}

The statistics $h^{+}_{p/q}(D)$ was introduced in \cite{LW} in connection with some combinatorial models of the bigraded Catalan numbers.

\begin{proposition}
\label{prop:bottom3}
The gradings of Dyck paths are given by the following equations:
\begin{enumerate}

\item{The $q$-grading assigned to $D$ equals to $2\left[|D|+2h^{+}_{p/q}(D)\right]$.}

\item{The $t$-grading assigned to $D$ equals to $2|D|$.}
\end{enumerate}
\end{proposition}


Motivated the refined exponential growth conjecture, we assume that the dimension of the $S^r$-colored homology is equal to the $r$-th power of the uncolored homology, {\it i.e.} the $r$-th power of the generalized Catalan number $c_{p,q}$.
Therefore it is natural to assume that one can find a basis in the $S^r$-colored homology labelled by all possible $r$-tuples of Young diagrams in $p\times q$ rectangle below the diagonal.

\begin{conjecture}
\label{prop:bottom4}
The bottom row of the $S^r$ colored homology of the $(p,q)$ torus knot has a basis labeled by the $r$-tuples $(D_1,\ldots,D_r)$ of the Dyck paths in $p\times q$ rectangle. The $(Q,t_r)$ gradings of Dyck paths are given by the following equations:
\begin{enumerate}

\item{The $Q$-grading assigned to $D$ equals to $2\sum_{i=1}^{r}\left[|D_i|+2h^{+}_{p/q}(D_i)\right]$.}

\item{The $t_r$-grading assigned to $D$ equals to $2\sum_{i=1}^{r}|D_i|$.}
\end{enumerate}
\end{conjecture}

The $q$-grading (and, therefore, the $t_c$-grading) has yet to be constructed. We expect it to be related to the combinatorial constructions of \cite{BDZ} and \cite{HMZ}.




\subsection{Coupled instanton-vortex counting}
\label{sec:inst-surf}

The ``bottom row'' \eqref{bottomrow} has a simple and beautiful interpretation in terms of instanton / vortex counting.
As a warm-up, let us start with a simple vortex counting problem that is easy to do ``by hand''
and that has all the essential features. Then, we shall upgrade it to the equivariant instanton counting relevant to arbitrary knots and links.

Let $\CV_m$ be the moduli space of $m$ abelian vortices on a two-dimensional plane, $D = \R^2$.
In other words, $\CV_m$ is the moduli space of solutions to the PDEs
\be
\begin{array}{rl}
* F_A & =~ i |\phi|^2 - it \\
\bar \partial_A \phi & =~ 0
\end{array}
\label{abelianvorteq}
\ee
where $A$ is a connection on a $U(1)$ bundle of first Chern class $m$, and $t$ is a parameter.
These equations describe supersymmetric configurations (BPS states) in a two-dimensional theory
on $D$ with $\CN=(2,2)$ supersymmetry:
\be
\CT_{\text{vortex}}~:~ U(1)~\text{gauge theory with a single charged field}~\phi
\ee

It is well known that $\CV_m$ is a K\"ahler manifold of (real) dimension $2m$. Namely,
\be
\CV_m \; = \; \Sym^m (\C) \; \equiv \; \C^m / S_m \,,
\label{vortsymm}
\ee
where one can think of coordinates on $\CV_m$ as vortex positions on $D = \R^2 \cong \C$.

Since $D$ admits a circle action, one can consider the equivariant character, $Ch_q (\CV_m)$,
with respect to the rotation group $U(1)_q$ acting on $D$.
Indeed, $U(1)_q$ acts on $\CV_m$ in a natural way, by equal phase rotations on all factors in the symmetric product \eqref{vortsymm}.
Moreover, identifying the vortex moduli space $\CV_m = \Sym^m (\C)$
with the space of monic polynomials of degree $m$,
\be
f (x) \; = \; \prod_{j=1}^m (x - x_j) = x^m + a_1 x^{m-1} + \ldots + a_m \,,
\ee
we immediately deduce the isomorphism $\CV_m \cong \C^m = (\{ a_1, \ldots, a_m \})$
and also learn that $U(1)_q$ acts on the space $\CV_m$ with weights $(1, 2, \ldots, m)$.
Therefore, the $U(1)_q$-equivariant character of $\CV_m$ is
\be
Ch_q (\CV_m) \; = \; \frac{1}{(1-q)(1-q^2) \ldots (1-q^m)} \,,
\label{unknotvortchar}
\ee
in which a careful reader will recognize the ``bottom row'' of the \textsl{unnormalized} $S^m$-colored HOMFLY polynomial of the unknot.

This is not an accident, of course, and the physics setup \eqref{theoryB} predicts that the ``bottom row''
of any $\lambda$-colored HOMFLY homology of any knot $K$ has a similar interpretation in terms
of equivariant vortex counting on $D = \R^2$.
In order to explain this relation, we need to generalize our warm-up example in two important ways:
first, we need to introduce the homological $t$-grading, and secondly we need a generalization to arbitrary knots.
Both of these problems can be achieved by embedding $D = \R^2$ into a larger space $M_4 = \R^4$,
and realizing our vortex counting problem on $D$ as a special case of counting solutions
to coupled \textsl{instanton-vortex equations} or, equivalently, via equivariant instanton
counting on the 4-manifold $M_4$ in the presence of ramification along $D \subset M_4$.

However, before we proceed to generalizations, let us stay a bit longer in the world of vortex equations
and explore the picture which seems to emerge:
\be
\text{knot}~K \quad \leadsto \quad \text{2d vortex theory}~\CT_{\text{vortex}} (K) \quad \leadsto \quad \CV_m (K)
\ee
so that a suitable version $Ch_{q,t} (\CV_m)$ of the equivariant character computes the bottom row of
the colored superpolynomial \eqref{bottomrow} with $\lambda = S^m$,
\be
Ch_{q,t} (\CV_m) \; = \; \CP^{S^m}_{\text{bottom}} (q,t) \,.
\label{naiveVmP}
\ee
Already at this stage the reader might suspect that incorporating the $t$-grading and passing to knot homologies
can be addressed by considering equivariant cohomology or K-theory of the vortex moduli space,
\be
H^*_{U(1)_q} (\CV_m (K)) \,,
\label{naiveHvort}
\ee
where $t$-grading is identified with the homological grading.
Although this idea is a little too naive, it is actually on the right track, and it is instructive to pursue it a little further.

Therefore, as the natural next step let us consider a non-abelian generalization of \eqref{abelianvorteq}
that describes supersymmetric solutions in the 2d theory:
\be
\CT_{\text{vortex}}~:~ U(p+1)~\text{gauge theory with}~p+1~\text{fundamental fields}~\phi_i
\ee
The corresponding vortex equations
\be
\begin{array}{rl}
* F_A & =~ i\sum_{i=1}^{p+1} \phi_i \phi_i^{\dagger} - i t \\
\bar \partial_A \phi_i & =~ 0
\end{array}
\label{vortexeq}
\ee
involve a $U(p+1)$ gauge connection and $p+1$ Higgs fields $\phi_i$ in the fundamental
representation of the gauge group. Again, the $m$-vortex moduli space is a K\"ahler manifold
of real dimension
\be
\dim~ \CV_m^{U(p+1)} = 2 m (p+1) \,,
\label{mmndimension}
\ee
In particular, the single-vortex moduli space is well known to be a $(2p+2)$-dimensional space
\be
\CV_1^{U(p+1)} \; \cong \; \C \times \cp^p
\ee
where the factor $\C$ parametrized by the ``center-of-mass'' position,
while $\cp^p$ encodes the ``internal degrees of freedom'' of a single non-abelian vortex.
The rotation symmetry $U(1)_q$ acts on $\C$ with weight 1,
so we expect that it contributes to the equivariant character a factor $\frac{1}{1-q}$.
However, unlike our first example (related to the unknot), now the moduli space $\CV_1^{U(p+1)}$
has non-trivial topology and, therefore, if $t$-grading is simply the homological grading on \eqref{naiveHvort}
the suitable generalization of the equivariant character should be a product of $\frac{1}{1-q}$
and the Poincar\'e polynomial of $\cp^p$,
\be
\frac{1}{1-q} \sum_{i=0}^p t^{2i}
\ee
This turns out to be the correct answer for the bottom row of the HOMFLY homology of the $(2,2p+1)$ torus knot.


Now let us explain why all these examples are ``working'' and where the connection with vortex equations come from.
The reason, in fact, is already contained in section~\ref{sec:geomphys}
where we reviewed the interpretation~\eqref{HHBPS} of homological knot invariants
in terms of supersymmetric configurations (BPS states) in the string theory setup~\eqref{theoryB}.
What this interpretation tells us is that specializing to the bottom row \eqref{bottomrow},
{\it i.e.} taking the limit $\a \to 0$, means the ``large volume limit.''
Indeed, according to the identification of the parameters \eqref{NvolCP1},
in this limit the interesting geometry (and topology) of the Calabi-Yau space $X$
is replaced by the simplest Calabi-Yau 3-fold, namely a flat space:
\be
X \;\overset{\a \to 0}{\leadsto}\; \C^3 \,.
\label{Xatozero}
\ee

In other words, the bottom row of the colored HOMFLY homology is described by
a much simpler ``toy model'' of \eqref{theoryB} in which the pair $(X,L_K)$ is replaced by $(\C^3, L_K)$.
(Not much happens to the Lagrangian submanifold $L_K$ in this limit.)

The next step is to look at this system from the vantage point of the 4-manifold $M_4 \cong \R^4$
and the defect (called the ``surface operator'' \cite{Ramified}) supported on $D \cong \R^2$.
Before we took the limit $\a \to 0$, the compactification on $X$ produces abelian gauge theory
on $M_4$ with gauge group $U(1)$ \cite{KKV}.
Incorporating an extra brane in this setup means including the so-called surface operator supported on $D$
or, mathematically speaking, ramification in the gauge theory on $M_4$.

Let $\CM_{k,m}$ be the moduli space of abelian instantons on $M_4 = \R^4$ with ramification along $D \subset M_4$.
In other words, $\CM_{k,m}$ is the moduli space of solutions to the self-duality equation on $M_4 \setminus D$,
\be
F_A^+ \; = \; 0
\label{sdeq}
\ee
with the second Chern class $k$, with the monopole number $m = \frac{1}{2\pi} \int_D F_A$,
and with the prescribed behavior along $D$.
The latter is what we call the ramification data;
{\it e.g.} a simple example of the so-called \textsl{tame} ramification
can be obtained by introducing a $\delta$-function source
in the self-duality equation \eqref{sdeq} on $M_4$:
\be
F_A^+ \; = \; 2\pi \alpha (\delta_D)^+ \,.
\ee
The gauge connections which solve this equation have a first-order pole at $D$.
More generally, one can study solutions to self-duality equations with singularities of arbitrarily high order,
\be
A = dz  \left( \frac{\alpha_1}{z} + \frac{\alpha_2}{z^2} + \ldots \right) + d \bar z \left( \ldots \right) \,.
\ee
This is called \textsl{wild} ramification and is precisely how the dependence on the knot $K$ will enter,
via the choice of the ramification data.\footnote{For instance, it was conjectured~\cite{DGH} that $(2,2p+1)$ torus knots
correspond to wild ramification of order $p$.}
Let us denote the corresponding moduli space by $\CM_{k,m} (K)$.

Much like the vortex moduli space $\CV_m$ enjoyed an action of the rotation group $U(1)_q$,
the moduli space of ``ramified instantons'' on $M_4 \setminus D \cong \C \times \C^*$
has an action of the rotation group $U(1)_q \times U(1)_t$,
where $U(1)_q$ acts by rotations of $D = \C$ and $U(1)_t$ acts by rotations of its normal bundle, $\C^*$.

Then, in the limit \eqref{Xatozero} the physical interpretation \eqref{HHBPS} of the colored HOMFLY homology predicts
\be
Ch_{q,t} (\CM_{0,m} (K)) \; = \; \bar \CP^{S^m}_{\text{bottom}} (K; q,t)
\ee
which is very close to \eqref{naiveVmP} and, in fact, is exactly the sought-after proper generalization of it.











The connection with vortex equations is now easy to see. At least for some knots
the moduli space $\CM_{k,m} (K)$ can be equivalently described as the moduli space of solutions
to the coupled \textsl{instanton-vortex equations}:
\begin{eqnarray}
F_A^+ & = & 2\pi \phi \otimes \phi^{\dagger} \; (\delta_D)^+  \nonumber \\
*_{D} F_B & = & i \phi^{\dagger} \otimes \phi - i t {\bf 1}_E \label{coupledvort} \\
\bar \partial_{A,B} \phi & = & 0 \nonumber
\end{eqnarray}
where $A$ is a unitary connection on the line bundle $\CL$ over $M_4$,
$B$ is a unitary connection on the bundle $E$ over $D \subset M_4$,
$\phi$ is an element $\phi \in H^0 (\Hom (E,\CL \vert_D ))$, and $\phi^{\dagger}$ is its adjoint.


As far as we know the instanton-vortex equations \eqref{coupledvort} are new and have not appeared in the literature previously.
Their closest cousin is a set of the so-called coupled vortex equations studied {\it e.g.} in~\cite{BGP1,BGP2},
where both $E$ and $\CL$ are bundles over $D$. In other words, our equations \eqref{coupledvort} can be viewed
as analogs of the coupled vortex equations where one of the bundles is extended over $M_4$.
For instance, for a $(2,2p+1)$ torus knot $T^{2,2p+1}$ one takes $E$ to be a unitary bundle of rank $p+1$.

Then, as before, to get the ``bottom row'' of the \textsl{unreduced} $S^m$-colored HOMFLY homology we need to consider
the equivariant character of $\CM_{0,m} (K)$ with instanton number $k=0$ and vortex number $m$.
In situations where $\CM_{k,m} (K)$ can be identified with the moduli space of solutions to \eqref{coupledvort}
this boils down to studying non-abelian vortex equations on $D$.
Thus, for $2p+1$ torus knots we end up with $U(p+1)$ vortex equations,
so that the equivariant character of $\CM_{0,m} (T^{2,2p+1}) \cong \CV_m^{U(p+1)}$
essentially consists of $p+1$ copies of the abelian vortex character that we discussed earlier, {\it cf.} \eqref{unknotvortchar}.

Our prediction is that the equivariant character of the $m$-vortex moduli space $\CV_m^{U(p+1)}$
is the ``bottom row'' of the $S^m$-colored HOMFLY homology of the $(2,2p+1)$ torus knot, {\it i.e.}
\begin{eqnarray}\nonumber
\!\!\!\!\!\!\!\!Ch_{q,t} (\CV_m^{U(p+1)})  &=& \frac{q^{-pm}}{(q;q)_m}  \sum_{0\le k_p \le \ldots \le k_2 \le k_1 \le m}
\left[\!\begin{array}{c} m \\k_1 \end{array}\!\right]\left[\!\begin{array}{c} k_1\\k_2 \end{array}
\!\right]\cdots\left[\!\begin{array}{c} k_{p-1}\\k_p \end{array}\!\right]  \times\\
& & \nonumber \!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\! \times \,\,\, q^{(2m+1)(k_1+k_2+\ldots+k_p)-\sum_{i=1}^p k_{i-1}k_i}
t^{2(k_1+k_2+\ldots+k_p)} ,
\end{eqnarray}
with the convention $k_0:=m$.
For example, when $m=2$ and $p=1$, {\it i.e.} for the $(2,3)$ torus knot (= trefoil knot $3_1$) colored by $\lambda = \tableau{2}$ we have
\be
Ch_{q,t} (\CV_2^{U(2)}) \; = \; q^{-2} \frac{1 + q^3 t^2 + q^4 t^2 + q^6 t^4}{(1-q)(1-q^2)}
\label{S2chtref}
\ee
which can be verified using equivariant $U(2)$ action on $\CV_2^{U(2)}$, see {\it e.g.} \cite{DGH} and \cite{Taipale}.

It would be interesting to understand better the relation between vortex moduli spaces
and the combinatorics of the Bialynicki-Birula cell decomposition discussed in Section \ref{sec:combbot}
that also determines the bottom row of the colored HOMFLY homology.
Thus, in the above example \eqref{S2chtref} of the $S^2$-colored trefoil, the corresponding
moduli space of two $U(2)$ vortices $\CV_2^{U(2)}$ has been studied in the literature \cite{Tong,Shifman,Baptista}
and is known to have two strata, which correspond to separated vortices and coincident vortices.
The first stratum --- of complex dimension 4 --- is simply the product of two single-vortex moduli spaces $\CV_1^{U(2)}$,
modulo the permutation of the two vortices,
\be
\CU_1 ( \CV_2^{U(2)} ) \; \cong \; \C \times \frac{\C \times \cp^1 \times \cp^1}{\Z_2}
\ee
with the ``diagonal'' removed.
The second stratum --- of complex dimension 3 ---  is known to be the space of Hecke modifications
(times the center of mass position),
\be
\CU_2 ( \CV_2^{U(2)} ) \; \cong \;  \C \times \mathbb{W} \cp^2_{(1,1,2)} \,.
\ee
See \cite{GS} for color graphics illustrating the bottom row of the $S^2$-colored HOMFLY homology
and the role of $\mathbb{W} \cp^2_{(1,1,2)}$ in its construction.
In this, and more general examples, it would be interesting to match the geometry of these strata
with the Bialynicki-Birula cell decomposition discussed in Section \ref{sec:combbot}.

Another direction for future work, already mentioned in Section \ref{sec:Bmodel},
is the relation between theory $\CT_{\text{vortex}} (K)$ and the surface operator theory considered in \cite{FGS2,FGSS}.
Indeed, here, in Section \ref{sec:Bmodel}, and in \cite{FGS2,FGSS} the Poincar\'e polynomial
of the colored HOMFLY homology (a.k.a. the superpolynomial) is realized as a certain index (or, character)
of a two-dimensional $\CN=2$ theory that describes the physics on $D$ in the brane construction \eqref{theoryB}.
Yet, the key difference is that here and in Section \ref{sec:Bmodel} there is a different $\CN=2$ theory
for each choice of ``color'' $\lambda$; the index of such theories determines colored superpolynomials
and {\it a priori} all such theories are unrelated.
In \cite{FGS2,FGSS}, on the other hand, a single $\CN=2$ theory $\CT_K$ (that depends only on the knot $K$)
determines the entire tower of $S^m$-colored homological invariants, via specializations of its supersymmetric index:
\be
\bar \CP^{S^m}_K (a,q,t) \; = \; \CI_{\CT_K} (x = q^m; a,q,t) \,.
\ee
Moreover, recursion relations found in \cite{FGS2,Nawata,FGSS}, which have a natural meaning\footnote{{\it e.g.} the characteristic
variety of the corresponding $q$-difference equations has a nice interpretation as the moduli space of SUSY parameters, {\it etc.}}
in the $\CN=2$ theory $\CT_K$, relate equivariant characters $Ch_{q,t} (\CM_{0,m} (K))$
with different values of the ``vortex number'' $m = \frac{1}{2 \pi} \int_D F$.
Similarly, from the vantage point of Section \ref{sec:Bmodel}, the recursion relations of \cite{FGS2,Nawata,FGSS}
relate B-models with target manifolds of different (super-)dimension
in a way reminiscent of the notions of ``endoscopy'' and ``transfer'' in the geometric Langlands correspondence \cite{FW}.
Thus, in the case of the trefoil knot we have:
\begin{align}
\CP^{S^{m+2}}_{\text{bottom}}
- (q^{-1} - t^2 q^m + (1+q) q^{2m} t^2) \CP^{S^{m+1}}_{\text{bottom}}
& \\
+ t^4 q^{3m-1} (q^m - 1) \CP^{S^{m}}_{\text{bottom}} & = 0 \notag
\end{align}



\begin{appendix}

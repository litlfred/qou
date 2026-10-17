---
doc_id: arxiv-math-0006057v2
doc_title: "arXiv:math/0006057v2 [math.QA] 10 Jun 2000"
section_id: sec-020-024-existence-of-the-haar-integral
section_title: "Existence of the Haar integral"
section_number: 0.24
pages: 28-35
source_pdf: 0006057v2.pdf
source_sha256: c881434fe9f4b04f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.972
latex_coverage_ratio: 0.981
doc_brief: "arXiv:math/0006057v2 [math.QA] 10 Jun 2000 — We give a survey of the theory of ﬁnite quantum groupoids (weak Hopf algebras), including foundations of the theory and applications to ﬁnite depth"
---
Given a dual bases $\{f_i\}$ and $\{\xi^i\}$ of $H$ and $\widehat H$, 
respectively,  let us consider the following canonical element
$$
\chi =\sum_i(\xi^i\actl S^{-2}(f_i)).
$$
One can show that $\chi$ is a left integral in $\widehat H$ such that
$\chi(xy)=\chi(yS^2(x))$ for all $x,y\in H$ and $l\act\chi={\widehat S}^2(\widehat 1\actl l)$ 
for any left integral $l$ in $H$ (see \cite{BNSz}, 3.25).

\begin{lemma}[\cite{BNSz}, 3.26]
\label{Haar}
\begin{enumerate}
\item[(i)] The Haar integral $h\in H$ exists iff the above mentioned $\chi$ is
non-degenerate, in which case $(h,\chi)$ is a dual pair of left integrals.
\item[(ii)] A left integral $l$ is a Haar integral iff $\eps_s(l)=1$.
\end{enumerate}
\end{lemma}
\begin{proof} (ii) If $\eps_s(l)=1$, then by 
$l\act\chi={\widehat S}^2(\widehat 1\actl l)$ one has $l\act\chi=\widehat 1$. 
Therefore, $(h,\chi)$ is a dual pair of non-degenerate left integrals. 
The property $\chi(xy)=\chi(yS^2(x))$ is equivalent to that the 
quasi-basis of $\chi$ satisfies
$$
l\2\otimes S^{-1}(l\1)=S(l\1)\otimes l\2,
$$
from where $\Delta(l)=\Delta(S(l))$ and $l=S(l)$. Furthermore, $\eps_t(l)=
\eps_t(S(l))=S\cdot \eps_s(l)=1$. Thus, $l$ is a Haar integral. The inverse 
statement is obvious.
\newline
(i) The "only if" part follows from the proof of (ii). 
If $\chi$ is non-degenerate 
and $h$ is its dual left integral, then, as above, $S(h)=h$; so $h$ is a 
two-sided integral and since $l\act\chi={\widehat S}^2(\widehat 1\actl l)$, 
it is normalized.
\end{proof}
 
\begin{theorem}[\cite{BNSz}, 3.27]
\label{Haar theorem}
Let $H$ be a finite quantum groupoid over an algebraically closed field $k$. 
Then the following conditions are equivalent:
\begin{enumerate}
\item[(i)] There exists a Haar integral, 
\item[(ii)] $H$ is semisimple and there exists an invertible element $g\in H$ 
such that $gxg^{-1}=S^2(x)$ for all $x\in H$ and
$Tr(\pi_\alpha(g^{-1}))\neq 0$ for all irreducible representations $\pi_\alpha$
of $H$ (here $Tr$ is the usual trace on a matrix algebra). 
\end{enumerate}
\end{theorem}

\begin{proof} 
The assumption on $k$ is used only to ensure that
$H=\oplus_\alpha M_{n_\alpha}(k)$, once knowing that it is semisimple, 
so that there is a $k$-basis of matrix units $\{e^{\alpha}_{ij}\}$ in $H$.

(ii)$\implies$(i):  Recall that any trace $\tau$ on $H$ is 
completely determined by its \textit{trace vector}  
$\tau_\alpha =\tau(1_\alpha)$. 
Now let $\tau:H\to k$ be the trace with trace vector $\tau_\alpha=
\tr \pi_\alpha(g^{-1})$. Then $\tau$ is non-degenerate and has a quasi-basis
$$
\sum_i x_i\otimes y_i=\sum_\alpha{\frac{1}{\tau_\alpha}}\sum^{n_\alpha}_{i,j=1}
e^{\alpha}_{ij}\otimes e^{\alpha}_{ji}.
$$
Notice that $\sum_i x_ig^{-1}y_i=1$. It is straightforward to verify that
$\chi'=g\act\tau$ coincides with $\chi$, so $\chi$ is  
non-degenerate and therefore its dual left integral $l$ has $\eps_s(l)=1$ by 
$l\act\chi={\widehat S}^2(\widehat 1\actl l)$. Thus, $l$ is a Haar integral.

(i)$\implies$(ii): If $h$ is a Haar integral, then $H$ is semisimple by
Theorem~\ref{maschke}. Let $\tau$ be a non-degenerate trace on $H$, 
then there exists a  unique $i\in H$ such that $i\act\tau=\widehat 1=\tau\actl i$. 
One can verify that $i$  is a two-sided non-degenerate integral in $H$ 
and that $S(i)=i$ (see \cite{BNSz}, I.3.21). 
To prove that $S^2$ is inner, it is enough to construct a non-degenerate 
functional $\chi$ on $H$ such that $\chi(xy)=\chi(yS^2(x))$ for all $x,y\in H$. 
But the proof of Lemma \ref{Haar} shows that this is the case for the dual 
left  integral to $i$.
\end{proof}

\begin{remark} 
\label {C*-semisimple}
\begin{enumerate}
\item[(a)]
There is a unique normalization of $g$
from Theorem~\ref{Haar theorem}(ii) 
such that the following conditions hold (\cite{BNSz}, 4.4) :
\begin{enumerate}
\item[(i)] $\tr(\pi_\alpha(g^{-1}))=\tr (\pi_\alpha(g))$ for all irreducible
representations $\pi_\alpha$ of $H$ (here $\tr$ is a usual trace on a
matrix algebra);
\item[(ii)] $S(g)=g^{-1}$.
\end{enumerate}
One can show that such a $g$ is {\em group-like}, i.e.,
$$
\Delta(g) =(g\otimes g)\Delta(1) = \Delta(1) (g\otimes g).
$$
The element $g$ implementing $S^2$ and satisfying
normalization conditions (i) and (ii) is called
the {\em canonical group-like element} of $H$.
\item[(b)]
Since $\chi = g\act\tau$ is the dual left integral to $h$, its quasi-basis
$\sum_i x_ig^{-1}\otimes y_i$ equals to $h\2\otimes S^{-1}(h\1)$, which
implies the formula
$$ 
(S\otimes id)\Delta(h)=\sum_i x_i\otimes g^{-1}y_i=\sum_\alpha 1/\tau_\alpha
\sum_{ij}e^\alpha_{ij}g^{-1/2}\otimes g^{-1/2}e^\alpha_{ji}.
$$
\end{enumerate}
\end{remark}

A dual notion to that of the Haar integral is the Haar measure. 
Namely, a functional $\phi \in \widehat H$ is said to be a {\em Haar measure} 
on $H$  if it is a normalized left and right invariant measure and 
$\phi\circ S=\phi$. Any of the  
equivalent conditions of Theorem \ref{Haar} is also equivalent to existence 
(and uniqueness) of the Haar measure.



\subsection{$C^*$-quantum groupoids}

Definition \ref{semisimple and C*} and the uniqueness of the unit, counit and 
the antipode (see Proposition \ref{properties of S}) imply that 
$$
1^*=1,\quad \eps(x^*)= \overline{\eps(x)},\quad (S\circ *)^2 =\id
$$ 
for all $x$ in any $*$-quantum groupoid. It is also easy to check the relations 
$$
\eps_t(x)^*=\eps_t(S(x)^*),\qquad \eps_t(x)^*=\eps_t(S(x)^*),
$$
therefore, $H_t$ and $H_s$ are $*$-subalgebras, and to show that the dual, 
$\widehat H$, is also a $*$-quantum groupoid with respect to the $*$-operation
\begin{equation}
\la\phi^*,x\ra=\overline{\la\phi,S(x)^*\ra}\qquad \mbox{ for all } 
\phi\in \widehat H,\ x\in H.
\end{equation}

The $*$-operation allows to simplify the axioms of a quantum groupoid 
(cf. the  axioms used in \cite{NV1}, \cite{N1}). The second parts of
equalities~(\ref{eps m}) and (\ref{Delta 1})  
of Definition~\ref{finite quantum groupoid} 
follow from the rest of the axioms, also $S*\id = \eps_s$ is 
equivalent to $\id* S=\eps_t$. Alternatively, 
under the condition that the antipode is both algebra and coalgebra 
anti-homomorphism, the axioms (\ref{eps m}) and (\ref{Delta 1}) can be
replaced  by the identities of Proposition~\ref{counital properties} (ii) 
and (v) involving the target counital map.

\begin{theorem} (\cite{BNSz}, 4.5)
\label{C*-Haar}
In a $C^*$-quantum groupoid the Haar integral $h$ exists, $h=h^*$ and
$$
(\phi,\psi)=\la\phi^*\psi,h\ra,\qquad \phi,\psi\in \widehat H
$$
is a scalar product making $\widehat H$ a Hilbert space where the left regular
representation of $\widehat H$ is faithful. 
Thus, $\widehat H$ is a $C^*$-quantum groupoid, too.
\end{theorem}

\begin{proof}
Clearly, $H$ and $g$ verify all 
the conditions of Theorem \ref{Haar theorem}, from where the existence of Haar 
integral follows. Since $h$ is non-degenerate, the scalar product 
$(\cdot,\cdot)$ is  also non-degenerate. By the equality 
$$
(\phi,\phi)=\la\phi^*\phi,h\ra=\overline{\la\phi,S(h\1)^*\ra}\la\phi,h\2\ra,
$$
positivity of $(\cdot,\cdot)$ follows from Remark \ref{C*-semisimple}(b).
\end{proof}

We will denote by $\widehat h$ the Haar measure of $\widehat H$.

\begin{remark} 
\label{eps is positive}
$\eps$ is a positive functional, i.e., $\eps(x^*x) \geq 0$ for all $x\in H$.
Indeed, for all $x\in H$ we have
$$
\eps(x^*x)
= \eps(x^*1\1)\eps(1\2 1'\2)\eps(1'\1 x)=\eps(\eps_t(x)^* \eps_t(x))
= \la\widehat h,\eps_t(x)^*\eps_t(x)\ra\geq 0,
$$
where $\widehat h\vert_{H_t}=\eps\vert_{H_t}$, since
$\la\widehat h,z\ra=\la\widehat\eps_t(\widehat h),z\ra=\la\widehat 1,z\ra$ 
for all $z\in H_t$.
\end{remark}

The Haar measure provides target and source {\em Haar conditional 
expectations} (all properties are easy to verify):
\begin{eqnarray*}
E_t &:& H\to H_t :  E_t(x)=(id\otimes\widehat h)\Delta(x), \\
E_s &:& H\to H_s :  E_s(x)=(\widehat h\otimes id)\Delta(x).
\end{eqnarray*}
Let us introduce an element $g_t=E_t(h)^{1/2}\in H_t$.


\begin{remark}
\label{group-like}
(\cite{BNSz}, 4.12).
$g_t$ is positive and invertible, and the canonical group-like element 
of $H$ can be written as $g=g_tS(g_t^{-1})$.
\end{remark}

One can check that for a quasitriangular $*$-quantum groupoid $\bR=\R^*$.
\begin{proposition}[\cite{NTV}, 9.3]
\label{*-double} 
If $H$ is a $C^*$-quantum groupoid, then $D(H)$ is a quasitriangular
$C^*$-quantum groupoid.
\end{proposition}

\begin{proof}
The result follows from the fact that $\widehat{D(H)}$ is a $C^*$-quantum
groupoid, which is easy to verify using the explicit formulas from
Remark~\ref{dual double}.
\end{proof}

\begin{proposition}
\label{*-Ribbon WHA}
A quasitriangular $C^*$-quantum groupoid $H$ is automatically ribbon 
with the ribbon element $\nu=u^{-1}g=gu^{-1}$, where $u$ is the Drinfeld
element from Definition~\ref{Drinfeld element} and $g$ is the canonical
group-like element.
\end{proposition}

\begin{proof}
Since $u$ also implements $S^2$ (Proposition \ref{elements u and v}), 
$\nu=u^{-1}g$ is central, therefore $S(\nu)$ is also central.
Clearly, $u$ must commute with $g$. The same Proposition gives
$\Delta(u^{-1}) = \R_{21}\R(u^{-1}\otimes u^{-1})$,
which allows us to compute
$$
\Delta(\nu) = \Delta(u^{-1})(g\otimes g) = 
\R_{21}\R(u^{-1}g\otimes u^{-1}g) = \R_{21}\R(\nu \otimes \nu).
$$
Propositions~\ref{properties of R} and \ref{elements u and v}
and the trace property imply that
\begin{eqnarray*}
\tr(\pi_\alpha(u^{-1})) 
&=& \tr(\pi_\alpha( \R^{(2)}S^2(\R^{(1)}) )) \\ 
&=& \tr (\pi_\alpha(S^3(\R^{(1)}) S(\R^{(2)}) ) = \tr(\pi_\alpha(S(u^{-1}))).
\end{eqnarray*}
Since $u^{-1} = \nu g^{-1}$ and $\nu$ is central, the above relation 
means that 
$$
\tr(\pi_\alpha(\nu))\tr(\pi_\alpha(g^{-1})) =
\tr(\pi_\alpha(S(\nu)))\tr(\pi_\alpha(g)),
$$
and, therefore, $\tr(\pi_\alpha(\nu)) = \tr(\pi_\alpha(S(\nu)))$ for
any irreducible representation $\pi_\alpha$, which shows that
that $\nu = S(\nu)$ (cf. \cite{EG}).
\end{proof}

\begin{remark}
\label{C*-q-trace}
For a connected ribbon $C^*$-quantum groupoid we have:
$$
\tr_q(f) = (\dim H_t)^{-1} \Tr_V(g\circ f),\ \dim_q(V) = 
(\dim H_t)^{-1} \Tr_V(g).
$$
for any $f\in \End(V)$, $V$ is an $H$-module. 
\end{remark}



\subsection{$C^*$-quantum groupoids and unitary modular categories}

To define the (unitary) representation category $\URep(H)$ of a $C^*$-quantum groupoid
$H$ we consider {\it unitary} $H$-modules, i.e., $H$-modules $V$ 
equipped with a scalar product 
$$
(\cdot,\cdot): V\times V\to \mathbb{C} \qquad
\mbox{ such that } \qquad 
(h\cdot v,w)=(v,h^*\cdot w)\ \forall h\in H, v,w\in V.
$$
The notion of a morphism in this category is the same as in $\Rep(H)$.

The monoidal product of $V,W\in \URep(H)$ is defined as follows. We
construct a tensor product $V\otimes_\mathbb{C} W$ of Hilbert spaces and note
that the action of $\Delta(1)$ on this left $H$-module is an orthogonal
projection. The image of this projection is, by definition, the
monoidal product 
of $V,W$ in $\URep(H)$. Clearly, this definition is compatible with the monoidal
product of morphisms in $\Rep(H)$.
 
For any $V\in \URep(H)$, the dual space $V^*$ is naturally identified 
($v\to \overline v$) with the conjugate Hilbert space, and under this 
identification we have 
$h\cdot\overline v= \overline{S(h)^*\cdot v}\ (v\in V, \overline v\in V^*$). 
In this way $V^*$ becomes a unitary $H$-module with scalar product 
$(\overline v, \overline w)=(w,gv)$, where $g$ is the canonical group-like 
element of $H$. 

The unit object in $\URep(H)$ is $H_t$ equipped with scalar product 
$(z,t)_{H_t}= \eps(zt^*)$ (it is known \cite{BNSz}, \cite{NV1} that
the restriction of $\eps$ to $H_t$ is a non-degenerate positive form). 
One can verify that the maps  $l_V,r_V$ and their inverses are isometries
and that $\URep(H)$ is a monoidal category with duality
(see also \cite{BNSz}, Section 3). In a natural way we have a notion of a 
{\em conjugation} of morphisms (\cite{T}, II.5.1).

\begin{remark}
\label{*-R-matrix}
a) One can check that for a quasitriangular $*$-quantum groupoid $H$
the braiding is an isometry in $\URep(H) : c^{-1}_{V,W}=c^{*}_{V,W}$.

b) For a ribbon $C^*$-quantum groupoid $H$,
the twist is an isometry in $\URep(H)$. 
Indeed, the relation $\theta_{V}^*=\theta_{V}^{-1}$ 
is equivalent to the identity $S(u^{-1}) = u^*$, 
which follows from Proposition~\ref{properties of R} and 
Remark~\ref{*-R-matrix}a).
\end{remark} 

A {\em Hermitian ribbon category} is a ribbon category endowed with a 
conjugation of morphisms $f\mapsto\overline{f}$ satisfying natural conditions
of (\cite{T}, II.5.2).
A {\em unitary ribbon category} is a Hermitian ribbon category over the
field $\mathbb{C}$ such that for any morphism $f$ we have $\tr_q(f\overline{f})
\geq 0$.
In a natural way we have a {\em conjugation}
of morphisms in $\URep(H)$. Namely, for any morphism $f:V\to W$ we define 
$\overline f:W\to V$ as $\overline f (w)=\overline{f^*(\overline w)}$ for
any $w\in W$. Here $\overline w\in W^*, f^*:W^*\to V^*$ is the standard dual
of $f$ (see \cite{T}, I.1.8) and $\overline{f^*(\overline w)}\in V$.
For the proof of the following lemmma see (\cite{NTV}, 9.7).

\begin{lemma}
\label{hermit-ribbon}
Given a quasitriangular $C^*$-quantum groupoid $H,\ \URep(H)$ is a unitary 
ribbon $Ab$-category with respect to the above conjugation of morphisms.
\end{lemma}

The next proposition extends (\cite{EG}, 1.2).

\begin{proposition}
\label{rep of C* is modular}
If $H$ is a connected $C^*$-quantum groupoid, then $\Rep(D(H))$ is a unitary 
modular category.
\end{proposition}

\begin{proof}
The proof follows from Lemmas~\ref{hermit-ribbon}, 
\ref{factorizable implies modular} and
Propositions~\ref{D(H) is factorizable}, \ref{*-double}.






\end{proof}
\end{section}





\begin{section} 
{$C^*$-quantum groupoids and subfactors : the depth 2 case}
 
In this section we characterize finite index  type II$_1$ subfactors 
of depth $2$ in terms of $C^*$-quantum groupoids.
Recall that a II$_1$ factor is a $*$-algebra of operators on a Hilbert
space that coincides with its second centralizer, or, equivalently,
is weakly closed (i.e., a von Neumann algebra)
with the trivial center that admits a finite trace.
An  example of such a factor is the group von Neumann algebra of a discrete
group whose every non-trivial conjugacy class is infinite, the corresponding
trace given by its Haar measure. It is also known, that there exists
a unique, up to an isomorphism, hyperfinite (i.e., generated by an 
increasing sequence of finite-dimensional $C^*$-algebras) II$_1$ factor.

There is a notion of index for subfactors, extending the notion of index of
a subgroup in a group, though it can be non-integer. 
For the foundations of  the subfactor theory see \cite{GHJ}, \cite{JS}.


\subsection{Actions of $C^*$-quantum groupoids on von Neumann algebras}
Let a von Neumann algebra $M$ be a left 
$H$-module algebra in the sense of Definition \ref{module algebra} via a
weakly continuous action of a $C^*$-quantum groupoid 
\begin{equation*}
H\otimes_\mathbb{C} M \ni  x\otimes m \mapsto (x\lact m)\in M
\end{equation*}
such that $(x\lact m)^* = S(x)^* \lact m^*$ 
and $x\lact 1 =0$ iff $\eps_t(t)=0.$

Then one can show (\cite{NSzW}, 3.4.2) that the smash product algebra 
(now we call it {\em crossed product algebra} and  denote by $M\rtimes H$),  
equipped with an involution  
$[m\otimes x]^* = [(x\1^*\lact m^*) \otimes  x\2^*]$, is a von Neumann algebra.

The collection
$ M^H =\{ m\in M \mid x\lact m = \eps_t(x)\lact m,\ \forall x\in H\}$
is a von Neumann subalgebra of $M$, called a {\em fixed point subalgebra}.
The centralizer $M^\prime \cap M \rtimes H$ always contains
a the source counital subalgebra $H_s$. 
Indeed, if $y\in H_s$, then $\Delta(y) =1\1\otimes 1\2 y$, therefore
\begin{eqnarray*}
[1\otimes y][m\otimes 1]
&=& [(y\1\lact m)\otimes y\2]=[(1\1\lact m)\otimes  1\2 y] \\
&=& [m\otimes y]=[m\otimes 1][1\otimes y],
\end{eqnarray*}
for any $m\in M$, and $H_s\subset M^\prime \cap M \rtimes H$.
An action of $H$ is
called {\em minimal} if $H_s = M^\prime \cap M\rtimes H$.

One can define the dual action of $\widehat H$  on the von
Neumann algebra $M\rtimes H$ as in (\ref{dual action}) and 
construct the von Neumann algebra $(M\rtimes H) \rtimes \widehat H$.

\begin{remark}
The following results hold true if $S^2=\id$, i.e., if $H$ is involutive
(\cite{N1}, 4.6, 4.7).
\begin{enumerate}
\item[(a)] $M\subset M\rtimes H\subset (M\rtimes H)
\rtimes \widehat H$ is a basic construction;
\item[(b)] $M\rtimes H$ is free as a left $M$-module;
\item[(c)]  $(M\rtimes H)\rtimes \widehat H \cong M\otimes_\mathbb{C}
M_n(\mathbb{C})$ for some integer $n$.
\end{enumerate}
\end{remark}

\begin{example} 
\label{Weyl algebra} 
For a trivial action of $H$ on $H_t$  and
the corresponding dual action of $\widehat H$ on $H\cong H_t\rtimes H$ (see
Example \ref{examples of actions} (i) and (ii)), 
$H_t\subset H\subset H\rtimes \widehat H$ is the basic
construction of finite-dimensional $C^*$-algebras with respect to the
Haar conditional expectation $E_t$ (\cite{BSz2}, 4.2). 
\end{example}

If $H$ is a connected
$C^*$-quantum groupoid having a minimal action on a II${}_1$ factor $M$
then one can show  (\cite{NSzW}, 4.2.5, 4.3.5) that 
$\widehat H$ is also connected and that 
$$ 
N=M^H\subset M\subset M_1=M \rtimes H\subset M_2=(M\rtimes H)\rtimes \widehat H
\subset \cdots
$$
is the Jones tower of factors of finite index with {\em the derived tower} 
$$
N'\cap N=\mathbb{C}\subset N'\cap M=H_t\subset N'\cap M_1=H\subset N'\cap M_2=
H\rtimes \widehat H\subset  \cdots
$$ 
The fact that the last triple of finite-dimensional $C^*$-algebras is a
basic construction, means exactly that the subfactor $N\subset M$ 
has depth 2. Moreover, the finite-dimensional $C^*$-algebras 
\begin{equation}
\label{square}
\begin{array}{ccc}
H^* & \subset & H^* \rtimes H  \\
\cup&         & \cup        \\   
H_t= H_s^* & \subset & H,
\end{array}
\end{equation}
form {\em a canonical commuting square}, 
which completely  determines the equivalence class of the
initial subfactor. This implies that any biconnected $C^*$-quantum groupoid
has at most one minimal action on a given II$_1$ factor and thus corresponds 
to no more than one (up to equivalence) finite index depth 2 subfactor.

\begin{remark}
It was shown in (\cite{N1}, 5) that any biconnected involutive $C^*$-quantum 
groupoid has a minimal action on the  hyperfinite II$_1$ factor. This
action is constructed by iterating the basic construction for the
square (\ref{square}) in the horizontal direction, see \cite{N1} for
details.
\end{remark}







\subsection{Construction of a $C^*$-quantum groupoid from a depth 2 subfactor}

Let $N\subset M$ be a finite index ($[M:N]= \lambda^{-1}$) depth 2
II${}_1$ subfactor and
\begin{equation}
N \subset M \subset M_1 \subset M_2 \subset \cdots
\end{equation}
the corresponding Jones tower, $M_1 = \langle M,\,e_1 \rangle,\,
M_2 = \langle M_1,\,e_2 \rangle,\dots,$ where $e_1 \in N^\prime
\cap M_1,\,e_2 \in M^\prime \cap M_2,\cdots$
are the Jones  projections. The depth 2 condition means that
$N^\prime \cap M_{2}$ is the basic construction of the inclusion
$N^\prime \cap M  \subset  N^\prime \cap M_{1}$. Let $\tau$ be
the trace on $M_2$ normalized by $\tau(1)=1$.

Let us denote
$$
A=N'\cap M_1, \quad B=M'\cap M_2, \quad B_t=M'\cap M_1, \quad B_s=M_1'\cap M_2
$$
and let $\Tr$ be the trace of the regular representation of $B_t$ on
itself. Since both $\tau$ and $\Tr$ are non-degenerate, there exists a positive
invertible element $w\in Z(B_t)$  such that $\tau(wz)=\Tr(z)$ for all
$z\in B_t$ (the index of $\tau\vert_{M'\cap M_1}$
in the sense of \cite{W}).

\begin{proposition} 
\label{duality}
There is a canonical non-degenerate duality form between 
$A$ and $B$ defined by 
\begin{equation}
\la a,\, b \ra = \lambda^{-2}\tau(ae_2e_1wb)= \lambda^{-2}Tr E_{B_t}(bae_2e_1),
\end{equation}
for all $a\in A$ and $b\in B$.
\end{proposition}

\begin{proof}
If $a\in A$ is such that $\la a,\, B\ra = 0$ , then, using 
\cite{PP1}, 1.2, one has
$$
\tau(a e_2 e_1 B) = \tau(a e_2 e_1 (N^\prime \cap M_2)) = 0,
$$
therefore, using the properties of $\tau$ and Jones projections, we get
\begin{eqnarray*}
\tau(a a^*) &=& \lambda^{-1} \tau(a e_2 a^*) =
\lambda^{-2}\tau(a e_2 e_1 (e_2 a^* ) ) = 0,
\end{eqnarray*}
so $a=0$. Similarly for $b\in B$.
\end{proof}

Using the duality $\la a,\, b \ra$, one defines a coalgebra structure on $B$ :
\begin{eqnarray}
\la a_1\otimes a_2,\, \Delta(b) \ra &=&   \la a_1 a_2,\, b \ra, \\
\eps(b) &=& \la 1,\, b\ra, 
\end{eqnarray}
for all $a,a_1,a_2\in A$ and $b\in B$. Similarly, one defines a
coalgebra structure on $A$.

We define a linear endomorphism $S_B:B\to B$ by 
\begin{equation}
E_{M_1}( b e_1 e_2) = E_{M_1}(e_2 e_1 S_B(b)),
\end{equation}
Note that $\tau\circ S_B =\tau$.
Similarly one can define a linear endomorphism $S_A:A\to A$ such that
$E_{M^\prime}(S_A(a)e_2 e_1) = E_{M^\prime}(e_1 e_2 a)$
and $\tau\circ S_A =\tau$.

\begin{proposition}
\label{properties of S (1)} (\cite{NV2}, 4.5, 5.2):
The following identities hold :
\begin{enumerate}
\item[(i)] $S_B(B_s)=B_t$,
\item[(ii)] $S_B^2(b) =b$ and $S_B(b)^* = S_B(b^*)$,
\item[(iii)] $\Delta(b)(S_B(z)\otimes 1) = \Delta(b)(1\otimes z), \qquad 
\Delta(bz)= \Delta(b)(z\otimes 1),\ (\forall z\in B_t)$,
\item[(iv)] $S_B(bc) = S_B(c)S_B(b)$, \newline
      $\Delta(S_B(b)) = (1\otimes w^{-1})(S_B(b\2)\otimes S_B(b\1))
      (S_B(w)\otimes 1)$.
\end{enumerate}
\end{proposition}

Define an  antipode and new involution of $B$ by
\begin{equation}
S(b)=S_B(wbw^{-1}), \qquad
b^\star = S(w)^{-1}b^*S(w).
\end{equation} 

\begin{theorem}
\label{B is a quantum groupoid}
With the above operations $B$ becomes a biconnected $C^*$-quantum groupoid 
with the counital subalgebras $B_s$ and $B_t$.  
\end{theorem}

\begin{proof}
One can check (\cite{NV2}, 4.6) that $\Delta(1)\in B_s\otimes B_t$, hence, 
since  $\Delta(1)\in B_s\otimes B_t$ and $B_t$ commutes with $B_s$, we have
\begin{eqnarray*}
(\id\otimes\Delta)\Delta(1) 
&=& 1\1 \otimes \Delta(1)(1\2 \otimes 1) \\
&=& (1 \otimes \Delta(1))(\Delta(1)\otimes 1)
    = (\Delta(1)\otimes 1) (1 \otimes \Delta(1))
\end{eqnarray*}
which is axiom (\ref{Delta 1}) of Definition~\ref{finite quantum groupoid}.
The axiom~(\ref{eps m})  dual to it is obtained similarly, considering
the comultiplication in $A$.

As a consequence of the ``symmetric square'' relations $BM_1 =M_1B =M_2$
one obtains (\cite{NV2}, 4.12) the identity
\begin{equation}
\label{crucial}
bx =\lambda^{-1} E_{M_1}(b\1 x e_2) b\2 \quad \mbox{ for all } \quad
b\in B,\,  x\in M_1,
\end{equation}
from where it follows that
\begin{equation}
\label{good property}
E_{M_1}(bxye_2)  =\lambda^{-1} E_{M_1}(b\1 x e_2) E_{M_1}(b\2ye_2) 
\quad \mbox{ for all } \quad b\in B,\,x,y\in M_1.
\end{equation}
We use this identity to prove that $\Delta$ is a homomorphism :
\begin{eqnarray*}
\la a_1a_2,\, bc \ra 
&=& \la \lambda^{-1}E_{M_1}(ca_1a_2e_2),\, b \ra \\
&=& \la \lambda^{-2}E_{M_1}(c\1 a_1e_2)E_{M_1}(c\2 a_2e_2),\, b \ra \\
&=& \la \lambda^{-1}E_{M_1}(c\1 a_1e_2), b\1 \ra
    \la \lambda^{-1}E_{M_1}(c\2 a_2 e_2),\, b\2 \ra    \\
&=& \la a_1,\, b\1c\1 \ra \la a_2,\, b\2 c\2 \ra,
\end{eqnarray*}
for all $a_1,a_2 \in A$, whence $\Delta(bc) =  \Delta(b)\Delta(c)$.
Next, 
\begin{eqnarray*}
\la a,\, \eps(1\1b)1\2 \ra
&=& \la 1,\,1\1b \ra \la a,\, 1\2 \ra \\
&=& \la \lambda^{-1}E_{M_1}(be_2), 1\1 \ra \la  a,\, 1\2 \ra \\
&=& \la \lambda^{-1}E_{M_1}(be_2)a, 1 \ra
 = \la a,\, \lambda^{-1}E_{M_1}(be_2) \ra, 
\end{eqnarray*}
therefore $\eps_t(b) = \lambda^{-1}E_{M_1}(be_2)$ (similarly,
$\eps_s(b) = \lambda^{-1}E_{M_1'}(e_2b)$).
Using Equation (\ref{good property}) we have
\begin{eqnarray*}
\la a,\, b\1 S(b\2) \ra 
&=& \la a,\, b\1 S_B(wb\2 w^{-1}) \ra \\
&=&  \lambda^{-3} \tau (E_{M_1}(S_B(w b\2 w^{-1}) a e_2) e_2 e_1 wb\1) \\
&=&  \lambda^{-3} \tau (E_{M_1}(e_2 a wb\2 w^{-1}) e_2 e_1 wb\1) \\
&=& \lambda^{-3} \tau (E_{M_1}(e_2 a wb\2 w^{-1})E_{M_1}(e_2 e_1 wb\1) ) \\
&=& \lambda^{-2} \tau (E_{M_1}(e_2 a e_1 wb)) = \la a,\, \eps_t(b) \ra. 
\end{eqnarray*}
The antipode $S$ is anti-multiplicative and anti-comultiplicative,
therefore axiom~(\ref{S id S}) of Definition~\ref{finite quantum groupoid}
follows from the other axioms. Clearly,
$\eps_t(B) = M'\cap M_1$ and $\eps_s(B) = M_1'\cap M_2$.
$B$ is biconnected, since the inclusion
$B_t=M^\prime \cap M_1 \subset B =M^\prime \cap M_2$  is connected
(\cite{GHJ}, 4.6.3) and $B_t \cap B_s =(M^\prime \cap M_1)\cap
(M_1^\prime \cap M_2)= \mathbb{C}$.

Finally, from the properties of
$\Delta$ and $S_B$ we have $\Delta(b^\star)=\Delta(b)^{\star\otimes\star}$.
\end{proof}


\begin{remark}
\label{properties of B}
\begin{enumerate}
\item[(i)] $S^2(b) = gbg^{-1}$, where $g=S(w)^{-1}w$. 
\item[(ii)] The Haar projection of $B$ is $e_2w$ 
and the normalized Haar functional is $\phi(b) =$ $= \tau(S(w)wb)$.
\item[(iii)]  The non-degenerate duality $\la\, ,\,\ra$ makes 
$A=N^\prime \cap M_1$ the $C^*$-quantum groupoid dual to $B$.
\item[(iv)] Since the Markov trace (\cite{GHJ}, 3.2.4) of the inclusion
$N\subset M$ is also the Markov trace of the finite-dimensional inclusion
$A_t\subset A$, it is clear that $[M:N]=[A:A_t]=[B:B_t]$. We call last
number {\em the index of the quantum groupoid} $B$.

\item[(v)] Let us mention two classification results obtained in 
(\cite{NV2}, 4.18, 4.19)  by quantum groupoid methods:
\subitem (a) If $N\subset M$ is a depth 2 subfactor such that
$[M:N]$ is a square free integer (i.e., $[M:N]$ is an integer which
has no divisors of the form $n^2,\, n > 1$), then 
$N^\prime\cap M=\mathbb{C}$, and there is a (canonical) minimal action
of a Kac algebra $B$ on $M_1$ such that $M_2 \cong  M_1\rtimes B$ 
and $M=M_1^B$.
\subitem (b) If $N\subset M$ is a depth 2  II${}_1~$subfactor such that
$[M:N]=p$ is prime, then $N^\prime\cap M=\mathbb{C}$, and there is an
outer action of the cyclic group $G=\mathbb{Z}/p\mathbb{Z}$ on $M_1$ such that 
$M_2 \cong  M_1\rtimes G$ and $M=M_1^G$.
\end{enumerate}
\end{remark}

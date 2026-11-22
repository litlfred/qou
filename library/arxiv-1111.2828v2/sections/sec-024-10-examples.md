---
doc_id: arxiv-1111.2828v2
doc_title: "THE COMPLEX VOLUME OF SL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-024-10-examples
section_title: "Examples"
section_number: 10
pages: 35-39
source_pdf: 1111.2828v2.pdf
source_sha256: 90e2f5a9b978d403
toc_source: outline
text_source: latex
latex_prose_ratio: 0.81
latex_coverage_ratio: 0.98
doc_brief: "THE COMPLEX VOLUME OF SL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS — For a compact 3-manifold M with arbitrary (possibly empty) boundary, we give a parametrization of the set of conjugacy classes of"
---
\lbl{sec.examples}

In the examples below, all computations of Ptolemy varieties are exact, whereas the computations of complex volume are numerical with at least $50$ digits precision.

\begin{example}
[The $5_2$ knot complement]
\lbl{ex.52}
Consider the $3$-cycle $K$ obtained from the simplices in 
Figure~\ref{52triangulation} by identifying the faces via the unique 
simplicial attaching maps preserving the arrows. The space obtained 
from $K$ by removing the $0$-cell is homeomorphic to the complement of 
the $5_2$ knot, as can be verified by SnapPy~\cite{SnapPy}.

\begin{figure}[ht]
$$
\psdraw{SLrepFigures.12}{1.8in} \qquad
\psdraw{SLrepFigures.13}{1.8in} \qquad
\psdraw{SLrepFigures.14}{1.8in} 
$$
\caption{A $3$-cycle structure on the $5_2$ knot complement, and Ptolemy 
coordinates for $n=3$.}\lbl{52triangulation}
\end{figure}

Labeling the Ptolemy coordinates as in Figure~\ref{52triangulation}, the 
Ptolemy variety for $n=3$ is given by the equations
\begin{equation}
\begin{aligned}
&a_0x_3+b_0x_1=b_0x_2,&\quad &a_0y_3+a_0x_0=c_0y_2,&\quad &a_0x_2+b_0y_2=a_0x_1\\
&x_2c_0+b_1x_0=x_3a_0,&\quad &y_2b_0+a_1x_3=y_3b_0,&\quad &x_1a_0+b_1y_3=x_2c_0\\
&x_1c_1+x_3c_0=b_1x_0,&\quad &x_0b_1+y_3c_0=c_1x_3,&\quad &y_2a_1+x_2b_0=a_1y_3\\
&a_1x_0+x_2c_1=x_1a_1,&\quad &a_1x_3+y_2c_1=x_0b_1,&\quad &a_1y_3+x_1b_1=y_2c_1
\end{aligned} 
\end{equation}
together with an extra equation (involving an additional variable $t$)
\begin{equation}
a_0a_1b_0b_1c_0c_1x_0x_1x_2x_3y_2y_3t=1,
\end{equation}
making sure that all Ptolemy coordinates are non-zero. By 
Remark~\ref{normalizerremark}, the diagonal matrices act on the decorations, 
and one easily checks that the action by a matrix $\diag(x,y,z)$ 
with determinant $1$ multiplies a Ptolemy coordinate on an edge by $x^2y$ and a Ptolemy coordinate on a face by $x^3$.
Since we are not interested in the particular decoration, we may thus assume e.g.~that $a_0=y_3=1$.  
Using Magma~\cite{Magma}, one finds that 
the Ptolemy variety, after setting $a_0=y_3=1$, has three zero-dimensional
components with $3$, $4$ and $6$ points respectively. 
One of these is given by
\begin{equation}
\lbl{geometriccomp}
\begin{gathered}
a_0=a_1=y_3=1,\quad x_1=-1, \quad c_0=c_1=x_0^2+2x_0+1\\
y_2=x_0^2+2=-x_2,\quad x_3=-x_0^2-x_0-1\\
x_0^3+x_0^2+2x_0+1=0 












\end{gathered}
\end{equation}
Thus, this component gives rise to $3$ representations, one for each 
solution to $x_0^3+x_0^2+2x_0+1=0$. Using the fact that 
$R(\lambda(c))=i\Vol_\C(\rho)$, the complex volumes of these can be 
computed to be
\begin{equation}
\lbl{SL3geometric} 
0.0-4.453818209\dots i\in\C/4\pi^2i\Z,
\qquad \pm 11.31248835\ldots+12.09651350\dots i\in\C/4\pi^2i\Z
\end{equation}
corresponding to the values $x_0=-0.5698\dots$ and 
$x_0=-0.2150\mp1.3071\dots i$, respectively. 

In Zickert~\cite[Section~6]{ZickertDuke}, the complex volumes of the 
Galois conjugates of the geometric representation are computed to be
\begin{equation}
\lbl{PSL2geometric}
0.0-1.113454552\ldots i\in\C/\pi^2i\Z,
\qquad \pm 2.828122088\ldots + 3.024128376\ldots i\in\C/\pi^2i\Z.
\end{equation}
Notice that \eqref{SL3geometric} is (approximately) $4$ times 
\eqref{PSL2geometric}. It thus follows from Theorem~\ref{detectgeo} 
that the representations given by~\eqref{geometriccomp} are $\phi_3$ 
composed with the geometric component of $\PSL(2,\C)$-representations 
and that the factor of $4$ is exact.

Another component is given by
\begin{equation}
\begin{gathered} 
a_0=a_1=y_3=1,\quad x_1=-1,\quad b_1=-x_0\\
b_0=1/4x_0^3-1/4x_0^2+3/4x_0-1/2\\
c_0=c_1=1/4x_0^3-1/4x_0^2-1/4x_0+1/2\\
y_2=-x_2=1/4x_0^3+3/4x_0^2+7/4x_0+3/2\\
x_3=-x_0^2-x_0-1\\
x_0^4+x_0^3+x_0^2-4x_0-4=0.  












\end{gathered}
\end{equation}
In this case there are two distinct complex volumes given by:
\begin{equation}
0.0+2.631894506\ldots i=\frac{4}{15}\pi^2i\in\C/4\pi^2i\Z,
\quad 0.0+10.527578027\ldots i=\frac{16}{15}\pi^2i\in\C/4\pi^2i\Z.
\end{equation}

The third component has somewhat larger coefficients, but after introducing 
a variable $u$ with $u^6 + 5u^4 + 8u^2 - 2u + 1=0$, the defining equations 
simplify to
\begin{equation}
\begin{gathered}
a_0=y_3=1,\quad a_1=1/4u^5+1/4u^4+5/4u^3+1/2u^2+2u-3/4\\
b_0=b_1=-1/4u^4-3/4u^2-1/4u-3/4,\\
c_1=-1/4u^5-3/4u^3-1/4u^2-3/4u,\\
c_0=1/2u^5+9/4u^3+1/4u^2+7/2u-1/4,\\
y_2=-8/17u^5-1/34u^4-79/34u^3-3/17u^2-105/34u+26/17,\\
x_3=1/17u^5-1/17u^4+6/17u^3-6/17u^2+14/17u-16/17,\\
x_2=9/34u^5+4/17u^4+37/34u^3+31/34u^2+75/34u+13/17,\\
x_1=8/17u^5+1/34u^4+79/34u^3+3/17u^2+139/34u-9/17,\\
x_0=15/34u^5+1/17u^4+73/34u^3+29/34u^2+125/34u-1/17,\\
u^6 + 5u^4 + 8u^2 - 2u + 1=0.\\













\end{gathered}
\end{equation}
In this case, there are $3$ distinct complex volumes:
\begin{equation}
0.0+1.241598704\dots i,\quad \pm 6.332666642\ldots+1.024134714\dots i
\end{equation}
According to Conjecture~\ref{newconjecture}, $6.33\dots + 1.02\dots i$ 
should (up to rational multiples of $\pi^2i$) be an integral linear 
combination of complex volumes of hyperbolic manifolds. 
Using e.g.~Snap~\cite{snapprogram}, one checks that the complex volume of 
the manifold $m034$ is given by
\begin{equation}
3.166333321\ldots + 2.157001424\dots i,
\end{equation}
and we have
\begin{equation}
6.332666642\ldots+1.024134714\dots i=2\Vol_\C(m034)
-\frac{1}{3}\pi^2i\in\C/4\pi^2i\Z.
\end{equation}

\end{example}


\begin{example}
[The figure $8$ knot complement]
\lbl{ex.41}
Let $K$ be the $3$-cycle in Figure~\ref{fig8triangulation}. Then $M=M(K)$ 
is the figure $8$ knot complement, and $H^2(K;\Z/2\Z)=H^2(M,\partial M;
\Z/2\Z)=\Z/2\Z$.

\begin{figure}[ht]
$$
\psdraw{SLrepFigures.15}{1.7in} \qquad
\psdraw{SLrepFigures.16}{1.7in} 
$$
\caption{A $3$-cycle structure on the figure $8$ knot complement and 
Ptolemy coordinates for $n=2$. The signs indicate the non-trivial second 
$\Z/2\Z$ cohomology class.} 
\lbl{fig8triangulation}
\end{figure}

For the trivial obstruction class, the Ptolemy variety for $n=2$ is given by
\begin{equation}
yx+y^2=x^2,\qquad xy+x^2=y^2, 
\end{equation}
and is thus empty since $x$ and $y$ are non-zero. In fact, the only 
boundary-unipotent representations in $\SL(2,\C)$ are reducible, so this is not surprising. 
The non-trivial obstruction 
class can be represented by the cocycle indicated in 
Figure~\ref{fig8triangulation}, and the Ptolemy variety is given by
\begin{equation}
yx-y^2=x^2,\qquad xy-x^2=y^2.
\end{equation}
As in Example~\ref{ex.52}, we may assume $y=1$. Hence, the Ptolemy variety 
detects two (complex conjugate) representations corresponding to the 
solutions to $x^2-x+1=0$. The extended Bloch group elements are
\begin{equation}
-(-\widetilde x,-2\widetilde x)+(\widetilde x,2\widetilde x)
\in\widehat\B(\C)_{\PSL},
\end{equation}
with complex volume
\begin{equation}
\pm 2.029883212\ldots + 0.0i.
\end{equation}
We thus recover the well known complex volume of the figure $8$ knot 
complement.
\end{example}
For $n=3$, similar calculations as those in Example~\ref{ex.52} show that 
the Ptolemy variety detects $3$ zero-dimensional components, but the only one with non-zero volume 
is the one induced by the geometric representation. For $n=4$, lots of new 
complex volumes emerge. For the trivial obstruction class, the non-zero 
complex volumes are
\begin{equation}
\pm 7.327724753\ldots + 0.0i=2\Vol_\C(5^2_1)+\pi^2i/4,
\end{equation}
where the manifold $5^2_1$ is the whitehead link complement.
For the non-trivial obstruction class, the complex volumes are
\begin{equation}
\begin{gathered}
\pm20.29883212\ldots+0.0i=10\Vol_\C(4_1)\in\C/\pi^2i\Z\\
\pm4.260549384\ldots\pm 0.136128165\ldots i\\
\pm3.230859569\ldots+0.0i\\
\pm8.355502146\ldots + 2.428571615\ldots i=\Vol_\C(-9^3_{15})+2\pi^2i/3\\
\pm3.276320849\ldots + 9.908433886\ldots i.
\end{gathered}
\end{equation}

\begin{example}[$S^1\times S^2$]
\lbl{ex.S1S2}
Figure~\ref{S1S2triangulation} shows a triangulation of $M=S^1\times S^2$ 
taken from the Regina census~\cite{Regina}. Since $\pi_1(S^1\times S^2)=\Z$, 
all representations in $\PSL(2,\C)$ lift to $\SL(2,\C)$, so we expect the 
Ptolemy variety for the non-trivial class in $H^2(M;\Z/2\Z)$ to be zero. 
This class is represented by the cocycle shown in 
Figure~\ref{S1S2triangulation}, and the Ptolemy variety is given by
\begin{equation}
-zx+x^2=y^2,\qquad x^2+zx=y^2,
\end{equation}
which indeed has no solutions in $\C^*$. For the trivial cohomology class, 
all signs are positive, and the two equations are equivalent. The extended 
Bloch group element is 
\begin{equation}
(\widetilde z+\widetilde x-2\widetilde y,2\widetilde x-2\widetilde y)
-(\widetilde z+\widetilde x-2\widetilde y,2\widetilde x-2\widetilde y)
=0\in\widehat\B(\C).
\end{equation}
In fact, the extended Bloch group element of a Ptolemy assignment is trivial 
for all $n$, as one easily verifies (the subsimplices cancel out in pairs).

We wish to find out which representations are detected by $P_2(K)$.
A choice of fundamental domain $F$ for $K$ in $L$ determines a presentation 
of $\pi_1(M)$ with a generator for each face pairing of $F$ and a relation 
for each $1$-cell of $K$ (to see this consider the standard presentation 
for the dual triangulation of $K$). Letting $F$ be the fundamental domain 
of $S^1\times S^2$ given by gluing the bottom faces of the two simplices 
together, one easily checks that the generator of $\pi_1(M)=\Z$ is given 
by the self gluing of the first simplex taking the face opposite the third 
vertex to the face opposite the zeroth. For $\alpha\in\SL(2,\C)$, the 
representation given by taking the generator to $\alpha$ has a decoration 
as in Figure~\ref{S1S2triangulation}. For $A=\Mat{a}{b}{c}{d}$, let 
$c(A)=c$, and note that $\det(e_1,Ae_1)=c(A)$. Letting $x$, $y$ and $z$ 
denote the Ptolemy coordinates, we have
\begin{equation} 
x=c(\alpha),\quad y=c(\alpha^2)=x\Tr(\alpha),\quad 
z=c(\alpha^3)=x(\Tr(\alpha)^2-1),
\end{equation}
and it follows that the Ptolemy variety detects all representations except 
those where $\Tr(\alpha)=\pm 1$.

\begin{figure}[ht]
$$
\psdraw{SLrepFigures.17}{2.15in} \qquad
\psdraw{SLrepFigures.18}{2.15in} 
$$
\caption{A triangulation of $S^1\times S^2$. Both simplices have self 
gluings.}
\lbl{S1S2triangulation}
\end{figure}
\end{example}

\begin{remark}
When $n=2$, examples of Conjecture~\ref{newconjecture} are abundant. E.g.~for the $10_{155}$ knot complement ($10$ simplices), the volumes of the representations detected by the Ptolemy variety are (numerically)
\begin{equation}
\Vol(m032(6,1)),\quad 2\Vol(4_1),\quad 3\Vol(10_{155})-4\Vol(v3461),\quad \Vol(10_{155}).
\end{equation}
\end{remark}

\begin{remark} For the hyperbolic census manifolds, most of the components of the Ptolemy varieties (after fixing the action by diagonal matrices) tend to be zero-dimensional. By a result of Menal-Ferrer and Porti~\cite{FerrerPorti}, the composition of the geometric representation with $\phi_n$ is isolated among boundary-unipotent $p\SL(n,\C)$-representations. Higher dimensional components also occur (rarely for $n=2$, quite often for $n>2$), but as mentioned earlier, the complex volume is constant on components. 
\end{remark}

\begin{remark} 
If the face pairings do not respect the vertex orderings, one can still 
define a Ptolemy variety by introducing more signs. See~Garoufalidis--Goerner--Zickert~\cite{GaroufalidisGoernerZickert} for details.
\end{remark}




\section{The irreducible representations of $\SL(2,\C)$}
\lbl{sec.adjoint}

Let $\phi_n\colon\SL(2,\C)\to\SL(n,\C)$ denote the canonical irreducible 
representation. It is induced by the Lie algebra homomorphism 
$\mathfrak{sl}(2,\C)\to\mathfrak{sl}(n,\C)$ given by
\begin{equation}
\left[\begin{smallmatrix}0&1\\0&0\end{smallmatrix}\right]
\mapsto\diag^+(n-1,\dots,1),\quad 
\left[\begin{smallmatrix}0&0\\1&0\end{smallmatrix}\right]
\mapsto\diag^-(1,\dots,n-1),\quad \left[\begin{smallmatrix}1&0\\0&-1
\end{smallmatrix}\right]\mapsto\diag(n-1,n-3,\dots,-n+1),
\end{equation}
where $\diag^+(v)$ and $\diag^-(v)$ denote matrices whose first upper 
(resp.~lower) diagonal is $v$ and all other entries are zero. One has
\begin{align}
\phi_n\left(\left[\begin{smallmatrix}0&-a^{-1}\\a&0\end{smallmatrix}
\right]\right)&=q(a^{n-1},-a^{n-3},\dots,(-1)^{n-1}a^{-(n-1)})\lbl{phinlong}\\
\phi_n\left(\left[\begin{smallmatrix}1&x\\0&1\end{smallmatrix}\right]\right)&
=\pi_{n-1}(x,\dots ,x)\pi_{n-2}(x,\dots,x)\cdots\pi_1(x)\lbl{phinshort}.
\end{align}

\begin{proposition}
\lbl{adjointPtolemy} 
Let $c$ be a Ptolemy assignment on $\Delta_2^3$, and let $\tau$ denote the 
corresponding cocycle. The assignment 
\begin{equation}
\phi_n(c)\colon\dot\Delta^3_n(\Z)\to \C^*,\qquad t\mapsto\phi_n(c)_t
=\prod_{i<j}c_{ij}^{t_it_j}
\end{equation}
is a Ptolemy assignment on $\Delta_n^3$. If $c$ is a $\PSL(2,\C)$-Ptolemy 
assignment with obstruction cocycle $\sigma$, $\phi_n(c)$ is a 
$p\SL(n,\C)$-Ptolemy assignment with obstruction cocycle $\sigma$. Moreover, 
$\phi_n(c)$ is the Ptolemy assignment corresponding to $\phi_n(\tau)$.
\end{proposition}

\begin{proof}
Let $\alpha=(a_0,\dots,a_3)\in \Delta^3_{n-2}(\Z)$. Letting 
$k_\alpha=\prod_{i<j}c_{ij}^{a_ia_j}$, and $l_\alpha=\prod_{i<j}c_{ij}^{a_i+a_j}$, we have
\begin{equation}
\phi_n(c)_{\alpha_{03}}\phi_n(c)_{\alpha_{12}}=k_\alpha^2l_\alpha c_{03}c_{12},\quad 
\phi_n(c)_{\alpha_{01}}\phi_n(c)_{\alpha_{23}}=k_\alpha^2l_\alpha c_{01}c_{23},\quad 
\phi_n(c)_{\alpha_{02}}\phi_n(c)_{\alpha_{13}}=k_\alpha^2l_\alpha c_{02}c_{13}.
\end{equation}
Hence, the appropriate Ptolemy relations are satisfied, proving the first 
two statements. The long and short edges of the cocycle corresponding to 
$\phi_n(c)$ are given by \eqref{qij} and \eqref{alphaijk}, and we must 
prove that these agree with those of $\phi_n(\tau)$. For the long edges, 
this follows immediately from \eqref{phinlong}. For the short edges, an 
easy computation shows that all the diamond coordinates of a face are equal, 
and equal to the corresponding diamond coordinate of $c$. For example, the 
type $1$ diamond coordinate on face $3$ whose left vertex is 
$t=(t_0,t_1,t_2,0)$ is given by
\begin{equation}
\begin{aligned}
\frac{\phi_n(c)_{t+(0,-1,1,0)}\phi_n(c)_{t+(-1,1,0,0)}}{\phi_n(c)_{t}\phi_n(c)_{t+(-1,0,1,0)}}&=\frac{c_{01}^{t_0(t_1-1)}c_{02}^{t_0(t_2+1)}c_{12}^{(t_1-1)(t_2+1)}c_{01}^{(t_0-1)(t_1+1)}c_{02}^{(t_0-1)t_2}c_{12}^{(t_1+1)t_2}}{c_{01}^{t_0t_1}c_{02}^{t_0t_2}c_{12}^{t_1t_2}c_{01}^{(t_0-1)t_1}c_{02}^{(t_0-1)(t_2+1)}c_{12}^{t_1(t_2+1)}}\\&=\frac{c_{02}}{c_{01}c_{12}},
\end{aligned}
\end{equation}
which is a diamond coordinate for $c$. By~\eqref{phinshort} the short edges 
thus agree with those of $\phi_n(\tau)$, proving the result.  
\end{proof}

\begin{corollary}\label{adjointPtolemycor} If a representation $\rho\colon\pi_1(M)\to\PSL(2,\C)$ is detected by $P_2^\sigma(K)$ then $\phi_{2k+1}\circ\rho$ is detected by $P_{2k+1}(K)$ and $\phi_{2k}\circ\rho$ is detected by $P_{2k}^\sigma(K)$.\qed
\end{corollary}

\begin{theorem}
Let $\rho$ be a boundary-unipotent representation in $\SL(2,\C)$ or 
$\PSL(2,\C)$. The extended Bloch group element of $\phi_n\circ \rho$ 
is $\binom{n+1}{3}$ times that of $\rho$. In fact, the shapes of all subsimplices are equal.
\end{theorem}

\begin{proof}
By refining the triangulation if necessary, we may represent $\rho$ by a 
Ptolemy assignment $c$ on $K$. Then $\phi=\phi_n(c)$ is a Ptolemy assignment 
representing $\phi_n\circ \rho$, and the extended Bloch group element of 
$\phi_n\circ\rho$ is given by
\begin{equation}
[\phi_n(\rho)]=\sum_i\epsilon_i\sum_{\alpha\in \Delta^3_{n-2}(\Z)}
(\widetilde{\phi}^i_{\alpha_{03}}+\widetilde{\phi}^i_{\alpha_{12}}
-\widetilde{\phi}^i_{\alpha_{02}}-\widetilde{\phi}^i_{\alpha_{13}},
\widetilde{\phi}^i_{\alpha_{01}}+\widetilde{\phi}^i_{\alpha_{23}}
-\widetilde{\phi}^i_{\alpha_{02}}-\widetilde{\phi}^i_{\alpha_{13}}).
\end{equation} 
By Proposition~\ref{independenceoflog}, we may choose the logarithms 
independently as long as we use the same logarithm for identified points. 
Defining $\widetilde{\phi}^i_t=\sum_{j<k}t_jt_k\widetilde c^i_{jk}$,
we see that
\begin{equation}
(\widetilde{\phi}^i_{\alpha_{03}}+\widetilde{\phi}^i_{\alpha_{12}}
-\widetilde{\phi}^i_{\alpha_{02}}-\widetilde{\phi}^i_{\alpha_{13}},
\widetilde{\phi}^i_{\alpha_{01}}+\widetilde{\phi}^i_{\alpha_{23}}
-\widetilde{\phi}^i_{\alpha_{02}}-\widetilde{\phi}^i_{\alpha_{13}})
=(\widetilde c_{03}+\widetilde c_{12}-\widetilde c_{02}-\widetilde c_{13},
\widetilde c_{01}+\widetilde c_{23}-\widetilde c_{02}-\widetilde c_{13}),
\end{equation}
which means that the flattenings assigned to each subsimplex of $\Delta^i_n$ 
are equal. By Lemma~\ref{numberofsubsimplices}, 
$\Norm{\Delta^3_{n-2}(\Z)}=\binom{n+1}{3}$, and the result follows.
\end{proof}

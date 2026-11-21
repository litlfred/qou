---
doc_id: arxiv-1304.3481v1
doc_title: "Quadruply-Graded Colored Homology of Knots"
section_id: sec-004-5-colored-homfly-homology-for-torus-knots
section_title: "Colored HOMFLY homology for torus knots"
section_number: 5
pages: 47-55
source_pdf: 1304.3481v1.pdf
source_sha256: d0840f2775c0f761
toc_source: outline
text_source: latex
latex_prose_ratio: 0.961
latex_coverage_ratio: 0.966
doc_brief: "Quadruply-Graded Colored Homology of Knots — We conjecture the existence of four independent gradings in the colored HOMFLY homology."
---
\label{sec:algmodel}

In this part we describe various algebraic and geometric approaches to the colored homology of
torus knots.


\subsection{Stable HOMFLY homology of torus knots}
\label{sec:torus}


We will be interested in the stable limit of the colored HOMFLY polynomials of $(n,m)$ torus knots at $m\to\infty$.
Using e.g. \cite[eq. (5.4)]{stevan}, one can prove the following result.

\begin{proposition}
Let $\kappa(\mu)=\sum_{(i,j)\in \mu}(i-j).$
Define
$$P_{st}^{\lambda}(T({m,n})) := q^{-mn\kappa(\lambda)+\frac{m}{n}\kappa(n\lambda)}a^{-\frac{m(n-1)|\lambda|}{2}}P^{\lambda}(T({m,n})).$$
Then
\begin{equation}
\label{stable poly}
\lim_{m\to\infty}P_{st}^{\lambda}(T({m,n}))=P^{n\lambda}(a,q).
\end{equation}
\end{proposition}
As a corollary, one can compute the stable colored invariants of torus knots using the hook formula (\ref{plambda}).
One can easily check that the unreduced stable polynomial $P^{\lambda}(T(n,\infty))=P^{n\lambda}(\unknot ; a,q)$ is
a series in $(-a)$ and $q$ with nonnegative coefficients.


Let us compute the stable polynomial of the $(2,\infty)$ torus knot colored by the Young diagram $\lambda=(2,1)$.
By (\ref{stable poly}) it is the same as the polynomial of the unknot colored by the Young diagram $2\lambda=(4,2)$.
The hook formula (\ref{plambda}) gives the following answer (up to an overall scaling):
$$P^{2\lambda}(\unknot)=\frac{(1-aq^{-1})(1-a)^2(1-aq)(1-aq^2)(1-aq^{3})}{(1-q)^2(1-q^2)^2(1-q^4)(1-q^5)}.$$
Note that
$$P^{\lambda}(\unknot)=\frac{(1-aq^{-1})(1-a)(1-aq)}{(1-q)^2(1-q^3)}.$$
The reduced polynomial
$P^{red}_{\lambda}(T(2,\infty))=\frac{P^{\lambda}(T(2,\infty))}{P^{\lambda}(a,q)}$ has positive and negative terms
in the $q$-expansion of the coefficient at $a^{0}$:
$$\frac{(1-q^3)}{(1-q^2)^2(1-q^4)(1-q^5)}=1 + 2 q^2 - q^3 + 4 q^4 - q^5 + 6 q^6 - 2 q^7 + 8 q^8 - 2 q^9 +
 11 q^{10}+\dots$$




We would like to use the equation (\ref{stable poly}) as a definition of the stable colored homology of $(n,\infty)$ torus knot.
More precisely, we conjecture that as a vector space $\CH^{\lambda}(n,\infty)$ is isomorphic to $\CH^{n\lambda}(\unknot)$, moreover, the $a,q,t_{c}$ gradings on these spaces match. This suggests that $\CH^{\lambda}(n,\infty)$
is a free supercommutative algebra with bosonic and fermionic generators labelled by the boxes of $n\lambda$.


Let $\lambda$ be an $R \times S$ rectangular Young diagram, and let $K=T(p,q)$ be a $(p,q)$-torus knot.
We assume that  $\CH^{\lambda}(K)$ is a quotient of $\CH^{\lambda}(T(p,\infty))$, the latter space being
$(a,q,t_{c})$-graded isomorphic to the $p\lambda$-colored homology of the unknot. Under this assumption,
the multiplicative generators of $\CH^{\lambda}(K)$ coincide with the ones of $\CH^{\lambda}(T(p,\infty))$,
while some additional relations are imposed.  Let us determine the gradings of these generators.
The diagram $p\lambda$ is a $R\times pS$ rectangle, which can be naturally divided into $p$ different $R\times S$ rectangles.
Let us denote by $u_{ij}^{(n)}$ a bosonic generator in $n$-th rectangle {\em from the right} at box $(i,j)$,
and by   $\xi_{ij}^{(n)}$ a fermionic generator in $n$-th rectangle {\em from the left} at box $(i,j)$, as in Figures \ref{nrect1} and \ref{nrect2} .
\begin{figure}
\begin{tikzpicture}
\draw (0,0)--(0,3)--(12,3)--(12,0)--(0,0);
\draw (4,0)--(4,3);
\draw (8,0)--(8,3);
\draw (2,1) node {$\bullet$};
\draw [<->,>=stealth] (0,1)--(1.9,1);
\draw [<->,>=stealth] (2,0)--(2,0.9);
\draw [<->,>=stealth] (4,-0.2)--(12,-0.2);
\draw (1,1.2) node {$i$};
\draw (2.2,0.5) node {$j$};
\draw (8,-0.5) node {$(n-1)S$};
\end{tikzpicture}
\caption{Generators $u_{ij}^{(n)}$}
\label{nrect1}
\end{figure}
\begin{figure}
\begin{tikzpicture}
\draw (0,0)--(0,3)--(12,3)--(12,0)--(0,0);
\draw (4,0)--(4,3);
\draw (8,0)--(8,3);
\draw (10,1) node {$\bullet$};
\draw [<->,>=stealth] (8,1)--(9.9,1);
\draw [<->,>=stealth] (10,0)--(10,0.9);
\draw [<->,>=stealth] (0,-0.2)--(8,-0.2);
\draw (9,1.2) node {$i$};
\draw (10.2,0.5) node {$j$};
\draw (4,-0.5) node {$(n-1)S$};
\end{tikzpicture}
\caption{Generators $\xi_{ij}^{(n)}$}
\label{nrect2}
\end{figure}
Their gradings are given by the following equations:
\begin{eqnarray*}
(a,q)\left[u_{ij}^{(n)}\right]=(0,2(nS-i+R-j+1)),\\
(t_c,t_r)\left[u_{ij}^{(n)}\right]=2(nS-i),2((n-1)R+j-1)),\\
(a,q)\left[\xi_{ij}^{(n)}\right]=(2,2((n-1)S+i-j)),\\
(t_c,t_r)\left[\xi_{ij}^{(n)}\right]=(2((n-1)S+i)-1,2((n-1)R+j)-1).
\end{eqnarray*}
Note that $t_{r}$ is constant in rows and $t_{c}$ is constant in columns. This explains the notations
$t_{r}$ and $t_{c}$. Using the equation $Q=\frac{q+t_r-t_c}{R}$, we get
$$Q\left[u_{ij}^{(n)}\right]=2n,\quad Q\left[\xi_{ij}^{(n)}\right]=2n-2.$$

It is important to note that these elements generate {\em unreduced} stable homology. To work with the reduced homology,
one should consider $u_{ij}^{(n)},\xi_{ij}^{(n)}$ for $n\ge 2$ since the subalgebra generated by  $u_{ij}^{(1)},\xi_{ij}^{(1)}$
coincides with the unreduced homology of the unknot.

There exists a map $M_{\lambda} :\CH^{\lambda}(T(p,\infty))\to \CH^{\lambda^t}(T(p,\infty))$
such that for any $w$ we have
\begin{equation}
\label{gradings of M}
(Q,t_{c},t_{r})[M_{\lambda} (w)]=(Q,t_{r},t_{c})[w].
\end{equation}
The  map $M_{\lambda}$ is defined by the equations
$$M_{\lambda} \left(u_{ij}^{(n)}\right):=u_{R-j+1,S-i+1}^{(n)},\quad M_{\lambda} \left(\xi_{ij}^{(n)}\right):=\xi_{ji}^{(n)}.$$
One can check that it satisfies (\ref{gradings of M}).
The refined exponential growth conjecture also holds for the stable homology $\CH^{\lambda}(T(p,\infty)):$
\be
\label{stable exp growth}
\CP^{R\times S}(T(p,\infty),a,Q,t_{r})=\left(\CP^{\Lambda^R}(T(p,\infty),a,Q,t_{r})\right)^{S}.
\ee
The exponential growth conjecture follows from the fact that $t_{r}$ is constant in rows:
if we consider generators in $(a,Q,t_{r})$ gradings, then we get $S$ copies of $\CH^{\Lambda^R}(T(p,\infty))$ in the same gradings, which in turn implies (\ref{stable exp growth}).

Let us recall that in (\ref{Llambda}) we conjectured that the self-duality map $\Phi$ can be obtained as follows:
there exists a ``D0-brane'' operator $L_{\lambda}:\CH^{\lambda}(K)\to\CH^{\lambda}(K)$
such that
\begin{equation}
(a,q,Q,t_r,t_c)[L_{\lambda}]=(0,R+S,2,R,S),\quad \Phi_{\lambda}(x)=L_{\lambda}^{-Q(x)}.
\end{equation}
We conjecture that for torus knots colored by $\lambda=R\times S$ rectangular diagrams
such operator $L_{\lambda}$ coincides with the multiplication operator by $u_{S,1}^{(2)}.$ One can check that it has
the prescribed degrees. Moreover, the mirror map $M_{\lambda}$ is chosen in such a way that $M_{\lambda} (u_{S,1}^{(2)})=u_{R,1}^{(2)}$,
and so for the rectangular diagrams we have an equation
$$M_{\lambda} \circ L_{\lambda}=L_{\lambda^t}\circ M_{\lambda}, $$
and therefore
$$M_{\lambda} \circ \Phi_{\lambda} = \Phi_{\lambda^t}\circ M_{\lambda} .$$
This is indeed the required compatibility relation between $M$ and $\Phi$.


Now let us describe the action of colored differentials
in this algebraic model.
The positive row-removing differentials are given by the equation
$$d^{+}_{R\times S\to k\times S}\left(\xi_{i,j}^{(n)}\right)=u_{S+1-i,j-k}^{(n)}, j>k.$$
The positive column-removing differentials are given by the equation
$$d^{+}_{R\times S\to R\times l}\left(\xi_{i,j}^{(n)}\right)=u_{S+l+1-i,j}^{(n)}, i>l.$$
The negative row-removing differentials are given by the equation
$$d^{-}_{R\times S\to k\times S}\left(\xi_{1,k+1}^{(2)}\right)=1.$$
The negative column-removing differentials are given by the equation
$$d^{-}_{R\times S\to R\times l}\left(\xi_{l+1,1}^{(2)}\right)=1.$$
The differentials vanish on all other generators of the colored HOMFLY homology.
One can check that the degrees of these differentials agree with the expected ones.

The duality between positive and negative differentials is party explained by the identities
$$d^{+}_{R\times S\to k\times S}(\xi_{1,k+1}^{(2)})=u_{S,1}^{(2)},\ d^{-}_{R\times S\to k\times S}(\xi_{1,k+1}^{(2)})=1,$$
$$d^{+}_{R\times S\to R\times l}(\xi_{l+1,1}^{(2)})=u_{S,1}^{(2)},\ d^{-}_{R\times S\to R\times l}(\xi_{l+1,1}^{(2)})=1.$$
Finally, we describe the action of the universal differentials. As a model example, consider the unreduced $S^2$ homology of the unknot. It has two even generators $u_1,u_2$ and two odd generators $\xi_1,\xi_2$.
We define the universal differential on the bottom row by the formula
$$d(f(u_1,u_2))=u_2\frac{f(u_1,u_2)-f(-u_1,u_2)}{u_1}.$$
In other words,
$$d(u_1^{a}u_2^{b})=\begin{cases}
2u_1^{a-1}u_2^{b+1},& {\rm if}\ a\ {\rm is\ odd},\\
0,& {\rm if}\ a\ {\rm is\ even}.\\
\end{cases}$$
It is clear that $d^2=0$ and the homology of $d$ is isomorphic to $\mathbb{C}[u_1^2]$, as predicted by the grading restrictions in Section \ref{sec:gradings}. Similarly, on higher levels we define the differential by the equation
$d(\xi_1)=\xi_2$, so $d(\xi_1\wedge \xi_2)=0$. The total homology is a free algebra generated by $u_1^2$ and $\xi_1\xi_2$.

In general, we can always split variables into pairs, define a universal differential in each pair as above and extend it to the whole algebra by the Leibnitz rule. For example, in stable $S^2$ homology of the $(2,\infty)$ torus knot we have two even generators $u_3,u_4$ and two odd generators $\xi_3,\xi_4$. As in the above example, one can define a universal differential by the equations
$$d(u_3^{a}u_4^{b})=\begin{cases}
2u_3^{a-1}u_4^{b+1},& {\rm if}\ a\ {\rm is\ odd},\\
0,& {\rm if}\ a\ {\rm is\ even},\\
\end{cases}
\quad d(\xi_3)=\xi_4.
$$
It clearly agrees with the description of the universal differential for the trefoil in Section \ref{sec:trefoil}.


\subsection{Differential forms}
\label{sec:symtorusforms}

\begin{definition}
The {\em unreduced} moduli space $\overline{\CM}_{p,q}(r)$ is defined in the affine space
with the coordinates $u_1, \ldots, u_{rp}; v_1,\ldots,v_{rq}$ by the equation
\begin{equation}
\label{equv}
(1+u_1z+u_2z^2+\ldots+u_{rp}z^{rp})^{q}=(1+v_1z+v_2z^2+\ldots+v_{rq}z^{rq})^{p}.
\end{equation}
which should hold at every coefficient of its expansion in powers of  $z$.
\end{definition}

The space $\overline{\CM}_{p,q}(r)$ can be also defined in the affine space
with the coordinates $u_1,\ldots,u_{rp}$ by the coefficients in the $z$-expansion of the equation
$$(1+u_1z+u_2z^2+\ldots+u_{rp}z^{rp})^{q/p},$$
starting from $(qr+1)$-st. Indeed, one can rewrite the equation (\ref{equv}) as
$$(1+u_1z+u_2z^2+\ldots+u_{pr}z^{pr})^{q/p}=(1+v_1z+v_2z^2+\ldots+v_{qr}z^{qr}).$$
This will express $v_i$ through $u_j$. The dimension of $\overline{\CM}_{p,q}(r)$ equals to $r$.
Indeed, let us forget the scheme structure and study the underlying subset of the affine space.
One has $U(z)^{q}=V(z)^{p}$ for coprime $p$ and $q$ iff there exists a polynomial $F(z)$ such that
$U(z)=F(z)^{p}, V(z)=F(z)^{q}$. Since $F(z)$ starts from 1 and has degree $r$, we have $r$ parameters at our disposal.

\begin{conjecture}
\label{symmetric torus unreduced}
The {\em unreduced} $S^r$ homology of the $(p,q)$ torus knot is the space of differential forms on $\overline{\CM}_{p,q}(r)$:
\begin{equation}
\overline{\CH}^{S^r} (T(p,q)) \; = \; \Omega^{\bullet}(\overline{\CM}_{p,q}(r)) \,.
\label{HMunreduced}
\end{equation}
\end{conjecture}

As an illustration of this conjecture, let us consider an example of the unknot. We can choose $p=q=1$, so (\ref{equv}) takes the form
$$1+u_1z+u_2z^2+\ldots+u_{r}z^r=1+v_1z+v_2z^2+\ldots+v_{r}z^r$$
Therefore $\overline{\CM}_{p,q}(r)=\Spec\C[u_1,\ldots,u_r],$
and $$\Omega^{\bullet}(\overline{\CM}_{p,q}(r))=\C[u_1,\ldots,u_r,du_1,\ldots,du_r].$$
This agrees with the above description of the unreduced $S^r$-colored triply graded homology of the unknot.

For a more interesting example, consider the $S^2$-colored trefoil knot.
The  generators are $u_2$, $u_3$, $u_4$, and the defining equations are
\be
\label{s2 colored trefoil}
-\frac{3}{16} u_3 (u_2^2 - 4 u_4)=\frac{3}{128} (u_2^4 - 8 u_2 u_3^2 - 8 u_2^2 u_4 + 16 u_4^2)=0,
\ee
$$-\frac{1}{32} u_3 (-3 u_2^3 + 2 u_3^2 + 12 u_2 u_4)=0.$$

\begin{definition}
The {\em reduced} moduli space $\CM_{p,q}(r)$ is defined in the affine space
with the coordinates $u_{r+1},\ldots,u_{pr}; v_{r+1},\ldots,v_{qr}$ by all coefficients in the $z$-expansion of the equation
\begin{equation}
\label{equvred}
(1+u_{r+1}z^{r+1}+u_{r+2}z^{r+2}+\ldots+u_{pr}z^{pr})^{q}=(1+v_{r+1}z+v_2z^2+\ldots+v_{qr}z^{qr})^{p}
\end{equation}
\end{definition}

One can check that $\CM_{p,q}(r)$ defines a single point 0, so it is zero-dimensional.
We propose the following

\begin{conjecture}
\label{symmetric torus reduced}
The {\em reduced} $S^r$ homology of the $(p,q)$ torus knot is the space of differential forms on $\CM_{p,q}(r)$:
\begin{equation}
\CH^{S^r} (T(p,q)) \; = \; \Omega^{\bullet}(\CM_{p,q}(r)) \,.
\label{HMreduced}
\end{equation}
\end{conjecture}

For $r=1$ this conjecture is equivalent to the main conjecture of \cite{GORS}, since by the results of \cite{Gdaha} the right hand side of (\ref{HMreduced}) can be identified with a certain isotypic component of the finite-dimensional representation of rational Cherednik algebra with parameter $p/q$.
Moreover, it follows from \cite{GORS} for $r=1$ and from \cite{EGL} for general $r$ that the $(a,q)$-character
of $\Omega^{*}(\overline{\CM}_{p,q}(r))$ is equal to the unreduced $S^r$-colored HOMFLY polynomial of the $(p,q)$ torus knot.
One can also check (\cite{EGL}) that the $(a,q)$-character of $\Omega^{*}(\CM_{p,q}(r))$ is equal to the reduced $S^r$-colored HOMFLY polynomial
of the same knot. 

Let us describe the gradings on the space $\Omega^{*}(\CM_{p,q}(r))$.
The $a$-grading is defined by the degree of a differential form, so that $a(u_i)=0,\ a(du_i)=2.$ Furthermore, we define the $(q,t_r,t_c)$ gradings by the formula
\be
\label{deg ui for symmetric}
(q,t_c,t_r)[u_i]=\left(2i,2i-2,2\left\lfloor\frac{i-1}{r}\right\rfloor\right),
\ee
$$(q,t_r,t_c)[du_i]=\left(2i-2,2i-1,2\left\lfloor\frac{i-1}{r}\right\rfloor+1\right).$$
It is easy to check that the defining equations of $\CM_{p,q}(r)$ are homogeneous in $q$-grading and not homogeneous in $t$-gradings. Therefore, strictly speaking, on $\Omega^{*}(\CM_{p,q}(r))$ we get  $(a,q)$ bigrading and a pair of filtrations $(t_r,t_c)$.

For example, in the uncolored case the reduced homology of the trefoil knot has only one bosonic generator $u_2$,
and the defining equation for $\CM_{2,3} (1)$ reads as
\be
u_2^2=0
\label{tref3876}
\ee
Similarly, for the $(3,4)$ torus knot the reduced uncolored homology has two bosonic generators $u_2$ and $u_3$,
with the following defining equations for $\CM_{3,4} (1)$:
\be
u_2u_3=0,\ \frac{2 u_2^3}{9} = u_3^2.
\label{knot34829054}
\ee
Finally, the reduced $S^2$-colored homology of the trefoil knot
has two even generators $u_3$ and $u_4$ and the defining equations can be obtained from (\ref{s2 colored trefoil}) by setting $u_2=0$:
$$u_3u_4=u_4^2=u_3^3=0.$$
Their differentials have the form
$$u_3du_4+u_4du_3=2u_4du_4=3u_3^2du_3=0.$$
Therefore one can check that the monomial basis in $\Omega^{*}(\CM_{2,3} (2))$ is given by
\be
1,~ u_3,~ u_4,~ u_3^2,~ du_3,~ du_4,~ u_3du_3,~ u_3du_4,~ du_3\wedge du_4.
\label{tref456}
\ee
We illustrate this homology with the Figure \ref{s2tref} (compare with the Figures in Section \ref{sec:trefoil}).

\begin{figure}
\begin{tikzpicture}
\draw (0,0) node {$1$};
\draw (6,0) node {$u_3$};
\draw (8,0) node {$u_4$};
\draw (12,0) node {$u_3^2$};
\draw (4,1) node {$du_3$};
\draw (6,1) node {$du_4$};
\draw (10,1) node {$u_3du_3$};
\draw (11.7,1) node {$u_3du_4$};
\draw (10,2) node {$du_3\wedge du_4$};
\draw (0,-1)--(12,-1);
\draw (0,-1.1)--(0,-0.9);
\draw (2,-1.1)--(2,-0.9);
\draw (4,-1.1)--(4,-0.9);
\draw (6,-1.1)--(6,-0.9);
\draw (8,-1.1)--(8,-0.9);
\draw (10,-1.1)--(10,-0.9);
\draw (12,-1.1)--(12,-0.9);
\draw (0,-1.3) node {0};
\draw (2,-1.3) node {2};
\draw (4,-1.3) node {4};
\draw (6,-1.3) node {6};
\draw (8,-1.3) node {8};
\draw (10,-1.3) node {10};
\draw (12,-1.3) node {12};
\draw (11,-1.5) node {$q$};








\end{tikzpicture}
\caption{Algebraic model for the $S^2$ homology of the trefoil.}
\label{s2tref}
\end{figure}

For example, by computing the gradings of the basic elements \eqref{tref456} one finds
the Poincar\'e polynomial of the $S^2$-colored trefoil knot (in the $(a,q,t_r)$ grading):
\be
\CP^{S^2}(3_1)=1+q^6t^2+q^8t^2+q^{12}t^4+a^2q^4t^3+a^2q^6t^3+a^2q^{10}t^5+a^2q^{12}t^5+a^4q^{10}t^6.
\ee
More generally, for the $S^r$-colored reduced homology of the trefoil knot
the $(a,q,t_r)$ gradings of the generators are given by the equations:
$$(a,q,t_r)[u_i]=(0,2i,2),\  (a,q,t_r)[du_i]=(2,2i-2,3).$$
In particular, the monomial $u_{r+1}^{i}\cdot du_{r+1}\wedge du_{r+2}\wedge du_{r+j}$
has grading
$$i(0,2r+2,2)+\sum_{l=1}^{j}(2,2r+2l-2,3)=(2j,2(r+1)i+2jr+j(j-1),2i+3j)$$
and contributes the term
$a^{2j} q^{2(r+1)i+2rj+j(j-1)}t_r^{2i+3j}$ in the Poincar\'e polynomial
\begin{equation}\label{f1}
\CP^{S^r}(3_1)= a^{2r}q^{-r} \sum_{i+j\le r} { a^{2j} q^{2(r+1)i+2rj+j(j-1)}t_r^{2i+3j} \frac{ [r]!}{[i]![j]![r-i-j]!}, }
\end{equation}
obtained from the categorification of the Volume Conjecture and the super-$A$-polynomial \cite{FGS1,FGS2,FGSS}.
Here $[N]!$ is the unbalanced quantum factorial:
\[
[N]!=[N]\cdot [N-1]\cdot \ldots[2]\cdot[1]',
\]
\[
[N]'=\frac{q^N-1}{q-1}=1+q+\ldots +q^{N-1}.
\]
and one can easily verify that (\ref{f1}) satisfies the refined exponential growth conjecture
as well as the rest of the structural properties of section \ref{sec:gradings}.

Finally, let us match the gradings \eqref{deg ui for symmetric} with those in the construction of Section \ref{sec:alggrad}.
We have $R=1, S=r$, so there are  generators $u_{i,1}^{(n)},\xi_{i,1}^{(n)},\ 1\le i\le r$ with gradings
$$(a,q,t_c,t_r)[u_{i,1}^{(n)}]=(0,2+2rn-2i,2rn-2i,2n-2),\ $$
$$(a,q,t_c,t_r)[\xi_{i,1}^{(n)}]=(2,2r(n-1)+2i-2,2r(n-1)+2i-1,2n-1).$$
Indeed, these gradings agree with (\ref{deg ui for symmetric}) if one identifies
$$u_{i,1}^{(n)}=u_{rn+1-i},\ \xi_{i,1}^{(n)}=du_{r(n-1)+i}.$$












\subsection{Differentials for supergroups}

It has been conjectured in \cite[Conj. 3.22]{G} that the differentials $d_{0},d_{\pm n}$ belong to a bigger algebra.
In particular, for the uncolored homology of $(4,5)$ torus knot the following operators were introduced:
$\alpha_2$ of $(a,q,t)$ degree $(-2,-2,-5)$, $\alpha_1$ of $(a,q,t)$ degree $(-2,2,-3)$.
Their introduction was motivated by the observation that the ``usual'' differentials $d_N$ applied to the (unique)
generator with top $a$-degree 6 do not generate uncolored triply graded homology: there are 7 nontrivial differentials
$d_{0},d_{\pm n}$, while there are 9 generators with $a$-degree 4. The extra differentials solve this problem.
We can now identify these operators with the supergroup differentials:
$$\alpha_2=d_{1|2}, \quad \alpha_1=d_{2|1}.$$
In total, for the uncolored (4,5) knot we have 9 nontrivial differentials:
$$d_1=d_{1|0},\ \quad d_{-1}=d_{0|1},$$
$$d_2=d_{2|0},\ \quad d_0=d_{1|1},\ \quad d_{-2}=d_{0|2},$$
$$d_{3}=d_{3|0},\ \quad \alpha_1 =d_{2|1},\ \quad \alpha_2=d_{1|2},\ \quad d_{-3}=d_{0|3}.$$
For a general $(n,m)$ torus knot $(m>n)$ we will have all differentials $d_{a|b}$ with $a+b<n$,  of total number
$$2+3+4+...+n=\frac{n(n+1)}{2}-1=\frac{(n+2)(n-1)}{2}.$$
It has been explained in \cite{GORS} that the differentials are tightly related to the
(conjectural) action of the rational Cherednik algebra $H_{c}$ on the triply graded homology of torus knots.
More precisely, \cite[Definitions 7.2-7.3]{GORS} assign a differential to every $S_n$-equivariant copy
of the standard $(n-1)$-dimensional irreducible representation $V_{n}$ inside $H_c$. These differentials satisfy some nice
properties: for example, if the two copies $\alpha$ and $\beta$ are {\em pure}, then by \cite[Lemma 7.7]{GORS} the corresponding differentials
$d_{\alpha}$ and $d_{\beta}$ anticommute.

The new supergroup differentials can be naturally embedded in this framework.
Namely, recall that $H_{c}$ has generators $x_i, y_j$.
We define $\alpha(m|k)$ to be a copy of  $V_{n}$ spanned by $x_{i}^{m}y_{i}^{k}$,
and
$$d_{m|k}=d_{\alpha(m|k)}.$$
Since this copy is pure in the sense of \cite{GORS}, the corresponding differentials anticommute.
Moreover, one can check that $\alpha(m|k)$ span $\Hom_{S_{n}}(V_{n},H_{c})$, so the supergroup differentials
form a complete collection of differentials for the uncolored torus knot homology. The grading conventions of \cite{GORS}
assure that $d_{m|n}$ have the prescribed gradings.


\subsection{Examples}

We have compared the results of \ref{sec:trefoil} with the algebraic model in (\ref{tref456}). Let us make the similar comparisons for other torus knots in Section \ref{sec:examples}.

The stable reduced $\tableau{2 2}$-colored homology
of $(2,\infty)$ torus knot have 4 even and 4 odd generators
$u_{ij}^{(2)}$ and $\xi_{ij}^{(2)}$ (see Section \ref{sec:torus}). They have the following $(a,q,t_c,t_r)$-degrees:
$$\deg[u_{11}^{(2)}]=(0,10,6,4),\ \deg[u_{12}^{(2)}]=(0,8,6,6),$$
$$\deg[u_{21}^{(2)}]=(0,8,4,4),\ \deg[u_{22}^{(2)}]=(0,6,4,6),$$
$$\deg[\xi_{11}^{(2)}]=(2,4,5,5),\ \deg[\xi_{12}^{(2)}]=(2,2,5,7),$$
$$\deg[\xi_{21}^{(2)}]=(2,6,7,5),\ \deg[\xi_{22}^{(2)}]=(2,4,7,7).$$
As explained in Section \ref{sec:torus},  $Q\left[u_{ij}^{(2)}\right]=4$ and $Q\left[\xi_{ij}^{(2)}\right]=2$.
For example, the ``bottom row'' of the homology (with appropriate shift of gradings) is 16-dimensional and has monomial basis
$$1,~u_{21}^{(2)},~\left(u_{21}^{(2)}\right)^2,~\left(u_{21}^{(2)}\right)^3,~\left(u_{21}^{(2)}\right)^4,$$
$$u_{11}^{(2)},~u_{11}^{(2)}u_{21}^{(2)},~u_{11}^{(2)}~\left(u_{21}^{(2)}\right)^2,$$
$$u_{12}^{(2)},~u_{12}^{(2)}u_{21}^{(2)},~u_{12}^{(2)}~\left(u_{21}^{(2)}\right)^2,$$
$$u_{22}^{(2)},~u_{22}^{(2)}u_{21}^{(2)},~u_{22}^{(2)}~\left(u_{21}^{(2)}\right)^2,$$
$$\left(u_{22}^{(2)}\right)^2,\left(u_{11}^{(2)}\right)^2.$$
The self-symmetry map $\Phi$ reflects first four sets of monomials in the vertical axis, and preserved two remaining monomials.

The stable reduced $\tableau{2 2 2}$-colored homology
of $(2,\infty)$ torus knot have 6 even and 6 odd generators. They have the following $(a,q,t_c,t_r)$-degrees:
$$\deg[u_{11}^{(2)}]=(0,12,6,6),\ \deg[u_{12}^{(2)}]=(0,10,6,8),$$
$$\deg[u_{13}^{(2)}]=(0,8,6,10),\ \deg[u_{21}^{(2)}]=(0,10,4,6),$$
$$\deg[u_{22}^{(2)}]=(0,8,4,8),\ \deg[u_{23}^{(2)}]=(0,6,4,10),$$
$$\deg[\xi_{11}^{(2)}]=(2,4,5,7),\ \deg[\xi_{12}^{(2)}]=(2,2,5,9),$$
$$\deg[\xi_{13}^{(2)}]=(2,0,5,11),\ \deg[\xi_{21}^{(2)}]=(2,6,7,7).$$
$$\deg[\xi_{22}^{(2)}]=(2,4,7,9),\ \deg[\xi_{23}^{(2)}]=(2,2,7,11).$$
Indeed,  $Q\left[u_{ij}^{(2)}\right]=4$ and $Q\left[\xi_{ij}^{(2)}\right]=2$.

Finally, consider the $S^2$-colored $(3,4)$ torus knot.
In the notations of Section \ref{sec:symtorusforms}, we have
4 generators $u_3,u_4,u_5,u_6$ of $(a,q,t_c,t_r)$ gradings
$$\deg u_3=(0,6,4,2),\ \deg u_4=(0,8,6,2),$$
$$\deg u_5=(0,10,8,4),\ \deg u_6=(0,12,10,4).$$
Note that in the notations of Section \ref{sec:torus},
one would have
$$u_3=u_{21}^{(2)},\ u_4=u_{11}^{(2)},\ u_5=u_{21}^{(3)},\ u_6=u_{11}^{(3)},$$
and the grading conventions agree.
The defining relations have the form
$$u_3^3 - 9 u_4 u_5 - 9 u_3 u_6=2 u_3^2 u_4 - 3 (u_5^2 + 2 u_4 u_6)=u_3 u_4^2 + u_3^2 u_5 - 3 u_5 u_6=0,$$ $$5 u_3^4 - 12 u_4^3 - 72 u_3 u_4 u_5 - 36 u_3^2 u_6 + 54 u_6^2=5 u_3^3 u_4 - 9 u_4^2 u_5 - 9 u_3 (u_5^2 + 2 u_4 u_6) =0.$$
One can check that the monomial basis on the ``bottom row'' is given by the following 25 monomials:
$$1,\ u_3,\ u_3^2,\ u_3^3,\ u_3^4,\ u_3^5,\ u_3^6,$$
$$u_4,\ u_4u_3,\ u_4u_3^2,\ u_4u_3^3,\ u_4u_3^4,$$
$$u_5,\ u_5u_3,\ u_5u_3^2,\ u_5u_3^3,$$
$$u_6,\ u_6u_3,\ u_6u_3^2,\ u_6u_3^3,$$
$$u_4^2\, u_4^2u_3,\ u_4^2u_3^2,$$
$$u_5^2, u_4^3.$$
The self-symmetry map $\Phi$ reflects first five sets of monomials in the vertical axis, and preserved two remaining monomials.

---
doc_id: arxiv-1304.0323v3
doc_title: "SYMMETRIC QUIVER HECKE ALGEBRAS"
section_id: sec-014-33-exactness-of-the-functor-f
section_title: "Exactness of the functor F"
section_number: 3.3
pages: 33-36
source_pdf: 1304.0323v3.pdf
source_sha256: 92e2b9dc876e1a52
doc_brief: "SYMMETRIC QUIVER HECKE ALGEBRAS — Let J be a set of pairs consisting of good U ′ q(g)-modules and invertible elements in the base ﬁeld C(q)."
text_source: latex
latex_prose_ratio: 0.958
latex_coverage_ratio: 0.817
---
The following
propositions are  key ingredients in proving our main theorem.
\begin{prop}[{\cite[Corollary 2.9]{Kato12}, \cite[Theorem 4.6]{McNa12}}]
\label{pro:finite global dimension}
If the quiver associated with  $R^J$   is of   finite  type $A,D,E$, then $R^J( \beta )$ has
a finite global dimension  for every $\beta \in \rootl^+$.
\end{prop}



\begin{prop} \label{pro:projectivity}
Let $A\to B$ be a homomorphism of algebras.
We assume the following conditions:
\bna
\item $B$ is a finitely generated projective $A$-module,
\item $\Hom_A(B,A)$ is a projective $B$-module,
\item the global dimension of $B$ is finite.
\ee
Then we have:
\bni
\item any $B$-module projective over $A$ is projective over $B$,
\item any $B$-module flat over $A$ is flat over $B$.
\ee
\end{prop}

\begin{proof}
Since the proof is similar, we give only the proof of (ii).

Let us denote by $\fd M$ the flat dimension of an $A$-module $M$.
Then we have $$\fd(M)\le\fd[B](M)$$ for any $B$-module $M$,
because $\Tor_k^A(N,M)\simeq \Tor_k^B(N\tens_A B,M)$ for any
$A^\opp$-module $N$ and $k\in\Z$ by (a).


By (b),  $\Hom_A(B,A)\tens_AL$ is a flat $B$-module
if $L$ is a flat $A$-module. Indeed,
the functor $X\tens_B\Hom_A(B,A)$ is exact in $X\in\Mod(B^\opp)$
and hence the functor $X\tens_B\Hom_A(B,A)\tens_AL$
is also exact in $X$.

On the other hand, for any $A$-module $L$, the canonical $B$-module homomorphism
$$\Hom_A(B,A)\tens_AL\to \Hom_A(B,L),
\qquad f\tens s\longmapsto (B\ni b\mapsto f(b)s)
$$
is an isomorphism by (a).
Hence we conclude that
$\Hom_A(B,L)$ is a flat $B$-module
for any flat $A$-module $L$.
It immediately implies that
$$\fd[B]\bl\Hom_A(B,L)\br\le\fd (L)\quad\text{for any $A$-module $L$.}$$

Now, let $M$ be a $B$-module.
Then there exists a canonical $B$-module homomorphism
$$\vphi_M\colon M\to \Hom_A(B,M)$$
given by $\vphi_M(x)(b)=bx$.
It is evidently injective.

In order to prove the proposition,
it is enough to show the following statement for any $d\ge0$:
\eq \text{for any $B$-module $M$,
$\fd (M)\le d$ implies $\fd[B](M)\le d$.} \nonumber
\eneq
We shall show it by the descending induction on $d$.
If $d\gg0$, it is a consequence of (c).
Let $M$ be a $B$-module with $\fd(M)\le d$.
We have an exact sequence
$$0\to M\To[\vphi_M] \Hom_A(B,M)\to N\to 0.$$
Then
$$\fd\bl\Hom_A(B,M)\br\le\fd[B]\bl\Hom_A(B,M)\br\le \fd (M)\le d.$$
Hence we have $\fd[A]N\le d+1$,
which implies that $\fd[B](N)\le d+1$
by the induction hypothesis.
Finally, we conclude that
$\fd[B](M)\le d$.
Thus the induction proceeds.
\end{proof}



\begin{theorem} \label{thm:exact}
If the quiver associated with  $R^J$  is of finite type $A, D, E$,
then the functor  $\F_\beta$ is exact  for every $\beta \in
\rootl^+$.
\end{theorem}
\begin{proof}
Let us apply Proposition \ref{pro:projectivity} with $A=\mathbb{P}_{ \beta }^\opp$
and $B= R^J({ \beta })^\opp$.
The conditions (a) and (b) are well-known, and (c) is nothing but Proposition \ref{pro:finite global dimension}. Therefore,
$\bV[{ \beta }]$ is a flat $R^J({ \beta })^\opp$-module
since it is a flat $\mathbb{P}_{ \beta }^\opp$-module.
\end{proof}


\section{Quantum affine algebra $\UA$
and the category $\mathcal C_{J}$}

In this section, we investigate the tensor category structure
of  $\CC_{\slnh}$  ($N\ge2$)  via its
vector representation using the method introduced in the previous section.
 In the case of $\g=\slnh$, we have
$I=\{0,1,\ldots,N-1\}$ and
$$(\al_i,\al_j)=
2\delta_{i,j}-\delta(i\equiv j+1\mod N)-\delta(i\equiv j-1\mod N).$$
The base field $\cor$ is $\C(q)$.



\subsection{R-matrix for $V(\varpi_1)$ of $\UA$}

Let $V\seteq V(\varpi_1)$ be the fundamental representation of $\UA$
of fundamental weight $\varpi_1$.
Then
$V=\soplus_{k=1}^{N}\cor u_k$
with the action
\eqn
e_i(u_k)&=&\delta({k\equiv i+1\hs{-1ex}\mod N}) u_{i}, \\
f_i(u_k)&=&\delta({k\equiv i\hs{-1ex}\mod N}) u_{i+1},\\
K_iu_k&=&q^{\delta(k\equiv i\hs{-1ex}\mod N)-\delta(k\equiv i+1\hs{-1ex}\mod N)}u_k.
\eneqn
Here $u_0=u_N$.

The normalized R-matrix
$$R=\Rnorm_{V(\varpi_1), V(\varpi_1)} \col
V_{z} \otimes V_{z'}
\rightarrow V_{z'} \otimes V_{z}$$
is explicitly given by
\eq&&
\ba{l}
 R((u_i)_z\tens (u_j)_{z'})\\
\hs{5ex}=\bc \dfrac{(1-q^2)z'{}^{\delta(i>j)}z^{\delta(i<j)}}{z'-q^2z}
(u_i)_{z'}\tens (u_j)_z+
 \dfrac{q(z'-z)}{z'-q^2z}(u_j)_{z'}\tens (u_i)_z&\text{if $i\not=j$,}\\
(u_i)_{z'}\tens (u_i)_z&\text{if $i=j$.}
\ec\ea\label{eq: RV}
\eneq
 It shows that $d_{V,V}(z'/z)=z'/z-q^2$.

\smallskip

Let $\mathcal{S}=\{V\}$,
$J=\Z$ and let $X\col J\to \cor^\times$ be the
map given by $X(j)=q^{2j}$.
Then we have
\eq
d_{ij}=\delta(j=i+1)\qtext{for $i,j\in J$.}
\eneq
Then, for $i,j\in J$, we have
$$(\al_i,\al_j)=\begin{cases}-1&\text{if $i-j=\pm1$,}\\
2&\text{if $i=j$,}\\
0&\text{otherwise,}
\end{cases}$$
and
$$Q_{ij}(u,v)=\begin{cases}
\pm(u-v)&\text{if $j=i\pm1$,}\\
0&\text{if $i=j$,}\\
1&\text{otherwise.}
\end{cases}$$
Therefore the corresponding \KLR\ $R=R^J$ is of type $\mathrm{A}_{\infty}$.

\medskip

We take
$$P_J=\soplus_{a\in \Z}\Z\oep_a$$
as the weight lattice with $(\oep_a,\oep_b)=\delta_{a,b}$.
The root lattice $\rtl_J=\soplus_{i\in J}\Z\al_i$
is embedded into $P_J$ by
$\al_i=\oep_i-\oep_{i+1}$. We write as usual $\rtl_J^+$
for $\soplus_{i\in J}\Z_{\ge0}\al_i$.


Note that,  for $\beta\in \rtl^+_J$ and $\nu\in J^\beta$,  we have
$$(\tau_{a+1}\tau_a\tau_{a+1}-\tau_a\tau_{a+1}\tau_{a})e(\nu)
=\begin{cases}\pm e(\nu)&\text{if $\nu_a=\nu_{a+2}=\nu_{a+1}\mp1$,}\\
0&\text{otherwise.}
\end{cases}$$
 Also,  we have
$$P_{ij}(u,v)=(u-v)^{\delta(j=i+1)}c_{i,j}(u,v).$$
 We will choose
$c_{i,j}(u,v)$  satisfying \eqref{cond:cij} later in  Theorem \ref{thm:cij}.
Recall  that
 the functor $$\F \col \soplus_{\beta\in  \rtl^+_J} \Modg(R(\beta))\to
\Mod( \UA) $$
 defined in \eqref{eq:the functor} is exact (Theorem \ref{thm:exact}).

\bigskip

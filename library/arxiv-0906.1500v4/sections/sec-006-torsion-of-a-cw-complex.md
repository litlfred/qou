---
doc_id: arxiv-0906.1500v4
doc_title: "Twisted Alexander invariant and non-abelian Reidemeister torsion for hyperbolic three-manifolds"
section_id: sec-006-torsion-of-a-cw-complex
section_title: "Torsion of a CW-complex"
section_number: null
pages: 4-5
source_pdf: 0906.1500v4.pdf
source_sha256: 9a586f6d134ca47f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.975
latex_coverage_ratio: 0.992
doc_brief: "Twisted Alexander invariant and non-abelian Reidemeister torsion for hyperbolic three-manifolds — We study a computational method of the hyperbolic Reidemeister torsion (also called in the literature"
---
Let $W$ be a finite CW-complex and $(V, \rho)$ be a pair of a vector
space with an inner product over $\FF$ and a homomorphism of $\pi_1(W)$
into $Aut(V)$.  The vector space $V$ turns into a right $\ZZ[\pi_1(W)]$-module denoted $V_{\rho}$ by using the right
action of $\pi_1(W)$ on $V$ given by $v \cdot \gamma = \rho(\gamma)^{-1}(v)$, for
$v \in V$ and $\gamma \in \pi_1(W)$.  The complex of the universal cover 
with integer coefficients $C_*(\ucover{W}; \ZZ)$ also inherits a left
$\ZZ[\pi_1(W)]$-module via the action of $\pi_1(W)$ on
$\ucover{W}$ as the covering group.
We define the $V_\rho$-twisted
chain complex of $W$ to be
\[
C_*(W; V_\rho) = V_{\rho} \otimes_{\ZZ[\pi_1(W)]} C_*(\ucover{W}; \ZZ).
\]
The complex $C_*(W; V_\rho)$ computes the {\it $V_\rho$-twisted homology} of $W$
which we denote as $H_*(W;V_\rho)$.

Let $\left\{e^{i}_1, \ldots, e^{i}_{n_i}\right\}$ be the set of
$i$-dimensional cells of $W$. We lift them to the universal cover and
we choose an arbitrary order and an arbitrary orientation for the
cells $\left\{ {\tilde{e}^{i}_1, \ldots, \tilde{e}^{i}_{n_i}}
\right\}$. If we let $\{\bm{v}_1, \ldots, \bm{v}_m\}$ be an
orthonormal basis of $V$, then we consider the corresponding basis
$$
\cbasis{i} = 
  \left\{ 
    \bm{v}_1 \otimes \tilde{e}^{i}_{1} , 
    \ldots, 
    \bm{v}_m \otimes \tilde{e}^{i}_{1}, 
    \cdots, 
    \bm{v}_1 \otimes \tilde{e}^{i}_{n_i}, 
    \ldots, 
    \bm{v}_m \otimes \tilde{e}^{i}_{n_i}
  \right\}
$$ 
of 
$C_i(W; V_\rho) = V_\rho \otimes_{\ZZ[\pi_1(W)]} C_*(\ucover{W};\ZZ)$. 
We call the basis $\cbasis{*} = \oplus_{i} \cbasis{i}$ 
{\it a geometric basis} of $C_*(W;V_\rho)$.
Now choosing for each $i$ a basis $\hbasis{i}$ of the
$V_\rho$-twisted homology $H_i(W; V_\rho)$, we can compute the torsion
$$\Tor{C_*(W; V_\rho)}{\cbasis{*}}{\hbasis{*}} \in \FF^*.$$

The cells 
$\left\{ \left. 
  \tilde{e}^{i}_j \, 
         \right|\, 
  0 \myleq i \myleq \dim W, 
  1 \myleq j \myleq n_i
\right\}$ are in one--to--one correspondence with the cells of $W$, 
their order and orientation induce an order and 
an orientation for the cells 
$\left\{ \left. 
  \tilde{e}^{i}_j \,
         \right|\, 
  0 \myleq i \myleq \dim W, 
  1 \myleq j \myleq n_i
\right\}$. 
Again, corresponding to these
choices, we get a basis $\cbasis{i}_\IR$ over $\IR$ of $C_i(W; \IR)$.

Choose an \emph{homology orientation} of $W$, which is an orientation
of the real vector space $H_*(W; \IR) = \bigoplus_{i\mygeq 0}
H_i(W; \IR)$. Let $\mf{o}$ denote this chosen
orientation. Provide each vector space $H_i(W; \IR)$ with a reference
basis $\hbasis{i}_\IR$ such that the basis 
$\left\{ {\hbasis{0}_\IR, \ldots, \hbasis{\dim W}_\IR} \right\}$ of 
$H_*(W; \IR)$ is {positively oriented} with respect to $\mf{o}$. 
Compute the sign--determined Reidemeister torsion 
$\Tor{C_*(W; \IR)}{\cbasis{*}_\IR}{\hbasis{*}_\IR} \in \IR^*$ of 
the resulting based and homology based chain complex and consider its sign 
$$\tau_0 =
  \mathrm{sgn}\left(
    \Tor{C_*(W; \IR)}{\cbasis{*}_\IR}{\hbasis{*}_\IR}
   \right)
\in \{\pm 1\}.$$

We define the \emph{sign--refined twisted Reidemeister torsion} of $W$
{(with respect to $\hbasis{*}$ and $\mf{o}$)} to be
\begin{equation}\label{eqn:TorsionRaff}
  \tau_0 \cdot 
  \Tor{C_*(W; V_\rho)}{\cbasis{*}}{\hbasis{*}} \in \FF^*.
\end{equation}
This definition only depends on the combinatorial class of $W$, the
conjugacy class of $\rho$, the choice of $\hbasis{*}$ and the
{homology} orientation $\mf{o}$. It is independent of the
orthonormal basis of $V$, of the choice of the lifts
$\tilde{e}^{i}_j$, and of the choice of the positively oriented basis
of $H_*(W; \IR)$. Moreover, it is independent of the order and
orientation of the cells (because they appear twice).

\begin{remark}
  In particular, if the Euler characteristic $\chi(W)$ is zero, then
  we can use any basis of $V$. If we change the basis of $V$ by another one, then the torsion is multiplicated 
by  the determinant of the bases change matrix to the power $\chi(W)$.
\end{remark}

One can prove that the sign--refined Reidemeister torsion is invariant 
under cellular subdivision, 
homeomorphisms and simple homotopy equivalences. In fact,
it is precisely the sign $(-1)^{|C_*|}$ in Equation~(\ref{def:RTorsion})
which ensures all these important invariance properties to hold (see~\cite{Turaev:2002}).

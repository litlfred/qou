---
doc_id: arxiv-0906.1500v4
doc_title: "Twisted Alexander invariant and non-abelian Reidemeister torsion for hyperbolic three-manifolds"
section_id: sec-023-732-proof-from-one-variable-to-two-variables
section_title: "Proof from one variable to two variables"
section_number: 7.3.2
pages: 22-23
source_pdf: 0906.1500v4.pdf
source_sha256: 9a586f6d134ca47f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.991
latex_coverage_ratio: 1.0
doc_brief: "Twisted Alexander invariant and non-abelian Reidemeister torsion for hyperbolic three-manifolds — We study a computational method of the hyperbolic Reidemeister torsion (also called in the literature"
---
Suppose that $\varphi\colon \pi_1(M) \to \ZZ \oplus \ZZ$. A priori, up to
multiplications by $t_1^{r}t_2^{s}$, 
the torsion $\PolyTors{M}{\otAd{\varphi}{\rho}}(t_1, t_2)$ is a
rational function  $P(t_1, t_2) / Q(t_1, t_2)$, where $P(t_1, t_2)$ and
$Q(t_1, t_2) \ne 0$ are coprime in $\CC[t_1, t_2]$. We will prove in fact, reducing
the situation to one variable, that the polynomial $Q(t_1,t_2)$ is
constant.

To this end, suppose that $Q(t_1, t_2)$ is a non--constant
polynomial. Without loss of generality we assume that $Q(t_1, t_2)$ is
a non--constant in $t_2$.  Applying Euclidean algorithm to $P(t_1,
t_2)$ and $Q(t_1, t_2)$ in $\CC(t_1)[t_2]$, we obtain the following
equality in the polynomial ring $\CC(t_1)[t_2]$ over the rational
function field $\CC(t_1)$:
\[
P(t_1, t_2)\tilde u(t_1, t_2) + Q(t_1, t_2) \tilde v(t_1, t_2) = 1.
\]
Here the coefficients of the polynomials in $t_2$ $\tilde u(t_1, t_2)$ and $\tilde v(t_1, t_2)$ are rational
functions in $\CC(t_1)$.  By taking product with some polynomial
$w(t_1) \in \CC[t_1]$, the following equality holds in $\CC[t_1, t_2]$:
\begin{equation}
  \label{eqn:EuclidAlgo_two_variables}
  P(t_1, t_2) u(t_1, t_2) + Q(t_1, t_2) v(t_1, t_2) = w(t_1).
\end{equation}
To each  pair of coprime integers $(a_1, a_2)$, consider the
homomorphism $h_{(a_1, a_2)}\colon \ZZ^2 \to \ZZ$ defined by $h_{(a_1,
  a_2)} (t_1) = t^{a_1}$ and $h_{(a_1, a_2)} (t_2) = t^{a_2}$ and let
$\varphi_{(a_1, a_2)} = h_{(a_1, a_2)} \circ \varphi$.  Using
Proposition~\ref{cor:naturality} and by the first part of the proof (for
one variable), we know that:
\[
\PolyTors{M}{\otAd{\varphi_{(a_1, a_2)}}{\rho}}(t) =
\PolyTors{M}{\otAd{\varphi}{\rho}}(t^{a_1}, t^{a_2}) = \frac{P(t^{a_1}, t^{a_2})}{Q(t^{a_1}, t^{a_2})} \in \CC[t].
\]
Thus there exists a polynomial $R(t) \in \CC[t]$ such that $P(t^{a_1}, t^{a_2})= R(t) Q(t^{a_1},
t^{a_2})$.  Hence by substituting $t^{a_1}$ and $t^{a_2}$ to $t_1$
and $t_2$ respectively, Equation~$(\ref{eqn:EuclidAlgo_two_variables})$ turns into
\[
Q(t^{a_1}, t^{a_2}) \{ R(t) u(t^{a_1}, t^{a_2}) + v(t^{a_1},
t^{a_2})\} = w(t^{a_1}).
\]

From our assumption $a_2$ can be chosen sufficiently large.  Since we
suppose that $Q(t_1, t_2)$ is not constant in $t_2$, by changing $a_2$
into a sufficient large integer, we obtain an arbitrary large degree
polynomial $Q(t^{a_1}, t^{a_2})$.  This contradicts the fact that the
degree of $Q(t^{a_1}, t^{a_2})$ must be less or equal to that of
$w(t^{a_1})$.  Therefore $Q(t_1, t_2)$ is constant in $t_2$.

Similarly, we can also
conclude that $Q(t_1, t_2)$ is constant in $t_1$.  As a consequence, the
polynomial $Q(t_1, t_2)$ is constant which proves that
$\PolyTors{M}{\otAd{\varphi}{\rho}}(t_1, t_2)$ is a polynomial in two
variables.

By an inductive argument (in descending order of $a_i$), the general
case works in the same way: $\PolyTors{M}{\otAd{\varphi}{\rho}}(t_1,
\ldots, t_n) \in \CC[t_1, \ldots, t_n]$. The multivariable case in
Theorem~\ref{theorem:poly} is also proved.














\begin{remark}
  Actually, in the multivariable case of Theorem~\ref{theorem:poly},
  it is sufficient to assume that there exists some positive integer
  $N_0$ such that for any $N \mygeq N_0$ we have a dual surfaces
  $S_{(a_1, \ldots, a_n)}$ satisfying that $|a_i -a_j| > N$ for all
  distinct $i, j$.
\end{remark}

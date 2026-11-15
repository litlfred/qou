---
doc_id: arxiv-1204.4824v2
doc_title: "Spectral networks"
section_id: sec-046-105-dimension-counts
section_title: "Dimension counts"
section_number: 10.5
pages: 67-68
source_pdf: 1204.4824v2.pdf
source_sha256: bf01cbaa5a8712c8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.931
latex_coverage_ratio: 0.919
doc_brief: "Spectral networks — We introduce new geometric objects called spectral networks. Spectral net- works are networks of trajectories on Riemann surfaces obeying certain local rules."
---
\label{sec:dimensions}

Now let us compare the dimensions of the moduli spaces related by $\Psi_\wnet$.

First we consider
$\CM(C, GL(K);\mathfrak{m})$.  This space can be represented
as the space of $GL(K,\IC)$ matrices $A_1, \dots, A_{g_C}$, $B_1, \dots, B_{g_C}$,
$C_1, \dots, C_s$, subject to some relations:  first, the eigenvalues of the $C_n$
are fixed; second, we impose
\begin{equation} \label{eq:fund-rel}
 \prod_i [A_i,B_i] \prod_n C_n = 1;
\end{equation}
third, we divide out by overall conjugation.
The condition on the eigenvalues of the $C_n$ eliminates $K s$ degrees of freedom.
The equation \eqref{eq:fund-rel} imposes only
$K^2-1$ independent conditions:  if $\prod_n \det C_n\not=1$
there are no solutions, but if $\prod_n \det C_n = 1$, while there are solutions,
the determinant equation is redundant.  Similarly, the center of the
gauge group acts trivially, so the quotient by the gauge group reduces the dimension
by $K^2-1$.  Altogether we get
\begin{equation}
\dim_\IC \CM(C, GL(K);\mathfrak{m}) = (2g_C + s) K^2 - K s - 2(K^2-1).
\end{equation}
On the other hand, using the Riemann-Hurwitz relation
\begin{equation}
\dim_\IC \CM(\Sigma, GL(1);\mathfrak{m}) = 2g_\Sigma = K(2g_C-2) + B + 2,
\end{equation}
where $B$ is the branching number (which is simply the number of branch points,
since we assume all branch points are simple.)
It follows that
\begin{equation} \label{eq:diff-dim}
\dim_\IC \CM(C, GL(K);\mathfrak{m}) - \dim_\IC \CM(\Sigma, GL(1);\mathfrak{m}) = (K^2-K)(2g_C + s - 2) - B.
\end{equation}
Since $\Psi_{\wnet}$ is symplectic it is in particular locally injective,
so the quantity in \eqref{eq:diff-dim} must be nonnegative.
We thus get a topological restriction
on the branching number of a branched cover $\Sigma \to C$ of degree $K$
admitting a spectral network:
\begin{equation}\label{eq:Branch-bound}
B \leq (K^2-K)(2g_C + s - 2).
\end{equation}
If this bound is saturated, $\Psi_{\wnet}$ is a local
symplectomorphism.  Note that this does happen for the
spectral curves \eqref{eq:sw-curve}, to which the spectral networks
$\wnet_\vartheta$ are subordinate.

Equation \eqref{eq:Branch-bound} is a
purely topological statement.  It says that there cannot
be too many branch points in a
spectral network.  It would be interesting to give a
more direct topological proof of this assertion.

In the case where \eqref{eq:Branch-bound} is saturated and $\Psi_\wnet$ is a covering
map, we have constructed not only a local isomorphism between $\CM(C)$ and $\CM(\Sigma)$,
but also a local identification between $(\pi_* \CL, \pi_* \nabla^\ab)$ and $(\hat E, \nabla)$.
We can use this to tie up a loose end from \S\ref{subsec:2d4d-wcf}.  Letting $(\CL,\nabla)$
vary we get a \ti{universal bundle} $\pi_*(\CL)$ over $\CM(\Sigma) \times C$.
Restricting this to some point
$\tilde{z} \in \tilde{C}$ gives a line bundle over $\CM(\Sigma)$, which we call $\pi_*(\CL)_{\tilde{z}}$.
Similarly we have a universal bundle $\hat E_{\tilde{z}}$ over $C$.\footnote{Actually this universal bundle does not quite exist owing
to subtleties involving the center of $GL(K)$; but its bundle of endomorphisms does exist, which is all we will use below.}
Now let $A(\Sigma)$ be the algebra of
global rational sections of $\End(\pi_*(\CL)_{\tilde{z}})$ (i.e. the algebra of sections over the generic point),
and similarly $A(C)$ the algebra of global rational sections
of $\End(\hat E_{\tilde{z}})$.  $A(\Sigma)$ is a central simple algebra of degree $K$ over
$\CR(\CM(\Sigma))$, the field of rational functions on $\CM(\Sigma)$,
and similarly $A(C)$ is a central simple algebra of degree $K$ over $\CR(\CM(C))$.
Our nonabelianization construction gives an embedding of
$A(C)$ in $A(\Sigma)$ and a compatible embedding of $\CR(\CM(C))$ in $\CR(\CM(\Sigma))$.  Now, we have just
shown that this embedding realizes $\CM(\Sigma)$ as a \ti{cover} of $\CM(C)$.  It follows that
$\CR(\CM(\Sigma))$ is a finite extension of $\CR(\CM(C))$ (since it is an extension and the two have the same
dimension, hence the same transcendence degree over $\IC$, and are both finitely generated).
Thus the group $Aut(\CR(\CM(\Sigma)):\CR(\CM(C)))$ is finite.
But now it follows by dimension counting that $Aut(A(\Sigma):A(C))$ is also finite.

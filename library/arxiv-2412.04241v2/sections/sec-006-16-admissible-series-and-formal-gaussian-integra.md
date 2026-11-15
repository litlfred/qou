---
doc_id: arxiv-2412.04241v2
doc_title: "The Habiro ring of a number field"
section_id: sec-006-16-admissible-series-and-formal-gaussian-integra
section_title: "Admissible series and formal Gaussian integration"
section_number: 1.6
pages: 11-13
source_pdf: 2412.04241v2.pdf
source_sha256: 308d1dd1c42bd979
toc_source: outline
text_source: latex
latex_prose_ratio: 0.96
latex_coverage_ratio: 0.964
doc_brief: "The Habiro ring of a number field — We introduce the Habiro ring of a number field K and modules over it graded by K3(K)."
---
\label{sub.admFGI}
It was conjectured by Nahm that the modularity of certain $q$-hypergeometric
functions is intimately related to the vanishing of certain associated classes in
algebraic $K$-theory, as was indeed later seen in a variety of
works~\cite{Nahm,Zagier:dilog,GZ:asymptotics,CGZ}.
The asymptotics of these $q$-hypergeometric functions as $q$ appraoches roots of
unity can be defined using formal Gaussian integration~\cite{Zagier:dilog,DG,DG2}.
Modularity would then imply some triviality of these asymptotic series.
We will see that this link goes even deeper, and that the
integrality of the formal series (as series in $q-\z$) is also linked to the
vanishing of the same classes in algebraic $K$-theory.

As we will see, there are two sources of these collections of power series at roots
of unity, with complementary properties.
One of these is the ``admissible series''
of Kontsevich--Soibelman~\cite[Sec.6]{KS:cohomological}, which arise as generating
series of cohomological Hall algebras that appear in enumerative algebraic geometry
such as Donaldson--Thomas theory.

\begin{definition}
For $N\in\BZ_{>0}$ and $t=(t_1,\dots,t_N)$, an admissible series is a power series
$F(t,q)\in\BQ(q)[\![t]\!]$ satisfying $F(t,q)=1+\mathrm{O}(t)$ and
\be
\label{logF}
\log F(t,q) \= -\!\!\!\!\sum_{0\neq n\in(\BZ_{\geq0})^N}\sum_{\ell \geq 1}
\frac{L_n(q^\ell)}{\ell\thinspace(1-q^\ell)}
t_1^{\ell n_1}\cdots t_N^{\ell n_N}\,,\qquad
\text{where}\qquad
L_n(q)\inn\BZ[q^{\pm1}].
\ee
\end{definition}

\noindent An equivalent way to describe admissible series is via their factorisation
into Pochhammer symbols. In particular, a series $F(t,q)$ is admissible if and only
if the unique integers $c_{n,i}$ (generalised Donaldson--Thomas invariants), defined
by the equality
\be
\label{defgamma}
F(t,q) \= \prod_{0\neq n\in(\BZ_{\geq0})^N}
\prod_{i \in \BZ} (q^i t_1^{n_1}\cdots t_N^{n_N};q)_\infty^{c_{n,i}},
\ee
vanish for all but finitely
many $i$ for each fixed $n$.
Here, as usual $(x;q)_n = \prod_{j=0}^{n-1}(1-q^j x)$
and
$(x;q)_{\infty}^{-1}=\sum_{k=0}^{\infty}x^k/(q;q)_k$.
The equivalence follows from the elementary but key identity~\eqref{logpoc}
for the infinite Pochhammer symbol, which implies the relation
\be
  L_n(q) \= \sum_{i \in \BZ} c_{n,i} \, q^i \inn \BZ[q^{\pm 1}]
\ee
between the exponents $c_{n,i}$ and the Laurent polynomials $L_{n}(q)$.

An admissible series $F(t,q)$ can be expanded at each root of unity and defines
a collection of series in $t^{1/m}=(t_1^{1/m},\dots,t_N^{1/m})$ given by
\be
\label{Phidef}
\Phitof_m(t,x) \= F(t^{1/m},\z_m+x) \,. 

\ee
The properties of these collections of series at roots of unity are explained in
detail in Section~\ref{sub.admissible} below.

Certain admissible series are easy to construct, compute and analyse.
A main theorem of~\cite[Sec.\thinspace6.1, Thm.\thinspace9]{KS:cohomological} (see
also Efimov~\cite{Efimov}) is that $q$-hypergeometric Nahm
sums\footnote{The original Nahm sums were given for positive definite $A$ by the
  special case when $t=(-1)^{\diag(A)}q^{b}$ for some $b\in\BZ^{N}$.}
\be
\label{FAdef}
F_A(t,q) \= \sum_{n \in \BZ^N_{\ge0}} \frac{

(-1)^{\mathrm{diag}(A)\cdot n}\,
q^{\frac{1}{2}(n^t A n + \mathrm{diag}(A)\cdot n)} }{(q;q)_{n_1}
\dots (q;q)_{n_N}} t_1^{n_1} \dots t_N^{n_N}
\ee
defined from a symmetric, integral $N \times N$ matrix $A$,
are always admissible series. These series encode the Poincar\'e polynomials of
representations of a quiver with symmetric potential and arbitrary dimension vector.

An elementary proof of the admissibility of $F_A(t,q)$ that uses the system of linear
\hbox{$q$-difference} equations~\eqref{PhiAshift} is given in Section~\ref{sub.DT}.
The proof also leads to a notion of a level $m$ admissible series defined in
Section~\ref{sub.madmissible} (abbreviated by $m$-admissible series throughout
this paper), the prototypical example being given by exactly the same sums as in
equation~\eqref{FAdef} with $n$ restricted to an $m$-congruence class
$k\in\{0,\dots,m-1\}^N$
\be
\label{FAmdef}
F_{A,m,k}(t,q) \;=\!\!\!\!
\sum_{n \,\in\, k+m\BZ^N_{\ge0}}\!\!\!\!\!\! \frac{
(-1)^{\mathrm{diag}(A)\cdot (n-k)}
q^{\frac{1}{2}(n^t A n-k^t A k)
  +\frac{1}{2}\mathrm{diag}(A)\cdot (n-k)} }{(q^{k_1+1};q)_{n_1-k_1}
\dots (q^{k_N+1};q)_{n_N-k_{N}}}\,t_1^{n_1-k_1}\!\!\cdots
t_N^{n_N-k_N}\!\!.
\ee

On the other hand, we also have a collection of power series at roots of unity
$\Phitof^\FGI_{A,m}(t,x)$ associated, by formal Gaussian integration, to an integer
symmetric matrix $A$. These series were previously defined
in~\cite{Zagier:dilog,DG,DG2} for the special case $t=(1,\dots,1)$ giving series
$\Phi_{A,m}(h)=\Phitof^\FGI_{A,m}(1,x)$, expressed there with respect to the
variable $h=\log(1+\z_m^{-1}x)$. This definition mimics the perturbation
expansions of complex Chern--Simons theory given in terms of state-integrals, and is
discussed in detail in Section~\ref{sub.FGI}.
Both collections $\Phitof_{A,m}(t,x)$ and $\Phitof^\FGI_{A,m}(t,x)$ are
in $\BQ[\z_m](\!(x)\!)[\![t^{1/m}]\!]$, for every positive integer $m$. 

Our two main results are that these two seemingly independent collections of
power series agree and that their values at $t=(1,\dots,1)$ belong to explicit
Habiro modules. In fact, these series
can be defined by the admissible series of Kontsevich--Soibelman and this gives
a new perspective to the arithmetic properties of DT-invariants and the
enumerative properties of the elements of the Habiro ring.

\begin{remark}
\label{rem:coprimeto6}
The primes $p=2$ and $3$ require special consideration. This is true for the
Bloch group itself, which has a uniform definition up to $2$-torsion and agrees
with the algebraic third $K$ group of a field away from some primes that always
include $2$ and $3$. There are further difficulties with the primes $2$ and $3$
due to the presence of a $\tfrac{1}{24}$ whose origin can be seen to
come from the Dedekind $\eta$-function and the famous equation of Euler
$\Li_{2}(1)=-\tfrac{1}{24}(2\pi i)^2$. Therefore, throughout the paper we will
only consider primes $p>3$ and always assume that $2,3|\Delta$ unless otherwise
stated. However, a more refined approach should be able to cover the remaining cases
as well.
\end{remark}

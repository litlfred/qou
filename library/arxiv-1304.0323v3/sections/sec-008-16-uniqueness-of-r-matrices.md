---
doc_id: arxiv-1304.0323v3
doc_title: "SYMMETRIC QUIVER HECKE ALGEBRAS"
section_id: sec-008-16-uniqueness-of-r-matrices
section_title: "Uniqueness of R-matrices"
section_number: 1.6
pages: 21-22
source_pdf: 1304.0323v3.pdf
source_sha256: 92e2b9dc876e1a52
doc_brief: "SYMMETRIC QUIVER HECKE ALGEBRAS — Let J be a set of pairs consisting of good U ′ q(g)-modules and invertible elements in the base ﬁeld C(q)."
text_source: latex
latex_prose_ratio: 0.972
latex_coverage_ratio: 0.901
---
The following lemma says that the convolution of
two  simple modules
(after adding spectral parameters)
remains simple.

\Lemma Assume that $\cor$ is a field. Let $z$, $z'$ be algebraically
independent indeterminates and set $K=\cor(z,z')$. Let $M$ and $N$
be a simple $R( \beta )$-module and a simple $R( \gamma )$-module,
respectively. Then $K\tens_{\cor[z, z']} (M_z\circ N_{z'})$ is a
simple $K\tens R( \beta+ \gamma )$-module. \enlemma


\Proof
In  this  proof,  we  write
 $M_z$ for the  $K\tens R( \beta )$-module $K\tens_{\cor[z]} M_z$ 
for the sake of simplicity. Recall that $\sym_{m,n}\seteq\set{w\in
\sym_{m+n}}{\text{$w(k)<w(k+1)$ for any $k\not=m$}}$. Then we can
easily see that
$$M_z\circ N_{z'}=\soplus_{w\in \sym_{m,n}}\vphi_w\cdot M_z\tens N_{z'}.$$
 Indeed, it follows from \eqref{eq:phitau} and
the fact that $x_i-x_j\col M_z\tens N_{z'}\to M_z\tens N_{z'}$ is bijective
for $1\le i\le m<j\le m+n$.

Let $L$ be a non-zero $K\tens R( \beta+\gamma )$-submodule of $M_z\circ N_{z'}$.
For $u\in M_z\circ N_{z'}$, we write
$$u=\sum_{w\in \sym_{m,n}}\vphi_w u_w\qtext{with $u_w\in M_z\tens N_{z'}$,}$$
and set $S(u)=\set{w\in \sym_{m,n}}{u_w\not=0}$.


Let us take  a \ non-zero $u\in L$ such that the cardinality of $S(u)$ is
minimal and let $w\in S(u)$. Assume that there exists $w'\not=w$ in
$S(u)$. Since we have $$\set{1\le k\le m+n}{w^{-1}(k)\le m}
\not\subset\set{1\le k\le m+n}{{w'}^{-1}(k)\le m},$$ there exists
$a$ such that $1\le w^{-1}(a)\le m$ and $m<{w'}^{-1} (a)$.

Take a monic polynomial $f(x)$ such that $f(x_k)\vert_N=0$ for $1\le
k\le n$. Then $f(x_k-z')$ acts by zero on $M_z\tens N_{z'}$ for $k>
m$, and the action of $f(x_k-z')$ is invertible on $M_z\tens N_{z'}$
for $k\le m$. Hence $f(x_{{w'}^{-1}(a)}-z')u_{w'}=0$. Since
$$f(x_{a}-z')u=\sum_{y\in S(u)\setminus\{w'\}}\vphi_yf(x_{y^{-1}(a)}-z')u_y,$$
the minimality of $S(u)$ implies that $f(x_{a}-z')u=0$.
In particular, we have
$f(x_{w^{-1}(a)}-z')u_w=0$, which implies that $u_w=0$.
It is a contradiction and we conclude that $S(u)=\{w\}$
and $u=\vphi_w u_w$.

Since $\vphi_{w^{-1}}\vphi_w\col M_z\tens N_{z'}\to M_z\tens N_{z'}$
is a $K[x_1,\ldots, x_{m+n}]$-linear isomorphism, we have $u_w\in
L$. Since $M_z\tens N_{z'}$ is a simple $K\tens R( \beta )\tens R(
\gamma )$-module, we have $M_z\tens N_{z'}\subset L$, and we
conclude that $L=M_z\circ N_{z'}$. \QED


This lemma immediately implies
the following proposition which  says  that an R-matrix for
simple modules is unique up to constant multiple.

\Prop Assume that $\cor$ is a field and let $z$, $z'$ be independent
indeterminates. Let $M$ and $N$ be a  simple  $R( \beta )$-module
and $R( \gamma )$-module, respectively. Then we have \eqn &&\Hom_{R(
\beta +\gamma)}\bl M_z\circ N_{z'}, M_z\circ N_{z'}\br
\simeq\cor[z,z'],\\[1ex]
&&\Hom_{ R( \beta +\gamma)}\bl M_z\circ N_{z'},
N_{z'}\circ M_z\br
\simeq \cor[z,z'](z-z')^{-s} R_{M_z, N_{z'}}.
\eneqn
Here $s$ is the order of zeroes of
$R_{M_z,N_{z'}}$ \ro see \eqref{def:s}\rf.
\enprop
\Proof
The first assertion immediately follows from the preceding lemma.
The second follows from the first since
$R_{M_z, N_{z'}}$ gives an isomorphism
from
$ K\tens_{ \cor[z,z']}(M_z\circ N_{z'})$ to $K\tens_{ \cor[z,z']}(N_{z'}\circ M_z)$,
where $K=\cor[z,z',(z-z')^{-1}]$.
\QED

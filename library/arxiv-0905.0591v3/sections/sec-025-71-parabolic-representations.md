---
doc_id: arxiv-0905.0591v3
doc_title: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS"
section_id: sec-025-71-parabolic-representations
section_title: "Parabolic representations"
section_number: 7.1
pages: 24-25
source_pdf: friedvidu1.pdf
source_sha256: cfeaf61f759a6af8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.991
latex_coverage_ratio: 1.0
doc_brief: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS — We give a short introduction to the theory of twisted Alexander polynomials of a 3–manifold associated to a representation of its fundamental group."
---
\label{section:specialknots}


Let $K\subset S^3$ be a knot. A representation
$\gamma:\pi_1(S^3\setminus \nu K)\to \mbox{SL}(2,\mathbb{C})$ is called \emph{parabolic}
if the
image of any meridian is a matrix with trace 2. Note that Thurston \cite{Th87} showed that
given a hyperbolic knot $K$   the discrete faithful representation
$\pi_1(S^3\setminus \nu K) \to \mbox{PSL}(2,\mathbb{C})$ lifts to a
parabolic representation $\gamma : \pi_1(S^3\setminus \nu K) \to \mbox{SL}(2,\mathbb{C})$.
The twisted Reidemeister torsion corresponding to this canonical representation has been surprisingly little studied
(cf. though \cite{Sug07} and \cite[Corollary~4.2]{Mo08}).

Throughout the remainder of this section let $K$ be a 2--bridge knot. Then the group $\pi_1(S^3\setminus \nu K)$ has a presentation of the form
$\langle x,y | Wx=yW \rangle$ where $x,y$ are meridians of $K$ and $W$ is a word in $x^{\pm 1}, y^{\pm 1}$.
Parabolic representations of 2--bridge knots have been extensively studied by Riley \cite[Section~3]{Ri72}.
To a 2--bridge knot $K$ Riley associates a monic polynomial $\Phi_K(t)\in \mathbb{Z}[t^{\pm 1}]$
such that  any zero $\zeta$ of $\Phi_K(t)$ gives rise to a representation
$\gamma_\zeta:\pi_1(S^3\setminus \nu K)\to \mbox{SL}(2,\mathbb{C})$ of the form
\[ \gamma_\zeta(x)= \begin{pmatrix} 1&1\\ 0&1 \end{pmatrix} \mbox{ and }\gamma_\zeta(y)= \begin{pmatrix} 1&0\\ \zeta &1 \end{pmatrix}. \]
Furthermore Riley shows that any parabolic representation of a 2--bridge knot is conjugate to such a representation
(cf. also \cite[Section~5]{SW09c} for details).

Given an irreducible factor $\phi(t)$ of $\Phi_K(t)$ of degree $d$ one can consider the representation $\oplus \gamma_{\zeta'}$ where $\zeta'$ runs over the set of all zeroes of $\phi(t)$.
Silver and Williams show that this representation is conjugate to an integral representation $\gamma_{\phi(t)}:\pi_1(S^3\setminus \nu K)\to \mbox{GL}(2d,\mathbb{Z})$
which is called the \emph{total representation corresponding to $\phi(t)$}.

Twisted Alexander polynomials of 2--bridge knots corresponding to such parabolic and total representations have been studied
extensively by Silver and Williams \cite{SW09c} and Hirasawa and Murasugi (cf. \cite{Mu06} and \cite{HM08}).
In particular the following theorem is shown. It should be compared  to the classical result that given a knot
$K$ we have $\Delta_K(1)=1$.


\begin{theorem}
Let $K$ be a two--bridge knot and $\phi(t)$ an irreducible factor of $\Phi_K(t)$ of degree $d$.
Then
\[ \left|\Delta_K^{\gamma_{\phi(t)}}(1)\right| =2^d.\]



\end{theorem}

A special case of the
theorem

is shown in \cite[Theorem~A]{HM08},
the general case is proved in \cite[Theorem~6.1]{SW09c}.
Silver and Williams also conjectured that under the assumptions of the theorem we have
\[ \left|\Delta_K^{\gamma_{\phi(t)}}(-1)\right| =2^d m^2\]
for some odd number $m$.





We refer to \cite{SW09c} and \cite{HM08} for more on twisted Alexander polynomials of 2--bridge knots.
All three  papers contain a wealth of interesting examples and results which we find impossible to summarize in this short survey.

Silver and Williams also considered twisted Alexander polynomials of torus knots.
They showed \cite[Section~7]{SW09c} that for any parabolic representation $\gamma$ of a torus knot $K$, the
twisted Alexander polynomial $\Delta^\gamma_K$ is a product of cyclotomic polynomials.

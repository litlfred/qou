---
doc_id: arxiv-1412.4711v1
doc_title: "CHARACTER VARIETIES FOR SL(3, C): THE FIGURE EIGHT KNOT"
section_id: sec-019-5-deforming-representations-another-way-to-param
section_title: "Deforming representations: another way to parametrize the components"
section_number: 5
pages: 22-24
source_pdf: 1412.4711v1.pdf
source_sha256: 4fb1d6ee062cca8c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.976
latex_coverage_ratio: 0.981
doc_brief: "CHARACTER VARIETIES FOR SL(3, C): THE FIGURE EIGHT KNOT — We give a description of several representation varieties of the fundamental group of the complement of the ﬁgure eight knot in PGL(3, C) or"
---
\label{deformation}

Having found a specific representation $\rho: \Gamma_8 \to \mathrm{SL(3,\mathbb C)}$ by
algebraic means, there is a complementary method we can often use to determine
the component $\mathcal{V}$ of the variety containing $\rho$. We apply this procedure to a representation in each of the three components found in the previous section. As a product, we get an explicit parametrisation of the representations, i.e. an explicit parametrisation of matrices generating the representation, at least for a Zariski-open subset of the studied component. This information is of course very valuable for the study of the representations found, as in \cite{DF}.


The procedure may be broken
down into four steps, which we now describe briefly; a detailed account of the
method is given in \cite{CLTb}.  Repeated use is made of the LLL algorithm \cite{LLL}
for finding an algebraic number of low degree, close to a number given numerically to
high precision.  For ease of exposition, we shall assume that
$\mathcal{V}$ has dimension $2$; in advance we might not know this dimension,
but usually with experimentation it quickly becomes evident.  Also, the dimension of
the Zariski tangent space at $\rho$ (\cite{CLTa}) provides an upper bound for the
dimension of $\mathcal{V}$.

\begin{itemize}
\item[\bf (i)]  First, we perturb the images of the group generators under $\rho$
slightly, and use these perturbed matrices as a starting point for Newton's method
in conjunction with the group relators, so as to converge numerically to a
representation $\sigma$.  If the original representation $\rho$ is not isolated,
$\sigma$ will typically be some generic representation close to $\rho$; however,
by carefully imposing extra constraints one can ``steer'' the Newton process so
that $\sigma$ has some specified character.  In this way we can obtain a
finite array of representations $\{\sigma_{ij}\}$ such that for each generator $g_k$ of $\Gamma_8$
the traces of the matrices $\alpha_{ij} = \sigma_{ij}(g_k) $ form a suitable array of (numerical
approximations to) rational numbers.  Of course the matrix $\alpha_{ij}$ depends on the
index $k$ of $g_k$, but to avoid excess of notation we omit mention of this index.
\item[\bf (ii)]  Matrices $\beta_{ij}$ are chosen (independently of $k$) so that the conjugates
$\alpha'_{ij} = \beta^{-1}_{ij} \alpha_{ij} \beta_{ij}$ have entries that are all algebraic.
This is always possible, owing to the fact that $\mathcal{V}$ is an algebraic
set; in practice we desire that the degrees of these algebraic numbers should be
as small as possible.
\item[\bf (iii)]  So far, for each group generator $g_k$ we have a two-dimensional array
of matrices $\alpha'_{ij}$ whose entries
are numerical approximations to elements of a number field $\mathcal{F}_{ij}$.
We choose a suitable basis for $\mathcal{F}_{ij}$ over the field of rationals,
noting that the field depends on the parameters $i, j$.  Next, LLL allows us to emerge
from the world of numerical approximations to that of exact quantities by guessing
an expression for each matrix entry as a linear combination of basis elements.
Of course we wish also to be freed from the discrete coordinates $(i, j)$ to
general (complex) coordinates $(u, v)$ for the variety $\mathcal V$, and this is
achieved, up to judicious guesswork, by means of polynomial interpolation across
the $(i,j)$--lattice.

\item[\bf (iv)]  The reader will note that guesswork has been employed at several
points of this procedure, and that substantial use was made of numerical approximations
to algebraic numbers.  However, we have arrived at a function $\Phi$ that associates to
each generator $g_k$ of $\Gamma_8$ an exact matrix, whose entries lie in an algebraic extension
of $\mathbb Q(u,v)$, where $u,v$ are independent transcendentals.  Using software
such as Mathematica or Maple, it is relatively straightforward to verify by formal
manipulation that the matrices $\Phi(g_k)$ satisfy the group relations, {\it i.e.} that
$\Phi$ extends to a representation of $\Gamma_8$.  Following the nomenclature of M. Culler and
P. Shalen, we call $\Phi$ the {\it tautological represention} of $\Gamma_8$ associated to $\mathcal{V}$.
A tautological representation depends of course on a chosen parametrization, {\it i.e.}
a coordinate system for the variety; also, two matrix representations are considered
to be equivalent if they agree up to postmultiplication by an inner automorphism of
the target linear group.
\end{itemize}

The method just described would appear at first sight to be remarkably {\it ad hoc;}\/
however, it often works well.  It was applied to three representations
$\rho_1 \,,\, \rho_2 \,,\, \rho_3$ given in \S \ref{section:example-unipotent} -- one in each of the components found in the previous section. It produces tautological
representations $R_i \; (i=1,2,3)$ of the figure-eight knot group
$\Gamma_8$ into $\mathrm{SL(3,\mathcal{F})}$, where the field $\mathcal{F}$ is an
algebraic extension of $\mathbb Q(u,v)$.  Our brief descriptions of the salient
properties of the $R_i$ are given mostly without proof; however, the reader can
check most of them with the aid of suitable computer algebra software.
\vvv\noind

---
doc_id: arxiv-math-0408210v3
doc_title: "A simple algebraic proof of the algebraic index theorem"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: 0408210v3.pdf
source_sha256: 16d5ccb83a86954f
toc_source: inferred
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.983
doc_brief: "A simple algebraic proof of the algebraic index theorem — In math.QA/0311303 B. Feigin, G. Felder, and B."
---
The famous Atiyah-Singer index theorem \cite{AS} relates the
index of an elliptic pseudo-differential operator on a compact
manifold $X$ to the Todd class of $X$ and the Chern character
of the bundle naturally associated with the symbol of
the pseudo-differential operator. It is well-known that
the algebra of pseudo-differential operators can be viewed as
a ``quantization'' of the cotangent bundle $T^{*}X$.
Starting from this point B. Fedosov \cite{F1} proposed a natural
analogue of the Atiyah-Singer index theorem for
the deformation quantization of an arbitrary symplectic
manifold. This theorem expresses the index of a compactly
supported element in $K$-theory of the quantum algebra
of functions on a symplectic manifold $\M$ via the $\hA$-genus
of $\M$, the Deligne-Fedosov class of the quantum algebra,
and the Chern character of the principal symbol of
the $K$-theory element. While the original index theorem
of Atiyah and Singer relates two integers, the Fedosov
index theorem relates two formal power series with complex
coefficients.

In paper \cite{NT} R. Nest and B. Tsygan proposed a completely
different proof of the algebraic index theorem based on
the relations between Hochschild (co)homology, cyclic
(co)homology, and Lie algebra (co)homology. In their next
paper \cite{NT1} they also showed that the analytic index theorem
for a compact manifold (without a boundary)
could be derived from the algebraic one.
In order to generalize this result to manifolds
with a boundary (or more generally, with corners) one
is in great need of {\it a local version of the algebraic
index theorem} which relates De Rham cohomology
classes, rather than formal power series of
complex numbers.

The aim of this paper is to give such a version (see theorem
\ref{index} in section $3$) using the trace density
map proposed in paper \cite{FFS} by B. Feigin, G. Felder,
and B. Shoikhet. Namely,
we show that the Feigin-Felder-Shoikhet (FFS) trace
density map sends an arbitrary element of $K$-theory of the
algebra of quantum functions on $\M$ to the top
component of the cup product of the $\hA$-genus
of $\M$, the exponent of the Deligne-Fedosov class
of the quantum algebra, and the Chern character of the principal
symbol of the element. Thus, we generalize the result
of \cite{FFS}, in which the trace density map was
evaluated at the trivial element of $K$-theory.
For the case of the cotangent bundle this computation of
\cite{FFS} was performed in \cite{CFS}.

We have to mention that
in \cite{BNT1} another version of the trace density
map was proposed. This map sends a cohomology class of the
sheaf of the periodic cyclic complex $CC^{per}_{\bul}(\cO^{quant}_X)$
of the structure sheaf $\cO^{quant}_X$ of quantum functions on
a holomorphic symplectic manifold $X$ to the cohomology
of the constant sheaf on $X$. In \cite{BNT1} it was proven that
the evaluation of this map on an arbitrary cohomology class of the
sheaf of periodic cyclic complex $CC^{per}_{\bul}(\cO^{quant}_X)$
can be expressed in terms of the principal
symbol of the class, $\hA$-genus of $X$ and the
Deligne-Fedosov class of the quantum deformation.
In \cite{BNT1} the authors refer to this result
as a Riemann-Roch theorem for deformation
quantizations. It is not hard to see that the local
version of the algebraic index theorem proven in our paper
follows from the results of P. Bressler, R. Nest and
B. Tsygan \cite{BNT1}. However, our proof is
more explicit and straightforward. For this reason we expect
that our technique is more powerful for exploring the parallel
analytic results.

We would like to mention an alternative deformation
quantization procedure due to L. Boutet de Monvel
and V. Guillemin \cite{BM-G}. This procedure allows us
to quantize an arbitrary compact symplectic manifold with
an integral symplectic form. Recently R. Melrose proposed
in \cite{RM} a beautiful idea on how one can relax the
integrality condition in the quantization of L. Boutet de Monvel
and V. Guillemin. R. Melrose suggests that using this procedure one
could derive the algebraic index theorem from the
analytic one.

The organization of the paper is as follows. In section two, we give
a reminder of Fedosov's construction \cite{F1} of the deformation quantization
with twisted coefficients on a symplectic manifold. In this section
we also recall the necessary results of Feigin, Felder, and
Shoikhet about their trace density map
proposed in \cite{FFS}.
In section three, we prove the local version
of the algebraic index theorem (see theorem {\ref{index}), using
the FFS trace density map.
In the concluding section we make a few remarks about the local
algebraic index theorem for symplectic Lie algebroids and
the versions of the local Riemann-Roch-Hirzebruch theorem.

Throughout the paper we assume the summation over repeated indices.
We assume that $\M$ is either a smooth real symplectic ma\-ni\-fold
of dimension $2n$ or a smooth affine algebraic variety (over $\bbC$)
of the complex dimension $2n$, endowed with an algebraic
symplectic form. $C(\M)$ stands, respectively, for the
algebra of smooth function or for the algebra of regular
functions on $\M$. The notation $S_k$ is reserved  for
the group of permutations of $k$ elements.
We omit the symbol $\wedge$ referring to a local basis
of exterior forms, as if we thought of $dx^i$'s as anti-commuting variables.
For a vector space $\mh$ we denote by $S^j\mh$ the subspace
of monomials of degree $j$ in the symmetric algebra $S\mh$ of $\mh$\,.
Finally, we always assume that a nilpotent linear operator is
the one whose second power is vanishing.



{\bf Acknowledgments.} This work was done while the first author
was a student and the second author was a mentor in
the Summer Program for Undergraduate Research.
We both express sincere thanks to Hartley Rogers who
organizes this remarkable program at M.I.T.
We thank Richard Melrose and all participants
of his Spring analysis seminar for their interest and
stimulating discussions. The second author also thanks
Alberto Cattaneo and Giovanni Felder for useful
conversations. We are grateful to Teal Guidici for criticisms
concerning our English.  This work is partially
supported by the NSF grant DMS-9988796, the Grant
for Support of Scientific Schools NSh-1999.2003.2,
the grant INTAS 00-561 and the grant CRDF
RM1-2545-MO-03.

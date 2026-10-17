---
doc_id: arxiv-1004.1533v3
doc_title: "TURAEV-VIRO INVARIANTS AS AN EXTENDED TQFT"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 1-2
source_pdf: 1004.1533v3.pdf
source_sha256: 95c1544431e6bf37
toc_source: outline
text_source: latex
latex_prose_ratio: 0.969
latex_coverage_ratio: 0.945
doc_brief: "TURAEV-VIRO INVARIANTS AS AN EXTENDED TQFT — In this paper we show how one can extend Turaev-Viro invariants, deﬁned for an arbitrary spherical fusion category C, to 3-manifolds with cor- ners."
---
Turaev--Viro (TV) invariants of 3-manifolds $Z_{TV}(M)$ were defined by
Turaev and Viro in \ocite{TV} using a quantum analog of 6j symbols for
$sl_2$. In the same paper it was shown that these invariants can be
extended to a 3-dimensional TQFT. 

Later, Barrett and Westbury \ocite{barrett} showed that these
invariants can be defined for any monoidal category $\C$ possessing a
suitable notion of duality (``spherical category''). In particular, they
can be defined for the category of $G$-graded vector spaces, where $G$ is a
finite group. In this special case, the resulting TQFT coincides with the
version of Chern--Simons theory with the finite gauge group $G$, described
in \ocite{freed-quinn} (or in more modern language, in \ocite{FHLT}); in
physics literature, this theory is also known as the Levin--Wen model.

In the case when the category $\C$ is not only monoidal but in fact
modular (in particular, braided), there is another 3-dimensional TQFT
based on $\C$, namely Reshetikhin--Turaev TQFT. It was shown in
\ocite{turaev} that in this case, one has
$$
Z_{TV, \C}(M)=Z_{RT,\C}(M)Z_{RT,\C}(\ov{M})
$$
where $\ov{M}$ is $M$ with opposite orientation. In particular, if $\C$ is
unitary category over $\CC$, then $Z_{TV, \C}(M)=|Z_{RT,\C}(M)|^2$.

It has been conjectured that in the general case, when $\C$ is a spherical
(but not necessarily modular) category, one has
$$
Z_{TV, \C}(M)=Z_{RT, Z(\C)}(M)
$$
where $Z(\C)$ is the so-called Drinfeld center of $\C$ (see
\seref{s:center}); moreover, this extends to an isomorphism of the
corresponding TQFTs. Some partial results in this direction can be found,
for example, in \ocite{muger2}; however, the full statement remained a
conjecture.

The current paper is the first in a series giving a proof of this
conjecture for an arbitrary spherical category $\C$ over an algebraically
closed field $\kk$ of characteristic zero. In the current paper, we extend
TV invariants to 3-manifolds with corners of codimension 2 (or, which is
closely related, to 3-manifolds with framed tangles inside); in the
language of \ocite{lurie}, we construct a 3-2-1  extension of TV theory.
This extension satisfies $Z_{TV}(S^1)=Z(\C)$: boundary circles of
2-surfaces
should be colored by objects of $Z(\C)$. We also show that for an
$n$-punctured sphere, the
resulting vector space coming from this extended TV theory coincides with
the one coming from Reshetikhin-Turaev theory based on $Z(\C)$.

Thsi extended theory is related to the one
suggested in \ocite{turaev94}; however, that paper only considered the case
when $\C$ itself is modular and the components of links are labeled by
objects of $\C$, not $\Z(\C)$. We will investigate the relation between
these constructions in forthcoming papers. 

After the preliminary version of this paper was posted, a proof of formula
$Z_{TV, \C}(M)=Z_{RT, Z(\C)}(M)$ was announced by Turaev
\ocite{turaev-conference}; howevere, details of this proof are not yet
available.

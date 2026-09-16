---
doc_id: arxiv-q-alg-9709040v1
doc_title: "DEFORMATION QUANTIZATION OF POISSON MANIFOLDS, I"
section_id: sec-080-834-comparison-with-the-duﬂo-kirillov-isomorphis
section_title: "Comparison with the Duﬂo-Kirillov isomorphism"
section_number: 8.3.4
pages: 43-44
source_pdf: 9709040v1.pdf
source_sha256: 8baf650d86c5b8ab
doc_brief: "DEFORMATION QUANTIZATION OF POISSON MANIFOLDS, I — 83 sections: Front matter; Introduction; Deformation quantization"
---
For the case of semi-simple g there is so called Harish-Chandra isomorphism between alge bras
(
Sym (g)
) g
and Center(Ug). A. Kirillov realized that there is a way to rewrite the Hari sh-Chandra isomorphism in a
form which has sense for arbitrary ﬁnite-dimensional Lie al gebra, i.e. without using the Cartan and Borel
subalgebras, the Weyl group etc. Later M. Duﬂo (see [D]) prov ed that the map proposed by Kirillov is an
isomorphism for all ﬁnite-dimensional Lie algebras.
The explicit formula for the Duﬂo-Kirillov isomorphism is t he following:
IDK :
(
Sym (g)
) g
≃ Center(U(g)), I DK =IP BW|(Sym(g))g◦Istrange|(Sym(g))g,
whereIstrange is an invertible translation invariant operator on Sym (g) associated with the following formal
power series on g at zero, reminiscent of the square root of the Todd class:
γ↦→exp

∑
k≥1
B2k
4k(2k)!Trace (ad(γ)2k)


43
where B2,B 4,... are Bernoulli numbers. Formally, one can write the r.h.s. as det(q(ad(γ))) where
q(x) :=
√
ex/ 2−e−x/ 2
x .
The fact that the Duﬂo-Kirillov isomorphism is an isomorphi sm of algebras is highly non-trivial. All
proofs known before (see [Du],[Gi]) used certain facts abou t ﬁnite-dimensional Lie algebras which follow only
from the classiﬁcation theory. In particular, the fact that the analogous isomorphism for Lie superalgebras
is compatible with products, was not known.
We claim that our isomorphism coincides with the Duﬂo-Kiril lov isomorphism. Let us just sketch the
argument. In fact, we claim that
I−1
alg◦IT =IP BW◦Istrange .
If it is not true then we get a non-zero series Err∈ t2R[[t2]] such that the translation invariant operator
on Sym (g) associated with γ↦→Idet(exp(adγ ))) gives an automorphism of algebra (Sym (g))g. Let 2 k >0 be
the degree of ﬁrst non-vanishing term in the expansion of Err. Then it is easy to see that the operator on
Sym (g) associated with the polynomial γ↦→Trace (ad(γ)2k is a derivation when restricted to ( Sym (g))g.
One can show that it is not true using Lie algebras g =gl(n) for large n. Thus, we get a contradiction and
proved that Err = 0. Q.E.D.
As a remark we would like to mention that if one replaces serie s q(x) above just by
( x
1−e−x
) − 1
2
then one still get an isomorphism of algebras. The reason is t hat the one-parameter group of automorphisms
of Sym (g) associated with series
γ−→exp(const·Trace (ad(γ)))
preserves the structure of Poisson algebra on g∗. This one-parameter group also acts by automorphisms of
Ug. It is analogous to the Tomita-Takesaki ﬂow of weights for vo n Neumann factors.

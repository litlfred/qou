---
doc_id: arxiv-1309.0865v1
doc_title: "SOERGEL CALCULUS"
section_id: sec-032-26-ben-elias-and-geordie-williamson
section_title: "BEN ELIAS AND GEORDIE WILLIAMSON"
section_number: 26
pages: 26-27
source_pdf: 1309.0865v1.pdf
source_sha256: e610a4fa938a7cc9
doc_brief: "SOERGEL CALCULUS — The monoidal category of Soergel bimodules is an incarnati on of the Hecke category , a fundamental object in representation the ory ."
---
monoidal category to the 2-groupoid for W over k, and can be deﬁned without any
restrictions on k. Presenting this 2-groupoid as a monoidal category by gener ators
and relations is surprisingly interesting (see [EWa] and th e next chapter).
We note that all tensor products of Soergel bimodules and sta ndard bimodules
are free as left (or right) R-modules, and thus the Hom spaces between them are R-
torsion-free. We will soon show that, under certain assumpt ions on the realization,
they are free as R-modules.
Now we discuss the maps between Soergel bimodules and standa rd bimodules.
There is an injection of bimodules R(−1) → Bs arising from the Frobenius algebra
structure, sending 1 ↦→∆ s (deﬁned in the previous section). The cokernel of this
map is naturally isomorphic toRs(1), via the mapBs →Rs(1) sendingf ⊗g ↦→fs (g).
Conversely , there is a surjectionBs → R(1) sendingf ⊗g ↦→fg . The kernel of this
map is naturally isomorphic to Rs(−1) via the map sending 1 ↦→δ ⊗ 1 − 1 ⊗δ.
Remark 3.13. Just as ∆ s has a canonical description, so too does this element δ ⊗ 1 −
1 ⊗δ. The trace map ∂s : R → Rs induces an R-bilinear pairing (f,g ) ↦→∂s(fg ), but
it also induces a twisted-bilinear pairing (f,g ) ↦→∂s(fs (g)). The bases {1,δ } and
{−δ, 1} ofR overRs are dual for the twisted pairing, and the element δ ⊗ 1 − 1 ⊗δ
is independent of the choice of dual bases. The reader can pon der the notion of a
twisted Frobenius extension.
All four of these maps have graded degree 1. We encode them in two short exact
sequences:
(3.4) 0 →R(−1) →Bs →Rs(1) → 0
(3.5) 0 →Rs(−1) →Bs →R(1) → 0
ThusBs is ﬁltered by R andRs, though in no particular order, and the grading shifts
which appear depend on the chosen order. This implies that ev ery Bott-Samelson bi-
module has a ﬁltration whose subquotients are standard bimo dules (with shifts). Be-
cause each bimoduleRw is indecomposable, any direct summand of a Bott-Samelson
bimodule (and hence any Soergel bimodule) also has such a ﬁlt ration. However, the
order in which standard modules appear in such a ﬁltration ne ed not respect the
Bruhat order.
Now assume that h is a Soergel realization. It is a deeper fact that any Soergel
bimodule has a ﬁltration in which all successive subquotien ts are standard mod-
ules, occurring in an order reﬁning the Bruhat order (resp. t he reversed Bruhat or-
der). Such ﬁltrations are called standard ﬁltrations , and the graded multiplicities of
the standard modules appearing do not depend on the choice of ﬁltration. One de-
ﬁnes the character of a Soergel bimoduleB as the element ch(B) of the Hecke algebra
counting these graded multiplicities. (For the precise deﬁ nition of the character see
[Soe07, §5]).
SOERGEL CALCULUS 27
Soergel went on to prove that the space of homomorphisms betw een any two So-
ergel bimodules is free as a left or right R-module, with graded rank given by eval-
uating the standard pairing on the characters of each bimodu le. Soergel used this
formula to classify , in a non-constructive way , all the inde composable Soergel bi-
modules. From the above discussion it is clear that if w is a rex, then Bw hasRw in
its standard ﬁltration with multiplicity 1, and all other standard modules appearing
are isomorphic toRy fory <w. The following theorem is due to Soergel [Soe07, Satz
6.14]:
Theorem 3.14. Let h be a Soergel realization of W . For all w ∈ W there exists a unique
(up to isomorphism) bimodule Bw which occurs as a direct summand of Bw for any reduced
expressionw forw. The bimodule Bw is uniquely determined as a summand of Bw by the
fact that it is indecomposable and (some shift of) Rw occurs in its standard ﬁltration. The
set {Bw | w ∈ W } constitutes a complete set of non-isomorphic indecomposab le Soergel
bimodules, up to isomorphism and grading shift.
The statement that Bw contains a unique summand such that (some shift of) Rw
occurs in its standard ﬁltration follows immediately from t he indecomposability of
Rw. The fact that such summands for different rexes are isomorp hic is not difﬁcult
to prove (using the Krull-Schmidt property and an idempoten t lifting argument).
The difﬁculty in the theorem is to show that any summand of any Bott-Samelson
bimodule is isomorphic to one of the bimodules Bx up to a shift.
The theorem implies that Bw is the only summand of Bw which is not a summand
of (some shift of) By for any shorter sequence y. In principle one can “construct”
Bw by ﬁnding all the summands of Bw which occur as shifts of summands of lower
terms, removing them, and seeing what remains. This amounts to a calculation of
all idempotents in End0(Bw), which is a difﬁcult and subtle question.
Because of the implicit deﬁnition of the indecomposable bim oduleBw, its intrinsic
properties often depend on the characteristic of k and the realization h of (W,S ). For
example, it may happen that Bw admits a non-trivial decomposition in characteris-
tic 0, with a nontrivial summand Bw, while for a certain ﬁnite characteristics Bw is
indecomposable, meaning that Bw = Bw. In this paper we determine the algebra of
endomorphisms of Bw, but are only able to make very basic statements about the
representation theory of this algebra.

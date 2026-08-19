---
doc_id: arxiv-0910.5695v2
doc_title: "ON BLOCKS OF DELIGNE’S CATEGORY Rep(St)"
section_id: sec-015-62-comparison-of-non-semisimple-blocks-in-repsd
section_title: "Comparison of non-semisimple blocks in Rep(Sd; F)."
section_number: 6.2
pages: 39-40
source_pdf: 0910.5695v2.pdf
source_sha256: 703c2a2f1f9380b1
doc_brief: "ON BLOCKS OF DELIGNE’S CATEGORY Rep(St) — We describe blocks in Deligne’s category Re p(St)."
---
show that for ﬁxed d∈Z≥0, the non-semisimple blocks in Re p(Sd;F ) are all equi-
valent as additive categories. Thereafter we conjecture that a restriction func-
tor induces an equivalence of categories between certain non-semisimple blocks in
Rep(Sd;F ) and Re p(Sd−1;F ). First, let us ﬁx some notation. Given a block B in
Rep(Sd;F ), let IncB :B→ Rep(Sd;F ) and ProjB : Re p(Sd;F )→B denote the
inclusion and projection functors respectively.
Proposition 6.6. SupposeB is a nontrivial block in Rep(Sd;F ) which is not min-
imal with respect to≺. There exists a block B′ in Rep(Sd;F ) withB′⪵B such that
ProjB′◦(−⊗ L(2))◦ IncB :B→B ′ is an equivalence of additive categories. Hence,
all nontrivial blocks in Rep(Sd;F ) are all equivalent as additive categories.
Proof. First, noticed⁄= 0 as we are assuming a nontrivial block exists in Rep(Sd;F ).
Hence, Liftd(L(2)) = L(2) (see Example 3.11(1)). Let B ={λ(0)⊂ λ(1)⊂···}
denote the set of Young diagrams corresponding to indecomposable objects in B.
Now, let B′ ={ρ(0)⊂ ρ(1)⊂···} be the set of Young diagrams given by Lemma
5.18(2), andB′ the corresponding block. By Lemma 5.20 we have the following
Liftd(L(λ(0))) = L(λ(0)),
Liftd(L(λ(i))) = L(λ(i))⊕L(λ(i−1)) ( i> 0),
Liftd(L(ρ(0))) = L(ρ(0)),
Liftd(L(ρ(i))) = L(ρ(i))⊕L(ρ(i−1)) ( i> 0).
Hence, by Proposition 3.12(1) and Lemma 5.18(2),
Liftd(L(λ(i))⊗L(2)) = Lift d(L(λ(i)))⊗L(2) = Lift d(L(ρ(i)))⊕A,
Liftd(L(ρ(i))⊗L(2)) = Lift d(L(ρ(i)))⊗L(2) = Lift d(L(λ(i)))⊕B,
in Rep(ST ;K) for alli≥ 0, whereA (resp. B) is an object in Rep(ST ;K) with no in-
decomposable summands of the formL(ρ(j)) (resp. L(λ(j))). Thus, by Propositions
3.12(3) and 5.19, L(λ(i))⊗L(2) =L(ρ(i))⊕A′ and L(ρ(i))⊗L(2) =L(λ(i))⊕B′
in Re p(Sd;F ) for all i ≥ 0, where A′ (resp. B′) is an object in Re p(Sd;F )
with no indecomposable summands of the form L(ρ(j)) (resp. L(λ(j))). Hence,
40 JONATHAN COMES AND VICTOR OSTRIK
ProjB′◦(−⊗ L(2))◦ IncB and ProjB◦(−⊗ L(2))◦ IncB′ are inverse to one an-
other on objects. Moreover, since ( −⊗ L(2)) is self-adjoint and Proj B is both
right and left adjoint to Inc B, it follows that Proj B◦(−⊗ L(2))◦ IncB′ is adjoint
to ProjB′◦(−⊗ L(2))◦ IncB. The result follows. □
Next, we use the universal property of Re p(St;F ) (see [Del07, 8.3]) to deﬁne a
restriction functor.
Deﬁnition 6.7. Let ResSt
St−1 : Rep(St;F )→ Rep(St−1;F ) denote the functor given
by the universal property of Rep(St;F ) which sends ([1], id1)↦→ ([1], id1)⊕([0], id0).
Conjecture 6.8. Ford∈Z≥0, let Bd denote the nontrivial block in Re p(Sd;F )
containing the object L(∅). Then the functor ProjBd◦ResSd+1
Sd ◦ IncBd+1 induces an
equivalence of additive categoriesBd+1∼=Bd.
Remark 6.9. It is not hard to show that ProjBd◦ResSd+1
Sd ◦ IncBd+1 is bijective on
objects. Hence, to prove Conjecture 6.8 it suﬃces to show ProjBd◦ResSd+1
Sd ◦IncBd+1
is either full or faithful.

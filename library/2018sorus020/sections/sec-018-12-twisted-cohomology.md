---
doc_id: 2018sorus020
doc_title: "HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific re- search documents, whether they are published or not"
section_id: sec-018-12-twisted-cohomology
section_title: "Twisted cohomology"
section_number: 1.2
pages: 27-30
source_pdf: 2018SORUS020.pdf
source_sha256: c3f929e5195983ce
doc_brief: "HAL Id: tel-02108892 HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific re- search documents, whether they are published or not — 78 sections: Introduction"
---
In this section we recall the basics of twisted cohomology that we will use in the
sequel of the manuscript. Given a groupΓ, we will denote byZ[Γ] the group ring of
Γ, whose elements are formal sums∑
γ∈Γnγeγ,nγ∈ Z with multiplicationeγeδ =eγδ
extended by linearity.
We ﬁx an abelian groupA together with a left-actionΓ×A→A, (γ,a )↦→γ·a. It
induces a right-action bya·γ =γ−1·a. It turnsA into a Z[Γ]-module.
Deﬁnition 1.2.1(Group homology and cohomology). Let EΓ be the full simplex
set over Γ, that is, the vertices ofEΓ are in bijection withΓ, and any ﬁnite part of
Γ of cardinaln deﬁnes ann− 1 simplex inEΓ. This space is contractile, and the
natural transitive action ofΓ on itself by left multiplication induces an action on
EΓ, denote byBΓ =EΓ/Γ.
Deﬁne thecomplex of twisted chainsas the Z[Γ]-modules :
Ck(Γ,A ) =A⊗Z[Γ]Ck(EΓ)
={a⊗ [γ0,...,γ k] :∀γ∈ Γ,a·γ⊗ [γ0,...,γ k] =a⊗ [γγ0,...,γγ k]}
and thecomplex of twisted co-chainsas the Z[Γ]-modules :
Ck(Γ,A ) = HomZ[Γ](Ck(EΓ),A )
={f : Γk+1→A :f(γγ0,...,γγ k) =γ·f(γ0,...,γ k)}
with boundary maps given by∂(a⊗ [γ0,...,γ k]) =∑
i(−1)ia⊗ [γ0,..., ˆγi,...,γ k]∈
Ck−1(Γ,A ) anddf(γ0,...,γ k+1) =∑
i(−1)if(γ0,..., ˆγi,...,γ k+1)∈Ck+1(Γ,A ). Re-
call that the hat notation means that the term with a hat does not appear.
As usual we denote by
Zk(Γ,A ) = ker∂ :Ck(Γ,A )→Ck−1,Z k(Γ,A ) = kerd :Ck(Γ,A )→Ck+1(Γ,A )
and
Bk(Γ,A ) = im∂ :Ck+1(Γ,A )→Ck(Γ,A ),Bk(Γ,A ) = imd :Ck−1(Γ,A )→Ck(Γ,A )
We deﬁne the twisted homologyZ-modules as
Hk(Γ,A ) =Zk(Γ,A )/Bk(Γ,A )
26
and the twisted cohomologyZ-modules as
Hk(Γ,A ) =Zk(Γ,A )/Bk(Γ,A )
Remark 1.2.2. When A = Z and Γ acts trivially, then what we deﬁned is the
homology (resp cohomology) of the spaceBΓ. We will generalize this observation
later.
Remark1.2.3. Forcomputation,wewillusethefollowingnonhomogeneousconven-
tion for the group homology and cohomology : the homological complex will be
Ci(Γ,A ) ={a⊗ [γ1,...,γ i]| a∈A,γk∈ Γ}
with boundary
δ(a⊗[γ1,...,γ i]) =a.γ1⊗[γ2,...,γ i]−a⊗[γ1γ2,...,γ i]+... +(−1)ia⊗[γ1,...,γ i−1]
and the cohomological complex will be
Ci(Γ,A ) ={f :Gi→A}
with boundary
df(γ1,...,γ i) =γ1.f(γ2,...,γ i)−f(γ1γ2,...,γ i) +... + (−1)if(γ1,...,γ i−1)
It is a straightforward computation to show that those conventions deﬁne isomorphic
complexes, hence the same homology.
In the sequel we ﬁx a ﬁnite connected CW-complexK with universal cover˜K, which
will be in general a cell decomposition of a compact manifoldM and we denote by
Γ = π1(M) its fundamental group. If{ek
1,...,e k
rk} is the family ofk-dimensional
cells ofK, we denote by{˜ek
1,..., ˜ek
rk} a choice of lifts in˜K, it provides aZ[Γ]-basis
of the Z[Γ]-module Ck( ˜M).
Again we ﬁx an abelian groupA, and a left-action ofΓ on A.
Deﬁnition 1.2.4(Twisted homology and cohomology). We deﬁne the homological
and cohomological twisted complexes
Ck(M,A ) =A⊗Z[Γ]Ck( ˜M) and Ck(M,A ) = HomZ[Γ](Ck( ˜M),A )
27
with boundary maps∂(a⊗ek
i ) = a⊗∂ek
i and df(ek
i ) = (−1)if(∂ek
i ). Finally, the
twistedhomologyandcohomologyof M arethe Z-modulesHk(M,A )andHk(M,A ).
This deﬁnitions extend naturally to relative homology and cohomology in the case
when M has a non-empty boundary∂M.
Remark 1.2.5. The generalization of Remark 1.2.2 is that the homology (resp.
cohomology) H∗(Γ,A ) of the group Γ is the twisted homology (resp. cohomology)
H∗(BΓ,A ) of the spaceBΓ.
A classical fact, that is a consequence of this remark, is the following theorem, see
for instance [Bro82].
Theorem 1.2.6.If ˜M is contractible, then we have the natural isomorphisms
Hk(M,A )≃Hk(Γ,A ) and Hk(M,A )≃Hk(Γ,A )
Moreover, without hypothesis onM, the following is proved in [Por97, Lemma 0.6].
Proposition 1.2.7. Fori = 0, 1, we have the natural isomorphisms :
Hi(M,A )≃Hi(Γ,A ) and Hi(M,A )≃Hi(Γ,A )
We will be interested in the case whenA is a free module of ﬁnite type (or a vector
space)V over ak-algebraR, together with a bilinear non-degenerate invariant form
B : V ×V → R, hence we can deﬁne the following operation in homology and
cohomology :
— The Kronecker product
⟨·,·⟩ :Hk(M,V )×Hk(M,V )→R
(f,v ⊗ek
i )↦→B(v,f (ek
i ))
— The Universal Coeﬃcient Theorem
— ThePoincaré-Lefschetzduality Hi(M,∂M,V )≃Hn−i(M,V )∗≃Hn−i(M,V )
where n = dimM
— The cup-product :
·∪· :Hi(Γ,V )×Hj(Γ,V )→Hi+j(Γ,R )
(f,g )↦→
(
(γ1,...,γ i,γi+1,...,γ i+j)↦→ (−1)ijB(f(γ1,...,γ i),g (γi+1,...,γ i+j)
)
28

---
doc_id: arxiv-1412.4229v4
doc_title: "THE SQUARING OPERATION FOR COMMUTATIVE DG RINGS"
section_id: sec-007-7-the-squaring-operation
section_title: "The Squaring Operation"
section_number: 7
pages: 38-43
source_pdf: 1412.4229v4.pdf
source_sha256: 248d6a1e28a76a94
toc_source: outline
doc_brief: "THE SQUARING OPERATION FOR COMMUTATIVE DG RINGS — Let A →B be a homomorphism of commutative rings."
---
In this section all DG rings are commutative; namely, we work inside the category
DGR≤0
sc . See Deﬁnition 3.3. The category PDGR≤0
sc of commutative pairs of DG rings
was introduced in Deﬁnition 3.7(2); it is a full subcategory of the category PDGR
of central pairs of DG rings.
Deﬁnition 7.1.
(1) Let B/A be an object of PDGR≤0
sc . A K-ﬂat resolution of
B/A in PDGR≤0
sc is a resolution s/r : ˜B/ ˜A →B/A in the sense of Deﬁnition
3.8, such that the pair ˜B/ ˜A is commutative and K-ﬂat (Deﬁnition 3.11(3)).
(2) Morphisms of resolutions in PDGR≤0
sc , and resolutions of morphisms in
PDGR≤0
sc , are as in Deﬁnition 3.9, but all the pairs are now commutative.
Proposition 7.2. Any object and any morphism in PDGR≤0
sc admits a K-ﬂat res-
olution.
Proof. Like the proof of Corollary 3.25, but using commutative semi-free resolu-
tions.
□
For a commutative DG ring B we have Bce = B of course. This is used in the
following deﬁnitions.
Deﬁnition 7.3. Let B/A be a pair of commutative DG rings, and let M be a DG
B-module. Given a K-ﬂat resolution ˜B/ ˜A of B/A in PDGR≤0
sc , we let
Sq
˜
B/ ˜
A
B/A(M) := Rect
˜
B/ ˜
A
B/A(M, M) ∈D(B).
See Proposition 5.15.
THE SQUARING OPERATION
39
Deﬁnition 7.4. Let w/v : B′/A′ →B/A be a morphism in PDGR≤0
sc , let M ∈
D(B), let M ′ ∈D(B′), and let θ : M →M ′ be a morphism in D(B′). Given a
K-ﬂat resolution ˜w/˜v : ˜B′/ ˜A′ →˜B/ ˜A of w/v in PDGR≤0
sc , we deﬁne
Sq ˜
w/˜v
w/v(θ) : Sq
˜
B/ ˜
A
B/A(M) →Sq
˜
B′/ ˜
A′
B′/A′(M ′)
to be the morphism
Sq ˜
w/˜v
w/v(θ) := Rect ˜
w/˜v
w/v(θ, θ)
in D(B′) from Proposition 5.16.
Remark 7.5. As explained in Remark 5.18, we can write
Sq
˜
B/ ˜
A
B/A(M) = RHom ˜
Ben(B, M ⊗L
˜
A M).
However, the morphism Sq ˜
w/˜v
w/v(θ) in Deﬁnition 7.4 is not standard, so we have to
use the more explicit approach with compound resolutions, as was done in Section
5.
Still, here we can simplify matters by using symmetric compound resolutions.
A symmetric compound resolution of a DG B-module M is data P = ( ˜P, ˜I; α, β),
consisting of a K-ﬂat resolution α : ˜P →M in M( ˜B), and a K-injective resolution
β : ˜P en = ˜P ⊗˜
A ˜P →˜I in M( ˜Ben).
Likewise, a morphism θ : M →M ′ can be resolved by a symmetric compound
morphism η : P →P ′, where η = ( ˜Q; γ, ˜θ, η) consists of a K-projective resolution
γ : ˜Q →˜P in M( ˜B′); a homomorphism ˜θ : ˜Q →˜P ′ in M( ˜B′) lifting θ; and a
homomorphism η : ˜I →˜I′ in M( ˜B′ en) lifting
˜θ ⊗˜θ : ˜Q ⊗˜
A′ ˜Q →˜P ′ ⊗˜
A′ ˜P ′.
Here is the key technical result of our paper (Theorem 0.3.3 in the Introduction).
Actually, it is just a special case of Theorem 6.11.
Theorem 7.6 (Homotopy Invariance). Let w/v : B′/A′ →B/A be a morphism
in PDGR≤0
sc , let M ∈D(B), let M ′ ∈D(B′), and let θ : M →M ′ be a mor-
phism in D(B′). Suppose ˜B/ ˜A and ˜B′/ ˜A′ are K-ﬂat resolutions of B/A and B′/A′
respectively in PDGR≤0
sc , and
˜w0/˜v0, ˜w1/˜v1 : ˜B′/ ˜A′ →˜B/ ˜A
are morphisms of resolutions above w/v. Then the morphisms
Sq ˜
w0/˜v0
w/v
(θ), Sq ˜
w1/˜v1
w/v
(θ) : Sq
˜
B/ ˜
A
B/A(M) →Sq
˜
B′/ ˜
A′
B′/A′(M ′)
in D(B′) are equal.
Proof. Take M l = M r := M, M ′ l = M ′ r := M ′, and θl = θr := θ in Theorem
6.11.
□
This brings us to the ﬁrst main theorem of the paper (which is Theorem 0.3.4
in the Introduction).
Theorem 7.7 (Existence of Squares). Let A →B be a homomorphism of commu-
tative DG rings, and let M be a DG B-module. There is a DG module SqB/A(M),
unique up to a unique isomorphism in D(B), together with an isomorphism
sq
˜
B/ ˜
A : SqB/A(M)
≃
−→Sq
˜
B/ ˜
A
B/A(M)
in D(B) for each K-ﬂat resolution ˜B/ ˜A of B/A in PDGR≤0
sc , satisfying the following
condition.
40
AMNON YEKUTIELI
(∗) Let ˜w/˜v : ˜B′/ ˜A′ →˜B/ ˜A be a morphism of K-ﬂat resolutions of B/A in
PDGR≤0
sc . Then there is equality
Sq ˜
w/˜v
id/id(idM) = sq
˜
B′/ ˜
A′ ◦(sq
˜
B/ ˜
A)−1
of isomorphisms Sq
˜
B/ ˜
A
B/A(M)
≃
−→Sq
˜
B′/ ˜
A′
B/A (M) in D(B).
Proof. The proof is very similar to that of Theorem 6.15: we ﬁx a universal K-ﬂat
resolution of B/A; but now it has to be a commutative resolution. So let ˜Aun/Z
be a commutative semi-free resolution of A/Z, and let ˜Bun/ ˜Aun be a commutative
semi-free resolution of B/ ˜Aun, both in PDGR≤0
sc . This is possible by Theorem 3.21.
Deﬁne
SqB/A(M) := Sq
˜
Bun/ ˜
Aun
B/A
(M).
Given any K-ﬂat resolution ˜B/ ˜A of B/A in PDGR≤0
sc , Theorem 3.22 says there
is a morphism of resolutions
˜wun/˜vun : ˜Bun/ ˜Aun →˜B/ ˜A.
We deﬁne the isomorphism
sq
˜
B/ ˜
A : Sq
˜
Bun/ ˜
Aun
B/A
(M)
≃
−→Sq
˜
B/ ˜
A
B/A(M)
to be
sq
˜
B/ ˜
A := Sq ˜
wun/˜vun
id/id
(idM)−1.
The veriﬁcation of condition (∗) is the same as in the proof of Theorem 6.15,
except that here we use Theorem 7.6 instead of Theorem 6.11.
□
Deﬁnition 7.8. A triple in DGR≤0
sc is the data of homomorphisms A
u−→B
v−→C
in DGR≤0
sc . We refer to this triple as C/B/A.
A commutative K-ﬂat resolution of C/B/A is a triple ˜A
˜u−→˜B
˜v−→˜C in DGR≤0
sc ,
together with homomorphisms r : ˜A →A, s : ˜B →B and t : ˜C →C in DGR≤0
sc ,
such that:
• r is a quasi-isomorphism, and s, t are surjective quasi-isomorphisms.
• s ◦˜u = u ◦r and t ◦˜v = v ◦s.
• ˜u and ˜v ◦˜u are K-ﬂat.
See diagram (0.2.4) in the Introduction. A commutative K-ﬂat resolution ˜A
˜u−→
˜B
˜v−→˜C can be viewed as follows: K-ﬂat resolutions s/r : ˜B/ ˜A →B/A and
t/r : ˜C/ ˜A →C/A in PDGR≤0
sc , and a morphism of resolutions ˜v/id ˜
A : ˜B/ ˜A →˜C/ ˜A
above the morphism of pairs v/idA : B/A →C/A.
Proposition 7.9. Commutative K-ﬂat resolutions of triples exist.
Proof. This follows from Theorems 3.21 and 3.22. Compare to the proof of Corol-
lary 3.25.
□
Here is the second main theorem of the paper (which is Theorem 0.3.5 in the
Introduction).
Theorem 7.10 (Trace Functoriality). Let A −→B
v−→C be homomorphisms of
commutative DG rings, let M ∈D(B), let N ∈D(C), and let θ : N →M be a
morphism in D(B). There is a unique morphism
Sqv/idA(θ) : SqC/A(N) →SqB/A(M)
in D(B), satisfying the condition:
THE SQUARING OPERATION
41
(∗∗) For any commutative K-ﬂat resolution ˜A →˜B
˜v−→˜C of the triple A →B
v−→
C, there is equality
Sq˜v/id ˜
A
v/idA(θ) = sq
˜
B/ ˜
A ◦Sqv/idA(θ) ◦(sq
˜
C/ ˜
A)−1
of morphisms Sq
˜
C/ ˜
A
C/A(N) →Sq
˜
B/ ˜
A
B/A(M) in D(B).
Proof. We begin by choosing a universal K-ﬂat resolution of the triple A
u−→B
v−→C.
We choose, in this order, commutative semi-free resolutions run/id : ˜Aun/Z →A/Z,
sun/run : ˜Bun/ ˜Aun →B/ ˜Aun and tun/sun : ˜Cun/ ˜Bun →C/ ˜Bun. In this way we
obtain a K-ﬂat resolving triple ˜Aun
˜uun
−−→˜Bun
˜vun
−−→˜Cun of A
u−→B
v−→C. Now we
deﬁne
Sqv/idA(θ) := (sq
˜
Bun/ ˜
Aun)−1 ◦Sq
˜vun/id ˜
Aun
v/idA
(θ) ◦sq
˜
Cun/ ˜
Aun .
Let us verify condition (∗∗).
We are given an arbitrary commutative K-ﬂat
resolution ˜A
˜u−→˜B
˜v−→˜C of the triple A →B
v−→C. According to Theorem 3.22 we
can ﬁnd homomorphisms ˜r : ˜Aun →˜A, ˜s : ˜Bun →˜B and ˜t : ˜Cun →˜C, such that
the diagram below in PDGR≤0
sc is commutative.
(7.11)
˜Bun/ ˜Aun
˜vun/id
/
˜s/˜r

sun/run
!
˜Cun/ ˜Aun
˜t/˜r

tun/run
}
˜B/ ˜A
˜v/id
/
s/r

˜C/ ˜A
t/r

B/A
v/id
/ C/A
Now let us look at the corresponding diagram with the squaring operation. It is
a diagram in D(B).
Sq
˜
Bun/ ˜
Aun
B/A
(M)
Sq
˜
Cun/ ˜
Aun
C/A
(N)
Sq˜vun/id
v/id
(θ)
o
Sq
˜
B/ ˜
A
B/A(M)
Sq˜s/˜r
id/id(id)
O
Sq
˜
C/ ˜
A
C/A(N)
Sq
˜t/˜r
id/id(id)
O
Sq˜v/id
v/id(θ)
o
SqB/A(M)
sq
˜
Bun/ ˜
Aun
=
sq
˜
B/ ˜
A
O
SqC/A(N)
sq
˜
C/ ˜
A
O
Sqv/id(θ)
o
sq
˜
Cun/ ˜
Aun
]
The top square is commutative by Proposition 5.17 (applied twice). The two
half-moons are commutative by condition (∗) of Theorem 7.7. The outer paths are
equal by deﬁnition of Sqv/id(θ). Because the vertical arrows are isomorphisms, we
conclude that the bottom square is commutative. This is what we had to prove.
□
Corollary 7.12. Let B/A be a pair of commutative DG rings. The assignments
M 7→SqB/A(M)
and
θ 7→SqidB/idA(θ)
are a functor
SqB/A : D(B) →D(B).
42
AMNON YEKUTIELI
Proof. Consider morphisms M0
θ1
−→M1
θ2
−→M2 in D(B). A combination of Propo-
sition 5.17 and condition (∗∗) of Theorem 7.10 shows that
Sqid/id(θ2) ◦Sqid/id(θ1) = Sqid/id(θ2 ◦θ1).
And by Lemma 5.12, Sqid/id(idM) = idSqB/A(M).
□
Deﬁnition 7.13. The object SqB/A(M) from Theorem 7.7 is called the square
of M over B relative to A. The functor SqB/A from Corollary 7.12 is called the
squaring operation over B relative to A.
The following result says that the squaring operation SqB/A is also functorial in
the DG ring B.
Proposition 7.14. We are given homomorphisms of commutative DG rings A →
B2
v2
−→B1
v1
−→B0, DG modules Mk ∈D(Bk), and morphisms θk : Mk−1 →Mk in
D(Bk). Then
Sqv2/idA(θ2) ◦Sqv1/idA(θ1) = Sq(v1◦v2)/idA(θ2 ◦θ1),
as morphisms SqB0/A(M0) →SqB2/A(M2) in D(B2).
Proof. Choose a K-ﬂat resolution ˜A −→˜B2
˜v2
−→˜B1
˜v1
−→˜B0 of A →B2
v2
−→B1
v1
−→B0,
in the obvious sense that generalizes Deﬁnition 7.8. According to condition (∗∗) of
Theorem 7.10, it suﬃces to prove that
Sq˜v2/id
v2/id(θ2) ◦Sq˜v1/id
v1/id(θ1) = Sq(˜v1◦˜v2)/id
(v1◦v2)/id(θ2 ◦θ1),
as morphisms Sq
˜
B0/ ˜
A
B0/A(M0) →Sq
˜
B2/ ˜
A
B2/A(M2) in D(B2). This is true by Proposition
5.17.
□
Proposition 7.15. Let A be a commutative DG ring. The action from Proposition
2.5(1) makes D(A) into an H0(A)-linear category.
Proof. Because A0 is in the center of A, and d(A0) = 0, we see that M(A) is an A0-
linear category. See formula (1.15). Next, from formula (2.1) we see that K(A) is an
H0(A)-linear category. Hence its localization D(A) is an H0(A)-linear category.
□
Given a homomorphism B →C of commutative DG rings, and objects M ∈
D(B) and N ∈D(C), the set HomD(B)(N, M) is an H0(C)-module, with action
coming the action of H0(C) on N as an object of D(C), as in the proposition above.
We end the paper with the next result.
Theorem 7.16. In the situation of Theorem 7.10, let c ∈H0(C). Then
Sqv/id(c · θ) = c2 · Sqv/id(θ),
as morphisms
SqC/A(N) →SqB/A(M)
in D(B).
Proof. Choose a K-ﬂat resolution ˜B/ ˜A of B/A. Then choose a strict commuta-
tive semi-free resolution ˜C/ ˜B of C/ ˜B. Putting them together we obtain a K-ﬂat
resolution ˜A −→˜B
˜v−→˜C of A →B
v−→C, where ˜v is commutative semi-free. Let
P M = ( ˜PM, ˜IM; αM, βM) be a symmetric compound resolution of M over ˜B/ ˜A,
and let P N = ( ˜PN, ˜IN; αN, βN) be a symmetric compound resolution of N over
˜C/ ˜A. See Remark 7.5 and Deﬁnition 5.8.
Because ˜PN is K-projective over ˜B, we can ﬁnd a homomorphism ˜θ : ˜PN →˜PM
in M( ˜B) that lifts θ. We obtain a symmetric compound morphism η : P N →P M,
THE SQUARING OPERATION
43
η := ( ˜PN; id ˜
PN , ˜θ, η) above θ and ˜v/id ˜
A. Speciﬁcally, the homomorphism η : ˜IN →
˜IM in M( ˜Ben) is a lift of
˜θ ⊗˜θ : ˜PN ⊗˜
A ˜PN →˜PM ⊗˜
A ˜PM.
By Proposition 5.16, Sqv/id(θ) is represented by
Homven(v, η) : HomCen(C, ˜IN) →HomBen(B, ˜IM).
We remind that ˜Ben = ˜B ⊗˜
A ˜Bop and ˜Cen = ˜C ⊗˜
A ˜Cop.
Now choose some ˜c ∈˜C0 that represents the cohomology class c ∈H0(C) ∼=
H0( ˜C). Then ˜c · ˜θ : ˜PN →˜PM lifts c · θ : N →M, and (˜c ⊗˜c) · η : ˜IN →˜IM lifts
(˜c · ˜θ) ⊗(˜c · ˜θ). We get a symmetric compound morphism ηc : P N →P M,
ηc :=
  ˜PN; id ˜
PN , ˜c · ˜θ, (˜c ⊗˜c) · η

resolving c · θ. But then the homomorphism
Homven(v, (˜c ⊗˜c) · η) = Homven(˜c2 · v, η) = ˜c2 · Homven(v, η)
represents Sqv/id(c · θ).
□
This theorem shows that the functor SqB/A is a quadratic functor.

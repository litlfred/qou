---
doc_id: invariant-eigendistributions-2
doc_title: "REPRESENTATIONS OF WEYL GROUPS 1 Invariant eigendistributions on a semisimple Lie algebra and homology classes on the conormal variety II: representations of Weyl groups W. ROSSMAN"
section_id: sec-013-31-lemma-the-inclusion-bν-b-induces-a-w-map-hbν
section_title: "Lemma. The inclusion Bν →B induces a W-map H∗(Bν) → H∗(B). This map factors"
section_number: 3.1
pages: 4-6
source_pdf: Invariant_eigendistributions_2.pdf
source_sha256: ee43c3ebeff95265
doc_brief: "REPRESENTATIONSOFWEYL GROUPS 1 Invariant eigendistributions on a semisimple Lie algebra and homology classes on the conormal variety II: representations of Weyl groups W. ROSSMANN1 — 25 sections: Intr"
---
through the projection H∗(Bν)→H∗(Bν)A(ν) onto the A(ν)-invariants.
REPRESENTATIONS OF WEYL GROUPS 5
Proof. It suﬃces to show that the homotopyequivalence of Bν constuct above has a representative
Bν →B ν, denotedaν(w), so that the inclusioni :Bν →B satisﬁes
i◦aν(w)∼a(w)◦i.
Choose a neighbourhoodV ofBν for which the inclusionk :Bν →V has a homotopyinverseq :V →B ν:
q◦k ∼ 1o nBν,k ◦q ∼ 1o nV.
Let U ={(b,ν ′): b∈V,|ν′|≤ R} for some ﬁxedR> |ν|. Deﬁne maps
j :Bν →U,j(b)=( k(b),ν)=( b,ν),p :V →B ν,p(b,ν ′)= q(b).
We show that
p◦j ∼ 1o nBν,j ◦p∼ 1o nU. (1)
The ﬁrst relation is clear since
p◦j(b)= q◦k(b)a n dq◦k ∼ 1o nBν.
To see the second relation, usek◦q ∼ 1 to choose a homotopyqs : V → V,0 ≤ s ≤ 1, fromq0 =1 V to
q1 =k◦q. Perform successivelythe following homotopies of mapsU →U :
(1) (b,ν ′)→ (b,sν ′), s going from 1 to 0,
(2) (b,ν ′)→ (qs(b),0), s going from 0 to 1,
(3) (b,ν ′)→ (k◦q(b),sν), s going from 0 to 1.
This gives a homotopyfrom the identity1U :(b,ν ′)→ (b,ν ′)t op◦j :(b,ν ′)→ (k◦q(b),ν) as required.
Forλcloseto0, aλ(w)j(Bν)staysin the neighbourhoodU ofj(Bν). Therelation(1)showsthatthe
p,j can take the placeof thep,i in the deﬁnition (2.7) ofaν(w). For suchλthe mapp◦aλ(w)◦j :Bν →B ν
therefore represents the homotopyclassaν(w):
aν(w)∼p◦aλ(w)◦j :Bν →B ν. (2)
For 0≤s≤ 1, deﬁne of maps
js :Bν →U,js(b)=( b,sν),p s :U →V,ps(b,ν ′)= qs(b)
with qs as above. Consider the homotopyof maps
ps ◦aλ(w)◦js :Bν →V, 0≤s≤ 1. (3)
For s = 0 we get
po ◦aλ(w)◦jo(b)= qo ◦aλ(w)(b,0) =a(w)b
becauseaλ(w)a n da(w)c o i n c i d eo nB consideredas the zerosection inB∗: this is clear fromthe deﬁnition
of aλ(w). So fors = 0, (3) reduces toa(w)◦i. On the other hand, fors =1w eg e t
p1 ◦aλ(w)◦j1(b)= p◦aλ(w)(b,ν)) =p◦aλ(w)◦j(b)) =aν(b)b
by(2). So fors =1,(3) reduces toaν(w)◦i. Hence (3) provides the desired homotopyi◦aν(w)∼a(w)◦i.
REPRESENTATIONS OF WEYL GROUPS 6
To see the second assertion of the lemma one onlyhas to note that the action of the stabilizer of
ν in U, which induces the action ofA(ν)i nH∗(Bν), becomes trivial inH∗(B)a sU is connected. This
proves the lemma.

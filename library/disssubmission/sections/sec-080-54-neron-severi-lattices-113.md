---
doc_id: disssubmission
doc_title: "Tannakian categories of perverse sheaves on abelian varieties"
section_id: sec-080-54-neron-severi-lattices-113
section_title: "N´eron-Severi lattices 113"
section_number: 5.4
pages: 121-123
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
doc_brief: "Tannakian categories of perverse sheaves on abelian varieties — 121 sections: Acknowledgements; Introduction; Introduction"
---
Proof. This is a direct application of the criterion for the extension of
lattice isomorphisms in [62]. Let us brieﬂy check that the two conditions
in loc. cit. are satisﬁed in this case: The ﬁrst condition is that the rankr
of the two primitive sublattices and the signature(s+,s−) = (35,51) of the
ambient latticeLY satisfy
2(r +1)≤ (s+ +s−)−|s+−s−|,
which in the present situation is granted by our assumption thatr≤34. The
second condition concerns primitive vectorsv∈ LY which are characteristic
in the sense thatb(v,w)≡ b(w,w) mod 2Z for all vectorsw∈ LY. But in the
case at hand this condition is void because an even unimodular lattice does
not contain any primitive characteristic vectors. So by loc. cit. the given
isomorphismϕ0 can be extended to an automorphismϕ as claimed. □
To ﬁnish the proof of proposition 5.12 it remains to deal with the square
on the left hand side in the diagram of that proposition. For this we need to
compute the image of the weak Lefschetz embedding, by which we mean
the sublattice
LX = H2(X,Z)⊂ L+
Y = H2(Y,Z)+.
Note thatK =U12⊕Λ has signature(13,15) and discriminant−3 whereas
the even unimodular latticeL = U13⊕E8(−1) has signature(13,21). So
the orthocomplementK⊥ of any embedding
i : K ↪→ L
must be a negative deﬁnite even lattice of rank six with discriminant 3,
hence abstractly isomorphic toE6(−1) by the classiﬁcation of lattices with
small discriminant in [21]. Thus the proof of proposition 5.12 is completed
by the following computation.
LEMMA 5.17. With notations as above, there exists an isomorphism of
lattices
LX
∼=−→K(2).
Proof.Consider the embeddingi : Y = Θ∩Θx ↪→ X. By deﬁnition the
Gysin morphismi! on cohomology is the Poincar´e dual of the pushforward
morphismi∗ on homology, so we have a commutative diagram
Hn(Y,Z)
i! //
∼=

Hn+4(X,Z)
∼=

H4−n(Y,Z)
i∗ // H4−n(X,Z).
114 Chapter 5 – A family of surfaces
If 1∈ H0(Y,Z) denotes the unit element of the cohomology ring ofY, the
fundamental cohomology class ofY in X is i!(1) = [Y]∈ H4(X,Z). So the
projection formula shows
i!(i∗(γ)) = i!(i∗(γ)∪1) = γ∪i!(1) = γ∪[Y]
for all cohomology classesγ∈ H4(X,Z). This being said, it follows from
the commutative diagram
H2(X,Z)×H2(X,Z) ∪ //
i∗

H4(X,Z)
−∪[Y] //
i∗

H8(X,Z)
degX

H2(Y,Z)×H2(Y,Z) ∪ // H4(Y,Z)
degY //
i!
77ooooooooooo
Z
that the intersection form onH2(Y,Z) restricts on the subspaceH2(X,Z) to
the bilinear form
b : H2(X,Z)×H2(X,Z)−→Z, (α,β)↦→degX(α∪β∪[Y]).
We want to compute this bilinear form. Since the intersection product in
homology corresponds to the cup product in cohomology, the fundamental
class ofY in cohomology is
[Y] = [ Θ∩Θx] = [ Θ]∪[Θx] = [ Θ]2.
To compute this class explicitly, we choose a basis of the cohomology ring
of X as follows. The principal polarization onX is given by an alternating
bilinear form onH1(X,Z). Take an integral basis
λ1, . . . ,λ4, µ1, . . . ,µ4∈ H1(X,Z)∼= Z8
with respect to which this alternating form is given by(λi,λk) = (µi, µk) =0
and (λi, µk) =−(µk,λi) = δik for alli, k, and denote by
x1, . . . ,x4,y1, . . . ,y4∈ H1(X,Z) = Hom(H1(X,Z),Z)
the dual basis. Since the Chern class[Θ] =c1(OX(Θ)) deﬁnes the principal
polarization, it follows that in the exterior algebraH•(X,Z) =Λ•(H1(X,Z))
this class is given by
[Θ] =
4
∑
i=1
xi∧yi∈ H2(X,Z).
The cup product in cohomology corresponds to the wedge product in the
exterior algebra, so we get
[Y] = [ Θ]2 =
( 4
∑
i=1
xi∧yi
)
∧
( 4
∑
j=1
xj∧yj
)
= 2·∑
1≤i<j≤4
xi∧yi∧xj∧yj.

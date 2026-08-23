---
doc_id: disssubmission
doc_title: "Tannakian categories of perverse sheaves on abelian varieties"
section_id: sec-075-53-integral-cohomology-107
section_title: "Integral cohomology 107"
section_number: 5.3
pages: 115-116
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
doc_brief: "Tannakian categories of perverse sheaves on abelian varieties — 121 sections: Acknowledgements; Introduction; Introduction"
---
is an isomorphism fork <n−1 and an epimorphism fork =n−1. Applying
this ﬁrst to the ample divisorΘ⊂ X and then to the ample divisorY⊂ Θ,
we in particular obtain that
Hn(Y,Z)∼= Hn(X,Z) and Hn(Y,Z)∼= Hn(X,Z) for n < 2.
In particular, the weak Lefschetz theorem for cohomology implies that the
groups Hn(Y,Z) have the claimed form forn < 2. Similarly, for n > 2
the corresponding statement follows from the weak Lefschetz theorem for
homology becauseHn(Y,Z)∼= H4−n(Y,Z) by Poincar´e duality. For anyn
we furthermore have an exact sequence
0−→Ext(Hn−1(Y,Z),Z)| {z }
torsion group
−→Hn(Y,Z)−→Hom(Hn(Y,Z),Z)| {z }
torsion-free
−→0
by the universal coefﬁcient theorem. Puttingn = 2 and using that by the
weak Lefschetz theorem the groupH1(Y,Z)∼= H1(X,Z) is torsion-free so
thatExt(H1(Y,Z),Z) =0, we obtain that
H2(Y,Z)∼= Hom(H2(Y,Z),Z)
is a free abelian group. The rank of this group is equal toh2(Y) = 86 by
lemma 5.8. Altogether it then follows that the integral cohomology groups
ofY are those given in the table.
It remains to show thatq∗ : H2(Y+,Z)−→H2(Y,Z) is an epimorphism
onto theσ-invariants whose kernel is the torsion subgroup, and to determine
the groupsHn(Y+,Z). In the computation of these cohomology groups we
can in fact restrict our attention to degreesn≤ 2. Indeed, Poincar´e duality
says that
Hn(Y+,Z)∼= H4−n(Y+,Z)
for alln, hence by the universal coefﬁcient theorem we have (non-canonical)
isomorphisms
Hn(Y+,Z) ∼= Hn−1(Y+,Z)tor⊕Hn(Y+,Z)free
∼= H5−n(Y+,Z)tor⊕H4−n(Y+,Z)free
where the subscriptstor andfreerefer to the maximal torsion subgroup and
the maximal free abelian subgroup, respectively. So for the computation of
the groupsHn(Y+,Z) it sufﬁces to deal with degreesn≤2. This being said,
we can argue as follows.
Recall from topology [18, ex. VII.4(b)] that for every regular covering
map W−→W+ = W/Γ between connected, locally pathwise connected
topological spaces with Galois groupΓ = Aut(W/W+), one has a spectral
sequence
Epq
2 = Hp(Γ,Hq(W,Z)) =⇒ Hp+q(W+,Z)
108 Chapter 5 – A family of surfaces
where the left hand side denotes group cohomology with coefﬁcients in the
Γ-moduleHq(W,Z). We apply this forW = Y and Γ =⟨σ⟩. To compute
in this case some of theE2-terms, recall that the group cohomology of any
moduleM under the cyclic group⟨σ⟩∼= Z/2Z is given by
Hp(⟨σ⟩,M) =



ker(σ−1) for p = 0,
ker(σ +1)/im(σ−1) for p > 0 odd,
ker(σ−1)/im(σ +1) for p > 0 even.
Let us plug inM =Hq(Y,Z) withq∈{0,1,2}. Clearly onH0(Y,Z)∼= Z the
involutionσ acts trivially, whereas by the weak Lefschetz theorem we know
that onH1(Y,Z)∼= H1(X,Z)∼= Z8 the involutionσ acts by−1. Hence in
this case we have
ker(σ +1| Hq(Y,Z))
im(σ−1| Hq(Y,Z))
∼=
{
0 for q = 0,
(Z/2Z)8 for q = 1,
ker(σ−1| Hq(Y,Z))
im(σ +1| Hq(Y,Z))
∼=
{
Z/2Z for q = 0,
0 for q = 1.
In other words, in the case at hand theE2-tableau of the spectral sequence
takes the following form.
q
... ... ... ...

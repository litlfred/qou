---
doc_id: 2018sorus020
doc_title: "Reidemeister torsion on character varieties"
section_id: sec-027-2-for-each-componentσi-of-σ-the-homomorphismπ1σi
section_title: "For each componentΣi of Σ, the homomorphismπ1(Σi)→ π1(M) induced"
section_number: 2
pages: 36-37
source_pdf: 2018SORUS020.pdf
source_sha256: c3f929e5195983ce
doc_brief: "Reidemeister torsion on character varieties — 78 sections: Introduction; (−1)i+1; ByH∗(M, Ad◦ρ) (respectivelyH∗(M,ρ"
---
by inclusion is injective.
3. No component ofΣ is a sphere or is boundary parallel.
Remark 1.3.14.A compression diskD⊂M is an embedded disk inM such that
∂D lies inS and is not homotopically trivial inS. The second condition above is
equivalent to saying that there is no compression disk inM.
If S is a surface dual to aπ1 action on a tree T, there is a way to modify the
equivariant map f in order to avoid compression disks, spherical and boundary
parallel components, and hence to obtain a new surfaceΣ that is incompressible.
We refer the reader to the references given above, where a proof of this fact will be
found.
1.3.6 The split case.
Let Σbe an incompressible surface associated to an ideal pointv∈ ˆX. In this section
we suppose thatΣ is a union ofn parallel copiesΣi,i = 1,...,n and that each copy
35
splits M into two handlebodiesM =M1∪ΣiM2. ConsiderV (Σ) a neighborhood of
Σ homeomorphic toΣ1× [0, 1], and we consider the splittingM =M1∪V (Σ)M2. We
ﬁx a basepointp∈ Σ1, and we will denote byπ1(Σ) the fundamental group ofΣ1
based inp. We identifyπ1(V (Σ)) to π1(Σ), and the Seifert-Van Kampen Theorem
provides the amalgamated productπ1(M) =π1(M1)∗π1(Σ)π1(M2). A sketchy picture
is drafted in Figure 1.3.
M1
Σ1 Σn
M2
V (Σ)
p
Figure 1.3 – The splittingM =M1∪V (Σ)M2.
Lemma 1.3.15. One can chose a conjugate of the tautological representationρ :
Γ→ SL2(k(X)) that restricts to representationsρ1 and ρ2 from π1(M1),π 1(M2) to
SL2(k(X)) respectively; such that ρ1 is convergent and thatρΣ, its restriction to
π1(Σ), is residually reducible. Moreover, there is a convergent representationρ′
2 :
π1(M2)→ SL2(Ov) such thatρ2 =Unρ′
2U−1
n , withUn = (tn 0
0 1 ).
Proof. Let s1 ∈ Tv be a vertex in the Bass-Serre tree that is ﬁxed byπ1(M1),
and ﬁx a basis such that it corresponds to the latticeO2
v. Then there is a vertex
s2∈ T, ﬁxed byπ1(M2), such thatd(s1,s 2) = n. Moreover, assume that in this
basis s2 has a representative of the formtnOv⊕O v. The ﬁrst observation is that
ρ1(π1(M1))⊂ SL2(Ov) because it stabilizesO2
v. SinceρΣ ﬁxes the ﬁrst edge of the
segment [s1s2], in this basis it ﬁxes the latticesO2
v and tOv⊕O v, hence for all
γ∈π1(Σ), ρΣ(γ) =
(
a(γ) b(γ)
c(γ) d(γ)
)
, withc(γ)∈ (t), hence ¯ρΣ is reducible.
Letρ′
2 =U−1
n ρ2Un, thenρ′
2·s1 =U−1
n ρ2·s2 =U−1
n ·s2 =s1 and we have proved that
the representationρ′
2 converges.

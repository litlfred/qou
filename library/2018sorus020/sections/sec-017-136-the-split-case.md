---
doc_id: 2018sorus020
doc_title: "Reidemeister torsion on character varieties"
section_id: sec-017-136-the-split-case
section_title: "The split case"
section_number: 1.3.6
pages: 36-37
source_pdf: 2018SORUS020.pdf
source_sha256: c3f929e5195983ce
toc_source: inferred
doc_brief: "Reidemeister torsion on character varieties — 52 sections: Front matter; Introduction; Character varieties and Reidemeist"
---
The split case.
Let Σ be an incompressible surface associated to an ideal point v ∈ˆX. In this section
we suppose that Σ is a union of n parallel copies Σi, i = 1, . . . , n and that each copy
35
splits M into two handlebodies M = M1 ∪Σi M2. Consider V (Σ) a neighborhood of
Σ homeomorphic to Σ1 × [0, 1], and we consider the splitting M = M1 ∪V (Σ) M2. We
ﬁx a basepoint p ∈Σ1, and we will denote by π1(Σ) the fundamental group of Σ1
based in p. We identify π1(V (Σ)) to π1(Σ), and the Seifert-Van Kampen Theorem
provides the amalgamated product π1(M) = π1(M1)∗π1(Σ)π1(M2). A sketchy picture
is drafted in Figure 1.3.
M1
Σ1
Σn
M2
V (Σ)
p
Figure 1.3 – The splitting M = M1 ∪V (Σ) M2.
Lemma 1.3.15. One can chose a conjugate of the tautological representation ρ :
Γ →SL2(k(X)) that restricts to representations ρ1 and ρ2 from π1(M1), π1(M2) to
SL2(k(X)) respectively ; such that ρ1 is convergent and that ρΣ, its restriction to
π1(Σ), is residually reducible. Moreover, there is a convergent representation ρ′
2 :
π1(M2) →SL2(Ov) such that ρ2 = Unρ′
2U −1
n , with Un = ( tn 0
0 1 ).
Proof. Let s1 ∈Tv be a vertex in the Bass-Serre tree that is ﬁxed by π1(M1),
and ﬁx a basis such that it corresponds to the lattice O2
v. Then there is a vertex
s2 ∈T, ﬁxed by π1(M2), such that d(s1, s2) = n. Moreover, assume that in this
basis s2 has a representative of the form tnOv ⊕Ov. The ﬁrst observation is that
ρ1(π1(M1)) ⊂SL2(Ov) because it stabilizes O2
v. Since ρΣ ﬁxes the ﬁrst edge of the
segment [s1s2], in this basis it ﬁxes the lattices O2
v and tOv ⊕Ov, hence for all
γ ∈π1(Σ), ρΣ(γ) =

a(γ) b(γ)
c(γ) d(γ)

, with c(γ) ∈(t), hence ¯ρΣ is reducible.
Let ρ′
2 = U −1
n ρ2Un, then ρ′
2 · s1 = U −1
n ρ2 · s2 = U −1
n · s2 = s1 and we have proved that
the representation ρ′
2 converges.

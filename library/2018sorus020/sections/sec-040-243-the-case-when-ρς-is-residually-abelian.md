---
doc_id: 2018sorus020
doc_title: "Reidemeister torsion on character varieties"
section_id: sec-040-243-the-case-when-ρς-is-residually-abelian
section_title: "The case when ρΣ is residually abelian"
section_number: 2.4.3
pages: 79-82
source_pdf: 2018SORUS020.pdf
source_sha256: c3f929e5195983ce
toc_source: inferred
doc_brief: "Reidemeister torsion on character varieties — 52 sections: Front matter; Introduction; Character varieties and Reidemeist"
---
The case when ρΣ is residually abelian
In this section we treat the case when the residual reducible representation ¯ρΣ is
abelian. This case is motivated by the example of the ﬁgure-eight knot complement,
see Remark 3.3.1. In fact, if Σ is two holed torus, as soon as the boundary curve
will be mapped to ± Id by ¯ρΣ, then the representation ¯ρΣ will be residually abelian.
Computational evidences suggest that it is always the case. Remark that in this
case, the eigenvalues of ¯ρΣ(∂Σ) are necessarily ±1 because they are roots of unity
with order that divides the number of boundary components of the surface Σ.
The main diﬀerence with the previous case is the following :
Lemma 2.4.12. The Ov-module H1(Σ, Ad ◦ρΣ)v is isomorphic to O−3χ(Σ)
v
⊕Ov/(tm)
for some positive integer m.
Proof. Again H0(Σ, Ad ◦ρΣ) is trivial because ρΣ is not abelian, but in this case we
have H0(Σ, Ad ◦¯ρΣ) ≃k. The Universal Coeﬃcients theorem gives
0 →H0(Σ, Ad ◦ρΣ)v ⊗Ov Ov/(t) →H0(Σ, Ad ◦¯ρΣ) →
Tor(H1(Σ, Ad ◦ρΣ)v, Ov/(t)) →0
It follows that the torsion part of the module H1(Σ, Ad ◦ρΣ)v is isomorphic to
Ov/(tm) for some m, and the lemma follows.
Again, we pick basis ci, cΣ of the complexes of k(Y )-vector spaces C∗(Mi, Ad ◦ρi),
C∗(Σ, Ad ◦ρΣ) and basis hi, hΣ of their ﬁrst homology group (the only one that is
not trivial). We want to use the formula :
tor(M, Ad ◦ρ) = tor(M1) tor(M2)
tor(Σ)
tor(H)
Proposition 2.4.13. The terms tor(M1) and tor(M2) lie in O∗
v, but tor(Σ) has
valuation m.
Proof. The ﬁrst part of the statement works in the same way than the proof of
Proposition 2.4.4.
Recall that Σ has the same homotopy type that a wedge of −χ(Σ)+1 circles, hence
the complex C∗(Σ, Ad ◦ρΣ) looks like
sl2(k(Y )) →sl2(k(Y ))−χ(Σ)+1
78
and to compute its torsion it is enough to compute the determinant of the co-
restricted isomorphism k(Y )3 →k(Y )3. But this map induces a morphism of Ov-
modules O3
v →O3
v whose co-kernel is isomorphic to Ov/(tm), hence the result.
Again, we need to focus on the term tor(H), where the exact sequence H is :
0 →H1(M, Ad ◦ρ) →H1(M1, Ad ◦ρ1) ⊕H1(M2, Ad ◦ρ2)
→H1(Σ, Ad ◦ρΣ) →H2(M, Ad ◦ρ) →0
We consider rather the sequence Ht :
0 →k(Y )
d1
−→H1(M1, Ad ◦ρ1) ⊕H1(M2, Ad ◦ρ′
2)
tn.d2
−−−→H1(Σ, Ad ◦ρΣ)
δ−→k(Y ) →0
for n the number of parallel components in Σ, and the very same arguments that in
the previous section lead to the lemma :
Lemma 2.4.14 (Lemma 2.4.7). Let ∆2 be the restriction of td2 as above Lemma
2.4.7. Then
tor(Ht) =
1
det ∆2
c, with c ∈O∗
v
Since ¯ρΣ = ¯ρ1,Σ is abelian, so is ¯ρ2,Σ, hence we can write ¯ρΣ(γ) =

λ(γ)
0
0
λ−1(γ)

for
all γ ∈π1(Σ), with λ ∈H1(Σ, k∗). Consequently we have the decomposition
H1(Σ, Ad ◦¯ρΣ) = H1(Σ, λ2) ⊕H1(Σ, k) ⊕H1(Σ, λ−2)
Lemma 2.4.15. The dimension of the kernel of the induced map
H1(M2, Ad ◦¯ρ2) →H1(Σ, Ad ◦¯ρΣ)
ζ2 =
 
x2
y2
z2
−x2
!
7→z2,ΣF
is d ≥−χ(Σ)/2.
Proof. We observe that this map factors through the maps H1(M2, Ad ◦¯ρ2) ,→
H1(Σ, Ad ◦¯ρΣ)
p−→H1(Σ, λ−2) ,→H1(Σ, Ad ◦¯ρΣ). Since ker p = H1(Σ, λ2)⊕H1(Σ, k)
79
we ﬁnd that the dimension d is at least
d ≥dim H1(M2, Ad ◦¯ρ2) + dim H1(Σ, λ) + dim H1(Σ, k) −dim H1(Σ, Ad ◦¯ρΣ)
= −3/2χ(Σ) −χ(Σ) −χ(Σ) + 1 −(−3χ(Σ) + 1)
= −χ(Σ)/2
Lemma 2.4.16. The valuation of the torsion v(Ht) is smaller than n(2χ(Σ) + 1).
Proof. By Lemma 2.4.8, the map
∆2 : (H1(M1, Ad ◦ρ1) ⊕H1(M2, Ad ◦ρ′
2))/(im H1(M, Ad ◦ρ)) →im(∆2)
has determinant greater that the sum of the dimensions of the kernels of the residual
maps
¯D2 = ∆2|t=0 : (H1(M1, Ad ◦¯ρ1) ⊕H1(M2, Ad ◦¯ρ2))/k →H1(Σ, Ad ◦¯ρΣ)
[ζ1, ζ2] 7→z2,ΣF
and
di
dti|t=0∆2 : ker( di−1
dti−1|t=0∆2) →H1(Σ, Ad ◦¯ρΣ)
for i = 1, . . . , n −1.
But dim ker ¯D2 is at least dim H1(M1, Ad ◦¯ρ1) + d −1 = −2χ(Σ) −1, and the maps
di
dti|t=0∆2 are identically zero on ker ¯D2, hence the sum of the kernels dimensions is
at least −n(2χ(Σ) + 1). The lemma follows now from Lemma 2.4.7 above.
Lemma 2.4.17. The valuation of the sequence H is v(tor(H)) ≤−nχ(Σ)
Proof. It follows from the fact that trk(d2) tor(Ht) = tor(H), and rk(d2) = −3χ(Σ)−
1
Proof of Theorem 2.0.2, second part. Using Milnor’s formlula, we know that
v(tor(M, Ad ◦ρ)) = v(tor(H)) −v(tor(Σ)) ≤−nχ(Σ) −m
80

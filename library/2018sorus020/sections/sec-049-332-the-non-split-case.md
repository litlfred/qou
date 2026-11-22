---
doc_id: 2018sorus020
doc_title: "Reidemeister torsion on character varieties"
section_id: sec-049-332-the-non-split-case
section_title: "The non-split case"
section_number: 3.3.2
pages: 96-100
source_pdf: 2018SORUS020.pdf
source_sha256: c3f929e5195983ce
toc_source: inferred
doc_brief: "Reidemeister torsion on character varieties — 52 sections: Front matter; Introduction; Character varieties and Reidemeist"
---
The non-split case
In this section we prove the following theorem :
95
Theorem (Theorem 3.0.2, the non-split case). Let x ∈ˆX be an ideal point in the
smooth projective model of a component X of the character variety, that produces
an incompressible surface S in M which is a union of parallel copies S1 ∪. . . ∪Sn of
a Seifert surface. Then the torsion function tor(M, ρ) has a pole at x, in particular
it is non-constant.
In this section we assume that the incompressible surface associated to x is a union
of parallel Seifert surfaces. Recall from Section 1.3.7 that we ﬁx a base-point p ∈
S1, and that we identify π1(S) with π1(S1). We have the following splitting M =
H ∪S1∪Sn V (S), where V (S) is a neighborhood of S homeomorphic to S1 ×[0, 1] with
∂V (S) = S1 ∪Sn. We identify as well π1(V (S)) with π1(S). Given α : π1(S1) →
π1(Sn), one can write the fundamental group of M as an HNN extension π1(M) =
⟨π1(H), v | vγv−1 = α(γ), ∀γ ∈π1(S)⟩.
We denote by ρ1 : π1(S) →SL2(Ov) the restriction of ρ to π1(S), and by ρn :
π1(Sn) →SL2(k(X)) its restriction to π1(Sn) = vπ1(S)v−1, hence we deﬁne ρn(γ) =
Vnρ1(γ)V −1
n
for γ ∈π1(S). The splitting above induces the following exact sequence
of twisted complexes :
0 →C∗(M, ρ) →C∗(H, ρH) ⊕C∗(S, ρ1) →C∗(S, ρ1) ⊕C∗(S, ρn) →0
The following proposition recaps the series of lemmas in Section 3.3.1, we refer to
the corresponding lemmas for proofs, that translate in exactly the same way here.
We use the isomorphism H1(S, ρn) →H1(S, ρ1), Z 7→Un (
0 1
−1 0 ) Z.
Proposition 3.3.9. The vanishing order of the torsion at the ideal point x ∈¯X is
given by computing −v(det θ), where the isomorphism θ is given by
θ : H1(H, ρH) ⊕H1(S, ρ1) →H1(S, ρ1) ⊕H1(S, ρ1)
(Z1, Z2) 7→((Z1 −Z2)|S, Un (
0 1
−1 0 ) (Z1 −Z2)|S)
Since we want to show that v(det θ) > 0, we focus on the residual map ; it is of the
form
¯θ : H1(H, ¯ρH) ⊕H1(S, ¯ρS) →H1(S, ¯ρS) ⊕H1(S, ¯ρS)
(z1, z2) 7→(z1|S −z2|S, −
 
0
x1|S −x2|S
!
)
96
where zi =
 
xi
yi
!
. We show that it has a non trivial kernel.
Lemma 3.3.10. The kernel of the map
ψ : H1(H, ¯ρH) →H1(S, ¯ρS)
z1 7→
 
0
−x1|S
!
has dimension d > −χ(S).
Proof. The relation ρn = Vnρ1V −1
n
implies that the residual representation ¯ρ1 has
the form, for γ ∈π1(S), ¯ρ1(γ) =

λ(γ)
0
∗
λ−1(γ)

. Hence we have the exact sequence
0 →H1(S, λ−1) →H1(S, ¯ρ1) →H1(S, λ) →0
We denote by ρ′
1 : π1(S) →SL2(Ov) the representation ρ′
1(γ) = (
0 1
−1 0 ) ρ1(γ) ( 0 −1
1
0 ),
and the map ψ is the composition
H1(H, ¯ρH) →H1(S, ¯ρ′
1) →H1(S, λ) ≃H1(S, λ−1) →H1(S, ¯ρ1)
 
x
y
!
→
 
x|S
y|S
!
→x|S →
 
0
x|S
!
We show that the composition H1(H, ¯ρH) →H1(S, λ−1) is not surjective, and it is
enough to prove the lemma by a count of dimensions.
To see that it is not surjective, notice that it factors through the composition
H1(H, ¯ρH) →H1(∂H, ¯ρ∂H) →H1(S, ¯ρ′
1). Now we have the exact sequence of the
pair (∂H, S) :
0 →C∗(∂H, S; ρ∂H) →C∗(H, ρ∂H) →C∗(S, ρ′
1) →0
hence the long exact sequence in cohomology provides
H1(∂H, ¯ρ∂H) →H1(S, ¯ρ′
1) →H2(∂H, S, ¯ρ∂H) →0
but by excision, H2(∂H, S, ¯ρ∂H) ≃H2(∂S × [0, 1], ∂S, ¯ρ∂S), the latter is H0(∂S ×
[0, 1], ¯ρ∂S) by Poincaré-Lefschetz duality, which is H1(∂S, ¯ρ∂S).
We deduce the diagram :
97
H1(H, ¯ρH)
H1(∂H, ¯ρ∂H)
H1(S, ¯ρ1)
H1(S, λ)
H1(S, λ−1)
H1(∂S, ¯ρ∂S)
H1(∂S, k)
0
0
0
F
We conclude because the commutativity of the diagram and the exactness of the
vertical arrows imply that the map F cannot surjective.
Proof of Theorem 3.0.2. We prove that the map residual map ¯θ is not an isomor-
phism, hence its determinant vanishes and it proves the theorem. To see that we
show that it is not surjective, in particular the map
H1(H, ¯ρH) ⊕H1(S, ¯ρS) →H1(S, ¯ρS)
(z1, z2) 7→−
 
0
x1|S −x2|S
!
is not surjective : the ﬁrst part of the map has rank strictly less than −χ(S) by
Lemma 3.3.10, and the second part has rank −χ(S). It proves the theorem.
98

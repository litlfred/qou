---
doc_id: disssubmission
doc_title: "Tannakian categories of perverse sheaves on abelian varieties"
section_id: sec-033-53-integral-cohomology
section_title: "Integral cohomology"
section_number: 5.3
pages: 114-117
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
toc_source: inferred
doc_brief: "Tannakian categories of perverse sheaves on abelian varieties — 52 sections: Front matter; Introduction; Some commonly used notations"
---
Let X be a complex ppav of dimension g = 4 with a smooth symmetric
theta divisor Θ ⊂X. We ﬁx a general point x ∈X(C) and consider the ´etale
double covering of smooth surfaces
Y = Θ∩Θx −→Y + = Y/σ
for the involution σ = σx as in corollary 5.4. In this section we determine
the cohomology of these surfaces with integral coefﬁcients, reﬁning the
computations that we did with rational coefﬁcients in section 5.1. The result
can be summarized in the following way.
PROPOSITION 5.11. The smooth projective surfaces Y and Y + have the
following integral cohomology groups.
n
0
1
2
3
4
Hn(Y,Z)
Z
Z8
Z86
Z8
Z
Hn(Y +,Z)
Z
0
Z34 ⊕(Z/2Z)9
(Z/2Z)9
Z
Moreover, the quotient morphism q : Y −→Y + induces an epimorphism
onto the σ-invariants
q∗: H2(Y +,Z) ↠H2(Y,Z)+ ⊂H2(Y,Z)
and the kernel of this epimorphism is the torsion subgroup of H2(Y +,Z).
Proof. We will use the weak Lefschetz theorem in the following integral
form, see [76, cor. 7.3] and [104, th. 1.23]. Let V be a complex projective
variety of dimension n with an ample effective divisor W ⊂V with smooth
complement V \W. Then the restriction map
Hk(V,Z) −→Hk(W,Z)
is an isomorphism for k < n −1 and a monomorphism for k = n −1, and
the pushforward map
Hk(W,Z) −→Hk(V,Z)
5.3. Integral cohomology
107
is an isomorphism for k < n−1 and an epimorphism for k = n−1. Applying
this ﬁrst to the ample divisor Θ ⊂X and then to the ample divisor Y ⊂Θ,
we in particular obtain that
Hn(Y,Z) ∼= Hn(X,Z)
and
Hn(Y,Z) ∼= Hn(X,Z)
for
n < 2.
In particular, the weak Lefschetz theorem for cohomology implies that the
groups Hn(Y,Z) have the claimed form for n < 2. Similarly, for n > 2
the corresponding statement follows from the weak Lefschetz theorem for
homology because Hn(Y,Z) ∼= H4−n(Y,Z) by Poincar´e duality. For any n
we furthermore have an exact sequence
0 −→Ext(Hn−1(Y,Z),Z)
|
{z
}
torsion group
−→Hn(Y,Z) −→Hom(Hn(Y,Z),Z)
|
{z
}
torsion-free
−→0
by the universal coefﬁcient theorem. Putting n = 2 and using that by the
weak Lefschetz theorem the group H1(Y,Z) ∼= H1(X,Z) is torsion-free so
that Ext(H1(Y,Z),Z) = 0, we obtain that
H2(Y,Z) ∼= Hom(H2(Y,Z),Z)
is a free abelian group. The rank of this group is equal to h2(Y) = 86 by
lemma 5.8. Altogether it then follows that the integral cohomology groups
of Y are those given in the table.
It remains to show that q∗: H2(Y +,Z) −→H2(Y,Z) is an epimorphism
onto the σ-invariants whose kernel is the torsion subgroup, and to determine
the groups Hn(Y +,Z). In the computation of these cohomology groups we
can in fact restrict our attention to degrees n ≤2. Indeed, Poincar´e duality
says that
Hn(Y +,Z) ∼= H4−n(Y +,Z)
for all n, hence by the universal coefﬁcient theorem we have (non-canonical)
isomorphisms
Hn(Y +,Z) ∼= Hn−1(Y +,Z)tor ⊕Hn(Y +,Z)free
∼= H5−n(Y +,Z)tor ⊕H4−n(Y +,Z)free
where the subscripts tor and free refer to the maximal torsion subgroup and
the maximal free abelian subgroup, respectively. So for the computation of
the groups Hn(Y +,Z) it sufﬁces to deal with degrees n ≤2. This being said,
we can argue as follows.
Recall from topology [18, ex. VII.4(b)] that for every regular covering
map W −→W + = W/Γ between connected, locally pathwise connected
topological spaces with Galois group Γ = Aut(W/W +), one has a spectral
sequence
E pq
2
= H p(Γ,Hq(W,Z)) =⇒H p+q(W +,Z)
108
Chapter 5 – A family of surfaces
where the left hand side denotes group cohomology with coefﬁcients in the
Γ-module Hq(W,Z). We apply this for W = Y and Γ = ⟨σ⟩. To compute
in this case some of the E2-terms, recall that the group cohomology of any
module M under the cyclic group ⟨σ⟩∼= Z/2Z is given by
H p(⟨σ⟩,M) =





ker(σ −1)
for p = 0,
ker(σ +1)/im(σ −1)
for p > 0 odd,
ker(σ −1)/im(σ +1)
for p > 0 even.
Let us plug in M = Hq(Y,Z) with q ∈{0,1,2}. Clearly on H0(Y,Z) ∼= Z the
involution σ acts trivially, whereas by the weak Lefschetz theorem we know
that on H1(Y,Z) ∼= H1(X,Z) ∼= Z8 the involution σ acts by −1. Hence in
this case we have
ker(σ +1 | Hq(Y,Z))
im(σ −1 | Hq(Y,Z))
∼=
(
0
for q = 0,
(Z/2Z)8
for q = 1,
ker(σ −1 | Hq(Y,Z))
im(σ +1 | Hq(Y,Z))
∼=
(
Z/2Z
for q = 0,
0
for q = 1.
In other words, in the case at hand the E2-tableau of the spectral sequence
takes the following form.
q
...
...
...
...
2
H2(Y,Z)+
+W
W
W
W
W
W
W
W
W
W
W
W
W
W
W
W
W
W
∗
*V
V
V
V
V
V
V
V
V
V
V
V
V
V
V
V
V
∗
∗
···
1
0
+W
W
W
W
W
W
W
W
W
W
W
W
W
W
W
W
W
W
W
W
(Z/2Z)8
+V
V
V
V
V
V
V
V
V
V
V
V
V
V
V
V
V
0
(Z/2Z)8
···
0
Z
0
Z/2Z
0
···
/
O
0
1
2
3
p
In particular it follows that H0(Y +,Z) = Z and H1(Y +,Z) = 0. The zeroes
for (p,q) = (2,1),(3,0) furthermore show that for the graded object with
respect to the limit ﬁltration we have
Gri(H2(Y +,Z)) =





H2(Y,Z)+
for i = 2,
(Z/2Z)8
for i = 1,
Z/2Z
for i = 0,

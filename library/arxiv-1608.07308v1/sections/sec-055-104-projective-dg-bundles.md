---
doc_id: arxiv-1608.07308v1
doc_title: "FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY"
section_id: sec-055-104-projective-dg-bundles
section_title: "Projective dg bundles"
section_number: 10.4
pages: 74-75
source_pdf: 1608.07308v1.pdf
source_sha256: bcc3b6f1a91a55c6
doc_brief: "FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY — We construct a categoriﬁcation of the maximal commutative subalgebra of the type A Hecke algebra."
---
generality, but instead focus on projectivizations of dg vector bundlesV• on a spaceX.
Deﬁnition 10.7. A projective dg bundle is deﬁned through its category of coherent sheaves:
Coh(ProjSXV•) ={gradedS∗
XV• dg modules}
(S∗V•/S∗>0V•)∼= 0
Let us make two remarks: ﬁrst of all, an object in Coh(Proj SXV•) has two gradings. The
ﬁrst comes from the power∗ of the symmetric power, and the second comes from the dg grading
onV•. Secondly, the difference between a projectivization and the afﬁne cone Spec SXV• is
the same as in the classical case: there is, in the derived category of the former, an additional
quasi-isomorphism between the structure sheaf of the zero section and the zero module.
Example 10.8. As in Example 10.8, let us study the case whenV• = [M
s
−→N ] is a two step
complex of vector bundles, concentrated in degrees−1 and 0. In this case, we have a map:
(10.9)
where the map π is an actual projective bundle sinceN is a vector bundle on X. The symbol
↪→ emulates closed embeddings of schemes, because we tautologically have:
(10.10) Coh
(
ProjSX[M
s
−→N ]
)
∼=
FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY 75
∼=
{
coherent sheaves on ProjSXN endowed with a dg action of∧•[π∗M(−1)
s
→O Proj SXN ]
}
With this in mind, we think of ProjSX[M
s
−→N ] as the dg subscheme of ProjSXN cut out
by the cosections of the vector bundleπ∗M(−1).
Our main Example 10.8 should be interpreted as a dg version of the familiar notion of pro-
jective bundles Proj SXV
π
−→X, whereV is a rank n locally free sheaf of X. In this case,
recall the following formulas:
π∗(O(k)) =SkV concentrated in degree 0
π∗(O(−k)) =Sk−nV∨⊗∧ topV∨ concentrated in degreen− 1
for all k∈ N, where π∗ denotes the derived pull-back. The second equality follows from the
ﬁrst one, together with relative Serre duality:
(10.11) R•π∗(A) =R•−n+1π∗(A∨⊗∧ topV(−n))∨
for allA∈ Db(Coh(ProjSXV)). We now prove a similar formula in the dg setting
Proposition 10.9. In the notation of Example 10.8, suppose rank M = m and rankN = n.
Then:
(10.12) R•πdg
∗ (A) =R•−n+m+1πdg
∗
(
A∨⊗ ∧topN (−n)
∧topM(−m)
)∨
for allA∈ Db(Coh(ProjSX[M
s
−→N ]))
Proof. Implicitly in equation (10.10), one has the equation:
R•πdg
∗ (A) =R•π∗
(
A⊗∧ •[π∗M(−1)
s
→O ]
)
Applying (10.11) to the right hand side, we obtain
R•πdg
∗ (A) =R•−n+1π∗
(
A∨⊗∧•
[
π∗M(−1)
s
→O
]∨
⊗∧ topN∨(−n)
)∨
It is easy to see that∧•
[
π∗M(−1)
s
→O
]∨
=∧•+m
[
π∗M(−1)
s
→O
]
⊗∧ topM∨(m), hence:
R•πdg
∗ (A) =R•−n+m+1π∗
(
A∨⊗∧•
[
π∗M(−1)
s
→O
]
⊗ ∧topN (−n)
∧topM(−m)
)∨
which equalsR•−n+m+1πdg
∗
(
A∨⊗ ∧topN (−n)
∧topM(−m)
)∨
by another application of (10.10).
□

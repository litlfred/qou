---
doc_id: s0894-0347-08-00618-8
doc_title: "AMERICAN MATHEMATICAL SOCIETY"
section_id: sec-004-23-symmetric-homogenization
section_title: "Symmetric homogenization"
section_number: 2.3
pages: 10-11
source_pdf: S0894-0347-08-00618-8.pdf
source_sha256: 7c0b2ca41992b21c
doc_brief: "AMERICAN MATHEMATICAL SOCIETY — 20 sections: Introduction; A plethora of negative dependence ; Negative dependence concepts"
---
tion procedure for arbitrary measures in Pn. This natural construction proves to
be quite useful for studying strongly Rayleigh measures (§4.1).
Deﬁnition 2.12. Given a measure µ ∈ Pn deﬁne a new measure µsh ∈ P2n called
the symmetric homogenization of µ by
µsh(S)=
{
µ(S ∩ [n])
( n
|S∩[n]|
)−1
if |S| = n,
0o t h e r w i s e .
Note that the generating polynomial of µsh may be written as
gµsh (z1,...,z n,zn+1,...,z 2n)=
∑
S⊆[n]
µ(S)
( n
|S|
)−1
zSen−|S|(zn+1,...,z 2n),
where z =( z1,...,z n)a n dw h e r eek,0 ≤ k ≤ n, denotes the k-th elementary sym-
metric function. Clearly, gµsh is symmetric in the variables zn+1,...,z 2n and µsh
projects to µ,t h a ti s ,gµsh (z1,...,z n, 1,..., 1) = gµ(z1,...,z n). It is not diﬃcult
to show that gµsh is actually the unique polynomial in P2n of total degree n that
is symmetric in zn+1,...,z 2n and satisﬁes the latter identity. Therefore, µsh is
canonically determined by the aforementioned conditions.
2.4. Measures on countably inﬁnite sets. In §5 we will need to extend some
of the notions of negative dependence to probability measures on 2E,w h e r eE is a
countably inﬁnite set. This is canonically done as follows.
NEGATIVE DEPENDENCE AND THE GEOMETR Y OF POL YNOMIALS 531
Deﬁnition 2.13. Let µ be a probability measure on 2 E,w h e r eE is a countably
inﬁnite set satisfying
(A) for all x ∈ E the set
{
T ∈ 2E : x ∈ T
}
is measurable.
Let P be a property deﬁned for measures on power-sets of ﬁnite sets. We say that
µ has property P provided that the projection of µ to all ﬁnite subsets of E has
property P. (Note that condition (A) is necessary for projections on ﬁnite sets to
be well-deﬁned.)

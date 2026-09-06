---
doc_id: arxiv-1608.07308v1
doc_title: "FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY"
section_id: sec-016-27-the-dg-scheme
section_title: "The dg scheme"
section_number: 2.7
pages: 18-19
source_pdf: 1608.07308v1.pdf
source_sha256: bcc3b6f1a91a55c6
doc_brief: "FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY — We construct a categoriﬁcation of the maximal commutative subalgebra of the type A Hecke algebra."
---
we leave it as an exercise to the interested reader to show that the two descriptions are equivalent
(we will only use the deﬁnition in this Subsection for the remainder of this paper). The idea
is to note that the map Ψ of the complex (2.35) fails to be injective on many ﬁbers, and this
will lead to the ﬂag Hilbert scheme misbehaving. To remedy this issue, we replace the middle
cohomology sheafH0(En) in (2.25) by the entire complexEn (we tacitly suppress the symbol
∗∈{ C2, C, point} since the construction applies equally well to all three choices).
Proposition 2.10. There exist dg schemes FHilbdg
n endowed with ﬂags of objects:
Tn→T n−1→...→T 1 ∈Db(Coh(FHilbdg
n ))
together with mapsqTn
X
→T n,tTn
Y
→T n that respect the above ﬂag, andO
v
→T n such that:
(2.36) FHilbdg
n+1 = PFHilbdg
n
(E∨
n ) := ProjFHilbdg
n
(S•En)
where the complexEn is deﬁned by formula (2.25). See Subsection 10.4 for the deﬁnition of the
Proj construction of a two-step complex of vector bundles (according to (2.35)).
Proof. Let us writeLn+1 =O(1) for the tautological line bundle on the projectivization (2.36),
andπ : FHilbn+1→ FHilbn for the natural map. Take the deﬁning map of projective bundles:
Taut∈ Hom(π∗En,O(1))
and compose it with the natural mapTn[−1]
i
→E n. We obtain an object:
i∗(Taut) =: Tn+1∈ Hom (π∗Tn[−1],Ln+1)
Composing the mapi withqTn⊕tTn⊕O
(X,Y,v)
−−−−→Tn yields 0, hence:
(X,Y,v )∗ (Tn+1)∈ Hom (π∗(qTn⊕tTn⊕O )[−1],Ln+1)
equals 0 as well. This precisely gives rise to a splitting:
and the dotted map is the desired extension of the arrows X,Y,v fromTn toTn+1. Note that
we may write the above diagram as an equality in the derived category of FHilbdg
n+1:
(2.37)
[
qtLn+1
(−y,x)
−−−→qLn+1⊕tLn+1
(x,y)
−−→Ln+1
]
∼=
[
En+1−→ ~π∗(En)
]
where we have underlined the 0–th terms of both complexes. In the above equation, we write
x andy for the operators of multiplication byxn−xn+1 andyn−yn+1, respectively, and:
(2.38) ~π∗(En) denotes π∗(En) with the variables (xn,xn+1) and (yn,yn+1) switched
□
One can run the proof of Proposition 2.10 withEn replaced byH0En. We leave it as an exercise
to the interested reader to show that one would obtain the schemes FHilbn of Theorem 2.6.
FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY 19

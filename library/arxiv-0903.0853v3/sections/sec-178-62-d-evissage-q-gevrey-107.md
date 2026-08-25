---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-178-62-d-evissage-q-gevrey-107
section_title: "D ´EVISSAGE q-GEVREY 107"
section_number: 6.2
pages: 113-114
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
doc_brief: "Local analytic classification of q-difference equations — 229 sections: Vector bundles associated to q-diﬀ; The q-Euler equation and conﬂuent ; The symmetric square of the q-Eule"
---
graded part A0 and are in Birkhoﬀ-Guenther normal form. Assume moreover
that they coincide up to levelδ−1. Then the same is true for ˆFA and ˆFA′; there-
fore, it is also true for ˆFA,A′ and In, that is, ˆFA,A′∈ G≥δ(C((z))). The ﬁrst
non-trivial upper diagonal of ˆFA,A′ is at levelδ and, as a divergent series, gener-
ically it actually has q-Gevrey levelδ; if it has level <δ , then it is convergent.
The classes of A,A ′ inF≤δ(M0) = H 1(Eq, Λ/Λ≥δ+1) have the same image
inF≤δ−1(M0) = H 1(Eq, Λ/Λ≥δ). After theorem 6.2.1, there exists a unique
element of V (δ) which carries the class of A to the class of A′. The Stokes
matrices Sc,d ˆFA :=
(
Sc,d ˆFA
) −1
Sd ˆFA and Sc,d ˆFA′ :=
(
Sc,d ˆFA′
) −1
Sd ˆFA′ are
congruent modulo Λ≥δ, so that their quotient Sc,d ˆFA,A′ is in Λ≥δ. Its ﬁrst non
trivial upper diagonal is at level δ; call it fc,d and consider it as an element
of λ(δ). This deﬁnes a cocycle, hence a class in H 1(Eq,λ (δ)). This class is the
element of V (δ) we look for.
Example 6.2.3 . — Take A0 :=


a 0 0
0 bz 0
0 0 cz2

 andA :=


a u v 0 +v1z
0 bz wz
0 0 cz2


in Birkhoﬀ-Guenther normal form, so that u,v 0,v 1,w ∈ C. Here, the total
space of classes H 1(Eq, ΛI(M0)) has dimension 4, while each of the compo-
nentsH 1(Eq,λ (1)) and H 1(Eq,λ (2)) has dimension 2.
To compute the class of A in H 1(Eq, ΛI(M0)) identiﬁed with H 1(Eq,λ (1))⊕
H 1(Eq,λ (2)), we introduce the intermediate point A′ :=


a u 0
0 bz wz
0 0 cz2

 and
the intermediate gauge transformsG :=


1 f x
0 1 h
0 0 1

 such thatG[A0] =A′ and
H :=


1 0 g
0 1 0
0 0 1

 such that H[A′] = A, so that F :=HG =


1 f g +x
0 1 h
0 0 1


is such that F[A0] =A.
The component in H 1(Eq,λ (1)) is computed by considering G alone. Its
coeﬃcients satisfy the equations:
bzσqf−af =u and czσqh−bh =w.
(The coeﬃcientx is irrelevant here.) We shall see in section 7.1 how to compute
the corresponding cocycles (fc,d) and (hc,d), but what is clear here is that they
are respectively linear functions of u and of w. So in the end, the component
of the class of A inH 1(Eq,λ (1)) isuL1(a,b ) +wL1(b,c ) for some explicit basic
108 CHAPTER 6. GEOMETRY OF THE SPACE OF CLASSES
classes L1(a,b ), L1(b,c ) (the index 1 is for the level).
Similarly, the component inH 1(Eq,λ (2)) is computed by considering H alone.
Its coeﬃcient satisﬁes the equation:
cz2σqg−ag =v0 +v1z.
It is therefore clear that the component we look for isv0L2,0(a,c )+v1L2,1(a,c )
for some explicit base of classes L2,0(a,c ),L 2,1(a,c ).
This example will be pursued in section 7.2.

---
doc_id: arxiv-1702.00039v1
doc_title: "Gentle introduction to Soergel bimodules I: The basics NICOLAS LIBEDINSKY"
section_id: sec-011-3-quantum-level-hecke-algebras
section_title: "Quantum level: Hecke algebras"
section_number: 3
pages: 12-14
source_pdf: 1702.00039v1.pdf
source_sha256: b47ca7d1cf7b44be
doc_brief: "Gentle introduction to Soergel bimodules I: The basics NICOLAS LIBEDINSKY — This paper is the ﬁrst of a series of introductory papers on the fascinating world of Soergel bimodules."
---
3.1 Kazhdan-Lusztig’s theory
For the basic deﬁnitions of Hecke algebras and Kazhdan-Lusztig polynomials
we follow [So3]. Let (W,S ) be a Coxeter system.
Deﬁnition 2 The Hecke algebraH of a Coxeter system(W,S ) is theZ[v,v−1]−algebra
with generatorshs fors∈S and relations
• h2
s = (v−1−v)hs + 1 (quadratic relation)
• hshrhs...| {z }
msr
=hrhshr...| {z }
msr
for alls,r∈S (braid relation)
When v is replaced by 1 in the deﬁnition, one obtains the algebra ZW . Thus
we can see the Hecke algebra as a deformation of the group algebra.
12
For any reduced expression s = sr...t of an element x∈ W deﬁne the el-
ement hs = hshr··· ht. By the forementioned result of Matsumoto [Ma] we
know thaths does not depend on the reduced expressions, it just depends on
x. We call this elementhx. We deﬁne he = 1. The following is a basic lemma.
Lemma 3.1 (Nagayoshi Iwahori) The set{hx}x∈W is a basis ofH as aZ[v,v−1]−algebra,
called the standard basis.
The element hs has an inverse, namely (hs +v−v−1) as it is shown in the
following calculation.
hs(hs +v−v−1) = [( v−1−v)hs + 1] +hs(v−v−1)
= 1 (3)
This implies that hx has an inverse for every x∈ W. So we can deﬁne a Z-
module morphism d : H → Hby the formula d(v) = v−1 and d(hx) =
(hx−1)−1. It is an exercice to prove that this is a ring morphism, and we call
it the duality in the Hecke algebra.
Let us make a short calculation
d(hs +v) = ( hs)−1 +v−1
= ( hs +v−v−1) +v−1
= ( hs +v) (4)
So we obtain our ﬁrst example of self-dual element. The following theorem
(see [KL]) is the foundational theorem of Kazhdan-Lusztig theory.
Theorem 3.2 (David Kazhdan and George Lusztig) For every element x∈
W there is a unique self-dual elementbx∈H such that
bx∈hx +
∑
y∈W
vZ[v]hy. (5)
The set{bx}x∈W is a Z[v,v−1]−basis ofH, called the Kazhdan-Lusztig basis.
If we writebx =hx+∑
y∈Why,xhy then the Kazhdan-Lusztig polynomialspy,x
are deﬁned by the formula py,x =vl(x)−l(y)hy,x.
Remark 1 We will prove in Section 3.3 a stronger version of this theorem,
namely that
bx∈hx +
∑
y<x
vZ[v]hy, (6)
where< refers to the Bruhat order.
13
Before we prove this theorem we will believe it for a while and calculate the
Kazhdan-Lusztig bases in some examples.

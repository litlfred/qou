---
doc_id: arxiv-math-0605314v1
doc_title: "A UNIFIED WITTEN-RESHETIKHIN-TURAEV INV ARIANT FOR INTEGRAL HOMOLOGY SPHERES KAZUO HABIRO"
section_id: sec-086-3-if-αz-then-ˆzα
section_title: "If α∈Z , then ˆZ[α]"
section_number: 3
pages: 48-49
source_pdf: 0605314v1.pdf
source_sha256: 5fb8b89b432401ea
doc_brief: "A UNIFIED WITTEN-RESHETIKHIN-TURAEV INVARIANT FOR INTEGRAL HOMOLOGY SPHERES KAZUO HABIRO — W e construct an invariant JM of integral homology spheres M with values in a completion ˆZ[q] of the"
---
α∼
= Z[α].
The case α∈ Q is of special interest.
Proposition 13.1. If a/b∈ Q\{± 1} with a,b∈ Z, (a,b ) = 1 , then we have
ˆZ[a/b]
a/b
∼
= lim
←−m∈N,(m,ab)=1Z/mZ∼
=
∏
p∈Pab
Zp,(13.1)
where, for n∈ N, Pn denote the set of primes p coprime with n.
Proof. We have
ˆZ[a/b]
a/b
= lim←−nZ[1/b]/((a/b)n)∼
= lim
←−nZ[1/b]/((b,a )n),
where we set
(b,a )n =b
1
2 n(n+1)(a/b)n = (b−a)(b2−a2)··· (bn−an)∈ Z.
The families of ideals in Z[1/b], X :={((b,a )n)}n≥0 and Y :={(m)}m∈N,(m,ab)=1,
are coﬁnal with each other. (Indeed, a/b⁄= 1 implies X ⊂ Y . Conversely, for
m∈Y , we have bn−an≡ 0 mod m, where n≥ 1 is the least common multiple of
the orders of b and a in ( Z/mZ)×. Then ( b,a )n is divisible by m.) Therefore,
ˆZ[a/b]
a/b
∼
= lim
←−m∈N,(m,ab)=1Z[1/b]/(m)∼
= lim
←−m∈N,(m,ab)=1Z/mZ.
Here the latter isomorphism follows from invertibility of b in Z/mZ for each m.
The latter isomorphism in (13.1) is standard.
By Proposition 13.1, we may regard ev a/b(JM ) as an element in ∏
p∈Pab
Zp.
Hence, for each p∈Pa,b, we can extract a Zp-valued function
τ p(M ) : Up(Q)→ Zp,(13.2)
where Up(Q) is the set of a/b∈ Q with a,b∈ Z, (a,b ) = 1, such that p is coprime
with ab.
A UNIFIED WITTEN-RESHETIKHIN-TURAEV INV ARIANT 49
Note that Up(Q) = Q∩U (Zp), where U (Zp) is the group of units in the ring Zp.
We extend the domain of τ p(M ) in the next subsection.

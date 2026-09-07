---
doc_id: arxiv-2208.13448v2
doc_title: "ON THE COMPUTATION OF THE DIFFERENCE GALOIS GROUPS OF ORDER THREE EQUATIONS"
section_id: sec-008-33-the-primitive-case
section_title: "The primitive case"
section_number: 3.3
pages: 19-20
source_pdf: 2208.13448v2.pdf
source_sha256: 8bfa244cf7ca867d
doc_brief: "ON THE COMPUTATION OF THE DIFFERENCE GALOIS GROUPS OF ORDER THREE EQUATIONS — In this paper we consider the problem of computing the diﬀere nce Galois groups of order three equations for a large"
---
is prime. We want to prove that the same holds for G0 and D(G0) where D(G0) denotes
the derived group of G0. Note that G0 is a connected normal subgroup of G and D(G0)
is a connected normal subgroup of G0.
First, we recall the following result given in [ ADH21, Lemma 4.2].
Lemma 3.16. If K ⊂ GLn(C) is a connected and irreducible algebraic group, then K is
also primitive.
Lemma 3.17. Let n be a prime number. If H ⊂ GLn(C) is an irreducible and primitive
group, then the derived subgroup of H, denoted by D(H), is not composed only of
dilatations.
Proof. By contradiction, assume that D(H) is composed only of dilatations. In this
case, for all G , H ∈ H, there exists α ∈ C ∗ such that G H G −1H −1 = αIdn, that is
G H = αH G . The group H is irreducible so there exists H0 ∈ H having an eigenspace W
20 THOMAS DREYFUS AND MARINA POULET
of maximal dimension ν < n , otherwise H would be composed of dilatations contradicting
its irreducibility. Let V be the direct sum of the eigenspaces of H0 of dimension ν. From
the previous equality and the fact that H0(W ) = W , we obtain that
(3.5) ∀G ∈ H, H0(G (W )) = G (W ) .
Thus, G (W ) is also an eigenspace of H0 of dimension ν for all G ∈ H so H(W ) ⊂ V .
Therefore, H(V ) ⊂ V (in fact, taking the dimension, it is an equality of vector sp aces)
which implies that V = C n by irreducibility of H. Hence ν divides n. Since n is a
prime number and ν < n , we have ν = 1. This means that H0 is a diagonal matrix
with distinct eigenvalues and we denote by V1, . . . , Vn its eigenspaces. However, from ( 3.5)
with W := V1, we obtain that every G ∈ H induces a permutation between the Vi, which
contradicts the fact that H is primitive. □
Proposition 3.18. Assume that n is prime and G ⊂ GLn(C) is an irreducible and primitive
group. Then, the same holds for G0 and D(G0) and we may write G0 = Z(G0).D(G0)
where Z(G0) denotes the center of G0.
Proof. We recall that G0 is a connected normal subgroup of G and D(G0) is a connected
normal subgroup of G0.
From Lemma 3.4 (with H := G0), G0 is not composed only of dilatations. Thus, by
Proposition 3.8 (with H := G and K := G0), G0 is irreducible. Using Lemma 3.16, G0 is
also primitive. Then, the irreducibility of D(G0) follows from Lemma 3.17 (with H := G0)
and Proposition 3.8 (with H := G0 and K := D(G0)). Thanks to Lemma 3.16, D(G0) is
also primitive.
By [SS98, Corollary 8.1.6], any connected algebraic group H satisﬁes H ∼ Z(H).D(H),
which proves that G0 = Z(G0).D(G0). □

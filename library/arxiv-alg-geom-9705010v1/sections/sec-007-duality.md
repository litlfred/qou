---
doc_id: arxiv-alg-geom-9705010v1
doc_title: "Seiberg-Witten Integrable Systems"
section_id: sec-007-duality
section_title: "Duality"
section_number: null
pages: 12-13
source_pdf: 9705010v1.pdf
source_sha256: 30ab8d0cc2d8f1ae
toc_source: inferred
doc_brief: "Seiberg-Witten Integrable Systems — 32 sections: Front matter; Contents; Introduction"
---
The original conjecture of Montonen and Olive [MO] was that the low en-
ergy theory should be invariant under a duality exchanging electric and magnetic
charges, and also exchanging the coupling constant g with its inverse. In other
words: electric charge in the strongly coupled theory (large g) behaves like mag-
netic charge at weak coupling, and vice versa. Seiberg and Witten found that a
modiﬁed version of this duality holds in pure N = 2 SYM for SU(2). They applied
the super version of the Hodge ∗operator to the Lagrangian Leﬀ, added some vari-
ables (Lagrange multipliers) and integrated out others, and ended up with a new
Lagrangian LD
eﬀwhich is equivalent to the original, and has the same form, but in
terms of a new quantity aD := dF
da :
LD
eﬀ(aD) = Leﬀ(a).
The same transformation sends aD to −a = −dF
daD . (This must be so, since the
ﬁrst term in Leﬀchanges sign when a, aD are simply exchanged.) The physical
meaning of aD is therefore that of the dual, or magnetic, charge. As to the coupling
constants, the deﬁning relations
τ = daD
da ,
τD = d(−a)
daD
SEIBERG-WITTEN INTEGRABLE SYSTEMS
13
together with the chain rule, imply that the actual duality transformation is
τ D = τ D(aD) = −τ(a)−1.
This specializes to the Montonen-Olive transformation
gD = g−1
when θ = 0, but not otherwise.
There is another, more elementary, transformation which preserves the La-
grangian: the θ angle is deﬁned only modulo 2πZ, so τ is deﬁned modulo Z. There
is therefore a transformation which ﬁxes a and sends τ 7→τ + 1. Since τ = daD
da ,
this requires that aD goes to aD + a.
The two transformations can be represented by the matrices
S =

0
1
−1
0

T =

1
1
0
1

,
acting linearly on the 2-vector

aD
a

and fractional-linearly on τ. Since S and T
generate SL(2, Z),we see that the theory has an SL(2, Z) action. (For other groups,
SL(2, Z) is replaced by a subgroup of ﬁnite index in Sp(2r, Z).)

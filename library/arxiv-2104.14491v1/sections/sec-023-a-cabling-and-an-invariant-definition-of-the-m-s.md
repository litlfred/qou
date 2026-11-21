---
doc_id: arxiv-2104.14491v1
doc_title: "Khovanov polynomials for satellites and asymptotic adjoint polynomials A. Anokhinaa,∗A. Morozova,b,c,† A. Popolitova,b,c,‡ a Institute for Theoretical and Experimental Physics, Mos"
section_id: sec-023-a-cabling-and-an-invariant-definition-of-the-m-s
section_title: "A Cabling and an invariant definition of the m-strand satellite"
section_number: null
pages: 16-17
source_pdf: 2104.14491v1.pdf
source_sha256: 1aea658f17283df1
toc_source: outline
doc_brief: "Khovanov polynomials for satellites and asymptotic adjoint polynomials A. Anokhinaa,∗A. Morozova,b,c,† A. Popolitova,b,c,‡ a Institute for Theoretical and Experimental Physics, Moscow 117218, Russia"
---
Cabling and an invariant deﬁnition of the m-strand satellite
In this section, we assume that a satellite is deﬁned by a planar diagram, like one in ﬁg.1. We wish to
substitute the two strands that ﬁrst go along the companion and than intertwine with each other with any
number of such ones.
Let K◦m
w
be the satellite of the knot K that is obtained when each line on the K diagram with the
writhe number w is substituted with m parallel strands. The satellite polynomial is then expanded over the
coloured polynomials of the as
ˇHK◦m
ν
=
X
Q⊢□⊗m
ˇHKν
Q ,
(46)
where the colour (representation) label Q runs over all partitions of the m. Identity (46) holds for the
unreduced polynomials in the group theory normalisation (in the vertical framing) [5], which are deﬁned for
a knot diagram and are knot invariants only up to a factor. The true unreduced knot polynomials (in the
topological framing) diﬀer by the exponential of the writhe number, namely
HK
Q = A−mνq−2κQν ˇHKν
Q ,
(47)
where Q is a partition of m and κQ is an explicitly deﬁned integer-valued function of Q (the second Casimir
of the representation Q [64]). In particular, the plain (uncoloured) HOMFLY is associated with the partition
Q = 1 of m = 1 and has κ = 0. Hence, the analogue of (46) for the topological invariant quantities is
Am2νHK◦m
ν
=
X
Q⊢□⊗m
Amνq2κQνHKν
Q
⇒
HK◦m
ν
=
X
Q⊢□⊗m

Am(m−1)q2κQ
ν
HK
Q
(48)
where we substituted the writhe number W = m2w of the K◦m
w
deﬁned above (see examples in ﬁg.1 where
m = 2). We omit the label w in HK
Q, since they depend only on the knot K, unlike the K◦m
w , whose deﬁnition
still depends on the knot diagram.
Table 1: Basic properties of the knot polynomials we study.
Torn
=
Tor−n
Tw
◦◦
n
=
Tw••
−n
Tw
••
n
=
Tw◦◦
−n
σK(A) = σ ¯K( 1
A)
q=1
←−HK(A, q) = H ¯K( 1
A, q−1)
A=q2
−→JK(q) = J ¯K(1
q) t=−1
←−KhK(q, t) = Kh ¯K(1
q, 1
t )
⟲
q ↔−1
q
⟲
HK
adj(A, q) = H ¯K
adj( 1
A, 1
q)
↙
↘

σK(A)
2
q=1
←−HK
sym(A, q) = H ¯K
sym( 1
A, 1
q)
A=q2
−→JK
sym
(adj)
(q) = J ¯K
sym
(adj)
(1
q) t=−1
←−
” KhK
sym
(adj)
(q, t) ”
q ↔−1
q
↕
HK
asm(A, q) = H ¯K
asm( 1
A, 1
q) A=q2
↘
1
=
HK
trv(A, q)
=
JK
trv(q)
=
KhK
trv(q, t)
On the other hand, the full twist on m strands, which is represented by the braid word
FTm = (m−1) . . . 21(m−2) . . . 21 . . . . . . 1,
(49)
is a distinguished braid group element [49, 47]. I.e., insertion of the ν copies of the full twists in the m-strand
cable results just in an extra factor of the form cν
Q. Precisely, ˇcν
Q = q−2κQ in the vertical framing, as follows
from the Rosso–Jones formula (e.g., (11) of [54]), so that ˇcν
Q = A−m(m−1)q−2κQ in the topological framing
(see (15) of [54]), because the FTm contains m(m −1) co-oriented crossings. Hence, (48) can be rewritten
as
HK◦m
ν
=
X
Q⊢□⊗m
HFT −ν
m
♯Kν
Q
(50)
HSK
Torm
κ =
X
Q⊢□⊗m
µκHK
Q,
for SK
Torm
κ = FT κ−ν
m
♯Kν,
(51)
where
µ = A−m(m−1)q−2κQ.
(52)
and the notation FT w′
m ♯Kw implies that we insert w′ > 0 or (−w′) > 0 copies of the FTm or of its mirror
image FT m, respectively, in a section of the m strand cable between any two groups of crossings that
substitute a crossing in K.
The coloured polynomials HK
Q in the r.h.s. of (51) are the knot invariants, and the coeﬃcients µ do not
depend on the knot at all. Hence, the above deﬁned SK
Torm
κ is a topological invariant as long as so does the
k.
If m = 2, then the satellite is the torus satellite SK
Tor2κ ≡SK
Tork we study above. The colour label in (46)
then runs over the partitions of m = 2, which are Q = [2] and Q = [1, 1] and have κ[2] = 2 and κ[1,1] = −1.
Hence (46) and (48) are reduced to (9) and (10), respectively. The pattern includes w half-twists on the
two strands. Hence, one can set κ −ν = w/2 for the number of the full

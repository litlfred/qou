---
doc_id: arxiv-1604.01247v2
doc_title: "Exceptional quantum geometry and particle physics"
section_id: sec-010-6-connections-on-jordan-modules
section_title: "Connections on Jordan modules"
section_number: 6
pages: 30-32
source_pdf: 1604.01247v2.pdf
source_sha256: 5a402405aadf5d54
doc_brief: "Exceptional quantum geometry and particle physics — Based on an interpretation of the quark-lepton symmetry in t erms of the unimodularity of the color group SU (3) and on the existence of 3"
---
6.1 Derivation-based connections. First deﬁnition
Let J be a unital Jordan algebra with center (= centroid) Z(J) and let Der(J)
be the Lie algebra and Z(J)-module of derivations of J. A (derivation-based)
connection ∇ on a unital J-module M is a linear mapping X ↦→ ∇X of Der(J)
into the linear endomorphisms of M such that



∇X(xm) = X(x)m + x∇X (m)
∇zX (m) = z∇X (m)
(6.1)
for any m ∈ M, x ∈ J and z ∈ Z(J).
It follows from this deﬁnition that the diﬀerence ∇ − ∇′ between 2 con-
nections on M is a Z(J)-linear mapping of Der( J) into the Z(J)-module of
all the J-module endomorphisms of M.
It also follows that
RX,Y = [∇X , ∇Y ] − ∇[X,Y ] (6.2)
satisﬁes 


RX,Y (xm) = xRX,Y (m)
RzX,Y (m) = zRX,Y (m)
(6.3)
in other words that R is a Z(J)-linear mapping of ∧2
Z(J)Der(J) into the Z(J)-
module of all the J-module endomorphism of M which will be referred to as
the curvature of ∇.
It is clear that if g is a Lie subalgebra and a Z(J)-submodule of Der( J),
the restriction of (6.1) to g, i.e. for X ∈ g, makes sense and the corresponding
notion will be referred to as a derivation-based g-connection on M.
6.2 Derivation-based connections. Second deﬁnition
Let J, Z(J), Der( J) and M be as in §6.1 and let Ω n
Der(M) be the J-module
of all n-Z(J)-linear antisymmetric mapping of Der( J) into M, which means
30
that Φ ∈ Ω n
Der(M) is a Z(J)-linear mapping
Φ : ∧n
Z(J)Der(J) → M
with the notations of §5.4. The graded J-module Ω Der(M) = ⊕n≥0Ω n
Der(M)
in naturally a graded Jordan module over the graded Jordan algebra Ω Der(J):
The product of ω ∈ Ω m
Der(J) with Φ ∈ Ω n
Der(M) is the element ω Φ ∈ Ω m+n
Der (M)
obtained by product of evaluations on derivations followed by antisymmetriza-
tion in the derivations. A (derivation-based) connection on M is a linear
endomorphism ∇ of Ω Der(M) such that



∇(Ω n
Der(M)) ⊂ Ω n+1
Der (M)
∇(ω Φ) = d(ω )Φ + ( −1)mω ∇(Φ)
(6.4)
for any m, n ∈ N, ω ∈ Ω m
Der(J) and Φ ∈ Ω Der(M). Let ∇ be such a connection
and deﬁne ∇X m by
∇(m)(X) (6.5)
for m ∈ M = Ω 0
Der(M) and X ∈ Der(J). Then X ↦→ ∇X is a connection on
M in the sense of §6.1. Conversely if X ↦→ ∇X is a connection in the sense
of §6.1 one deﬁnes ∇ on Ω n
Der(M) by
∇(Φ)( X0, · · · , X n) = ∑ n
p=0(−1)p∇Xp(Φ( X0,
p
∨
· · · · · ·, X n))
+ ∑
0≤r<s≤n(−1)r+s Φ([ Xr, X s], X 0,
r
∨
· · ·
s
∨
· · ·, X n)
(6.6)
for Φ ∈ Ω n
Der(M), Xp ∈ Der(J). This ∇ satisﬁes the axioms (6.4). We shall
refer to ∇ as the covariant diﬀerential while ∇X for X ∈ Der(J) will be
refered to as the covariant derivative along X.
From the axioms (6.4), it follows that one has
∇2(ω Φ) = ω ∇2(Φ) (6.7)
for any ω ∈ Ω Der(J) and Φ ∈ Ω Der(M) furthermore
∇2(m)(X, Y ) = RX,Y (m)
for m ∈ M. Thus ∇2 is an homomorphism of Ω Der(J)-module which is also
called the curvature of ∇ since it is expressible in terms of the RX,Y and
conversely.
31

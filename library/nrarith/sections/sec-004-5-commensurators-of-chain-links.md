---
doc_id: nrarith
doc_title: "Arithmetic of Hyperbolic Manifolds"
section_id: sec-004-5-commensurators-of-chain-links
section_title: "Commensurators of chain links"
section_number: 5
pages: 15-19
source_pdf: nrarith.pdf
source_sha256: 085ec9541ddc6cd4
toc_source: inferred
doc_brief: "Arithmetic of hyperbolic manifolds (Neumann–Reid) — survey of arithmetic Kleinian groups: an arithmetic M = H³/Γ is determined up to commensurability by its invariant trace field and quaternion…"
---
Let C(p, s) denote the complement of the link in S3 consisting of a p-link chain
with s left half-twists (if s is negative we mean −s right half-twists, cf. Fig. 1 for
(p, s) = (6, −3) or in Fig. 2 for (p, s) = (7, 0)). C(p, s) has several symmetries: α the
symmetry that rotates the chain clockwise, taking each link into the next; β the rotation
by 180◦about the circular axis of Fig. 2; and γ the 180◦rotation about the horizontal
axis. These elements generate a group of symmetries of order 4p:
G(p, s) = ⟨α, β, γ : αp = βs, β2 = 1, γ2 = 1, αβ = βα, γβ = βγ, γ−1αγ = α−1⟩
∼= D2p × C2
if s is even
∼= D4p
if s is odd,
where D2n and C2 denote the dihedral group of order 2n and the cyclic group of order
2.
γ
β
Figure 2
Theorem 5.1.
(i)
C(p′, s′) is commensurable with C(p, s) if (p′+s′, s′) = ±(p+s, s) or ±(−s, p+
s) and is commensurable with C(p, s) with reversed orientation if (p′ + s′, s′) =
±(p + s, −s) or ±(s, p + s).
(ii)
C(p, s) has a hyperbolic structure (complete of ﬁnite volume) if and only if
{|p + s|, |s|}̸ ⊂{0, 1, 2}.
(iii) C(p, s) is arithmetic (and hence has inﬁnitely many hidden symmetries) if and only if
(|p+s|, |s|) or (|s|, |p+s|) is in (3, 0), (3, 1), (3, 2), (3, 3), (4, 0), (4, 2), (4, 4),
(6, 0). The ﬁeld of deﬁnition k(C(p, s)) is then Q(
√
−d) with d respectively 7,
1, 3, 1, 3, 7, 2, and 15.
(iv) If C(p, s) is hyperbolic and non-arithmetic then it has no orientation preserving
hidden symmetries and its full orientation preserving symmetry group is G(p, s)
(so π1C(p, s) is normal in its orientation preserving commensurator with quotient
G(p, s)).
(v) If C(p, s) is hyperbolic and non-arithmetic then it has an orientation reversing
commensurability if and only if p + s = ±s or p + s = 0 or s = 0.
In the remainder of this section we give the topological part of the proof—part (i),
the “only if” of (ii), and the “if” of (v). In the next section we describe the hyperbolic
structures on chain link complements by means of Dehn surgery on a component of the
Whitehead link and compute some of their arithmetic invariants; (ii) of the theorem is a
side-product. In the subsequent two sections we prove parts (iii) and (iv) and (v).
We shall be using Dehn surgery a lot, so we brieﬂy recall the basic terminology. Let
M be a 3-manifold with an end homeomorphic to T 2 ×[0, ∞), where T 2 is the 2-torus.
We can cut off the end to get a 3-manifold M0 = M −T 2 × (1, ∞) with a boundary
component T 2 = T 2 ×{1}. Let m, l be some chosen basis of H1(T 2; Z) and let (p, q)
be a coprime integer pair. We can paste a solid torus onto M0 at the boundary component
T 2 to kill the homology class pm + ql. This process is called “(p, q) Dehn ﬁlling” the
chosen end of M. If the end of M resulted by removing a knot K from a manifold N,
then we also speak of “(p, q) Dehn surgery” on K.
We shall also need orbifold versions of Dehn ﬁlling and Dehn surgery. If (p, q) is
an integer pair that is not coprime, say d = gcd(p, q), then (p, q) Dehn ﬁlling means
the following: ﬁrst perform (p/d, q/d) Dehn ﬁlling and then give the core circle of the
added solid torus a transverse angle of 2π/d, so that it becomes the singular set of an
orbifold structure with local group Cd (the cyclic group of order d).
Figure 3
Let τ be the involution on T 2 which acts by multiplication by −1 on H1(T 2)
(Fig. 3). The orbit space P = T 2/τ is a 2-sphere with four order 2 orbifold points
(points with cone angle π ). The involution τ extends to any solid torus D2 × S1 that
T 2 bounds and (D2 × S1)/τ is the orbifold Q of Fig. 4 with ∂Q = P . Thus, given a
3-orbifold M with an end homeomorphic to P × [0, ∞), and a chosen homology basis
2
2
2
2
Figure 4
Figure 5
for the double cover T 2 of P , we can deﬁne (p, q) Dehn ﬁlling the end of M to mean
the process of cutting off the end and replacing it by Q in a way that induces (p, q) Dehn
ﬁlling by a solid torus in the double cover of the end.
Proof of (i) and “if” of (v) of Theorem 5.1. Let W denote the complement of the
Whitehead link pictured in Fig. 5. We can obtain C(p, 2q) by performing (p, q) Dehn
ﬁlling of W at one component of the Whitehead link (with respect to the standard
meridian/longitude pair) and then taking the p-fold cover of the resulting manifold or
orbifold (it is an orbifold if gcd(p, q)̸ = 1). To obtain C(p, s) this way for s odd, one
can give an interpretation of (p, q) Dehn ﬁlling for q half-integral, but instead we shall
use a suitable quotient of W .
W double covers the orbifold W ′ pictured in Fig. 6, with one toral end and one end
whose cross section is a sphere with four order 2 orbifold points.
(p, s) Dehn ﬁlling
the toral end of W ′ lifts to (p, s/2) Dehn ﬁlling of one end of W . In fact, the result
W ′(p, s) of this (p, s) Dehn ﬁlling is simply the quotient of C(p, s) by the subgroup
G0 = ⟨α, β⟩of G(p, s). If we quotient W ′ by the symmetry γ we obtain the orbifold
W ′′ pictured in Fig. 7. Its underlying space is S3 with two balls removed, i.e., S2 × I.
We have re-drawn W ′′ in Fig. 8 in a more symmetric fashion; it has an order 2 rotational
symmetry about its vertical axis and reﬂection symmetries across appropriate vertical
planes.
Let W ′′(p, s) be the corresponding quotient of W ′(p, s) (so W ′′(p, s) results by
(p, s) Dehn ﬁlling one end of W ′ —the end is ﬁlled by the orbifold of Fig. 4). By drawing
2
Figure 6
2
2
2
2
Figure 7
2
2 2
2
2 2
2
Figure 8
the curves killed by the Dehn ﬁlling (or by a homological calculation) it is not hard to see
that the rotational symmetry of W ′′ takes (p, s) Dehn ﬁlling to (p + 2s, −p −s) Dehn
ﬁlling, so W ′′(p, s) ∼= W ′′(p+2s, −p−s). Note that (p, s) and (−p, −s) Dehn ﬁlling
mean the same thing, and (p′, s′) = (p+2s, −p−s) implies (p′ +s′, s′) = (s, −p−s),
so the orientation preserving commensurability of the theorem is proved. The reﬂection
symmetries of W ′′ take (p, s) Dehn ﬁlling to (p, −p −s) and (p + 2s, −s) Dehn
ﬁlling, so W ′′(p, s) ∼= W ′′(p, −p −s) and W ′′(p + 2s, −s). This gives the orientation
reversing commensurabilities of the theorem.
If W(p1, q1; p2, q2) denotes the result of Dehn ﬁlling at both cusps of W (that is,
(p1, q1) and (p2, q2) Dehn surgery on the two components of the Whitehead link) and
similarly for W ′′ then the same argument shows:
Proposition 5.2. W ′′(p1, s1; p2, s2) ∼= −W ′′(p1, −p1 −s1; p2 + 2s2, −s2), where the
minus sign signiﬁes reversed orientation, so W(p1, q1; p2, q2) is commensurable with
−W(p1, −p1/2 −q1; p2 + 4q2, −q2).
Figure 9
Proof of “only if” of part (ii) of Theorem 5.1.. We must show non-hyperbolicity for
the cases claimed. For this it sufﬁces, by the commensurability statement of part (i),
to consider the ﬁve cases (p, s) = (1, 0), (2, 0), (2, −1), (3, −1), and (4, −2). The
(p, s) chain link is then respectively the unknot, the (4, 2) cable link, the two component
unlink, the (3, 3) cable link, and the link pictured in Fig. 9, which has an essential
torus separating the pairs of parallel components. None of these admits a complete ﬁnite
volume hyperbolic structure.

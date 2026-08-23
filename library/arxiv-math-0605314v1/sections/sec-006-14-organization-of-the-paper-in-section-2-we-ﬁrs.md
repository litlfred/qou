---
doc_id: arxiv-math-0605314v1
doc_title: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres"
section_id: sec-006-14-organization-of-the-paper-in-section-2-we-ﬁrs
section_title: "Organization of the paper. In Section 2, we ﬁrst recall the deﬁnition of"
section_number: 1.4
pages: 4-6
source_pdf: 0605314v1.pdf
source_sha256: 5fb8b89b432401ea
doc_brief: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres — W e construct an invariant JM of integral homology spheres M with values in a completion ˆZ[q] of the polynomial ring"
---
the quantized enveloping algebra Uh = Uh(sl2) of the Lie algebra sl2, which is a
h-adically complete Hopf Q[[h]]-algebra, and then introduce Z[q,q −1]-subalgebras
Uq, where Z[q,q −1] is regarded as a subring of Q[[h]] by setting q = exph. The Hopf
algebra structure of Uh induces a Hopf algebra structure on Uq. We also introduce
a Z[q,q −1]-subalgebraU ev
q , which is the even part of Uq with respect to a natural
(Z/2Z)-grading of Uq. We deﬁne completions ˜Uq and ˜U ev
q of the algebras Uq and
U ev
q , and also completed tensor products of copies of ˜Uq and ˜U ev
q . ˜Uq is equipped
with a complete Hopf algebra structure induced by the Hopf al gebra structure of
Uq.
In Section 3, we ﬁrst recall the ribbon Hopf algebra structur e for Uh, and then
the braided Hopf algebra structure Uh
, canonically deﬁned for Uh. The main ob-
servation in this section (Theorem 3.1) is that ˜U ev
q is equipped with a braided Hopf
algebra structure inherited from that for Uh.
In Section 4, we ﬁrst recall from [20] the notion of bottom tan gles. An n-
component bottom tangle T is a tangle in a cube consisting of n arc components
whose endpoints lie in a line in the bottom square of the cube i n such a way that
between the two endpoints of each arc there are no endpoints o f other arcs. Then
we adapt the universal invariants for bottom tangles associ ated to the ribbon Hopf
algebra to the case of Uh. The universal invariant JT of T takes values in the
invariant part Inv(U ˆ⊗n
h ) of the n-fold completed tensor product U ˆ⊗n
h of Uh, where
the invariant part is considered with respect to the standar d tensor product left Uh-
module structure deﬁned using the left adjoint action of Uh. The main observation
in this section (Theorem 4.1) is that if T is an n-component, algebraically-split,
0-framed bottom tangle, then JT is contained in the invariant part Kn of the n-fold
A UNIFIED WITTEN-RESHETIKHIN-TURAEV INV ARIANT 5
completed tensor product ( ˜U ev
q ) ˜⊗n of ˜U ev
q . (Recall that a link L is algebraically
split if the linking number of any two distinct components are zero .) The proof of
Theorem 4.1 uses the braided Hopf algebra structure of ˜U ev
q .
For a 0-framed bottom knot (i.e., 1-component bottom tangle )T , the universal
invariantJT ofT takes values in the center Z( ˜U ev
q ) of ˜U ev
q . In view of a result proved
in [19], this implies that we can express JT as an inﬁnite sum ∑
p≥0ap(T )σp, where
ap(T )∈ Z[q,q −1], p≥ 0, and where σp∈ Z(U ev
q ), p≥ 0, are a certain basis of
Z(U ev
q )⊂ Z( ˜U ev
q ). Each ap(T ) gives a Z[q,q −1]-valued invariant of T , which may
be regarded also as an invariant of the closure cl(T ) of T .
In Section 5, we recall the deﬁnition of the colored Jones pol ynomialJL(W1,... ,W n)
of a framed link L = L1∪···∪ Ln, where each component Li of L is colored by
a ﬁnite-dimensional, irreducible representation Wi ofUh(sl2). Then we recall from
[20] a formulation of the colored Jones polynomial using uni versal invariant of bot-
tom tangle:
JL(W1,... ,W n) = (tr W1
q ⊗···⊗ trWn
q )(JT ),
whereT is a bottom tangle whose closure is L, and where tr Wi
q : Uh→ Q[[h]] is the
quantum trace in Wi.
Recall that for each d≥ 0 there is exactly one ( n + 1)-dimensional, irreducible
representation of Uh up to isomorphism, denoted by Vd. We need extensions of the
colored Jones polynomials for framed links whose component s are colored by linear
combinations (over Q(v), Z[v,v −1], etc., where v =q1/2 = exp h
2 ) of the Vd, which
are deﬁned naturally by multilinearity.
In Section 6, we relate the universal invariant JT ∈ Z( ˜U ev
q ) and the Z[q,q −1]-
valued invariants ap(T ), p≥ 0, of a bottom knot T deﬁned in Section 4 to the
colored Jones polynomials of the closure cl(T ) of T . Theorem 6.4 identiﬁes ap(T )
with Jcl(T )(P ′′
p ), where P ′′
p is a Q(v)-linear combination of V0, V1,... , Vp.
In Section 7, we give some remarks on the universal invariant JT∈Z( ˜U ev
q ) for a
bottom knot. First of all, Z( ˜U ev
q ) is identiﬁed with a completion Λ of Z[q,q −1,t +
t−1]. For a knot K = cl(T ) with T a bottom knot, we set JK(t,q ) = JT ∈ Λ
by abuse of notation, which we call the two-variable colored Jones invariant of K.
The normalized colored Jones polynomial JK(Vn)/Junknot(Vn)∈ Z[q,q −1] is equal
to the specialization JK (qn+1,q ) of JK(t,q ). The specialization JK(1,q )∈ ˆZ[q] can
be regarded as a universal form for the Kashaev invariants of K. We relate the
invariantJK(t,q ) to Rozansky’s integral version of the Melvin-Morton expan sion of
the colored Jones polynomials of K, and give several conjectures which generalizes
Rozansky’s rationality theorem.
In Section 8, we consider invariants of algebraically-spli t links. We deﬁne a
Z[q,q −1]-algebraP which is spanned by certain normalizations ˜P ′
n ofP ′′
n , and deﬁne
a completion ˆP ofP. We show that for any n-component, algebraically-split, 0-
framed link L and for any elements x1,... ,x n∈ ˆP, there is a well-deﬁned element
JL(x1,... ,x m)∈ ˆZ[q], see Corollary 8.3. In the proof, results proved in the prev ious
sections, such as Theorem 4.1, are used.
In Section 9, we deﬁne an element ω in the ring ˆP. Theorem 9.4 states that for
any (m + 1)-component, algebraically-split, 0-framed link L1∪···∪ Lm∪K such
thatK is an unknot, and for x1,... ,x m∈ ˆP, we have
JL∪K(x1,... ,x m,ω ∓1) = JL(K, ±1)(x1,... ,x m).

---
doc_id: arxiv-1507.06276v2
doc_title: "UNIVERSAL K-MATRIX FOR QUANTUM SYMMETRIC PAIRS"
section_id: sec-010-31-the-algebra-u
section_title: "The algebra U"
section_number: 3.1
pages: 12-13
source_pdf: 1507.06276v2.pdf
source_sha256: f552aa5de7125b23
toc_source: outline
doc_brief: "UNIVERSAL K-MATRIX FOR QUANTUM SYMMETRIC PAIRS — Let g be a symmetrizable Kac-Moody algebra and let Uq(g) de- note the corresponding quantized enveloping algebra."
---
category O. Recall that category O consists of all ﬁnitely generated Uq(g)-modules
M which decompose into weight spaces M = ⊕λ∈PMλ and on which the action of
U + is locally ﬁnite. Objects in Oint are additionally locally ﬁnite with respect to the
action ofUqi(sl2)i for alli ∈I. Simple objects in Oint are irreducible highest weight
modules with dominant integral highest weight [Lus94, Corollary 6.2.3 ]. If g is of
ﬁnite type then Oint is the category of ﬁnite dimensional type 1 representations.
Let Vect be the category of vector spaces over K(q1/d). Both Vect and Oint are
tensor categories, and the forgetful functor
For : Oint → Vect
is a tensor functor. Let U = End(For) be the set of natural transformations from
For to itself. The category Oint is equivalent to a small category and hence U is
indeed a set. More explicitly, elements of U are families (ϕM )M∈Ob(Oint) of vector
space endomorphisms ϕM : For(M ) → For(M ) such that the diagram
For(M )
ϕM /d47/d47
For(ψ)
/d15/d15
For(M )
For(ψ)
/d15/d15
For(N )
ϕN /d47/d47For(N )
commutes for any Uq(g)-module homomorphism ψ :M →N . Natural transforma-
tions of For can be added and multiplied by a scalar, both operations coming from
the linear structure on vector spaces. Composition of natural tr ansformations gives
a multiplication on U which turns U into a K(q1/d)-algebra.
Example 3.1. The action of Uq(g) on objects of Oint gives an algebra homomor-
phism Uq(g) → U which is injective, see [Lus94, Proposition 3.5.4] and [Jan96,
5.11]. We always consider Uq(g) a subalgebra of U .
Example 3.2. Let ˆU + = ∏
µ∈Q+U +
µ and let (Xµ)µ∈Q+ ∈ ˆU +. Let M ∈Ob(Oint)
and m ∈ M . As the action of U + on M is locally ﬁnite there exist only ﬁnitely
many µ ∈Q+ such that Xµm ⁄= 0. Hence the expression
∑
µ∈Q+
Xµm(3.1)
is well deﬁned. In this way the element (Xµ)µ∈Q+ ∈ ˆU + deﬁnes an endomorphism
of For, and we may thus consider ˆU + as a subalgebra of U . We sometimes write
UNIVERSAL K-MATRIX FOR QUANTUM SYMMETRIC PAIRS 13
elements of ˆU + additively as X = ∑
µ∈Q+Xµ. In view of (3.1) this is compatible
with the inclusions U + ⊆ ˆU + ⊆ U .
Example 3.3. Let ξ : P → K(q1/d) be any map. For M ∈ Ob(Oint) deﬁne a
linear map ξM : M → M by ξM (m) = ξ(λ)m for all m ∈ Mλ. Then the family
(ξM )M∈Ob(Oint) is an element in U . By slight abuse of notation we denote this
element by ξ as well.
Lusztig showed that U contains a homomorphic image of the braid group cor-
responding to W . For any M ∈Ob(Oint) and any i ∈I the Lusztig automorphism
TiM :M →M is deﬁned on m ∈Mλ with λ ∈P by
TiM (m) =
∑
a,b,c≥0
a−b+c=λ(hi)
(−1)bqb−ac
i E(a)
i F (b)
i E(c)
i m.(3.2)
The family Ti = (TiM ) deﬁnes an element in U . By [Lus94, Proposition 5.2.3] the
elementsTi of U are invertible with inverse T −1
i = (Ti
−1
M ) given by
Ti
−1
M (m) =
∑
a,b,c≥0
a−b+c=λ(hi)
(−1)bqac−b
i F (a)
i E(b)
i F (c)
i m
By [Lus94, 39.43] the elements Ti for i ∈I satisfy the braid relations
TiTjTi.../bracehtipupleft /bracehtipdownright/bracehtipdownleft/bracehtipupright
mij factors
= TjTiTj.../bracehtipupleft /bracehtipdownright/bracehtipdownleft/bracehtipupright
mij factors
where mij denotes the order of σiσj ∈ W . Hence, for any w ∈ W there is a well
deﬁned element Tw ∈ U given by
Tw =Ti1Ti2...T ik
if w =σi1σi2...σ ik is a reduced expression.
We also use the symbol Ti for i ∈ I to denote the corresponding algebra auto-
morphism of Uq(g) denoted by T ′′
i,1 in [Lus94, 37.1]. This is consistent with the
above notation, in the sense that for any u ∈ Uq(g), any M ∈ Ob(Oint), and any
m ∈M we haveTiM (um) = Ti(u)TiM (m). Hence Ti, as an automorphism of Uq(g),
is nothing but conjugation by the invertible element Ti ∈ U . In this way we obtain
automorphisms Tw of Uq(g) for all w ∈W .
Furthermore, the bar involution for Uq(g) intertwines Ti and T −1
i . More explic-
itly, for u ∈U +
µ one has
(3.3) Ti(u) = ( −1)µ(hi)q(µ,αi)T −1
i (u),
see [Lus94, 37.2.4]

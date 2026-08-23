---
doc_id: arxiv-1601.02479v5
doc_title: "Cohomological Donaldson-Thomas theory of a quiver with potential and quantum enveloping algebras"
section_id: sec-026-63-proof-of-theorem-c-and-construction-of-the-bp
section_title: "Proof of Theorem C and construction of the BPS Lie algebra"
section_number: 6.3
pages: 56-60
source_pdf: 1601.02479v5.pdf
source_sha256: 52c2dcd4adf2e72b
doc_brief: "Cohomological Donaldson-Thomas theory of a quiver with potential and quantum enveloping algebras — This paper concerns the cohomological aspects of Donaldson – Thomas theory for Jacobi algebras and"
---
start with a couple of technical lemmas for the proofs in this section .
Lemma 6.5. Let F , G ∈ MMHM(X). Then f : F → G is an isomorphism if and
only if fx is an isomorphism for every closed point x ∈ X.
Proof. One implication is trivial, so we assume that fx is an isomorphism for every
x and prove that f is an isomorphism. Since the functor
forgmon
X : MMHM( X) → Perv(X)
is faithful, it suﬃces to prove the lemma with the category MMHM( X) replaced
by Perv( X). Write C = cone( f ). Assume for a contradiction that C ⁄= 0. Let
i ∈ Z be the lowest number such that the constructible cohomology shea f Hi
con(C)
is nonzero, and set
R := Hi
con(C)[−i].
Denote by ιx :֒→X the inclusion. The functor ι∗
x is exact for the natural t-
structure on the derived category of constructible sheaves, an d there is an isomor-
phism ι∗
xC ∼
= cone(fx), so the ﬁrst term in the exact sequence
→ H i−1
con (ι∗
xτ>iC) → H i
con(ι∗
xR) → H i
con(ι∗
xC) → .
COHAS AND QUANTUM ENVELOPING ALGEBRAS 57
is zero, as well as the last, by supposition. Then R[i] is a nonzero constructible
sheaf satisfying ι∗
xR[i] = 0 for all x, a contradiction. □
Lemma 6.6. Let F , G ∈ MMHM(X), with forgmon
X (F ) and forgmon
X (G) semisimple
perverse sheaves, and let f : F → G be a morphism between them. Then f = 0 if
and only if fx = 0 for every closed point ιx :֒→X.
Proof. Again, one direction is trivial, and we may assume that we are working in
Perv(X) throughout, by faithfulness of forg mon
X . So assume that fx = 0 for all x.
Let {St}t∈T be the set of all simple perverse sheaves appearing in a direct sum
decomposition of F and G. Then there is a commutative diagram
⨁
t∈T St ⊗C Hom(St, F )
∼
= /d47/d47
⨁
t idt ⊗ft
/d15/d15
F
f
/d15/d15⨁
t∈T St ⊗C Hom(St, G)
∼
= /d47/d47
G
where id t : St → St is the identity map, and ft : Hom( St, F ) → Hom(St, G) is
obtained from composition with f . Writing
St = ˜IC Y (L)[dim(Y )]
for Y ⊂ X a closed irreducible subvariety, and L a local system deﬁned on Y ′ ⊂ Y
a regular open subvariety, and picking x ∈ Y ′, we deduce that ι∗
x idt ⁄= 0, and so
ft = 0 for all t. □
With these lemmas in hand, we move back to consideration of cohomolo gical Hall
algebras. Throughout this section we assume that ζ isµ -generic. By Proposition
4.11 there is a canonical embedding
ι = H(dim∗ ˜ωζ ,!
µ Υζ
W,µ )
of H(B C*)vir ⊗ BPSζ ,S
W,µ inside Gr P(H(Aζ ,S
W,µ )).
Proposition 6.7. The subspace ι(H(BC*)vir ⊗ BPSζ ,S
W,µ ) is a primitive subspace in
GrP(H(Aζ ,S
W,µ )), i.e. the following composition of maps is zero:
⨁
d∈Λ ζ
µ \{0}
H(BC*)vir ⊗ BPSζ ,S
W,d
ι
− →GrP(H(Aζ ,S
W,µ ))
GrP(∆ ζ , S
W,µ )
− − − − − − − →
⨁
d′,d′′∈Λ ζ
µ
GrP
(
(H(Aζ ,S
W,d′) ⊠tw
+ H(Aζ ,S
W,d′′ ))[L−1
d′,d′′ ]
)
։
⨁
d′,d′′∈Λ ζ
µ \{0}
GrP
(
(Aζ ,S
W,d′ ⊠tw
+ Aζ ,S
W,d′′ )[L−1
d′,d′′ ]
)
.
Proof. We need to show that for decompositions d = d′ + d′′, with d′ ⁄= 0 ⁄= d′′,
the image of ι(H(BC*)vir ⊗ BPSζ ,S
W,d) under the map
GrP(∆ ζ ,S
d′,d′′ ) : H
(
Mζ -ss,S
d , ˜ω!
d H
(
pζ
d,∗φ mon
Tr(W )ζ
d
IC Mζ -ss
d
))
→
(100)
(
H
(
Mζ -ss,S
d′ , H
(
pζ
d′,∗φ mon
Tr(W )ζ
d′
IC Mζ -ss
d′
))
⊠tw
+ H
(
Mζ -ss,S
d′′ , H
(
pζ
d′′,∗φ mon
Tr(W )ζ
d′′
IC Mζ -ss
d′′
)))
[L−1
d′,d′′ ]
is zero. We assume that Mζ -st
d ⁄= ∅, or the statement is trivial, for then by deﬁnition
BPSζ ,S
W,d = 0. Denote by RΓ the derived global sections functor on Mζ -ss,S
d . In
58 BEN DA VISON AND SVEN MEINHARDT
terms of the commutative diagram
(101)
RΓ
(
˜ωζ ,!
d H
(
pζ
µ ,∗φ mon
Tr(W )ζ
d
IC Mζ -ss
d
(Q)
)) GrP(γ ) /d47/d47
RΓ
(
˜ωζ ,!
d H
(
pζ
µ ,∗sd′,d′′,∗φ mon
Tr(W )ζ
d′, d′′
L(d,d)/2
Mζ -ss
d′, d′′
))
RΓ
(
˜ωζ ,!
d φ mon
T r(W )ζ
d
H
(
pζ
µ ,∗IC Mζ -ss
d
(Q)
)) γ ′
/d47/d47
L(d, d)/ 2⊗RΓ (˜ωζ , !
d ν d)
/d79/d79
RΓ
(
˜ωζ ,!
d φ mon
T r(W )ζ
d
H
(
pζ
µ ,∗sd′,d′′,∗L(d,d)/2
Mζ -ss
d′ , d′′
))
L(d, d)/ 2⊗RΓ (˜ωζ , !
d ν d′, d′′ )
/d79/d79
RΓ
(
˜ωζ ,!
d φ mon
T r(W )ζ
d
IC Mζ -ss
d
(Q) ⊗ H(BC*)vir
)
ι
/d79/d79withγ as in (93), it is suﬃcient to show that
GrP(γ ) ◦ (L(d,d)/2 ⊗ RΓ(˜ωζ ,!
d ν d)) ◦ ι = 0.
The maps ν d andν d′,d′′ are as in Proposition 4.3. On the other hand, the map γ ′ι
is obtained by applying RΓ
(
˜ωζ ,!
d φ mon
T r(W )ζ
d
)
to a map
H(BC*)vir ⊗ IC Mζ -ss
d
(Q) → H
(
pζ
µ ,∗sd′,d′′,∗L(d,d)
Mζ -ss
d′, d′′
)
(102)
which preserves perverse degree, and so is necessarily zero, sinc e for every coho-
mological degree, the domain and the target of (102) are pure com plexes of mixed
Hodge modules with distinct strict support. □
Let Pζ ,S
W,µ ⊂ GrP(H(Aζ ,S
W,µ )) be the subalgebra generated by
⨁
d∈Λ ζ
µ
H(BC*)vir ⊗ BPSζ ,S
W,d .
Since Pζ ,S
W,µ is generated by primitive elements of the localised Hopf algebra, it
follows from Lemma 6.3 that the localised bialgebra structure on Pζ ,S
W,µ lifts to
an honest cocommutative bialgebra structure. Here, cocommuta tivity is with re-
spect to the symmetrizing morphism τ sw deﬁned in Section 6.1. We denote by
∆
ζ ,S
W,µ : Pζ ,S
W,µ → Pζ ,S
W,µ ⊠+ Pζ ,S
W,µ the induced coproduct.
Corollary 6.8. Assume that ζ isµ -generic. The triple
(
Pζ ,S
W,µ , H
(
dim∗ H(˜∗ζ ,S
W,µ )
)
, ∆
ζ ,S
W,µ
)
.
extends to a Hopf algebra.
Proof. All that is missing is a compatible antipode, but existence and uniquene ss
of an antipode is a formal consequence of connectedness of the a lgebra. □
We deﬁne H(Γζ
W,µ ) to be the composition of maps in the following diagram
τ Sym⊠⊕(H(BC*)vir ⊗ BPSζ
W,µ )/d31 /d127 /d47/d47
Free⊠⊕(H(BC*)vir ⊗ BPSζ
W,µ )
Free⊠⊕ (Υζ
W,µ )/d115/d115❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤
Free⊠⊕
(
H(Aζ
W,µ )
)
/d47/d47
H
(
Aζ
W,µ
)
,
COHAS AND QUANTUM ENVELOPING ALGEBRAS 59
where the upper horizontal arrow comes from the natural inclusio n
τ Symn
⊠⊕ (H(BC*)vir⊗BPSζ
W,µ ) ⊂
(
H(BC*)vir ⊗ BPSζ
W,µ
)
⊠⊕ . . . ⊠⊕
(
H(BC*)vir ⊗ BPSζ
W,µ
)
/bracehtipupleft
/bracehtipdownright/bracehtipdownleft /bracehtipupright
n times
,
the lower horizontal arrow is given by iterated relative CoHA multiplica tion, and
Υζ
W,µ is as in (63). The relative version of Theorem C amounts to the followin g
theorem.
Theorem 6.9. The map H(Γζ
W,µ ) is an isomorphism.
Proof. It is enough to show that Ξ = Dmon
Mζ -ss
µ
H(Γζ
W,µ ) is an isomorphism, and for
this it is enough to show that Ξ |x is an isomorphism for each x a point in Mζ -ss
d ,
with d ∈ Λζ
µ , by Lemma 6.5. Let x represent the polystable d-dimensional CQ-
representation ⨁
i
Vi ⊗Cρi
where the ρi are pairwise distinct ζ-stable CQ-representations of slope µ , and Vi
are ﬁnite-dimensional complex vector spaces. Let Mx ⊂ Mζ -ss
µ be the reduced
substack, of which the closed points represent CQ-representations that are objects
of the Serre subcategory for which the objects are all of the iter ated extensions of
the representations ρi. Let Mx ⊂ Mζ -ss
µ be the discrete subscheme for which the
points represent ﬁnite direct sums of the ρi. Then
Mx ∩ Mζ -ss
d ⊃ (pζ
µ )−1(x)
and Mx
d ⊂ Mζ -ss
d is a discrete set of points containing x. So Ξ |x is an isomorphism
if and only if Ξ |Mx
d is. By Theorem A and Proposition 6.2, there is an isomorphism
of NQ0 ⊕ Z-graded vector spaces (the extra Z-factor is the cohomological grading)
(103) τ Sym⊠+
(
H(BC*)vir ⊗ BPSζ ,x
W,µ
)
∼
= Hc(Mx, ICζ
W,µ )∨.
On the other hand, by Proposition 6.7 the subspaces
H(BC*)vir ⊗ BPSζ ,x
W,µ ⊂ GrP
(
Hc(Mx, ICζ
W,µ )∨
)
are primitive for the induced coproduct, so they form a Lie algebra u nder the com-
mutator Lie bracket. Letting g be the space of primitives for Gr P
(
Hc(Mx, ICζ
W,µ )∨
)
,
and letting U (g) be the universal enveloping algebra of g,then by the Milnor–Moore
theorem, there is an isomorphism
U (g) ∼
= GrP
(
Hc(Mx, ICζ
W,µ )∨
)
.
Setting υ = H(dim∗ ˜ω!
µ H(ΓW,µ )) there is a commutative diagram
τ Sym⊠+
(
H(BC*)vir ⊗ BPSζ ,x
W,µ
)
/d127 /d95
/d15/d15
∼= /d47/d47
υ
/d42/d42❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯
U
(
H(BC*)vir ⊗ BPSζ ,x
W,µ
)
/d15/d15
τ Sym⊠+ (g)
∼
= /d47/d47
GrP
(
Hc(Mx, ICζ
W,µ )∨
)
where the top and bottom horizontal arrows are the PBW isomorph ism and the
Milnor–Moore isomorphism, respectively. It follows that υ is injective, and hence an
isomorphism, since the domain and the codomain have the same grade d dimensions,
by (103). The dual of the restriction of this map to the degree d piece is Ξ |Mx
d ,
which is thus an isomorphism, as required. □
60 BEN DA VISON AND SVEN MEINHARDT
We construct the map
H(Γζ ,S
W,µ ) :τ Sym⊠+
(
H(BC*)vir ⊗ BPSζ ,S
W,µ
)
→ H
(
Aζ ,S
W,µ
)
in the same way as H(Γζ
W,µ ), using Corollary 5.9 instead of Corollary 4.11. Then
this map preserves the perverse ﬁltration, and
GrP
(
H(Γζ ,S
W,µ )
)
= H(dim∗ ˜ωζ ,!
µ H(Γζ
W,µ ))
is an isomorphism, so that H( Γζ ,S
W,µ ) is at least an injection. The domain and target
of this map are graded vector spaces of the same dimension (ﬁnite in every graded
degree) by Theorem A. It follows that H( Γζ ,S
W,µ ) is an isomorphism. This completes
all but the free commutativity statements of Theorem C, which we n ow deduce as
a corollary.
Corollary 6.10. The (twisted) relative cohomological Hall algebra H(Aζ ,S
W,µ ) is a
free commutative algebra (for the symmetrizing morphism τsw), as is the algebra
GrP
(
H(Aζ ,S
W,µ )
)
, and so the twisted algebra GrP
(
H(ψ Aζ ,S
W,µ )
)
is a free supercom-
mutative algebra (for the usual symmetrizing morphism sw).
Proof. The result regarding the relative cohomological Hall algebra follows f rom
Theorem 6.9 and the claim that H(Aζ
W,µ ) is commutative. This claim in turn can
be checked at ﬁbres as in the proof of Theorem 6.9, this time using Le mma 6.6,
and so it is suﬃcient to prove commutativity for Gr P
(
H(Aζ ,S
W,µ )
)
(as in the same
proof). Let P ⊂ K = Gr P
(
H(Aζ ,S
W,µ )
)
be the subspace of primitives. Then the
algebra generated by P is a cocommutative sub bialgebra of K, and so there is a
chain of inclusions
τ Sym
(
H(BC*)vir ⊗ BPSζ ,S
W,µ
)
⊂τ Sym(P) ⊂ K
where the ﬁrst inclusion is given by Proposition 6.7 and the second by t he Milnor–
Moore theorem. Since by Theorem A the ﬁrst and last graded vecto r spaces have the
same graded dimensions, all of the inclusions are equalities, and in par ticular P =
BPSζ ,S
W,µ ⊗ H(BC*)vir, and K is the universal enveloping algebra of P, considered
as a Lie sub-algebra of K. On the other hand, the Lie bracket on P is zero, since
it respects the perverse grading, and P is concentrated entirely in odd perverse
degree. The statement regarding the ψ -twisted algebra then follows. □
Finally, we are in a position to deﬁne the BPS Lie algebra:
Corollary 6.11. Letψ be as in (16). The subspace
L1/2 ⊗ BPSζ ,S
W,µ = P≤1
(
H(Aζ ,S
W,µ )
)
⊂ H(Aζ ,S
W,µ )
is closed under the commutator Lie bracket in H(ψ Aζ ,S
W,µ ), and so carries the struc-
ture of a Lie algebra, called the BPS Lie algebra .
The proof is an immediate consequence of Corollary 6.10, as explained in Section
1.7.

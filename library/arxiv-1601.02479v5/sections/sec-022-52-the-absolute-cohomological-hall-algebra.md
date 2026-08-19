---
doc_id: arxiv-1601.02479v5
doc_title: "COHOMOLOGICAL DONALDSON–THOMAS THEORY OF A"
section_id: sec-022-52-the-absolute-cohomological-hall-algebra
section_title: "The absolute cohomological Hall algebra"
section_number: 5.2
pages: 46-50
source_pdf: 1601.02479v5.pdf
source_sha256: 52c2dcd4adf2e72b
doc_brief: "COHOMOLOGICAL DONALDSON–THOMAS THEORY OF A — This paper concerns the cohomological aspects of Donaldson – Thomas theory for Jacobi algebras and the associated cohomo logical Hall alge- bra"
---
W,µ ), a monoid in the
monoidal category (D≥,lf (MMHM(NQ0 )), ⊠tw
+ ), deﬁned by Kontsevich and Soibel-
man (we recall the deﬁnition below). I.e. we obtain the “ambi ent perverse associated
graded” monoid
(86) Gr P(H(Aζ ,S
W,µ )) = H
(
dim∗ ˜ωζ ,!
µ H
(
Aζ ,S
W,µ
))
.
COHAS AND QUANTUM ENVELOPING ALGEBRAS 47
See Proposition 5.7 for a more precise statement. The notati on in the left hand
side of (86) will be justiﬁed after we introduce the (ambient ) perverse ﬁltration in
Section 5.3.
5.2. The absolute cohomological Hall algebra. We start to complete Remark
5.4 by recalling the deﬁnition of the cohomological algebra structure on H( Aζ ,S
W,µ )
from [30]. Extending (78, 79) we set
Xζ -ss
d′ ■ d′′,N :=Xζ -ss
d′,d′′ ×Gd′ ×Gd′′ UN
Xζ -ss
d′ □ d′′,N :=(Xζ -ss
d′ × Xζ -ss
d′′ ) ×Gd′ ×Gd′′ UN .
We denote by
ω■ ,N : Xζ -ss,S
d′ ■ d′′,N → Xζ -ss
d′ ■ d′′,N
ω□ ,N : Xζ -ss,S
d′ □ d′′,N → Xζ -ss
d′ □ d′′,N
ω◦,N : Xζ -ss,S
d′,d′′,N → Xζ -ss
d′,d′′,N
the inclusions, and we denote by φ mon
■ ,□ ,◦ the vanishing cycle functors induced by
Tr(W ) on the targets of these three maps. Then for n ∈ Z and N ∈ N there is an
isomorphism
Φ : H n
c
(
r1,N,!ω∗
■ ,Nφ mon
■ QXζ -ss
d′ ■ d′′ ,N
→ ω∗
□ ,N r1,N,!φ mon
■ QXζ -ss
d′ ■ d′′ ,N
→ ω∗
□ ,Nφ mon
□ Lv
Xζ -ss
d′ □ d′′ ,N
) ∨
where v =∑
a∈Q1 d′′
s(a) d′
t(a), provided by base change and the Verdier dual of the
morphism
QXζ -ss
d′ □ d′′ ,N
→ r1,N,∗QXζ -ss
d′ ■ d′′,N
.
Similarly, we deﬁne the isomorphism
Ψ : H n
c
(
r2,N,!ω∗
■ ,Nφ mon
■ QXζ -ss
d′ ■ d′′ ,N
→ ω∗
◦,N r2,N,!φ mon
■ QXζ -ss
d′ ■ d′′ ,N
→ ω∗
◦,Nφ mon
◦ Lu
Xζ -ss
d′, d′′ ,N
) ∨
where u = ∑
i∈Q0 d′
i d′′
i . Taking N suﬃciently large (for each cohomological de-
gree), and composing the appropriate twist of Φ with Ψ −1, we deﬁne the isomor-
phism
αζ
d′,d′′ : H c
(
Mζ -ss,S
d′ ,φ mon
Tr(W )ζ
d′
IC Mζ -ss
d′
(Q)
) ∨
⊠+ Hc
(
Mζ -ss,S
d′′ ,φ mon
Tr(W )ζ
d′′
IC Mζ -ss
d′′
(Q)
) ∨
→
L−(d′′,d′)/2 ⊗ Hc
(
Mζ -ss,S
d′,d′′ ,φ mon
Tr(W )ζ
d′ , d′
IC Mζ -ss
d′, d′′
(Q)
) ∨
.
Similarly, with notation as in (80), applying H c
(
ω∗
Nφ mon
Tr(W )ζ
d,N
) ∨
to
QXζ -ss
d,N
→ sζ
d′,d′′,N,!QXζ -ss
d′, d′′ ,N
and passing to the limit, we obtain the morphism
β
ζ
d′,d′′ : H c
(
Mζ -ss,S
d′,d′′ ,φ mon
Tr(W )ζ
d′, d′
IC Mζ -ss
d′, d′′
(Q)
) ∨
→ L(d′,d′′)/2⊗Hc
(
Mζ -ss,S
d ,φ mon
Tr(W )ζ
d
IC Mζ -ss
d
(Q)
) ∨
.
We set
H(Aζ ,S
W,µ ) := H c(Mζ -ss,S
µ , ICζ
W,µ )∨
and
H(∗ζ ,S
W,µ ) :=
⨁
d′,d′′∈NQ0
(L−(d′,d′′)/2 ⊗
β
ζ
d′,d′′ ) ◦ (L⟨d′′,d′⟩/2 ⊗
αζ
d′,d′′ )
48 BEN DA VISON AND SVEN MEINHARDT
to obtain the “absolute cohomological Hall algebra” in the sense of S ection 1.2.
This is precisely the CoHA deﬁned and studied by Kontsevich and Soibe lman in
[30, Sec.7].
5.3. The ambient perverse ﬁltration. For f , d ∈ NQ0 set
γ (f , d) = ( d, d)/2 − f · d .
Since Mζ
f ,d is smooth, and πζ
f ,d : Mζ
f ,d → Mζ -ss
d is proper, by the decomposition
theorem there is an isomorphism
πζ
f ,d,!Lγ (f ,d)
Mζ
f , d
∼
= H
(
πζ
f ,d,!Lγ (f ,d)
Mζ
f , d
)
.
This decomposition is not canonical, but the mere existence of such a decomposition
implies that the natural map
Γ :πζ
f ,d,!Lγ (f ,d)
Mζ
f , d
→τ≥pπζ
f ,d,!Lγ (f ,d)
Mζ
f , d
admits a right inverse, where τ≥p is the truncation functor with respect to the
natural t-structure on the category of monodromic mixed Hodge modules. We
deduce that the morphism Γ′ given by the composition of natural maps
πζ
f ,d,!φ mon
T r(W )ζ
f , d
Lγ (f ,d)
Mζ
f , d
∼= /d47/d47
φ mon
T r(W )ζ
d
πζ
f ,d,!Lγ (f ,d)
Mζ
f , d
φ mon
T r(W )ζ
d
Γ
/d117/d117❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥
φ mon
T r(W )ζ
d
τ≥pπζ
f ,d,!Lγ (f ,d)
Mζ
f , d
∼= /d47/d47
τ≥pπζ
f ,d,!φ mon
T r(W )ζ
f , d
Lγ (f ,d)
Mζ
f , d
admits a right inverse Σ. With
˜ωζ
d : Mζ -ss,S
d → Mζ -ss
d
˜ωζ
f ,d : Mζ ,S
f ,d → Mζ
f ,d
the natural inclusions, there is a natural isomorphism given by base change
Ω : πζ ,S
f ,d,! ˜ωζ ,∗
f ,dφ mon
T r(W )ζ
f , d
Lγ (f ,d)
Mζ
f , d
→ ˜ωζ ,∗
d πζ
f ,d,!φ mon
T r(W )ζ
f , d
Lγ (f ,d)
Mζ
f , d
.
Setting
Pp
(
Hc
(
Mζ ,S
f ,d ,φ mon
T r(W )ζ
f , d
Lγ (f ,d)
) ∨)
:= Hc
(
Mζ ,S
f ,d , ˜ωζ ,∗
d τ≥−pπζ
f ,d,!φ mon
T r(W )ζ
f , d
Lγ (f ,d)
) ∨
∼
= H
(
Mζ ,S
f ,d , ˜ωζ ,!
d τ≤pπζ
f ,d,∗φ mon
T r(W )ζ
f , d
L−(d,d)/2
)
we consider the morphism ιp := H c
(
˜ωζ ,∗
f ,dΓ′ ◦ Ω
) ∨
. This is a split injection, since it
is the dual of a split surjection with right inverse H c(Ω −1 ◦ ˜ωζ ,∗
f ,dΣ). We thus arrive
at a canonical ﬁltration, indexed by p ∈ Z, which we call the ambient perverse
ﬁltration:
Pp
(
Hc
(
Mζ ,S
f ,d ,φ mon
T r(W )ζ
f , d
Lγ (f ,d)
) ∨)
⊂ Hc
(
Mζ ,S
f ,d ,φ mon
T r(W )ζ
f , d
Lγ (f ,d)
) ∨
.
Warning 5.5. Throughout the paper, we always consider the perverse trunc ation
functors for Mζ
d, and never the truncation functors for monodromic mixed Hod ge
modules on Mζ ,S
d . As a result, the associated graded of
Hc
(
Mζ ,S
f ,d ,φ mon
T r(W )ζ
f , d
Lγ (f ,d)
) ∨
∼
= H
(
Mζ ,S
d , ˜ωζ ,!
d πζ
f ,d,∗φ mon
T r(W )ζ
f , d
L−(d,d)/2
)
COHAS AND QUANTUM ENVELOPING ALGEBRAS 49
is in general not isomorphic as a graded object to the hyperco homology of the total
perverse cohomology of ˜ωζ ,!
d πζ
f ,d,∗φ mon
T r(W )ζ
f , d
L−(d,d)/2, for which the grading comes
from the perverse truncation functors for Mζ ,S
d . For example, let Q be the one loop
quiver, let W = 0 , let MS ⊂ M(Q) be the reduced substack, the closed points of
which correspond to nilpotent CQ-representations, let d = f = 1 , and let ζ be any
stability condition on Q. Then there are isomorphisms
Mζ
f ,d
∼
= Mζ -ss
d
∼
= A1
Mζ ,S
f ,d
∼
= Mζ -ss,S
d
∼
= {0}
and we may identify the (reduced) nilpotent locus with 0 ∈ A1, and the map πζ
f ,d
with the identity map. We have (d, d) = 0 , and so the perverse cohomology of
πζ
f ,dL−(d,d)
Mζ
f , d
∼
= QA1 is concentrated in degree 1, and so
GrP
(
H
(
Mζ ,S
f ,d , ˜ωζ ,!
d πζ
f ,d,∗φ mon
T r(W )ζ
f , d
L−(d,d)/2
))
is concentrated in degree 1. On the other hand ˜ωζ ,!
d QA1 ∼
= L{0} is concentrated in
perverse degree 2.
Furthermore, since ˜ωζ ,!
d is in general not exact, there is no obvious way to use the
decomposition theorem to deduce that ˜ωζ ,!
d πζ
f ,d,∗φ mon
T r(W )ζ
f , d
L−(d,d)/2 is isomorphic
to its total perverse cohomology, for the perverse truncati on functors associated to
Mζ ,S
d . In fact it is not hard to produce examples in which this state ment is false,
for instance by modifying the above example by setting MS ⊂ M(Q) to be the open
substack of Q-representations for which the loop of Q acts invertibly.
Remark 5.6. The distinction between diﬀerent perverse ﬁltrations exem pliﬁed by
Warning 5.5 is the reason for our being explicit about pickin g the ambient perverse
ﬁltration. Since this is the only type of ﬁltration we consid er, we will omit the word
ambient from now on.
The perverse ﬁltration is well-deﬁned in the limit f ≫ 0, as for ﬁxed d ∈ NQ0 ,
ﬁxed cohomological degree n, and for f ′ > f ≫ 0, in the commutative diagram
Hn
c
(
Mζ ,S
f ′,d,πζ
f ′,d,!Lγ (f ′,d)
Mζ
f ′ , d
)
/d15/d15
Hn
c
(
Mζ ,S
f ,d ,πζ
f ,d,!Lγ (f ,d)
Mζ
f , d
)
/d111/d111
/d15/d15
Hn
c
(
Mζ ,S
f ′,d,τ≥p
(
πζ
f ′,d,!Lγ (f ′,d)
Mζ
f ′ , d
))
Hn
c
(
Mζ ,S
f ,d ,τ≥p
(
πζ
f ,d,!Lγ (f ,d)
Mζ
f , d
))
/d111/d111
the horizontal maps are isomorphisms by the argument of Lemma 4.1 .
Since the constituent morphisms of H( ∗ζ ,S
W,µ ) lift to morphisms of monodromic
mixed Hodge modules on Mζ -ss
µ , it follows that H( ∗ζ ,S
W,µ ) respects the perverse
ﬁltration, and from the deﬁnitions we obtain the ﬁrst statement of the following
proposition, while the second is Proposition 4.4.
Proposition 5.7. There is a natural isomorphism of monoids in D≥,lf (MMHM(NQ0 ))
(87)
GrP
(
H(Aζ ,S
W,µ ), H(∗ζ ,S
W,µ ), H(Aζ
W,0)
)
∼
= H
(
dim∗ ˜ωζ ,!
µ
(
H(Aζ
W,µ ), H(˜∗ζ
W,µ ), ICζ -ss
M0 (Q)
))
.
Furthermore, forgetting the algebra structure, there is a n oncanonical isomorphism
of underlying monodromic mixed Hodge modules GrP(H(Aζ ,S
W,µ )) ∼
= H(Aζ ,S
W,µ ).
50 BEN DA VISON AND SVEN MEINHARDT
The isomorphism of algebras is what justiﬁes the notation of (86). T he following
technical lemma is what will enable us to use the localised coproduct on H(Aζ ,S
W,µ )
to induce a Hopf algebra structure on the associated graded algeb ra (87). It is only
a very slight variation of [14, Prop.1.4.4], but we include the proof for c ompleteness.
Lemma 5.8. Let V be a vector bundle on Md, and let eu(V ) ∈ H(Md, Q) be the
corresponding equivariant Euler class. Then
eu(V ) · Pp(Hc(MS,ζ -ss
d , ICζ
W,d)∨) ⊂ Pp+2 dim(V )(Hc(MS,ζ -ss
d , ICζ
W,d)∨).
Proof. Let pr : T (V ) → Mζ -ss
d be the projection from the total space of V restricted
to Mζ -ss
d , and let i : Mζ -ss
d → T (V ) be the inclusion of the zero section. Let Tf (V )
be the total space of the bundle V pulled back along the map Mζ
f ,d → Mζ -ss
d deﬁned
by forgetting the framing, and let pr f and if denote the corresponding projections
and inclusions. Let T r(W )V,f be the function induced by Tr( W ) on Tf (V ) and let
N = H c(Mζ ,S
f ,d ,φ mon
T r(W )ζ
f , d
QMζ
f , d
)∨. Then we have the equality of morphisms
(88)
· eu(V )|N = H
(
˜ωζ ,!
f ,d prf ,∗φ mon
T r(W )V, f
(
if ,∗QMζ
f , d
→ L− dim(V )
Tf (V ) → if ,∗L− dim(V )
Mζ
f , d
))
and the action of ·eu(V ) on H c(Mζ -ss,S
d , ICζ
W,d)∨ is given by letting f ≫ 0 in
(88) and twisting by L(d,d)/2. This morphism respects the perverse ﬁltration on
H(Mζ ,S
f ,d ,φ mon
T r(W )ζ
f , d
L(d,d)/2
Mζ
f , d
) (with the shift by 2 dim C(V )) since
πζ
f ,d,∗ prf ,∗φ mon
T r(W )V, f
(
if ,∗L(d,d)/2
Mζ
f , d
→ if ,∗L− dim(V )+(d,d)/2
Mζ
f , d
)
is a map of complexes of mixed Hodge modules on Mζ -ss
d . The result then follows
from the deﬁnition of the perverse ﬁltration on H c(Mζ -ss,S
d , ICζ
W,d)∨. □
We ﬁnish this section with the “absolute” version of Corollary 4.11.
Corollary 5.9. There is a canonical inclusion
(89) Υ ζ ,S,abs
W,µ : H(B C*)vir ⊗ BPSζ ,S
W,µ → H
(
Aζ ,S
W,µ
)
Proof. There is a natural inclusion L1/2 ⊗ BPSζ ,S
W,µ → H
(
pζ
µ ,∗ICζ
W,µ
)
since BPSζ ,S
W,µ
is precisely the ﬁrst piece of the perverse ﬁltration of the target. Via the H(B C*)-
action on H
(
Aζ ,S
W,µ
)
, this gives rise to a map Υ ζ ,S,abs
W,µ , which respects the perverse
ﬁltration by Lemma 5.8. After passing to the associated graded of t he perverse
ﬁltration, it is an injection, since it is obtained by restricting the (split ) injection
of Corollary 4.11 to the locus of points in S. Therefore Υ ζ ,S,abs
W,µ is an injection. □

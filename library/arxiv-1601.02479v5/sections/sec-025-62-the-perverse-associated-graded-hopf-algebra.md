---
doc_id: arxiv-1601.02479v5
doc_title: "Cohomological Donaldson-Thomas theory of a quiver with potential and quantum enveloping algebras"
section_id: sec-025-62-the-perverse-associated-graded-hopf-algebra
section_title: "The perverse associated graded Hopf algebra"
section_number: 6.2
pages: 53-56
source_pdf: 1601.02479v5.pdf
source_sha256: 52c2dcd4adf2e72b
doc_brief: "Cohomological Donaldson-Thomas theory of a quiver with potential and quantum enveloping algebras — This paper concerns the cohomological aspects of Donaldson – Thomas theory for Jacobi algebras and"
---
localised comultiplication in a little more detail, for further details see [1 0]. Consider
the proper map sd′,d′′ : Mζ -ss
d′,d′′ → Mζ -ss
d deﬁned as in (77). We form the map
(93)
γ : H c(Mζ -ss,S
d , ICζ
W,d)∨ → L(d′,d′′)/2 ⊗ Hc(Mζ -ss,S
d′,d′′ ,φ mon
Tr(W )ζ
d′ , d′′
IC Mζ -ss
d′, d′′
(Q))∨
54 BEN DA VISON AND SVEN MEINHARDT
given, via Verdier duality and Proposition 2.13(2), as the tensor pro duct with
L(d,d)/2 of the limit as N ↦→ ∞of the composition of maps
H
(
Dim∗ ω!
d,Nφ mon
Tr(W )ζ
d,N
QXζ -ss
d,N
)
→ H
(
Dim∗ ω!
d,Nφ mon
Tr(W )ζ
d,N
sd′,d′′,N,∗QXζ -ss
d′ , d′′,N
) ∼=− →
(94)
→ H
(
Dim∗ ω!
d,N sd′,d′′,N,∗φ mon
Tr(W )ζ
d′ , d′′,N
QXζ -ss
d′, d′′ ,N
)
∼=− → H
(
Dim∗ sd′,d′′,N,∗ω!
d′,d′′,Nφ mon
Tr(W )ζ
d′ , d′′,N
QXζ -ss
d′, d′′ ,N
)
.
Since the morphism Dim factors through a map to the base Mζ -ss
d , we deduce as
in Section 5.3 that γ preserves the perverse ﬁltration, i.e.
γ
(
Ps
(
Hc(Mζ -ss,S
d , ICζ
W,d)∨
))
⊂ Ps
(
L(d′,d′′)/2 ⊗ Hc
(
Mζ -ss,S
d′,d′′ ,φ mon
Tr(W )ζ
d′, d′′
IC Mζ -ss
d′ , d′′
(Q)
) ∨)
.
Composing with the isomorphism
Γ : L(d′,d′′)/2 ⊗ Hc
(
Mζ -ss,S
d′,d′′ ,φ mon
Tr(W )ζ
d′, d′′
IC Mζ -ss, S
d′ , d′′
(Q)
) ∨
→
L(d′,d′′)/2+(d′′,d′)/2 ⊗ Hc(Mζ -ss
d′ , ICζ
W,d′ )∨ ⊗ Hc(Mζ -ss,S
d′′ , ICζ
W,d′′ )∨
we likewise deduce
Γ ◦γ
(
Ps
(
Hc(Mζ -ss,S
d , ICζ
W,d)∨
))
⊂
Ps
(
L(d′,d′′)/2+(d′′,d′)/2 ⊗ H(Mζ -ss,S
d′ , ICζ
W,d′ ) ⊗ Hc(Mζ -ss,S
d′′ , ICζ
W,d′′ )∨
)
= Ps
(
L(d′,d′′) ⊗ Hc(Mζ -ss,S
d′ , ICζ
W,d′ )∨ ⊠tw
+ Hc(Mζ -ss,S
d′′ , ICζ
W,d′′ )∨
)
= Ps−2(d′,d′′)
(
Hc(Mζ -ss,S
d′ , ICζ
W,d′ )∨ ⊠tw
+ Hc(Mζ -ss,S
d′′ , ICζ
W,d′′ )∨
)
,(95)
since Γ is obtained by taking the hypercohomology of a morphism of complexe s
of monodromic mixed Hodge modules on Mζ -ss
µ . The ﬁnal equality (95) does not
preserve the cohomological degree, or the mixed Hodge structur e. We deﬁne
E1,d′,d′′ :=
∏
a∈Q1
∏
1≤l′≤d′
s(a)
∏
1≤l′′≤d′′
t(a)
(xs(a),l′ − yt(a),l′′ )
and
E0,d′,d′′ :=
∏
i∈Q0
∏
1≤l′≤d′
i
∏
1≤l′′≤d′′
i
(xi,l′ − yi,l′′ ).
Multiplication by E−1
1,d′,d′′ E0,d′,d′′ deﬁnes a map
β ∗ : H( Aζ ,S
W,d′) ⊠tw
+ H(Aζ ,S
W,d′′ ) →
(
H(Aζ ,S
W,d′) ⊠tw
+ H(Aζ ,S
W,d′′ )
)
[L−1
d′,d′′ ].(96)
The comultiplication is deﬁned [10, Cor.5.9] by
∆ ζ ,S
W,d′,d′′ : H( Aζ ,S
W,d) →
(
H(Aζ ,S
W,d′ ) ⊠tw
+ H(Aζ ,S
W,d′′ )
)
[L−1
d′,d′′ ]
∆ ζ ,S
W,d′,d′′ :=(·E−1
1,d′,d′′ E0,d′,d′′ ) ◦Γ ◦γ .
This comultiplication then respects cohomological degree, and lifts t o a morphism
in the category of cohomologically graded monodromic mixed Hodge st ructures.
For a dimension vector e, we deﬁne |e| =∑
i∈Q0 ei. So, for example, Ld′,d′′ is of
cohomological degree 2 |d′||d′′|. We extend the perverse ﬁltration to the right hand
COHAS AND QUANTUM ENVELOPING ALGEBRAS 55
side of (90) by setting
Ps
((
H(Aζ ,S
W,d′ ) ⊠tw
+ H(Aζ ,S
W,d′′ )
)
[L−1
d′,d′′ ]
)
:=(97)
∑
n≥0
Ps+2|d′′||d′|n
((
H(Aζ ,S
W,d′ ) ⊠tw
+ H(Aζ ,S
W,d′′ )
))
· L−n
d′,d′′ .
By [10, Prop.4.1], the localisation map
(
H(Aζ ,S
W,d′) ⊠tw
+ H(Aζ ,S
W,d′′ )
) fd′, d′′
− − − − →
(
H(Aζ ,S
W,d′ ) ⊠tw
+ H(Aζ ,S
W,d′′ )
)
[L−1
d′,d′′ ](98)
is an inclusion, since the operation ·Ld′,d′′ is injective on the domain. By deﬁnition
(97), fd′,d′′ preserves the perverse ﬁltration. By Lemma 5.8 multiplication by
E−1
1,d′,d′′ · E0,d′,d′′ induces a map
Ps
((
H(Aζ ,S
W,d′) ⊠tw
+ H(Aζ ,S
W,d′′)
)
[L−1
d′,d′′ ]
)
→
Ps+2(d′,d′′)
((
H(Aζ ,S
W,d′ ) ⊠tw
+ H(Aζ ,S
W,d′′ )
)
[L−1
d′,d′′]
)
.(99)
Combining the shifts in perverse degree in (99) and (95), we deduce that
∆ ζ
W,d′,d′′
(
Ps
(
H
(
Aζ ,S
W,d
)))
⊂ Ps
((
H(Aζ ,S
W,d′ ) ⊠tw
+ H(Aζ ,S
W,d′′ )
)
[L−1
d′,d′′ ]
)
.
The proof of the following is essentially the original proof of the Atiya h–Bott lemma
of [2], adapted to deal with vanishing cycles and passage to the asso ciated graded
of the perverse ﬁltration.
Lemma 6.3. The map GrP(fd′,d′′) induced by the map (98) is injective.
Proof. We abbreviate Pi = Pi
(
H(Mζ -ss,S
d′ , ICζ
W,d′) ⊠tw
+ H(Mζ -ss,S
d′′ , ICζ
W,d′′ )
)
. It
is suﬃcient to show that the degree 2 |d′||d′′| map Gr P(·Ld′,d′′ ) is injective. For
then if
fd′,d′′ (a) ∈

∑
r≥0
Pi+2|d′||d′′|r
(
H(Mζ -ss,S
d′ , ICζ
W,d′ ) ⊠tw
+ H(Mζ -ss,S
d′′ , ICζ
W,d′′ )
)
· L−r
d′,d′′


we can write a = ∑
r≤n br · L−r
d′,d′′ for br ∈ Pi+2|d′||d′′|r. Then a · Ln
d′,d′′ ∈
Pi+2|d′||d′′|n by Lemma 5.8, and so a ∈ Pi, by injectivity of Gr P(·Ld′,d′′ ).
Consider the subgroup Gm ∼
= T ⊂ Gd′ × Gd′′ given by the embedding
z ↦→
(
(zd′′
i idCd′
i )i∈Q0 , (z− d′
i idCd′′
i )i∈Q0
)
and let Pd′,d′′ := (Gd′ × Gd′′ )/T . Note that T acts trivially on Xζ -ss
d′ × Xζ -ss
d′′ and
furthermore T acts trivially on the linearization (39), so that the linearization of
the Gd′ × Gd′′ -action lifts to a linearization of the Pd′,d′′ action. Let
p′
d′,d′′ : ( Xζ -ss
d′ × Xζ -ss
d′′ )/Pd′,d′′ → Mζ -ss
d′ × Mζ -ss
d′′
be the map to the GIT quotient. Via the Cartesian square
Mζ -ss
d′ × Mζ -ss
d′′ /d47/d47
/d15/d15
pt /(Gd′ × Gd′′ )
/d15/d15
(Xζ -ss
d′ × Xζ -ss
d′′ )/Pd′,d′′ /d47/d47 pt /Pd′,d′′
56 BEN DA VISON AND SVEN MEINHARDT
we obtain the isomorphism
H
(
pζ
d′,∗ICζ
W,d′ ⊠ pζ
d′′,∗ICζ
W,d′′
)
∼
=
H
(
p′
d′,d′′,∗φ mon
f IC Xζ -ss
d′ ×Xζ -ss
d′′ /Pd′ , d′′ (Q)
)
⊗HPd′, d′′ (pt) HGd′ ×Gd′′ (pt) ⊗ L1/2.
where f is the function induced by Tr( W )d′ ⊞ Tr(W )d′′ on ( Xζ -ss
d′ × Xζ -ss
d′′ )/Pd′,d′′ .
After picking a splitting
λ : H Gd′ ×Gd′′ (pt) ∼
= HPd′, d′′ (pt) ⊗ HT (pt)
we obtain an isomorphism
H
(
pζ
d′,∗ICζ
W,d′ ⊠ pζ
d′′,∗ICζ
W,d′′
)
∼
= H
(
p′
d′,d′′,∗φ mon
f IC Xζ -ss
d′ ×Xζ -ss
d′′ /Pd′ , d′′ (Q)
)
⊗ H(IC pt /T (Q)).
We deﬁne the ﬁltration
Di = H
(
Mζ -ss,S
d′ × Mζ -ss,S
d′′ , ˜ω! H≥i
(
p′
d′,d′′,∗φ mon
f IC Xζ -ss
d′ ×Xζ -ss
d′′ /Pd′ , d′′ (Q)
)
⊗ H(IC pt /T (Q)
)
⊂ H
(
Mζ -ss,S
d′ × Mζ -ss,S
d′′ , ˜ω! H
(
pζ
d′,∗ICζ
W,d′ ⊠ pζ
d′′,∗ICζ
W,d′′
))
= Gr P
(
H(Aζ ,S
W,d′) ⊠tw
+ H(Aζ ,S
W,d′′ )
)
=: B
where we have made the abbreviation
˜ω = ˜ωζ
d′ × ˜ωζ
d′′ : Mζ -ss,S
d′ × Mζ -ss,S
d′′֒Mζ -ss
d′ × Mζ -ss
d′′ .
Consider the associated graded object Gr D B. Multiplication by Ld′,d′′ preserves
D degree, and so induces a map
GrD(GrP(·Ld′,d′′ )) : Gr D B → GrD B.
Speciﬁcally, the map is given by multiplication by the T -equivariant Euler charac-
teristic of Xd′,d′′ → Xd′ × Xd′′ , which is nonzero since the vector bundle has no
sub-bundle with trivial T -weight. It follows that Gr D(GrP(·Ld′,d′′ )) is injective, so
that Gr P(·Ld′,d′′ ) is injective too.
□
We deduce the following proposition.
Proposition 6.4. The triple
(
GrP(H(Aζ ,S
W,µ )), GrP(H(˜∗ζ ,S
W,µ )), GrP(∆ ζ ,S
W,µ )
)
deﬁnes
a localised bialgebra in the categoryτ D≥,lf (MMHM(Λζ
µ )) in the sense of [10, Def.5.3].

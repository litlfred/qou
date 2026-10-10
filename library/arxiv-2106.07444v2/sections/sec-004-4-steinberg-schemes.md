---
doc_id: arxiv-2106.07444v2
doc_title: "FROM THE HECKE CATEGORY TO THE UNIPOTENT LOCUS"
section_id: sec-004-4-steinberg-schemes
section_title: "Steinberg Schemes"
section_number: 4
pages: 32-38
source_pdf: 2106.07444v2.pdf
source_sha256: 5acca39c07bcdddd
doc_brief: "FROM THE HECKE CATEGORY TO THE UNIPOTENT LOCUS — Let W be the W eyl group of a split semisimple group G. Its Hecke category HW can be built from pure perverse sheaves on the double ﬂag variety of G."
---
4.1. In Section 2, we reviewed the (mixed) Springer sheaf S ∈ Db
G,m(U0) and
the (mixed) Grothendieck–Springer sheaf G ∈ Db
G,m(G0). In Section 3, we gave a
construction of a graded algebra AK from a mixed complex K: explicitly,
AK =
⨁
n
grw
0 Hom0(K,K ⟨n⟩ )
≃
⨁
n
grw
n Endn(K).
In this section, we use topological methods to prove Theorem 1: The map
i∗ : AG → AS
induced by i : U0 → G 0 via Lemma 1.6.1 is an isomorphism of graded ¯Qℓ-algebras.
Remark 4.1.1. By Lemma 2.10.2, Endn(S) is concentrated in weight n (see also
[R, Lem. 5.4].) However, if n >0, then End n(G) is not concentrated in weight n,
essentially because the cohomology of the Grothendieck–Sp ringer resolution of G
contains the cohomology of a torus. See Example 6.2.2.
Remark 4.1.2. Our proof of Theorem 1 is inspired by an unpublished note of Riche
about the analogous statement at the level of Lie algebras, w hich is well-known.
Riche states that his note was inspired by [ CG, §3.4].
4.2. If X0 is a G0-variety over F, with structure map a :X0 → pt0, then its mixed
equivariant dualizing complex is
ω =ωX0/G0 :=a! ¯Qℓ ∈ Db
G,m(X0).
Its equivariant Borel–Moore homology (with coeﬃcients in ¯Qℓ) is
H!,G
−∗ (X) := Hom ∗( ¯Qℓ,ω ),
viewed as a graded ¯Qℓ[F ]-module. Borel–Moore homology is functorial in the fol-
lowing senses:
(1) If f :Y →X is proper, then it induces a pushforward
f∗ : H !,G
−∗(Y ) → H!,G
−∗(X)
via the composition f∗ωY/G
∼
− →f!f !ωX/G →ωX/G.
(2) If f :Y →X is smooth of relative dimension d, then it induces a pullback
f ∗ : H !,G
−∗ (X) → H!,G
−∗(Y )⟨− 2d⟩
via the composition ωX/G →f∗f ∗ωX/G
∼
− →f∗ωY/G ⟨− 2d⟩ . If f is an aﬃne-
space bundle, then f ∗ is a shifted isomorphism.
(3) If i : Z → X is a closed immersion with complement j : U → X, then it
induces a long exact sequence
· · · → H!,G
i (Z) → H!,G
i (X) → H!,G
i (U ) → H!,G
i−1(Z) → · · ·(13)
via the exact triangle i!i! → id →j∗j∗ →i!i![1].
FROM THE HECKE CATEGORY TO THE UNIPOTENT LOCUS 33
(4) If we have a cartesian square
Y Y ′
X X ′
fY
g g′
f
in which [ X/G], [X ′/G] are smooth of respective dimensions d,d ′, then f
induces a pullback with restricted support
f ∗
Y : H !,G
−∗ (Y ′) → H!,G
−∗ (Y )⟨ 2(d′ −d)⟩
via the composition
ωY ′/G⟨− 2d′⟩
∼
− →g′! ¯Qℓ →fY,∗g!f ∗ ¯Qℓ
∼
− →fY,∗ωY/G ⟨− 2d⟩.
Here, we use proper base change [ LO08, §5] to identify g′!f∗ ≃fY,∗g!.
4.3. We can express Hom -spaces between pushforward sheaves, like AS and AG,
in terms of the Borel–Moore homology of associated schemes.
Lemma 4.3.1. If we have a cartesian square of G-varieties
˜Y ˜X
Y X
˜f
pY p
f
in which [ ˜X/G] is smooth of dimension ˜d, then
Hom∗(f! ¯Qℓ,p ∗ ¯Qℓ) ≃ H!,G
−∗ ( ˜Y )⟨− 2 ˜d⟩.
In particular, if p is proper and K =p∗ ¯Qℓ, then
An
K ≃ grw
n−2 ˜d H!,G
−(n−2 ˜d)( ˜X ×X ˜X)
for all n, and H!,G
−∗( ˜Y ) forms a left graded AK-module.
Proof. By proper base change,
f !p∗ ¯Qℓ ≃pY,∗ ˜f ! ¯Qℓ ≃pY,∗ ˜f !ω ˜X/G ⟨− 2 ˜d⟩ ≃ pY,∗ω ˜Y/G ⟨− 2 ˜d⟩,
giving Hom (f! ¯Qℓ,p ∗ ¯Qℓ) ≃f∗Hom( ¯Qℓ,f !p∗ ¯Qℓ) ≃f∗pY,∗Hom( ¯Qℓ,ω ˜Y/G)⟨− 2 ˜d⟩ . □
4.4. In the notation of Section 2, let
Z0 = ˜U0 ×U0
˜U0,
Z ′
0 = ˜G0 ×G0
˜G0.
In the literature, the underlying reduced scheme of Z is called the Steinberg
variety, since it was introduced in [ St76]. Lemma 4.3.1 implies that
An
S ≃ grw
n+2r H!,G
−(n+2r)(Z)
(
≃ H!,G
−(n+2r)(Z)
)
,(14)
An
G ≃ grw
n H!,G
−n(Z ′).(15)
34 MINH-TÂM QUANG TRINH
It remains to compare the Borel–Moore homologies of Z and Z ′.
Let us outline the strategy. We will lift the Bruhat strata of B × B to strata
Zw ⊆ Z and Z ′
w ⊆ Z ′. To compare the Borel–Moore homologies of Zw and Z ′
w,
we will further replace these strata with aﬃne-space bundle s Yw and Y ′
w such that
there is an explicit map Yw ×T → Y ′
w, where T is a maximal torus of G. Finally,
we will use the long exact sequence ( 13) to patch the stratum-wise comparisons
together.
4.5. Let ˜i : ˜U0 → ˜G0 be the lift of the inclusion i : U0 →G0. Let ˜p1, ˜p2 : Z0 → ˜U0
be the two projection maps, and let ˜ p′
1, ˜p′
2 : Z ′
0 → ˜G0 be deﬁned similarly. Below,
we will continually refer to the commutative diagram:
(16)
Z0 Z ′
0
˜U0 ˜G0
U0 G0
iZ
˜pj ˜p′
j
˜i
p p′
i
Note that both squares in the diagram are cartesian.
Lemma 4.5.1. We have a commutative diagram
An
G An
S
grw
n H!,G
−n(Z ′) H !,G
−(n+2r)(Z)
i∗
∼
∼
i∗
Z
wherei∗ is deﬁned by (10), the vertical isomorphisms are (14) and (15), and i∗
Z is
the pullback with restricted support induced by ˜i via the top square of (16).
Proof. The morphism i∗
Z is induced by the morphism
(˜p′)!
1 → (˜p′)!
1˜i∗˜i∗ ∼
− →iZ,∗ ˜p!
1˜i∗,
while the morphism i∗ is induced by the composition
˜p′
2,∗(˜p′)!
1
∼
− →p′!p′
∗
→p′!i∗i∗p′
∗
∼
− →˜i∗p!p!˜i∗
∼
− →˜i∗ ˜p2,! ˜p!
1i∗
∼
− →˜p′
2,∗iZ,∗ ˜p!
1i∗.
By further diagram-chasing, the latter is obtained by apply ing ˜p′
2,∗ to the former.
□
To analyzei∗
Z, we decompose Z0 and Z ′
0 into strata. For each w ∈W , we deﬁne
subschemes Zw,0 ⊆ Z 0 and Z ′
w,0 ⊆ Z ′
0 by stipulating that both squares in the
FROM THE HECKE CATEGORY TO THE UNIPOTENT LOCUS 35
commutative diagram below are cartesian:
(17)
Zw,0 Z ′
w,0 Ow,0
Z0 Z ′
0 B0 × B0
iZ,w
iZ
jw
Here, the map Z ′
0 → B 0 × B0 is induced by the map Z ′
0
˜p′
1× ˜p′
2
− − − − →˜G0 × ˜G0.
To analyze iZ,w : Zw,0 → Z ′
w,0, we rewrite these strata in a way that expresses
their structure as ﬁber bundles over Ow,0. Choose a split maximal torus T0 ⊆G0.
Choose a Borel B0 ⊇ T0 with unipotent radical U0 ⊆ B0, so that B0 ≃ T0 ⋉U0.
Let N0 be the normalizer of T0 in G0. For each w ∈ W , ﬁx a lift ˙ w ∈ N0. Then
˙wB0 ˙w−1 contains ˙wT0 ˙w−1 =T0 and only depends on w. If we write
Bw,0 =B0 ∩ ˙wB0 ˙w−1,
Uw,0 =U0 ∩ ˙wU0 ˙w−1,
thenBw,0 ≃T0 ⋉Uw,0. In what follows, let Bw,0 act on G0 by right multiplication
and on Uw,0 and itself by right conjugation.
Lemma 4.5.2. We have a commutative diagram
(G0 ×Uw,0)/Bw,0 (G0 ×Bw,0)/Bw,0 G0/Bw,0
Zw,0 Z ′
w,0 Ow,0
∼
∼
∼
iZ,w
where the middle vertical map sends [g,b ] ↦→[gbg −1,gBg −1,g ˙wB ˙w−1g−1].
Remark 4.5.3. The vertical isomorphisms respectively transport the G-actions on
Zw, Z ′
w,Ow to the G-actions on (G ×Uw)/Bw, (G ×Bw)/Bw,G/Bw given by left
multiplication on the factor of G.
Proof. Thew = 1 case, entailing isomorphisms (G×U )/B ≃ ˜U and (G×B)/B ≃ ˜G,
is explained in [ Sl, Ch. 4], and the general case is similar. □
Again, let T0 act on G0 by right multiplication and on Uw,0 and Bw,0 by right
conjugation. Let Yw,0 and Y ′
w,0 be deﬁned by the cartesian squares:
Yw,0 (G0 ×Uw,0)/T0
Zw,0 (G0 ×Uw,0)/Bw,0
∼
∼
Y ′
w,0 (G0 ×Bw,0)/T0
Z ′
w,0 (G0 ×Bw,0)/Bw,0
∼
∼
Let iY,w : Yw,0 → Y ′
w,0 be the pullback of iZ,w : Zw,0 → Z ′
w,0. The advantage of
iY,w overiZ,w is that the former can be factored as
Yw,0
∼
− → Yw,0 × {1} → Yw,0 ×T0
∼
− → Y′
w,0.
If we let G0 act trivially on T0, then these maps are all G0-equivariant.
36 MINH-TÂM QUANG TRINH
4.6. In what follows, if M =⨁
nMn is a Z-graded ¯Qℓ[F ]-module, then we write
M † ≃
⨁
n
grw
n Mn.
Let i∗
Z,w : H !,G
−∗(Z ′
w) → H!,G
−∗ (Zw)⟨ 2r⟩ be the pullback with restricted support in-
duced by ˜i via the top square of ( 16) and the left square of ( 17), and let
i†
Z,w : H !,G
−∗ (Z ′
w)† → H!,G
−∗ (Zw)⟨ 2r⟩
be its restriction to H !,G
−∗(Z ′
w)†. Let i†
Y,w,i†
Y,w be deﬁned similarly.
Lemma 4.6.1. The map i†
Y,w is an isomorphism.
Proof. WritingNw = dimUw, we have
H!,G
−∗(Yw) ≃ H!,G
−∗(G/T )⟨ 2Nw⟩ ≃ H!,T
−∗(pt)⟨ 2Nw⟩.
By Poincaré duality, H !,T
−i (pt) ≃ H−i
!,T (pt) ≃ Hi−2r
T (pt), where H ∗
!,T denotes T -
equivariant, compactly-supported cohomology. So Frobeni us acts on H !,T
−i (pt) by
q
i
2 −r, which means it is concentrated in weight i − 2r.
Again by Poincaré duality, H !
−j(T ) ≃ H−j
! (T )∨ ≃ Hj+2r(T ), where H !
∗, resp. H∗
! ,
denotes non-equivariant Borel–Moore homology, resp. compactly-supported coho-
mology. So Frobenius acts on H !
−j(T ) by qj+2r, which means it is concentrated in
weight 2j + 4r.
Altogether, the Künneth isomorphism
H!,G
−n(Y ′
w)
∼
− →
⨁
i+j=n
H!,G
−i (Yw) ⊗ H!
−j(T )
restricts to an isomorphism
H!,G
−n(Y ′
w)† ∼
− →H!,G
−(n+2r)(Yw) ⊗H !
2r(T ).
But i∗
Y,w is the composition of the Künneth isomorphism with
H!,G
−∗(Yw) ⊗ H!
−∗(T ) → H!,G
−∗(Yw) ⊗ H!
2r(T )
∼
− →H!,G
−∗ (Yw) ⊗ H!
0(pt)⟨ 2r⟩
∼
− →H!,G
−∗ (Yw)⟨ 2r⟩,
so we win. □
Lemma 4.6.2. The map i†
Z,w is an isomorphism.
Proof. The maps Yw,0 → Zw,0 and Y ′
w,0 → Z ′
w,0 deﬁne aﬃne-space bundles of rank
Nw, so they induce pullback isomorphisms
H!,G
−∗ (Zw)
∼
− →H!,G
−∗ (Yw)⟨− 2Nw⟩,
H!,G
−∗ (Z ′
w)
∼
− →H!,G
−∗ (Y ′
w)⟨− 2Nw⟩
that preserve weights. Now we are done by the previous lemma. □
FROM THE HECKE CATEGORY TO THE UNIPOTENT LOCUS 37
Proof of Theorem 1. Fix a total order ≼ onW in whichw1 ≼ w2 implies |w1| ≤ |w2|,
where |−| denotes Bruhat length. Such a total order is necessarily a re ﬁnement of
the Bruhat partial order. For any w ∈W , let
Z≼ w,0 =
∐
x≼ w
Zx,0 ⊆ Z 0,
Z≺w,0 =
∐
x≺w
Zx,0 ⊆ Z 0.
Then Zw,0 → Z ≼ w,0 is a closed immersion with complement Z≺w,0 → Z ≼ w,0. Let
Z ′
≼ w,0, Z ′
≺w,0 be deﬁned similarly. The map iZ : Z0 → Z ′
0 gives rise to the follow-
ing commutative diagram whose rows are long exact sequences and whose vertical
arrows are pullbacks with restricted support:
· · · H!,G
n (Z ′
w) H !,G
n (Z ′
≼ w) H !,G
n (Z ′
≺w) · · ·
· · · H!,G
n (Zw)⟨ 2r⟩ H!,G
n (Z≼ w)⟨ 2r⟩ H!,G
n (Z≺w)⟨ 2r⟩ · · ·
i∗
Z,w i∗
Z,≼ w i∗
Z,≺w
Since ( −)† is exact, we obtain another commutative diagram
· · · H!,G
n (Z ′
w)† H!,G
n (Z ′
≼ w)† H!,G
n (Z ′
≺w)† · · ·
· · · H!,G
n (Zw)⟨ 2r⟩ H!,G
n (Z≼ w)⟨ 2r⟩ H!,G
n (Z≺w)⟨ 2r⟩ · · ·
i†
Z,w i†
Z,≼ w i†
Z,≺w
in which the top row remains exact.
We induct along ≼ . If w = 1, then i†
Z,≺w = i†
Z,w. By Lemma 4.6.2, the latter
is an isomorphism in every homological degree n. Now let w be arbitrary. If x
is the immediate predecessor of w in the total order ≼ , then Z≺w = Z≼ x and
i†
Z,≺w =i†
Z,≼ x. Lemma 4.6.2 and the inductive hypothesis respectively imply that
i†
Z,w and i†
Z,≺w are isomorphisms in every degree. So, by the ﬁve lemma, i†
Z,≼ w is
an isomorphism in every degree as well, completing the induc tion. □
38 MINH-TÂM QUANG TRINH

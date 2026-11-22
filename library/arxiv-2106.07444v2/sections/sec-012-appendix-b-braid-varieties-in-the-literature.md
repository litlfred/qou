---
doc_id: arxiv-2106.07444v2
doc_title: "FROM THE HECKE CATEGORY TO THE UNIPOTENT LOCUS"
section_id: sec-012-appendix-b-braid-varieties-in-the-literature
section_title: "Appendix B. Braid Varieties in the Literature"
section_number: null
pages: 78-82
source_pdf: 2106.07444v2.pdf
source_sha256: 5acca39c07bcdddd
toc_source: outline
doc_brief: "FROM THE HECKE CATEGORY TO THE UNIPOTENT LOCUS — Let W be the Weyl group of a split semisimple group G. Its Hecke category HW can be built from pure perverse sheaves on the double ﬂag variety of G."
---
B.1.
In this appendix, we explain how the varieties U(β), Z(β), X(β) are related
to other varieties that have appeared in the literature. Throughout, we assume
the notation and hypotheses of Sections 1-2. All varieties in this section can be
constructed over F, not just ¯F, but we will omit the subscript 0’s anyway to lighten
notation.
B.2.
Let w ∈W. As in Section 2, let Ow ⊆B × B be the G-orbit indexed by w,
and let act : G × B →B × B be the map
act(g, B) = (g−1Bg, B).
In the following diagram, all squares are cartesian:
Ow
Gw
Uw
Zw
B × B
G × B
U × B
˜U × B
act
To the best of my knowledge:
(1) For ﬁxed g ∈G and w a Coxeter element of minimal length, the ﬁber
(Gw)g ⊆Gw ﬁrst appears [St65, §4]. For general w, it ﬁrst appears in Lem.
3.6 of Kawanaka’s paper [Kaw], where it is denoted Fg,w, and independently
in Lusztig’s note [L80], where it is denoted Ys,w in the case where g is a
regular semisimple element s. More recently, it has appeared in Lusztig’s
paper [L11], where it is denoted Bw
g , and in D. Kim’s papers [K18-1, K18-2],
where it is denoted Yw,g.
(2) The variety Gw ﬁrst appears in Lusztig’s paper [L85-I], where it is denoted
Yw. It is used throughout his series of works on character sheaves. It also
appears in [L11] and its sequels, where it is denoted Bw.
(3) The varieties Ured
w
and Zred
w
ﬁrst appear in Lusztig’s note [L21], where they
are respectively denoted B(1)
w
and ˜B1
w.
More generally: Let T be the universal maximal torus of G, so that
there are maps G →T 
 W and ˜G →T .
For any δ ∈T with image
(δ) ∈T 
 W, Lusztig deﬁnes varieties B(δ)
w
⊆Gw and ˜Bδ
w ⊆˜G ×G Gw as
the corresponding ﬁbers.
B.3.
Let β ∈Br+
W be a positive braid of writhe ℓ. Thus we have β = σs1 · · · σsℓ
for some s1, . . . , sℓ∈S. By deﬁnition,
O(β) = {(B0, B1, . . . , Bℓ) : (Bi−1, Bi) ∈Osi for 1 ≤i ≤ℓ}.
In the following diagram, all squares are cartesian:
O(β)
G(β)
U(β)
Z(β)
B × B
G × B
U × B
˜U × B
pr0 × prℓ
act
FROM THE HECKE CATEGORY TO THE UNIPOTENT LOCUS
79
In addition, we will abbreviate
X(β) := G(β)1 = U(β)1.
To the best of my knowledge:
(1) For general β, the variety O(β) ﬁrst appears in Broué–Michel’s paper
[BM97], where it is denoted B(β). See also [D97, Application 2]. However,
it is arguably implicit in the works of Bott–Samelson [BS] and Hansen [H].
In §6 of the paper [STZ] by Shende–Treumann–Zaslow, O(β) is called the
open Bott–Samelson variety of β and denoted M1(β).
(2) The variety G(β) ﬁrst appears in [L85-I, §2.5], where it is denoted Yw in the
case where w is an expression for β (see §A.2). Later, it implicitly appears
in [STZ, §6] along with X(β): In the notation of loc. cit.,
M(β◦) = [G(β)/G],
M(β≻) = [X(βπ)/G].
(The authors assume G = PGLn, but this hypothesis is extraneous.) From
the viewpoint of cluster geometry, the stack M(β≻) has been studied by L.
Shen and D. Weng in [SW]: It is the special case of their stack Confb
d(B)
where b = β and d = 1.
(3) For ﬁxed B ∈B, the variety X(β)red
B
⊆X(β)red ﬁrst appears in §5.3 of
Mellit’s paper [Me] in an isomorphic form denoted X0(β), in the case where
G = GLn.
In the next subsection, we generalize Mellit’s deﬁnition to
arbitrary reductive G and explain the isomorphism in detail.
More recently, X0(β) has been studied by Casals, Gorsky, Gorsky, and
Simental in the paper [CGGS]: It is the special case of their variety X0(γ; π)
where γ = β and π = 1. (Note that in their notation, π is an element of
Sn, not the full twist.)
(4) The schemes U(β) and Z(β) are constructed similarly to the representation
varieties X 1
sing and X 1
sm in [Me, §8]. However, they are not a special case of
those varieties, or vice versa.
B.4.
Below, we relate the scheme X(β) to the variety X0(β) in [Me], hence to the
varieties in [CGGS].
Fix a maximal torus T ⊆G and a Borel B ⊇T . For each s ∈S, we have a
corresponding positive root subgroup
uαs : A1 →Uαs ⊆B.
Recall that NG(T )/T ≃W. Fix a section W →NG(T ), to be denoted w 7→wT .
For all s ∈S, let fαs : A1 →G be the map
fαs(z) = sT · uαs(z).
Let fβ,B : Aℓ→G be the map
fβ,B(⃗z) = fαs1(z1) · · · fαsℓ(zℓ).
80
MINH-TÂM QUANG TRINH
With these notations, let
X0(β, B) = f −1
β,B(B) ⊆Aℓ.
For G = GLn and B ﬁxed, the underlying reduced scheme of X0(β, B) is the variety
denoted X0(β) in [Me, §5.3].
Example B.4.1. Let G = GL2 and B the upper-triangular subgroup. In this case,
fαs(z) =
 
1
1
z
!
.
Let σ be the positive generator of BrW = Br 2, and let G be the punctured aﬃne
line. Then we can check that:
X0(σ) = ∅,
X0(σ2) = {⃗z ∈A2 : z1 = 0}
= pt × A1,
X0(σ3) = {⃗z ∈A3 : 1 + z1z2 = 0}
= G × pt × A1,
X0(σ4) = {⃗z ∈A4 : z1 + z3 + z1z2z3 = 0}
= (A1 × pt × A1) ⊔(G × A1 × G).
The argument in [Me, §5.4] shows that for general G and β, it is always possible to
stratify X0(β) into cells of the form Aa × Gb with a, b ≥0.
It would be desirable to organize the varieties X0(β, B) into an algebraic family
over the ﬂag variety B. I do not know how to do this directly, given the dependence
of fβ,B on the section w 7→wT . Nonetheless:
Proposition B.4.2. For all β ∈Br+
W , there is a commutative diagram
G(β)
B × Aℓ
X0(β, B)
G × B
G
{1}
(fβ,B(⃗z),⃗z)
fβ,B
id ×{B}
where the middle vertical map sends (b,⃗z) 7→b−1fβ,B(⃗z) and both squares are carte-
sian. In particular, X0(β, B) is isomorphic to the ﬁber G(β)1,B = X(β)B.
Proof. It is enough to construct the map B × Aℓ→G(β). To this end, let Bℓ−1
act on Bs1,T B × · · · × Bsℓ,T B on the right by:
(x1, x2, . . . , xi, . . . , xℓ) · (b1, . . . , bℓ−1)
= (x1b1, b−1
1 x2b2, . . . , b−1
i−1xibi, . . . , b−1
ℓ−1xℓ).
We denote the quotient by
M(β, B) = (Bs1,T B × · · · × Bsℓ,T B)/Bℓ−1.
FROM THE HECKE CATEGORY TO THE UNIPOTENT LOCUS
81
(When β = σw, this variety is a dense open stratum in the variety denoted Mw in
[H].) We have an isomorphism:
B × Aℓ
∼
−→
M(β, B)
(b,⃗z)
7→
[bfαs1(z1), fαs2 (z2), . . . , fαsℓ(zℓ)]
Let B act on M(β, B) by outer right conjugation and on G by right multiplication.
Writing xg = g−1xg and Bg = g−1Bg , we have a further isomorphism:
(M(β, B) × G)/B
∼
−→
G(β)
[x1, . . . , xℓ, g]
7→
((x1 · · · xℓ)g, Bx2···xℓg, . . . , Bg)
(33)
We now have a composition
M(β, B)
∼
−→(M(β, B) × B)/B →(M(β, B) × G)/B
∼
−→G(β).
It forms the top arrow of a cartesian diagram
G(β)
M(β, B)
G × B
G
mβ,B
id ×{B}
in which mβ,B([x1, . . . , xℓ]) = x1 · · · xℓ. This is the left-hand square of the diagram
in the proposition, once we identify M(β, B) with B × Aℓ.
□
Remark B.4.3. The isomorphism (33) can be pulled back to an isomorphism
(X0(β, B) × G)/B
∼
−→X(β).
Thus, we have an isomorphism of stacks:
[X0(β, B)/B] ≃[X(β)/G].
Note that [X0(β, B)/B] is homotopy equivalent to [X0(β, B)/T ]. The T -action on
X0(β, B) is important in [Me] and [CGGS].
82
MINH-TÂM QUANG TRINH

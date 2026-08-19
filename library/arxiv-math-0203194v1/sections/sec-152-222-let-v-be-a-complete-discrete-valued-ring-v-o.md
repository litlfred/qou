---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and diﬀerential equations. From C to Cp Tˆohoku-Hokkaidˆo lectures in Arithmetic Geometry Yves Andr´ e (with appendices by F. Kato and N. Tsuzuki)"
section_id: sec-152-222-let-v-be-a-complete-discrete-valued-ring-v-o
section_title: "Let v be a complete discrete valued ring v of mixed characteristic"
section_number: 2.2.2
pages: 77-78
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
doc_brief: "Period mappings and differential equations. From C to Cp Tôhoku-Hokkaidô lectures in Arithmetic Geometry Yves André (with appendices by F. Kato and N. Tsuzuki) — 580 sections: INTRODUCTION; INTRODUCTI"
---
(0,p ). Let Nil v denote the category of locally noetherian v-schemes S on
which p is locally nilpotent. For any S in Nil v, the ideal of deﬁnition J =
JSred of the closed subscheme Sred (of characteristic p) is locally nilpotent.
Theorem 2.2.3 (Rigidity theorem for p-divisible groups up to isogeny) . Every
homomorphism ρ : Λ ×SSred→ Λ′×SSred ofp-divisible groups up to isogeny
admits a unique lifting ρ : Λ → Λ′. Moreover, ρ is a quasi-isogeny if ρ is.
Proof. (following an argument of V. Drinfeld). We may assume that S is
aﬃne, and that J is nilpotent. Then the connected part ˆΛ′ is a formal Lie
group, hence there is a power pn of p such that for any aﬃne S-schemeS′,
ˆΛ′(S′) is killed by [ pn] (in fact if J r+1 = 0 on S, one can take n =r2).
We observe that Ker(Λ ′(S′)→ Λ′(S′
red)) = ˆΛ′(S′). We have
Ker(Hom(Λ( S′), Λ′(S′))→ Hom(Λ( S′
red), Λ′(S′
red))
= Hom(Λ(S′), Ker(Λ′(S′)→ Λ′(S′
red)))
which is zero because Ker(Λ ′(S′) → Λ′(S′
red) is killed by [ pn] while Λ is
p-divisible.
This implies the injectivity of qisog S(Λ , Λ′)→ qisogSred(Λ×SSred, Λ′×SSred)
(taking into account the fact that Hom(Λ( S′
red), Λ′(S′
red)) is torsion-free).
For the surjectivity, let us ﬁrst show that for any f∈ Hom(Λ( S′
red), Λ′(S′
red)),
there is a lifting g∈ Hom(Λ( S′), Λ′(S′)) of pnf . For any x∈ Λ( S′), let x
denote its image in Λ( S′
red). Since Λ ′ is formally smooth, f (x) admits a
lifting y∈ Λ′(S′). Since Ker(Λ ′(S′)→ Λ′(S′
red))) is killed by pn, g(x) :=
[pn]y is well-deﬁned. This construction provides the desired lif ting g.
It remains to show that g is an isogeny if f is. Let f
′
be a quasi-inverse of
f (f
′
f = [pm]), and g′ be a lifting of pnf
′
. Then g′g = [p2n+m] by unicity of
liftings. Thus g is an epimorphism, and the subscheme Ker g of Ker[p2n+m]
is ﬁnite over S. On the other hand, Λ is ﬂat over S and the ﬁbers of g′
are ﬂat (being isogenies). The criterium of ﬂatness ﬁber by ﬁ ber [ EGA IV ,
11.3.10] implies that g′ is ﬂat, and we conclude that it is an isogeny.
74 II. INTRODUCTION TO THE THEORY OF p-ADIC PERIOD MAPPINGS.
Let us observe that there is variant of both the statement and the proof
of 2.2.3 for abelian schemes, instead of p-divisible groups.
The next theorem asserts that deforming an abelian scheme of char-
acteristic p is equivalent to deforming its p-divisible group. For any S in
Nilv, let Def p-div(S) be the category of triples ( A, Λ ,ǫ ) consisting of an
abelian scheme over Sred, a p-divisible group Λ over S and an isomorphism
ǫ :A[p∞]∼
= Λ ×SSred.
Theorem 2.2.4 (The Serre-Tate theorem) . The functor
A ↦→(Ared, Λ = A[p∞], ǫ:Ared[p∞]∼
= Λ ×SSred)
induces an equivalence of categories between the category o f abelian schemes
over S and the category Def p-div(S).
We again follow Drinfeld’s argument [ Dri76], cf. also [ Ka81]. We
may assume that S is aﬃne and that J n+1 = 0. We begin with the full
faithfulness: given a homomorphism f∞ : A[p∞]→ B[p∞] such that f∞
(modJ ) comes from a homomorphism
f :Ared→Bred of abelian schemes
over Sred, we have to show that there exists a unique homomorphism f :
A→B compatible with f∞ andf . The unicity follows from the injectivity
of Hom(A,B )→ Hom(Ared,B red) (2.2.3). Furthermore, 2.2.3 shows the
existence of a homomorphism g compatible with pnf∞ and pnf . To show
the existence of an f such that g =pnf =f◦ [pn], the point is to show that
g killsA[pn], which can be seen on g∞.
For the essential surjectivity, we have to construct an abel ian scheme A
overS compatible with a given datum ( A, Λ ,ǫ ) in Def p-div(S). By unicity
of liftings, it suﬃces to do so locally on S. hence we may assume that S is
aﬃne, and choose an abelian scheme A′ overS and an isogeny A′
red→
A. By
the above argument, pn times the given isogeny A′
red→
A lifts to a (unique)
isogeny e : A′[p∞]→ Λ of p-divisible groups over S. Its kernel is a ﬁnite
locally free subgroup scheme of A′, and we can form the abelian scheme
A′′ :=A′/ Kere. The isogeny A′′[p∞]→ Λ induced by e is an isomorphism
(modJ ), hence is an isomorphism.

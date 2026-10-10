---
doc_id: arxiv-2106.07444v2
doc_title: "FROM THE HECKE CATEGORY TO THE UNIPOTENT LOCUS"
section_id: sec-006-6-khovanovrozansky-homology
section_title: "Khovanov–Rozansky Homology"
section_number: 6
pages: 41-45
source_pdf: 2106.07444v2.pdf
source_sha256: 5acca39c07bcdddd
doc_brief: "FROM THE HECKE CATEGORY TO THE UNIPOTENT LOCUS — Let W be the W eyl group of a split semisimple group G. Its Hecke category HW can be built from pure perverse sheaves on the double ﬂag variety of G."
---
6.1. A link in a 3-manifold is the image of a disjoint union of ﬁ nitely many circles
under a smooth embedding. The HOMFLY series of a link in S3 is a bivariate
Laurent series that only depends on its isotopy class [ HOMFLY].
Dunﬁeld–Gukov–Rasmussen predicted [DGR], and Khovanov–Rozansky constructed
[KR], a categoriﬁcation of the HOMFLY series, sending a link in 3 -space to a triply-
graded vector space over Q. This isotopy invariant is now known as HOMFL Yor
Khovanov–Rozansky homology . The original construction used the homotopy
theory of matrix factorizations. In [ Kh], Khovanov gave an alternative approach
via the Hochschild homology of Soergel bimodules for the gro ups W = Sn. Via
Soergel’s Erweiterungssatz [ So, Thms. 15-17], the output of his construction (after
base change from Q to ¯Qℓ) is equivalent to a functor
HHH : HW → Kb(Vect2) ⊆ Vect3,
where Vectd denotes the category of Zd-graded ¯Qℓ-vector spaces. Khovanov’s con-
struction extends to Soergel bimodules for any Coxeter grou p, so in particular, HHH
can be deﬁned on the Hecke category of any such group.
Remark 6.1.1. To dispel any ambiguity from our conventions, we state expli citly:
Ifβ is a topological braid on n =r + 1 strands, and ˆβ is the link closure of β, then
P(β) = (at)|β|a−r∑
i,j,k
(a2q
1
2t)r−iq
j
2tk dim HHHi,i+j,k(R(β))
is an isotopy invariant of ˆβ that equals 1 when ˆβ is the unknot. It matches the
invariant in [ DGR] once we substitute q
1
2 =q. In particular, for β = 1, we have
P(1) =
(
q
1
2
a
(1 +a2t
1 − q
))r
.
Compare to Example 6.2.2, below.
6.2. In [ WW08], Webster–Williamson interpreted the Hochschild homolog y of a
Soergel bimodule as the hypercohomology of a sum of shifted p ure perverse sheaves
over G. In subsequent papers [ WW11, WW17], they showed how to interpret
HHH∗,∗,∗ in a similar way, except in terms of a complex of such objects. We will
rewrite their work in our notation.
For any G0-varietyX0 over F, we write
H∗
G(X, −) := Hom ∗( ¯Qℓ, −) : Db
G,m(X0) → Mod1( ¯Qℓ[F ]),
where ¯Qℓ[F ] is concentrated in degree zero. In other words, H∗
G(X,K ) is the
hypercohomology of ξK ∈ Db
G(G), implicitly endowed with the Frobenius action
coming from K. With this notation, the theorem below summarizes the main
results of [ WW08] and [ WW17].
Theorem 6.2.1 (Webster–Williamson). We have
HHHi,i+j,k ≃ Hk ◦ Kb(grw
i+j Hj
G(G, (κ ◦ CH)(−)))
42 MINH-TÂM QUANG TRINH
for all i,j,k ∈ Z. In particular, we have
HHHi,i+j,k(ICw,0[−n]△) ≃
{
grw
i+j Hj
G(G, CH(ICw)) k =n
0 k ⁄=n
for all w ∈W and n ∈ Z.
Example 6.2.2. Below, we review the calculation of HHH(IC 1) ≃ grw
∗ H∗
G(G, G).
Since G is the pushforward of the constant sheaf on the Grothendieck –Springer
resolution, it suﬃces to calculate the G-equivariant cohomology of ˜G together with
its weight ﬁltration.
Fix a maximal torus T0 ⊆G0 and a Borel B0 ⊇T0. By Lemma 4.5.2, [ ˜G0/G0] ≃
[B0/B0], where B0 acts on itself by conjugation. Therefore, there are weight-
preserving isomorphisms
Hj
G(G, G) ≃ Hj
B(B, ¯Qℓ)
≃ Hj
T (T, ¯Qℓ)
≃
⨁
i
Hj−i
T (pt, ¯Qℓ) ⊗ Hi(T, ¯Qℓ).
Above, Frobenius acts by q
j−i
2 on Hj−i
T (pt) and by qi on Hi(T ), so it acts by q
i+j
2
on the ith summand of the last expression. We deduce that
grw
i+j Hj
G(G, G) ≃ Hj−i
T (pt, ¯Qℓ) ⊗ Hi(T, ¯Qℓ).
The proof of [ WW11, Prop. 11] shows that this isomorphism is W -equivariant with
respect to:
(1) The W -action on the left-hand side induced by ¯Qℓ[W ] ⊆ AW ≃ AG, i.e.,
the Springer action arising from the monodromy of G over the regular
semisimple locus of G.
(2) The W -action on the right-hand side induced by Hj−i
T (pt, ¯Qℓ) ≃ Sym
j−i
2 (V)
and Hi(T, ¯Qℓ) ≃ Λi(V).
6.3. In the rest of this section, we prove Theorem 3, stating that Khovanov–
Rozansky homology is a summand of the AW trace.
In what follows, recall from Section 2 that for all φ ∈ ˆW , we write Vφ for an
irreducible representation of W that aﬀords the character φ, endowed with the
trivial action of Frobenius.
Lemma 6.3.1. LetK ∈ C ˆW (G0) be an indecomposable shifted perverse sheaf, and
writeK = Gφ ⊗M , where φ ∈ ˆW andM is the pullback of a pure weight-zero object
of Db
G,m(pt 0). Then we have W -equivariant isomorphisms:
grw
i+j Hj
G(G,K ) ≃ HomW (Vφ, (Sym
j−i
2 ⊗Λi)(V)) ⊗ξM,(18)
grw
0 Hom0(K, G⟨i⟩ ) ≃ HomW (V ∨
φ , ¯Qℓ[W ] ⊗ Sym
j
2 (V)) ⊗ξM ∨(19)
≃Vφ ⊗ Sym
i
2 (V) ⊗ξM ∨.
Moreover, these isomorphisms are functorial in K.
FROM THE HECKE CATEGORY TO THE UNIPOTENT LOCUS 43
Proof. By Example 6.2.2, there is a W -equivariant isomorphism
grw
i+j Hj
G(G, G) ≃ (Sym
j−i
2 ⊗ Λi)(V),
which yields ( 18). Next, Theorems 3.3.1 and 1 give a W -equivariant isomorphism
grw
0 Hom0(G, G⟨i⟩ ) ≃ ¯Qℓ[W ] ⊗ Sym
i
2 (V),
which yields (19). Functoriality is a consequence of the fact that AG
∼
− →AS
∼
− →AW
is an isomorphism of algebras, not just of vector spaces. □
Lemma 6.3.2. We have
(grw
i+j Hj
G(G, −))∨ ≃ HomW (Λi(V), grw
0 Hom0(−, G⟨j⟩ ))
as contravariant functors C(G0)op → Vect0.
Proof. By the preceding lemma and the self-duality of Sym ∗(V) as a representation
of W , the statement holds with C ˆW (G0) in place of C(G0). Now apply Theorem
2.11.1, observing that the constant sheaf is a summand of G. □
Lemma 6.3.3. We have
grw
0 Hom0(−, G⟨j⟩ ) ≃ Hom0(i∗(−)⟨−r⟩, S⟨j⟩ )
as contravariant functors C(G0)op → Mod0( ¯Qℓ[W ]).
Proof. By Theorem 1, the statement holds with C ˆW (G0) in place of C(G0). Now
apply Theorem 2.11.1, observing that i∗⟨−r⟩ is compatible with the functors PR.
□
Proof of Theorem 3. The theorem claims that
(HHHi,i+j,k)∨ ≃ HomW (Λi(V), AHj+k,j (−))
as contravariant functors on HW = Kb(C(B0 × B0)). For ease of notation, let
Φj = Hom C(G0)(i∗(−)⟨−r⟩, S⟨j⟩ ),
resp. Ψi,j = Hom Kb(C(G0))(i∗(−)⟨−r⟩, S⟨j⟩ [i −j]△),
as a functor C(G0) → Mod0( ¯Qℓ[W ]), resp. Kb(C(G0)) → Mod0( ¯Qℓ[W ]). By Lemma
2.11.2, we have κ ◦i∗⟨−r⟩ ≃ i∗⟨−r⟩ ◦ κ as functors on C(G0), and therefore,
AHj+k,j ≃ Ψj+k,j ◦ Kb(κ ◦ CH).
At the same time, we have
Ψj+k,j ≃ Hk ◦ KbΦj.
Furthermore, by Lemmas 2.10.2 and 6.3.3,
Φj ≃ Hom0(i∗(−)⟨−r⟩, S⟨j⟩ ) ≃ grw
0 Hom0(−, G⟨j⟩ ).
44 MINH-TÂM QUANG TRINH
Combining these equivalences with Lemma 6.3.2, we compute
HomW (Λi(V), AHj+k,j (−))
≃ HomW (Λi(V), Hk ◦ Kb(Φj ◦κ ◦ CH))
≃ HomW (Λi(V), Hk ◦ Kb(grw
0 Hom0((κ ◦ CH)(−), G⟨j⟩ )))
≃ Hk ◦ Kb(HomW (Λi(V), grw
0 Hom0((κ ◦ CH)(−), G⟨j⟩ )))
≃ Hk ◦ Kb((grw
i+j Hj
G(G, (κ ◦ CH)(−)))∨).
The last expression is equivalent to ( HHHi,i+j,k)∨ by Theorem 6.2.1. □
6.4. Let X (β) be deﬁned by the cartesian square:
X (β) U(β)
{1} U
pβ
Proof of Corollary 4. We claim that for all β ∈ Br +
W , we have
HHH0,j,k(R(β))∨ ≃ grw
j+2r H!,G
−(j+k+2r)(U(β)),
HHHr,r+j,k(R(β))∨ ≃ grw
j+2(r−N ) H!,G
−(j+k+2(r−N ))(X (β)).
Let 1 and ε be the trivial and sign characters of W , respectively. Then 1, resp.ε,
is the character of Λ 0(V), resp. Λr(V), so Theorems 3 and 5.4.2 give us
HHH0,j,k(R(β))∨ ≃ grw
j+r Homj+k+r(pβ,! ¯Qℓ, S1)
HHHr,r+j,k(R(β))∨ ≃ grw
j+r Homj+k+r(pβ,! ¯Qℓ, Sε).
By Springer theory, we know that:
• S 1 is the sheaf ¯Qℓ⟨−r⟩ over U.
• S ε is the skyscraper sheaf at 1 ∈ U with stalk ¯Qℓ⟨−r − 2N ⟩ .
Now, both of the desired isomorphisms follow from Lemma 4.3.1. □
FROM THE HECKE CATEGORY TO THE UNIPOTENT LOCUS 45

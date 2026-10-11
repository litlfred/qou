---
doc_id: arxiv-2401.00636v2
doc_title: "PERIODIC AND QUASI-MOTIVIC PENCILS OF FLAT CONNECTIONS"
section_id: sec-004-23-generically-periodic-holomorphic-maps-up-to-g
section_title: "Generically periodic holomorphic maps up to G-action"
section_number: 2.3
pages: 4-5
source_pdf: 2401.00636v2.pdf
source_sha256: 35e372d04cedf234
toc_source: outline
---
standard basis of the standard n-dimensional space. Let G be an complex aﬃne algebraic
group and V a ﬁnite dimensional algebraic representation of G.
Let ρ : Cn →V be a
holomorphic map.
Deﬁnition 2.4. We say that ρ is generically periodic up to G-action if for each j the
vectors ρ(s + ej) and ρ(s) are G-conjugate for an analytically Zariski dense set of s ∈Cn.
Theorem 2.5. Let ρ : Cn →V be an exponentially bounded holomorphic map which is
generically periodic up to G-action. Then there exists a nonempty aﬃne open subset U of
(C×)n, a ﬁnite unramiﬁed Galois cover p : eU →U, and a Galois-stable up to G-action regular
function η : eU →V such that ρ(s) is G(C)-conjugate to η|e2πis for e2πis ∈U. Moreover, η is
unique up to action of G(C(q)).
Proof. Consider the closed subvarieties Yi of V of vectors y ∈V with stabilizer Gy ⊂G of
codimension ≤i. Thus Y0 ⊂Y1 ⊂... ⊂Ydim G = V . Let d be the smallest integer such that
ρ : Cn →Yd.
Let E ⊂V be a generic aﬃne subspace of codimension d (a gauge ﬁxing subspace). Then
for suﬃciently generic s (namely, outside of a proper analytic subset Z ⊂Cn) the set Ξs of
v ∈E which are G-conjugate to ρ(s) has a ﬁnite cardinality m.
So we obtain a meromorphic map R : Cn →ΣmV (m-th symmetric power of V as a
variety) with poles at Z given by R(s) = Ξs; i.e. for each regular function Ψ on ΣmV the
function fΨ := Ψ ◦R : Cn →C is meromorphic with poles at Z.
PERIODIC AND QUASI-MOTIVIC PENCILS OF FLAT CONNECTIONS
5
Moreover, since ρ is generically periodic up to G-action, R(s + ej) = R(s) and therefore
fΨ(s+ej) = fΨ(s) for an analytically Zariski dense set of s. Thus fΨ(s+ej) = fΨ(s) as mero-
morphic functions on Cn. So fψ(s) = FΨ(e2πis), where FΨ : (C×)n →C is a meromorphic
function.
Finally, by construction, fΨ can be written as g/h, where g, h : Cn →C are polynomials
of ρ(s), hence they are exponentially bounded. So it follows from Lemma 2.3 that FΨ is
rational. Thus R descends to a rational map R : (C×)n →ΣmV , which deﬁnes a point of
Q ∈ΣmV (C(q)). Now any η ∈Q is a Galois-stable element of C(q)⊗V , and in fact belongs
to C[eU] ⊗V for some U ⊂(C×)n and p : eU →U, such that η has the required property for
e2πis ∈U.
It remains to show that η is unique up to G-action. Let η1, η2 be two such elements.
We may assume that both of them are deﬁned over C[eU] where U ⊂(C×)n is a nonempty
aﬃne open subset and p : eU →U is a ﬁnite unramiﬁed Galois cover. Let a ∈U, Ua be a
small ball around a, and U1 be a connected component of p−1(Ua). There exists a connected
component U2 of p−1(Ua) such that for an analytically dense set of b ∈Ua , η1|b1 = η2|b2,
where bi are the preimages of b in Ui, i = 1, 2. So by Chevalley’s elimination of quantiﬁers,
there exists g ∈G(C(q)) such that gη1 = η2.
□

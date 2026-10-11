---
doc_id: arxiv-2208.05331v6
doc_title: "PURE BRAID GROUP ACTIONS ON CATEGORY O MODULES"
section_id: sec-006-7-the-equivariant-monodromy-theorem
section_title: "The equivariant monodromy theorem"
section_number: 7
pages: 24-27
source_pdf: 2208.05331v6.pdf
source_sha256: 54b4a400388dbf41
toc_source: outline
---
We review in this section the main result of [ATL15], which extends that of
[TL08, TL16] to the case of an arbitrary symmetrisable Kac–Moody algebra, and
yields an equivalence of braided Coxeter categories Oℏ,int
g,∇→O int
Uℏg,R,S. Its proof
relies on the Etingof–Kazhdan equivalence, which is brieﬂy reviewed in 7.1–7.2.
7.1. The Etingof–Kazhdan equivalence. In [EK08, Thm. 4.2], Etingof and
Kazhdan construct an equivalence of categories F : Oℏ
∞,g →O∞,Uℏg, together
with an isomorphism α of functors
Oℏ
∞,g
O∞,Uℏg
Vectℏ
F
f
fℏ
α
where f and fℏare the forgetful functors.1 The equivalence F is the identity on
h–modules and preserves integrability [ATL15, Lemma 22.9]. It therefore gives rise
to a diagram of functors in which every face commutes
Oℏ,int
∞,g
Oint
∞,Uℏg
Oℏ
∞,g
O∞,Uℏg
Modℏ
h
Modℏ
h
Vectℏ
Vectℏ
Fint
fint
fint
0
fint
ℏ,0
fint
ℏ
F
f0
f
fℏ,0
fℏ
fh
fh
(7.1)
where the vertical arrows are restriction functors, and the natural isomorphisms
are either trivial or induced from α.2
1More precisely, in [EK08] Etingof–Kazhdan construct an equivalence F between the larger
categories of Drinfeld–Yetter modules over the negative Borel subalgebra b−, and admissible
Drinfeld–Yetter modules over Uℏb−(see also [ATL18, 6.13]). It easily follows that F restricts to
an equivalence Oℏ
∞,g →O∞,Uℏg, since it is the identity on Drinfeld–Yetter h–modules, see [ATL15,
Lemma 22.11]. By the same argument, it also restricts to an equivalence Oℏ
g →OUℏg.
2The categories Wℏ, Oℏ
∞,g and O∞,Uℏg naturally ﬁt within the diagram (7.1), but are omitted
for simplicity.
PURE BRAID GROUP ACTIONS ON CATEGORY O MODULES
25
7.2. The Etingof–Kazhdan isomorphism. In terms of completions, the Etingof–
Kazhdan equivalence (F, α) gives rise to an isomorphism Ψ : End(fℏ) →End(f) via
the composition
End(fℏ) −→End(fℏ◦F) −→End(f)
(7.2)
where the ﬁrst isomorphism is induced by F, and the second is given by Ad(α). By
(7.1), Ψ restricts to an isomorphism Ψint : End(fint
ℏ) →End(fint) such that
End(fint
ℏ)
End(fint)
End(fℏ)
End(f)
End(fh)
End(fh)
Ψint
Ψ
⟲
⟲
where the vertical arrows are restriction to category O∞and integrable modules.
7.3. The classical Drinfeld algebra. Let D be the analogue of the Drinfeld
algebra Dℏfor Ug[[ℏ]] (cf. Section 3.1). Namely, for any β ∈Q+, let Bβ = {Xβ,p}
be a basis of Un+
β and B = F
β∈Q+ Bβ. Set
D0 =
( X
X∈B
cXX : cX ∈Ub−
)
=
Y
β∈Q+
Ub−⊗Un+
β ⊃Ug
and D = D0[[ℏ]]. The algebra structure of Ug[[ℏ]] extends to one on D and yields a
chain of morphisms Ug[[ℏ]] ⊂D →End(f). Proceeding as in Section 3 one shows
that D embeds into End(f) and End(fint).
7.4. The monodromy theorem. In [ATL15, Thm. 22.1] we prove the following.
Theorem.
(1) There is a canonical equivalence of braided pre–Coxeter categories (cf. Re-
mark 6.6)
Hg = (HB, γF) : Oℏ
g,∇→OUℏg,R,S
such that
• for any B ⊆D, the equivalence HB is the Etingof–Kazhdan functor
FgB : Oℏ
∞,gB →O∞,UℏgB
• for any B′ ⊆B and F ∈Mns(B, B′), the natural isomorphism γF is in-
duced by the action of an invertible weight zero element gF in the Drinfeld
26
A. APPEL AND V. TOLEDANO LAREDO
algebra of gB, i.e., there is a commutative diagram of functors
O∞,UℏgB
Oℏ
∞,gB
O∞,UℏgB′
Oℏ
∞,gB′
Vectℏ
Vectℏ
fℏ,B
fℏ,B′B
γF
fB
fB′B
FgB
fℏ,B′
FgB′
fB′
gF
(7.3)
where the unmarked back face is the identity and the two unmarked lateral
faces are the isomorphisms α for gB and gB′.
(2) Hg restricts to an equivalence of braided Coxeter categories
H
int
g = (H
int
B , γF) : Oℏ,int
g,∇→O
int
Uℏg,R,S
where H int
B = Fint
gB.
(3) For any F ∈Mns(D), the isomorphism
Ψ
int
F = Ad(gF) ◦Ψ
int : End(f
int
ℏ) →End(f
int)
intertwines the quantum Weyl group and the monodromy actions of BW , i.e.,
BW
End(fint
ℏ)
End(fint)
λ
µF
Ψint
F
⟲
(7.4)
where µF = PF
τ,B denotes the monodromy action of BW around the point at
inﬁnity in the De Concini–Procesi compactiﬁcation of X corresponding to F.
Since the diagrammatic equivalences are ﬁxed, the proof amounts to construct-
ing suitable isomorphisms (6.2). The construction is in two steps. First, we prove
that O int
Uℏg,R,S is equivalent to a braided Coxeter category Oℏ,int
g,R,S with diagram-
matic categories Oℏ,int
∞,gB, B ⊆D, and standard restriction functors with non–trivial
tensor structures. The equivalence is given by the diagrammatic Etingof–Kazhdan
functors, equipped with natural isomorphisms eγF whose construction is carried out
in [ATL18, ATL19a]. Then, relying on the rigidity result from [ATL19b], we prove
that Oℏ,int
g,R,S is equivalent to Oℏ,int
g,∇with diagrammatic equivalences given by the
identity functors. Finally, we observe that, by [ATL19a, Thm. 10.7], the resulting
isomorphisms γF satisfy (7.3) for weight zero elements gF in the Drinfeld algebra.
PURE BRAID GROUP ACTIONS ON CATEGORY O MODULES
27

---
doc_id: arxiv-1103.4815v3
doc_title: "Four Equivalent Versions of Non-Abelian Gerbes"
section_id: sec-006-3-version-i-groupoid-valued-cohomology
section_title: "Version I: Groupoid-valued Cohomology"
section_number: 3
pages: 16-18
source_pdf: 1103.4815v3.pdf
source_sha256: 28647b02ea1441e3
doc_brief: "Four Equivalent Versions of Non-Abelian Gerbes — We recall and partially improve four versions of smooth, non -abelian gerbes: ˇCech cocycles, classifying maps, bundle gerbes, and principal"
---
We have already mentioned group valued ˇCech 1-cocycles in the introduction. They consist of an
open cover U = {Ui}i∈I of M and smooth functions gij : Ui ∩Uj /d47/d47 G satisfying the cocycle
condition gij ·gjk =gik. Segal realized [Seg68] that this is the same as a smooth functor
g : ˇC(U ) /d47/d47 BG
where BG denotes the one-object groupoid introduced in Example 2.1.1 (b) an d ˇC(U ) denotes the
ˇCech groupoid corresponding to the cover U . It has objects ⨆
i∈IUi and morphisms ⨆
i,j ∈IUi ∩Uj,
and its structure maps are
s(x,i,j ) = (x,i ) , t(x,i,j ) = (x,j ) , id (x,i ) = (x,i,i ) and ( x,j,k ) ◦ (x,i,j ) = (x,i,k ).
Analogously, smooth natural transformations between smooth f unctors ˇC(U ) /d47/d47 BG give rise
to ˇCech coboundaries. Thus the set
[ ˇC(U ), BG
]
of equivalence classes of smooth functors equals
the usual ﬁrst ˇCech cohomology with respect to the cover U . The classical ﬁrst ˇCech-cohomology
ˇH1(M,G ) of M is hence given by the colimit over all open covers U of M
ˇH1(M,G ) = lim− →U
[ ˇC(U ), BG
]
.
We use this coincidence in order to deﬁne the 0-th ˇCech cohomology with coeﬃcients in a general
Lie groupoid Γ:
– 16 –
Deﬁnition 3.1. If Γ is a Lie groupoid we set
ˇH0(M, Γ) := lim− →U
[ ˇC(U ), Γ
]
where the colimit is taken over all covers U of M and
[ ˇC(U ), Γ
]
denotes the set of equivalence
classes of smooth functors ˇC(U ) /d47/d47 Γ .
Remark 3.2. The choice of the degree is such that ˇH0(M, Γ) agrees in the case Γ = Gdis (Example
2.1.1 (a)) with the classical 0-th ˇCech-cohomology ˇH0(M,G ) of M with values in G.
The geometrical meaning of the set is given in the following well-known t heorem, which can be
proved e.g. using Lemma 2.2.8.
Theorem 3.3. There is a bijection
ˇH0(M, Γ) ∼=
{ Isomorphism classes of
principal Γ -bundles over M
}
.
If Γ is not only a Lie 2-groupoid but a Lie 2-group one can also deﬁne a ﬁrst cohomology
group ˇH1(M, Γ). Indeed, in this case one can consider the Lie 2-groupoid BΓ with one object,
morphisms Γ 0 and 2-morphisms Γ 1. Multiplication in Γ gives the composition of morphisms in
BΓ. Let
[ ˇC(U ), BΓ] denote the set of equivalence classes of smooth, weak 2-funct ors from the
ˇCech-groupoid ˇC(U ) to the Lie 2-groupoid BΓ. For the deﬁnition of weak functors see [B´ en67] –
below we will determine this set explicitly.
Deﬁnition 3.4. For a 2-group Γ we set
ˇH1(M, Γ) := lim− →U
[ ˇC(U ), BΓ
]
.
Remark 3.5. This agrees for Γ = Gdis with the classical ˇH1(M,G ). Furthermore, for an abelian
Lie group A the Lie groupoid BA is even a 2-group and ˇH1(M, BA) agrees with the classical ˇCech-
cohomology ˇH2(M,A ).
Unwinding the above deﬁnition, we get Version I of smooth Γ-gerbes :
Deﬁnition 3.6. Let Γ be a Lie 2-group, and let U = {Uα }α ∈A be an open cover of M .
1. A Γ -1-cocycle with respect to U is a pair (fαβ ,gαβγ ) of smooth maps
fαβ :Uα ∩Uβ /d47/d47 Γ 0 and gαβγ :Uα ∩Uβ ∩Uβ /d47/d47 Γ 1
satisfying s(gαβγ ) = fβγ ·fαβ and t(gαβγ ) = fαγ , and
gαβδ ◦ (gβγδ · idfαβ ) = gαγδ ◦ (idfγδ ·gαβγ ). (3.1)
Here, the symbols ◦ and · stand for the composition and multiplication of Γ , respectively.
– 17 –
2. Two Γ -1-cocycles (fαβ ,gαβγ ) and (f ′
αβ ,g ′
αβγ ) are equivalent, if there exist smooth maps hα :
Uα /d47/d47 Γ 0 and sαβ :Uα ∩Uβ /d47/d47 Γ 1 with
s(sαβ ) = g′
αβ ·hα , t(sαβ ) = hβ ·gαβ
and (idhγ ·gαβγ ) ◦ (sβγ · idfαβ ) ◦ (idfβγ ·sαβ ) = sαγ ◦ (g′
αβγ · idhα ).
Remark 3.7. For a crossed module t : H /d47/d47 G and Γ := G/ /Hthe associated Lie 2-group
(Example 2.4.2) one can reduce Γ-1-cocycles to pairs
˜fαβ :Uα ∩Uβ /d47/d47 G and ˜ gαβγ :Uα ∩Uβ ∩Uβ /d47/d47 H
which satisﬁes then a cocycle condition similar to (3.1). Analogously, c oboundaries can be reduced
to pairs
˜hα :Uα /d47/d47 G and ˜ sαβ :Uα ∩Uβ /d47/d47 H.
This yields the common deﬁnition of non-abelian cocycles, which can fo r example be found in
[Bre90] or [BS09].
Example 3.8. In case of the crossed module i :H /d47/d47 Aut(H) with Γ = AUT( H) (see Example
2.4.4) Γ-1-cocycles consist of pairs ˜fαβ : Uα ∩Uβ /d47/d47 Aut(H) and ˜gαβ : Uα ∩Uβ ∩Uγ /d47/d47 H.
Cocycles of this kind classify so-called Lie groupoid H-extensions [CLGX09, Proposition 3.14],
which can hence be seen as another equivalent version for AUT( H)-gerbes.

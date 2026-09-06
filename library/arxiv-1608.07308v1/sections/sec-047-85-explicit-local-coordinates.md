---
doc_id: arxiv-1608.07308v1
doc_title: "FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY"
section_id: sec-047-85-explicit-local-coordinates
section_title: "Explicit local coordinates"
section_number: 8.5
pages: 62-64
source_pdf: 1608.07308v1.pdf
source_sha256: bcc3b6f1a91a55c6
doc_brief: "FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY — We construct a categoriﬁcation of the maximal commutative subalgebra of the type A Hecke algebra."
---
the neighborhood of the ﬁxed pointIT for any standard Young tableauT :
(8.14) ˚FHilbT := (FHilbn)localized atT
and the dg local ring ˚Adg
T = C[ ˚FHilb
dg
T ]. In fact, we will actually describe an open subscheme
of FHilbT given by the non-vanishing of certain torus invariant functions. The resulting open
subschemes also form a cover of FHilbn because of the principle (8.10), so we abuse notation
and use (8.14) both for the local neighborhood and for the open subscheme ˚FHilbT⊂ FHilbT .
Proposition 8.6. For any standard Young tableauT⊣n, the complexEn of (2.25) is:
(8.15) En| ˚FHilbT
q.i.s.
∼=
[ ■ outer⨁
corner ofT
O· e■
ψ
−→
□ inner⨁
corner ofT
O· f□
]
Theorem 2.6 describes the map π : FHilbn+1→ FHilbn as the projectivization of H0(En).
Locally, this map takes the form:
π−1
(
˚FHilbT
)
=
□ inner⋃
corner ofT
˚FHilbT∪□
where ˚FHilbT∪□⊂ PH0(
E∨
n| ˚FHilbT
)
is the afﬁne chart of (8.15) given byf□ = 1. We conclude
(8.5), where the generators aref□′ for inner corners□′⁄=□ and the relations arer■ =ψ(e■).
Proof. From each box inT , draw two lines of unit length, one going up and one to the right:
1
3
4
2
5
6
8
7
The lines are of two types: thick or dotted, and black or red. The color of a line is determined
by whether the line points to a box in T or outside of T . The shape of a line is determined
FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY 63
by the following rule: If i > i′ wherei′ is the label of the box to the southeast (respectively
northwest) ofi, then we make the horizontal (respectively vertical) line starting at i thick. All
the boxes below and to the left of the diagram are thought to have label 0 for the purpose of
this rule, and all the boxes above and to the right of the diagram are thought to have label ∞.
By deﬁnition:
(8.16) En =
[
qtTn
Ψ
−→qTn⊕tTn⊕O
Φ
−→Tn
]
When we restrict the complex to the afﬁne chart ˚FHilbT , we observe that the tautological
bundles are already trivialized by the basise1,...,e n of Deﬁnition 8.2:
Tn| ˚FHilbT
=O· e1⊕...⊕O· en
Therefore, the middle term of (8.16) has a basis which we will denote bye1,...,e n,e′
1,...,e′
n, 1.
We claim that the projection that forgets some of these basis vectors induces an isomorphism:
(8.17) Ker Φ| ˚FHilbT
∼=
red or dotted horizontal⨁
lines from boxi
O· ei
red or dotted vertical⨁
lines from boxi
O· e′
i
In other words, we claim that if one speciﬁes rescaled basis vectors ciei anddie′
i correspond-
ing to the red and dotted edges, then there exist unique rescaled basis vectors γiei and δie′
i
corresponding to the black thick edges, and a functionf, such that:
(X−xn+1)
(∑
i dotted
ciei +
∑
i thick
γiei
)
+ (Y−yn+1)
(∑
i dotted
diei +
∑
i thick
δiei
)
+fe 1 = 0
Any box k has a unique black thick line going to the left or down. Assume without loss of
generality that the black thick line from k leads one step left to the box i. Then (8.8) implies
that equating the coefﬁcient ofek in the left hand side to 0 yields the equation:
γi∈
∑
j
(cj ordj)· coefﬁcients +
∑
j
(γj orδj)· ˚mT
This system of equations can be solved in the localization˚AT , since its determinant is in1+˚mT .
Therefore, we conclude that in the local chart ˚FHilbT , we have:
(8.18) En| ˚FHilbT
q.i.s.
∼=
[ n⨁
i=1
O· ei
Ψ
−→
red or dotted horizontal⨁
lines from boxi
O· ei
red or dotted vertical⨁
lines from boxi
O· e′
i
]
The Proposition will be proved once we show that projecting the two terms in the above com-
plex to a certain subset of factors induces a quasi-isomorphism. Speciﬁcally, in the domain of
Ψ we consider the subspace spanned by basis vectorse■ corresponding to outer corners■, and
in the codomain of Ψ we project onto one basis vector f□ corresponding to each inner corner.
The rule is thatf□ =ei ore′
i′, depending on whether the number i to the left of□ is bigger or
smaller than the number i′ below□. In other words, the only ei ore′
i we will consider in the
codomain of Ψ are the ones corresponding to thick red lines:
(8.19) En| ˚FHilbT
q.i.s.
∼=
[ ■ outer⨁
corner ofT
O· e■
ψ
−→
□ inner⨁
corner ofT
O· (e□← ore′
□↓)
]
64 EUGENE GORSKY, ANDREI NEGUT , , AND JACOB RASMUSSEN
In plain English, the claim is that for anyei wherei is not an outer corner ofT , quotienting the
codomain of (8.18) by the vector:
(8.20)
red or dotted horizontal∑
lines between boxes ¯jk
(xj
i−δi
jxn+1)ej +
red or dotted vertical∑
lines between boxes ¯jk
(yj
i−δi
jyn+1)e′
j
will allow us to solve for one of the ej,e′
j. The only basis vectors which remain unsolved for
should be the ones that appear in the codomain of (8.19). For example, suppose we are trying
to solve for ej, wherej corresponds to a dotted horizontal edge ¯jk. Then with the notation in
the following picture:
i
j
j′
k
let us observe that (8.8)–(8.9) imply thatyj
i =xj′
i =yk
j′∈ 1 + ˚mT . Then the vector (8.20) lies
inej + ˚mT , andej can therefore be solved for in the localization ˚AT .
□

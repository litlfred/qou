---
doc_id: arxiv-1604.02688v1
doc_title: "THE 3D-INDEX AND NORMAL SURFACES"
section_id: sec-006-4-the-3d-index-of-an-ideal-triangulation
section_title: "The 3D-index of an ideal triangulation"
section_number: 4
pages: 6-8
source_pdf: 1604.02688v1.pdf
source_sha256: bdcafe379519287c
doc_brief: "THE 3D-INDEX AND NORMAL SURFACES — Dimofte, Gaiotto and Gukov introduced a powerful invariant, the 3D-index, associated to a suitable ideal triangulation of a 3-manifold with torus boundary"
---
Using the notation from the previous section, we now give a deﬁnition of the 3D-index of
an ideal triangulationT as formulated in [GHRS15, section 4.7].
Given k = (k1,...,k n)∈ Zn, we can assign an integer weightki to theith edge class. Eﬀec-
tively, this also gives a weight on each edge of each tetrahedronσj in T. Letaj(k),bj(k),cj(k)
be the sums of weights assigned to the pair of edges in tetrahedronj opposite quadsqj,q′
j,q′′
j
respectively. Note that these coeﬃcients are precisely the entries in the linear combination∑n
i=1kiEi of the rows of the gluing matrix corresponding to the edge equations.
Now we deﬁne a tetrahedral index associated to the tetrahedronσj by
J(σj; k) =J∆(aj(k),bj(k),cj(k)).
THE 3D-INDEX AND NORMAL SURF ACES 7
and the3D-index IT(0) of the triangulationT is deﬁned as
IT(0)(q) =
∑
k∈Zn−r
q
∑
iki
n∏
j=1
J(σj; k), (15)
where the summation is over a (suitable) sublatticeZn−r⊂ Zn, obtained by settingr of the
edge weightski equal to zero. Forr = 1 we can set anyki = 0; but in general ther edge
weights set to zero must be chosen carefully (see [GHRS15, sections 4.5, 4.6]).
More generally, the 3D-index gives a functionIT :H1(∂M ; Z)∼= Z2r→ Z((q
1
2 )) deﬁned as
follows. Letγ be an oriented multicurve on∂M with no contractible components, such that
γ is innormal positionwith respect to the induced triangulationT∂ of ∂M. Then letγh be
the component ofγ in cusph and expressγh = phµh +qhλh, whereµh corresponds to the
rowMh in the gluing matrix andλh corresponds toLh. Now put
J(σj; k,γ ) =J∆(aj(k,γ ),bj(k,γ ),cj(k,γ ))
where the coeﬃcientsaj(k,γ ),bj(k,γ ),cj(k,γ ) are precisely the entries in the linear combi-
nation∑n
i=1kiEi +∑n
h=1(phMh +qhLh) corresponding to tetrahedronσj.
Then the general3D-index of the triangulationT is deﬁned as
IT([γ])(q) =
∑
k∈Zn−r
q
∑
iki
∏
j
J(σj; k,γ ), (16)
where [γ]∈H1(∂M ; Z) is the homology class ofγ and the summation is overZn−r⊂ Zn as
above. (It is shown in [GHRS15] that the sum only depends on the homology class ofγ.)
Example 4.1.For the ﬁgure eight knot complementM, with the ideal triangulation given
by Thurston [Thu77, §4], we have the following induced triangulation on∂M (as viewed
from the cusp).
Figure 2. A labelled triangulation of the cusp of the ﬁgure 8 knot complement.
From this we can read oﬀ the following gluing data.
Choosing generatorsµ,λ forH1(∂M, Z) = Z2 corresponding to the standard meridian and
longitude, and integer weightsk1 =k,k 2 = 0 on the edges gives
8 STA VROS GAROUF ALIDIS, CRAIG D. HODGSON, NEIL R. HOFFMAN, AND J. HYAM RUBINSTEIN
edge/peripheral curve a1 b1 c1 a2 b2 c2
edge 1 (blue) 2 1 0 2 1 0
edge 2 (red) 0 1 2 0 1 2
meridian µ 0 0 1 -1 0 0
longitude λ 0 0 0 2 0 -2
IT(xµ +yλ) =
∑
k∈Z
qkJ∆(2k,k,x )J∆(2k−x + 2y,k,−2y)
=
∑
k∈Z
I∆(k−x,k )I∆(k + 2y,k−x + 2y).
For example, up to terms of orderq10, we have
IT(0) = 1− 2q− 3q2 + 2q3 + 8q4 + 18q5 + 18q6 + 14q7− 12q8− 52q9− 106q10 +...
IT(µ) = 2q− 2q2 + 2q3 + 8q4 + 16q5 + 16q6 + 10q7− 14q8− 52q9− 102q10 +...
IT(2µ) =−q−q2 + 3q3 + 6q4 + 12q5 + 9q6 + 3q7− 19q8− 50q9− 88q10 +...
IT(λ) =q3 + 2q4 + 5q5 + 2q6− 3q7− 16q8− 32q9− 52q10 +...
IT(4µ +λ) =q−q4− 2q5− 5q6− 8q7− 10q8− 11q9− 6q10 +...
In this example, it is easy to check thatIT(±xµ±yλ) =IT(xµ +yλ), and we can also deﬁne
the index forx∈ Z,y∈ 1
2 Z, as done in [DGG13]. For example,
IT(1
2λ) =−2q3/2 + 4q7/2 + 10q9/2 + 14q11/2 + 10q13/2− 2q15/2− 32q17/2− 68q19/2 +...
IT(µ + 1
2λ) =−q−q2 + 2q3 + 7q4 + 11q5 + 11q6 + 3q7− 17q8− 49q9− 88q10 +...
IT(2µ + 1
2λ) =−q1/2 +q5/2 + 4q7/2 + 7q9/2 + 7q11/2 + 3q13/2− 12q15/2− 31q17/2− 62q19/2 +...

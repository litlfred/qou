---
doc_id: arxiv-2104.04941v2
doc_title: "FOCK–GONCHAROV COORDINATES FOR SEMISIMPLE LIE GROUPS S. GILLES"
section_id: sec-024-73-rotation-mutations
section_title: "Rotation mutations"
section_number: 7.3
pages: 36-40
source_pdf: 2104.04941v2.pdf
source_sha256: 84426ed37754aa78
doc_brief: "FOCK–GONCHAROV COORDINATES FOR SEMISIMPLE LIE GROUPS S. GILLES — Fock and Goncharov [FG06b] introduced cluster ensembles, p roviding a framework for coordi- nates on varieties of surface"
---
recall work of Zickert to describe the eﬀect of rot in terms of canonical forms, taking (h1,h 2,h 3,u ) to
(h3,h 1,h 2,~u). We show, using an identity of Fomin–Zelevinsky, that when a ll hi are trivial, µ∗
rotTw takes
coordinates of u to those of ~u. Then we show that the monomial map m of M is exactly what is necessary
to extend to the general case. The ﬁnal pieces ~µO1 and ~µO2, rearrange the vertices without changing their
coordinates according to Lemmas 7.1 and 7.2.
Recall that by Proposition 4.5, we have
~u =h−1
2 (w0(h1))−1(ΦΨΦΨ)( u)(w0(h1))h2.
So we must consider (ΦΨ) 2(u) in terms of minor coordinates, then show that the result agre es in general
with the cluster action of µrot. In other words, we must show that µ∗
rot ﬁts into the diagram of Figure 30.
We interpret the actions of the maps Φ and Ψ on generalized minors, then appeal to an identity of Fomin–
Zelevinsky that applies at every step of the mutation sequen ce µrotTw.
Conf ∗
3(G/N) N− ∩w0G0 (C∗)m
Conf ∗
3(G/N) N− ∩w0G0 (C∗)m
cyc3 (w0(h1)h2)
(
ΦΨ) 2(•)
)
YV
µ∗
rot
YV
Figure 30. Maps Φ and Ψ by Proposition 4.5, YV by Deﬁnition 5.18.
Lemma 7.4. Item 4 of Deﬁnition 4.16 holds for h1 =h2 =h3 are all trivial.
Proof. By Remark 2.35, we need only consider the commuting diagrams for A-coordinates; the diagrams for
X -coordinates will then follow immediately by applying p.
Let ~u = (w0(h1))−1(ΦΨ) 2(u)w0(h1)h2 for notation. The core idea is that, modulo coordinates of hi,
∆ wkωik ,eωik
(u) is approximately ∆ w0ωik ,wkωik
(~u). The mutation sequence µrot transforms ∆ w0ωik ,wkωik
to
∆ wkωik ,eωik
by [FZ99, Theorem 1.17], therefore changing coordinates of u into coordinates of ~u. Later, we
will show that the monomial map exactly compensates for the c oordinates of hi.
To be more precise, the coordinate assigned to interior vert exvi,j is (lettingk =k(i,j ) as in Deﬁnition 5.18)
vi,j = ∆ wkωik ,eωik
(u) · ∆ ωi (σG(h−1
1 )h2) · ∆
wk(i,j) ωi
⊕ (σG(h1))
Focusing on the ﬁrst term, consider (ΦΨ) 2(u) = [Ψ([Ψ( u)w0]−)w0]−. Letting x• ∈ N+, h• ∈ H, and
y• ∈N−,
y0 =u x 1 = Ψ( y0) y2H2x2 =x1w0
y2 = (ΦΨ)( u) x3 = Ψ( y2) y4H4x4 =x3w0
y4 = (ΦΨ) 2(u).
36
Expanding those terms, we have
y4H4x4 =x3w0
= Ψ( y2)w0
= Ψ( x1w0x−1
2 H −1
2 )w0
= Ψ(Ψ( y0)w0x−1
2 H −1
2 )w0
= Ψ( H −1
2 )Ψ(x−1
2 )Ψ(w0)y0w0
=H −1
2 Ψ(x−1
2 )w0y0w0
=
∈N−
/bracehtipdownleft/bracehtipupright/bracehtipupleft/bracehtipdownright
H −1
2 Ψ(x−1
2 )H2 ·
∈H/bracehtipdownleft/bracehtipupright/bracehtipupleft/bracehtipdownright
H −1
2 sG ·
∈N+
/bracehtipdownleft/bracehtipupright/bracehtipupleft/bracehtipdownright
w0−1y0w0
Extracting the N− term, (ΦΨ) 2(u) = y4 =H −1
2 Ψ(x−1
2 )H2, which we can rewrite via
H2 = [Ψ( y0)w0]0, x 2 = Ψ([Ψ( y0)w0]−1
+ ).
Now, consider the minor ∆ w0ωik ,wkωik
(y4). Denote by w∗
k the word deﬁned by Deﬁnition 2.18 using ﬁxed
presentation i∗ =σG(i). By relying on a number of identities from [FZ99],
∆ w0ωik ,wkωik
(H −1
2 Ψ(x−1
2 )H2) =
∆ w0ωik ,wkωik
(Ψ(x−1
2 )) · ∆ wkωik ,wkωik
(H2)
∆ w0ωik ,w0ωik
(H2)([FZ99, Equation 2.14])
∆ w0ωik ,wkωik
(Ψ(x−1
2 )) = ∆ wkωik ,w0ωik
(x−1
2 )([FZ99, Equation 2.25])
= ∆ wkωik ,w0ωik
(Ψ([Ψ( y0)w0]−1
+ )−1)
= ∆ w∗
kωi∗
k
,w0ωi∗
k
(w0[Ψ(y0)w0]−1
+ w0
−1)
= ∆ w0w∗
kωi∗
k
,eωi∗
k
([Ψ(y0)w0]−1
+ )
= ∆ w0w∗
kωi∗
k
,eωi∗
k
([w0y0]−)
=
(
∆ w0w∗
kωi∗
k
,eωi∗
k
(w0y0)
)/(
∆ eωi∗
k
,eωi∗
k
(w0y0)
)
([FZ99, Equation 2.23])
=
(
∆ w∗
kωi∗
k
,eωi∗
k
(y0)
)/(
∆ ωi∗
k ([w0
−1y0]0)
)
Also, by Lemma 4.3, H2 = [Ψ( y0)w0]0 = [w0−1y0]0 = (w0(h3h1)h2)−1, where the hi in the last term refer
to the elements of H in the canonical form for Conf ∗
3(G/N+). Writing solely in terms of (h1,h 2,h 3,u )), we
have
∆ w0ωik ,wkωik
((ΦΨ) 2(u)) = ∆ w∗
kωi∗
k
,eωi∗
k
(u) ·
∆ w0ωik ,w0ωik
(w0(h3h1)h2)∆ eωi∗
k
,eωi∗
k
(w0(h3h1)h2)
∆ wkωik ,wkωik
(w0(h3h1)h2)
= ∆ w∗
kωi∗
k
,eωi∗
k
(u) · 1
∆ wkωik ,wkωik
(w0(h3h1)h2)
Now, introducing the factor of w0(h1)h2, we have
∆ w0ωik ,wkωik
(~u) = ∆ w0ωik ,wkωik
((w0(h1))−1(ΦΨ) 2(u)w0(h1)h2)
= ∆ w0ωik ,wkωik
((ΦΨ) 2(u)) · ∆ w0ωik ,w0ωik
(w0(h1)−1h−1
2 ) · ∆ wkωik ,wkωik
(w0(h1)h2)
= ∆ w∗
kωi∗
k
,eωi∗
k
(u) · 1
∆ wkωik ,wkωik
(w0(h3))∆ w0ωik ,w0ωik
(w0(h1)h2)
Thus, including the assignment of the monomial map m, the coordinate at vi,j is given by
vi,j = ∆ w0ωik ,wkωik
(~u) ·
1/bracehtipdownleft /bracehtipupright/bracehtipupleft /bracehtipdownright
∆ eωii ,eωii (w0(h1)h2) · ∆ w0ωik ,w0ωik
(w0(h1)h2) ·∆ wkωik ,wkωik
(w0(h3)) · ∆
wkωik
⊕ (w0(h−1
1 ))
= ∆ w0ωik ,wkωik
(~u ·w0(h3)) · ∆
wkωik
⊕ (w0(h−1
1 ))
37
In the case that h1 =h2 =h3 =e, we may ignore the frozen vertices of the quiver. The proof is completed
by appealing to the identity of [FZ99, Theorem 1.17], which s tates that when length(usi) = length(u) + 1
and length(vsi) = length(v) + 1,
∆ uωi,vωi∆ usiωi,vsiωi = ∆ usiωi,vωi ∆ vωi,usiωi +
∏
j⁄=i
∆ −aji
uωi,vωi.
This identity exactly matches the quiver mutation relation at each step of µrotTw, so each ~µCol(i) in µrot
transforms the coordinates of vi,• from
∆ cnωj,cmωj (~u)
to
∆ cn−1ωj ,cm−1ωj (~u).
Thus, after applying µrotTw the vertex vi,j has coordinate
∆ w∗
m+r−kωi∗
k
,eωi∗
k
(~u).
By Lemmas 7.1 and 7.2, ~µO1 converts the wm+r−k to wk, and ~µO2 removes the ·∗. Thus µrot changes
coordinates for u into those for h−1
2 w0(h1)−1(ΦΨ) 2(u)w0(h1)h2 as desired. □
Proof of Lemma 5.10. Since we ignored frozen vertices above, the result applies t o Q0. Since the quiver
mutation changes coordinates of α to those of rot(α), it is of order 3 and induces a graph isomorphism. □
Lemma 7.5. Item 4 of Deﬁnition 4.16 holds for arbitrary h1,h 2,h 3.
Proof. In the case that h1,h 2,h 3 are not trivial, we must verify that the equation of [FZ99, Th eorem 1.17]
still holds with the frozen vertices considered, which intr oduce factors not included in the equation. Again,
we only consider A-coordinates by Remark 2.35. We note the following:
• The vertices Bk take the place of ∆ w0ωik ,eωik
(~u) = χi∗
k ([w0−1~u]0) = χi∗
k (w0(h2h3)h1)−1 in the
equation. Therefore, they should be considered as
Bk = ∆ w0ωik ,eωik
(~u) · Ak∗
Ck
= ∆ w0ωik ,eωik
(~u ·w0(h3)) ·Ak∗.
• If, at each step of the mutation, the frozen vertices and the m onomial map m induce equal extra
factors on the ∆ usiωi,vωi∆ vωi,usiωi and∏
j⁄=i ∆ −aji
uωi,vωi terms, then the diﬀerence of the ﬁnal terms
from coordinates of ~u will also be a monomial map.
• If this ﬁnal diﬀerence monomial map matches m, the result will be proven.
• Since the extra factors at each coordinate are given by a mono mial map, each frozen vertex may be
checked individually.
For any particular group, these results may be veriﬁed by a fe w numerical calculations: to verify the
monomial identity xa1
1 · · ·xam
m
?
= xb1
1 · · ·xbm
m , taking log of both sides reduces to ∑
i log(xi)(ai −bi)
?
= 0 .
Therefore, evaluating at m + 1 linearly independent choices of vector ⟨log(xi)⟩ veriﬁes the result. This has
been carried out for the exceptional groups. The test-murot sub-program of [Gil20] may be used for this
purpose.
We present an argument that the coordinates of h1 are treated correctly by the monomial map and µrot
for type Dn; other arguments are similar.
We will ignore all terms other than h1,j =Aj, and annotate vertices with these. Half the Coxeter number
minus one will be denoted ℓ, which in the case of Dn is equal to n − 2. Then we will trace the eﬀects of
µrotTw in general. The objective is to show that, starting with the a ssignments given by the monomial factors
attached to ∆ w0ωik ,wkωik
(~u) above, we end with those factors of given by the monomial map m following
rot (i.e. the powers associated to h2 by m). Before applying any mutations, QDn is as in Figure 31. The
formula for Aj factors is, following ∆
wkωik
⊕ (w0(h−1
1 )),
at vi,j :



Aj i ≥n − 1
Aj i<n − 1,i +j <n
AjAi+j+1−n i<n − 1,i +j ≥n
at Ak :Ak, at Bk :Ak∗, at Ck : 1
38
A1A2
· · ·
Aℓ−1Aℓ
A1A2
· · ·
Aℓ−1A1Aℓ
...............
A1A2
· · ·
Aℓ−3Aℓ−1Aℓ−2Aℓ
A1A1A2
· · ·
Aℓ−2Aℓ−1Aℓ−1Aℓ
A1A2
· · ·
Aℓ−1Aℓ
A1A2
· · ·
Aℓ−1Aℓ
A1
A2
...
Aℓ−1
Aℓ
An
An−1
1
1
...
1
1
1
1
A1A2
· · ·
Aℓ−1Aℓ
An−1
An
Figure 31. QDn before any mutation.
After one iteration of ~µCol(1), by straight-forward induction the factor at vi,j matches that at vi,j+1, as
in Figure 32.
A2A2
· · ·
Aℓ−1Aℓ
A2A2
· · ·
Aℓ−1A1Aℓ
...............
A2A2
· · ·
Aℓ−3Aℓ−1Aℓ−2Aℓ
A1A2A1A2
· · ·
Aℓ−2Aℓ−1Aℓ−1Aℓ
A2A2
· · ·
Aℓ−1Aℓ
A2A2
· · ·
Aℓ−1Aℓ
A1
A2
...
Aℓ−1
Aℓ
An
An−1
1
1
...
1
1
1
1
A1A2
· · ·
Aℓ−1Aℓ
An−1
An
Figure 32. QDn after~µCol(1).
After∏ ℓ
y=1~µCol(y), this pattern continues as shown in Figure 33: for j < ℓ, we have the factor at vi,j
matching the original factor at vi,j+1. At vi,ℓ, however, the factor matches the original factor associate d to
39
Bi. Therefore, the new formula for Aj factors at vi,j is
at vi,j :



Ai∗ j =ℓ
Aj+1 j <ℓ,i ≥n − 1
Aj+1 j <ℓ,i<n − 1,i +j <n
Aj+1Ai+j+2−n j <ℓ,i<n − 1,i +j ≥n
A2A3
· · ·
AℓA1
A2A3
· · ·
A1AℓA2
...............
A2A3
· · ·
Aℓ−2AℓAℓ−1
A1A2A2A3
· · ·
Aℓ−1AℓAℓ
A2A3
· · ·
AℓAn
A2A3
· · ·
AℓAn−1
A1
A2
...
Aℓ−1
Aℓ
An
An−1
1
1
...
1
1
1
1
A1A2
· · ·
Aℓ−1Aℓ
An−1
An
Figure 33. QDn after∏ ℓ
y=1~µCol(y).
Each successive ∏ ...
y=1~µCol(y) performs the same adjustment: factors of Aj are copied from left to right.
As can be shown by induction, after ∏ k
x=1
∏ ℓ+1−x
y=1 ~µCol(y), the formula for Aj factors at vi,j is
at vi,j :



Ai∗ j >ℓ −k
Aj+k j ≤ℓ −k,i ≥n − 1
Aj+k j ≤ℓ −k,i<n − 1,i +j <n
Aj+kAi+j+1+k−n j ≤ℓ −k,i<n − 1,i +j ≥n
Thus, after applying µrotTw, each vi,j has a factor of Ai∗ attached. Since the monomial map m associates
a factor of ∆ ωi (h2) = Bi, rotation renames A• to B•, and ~µO1 renames vi,j to vi∗,j, the result is proven.
Proofs that the monomial map works correctly for factors of h2 and h3 for type D, and for all factors of
type A, B, and C, have similar forms, and the result has been numerically che cked for exceptional types.
This proves the result in all cases. □

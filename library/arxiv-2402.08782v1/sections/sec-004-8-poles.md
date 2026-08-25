---
doc_id: arxiv-2402.08782v1
doc_title: "Hecke–Farey coordinates for Bring’s surface"
section_id: sec-004-8-poles
section_title: "Poles"
section_number: 8
pages: 9-11
source_pdf: 2402.08782v1.pdf
source_sha256: 30311f0bd815f93f
doc_brief: "Hecke–Farey coordinates for Bring’s surface — The modular groupΓ (which is the Hecke groupH3) can be used to study triangular maps, Here we use the Hecke groupH4 to study the reg- ular map that"
---
In a Farey map (the caseq = 3) a pole is a vertex with a Farey coordinate of
the form a
0, wherea̸= 0. For example, in the icosahedronM3(5) the poles are 1
0
and 2
0. which from Figure 4 are the north and south poles of the icosahedron. Also,
in [4] Farey fractions were used to construct the fundamental region for the Klein
quartic. We found that 1
0 was at the centre whilst2
0 and 3
0 lie on the boundary.
This is a typical situation. The pole1
0 always lies at the centre and the other poles
lie on the boundary. In a rough sense these other poles lie at "infinity". The poles
of M4(5) are
A1 = 1
0
√
2, B1 = 2
0
√
2, C2 =
√
2
0 , H2 = 2
√
2
0 .
P3 P2
1
2
3
4
5
6
7
8
910
11
12
13
14
15
18
P1
17
P2
D1K2
E2H1 K1
2019
B2
K2
L1
I1
E1
J2
J1
F2
L1
F2
A1
G1
I1
J1
F1
P1C1
F1
K2
B2 P2
P3
P2
B2
J2
P1C1
P2B2
P3H1
P2
F2J2
P1
G1E1
P2
J2
K1P3
E2P2
P1
D1
P2
E2
F2
P3
16
P2 E2
K2
Figure 6.
9. Hecke–Farey coordinates for Bring’s surface
There are two important papers where Bring’s surface is drawn as a 20-sided
polygon with side identifications. The first of these is by G. Riera and R. E. Rodrig-
uez [9] from 1992. The second is by H. W. Braden and T. P. Northover [1], who just
used the Riera–Rodriguez diagram. This diagram is slightly clearer so we use this.
ThisisgiveninFigure6, butwithouttheHecke–Fareycoordinates G1,J 2 etc. Inthe
10 DOHA KATTAN 1 AND DAVID SINGERMAN2
diagram we also use their notation for the poles, SoP 1 =H2, P2 =B2, P3 =C2.
Otherwise we use the original notation.
Riera and Rodriguez did not give a proof that that their polygon represents
Bring’s surface. They write that the consider a Cayley diagram forS5 and embed
it into the surface but no details are given, nor did they justify the side pairings.
Our aim is to give Hecke–Farey coordinates for the vertices of the 20-sided polygon.
This will tell us how to draw the polygon and also how to find the side-pairings.
We start with a simple observation.
Lemma 9.1. The map z7→ z +
√
2 of the Hecke-Farey coordinates induces a
rotation of M4(5) through 2π/5 about the centre 1
0.
Proof. As we are working modulo 5 in inM4(5) the transformation has order
5 and fixes the centre1
0. (Here we are identifying the Hecke-Farey coordinate with
its corresponding vertex.) □
For example, consider the poleH2 = 2
√
2
0 , which we regard as the top vertex
of our 20-sided polygon (See Figure 6). AsH2 +
√
2 =H2 we find that there are 5
vertices of our polygon, labelledH2. The same applies to the poleC2. There are 5
poles with labelC2. However, as we now see, there are 10 poles with labelB1.
Definition 9.2. A Farey circuitis a collection of pointsv0,v 1,··· vn each with
a Hecke-Farey coordinate such thatvi is adjacent tovi+1 and v0 =vn.
A Farey circuit onM4(5) is given byH2,E 1,F 2,B 1,J 2,K 1,C 2,L 1,E 2,B 1,
F2,D 1,H 2 (12 vertices). For exampleH2 = 2
√
2
0 is adjacent toE1 = 2√
2 and E1 is
adjacent toF2 =
√
2
3 , etc. We continue this Farey sequence just by adding multiples
of
√
2.For example, if we add
√
2to our circuit we getH2+
√
2 =H2,E1+
√
2 =G1,
F2 +
√
2 = E2 etc., and we get another 12 vertices. We get 12 more vertices each
by adding2
√
2, 3
√
2 and 4
√
2. In this way we find Hecke-Farey coordinates for all
of the 60 boundary vertices as illustrated in Figure 6. Now in the first 12 vertices
we found that there was one pole labelledH2 = P1, one pole labelledC2 = P3
and two poles labelledB2 =P2. Thus in total there are 5 poles of the formP1, 5
poles labelledP3 and 10 poles labelledP2. Thus in total there are 20 poles on the
boundary and we regard these as the vertices of a 20-sided hyperbolic polygon. We
use the diagram in [1], where the edges are labelled1, 2,··· , 20.
In the diagram of Bring’s surface with its Hecke-Farey coordinates, each at the
20 edges has one vertex of valency 5 in its interior. For example, edge 1 hasK2
as the vertex of valency 5 in its interior. In Table 2 we just list the edges together
with these vertices.
We now just pair the sides of the polygon which have the same Hecke-Farey
coordinate. For example both side 1 and side 18 have the vertexK2 so we pair
them.
We give all the side pairings in Table 3.
We notice that ifk≡ 2 mod 4 then we pairk with k + 3, while ifk≡ 3 mod 4
then we pairk withk + 9. This is similar, but not exactly the same as in [9] or [1]
where they give their answers without proof.
HECKE–FAREY COORDINATES FOR BRING’S SURFACE 11
1↔K2 2↔B2
3↔L1 4↔I1
5↔B2 6↔J2
7↔J1 8↔H1
9↔J2 10↔F2
11↔K1 12↔L1
13↔F2 14↔E2
15↔I1 16↔J1
17↔E2 18↔K2
19↔H1 20↔K1
Table 2.
2↔ 5 6↔ 9
10↔ 13 14↔ 17
18↔ 1 3↔ 12
7↔ 16 11↔ 20
15↔ 4 19↔ 8
Table 3.

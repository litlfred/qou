---
doc_id: arxiv-0808.2716v4
doc_title: "CUSP AREAS OF F AREY MANIFOLDS"
section_id: sec-010-33-horosphere-estimate
section_title: "Horosphere estimate"
section_number: 3.3
pages: 17-20
source_pdf: 0808.2716v4.pdf
source_sha256: ea66f7ddcf9e9fe6
doc_brief: "CUSP AREAS OF F AREY MANIFOLDS — This paper gives the ﬁrst explicit, two–sided estimates on t he cusp area of once– punctured torus bundles, 4–punctured sphere bundles, and 2 –bridge link"
---
Proposition 3.6. LetM be a Farey manifold. If M is a 4–punctured sphere bundle or two–
bridge link complement, denote its meridian length by µ; if M is a punctured torus bundle,
denote its meridian length by 2µ. (See Deﬁnition 2.3.) Then every zigzag in M contains a
horosphere of diameter at least µ2/7.
Proof. Let S be a zigzag in M . As at the beginning of §3.2, let a denote the radius of the
largest face of the Ford domain of S. Call this face Fa. Rescale such that the distance
between the center of Fa and the center of the face directly to its right is 1. Call the f ace
to its right Fb, and let b denote the radius of the face Fb. The third face, which we will call
Fab, will then have radius ab, and have center distance b2 fromFb, and distance a2 fromFa,
by Lemma 3.2. Then the length µ is equal to d/h, where d is the minimal distance between
centers of faces Fa and h is the height of the maximal cusp in M .
By Lemma 3.1, a, b, and 1 satisfy the triangle inequality. Additionally, beca use Fa was
chosen to have radius larger than that of Fb and Fab, we have the following inequalities.
(1) a ≥b, and a ≥ab, hence 1 ≥b.
(2) b> −a + 1 and b>a − 1.
This forces values of a and b to lie within the region shown in Figure 7.
Label the angles of the zigzag as follows. Let θ denote the acute angle between the edges
of the zigzag of length a2 andb2. Let η denote the acute angle between edges of the zigzag of
length 1 and b2. Note this means that the angle between edges of length 1 and a2 isπ −θ +η.
By considering orthogonal projections to the edge of length b2, we ﬁnd that
(3) d2 = 1 +a4 +b4 − 2a2b2 cosθ − 2b2 cosη − 2a2 cos(π −θ +η).
See Figure 8 for an example. Note in Figure 8, the angles θ and η correspond to angles of
tetrahedra in the canonical decomposition. Because we chos e Fa to be the largest face, this
will not necessarily be the case, but two of the three angles θ,η, π −θ +η will be canonical
(or, if 2π − (π −θ +η) happens to be acute rather than π −θ +η, then exactly two of the
three angles θ, η, and 2π − (π −θ +η) will be canonical).
18 D. FUTER, E. KALF AGIANNI, AND J. PURCELL
By Lemma 3.4, and because we chose the face Fa to be largest, the largest horosphere in
the zigzag S has diameter a2/h2.
Write:
a2
h2 = a2µ2
d2 =µ2a2
d2.
We minimize the quantity a2/d2.
Note that if θ is an angle of a tetrahedron in the canonical polyhedral deco mposition of
M , then by Lemma 3.5, cos θ satisﬁes:
cosθ >1 +a4 +b4 − 2a2 − 2b2
2a2b2 .
Similarly, Lemma 3.5 implies that if η is an angle of a tetrahedron in the canonical polyhedral
decomposition of M , then cos η satisﬁes:
cosη >1 +a4 +b4 − 2a2b2 − 2a2
2b2 ,
and if π −θ +η (or 2π − (π −θ +η)) is an angle of a tetrahedron in the canonical polyhedral
decomposition, then cos(π −θ +η) satisﬁes:
cos(π −θ +η)> 1 +a4 +b4 − 2a2b2 − 2b2
2a2 .
Two of the three will be canonical. The third will not, since a ll three angles cannot be
canonical at the same time. However, we know the cosine in tha t case will be at least −1.
Hence combining the cosine inequalities above with the form ula for d2 of (3), we will have
one of the three inequalities:
(1) If θ and η are canonical:
a2
d2 > a2
6a2 + 2a2b2 + 2b2 − 1 −a4 −b4 =:f1(a,b ).
(2) If θ and π −θ +η are canonical:
a2
d2 > a2
6b2 + 2a2b2 + 2a2 − 1 −a4 −b4 =:f2(a,b ).
(3) If η and π −θ +η are canonical:
a2
d2 > a2
6a2b2 + 2b2 + 2a2 − 1 −a4 −b4 =:f3(a,b ).
0.2
0.4
0.6
0.8
1.0
b
0.2 0.4 0.6 0.8 1.0 1.2 1.4
a
1.6 1.8 2.0
Figure 7. The region of allowable values for a and b in Proposition 3.6.
CUSP AREAS OF F AREY MANIFOLDS 19
d
η
a2 a2
b2 b2
ζ 11
θθ
η
Figure 8. A zigzag. Here the dotted circles correspond to faces of the F ord
domain. Recall the corners of the zigzag are geometric duals of these faces.
Reading left to right following the zigzag, the faces of the F ord domain have
radiusa,b,ab,a,b,ab, anda. Here η andθ are angles of canonical tetrahedra.
The angle π −θ +η is not an angle of a canonical tetrahedron.
To complete the proof, we minimize all three of these functio ns in the region of Figure 7.
This is a calculus problem.
For each fj(a,b ), j = 1, 2, 3, we ﬁnd the only critical point of fj in the region of Figure
7 is the point a = 1,b = 0. For all positive a, the function fj is decreasing on the line
b =a, increasing on the line b = 1, increasing or constant on b = −a + 1, and decreasing or
constant on b = a − 1. This implies that fj takes its minimum value in the region at the
point a = 1,b = 1.
At this value, fj(1, 1) = 1/7. Hence a2/h2 ≥µ2/7. □
Remark. The proof of Proposition 3.6 does not require the zigzag S to be embedded. In
other words, the proposition applies even to the terminal pl eated surfaces S1 and Sc that
are folded in the construction of a 2–bridge link. When S is a folded surface S1 or Sc, one
of the angles θ, η, or (π −θ +η) is actually 0, hence its cosine is even larger than claimed,
which only improves the estimate.
Proposition 3.6 should be compared to previous work of Jørge nsen [34, Lemma 4.3], which
was carefully written down by Akiyoshi, Sakuma, Wada, and Ya mashita [8, Lemma 8.1.1].
After adjusting for slightly diﬀerent choices of normalizat ion, Jørgensen’s Lemma 4.3 can be
summarized as saying that, whenever a zizag of a quasifuchsi an punctured torus group is
dual to six faces of the Ford domain, one of those faces has rad ius at least
µ/(4 + 2
√
5).
It follows from Minksy’s classiﬁcation of punctured torus g roups [42], that given a punctured
torus bundle M , the Kleinian subgroup of π1(M ) that corresponds to the ﬁber can be
obtained as a geometric limit of quasifuchsian groups. As a r esult, Jørgensen’s estimate
extends to punctured torus bundles. Because a Ford domain fa ce of radius r corresponds to
a horosphere of diameter r2, Jørgensen’s Lemma 4.3 implies that every zigzag in a punctu red
torus bundle contains a horosphere of diameter at least
µ2
(4 + 2
√
5)2 ≈ µ2
71.777.
20 D. FUTER, E. KALF AGIANNI, AND J. PURCELL
Proposition 3.6, which is proved by a direct geometric argum ent without reference to quasi-
fuchsian groups, improves this estimate by a factor of about 10.25.
This improvement becomes highly signiﬁcant in Section 4. In Theorem 4.1, we estimate
the area of a maximal cusp by packing the horospherical torus with disjoint disks that are
shadows of large horospheres. As a result, a 10–fold increas e in the estimate for the diameter
of a horosphere turns into a 100–fold increase in the estimat e for the area of its shadow.
Since our applications in Sections 5 and 6 rely on these expli cit estimates for cusp area, the
100–fold improvement becomes particularly important for a pplications.

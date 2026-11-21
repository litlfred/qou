---
doc_id: arxiv-0901.1612v1
doc_title: "Triple linking numbers, ambiguous Hopf invariants and integral formulas for three-component links"
section_id: sec-004-31-an-asymmetric-version-of-the-characteristic-m
section_title: "An asymmetric version of the characteristic map"
section_number: 3.1
pages: 6-8
source_pdf: 0901.1612v1.pdf
source_sha256: b4f3efcadd1e5caf
toc_source: outline
doc_brief: "Triple linking numbers, ambiguous Hopf invariants and integral formulas for three-component links — Three-component links in the 3-dimensional sphere were classi- fied up to link homotopy by John"
duplicate_of: "deturck-melvin-gluck-komendarczyk-shonkwiler-2008-triple-lin"
---
S3 ⊂R4, let ℘x denote stereographic projection of S3 −{x} onto the 3-space R3
x
through the origin in R4 that is orthogonal to the vector x, as shown in Figure 2.
x
−x
y
z
℘xy
℘xz
R3
x
S3
(℘xy −℘xz)/∥℘xy −℘xz∥
Figure 2. Stereographic projection
6
Triple linking numbers, ambiguous Hopf invariants and integral formulas
For any (x, y, z) ∈Conf3S3, consider the points ℘xy and ℘xz in R3
x. Translation in
R3
x moves ℘xz to the origin, and then dilation in R3
x makes the translated ℘xy into a
unit vector. Composing with ℘−1
x , we see that x has been kept ﬁxed, y has moved to
the point (℘xy −℘xz)/∥℘xy −℘xz∥on the equatorial 2-sphere S2
x = S3 ∩R3
x, and z
has moved to −x, as indicated in the ﬁgure.
This procedure deﬁnes a deformation retraction
r(x, y, z) = (x , (℘xy −℘xz)/∥℘xy −℘xz∥, −x)
of Conf3S3 onto the subspace {(x, w, −x) | x • w = 0}, which is a copy of the unit
tangent bundle US3 of the 3-sphere via the correspondence (x, w, −x) ↔(x, w). Let
π : US3 →S2 denote the projection onto the ﬁber, sending (x, w) to wx−1.
Now deﬁne the asymmetric characteristic map egL : T 3 −→S2 of a link L, as
above, to be the composition π ◦r ◦eL. Noting that (℘xv)x−1 = ℘1(vx−1), we have
explicitly
egL(s, t, u) =
℘1(yx−1) −℘1(zx−1)
∥℘1(yx−1) −℘1(zx−1)∥
where x = x(s), y = y(t) and z = z(u) parametrize the components of L. This map is
easily seen to be homotopic to the characteristic map gL deﬁned above.
The restriction of egL to ∗× S1 × S1 is the negative of the Gauss map for the link
℘1((Y ∪Z)x−1), and so noting that ℘1 is orientation reversing (with the usual sign
conventions) its degree is the linking number of Y with Z. Since gL is homotopic to
egL, the same is true for gL. But then it follows from the symmetry of gL that its degree
on S1 × ∗× S1 is the linking number of X with Z, and its degree on S1 × S1 × ∗is the
linking number of X with Y . This proves the ﬁrst statement in Theorem A.
This version egL of the characteristic map will also facilitate the topological proof of
the rest of Theorem A, to be given next.
7
DeTurck, Gluck, Komendarczyk, Melvin, Shonkwiler and Vela-Vick

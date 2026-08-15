---
doc_id: arxiv-2402.08782v1
doc_title: "Hecke–Farey coordinates for Bring’s surface"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: 2402.08782v1.pdf
source_sha256: 30311f0bd815f93f
doc_brief: "Hecke–Farey coordinates for Bring’s surface — The modular groupΓ (which is the Hecke groupH3) can be used to study triangular maps, Here we use the Hecke groupH4 to study the reg- ular map that"
---
The Farey mapF, defined in section 2, is the universal triangular map, in that
every triangular map on an orientable surface is a quotient ofF by a subgroup of
the modular group, Γ and every regular triangular map is a quotient ofF by a
normal subgroup of Γ. This gives rise to many important Riemann surfaces such
as the Klein surface. In [4] we used the Farey map to study the Klein surface. In
particular we showed how the Farey structure could be used to construct the famous
14-sided fundamental polygon that represents the Klein surface. (Other Riemann
surfaces coming out of triangular maps are described in [11]). In this paper we
describe an important Riemann surface that comes from a regular 4-gonal map,
namely Bring’s surface. We now use the universal 4-gonal map and the modular
group is replaced by the Hecke groupH4. Our main result is to use Hecke-Farey
coordinates to describe the 20-sided polygon that represents Bring’s surface and
describe the side pairings needed to construct the surface. This polygon was also
given by [9] and discussed by [1] but here we provide detailed proofs that this
polygon and side pairings does indeed give Bring’s surface.
2. Bring’s surface
We start with the following result which comes from Conder and Dobcsanyi’s
classifications of regular maps of small genus [2].
Theorem 2.1. There is a unique regular map of type {5, 4} of genus 4 with
120 automorphisms. The automorphism group of this map here is the symmetric
groupS5.
Underlying this map is a unique Riemann surface of genus 4 with automorphism
group S5. This surface is calledBring’s Surface. (Type{5, 4} means that all faces
are quadrilaterrals and all vertices have valency 5.)
We let Γ(2, 5, 4) denote the triangle group with periods 2, 5, 4. This triangle
group acts as a group of conformal automorphisms of the upper-half complex plane
H and it has a presentation
1
arXiv:2402.08782v1  [math.GR]  13 Feb 2024
2 DOHA KATTAN 1 AND DAVID SINGERMAN2
Γ(2, 5, 4) =⟨X,Y,Z |X 2 =Y 5 =Z 4 =XYZ = 1⟩.
There is an epimorphismθ : Γ(2, 5, 4)7→S5 given byX7→x = (1, 5),Y 7→y =
(5, 4, 3, 2, 1), andZ7→z = (2, 3, 4, 5).
The kernelK of this epimorphism is a surface group of index 120 inΓ and so
by the Riemann-Hurwitz formulaH/K is a Riemann surface of genus 4 withS5 as
automorphism group and so by Theorem 2.1, this surface is Bring’s Surface.
As K is a normal subgroup of the triangle groupΓ(2, 5, 4), it follows from [5]
that underlying Bring’s surface there is a regular map of type{5, 4} which we
consider in more detail later.
All compact Riemann surfaces arise from compact algebraic curves. Bring’s
surface is the underlying Riemann surface ofBring’s Curve which is the complete
intersection of of the three hyper-surfaces
(2.1)
5X
i=1
xi = 0
5X
i=1
x2
i = 0
5X
i=1
x3
i = 0.
Another way of considering Bring’s Surface is in terms of the Hecke groupH4.
Consider a group with the two generatorsT :z7→z +λ and S :z7→−1
z .
Hecke showed that this group is discrete, i.e., a Fuchsian group, if and only if
(i) λ =λq = 2 cosπ
q or
(ii) λ≥ 2.
We are interested in case (i).
We then find that
R(z) =TS (z) = λqz− 1
z .
This transformation is represented by the matrix
λq −1
1 0

.
The eigenvalues of this matrix aree±πi/q and soR has periodq. It is known
that as a groupHq∼=C2∗Cq.
In this paper we are interested in the caseq = 4 and thenλ4 =
√
2. The group
H4 has two generators
T :z7→z +
√
2 and S :z7→−1
z .
Writing the Möbius transformations as matrices we find that the transforma-
tions ofH4 are of two types
(i)  a b
√
2
c
√
2 d

a,b,c,d ∈ Z, ad− 2bc = 1
and
HECKE–FAREY COORDINATES FOR BRING’S SURFACE 3
(ii)
a
√
2 b
c d
√
2

a,b,c,d ∈ Z, 2ad−bc = 1.
The matrices of type (i) form a subgroup of index 2 inH4 and are calledeven
matrices. We denote this subgroup byHe
4. The matrices of type (ii) are calledodd
matrices and they form a coset.

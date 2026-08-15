---
doc_id: 18
doc_title: "Mathematical Research Letters3, 51–60 (1996) COMBINATORIAL SCALAR CURVATURE"
section_id: sec-004-3-denote-the-vertices-of-t-by-v1v-4-and
section_title: "Denote the vertices of T by v1,...,v 4, and"
section_number: 3
pages: 1-4
source_pdf: 18.pdf
source_sha256: 0b7bf055085cb04b
doc_brief: "Mathematical Research Letters3, 51–60 (1996) COMBINATORIAL SCALAR CURVATURE — 19 sections: Introduction; These; Conformal simplices"
---
denote the edge joiningvi andvj byeij. The length ofeij shall be denoted
by lij, while the dihedral angle of eij shall be denoted by αij. The solid
angle at the vertexvi ofT shall be denoted bySi. From the Gauss-Bonnet
formula we know thatSi = ∑
j⁄=iαij −π.
We say thatT is conformal if there arer1,...,r 4 > 0 such thatl(eij)=
ri+rj. Denote the space of all conformal simplices byCT – this is a topolog-
ical space, if we require that the map ofC to R4, where we map a conformal
sequence to the radiir1,...,r 4 deﬁning it, be a homeomorphism. The col-
lection of vectors (r1,...,r 4) ∈ R4 which correspond to geometric simplices
Received October 26, 1995.
51
52 DARYL COOPER AND IGOR RIVIN
is an open set. Denote this set byCr
T . Since the set of all three-dimensional
Euclidean simplices is an open set inR6 (as parametrized by edge-lengths,
for example), it is clear that the property of conformality is rather special.
In the sequel the simplexT and all of its geometric parameters will be
viewed as functions ofr =(r1,r 2,r 3,r 4) ∈C r
T. Let
S(r)=
4∑
i=1
Siri.
The next two results form the foundation of what follows.
Lemma 1.1.
dS =
4∑
i=1
Sidri.
Proof. Let us rewrite the formula forS using the relationslij =ri +rj and
Si = ∑
j⁄=iαij −π. A short computation shows that
S =
∑
i⁄=j
lijαij −π
4∑
i=1
ri,
and thus
dS =
∑
i⁄=j
αijdlij +
∑
i⁄=j
lijdαij −π
4∑
i=1
dri.
However, by the Euclidean case of the Schl¨aﬂi diﬀerential formula, the
second sum above vanishes, and sincelij =ri +rj, the claim of the lemma
follows. □
Note. The Schl¨aﬂi diﬀerential formula (for a good exposition and proof,
see [1][Chapter 7, section 2.2.2]) states that as a simplexT (and thus any
polyhedron) varies smoothly in one of the spaces of constant curvatureHn,
Sn or En, its volume also varies smoothly, and furthermore
(1.1) Kd volT = 1
n − 1
∑
dim F =n−2
volFd αF,
where K is the curvature of the space, andαF is the dihedral angle at the
(n −2)-dimensional faceF. Note that whenK =0, the formula simply says
that the right-hand side vanishes.
COMBINATORIAL SCALAR CURVATURE 53
Lemma 1.2. The HessianH ofS is negative semi-deﬁnite – its null-space
is spanned bythe vector r.
Proof. It is clear that r is in the null-space of the Hessian, since it corre-
sponds to a rescaling of the simplex. To show that all other eigenvalues
of H are negative it is enough to show that the diagonal entries of H
are negative, while the oﬀ-diagonal elements are positive. To see this, let
(v
1,...,v 4) be an eigenvector ofH corresponding to a non-negative eigen-
value λ, and let wi = vi/ri. We want to show that wi = wj, for all i,j.
If not, assume without loss of generality that 0 <w 1 = max{wi}. Then,
(λ −H11)v1 = ∑
i>1H1ivi, so
λr1w1 −H11r1w1 =
∑
i>1
H1iriwi ≤
∑
i>1
H1iriw1,
and soλ ≤ 0, with equality if and only if all of thewi are equal.
Note now that Hij = ∂Si/∂rj. If r1,r 2,r 3 are kept ﬁxed and r4 is in-
creased,v4 is moving along a trajectoryh such that the angles between the
tangent vector toh and the edgese4i are equal (an easy consequence of the
law of cosines). Thus, the simplexT(r1,r 2,r 3,r 4 +ϵ) (whereϵ>0) strictly
contains T(r1,r 2,r 3,r 4), while sharing its base. The desired inequalities
are then clear. □
As a preview of the argument to come in the next section, we prove the
following results.
Theorem 1.3. Fix the scale of the simplices under consideration, byset-
ting
(1.2) r1 +r2 +r3 +r4 =1.
Then the regular simplex, for which ri =1 /4, is a critical point of the
function S, and furthermore, the regular simplex cannot be conformally
deformed while keeping the solid angles ﬁxed.
Proof. By Lemma 1.2, the functionS is strictly concave on the slice ofCr
T
determined by the equation 1.2. By the principle of Lagrange multipliers
and Lemma 1.1, S has a critical point subject to equation 1.2, precisely
when all of the solid angles are equal. By concavity, such a critical point
is isolated, proving the rigidity statement. □
A similar argument shows the following:
54 DARYL COOPER AND IGOR RIVIN
Theorem 1.4. A conformal simplex cannot be deformed while keeping the
solid angles ﬁxed; that is, the setCS1,S2,S3,S4 ⊂C 1 is discrete.
Proof. We have seen above that this is true for the regular simplex. To
show the theorem, we modify the functionS as follows: Let Sa1,a2,a3,a4 =
S+ ∑ airi. NowSa1,a2,a3,a4 is still strictly concave subject to the condition
1.2, but its gradient is (S1 +a1,...,S 4 +a4). Hence the critical points of
Sa1,...,a4 occurs when Si +ai = Sj +aj, for all i,j ≤ 4. This shows the
assertion of the theorem. □

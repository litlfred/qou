---
doc_id: angled-survey
doc_title: "From angled triangulations to hyperbolic structures"
section_id: sec-014-4-leadingtrailing-deformations
section_title: "Leading–trailing deformations"
section_number: 4
pages: 10-12
source_pdf: angled-survey.pdf
source_sha256: 8b49e682a39848bc
doc_brief: "From angled triangulations to hyperbolic structures — This survey paper contains an elementary exposition of Casson and Rivin’s technique for ﬁnding the hyperbolic metric on a 3–manifoldM with"
---
Given a pointp of the angle polytopeA(τ), let TpA(τ) be the tangent space
to A(τ) at the pointp. There is a particularly convenient choice of spanning vec-
tors forTpA(τ). Theseleading–trailing deformations, which were probably folklore
knowledge to experts for several years, are the main innovation in our direct proof
of Theorem 1.2. In a certain sense, they serve as a more concrete reformulation of
Neumann and Zagier’s symplectic pairing [22]. To the best of the authors’ knowl-
edge, this is the ﬁrst place where they are described in print.
Definition 4.1. Let C be a cusp torus ofM, with a tessellation by boundary
triangles coming from τ.L e t σ ⊂ C be an oriented normal closed curve (see
Deﬁnition 2.2), consisting of segmentsσ1,...σ k. Every oriented segment σi lies
in a boundary triangle Δi. We deﬁne the leading corner of Δi to be the corner
opposite the side whereσi enters Δi, and mark it with a +. We deﬁne thetrailing
corner of Δi to be the corner opposite the side whereσi leaves Δi,a n dm a r ki t
with a⊖. See Figure 3.
For every oriented segmentσi, we deﬁne a vectorw(σi) ∈ R3n, where as above
each coordinate ofR3n corresponds to one pair of opposite edges in one of then
tetrahedra. Every corner of Δi corresponds to one such edge pair in a tetrahedron.
The vectorw(σi) will have a 1 in the coordinate corresponding to the leading corner
168
Licensed to Temple Univ.  Prepared on Tue Jul 30 15:53:49 EDT 2019for download from IP 155.247.31.215.
License or copyright restrictions may apply to redistribution; see https://www.ams.org/publications/ebooks/terms
FROM ANGLED TRIANGULATIONS TO HYPERBOLIC STRUCTURES 11
+
+
+
++
+
+
+ ⊖
⊖
⊖⊖
⊖⊖
⊖
⊖
Figure 3. The leading–trailing deformation alongσ increases the
angles marked + and decreases the angles marked⊖.
of Δi,a −1 in the coordinate corresponding to the trailing corner of Δi,a n d0 ’ s
otherwise.
Finally, theleading-trailing deformationcorrespondingto σ isthevector w(σ)=∑
i w(σi).
Example 4.2. Let e be an edge of M, and suppose for simplicity that all
tetrahedra adjacenttoeare distinct. Letσ bea simple closed curve on∂M, running
counterclockwise about one endpoint ofe. The boundary triangles intersected byσ
have anglesαi,βi,γi, labeled clockwise withαi inside σ. Then the leading–trailing
deformation w(σ) adds 1 to everyβi and subtracts 1 from everyγi, keeping the
angle sum in each tetrahedron equal toπ. In addition, the dihedral angle marked
βi is adjacent to the same edge ofM as the dihedral angle markedγi+1.T h u st h e
angle sum at each edge is unchanged. (See Figure 4.) Observe thatw(σ)h a sn o
eﬀect at all on the dihedral anglesαi adjacent toe.
α1α2
α3
α3
α4 α4
α5e
+
+ +
+
+
+
+
++
+
+
⊖
⊖ ⊖
⊖⊖
⊖
⊖
⊖
⊖
⊖
⊖
Figure 4. The leading–trailing deformation about a single edgee
of M. Every increase to an angle in a tetrahedron is canceled out
by a decrease to an adjacent angle.
In the more general setting, we will prove in Lemma 4.5 that leading–trailing
deformations are always tangent toA(τ). To do that, we need a better understand-
ing of the interaction between diﬀerent deformations.
Definition 4.3. Let τ be an ideal triangulation ofM, and letρ,σ be oriented
normal closed curves on∂M that intersect transversely (if at all). Deﬁne thesigned
intersection numberι(ρ,σ) to be the number of times thatσ crosses ρ from right to
169
Licensed to Temple Univ.  Prepared on Tue Jul 30 15:53:49 EDT 2019for download from IP 155.247.31.215.
License or copyright restrictions may apply to redistribution; see https://www.ams.org/publications/ebooks/terms

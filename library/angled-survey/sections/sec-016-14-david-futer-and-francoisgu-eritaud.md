---
doc_id: angled-survey
doc_title: "From angled triangulations to hyperbolic structures"
section_id: sec-016-14-david-futer-and-francoisgu-eritaud
section_title: "DAVID FUTER AND FRANC¸OISGU ´ERITAUD"
section_number: 14
pages: 14-16
source_pdf: angled-survey.pdf
source_sha256: 8b49e682a39848bc
doc_brief: "From angled triangulations to hyperbolic structures — This survey paper contains an elementary exposition of Casson and Rivin’s technique for ﬁnding the hyperbolic metric on a 3–manifoldM with"
---
α1
α1
α2α2
α3α3
α4
α4
+
+
+
+
+
+
+
+
⊖
⊖ ⊖
⊖⊖
⊖⊖
⊖
v
Pv P′
v
Figure 6. Left: the boundary polygonPv comprised of boundary
triangles Δ1,...,Δ j adjacent tov.I ne a c hΔi, the smallest angle
is αi. Right: in the boundary polygon P′
v =Δ ′
1 ∪ ... ∪ Δ′
j,a t
the other end of the edge that starts atv, none of the total angles
along ∂P′
v change.
We conclude that for every vertexv in a boundary triangle visited byσ,t h e
polygon P′
v on the other end of the same edge will have all its external angles
unaﬀected byw(σv). Since each segmentσi of σ belongs to three diﬀerent maximal
arcs σv (corresponding to the three distinct vertices of Δi), we have∑
v w(σv)=
3w(σ). Thus, since each w(σv) does not aﬀect the holonomy ofρ “on the other
side” of the ambient tetrahedra, neither doesw(σ). This completes Step 2.
Step 3 considers the holonomy ofρ in the same boundary triangles that are
also visited byσ. Consider a maximal consecutive string of segmentsσ1,...,σ j,
contained in Δ1,...,Δ j, such that consecutive segmentsρ1,...,ρ j run through the
same boundary triangles. Depending on orientations, we can have eitherρ1 ⊂ Δ1
or ρ1 ⊂ Δj.
In the special case where Δ1 ∪... ∪Δj contains all ofσ and all ofρ,t h et w o
curves cut oﬀ exactly the same corners of boundary triangles (possibly in opposite
cyclic order). Then, since∂M is orientable, we must haveι(ρ,σ) = 0. In this case,
the angles that go into computing the angular holonomy Im(H(ρ)) are exactly the
angles that are unaﬀected byw(σ). Thus, in this special case,∂Im(H(ρ))/∂w(σ)=
0=2 ι(ρ,σ).
In the general case, we may assume thatσ and ρ do not run in parallel through
Δ1 or through Δj (otherwise, the sequence 1,...,j is not maximal). As above, it
helps to construct a polygonP by gluing Δ1 to Δ2 along their (unique) shared
edge, and so on up to Δj. By Deﬁnition 4.1, each Δi has one mark of + in the
leading corner relative toσi, and one mark of⊖in the trailing corner. Altogether,
the polygonP contains 2j markers, withj pluses andj minuses. We consider how
many of these markers are to the left and right ofρ.
If σ enters polygonP to the right ofρ and leaves to the left ofρ, the interior of
P contributes +1 toι(ρ,σ). Also, the part ofP to the left ofρ will have a surplus
of two +’s. Thusw(σ1 ∪... ∪σj) increases the angular component ofH(ρ)b y2 .
See Figure 7.
If σ enters polygonP to the left ofρ and leaves to the right ofρ, the interior of
P contributes −1t oι(ρ,σ). Also, the part ofP to the left ofρ will have a surplus
of two⊖’s. Thusw(σ1 ∪... ∪σj) increases the angular component ofH(ρ)b y−2.
172
Licensed to Temple Univ.  Prepared on Tue Jul 30 15:53:49 EDT 2019for download from IP 155.247.31.215.
License or copyright restrictions may apply to redistribution; see https://www.ams.org/publications/ebooks/terms
FROM ANGLED TRIANGULATIONS TO HYPERBOLIC STRUCTURES 15
σ
ρ
+
+
+
+
⊖
⊖
⊖
⊖
Figure 7. When σ crosses ρ from right to left, the part of the
polygon P to the left ofρ contains an excess of two +’s.
Finally, ifσ enters and leavesP on the same side ofρ, the interior ofP con-
tributes 0 toι(ρ,σ). Also, the part ofP to the left ofρ will have the same number
of +’s and⊖’s, hencew(σ1 ∪ ... ∪ σj) does not aﬀect the angular component of
H(ρ).
Summing these contributions over the (disjoint) polygons of intersection, we
conclude that∂Im(H(ρ))/∂w(σ)=2 ι(ρ,σ), as desired. □
We can now show that every leading–trailing deformationw(σ) is tangent to
A(τ).
Lemma 4.5. Let p ∈A (τ) be an angle structure, and let σ be an oriented
normal curve on a cusp ofM. Then the vectorw(σ) is tangent toA(τ).I no t h e r
words, for all suﬃciently smallε> 0, p+εw(σ) ∈A (τ).
Proof. Let us check the conditions of Deﬁnition 3.1. By condition (1) of the
deﬁnition, p lies in the open set (0,π)3n. Thus, for suﬃciently small ε,w eh a v e
p+εw(σ) ∈ (0,π)3n also.
Next, observe that in Deﬁnition 4.1, every vectorw(σi) only aﬀects a single
tetrahedron. In this tetrahedron,εw(σi) addsε to the dihedral angle on one (lead-
ing) pair of opposite edges, and adds−ε to the dihedral angle on another (trail-
ing) pair of opposite edges. Thus the deformation of angles coming fromw(σi)
keeps the angle sum equal toπ in every tetrahedron. Clearly, the same is true for
w(σ)= ∑
i w(σi).
Finally, we check condition (3) of Deﬁnition 3.1. Lete be an edge ofM,a n d
let ρ be a normal closed curve on∂M that encircles one endpoint ofe. Because
ρ is homotopically trivial, we haveι(ρ,σ) = 0. Thus, by Lemma 4.4, deforming
the dihedral angles alongw(σ) does not change the imaginary part ofH(ρ). But
Im(H(ρ)) is nothing other than the sum of dihedral angles about edgee; this sum
stays constant, equal to 2π. □
There is a convenient choice of leading–trailing deformations that will span
TpA(τ).
Proposition 4.6. For every edgeei of M,w h e r e1 ≤ i ≤ n, choose a normal
closed curve ρi about one endpoint ofei. In addition, if M has k cusps, choose
simple closed normal curvesσ1,...,σ 2k that will spanH1(∂M). Then the vectors
w(ρi) and w(σj) span the tangent spaceTpA(τ).
173
Licensed to Temple Univ.  Prepared on Tue Jul 30 15:53:49 EDT 2019for download from IP 155.247.31.215.
License or copyright restrictions may apply to redistribution; see https://www.ams.org/publications/ebooks/terms

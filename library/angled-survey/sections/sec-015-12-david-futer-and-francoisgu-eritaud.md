---
doc_id: angled-survey
doc_title: "From angled triangulations to hyperbolic structures"
section_id: sec-015-12-david-futer-and-francoisgu-eritaud
section_title: "DAVID FUTER AND FRANC¸OISGU ´ERITAUD"
section_number: 12
pages: 12-14
source_pdf: angled-survey.pdf
source_sha256: 8b49e682a39848bc
doc_brief: "From angled triangulations to hyperbolic structures — This survey paper contains an elementary exposition of Casson and Rivin’s technique for ﬁnding the hyperbolic metric on a 3–manifoldM with"
---
σσ
σ′σ′
σ′′
σ′′
⇒
⇒
⇒
Figure 5. Decomposing σ into smaller curves. Left: when two
segments ofσ pass through the same boundary triangle, we may
cut and rejoin to form two normal curvesσ′, σ′′. Right: a local
isotopy in thecomplement oftheverticesmay berequiredtoensure
that σ′, σ′′are again normal curves.
left, minus the number of times thatσ crosses ρ from left to right. This deﬁnition
has a few immediate properties:
• It is anti-symmetric:ι(ρ,σ)= −ι(σ,ρ).
• It depends only on the homology classes ofσ and ρ in H1(∂M).
• By considering a transverse pushoﬀ ofσ, one obtainsι(σ,σ)=0 .
Lemma 4.4. Let ρ,σ be oriented normal closed curves on∂M that intersect
t r a n s v e r s e l y ,i fa ta l l .T h e n
∂
∂w(σ)Im(H(ρ)) = 2ι(ρ,σ).
Recall that Im(H(ρ)) is the linear, angled part of the holonomy in Deﬁnition
2.3.
Proof. The proof involves three steps.
Step 1 introduces several simplifying assumptions with no loss of generality.
First, it will help to assume that every tetrahedronT is embedded in M (that
is, T does not meet itself along an edge or face). This assumption can always be
met by passing to a ﬁnite–sheeted cover ofM,s i n c eπ1(M) is residually ﬁnite by
Selberg’s lemma. Note that the tetrahedra, angles, boundary curves, holonomies,
and leading–trailing deformations all lift naturally to covers. This assumption also
implies that boundary triangles Δ
i,Δj meet in either at most one edge or at most
one vertex.
Next, no generality is lost by assuming thatσ passes through each boundary
triangle at most once. For, if two segmentsσi,σj run through the same boundary
triangle Δ, we may cut and rejoin the curveσ into a pair of shorter normal closed
curves σ′,σ′′. See Figure 5. (To ensure thatσ′and σ′′are normal curves, it may
be necessary to move them by isotopy in the complement of the vertices, as in the
right panel of the ﬁgure.) Note that this operation is natural and topologically
additive: we havew(σ)= w(σ
′)+ w(σ′′), andι(ρ,σ)= ι(ρ,σ′)+ ι(ρ,σ′′). Thus, if
170
Licensed to Temple Univ.  Prepared on Tue Jul 30 15:53:49 EDT 2019for download from IP 155.247.31.215.
License or copyright restrictions may apply to redistribution; see https://www.ams.org/publications/ebooks/terms
FROM ANGLED TRIANGULATIONS TO HYPERBOLIC STRUCTURES 13
we prove the lemma for each ofσ′and σ′′, the result will follow forσ.I np a r t i c u l a r ,
we may now assume thatσ is embedded.
Similarly, we may assume thatρ also passes through each boundary triangle
at most once. For, if ρi,ρj run through the same boundary triangle Δ, we may
decompose ρ i n t oap a i ro fc u r v e sρ′, ρ′′just as above. This natural operation
ensures H(ρ)= H(ρ′)+ H(ρ′′), andι(ρ,σ)= ι(ρ′,σ)+ ι(ρ′′,σ). Thus it suﬃces to
consider each ofρ′and ρ′′in place ofρ.
Given these simplifying assumptions, suppose that the segmentsσ1,...,σ k of
σ are contained in distinct boundary triangles Δ1,...,Δ k. A priori, there are two
ways in whichw(σ) could aﬀect the angular component ofH(ρ):
(1) A segment ofρ lies in the same boundary triangle Δi that contains σi.
Then, w(σi) changes the angles of Δi, thereby changing Im(H(ρ)).
(2) A segment ofρ lies in a boundary triangle Δ′
i,w h e r eΔi ⁄=Δ ′
i
are two
truncated vertices of the same ideal tetrahedron. By changing dihedral
angles in the ambient tetrahedron,w(σi) also changes the angles of Δ′
i.
We consider the eﬀect of (2) in Step 2 and the eﬀect of (1) in Step 3.
Step 2 is to show that the eﬀect ofw(σ) in the boundary triangles “on the
other side” of the ambient tetrahedra, as in (2) above, will never change Im(H(ρ)).
To see why this is true, it helps to group together boundary triangles that share a
common vertexv.
Let v be a vertex of∂M, and let σv = σ1 ∪ ... ∪ σj be a maximal union of
consecutive segments inσ, such that the ambient boundary triangles Δ1 ...,Δ j are
all adjacent tov. By our embeddedness assumption, each Δi is adjacent tov in
only one corner. Recall thatv is one endpoint of an edgee ⊂ M; we will investigate
the eﬀect ofw(σv) on boundary triangles Δ′
1,...,Δ ′
j at the other end of edgee.
The arcσv can take one of three forms:
(i) σv = σ, and forms a closed loop aboutv.
(ii) σv t a k e sar i g h tt u r ni nΔ1, followed by a sequence of left turns aboutv,
f o l l o w e db yar i g h tt u r ni nΔj.
(iii) σv takes a left turn in Δ1, followed by a sequence of right turns aboutv,
followed by a left turn in Δj.
Scenario (i) is depicted in the right panel of Figure 4. Here,v is in the interior
of a polygonPv =Δ 1 ∪... ∪Δj. Notice that none of the external angles along∂Pv
actually change, even though the shapes of constituent triangles are changing. The
same will be true in the boundary polygonP′
v =Δ ′
1 ∪... ∪Δ′
j at the other end of
e.T h u s ,i fρ passes throughP′
v, its holonomy will be unaﬀected by this change.
In Scenario (ii), we once again construct a polygonPv by gluing Δ1 to Δ2 along
their (unique) shared edge, and so on up to Δj.L e tP′
v =Δ ′
1 ∪ ... ∪ Δ′
j be the
polygon formed by the boundary triangles in the same tetrahedra, on the other end
of e. These two polygons are depicted in Figure 6. Notice that although Δi and
Δ′
i are in the same oriented similarity class (both have the same anglesαi,βi,γi,
in clockwise order), the triangles in these similarity classes are rearranged to form
P′
v.I n p a r t i c u l a r ,w(σv) does not change any of the external angles along∂P′
v,
even though the shapes of constituent triangles Δ′
i
are changing. Thus, ifρ passes
through P′
v, its holonomy will be unaﬀected.
Scenario (iii) is the mirror image of (ii). Once again,w(σv) does not change
any of the external angles along∂P′
v.
171
Licensed to Temple Univ.  Prepared on Tue Jul 30 15:53:49 EDT 2019for download from IP 155.247.31.215.
License or copyright restrictions may apply to redistribution; see https://www.ams.org/publications/ebooks/terms

---
doc_id: arxiv-1112.5179v1
doc_title: "3-Manifolds and 3d Indices"
section_id: sec-019-63-chern-simons-theory-from-6d
section_title: "Chern-Simons theory from 6d"
section_number: 6.3
pages: 65-68
source_pdf: 1112.5179v1.pdf
source_sha256: b58af08336c40994
doc_brief: "3-Manifolds and 3d Indices — We identify a large classR of three-dimensionalN = 2 superconformal ﬁeld the- ories."
---
As we argued in [19], a three-dimensional N = 2 theory TM labeled by a 3-manifold M can
be thought of as the result of compactiﬁcation of the six-dimensional (2 , 0) theory of type A1
on a 3-manifold M. Therefore, a 3d N = 2 theory TM in the space-time S1×S2 relevant
to the index computation can be equivalently approached by studying the A1 6d theory that
describes two coincident M5-branes on S1×S2×M.
This conﬁguration of two ﬁve-branes on S1×S2×M ﬁts in a large web of dualities
that connects a number of closely related systems studied in the literature. Here, we brieﬂy
discuss some of these dualities, providing a further piece of evidence for the interpretation of
3d index in terms of the full SL(2, C) Chern-Simons theory (not just a holomorphic half of
it).
In general, putting a 3d N = 2 theoryT in diﬀerent space-times with an Ω-background
allows one to associate diﬀerent quantities (partition functions) to T . Below we list several
examples of such partition functions and the corresponding 3d space-times, illustrating their
concrete form in a basic example of the tetrahedron theory T =T∆, which basically consists
– 64 –
of a single chiral multiplet:
S1×S2 : I[T∆] =
∞∏
r=0
1−qr+1z−1
1−qr¯z−1
“solid torus” S1× R2
ℏ : Zvortex[T∆] =
∞∏
r=0
(1−qr+1z−1) (6.35)
“ellipsoid” S3
b : Zb[T∆] =
∞∏
r=0
1−qr+1z−1
1− (Lq)r(Lz)−1
where, as usual, the Ω-deformation parameter is proportional to ℏ, and in the case ofS3
b there
are dual deformations proportional to ℏ = 2πib and Lℏ = 2πib−1. In all cases, z is related to
a fugacity for the ﬂavor U(1) symmetry (and Lz =z
2πi
ℏ ).
By comparing the expressions of these partition functions for T = T∆, the reader will
immediately notice that both the indexI[T ] and the ellipsoid partition functionZb[T ] roughly
contain two copies of the vortex partition function Zvortex[T ]. This observation has a simple
heuristic explanation based on the geometry of the three-dimensional space-times that lead
to these partition functions. Indeed, both a 3-sphere and S1×S2 consist of two copies of
the solid torus glued together either “back-to-back” or with a twist, i.e. in a way where the
A-cycle on the boundary torus of one copy is glued to the A-cycle on the boundary of the
second copy, or to the dual B-cycle. These two ways of gluing solid tori produce S1×S2 and
S3, respectively, which in turn lead to the partition functions (6.35).
D4
D6
S1
M
D6
Figure 13 . Upon reduction on
a circle ﬁber of S2, a conﬁgura-
tion of M5-branes wrapped on S2
becomes a system of D4-branes
stretched between two D6-branes
in type IIA string theory.
Another intuitive explanation of the relation between
diﬀerent partition functions (6.35) and Chern-Simons the-
ory with complex gauge group SL(2, C) can be seen directly
in the system of two M5-branes supported on S3
b×M or
S1×D×M, whereD =S2 leads to the superconformal index
and D = R2
ℏ leads to the vortex partition function. In each
case, it is convenient to use a dual description of this ﬁve-
brane conﬁguration by reducing it on a circle down to type
IIA string theory. There are several choices on can consider,
which depend on the choice of the “M-theory circle,” and all
of which are supposed to provide equivalent descriptions of
the same physical system. For example, if a 3-manifold M
admits a circle action, then one can ﬁnd a dual description
of the ﬁve-brane system in terms of D4-branes wrapped on
the quotient space M/U (1).
In our discussion, the 3-manifoldM is generic35 and since
the S1 part of the 3d space-time is used in the deﬁnition of
the 3d index, our only choice is to take the M-theory circle
35I.e., we do not make any special assumptions about isometries of M.
– 65 –
be a part of the D orS3 geometry. Luckily, all our 3d space-
times in (6.35) admit such circle actions (aside from obvious isometries arising from the S1
factor). In particular, the sphere D = S2 relevant for the 3d index can be represented as a
circle ﬁbration,
S1
M→ S2
↓
I
(6.36)
with two degenerate ﬁbers at the end-points of the intervalI = [0, 1]. Therefore, if we identify
the M-theory circle with S1
M, we can relate the original ﬁve-brane system on S1×S2×M
with the system of D4-branes stretched between two D6-branes, as shown in Figure 13. In
other words, the 3d index (= partition function of the ﬁve-brane theory on S1×S2×M) can
be equivalently computed in a gauge theory that lives on the world-volume of the D4-branes,
S1×I×M, (6.37)
with suitable boundary conditions associated with the D6-branes at the end-points of the
interval I. Note, upon this reduction to type IIA theory the angular momentum for the
U(1) rotation symmetry of D = S2 (similarly for D = R2) becomes the instanton charge
kinst = 1
16π2
∫
I×M TrF∧F in the D4-brane gauge theory. One quick way to see this is to note
that instantons in the D4-brane theory can be interpreted as D0-branes which, in turn, are
precisely the Kaluza-Klein modes for the reduction on S1
M.
The resulting conﬁguration of D4-branes ending on the D6-branes essentially comprises
two (interacting) copies of the D6-D4 brane system studied in [42], where it was argued that
its partition function equals the partition function of analytically continued Chern-Simons
theory, see also [8]. In the present case, we have two such systems coupled together. We
claim that these are precisely the two sectors (“holomorphic” and “anti-holomorphic”) of the
full SL(2, C) Chern-Simons theory discussed in Section 6.1.
Moreover, the coupling constants in these two sectors are related precisely as in Sec-
tion 6.1. Indeed, in a single D6-D4 brane system the coupling constant of the analytically
continuedSU (2) Chern-Simons theory is identiﬁed with the fugacity for the instanton charge
kinst. If we denote this fugacity byq =eℏ, then the fugacity of the second D6-D4 brane system
is equal to ˜q =e−ℏ =q−1 due to the opposite orientation. This is exactly the relation between
coupling constants t =−˜t = is that we encountered in Section 6.1, with the identiﬁcation
ℏ = 4π
s . In fact, we can even observe that the ρ symmetry of Section 2.4, lifted to the D6-D4
system, simply looks like a reﬂection of the geometry that exchanges the holomorphic and
anti-holomorphic sectors, and the two fugacities q and ˜q.
Acknowledgments
We would like to thank Christopher Beem, Abhijit Gadde, Daniel Green, Anton Kapustin,
Sara Pasquetti, Leonardo Rastelli, Schlomo Razamat, Nathan Seiberg, Cumrun Vafa, Roland
– 66 –
van der Veen, and Edward Witten for illuminating discussions. The work of TD is supported
primarily by the Friends of the Institute for Advanced Study, and in part by DOE grant
DE-FG02-90ER40542. The work of DG is supported in part by NSF grant PHY-0503584 and
in part by the Roger Dashen membership in the Institute for Advanced Study. The work of
SG is supported in part by DOE Grant DE-FG03-92-ER40701 and in part by NSF Grant
PHY-0757647. TD and SG thank the Simons Center for Geometry and Physics for their
hospitality during the Simons Workshop in Mathematics and Physics, 2011, where part of
this work was initiated. Opinions and conclusions expressed here are those of the authors
and do not necessarily reﬂect the views of funding agencies.

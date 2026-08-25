---
doc_id: angled-survey
doc_title: "From angled triangulations to hyperbolic structures"
section_id: sec-010-3-the-polytope-of-angle-structures
section_title: "The polytope of angle structures"
section_number: 3
pages: 7-8
source_pdf: angled-survey.pdf
source_sha256: 8b49e682a39848bc
doc_brief: "From angled triangulations to hyperbolic structures — This survey paper contains an elementary exposition of Casson and Rivin’s technique for ﬁnding the hyperbolic metric on a 3–manifoldM with"
---
As we have seen in the last section, the shape of a hyperbolic ideal tetrahedron
is completely determined by its dihedral angles. The notion of an angle structure
is that these dihedral angles should ﬁt together coherently.
Definition 3.1. An angle structure on an ideal triangulationτ is an assign-
ment of an (internal) dihedral angle to each edge of each tetrahedron, such that
opposite edges carry the same dihedral angle, and such that
(1) all angles lie in the range (0,π),
(2) around each ideal vertex of a tetrahedron, the dihedral angles sum toπ,
(3) around each edge ofM, the dihedral angles sum to 2π.
The set of all angle structures onτ is denotedA(τ).
Conditions (1) and (2) in the deﬁnition above are precisely what is needed to
specify a non-degenerate hyperbolic ideal tetrahedron up to isometry. For con-
creteness, if the three dihedral angles meeting at a vertex ofT are labeled α,β,γ
in clockwise order, then the shape parameter corresponding toα is
(3.1) z(α)= sinγ
sinβ eiα,
by the law of sines. Meanwhile, condition (3) in the deﬁnition is nothing other than
the imaginary part of the edge equation (2.3).
The notion of an angle structure can be summarized by saying that the tetra-
hedra ofτ carry genuine hyperbolic shapes, but the conditions these shapes must
satisfy are much weaker than the gluing equations. The completeness equations
are discarded entirely
1, and the real part of the edge equations is also discarded. If
we attempt to glue the metric tetrahedra coming from an angle structure, we can
encounter shearing singularitiesat the edges ofτ, as in Figure 1.
One may separate the gluing equations of Deﬁnition 2.4 into a real part and
an imaginary part. The real part of the equations is non-linear, because the shape
parameters within one tetrahedron are related in a non-linear way in equation (2.1).
On the other hand, the imaginary part of the equations is linear in the dihedral
angles, and theset ofanglestructuresA(τ)isdeﬁned byasystem oflinear equations
and strict linear inequalities. This leads to
1There is an alternative version of an angle structure, in which the angles must also satisfy
the imaginary part of the completeness equations. This corresponds to taking a linear slice of the
polytope A(τ). We will not need this version for the main part of the paper — but see Section
6.1 for variations on this theme.
165
Licensed to Temple Univ.  Prepared on Tue Jul 30 15:53:49 EDT 2019for download from IP 155.247.31.215.
License or copyright restrictions may apply to redistribution; see https://www.ams.org/publications/ebooks/terms

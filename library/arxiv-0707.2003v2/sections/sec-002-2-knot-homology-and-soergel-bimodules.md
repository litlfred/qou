---
doc_id: arxiv-0707.2003v2
doc_title: "A geometric model for Hochschild homology of Soergel bimodules BEN WEBSTER GEORDIE WILLIAMSON School of Mathematics Mathematisches Institut Institute for Advanced Study der Univers"
section_id: sec-002-2-knot-homology-and-soergel-bimodules
section_title: "Knot homology and Soergel bimodules"
section_number: 2
pages: 5-7
source_pdf: 0707.2003v2.pdf
source_sha256: 0b8fe37aabeee412
doc_brief: "A geometric model for Hochschild homology of Soergel bimodules BEN WEBSTER GEORDIE WILLIAMSON School of Mathematics Mathematisches Institut Institute for Advanced Study der Universität Freiburg — An"
---
While Soergel bimodules merit study simply by being connect ed so much de-
lightful mathematics, we have applications in knot theory i n mind, as we will
now brieﬂy describe. The interested reader can ﬁnd more detai ls in the papers
of Khovanov [Kh], Rasmussen [Ra], and Webster [We].
The braid group BG of G is a ﬁnitely presented group, with generators σs for
each simple reﬂection s∈ W , which is deﬁned by the presentation
σsσt = σtσs
(
when (st)2 = e
)
σsσtσs = σtσsσt
(
when (st)3 = e
)
(σsσt)2 = (σtσs)2 (
when (st)4 = e
)
(σsσt)3 = (σtσs)3 (
when (st)6 = e
)
Note that if G = SL( n), then Bn = BG is the standard braid group familiar
from knot theory .
There are several natural weak actions of the braid group on c ategoryO by
families of functors (see, for example, [AS, KM]), which have a n avatar on the
5
bimodule side of the picture in the form of a complex of bimodu les attached to
each braid group element. The description of these bimodule complexes can
be found in various sources, for example [Kh], or for general C oxeter groups
in [Ro].
Deﬁne the complexes of S -bimodules:
F (σs) =···−→ S[−1]−→ Rs−→ 0 −→···
F (σ−1
s ) =···−→ 0 −→ Rs−→ S[1]−→···
where the maps between non-zero spaces are the unique (up to s calar) non-
zero maps of degree 0. These maps are deﬁned by (respectively) the push-
forward and pullback in B× B -equivariant cohomology for the inclusion
֒→BsB .
Theorem 2.1 The shufﬂing complex
F (σ) = F (σǫ1
i1 )⊗S···⊗ S F (σǫm
im )
of a braid σ = σǫ1
i1··· σǫm
im (where ǫi =±1) depends up to homotopy only on σ
not its factorization. In particular,
F (σσ′) = F (σ)⊗S F (σ′),
so F deﬁnes a categoriﬁcation of BG .
The maps in this complex also have a geometric interpretatio n: each degree is
a direct sum of Bott-Samelson modules for subsequences of i, and the “matrix
coefﬁcients” of the differential between these are induced b y pullback or push-
forward maps on B× B -equivariant cohomology for inclusions Gi′→ Gi′′ of
Bott-Samelson spaces where i′ and i′′ are subsequences of i which differ by a
single index.
Even better, this complex can be used to ﬁnd a knot invariant, a s was shown
by Khovanov [Kh]. Let HH∗(R) be the Hochschild homology of R , which can
be deﬁned (using the standard equivalence between S− S -bimodules with
S⊗ Sop ) by
HHi(R) = Tor i
S⊗Sop(S, R).
This can be calculated by the Hochschild complex of S (which is often used as
a deﬁnition), or by the Koszul complex, both of which are free re solutions of S
as an S⊗ Sop -module.
In the case where G = SL(n), Hochschild homology is a categoriﬁcation of the
trace on the braid group deﬁned by Jones [Jo]. Remarkably , com bining these
creates a categoriﬁcation of knot polynomials, which had pre viously been de-
ﬁned by Khovanov and Rozansky .
6
Theorem 2.2 (Khovanov , [Kh])As a graded vector space, the homologyKR(¯σ)
of the complex HHi(F (σ)) is depends only on the knot ¯σ, and in fact, is
precisely the triply graded homology deﬁned by Khovanov and Ro zansky in
[KR].
Applying Theorem 1.2 to our remarks above, we can understand the differ-
entials of the complex HHi(F (σ)) in terms of pullback and pushforward on
B -equivariant cohomology .

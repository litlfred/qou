---
doc_id: arxiv-0812.2426v1
doc_title: "CATEGORICAL CENTERS AND RESHETIKHIN-TURAEV INVARIANTS"
section_id: sec-020-23-hopf-diagrams-for-a-precise-treatment-of-the
section_title: "Hopf diagrams. For a precise treatment of the theory of Hopf diagrams, we"
section_number: 2.3
pages: 8-10
source_pdf: 0812.2426v1.pdf
source_sha256: df1eb953bc2c6c63
doc_brief: "CATEGORICAL CENTERS AND RESHETIKHIN-TURAEV INVARIANTS — A theorem of M¨ uger asserts that the center Z(C) of a spherical k-linear category C is a modular category if k is an algebraically closed ﬁeld"
---
refer to [BV05]. Note that Habiro, shortly after us, had similar resu lts in [Hab06].
Brieﬂy speaking, a Hopf diagram is a planar diagram, with inputs but no output,
obtained by stacking the generators of Figure 1 (diagrams are rea d from bottom
to top). Examples of Hopf diagrams with 1 and 2 inputs are depicted in Figure 2.
Hopf diagrams are submitted to the relations of Figure 3 (plus relatio ns expressing
that τ is an invertible QYBE solution which is natural with respect to the othe r
generators). In particular, the relations of Figure 3 say that ∆ be haves as a co-
product with counit ε, S behaves as an antipode, ω± behaves as a Hopf pairing,
andθ± behaves as a twist form. The last two relations of Figure 3 are nothin g but
the Markov relations for pure braids.
Hopf diagrams with the same number of inputs can be composed using the
convolution product ⋆ deﬁned in Figure 4. This leads to the category Diag of Hopf
diagrams. Objects of Diag are the non-negative integers. For two non-negative
integers m and n, the set Hom Diag(m,n ) of morphisms from m to n is the empty
set if m ⁄=n and is the set of Hopf diagrams with m inputs (up to their relations)
if m =n. The composition is the convolution product and the identity of n is the
Hopf diagram obtained by juxtaposing n copies of ε.
The category Diag is a monoidal category: m ⊗n =m +n on objects and the
monoidal product D ⊗D′ of two Hopf diagrams D and D′ is the Hopf diagram
obtained by juxtaposing D on the left of D′.
Let us denote by RSL the category of ribbon string links. The objec ts of RSL
are the non-negative integers. For two non-negative integers m and n, the set of
morphisms from m to n is
HomRSL(m,n ) =
{
∅ if m ⁄=n,
RSLn if m =n,
CATEGORICAL CENTERS AND RESHETIKHIN-TURAEV INV ARIANTS 9
denoted , ,
, , , ,
, ,
PSfrag replacements , , ,
.
PSfrag replacements , ,
.
PSfrag replacements ,
.
PSfrag replacements
,
.
Figure 3. Relations on Hopf diagramsPSfrag replacements
D⋆D ′ DD D′D′
◦
Figure 4. Composition of Hopf diagrams
where RSL n denotes the set of (isotopy classes) of ribbon n-string links. The
composition T ′ ◦T of two ribbon n-string links is given by stacking T ′ on the top
of T (i.e., with ascending convention). Identities are the trivial string link s. Note
that the category RSL is a monoidal category: m ⊗n =m +n on objects and the
monoidal product T ⊗T ′ of two ribbon string links T and T ′ is the ribbon string
link obtained by juxtaposing T on the left of T ′.
Hopf diagrams give a ‘Hopf algebraic’ description of ribbon string links . Indeed,
any Hopf diagram D with n inputs gives rise to a ribbon n-string link Φ( D) in
the following way: using the rules of Figure 5, we obtain a ribbon n-handle2 hD,
2Ribbon handles are called bottom tangles in [Hab06].

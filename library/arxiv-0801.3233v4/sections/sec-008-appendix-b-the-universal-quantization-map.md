---
doc_id: arxiv-0801.3233v4
doc_title: "Contemporary Mathematics Twisted Deformation Quantization of Algebraic Varieties (Survey) Amnon Yekutieli"
section_id: sec-008-appendix-b-the-universal-quantization-map
section_title: "Appendix B. The Universal Quantization Map"
section_number: null
pages: 12-15
source_pdf: 0801.3233v4.pdf
source_sha256: d98f9d4a9ecb4c5e
doc_brief: "Contemporary Mathematics Twisted Deformation Quantization of Algebraic Varieties (Survey) Amnon Yekutieli — Let X be a smooth algebraic variety over a ﬁeld of characteristic 0."
---
LetC beasmooth K-algebra. Thereisacanonicalhomomorphismofcomplexes
of K-modules
Υ 1 :Tpoly(C)→Dpoly(C)
given by
Υ 1(∂1∧···∧∂k)(f1,...,fk) := 1
k!
∑
σ∈Sk
sgn(σ)∂σ(1)(f1)···∂σ(k)(fk)
forfi∈C and∂i∈TC. HereSk is the group of permutations. The homomorphism
Υ 1 is called theantisymmetrization mapor theHKR map, the latter because of its
similarity to the famous Hochschild-Kostant-Rosenberg Theorem. It is known that
Υ 1 is a quasi-isomorphism – see [Ko1] for theC∞case, and [Ye1] for the algebraic
case – and it induces an isomorphism of graded Lie algebras in cohomology. But
Υ 1 is not a DG Lie algebra homomorphism!
Here is the major result in the area of deformation quantization:
Theorem B.1 (Kontsevich Formality Theorem, [ Ko1], 1997) . Let C :=
K[t1,...,tn], the polynomial ring overK, and assumeR⊂K. Then Υ 1 extends to
an L∞quasi-isomorphism
Υ = {Υj}∞
j=1 :Tpoly(C)→Dpoly(C).
In other words,Υ 1 is a DG Lie algebra quasi-isomorphism, up to speciﬁed higher
homotopies Υ 2, Υ 3,.... Each of the functionsΥj is a poly diﬀerential operator, and
is invariant under linear change of coordinates inC.
There is an inducedK[[ℏ]]-multilinear L∞quasi-isomorphism
(B.2) Υ : Tpoly(C)[[ℏ]]+→Dpoly(C)[[ℏ]]+.
The next result was known in the nilpotent case, namely for artinian parameter
algebras as in Remark 1.4, at least since [Ko1]. The complete case was only proved
recently [Ye7, Theorem 0.4].
Theorem B.3(Equivalence Theorem). Let Φ : g→h be anL∞quasi-isomorphism
between DG Lie algebras. Then there is an induced bijection
MC(Φ) : MC(g[[ℏ]]+)→MC(h[[ℏ]]+),
functorial in Φ, with an explicit formula.
Combining Theorems B.1 and B.3 we ﬁnd that there is a canonical bijection
MC(Υ) : MC
(
Tpoly(C)[[ℏ]]+{ ≃
−→MC
(
Dpoly(C)[[ℏ]]+{
.
Therefore:
TWISTED DEFORMATION QUANTIZATION 13
Corollary B.4. Assume R⊂K and C = K[t1,...,tn]. Then there is a canonical
bijection of sets
quant :
{
formal Poisson brackets onC[[ℏ]]
}
gauge equivalence
≃
−→
{
star products onC[[ℏ]]
}
gauge equivalence
preserving ﬁrst order brackets.
Remark B.5. The reason we require that K contains R is because the explicit
formula of Kontsevich for the higher homotopiesΥj involves transcendental real
numbers. See discussion in [Ko2]. More recent work (based on ideas of Tamarkin,
cf. [CV2]) shows that this requirement can be avoided.
Appendix C. The L∞quasi-isomorphism of the Level of Sheaves
Here is an outline of the proof of Theorem 4.3. Details can be found in the
Erratum to [Ye1]. We assumeR⊂K, andX is a smoothn-dimensional algebraic
variety overK.
A formal coordinate system at a closed pointx ∈X is an isomorphism of
K-algebras
k(x)[[t]] =k(x)[[t1,...,tn]]
≃
−→ˆOX,x,
wherek(x) is the residue ﬁeld, andˆOX,x is the complete local ring.
There is an inﬁnite dimensional schemeCoorX, called thecoordinate bundle,
with a projectionπ: CoorX→X, which is a moduli space for formal coordinate
systems. (In [Ko1] the notation forCoorX isXcoor.) In particular, for every closed
point x∈X, thek(x)-rational points in the ﬁberπ−1(x) stand in bijection to the
set of formal coordinate systems atx.
To get an idea of how the schemeCoorX looks, let us note that CoorX =
lim←CooriX, where eachCooriX is the variety parameterizing formal coordinate
systems up to orderi.
LetPX be the sheaf of principal parts onX (a.k.a. the jet sheaf). Recall that
PX is the formal completion ofOX×X along the diagonal. As such,PX is a sheaf
of rings onX, with two ring homomorphismsOX→PX (corresponding to the two
projections X×X→X), which makePX into anOX-bimodule. When we view
PX as a leftOX-module, it has theGrothendieck connection
∇:PX→Ω 1
X⊗OXPX,
which is the completion of pullback, under the ﬁrst projectionX×X→X, of the
standard connection d :OX→Ω 1
X . The Grothendieck connection is ﬂat, and its
kernel isOX (coming from the second projection).
Let us denote byπ∗PX the pullback of the leftOX-modulePX; and letπˆ∗PX
be its adic completion. The universal property ofπ: Coor X→X implies that
there is a canonical isomorphism
(C.1) OCoorXˆ⊗K K[[t]]∼=πˆ∗PX,
of sheaves ofOCoorX-algebras on CoorX.
Like (C.1), there are canonical isomorphisms
OCoorXˆ⊗KTpoly(K[[t]])∼=πˆ∗(PX⊗OXTpoly,X)
and
OCoorXˆ⊗KDpoly(K[[t]])∼=πˆ∗(PX⊗OXDpoly,X)
14 AMNON YEKUTIELI
of graded Lie algebras onCoorX. Let us writeA := Ω CoorX, the sheaf of diﬀeren-
tial forms onCoorX; so in particularA0 =OCoorX. Then, by applyingAˆ⊗A0−,
we get canonical graded Lie algebra isomorphisms
(C.2) Aˆ⊗KTpoly(K[[t]])∼=Aˆ⊗A0πˆ∗(PX⊗OXTpoly,X)
and
(C.3) Aˆ⊗KDpoly(K[[t]])∼=Aˆ⊗A0πˆ∗(PX⊗OXDpoly,X)
on CoorX. However the diﬀerentials do not match: to compensate for the Grothen-
dieck connection on the right side, we have to add the diﬀerentialad(ω) on the left
side, whereω∈A1ˆ⊗KT 0
poly(K[[t]]) is a universal MC element.
Due to the Kontsevich Formality Theorem (Theorem B.1) we obtain an induced
A-multilinear L∞quasi-isomorphism
Υ : Aˆ⊗KTpoly(K[[t]])→Aˆ⊗KDpoly(K[[t]])
between sheaves of DG Lie algebras onCoorX. (This should be compared to the
L∞quasi-isomorphism (B.2) in the local case.) Using the isomorphisms (C.2) and
(C.3), and twisting Υ by the elementω(in the sense of [Ye3, Theorem 3.2]), we
then obtain anA-multilinear L∞quasi-isomorphism
Υω:Aˆ⊗A0πˆ∗(PX⊗OXTpoly,X)→Aˆ⊗A0πˆ∗(PX⊗OXDpoly,X).
If we had a sectionσ: X→CoorX then we could pullΥωdown to an L∞
quasi-isomorphism onX. However usually there are no global sections ofCoorX,
because of topological obstructions.
The group GLn acts on CoorX by linear change of coordinates. Let us deﬁne
LCCX to be the quotient schemeCoorX/ GLn. (“LCC” stands for “linear coordi-
nate classes”.) So the projectionπ: CoorX→X factors through LCCX. Recall
that the universal quantization of Kontsevich is invariant under linear change of
coordinates, namely under the action of the groupGLn and its Lie algebra. This
implies that theL∞morphism Υωdescends toLCCX; and hence it suﬃces to look
for sectionsσ:X→LCCX of the projectionLCCX→X.
In the C∞context such global sectionsσ: X →LCCX do exists (because
the ﬁbers of the bundleLCCX are contractible). But this is not the case in our
algebraic situation; so we must use a trick.
Let G be the group ofK-algebra automorphisms of K[[t]]. So G∼= GLn ⋉N,
where N is the subgroup of elements that act trivially modulo(t)2. The groupN
is pro-unipotent. It turns out thatCoorX is aG-torsor overX, locally trivial in
the Zariski topology.
Suppose we are given a ﬁnite number of sections
σ0,...,σq :U→LCCX
over some open setU⊂X. Using an averaging process for unipotent group actions
[Ye4], we show that there exists a morphism
σ: ∆ q
K×U→LCCX
which restricts to σj on the j-th vertex of ∆ q
K. Here ∆ q
K is the q-dimensional
geometric simplex.
TWISTED DEFORMATION QUANTIZATION 15
Figure 2. Simplicial sections,q = 1. We start with sections over
two open setsU0 and U1 in the left diagram; and we pass to a
simplicial sectionσon the right.
Since sections exist locally, we can choose an open coveringU ={Ui}of X,
with sectionsσi :Ui→LCCX. For anyi0,...,iq we then obtain a morphism
σ: ∆ q
K×(Ui0∩···∩Uiq)→LCCX.
(See Figure 2 for an illustration of the caseq = 1.) Asq varies we have asimplicial
section of the projectionLCCX→X. Details are in [Ye2].
Anotherdeviceweuseis mixed resolutions. Themixedresolution MixU(Tpoly,X)
is a sheaf of DG Lie algebras onX, depending on the coveringU, and equipped
with a DG Lie algebra quasi-isomorphism
Tpoly,X→MixU(Tpoly,X).
Likewise forDpoly,X.
The simplicial sectionσallows us to pull theL∞quasi-isomorphism Υωdown
to X, giving anL∞quasi-isomorphism
Ψσ: MixU(Tpoly,X)→MixU(Dpoly,X)
between these sheaves of DG Lie algebras onX. The dependence on U and σ
disappears when we pass to homotopy classes.

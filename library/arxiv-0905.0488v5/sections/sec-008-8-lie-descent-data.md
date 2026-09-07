---
doc_id: arxiv-0905.0488v5
doc_title: "TWISTED DEFORMATION QUANTIZATION OF ALGEBRAIC VARIETIES AMNON YEKUTIELI"
section_id: sec-008-8-lie-descent-data
section_title: "Lie Descent Data"
section_number: 8
pages: 36-39
source_pdf: 0905.0488v5.pdf
source_sha256: fcf8dee7cd3849b9
doc_brief: "TWISTED DEFORMATION QUANTIZATION OF ALGEBRAIC VARIETIES AMNON YEKUTIELI — Let X be a smooth algebraic variety over a ﬁeldK containing the real numbers."
---
We begin this section by recalling what are L∞morphisms between DG Lie
algebras, following [Ye7, Sections 7-8]; see also [Ko1, Hi2, CKTB]. We denote by
DGLie(K) the category of diﬀerential graded Lie algebras overK, and byDGCog(K)
the category of DG unital cocommutative coalgebras overK. There are functors
DGLie(K)
C
− →DGCog(K)
L
− →DGLie(K),
called the bar and cobar functors respectively. These functors are adjoint to each
other, and they have explicit formulas. The functorC is faithful. By deﬁnition an
L∞morphism Ψ : g→h between DG Lie algebrasg and h is a coalgebra homo-
morphism C(Ψ) : C( g)→C(h). In this way we get a new categoryDGLie∞(K),
with functors
DGLie(K)
inc
−−→DGLie∞(K)
C
− →DGCog(K),
the ﬁrst faithful and bijective of objects, and the second fully faithful.
The explicit formula for the functorC allows an explicit (yet cumbersome) de-
scription of L∞morphisms. An L∞morphism Ψ : g→h can be described as a
sequence Ψ = {Ψi}i≥1 of K-multilinear functions Ψi :⋀ig→h, satisfying certain
equations (see [Ko1], [Ye1, Deﬁnition 3.7], [CKTB, Section 3.7] or [Ye7, Section
7]). The homomorphism Ψ 1 : g→h is a homomorphism of DGK-modules, and it
respects the Lie brackets up to the homotopyΨ 2; and so on. Thus ifΨi = 0 for
all i≥2, then Ψ 1 : g→h is a DG Lie algebra homomorphism. AnL∞morphism
Ψ = {Ψi}i≥1 is called a quasi-isomorphism ifΨ 1 is a quasi-isomorphism.
Take a DG Lie algebrag, and let ˜g := (L◦C)(g). According to [Hi2, Propo-
sition 4.4.3(1)] the adjunction homomorphismζg : ˜g→g in DGLie(K) is a quasi-
isomorphism. Thus ifg is a quasi quantum type DG Lie algebra, then so is˜g. (Note
that even if g is quantum type, but nonzero, the DG Lie algebra˜g is unbounded
below.) Thus we have a functor
L◦C : DGLie∞(K)→DGLie(K)
sending quasi quantum type DG Lie algebras to quasi quantum type DG Lie alge-
bras.
Now suppose (S, n) is another parameter algebra, andν:R→S is a homomor-
phism of parameter algebras. There are pronilpotent DG Lie algebrasmˆ⊗g and
nˆ⊗h, an inducedR-multilinear L∞morphism νˆ⊗Ψ : mˆ⊗g→nˆ⊗h. We know
that there is an induced function
(8.1) MC(νˆ⊗Ψ) : MC( mˆ⊗g)→MC(nˆ⊗h)
between MC sets, with explicit formula
(8.2) MC(νˆ⊗Ψ)(ω) :=
∑
i≥1
1
i!Ψi(ν(ω),...,ν(ω)).
The functionMC(νˆ⊗Ψ) is functorial inΨ andν. If Ψ is anL∞quasi-isomorphism
and νis an isomorphism, then we get an induced bijection
(8.3) MC(νˆ⊗Ψ) : MC(mˆ⊗g)→MC(nˆ⊗h)
on gauge equivalence classes. See [Ye7, Theorem 4.2].
TWISTED DEFORMATION QUANTIZATION 37
Now let us suppose thatg and h are of quasi quantum type (Deﬁnition 3.1), so
that their Deligne crossed groupoids exits. IfΨ : g→h is a DG Lie homomorphism,
then there is an induced morphism of crossed groupoids
(8.4) Del(Ψ,ν) : Del(g,R )→Del(h,S ),
and this is functorial inΨ andν. Furthermore, ifΨ is a quasi-isomorphism andνis
an isomorphism, thenDel(Ψ,ν) is a weak equivalence of crossed groupoids, by [Ye7,
Theorem 0.4]. However we do not know if this is true whenΨ is anL∞morphism;
to be precise, we do not know if there is a functorDel(−,R ) from DGLie∞(K) to
CrGrpd. The best we can do is the next theorem.
Theorem 8.5. Let Ψ : g→h be an L∞morphism between quasi quantum type
DG Lie algebras, and letν: R→S be a homomorphism between parameter al-
gebras. Consider the ﬁrst diagram below. It is a diagram in DGLie(K), where
˜g := (L◦C)(g), ˜h := (L◦C)(h), ˜Ψ := (L ◦C)(Ψ), and ζg, ζh are the adjunction
morphisms. Applying Del(−,−) to it we obtain the second diagram, which is in
CrGrpd.
˜g
ζg

˜Ψ // ˜h
ζh

g h
Del(˜g,R )
Del(ζg,1R)

Del(˜Ψ,ν) // Del(˜h,S )
Del(ζh,1S)

Del(g,R ) Del( h,S )
Then the morphismsDel(ζg, 1R) and Del(ζh, 1S) in CrGrpd are weak equivalences.
If Ψ is an L∞quasi-isomorphism, and ifνis an isomorphism, thenDel( ˜Ψ,ν) is a
weak equivalence.
Proof. As already noted, the vertical arrows in the ﬁrst diagram above are quasi-
isomorphisms (this is by [Hi2, Proposition 4.4.3(1)]). According to [Ye7, Theorem
6.13] the morphismsDel(ζg, 1R) and Del(ζh, 1S) are weak equivalences.
If Ψ is anL∞quasi-isomorphism andνis an isomorphism, then by [Ye7, Lemma
7.3] the DG Lie homomorphism ˜Ψ : ˜g→˜h is a quasi-isomorphism. Again using
[Ye7, Theorem 6.13] we conclude thatDel( ˜Ψ,ν) is a weak equivalence. □
A cosimplicial DG Lie algebra, i.e. an object of∆ (DGLie(K)), is a collection
g ={gp}p∈N of DG Lie algebrasgp =⨁
i∈Z gp,i. For everyα∈∆ q
p there is a DG
Lie algebra homomorphismg(α) : gp→gq, and these homomorphisms satisfy the
simplicial relations. A cosimplicial DG Lie algebra g ={gp}p∈N is said to be of
quasi quantum type if everygp is a quasi quantum type DG Lie algebra.
A cosimplicial quasi quantum type DG Lie algebrag ={gp}p∈N and a parameter
algebraR give rise to a cosimplicial crossed groupoidDel(g,R ) =
{
Del(gp,R )
}
p∈N.
Deﬁnition 8.6.Let g be a cosimplicial quasi quantum type DG Lie algebra, and
letR be a parameter algebra, all over the ﬁeldK. A Lie descent datumin (g,R ) is
an element of the setDesc(Del(g,R )); cf. Deﬁnition 5.2.
Givenδ,δ′∈Desc(Del(g,R )), agauge transformationδ→δ′is a gauge trans-
formation of combinatorial descent data, as deﬁned in Deﬁnition 5.3.
Passing to gauge equivalence classes we get the setDesc(Del(g,R )).
Let g ={gp}p∈N be a cosimplicial quasi quantum type DG Lie algebra. In a
Lie descent datumδ= (δ0,δ1,δ2)∈Desc(Del(g,R )), the componentδ0 belongs
to MC(mˆ⊗g0). Thus there is a function Desc(Del(g,R ))→MC(mˆ⊗g0). This
function respects gauge equivalence, and we get an induced function
(8.7) Desc(Del(g,R ))→MC(mˆ⊗g0).
38 AMNON YEKUTIELI
Let g = {gp}p∈N and h = {hp}p∈N be cosimplicial quasi quantum type DG
Lie algebras. By cosimplicial L∞morphism Ψ : g →h we mean a collection
Ψ = {Ψp}p∈N of L∞morphisms Ψp : gp →hp, such that for everyα: p→q
in ∆ we have Ψq◦g(α) = h(α)◦Ψp in DGLie∞(K). This gives us a category
∆ (DGLie∞(K)). We call suchΨ a cosimplicial L∞quasi-isomorphism if eachΨp is
an L∞quasi-isomorphism.
Theorem 8.8 (Equivalence for Lie Descent). Let Ψ : g→h be a cosimplicial
L∞morphism between cosimplicial quasi quantum type DG Lie algebras, and let
ν: R →S be a homomorphism between parameter algebras. Then there is a
function
Desc(Del)(Ψ,ν) : Desc(Del(g,R ))→Desc(Del(h,S ))
with these properties.
(i) The function Desc(Del)(Ψ,ν)) is functorial inΨ and ν.
(ii) If Ψ is a morphism inDGLie(K) then Desc(Del)(Ψ,ν) = Desc(Del(Ψ,ν)),
where Del(Ψ,ν) is corresponding the morphism in∆ (CrGrpd).
(iii) The diagram
Desc(Del(g,R ))

Desc(Del)(Ψ,ν) // Desc(Del(h,S ))

MC(mˆ⊗g0)
MC(νˆ⊗Ψ) // MC(nˆ⊗h0)
with vertical arrows(8.7), commutative.
(iv) If Ψ is a cosimplicialL∞quasi-isomorphism, and ifνis an isomorphism,
then Desc(Del)(Ψ,ν) is bijective.
Please note the subtle notational distinction between Desc(Del)(Ψ,ν) and
Desc(Del(Ψ,ν)). In general (except in the situation of property (ii)) there is
no morphism of cosimplicial crossed groupoids Del(Ψ,ν), and thus the function
Desc(Del(Ψ,ν)) is not deﬁned; only the functionDesc(Del)(Ψ,ν) on equivalence
classes of descent data is deﬁned.
Proof. Applying the functorDesc to the second diagram in Theorem 8.5 we get a
diagram (the solid arrows)
(8.9) Desc(Del(˜g,R ))

Desc(Del(˜Ψ,ν)) // Desc(Del(˜h,S ))

Desc(Del(g,R ))
Desc(Del)(Ψ,ν) // Desc(Del(h,S ))
in Set. Theorem 5.6 tells us that the vertical arrows here are bijections. Hence there
is a unique functionDesc(Del)(Ψ,ν) making this diagram commutative. The func-
toriality ofDesc(Del)(Ψ,ν) in Ψ is because L◦C is a functor; and the functoriality
in νis trivial.
If Ψ is inDGLie(K) then we can add the arrowDel(Ψ,ν) into the second diagram
in Theorem 8.5, making it commutative. This proves property (ii).
Since the solid arrows in the diagram (8.9) respect the function (8.7), so does
the remaining arrow. This implies property (iii).
Finally, ifΨ happens to be anL∞quasi-isomorphism, andνis an isomorphism,
then according to Theorem 8.5 the morphism of crossed groupoidsDel( ˜Ψ,ν) is also
a weak equivalence. Hence the functionsDesc(Del(˜g,R )) and Desc(Del)(Ψ,ν) are
bijective. □
TWISTED DEFORMATION QUANTIZATION 39
Remark 8.10. If we assume that the parameter algebras in question are all ar-
tinian, then in Theorems 8.5 and 8.8 we can drop the condition that the DG Lie
algebras are quasi quantum type. See [Ye7, Theorem 6.13].
Remark 8.11. Here is a brief comparison to other work on these matters. A
special case of Theorem 8.8 is [BGNT1, Proposition 3.3.1], which only deals with
cosimplicial DG Lie quasi-isomorphisms between quantum type DG Lie algebras,
and only with artinian parameter algebras. The methods used in [BGNT1] do not
seem to be adequate for obtaining the result we need.
Getzler wrote two papers [Ge1, Ge2] on higher Deligne groupoids. Supposeg is
quantum type DG Lie algebra, andR is an artinian parameter algebra. In the ﬁrst
paper Getzler discusses the Deligne2-groupoid Del(g,R ), which is denoted there by
C(m⊗g). In the second paper he introduced a simplicial setγ·(m⊗g). A main result
of [Ge2] is that anL∞quasi-isomorphism g→h induces a homotopy equivalence
γ·(m⊗g)→γ·(m⊗h). Getzler says that the simplicial setγ·(g⊗m) “generalizes
the Deligne2-groupoid”, but this is not proved, nor even explained. For some time
we had hoped to rely on Getzler’s results for a quick proof of Theorem 8.8 (at least
for artinian parameter algebras), but we could not ﬁnd a satisfactory way to ﬁll the
gap mentioned above. This is why we eventually had to come up with Theorem
8.5.
Theorem 8.8 (for artinianR and S) is similar to [CH, Theorem 3.5]. But [CH,
Theorem 3.5] is not actually proved in that paper (there appear to be holes in the
arguments, cf. Remark 5.7). Another possible diﬃculty is that in [CH] the authors
rely on the unproved part of Getzler’s work that we mentioned above.
Here is a very recent development. The new paper [BGNT3] appears to ﬁll the
gap in [Ge2] mentioned above. According to [BGNT3, Remark 1.1], their work
implies that the simplicial setγ·(m⊗g) equals the 2-nerve of the Deligne crossed
groupoid Del(g,R ) !

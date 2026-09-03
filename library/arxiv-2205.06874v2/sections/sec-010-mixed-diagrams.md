---
doc_id: arxiv-2205.06874v2
doc_title: "State sum models with defectsbased on spherical fusion categories Catherine Meusburger Department Mathematik Friedrich-Alexander-Universität Erlangen-Nürnberg"
section_id: sec-010-mixed-diagrams
section_title: "Mixed diagrams"
section_number: null
pages: 14-17
source_pdf: 2205.06874v2.pdf
source_sha256: 9b41365160c17ab4
doc_brief: "State sum models with defectsbased on spherical fusion categories Catherine Meusburger Department Mathematik Friedrich-Alexander-Universität Erlangen-Nürnberg — We define a"
---
The diagrams for pivotal 2-categories in the previous section can be used to describe morphisms in the
pivotal 2-categoriesBimodθ(C,D) and Modθ(C) from Theorem 1.17. In this case, regions are labeled with
(bi)module categories with (bi)module traces, lines with (bi)module functors and vertices with (bi)module
natural transformations. The duals are given by adjoint functors and the pivot is the natural isomorphism
between a bimodule functor and its double adjoint.
To describe the interaction of the data inBimodθ(C,D) with data fromC andD, we generalise pivotal
2-category diagrams. We consider diagrams with additional lines and vertices labeled with data fromC and
D. These diagrams may involve crossings of lines labeled byC andD as well as crossings of such lines with
lines labeled by(C,D)-bimodule functors.
14
Definition 2.3. LetC,D be spherical fusion categories. Amixed diagramfor Bimodθ(C,D) is a diagram
obtained by superimposing a diagramD for Bimodθ(C,D) with diagramsDC forC and DD forDrev. It is
called generic if
• no vertex of any diagram is on a line or vertex of any of the others,
• each point is on at most two lines from distinct diagrams,
• each point in the interior that is on lines of two distinct diagrams is a transversal crossing.
While each diagram for Bimodθ(C,D) describes a 2-morphism in Bimodθ(C,D), a mixed diagram for
Bimodθ(C,D) can be viewed as a 2-category diagram for Cat.
For this recall from Remark 1.3 that eachC-module categoryM defines a monoidal functorF :C→ End(M)
that assigns toc∈ ObC the functorc▷− :M→M and to a morphismα :c→c′ the natural transformation
α▷− :c▷−⇒ c′▷−. Its monoidal structure is given by the coherence isomorphisms from Definition 1.2.
The monoidal functorF :C→ End(M) preserves duals. The adjoint ofc▷− :M→M isc∗▷− :M→M
with the (co)units of the adjunction given by the (co)evaluations from (1) and (3), up to coherence data:
ηc▷− =cc,c∗,−◦ (coevL
c▷−) ϵc▷− = (evL
c▷−)◦c−1
c∗,c,−
η′c▷− =cc∗,c,−◦ (coevR
c ▷−) ϵ′c▷− = (evR
c ▷−)◦c−1
c,c∗,−.
The pentagon relation(6) and triangle relation(7) allow one to suppress bracketings and action of the unit
object in expressions involving multiple action functors. They lead to strictification and coherence theorems
for module categories that generalise the ones for monoidal categories, see [EGNO, Rem. 7.2.4].
One can therefore interpret diagrams forC as 2-category diagrams for Cat, whose regions are labeled by
aC-module categoryM and whose lines by action functorsc▷− for c∈ ObC. Vertices are labeled by
natural transformations that are composites of natural transformationsα▷− for morphismsα inC with the
coherence isomorphismsc and γ. The result is a natural transformation between the endofunctors given by
the objects at the top and bottom of the diagrams. It is unique up to coherence data.
Analogous statements hold forD-right module categoriesM. The only difference is that the action is a right
action and one has an associated monoidal functorF :Drev→ End(M), whose coherence data is given by
the natural isomorphismsd−,i,j : (−◁i)◁j⇒− ◁ (i⊗j) and δ :−◁e⇒ idM from Definition 1.2.
In this way, one can interpret any mixed diagram forBimodθ(C,D) without crossingsas a 2-category diagram
for Cat in which the objects and morphisms fromC andD are replaced by the associated action functors and
natural transformations for the bimodule category labeling their region in the diagram.
Crossings of lines labeled byc∈ ObC andd∈ ObD and crossings of such lines with lines labeled by (bi)module
functors F also have a direct interpretation. The former correspond to the natural isomorphismsbc,−,d from
Definition 1.2 and the latter to the natural isomorphismssF and tF from Definition 1.8. We represent them
as over- and undercrossings.
Definition 2.4. LetD′ be a generic mixed diagram forBimodθ(C,D) that superimposes diagramsD, DC
and DD. The 2-category diagram associated toD′ is the diagram obtained by
• replacing labelsc∈ ObC, d∈ ObD in a region labeledM with c▷− :M→M ,−◁d :M→M ,
• replacing morphism labelsα and β fromC andD by natural transformations composed ofα▷− and
−◁β and the coherence isomorphismsc,γ and d,δ from Definition 1.2,
• transforming crossings of a line fromDC with a line fromD or DD into overcrossings of the line from
DC and crossings of a line fromD with a line fromDD into overcrossings of the line fromD,
• labeling the crossing points with natural transformations as follows:
– crossings of a line labeled byc∈ ObC with a line labeled byd∈ ObD by the natural isomorphism
bc,−,d : (c▷−)◁d⇒c▷ (−◁d) and its inverse from Definition 1.2
d c dc
(36)
bc,−,d : (c▷−)◁d⇒c▷ (−◁d) b−1
c,−,d :c▷ (−◁d)⇒ (c▷−)◁d,
15
– crossings of a line labeled byc∈ ObC with a line fromD labeledF by the natural isomorphism
sF :F (c▷−)⇒c▷F (−) and its inverse from Definition 1.8
F c Fc
(37)
sF
c,− :F (c▷−)⇒c▷F (−) sF−1
c,− :c▷F (−)⇒F (c▷−),
– crossings of a line labeled byd∈ ObD with a line fromD labeledF by the natural isomorphism
tF :F (−)◁d⇒F (−◁d) and its inverse from Definition 1.8
d F dF
(38)
tF
−,d :F (−)◁d⇒F (−◁d) tF−1
−,d :F (−◁d)⇒F (−)◁d.
In this way, every generic mixed diagram defines a 2-category diagram for Cat that represents a unique
natural transformation between the composites of the functors at the top and bottom of the diagram.
Definition 2.5. The evaluation of a generic mixed diagram forBimodθ(C,D) is the natural transformation
represented by the associated 2-category diagram.
The properties of the coherence isomorphisms associated to crossing points allow one to define the evaluation of
non-generic mixed diagrams. The invertibility of the isomorphismsb, sF andtF translates into diagrammatic
identities that are an analogue of the Reidemeister 2 move for a braid diagram
d c
=
d c dc
=
dc F c
=
F c Fc
=
Fc d F
=
d F dF
=
dF
(39)
Similarly, the hexagon relation(17) for a (C,D)-bimodule functor translates into a diagrammatic identity
that is an analogue of the Reidemeister 3 move for a braid diagram
dF c
=
dF c
(40)
The naturality conditions from Definitions 1.2 and 1.8 and the conditions on a bimodule natural transformation
from (18) and (19) allow one to slide vertices under or over crossings. The naturality of the isomorphisms
bc,d,m : (c▷m)◁d→c▷ (m◁d) in c and d is expressed as
d c
c′
α
=
d c
c′
α
d
d′
c
β =
d
d′
c
β
(41)
The naturality ofsF
c,m :F (c▷m)→c▷F (m) and tF
m,d :F (m)◁d→F (m◁d) in c and d implies
F c
c′
α
=
F c
c′
α
d
d′
F
β =
d
d′
F
β
(42)
16
The defining conditions(18) and (19) on aC-module andD-right module natural transformationν :F⇒G
give the diagrammatic identities
F
G
c
ν
=
F
G
c
ν
d F
G
ν
=
d F
G
ν
(43)
In particular, identities(41) and (42) can be applied to the (co)evaluations for the duals inC andD. This
allows one to slide maxima and minima of lines labeled with objects inC andD over or under lines labeled
with bimodule functors. Similarly, the (co)evaluations for 1-morphisms inBimodθ(C,D) are (C,D)-bimodule
natural transformations and hence satisfy identity(43). This allows one to slide maxima and minima of lines
labeled with bimodule functors over or under lines labeled with objects fromC orD.
Note that the diagrammatic identities involving only lines and vertices labeled byC andD are special
cases of the ones involving data from Bimodθ(C,D). The diagrams (36) for the natural isomorphism
bc,−,d : (c▷−)◁d⇒c▷(−◁d) are just the diagrams(37) and (38) for theC-module functor−◁d :M→M
and theD-right module functorc▷− :M→M . The identities (41) are a special case of (42) and (43).
The diagrammatic identities(39) to (43) allow one to define the evaluation of non-generic mixed diagrams.
Any point of a mixed diagram that lies on more than two lines from distinct diagrams is on three lines, one
from each diagramD,DC and DD. By slightly displacing the lines one can transform such a triple point
into multiple crossings of two lines. The diagrammatic identities for the crossings and their inverses and the
identity (40) ensures that all diagrams obtained in this way have the same evaluation.
Similarly, if there is a point on two lines from different diagrams that is not a transversal crossing, then
by slightly displacing the lines one can either create a double crossing or ensure that the lines do not meet.
Identities (39) ensure that all resulting diagrams have the same evaluations. Any vertex on two lines from
different diagrams can be displaced slightly from the crossing. Identities(41), (42) and (43) ensure that all
ways of doing so yield diagrams with the same evaluation.
Definition 2.6. The evaluation of a mixed diagram forBimodθ(C,D) is defined as the evaluation of any
generic mixed diagram obtained by slightly displacing the lines and vertices of the diagram.

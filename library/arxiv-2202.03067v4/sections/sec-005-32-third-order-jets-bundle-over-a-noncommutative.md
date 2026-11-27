---
doc_id: arxiv-2202.03067v4
doc_title: "QUANTUM JET BUNDLES"
section_id: sec-005-32-third-order-jets-bundle-over-a-noncommutative
section_title: "Third order jets bundle over a noncommutative algebra"
section_number: 3.2
pages: 8-13
source_pdf: 2202.03067v4.pdf
source_sha256: 22cf51d9d54ff681
toc_source: outline
doc_brief: "QUANTUM JET BUNDLES — We formulate a notion of jet bundles over a possibly noncommutative algebra A equipped with a torsion free connection."
---
A
which is considerably more involved than J 1
A, J 2
A, and will lay the groundwork for the general
case. Here we have to make further assumptions, which we will illustrate and motivate during
this subsection. These are presented in Fig. 1 using the diagrammatic notion where maps are
read downwards, as discussed at the end of Section 2. Recall that we denoted the wedge product
by a join, ∇by a splitting and its associated σ by a braid crossing.
From now on, we will use the notation ∧i,σi for the wedge product and braiding respectively
applied to the i,i + 1 tensor factors of Ω 1⊗A Ω1⊗A Ω1. We deﬁne sub-module of quantum sym-
metric 3-forms as Ω3
S = ker∧1∩ker∧2, the joint kernel of Ω 1⊗A Ω1⊗A Ω1 by applying ∧in the
adjacent places. We continue with a torsion free ∇∶Ω1→Ω1⊗A Ω1 as needed for J 2
A and now
denote by
∇2∶Ω1⊗
A
Ω1→Ω1⊗
A
Ω1⊗
A
Ω1, ∇2 = (∇⊗id)+σ1(id⊗∇)
the tensor product connection on Ω 1⊗A Ω1, with braiding
σ∇2∶Ω1⊗
A
Ω1⊗
A
Ω1→Ω1⊗
A
Ω1⊗
A
Ω1, σ ∇2 =σ1σ2.
The 3rd-order jet bimodule and jet prolongation bimodule map will be deﬁned as
J 3
A =A⊕Ω1⊕Ω2
S⊕Ω3
S, j 3(s) =s+ ds+∇ds+∇2∇ds
for certain bimodule bullet actions ●3 to be determined.
QUANTUM JET BUNDLES 9
=d
∇
∇
∧
(b)
∇
(f)
d
d
− = ∇
∧
∇
∧
+
(g)
=
axioms.pdf
(e) ∇− ∇
∇ = − ∇
(a)
d=∇
∧
=−∧ ∧
(c)
+ = ∇Ω2
∧
∇
∧
∇
∧
∧
=
∧σΩ2
(d)
=
∧
∧
σΩ1,Ω2
Figure 1. Conditions for the connection ∇: (a) torsion-free and its conse-
quence, (b) ﬂat, (c) ∧-compatibility and its consequence, (d) extendability (e)
Leibniz compatibility ∇2σ1 = σ2∇2 in Lemma 3.5, which with (a), (d) implies
condition (f) in Lemma 3.4 for the curvature to be a bimodule map. It also
implies the Yang-Baxter or braid relations (g).
We ﬁrst analyse the conditions for the proposed j3 to land in the right place, namely that
∇2∇ds ∈Ω3
S. For this we need ﬂatness and the ∧-compatibility condition as shown in Fig. 1(b)
and 1(c) respectively.
Lemma 3.3. Suppose that ∇is torsion free, ﬂat and ∧-compatible in the sense that
∇Ω2(η∧ω)∶= (∇η)∧ω+∧2σ1(η⊗∇ω)
for all η,ω ∈Ω1 is a well-deﬁned bimodule connection on Ω2. Then ∇2 restricts to a bimodule
connection on Ω2
S and ∇2∇ds∈Ω3
S for all s∈A.
Proof. For wedge acting on the ﬁrst factors, we have
∧1∇2∇ω =∧1(∇⊗id+σ1(id⊗∇))∇ω = (∧∇⊗id+∧1σ1(id⊗∇))∇ω
= (d⊗id−∧1(id⊗∇))∇ω = (d⊗id−(id∧∇))∇ω =R∇(ω) = 0,
where we used ∧∇= d, im(id+σ) ⊆ker∧and that the curvature R∇of ∇vanishes. We actually
only needed R∇ds= 0, but since R∇is a left module map, this is equivalent. For ∧to vanish in
the second position, we have
∧2∇2∇ω =∧2(∇⊗id+σ1(id⊗∇))∇ω =∇Ω2(∧∇ω) =∇Ω2dω,
since ∇is assumed to be ∧-compatible and torsion free. This vanishes if ω = ds. In fact, we have
proven the stronger property
(2) ∧2∇2(Ω2
S) = 0
so that ∇2 restricts to ∇Ω2
S
∶Ω2
S→Ω1⊗A Ω2
S as also required. It is shown in [4, p. 575] that (2)
holds iﬀ ∇is ∧-compatible, i.e. the converse is also true. □
The ∧-compatibility condition used in Lemma 3.3 also entails the existence of a braiding for
∇Ω2, which is necessarily given by
σΩ2 ∶Ω2⊗
A
Ω1→Ω1⊗
A
Ω2, σ Ω2(ω∧η⊗ζ) =∧2σ1σ2(ω⊗η⊗ζ)
10 SHAHN MAJID AND FRANCISCO SIM ˜AO
as shown in Fig. 1(c).
Next, we will need the notion that ∇is extendable [4, Def. 4.10] in the sense that σ extends
to a well deﬁned bimodule map
σΩ1,Ω2 ∶Ω1⊗
A
Ω2→Ω2⊗
A
Ω1, σ Ω1,Ω2(ω⊗η∧ζ) =∧1σ2σ1(ω⊗η⊗ζ)
for allω,η,ζ ∈Ω1. This is shown in Fig. 1(d) and restores a certain symmetry to our assumptions.
It is also motivated geometrically as part of the conditions for an object in the monoidal category
AGA in [4], which consists of bimodules with extendable connections of which the curvatures are
bimodule maps.
Lemma 3.4. An extendable connection ∇on Ω1 has curvature a bimodule map iﬀ the condition
in Fig. 1(f) holds. In this case the curvature of ∇2 is
R∇2 =R∇⊗id+(σΩ1,Ω2⊗id)(id⊗R∇).
Proof. For the ﬁrst part, the operator (d⊗id−id∧ ∇) is a left module map as ∇is a left
connection, which in turn makes R∇a left module map as is well-known, using d 2 = 0. On the
other side
R∇(ωa) = (d⊗id−∧1∇)((∇ω)a+σ(ω⊗da))
=R∇(ω)a−∧1(id⊗σ)(∇ω⊗da)+(d⊗
A
id−∧1∇)σ(ω⊗da)
for all ω ∈Ω1 anda∈A. So we have a bimodule map iﬀ Fig. 1(f) holds when applied to ω⊗A da,
since d 2a = 0. Writing C(ω,η ) for the left minus the right side of (f), it is easy to see from
∇a bimodule connection, the graded Leibniz rule for d, and extendability in Fig. 1(d) that
C(ω,aη ) =C(ωa,η ) for all a∈A. Hence if C(ω, db) = 0 for all b,ω then C(ω,a db) = 0 and hence
C(ω,η ) = 0 for all ω,η ∈Ω1. One can similarly prove that C(ω,ηa ) =C(ω,η )a and more easily
thatC(aω,η ) =aC(ω,η ). Hence the condition actually makes sense as the vanishing of a certain
bimodule map from Ω 1⊗A Ω1 to itself. The last part is a special case of the proof in [6, 4] that
AGA has tensor products, so we omit details. □
We are mainly interested in the case of zero curvature R∇= 0 in view of Lemma 3.3, and zero
is a bimodule map so the above will also ensure that ∇2 is ﬂat. It also means that the stated
diagram (f) must hold in the ﬂat extendable case. It will be useful, however, whether or not
the connection is ﬂat, to impose a novel condition, shown in Fig. 1(e), which in the torsion free
extendable case implies (f). To further understand its signiﬁcance, we note that the ‘braided
integer’ and ‘co-braided integer’ maps on (Ω1)⊗A 3 restrict to
[3,σ]∶= id+σ2+σ1σ2∶Ω2
S⊗
A
Ω1→Ω3
S, [3,σ]′∶= id+σ1+σ2σ1∶Ω1⊗
A
Ω2
S→Ω3
S(3)
where the indices on σ refer to the position. That [3,σ],[3,σ]′land in the right place as shown
assumes that the ∧-compatibility and extendability in Fig. 1(c),(d) hold. We also note that
(4) [3,σ]([2,σ]⊗id) = [3,σ]′(id⊗[2,σ])
holds if and only if the Yang-Baxter or braid relations shown in Fig. 1(g) holds. The proof is
just a matter of writing out both sides as 6 terms and comparing. This is part of the theory of
Hopf algebras in braided categories but applied now in the category of A-bimodules with tensor
product over A.
Lemma 3.5. Let ∇be a bimodule connection on Ω1. The 3rd-order Leibniz rule
∇2∇d(ab) = (∇2∇da)b+[3,σ](∇da⊗db)+[3,σ]′(da⊗∇db)+a(∇2∇db)
QUANTUM JET BUNDLES 11
holds for all a,b ∈A if and only if the Leibniz-compatibility condition ∇2σ1 =σ2∇2 in Fig. 1(e)
holds. In this case, σ obeys the braid relations and if ∇is torsion free and extendable then R∇
is a bimodule map.
Proof. Computing the left hand side using d(ab) = (da)b+adb and the iterated Leibniz properties
of ∇and ∇2, and comparing, equality of the stated 3rd-order Leibniz rule needs
[3,σ](∇da⊗db) =σ∇2(∇da⊗db)−σ1(da⊗∇db)−σ2σ1(da⊗∇db)+∇2[2,σ](da⊗db).
Dissecting [3,σ] and∇2 and cancelling terms requires the condition in Fig. 1(e). More precisely,
if we write C(ω,η ) =∇2σ1(ω⊗η)−σ2∇2(ω⊗η) for the left hand side minus the right hand side,
we need C(da, db) to vanish. But by the Leibniz properties of a connection, one can see that
C ∶Ω1⊗A 2→Ω1⊗A 3 is a well-deﬁned left module map. It follows that its vanishing on d a, db
is equivalent to its vanishing on all ω,η . In fact, the map C =∇ ∇(σ) is the covariant derivative
of σ in the notation of [4] and as such is a right module map iﬀ σ intertwines the braiding
before and after σ by [4, p302], which is iﬀ the braid-relations (g) given that the braiding on
the bimodule Ω 1⊗A Ω1 is itself σ1σ2. Moreover, zero is a right module map, hence condition (e)
implies (g). Also, applying ∧1 to the condition (e) in the torsion free case extendable case gives
the condition (f) and we then use Lemma 3.4. Incidentally, applying instead ∧2 gives something
which is automatic in the ∧-compatible case, i.e. a weaker form of ∧-compatibility. □
With these preliminary observations, we are now ready to state and prove our main result of
this section.
Theorem 3.6. (Construction of J 3
A). Let ∇be torsion free, ﬂat, ∧-compatible, extendable and
Leibniz-compatible. Then
a●3s=a●2s+(∇2∇da)s, s ●3a=s●2a+s(∇2∇da),
a●3ω =a●2ω+[3,σ](∇da⊗ω), ω ●3a=ω●2a+[3,σ]′(ω⊗∇da),
a●3 (ω1⊗ω2) =a●2 (ω1⊗ω2)+[3,σ]′(da⊗ω1⊗ω2), (ω1⊗ω2)●3a= (ω1⊗ω2)●2a+[3,σ](ω1⊗ω2⊗da),
a●3 (ω1⊗ω2⊗ω3) =aω1⊗ω2⊗ω3, (ω1⊗ω2⊗ω3)●3a=ω1⊗ω2⊗ω3a
for s∈A, ω ∈Ω1, ω1⊗ω2 ∈Ω2
S and ω1⊗ω2⊗ω3 ∈Ω3
S, makes J 3
A a bimodule and j3 a bimodule
map. Quotienting out Ω3
S gives a bimodule surjection π3∶J 3
A→J 2
A such that π3○j3 =j2.
Proof. (1) All the stated action maps land in one of the components Ω i
S of J 3
A given Lemma 3.3
and given where the [3,σ] and [3,σ]′land.
(2) We check that we indeed have an action when acting on each degree. On degree 0,
a●3 (b●3s) =a●3 (b●2s+(∇2∇db)s)
=a●2 (b●2s)+(∇2∇da)bs+[3,σ](∇da⊗(db)s)+[3,σ]′(da⊗(∇db)s)+a(∇2∇db)s
where we decompose b●2s=bs+(db)s+(∇db)s, apply the stated a●3 and recombine all the a●2
parts of these as the ﬁrst term of the result. The next three terms are the other terms from a●3
in this process. For this to equal (ab)●3s, we need the 3rd-order Leibniz rule in Lemma 3.5.
Next, on degree 1, we have
a●3 (b●3ω) =a●3 (b●2ω+[3,σ](∇db⊗ω))
=a●2 (b●2ω)+[3,σ](∇da⊗bω)+[3,σ]′(da⊗[2,σ](db⊗ω))+[3,σ](a∇db⊗ω),
(ab)●3ω = (ab)●2ω+[3,σ](a∇db+ da⊗db+(∇da)b+σ(da⊗db)⊗ω)
where for the second equality we decomposed b●2ω = bω+ [2,σ](db⊗ω), applied a●3 to each
term and then recombined the a●2 parts of these. For the last equality, we used the Leibniz
12 SHAHN MAJID AND FRANCISCO SIM ˜AO
properties on ab. For these expressions to be equal, we need the braid relations (g) according to
equation (4), but these are implied by Leibniz compatibility.
On degree 2, we have
a●3 (b●3 (ω1⊗ω2)) =a●3 (b●2 (ω1⊗ω2)+[3,σ]′(db⊗ω1⊗ω2))
=a●2 (b●2 (ω1⊗ω2)+[3,σ]′(da⊗bω1⊗ω2)+a[3,σ]′(db⊗ω1⊗ω2)
= (ab)●2 (ω1⊗ω2)+[3,σ]′((( da)b+adb)⊗ω1⊗ω2) = (ab)●3 (ω1⊗ω2)
without further conditions needed. The action on degree 3 works automatically also.
(3) The right actions work the same way without further conditions being needed. For exam-
ple, on degree 0 we again need Lemma 3.5.
(4) Now we check that these actions commute, so that we have a bimodule. On degree 0,
(a●3s)●3b= (a●2s+(∇2∇da)s)●3b
= (a●2s)●2b+as∇2∇db+[3,σ]′((da)s⊗∇db)+[3,σ]((∇da)s⊗db)+(∇2∇da)sb,
a●3 (s●3b) =a●3 (s●2b+s∇2∇db)
=a●2 (s●2b)+(∇2∇da)sb+[3,σ](∇da⊗sdb)+[3,σ]′(da⊗s∇db)+as∇2∇db
by the same method as above, i.e. decomposing a●2s, s●2b, applying the other ●3 and recom-
bining. Comparing, we see that these are equal without further conditions needed.
On degree 1, we have
(a●3ω)●3b= (a●2ω+[3,σ](∇da⊗ω))●3b
= (a●2ω)●2b+[3,σ]′(aω⊗∇db)+[3,σ]([2,σ](da⊗ω)⊗db)+[3,σ](∇da⊗ωb),
a●3 (ω●3b) =a●3 (ω●2b+[3,σ]′(ω⊗∇db))
=a●2 (ω●2b)+[3,σ](∇da⊗ωb)+[3,σ]′(da⊗[2,σ](ω⊗db))+[3,σ]′(aω⊗∇db)
by the same method as before. For these expressions to be equal, we need the braid relations (g)
according to equation (4).
Similarly on degree 2,
(a●3 (ω1⊗ω2))●3b= (a●2 (ω1⊗ω2))●3b+[3,σ]′(da⊗ω1⊗ω2)b
=aω1⊗ω2b+[3,σ](aω1⊗ω2⊗db)+[3,σ]′(da⊗ω1⊗ω2b)
=a●3 ((ω1⊗ω2)●2b)+[3,σ](aω1⊗ω2⊗db) =a●3 ((ω1⊗ω2)●3b)
without further conditions needed. The bimodule property on degree 3 works automatically also.
(5) Finally, it remains to check that j3 is a bimodule map (in fact, the stated ●3 action was
discovered by reverse-engineering this requirement). Similarly to the methods above, we have
j3(as) =j2(as)+∇2∇d(as)
=a●2j2(s)+(∇2∇da)s+[3,σ](∇da⊗ds)+[3,σ]′(da⊗∇ds)+a∇3∇ds
=a●3 (j2(s)+∇2∇ds) =a●3j3(s)
precisely by the ∇2∇d Leibniz property in Lemma 3.5. Similarly for the action from the other
side. The properties of π3 are clear and imply that π1○π2○π3 splits j3 given that π1○π2 split
j2 in Proposition 3.1. □
We are in fact forced to the above ●3 actions by the requirement for j3 to be a bimodule map
and an assumption that the actions factor through the iterated derivatives of a. This then lays
the groundwork for the general case.
QUANTUM JET BUNDLES 13

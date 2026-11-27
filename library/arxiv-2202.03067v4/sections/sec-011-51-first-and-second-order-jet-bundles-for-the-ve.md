---
doc_id: arxiv-2202.03067v4
doc_title: "QUANTUM JET BUNDLES"
section_id: sec-011-51-first-and-second-order-jet-bundles-for-the-ve
section_title: "First and second order jet bundles for the vector bundle case"
section_number: 5.1
pages: 22-25
source_pdf: 2202.03067v4.pdf
source_sha256: 22cf51d9d54ff681
toc_source: outline
doc_brief: "QUANTUM JET BUNDLES — We formulate a notion of jet bundles over a possibly noncommutative algebra A equipped with a torsion free connection."
---
bimodule. For the split jet bundle we will also need a bimodule connection ∇E,σE as discussed,
but for the bimodule structure in the case of the ﬁrst-order jet bimodule, we need only σE.
Proposition 5.1. LetσE ∶E⊗A Ω1→Ω1⊗AE be a bimodule map, and a∈A,s ∈E, ω ∈Ω1.
(1) The actions
a●1s=as+ da⊗s, s ●1a=sa+σE(s⊗da),
a●1 (ω⊗s) =aω⊗s, (ω⊗s)●1a=ω⊗sa
make J 1
E =E⊕Ω1⊗AE a bimodule and
0→Ω1⊗
A
E→J 1
E→E→0
(where we quotient out the Ω1⊗AE part) an exact sequence of bimodules.
(2) Bimodule map splittings j1
E of this exact sequence are in 1-1 correspondence with bimodule
connections∇E with generalised braiding σE and take the form
j1
E∶E→Ω1⊗
A
E, j 1
E(s) =s+∇Es.
Proof. (1) We ﬁrst check the bimodule structure. For a,b ∈A, we have
a●1 (b●1s) =a●1 (bs+ db⊗s) =abs+ da⊗bs+adb⊗s= (ab)s+ d(ab)⊗s= (ab)●1s,
(s●1a)●1b= (sa+σE(s⊗da))●1b=sab+σE(sa⊗db)+σE(s⊗da)b=s(ab)+σE(s⊗d(ab)) =s●1 (ab),
(a●1s)●1b= (as+ da⊗s)●1b=asb+σE(as⊗db)+ da⊗sb=a●1 (sb+σE(s⊗db)) =a●1 (s●1b).
These properties for the action on ω⊗s are immediate as the product ●1 is simply given by left
or right multiplication by a ∈A. It is immediate from the form of the bimodule structure that
the map π1∶J 1
E→E setting Ω1⊗AE to zero part a bimodule map and gives the exact sequence
stated.
(2) If we are give ∇E then we deﬁne j1
E as stated with j1
E(s) ∈E⊕Ω1⊗AE = J 1
E as ∇Es ∈
Ω1⊗AE. We check that j1
E is a bimodule map
j1
E(as) =as+∇E(as) =as+ da⊗s+a∇Es=a●1 (s+∇Es) =a●1j1
E(s),
j1
E(sa) =sa+∇E(sa) =sa+∇E(s)a+σE(s⊗da) = (s+∇Es)●1a=j1
E(a)●1a.
Conversely, given a splitting j1
E∶E→J 1
E means π1○j1
E = id, so j1
E(s) =s+∇Es for some map
∇E∶E→Ω1
E. Reversing the proof that j1
E is a bimodule map immediately gives that ∇E is a
bimodule connection. □
It should be noted that at k = 1, this construction is independent of the choice of connec-
tion (∇E,σE). Similarly to before, we say that J 1
E, ˜J
1
E with respective jet prologantion maps
j1
E∶E→J 1
E, ˜j1
E∶E→˜J
1
E and bullet actions ●1, ˜●1, are equivalent as jet bimodules if there is a
isomorphism ϕ∈AHomA(J 1
E, ˜J
1
E) such that ϕ○j1
E = ˜j1
E. We have:
Lemma 5.2. Consider J 1
E, ˜J
1
E as constructed from the connections (∇E,σE), ( ˜∇E, ˜σE). Then
J 1
E /uni2243˜J
1
E as jet bimodules.
Proof. Consider the map ϕ∶J 1
E→˜J
1
E deﬁned on s+ω1⊗s1 ∈J 1
E as
ϕ(s+ω1⊗s1) =s+( ˜∇E−∇E)s+ω1⊗s1.
It automatically fulﬁls the above commuting diagram as ϕ○j1
E = ˜j1
E. To check that it is indeed
a bimodule map we compute
ϕ(a●1 (s+ω1⊗s1)) =ϕ(as+ da⊗s+aω1⊗s1) =as+( ˜∇E−∇E)(as)+ da⊗s+aω1⊗s1
QUANTUM JET BUNDLES 23
ConditionsJ2E.pdf
Ω1Ω1E
Ω1Ω1E
Ω1Ω1E
Ω1Ω1E
=σE σE
σE
σEσ
σ
(d)(c)
=
∧
∧
Ω1Ω1E Ω1Ω1E
Ω2E Ω2E
σE
σE
(e)
(b)
− = −
d ∧
(a)
∇E
−
∇E
∇E
E
EΩ2 Ω2 E
E
=0
σE,Ω2
Ω1
∇
∇ ∇E
∇E
σ
EE E E
E E E EΩ1 Ω1 Ω1 Ω1
σEσE
σE
σE
σE
Ω1 Ω1 Ω1
Ω1
Ω1 Ω1 Ω1
=
∧ ∧
+d
d
−
EΩ1 Ω1E E EΩ1
Ω1
Ω2 Ω2 Ω2 Ω2E E E E
∇E
∇EσE
σE
Figure 3. Conditions for J 2
E. Here, (a) says that ∇E is ﬂat, (b) is the Leibniz
compatibility condition, (c) the extendability property of a left connection as in
[4, Def. 4.10] and (d) the coloured braid relations implied by (b). Given (c),
condition (e) characterises that RE is a bimodule map and is also implied by
(b) if ∇is torsion free.
=as+a( ˜∇E−∇E)s+ da⊗s+aω1⊗s1 =a˜●1ϕ(s+ω1⊗s1).
and
ϕ(a●1 (s+ω1⊗s1)) =ϕ(sa+σE(s⊗da)+ω1⊗s1a) =sa+( ˜∇E−∇E)(sa)+σE(s⊗da)+aω1⊗s1
=as+( ˜∇E−∇E)s)a+ ˜σE(s⊗da)+aω1⊗s1 =a˜●1ϕ(s+ω1⊗s1).
due to the right Leibniz rule of the connections ∇E, ˜∇E. □
For the 2nd-order jet bimodule we also assume a torsion free connection ∇∶Ω1→Ω1⊗A Ω1 on
Ω1 with a generalised braiding σ∶Ω1⊗A Ω1→Ω1⊗A Ω1. The induced bimodule connection on
Ω1⊗AE will be denoted
∇(1,E)∶Ω1⊗
A
E→Ω1⊗A 2⊗
A
E, ∇(1,E) =∇⊗idE+σ1(id⊗∇E),
where id denotes the identity on Ω 1 and idE the identity on E. The associated generalised
braiding is σ∇(1,E) =σ1σE,2. We then deﬁne
J 2
E =E⊕Ω1⊗
A
E⊕Ω2
S⊗
A
E, j 2
E(s) =s+∇Es+∇(1,E)∇Es.
As before, we need to impose some conditions on this datum, shown in Fig. 3 and analogous
to the conditions imposed on ∇when dealing with J 3
A, see Fig. 1. Moreover, note that the
identities in Fig. 3 are trivial in the case ∇E = d, σE = id∶A⊗A Ω1→Ω1⊗AA, so we did not
already need them as additional data for the case of J 2
A.
Proposition 5.3. Let∇be torsion free withσ obeying the braid relations and∇E ﬂat, extendable
and Leibniz compatible (c.f. Fig. 3(a)-(c)). Then the k = 2 bullet actions deﬁned by
a●2s=a●1s+(∇da)⊗s, s ●2a=s●1a+σE,2σE,1(s⊗∇da),
a●2 (ω⊗s) =a●1 (ω⊗s)+[2,σ]1(da⊗ω⊗s), (ω⊗s)●2a= (ω⊗s)●1a+[2,σ]1σE,2(ω⊗s⊗da),
a●2 (ω1⊗ω2⊗s) =aω1⊗ω2⊗s, (ω1⊗ω2⊗s)●2a=ω1⊗ω2⊗sa
for a∈A,s ∈E,ω ∈Ω1,ω 1⊗ω2 ∈Ω2
S, make J 2
E a bimodule and j2
E a bimodule map.
24 SHAHN MAJID AND FRANCISCO SIM ˜AO
Proof. (1) We need to check that the product lands in J 2
E, namely that the terms added to
●1 are in Ω 2
S⊗AE = ker∧⊗AE. Since we assume ∇to be torsion free, we have ∧∇= d and
∧(id+σ) = 0. In the case of a●2s and s●2a, this gives ∧1(∇da⊗s) = d2a⊗s= 0 and
∧1σE,2σE,1(s⊗∇da) =σE,Ω2(s⊗∧∇da) = 0,
where we used thatσE is extendable (condition in Fig 3(c)). The added terms in a●2(ω⊗s) and
(ω⊗s)●2a are quantum symmetric due to ∧(id+σ) = 0 and a●2 (ω1⊗ω2⊗s), (ω1⊗ω2⊗s)●2a
are automatically quantum symmetric as ω1⊗ω2 ∈Ω2
S.
(2) We check that ●2 makes J 2
E into a bimodule, starting with the action ●2 on s ∈E. Let
a,b ∈A and recall that we have the 2nd-order Leibniz rule for ∇d in equation (1). Then
a●2 (b●2s) =a●2 (b●1s+∇db⊗s) =a●1 (b●1s)+∇da⊗bs+[2,σ]1(da⊗db⊗s)+a∇db⊗s
= (ab)●1s+∇d(ab)⊗s= (ab)●2s,
(s●2b)●2a= (s●1b+σE,2σE,1(s⊗∇db))●2a
= (s●1b)●1a+σE,2σE,1(sb⊗∇da)+[2,σ]1σE,2σE,1(s⊗db⊗da)+σE,2σE,1(s⊗(∇db)a)
=s●1 (ba)+σE,2σE,1(s⊗b∇da)+σE,2σE,1[2,σ]2(s⊗db⊗da)+σE,2σE,1(s⊗(∇db)a)
=s●1 (ba)+σE,2σE,1(s⊗∇d(ba)) =s●2 (ba).
These computations are analogous to the E = A case, but now with the coloured braid rela-
tions Fig. 3(d) for the 3rd equality of the second group, which is, however implied by Leibniz-
compatibility. Similarly,
(a●2s)●2b
= (a●1s+∇da⊗s)●2b= (a●1s)●1b+σE,2σE,1(as⊗∇db)+[2,σ]1σE,2(da⊗s⊗db)+∇da⊗sb
=a●1 (s●1b)+aσE,2σE,1(s⊗∇db)+[2,σ]1(da⊗σE(s⊗db))+∇da⊗sb
=a●2 (s●1b)+a●2σE,2σE,1(s⊗∇db) =a●2 (s●2b).
In the case of ω⊗s∈Ω1⊗AE we have
a●2 (b●2 (ω⊗s)) =a●2 (b●1 (ω⊗s)+[2,σ]1(db⊗ω⊗s))
=a●1 (b●1 (ω⊗s))+[2,σ]1(da⊗bω⊗s)+[2,σ]1(adb⊗ω⊗s)
= (ab)●1 (ω⊗s)+[2,σ]1(d(ab)⊗ω⊗s) = (ab)●2 (ω⊗s),
((ω⊗s)●2b)●2a= ((ω⊗s)●1b+[2,σ]1σE,2(ω⊗s⊗db))●2a
= ((ω⊗s)●1b)●1a+[2,σ]1σE,2(ω⊗sb⊗da)+[2,σ]1σE,2(ω⊗s⊗dba)
= (ω⊗s)●1 (ba)+[2,σ]1σE,2(ω⊗s⊗d(ba)) = (ω⊗s)●2 (ba),
(a●2 (ω⊗s))●2b= (a●1 (ω⊗s)+[2,σ]1(da⊗ω⊗s))●2b
= (a●1 (ω⊗s))●1b+[2,σ]1σE,2(aω⊗s⊗db)+[2,σ]1(da⊗ω⊗sb)
=a●1 ((ω⊗s)●1b)+a●2 [2,σ]1σE,2(ω⊗s⊗db)+[2,σ]1(da⊗ω⊗sb)
=a●2 ((ω⊗s)●1b+[2,σ]1σE,2(ω⊗s⊗db)) =a●2 ((ω⊗s)●2b).
Again for the actions on ω1⊗ω2⊗s ∈Ω2
S⊗AE these properties are straight forward as ●2 is
simply multiplication by a∈A.
(3) We need to check that the map j2
E is well-deﬁned, namely that ∇(1,E)∇Es ∈Ω2
S⊗AE.
Recall that we assume ∇E to be ﬂat, i.e. RE = (d⊗id−id∧∇E)∇E = 0, shown in Fig. 3(i).
Applying ∧1 to ∇(1,E)∇Es gives
∧1∇(1,E)∇Es=∧1(∇⊗id+σ1id⊗∇E)∇Es= (d⊗id−id∧∇E)∇Es=RE(s) = 0,
where we have used that ∇is torsion free.
QUANTUM JET BUNDLES 25
(4) To complete the proof, we show that ●2 makesj2
E a bimodule map. We ﬁrst compute the
2nd-order Leibniz rule for ∇(1,E)∇E,
∇(1,E)∇E(as) =∇(1,E)(da⊗s+a∇Es) =∇da⊗s+σ1(da⊗∇Es)+ da⊗∇Es+a∇(1,E)∇Es
=∇da⊗s+[2,σ]1(da⊗∇Es)+a∇(1,E)∇Es.
Using this property we can show
j2
E(as) =j1
E(as)+∇(1,E)∇E(as) =a●1j1
E(s)+∇da⊗s+[2,σ]1(da⊗∇Es)+a∇(1,E)∇Es
=a●2j1
E(s)+a●2∇(1,E)∇Es=a●2j2
E(s),
where we usedj1
E(as) =a●1j1
E(s). For the other side, we again compute a 2nd-order Leibniz rule
for ∇(1,E)∇E, where we will need the Leibniz compatibility condition for ∇E shown in Fig. 3(b).
Using the coloured braid relations implied by this, one can show that this condition is compatible
with the tensor product ⊗A in a similar manner to the proof of Lemma 3.4. The second order
Leibniz rule then reads
∇(1,E)∇E(sa) =∇(1,E)(∇Esa+σE(s⊗da))
= (∇(1,E)∇Es)a+σ1σE,2(∇Es⊗da)+(∇⊗id)σE(s⊗da)+σ1(id⊗∇E)σE(s⊗da)
= (∇(1,E)∇Es)a+σ1σE,2(∇Es⊗da)+σE,2σE,1(s⊗∇da)+σE,2(∇Es⊗da)
= (∇(1,E)∇Es)a+[2,σ]1σE,2(∇Es⊗da)+σE,2σE,1(s⊗∇da)
where used Leibniz compatibility for the 3rd equality. We therefore have
j2
E(sa) =j1
E(sa)+∇(1,E)∇E(sa)
=j1
E(s)●1a+(∇(1,E)∇Es)a+[2,σ]1σE,2(∇Es⊗da)+σE,2σE,1(s⊗∇da)
=j1
E(s)●2a+(∇(1,E)∇Es)●2a=j2
E(s)●2a.
□
We again have a bimodule map surjectionπ2 deﬁned by quotienting out the top degree. As for
k = 1, one can again consider in what sense these constructions depend on (∇,σ) and (∇E,σE).
This is the same for all k ≥2 and hence deferred to the end of the next subsection.

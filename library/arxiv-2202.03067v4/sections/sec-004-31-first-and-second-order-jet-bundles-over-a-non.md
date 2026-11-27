---
doc_id: arxiv-2202.03067v4
doc_title: "QUANTUM JET BUNDLES"
section_id: sec-004-31-first-and-second-order-jet-bundles-over-a-non
section_title: "First and second order jet bundles over a noncommutative algebra"
section_number: 3.1
pages: 6-8
source_pdf: 2202.03067v4.pdf
source_sha256: 22cf51d9d54ff681
toc_source: outline
doc_brief: "QUANTUM JET BUNDLES — We formulate a notion of jet bundles over a possibly noncommutative algebra A equipped with a torsion free connection."
---
1st-order jet bimodule and jet prolongation map as
J 1
A =A⊕Ω1, j 1(s) =s+ ds,
wheres∈A is prolonged toj1(s) ∈J 1
A. Here, the ﬁrst order derivatives of s are encoded in j1(s)
though ds. The left and right bullet actions of a∈A on J 1
A are deﬁned on each degree as
a●1s= (a+ da)s, s ●1a=s(a+ da),
a●1ω =aω, ω ●1a=ωa,
where ω ∈Ω1. Here and in general, we use ●k to denote the bimodule actions of A on Jk
A. It
follows immediately from the Leibniz rule that J 1
A becomes a bimodule and j1 a bimodule map
where A is a bimodule by left and right action on itself. There is also clearly a bimodule map
surjection π1∶J 1
A→A given by projecting out the Ω 1 component and such that π1○j1 = id.
Fork = 2, we suppose that ∇∶Ω1→Ω1⊗A Ω1 is a torsion free bimodule connection on Ω 1 with
generalised braidingσ∶Ω1⊗A Ω1→Ω1⊗A Ω1 and deﬁne the sub-bimodule of quantum symmetric
2-forms as
Ω2
S ∶= ker∧⊆Ω1⊗
A
Ω1
which classically corresponds to the symmetric rank (0, 2)-tensors. We set
J 2
A =A⊕Ω1⊕Ω2
S, j 2(s) =j1(s)+∇ds.
The usual formula for j2(s) in terms of symmetric 2nd partial derivatives appears in a central
basis, see (16) later. We deﬁne the left and right bullet actions of a∈A on J 2
A as
a●2s=a●1s+(∇da)s, s ●1a=s●1a+s∇da,
a●2ω =a●1ω+[2,σ](da⊗ω), ω ●2a=ω●1a+[2,σ](ω⊗da),
a●2ω1⊗ω2 =aω1⊗ω2, ω 1⊗ω2●2a=ω1⊗ω2a
for s ∈A, ω ∈Ω1 and ω1⊗ω2 ∈Ω2
S. Here [2,σ]∶= id+σ is a ‘braided integer’ bimodule map on
Ω1⊗A 2. Note also that ●2 is the recursively deﬁned via ●1.
QUANTUM JET BUNDLES 7
Proposition 3.1. Let∇be a torsion free bimodule connection onΩ1. Then J 2
A is anA-bimodule
and j2 ∶A→J 2
A is a bimodule map. Moreover, π2 ∶J 2
A→J 1
A given by quotienting out Ω2
S is a
bimodule surjection with π2○j2 =j1.
Proof. Since we assume ∇to be torsion free, we have im(id+σ) = im[2,σ]⊆ker∧= Ω2
S, ensuring
that the bullet action of A on J 2
A indeed lands on J 2
A. Before addressing the bimodule action
axioms for k = 2, it is helpful to note the 2nd-order Leibniz rule for ∇d
∇d(ab) =∇((da)b+adb) = (∇da)b+σ(da⊗db)+ da⊗db+a∇db
= (∇da)b+[2,σ](da⊗db)+a∇db.(1)
It is also useful to consider these calculations in an inductive manner, using the results for ●1
when computing the properties of ●2. We again compute these degree by degree
a●2(b●2s) =a●2 (b●1s)+a(∇db)s=a●1 (b●1s)+(∇da)bs+[2,σ](da⊗(db)s)+a(∇db)s
= (ab)●1s+(∇d(ab))s= (ab)●2s.
In the second equality we wrote b●1s=bs+(db)s and found extra terms that this picks up when
acted upon by a●2. We then used (1) and that the generalised braiding σ is a bimodule map
to write σ(da⊗(db)s) = σ(da⊗db)s to recognise the answer. The proof of the right action is
strictly similar and omitted, while for a bimodule
a●2 (s●2b) =a●2 (s●1b)+as∇db=a●1 (s●1b)+(∇da)sb+(id+σ)da⊗sdb+as∇db
= (a●1s)●2b+((∇da)s)●2b= (a●2s)●2b.
Next, the additional term in j2 lands in J 2
A =A⊕Ω1⊕Ω2
S as ∇ds is quantum symmetric due to
torsion freeness of the connection so that ∧∇ds= d2s= 0. The computations to show that j2 is
a bimodule map can again be done in an inductive manner using (1) as
j2(as) =j1(as)+∇d(as) =a●1j1(s)+(∇da)s+[2,σ](da⊗ds)+a∇ds
=a●2j1(s)+a●2∇ds=a●2j2(s),
j2(sa) =j1(sa)+∇(sa) =j1(s)●1a+(∇ds)a+[2,σ](ds⊗da)+s∇da
=j1(s)●2a+(∇ds)●2a=j2(s)●2a.
The projection and its stated properties are clear. It also follows thatj2 is split byπ1○π2∶J 2
A→A
given that j1 was split by π1. □
Finally, it is natural to ask to what extent the 2nd-order jet bimodule J 2
A depend on choice
of the connection (∇,σ). Following the classical notion of jet equivalence, consider two jet
bimodules J 2
A, ˜J
2
A with respective jet prologantion maps j2∶A→J 2
A and ˜j2∶A→˜J
2
A and bullet
actions●2, ˜●2. We then say that J 2
A, ˜J
2
A are equivalent as jet bimodules if there is a isomorphism
ϕ∈AHomA(J 2
A, ˜J
2
A) w.r.t. the bullet actions such that the following diagram commutes
J 2
A ˜J
2
A
A
ϕ
j2 ˜j2
.
Lemma 3.2. Consider J 2
A, ˜J
2
A as constructed from the connections (∇,σ), ( ˜∇,σ) on Ω1 re-
spectively. Then J 2
A /uni2243˜J
2
A as A-bimodules w.r.t. the bullet actions.
8 SHAHN MAJID AND FRANCISCO SIM ˜AO
Proof. Consider the map ϕ∶J 2
A→˜J
2
A deﬁned on a+ω1+ω2 ∈J 2
A as
ϕ(a+ω1+ω2) =a+ω1+( ˜∇−∇)ω1+ω2.
To see that ϕ fulﬁls ϕ○j2 = ˜j2 we compute
ϕ(j2(a)) =ϕ(a+ da+∇da) =a+ da+( ˜∇−∇)da+∇da= ˜j2(a).
To check thatϕ is indeed a bimodule map note that
ϕ(b●2 (a+ω1+ω2)) =ϕ(ba+(db)a+(∇db)a+bω1+[2,σ]db⊗ω1+bω2)
=ba+(db)a+( ˜∇−∇)(( db)a)+(∇db)a+bω1+( ˜∇−∇)(bω1)+[2,σ]db⊗ω1+bω2
=ba+(db)a+( ˜∇db)a+bω1+b˜∇ω1−b∇ω1+[2,σ]db⊗ω1+bω2
=b˜●2a+b˜●2ω1+b˜●2( ˜∇ω1−∇ω1+ω2) =b˜●2ϕ(a+ω1+ω2)
and
ϕ((a+ω1+ω2)●2b) =ϕ(ab+adb+a∇db+ω1b+[2,σ](ω1⊗db)+ω2b)
=ab+adb+( ˜∇−∇)(adb)+a∇db+ω1b+( ˜∇−∇)(ω1b)+[2,σ](ω1⊗db)+ω2b
=ab+adb+a( ˜∇−∇)db+a∇db+ω1b+( ˜∇−∇)(ω1)b+[2,σ](ω1⊗db)+ω2b
=a˜●2b+ω1˜●2b+(( ˜∇−∇)(ω1)+ω2)˜●2b=ϕ(a+ω1+ω2)˜●2b
□
Therefore our 2nd-order jet construction only depends on the choice of braiding σ. It is
interesting to note that, if we consider J 2
A, ˜J
2
A with the right bullet action and the inherited
action from Ω 1 on the left, then they are isomorphic via the same ϕ as above, even if one takes
two connections (∇,σ), ( ˜∇, ˜σ) with diﬀerent braidings. This is due to the identity
( ˜∇−∇)(ω1b)+[2,σ](ω1⊗db) = ( ˜∇−∇)(ω1)b+[2, ˜σ](ω1⊗db)
which can be used in the second line of the last computation above to show that ϕ is still a
right-module map in this case. One can also check that ϕ is a left module map in this case.

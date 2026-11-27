---
doc_id: arxiv-2202.03067v4
doc_title: "QUANTUM JET BUNDLES"
section_id: sec-012-52-higher-order-leibniz-rules-for-the-jke-case
section_title: "Higher order Leibniz rules for the JkE case"
section_number: 5.2
pages: 25-28
source_pdf: 2202.03067v4.pdf
source_sha256: 22cf51d9d54ff681
toc_source: outline
doc_brief: "QUANTUM JET BUNDLES — We formulate a notion of jet bundles over a possibly noncommutative algebra A equipped with a torsion free connection."
---
E case. Here we collect the geometric data and
some facts needed for the general case. First, we observe as alluded to near the start of Section 4
that extendable connections have a simple rule for their tensor product curvature.
Lemma 5.4. Let ∇E be an extendable bimodule connection. Then RE is a bimodule map iﬀ
∇E is Leibniz compatible as shown in Fig. 3(b). In this case, if ∇F is another connection, then
∇E⊗AF has curvature
RE⊗AF =RE⊗id+(σE,Ω2⊗id)id⊗RF.
Proof. The proof is similar to that of Lemma 3.4 but with the diagrams as in Fig. 3, so we omit
the details. One can also view this as piece of the proof in [4, Thm 4.15] that the DG category
AGA of extendable connections with bimodule map curvatures has a tensor product. □
In our case,∇is assumed to be extendable andE plays the role ofF . Hence if ∇is extendable,
ﬂat, Leibniz compatible and ∇E is ﬂat then the tensor product connection ∇(1,E) on Ω1⊗AE is
ﬂat. Such considerations were not needed for for J 2
E, but in line to the formula ∧1∇(1,E)∇Es=
RE(s) in the proof there that needed ∇E to be ﬂat, we will similarly need ∇(1,E) ﬂat to show
that the map j3
E is indeed in the kernel of ∧1.
26 SHAHN MAJID AND FRANCISCO SIM ˜AO
Similarly, iterating the lemma, we see that all the higher∇(n,E)∶Ω1⊗An⊗AE→Ω1⊗A(n+1)⊗AE
deﬁned recursively through
∇(0,E) =∇E, ∇(n+1,E) =∇⊗idn−1⊗idE+σ1(id⊗∇(n,E))
are ﬂat. Here ∇(n,E) applies the appropriate connection to every factor in Ω1⊗An⊗AE and then
uses σ to switch the new term to the utmost left factor, i.e. one can also write
∇(n,E) =
n−1
/summation.disp
k=0
σ1...σ k(idk⊗∇⊗idn−1−k⊗idE)+σ1...σ n(idn⊗∇E).(12)
where the ﬁrst term is∇n⊗idE. The associated generalised braidingsσ(n,E)∶Ω1⊗An⊗AE⊗A Ω1→
Ω1⊗A(n+1)⊗AE are given by
σ(0,E) =σE, σ (n,E) =σ1(id⊗σ(n−1,E)) =σ1...σ nσE,n+1
where σE,n+1 means that we apply σE to the (n+ 1)-th tensor factor. We also deﬁne
σn
E∶E⊗
A
Ω1⊗An→Ω1⊗An⊗
A
E, σ n
E =σE,n...σ E,1
and note that for an extendable ∇E, this restricts to E⊗A Ωn
S →Ωn
S⊗E. We can view all of
these together as σE,ΩS∶E⊗A ΩS→ΩS⊗AE acting by σn
E on each degree n.
Lemma 5.5. If σ, σE satisfy the coloured braid relations σiσE,i+1σE,i =σE,i+1σE,iσi+1 then
/parenleft.alt3/bracketleft.alt3n
k,σ/bracketright.alt3⊗idE/parenright.alt3σn
E =σn
E /parenleft.alt3idE⊗/bracketleft.alt3n
k,σ/bracketright.alt3/parenright.alt3.
If ∇E is moreover extendable then
(⊙⊗id)(id⊗σE,ΩS)(σE,ΩS⊗id) =σE,ΩS(id⊗⊙).
Proof. First note that the coloured braid relations imply σlσn
E =σn
Eσl+1 for l = 1,...,n −1. It is
clear that the equation we want to show holds for n = 1. Assuming that it holds for n−1, we
then compute
/parenleft.alt3/bracketleft.alt3n
k,σ/bracketright.alt3⊗idE/parenright.alt3σn
E = /parenleft.alt3id⊗/bracketleft.alt3n−1
k−1,σ/bracketright.alt3⊗idE/parenright.alt3σ1...σ n−kσn
E+/parenleft.alt3id⊗/bracketleft.alt3n−1
k ,σ/bracketright.alt3⊗idE/parenright.alt3σn
E
= /parenleft.alt3id⊗/bracketleft.alt3n−1
k−1,σ/bracketright.alt3⊗idE/parenright.alt3σn
Eσ2...σ n−k+1+ id⊗/braceleft.alt3/parenleft.alt3/bracketleft.alt3n−1
k ,σ/bracketright.alt3⊗idE/parenright.alt3σn−1
E /braceright.alt3σE,1
= id⊗/braceleft.alt3σn−1
E /parenleft.alt3idE⊗/bracketleft.alt3n−1
k−1,σ/bracketright.alt3/parenright.alt3/braceright.alt3σE,1σ2...σ n−k+1+ id⊗/braceleft.alt3σn−1
E /parenleft.alt3idE⊗/bracketleft.alt3n−1
k−1,σ/bracketright.alt3/parenright.alt3/braceright.alt3σE,1
=σn
EidE⊗/braceleft.alt3/parenleft.alt3id⊗/bracketleft.alt3n−1
k−1,σ/bracketright.alt3/parenright.alt3σ1...σ n−k+/parenleft.alt3id⊗/bracketleft.alt3n−1
k−1,σ/bracketright.alt3/parenright.alt3/braceright.alt3=σn
E /parenleft.alt3idE⊗/bracketleft.alt3n
k,σ/bracketright.alt3/parenright.alt3,
where we assumed the lower case as the induction hypothesis for the 3rd equality. □
The second part implies that we can extend the product ⊙on ΩS to a bimodule structure on
ΩS⊗AE which will then be used as a base on which to build the jet bimodule for E.
Corollary 5.6. Let∇be a torsion free,∧-compatible, extendable connection on Ω1. Let σ satisfy
the braid relations and σE the coloured braid relations, and let ∇E be extendable. Then ΩS⊗E
is an ΩS-bimodule with the left and right actions ⊙E given by
η⊙E (ω⊗s) =η⊙ω⊗s, (ω⊗s)⊙Eη =ω⊙σE,ΩS(s⊗η)
for all s∈E, ω,η ∈ΩS.
Proof. That the left ⊙E is an action and commutes with the right ⊙E is immediate from the
form of the actions and ⊙associative. That the right ⊙E is an action follows immediately from
Lemma 5.5 in the more abstract form. One can also dissect the content of this by degree. □
QUANTUM JET BUNDLES 27
As in the E =A case, we are interested in analysing n-th order derivatives for any bimodule
E, which will have similar properties to the ones we encountered before. They are deﬁned as
∇n
E∶E→Ω1⊗An⊗
A
E, ∇n
Es=∇(n−1,E)∇n−1
E s=∇n
Es=∇(n−1,E)... ∇(0,E)s,
with ∇0
E = idE.
Lemma 5.7. Let ∇be a torsion free, ﬂat, ∧-compatible bimodule connection on Ω1 and ∇E
a ﬂat bimodule connection on E. Then the image of ∇n
E is a subset of the space of quantum
symmetric n-forms with values in E,
im∇n
E ⊆Ωn
S⊗
A
E.
Proof. The cases n = 0, 1 are trivial and the case n = 2 has already been shown in Proposition
5.3. For n > 2 the proof works in the same manner as for Lemma 4.1. When applying ∧1 on
∇n
Es, we again ﬁnd that it vanishes as we assumed ﬂatness,
∧1∇n
Es=∧1∇(n−1,E)∇(n−2,E)∇n−2
E s= (d⊗idE−∧1(id⊗∇(n−2,E)))∇(n−2,E)s∇n−2
E s
=R(n−2,E)(∇n−2
E s) = 0.
Next, we note that ∇(n−1,E) restricts to a connection Ωn−1
S ⊗AE as is clear from its the tensor
product form (12). The ﬁrst term here is ∇n−1 which by Lemma 4.1 restricts to Ω n−1S and the
second term also restricts by ∧-compatibility of ∇. Then for i = 2,...,n −1, we have ∧i∇n
Es =
∇(n−1,E)∇n−1
E s= 0 where we take as induction hypothesis that ∇n−1
E lands in Ωn−1
S ⊗AE. □
We now turn to the generalisation of the n-th order Leibniz rules. In contrast to the E =A
case, we have both left and right ones. During the proof, we will also see how ∇(n,E) can be
exchanged with the braidings σ,σE and the braided binomials /bracketleft.alt1n
k,σ/bracketright.alt, in an analogous fashion to
Lemma 4.6.
Lemma 5.8. Let ∇, ∇E be Leibniz compatible as in Fig. 1(e) and Fig. 3 (b). Then
∇n
E(as) =
n
/summation.disp
k=0
/parenleft.alt3/bracketleft.alt3n
k,σ/bracketright.alt3⊗idE/parenright.alt3∇n−ka⊗∇k
Es,
∇n
E(sa) =
n
/summation.disp
k=0
/parenleft.alt3/bracketleft.alt3n
k,σ/bracketright.alt3⊗idE/parenright.alt3(idn−k⊗σk
E)(∇n−k
E s⊗∇ka).
for all a∈A,s ∈E.
Proof. Taking the tensor product from of ∇(n,E) in (12), we ﬁrst observe that
∇(n,E)σi =σi+1∇(n,E), ∇(n,E) /parenleft.alt3/bracketleft.alt3n
k,σ/bracketright.alt3⊗idE/parenright.alt3= /parenleft.alt3id⊗/bracketleft.alt3n
k,σ/bracketright.alt3⊗idE/parenright.alt3∇(n,E).(13)
fori= 1,...,n −1,k = 0,...,n . Here the left hand side has two terms of which one is (∇n⊗idE)σi
and we apply Lemma 4.6, and the other isσ1...σ nσi(idn⊗∇E) and we apply the braid relations
for σ implied by Leibniz compatibility. This then implies the second half of (13) as before.
Next, we introduce the notation
∇(i,E,j)∶Ω1⊗Ai⊗
A
E⊗
A
Ω1⊗Aj→Ω1⊗A(i+1)⊗
A
E⊗
A
Ω1⊗Aj,
∇(i,E,j) =∇(i,E)⊗idj+σ1...σ iσE,i+1(idi⊗idE⊗∇j)
for the tensor product of ∇(i,E) as a bimodule connection and ∇j from Section 4. We now prove
the further relation
∇(j,E,n−j)σE,j =σE,j+1∇(j−1,E,n−j+1)(14)
28 SHAHN MAJID AND FRANCISCO SIM ˜AO
for j = 1,...,n . Here n=j = 1 means ∇(1,E,0)σE,1 =σE,2∇(0,E,1), which is our assumed Leibniz
compatibility condition for ∇E in Fig. 3(b). Now proceeding inductively,
∇(j,E,n−j)σE,j = /braceleft.alt1∇j−1⊗id⊗idE⊗idn−j+σ1...σ j−1/parenleft.alt1idj−1⊗∇(1,E,0)⊗idn−j/parenright.alt1
+σ1...σ jσE,j+1/parenleft.alt1idj−1⊗id⊗idE⊗∇n−j/parenright.alt1/braceright.alt1σE,j
=σE,j+1/parenleft.alt1∇j−1⊗idE⊗id⊗idn−j/parenright.alt1+σ1...σ j−1/parenleft.alt1idj−1⊗∇(1,E,0)σE,1⊗idn−j/parenright.alt1
+σ1...σ jσE,j+1σE,j /parenleft.alt1idj−1⊗idE⊗id⊗∇n−j/parenright.alt1.
The ﬁrst term is already in the desired form. For the second we apply Leibniz compatibility for
∇E to get
σ1...σ j−1/parenleft.alt1idj−1⊗σE,2∇(1,E,0)⊗idn−j/parenright.alt1=σ1...σ j−1σE,j+1/parenleft.alt1idj−1⊗∇(1,E,0)⊗idn−j/parenright.alt1
=σE,j+1σ1...σ j−1/parenleft.alt1idj−1⊗∇(1,E,0)⊗idn−j/parenright.alt1.
For the last term we can use the implied coloured braid relations to pass σE,j+1 to the utmost
left position σ1...σ jσE,j+1σE,j = σE,j+1σ1...σ j−1σE,jσi+1. Summing the three expressions, we
have
∇(j,E,n−j)σE,j =σE,j+1/braceleft.alt1∇j−1⊗idE⊗id⊗idn−j+σ1...σ j−1/parenleft.alt1idj−1⊗∇(0,E,1)⊗idn−j/parenright.alt1
+σ1...σ j−1σE,jσi+1/parenleft.alt1idj−1⊗idE⊗id⊗∇n−j/parenright.alt1/braceright.alt1
which we recognise as σE,j+1∇(j−1,E,n−j−1) when this is similarly decomposed.
Then computation for the stated left and rightn-th Leibniz rules now proceeds analogously to
the proof of Lemma 4.7, now using equation (13) and keeping in mind that equation (14) implies
∇(n,E,0)(idl−1⊗σn−l+1
E ) = (idl⊗σn−l+1
E )∇(l−1,E,n−l+1)
for the computation of the right stated identity. □
In our geometric setting where in addition ∇is torsion free, ﬂat, ∧-compatible and extendable
and ∇E is ﬂat and extendable, we can write this lemma in terms of the bimodule product ⊙E as
∇n
E(as) =
n
/summation.disp
k=0
∇n−ka⊙E∇k
Es ∇n
E(sa) =
n
/summation.disp
k=0
∇n−k
E s⊙E∇ka.(15)

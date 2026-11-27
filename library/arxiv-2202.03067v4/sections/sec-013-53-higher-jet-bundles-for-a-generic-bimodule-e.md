---
doc_id: arxiv-2202.03067v4
doc_title: "QUANTUM JET BUNDLES"
section_id: sec-013-53-higher-jet-bundles-for-a-generic-bimodule-e
section_title: "Higher Jet bundles for a generic bimodule E"
section_number: 5.3
pages: 28-30
source_pdf: 2202.03067v4.pdf
source_sha256: 22cf51d9d54ff681
toc_source: outline
doc_brief: "QUANTUM JET BUNDLES — We formulate a notion of jet bundles over a possibly noncommutative algebra A equipped with a torsion free connection."
---
derivatives on Ω1⊗Ak⊗AE, we are now ready to construct higher jets for a generic bimodule E.
Theorem 5.9. Let ∇be a torsion free, ﬂat, ∧-compatible, extendable and Leibniz compatible
bimodule connection on Ω1 as in Fig. 1(a)-(e) and ∇E a ﬂat, extendable and Leibniz compatible
bimodule connection on E as in Fig. 3 (a)-(c). Then
Jk
E =E⊕Ω1
S⊗
A
E⊕/uni22EF⊕Ωk
S⊗
A
E, j k
E ∶E→Jk
E, j k
E(s) =s+∇1
Es+⋅⋅⋅+∇k
Es,
form an A-bimodule and bimodule maps for the bullet action ●k given by
a●k (ωj⊗s) =jk−ja⊙E (ωj⊗s) =
k
/summation.disp
i=j
∇i−ja⊙E (ωj⊗s),
(ωj⊗s)●ka= (ωj⊗s)⊙Ejk−ja=
k
/summation.disp
i=j
(ωj⊗s)⊙E∇i−ja
for all ωj ∈Ωj
S, s∈E and j = 0,...,k . Quotienting out Ωk
S⊗AE gives a bimodule map surjection
πk∶Jk
E→Jk−1
E such that πk○jk
E =jk−1
E .
QUANTUM JET BUNDLES 29
Proof. This proof is analogous to the proof of Theorem 4.8 with ∇n,⊙replaced by∇n
E,⊙E where
necessary. That the action ●k and jet prolongation map jk
E land in Jk
E is from Lemmas 5.6 and
5.7. Thus, to show that jk
E is a bimodule map, we compute for a∈A,s ∈E,
jk
E(as) =
k
/summation.disp
i=0
∇i
E(as) =
k
/summation.disp
i=0
i
/summation.disp
j=0
∇i−ja⊙E∇j
Es=
k
/summation.disp
j=0
k
/summation.disp
i=j
∇i−ja⊙E∇j
Es=
k
/summation.disp
j=0
jk−j(a)⊙E∇js
=
k
/summation.disp
j=0
a●k∇j
Es=a●kjk
E(s).
Similarly, forjk
E(sa) =jk
E(s)●ka. Likewise, that the right action ●k is compatible with the tensor
product is
((ωj⊗s)●kb)●ka= ((ωj⊗s)⊙Ejk−j(b))●ka=
k
/summation.disp
i=j
((ωj⊗s)⊙E∇i−jb)●ka
=
k
/summation.disp
i=j
((ωj⊗s)⊙E∇i−jb)⊙Ejk−i(a) =
k
/summation.disp
i=j
(ωj⊗s)⊙E (∇i−jb⊙jk−i(a)) =
k
/summation.disp
i=j
(ωj⊗s)⊙E (∇i−jb●k−ja)
= (ωj⊗s)⊙E (jk−j(b)●k−ja) = (ωj⊗s)⊙Ejk−j(ba) = (ωj⊗s)●k (ab)
where in the 4th equality we have used that ⊙E is a bimodule action w.r.t. the product ⊙. The
rest of the properties follow in a similar manner. That πk∶Jk
E→Jk−1
E is a bimodule surjection
which connects jk
E tojk−1
E is then also clear. From the very deﬁnition of Jk
E it is also clear that
we have an exact sequence
0→Ωk
S⊗
A
E→Jk
E
πk
/leftrightline→Jk−1
E →0
of underlying bimodules. □
As in thek = 1 case, we want to investigate in what sense the jet bimodulesJk
E are independent
of the choice of connections (∇,σ) on Ω1 and (∇E,σE) on E. We say that two jet bimodules
Jk
E, ˜J
k
E with repective jet prologantion maps jk
E∶E→Jk
E and ˜jk
E∶E→˜J
k
E and bullet actions
●k, ˜●kare equivalent as jet bimodules if there is a isomorphism ϕ ∈AHomA(Jk
E, ˜J
k
E) such that
ϕ○jk
E = ˜jk
E.
In contrast to our result for k = 1, where J 1
E did not depend on the connection ∇E and also
not on its braiding σE, in higher degrees we ﬁnd that Jk
E does depend, but only weakly via the
braiding σE alone.
Lemma 5.10. Consider Jk
E, ˜J
k
E as constructed from the connection (∇,σ) on Ω1 and from the
connections (∇E,σE), ( ˜∇E,σE) on E respectively. Then Jk
E /uni2243˜J
k
E as jet bimodules.
Proof. We take the map ϕ∶Jk
E→˜J
k
E deﬁned on s+∑k
j=1ωj⊗sj ∈Jk
E as
ϕ(s+
k
/summation.disp
j=1
ωj⊗sj) =s+ ˜jk
E(s)−jk
E(s)+
k
/summation.disp
j=1
ωj⊗sj.
As before it automatically fulﬁls the above commuting diagram as ϕ○jk
E = ˜jk
E. In this case the
bulletA-actions on Jk
E, ˜J
k
E are the same●k = ˜●k as they are both constructed on the same (∇,σ)
and σE. To check that ϕ is indeed a bimodule map we compute
ϕ(a●k (s+
k
/summation.disp
j=1
ωj⊗sj)) =ϕ(as+(jk(a)−a)⊙Es+a●k
k
/summation.disp
j=1
ωj⊗sj)
30 SHAHN MAJID AND FRANCISCO SIM ˜AO
=as+ ˜jk
E(as)−jk
E(as)+(jk(a)−a)⊙Es+a●k
k
/summation.disp
j=1
ωj⊗sj
=a●ks+a●k ˜jk
E(s)−a●kjk
E(as+ da⊗s+a●k
k
/summation.disp
j=1
ωj⊗sj =a˜●1ϕ(s+ω1⊗s1).
and similarly for the right action. □

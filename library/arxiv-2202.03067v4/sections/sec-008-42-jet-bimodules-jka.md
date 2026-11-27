---
doc_id: arxiv-2202.03067v4
doc_title: "QUANTUM JET BUNDLES"
section_id: sec-008-42-jet-bimodules-jka
section_title: "Jet bimodules JkA"
section_number: 4.2
pages: 19-20
source_pdf: 2202.03067v4.pdf
source_sha256: 22cf51d9d54ff681
toc_source: outline
doc_brief: "QUANTUM JET BUNDLES — We formulate a notion of jet bundles over a possibly noncommutative algebra A equipped with a torsion free connection."
---
A. With the above theory of higher order derivatives on Ω 1⊗An and
braided binomials in hand, we have now done all the work to write down the jet bimodules of
any order over a possibly noncommutative algebra A.
Theorem 4.8. Let ∇be a torsion free, ﬂat, ∧-compatible, extendable and Leibniz-compatible
bimodule connection on Ω1 as shown in Fig. 1(a)-(e). Then
Jk
A =
k
/uni2295.big.disp
i=0
Ωi
S =A⊕Ω1
S⊕/uni22EF⊕Ωk
S, j k∶A→Jk
A, j k(s) =s+∇1s+/uni22EF+∇ks
form an A-bimodule and bimodule map with actions ●k given by
a●kωj =jk−j(a)⊙ωj =
k
/summation.disp
i=j
∇i−ja⊙ωj, ω j●ka=ωj⊙jk−j(a) =
k
/summation.disp
i=j
ωj⊙∇i−ja.
whereωj ∈Ωj
S and⊙is the product in Corollary 4.5 applied in the appropriate degree. Quotienting
out Ωk
S gives a bimodule surjection πk∶Jk
A→Jk−1
A such that πk○jk =jk−1.
Proof. (1) First note that both the action ●k and the jet prolongation mapjk land in Jk
A. Recall
that∇la∈Ωl
S due to Lemma 4.1, from which immediately follows that imjk ⊂Jk
A. For the action
●k, as we assume ωj ∈Ωj
S, then due to Corollary 4.5 we have ∇i−ja⊙ωj ∈Ωi
S. Since the sum in
a●kωj runs over i=j,...,k , the highest degree terms will be in Ω k
S and hence a●kωj ∈Jk
A.
(2) Next, for a,s ∈A, we compute
jk(as) =
k
/summation.disp
i=0
∇i(as) =
k
/summation.disp
i=0
i
/summation.disp
j=0
∇i−ja⊙∇js=
k
/summation.disp
j=0
k
/summation.disp
i=j
∇i−ja⊙∇js=
k
/summation.disp
j=0
jk−j(a)⊙∇js=
k
/summation.disp
j=0
a●k∇js
=a●kjk(s),
jk(sa) =
k
/summation.disp
i=0
∇i(sa) =
k
/summation.disp
i=0
i
/summation.disp
j=0
∇js⊙∇i−ja=
k
/summation.disp
j=0
k
/summation.disp
i=j
∇js⊙∇i−ja=
k
/summation.disp
j=0
∇js⊙ji−j(a) =
k
/summation.disp
j=0
∇js●ka
=jk(s)●ka
so that if ●k are actions then jk is a bimodule map.
(3) Next, for ωj ∈Ωj
S, j = 0,...,k and a,b ∈A, we compute
a●k (b●kωj) =a●k (jk−j(b)⊙ωj) =
k
/summation.disp
i=j
a●k (∇i−jb⊙ωj) =
k
/summation.disp
i=j
jk−i(a)⊙(∇i−jb⊙ωj)
=
k
/summation.disp
i=j
(jk−i(a)⊙∇i−jb)⊙ωj =
k
/summation.disp
i=j
(a●k−j∇i−jb)⊙ωj = (a●k−jjk−j(b))⊙ωj =jk−j(ab)⊙ωj = (ab)●kωj
where we used that ⊙is associative by Corollary 4.5 and that jk−j is a bimodule map w.r.t. ●k−j
for all j = 0,...,k . In the same manner we can compute
(ωj●kb)●ka= (ωj⊙jk−j(b))●ka=
k
/summation.disp
i=j
(ωj⊙∇i−jb)●ka=
k
/summation.disp
i=j
(ωj⊙∇i−jb)⊙jk−i(a)
=
k
/summation.disp
i=j
ωj⊙(∇i−jb⊙jk−i(a)) =
k
/summation.disp
i=j
ωj⊙(∇i−jb●k−ja) =ωj⊙(jk−j(b))●k−ja) =ωj⊙jk−j(ba) =ωj●k (ab)
It is just left to show that the left and right actions commute. This is
(a●kωj)●kb=
k−j
/summation.disp
m=0
(∇ma⊙ωj)●kb=
k−j
/summation.disp
m=0
k−j
/summation.disp
n=m
∇ma⊙ωj⊙∇n−mb=
k−j
/summation.disp
n=0
n
/summation.disp
m=0
∇ma⊙ωj⊙∇n−mb
20 SHAHN MAJID AND FRANCISCO SIM ˜AO
=
k−j
/summation.disp
n=0
n
/summation.disp
m=0
∇n−ma⊙ωj⊙∇mb=
k−j
/summation.disp
m=0
k−j
/summation.disp
n=m
∇n−ma⊙ωj⊙∇mb=
k−j
/summation.disp
m=0
a●k (ωj⊙∇mb) =a●k (ωj●kb).
(4) To see thatπk∶Jk
A→Jk−1
A is a bimodule map, it is helpful to write the bimodule action ●k
in a recursive matter, i.e. in terms of ●k−1. First we deﬁne the A-bimodule action ●0 on J 0
A =A
as simple multiplication in A. Then for a generic k, the left action can be recursively written as
a●kωj =jk−j(a)⊙ωj =jk−j−1(a)⊙ωj+∇k−j(a)⊙ωj =a●k−1ωj+∇k−ja⊙ωj.(10)
where ωj ∈Ωj
S for j = 0,...,k −1. Note that the added term ∇k−ja⊙ωj is in Ωk
S and therefore
in the kernel of πk. We then have πk(a●kωj) =a●k−1ωj =a●k−1πk(ωj) since j <k. For j =k
we simply have a●kωk = aωk and πk(aωk) = 0. The property that πk is a right-module map
can be shown in the same manner. It follows by iteration that π1○π2○/uni22EF○πk splits jk. These
considerations are analogous to the recursive analysis presented for the casesk = 1, 2, 3 in Section
3. It is also worth noting that by the very deﬁnition of Jk
A, we have an exact sequence
0→Ωk
S→Jk
A
πk
/leftrightline→Jk−1
A →0
of underlying bimodules, which seems to be of interest in the subsequent endofunctor generali-
sation in [11]. □
The inﬁnite jet bimodule J∞
A can then be deﬁned as the limit of the sequence
/uni22EF→Jk
A
πk
→Jk−1
A →/uni22EF→J 2
A
π2
→J 1
A
π1
→J 0
A =A(11)
of bimodules with bimodule maps compatible with jk∶A→Jk
A, with projections π∞,k∶J∞
A →Jk
A
for allk. This sequence can be thought of formally as a pro-object in the category ofA-bimodules,
in the classical terminology used on [26]. Then the collection (j0,j 1,j 2,j 3,...) of jet evaluations
represent a bimodule map fromA to this pro-object. Note also that J∞
A as a vector space is much
bigger than the ‘quantum symmetric forms’ Ω S =/uni2295.big∞
k=0 Ωk
S in Corollary 4.5 (since direct sums
have elements with support in only a ﬁnite number of diﬀerent degrees). Moreover, the latter
has the trivial A-bimodule structure, inherited from that of Ω 1 rather than the bullet bimodule
structure of J∞
A obtained from the ●k presented above.

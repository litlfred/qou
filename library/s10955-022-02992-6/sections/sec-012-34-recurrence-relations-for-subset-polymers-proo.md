---
doc_id: s10955-022-02992-6
doc_title: "Cluster Expansions: Necessary and Sufficient Convergence Conditions"
section_id: sec-012-34-recurrence-relations-for-subset-polymers-proo
section_title: "Recurrence Relations for Subset Polymers: Proof of Theorem 2.7"
section_number: 3.4
pages: 22-25
source_pdf: s10955-022-02992-6.pdf
source_sha256: aa73d797a89eaf06
toc_source: outline
doc_brief: "Cluster Expansions: Necessary and Sufficient Convergence Conditions — We prove a new convergence condition for the activity expansion of correlation functions in equilibrium statistical mechanics"
---
Just as in the continuous case, we will show that the expansions ˜T solve a system of integral
equations in the discrete setup. We do so by providing a recursive formula for the corre-
sponding coefﬁcients ϕT
1+k.
Lemma 3.11 For all ﬁnite subsets D′ ⊂Zd, all x ∈Zd \ D′, and all k ∈N,
ϕT
1+k(D′ ∪{x}, Y1, . . . , Yk)
= ϕT
1+k(D′, Y1, . . . , Yk) +
k

i=1

−1l{Yi∋x,Yi∩D=∅}

ϕT
k

D′ ∪Yi, (Y j) j̸=i

with ϕT
1 ≡1.
Proof Notice that the analogue of Lemma 3.9 holds in the discrete setup of subset poly-
mers as well, in particular for the choice D0 := {x} and D1 := D′. However, since two
disjoint polymers Y1 and Y2 cannot both intersect the same monomer x, only the summands
corresponding to L = ∅and |L| = 1 in the sum on the right-hand side of the identity in
Lemma 3.9 provide non-trivial contributions.
⊓⊔
Let D be a ﬁnite non-empty subset of Zd and z a non-negative activity function. Set
˜T (D; z) := 1 +
∞

k=1
1
k!

(Y1,...,Yk)∈Xk
ϕT
1+k(D, Y1, . . . , Yk)
z(Y1) · · · z(Yk)
and for N ∈N,
˜TN(D; z) := 1{|D|≤N}
+
∞

k=1
1
k!

(Y1,...,Yk)∈Xk
1l{|D|+k
i=1 |Yi|≤N}ϕT
1+k(D, Y1, . . . , Yk)z(Y1) · · · z(Yk).
(3.10)
Cluster Expansions: Necessary...
Page 23 of 47
33
Furthermore, we use the convention ˜TN(∅; z) = 1 for all N ≥1.
Again, we lift the established recurrent relations on the level of coefﬁcients (given by
Lemma 3.11) to the level of partial sums and series, deriving a system of integral equations
for those. The following result is an analogue of Proposition 3.6 and Proposition 3.10 for
subset polymers.
Proposition 3.12 Under the assumptions of Lemma 3.11, the identities
˜T (D′ ∪{x}; z) = ˜T (D′; z) +

Y∋x:
Y∩D′=∅
z(Y) ˜T (D′ ∪Y; z)
and for N ∈N,
˜TN+1(D′ ∪{x}; z) = ˜TN(D′; z) +

Y∋x:
Y∩D′=∅
z(Y) ˜TN(D′ ∪Y; z),
hold for any non-negative activity z.
Remark 3.2 Notice that the ﬁrst identity in Proposition 3.12 is just a sign-ﬂipped version of
the standard Kirkwood–Salsburg equations for the reduced correlation functions found in
[1].
Proof Lemma 3.11 yields
1l{|D′∪{x}|+k
i=1 |Yi|≤N+1}ϕT
1+k(D′ ∪{x}, Y1, . . . , Yk)
= 1l{|D′|+k
i=1 |Yi|≤N}ϕT
1+k(D′, Y1, . . . , Yk)
+
k

i=1

−1l{Yi∋x, Yi∩D′=∅}

1l{|D′∪Yi|+
j̸=i |Y j|≤N}ϕT
k(D′ ∪Yi, (Y j) j̸=i).
The proof of the recurrence relation for ˜TN(·; z) is concluded by exploiting the alternating
sign property of the Ursell functions, summing over k and Y1, . . . , Yk, and exploiting the
symmetry of ϕT
k. The recurrence relation for ˜T (·; z) follows by passing to the limit N →∞.
⊓⊔
Proof of Theorem 2.7 To prove the implication (i) ⇒(ii), suppose that condition (i) is sat-
isﬁed for some set function a(·). Proceeding as in the proof of Theorem 2.1 again, we prove
by induction over N that
˜TN(D; z) ≤exp(a(D)),
(3.11)
for all ﬁnite subsets D ⊂Zd. For N = 1, the inequality reads 1{|D|≤1} ≤exp(a(D)) and it is
true because a(D) ≥0. Now, suppose it holds true for some N ≥1 and all D. Let D ⊂Zd
be ﬁnite. If D is empty, then ˜TN+1(D; z) = 1 ≤exp(a(D)). If D is not empty, let x be any
element of D and let D′ := D\{x}. Then Proposition 3.12 yields
˜TN+1(D; z) = ˜TN(D′; z) +

Y∋x,
Y∩D′=∅
z(Y) ˜TN(D′ ∪Y; z).
By the induction hypothesis and condition (2.18),
˜TN+1(D; z) ≤ea(D′) +

Y∋x,
Y∩D′=∅
z(Y)ea(D′∪Y) ≤ea(D′∪{x}) = ea(D).
33
Page 24 of 47
S. Jansen, L. Kolesnikov
This completes the inductive proof of (3.11). Passing to the limit N →∞, we get ˜T (D; z) ≤
exp(a(D)) < ∞.
To prove the converse implication (ii) ⇒(i), suppose that T (D; z) is absolutely convergent
for all ﬁnite subsets D. Then ˜T (D; z) < ∞and Proposition 3.12 yields
˜T (D ∪{x}; z) = ˜T (D; z) +

Y∋x,
Y∩D=∅
z(Y) ˜T (D ∪Y; z).
Set a(D) := log ˜T (D; z). Then a(D) ≥0 because ˜T (D; z) ≥1, moreover
ea(D∪{x}) = ea(D) +

Y∋x,
Y∩D=∅
z(Y)ea(D∪Y)
and the inequality (2.18) follows.
⊓⊔
Notice that the preceeding results of Sect. 3.4 can be generalized by proving a more general
version of Lemma 3.11—a direct analogue of Lemma 3.9, where we consider two arbitrary
ﬁnite subsets D0 ⊂Zd and D1 ⊂Zd, instead of the special case where one of the subsets is
a monomer. Naturally, one can view conﬁgurations of polymers not only as conﬁgurations
of monomers but as conﬁgurations of disjoint snippets of arbitrary shape and derive from the
generalized version of Lemma 3.11 a system of Kirkwood–Salsburg equations different from
the one in Proposition 3.12, equations which involve terms of higher order in the activity z.
Those equations in turn lead to the following alternative for Theorem 2.7:
Theorem 3.13 Let (z(X))X∈X be a non-negative activity. The following two conditions are
equivalent:
(i) There exists a function a(·) from the ﬁnite subsets of Zd to [0, ∞) such that a(∅) = 0 and
the following system of inequalities is satisﬁed: For all ﬁnite, non-empty subsets D ⊂Zd
there exists a subset D0 ⊂D such that—setting D1 := D\{D0} — we have

k≥1

{Y1,...,Yk}⊂X
z(Y1) . . . z(Yk)ea(D1∪Y1∪...∪Yk)−a(D1) ≤ea(D1∪D0)−a(D1) −1,
where the sum runs over sets of mutually disjoint polymers {Y1, . . . , Yk} ⊂X such that
Yi ∩D0̸ = ∅and Yi ∩D1 = ∅for all i ∈{1 . . . , k}.
(ii) T (D; z) is absolutely convergent for all ﬁnite subsets D ⊂Zd.
Moreover, if one of the equivalent conditions (hence, both) holds true, then, for all ﬁnite
subsets D ⊂Zd, we have
log T (D; z)
 ≤
∞

k=1
1
k!

(Y1,...,Yk)∈Xk
1l{∃i: Yi∩D̸=∅}
ϕT
k(Y1, . . . , Yk)
z(Y1) · · · z(Yk) ≤a(D).
The details of the proof are left for the reader as an exercise. Notice that the sufﬁcient condition
for convergence given by Theorem 3.13 is more general than the one given by Theorem 2.7.
However, all the proofs of sufﬁcient conditions for systems of subset polymers in Sect. 4 are
using the special case of Theorem 2.7.
Cluster Expansions: Necessary...
Page 25 of 47

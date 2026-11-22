---
doc_id: s10955-022-02992-6
doc_title: "Cluster Expansions: Necessary and Sufficient Convergence Conditions"
section_id: sec-007-24-subset-polymers
section_title: "Subset Polymers"
section_number: 2.4
pages: 12-14
source_pdf: s10955-022-02992-6.pdf
source_sha256: aa73d797a89eaf06
toc_source: outline
doc_brief: "Cluster Expansions: Necessary and Sufficient Convergence Conditions — We prove a new convergence condition for the activity expansion of correlation functions in equilibrium statistical mechanics"
---
and assume that there is a designated collection Eε of bounded Borel sets in Rd, each of
which is contained in some open ball of radius ε, and a chopping map
C : X →P(Eε),
X →C(X)
such that for every X ∈X, C(X) = {E1, . . . , Em} with m ∈N and E1, . . . , Em a set partition
of X. We additionally want to assume that the topological boundary of every snippet is a
λ-null set, i.e., λ(E\E◦) = 0 for all E ∈Eε (where E denotes the topological closure and
E◦the interior of E).
Let Dε be the set of bounded domains D ⊂Rd that can be written as the union of ﬁnitely
many disjoint snippets. The empty set D = ∅is an element of Dε. For two disjoint subsets
D0, D1 ⊂Rd with D0̸ = ∅and for ﬁnitely many objects Y1, . . . , Yk ∈X, k ∈N, set
I(D0; D1; Y1, . . . , Yk) :=
 k
i=1
1l{D0∩Yi̸ =∅, D1∩Yi=∅}
	

1≤i< j≤k
1l{Yi∩Y j=∅}
	
. (2.16)
Theorem 2.6 Let z(·) be a non-negative activity function. The following two conditions are
equivalent:
(i) There exists a non-negative map a : Dε →R+ such that for all D ∈Dε, the map
K ′ ∋F →a(D∪F) is measurable and the following system of inequalities is satisﬁed:
For all non-empty D ∈Dε with C(D) = {E1, . . . , Em} ⊂Eε for some m ∈N, there
exists an s ∈{1, . . . , m} such that—setting D′ := D\Es—we have
∞

k=1
1
k!

Xk I(Es; D′; Y1, . . . , Yk)ea(D′∪Y1∪···∪Yk)−a(D′)λk
z(dY) ≤ea(Es∪D′)−a(D′) −1.
(ii) T (D; z) is absolutely convergent for all D ∈Dε.
Moreover, if one of the equivalent conditions (hence, both) holds true, then, for all D ∈Dε,
we have
log T (D; z)
 ≤
∞

k=1
1
k!

Xk 1l{∃i: Yi∩D̸=∅}
ϕT
k(Y1, . . . , Yk)
λk
z(dY) ≤a(D).
(2.17)
2.4 Subset Polymers
Let X consist of the ﬁnite non-empty subsets of Zd (or any other countable set), and let
X = P(X) be the σ-algebra containing all subsets of X. The reference measure λ is simply
the counting measure. The interaction is a pure hard-core interaction as in Sect. 2.3. Notice
that this setup is a special case of the abstract polymer setup introduced in Sect. 2.2. For a
ﬁnite set D ⊂Zd, deﬁne T (D; z) as in (2.14). In statistical physics T (D; z) corresponds
to the probability that no polymer intersects D. If D is a polymer or a union of disjoint
polymers, it corresponds to a reduced correlation function in the sense of [12].
Notice how in the case of subset polymers every polymer always can be “chopped” in a
canonical way—into a disjoint collection of monomers. Those play the role of snippets from
the previous section—that simpliﬁes the formulation of a criterion for absolute convergence
of the activity expansions ρ (compare next result with Theorem 2.6).
Theorem 2.7 Let (z(X))X∈X be a non-negative activity. The following two conditions are
equivalent:
Cluster Expansions: Necessary...
Page 13 of 47
33
(i) There exists a function a(·) from the ﬁnite subsets of Zd to [0, ∞) such that a(∅) = 0 and
the following system of inequalities is satisﬁed: For all ﬁnite, non-empty subsets D ⊂Zd
there exists an x ∈D such that—setting D′ := D\{x}—we have

Y∈X:
Y∋x, Y∩D′=∅
z(Y)ea(D′∪Y)−a(D′) ≤ea(D′∪{x})−a(D′) −1.
(2.18)
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
(2.19)
The theorem is similar to Claim 1 in [1, Sect. 4.2]. As noted in [1], Theorem 2.7 allows
for an easy recovery of the extended Gruber–Kunz criterion. The criterion is named after
Gruber and Kunz [12], who proved a similar condition but with a strict inequality. See [8]
for a comparison of the Gruber–Kunz criterion to other classical conditions.
Corollary 2.8 Let (z(X))X∈X be a non-negative activity. Suppose there exists some α ≥0
such that for all x ∈Zd,

Y∋x
z(Y) eα|Y| ≤eα −1.
(2.20)
Then T (D; z) is absolutely convergent, for all ﬁnite subsets D ⊂Zd.
Proof Set a(D) := α|D|, where α > 0 satisﬁes the inequality from (2.20). Because of the
additivity of a(·), we have a(D∪Y) = a(D)+a(Y) for all ﬁnite, disjoint subsets D, Y ⊂Zd.
Therefore condition (2.18) becomes

Y∋x:
Y∩D=∅
z(Y) ea(Y) ≤ea({x}) −1,
which depends on D only through the constraint Y ∩D̸ = ∅on the left-hand side. By the
non-negativity of the activity z, it is clearly sufﬁcient that

Y∋x
z(Y) ea(Y) ≤ea({x}) −1,
which holds true for all x ∈Zd because of (2.20).
⊓⊔
Another immediate consequence of Theorem 2.7 is that convergence of cluster expansions
implies exponential decay of the activities in the object size. Precisely, set
V (D) :=

Y∈X:
Y∩D̸=∅
z(Y).
Notice that if the activity is translationally invariant and not identically zero, one can choose
an arbitrary polymer X ∈X with positive activity, say z0 > 0, and obtain the bound
V (D) ≥z0|D|.
(2.21)
33
Page 14 of 47
S. Jansen, L. Kolesnikov
Theorem 2.9 If z(·) is a non-negative activity and T (D; z) is absolutely convergent for all
ﬁnite subsets D ⊂Zd, then necessarily

Y∋x
z(Y)eV (Y) < ∞
for all x ∈Zd.
Proof By condition (i) in Theorem 2.7, evaluated at D′ = ∅, there exists a non-negative
function a(·) such that

Y∋x
z(Y)ea(Y) ≤ea({x}) −1 < ∞.
For any polymer Y ∈X, the value a(Y) is necessarily larger than V (Y) by (2.19) and the
claim follows.
⊓⊔
For translationally invariant systems, Theorem 2.9 says that if the activity expansions are
absolutely convergent, then necessarily the activities are exponentially small in the size of
the object—by (2.21) we can observe that z(X) = O(exp(−z0|X|)) when |X| →∞. Let
us emphasize that the necessary exponential decay is an intrinsic limitation of the activity
expansion, which cannot be eliminated by tinkering with different sufﬁcient convergence
conditions. Rigorous results for one-dimensional and hierarchical models [13, 15] suggest
that the exponential decay is not needed for the convergence of the multi-species virial
expansion, however for general systems this is so far an unproven conjecture.

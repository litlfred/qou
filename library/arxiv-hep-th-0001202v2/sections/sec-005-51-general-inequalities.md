---
doc_id: arxiv-hep-th-0001202v2
doc_title: "Towards cohomology of renormalization: bigrading the combinatorial Hopf algebra of rooted trees"
section_id: sec-005-51-general-inequalities
section_title: "General inequalities"
section_number: 5.1
pages: 7-9
source_pdf: 0001202v2.pdf
source_sha256: b2e3e22ea3d51c0b
doc_brief: "Towards cohomology of renormalization: bigrading the combinatorial Hopf algebra of rooted trees — The renormalization of quantum ﬁeld theory twists the antipode of a non- cocommutative Hopf algebra"
---
prove that they are saturated in HR.
6
5.1 General inequalities
Let H be a commutative graded Hopf algebra with unit e. Let deg be the grading, with
deg(X) ∈ N for all X ∈ H and deg( e) = 0. We assume that H is reduced to scalars by
the counit ¯e.
Let Hk be the set of elements in the kernel of Uk which are in the range of Uk−1, so
that Uk(X) = 0 and Uk−1(X) ⁄= 0, for X ∈ H k. Then we call k the degree of primitivity
of X, writing deg p(X) = k. We let H0 be the set of elements in the kernel of P = U0,
i.e. the scalars. The augmentation ideal fulﬁlls Hc = H/H0 =∑ ∞
k=1 Hk.
To show that deg p(X) ≤ deg(X), suppose that
∆ deg(X)−1(X) =
∑
i
X (1)
i ⊗ . . . ⊗ X (deg(X))
i (21)
has nonscalar entries in H⊗deg(X)
c . Then they are all formed from 1-primitives, in H1,
since the coproduct is homogenous in deg and any element X with deg( X) = 1 also has
degp(X) = 1. Hence deg p is majorized by deg and is thus ﬁnite for each X ∈ H.
We denote by Hn,k the number of linearly inequivalent terms X with weight deg( X) =
n and primitivity deg p(X) = k. Then the generators Hk(x) := ∑
n≥k Hn,k xn satisfy
Hj+k(x) ≤ Hj(x)Hk(x), j, k > 0 . (22)
Proof: It is suﬃcient to show that an element X ∈ H j+k may be labelled by those
terms in ∆( X) that are in Hj ⊗ Hk. To prove this, suppose that X1 and X2 give the same
terms in Hj ⊗ Hk. Now observe that Uj,k := Uj−1 ⊗ Uk−1 projects onto Hj ⊗ Hk, giving
Uj,k ◦ ∆( X1 − X2) = 0. Finally, observe that coassociativity gives
0 = Uj,k ∆( X1 − X2) = P ⊗(j+k) ◦ ∆ j+k−1(X1 − X2) := Uk+j−1(X1 − X2) (23)
which shows that X1 −X2 is (j +k −1)-primitive and hence that X1 and X2 are equivalent
elements of Hj+k. ✷
In consequence of (22) we obtain
Hk(x) ≤ [H1(x)]k . (24)
This reﬂects the fact that the terms in ∆ k−1(X) which belong to H⊗k
1 are suﬃcient to
label elements X ∈ H k. The remarkable feature of the Hopf algebra of rooted trees, to
be proved below, is that all the elements of H⊗k
1 are necessary to label elements of Hk.
As a further comment, we note that (24) may be strengthened if t he Hopf algebra is
cocommutative, since then the order of labels is immaterial. In the ca se of Hladder, with
H 1(x) = x/(1 − x), one thus obtains
H k(x) ≤
∏
j≤k
x
1 − xj (25)
which is in fact saturated by Table 1.
7

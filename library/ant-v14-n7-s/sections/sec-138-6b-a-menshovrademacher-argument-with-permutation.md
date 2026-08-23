---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-138-6b-a-menshovrademacher-argument-with-permutation
section_title: "6B. A Menshov–Rademacher argument with permutations"
section_number: null
pages: 269-270
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
---
[Menshov 1923; Rademacher 1922] may be employed in a wide variety of circumstances; in general
it allows one to replace a supremum of a function | f(u j)| over an index set of size U by a sum of
differences| f(u j)− f(u j−1)| over an index set of size O(log U). In our present setting, these differences
1936 Lillian B. Pierce and Junyan Xu
are differences of partial sums over a box, which are themselves partial sums of the same kind, so that the
Menshov–Rademacher device is a useful tool.
However a typical Menshov–Rademacher argument would not immediately apply in our case, since we
cannot save a power of‖k‖ but typically only a power of kmin, the shortest side of the box. We see this
phenomenon is already present in Lemma 6.1, since we have assumed an orderingk1≤ k2≤···≤ kn for the
side-lengths of the box. Even if we assume in the beginning that we have such an ordering, certain internal
steps in the Menshov–Rademacher argument do not preserve such an ordering, and thus arranging the argu-
ment so that we may apply Lemma 6.1 will require delicate considerations of permutations of the variables.
Our main result in this section is the following:
Proposition 6.2. If 1≤ K1≤ K2≤···≤ Kn≤ q, then
∑
m
|mi|≤2q
max
k≤K
|S(F; m, k)|2r≪n,r,D,1‖K‖2r(log Kn)2nr
n∑
j=0
q(n+ j)/2~Bn,r( j; K)−1 (6-3)
with the implicit constant dependent on n, r, D,1 but independent of q,χ, K, and with
~Bn,r( j; K)=



1 if j= 0,
K
θ j
1 if j= 1,..., n− 1,
(K1··· Kn/2)(2r−1) if j= n, n even,
(K1··· K(n−1)/2)(2r−1)(K(n+1)/2)r if j= n, n odd.
(6-4)
Note that ~Bn,r(n; K)−1 loses one power in decay compared to Bn,r(n; K)−1. In contrast, in the one-
dimensional case, no decay is lost when passing from the nonmaximal estimate to the maximal estimate;
this minor loss will not affect our ﬁnal outcome, and we explain why it arises below.

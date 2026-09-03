---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I:"
section_id: sec-031-92-joint-cumulants
section_title: "Joint cumulants"
section_number: 9.2
pages: 72-73
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
doc_brief: "MOD-φ CONVERGENCE, I: — In this paper, we use the framework of mod- φ convergence to prove pre- cise large or moderate deviations for quite general sequences of real valued random variables (Xn)n∈N"
---
cumulants, that we shall use to prove Theorem 9.7. We present in this paragraph its
deﬁnition and basic properties. Most of this material can be found in Leonov’s and
Shiryaev’s paper [LS59] (see also [JŁR00, Proposition 6.16]).
9.2.1. Preliminaries: set-partitions. We denote by [n] the set{1, . . . ,n}. Recall from Sec-
tion 8.3 that a set partition of [n] is a (non-ordered) family of non-empty disjoint subsets
of S (called parts of the partition), whose union is [n]. For instance,
{{1, 3, 8},{4, 6, 7},{2, 5}}
is a set partition of [8]. Denote Q(n) the set of set partitions of [n]. Then Q(n) may be
endowed with a natural partial order: the reﬁnement order. We say that π is ﬁner than
π′ or π′ coarser than π (and denote π≤ π′) if every part of π is included in a part of
π′.
Lastly, denote µ the Möbius function of the poset Q(n). In this paper, we only use
evaluations of µ at pairs (π,{[n]}) (the second argument is the partition of [n] in only
one part, which is the maximum element of Q(n)), so we shall use abusively the nota-
tion µ(π) for µ(π,{[n]}). In this case, the value of the Möbius function is given by:
µ(π) = µ(π,{[n]}) = (−1)#(π)−1(#(π)− 1)! . (39)
9.2.2. Deﬁnition and properties of joint cumulants. If X1, . . . ,Xr are random variables with
ﬁnite moments on the same probability space (denote E the expectation on this space),
we deﬁne their joint cumulant by
κ(X1, . . . ,Xr) = [ t1··· tr] log
(
E
[
et1X1+···+trXr
])
. (40)
As usual, [t1 . . .tr]F stands for the coefﬁcient of t1··· tr in the series expansion of F
in positive powers of t1, . . . ,tr. Note that joint cumulants are multilinear functions.
In the case where all the Xi’s are equal, we recover the r-th cumulant κ(r)(X) of a
single variable. Using set-partitions, joint cumulants can be expressed in terms of joint
moments, and vice-versa:
E[X1··· Xr] = ∑
π∈Q(r)
∏
C∈π
κ(Xi ; i∈ C); (41)
κ(X1, . . . ,Xr) = ∑
π∈Q(r)
µ(π) ∏
C∈π
E
[
∏
i∈C
Xi
]
. (42)
In these equations, C∈ π shall be understood as “C is a part of the set partitionπ”. Re-
call that µ(π) has an explicit expression given by Equation (39). For example the joint
cumulants of one or two variables are simply the mean of a single random variable
and the covariance of a couple of random variables:
κ(X1) = E[X1] ; κ(X1, X2) = E[X1X2]− E[X1] E[X2].
For three variables, one has
κ(X1, X2, X3) = E[X1X2X3]− E[X1X2] E[X3]− E[X1X3] E[X2]
− E[X2X3] E[X1] + 2 E[X1] E[X2] E[X3].
MOD-φ CONVERGENCE, I 73
Remark 9.10. The most important property of cumulants is their relation with indepen-
dence: if the variables X1, . . . ,Xr can be split in two non-empty sets of variables which
are independent with each other, then κ(X1, . . . ,Xr) vanishes [JŁR00, Proposition 6.16
(v)]. We will not need this property here. In fact, we will prove a more precise version
of it, see Equation (47).
9.2.3. Statement with joint cumulants. Theorems 9.6 and 9.7 have some analog with joint
cumulants. Let{Yα}α∈V be a family of random variables with dependency graphG. As
in Theorem 9.6, we assume that the variables Yα are uniformly bounded by a constant
A: i.e., for all α∈ V,
‖Yα‖∞≤ A.
Consider r subsets V1, V2, . . . ,Vr of V, non necessarily distinct and set Xi = ∑α∈Vi Yα
(for i∈ [r]). We denote Di the maximal number of vertices in Vi adjacent to a given
vertex (not necessarily in Vi). Then one has the following result.
Theorem 9.11. With the notation above,
|κ(X1, . . . ,Xr)|≤ 2r−1 rr−2|V1| (D2 + 1)··· (Dr + 1) Ar.
The proof of this theorem is very similar to the one of Theorem 9.7. However, to sim-
plify notation, we only prove the latter here.

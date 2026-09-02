---
doc_id: arxiv-2007.13108v1
doc_title: "Log concavity and concentration of Lipschitz functions on the Boolean hypercube"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: 2007.13108v1.pdf
source_sha256: b298478f5f5b948d
---
In the Euclidean space Rn, log-concave measures, namely measures whose density is of the
form e−U with U being a convex potential are known to satisfy several concen tration inequali-
ties. For instance, if γ is the standard Gaussian measure on Rn and the probability measure
ν is absolutely continuous with respect to γ with density dν = eV dγ where the potential
V : Rn → R satisﬁes the condition
∇2V ≼ (1 − δ)In, (1)
then for every 1-Lipschitz test function ϕ , we will have Varν[ϕ ] ≤ 1
δ , see e.g., [14]. In fact,
much stronger concentration, for instance in the form of a lo garithmic Sobolev inequality, is
known to hold in this case.
The objective of this work is to try to generalize the notion o f log-concavity to the Boolean
hypercube in a way that analogous concentration inequalities are attained. Deﬁne Cn := {−1, 1}n.
We say that a function ϕ : Cn → R is 1-(Hamming)-Lipschitz if
|ϕ (x) − ϕ (y)| ≤ ‖ x − y‖1, ∀x, y ∈ C n.
Let µ be the uniform measure on Cn. Suppose that dν = eV dµ. Given a 1-Lipschitz function
ϕ , it is a trivial fact that Varν[ϕ ] ≤ n2, and this bound is sharp in general (e.g., take ϕ (x) =
∗ Weizmann Institute of Science. Supported by a European Rese arch Council Starting Grant (ERC StG) and by
an Israel Science Foundation grant no. 715/16.
†Weizmann Institute of Science. Supported by the European Re search Council.
1
∑
i xi and ν which assigns mass 1/ 2 to (−1, · · · , −1) and (1, . . . , 1)). We are interested in
the question of ﬁnding sufﬁcient conditions on the potentia l V , analogous to (1), under which
a nontrivial bound for Varν[ϕ ] is implied. Let us mention that in the case of the continuous
hypercube, concentration results of this nature we obtaine d by Klartag ([10]).
It is clear that any potential V : Cn → R is the restriction of some convex function on Rn
to Cn, meaning that the notion of convexity has to either consider the discrete derivatives of V
or to consider the continuous Hessian applied to a suitably c hosen interpolation. Our suggested
notion of convexity is roughly based on the multi-linear int erpolation, but the formal deﬁnition
will ﬁrst be given in terms of the logarithmic Laplace transf orm. Deﬁne,
L[ν](x) = log
∫
Cn
e⟨x,y⟩dν(y), ∀x ∈ Rn.
The function L[ν] is known as the log-Laplace transform of the measure ν. We are now ready
to deﬁne our main notion of semi-log-concavity.
Deﬁnition 1. (Semi log-concave measures). Given a measure ν on Cn, We say that ν is β -semi-
log-concave if
∇2L[ν](x) ≼ β In, ∀x ∈ Rn, (2)
where the inequality is in the positive-deﬁnite sense.
Our main theorem gives a nontrivial concentration bound for Lipschitz functions with re-
spect to such measures.
Theorem 2. Let β ≥ 1. If ν is a β -semi-log-concave probability measure on Cn and ϕ is
1-Lipschitz, then
Varν[ϕ ] ≤ Cβn 2−c/β
where C, c > 0 are universal constants.
The theorem shows in particular that for any β ∈ R there exists n large enough such that
β -semi-log-concave measures on Cn admit nontrivial concentration.
Before we proceed, let us give an alternative and slightly st ronger notion of semi-log-
concavity which could hopefully shed some light and give bet ter intuition regarding the relation
to the usual notion of log concavity in Rn. We ﬁrst need to recall the multi-linear extension of
the measure into the continuous hypercube, [−1, 1]n. Given a function f : Cn → R, it is known
that there is a unique function ˆf : 2 [n] → R such that
f (x) =
∑
A⊂[n]
ˆf (A)
∏
i∈A
xi. (3)
The function ˆf is known as the Walsh-Fourier transform of f . Observing that the above form
makes sense as a function from [−1, 1]n to R, we refer to this as the multi-linear (or harmonic)
extension of f . Since the two coincide on Cn, below we allow ourselves to use the same notation
for both the function and its multi-linear extension. The fo llowing fact is attained via a simple
calculation, see Section 4 below.
Fact 3. Suppose that
∇2 log dν
dµ (x) ≼ β In, ∀x ∈ [−1, 1]n. (4)
Then ν is (β + 3)-semi-log-concave.
2
Thus, a corollary to Theorem 2 is that the condition (4) impli es that every 1-Lipschitz func-
tion ϕ satisﬁes Varν[ϕ ] ≤ C(β + 3)n2−c/(β+3).
Remark 4. Let f be the multi-linear extension of dν
dµ. Since f is harmonic and since ∇ log f =
∇2f
f − ∇f ⊗ 2
f 2 , we see that in order for f to be log-concave, the Hessian of f can have at most
one positive eigenvalue, due to which the family of log-conc ave functions, or in other words
functions satisfying condition (4) with β = 0 , is rather restricted. Semi-log-concave measures
are a much richer family, as demonstrated below.

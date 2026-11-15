---
doc_id: 1-s20-s002212362200012x-main
doc_title: "Journal of Functional Analysis Log concavity and concentration of Lipschitz functions on the Boolean hypercube"
section_id: sec-001-1-introduction
section_title: "Introduction"
section_number: 1
pages: 2-4
source_pdf: 1-s2.0-S002212362200012X-main.pdf
source_sha256: 6fc7d28c8d40bf42
toc_source: outline
doc_brief: "Journal of Functional Analysis Log concavity and concentration of Lipschitz functions on the Boolean hypercube — V Article history: Received 17 December 2020 Accepted 13 January 2022 Available online"
---
In the Euclidean space Rn, log-concave measures, namely measures whose density is of 
the form e−U with U being a convex potential are known to satisfy several concentration 
inequalities. For instance, if a probability measure ν is absolutely continuous with respect 
to the standard Gaussian measure γ on Rn, with a corresponding density dν = eV dγ
where the potential V : Rn →R satisﬁes the condition
∇2V ⪯(1 −δ)In,
(1)
then any 1-Lipschitz test function ϕ, will satisfy Varν[ϕ] ≤1
δ, see e.g., [15]. In fact, much 
stronger concentration, for instance in the form of a logarithmic Sobolev inequality, is 
known to hold in this case.
The objective of this work is to try to generalize the notion of log-concavity to the 
Boolean hypercube in a way that analogous concentration inequalities are attained. De-
ﬁne Cn := {−1, 1}n. We say that a function ϕ : Cn →R is 1-(Hamming)-Lipschitz 
if
|ϕ(x) −ϕ(y)| ≤∥x −y∥1,
∀x, y ∈Cn.
Let μ be the uniform measure on Cn. Suppose that dν = eV dμ. Given a 1-Lipschitz 
function ϕ, it is a trivial fact that Varν[ϕ] ≤n2, and this bound is sharp in general (e.g., 
take ϕ(x) = 
i xi and ν which assigns mass 1/2 to (−1, · · · , −1) and (1, . . . , 1)). We are 
interested in the question of ﬁnding suﬃcient conditions on the potential V , analogous 
to (1), under which a nontrivial bound for Varν[ϕ] is implied. Let us mention that in the 
case of the continuous hypercube, concentration results of this nature were obtained by 
Klartag ([11]).
It is clear that any potential V : Cn →R is the restriction of some convex function 
on Rn to Cn, meaning that the notion of convexity has to either consider the discrete 
derivatives of V or to consider the continuous Hessian applied to a suitably chosen 
interpolation. Our suggested notion of convexity is roughly based on the multi-linear 
interpolation, but the formal deﬁnition will ﬁrst be given in terms of the logarithmic 
Laplace transform. Deﬁne,
L[ν](x) = log

Cn
e⟨x,y⟩dν(y),
∀x ∈Rn.
The function L[ν] is known as the log-Laplace transform of the measure ν. We are now 
ready to deﬁne our main notion of semi-log-concavity.
Deﬁnition 1. (Semi log-concave measures). Given a measure ν on Cn, we say that ν is 
β-semi-log-concave if
R. Eldan, O. Shamir / Journal of Functional Analysis 282 (2022) 109392
3
∇2L[ν](x) ⪯βIn,
∀x ∈Rn,
(2)
where the inequality is in the positive-deﬁnite sense.
Our main theorem gives a nontrivial concentration bound for Lipschitz functions with 
respect to such measures.
Theorem 2. Let β ≥1. If ν is a β-semi-log-concave probability measure on Cn and ϕ is 
1-Lipschitz, then
Varν[ϕ] ≤Cβ2n2−c/β
where C, c > 0 are universal constants.
Remark 3. Our proof shows that one can take for example C = 10 and c = 1/20, however 
these constants are probably very sub-optimal.
The theorem shows in particular that for any β ∈R there exists n large enough such 
that β-semi-log-concave measures on Cn admit nontrivial concentration.
Before we proceed, let us give an alternative and slightly stronger notion of semi-log-
concavity which could hopefully shed some light and give better intuition regarding the 
relation to the usual notion of log concavity in Rn. We ﬁrst need to recall the multi-linear
extension of the measure into the continuous hypercube, Cn := [−1, 1]n. Given a function 
f : Cn →R, there is a unique function ˆf : 2[n] →R such that
f(x) =

A⊂[n]
ˆf(A)

i∈A
xi.
(3)
The function ˆf : 2[n] →R is known as the Walsh-Fourier transform of f and satisﬁes 
ˆf(A) = 2−n 
x∈Cn f(x) 
i∈A xi. Observing that the above form makes sense as a func-
tion from Cn to R, we refer to this as the multi-linear (or harmonic) extension of f. 
Since the two coincide on Cn, below we allow ourselves to use the same notation for both 
the function and its multi-linear extension. The following fact is attained via a simple 
calculation, see Section 4 below.
Fact 4. Suppose that
∇2 log dν
dμ(x) ⪯βIn,
∀x ∈[−1, 1]n.
(4)
Then ν is (β + 3)-semi-log-concave.
Thus, a corollary to Theorem 2 is that the condition (4) implies that every 1-Lipschitz 
function ϕ satisﬁes Varν[ϕ] ≤C(β + 3)n2−c/(β+3).
4
R. Eldan, O. Shamir / Journal of Functional Analysis 282 (2022) 109392
Remark 5. Let f be the multi-linear extension of dν
dμ. Since f is harmonic and since 
∇2 log f = ∇2f
f
−∇f ⊗2
f 2 , we see that in order for f to be log-concave, the Hessian of 
f can have at most one positive eigenvalue, due to which the family of log-concave 
functions, or in other words functions satisfying condition (4) with β = 0, is rather 
restricted. Semi-log-concave measures are a much richer family, as demonstrated below.

---
doc_id: arxiv-math-0304010v1
doc_title: "Kerov's central limit theorem for the Plancherel measure on Young diagrams"
section_id: page-039
section_title: "Page 39"
section_number: null
pages: 39-39
source_pdf: 0304010v1.pdf
source_sha256: fc2296c027b3feb0
toc_source: undetermined
doc_brief: "Kerov's central limit theorem for the Plancherel measure on Young diagrams — Consider random Young diagrams with ﬁxed number n of boxes, dis- tributed according to the Plancherel measure Mn."
---
Deﬁnition 8.5. Fix n = 1, 2, . . .. To any λ ∈Yn we assign a probability measure
bλ ∈M0 as follows: bλ is the transition measure of the scaled diagram ¯λ( · ) ∈D0.
Equivalently, bλ is the push–forward of the transition measure (8.2)–(8.3) under the
shrinking x 7→n−1/2x of the real axis.
Viewing λ as the random element of the probability space (Yn, Mn), we interpret
bλ as a random probability measure.
The next result is simply a reformulation of Theorem 5.5. Recall that, by Deﬁ-
nition 8.2, we may view A as a function algebra on M0.
Theorem 8.6 (Law of large numbers for transition measures).
As n →∞, the random measures bλ concentrate near the Dirac mass at the
element µs-c ∈M0, the semi–circle distribution (8.4).
In more detail, let c
Mn stand for the push–forward of the measure Mn under the
correspondence λ 7→bλ. Then
lim
n→∞⟨f, c
Mn⟩= f[µs-c],
∀f ∈A.
Proof. Immediately follows from Theorem 5.5, Proposition 8.4 and Deﬁnition 8.2.
□
Now, our aim is to describe the ﬂuctuations of the random measures bλ around
the semi–circle distribution µs-c.
We do not know if this can be achieved by a
simple application of Theorem 7.1. The reason is that the transform ¯λ( · ) 7→bλ
is highly nonlinear. It turns out, however, that the proof of Theorem 7.1 can be
readily translated to the language of transition measures: it suﬃces to deal with
eh2, eh3, . . . instead of ep2, ep3, . . . .
The role of the polynomials uk(x) is played now by the polynomials tk(x). These
are slightly modiﬁed Chebyshev polynomials of the ﬁrst kind. By deﬁnition,
tk(x) = 2Tk( x
2) =
[k/2]
X
j=0
(−1)j
k
k −j
k −j
j

xk−2j = k
[k/2]
X
j=0
(−1)j (k −1 −j)!
j!(k −2j)! xk−2j ,
(8.5)
where k = 1, 2, . . . and the Tk’s are the conventional Chebyshev polynomials, see
[Sz], [Er].
We also have (cf. (7.4), (7.5))
tk(2 cos θ) = 2 cos(kθ),
k = 1, 2, . . .,
(8.6)
and
Z 2
−2
tk(x)tl(x)
1
2π
√
4 −x2 dx = δk,l ,
k, l = 1, 2, . . . .
(8.7)
Given λ ∈Yn , we set (cf. (7.1))
b∆λ = √n(bλ −µs-c).
(8.7a)
This is a compactly supported measure on R (in general, not a positive one). Drop-
ping λ, which is viewed as the random element of (Yn, Mn), we interpret (8.7a) as
a random measure, which we denote by b∆(n).
Next, we set
t(n)
k
=
Z
R
tk(x) b∆(n)(dx).
This is a random variable, deﬁned on the probability space (Yn, Mn).
39

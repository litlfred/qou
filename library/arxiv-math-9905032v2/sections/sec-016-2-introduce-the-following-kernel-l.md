---
doc_id: arxiv-math-9905032v2
doc_title: "ASYMPTOTICS OF PLANCHEREL MEASURES FOR SYMMETRIC GROUPS"
section_id: sec-016-2-introduce-the-following-kernel-l
section_title: "Introduce the following kernel L"
section_number: 2
pages: 12-14
source_pdf: 9905032v2.pdf
source_sha256: ba933d4cb484964b
doc_brief: "ASYMPTOTICS OF PLANCHEREL MEASURES FOR SYMMETRIC GROUPS — We consider the asymptotics of the Plancherel mea- sures on partitions of n as n goes to inﬁnity."
---
L(x, y; θ) =





0 , xy > 0 ,
1
x − y
θ(|x|+|y|)/ 2
Γ( |x| + 1
2 ) Γ( |y| + 1
2) , xy < 0 .
We shall consider the kernels K and L as operators in the ℓ2 space on
Z + 1
2.
We recall that simple multiplicative formulas (for example , the hook
formula) are known for the number dim λ in (1.1). For our purposes, it
is convenient to rewrite the hook formula in the following de terminantal
form. Let λ = ( p1, . . . , pd | q1, . . . , qd) be the Frobenius coordinates of
λ, see Section 1.2. We have
dim λ
|λ|! = det
[ 1
(pi + qj + 1) pi! qi!
]
1≤i,j ≤d
.(2.2)
The following proposition is a straightforward computatio n using (2.2).
Proposition 2.1. Let λ be a partition. Then
M θ (λ) = e−θ det
[
L(xi, xj; θ)
]
1≤i,j ≤s
,(2.3)
ASYMPTOTICS OF PLANCHEREL MEASURES 13
where Fr(λ) = {x1, . . . , xs} ⊂ Z + 1
2 are the modiﬁed Frobenius coordi-
nates of λ.
Let Fr ∗
(
M θ)
be the push-forward of M θ under the map Fr. Note
that the image of Fr consists of sets X ⊂ Z + 1
2 having equally many
positive and negative elements. For other X ⊂ Z + 1
2, the right-hand
side of (2.3) can be easily seen to vanish. Therefore Fr ∗
(
M θ)
is a
determinantal point process (see the Appendix) correspond ing to L,
that is, its conﬁguration probabilities are determinants o f the form
(2.3).
Corollary 2.2. det(1 + L) = eθ .
This follows from the fact that M θ is a probability measure. This is
explained in Propositions A.1 and A.4 in the Appendix. Note t hat, in
general, one needs to check that L is a trace class operator. However,
because of the special form of L, it suﬃces to check a weaker claim –
that L is a Hilbert–Schmidt operator, which is immediate.
Theorem 1 now follows from general properties of determinan tal
point processes (see Proposition A.6 in the Appendix) and th e fol-
lowing
Proposition 2.3. K = L (1 + L)−1.
We shall need three following identities for Bessel functio ns which are
degeneration of the identities (3.13–15) in [6] for the hype rgeometric
function. The ﬁrst identity is due to Lommel (see [39], Secti on 3.2 or
[12], 7.2.(60))
Jν (2z) J1−ν (2z) + J−ν (2z) Jν −1(2z) = sin πν
π z .(2.4)
The other two identities are the following.
Lemma 2.4. For any ν ⁄= 0, −1, −2, . . . and any z ⁄= 0 we have
∞∑
m=0
1
m + ν
zm
m! Jm(2z) = Γ( ν) Jν (2z)
zν ,(2.5)
∞∑
m=0
1
m + ν
zm
m! Jm+1(2z) = 1
z − Γ( ν) Jν −1(2z)
zν .(2.6)
Proof. Another identity due to Lommel (see [39], Section 5.23, or [1 2],
7.15.(10)) reads
∞∑
m=0
Γ( ν − s + m)
Γ( ν + m + 1)
zm
m! Jm+s(2z) = Γ( ν − s)
Γ( s + 1)
Jν (2z)
zν −s .

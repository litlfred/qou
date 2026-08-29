---
doc_id: arxiv-math-9905032v2
doc_title: "ASYMPTOTICS OF PLANCHEREL MEASURES FOR SYMMETRIC GROUPS"
section_id: sec-017-14-a-borodin-a-okounkov-and-g-olshanski
section_title: "A. BORODIN, A. OKOUNKOV, AND G. OLSHANSKI"
section_number: 14
pages: 14-16
source_pdf: 9905032v2.pdf
source_sha256: ba933d4cb484964b
doc_brief: "ASYMPTOTICS OF PLANCHEREL MEASURES FOR SYMMETRIC GROUPS — We consider the asymptotics of the Plancherel mea- sures on partitions of n as n goes to inﬁnity."
---
Substituting s = 0 we get (2.5). Substituting s = 1 yields
∞∑
m=0
1
(m + ν)(m + ν − 1)
zm
m! Jm+1(2z) = Γ( ν − 1) Jν (2z)
zν −1 .(2.7)
Let r(ν, z) the diﬀerence of the left-hand side and the right-hand side
in (2.6). Using (2.7) and the recurrence relation
Jν +1(2z) − ν
z Jν (2z) + Jν −1(2z) = 0 (2.8)
we ﬁnd that r(ν + 1 , z) = r(ν, z). Hence for any z it is a periodic
function of ν and it suﬃces to show that lim ν →∞ r(ν, z) = 0. Clearly,
the left-hand side in (2.6) goes to 0 as ν → ∞. From the deﬁning series
for Jν it is clear that
Jν (2z) ∼ zν
Γ( ν + 1) , ν → ∞ ,(2.9)
which implies that the right-hand side of (2.6) also goes to 0 as ν → ∞.
This concludes the proof.
Proof of Proposition. It is convenient to set z =
√
θ. Since the operator
1 + L is invertible we have to check that
K + K L − L = 0 .
This is clearly true for z = 0; therefore, it suﬃces to check that
˙K + ˙K L + K ˙L − ˙L = 0 ,(2.10)
where ˙K = ∂ K
∂z and ˙L = ∂ L
∂z . Using the formulas
d
dz Jx(2z) = −2Jx+1(2z) + x
z Jx(2z) (2.11)
= 2 Jx−1(2z) − x
z Jx(2z)
one computes
˙K(x, y) =
{ J|x|− 1
2
J|y|+ 1
2
+ J|x|+ 1
2
J|y|− 1
2
, xy > 0 ,
sgn(x)
(
J|x|− 1
2
J|y|− 1
2
− J|x|+ 1
2
J|y|+ 1
2
)
, xy < 0 ,
where Jx = Jx(2z). Similarly,
˙L(x, y) =





0 , xy > 0 ,
sgn(x) z|x|+|y|−1
Γ( |x| + 1
2 ) Γ( |y| + 1
2) , xy < 0 .
Now the veriﬁcation of (2.10) becomes a straightforward app lication of
the formulas (2.5) and (2.6), except for the occurrence of th e singularity
ASYMPTOTICS OF PLANCHEREL MEASURES 15
ν ∈ Z≤0 in those formulas. This singularity is resolved using (2.4) . This
concludes the proof of Proposition 2.3 and Theorem 1.
2.2. Proof of Theorem 2. Recall that by construction
Fr(λ) =
(
D(λ) + 1
2
)
△
(
Z≤0 − 1
2
)
.
Let us check that this and Proposition A.8 implies Theorem 2. In
Proposition A.8 we substitute
X = Z + 1
2 , Z = Z≤0 − 1
2 , K = K .
By deﬁnition, set
ε(x) = sgn( x)x+1/ 2 , x ∈ Z + 1
2 .
We have the following
Lemma 2.5. K△(x, y) = ε(x) ε(y) J(x − 1
2, y − 1
2)
It is clear that since the ε-factors cancel out of all determinantal
formulas, this lemma and Proposition A.8 establish the equi valence of
Theorems 1 and 2.
Proof of lemma. Using the relation
J−n = (−1)nJn
and the deﬁnition of K one computes
K(x, y) = sgn( x) ε(x) ε(y) J(x − 1
2 , y − 1
2) , x ⁄= y .(2.12)
Clearly, the relation (2.12) remains valid for x = y > 0. It remains to
consider the case x = y < 0. In this case we have to show that
1 − K(x, x) = J(x − 1
2 , y − 1
2) , x ∈ Z≤0 − 1
2 .
Rewrite it as
1 − J(k, k) = J(−k − 1, −k − 1) , k = −x − 1
2 ∈ Z≥0 .(2.13)
By (2.14) this is equivalent to
1 −
∞∑
m=0
(−1)m (2k + m + 2)m
Γ( k + m + 2)Γ( k + m + 2)
θk+m+1
m!
=
∞∑
n=0
(−1)n (−2k + n)n
Γ( −k + n + 1)Γ( −k + n + 1)
θ−k+n
n! .
Examine the right–hand side. The terms with n = 0, . . . , k− 1 vanish
because then 1 /Γ( −k + n + 1) = 0. The term with n = k is equal to
1, which corresponds to 1 in the left–hand side. Next, the ter ms with
n = k + 1, . . . ,2k vanish because for these values of n, the expression
(−2k + n)n vanishes. Finally, for n ≥ 2k + 1, set n = 2k + 1 +m. Then

---
doc_id: arxiv-math-0006051v1
doc_title: "Finite and p-adic polylogarithms"
section_id: sec-005-6-amnon-besser
section_title: "AMNON BESSER"
section_number: 6
pages: 6-8
source_pdf: 0006051v1.pdf
source_sha256: 10483e75bd3655ea
doc_brief: "Finite and p-adic polylogarithms — 8 sections: AMNON BESSER; Introduction; The proof"
---
Proposition 3.1. We deﬁne a sequence of functions fk(z, S ) inductively as fol-
lows:
f0(z, S ) = S
1 − S , f k+1(z, S ) =
∫ S
z
fk(z, t )d log t .
Then, when z, S ∈ W and z ≡ S (mod p) the following formula holds:
−
n∑
k=0
(−1)kk! ·
(n
k
)
fk+1(z, S ) logn− k(S) = ( −1)nn! (Ln+1(z) − Ln+1(S)) .(3.1)
We would like to remark on the potential importance of this formula. T he con-
struction of p-adic polylogarithms by Coleman is an inductive procedure. At each
step the degree n polylogarithm Li n is constructed as a locally analytic function
satisfying the diﬀerential equation d Lin(z) = Li n− 1(z)d log z. This determines Li n
up to a locally constant function and a Frobenius condition replaces t his by a
globally constant function ambiguity. As remarked by Kontsevich th e distribution
relation removes the ambiguity completely. The formula above allows f or a diﬀerent
approach: The functions fn have no ambiguity in their deﬁnitions and are in fact
given by converging power series in S and z − S. Once the fn are given, the for-
mula determines Ln up to a locally constant function and the distribution relation
determines it completely. The functions Li n can be determined from the Ln.
For our purposes, the formula is also useful because it allows us to r elate the
values of Ln at two congruent points.
Lemma 3.2. Suppose z ∈ X and w ∈ W . Then
p− nfn(z, z (1 + pw)) ≡ z
1 − z
wn
n! (mod p) .
The proof is a direct computation similar to the proof of proposition 2 .3. Suppose
now that z is a root of unity. Then log( z(1 + pw)) ≡ pw (mod p2). Thus, using
(3.1) we immediately obtain
p− n− 1(−1)nn!(Ln+1(z(1 + pw)) − Ln+1(z)) ≡ cn+1
z
1 − z wn+1 (mod p)
with
cn+1 =
n∑
k=0
(−1)k k!
(k + 1)!
(n
k
)
= 1
n + 1
n∑
k=0
(−1)k
(n + 1
k + 1
)
= 1
n + 1 .
so
p− n(Ln(z(1 + pw)) − Ln(z)) ≡ −(−1)n 1
n!
z
1 − z wn (mod p) .
We can deﬁne the derivation D on functions of two variables as D = S(1−S)∂/∂S +
z(1 − z)∂/∂z . One easily obtains the following
Lemma 3.3. If z, S ∈ X and z ≡ S (mod p) then pk|Dfk(z, S ).
FINITE AND p-ADIC POLYLOGARITHMS 7
Diﬀerentiating the key formula we ﬁnd, with S = z(1 + pw),
p− n(−1)nn!(DLn+1(S) − DLn+1(z))
= p− n
n∑
k=0
k!
(n
k
) [
Dfk+1(z, S ) logn− k(S) + (n − k)fk+1(z, S ) logn− k− 1(S)
]
(1 − S)
≡
n∑
k=0
k!
(n
k
)
(n − k)fk+1(z, S ) logn− k− 1(S)(1 − z) ≡ dn+1zw n (mod p) ,
where
dn+1 =
n∑
k=0
(−1)k k!
(k + 1)!
(n
k
)
(n − k) = −
n∑
l=1
(−1)l
(n
l
)
= 1 .
Let z be a root of unity. Since log( z) = 0 we have
DLn(z) = z(1 − z)
[
Lin− 1(z) 1
z
+
n− 1∑
m=1
(−1)m
m!
(
Lin− m− 1(z) 1
z logm(z) + m Lin− m(z) logm− 1(z) 1
z
) ]
= (1 − z)(Lin− 1(z) − Lin− 1(z)) = 0 .
Thus we ﬁnd
p− nDLn(S) ≡ −(−1)n n
n! zw n− 1 (mod p) .
Suppose now that we let F (z) = ∑ n
m=1 emLm(z) logn− m(z). Substituting ﬁrst of
all a root of unity in X we ﬁnd DF (z) = en− 1(1 − z)Ln− 1(z) so we should have
en− 1 = −1. Then
p1− nDF (S) =
n∑
m=1
em
(
DLm(S) logn− m(S)
+ (n − m)Lm(S) logn− m− 1(S)(1 − S)
)
p1− n
≡
n∑
m=1
em
(
− (−1)m m
m! zw m− 1 · wn− m
+ (n − m)(p− mLm(z) − (−1)m 1
m!
z
1 − z wm)wn− m− 1(1 − z)
)
= −zw n− 1
n∑
m=1
((−1)mem( m
m! + (n − m) 1
m! ))
+
n∑
m=1
em(n − m)p− mLm(z) (mod p) .
We wish to choose the coeﬃcients em in such a way that this expression is inde-
pendent of w. Since in the second sum we know by corollary 2.2 that p− mLm(z)
is not congruent to 0 modulo p (as a function of z) we see that the only non zero

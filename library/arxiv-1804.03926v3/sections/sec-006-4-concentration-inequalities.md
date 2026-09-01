---
doc_id: arxiv-1804.03926v3
doc_title: "Weighted Poincaré inequalities, concentration inequalities and tail bounds related to Stein kernels in dimension one"
section_id: sec-006-4-concentration-inequalities
section_title: "Concentration inequalities"
section_number: 4
pages: 21-28
source_pdf: 1804.03926v3.pdf
source_sha256: 8ad8e2d5a8881a5b
---
We state in this section some concentration inequalities related to Stein kernels in dimension one. Due
to the use of covariance identities stated in Section 2, the proofs indeed heavily rely on dimension one.
We can however notice that it is known from [LNP15] that a uniformly bounded (multi-dimensional)
Stein kernel ensures a sub-Gaussian concentration rate. We derive sharp sub-Gaussian inequalities
in Theorem 14. It is also reasonable to think that results suc h as in Theorem 18 could be generalized
to higher dimension, but this seems rather nontrivial and is left as an open question.
From Proposition 4, Section 2, we get the following proposit ion.
Proposition 13 Assume that ν has a a ﬁnite ﬁrst moment and a density p with respect to the
Lebesgue measure that has a connected support. If g ∈L∞ (ν) and h ∈L1 (ν) are absolutely contin-
uous and h is 1-Lipschitz, then
|Cov (g,h )| ≤ E
[ ⏐⏐g′⏐⏐·τv
]
, (44)
whereτv is given in (6) and is the Stein kernel. Furthermore, if the St ein kernel is uniformly bounded,
that is τv ∈L∞ (ν), then
|Cov (g,h )| ≤ ‖τv‖∞ E
[ ⏐⏐g′⏐⏐]
. (45)
Proof. Start from identity (12) and simply remark that, for hν (x) =x,
⏐⏐¯Lh (x)
⏐⏐ =
⏐⏐⏐⏐
1
p (x)
∫
R
kν (x,y )h′ (y)dy
⏐⏐⏐⏐
≤ ‖h′‖∞
p (x)
∫
R
kν (x,y )dy
=
‖‖h′‖‖
∞τv (x) .
21
Applying techniques similar to those developed in [BGH01] f or Gaussian vectors (see especially
Theorem 2.2), we have the following Gaussian type concentra tion inequalities when the Stein kernel
is uniformly bounded.
Theorem 14 Assume that ν has a ﬁnite ﬁrst moment and a density p with respect to the Lebesgue
measure that has a connected support. Assume also that the St ein kernel τv is uniformly bounded,
τv ∈ L∞ (ν), and denote c = ‖τv‖−1
∞ . Then the following concentration inequalities hold. For an y
1-Lipschitz function g,
P
(
g ≥
∫
gdν +r
)
≤e−cr2/ 2 . (46)
Furthermore, the function
Tg (r) =ecr2/ 2E (g − Eg) 1{g−Eg≥r}
is non-increasing in r ≥ 0. In particular, for all r> 0,
P (g − Eg ≥r) ≤ E (g − Eg)+
e−cr2/ 2
r , (47)
P (|g − Eg| ≥ r) ≤ E |g − Eg|e−cr2/ 2
r . (48)
Inequality (46) is closely related to Chatterjee’s Gaussia n coupling for random variables with
bounded Stein kernel [Cha12]. To our knowledge reﬁned conce ntration inequalities such as (47) and
(48) are only available in the literature for Gaussian rando m variables or by extension, for strongly
log-concave measures. Indeed, these inequalities can be established for strongly log-concave measures
as an immediate consequence of the Caﬀarelli contraction the orem, which states that such measures
can be realized as the pushforward of the Gaussian measure by a Lipschitz function. We refer to
these inequalities as generalized Mills’ type inequalitie s since taking g =Id in Inequality (48) allows
to recover Mills’ inequality (see for instance [D¨ um10]): if Z is the normal distribution, then for any
t> 0,
P (|Z|>t ) ≤
√
2
π
e−t2/ 2
t .
Here the setting of a bounded Stein kernel is much larger and i nclude for instance smooth pertur-
bations of the normal distribution that are Lipschitz and bo unded away from zero (see Remark 2.9
in [LNP15]) or bounded perturbations of measures having a bo unded Stein kernel and a density
bounded away from zero around its mean (see Section 3.4 above for more details).
Note that Beta distributions Bα,β as deﬁned in (24) are known to be log-concave of order α
whenever α ≥ 1 and β ≥ 1, [BL14]. Using this fact, Bobkov and Ledoux [BL14], Propos ition B.10,
prove the following concentration inequality: for X a random variable with distribution B (α,β ),
α ≥ 1, β ≥ 1 and any r ≥ 0,
P (|X − E (X)| ≥ r) ≤ 2e−(α +β )r2/ 8 .
Actually, for any α,β > 0, the Beta distribution B (α,β ) belongs to the Pearson’s class of
distributions and its Stein kernel is given a polynomial of o rder 2, τB(α,β ) (x) = (α +β)−1x (1 −x)
on [0, 1] (see [LRS17]). In particular,
‖‖τB(α,β )
‖‖
∞ = 4−1 (α +β)−1 and Theorem 14 applies even in
the case where α,β < 1, for which the B (α,β ) distribution is not log-concave.
22
Corollary 15 Letα,β > 0. Take X a random variable with distribution B (α,β ) andg a 1-Lipschitz
function on [0, 1]. Then for all r> 0,
P (g (X) − E [g (X)] ≥r) ≤ exp
(
−2 (α +β)r2)
.
Furthermore, for all r> 0,
P (g (X) − E [g (X)] ≥r) ≤ E (g − Eg)+
e−2(α +β )r2
r ,
P (|g (X) − E [g (X)]| ≥ r) ≤ E |g − Eg|e−2(α +β )r2
r (49)
and, if α,β ≥ 1,
P (|g (X) − E [g (X)]| ≥ r) ≤ C√α +β + 1
e−2(α +β )r2
r (50)
with the value C = 2. 5 - for which we always have C (α +β + 1)−1/ 2 < 2 - that holds.
Proof. We only need to prove (50). Start from (49). It is suﬃcient to p rove the following inequality,
E |g − Eg| ≤ 2. 5√α +β + 1 .
By proposition B.7 of [LRS17], by setting m the median of g (X), we have
E |g −m| ≤ 2. 5√α +β + 1
∫ 1
0
√
x (1 −x)
⏐⏐g′ (x)
⏐⏐dBα,β (x)
≤ 2. 5√α +β + 1
∫ 1
0
√
x (1 −x)dBα,β (x)
= 2. 5B (α + 1/ 2,β + 1/ 2)√α +β + 1B (α,β ) .
Now the conclusion follows from the basic inequalities, B (α + 1/ 2,β + 1/ 2) ≤ B (α,β )/ 2 and
E |g − Eg| ≤ 2E |g −m|.
Proof of Theorem 14. Takeg to be 1-Lipschitz and mean zero with respect to ν, then for any
λ ≥ 0,
E
[
geλg
]
= Cov
(
g,e λg
)
≤ ‖ τv‖∞ E
[ ⏐⏐⏐⏐
(
eλg
) ′
⏐⏐⏐⏐
]
≤ λ
c E
[
eλg
]
.
Deﬁne J (λ) = log E
[
eλg]
, λ ≥ 0. We thus have the following diﬀerential inequality, J ′ (λ) ≤ λ/c .
Since J (0) = 0, this implies that J (λ) ≤λ 2/ (2c). Equivalently, E
[
eλg]
≤eλ 2/ (2c), which by the use
of Chebyshev’s inequality gives (46).
Now, assume that as a random variable g has a continuous positive density p on the whole real
line. Take f =U (g) where U is a non-decreasing (piecewise) diﬀerentiable function on R. Applying
(45), we get
E [gU (g)] ≤ E
[
U ′ (g)
]
/c . (51)
23
Let G be the distribution function of g. Given r > 0 and ε > 0, applying (51) to the function
U (x) = min
{
(x −r)+,ε
}
leads to
∫ r+ε
r
x (x −h)dG (x) +ε
∫ +∞
r+ε
xdG (x) ≤ G (r +ε) −G (r)
c .
Dividing by ε and letting ε tend to 0, we obtain, for all h> 0,
∫ ∞
r
xdG (x) ≤ p (r)
c .
Thus, the function V (r) =
∫ +∞
r xdG (x) =
∫ +∞
r xp (x)dx satisﬁes the diﬀerential inequality V (r) ≤
−V ′ (r)/ (cr), that is
(logV (r))′ ≤ −cr ,
which is equivalent to saying that logV (r)+cr2/ 2 is non-increasing, and therefore the functionTg (r)
is non-increasing.
We relax now the condition on Stein kernels, by assuming thatit is ”sub-linear”. This condition is
fulﬁlled by many important distributions, for instance by the Gaussian, Gamma or Beta distributions.
We deduce a sub-Gamma behavior.
Theorem 16 Assume that ν has a ﬁnite ﬁrst moment and a density p with respect to the Lebesgue
measure that has a connected support. Assume also that the St ein kernel τv is sub-linear, that is
τv(x) ≤a |x −µ | +b, where µ is the mean value of ν. Then for any 1-Lipschitz function g and any
r> 0,
P
(
g ≥
∫
gdν +r
)
≤e− r2
2ar+2b . (52)
When g = Id, inequality (52) was proved by Nourdin and Viens [NV09] unde r the stronger
condition that τv(x) ≤a (x −µ) +b (which induces that the support of ν is bounded from below if
a> 0).
Proof. Takeg to be 1-Lipschitz and mean zero with respect to ν. Whithout loss of generality, we
may assume thatg is bounded (otherwise we approximateg by thresholding its largest values). Then
for any λ ≥ 0,
E
[
geλg
]
= Cov
(
g,e λg
)
≤ E
[ ⏐⏐⏐⏐
(
eλg
) ′
⏐⏐⏐⏐τv
]
≤ λE
[
eλgτv
]
. (53)
Furthermore,
E
[
eλgτv
]
≤aE
[
|X −µ |eλg (X)
]
+bE
[
eλg
]
(54)
and E
[
|X −µ |eλg (X)]
= E [(X −µ)h (X)] whereh (x) = sign (x −µ) exp (λg (x)) and sign (x −µ) =
2 · 1 {x ≥µ } − 1. As h′ (x) = sign (x −µ)λg ′ (x) exp (λg (x)) a.s. , we get
E
[
|X −µ |eλg (X)
]
=λE
[
sign (X −µ)g′ (X)eλg (X)τv (X)
]
≤λE
[
eλgτv
]
,
24
which gives, by combining with (54),
E
[
eλgτv
]
≤λaE
[
eλgτv
]
+bE
[
eλg
]
.
If λ< 1/a , this gives
E
[
eλgτv
]
≤ b
1 −λa E
[
eλg
]
. (55)
Combining (53) and (55), we obtain, for any λ< 1/a ,
E
[
geλg
]
≤ λb
1 −λa E
[
eλg
]
.
Deﬁne J (λ) = log E
[
eλg]
, λ ≥ 0. We thus have the following diﬀerential inequality,
J ′ (λ) ≤ λb
1 −λa.
Since J (0) = 0, this implies that J (λ) ≤ λ 2b/ (2(1 −λa)). Equivalently, E
[
eλg]
≤ eλ 2b/ (2(1−λa )),
which by the use of Chebyshev’s inequality gives (46).
Actually, particularizing to the variable X itself, we have the following concentration bounds, in
the spirit of the generalized Mills’ type inequalities obta ined in Theorem 14.
Theorem 17 Assume that ν has a ﬁnite ﬁrst moment and a density p with respect to the Lebesgue
measure that has a connected support. Assume also that the St ein kernel τv is ”sub-linear”, that is
τv(x) ≤a |x −µ | +b for some a> 0 and b ≥ 0, where µ is the mean value of ν. Then the function
T (r) = (ar +b)−b/a 2
er/a E
[
(X −µ) 1{X−µ ≥r}
]
is non-increasing in r ≥ 0. In particular, for all r> 0,
P (X ≥µ +r) ≤ E (X −µ)+
(ar +b)b/a 2
e−r/a
r , (56)
P (|X −µ | ≥ r) ≤ E |X −µ | (ar +b)b/a 2
e−r/a
r . (57)
The concentration bounds (56) and (57), that seem to be new, h ave an interest for large values
ofr, where they improve upon Theorem 16 if a> 0, due to the factor 2 in front of the constant a in
the right-hand side of (52).
Proof. The proof is essentially an adaptation of the proof of Theorem 14. Without loss of generality,
assume that the support of p is R and denote g (X) = X −µ where X ∼ν. Take f =U (g) where
U is a non-decreasing piecewise diﬀerentiable function on R. Applying (44), we get
E [gU (g)] ≤ E
[
τνU ′ (g)
]
≤aE
[
|g|U ′ (g)
]
+bE
[
U ′ (g)
]
. (58)
Let G be the distribution function of g (X). Given r >0 and ε >0, applying (58) to the function
U (x) = min
{
(x −r)+,ε
}
leads to
∫ r+ε
r
x (x −r)dG (x) +ε
∫ +∞
r+ε
xdG (x) ≤
∫ r+ε
r
(ax +b)dG (x) .
25
Dividing by ε and letting ε tend to 0, we obtain, for all r> 0,
∫ ∞
r
xdG (x) ≤ (ar +b)p (r +µ) .
Thus, the function V (r) =
∫ +∞
r xdG (x) =
∫ +∞
r xp (x +µ)dx satisﬁes the diﬀerential inequality
V (r) ≤ −(a + b
r)V ′ (r), that is
(logV (r))′ ≤ − r
ar +b = b
a2
a
ar +b − 1
a ,
which is equivalent to saying that logV (r)+r/a −ba−2 ln (ar +b) is non-increasing, and therefore the
function T (r) is non-increasing on R+. This directly gives (56). By applying (56) to the deviation s
at the right of the mean for −X, we also get
P (X ≤µ −r) ≤ E (X −µ)−
(ar +b)b/a 2
e−r/a
r .
Combining the last inequality with (56) yields (57).
Let us now state a more general theorem.
Theorem 18 Assume that ν has a ﬁnite ﬁrst moment, a density p with respect to the Lebesgue
measure that has a connected support and denote τν its Stein kernel. Set X a random variable of
distribution ν. Take f a 1-Lipschitz function with mean zero with respect to ν and assume that f
has an exponential moment with respect to ν, that is there exists a> 0 such that E
[
eaf (X)]
< +∞.
Then for any λ ∈ (0,a ),
E
[
eλf (X)
]
≤ E
[
eλ 2τ ν (X)
]
. (59)
Consequently, if we denote ψ τ (λ) = ln E
[
eλ 2τ ν (X)
]
∈ [0, +∞] and ψ ∗
τ (t) = sup λ ∈(0,a ) {tλ −ψ τ (λ)}
the Fenchel-Legendre dual function of ψ λ , then for any r> 0,
P (f (X)>r ) ∨ P (f (X)< −r) ≤ exp (−ψ ∗
τ (r)) . (60)
Theorem 18 states that the concentration of Lipschitz funct ions taken on a real random variable
with existing Stein kernel is controlled by the behavior of the exponential moments of the Stein kernel
itself - if it indeed admits ﬁnite exponential moments.
Let us now brieﬂy detail how to recover from Theorem 18 some re sults of Theorems 14 and 16,
although with less accurate constants. If ‖τν ‖∞< +∞, then inequality (59) directly implies
E
[
eλf (X)
]
≤eλ 2‖τ ν ‖∞ ,
which gives
P (f (X)>r ) ∨ P (f (X)< −r) ≤ exp
(
− r2
4 ‖τν ‖∞
)
.
The latter inequality takes the form of Inequality (46) of Th eorem 14, although with a factor 1/ 2 in
the argument of the exponential in the right-hand side of the inequality.
Assume now, as in Theorem 16, that the Stein kernelτν is sub-linear, that is there exista,b ∈ R+
such thatτν (x) ≤a (x −µ) +b, where µ is the mean value of ν. Inequality (59) implies in this case,
E
[
eλf (X)
]
≤ E
[
eaλ 2(X−µ )
]
ebλ 2
. (61)
26
The latter inequality being valid for any f being 1-Lipschitz and centered with respect to ν, we can
apply it for f (X) =X −µ. This gives
E
[
eλ (X−µ )
]
≤ E
[
eaλ 2(X−µ )
]
ebλ 2
.
Now, considering λ<a −1, we have by H¨ older’s inequality,E
[
eaλ 2(X−µ )
]
≤ E
[
eλ (X−µ )] aλ
. Plugging
this estimate in the last inequality and rearranging the ter ms of the inequality gives
E
[
eλ (X−µ )
]
≤e
bλ 2
1− λa .
Going back to inequality (61), we obtain, for any λ ∈
(
0,a −1)
,
E
[
eλf (X)
]
≤ E
[
eλ (X−µ )
] aλ
ebλ 2
≤ebλ 2( λa
1− λa +1) =e
bλ 2
1− λa .
By the use of Cram` er-Chernoﬀ method, this gives the result of Theorem 16, although with a constant
1/ 2 in the argument of the exponential term controlling the dev iations.
Proof. First note that Inequality (60) is direct consequence of Ine quality (59) via the use of the
Cram` er-Chernoﬀ method (see for instance Section 2.2 of [BLM13]). To prove Inequality (59), also
note that by Lemma 19 below, it suﬃces to prove that for any λ ∈ (0,a ),
E
[
λf (X)eλf (X)
]
≤ E
[
λ 2τν (X)eλf (X)
]
. (62)
Takeλ ∈ (0,a ), it holds by identity (12),
E
[
f (X)eλf (X)
]
= Cov
(
f (X),e λf (X)
)
= E
[
λf ′ (X) ¯L (λf ) (X)eλf (X)
]
.
Hence, we obtain
E
[
f (X)eλf (X)
]
≤λ 2E
[ ⏐⏐f ′ (X)
⏐⏐τν (X)eλf (X)
]
≤ E
[
λ 2τν (X)eλf (X)
]
.
Inequality (62) is thus proved, which completes the proof.
Lemma 19 TakeX a random variable on a measurable space (X, T ). Take g and h two measurable
functions from X to R such that
E
[
g (X)eg(X)
]
≤ E
[
h (X)eg(X)
]
< +∞ . (63)
Then it holds,
E
[
eg(X)
]
≤ E
[
eh(X)
]
. (64)
Lemma 19 summarizes the essence of the argument used in the proof of Theorem 2.3 of [BGH01].
We could not ﬁnd a reference in the literature for Lemma 19. We point out that Lemma 19 may have
an interest by itself as it should be very handy when dealing w ith concentration inequalities using
the Cram` er-Chernoﬀ method. Its scope may thus go beyond our framework related to the behavior
of the Stein kernel.
27
Proof. Note that if E
[
eh(X)]
= + ∞ then Inequality (64) is satisﬁed. We assume now that
E
[
eh(X)]
< +∞ and β = ln
(
E
[
eh(X)])
. By setting U = h (X) −β, we get E
[
eU]
= 1 and so,
by the duality formula for the entropy (see for instance Theo rem 4.13 in [BLM13]), we have
E
[
Ue g(X)
]
≤ Ent
(
eg(X)
)
= E
[
g (X)eg(X)
]
− E
[
eg(X)
]
ln
(
E
[
eg(X)
])
.
Furthermore,
E
[
g (X)eg(X)
]
−β E
[
eg(X)
]
≤ E
[
Ue g(X)
]
.
Putting the above inequalities together, we obtain β ≥ ln
(
E
[
eg(X)])
, which is equivalent to (64).

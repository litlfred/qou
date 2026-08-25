---
doc_id: arxiv-math-0304010v1
doc_title: "KEROV’S CENTRAL LIMIT THEOREM FOR THE PLANCHEREL MEASURE ON YOUNG DIAGRAMS"
section_id: sec-003-2-λx-ω-x-x-r-71
section_title: "(¯λ(x)− Ω( x)), x ∈ R. (7.1)"
section_number: 2
pages: 33-40
source_pdf: 0304010v1.pdf
source_sha256: fc2296c027b3feb0
doc_brief: "KEROV’S CENTRAL LIMIT THEOREM FOR THE PLANCHEREL MEASURE ON YOUNG DIAGRAMS — Consider random Young diagrams with ﬁxed number n of boxes, dis- tributed according to the Plancherel measure Mn."
---
This is a continuous function on R with compact support. Dropping λ, which we
consider as the random element from the probability space ( Yn, Mn), we interpret
(7.1) as a random function ∆ (n)(x).
For any polynomial v∈ R[x], the integral
v(n) =
∫
R
v(x)∆ (n)(x)dx (7.2)
makes sense (because ∆ (n) is compactly supported) and is a random variable. We
aim to show that the random variables (7.2), where v ranges over R[x], are asymp-
totically Gaussian.
The result will be stated in terms of the Chebyshev polynomia ls of the second
kind. Instead of the conventional polynomials Uk(x) (see [Sz], [Er]) we prefer to
deal with slightly modiﬁed polynomials
uk(x) = Uk(x/2) =
[k/2]∑
j=0
(−1)j
(k− j
j
)
xk−2j , k = 0, 1, 2, . . . . (7.3)
Note that
uk(2 cos θ) = sin((k + 1)θ)
sin θ (7.4)
and ∫ 2
−2
uk(x)ul(x)
√
4− x2
2π = δk,l , k, l = 0, 1, 2, . . . . (7.5)
33
Theorem 7.1 (Central limit theorem for Y oung diagrams).
According to (7.2), let
u(n)
k =
∫
R
uk(x)∆ (n)(dx), k = 1, 2, . . . ,
and let, as before, ξ2, ξ3, . . . stand for a system of independent standard Gaussians.
We have {
u(n)
k
}
k≥1
d
−→
{ ξk+1√
k + 1
}
k≥1
, n →∞ .
Recall that “
d
−→” means convergence in distribution.
Note that u(n)
0 ≡ 0, which explains why we start with k = 1, not k = 0. The
theorem is proved at the end of the section. The scheme of the p roof is as follows.
We remark that the moments of ∆ (n) (i.e., the random variables v(n), where the v’s
are monomials) are expressed in terms of the elements ~pk, appropriately centered
and scaled. To evaluate the asymptotics of the correspondin g random variables
we employ Theorem 6.1. The main work reduces to expressing th e (centered and
scaled) elements ~pk through the elements ηk and vice versa, up to lower degree
terms.
As in§6, it is convenient to deal with the extended algebra Aext⊃ A. We extend
the deﬁnition of deg 1(· ) to Aext as explained in §6.
We introduce the elements q1, q2, . . .∈ Aext, which are centered and scaled ver-
sions of the elements ~p2,~p3, . . .:
qk =









~pk+1− (2m)!
m!m! (p#
1 )m
(k + 1)(p#
1 )k/2
, if k is odd, k = 2m− 1, where m = 1, 2, . . .,
~pk+1
(k + 1)(p#
1 )k/2
, if k is even, k = 2m, where m = 1, 2, . . . .
(7.6)
Since 1
2~p2 = p1 and p1 = p#
1 , we have q1 = 0.
Proposition 7.2. For any λ∈ Y,
∫
R
xk∆ λ(x)dx = qk+1(λ)
k + 1 , k = 0, 1, . . . . (7.7)
Proof. Set n =|λ|. By the deﬁnition of ∆ λ(x), see (7.1),
∫
R
xk∆ λ(x)dx =√n
∫
R
xk ¯λ(x)−| x|
2 dx−√n
∫
R
xk Ω( x)−| x|
2 dx.
By Proposition 2.2, for any k = 0, 1, . . .,
√n
∫
R
xk ¯λ(x)−| x|
2 dx = n−(k+1)/2
∫
R
xk λ(x)−| x|
2 dx
= 1
(k+1)(k+2)
~pk+2(λ)
n(k+1)/2 = 1
(k+1)(k+2)
~pk+2
(p#
1 )(k+1)/2
(λ).
34
By Propositions 2.2 and 5.3, for any k = 0, 1, . . .,
√n
∫
R
xk Ω( x)−| x|
2 dx =
√n~pk+2[Ω]
(k + 1)(k + 2)
=
√n
(k + 1)(k + 2) ·



(2m)!
m!m! , if k is even, k = 2m− 2, where m = 1, 2, . . .,
0, if k is odd.
Combining this with the deﬁnition of q1, q2, . . ., we get (7.7). □
In order to apply Theorem 6.1 we need the expression of p#
k in terms of q2, q3, . . .
within lower degree terms. We obtain this in two steps. First , using a trick, we
deduce from Proposition 3.7 a formula expressing any qk through p#
2 , p#
3 , . . . , up
to lower degree terms. See Proposition 7.3. Next, we invert t his formula, see
Proposition 7.4. One could derive the result directly from P roposition 3.3 but this
way turns out to be more diﬃcult.
Proposition 7.3. For any k = 2, 3, . . .,
qk =
[ k− 2
2 ]∑
j=0
(k
j
) p#
k−2j
(p#
1 )(k−2j)/2
+ . . . , (7.8)
where dots mean a remainder term with deg1(· ) < 0.
Note that the elements occurring in the numerator of the righ t–hand side are
p#
2 , p#
3 , . . . but not p#
1 .
Proof. The claim of the proposition is equivalent to the following: for any k =
3, 4, . . .,
~pk =
[ k− 3
2 ]∑
j=0
k↓j+1
j! p#
k−1−2j (p#
1 )j +



(2m)!
m!m! (p#
1 )m, if k is even, k = 2m,
0, if k is odd.
+terms with deg 1(· ) < k− 1.
(7.9)
We shall deduce this from Proposition 3.7, which expresses ~pk as a polynomial in
p#
1 , p#
2 , . . ., up to terms of lower weight. A nontrivial point is how to swit ch from
the weight ﬁltration to the Kerov ﬁltration.
Write the exact expansion of ~pk through p#
1 , p#
2 , . . .,
~pk =
∑
ν
aν (p#
1 )ν1(p#
2 )ν2 . . . ,
where aν are certain coeﬃcients. Let us set
‖ν‖= 2ν1 + 3ν2 + 4ν3 + . . . , ‖ν‖′ = 2ν1 + 2ν2 + 3ν3 + . . . ,
so that
‖ν‖′ =‖ν‖−(ν2 + ν3 + . . . ). (7.10)
35
We have
wt((p#
1 )ν1(p#
2 )ν2 . . .) =‖ν‖, deg1((p#
1 )ν1(p#
2 )ν2 . . .)≤‖ν‖′.
By Proposition 3.7, we know all coeﬃcients aν with the maximal value of ‖ν‖(it
equals k), while we need all coeﬃcients with ‖ν‖′≥ k− 1. By (7.10), ‖ν‖′ does not
exceed k, and there are 3 possible cases:
•‖ν‖′ =‖ν‖= k. Then ν2 = ν3 =··· = 0, k = 2 ν1, so that k is even; write it
as 2 m. The corresponding monomial is ( p#
1 )k/2.
•‖ν‖′ = k− 1,‖ν‖= k. Then ν2 + ν3 +··· = 1, i.e., exactly one of the numbers
ν2,ν3, . . . equals 1. The corresponding monomial is of the form
p#
k−1−2j(p#
1 )j , j = ν1 = 0, 1, . . . ,[ k−3
2 ]. (7.11)
•‖ν‖′ =‖ν‖= k− 1. Then ν2 = ν3 =··· = 0, k is odd, and the corresponding
monomial is ( p#
1 )(k−1)/2.
In the ﬁrst and second cases, ‖ν‖takes the maximal value k, and then the
coeﬃcients aν are known from Proposition 3.7. In the third case, ‖ν‖is no longer
maximal, so that Proposition 3.7 does not tell us what is the c oeﬃcient. However,
an additional argument will imply that it is actually 0.
Indeed, in the third case k must be odd, which implies that ~pk is antisymmetric
with respect to “inv”, see (2.17). On the other hand, by virtu e of (4.10), any
monomial in p#
1 , p#
2 , . . . is either symmetric or antisymmetric. Therefore, in the
expansion of ~pk only antisymmetric monomials can occur. Since p#
1 is symmetric,
the monomial ( p#
1 )(k−1)/2 is also symmetric, so that it does not appear.
Thus, we have proved that the top degree component of ~pk is obtained from the
top weight terms as given in Proposition 3.7; we simply keep a ll terms proportional
either to ( p#
1 )k/2 or to a monomial of the form (7.11), and remove all the remaini ng
terms. This procedure leads to (7.9). □
In the next proposition we invert (7.8).
Proposition 7.4. For any k≥ 2,
p#
k
(p#
1 )k/2
=
[ k−2
2 ]∑
j=0
(−1)j k
k− j
(k− j
j
)
qk−2j + . . . , (7.12)
where dots mean a remainder term with deg1(· ) < 0.
Proof. We employ the following combinatorial inversion formula, see [Ri,§2.4, (10)]:
Let a0, a1, a2, . . . , b0, b1, b2, . . . be formal variables. Then


ak =
[k/2]∑
j=0
(k
j
)
bk−2j



k=0,1,...
⇐⇒


bk =
[k/2]∑
j=0
(−1)j k
k− j
(k− j
j
)
ak−2j



k=0,1,...
(7.13)
36
Set
a0 = a1 = 0, a k = qk (k≥ 2); b0 = b1 = 0, b k = p#
k
(p#
1 )k/2
(k≥ 2).
The relations (7.8) coincide with the ﬁrst system in (7.13), up to remainder terms
of negative degree. These terms can be neglected, because th ey aﬀect only similar
remainder terms in the inverse relations. These inverse rel ations are given then by
the second system in (7.13). This leads to (7.12). □
Proof of Theorem 7.1. We rewrite (7.12) as follows. For any k≥ 2,
[ k−2
2 ]
∑
j=0
(−1)j
(k− 1− j
j
) qk−2j
k− 2j = 1
k
p#
k
(p#
1 )k/2
+ Rk ,
where Rk∈ Aext is a certain element such that deg 1(Rk) < 0.
In the left–hand side, we may extend the summation up to [ k−1
2 ], because q1 = 0.
Comparing this with formula (7.3) for uk−1(x) and formula (7.7) for the moments
of ∆ λ, we conclude that
u(n)
k−1 = 1√
k η(n)
k + R(n)
k k≥ 2.
Or, equivalently,
u(n)
k = 1√k+1 η(n)
k+1 + R(n)
k+1 k≥ 1.
As n→∞ , the asymptotics of the (mixed) moments of the random variab les
u(n)
1 , u(n)
2 , . . . is the same as that for the random variables 1√
k+1 η(n)
k+1 , k = 1, 2, . . . .
Indeed, the remainder terms of negative degree do not aﬀect t he asymptotics, see
Proposition 6.2. As for the moments of the random variables η(n)
k+1, their asymp-
totics has been evaluated in the proof of Theorem 6.1. This co ncludes the proof. □
§8. The central limit theorem for
transition measures of Young diagrams
LetM denote the set of probability measures on R with compact support, and
letM0⊂M be the subset of measures with the ﬁrst moment equal to 0.
Proposition 8.1. There exists a bijective correspondence ω↔ µ betweenD and
M, which is also a bijection D0↔M 0. It is characterized by the relation
exp
∫
R
σ′(x)dx
x− z =
∫
R
µ(dx)
1− x
z
, (8.1)
where z∈ C\ I, where I⊂ R stands for a suﬃciently large interval, and, as usual,
σ(x) = 1
2 (ω(x)−| x|).
Proof. See [Ke2], [Ke4]. □
We call µ the transition measure of the continual diagram ω. In [Ke4], the
correspondence σ′↦→µ deﬁned by (8.1) is deﬁned in a greater generality, so that its
37
range is the set of all (not necessarily compactly supported ) probability measures
on R. (Note that in [Ke4], the symbol M refers to the latter set.)
Formula (8.1) means that the two sequences,
{
−k
∫
R
xk−1σ′(x)dx
}
k=1,2,...
and
{ ∫
R
xkµ(dx)
}
k=1,2,...
,
are related to each other in exactly the same way as the two sys tems of generators
of the algebra Λ, {pk}k=1,2,... and{hk}k=1,2,....
From now on and up to the end of this section we restrict oursel ves to measures
µ from the subset M0.
Deﬁnition 8.2. Recall that the algebra A can be realized as the image of Λ under
the morphism (2.18), and let ~h2,~h3, . . . denote the image in A of the elements
h2, h3, . . . .
We realize A as an algebra of functions on M0 by setting
~hk[µ] =
∫
R
xkµ(dx), µ ∈M 0, k = 2, 3, . . . .
Equivalently, for any f∈ A, we set f [µ] = f [ω], where ω↔ µ and f [ω] is understood
according to Deﬁnition 2.10 b).
Proposition 8.3. Let ω = λ(· ), where λ is a Young diagram, and let {xi}m+1
i=1 ,
{yj}m
j=1 be the local extrema of λ(x), see §2. Then the transition measure of ω is
supported by the ﬁnite set {x1, . . . , xm+1} and is given by the following formula:
µ =
m+1∑
i=1
µiδxi , (8.2)
where δx denotes the Dirac mass at x and the weights µ1, . . . , µm+1 are the coeﬃ-
cients in the expansion
∏ m
j=1(z− yj)
∏ m+1
i=1 (z− xi)
=
m+1∑
i=1
µi
z− xi
. (8.3)
Proof. See [Ke2], [Ke4]. □
The measure µ deﬁned by (8.2)–(8.3) is called the transition measure of a given
Young diagram λ. For a justiﬁcation of this term and more details, see [Ke2], [Ke3],
[Ke4].
Proposition 8.4. The transition measure of Ω ∈D 0 is the “semi–circle distribu-
tion ” µs-c supported by [−2, 2],
µs-c(dx) = 1
2π
√
4− x2. (8.4)
Proof. See [Ke2], [Ke4]. □
38
Deﬁnition 8.5. Fix n = 1, 2, . . .. To any λ∈ Yn we assign a probability measure
ˆλ∈M 0 as follows: ˆλ is the transition measure of the scaled diagram ¯λ(· )∈D 0.
Equivalently,ˆλ is the push–forward of the transition measure (8.2)–(8.3) u nder the
shrinking x↦→n−1/2x of the real axis.
Viewing λ as the random element of the probability space ( Yn, Mn), we interpret
ˆλ as a random probability measure.
The next result is simply a reformulation of Theorem 5.5. Rec all that, by Deﬁ-
nition 8.2, we may view A as a function algebra on M0.
Theorem 8.6 (Law of large numbers for transition measures).
As n → ∞, the random measures ˆλ concentrate near the Dirac mass at the
element µs-c∈M 0, the semi–circle distribution (8.4).
In more detail, let ˆMn stand for the push–forward of the measure Mn under the
correspondence λ↦→ˆλ. Then
lim
n→∞
⟨f,ˆMn⟩= f [µs-c], ∀f∈ A.
Proof. Immediately follows from Theorem 5.5, Proposition 8.4 and D eﬁnition 8.2.
□
Now, our aim is to describe the ﬂuctuations of the random meas uresˆλ around
the semi–circle distribution µs-c. We do not know if this can be achieved by a
simple application of Theorem 7.1. The reason is that the tra nsform ¯λ(· )↦→ˆλ
is highly nonlinear. It turns out, however, that the proof of Theorem 7.1 can be
readily translated to the language of transition measures: it suﬃces to deal with
~h2,~h3, . . . instead of ~p2,~p3, . . . .
The role of the polynomials uk(x) is played now by the polynomials tk(x). These
are slightly modiﬁed Chebyshev polynomials of the ﬁrst kind . By deﬁnition,
tk(x) = 2 Tk( x
2 ) =
[k/2]∑
j=0
(−1)j k
k− j
(k− j
j
)
xk−2j = k
[k/2]∑
j=0
(−1)j (k− 1− j)!
j!(k− 2j)! xk−2j ,
(8.5)
where k = 1 , 2, . . . and the Tk’s are the conventional Chebyshev polynomials, see
[Sz], [Er].
We also have (cf. (7.4), (7.5))
tk(2 cos θ) = 2 cos( kθ), k = 1, 2, . . . , (8.6)
and ∫ 2
−2
tk(x)tl(x) 1
2π
√
4− x2 dx = δk,l , k, l = 1, 2, . . . . (8.7)
Given λ∈ Yn , we set (cf. (7.1))
ˆ∆ λ =√n(ˆλ− µs-c). (8.7a)
This is a compactly supported measure on R (in general, not a positive one). Drop-
ping λ, which is viewed as the random element of ( Yn, Mn), we interpret (8.7a) as
a random measure, which we denote by ˆ∆ (n).
Next, we set
t(n)
k =
∫
R
tk(x)ˆ∆ (n)(dx).
This is a random variable, deﬁned on the probability space ( Yn, Mn).
39
Proposition 8.7. We have t(n)
1 = t(n)
2 ≡ 0.
Proof. Recall that for any measure from M0, the ﬁrst moment equals zero. In
particular, this holds for ˆλ and µs-c, which implies t(n)
1 ≡ 0.
Next, the relation h2 = 1

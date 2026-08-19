---
doc_id: arxiv-2404.03933v2
doc_title: "TENSOR POWERS OF VECTOR REPRESENTATION OF Uq(sl2) AT EVEN ROOTS OF UNITY"
section_id: sec-007-9-the-asymptotic-of-the-character-and-plancherel
section_title: "The asymptotic of the character and Plancherel measures for Uq(sl2)"
section_number: 9
pages: 23-28
source_pdf: 2404.03933v2.pdf
source_sha256: 48aff6e97e1f1267
doc_brief: "TENSOR POWERS OF VECTOR REPRESENTATION OF Uq(sl2) AT EVEN ROOTS OF UNITY — We study the decomposition of tensor powers of two dimensional irreducible rep- resentations of quantum sl2 at even roots of"
---
In this section we will compute the asymptotic of the character and the Plancherel measures
on tilting submodules of T (1)⊗N whenN→∞ . We will start with computing the asymptotic
of the multiplicity of T (k)⊂T (1)⊗N.
9.1. The asymptotic of the multiplicity function. Note that in the tensor productT (1)⊗N
only submodules T (k) with k≡N mod 2 can occur. For sufficiently large k the decomposition
of T (1)⊗T (k) is 2l periodic. This is why it is natural to write N in base 2l:
N = 2lN1 +N0, N 0 = 0, 1,..., 2l− 1.
Writingk =lk1 +k0 we see that N =k mod 2 have the following implication:
• N0 is even and k≡ 0 mod 2 orN0 is odd and k≡ 1 mod 2 implyk0≡N0 mod 2
• N0 is even and k≡ 1 mod 2 orN0 is odd and k≡ 0 mod 2 implyk0≡ (N0 + 1) mod 2
Let us define a parameter
γ =
(
1, if k0≡ (N0 + 1) mod 2,
0, if k0≡N0 mod 2.
In the limit N→∞ k0 remains discrete, and its parity is controlled by γ. Later we will see
that limiting distribution is independent of both N0 and γ.
The following theorem describes the pointwise asymptotic of the multiplicity function
Theorem 9.1. Assume that N = 2lN1 +N0, k = k1l +k0, N1→∞ , k1→∞ such that l,
N0 = 0,..., 2l− 1, k0 = 0,...,l − 1 and ξ = k1
2N1
remain fixed. Then the asymptotic of the
multiplicity has the following form:
(11) M (l)
T (k)(N) =
µ(l)
k0 (ξ,N 0,γ )√2π 2lN1
exp(2lN1S(ξ))

1 +O
 1
N1

where
S(ξ) =−
1−ξ
2

ln
1−ξ
2

−
1 +ξ
2

ln
1 +ξ
2

,
and if k0̸=l− 1
µ(l)
k0 (ξ,N 0,γ ) = 22+N0ξp
(1−ξ2)1+N0
1−ξ
1 +ξ
γl
2
1
1+ξ

1+ξ
1−ξ
l−k0
2
− 1
1−ξ

1+ξ
1−ξ
−l−k0
2

1+ξ
1−ξ
l
2
−

1+ξ
1−ξ
−l
2
,
if k0 =l− 1
µ(l)
k0 (ξ,N 0,γ ) = 22+N0ξp
(1−ξ2)1+N0
1
1 +ξ
1−ξ
1 +ξ
l(1+γ)−1
2
.
24 ANNA LACHOWSKA, OLGA POSTNOV A, NICOLAI RESHETIKHIN, AND DMITRY SOLOVYEV
The proof of this theorem is presented in Appendix C.1.
9.2. The pointwise asymptotic of the character measure density. Now let us find the
asymptotic of the character measure density function p(l)
N (k;t) when k, N→∞ in the same
way as in Theorem 9.1. All we have to do is to combine the results of Theorem 9.1 with the
asymptotical expansions of characters.
Using explicit formulae for characters we find that when k0̸=l− 1
chT (k)(et)
(chT (1)(et))N = (et(k0+1) +e−t(k0+1))(etk1l−e−tk1l)
et−e−t
e2t−e−2t
et−e−t
−N
=
= (et(k0+1) +e−t(k0+1))etγl
(et−e−t)(et +e−t)N0
 eξt
et +e−t
2lN1
(1 +o(1)),
and when k0 =l− 1
chT (lk1+l−1)(et)
(chT (1)(et))N = etl(1+γ)
(et−e−t)(et +e−t)N0
 eξt
et +e−t
2lN1
(1 +o(1)).
Combining these formulae with the results of Theorem 9.1 we obtain that if N = 2N1l +N0,
k = k1l +k0, and N1, k1→∞ such that l, k0, N0, t and ξ = k1
2N1
remain fixed we have the
following pointwise asymptotic for the probability measure density function
(12) p(l)
N (k;t) =
ν(l)
k0 (ξ,N 0,γ ;t)√2π 2lN1
exp(2lN1(S(ξ)−f(t) +tξ))

1 +O
 1
N1

,
where
f(t) = ln(et +e−t),
and if k0̸=l− 1
ν(l)
k0 (ξ,N 0,γ ;t) = etγl (et(k0+1)+e−t(k0+1))
(et−e−t)(et+e−t)N0
22+N0ξ√
(1−ξ2)1+N0

1−ξ
1+ξ
γl
2
1
1+ξ

1+ξ
1−ξ
l−k02
− 1
1−ξ

1+ξ
1−ξ
−l−k02

1+ξ
1−ξ
l
2
−

1+ξ
1−ξ
−l
2
,
if k0 =l− 1
ν(l)
k0 (ξ,N 0,γ ;t) = etl(1+γ)
(et−e−t)(et +e−t)N0
22+N0ξp
(1−ξ2)1+N0
1
1 +ξ
1−ξ
1 +ξ
l(1+γ)−1
2
.
By definition ξ∈ [0, 1). Note that the function S(ξ), the large deviation rate function has
its maximum at the isolated critical point ξ0, i.e.
∂
∂ξ (S(ξ)−f(t) +tξ) = 0
has a unique solution
(13) ξ0 = et−e−t
et +e−t.
In addition, S(ξ0) = 0.
TENSOR POWERS 25
Thus, we have a typical large deviation behavior of the density function p(l)
N (k;t): it is
exponentially decaying when ξ̸=ξ0 and it decays as N
− 1
2
1 when ξ =ξ0. Thus, asymptotically,
the character measure concentrates in the neighborhood of ξ =ξ0.
9.3. The asymptotic of the character measure for Uq(sl2). The following theorem de-
scribes the weak limit of the character probability measure for Uq(sl2).
Theorem 9.2. Letξ0 be as in (13), N = 2lN1 +N0 and N1→∞ such that N0, l, t are fixed.
Then for k = k1l +k0, random variables k0 and α = k1−2N1ξ0√2N1
converge to random variables
on{0,...,l − 1}× R and the character probability distribution weakly converges to the tensor
product of two distributions p1(•;t)⊗p2(•;t) on{0,...,l − 1}× R. The distribution p1(•;t) is
a discrete probability distribution on k0 = 0, 1,...,l − 1 with density given by
(14) p1(k0;t) =
( (et(k0+1)+e−t(k0+1))(et(l−1−k0)−e−t(l−1−k0))
l(etl−e−tl) , if k0 = 0,...,l − 2,
1
l, if k0 =l− 1.
The distribution p2(•;t) is a Gaussian distribution on R with density given by
(15) p2(α;t) =
r
l
2π cosh(t)e−α2l
2 (cosh(t))2
.
The proof of this theorem is presented in Appendix C.2. The meaning of weak convergence
is also recalled there.
Note that the asymptotic of the character measure is derived for N0 being fixed, but it does
not depend on N0. The only dependence is the condition N =k mod 2. It implies that:
• for even N0 the summation over k =k1l +k0 amounts for the summation over k0 and
k1 of the same parity,
• for odd N0 the summation over k = k1l +k0 amounts for the summation over k0 and
k1 of the opposite parity.
In the limit N1→∞ this dependence on N0 disappears. Dependence on γ disappears as well.
Period 2l coversk1, k1 + 1, which for any k1 includes all values of k0 = 0,...,l − 1, so parity
of k0 doesn’t have to be controlled.
This is why we conjecture that the asymptotic does not depend on N0. To be precise,
consider a sequence
N (p) = 2lN (p)
1 +N (p)
0 , N (p)
1 →∞ as p→∞,
and N (p)
0 = 0, 1,..., 2l− 1. For each p∈ Z>0 let k = lk1 +k0∈ Z≥0 be the random variable
distributed with respect to the character measure p(l)
N (p)(k;t). We expect the following is true.
As p→∞ with l, t being fixed and k = 2N (p)
1 ξ0 +
q
2N (p)
1 α, α∈ R, the character measure
converges to the measure on{0,...,l − 1}× R with the density p1(k0;t)p2(α;t) as above, and
the limit does not depend on the choice of sequences {N (p)
1 }p∈Z≥0,{N (p)
0 }p∈Z≥0.
26 ANNA LACHOWSKA, OLGA POSTNOV A, NICOLAI RESHETIKHIN, AND DMITRY SOLOVYEV
9.4. The asymptotic of the Placherel measure. Now let us find the asymptotic of the
Plancherel measure whenN→∞ andl is fixed. From definition 8.2 it is evident that the same
ideas as explored in Subsection 9.3 are applicable to the Plancherel measure.
In the considered limit we have the following asymptotical expression for dimensions when
k0̸=l− 1
dimT (k)
(dimT (1))N = 22−N0ξlN1
22lN1

1 +O
 1
N1

,
and when k0 =l− 1
dimT (lk1 +l− 1)
(dimT (1))N = 21−N0ξlN1
22lN1

1 +O
 1
N1

.
We obtain the following pointwise asymptotic for the probability measure distribution
(16) p(l)
N (k) =
ν(l)
k0 (ξ,N 0,γ )√2π 2lN1
exp(2lN1(S(ξ)− ln2))

1 +O
 1
N1

,
where if k0̸=l− 1
ν(l)
k0 (ξ,N 0,γ ) = 16ξ2lN1p
(1−ξ2)1+N0
1−ξ
1 +ξ
γl
2
1
1+ξ

1+ξ
1−ξ
l−k0
2
− 1
1−ξ

1+ξ
1−ξ
−l−k0
2

1+ξ
1−ξ
l
2
−

1+ξ
1−ξ
−l
2
,
and if k0 =l− 1
ν(l)
k0 (ξ,N 0,γ ) = 8ξ2lN1p
(1−ξ2)1+N0
1
1 +ξ
1−ξ
1 +ξ
l(1+γ)−1
2
Similarly to the character measure, the large deviation rate function S(ξ) for the Plancherel
measure has its maximum at the isolated critical point ξ0, i.e.
∂
∂ξ (S(ξ)− ln2) = 0
has a unique solutionξ0 = 0, where the Plancherel measure concentrates asymptotically. Thus,
we have the following theorem.
Theorem 9.3. LetN = 2lN1+N0 andN1→∞ such thatN0,l are fixed. Then for k =k1l+k0,
random variablesk0 andα = k1√2N1
converge to random variables on{0,...,l −1}× R≥0 and the
Plancherel probability distribution weakly converges to the tensor product of two distributions
p1(•)⊗p2(•) on{0,...,l −1}× R≥0. The distribution p1(•) is a discrete probability distribution
on k0 = 0, 1,...,l − 1 with density given by
p1(k0) =
( 2(l−1−k0)
l2 , if k0 = 0,...,l − 2,
1
l, if k0 =l− 1 ,
The distribution p2(•) is a radial part of the Gaussian distribution on R3 with density given by
p2(α) =
r
2
πl
3
2α2e−α2l
2 .
TENSOR POWERS 27
The proof of this theorem is presented in Appendix C.3.
This asymptotic does not depend on N0, γ. This is why we expect that the theorem holds
for any sequence{N (p)}p∈Z≥0 with N (p)→∞ as p→∞ .
9.5. The near Plancherel asymptotic of the character measure. Now consider the
character measure but assume that t = u√2N1
as N1→∞ . In this case the character measure
weakly converges to a deformation of a limiting measure obtained in Theorem 9.3.
Theorem 9.4. Let N = 2lN1 +N0 and N1→∞ such that N0, l are fixed and t = u√2N1
.
Then for k = k1l +k0, random variables k0 and b = k1√2N1
converge to random variables on
{0,...,l − 1}× R≥0 and the character probability distribution weakly converges to the tensor
product of two distributions p1(•)⊗p2(•;u) on{0,...,l − 1}× R≥0. The distribution p1(•) is
a discrete probability distribution on k0 = 0, 1,...,l − 1 with density given by
p1(k0) =
( 2(l−1−k0)
l2 , if k0 = 0,...,l − 2,
1
l, if k0 =l− 1 ,
The distribution p2(•;u) is a distribution on R≥0 with density given by
p2(b,u ) = b
u
r
l
2π (elbu−e−lbu)e−u2l
2 e−b2l
2 .
The proof of this theorem is presented in Appendix D. Analogously, we expect that this
theorem holds for any sequence of {N (p)}p∈Z≥0, where N (p)→∞ as p→∞ .
9.6. The Poisson asymptotic of the character measure. There is the limit whenN→∞
andt→∞ such that the random walk induced by the Markov process for the character measure
is drifted with the critical slope, meaning, the limit shape ξ0 is on the right boundary of the
Weyl alcove. It turns out that when t increases logarithmically as N → ∞the character
probability distribution weakly converges to a Poisson distribution in the vicinity of the right
boundary of the Weyl alcove.
The following theorem gives the pointwise asymptotic of the multiplicity function in the
limit when N→∞ , k→∞ such that N−k is fixed.
Theorem 9.5. Assume that N = 2lN1 +N0, k = k1l +k0, N1→∞ , k1→∞ , such that l,
N0 = 0,..., 2l− 1, k0 = 0,...,l − 1 remain fixed, N−k = 2s for some s∈ Z≥0. Then the
asymptotic of M (l)
T (k)(N) is given by
M (l)
T (k)(N) = N
N−k
2
 N−k
2

!

1 +o(1)

.
The proof of this theorem is presented in Appendix E.1.
Using results of the Theorem 9.5, we obtain the following limiting probability distribution
for the character measure near the right boundary.
Theorem 9.6. Let N = 2lN1 +N0 and N1 → ∞, such that N0, l are fixed. If t → ∞
such that θ = Ne−2t is fixed, then for k = k1l +k0, random variable s = N−k
2 converges to
28 ANNA LACHOWSKA, OLGA POSTNOV A, NICOLAI RESHETIKHIN, AND DMITRY SOLOVYEV
a random variable on Z≥0 and the character probability distribution weakly converges to the
Poisson distribution on Z≥0 with density given by
p(s;θ) = θse−θ
s! .
The proof of this theorem is presented in Appendix E.2. This result coincides with the one
for classical Lie algebra sl2.

---
doc_id: arxiv-0808.2716v4
doc_title: "CUSP AREAS OF F AREY MANIFOLDS"
section_id: sec-021-62-connections-to-volume
section_title: "Connections to volume"
section_number: 6.2
pages: 40-42
source_pdf: 0808.2716v4.pdf
source_sha256: ea66f7ddcf9e9fe6
doc_brief: "CUSP AREAS OF F AREY MANIFOLDS — This paper gives the ﬁrst explicit, two–sided estimates on t he cusp area of once– punctured torus bundles, 4–punctured sphere bundles, and 2 –bridge link"
---
following.
Theorem 6.6. Let K be a hyperbolic closed 3–braid. From the Jones polynomial JK (t),
deﬁne ζK,ζ ′
K as in Deﬁnition 6.4. Let ζ = max {|ζK|, |ζ ′
K|}. Then
4v3 ·ζ − 281 < vol(S3/integerdivideK) < 4v8 (ζ + 1).
Furthermore, the multiplicative constants in both the uppe r and lower bounds are sharp. □
In contrast with Proposition 6.5, there exist 3–braids for w hich the second coeﬃcient of
the Jones polynomial is quite diﬀerent from s.
Proposition 6.7. For every s> 1 there is a knot K =Ks, represented by the 3–braid word
b =C kσp1
1 σ−q1
2 · · ·σps
1 σ−qs
2 , with pi,q i> 0,
such that the second and next-to-last coeﬃcients of the Jone s polynomial JK(t) satisfy
βK = s(s + 3)
−2 + 1, β ′
K =s.
The head and tail of the Jones polynomial for several values o f s is computed in Table 1.
Proof. Fix s> 1, and let p1 =... =ps−1 = 2, p s = 3, q 1 =... =qs−1 = 6, q s = 7.
Notice that p =∑ pi = 2s + 1 and q =∑ qi = 6s + 1; thus, in particular, they are both
odd. Let k = 2s and let K be the closure of the generic 3–braid
b =C kσp1
1 σ−q1
2 · · ·σps
1 σ−qs
2 .
Since C k is a pure braid, and each of σp1
1 ,...,σ −qs− 1
2 is also a pure braid (because their
powers are even), K will have the same number of components as the closure of σ3
1σ−7
2 .
Hence K is a knot.
The Jones polynomial JK (t) will be the sum of equations (21) and (22). Note that the
leading terms of these equations are
(−1)p t(3q−p)/ 2−6k = −t(16s+2)/ 2−12s = −t−4s+1,
CUSP AREAS OF F AREY MANIFOLDS 41
s Jones polynomial JKs
2 2t−8 − 4t−9 + 9t−10 − 14t−11+ ... + 9t−22 − 5t−23 + 2t−24 −t−25
3 3t−12 − 8t−13 + 20t−14 − 39t−15+ ... + 20t−34 − 9t−35 + 3t−36 −t−37
4 4t−16 − 13t−17 + 37t−18 − 85t−19+ ... + 37t−46 − 14t−47 + 4t−48 −t−49
5 5t−20 − 19t−21 + 61t−22 − 160t−23+ ... + 61t−58 − 20t−59 + 5t−60 −t−61
6 6t−24 − 26t−25 + 93t−26 − 273t−27+ ... + 93t−70 − 27t−71 + 6t−72 −t−73
7 7t−28 − 34t−29 + 134t−30 − 434t−31+ ... + 134t−82 − 35t−83 + 7t−84 −t−85
8 8t−32 − 43t−33 + 185t−34 − 654t−35+ ... + 185t−94 − 44t−95 + 8t−96 −t−97
9 9t−36 − 53t−37 + 247t−38 − 945t−39+ ... + 247t−106 − 54t−107 + 9t−108 −t−109
10 10t−40 − 64t−41 + 321t−42 − 1320t−43+ ... +321t−118 − 65t−119 + 10t−120 −t−121
Table 1. The head and tail of the Jones polynomial for the ﬁrst few valu es
of s in Proposition 6.7. These values were computed independent ly by two
pieces of software: jpclosed.c by Nathan Broaddus and the Mathematica
package KnotTheory‘ by Dror Bar-Natan.
and
(−1)p−q t(q−p)/ 2−3k+1 = t(4s)/ 2−6s+1 = t−4s+1,
which will cancel. Thus, continuing along equations (21) an d (22), one can see that the
leading monomial of JKb(t) will be ( −1)p+1st −4s, and the second term will be
(γKa)t−4s−1 + (−1)(p−q) t−4s−1 = (γKa + 1)t−4s−1.
Since s> 1 and pi,q i> 1 for all i, Lemma 6.2(c) implies that
γKa = ( −1)p
(s(s + 3)
2
)
= s(s + 3)
−2 , hence βK = s(s + 3)
−2 + 1.
Now we consider the term β′
K . The two lowest–degree terms of (21) are
(−1)q t(q−3p)/ 2−6k = −t(−2)/ 2−12s = −t−12s−1 and ( −1)q+1st −12s = st −12s.
The remaining terms of (22) are
(−1)p−q+1t(q−p)/ 2−6k±1 = t(4s)/ 2−12s±1 = −t−10s±1.
Since −12s< −10s − 1 for all positive s, no term of (22) can aﬀect either of the two lowest–
degree terms of JKb(t). Therefore,
α′
K = (−1)q = −1 and β′
K = (−1)q+1s =s. □
Theorem 6.8. There does not exist a function f (·, ·) of two variables, together with positive
constantsC1,...,C 4 such that
C1f (βK,β ′
K ) −C2 < vol(S3/integerdivideK) < C3f (βK,β ′
K ) +C4
for every hyperbolic knot K. In other words, the second and next-to-last coeﬃcients of th e
Jones polynomial do not coarsely predict the volume of a knot .
Proof. Suppose, for a contradiction, that such a function f (·, ·) does exist. Then it will follow
that for every pair of knots K and L, such that βK =βL and β′
K =β′
L,
(24) vol( S3/integerdivideL) < C3
C1
vol(S3/integerdivideK) + C2C3
C1
+C4.
42 D. FUTER, E. KALF AGIANNI, AND J. PURCELL
On the other hand, we shall construct an inﬁnite sequence of s uch pairs Ks and Ls, such
that the volumes vol( S3/integerdivideLs), vol(S3/integerdivideKs), as well as the ratio vol( S3/integerdivideLs)/vol(S3/integerdivideKs) go
to inﬁnity as s goes to inﬁnity. This will contradict the existence of f .
The sequence Ks is the one given by Proposition 6.7, where we require that s ≡ 3 mod 4
and s> 10. By Proposition 6.7, these knots satisfy
βKs = s(s + 3)
−2 + 1, and β′
Ks =s.
The sequence Ls will consist of (3 ,..., 3, −3,..., −3) pretzel knots, where there are
n =
(s(s + 3)
2 − 2
)
positive 3’s and m = (s − 1) negative 3’s .
When s ≡ 3 mod 4, it follows that n is odd, m is even, and thus Ls is indeed a knot.
It is easy to check that the standard pretzel diagram Ds of one these knots is adequate.
Computing the graphs GA(Ds), GB(Ds) gives
vA =n + 2m, e ′
A =n + 3m, v B = 2n +m, e ′
B = 3n +m.
Also, we may compute the writhe of Ds to be w(D) = 3m − 3n. Now, Lemma 6.1 gives
βLs = ( −1)vB +w(D)(e′
B −vB + 1) = ( −1)−n+4m(n + 1) = ( −1)n(n + 1) = s(s + 3)
−2 + 1,
since n is odd. Similarly,
β′
Ls = ( −1)vA+w(D)(e′
A −vA + 1) = ( −1)m(m + 1) = s.
Therefore, βKs =βLs and β′
Ks =β′
Ls for all s ≡ 3 mod 4.
Now, consider the volumes of these links. By Theorem 5.6,
4v3s − 277< vol(S3/integerdivideKs)< 4v8s.
On the other hand, the pretzel diagram Ds contains (n +m) > s2/2 twist regions and is
built by joining together ( n +m)>s 2/2 rational tangles. Thus, by [26, Theorem 1.5],
vol(S3/integerdivideLs) ≥ v8
2
(
1 −
( 8π
11.524 +s2 4√
2/2
)2)3/ 2(s2
2 − 3
)
> v8s2
8 for s> 10.
Hence vol(S3/integerdivideLs)/vol(S3/integerdivideKs) ≥s/32. Since both volumes are eventually large enough that
the additive constants in equation (24) do not matter, this c ontradicts equation (24). Thus
the function f cannot exist. □

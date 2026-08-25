---
doc_id: arxiv-2506.10206v2
doc_title: "Analytic dilogarithm identities"
section_id: sec-022-6-a-proof-of-campbells-conjecture
section_title: "A proof of Campbell’s conjecture"
section_number: 6
pages: 16-18
source_pdf: 2506.10206v2.pdf
source_sha256: d0631a9abd9b1da3
doc_brief: "Analytic dilogarithm identities — We introduce dilogarithm identities through a beta integral-based technique that we apply to provide analytic proofs of previously conjectured dilogarithm relations"
---
To solve an open problem recently given by Campbell [8], we begin with the following
dilogarithm identity that we have obtained through our beta integral-based method.
16
Theorem 3. For complex u, letL(u) denote the three-term dilogarithm combination
Li2
2−√4− 3u√u−u
2

+ Li2
2 +√4− 3u√u−u
2

+ Li2(u)
and letE(u) denote the elementary expression
1
3 ln2
 2√4− 3u√u−u + 1

− 1
2 ln2

− 2
−u +√4− 3u√u + 2

−
1
2 ln2
 2
u +√4− 3u√u− 2

+ 1
3 ln2

1− 2
u +√4− 3u√u

−
2
3 ln(1−u) ln(−u) + 1
3 ln2(1−u)− 1
6 ln2(−u)− π2
2 .
For all u∈ C\ R>0, we have that L(u) = E(u). For u∈ R>0, we have that ℜ (L(u)) =
ℜ (E(u)) and that
lim
b→0
ℑ (L(u +bi)) = lim
b→0
ℑ (L(u +bi)).
Proof. Consider the cubic integrals
w1 =
Z 1
0
ln

1− 1
u(1−u)2x(1−x)2

1−x dx and w2 =
Z 1
0
ln

1− 1
u(1−u)2x(1−x)2

x dx (36)
along with
−z
6
∞X
n=0
4z
27
n1, 1, 3
2
4
3, 5
3, 2

n
=
Z 1
0
ln(1−zx(1−x)2)
x dx.
Using the shifting method found in the first section, we have w2
w1
= 2. Eventuating the
integrals and simplification using elementary dilogarithm identities, and we obtain the desired
result.
Example 1. Setting u =−1 we obtain a single-term complex dilogarithm evaluation, with
ℜLi2
 
−1
2− i
√
7
2
!
+ π2
8 + ln2(2)
4
+ 1
2

cot−1
 3√
7
2
− 1
3

cot−1
 5√
7
2
− arctan(
√
7) cot−1
 3√
7

= 0.
Example 2. Setting u = 1
2, we obtain that
3 Li2
 
3
4−
√
5
4
!
+ 3 Li2
 
3
4 +
√
5
4
!
−
3π2
4 + 3
2 ln2(3−
√
5)− ln2(
√
5− 2)− ln2(2 +
√
5) + 3
2 ln2(3 +
√
5) = 0,
and this provides a proof of a two-term dilogarithm identity given by Adegoke and Frontczak
[3].
17
Example 3. Setting u = 1
2 +bi, and using the reflection formula for the dilogarithm, this
leads us to
ℜLi2
1
2 +iu

= π2
12− 1
8 ln2
1 + 4u2
4

− (arctan (2u))2
2 . (37)
If we then plug (37) into Theorem 3, we obtain a two-term identity for real b, where r =
(144b4 + 136b2 + 25). This gives us a closed form for
Li2
 
3
4− 2bi
4 + r
1
4
4

cos
1
2 arctan
 4b
12b2 + 5

+i sin
1
2 arctan
 4b
12b2 + 5
!
+
Li2
 
3
4− 2bi
4 − r
1
4
4

cos
1
2 arctan
 4b
12b2 + 5

+i sin
1
2 arctan
 4b
12b2 + 5
!
.
Example 4. Setting u = 1+
√
5
2 , we obtain a remarkable single-term identity is derived
involving the golden ratio, using Theorem 3, namely
π2
100 =ℜ Li2
1
4

3−
√
5 +i
q
10− 2
√
5

.
More compactly, we have that π2
100 =ℜ Li2(ro), where ro≈ 0.1909... + 0.5877...i is a root of
r4− 3r3 + 4r2− 2r + 1 = 0. (38)
This proves an identity conjectured by Campbell [8], because 1 /(2ϕ2)− 1/2
p
−1− 1/ϕ2 is
the same root of the polynomial in (38), letting ϕ = 1+
√
5
2 denote the golden ratio.

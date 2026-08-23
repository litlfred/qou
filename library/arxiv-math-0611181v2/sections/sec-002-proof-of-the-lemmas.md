---
doc_id: arxiv-math-0611181v2
doc_title: "Proof of the volume conjecture for Whitehead chains"
section_id: sec-002-proof-of-the-lemmas
section_title: "Proof of the lemmas"
section_number: null
pages: 6-13
source_pdf: 0611181v2.pdf
source_sha256: 6931e3ebca584de9
doc_brief: "Proof of the volume conjecture for Whitehead chains — We prove the volume conjecture for an inﬁnite family of links called White- head chains that generalizes both the Whitehead link and the"
---
In this section we prove the more technical lemmas 2,3,4 and 5.
Proof. (of lemma 2) The proof of this lemma hinges on the following key esti-
mate of Sn,k in terms of the Lobachevski function Λ( x) that was proved in [11].
Deﬁne f (x,y ) = −2Λ(x +y) + 2Λ(y) + Λ(x). For integers 0 ≤n,k,n +k <N
we have the uniform estimate
logSn,k = N
πf (nπ
N ,kπ
N ) + O(logN ), N → ∞
Before we can apply this result we ﬁrst need to show that inside the t riangle
0<x,y,x +y<π the function f has a unique critical point ( π
2, π
4 ) and reaches
its maximum there, which equals 4Λ( π
4 ). Moreover the Taylor expansion of f
around the critical point is:
f (π
2 +x,π
4 +y) = f (π
2,π
4 ) − (x2 + 2xy + 2y2) + O(|x|3 + |y|3)
Lemma 2 part a) and b) are direct consequences of these facts on ce we note that
the diﬀerence between S⌊ N
2 ⌋, ⌊ N
4 ⌋ and the actual critical value f ( π
2, π
4 ) becomes
negligibly small as N grows.
To ﬁnd the critical points of f in 0 <x,y,x +y<π we use the fundamental
theorem of calculus to diﬀerentiate Λ and ﬁnd the system of equatio ns: 2 sin 2(x+
y) = sin( x) and sin( x +y) = sin( y). For 0 < x,y,x +y < π this has the
unique solution ( x,y ) = ( π
2, π
4 ). To determine the nature of the critical point
we diﬀerentiate again and this will be left to the reader.
The value of f at its critical point is f ( π
2, π
4 ) = −2Λ( 3
4π) + 2Λ( π
4 ) + Λ( π
2 ) =
4Λ( π
4 ) because Λ( x) = −Λ(π −x).
The next lemma is an expanded version of a result proven in [11].
Proof. (of lemma 3) If we deﬁne sn = −∑ n
j=1 log |2 sin(jπ/N )| then we can
write log ˜SN = −2s⌊N/ 4⌋+⌊N/ 2⌋ + 2s⌊N/ 4⌋ +s⌊N/ 2⌋. It was shown in [11] that
for 0 <n< 5
6N we have sn = N
π Λ( nπ
N ) − 1
2 logn + O(1), as N → ∞. To prove
the lemma we need to expand a little further. Assuming that r = lim N →∞n/N
exists, we show that
sn = N
π Λ(nπ
N ) − 1
2 logn sin(rπ)
rπ + O(N −1), N → ∞
By applying the above expansion for sn three times we then ﬁnd the desired
expansion for ˜SN .
To prove the expansion for sn we reason as follows: for x ∈ [0, 5
6π] − {0,u }
we have
sin(x −u)
x −u
x
sinx = 1 + −x cosx + sinx
x sinx u + O(u2), u → 0
6
Now taking the logarithm and expanding log(1 + f ) around f = 0 we ﬁnd:
log | sin(x −u)
sinx | = log |x −u
x | + −x cosx + sinx
x sinx u + O(u2)
Following [11] p.7 we set x =jπ/N and ﬁnd:
sn − N
π Λ(nπ
N ) =
n∑
j=1
N
π
∫ π
N
0
log sin(jπ/N −u)
sinjπ/N du =
− 1
2 logn − 1
2 log 2π +
n∑
j=1
N
π
∫ π
N
0
−(jπ/N ) cos(jπ/N ) + sinjπ/N
jπ/N sinjπ/N udu + O(N −1)
The term − 1
2 log 2π is the constant contribution of the Sterling series used in
[11] p.7. After integration with respect to u we can write the above sum as
a Riemann sum. A computation then shows that the limit of this sum equ als
1
2 (logrπ − log sinrπ).
Although the proof of lemma 4 below is quite long the main idea is simple: Us e
lemma 2 to estimate the value of the colored Jones polynomial in terms of the
maximum value ˜SN .
Proof. (of lemma 4) For convenience we will assume throughout the proof t hat
c +d ≥ 2, so that the value of CS is −4a−7c+7d
8 2π2. The proof in the case
c +d = 1 is completely analogous. According to lemma 1 the formula for the
N-colored Jones polynomial of the one-belted Whitehead chain is
JN,a, 1,c,d =φN
N −1∑
n=0
(2n + 1)χ4a−c+d
N,n
( N −1−n∑
k=0
Sn,k
) c+d
Deﬁne the quotient QN = JN,a, 1,c,d N −(c+d+3)/ 2 ˜S−(c+d)
N e
4a+7c−7d
8 N πi . We aim
to show that Q∞ = lim N →∞QN =C for some nonzero complex constant.
Step 1: By expanding the c +d-th power of the sum we obtain a multi-sum
over all N-tuples of natural numbers n, k < N such that n +kj < N. Deﬁne
Central to be the set of all such tuples that satisfy n + maxkj <N δ and deﬁne
Far to be the set of tuples such that n + max kj ≥ N δ. We can then rewrite
QN as follows:
QN =φNe
4a+7c−7d
8 N πiN −(c+d+3)/ 2 ∑
Central
(2n+1)χ4a−c+d
N,n Sn,k 1 · · ·Sn,k c+d
˜S−(c+d)
N
+φNe
4a+7c−7d
8 N πiN −(c+d+3)/ 2∑
Far
(2n + 1)χ4a−c+d
N,n Sn,k 1 · · ·Sn,k c+d
˜S−(c+d)
N
The Far sum converges to zero absolutely, because each tuple n, k in the sum
contains a km such that n +km ≥N δ. According to lemma 2b this means that
7
Sn,k m
˜S−1
N = O(exp(−ǫN 2δ−1)). We can estimate all other factors Sn,k j
˜S−1
N by a
constant and conclude that the sum of absolute values of the Far s um converges
to zero since δ >1/2. So far we have shown that Q∞ =
lim
N →∞
φNe
4a+7c−7d
8 N πiN − c+d+3
2
∑
Central
(2n + 1)χ4a−c+d
N,n Sn,k 1 · · ·Sn,k c+d
˜S−(c+d)
N
Step 2: In the next step we replace the factor (2 n + 1) in the expression for
Q∞ by a factor N . This is done by showing that the diﬀerence converges to
zero. The absolute value of the diﬀerence is less than
N −(c+d+3)/ 2 ∑
Central
|2n + 1 −N |Sn,k 1 · · ·Sn,k c+d
˜S−(c+d)
N
For central tuples n, k we have n′ < Nδ and hence 2 n + 1 = N + O(N δ).
The number of terms in the sum is of order O(N (c+d+1)δ) and the product
Sn,k 1 · · ·Sn,k c+d
˜S−(c+d)
N is O(1) by lemma 2a. Therefore the absolute value of the
diﬀerence is at most of order O(N −(c+d+3)/ 2+(c+d+2)δ). Since δ < c+d+5
2(c+d+4) <
c+d+3
2(c+d+2) the diﬀerence converges to zero and we have:
Q∞ = lim
N →∞
φNe
4a+7c−7d
8 N πiN −(c+d+1)/ 2 ∑
Central
χ4a−c+d
N,n Sn,k 1 · · ·Sn,k c+d
˜S−(c+d)
N
Step 3: Deﬁne the (c +d + 1)-variable Gaussian function
gN (x, y) = exp −π
N

(c +d − (4a +c −d)i)x2
2 + 2
c+d∑
j=1
(yj + x
2 )2


and let ψ = exp( 4a+3c−3d
4 πi). We will show that
Q∞ = lim
N →∞
ψN −(c+d+1)/ 2 ∑
Central
gN (n′, k′)
Starting with the sum from step 2 we use lemma 2 to replace the facto rsSn,k j
˜S−1
by exponentials and error terms:
lim
N →∞
φNe
4a+7c−7d
8 N πiN −(c+d+1)/ 2 ∑
Central
χ4a−c+d
N,n ·
c+d∏
j=1
(
exp(−π
N (n′2 + 2n′k′
j + 2k′2
j )) + O(N 3δ−2)
)
To show that the error terms can be removed we estimate the cont ribution
of their absolute values. There are O(N (c+d+1)δ) terms in the sum so their
contribution is of order O(N (c+d+1)δ+3δ−2−(c+d+1)/ 2). This converges to zero
because δ < c+d+5
2(c+d+4) .
8
Next we look at the phase factors φN andχN,n . We have lim N →∞φN =e(c−d)πi .
Furthermore:
χN,n e
N πi
8 = exp(n′2
2N − N
8 + n
2N + N
8 )πi = exp(n′2
2Nπi) exp( n
2Nπi)
Since n = N
2 + O(N δ) we have lim N →∞ n
2N = 1
4 . If we apply this to the above
sum we get the desired expression.
Step 4: It seems natural to replace the previous sum by an integral, this is
done in step 4. We will show that
Q∞ = lim
N →∞
ψN −(c+d+1)/ 2
∫
|x|+max|yj|<N δ −1
gN (|x|, |y|)dxdy
The strategy is to estimate the absolute value of the diﬀerence bet ween sum
and integral. First we write the sum from step 3 as follows:
Q∞ = lim
N →∞
ψN −(c+d+1)/ 2 ∑
Central
∫
B(n, k)
gN (n′, k′)dxdy
where B(n, k) = [ n − N
2 − 1
2,n − N
2 + 1
2 ) ×∏ c+d
j=1[kj − N
4 − 1
2,k j − N
4 + 1
2 ).
The absolute value of the diﬀerence between the sum and the propo sed integral
above is:
N −(c+d+1)/ 2|
∑
central
∫
B(n, k)
gN (n′, k′)dxdy −
∫
|x|+max|yj|<N δ −1
gN (|x|, |y|)dxdy|
The union of the disjoint blocks B(n, k) as n, k runs through Central, covers the
entire integration domain |x|+max|yj|<N δ −1 so we can subtract the integrals.
However some blocks continue over the boundary of the domain of in tegration,
resulting in a slight error. The terms n, k such that the corresponding blocks
B(n, k) intersect the complement of the domain will be called Border terms.
We can estimate the above quantity as follows:
<N −(c+d+1)/ 2 ∑
Central
∫
B(n, k)
|gN (n′, k′) −gN (|x|, |y|)|dxdy
+N −(c+d+1)/ 2 ∑
Border
|gN (n′, k′)|
Both sums will be shown to converge to zero, we start with the seco nd one. Since
the number of terms on the Border of the integration domain is O(N (c+d)δ) and
gN (n′, k′) = O(1) the second sum is of order O(N −(c+d+1)/ 2+(c+d)δ). This
implies that the sum converges to zero because δ < c+d+5
2(c+d+4) < c+d+1
2(c+d) .
For the ﬁrst sum we need to estimate the integrands:
|gN (n′, k′) −gN (|x|, |y|)| = |gN (n′, k′)||1−
9
exp −π
N

(c +d − (4a +c −d)i) |x|2 −n′2
2 + 2
c+d∑
j=1
(|yj| + |x|
2 )2 − (k′
j + n′
2 )2

 |
The last expression is of order O(N δ−1) because |gN (n′, k′)| = O(1) and |x|2 −
n′2 = (|x|+n′)(|x| −n′) and ( |yj|+ |x|
2 )2 − (k′
j + n′
2 )2 = (|yj |+ |x|
2 +k′
j + n′
2 )(|yj |+
|x|
2 −k′
j − n′
2 ). We integrate over B(n, k) so |n′ − |x||< 1 and |k′
j − |yj||< 1 and
all terms are central so |x| +n′ < Nδ and k′
j + |yj| < Nδ. Therefore the sec-
ond sum is of order O(N −(c+d+1)/ 2+δ−1+(c+d+1)δ) and thus converges to zero,
because δ < c+d+5
2(c+d+4) < c+d+3
2(c+d+2) .
Step 5: We make the substitution x =
√
Nw and yj =
√
Nz j with Jacobian
N (c+d+1)/ 2. This gives:
Q∞ = lim
M→∞
ψ
∫
w+max|zj|< (N δ −1)√
N
exp(−π

(c +d − (4a +c −d)i) |w|2
2 + 2
c+d∑
j=1
(|zj| + |x|
2 )2

)dwdz
Now δ > 1
2 and the integrand is rapidly decreasing so the limit exists and is
equal to:
ψ
∫
Rc+d+1
exp(−π

(c +d − (4a +c −d)i) |w|2
2 + 2
c+d∑
j=1
(|zj| + |w|
2 )2

)dwdz
Step 6: In this ﬁnal step we need to show that Q∞ ⁄= 0. We know that ψ ⁄= 0,
but what about the complicated Gaussian integral above? We can wr ite it as
an iterated integral and get rid of the absolute value signs by integr ating 2 c+d+1
times over the positive hyper-quadrant w,z j > 0:
Q∞ =ψ2c+d+1
∫ ∞
0
exp(−π(c +d − (4a +c −d)i)w2
2 )dw ·
c+d∏
j=1
∫ ∞
0
exp(−2π(zj + w
2 )2))dzjdw
Using the substitutions yj =
√
2π(zj + w
2 ) we get the integral below. We only
want to check that the integral is nonzero so all constants in fron t of the integral
and the Jacobian are written as C.
Q∞ =C
∫ ∞
0
exp(−π(c +d − (4a +c −d)i)w2
2 ) ·
c+d∏
j=1
∫ ∞
√πw√
2
exp(−y2
j )dyjdw
10
If we deﬁne the complementary error function by erfc( x) = 2√π
∫ ∞
x exp(−y2)dy,
then we can write the integral more concisely as:
Q∞ =C
∫ ∞
0
exp(−π(c +d − (4a +c −d)i)w2
2 )erfcc+d
( √πw√
2
)
dw =
C
∫ ∞
0
exp(−π(c +d)w2
2 )erfcc+d
( √πw√
2
)
·
(
cos( 4a +c −d
2 πw2) +i sin( 4a +c −d
2 πw2)
)
dw
After the substitution x =
√
4a+c−d
2 w we note that the imaginary part of inte-
gral is nonzero, because both the exponential function and the c omplementary
error function are bounded and decrease monotonically and the de crease is quite
rapid. Therefore the integral over the part where the sine is posit ive dominates
the integral over its complement, showing that the integral is a pos itive scalar
multiple of C.
The same proof also works for lemma 5 but in this case it is much easier
because the value of n is ﬁxed at the maximum. The Gaussian integral at the
end of step 5 is now a standard Gaussian integral so that the const ant in front
of lemma 5 can be computed easily.
References
[1] S. Garoufalidis, T. Le, On the Volume Conjecture for Small Angles , preprint 2005, ArXiv
GT/0502163.
[2] S. Gukov, H. Murakami, SL(2,C) Chern-Simons theory and the asymptotic behavior of
the colored Jones polynomial , preprint 2005, ArXiv GT/0608324.
[3] K. Hikami, Volume Conjecture and Asymptotic Expansion o f q-series, Exp. Math. 12, 3
(2003) 319-337.
[4] R. Kashaev, O. Tirkkonen, Proof of the volume conjecture for torus knots, J. Math. Sci.
115 (2003) 2033-2036.
[5] R. Meyerhoﬀ, Density of the Chern-Simons invariant for h yperbolic 3-manifolds, Low
dimensional topology and Kleinian groups , 217-239, Cambridge university press, Cam-
bridge, 1986.
[6] H. Murakami, A quantum introduction to knot theory, Primes and Knots: JAMI con-
ference, Contemp. Math., 2006.
[7] H. Murakami, J. Murakami, The colored Jones Polynomials and the simplicial Volume
of a Knot, Acta Math. 186 (2001) 85-104.
[8] H. Murakami, J. Murakami, M. Okamoto, T. Takata, Y. Yokot a, Kashaev’s Conjecture
and the Chern-Simons Invariant of Knots and Links, Exp. Math. 11, 3 (2002) 427-435.
[9] M. Ouyang, A note on the Chern-Simons invariant of hyperb olic 3-manifolds, Proc.
A.M.S. 125, 6 (1997) 1845-1851.
11
[10] R. van der Veen, The volume conjecture for Whitehead chains , master thesis, 2006.
http://www.science.uva.nl/∼ riveen/papers.html
[11] H. Zheng, The Volume Conjecture for Whitehead Doubles of Torus Knots , preprint
2005, ArXiv GT/0508138.
12
This figure "BTC.jpg" is available in "jpg"
 format from:
http://arxiv.org/ps/math/0611181v2

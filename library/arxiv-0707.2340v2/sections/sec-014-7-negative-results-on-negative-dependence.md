---
doc_id: arxiv-0707.2340v2
doc_title: "NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS"
section_id: sec-014-7-negative-results-on-negative-dependence
section_title: "Negative Results on Negative Dependence"
section_number: 7
pages: 41-45
source_pdf: 0707.2340v2.pdf
source_sha256: bf0f91277a5874ff
doc_brief: "NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS — W e introduce the class of strongly Rayleigh probability measures by means of geometric properties of their generating polyno mials that amount"
---
We will now use the results from the previous sections, in particular t hose of §6,
to construct counterexamples to the general cases of Pemantle ’s and Wagner’s con-
jectures on ULC rank sequences (Conjectures 2.3–2.5) and Pema ntle’s conjecture
on stochastic domination and truncations (Conjecture 2.9). We als o answer in the
negative some related problems as well as Problem 2.7 and [12, Problem 6].
Counterexample 1. Suppose that µ is a probability measure on 2 [n+1] whose gen-
erating polynomial
f (z1, . . . , zn+1) = zn+1
n∑
k=0
akek(z1, . . . , zn) +
n∑
k=0
bkek(z1, . . . , zn)
42 J. BORCEA, P. BR ¨AND ´EN, AND T. M. LIGGETT
is symmetric in its ﬁrst n variables. Clearly,
∆( f )(t) =
n+1∑
k=0
(n + 1
k
)
cktk =
n+1∑
k=0
[( n
k − 1
)
ak−1 +
(n
k
)
bk
]
tk,
where
ck = kak−1 + (n + 1 − k)bk
n + 1 .
In light of Proposition 6.2 and Corollary 6.6, Conjectures 2.4 and 2.5 re duce to the
following problem in the almost exchangeable case.
Problem 7.1. Let {ak}m
k=0, {bk}m
k=0 be two non-negative sequences satisfying
(1) {θak + (1 − θ)bk}m
k=0 is LC for all 0 ≤ θ ≤ 1, and
(2) akbk+1 ≥ ak+1bk for 0 ≤ k ≤ m − 1.
Is it true that the sequence
{kak−1 + (m + 1 − k)bk}m+1
k=0 , where a−1 = bm+1 = 0,
is LC?
A related problem is the following.
Problem 7.2. Let {ak}n
k=0, {bk}n
k=0 be two non-negative sequences satisfying
(1) {θak + (1 − θ)bk}n
k=0 is LC for all 0 ≤ θ ≤ 1, and
(2) akbk+1 ≥ ak+1bk for 0 ≤ k ≤ n − 1.
Is it true that the sequence
{kak−1 + bk}n+1
k=0 , where a−1 = bn+1 = 0,
is LC?
Note that a counterexample {ak}n
k=0, {bk}n
k=0 to the latter problem would ac-
tually give a counterexample to the former as well. This is because for some large
integer m ≥ n the sequence {dk}m
k=0 deﬁned by
dk = kak−1 + m + 1 − k
m bk, where dk = 0 if k > n + 1, (30)
will fail to be LC and the sequences {ak}m
k=0 and {bk/m}m
k=0 will therefore constitute
a counterexample to Problem 7.1.
It remains to ﬁnd negative solutions to Problems 7.1 and 7.2. Set
a0 = 2t2, a 1 = 2t, a 2 = 4
9 − t, a 3 = 2
3 , a 4 = 1, a 5 = 2
3 t,
b0 = 9t3, b 1 = 9t2, b 2 = 3t, b 3 = 1, b 4 = 3, b 5 = 9 − t.
For t suﬃciently small and positive this is seen to be a negative solution to Pr ob-
lem 7.2. Indeed,
λa0 + b0 = t2(2λ + 9t), λa 1 + b1 = t(2λ + 9t), λa 2 + b2 =
(4
9 − t
)
λ + 3t,
λa3 + b3 = 2
3 λ + 1, λa 4 + b4 = λ + 3, λa 5 + b5 = 2
3 tλ + 9 − t,
hence
(λa1 + b1)2 − (λa0 + b0)(λa2 + b2) = t2(2λ + 9t)
[( 14
9 + t
)
λ + 6t
]
≥ 0,
NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS 43
(λa2 + b2)2 − (λa1 + b1)(λa3 + b3) = λ2
[ (4
9 − t
)2
− 4
9 t
]
+ 2tλ
(1
3 − 6t
)
≥ 0,
(λa3 + b3)2 − (λa2 + b2)(λa4 + b4) = tλ2 + (1 − 9t) ≥ 0,
(λa4 + b4)2 − (λa3 + b3)(λa5 + b5) =
(
1 − 4
9 t
)
λ2 + t ≥ 0
for any λ ≥ 0 if e.g. 0 < t ≤ 1
20 . Moreover,
a0b1 − a1b0 = 0, a 1b2 − a2b1 = t2(2 + 9t) ≥ 0, a 2b3 − a3b2 = 4
9 − 3t ≥ 0,
a3b4 − a4b3 = 1, a 4b5 − a5b4 = 9 − 3t ≥ 0
for 0 < t ≤ 4
27 . However,
(b4 + 4a3)2 − (b3 + 3a2)(b5 + 5a4) = − 5
9 + 133
3 t − 3t2 < 0
for 0 < t ≤ 1
80 . Thus, if 0 < t ≤ 1
80 then both sequences {ak}5
k=0 and {bk}5
k=0
are positive and satisfy conditions (1) and (2) in Problems 7.1 and 7.2. By taking
e.g. t = 10 −4 one can then check that the corresponding sequences {ak}m
k=0 and
{bk/m}m
k=0 constructed in (30) produce a counterexample to Problem 7.1 for a ny
integer m ≥ 19. Therefore, both Conjecture 2.4 and Conjecture 2.5 fail when ever
the (total) number of variables satisﬁes n + 1 ≥ 20.
We note that our construction disproves slightly more than Conjec ture 2.4 and
Conjecture 2.5. Indeed, the rank sequence of the measures obt ained in this fashion
(i.e., measures on 2 [m+1] with a generating polynomial of the form
zm+1
m∑
k=0
akek(z1, . . . , zm) +
m∑
k=0
bk
m ek(z1, . . . , zm),
where m ≥ 19 and {ak}m
k=0, {bk}m
k=0 are the sequences constructed above with
t = 10 −4) is not even SLC, which is weaker than ULC (Deﬁnition 2.8).
In [12, Problem 6] it was asked whether Conjecture 2.4 would hold und er the
additional assumption that the Rayleigh measure µ is decreasing on 2 [n+1], i.e., the
coeﬃcients of its generating polynomial ∑ aSzS satisfy the monotonicity condition
aS ≥ aT whenever S ⊆ T ⊆ [n + 1]. This fails as well, since if f is as in the
above construction with n + 1 ≥ 20, then the polynomial f (λz1, . . . , λzn+1) is still
Rayleigh and satisﬁes the additional monotonicity assumption state d above for all
suﬃciently small λ ∈ R+, but its rank sequence {λkrk}n+1
k=0 is not ULC. □
Remark 7.1. In [72] it was shown that Conjectures 3.11 and 3.4 in loc. cit. are
equivalent and would follow from either Conjecture 3.13 or Conjectu re 3.14 in that
same paper. Counterexample 1 above shows that all these conjec tures fail.
Next we show that the above construction actually yields a counter example to
Conjecture 2.9 as well.
Counterexample 2. Let
f (z1, . . . , zn+1) = zn+1
n∑
j=0
ajej(z1, . . . , zn) +
n∑
j=0
bjej(z1, . . . , zn)
44 J. BORCEA, P. BR ¨AND ´EN, AND T. M. LIGGETT
be the n + 1 = 20 variable polynomial in the previous counterexample and let
µ be the corresponding probability measure in Pn+1, so that µ is CNA+. For
A = {S ∈ 2[n+1] : n + 1 ∈ S} we have
µk(A) =
ak−1
( n
k−1
)
ak−1
( n
k−1
)
+ bk
(n
k
), µ k+1(A) = ak
(n
k
)
ak
(n
k
)
+ bk+1
( n
k+1
).
Hence,
µk(A) ≤ µk+1(A) ⇐ ⇒ ak−1
( n
k − 1
)
bk+1
( n
k + 1
)
≤ ak
(n
k
)
bk
(n
k
)
.
This fails for k = 3 and 0 < t < 1
18 . □
As we noted in §2.5, a positive answer to Problem 2.7 would imply Conjecture 2.6.
However, the answer to Problem 2.7 is negative, which we will now prov e.
Counterexample 3. We claim that if µ ∈ Pm satisﬁes
(1) µ is Rayleigh,
(2) µ = θµk + (1 − θ)µk+1 for some 0 < θ < 1,
(3) µk ⁄≼ µk+1,
where µk, µk+1 are the truncations of µ as in Deﬁnition 2.15, then µ is not PHR
(projection of a Rayleigh measure with homogeneous generating po lynomial, cf. Def-
inition 2.6). To prove this claim, let gk and gk+1 be the generating polynomials for
µk and µk+1, respectively, and suppose that
f (z1, . . . , zℓ) = h1(zm+1, . . . , zℓ)gk(z1, . . . , zm) + h2(zm+1, . . . , zℓ)gk+1(z1, . . . , zm),
is a homogeneous Rayleigh polynomial that projects to θgk + (1 − θ)gk+1 and has a
minimal number of variables ℓ ≥ m+1. If the same variable, say zj, appears in both
h1(zm+1, . . . , zℓ) and h2(zm+1, . . . , zℓ), then we can diﬀerentiate f with respect to
zj and get a new homogeneous polynomial in fewer variables that still pr ojects
to θgk + (1 − θ)gk+1. Moreover, if either h1(zm+1, . . . , zℓ) or h2(zm+1, . . . , zℓ) is
the positive sum of several monomials we could set a variable equal to zero and
again get a polynomial in fewer variables with the desired properties. Hence, both
h1(zm+1, . . . , zℓ) and h2(zm+1, . . . , zℓ) are monomials and by the minimality of ℓ
we have that ℓ = m + 1 and
f (z1, . . . , zm+1) = θzm+1gk(z1, . . . , zm) + (1 − θ)gk+1(z1, . . . , zm).
Since f is a homogeneous Rayleigh polynomial, by Theorem 4.10 the correspon d-
ing measure µf ∈ Pm+1 is (strongly) negatively associated. As in the proof of
Proposition 4.12 we then deduce that µk ≼ µk+1, which contradicts assumption (3)
above.
It remains to ﬁnd a measure µ satisfying properties (1)–(3) above. If we let µ
have generating polynomial a constant multiple of
zn+1(a2e2(z1, . . . , zn) + a3e3(z1, . . . , zn)) + b3e3(z1, . . . , zn) + b4e4(z1, . . . , zn),
where m = n+1 and a2, a3, b3, b4 are as in Counterexample 1, we see that µ satisﬁes
all these three properties. Clearly, this counterexample fails to ha ve a ULC rank
sequence. Therefore, we conclude that not even the PHR proper ty implies ULC. □
NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS 45
Remark 7.2. We note that to disprove just the strongest version of Pemantle’s con-
jecture on ULC rank sequences (Conjecture 2.3) we can simply invo ke Example 2.2
in §2.1, which combined with Theorem 3.7 shows that Conjecture 2.3 actu ally fails
even for symmetric measures. To give yet another counterexamp le to Conjecture 2.3
we can also employ a construction used in [55]. Indeed, the measure in P4 consid-
ered in [55, Theorem 3.5] is seen to be NA but not ULC.
Note though that both examples mentioned above fail to be NLC (he nce also
CNA+, CNA, h-NLC+, h-NLC), so they do not provide counterexam ples to the
weaker conjectures (Conjectures 2.4 and 2.5).
Acknowledgements. We would like to thank David Wagner for discussions per-
taining to this project and the anonymous referee for useful com ments and sugges-
tions. The ﬁrst author is partially supported by Swedish Research C ouncil Grant
621-2005-870. The third author is supported by NSF Grant DMS-0 301795.

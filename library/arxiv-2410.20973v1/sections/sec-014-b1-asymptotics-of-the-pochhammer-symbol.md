---
doc_id: arxiv-2410.20973v1
doc_title: "SUMMABILITY FOR STATE INTEGRALS OF HYPERBOLIC KNOTS"
section_id: sec-014-b1-asymptotics-of-the-pochhammer-symbol
section_title: "B.1. Asymptotics of the Pochhammer symbol"
section_number: null
pages: 37-43
source_pdf: 2410.20973v1.pdf
source_sha256: 852b7bbc81a62883
doc_brief: "SUMMABILITY FOR STATE INTEGRALS OF HYPERBOLIC KNOTS — We prove conjectures of Garoufalidis-Gu-Mari˜ no [ 9] that perturbative series associated with the hyperbolic knots 4 1 and 5 2 are resurgent and"
---
symbol give rise to a particular branch of the dilogarithm for each ar gument of τ . The zeros
or poles then line up along the branch cuts deﬁning this principle branc h. For θ∈ [0, 2π)
deﬁne L θ : C\(Z + eiθR≤0)→ C to be the holomorphic function such that
Lθ(z) =
∫
z+eiθR≥0
∫
w+eiθR≥0
e(ζ)
1− e(ζ) dζ dw . (103)
This function Lθ(z) gives a particular branch of the multivalued function z↦→Li2(e(z))/(2πi)2
for each θ and if θ∈ (0, π) and Im( z) > 0 then L θ(z) = Li 2(e(z))/(2πi)2 for the principle
branch of Li 2. The domain of L θ is pictured in Figure 30. This function also satisﬁes
dk+2
dzk+2 Lθ(z) = (2 πi)k Li−k(e(z)) . (104)
38 VERONICA F ANTINI AND CAMPBELL WHEELER
Lemma B.1. Suppose that Im( τ ) > 0 and ε∈ R>0. Then as τ→ i∞ with ﬁxed argument
and z is bounded away from the half lines {z| Im((z + Z≥0)τ ) = 0 , and Im( z)≤ 0} by ε
with θ = arg(−1/τ )∈ (0, π) there exists a constant C > 0 such that
⏐
⏐
⏐(e(z);~q)∞− e
(
− Lθ(z)τ− 1
2 L′
θ(z)−
K−1∑
k=2
Bk
k!
(2πi)k−2
τ k−1 Li2−k(e(z))
) ⏐
⏐
⏐ < C ε −KK!|τ|−K. (105)
Proof. Given the positions of the branch cuts of L θ, we see that
1
2πi log(e(z); e(−1/τ ))∞ = −
∞∑
n=0
L′
θ(z− n/τ ) . (106)
Therefore, applying Euler-Maclaurin summation (and the fact that B2k+1 = 0 for k > 0) we
ﬁnd that
−
∞∑
n=0
L′
θ(z− n/τ ) = −
∫ ∞
0
L′
θ(z− η/τ ) dη− L′
θ(z)
2 −
K−1∑
k=2
Bk
k!
(2πi)k−2
τ k−1 Li2−k(e(z))
+ (−2πi)K
τ K−1
∫ ∞
0
Li2−K(e(z− η/τ )) BK(η−⌊ η⌋)
K! dη .
(107)
We see that
−
∫ ∞
0
L′
θ(z− η/τ ) dη = −τ Lθ(z) . (108)
The functions Li k for k≤ 0 can be expressed in terms of Eulerian numbers
Li−k(x) = 1
(1− x)k+1
k−1∑
ℓ=0
⟨ k
ℓ
⟩
xk−ℓ , (109)
where
⟨ k
ℓ
⟩
=
ℓ∑
i=0
(−1)i
( k + 1
i
)
(ℓ + 1 + i)k and 0 ≤
⟨ k
ℓ
⟩
≤ k! . (110)
Therefore, using the fact that Li k(x) =−(−1)k Lik(1/x) for k > 0 we ﬁnd that for |x−1|≥ ε
| Li−k(x)|≤ (k + 1)! min{|x|,|x−1|}ε−k−1 . (111)
Therefore, as z is bounded away from the branch cuts of Lθ by ε, we see that there is a
constant C1 such that
| Li2−K(e(z− η/τ ))| < (K− 1)!ε1−KC1|e(−η/τ )| . (112)
Moreover, we have Lehmer’s bounds for the periodic Bernoulli polyn omials
⏐
⏐
⏐BK(η−⌊ η⌋)
K!
⏐
⏐
⏐ < 2ζ(K)
(2π)K . (113)
Therefore, there exists C2 such that
⏐
⏐
⏐
∫ ∞
0
Li2−K(e(z− η/τ ))BK(η−⌊ η⌋) dη
⏐
⏐
⏐ < C 2 ε1−K (K− 1)!
(2π)K . (114)
SUMMABILITY FOR STATE INTEGRALS OF HYPERBOLIC KNOTS 39
Figure 31. Domain of D 3π/4(z) given by C\
(
(Z≥0 + (i− 1)R≤0)∪ (Z<0 + (i− 1)R≥0)
)
.
Therefore, there exists C such that
⏐
⏐
⏐(e(z);~q)∞− e
(
− Lθ(z)τ− 1
2 L′
θ(z)−
K−1∑
k=2
Bk
k!
(2πi)k−2
τ k−1 Li2−k(e(z))
) ⏐
⏐
⏐ < C ε 1−K(K− 1)!|τ|1−K.
(115)
□
Remark B.2. An easy way to see that L θ is the correct branching of the multivalued function
Li2(e(z))/(2πi)2 is that the zeros of ( e(z); e(−1/τ ))∞ accumulate to the lines {z| Im((z +
Z≥0)τ ) = 0 , and Im( z)≤ 0} in the limit as τ tends to inﬁnity.
B.2. Asymptotics of Faddeev’s dilogarithm for Im(τ )⁄= 0 . We are interested in Fad-
deev’s quantum dilogarithm, which in the upper half plane has the expr ession
Φ( z; τ ) = (qe(z); q)∞
(e(z/τ );~q)∞
. (116)
To understand the asymptotics of this function we need to conside r a diﬀerent branch of the
dilogarithm function again. For θ∈ (0, 2π) deﬁne the domain Cθ = C\
(
(Z≥0 + eiθR≤0)∪
(Z<0 + eiθR≥0)
)
depicted in Figure 1. Then deﬁne D θ : Cθ→ C to be
Dθ(z) =
∫ eiθ/2∞
z
∫ eiθ/2∞
w
e(ζ)
1− e(ζ) dζ dw , (117)
where the contours are contained in Cθ. Using this function we have the following asymp-
totics of Φ( z; τ ) in the upper half plane.
Lemma B.3. Suppose that Im( τ ) > 0 and ε∈ R>0. Then as τ→ i∞ with ﬁxed argument
and z is bounded away from the half lines C\Cθ and is bounded away from at least one of
the lines Im(( z + 1)τ ) = 0 and Im(( z + 1)τ ) by ε with θ = arg(−1/τ )∈ (0, π) there exists a
constant C∈ R>0 such that
⏐
⏐
⏐Φ( zτ ; τ )− e
(
Dθ(z)τ + 1
2D′
θ(z) +
K∑
k=2
Bk
k!
(2πi)k−2
τ k−1 Li2−k(e(z))
) ⏐
⏐
⏐ < C K ! ε−K|τ|−K . (118)
40 VERONICA F ANTINI AND CAMPBELL WHEELER
Figure 32. The blue region depicts the region the ﬁrst line of Equation ( 122)
considered for Φ( τ z; τ ) as τ is deﬁned and the green region depicts the region
the second line is deﬁned.
Proof. This follows from the Lemma B.1 when Im(( z + 1)τ ) >|τ|ε and the fact that in this
domain we have
|(qe(zτ ); q)∞− 1| < 2 exp(−2πε|τ|) . (119)
Then we use the fact that by the modularity of the θ-function and η-function, and the Jacobi
triple product
Φ( z; τ )Φ(−τ−z; τ ) = (qe(z); q)∞(e(−z); q)∞
(e(z/τ );~q)∞(~qe(z/τ );~q)∞
= iq1/6~q−1/6e(z2/2τ +z/2+z/2τ ). (120)
Therefore, this implies that for Im( zτ ) <|τ|ε
Φ( zτ ; τ ) = Φ( −τ− zτ ; τ )−1iq1/6~q−1/6e(z(z + 1 + 1/τ )τ /2) . (121)
Therefore, using the ﬁrst half of the proof and the relations betw een the polylogarithms
and Dθ under the map z↦→−z gives the result when Im( zτ ) <|τ|ε, which completes the
proof. □
Remark B.4. The previous remark about the function L θ also applies to the quantum
dilogarithm. An easy way to see that D θ is the correct branching of the multivalued function
Li2(e(z))/(2πi)2 is that the zeros and poles of Φ( zτ ; τ ) accumulate to the lines C\Cθ in the
limit as τ tends to inﬁnity. Here the most important point is that this domain re mains
connected for all θ∈ (0, 2π), which was not true for the lone Pochhammer symbol.
B.3. Asymptotics of Faddeev’s dilogarithm for Im(τ ) near 0. To understand the
asymptotics as we cross the real numbers we use the following equa lity for Im( z + τ ) > 0
and Im( z/τ ) > 0 along with Re(−√τ− 1/√τ ) < Re(z/√τ ) < 0
Φ( z; τ ) = (qe(z); q)∞
(e(z/τ );~q)∞
= exp
( ∞∑
k=1
e(kz)
k(q−k− 1)− e(kz/τ )
k(~qk− 1)
)
= exp
( ∫
i√τ R+ε√τ
e((z + 1 + τ )w/τ )
(e(w)− 1)(e(w/τ )− 1)
dw
w
)
,
(122)
for some small ε > 0. The various regions where the expression for Φ( τ z; τ ) as τ tends to
inﬁnity are depicted in Figure 32.
SUMMABILITY FOR STATE INTEGRALS OF HYPERBOLIC KNOTS 41
The asymptotics of Faddeev’s quantum dilogarithm in the lower half pla ne can be carried out
by a completely similar analysis as in the upper half plane using the formu la for Im( τ ) < 0
given by
Φ( z; τ ) = (~q−1e(z/τ );~q−1)∞
(e(z); q−1)∞
. (123)
In the upper and lower half planes there is one technicality that when τ is very close to the
reals or argument comparable with ε (the bound for z from the branch cuts) we ﬁnd that for z
in a neighbourhood of the interval [−1 + 2ε,−2ε] the methods we have previously mentioned
fail to produce the asymptotics. We also have the issue that the pr evious methods do not
work when τ ∈ R>0. These two problems can be dealt with by using Faddeev’s original
formula given in Equation ( 122).
Lemma B.5. Suppose that τ∈ C\R≤0 and ε∈ R>0. Then as τ→∞ with ﬁxed argument
bounded by ε and z bounded away from Cθ by ε with θ = arg(−1/τ )∈ (π− ε, π + ε) there
exists a constant C∈ R>0 such that
⏐
⏐
⏐Φ( zτ ; τ )− e
(
Dθ(z)τ + 1
2D′
θ(z) +
K∑
k=2
Bk
k!
(2πi)k−2
τ k−1 Li2−k(e(z))
) ⏐
⏐
⏐ < C K ! ε−K|τ|−K . (124)
Proof. By deforming the contour to inﬁnity for Im( z) > 0 we have
∫
i√
τ R+ε1
√τ
e(zw)
(e(−w)− 1)
dw
w2−k =
∞∑
ℓ=1
e(ℓz)
ℓ2−k = Li 2−k(e(z)) , (125)
while for Im( z) < 0 we can deform in the other direction and ﬁnd that for k > 1 we have
∫
i√τ R+ε1
√τ
e(zw)
(e(−w)− 1)
dw
w2−k = −δk,2−
∞∑
ℓ=1
e(−ℓz)
(−ℓ)2−k
= Li 2−k(e(z)) ,
(126)
While for k = 0 we have
∫
i√τ R+ε1
√τ
e(zw)
(e(−w)− 1)
dw
w2−k = −(2πi)2( 1
2 z(z + 1) + 1
12 )−
∞∑
ℓ=1
e(−ℓz)
(−ℓ)2 = Dθ(z) , (127)
and k = 1 we have
∫
i√τ R+ε1
√τ
e(zw)
(e(−w)− 1)
dw
w2−k = −(2πi)(z + 1
2 ) +
∞∑
ℓ=1
e(−ℓz)
ℓ = D′
θ(z) . (128)
Therefore, these equations hold for all z in our region. We can use these equations to deduce
our desired asymptotics. We want to compute the asymptotics of t he integral
∫
C
e(zw)
(e(−w)− 1)(e(−w/τ )− 1)
dw
w , (129)
where for z with Re(( ε1− 1)√τ− 1/√τ ) < Re(z√τ ) < −ε1Re(√τ ) we can take C =
i√τ R + ε1
√τ . We can deform the contour of this integral so that for z bounded away from
Cθ by ε the integral converges. This is given up to exponentially small terms by the same
42 VERONICA F ANTINI AND CAMPBELL WHEELER
integral cut oﬀ with |w| <|√
τ|. Then by Taylor’s theorem there exists a constant C1 such
that for|w| <|√τ| we have
⏐
⏐
⏐ 1
e(−w/τ )− 1−
K∑
k=0
Bk
k!
( −2πiw
τ
) k−1⏐
⏐
⏐≤ C1
⏐
⏐
⏐2π w
τ
⏐
⏐
⏐
K
(130)
Therefore, we ﬁnd that
⏐
⏐
⏐
∫
C
( e(zw)
(e(−w)− 1)(e(−w/τ )− 1)− e(zw)
(e(−w)− 1)
K∑
k=0
Bk
k!
( −2πiw
τ
) k−1) dw
w
⏐
⏐
⏐
< C 1 (2π)K|τ|−K
∫
C
⏐
⏐
⏐ e(zw)
w1−K(e(−w)− 1)
⏐
⏐
⏐dw .
(131)
This ﬁnal integral can be split into two parts depending on which domin ates max{e(−w), 1}.
The size of one of these integrals is then approximated by a constan t times an integral of
the form ∫ ∞
0
exp(−2πεw)wK−1dw = (2 πε)−K(k− 1)! (132)
The other integral has a similar bound. Therefore, we see that the re is a constant C such
that
⏐
⏐
⏐
∫
i√
τ R+ε1
√τ
( e(zw)
(e(−w)− 1)(e(−w/τ )− 1)− e(zw)
(e(−w)− 1)
K∑
k=0
Bk
k!
( −2πiw
τ
) k−1) dw
w
⏐
⏐
⏐
< C K ! ε−K|τ|−K.
(133)
□
Theorem B.6. Suppose that τ ∈ C\R≤0 and ε ∈ R>0. Then as |τ| → ∞with ﬁxed
argument and z bounded away from Cθ by ε with θ = arg(−1/τ )∈ (0, 2π) there exists a
constant C∈ R>0 such that
⏐
⏐
⏐Φ( zτ ; τ )− e
(
Dθ(z)τ + 1
2D′
θ(z) +
K∑
k=2
Bk
k!
(2πi)k−2
τ k−1 Li2−k(e(z))
) ⏐
⏐
⏐ < C ε −K K!|τ|−K . (134)
Proof. The proof follows by combining the results of Lemma
B.1, Lemma B.3 and Lemma B.5.
□
Corollary B.7. If Im( z) > 0 and − arg(z) + π/2 < arg(τ ) < arg(z + 1) + π/2, Im( z) < 0
and−π/2− arg(z + 1) < arg(τ ) <− arg(z)− π/2, or z∈ (−1, 0) and τ ∈ C\R≤0, then
Φ( zτ ; τ ) is the Borel–Laplace resummation of its asymptotics.
Proof. As τ→∞ we have
⏐
⏐
⏐Φ( zτ ; τ )− e
(
Dθ(z)τ + 1
2D′
θ(z) +
K∑
k=2
Bk
k!
(2πi)k−2
τ k−1 Li2−k(e(z))
) ⏐
⏐
⏐ < C ε −K K!|τ|−K . (135)
Therefore, we see that Φ( zτ, τ ) is the Borel–Laplace resummation of its asymptotics for τ in
these cones. □
SUMMABILITY FOR STATE INTEGRALS OF HYPERBOLIC KNOTS 43

---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-027-appendix-an-integral-formula-for-the-asai-l-func
section_title: "Appendix: An integral formula for the Asai L-function"
section_number: null
pages: 36-43
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
---
In this appendix, we provide a slight extension of Ghate’s results on the rationality of Asai L-values.
The main result is given in Theorem A.9. Most of the arguments go through almost exactly as in [Ghate
1999]. However, in order to present the p-adic interpolation computations in the main body of the paper
in the most natural way, we have adopted conventions which differ from those of Ghate’s in a few places:
ﬁrstly, the Eisenstein series which we work with are slightly different, as is our normalisation for the
Clebsch–Gordan map; secondly, we focus on computing the special values of the Asai L-series in the left
half of the critical strip (i.e., 1⩽ s⩽ k+ 1) rather than the right half (i.e., k+ 2⩽ s⩽ 2k+ 2) considered
by Ghate. Hence we shall explain how to modify his results for our setting.
Notation. Let F∈ Skk(U∗
F,1(n)) be a Bianchi modular form of weight (k, k) and level U∗
F,1(n), and
suppose that F is an eigenvector for the action of
(−1
1
)
(necessarily with eigenvalue either+1 or−1).
(i) WriteψF for the Dirichlet character given by restricting the character ofF from(OF/n)× to(Z/N)×.
(ii) LetωF be the differential form on H3 associated to F as in Section 2H. This descends to a differential
form on0∗
F,1(n)\H3.
p-adic Asai L-functions of Bianchi modular forms 1703
(iii) Write Fn, 0⩽ n⩽ 2k+ 2, for the n-th coordinate projection of F in the standard basis{X 2k+2−nY n}
of V2k+2(C), which is a C-valued function on H3.
Deﬁnition of the integrals. Pulling backωF via the inclusionι: Y1(N)=01(N)\H↪→0∗
F,1(n)\H3, we
obtain a0Q,1-invariant differential on H.
For each j with 0⩽ j⩽ k, we have a map of GL+
2(R)-modules
CG[k,k, j],⋆: Vk(C)⊗ Vk(C)→ V2k−2 j(C)
given by the transpose of the mapCG[k,k, j] of (5-2) above. Let us write(ι∗ωF)2k−2 j for CG[k,k, j]∗(ι∗ωF)∈
H1
cusp
(
YQ,1(N), V2k−2 j(C)
)
.
Deﬁnition A.1. Deﬁne
I j
F(s):=
∫
Y1(N)
(ι∗ωF)2k−2 j∧ E(2k−2 j+2)
1/N (τ, s) dw⊗2k−2 j(dx+ idy).
Here E(2k−2 j+2)
1/N (τ, s) is as in (3-1), and dw⊗2k−2 j is considered as a section of a symmetric tensor
power of T1,dR, which we are identifying with the de Rham cohomology of the universal elliptic curve
C/(Zτ+ Z).
The goal of this appendix is to evaluate I j
F(s) in terms of LAs(F, s+ 2k− j+ 2). We shall only use
this for one speciﬁc value of s, namely s=− 1− 2k+ 2 j, as the left-hand side of Proposition 7.4 is
exactly I j
F(−1− 2k+ 2 j) (by the adjointness of pushforward and pullback). However, since this s-value
lies outside the domain of convergence of the sums deﬁning the Eisenstein series and Asai L-function, we
need to work initially with an arbitrary s such thatℜ(s)≫ 0 and obtain the result by analytic continuation.
An explicit description of the differential. We recall the description of(ι∗ωF)2k−2 j obtained in [Ghate
1999]. Ghate uses a slightly different normalisation for the projection Vk⊗ Vk→ V2k−2 j (see [op. cit.,
Lemma 2]): he considers the map sending a polynomial δ( X, Y, X, Y)∈ Vkk(C) to
1
( j!)2∇ jδ( X, Y)
⏐⏐⏐
X=X,Y=Y
, where∇:=
( ∂2
∂ X∂Y
− ∂2
∂Y∂ X
)
.
Proposition A.2. We have
CG[k,k, j],⋆(δ)=(−1) j j!· 1
( j!)2∇ j(δ)
⏐⏐⏐
X=X,Y=Y
.
Proof. It is clear that these two maps must be proportional (since V2k−2 j is irreducible and appears with
multiplicity one in Vkk ), so we must compute the constant of proportionality. Let w[s,k−s], for 0⩽ s⩽ k,
be the basis of Tk(C) dual to the basis X sY k−s of Vk(C). An explicit formula for CG[k,k, j] in this basis is
1704 David Loeﬄer and Chris Williams
given in [Kings et al. 2020, Proposition 5.1.2]. 3 One case of this formula is
CG[k,k, j](w[0,2k−2 j])=
j∑
i=0
(−1)i(k− i)!(k+ i− j)!
(k− j)!(k− j)! w[i,k−i]⊗w[ j−i,k− j+i].
Pairing CG[k,k, j](w[0,2k−2 j]) with X 0Y k X jY k− j pulls out the i= 0 term in the sum, and yields the nonzero
scalar k!/(k− j)!. Meanwhile, applying (1/( j!)2)∇ j to X 0Y k X jY k− j gives the polynomial
(−1) jk!
j!(k− j)!Y k− jY k− j,
and if we set Y= Y and pair this withw[0,2k−2 j], we obtain
(−1) jk!
j!(k− j)!.
So the constant of proportionality is (−1) j j! as required. □
We thus get extra factors of(−1) j j! compared to [Ghate 1999], so we have the following formula:
Proposition A.3 [Ghate 1999, §5.2]. We have
(ι∗ωF)2k−2 j(x, y)=(−1) j j!
2k−2 j∑
𝓁=0
(A𝓁 dx+ 2B𝓁 dy)y2k− j−𝓁(X− xY)𝓁Y 2k−2 j−𝓁,
where
A𝓁=
k+1∑
n=0
(−1)ngn, j(x, y)a( j,𝓁, n), B𝓁=
k+1∑
n=0
(−1)ngn, j(x, y)b( j,𝓁, n),
gn, j(z, t)=
(2k+ 2
n
)−1{Fn(z, t)+(−1)k+1−n+ j F2k+2−n(z, t) if n∈{ 0,..., k},
Fk+1(z, t) if n= k+ 1,
and a( j,𝓁, n) and b( j,𝓁, n) are constants given by
a( j,𝓁, n)=
( k
j
)2
(−1)
1
2(k+n−𝓁− j)
j∑
t=0
(−1)t
( j
t
)[( k− j
1
2(k− j−𝓁+n)−t
)( k− j
1
2(3k−3 j−𝓁−n)+t
)
+
( k− j
1
2(k− j−𝓁+n−2)−t
)( k− j
1
2(3k−3 j−𝓁−n+2)+t
)]
,
b( j,𝓁, n)=
( k
j
)2
(−1)
1
2(k+n−1−𝓁− j)
j∑
t=0
(−1)t
( j
m
)( k− j
1
2(k− j−𝓁+n−1)−t
)( k− j
1
2(3k−3 j−𝓁−n+1)+t
)
.
(Here it is understood that
( c
d
)
= 0 if d is negative or not an integer). □
3Note that the formula appears with some typographical errors in [loc. cit .]: the terms (k− r+ i)! and(k′− r′+ j− i)!
should be(k− r− i)! and(k′− r′− j+ i)! respectively.
p-adic Asai L-functions of Bianchi modular forms 1705
Pairing with Eisenstein series and integrating. We shall compute I j
F(s) using a Rankin–Selberg unfold-
ing argument. Factoring out the denominator in (3-1), we have
E(k)
1/N(τ, s)=0(s+ k)N 2s+k
(−2πi)kπ s
∑
t>1
(t,N)=1
t−k−2s⟨t⟩−1
[ ∑
γ∈0∞\01(N)
(Im(τ) s|kγ)
]
, (A-1)
where as usual⟨u⟩ denotes the action of any element
( a
c
b
d
)
∈00(N) such that d≡ u mod N. The adjoint
of⟨u−1⟩ is⟨u⟩, which commutes withι∗. Hence, considering ωF as a differential on H3, we have
⟨u⟩ι∗ωF=ψF(u)(ι∗ωF).
In particular, for Re(s)≫ 0 we have
I j
F(s)=0(s+ k j)N 2s+k j
(−2πi)k jπ s
[ ∑
u>1
(u,N)=1
ψF(u)u−k j−2s
][∫
0∞\H
(ι∗ωF)2k−2 j∧ Im(τ) sdw⊗2k−2 jdτ
]
,
where we have deﬁned k j= 2k− 2 j+ 2 for ease of notation, and 0∞:=
{( 1
0
n
1
)
: n∈ Z
}
. The ﬁrst
bracketed term is simply the Dirichlet L-series L(N)(ψF, 2s+ k j).
We shall now substitute the explicit expression for(ι∗ωF)2k−2 j into the above. The basis vectors X, Y
correspond to the natural basis (τ, 1) of H1(C/(Zτ+ Z), Z)∼= Zτ+ Z, so we have⟨X, dw⟩= τ and
⟨Y, dw⟩= 1; hence
⟨(X− xY)𝓁Y 2k−2 j−𝓁, dw⊗2k−2 j⟩=⟨ (X− xY), dw⟩𝓁·⟨ Y, dw⟩2k−2 j−𝓁=(iy)𝓁.
So we obtain the following formula:
Proposition A.4. We have
I j
F(s)= H(s, k, j)· L(N)(ψF, 2s+ k j)
k+1∑
n=0
(−1)nc′( j, n)
∫ ∞
0
∫ 1
0
gn, j y2k− j+s dx dy,
where
H(s, k, j):=(−1) j j!0(s+ k j)N 2s+k j
(−2πi)k jπ s (A-2)
and
c′( j, n):=
2k−2 j∑
𝓁=0
i𝓁[
i· a( j,𝓁, n)− 2b( j,𝓁, n)
]
. □
To compute this, we look at components separately. In particular, consider the integral
J n,r
F (s):=
(2k+ 2
n
)−1∫ ∞
0
∫ 1
0
Fn(x, y)yr+s dx dy.
The expression I j
F is a linear combination of J n,2k− j
F for varying n.
1706 David Loeﬄer and Chris Williams
Proposition A.5. We have
J n,r
F (s)= G(n, r, s)
∑
0⁄=m∈Z
(−σ( m))k+1−nW f
( m√−D, F
)
|m|−(s+r+2),
whereσ( m) is the sign of m and
G(n, r, s)=0
(s− k+ n+ r+ 1
2
)
0
(s+ k− n+ r+ 3
2
)
2s+r
(√
D
4π
)s+r+2
.
Proof. Recall the Fourier expansion of Fn from [Ghate 1999, equation (16)]; we have
Fn(x, y)= y
(2k+ 2
n
) ∑
ζ∈F×
W f(ζ, F)
( ζ
i|ζ|
)k+1−n
× Kn−k−1(4π|ζ|y)e2πiTrF/Q(ζ x).
We substitute this in and isolate the terms involving x.
Lemma A.6. Suppose W f(ζ, F)⁄= 0. Then we have
∫ 1
0
e2πiTrF/Q(ζ x) dx=
{1 ifζ= m/√−D with 0⁄= m∈ Z,
0 otherwise.
Proof. We know that W f(ζ, F)⁄= 0 only ifζ∈ D−1. But since D−1 is the inverse different of F/Q, for
any suchζ we have TrF/Q(ζ)∈ Z. Hence the integral is 0 unless TrF/Q(ζ)= 0, which happens if and
only ifζ= m/√−D for some nonzero integer m, as required. □
In particular, the sum collapses to one over nonzero integers, and we remove the terms involving x.
We also see that ifζ= m/√−D, thenζ/ i|ζ|= i|ζ|/ζ=−σ( m). We conclude that
J n,r
F (s)=
∑
0⁄=m∈Z
(−σ( m))k+1−nW f
(
m√−D, F
)∫ ∞
0
ys+r+1Kn−k−1
(4π|m|y√
D
)
dy
=
( ∑
0⁄=m∈Z
(−σ( m))k+1−nW f
(
m√−D, F
)
|m|−(s+r+2)
)
× G(n, r, s),
(A-3)
where
G(n, r, s)=
∫ ∞
0
ys+r+1Kn−k−1(4πy/
√
D) dy.
A standard integral formula (see [Hida 1994, p. 485]) gives the explicit expression for G(n, r, s) in the
statement of Proposition A.5, completing the proof. □
Corollary A.7. (i) If k+ 1− n+ j is odd, then
c′( j, n)
∫ ∞
0
∫ 1
0
gn, j(x, y)yr+s dx dy= 0,
where gn, j is as deﬁned in Proposition A.3.
(ii) For𝓁 odd in the sum in Proposition A.3, only the a( j,𝓁, n) terms contribute to I j
F(s). For𝓁 even,
only the b( j,𝓁, n) terms contribute.
p-adic Asai L-functions of Bianchi modular forms 1707
Proof. For (i), we assume ﬁrst that 0⩽ n⩽ k. Recall that gn, j(z, t) is deﬁned as a scalar multiple of
Fn(z, t)+(−1)k+1−n+ j F2k+2−n(z, t). Proposition A.5 shows that
J n,r
F (s)= J 2k+2−n,r
F (s)
(a consequence of the fact that Kr= K−r). Suppose that k+ 1− n+ j is odd; then unwinding the integral
of part (i), we ﬁnd that it is equal to
J n,r
F (s)− J 2k+2−n,r
F (s)= 0,
as required.
This leaves the case n= k+ 1. In this case, k+ 1− n+ j= j. But if j is odd, then in the deﬁnition
of both a( j,𝓁, k+ 1) and b( j,𝓁, n+ 1), the t and j− t terms appear with opposite signs and are easily
checked to negate each other. Hence c′( j, n)= 0, and we are done.
For part (ii), for the n term to contribute to I j
F(s), by (i) k+ j+ n must be odd. If 𝓁 is odd, it follows
that all of the binomial coefﬁcients deﬁning b( j,𝓁, n) involve noninteger entries, so vanish; and if𝓁 is
even, similarly the a( j,𝓁, n) are all 0. □
By including these parity conditions, and exploiting the symmetry between binomial coefﬁcients to
renormalise the sum to be from 0 to 2k+ 2 (in the process removing the disparity between 0⩽ n⩽ k and
n= k+ 1) we arrive at the following.
Corollary A.8. We have
I j
F(s)= H(s, k, j)· L(N)(ψF, 2s+ k j)
2k+2∑
n=0
k+ j+n+1 even
(−1) j2c( j, n)J n,2k− j
F (s),
where
c( j, n):=(−1)k+1
2
2k−2 j∑
𝓁=0
𝓁 even
i𝓁[
a( j,𝓁− 1, n)− 2b( j,𝓁, n)
]
,
(normalised to agree with[Ghate 1999, p. 628]) where we take a( j,−1, n)= 0 for all j, n.
The following is the main result of this appendix.
Theorem A.9. Let 0⩽ j⩽ k. Then
I j
F(s)=
{
C(k, j, s)LAs(F, s+ 2k− j+ 2) if
(−1
1
)∗
F=(−1) j F
0 if
(−1
1
)∗
F=(−1) j+1F,
where
C(k, j, s):=(−1) j
(√
D
2π
)s+2k− j+2
H(s, k, j)G′
∞(s)
1708 David Loeﬄer and Chris Williams
for
G′
∞(s)=
(−1) j√π
(k
j
)2
2s
0
( s
2+ k− j+ 1
)
0
( s+1
2
) 0(s+ k− j+ 1)0(s+ 2k− j+ 2)
0(s+ 2k− 2 j+ 2) .
Here I j
F(s) was deﬁned in Deﬁnition A.1 and H(s, k, j) was deﬁned in (A-2).
Proof. In Proposition A.5, since k+ j+ n+ 1 is even, the exponent on(−σ( m)) is equal to j. In this
expression, we collapse the sum over m to be only over positive integers, using the relation W f(−ζ, F)=
W f(ζ,
(−1
1
)∗
F). If the eigenvalue of F for this involution is (−1) j+1, then the terms for m and−m
sum to 0, so the sum over all m vanishes and I j
F is identically 0, which proves the theorem in this case. If
the eigenvalue is(−1) j then the terms for−m and m are equal; assuming that this is the case, we have
J n,2k− j
F (s)= 2G(n, 2k− j, s)
∑
m>1
W f
(
m√−D, F
)
m−(s+2k− j+2).
Substituting this into Corollary A.8, the sum over positive m and the Dirichlet L-series combine to give
exactly LAs(F, s+ 2k− j+ 2), which we can bring outside the sum over n. The remaining terms are
4H(s, k, j)
2k+2∑
n=0
k+ j+n+1 even
(−1) jc( j, n)G(n, 2k− j, s)=(−1) j
(√
D
2π
)s+2k− j+2
H(s, k, j)G′
∞(s),
where
G′
∞(s):=
2k+2∑
n=0
k+ j+n+1 even
c( j, n)0
(s+ k+ n− j+ 1
2
)
0
(s+ 3k− n− j+ 3
2
)
is what Ghate [1999, p. 628] called G′
∞(s, f). The main result of [Lanphier and Skogman 2014] showed
that G′
∞(s) has the form stated in the theorem. □
We have proved Theorem A.9 assumingℜ(s)≫ 0; but both sides have analytic continuation to alls∈ C,
so the theorem remains valid on this larger domain. Thus we may evaluate at the value s=− 1− 2k+ 2 j,
and we ﬁnd:
Corollary A.10. Let 0⩽ j⩽ k. Then
I j
F(−1− 2k+ 2 j)=



C′(k, j)
N 2k−2 j LAs(F, j+ 1) if
(−1
1
)∗
F=(−1) j F,
0 if
(−1
1
)∗
F=(−1)1+ j F,
where
C′(k, j)=(−1)k+1
√−D
j+1
( j!)2(k
j
)2
2·(2πi) j+1 . □
This proves Proposition 7.4 of the main text.
p-adic Asai L-functions of Bianchi modular forms 1709

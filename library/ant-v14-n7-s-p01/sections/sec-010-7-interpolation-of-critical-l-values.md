---
doc_id: ant-v14-n7-s-p01
doc_title: "p-adic Asai L-functions of Bianchi modular forms"
section_id: sec-010-7-interpolation-of-critical-l-values
section_title: "Interpolation of critical L-values"
section_number: 7
pages: 30-41
source_pdf: ant-v14-n7-s-p01.pdf
source_sha256: 976199bfca4ac086
doc_brief: "p-adic Asai L-functions of Bianchi modular forms — 13 sections: Introduction; Preliminaries and notation; Siegel units and weight 2 Asai–Eis"
---
In this section, we want to show that the values of the Asai p-adic L-function at suitable locally algebraic
characters are equal to special values of the complex L-function.
7A. Automorphic forms for G ∗. We shall need to work with automorphic forms for the group G∗ of
Deﬁnition 2.1 above. We refer the reader to [Lei et al. 2018] for an account of automorphic forms for the
group G∗, and their relation to those for G, in the analogous setting where F is a real quadratic ﬁeld.
For U∗⊂ G∗(ˆZ), we let Skk(U∗) denote the space of automorphic forms for G∗ of level U∗ and
weight(k, k). These are deﬁned in the same way as for G; that is, they are functions
G∗(Q)+\G∗(AQ)/U∗→ V2k+2(C)
transforming appropriately under R>0· SU2(C), and with suitable harmonicity and growth conditions.
If U∗= U∩ G∗ for an open compact subgroup U of G(A f
Q), then there is a natural pullback map
∗: Skk(U)→ Skk(U∗).
Any F∈ Skk(U∗
F,1(n)) is uniquely determined by its restriction to G∗(R), since Y∗
F,1(n) is connected.
This restriction can be described by a Fourier–Whittaker expansion of the form
F
((y∞ x∞
0 1
))
=| y∞|
∑
ζ∈F×
W f(ζ, F)W∞(ζ y∞)eF(ζ x),
where W f(−, F) is a function on F× (supported in D−1). Of course, if F=∗(9) for some 9∈
Skk(UF,1(n)), then W f(−, F) is simply the restriction of W f(−,9) to F×⊂(A f
F)×.
Remark 7.1. The theory of automorphic representations of G∗ is more complicated than that of G: not all
cuspidal representations are globally generic, and the naive formulation of strong multiplicity one is false,
due to the presence of nontrivial global L-packets. In practice, this means that although cusp forms for G∗
do have Fourier–Whittaker expansions, one cannot necessarily recover all of their Fourier–Whittaker coef-
ﬁcients from the action of the Hecke algebra of G∗(A f
Q). However, this will not concern us here, since we
will only consider automorphic forms for G∗ which are restrictions of eigenforms for G, or twists of these.
p-adic Asai L-functions of Bianchi modular forms 1699
Lemma 7.2. Let F∈ Skk(U∗
F,1(n)),χ a Dirichlet character of conductor m, and a∈ OF/mOF. Then
the function
Ra,χ F=
∑
t∈(Z/m)×
χ(t)κ∗
at/m(F)
is in Skk(U∗
F,1(m2n)), and its Fourier–Whittaker coefﬁcients forζ∈ D−1 are given by
W f(ζ, Ra,χ F)= G(χ)χ(trF/Q aζ) W f(ζ, F),
where G(χ):=∑
t∈(Z/m)×χ(t)e2πit/m is the Gauss sum ofχ.
Proof. It is clear that Ra,χ F has level U∗
F,1(m2n), since each term in the sum is invariant underU∗
F,1(m2n).
It remains to compute its Fourier–Whittaker coefﬁcients. We have
W f(ζ, Ra,χ F)= W f(ζ, F)
∑
t∈(Z/m)×
χ(t)eF(ζ at/m)
= W f(ζ, F)
∑
t∈(Z/m)×
χ(t)e2πit tr(aζ)/ m.
This is 0 unless the integertr(aζ) is a unit modulo m, in which case it isχ(tr(aζ))−1G(χ), as required.□
7B. An integral formula for the Asai L-function. In this section, we describe an integral formula for
the Asai L-function of a Bianchi eigenform twisted by a Dirichlet character χ. This is a generalisation of
[Ghate 1999] (which considers the case where χ is trivial), and we shall prove our theorem by reduction
to his setting using the twisting maps Ra,χ.
Let 0⩽ j⩽ k, and deﬁne
I j
9,b,m:=
⟨
φ∗
9, (κb/m)∗ι∗CG[k,k, j]
∗ F(2k−2 j+2)
1/m2 N (τ) dw⊗2k−2 j dτ
⟩
,
where⟨−,−⟩ denotes the pairing of (6-1),φ∗
9=∗φ9 as before, and we view the Eisenstein class as an
element of the Betti cohomology (with complex coefﬁcients) using the standard comparison isomorphism.
Theorem 7.3. Letχ be a Dirichlet character of odd conductor m, and let 0⩽ j⩽ k. Let a∈ OF be the
value we chose in the remarks before Deﬁnition 6.4 (so that a− aσ=√−D). Then
∑
t∈(Z/mZ)×
χ(t)I j
9,at,m=



C′(k, j)G(χ)
(m2N)2k−2 j9
LAs(9,χ, j+ 1) if(−1) jχ(−1)= 1,
0 if(−1) jχ(−1)=− 1,
where
C′(k, j)=(−1)k+1
√−D
j+1
( j!)2(k
j
)2
2·(2πi) j+1N 2k−2 j.
We begin by explaining how to reduce the theorem to the case m= 1. Note that the deﬁnition of the
Asai L-function depends only on the pullback ∗9, and in fact makes sense for any F∈ Skk(U∗
F,1(n)),
1700 David Loeﬄer and Chris Williams
whether or not it is in the image of∗, as long as it is an eigenvector for the operators⟨x⟩ for x∈(Z/N Z)×.
If these operators act on F via the characterεF, then we can deﬁne
LAs(F, s):= L(N)(εF, 2s− 2k− 2)
∑
n>1
W f(n/
√
−D, F)n−s.
One sees easily that if χ is a Dirichlet character of odd conductor, and a is the value we chose above (so
that a− aσ=√−D), then
LAs(Ra,χ∗9, s)= G(χ)· LAs(9,χ, s).
Proposition 7.4. Let F∈ Skk(U∗
F,1(n)), and let N= n∩ Z. Then we have
⟨
ωF,ι∗CG[k,k, j]
∗ F(2k−2 j+2)
1/N (τ) dw⊗2k−2 j dτ
⟩
=
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
F=(−1) j+1F.
The proof of the proposition is very similar to the work of Ghate [1999], but our conventions are a
little different, so we shall give a proof using our conventions in the Appendix; see Corollary A.10.
Applying this proposition to Ra,χ∗9 and dividing by9 proves Theorem 7.3, since
(−1
1
)∗
acts on
Ra,χ∗9 asχ(−1).
7C. Interpolation of critical values. We now use the integral formula of Theorem 7.3 to relate the values
of the measure LAs
p (9) to critical values of the classical Asai L-function.
Theorem 7.5. Let p be an odd prime. Let9 be an ordinary Bianchi eigenform of weight(k, k) and level
UF,1(n), where all primes above p divide n, with Up-eigenvalueλp= c(pOF,9) . Letχ be a Dirichlet
character of conductor p r, and let 0⩽ j⩽ k.
(a) Ifχ(−1)(−1) j= 1, then
LAs
p (9,χ, j)= C(k, j)Ep(9,χ, j)G(χ)
9
· LAs(9,χ, j+ 1),
where
C(k, j):=(−1)k+1 j!·√−D
2·(2πi) j+1, Ep(9,χ, j):=



(
1− p j
λp
)
if r= 0,
(p jλ−1
p )r if r> 0.
(b) Ifχ(−1)(−1) j=− 1, then
LAs
p (9,χ, j)= 0.
Remark. Up to rescaling 9, this is precisely the interpolation formula predicted by Coates and
Perrin-Riou (see Section 2G).
p-adic Asai L-functions of Bianchi modular forms 1701
Proof. For convenience, let e[r] denote the operator(U−r
p )∗eord,∗ if r> 1, and(1− p j(U−1
p )∗)eord,∗ if
j= 0. By the deﬁnition of the measure and Proposition 6.3, we have
LAs
p (9,χ, j)= 1
√−D
j
j!
(k
j
)2
∑
t∈(Z/pr)×
χ(t)⟨φ∗
9, e[r]4k, j
pr,n,at⟩.
We know that(Up)∗ is the adjoint of(Up)∗, andφ∗
9 is a(Up)∗ eigenvector with unit eigenvalueλp;
thus the adjoint of e[r] acts onφ∗
9 as p− jr Ep(9,χ, j), so we have
LAs
p (9,χ, j)= Ep(9,χ, j)
p jr√−D
j
j!
(k
j
)2
∑
t∈(Z/pr)×
χ(t)⟨φ∗
9,4 k, j
pr,n,at⟩.
Now, by Lemma 5.4, we have4k, j
pr,n,at= p jr(κat/pr)∗ι∗CG[k,k, j]
∗ (Eis2k−2 j
p2r N ), and hence
⟨φ∗
9,4 pr,n,at⟩= p jr⟨
(CG[k,k, j])∗ι∗κ∗
at/pr(φ∗
9), Eis2k−2 j
p2r N
⟩
,
where the ﬁrst cup product is at the level of 0∗
F,1(n)\H3, and the second cup product is at the level of
01(p2r N)\H. Now work at the level of complex coefﬁcients. We know that
Eis2k−2 j
p2r N = Eis2k−2 j
p2r N =−(p2r N)2k−2 j F(2k−2 j+2)
1/p2r N (τ) dw⊗2k−2 j dτ,
Accordingly, we see that
LAs
p (9,χ, j)=−(p2r N)2k−2 j Ep(9,χ, j)
√−D
j
j!
(k
j
)2
∑
t∈(Z/pr)×
χ(t)I j
9,at,pr,
where I j
9,b,m is as deﬁned in the previous section. Using Theorem 7.3, we see that this expression vanishes
unlessχ(−1)(−1) j= 1, in which case we have
LAs
p (9,χ, j)=− Ep(9,χ, j)
9
√−D
j
j!
(k
j
)2× C′(k, j)G(χ) LAs(9,χ, j+ 1)
= C(k, j)Ep(9,χ, j)G(χ)
9
· LAs(9,χ, j+ 1),
which completes the proof of the theorem. □
As an immediate corollary, we get an identical interpolation formula for cLAs
p (9) with the additional
factor(c2− c2 j−2kε9(c)χ(c)2).
Remark 7.6. (i) The factor Ep(9,χ, j) is nonzero if r> 1. If r= 0 then this factor vanishes if and
only if k= 0,9 is new at the primes above p, andε9(p)= 1. In this case the p-adic L-function has an
exceptional zero at the trivial character. For exceptional zeroes of the standard p-adic L-function of a
Bianchi cusp form, a theory of L-invariants was developed in [Barrera Salazar and Williams 2019]; it
would be interesting to investigate analogues of this for the Asai L-function.
1702 David Loeﬄer and Chris Williams
(ii) The measure LAs
p (9) depends on the choice of√−D ﬁxed at the start; indeed, this choice was used
to pick a value of a∈ OF, which in turn was used to construct the Asai–Eisenstein elements. This choice
is further encoded by the appearance of
√
D= i√−D in the interpolation formula. Choosing the other
square root simply scales the measure by−1. The measure also depends on the choice of period 9, and
again a different choice changes the measure up to a scalar.
(iii) If the Bianchi eigenform 9 (or, more precisely, the automorphic representation it generates) is the
base-change lift of an elliptic modular eigenform f of weight k+ 2 and characterε f , then the complex
Asai L-function factors as
LAs(9,χ, s)= L(Sym2 f,χ, s)L(χε fεF, s− k− 1),
whereεK is the quadratic character associated to K. Note that all three L-functions in the above formula
have critical values at integer points s= 1+ j with 0⩽ j⩽ k and(−1) jχ(−1)= 1. By a comparison
of interpolating properties at these points, one can verify that if f is ordinary at p, then there is a
corresponding factorisation of LAs
p (9) as a product of a shifted p-adic Dirichlet L-function and Schmidt’s
p-adic L-function for Sym2 f.
This factorisation shows, in particular, that the possibility of poles of the p-adic Asai L-function is a
genuine aspect of the situation, rather than a shortcoming of our method: if ε fεF= 1, then one of these
factors is the p-adic Riemann zeta function ζp(s− k− 1), which has a simple pole at s= k+ 2. If f
has CM by an imaginary quadratic ﬁeld K (with K⁄= F, so that9= BC( f) is cuspidal), then there is a
second abelian factor L(χε fεK, s− k− 1); this gives rise to examples where both of the zeros of the
factor c2− c−2kε9(c)[c]2 correspond to genuine poles of LAs
p (9).
Appendix: An integral formula for the Asai L-function
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

---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-026-7c-interpolation-of-critical-values
section_title: "7C. Interpolation of critical values"
section_number: null
pages: 34-36
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
---
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

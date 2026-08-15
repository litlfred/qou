---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-025-7b-an-integral-formula-for-the-asai-l-function
section_title: "7B. An integral formula for the Asai L-function"
section_number: null
pages: 33-34
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
---
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

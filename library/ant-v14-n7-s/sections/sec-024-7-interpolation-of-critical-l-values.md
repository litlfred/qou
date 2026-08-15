---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-024-7-interpolation-of-critical-l-values
section_title: "Interpolation of critical L-values"
section_number: 7
pages: 32-33
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
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

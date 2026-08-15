---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-002-1b-statement-of-the-main-theorem
section_title: "1B. Statement of the main theorem"
section_number: null
pages: 4-5
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
---
which is an eigenform for the Hecke operators. We assume that the level n of9 is divisible by all primes
p| p of F; this leads to no loss of generality, since we may replace 9 by a p-stabilisation if necessary.
We let N be the integer generating the ideal n∩ Z.
The Asai L-function of9 is deﬁned by
LAs(9, s):= L(N)(ε9,Q, 2s− 2k− 2)
∑
n>1
c(nOF,9) n−s,
whereε9,Q is the restriction to ˆZ
×
of the nebentypus character of 9, L(N)(−) denotes the Dirichlet
L-function with its Euler factors at primes dividing N omitted, and c(m,9) is the Hecke eigenvalue of9
at the ideal m. We deﬁne similarly the twisted Asai L-function LAs(9,χ, s), for a Dirichlet character χ
(see Deﬁnition 2.10 below).
This function LAs(9, s) has an Euler product, in which the factors at primes 𝓁 ∤ N can be interpreted
in terms of Galois representations: they are the local Euler factors of the tensor induction to Gal(Q/Q)
of the compatible family of 2-dimensional 𝓁-adic representations of Gal(Q/F) attached to9. (We shall
discuss the Euler factors at the “bad” primes in Section 2F below.) The Asai L-function should not be
confused with the standard L-function
Lstd(9, s):=
∑
mPOF
c(m,9) Nm(m)−s
that corresponds to the usual (rather than tensor) induction of the same family ofGal(F/F)-representations.
We choose a ﬁnite extension L/Qp, containing F and the Hecke eigenvalues of 9, with ring of
integers R, and we assume that 9 is ordinary at p, i.e., c(pOF,9) is a unit in R.
p-adic Asai L-functions of Bianchi modular forms 1671
Theorem 1.1. For any integer c> 1 coprime to 6n, there exists a p-adic measure
cLAs
p (9)∈ R[[Z×
p]]
on Z×
p satisfying the following interpolation property: ifχ is a Dirichlet character of conductor pr, and
0⩽ j⩽ k, then we have
∫
Z×p
χ( x)x j dcLAs
p (9)(x)=
{(∗)LAs(9,χ, j+ 1) ifχ(−1)(−1) j= 1,
0 ifχ(−1)(−1) j=− 1,
where(∗) is an explicit factor (which is always nonzero if r> 1).
See Theorem 7.5 of the main text for a precise statement. Note that cLAs
p interpolates all critical values
in the left half of the critical strip. The critical values in the right half are related to these via a functional
equation, but we do not make this explicit.
It is possible to remove the dependence on c entirely if the restriction to Q of the character of 9
is nontrivial and does not have p-power conductor. If this condition is not satisﬁed, then we can only
remove c at the cost of passing to a slightly larger space of “pseudomeasures”, which may be interpreted
as meromorphic (rather than analytic) functions on p-adic weight space; this is a p-adic counterpart of
the fact that, for certain eigenforms 9, the Asai L-function and its twists can have poles. The details of
this are contained in Section 6B.

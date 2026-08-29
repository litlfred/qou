---
doc_id: arxiv-math-9905032v2
doc_title: "ASYMPTOTICS OF PLANCHEREL MEASURES FOR SYMMETRIC GROUPS"
section_id: sec-023-31-proof-of-theorem-3-we-refer-the-reader-to-sec
section_title: "Proof of Theorem 3. We refer the reader to Section 1.3 of the"
section_number: 3.1
pages: 18-20
source_pdf: 9905032v2.pdf
source_sha256: ba933d4cb484964b
doc_brief: "ASYMPTOTICS OF PLANCHEREL MEASURES FOR SYMMETRIC GROUPS — We consider the asymptotics of the Plancherel mea- sures on partitions of n as n goes to inﬁnity."
---
Introduction for the deﬁnition of a regular sequence X(n) ⊂ Z and the
statement of Theorem 3. Also, in this section, we shall be wor king in
the bulk of the spectrum, that is, we shall assume that all num bers ai
ASYMPTOTICS OF PLANCHEREL MEASURES 19
deﬁned in (1.10) lie inside ( −2, 2). The edges ±2 of the spectrum and
its exterior will be treated in the next section.
In our proof, we shall follow the strategy explained in Secti on 1.5.
Namely, in order to compute the limit of ̺(n, X(n)) we shall use the
contour integral
̺(n, X(n)) = n!
2πi
∫
|θ |=n
̺θ (X(n)) eθ
θn+1 dθ ,
compute the asymptotics of ̺θ for θ ≈ n, and estimate |̺θ | away from
θ = n. Both tasks will be accomplished using classical results ab out
the Bessel functions.
We start our proof with the following lemma which formalizes the
above informal depoissonization argument. The hypothesis of this
lemma is very far from optimal, but it is suﬃcient for our purp oses.
For the rest of this section, we ﬁx a number 0 < α < 1/4 which shall
play an auxiliary role.
Lemma 3.1. Let {fn} be a sequence of entire functions
fn(z) = e−z
∑
k≥0
fnk
k! zk , n = 1, 2, . . . ,
and suppose that there exist such constants f∞ and γ that
max
|z|=n
|fn(z)| = O
(
eγ √n
)
(3.1)
max
|z/n −1|≤n−α
|fn(z) − f∞| e−γ |z−n|/ √n = o(1) ,(3.2)
as n → ∞. Then
lim
n→∞
fnn = f∞ .
Proof. By replacing fn(z) by fn(z) − f∞, we may assume that f∞ = 0.
By Cauchy and Stirling formulas, we have
fnn = (1 + o(1))
√ n
2π
∫
|ζ |=1
fn(nζ) en(ζ −1)
ζ n
dζ
iζ .
Choose some large C > 0 and split the circle |ζ| = 1 into 2 parts as
follows:
S1 =
{ C
n1/ 4 ≤ |ζ − 1|
}
, S 2 =
{ C
n1/ 4 ≥ |ζ − 1|
}
.
The inequality (3.1) and the equality
⏐
⏐en(ζ −1)⏐
⏐ = e−n|ζ −1|2/ 2 .

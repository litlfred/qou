---
doc_id: li-braid-closures
doc_title: "Knot polynomials on braid closures Eddy Li"
section_id: sec-005-the-homflypt-polynomial
section_title: "The HOMFLYPT polynomial"
section_number: null
pages: 6-9
source_pdf: Li-braid-closures.pdf
source_sha256: f7410e7be5bc187e
---
In [1, Section 6], Jones proposed a multivariable polynomial link invariantX L(q,Λ), which
reduces to the Jones polynomial under the specializationq= Λ =tand to the Alexander
polynomial under the specializationq= 1
Λ =t. We recall the key definitions organized
in [4].
Definition 2.16([6, Theorem 1.1]).Letλ⊢nbe a partition. TheOcneanu weightcorre-
sponding toλis the product
Ωλ =
Y
b∈λ
qr(b)w−q c(b)z
1−q h(b) ,
wherez=− 1−q
1−Λq andw= 1−q+z.
Definition 2.17.Lete:B n→Zdenote thebraid exponent, the additive homomorphism
wheree(σ i) = 1 for alli.
Definition 2.18([1, Definition 6.1]).For a braidα∈B n, theHOMFLYPT polynomial
under Jones normalizationis the product
Xˆα(q,Λ) :=

− 1−Λq√
Λ(1−q)
n−1
(
√
Λ)e(α)
X
λ⊢n
Ωλχλ(α).
This two-variable polynomialX ˆα(q,Λ) is a link invariant. The sum P
λ⊢n Ωλχλ(α) is some-
times referred to as theOcneanu trace.
6
Remark.The HOMFLYPT polynomial often admits the much more common normalization
PL(a,z), related to the Jones normalization byX L(q,Λ) =P L((Λq)−1/2,q 1/2−q−1/2).
Ocneanu originally calculated the eponymous weights, but this work has been lost. A
reproof of the validity of these weights was given by Geck [6].
Example 2.19([4, Example A.10]).Under the Jones specializationq= Λ =t, the weights
Ωλ simplify drastically, as shown in [4]. Specifically, Ωλ = 0 ifλhas more than two columns,
and the braid closure of anyα∈B n has Jones polynomial
Vˆα(t) = (−1)n−1(
√
t)e(α)−n+1
t+ 1
⌊n/2⌋X
k=0
 n−kX
i=k
ti
!
χ(n−k,k)⊤(α).
Whenn= 3, this simplifies to
Vˆα(t) = (
√
t)e(α)−2((t2 + 1)χ(1,1,1)(α) +tχ (2,1)(α)).
Example 2.20([1, Section 7]).Under the Alexander specializationq= 1
Λ =t, the sim-
plification of the weights is less clear as it seems likez=− 1−q
1−Λq will exhibit a singularity.
However, it turns out that such singularities are removable due to the factor of (1−Λq) n−1
in Definition 2.18.
Letµ i be the hook-type partition made up of one row ofisquares and one column of
n−isquares beneath. As computed in [1, Equation 7.2], we find that
∆α(t) = (−1)n(t−1)
(
√
t)e(α)−n+1(tn−1)
nX
i=1
(−1)iχµi(α).
Whenn= 3, this implies that
∆ˆα(t) = χ(1,1,1)(α)−χ (2,1)(α) +χ (3)(α)
(
√
t)e(α)−2(t2 +t+ 1) .
Remark.If we substitutet=ζ n =e 2πi/n into Example 2.20 above, the denominator vanishes,
implying that the numerator must vanish too. In particular, we must have
nX
i=1
(−1)iχµi(α) = 0
att=ζ n. If we apply the KZ functor to the exact sequence proven due to the BGG resolution
in [7], we expect an exact sequence ofζ n-Specht modules on hook-shape partitions.
7
3 Closures of3-braids
We investigate the Jones and Alexander polynomials of 3-braid closures at−1.
Recall from Examples 2.12 and 2.13 thatS (1,1,1)
q is the sign representation, where each
gi acts as−1, whileS (3)
q is the trivial representation, where eachg i acts asq. Whenq=−1,
the representations become isomorphic, soχ (1,1,1)(α) =χ (3)(α). Hence
Vˆα(−1) = (
√
−1)e(α)−2(2χ(1,1,1)(α)−χ (2,1)(α))
and
∆ˆα(−1) = (
√
−1)−e(α)+2(χ(1,1,1)(α)−χ (2,1)(α) +χ (3)(α))
= (
√
−1)−e(α)+2(2χ(1,1,1)(α)−χ (2,1)(α)).
Note the use of√−1 rather thanior−idue to the lack of a continuous, single-valued square
root overC. If we define √−1 to be{i,−i}, then clearlyV ˆα(−1) = ∆ˆα(−1) =X ˆα(−1,−1).
Otherwise, the usual convention wherei= √−1 yields thatV ˆα(−1) = (−1)e(α)∆ˆα(−1).
From now on, we will adopt the latter convention whereV ˆα(−1) = (−1)e(α)∆ˆα(−1).
Definition 3.1.Letϕ:B 3→SL 2(Z) be the homomorphism satisfyingϕ(σ i) =M i, where
(M1,M 2) =
 1 0
−1 1

,
1 1
0 1

.
Proposition 3.2.For a braidα∈B 3, the Jones and Alexander polynomials ofˆαsatisfy
Vˆα(−1) = (−i)e(α)(tr(ϕ(α))−2)and∆ ˆα(−1) =i e(α)(tr(ϕ(α))−2).
Proof.From Example 2.14 we note thatg i acts as−M i inS −1
(2,1), whileg i acts as−1 in
S−1
(1,1,1). Thus, as found above, we have
Vˆα(−1) =i e(α)−2(2χ(1,1,1)(α)−χ (2,1)(α))
=i e(α)(−1)(2(−1)e(α)−(−1)e(α) tr(ϕ(α)))
= (−i)e(α)(tr(ϕ(α))−2),
as claimed.
An interesting question to consider is which integer valuesV ˆα(−1) can possibly take,
and what type of link ˆαcorresponds to. Here, we shall consider two extremal cases: when
ˆαis split and when ˆαis a knot.
8

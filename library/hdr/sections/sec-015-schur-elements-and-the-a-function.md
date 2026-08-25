---
doc_id: hdr
doc_title: "Hecke algebras, generalisations and representation theory"
section_id: sec-015-schur-elements-and-the-a-function
section_title: "Schur elements and the a-function"
section_number: null
pages: 34-35
source_pdf: HDR.pdf
source_sha256: 35c190fd2d2a393c
doc_brief: "Hecke algebras, generalisations and representation theory — 27 sections: Algebras of Finite Type; Blocks; Symmetrising forms and Schur eleme"
---
Let τ :Hq
n→R be the linear map deﬁned by
τ(Xa1
1 Xa2
2 ...X an
n tw) =
{ 1 if a1 =a2 =··· =an = 0 and w = 1,
0 otherwise ,
where w∈ Sn and 0⩽ am⩽ l− 1 for all m = 1, 2,...,n . The function τ was introduced by Bremke
and Malle [BreMa] who showed that τ is a trace form and that τ is essentially independent of the choice
of basis ofHq
n. It is not obvious from the deﬁnition above that τ coincides with the form introduced by
Bremke and Malle; however, this was proved by Malle and Mathas in [MalMat], where they also showed
that τ is a canonical symmetrising form on Hq
n whenever all Qi’s are invertible in R. As we will see in
Chapter 6, τ is the Markov trace on Hq
n with all parameters equal to 0.
From now on, we assume that all q,Q 0,...,Q l−1 are invertible in R. Let K be a ﬁeld containing
R such that KHq
n is split semisimple. As mentioned in the beginning of this chapter, but also due to
Tits’s deformation theorem, the simple modules of KHq
n are parametrised by the l-partitions of n. For
λ∈P (l,n ), we denote by V λ the corresponding simple module and by sλ(q) the Schur element of V λ
with respect to τ. As we saw in §1.2, sλ(q) belongs to the integral closure RK of R in K.
For example, we can take q,Q 0,...,Q l−1 to be indeterminates, R = Z[q±1,Q±1
0 ,...,Q ±1
l−1] and K =
Q(q,Q 0,...,Q l−1). In this case, we call Hq
n the generic Ariki–Koike algebra, and we have sλ(q)∈
Z[q±1,Q±1
0 ,...,Q ±1
l−1] for all λ∈P (l,n ).
The Schur elements ofHq
n have been calculated independently by Geck, Iancu and Malle [GIM], and
by Mathas [Mat]. Their papers provide diﬀerent combinatorial formulas for the calculation of sλ(q),
which are described in both cases as quotients of elements of K. Even though it was theoretically known
that these quotients belonged toRK, there was no combinatorial formula to describe the terms remaining
after the division. In [ChJa2], we managed to obtain a cancellation-free formula for the Schur elements
ofHq
n:
31
Theorem 4.3 Let λ = (λ(0),λ (1),...,λ (l−1)) be an l-partition of n. Then
sλ(q) = (−1)n(l−1)q−N(¯λ)(q− 1)−n ∏
0⩽s⩽l−1
∏
(i,j)∈[λ(s)]
∏
0⩽t⩽l−1
(qhλ(s),λ(t)
i,j QsQ−1
t − 1).
Since the total number of nodes in λ is equal to n, the above formula can be rewritten as follows:
sλ(q) = (−1)n(l−1)q−N(¯λ) ∏
0⩽s⩽l−1
∏
(i,j)∈[λ(s)]

[hλ(s),λ(s)
i,j ]q
∏
0⩽t⩽l−1,t⁄=s
(qhλ(s),λ(t)
i,j QsQ−1
t − 1)

,
where [m]q := (qm− 1)/(q− 1) =qm−1 +qm−2 +··· +q + 1, for all m∈ Z>0.
Jean Michel and the author programmed the cancellation-free formula for the Schur elements of
Ariki–Koike algebras into the GAP3 package CHEVIE. This made the algorithm for the computation of
the Schur elements faster than the pre-existing one.
Now, applying Theorem 1.7 with the formulas for the Schur elements given in Theorem 4.3 yields easily
Ariki’s semisimplicity criterion (4.2). Further, if we take q =ur and Qi =ζi
luri for all i = 0,...,l − 1,
where u is an indeterminate, r∈ Z>0 and r0,...,r l−1∈ Z, then the algebra Hq
n is a cyclotomic Ariki–
Koike algebra (since it can be obtained via the cyclotomic specialisation ϕ : q↦→ ur, Qi↦→ ζi
luri from
the generic Ariki–Koike algebra). Set mi :=ri/r for all i = 0,...,l − 1 and m := (m0,...,m l−1)∈ Ql.
Let λ∈P (d,n ). Then the a-value of the irreducible representation Eλ of G(l, 1,n ) corresponding to λ
(that is, the negative of the valuation of sλ(q)) is equal to a(m,r) [GeJa2, Proposition 5.5.11]. Theorem
4.3 allows us to give an alternative description of the a-value of Eλ [ChJa2, Proposition 4.5]:
Proposition 4.4 LetHm,r
n be the cyclotomic Ariki–Koike algebra deﬁned above, and let λ∈P (d,n ).
The a-value of Eλ is
a(m,r)(λ) =r

N(λ)−
∑
0⩽s⩽l−1
∑
(i,j)∈[λ(s)]
∑
0⩽t⩽l−1,t⁄=s
min(hλ(s),λ(t)
i,j +ms−mt, 0)

.

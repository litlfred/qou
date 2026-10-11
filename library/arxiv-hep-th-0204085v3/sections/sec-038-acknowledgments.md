---
doc_id: arxiv-hep-th-0204085v3
doc_title: "arXiv:hep-th/0204085v3 12 Nov 2002"
section_id: sec-038-acknowledgments
section_title: "Acknowledgments"
section_number: null
pages: 18-24
source_pdf: 0204085v3.pdf
source_sha256: e0df7d49c43273c4
toc_source: inferred
---
It is a pleasure to thank V. A. Fateev, I. Kostov, G. Mennessier, V. Schomerus, Ch. Schweigert,
Al. B. Zamolodchikov and J.-B. Zuber for discussions and interest in this work.
The author would like to thank V. B. Petkova for clarifying correspondence and for point-
ing out useful references after the ﬁrst version of this paper had appeared.
Work supported by EU under contract HPRN-CT-2000-00122.
18
Appendix A. Some residues of the Liouville fusion ma-
trix
It is well known that in the case where one of α1, . . . , α4, say αi equals −n
2b −m
2 b−1
where n, m ∈N and where a triple (∆α4, ∆α3, ∆α21), (∆α21, ∆α2, ∆α1) which contains ∆αi
satisﬁes the fusion rules of [28], one will ﬁnd that the fusion coeﬃcients that multiply the
conformal blocks are residues of the general fusion coeﬃcient.
In the case where α2 = −1
2b, the fusion rules are:
 α21 = α1 −s b
2
α32 = α3 −s′ b
2
where s, s′ = ±.
There are four entries for the fusion matrix in this special case
F L
α1−sb/2,α3−s′b/2

α3
−b/2
α4
α1

≡F L
s,s′
which expressions are well known to be:
F++
=
Γ(b(2α1 −b))Γ(b(b −2α3) + 1)
Γ(b(α1 −α3 −α4 + b/2) + 1)Γ(b(α1 −α3 + α4 −b/2))
F+−
=
Γ(b(2α1 −b))Γ(b(2α3 −b) −1)
Γ(b(α1 + α3 + α4 −3b/2) −1)Γ(b(α1 + α3 −α4 −b/2))
F−+
=
Γ(2 −b(2α1 −b))Γ(b(b −2α3) + 1)
Γ(2 −b(α1 + α3 + α4 −3b/2))Γ(1 −b(α1 + α3 −α4 −b/2))
F−−
=
Γ(2 −b(2α1 −b))Γ(b(2α3 −b) −1)
Γ(b(−α1 + α3 + α4 −b/2))Γ(b(−α1 + α3 −α4 + b/2) + 1)
(48)
The dual case where α2 = −b−1/2 is obtained by substituting b by b−1.
Appendix B. Special cases of the H+
3 fusion matrix
Degenerate representations and fusion rules are well known for ˆsl(2) [21]. We will study
three easy cases.
1. j2 = 1/2
This case was ﬁrst derived in [14].
The fusion rules are j21 = j1 + 1/2
(+),
j21 = j1 −1/2
(−). We are in the case
where the second term of the sum (24) always vanishes. It is straightforward to use
19
the results of Appendix A to get
F
H+
3
++
=
Γ(b2(−2j1 −1))Γ(b2(1 + 2j3) + 1)
Γ(b2(−j1 + j3 + j4 + 1/2) + 1)Γ(b2(−j1 + j3 −j4 −1/2))
F
H+
3
+−
=
Γ(b2(−2j1 −1))Γ(b2(−2j3 −1))
Γ(−b2(j1 + j3 + j4 + 3/2))Γ(b2(−j1 −j3 + j4 −1/2)
F
H+
3
−+
=
Γ(1 + b2(1 + 2j1))Γ(1 + b2(1 + 2j3))
Γ(1 + b2(j1 + j3 + j4 + 3/2)))Γ(1 + b2(j1 + j3 −j4 + 1/2))
F
H+
3
−−
=
−
Γ(1 + b2(1 + 2j1))Γ(−b2(2j3 + 1))
Γ(b2(j1 −j3 −j4 −1/2))Γ(b2(j1 −j3 + j4 + 1/2) + 1)
2. j2 = 1/2b2
This case can be found in [18], but as we use the same normalisation as [11], we
shall compare directly with this last paper.
The fusion rules are
j21 = j1 + 1
2b2
(+),
j21 = j1 −1
2b2
(−),
j21 = −j1 −k/2
(x).
We ﬁnd it more convenient to work directly with the representation (24).
The
second LFT fusion matrix of the sum is equal to 1 in the cases:
j21 = j1 −1
2b2,
or
j21 = −j1 −1 −1
2b2
j32 = j3 −1
2b2,
or
j32 = −j3 −1 −1
2b2,
and equal to zero otherwise. It is then straightforward to compute
F
H+
3
++
=
Γ(−2j1 −b−2)Γ(2j3 + b−2 + 1)
Γ(−j1 + j3 + j4 + b−2/2 + 1)Γ(−j1 + j3 −j4 −b−2/2)
F
H+
3
+−
=
Γ(−2j1 −b−2)Γ(−2j3 −1)
Γ(−j1 −j3 −j4 −1 −b−2/2)Γ(−j1 −j3 + j4 −b−2/2)
F
H+
3
+x
=
Γ(−2j1 −b−2)Γ(2j3 + 1)Γ(−2j3 −1 −b−2)
Γ(−b−2)Γ(−j1 + j3 −j4 −b−2/2)Γ(−j1 −j3 + j4 −b−2/2)
F
H+
3
−+
=
Γ(2j1 + 2)Γ(2j3 + b−2 + 1)
Γ(j1 + j3 + j4 + b−2/2 + 2)Γ(j1 + j3 −j4 + 1 + b−2/2)
F
H+
3
x+
=
Γ(−2j1)Γ(2j1 + 2 + b−2)Γ(2j3 + b−2 + 1)
Γ(1 + b−2)Γ(−j1 + j3 + j4 + b−2/2 + 1)Γ(j1 + j3 −j4 + 1 + b−2/2)
(49)
20
For other cases the second LFT fusion matrix contributes; we ﬁnd:
F
H+
3
−−
=
e−iπǫb−2Γ(2j1 + 2)Γ(−2j3 −1)
Γ(j1 −j3 −j4 −b−2/2)Γ(j1 −j3 + j4 + 1 + b−2/2)
F
H+
3
−x
= −
e−iπǫ(2j3+b−2)Γ(2j1 + 2)Γ(2j3 + 1)Γ(−2j3 −1 −b−2)
Γ(−b−2)Γ(j1 + j3 + j4 + 2 + b−2/2)Γ(j1 −j3 −j4 −b−2/2)
F
H+
3
x−
= −
e−iπǫ(2j1+b−2)Γ(−2j1)Γ(2j1 + 2 + b−2)Γ(−2j3 −1)
Γ(1 + b−2)Γ(−j1 −j3 −j4 −1 −b−2/2)Γ(j1 −j3 + j4 + 1 + b−2/2)
F H+
3
xx
=
Γ(−2j1)Γ(2j3 + 1)Γ(2j1 + 2 + b−2)Γ(−2j3 −1 −b−2)
×
sin π(−b−2) sin π(j1 −j3 −j4 −b−2/2) sin π(−j1 + j3 −j4 −b−2/2)
π2 sin π(j1 + j3 + j4 + 2 + 3b−2/2)
−
e−iπǫ(j1+j3+j4+2+3b−2/2)Γ(−2j1)Γ(2j3 + 1) sin π(j1 + j3 + j4 + 2 + b−2/2)
Γ(−2j1 −1 −b−2)Γ(2j3 + 2 + b−2) sin π(j1 + j3 + j4 + 2 + 3b−2/2)
These coeﬃcients are in agreement with [11] for the choice ǫ = 1 , excepted for F
H+
3
xx ,
where there seems to be a slight discrepancy in some of the arguments of the gamma
functions. (We did not redo the computations of [11], where the fusion matrix was
obtained thanks to an explicit integral representation for the conformal blocks).
3. j2 = −k/2
This elementary case was explicitly mentionned in [14]. The fusion rule is j21 =
−j1 −k/2. The ﬁrst term of the sum vanishes and the second LFT fusion matrix is
equal to one. It remains to evaluate the product of gamma functions; we ﬁnd:
F H+
3 = e−iπǫ(j1+j3+j4+1+ 1
b2 )
Appendix C. Fusion rules for ˆsl(2) algebra at generic
level
We present here a way to ﬁnd degenerate representations and fusion rules for ˆsl(2) from
the knowledge of the degenerate representations and fusion rules of the Virasoro algebra.
We derived in the main text the following asymptotic behavior when x →z for the
conformal blocks of the SL(2, C)/SU(2) WZNW, relating them to two Liouville conformal
21
blocks:
Gs
j21(j1, j2, j3, j4|x, z)
∼x→z
"
Γ(2 + b−2 + 2j21)Γ(2 + b−2 + j1 + j2 + j3 + j4)
Γ(2 + b−2 + j21 + j1 + j2)Γ(2 + b−2 + j21 + j3 + j4)F s
−bj21(−bj1, −bj2, −bj3, −bj4|z) +
+Γ(2 + b−2 + 2j21)Γ(−2 −b−2 −j1 −j2 −j3 −j4)
Γ(j21 −j1 −j2)Γ(j21 −j3 −j4)
F s
−bj21(−bJ1, −bJ2, −bJ3, −bJ4|z) ×
×
(x −z)j1+j2+j3+j4+2+b−2z−j3−j4−1−
1
2b2 (1 −z)j3+j2+1+
1
2b2
#
with Ji = ji −
1
2b2.
Although there is no closed form known for the Liouville conformal blocks, they are
completly determined by the conformal symmetry. They depend on conformal weights
only, i.e. are invariant when −bji (resp. −bJi) is changed into Q + bji (resp. Q + bJi).
1. Degenerate representations of the Virasoro algebra.
It is well known that the case where ji (resp. Ji) equals n
2 + m
2 b−2 with n, m non
negative integers, corresponds to a degenerate Virasoro representation V−bji (resp.
V−bJi). The conformal block F s
−bj21 then only exists for a ﬁnite number of values of
−bj21 [28]:
−bj21 = −bj1 + bj2 −ub −vb−1.
where u, v are integers such that 0 ≤u ≤n,
0 ≤v ≤m.
It would be equivalent to write Q + bj21 instead of −bj21 in equation (50) since the
Virasoro representations V−bj and VQ+bj are equivalent. We will see that this fact
will play an important role in the determination of the degenerate representations
and fusion rules for ˆsl(2).
2. Degenerate representations and fusion rules for ˆsl(2).
Let us call for short F 1 the ﬁrst Liouville conformal block of the sum (50) and the
second one F 2.
Claim 1 The spin jm,n that labels the degenerate representation of ˆsl(2) Pjn,m are
also labels for the degenerate Virasoro representation V−bjn,m or V−bJn,m.
In other words, it means that Pjn,m is a degenerate representation of ˆsl(2) iﬀ:
(a)
jn,m
=
n
2 + m
2 b−2
or
(b)
jn,m
=
−
n
2 + 1

−
m
2 + 1
2

b−2.
(50)
with n, m non negative integers.
We now provide two rules that will allow us to determine the ˆsl(2) fusion rules:
22
Rule 1 If j2 is such that both V−bj2 and V−bJ2 correspond to degenerate Virasoro
representations, then the admissible ˆsl(2) fusion rules consist of the set of common
fusions rules plus j21 = j1 + j2 if j2 is of the form (a), and j21 = −j1 −j2 −2 −b−2
if j2 is of the form (b).
Rule 2 If j2 is such that V−bj2 is a degenerate Virasoro representation and not V−bJ2
(or converse), then the ˆsl(2) fusion rules are such that the factor Γ−1(j21 −j1 −j2)
in front of F 2 should be equal to zero (resp. Γ−1(2 + b−2 + j21 + j1 + j2) in front of
F 1). Note that this case happens only if m=0.
We shall start by three easy examples as the generalization is straightforward.
(a) Examples:
i. j2 = 1
2
In this case we have −bj2 = −b
2 so the Virasoro representation V−b
2 is
degenerate. The fusion rules are:
−bj21
=
−bj1 −b
2,
−bj21 = −bj1 + b
2,
or
Q + bj21
=
−bj1 −b
2,
Q + bj21 = −bj1 + b
2.
(51)
(52)
Let us turn to F 2: −bJ2 = −b
2 + 1
2b does not correspond to any degenerate
Virasoro representation. We use rule 2 to select the admissible set of fusion
rules, and ﬁnd
j21 = j1 + j2,
j21 = j1 −j2.
(53)
ii. j2 =
1
2b2
In this case we have −bj2 = −1
2b so the Virasoro representation V−1
2b is
degenerate. The allowed values for j21 are:
−bj21
=
−bj1 −1
2b,
−bj21 = −bj1 + 1
2b,
or
Q + bj21
=
−bj1 −1
2b,
Q + bj21 = −bj1 + 1
2b.
(54)
As for the second term, we have −bJ2 = 0, which corresponds to the
identity representation. The fusion rules are −bj21 = −bj1+ 1
2b or Q+bj21 =
−bj1 + 1
2b. The common set of fusion rules consists of
−bj21 = −bj1 + 1
2b,
−bj21 = bj1 −1
2b + Q.
(55)
23
According to the rule 1, we should also include −bj21 = −bj1 −1
2b.
As a conclusion, we are left with the following three possibilities:
−bj21 = −bj1 −1
2b,
−bj21 = −bj1 + 1
2b,
−bj21 = bj1 −1
2b + Q. (56)
iii. j2 = −k
2
In this case −bj2 = b + 1
2b does not correspond to any degenerate Virasoro
representation, and −bJ2 = Q.
As VQ and V0 are equivalent Virasoro
representations, we see that −bJ2 = Q actually corresponds to the identity
representation. Hence the fusion rules are −bj21 = −bj1 + 1
2b or −bj21 =
bj1 + b + 1
2b. The latter rule is the only acceptable one, as it makes the
term Γ−1(2 + b−2 + j21 + j1 + j2) in front of F 1 vanish.
Let us note that the ˆsl(2) representation P−k
2 plays a role very similar to
the identity, as the decomposition of its tensor product with an arbitrary
representation Pj gives the representation P−j−k
2 only.
(b) General case:
i. j2 = n
2 + m
2 b−2, with n ∈N, m ∈N.
The allowed values for j21 are either
j21
=
j1 −j2 + u + vb−2
or
j21
=
j2 −j1 −(u′ + 1) −(v′ + 1)b−2,
(57)
where 0 ≤u ≤n,
0 ≤v ≤m,
0 ≤u′ ≤n,
0 ≤v′ ≤m −1.
ii. j2 = −
  n
2 + 1

−
  m
2 + 1
2

b−2, with n ∈N, m ∈N.
The allowed values for j21 are either
j21
=
j1 −j2 −(U + 1) −(V + 1)b−2
or
j21
=
j2 −j1 + U′ + V ′b−2,
(58)
where 0 ≤U ≤n,
0 ≤V ≤m −1,
0 ≤U′ ≤n,
0 ≤V ′ ≤m.
These results are in agreement with [21].

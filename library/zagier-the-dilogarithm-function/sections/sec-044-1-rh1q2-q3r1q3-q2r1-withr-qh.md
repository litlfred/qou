---
doc_id: zagier-the-dilogarithm-function
doc_title: "The Dilogarithm Function Don Zagier"
section_id: sec-044-1-rh1q2-q3r1q3-q2r1-withr-qh
section_title: "Rh,1−Q2 =Q3R,1−Q3 =Q2R−1 withR =(Qh"
section_number: 1
pages: 46-48
source_pdf: zagier-the-dilogarithm-function.pdf
source_sha256: 05079cf525c6ba0f
doc_brief: "The Dilogarithm Function Don Zagier — 56 sections: Don Zagier; The dilogarithm function in geomet; The Bloch-Wigner function D(z) and"
---
1Q2/Q3)α.
The last two give (1−Q2)(1−Q3)= Q2Q3 or Q2 +Q3 = 1, which implies
ﬁrst of all that [Q2]+[ Q3] is torsion in the Bloch group and secondly that
R = 1 and hence (sinceh is integral!) that 1−Q1 =QA1
1 , which because of the
choice ofA1 implies that [Q1] is also torsion. For the modularity, we note that
fA,B,C for (A,B,C ) as in (31) and (32) is equal to ∑qQ(l,m,n)/(q)l(q)m(q)n
where the sum is over alll, m, n≥ 0a n dQ(l,m,n ) is the quadratic form
Q(l,m,n )= α
2
(
hl +m−n−ν)2 + mn + A1
2 l2 + B1l +C1 − 1
24.
The identity (27) then gives
The Dilogarithm Function 49
Table 3. Rank 3 examples for Nahm’s conjecture. In the ﬁrst lineα and ν are rational and h is integral. In the third lineν is rational.
A


αh2 +1 αh −αh
αh α 1 −α
−αh 1 −αα

,c = 3
2


αh
2 +2 αh −αh
αh α 1 −α
−αh 1 −αα

,c = 7
5


αh
2 +1/2 αh −αh
αh α 1 −α
−αh 1 −αα

,c = 8
5


21 −1
110
−10 1

,c = 3
2
B


ανh
αν
−αν




ανh +1/2
αν
−αν




ανh − 1/2
αν
−αν




ανh
αν
−αν




ανh +1
αν
−αν




ανh
αν
−αν




ανh +1/2
αν
−αν




0
−
1
2
−1
2




0
0
1
2




0
1
2
0




1
1
2
0




1
1
−1
2


C αν2/2 − 1/16 αν2/2 αν2/2 αν2/2 − 7/120 αν2/2+1 7/20 αν2/2 − 1/15 αν2/2 − 1/60 1/8 1/48 −1/24 1/8 3/16
A


211
110
101

,c = 8
7


321
221
111

,c = 9
10
B


0
0
1/2




0
1/2
0




1
0
1/2




1
1/2
0




1
1/2
1




1
1
1/2




−1/2
0
−1/2




0
0
0




1/2
0
1/2




1/2
1
1/2




1
1
0




3/2
1
1/2


C
−1/84 −1/84 5/ 84 5/ 84 17/ 84 17/ 84 1/40 −3/80 1/40 9/40 13/80 9/40
A


211
120
102

,c =1


421
220
101

,c =1


642
442
222

,c = 2
3
B


0
2ν
−2ν




1/2
0
1




1/2
1
0




1
0
1




1
1
0




−1/2
0
0




−1
−1/2
−1/2




−1
−1
1/2




0
−1/2
1/2




0
0
0




0
0
1/2




2
1
1/2




2
1
1




0
0
0




1
0
0




2
1
0


C
ν2 − 1/24 7/48 7/48 5/24 5/24 −1/48 1/48 1/12 1/48 −1/24 0 1/3 11/24 −1/30 1/12 11/36
A


422
221
212

,c = 4
5


42 −1
22 −1
−1 −11

,c = 3
2


841
430
101

,c = 9
10
B


0
−1/2
0




0
0
−1/2




0
0
0




1
0
1/2




1
0
1




1
1/2
0




1
1
0




2
1
1




0
0
0




0
0
1/2




1
0
0




2
1
−1/2




2
1
0




0
−1/2
1/2




2
1/2
1/2


C
00 −1/30 11/120 1/6 11/120 1/6 11/30 −1/16 1/24 5/48 3/8 7/16 1/40 9/40
50 Don Zagier
fA,B,C (z)= 1
η(z)
∑
l≥0
(∑
r∈Z
qα(r+hl−ν)2/2
)
qA1l2/2+B1l+C1 ,
and (since h is integral!) we can now shift r by−hl in the inner sum to see
thatfA,B,C is the product offA1,B1,C1 and the function (26). We also remark
that one of the eight sporadic values ofA also has an inﬁnite family of (B,C )
making fA,B,C modular (checked only numerically):
f(211
120
102
)
,
( 0
2ν
−2ν
)
,ν 2− 1
24
(z)= 1
η(z)
∑
n∈Z+ν
qn2
(∀ν∈ Q). (33)
(f) Duality. Finally, we remark that the conditions on A in the conjecture
are invariant underA↦→A−1. For (i) this is clear, since if Q is a solution of
(25) for some A then the vector Q⋆ =( 1−Q1,..., 1−Qr) is a solution for
A⋆ =A−1 andξQ⋆ equals−ξQ modulo torsion in B(Q). On the modular side,
the analysis in C (speciﬁcally, eq. (38) below) suggests, though it does not
prove, that if fA,B,C is modular then fA⋆,B⋆,C⋆ is also modular and has an
asymptotic expression as in (28) with (c,K ) replaced by (c⋆,K ⋆), where
(A⋆,B ⋆,C ⋆,c⋆,K ⋆)=
(
A−1,A −1B, 1
2BtA−1B− r
24 −C, r−c, K
√
detA
)
.
These formulas, which one can verify in the examples in Table 2, were given
by Nahm in [28], p. 663–4 and [29], p. 164. On the conformal ﬁeld theory side,
the involutionA↔A−1 is related to a duality found by Goddard-Kent-Olive
[19] and to the so-called level-rank duality.

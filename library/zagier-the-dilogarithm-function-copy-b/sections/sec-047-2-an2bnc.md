---
doc_id: zagier-the-dilogarithm-function-copy-b
doc_title: "The Dilogarithm Function Don Zagier"
section_id: sec-047-2-an2bnc
section_title: "An2+Bn+C"
section_number: 2
pages: 48-50
source_pdf: zagier-the-dilogarithm-function-copy-b.pdf
source_sha256: c584944a501ef0c5
doc_brief: "The Dilogarithm Function Don Zagier — 56 sections: Don Zagier; The dilogarithm function in geomet; The Bloch-Wigner function D(z) and"
duplicate_of: "zagier-the-dilogarithm-function"
---
(q)n
(A, B, C ∈ R,A > 0). (34)
Since FA,B,C (q)= qCFA,B,0(q), it is enough to study the case C =0 ,i nw h i c h
case we omit the index C from the notation.
Proposition 5. For any A, B ∈ R, A> 0, we have the asymptotic expansion
log FA,B
(
e−ε)
∼
∞∑
j=−1
cj(A, B) εj (
ε ց 0
)
, (35)
The Dilogarithm Function 51
with coeﬃcients cj(A, B) ∈ R. The ﬁrst two coeﬃcients are given by
c−1(A, B)= L(1) − L(Q) ,c 0(A, B)= B log Q − 1
2 log ∆, (36)
where Q is the unique positive solution of Q + QA =1 , L(x) is the Rogers
dilogarithm, and ∆ = A + Q − AQ,w h i l ecj(A, B) for j ≥ 1 is a polynomial
of degree j +1 in B with coeﬃcients in Q[Q, A, ∆ −1],e . g .
c1(A, B)= 1 − Q
2∆ B2 − Q(1 − Q)(1 − A)
2∆2 B
− (1 − Q)((1 − Q2)A3 − 3QA2 +3 Q(1 + Q)A − 2Q2)
24∆3 .
Before proving the proposition, we say a little bit more about the coe f-
ﬁcients cj. The polynomial cj = cj(A, B) belongs to ∆−3jQ[A, Q, B∆]. Its
leading term is αjBj+1/(j + 1) where ∑ αjxj is the Taylor expansion of
log Q(x), Q(x)+ e−xQ(x)A = 1, e.g.
c2 = − Q(1 − Q)
6∆3 B3 + ··· ,c 3 = Q(1 − Q)(3Q − (1 + Q)∆)
24∆5 B4 + ··· .
We omit the other coeﬃcients, giving only the constant term of c2:
c2(A, 0) = Q(1 − Q)(A − 1)
48 ∆6
[
−4A(A + 1)(A − 1)2Q3
+3 A(A − 1)(A − 2)(2A +1 )Q2 +2 A2(5A − 4)Q − A3(2A − 1)
]
.
We will describe three diﬀerent approaches for obtaining the asympt otics
of log FA,B(e−ε)a s ε → 0. The ﬁrst, based on a functional equation for
FA,B, is short and elementary, but gives the coeﬃcients cj(A, B) only up
to a term depending on A. The second is also elementary—essentially based
on the Euler-Maclaurin summation formula—and gives the entire asymptoti c
expansion, but requires more work. The third, which is the one used by Nahm
and his collaborators, is based on Cauchy’s theorem together with formula ( 8)
for the quantum dilogarithm, and also leads to a full expansion; this met hod
also has a variant, using (7) rather than (8) for the quantum dilogarithm,
which has apparently not been noticed before. It seemed worth presen ting all
three approaches, at least brieﬂy, since the information they give is s omewhat
diﬀerent and since each of them is applicable (at least in principle) to the
general case of Nahm’s conjecture and to many other problems of this type.
(a) For the ﬁrst approach we set
FA,B
(
e−ε)
FA,0
(
e−ε) = QB HA,B(ε)
52 Don Zagier
where HA,B(ε)=
∞∑
n=0
hn(A, B) εn is a power series in ε satisfying HA,B(0) ≡ 1,
HA,0(ε) ≡ 1. Knowing HA,B(ε) is tantamount to knowing cj(A, B) − cj(A, 0)
for all j ≥ 1. The functional equation
FA,B(q) − FA,B+1(q)=
∞∑
n=1
q
1

---
doc_id: arxiv-1411.6062v2
doc_title: "EV ALUATION OF STATE INTEGRALS AT RATIONAL POINTS"
section_id: sec-003-13-evaluation-of-state-integrals
section_title: "Evaluation of state-integrals"
section_number: 1.3
pages: 4-6
source_pdf: 1411.6062v2.pdf
source_sha256: 5abd328d027de43c
doc_brief: "EVALUATION OF STATE INTEGRALS AT RATIONAL POINTS — Multi-dimensional state-integrals of products of Faddeev’s quant um diloga- rithms arise frequently in Quantum Topology, quantum Teichm¨ uller t"
---
M/N in terms of the state-sums GM,N , the Rogers dilogarithm and the cyclic dilogarithm.
Fix an admissible pair ( M, N ), and deﬁne
(11) b =
√
M/N , s =
√
M N .
Let
(12) S ={w| g(e2πsw) = 1 , 0 < s Im(w)− λ < 1},
where λ is a generic real number such that
(13) − (M + N)/ 2 < λ < 0
and
(14) g( z) = (−z)A(1− z)−B∈
/C9 [z±1] .
Note that if w∈S , then e2πsw is an algebraic number with a ﬁxed choice of N and M-th
roots.
Theorem 1.1. When b2 = M/N we have:
IA,B(b) = eπi B+3A(M +N+1)2−6M N
12M N s−1
∑
w∈S
e
iB
2π s2 R(z)(1− z)
(2N+1)(2M +1)
4M N B
z g′(z) /DN (θ+, q +)B /DM (θ−, q −)B GM,N (θ+, θ −) ,(15)
where
(16) z = e2πsw, θ + = e2πbw = z1/N, θ − = e2πb−1w = z1/M, q + = ζM
N , q − = ζN
M .
Note that when g( z) = 1, we have
(17) g ′(z) = Az−1 + B(1− z)−1 .
Corollary 1.2. For M = 1 we obtain that
(18) IA,B(b) = eπi B+3A(N+2)2−6N
12N
1√
N
∑
w∈S
e
iB
2πN R(z) (1− z)
2N+3
4N B
(A + Bz/ (1− z)) /DN (θ+, q +)B G+
N (θ+) .
When M = N = 1 we obtain that
(19) IA,B(1) = eπi B+3A−6
12
∑
w∈S
e
iB
2π R(z) (1− z)
B
4
(A + Bz/ (1− z)) .
EV ALUATION OF STATE INTEGRALS AT RATIONAL POINTS 5
Let us denote
(20) e(x) = e2πix .
Corollary 1.3. When M = N = 1 and ( A, B ) = (1 , 2), we choose λ to be a negative real
number near zero,
g(z) =−z(1− z)−2
S ={i/ 6, 5i/ 6}
z± = e(±1/ 6)
eπi B+3A−6
12 = e
(
− 1
24
)
(e
iB
2π R(z+), e
iB
2π R(z−)) =
(
e−Ce
(
− 1
24
)
,−eCe
(
− 1
24
)
e
(1
3
))
(1− z±)
B
4
(A + Bz±/ (1− z±)) = 1√
3 e
(
∓1
3
)
where C = V / (2π) and V is the volume of the 4 1 knot. When computing the Rogers
dilogarithm of z±, keep in mind that we use the branches of the logarithm log z+ = 2 πi/ 6
and log z− = 10πi/ 6 dictated by Equations ( 12) and ( 13).
The above computation, combined with Equation ( 19) implies Equation ( 2). As was
already mentioned, the proof of this equation was a main motivation f or the results of our
paper.
We now make few remarks about the number-theoretic, analytic an d geometric properties
of Equation ( 15).
Remark 1.4. It [ GZa] (see also [ Dim14b]) it was observed that although ( G+(θ+))N and
( /DN (θ+, ζ N ))N lie in the ﬁeld FG,N = /C9 (θ+, ζ N ), their ratio lies in the smaller ﬁeld /C9 (z, ζ N )
(where z satisﬁes g( z) = 1) which is an extension of /C9 (z) by ζN . In particular, the above
mentioned ratio is independent of the choice of the N-th root of z.
Remark 1.5. Although /DN is a multivalued function, the sum in Equation ( 15) is well-
deﬁned. This is a consequence of Theorem 1.9 below and the fact that the quantum diloga-
rithm is a meromorphic function.
Remark 1.6. When the state-integral is associated with a cusped hyperbolic man ifold M,
the setS is often in bijection with the set of nonabelian parabolic PSL(2 ,
/BV ) representations
of M. Under such a bijection, the Rogers dilogarithm matches with the co mplex volume,
and the value of g′(z) matches with the value of the 1-loop invariant of [ DG13], suitably
normalized. For an illustration, see Section 2.3.
Remark 1.7. When the state-integral is associated with a cusped hyperbolic man ifold M
and the identiﬁcation of Remark 1.6 is available, one can identify Equation ( 15) with a sum
of invariants of M parametrized by nonabelian parabolic PSL(2 , /BV ) representations of M.
Such invariants appear in Quantum Hyperbolic Geometry–see [ Kas97] and also [ BB07]. The
invariants of Quantum Hyperbolic Geometry are deﬁned up to multiplic ation by an N-root
6 STA VROS GAROUF ALIDIS AND RINAT KASHAEV
of unity. However, Equation (
15) gives a well-deﬁned relative choice of the N-th roots of
unity. This is a consequence of the meromorphicity of the quantum d ilogarithm.
Remark 1.8. As we already mentioned above, a numerical computation by the ﬁrs t author
and Zagier suggests an explicit formula for the Taylor series of I1,2(b) at b = 1 in terms of
the asymptotics of the Kashaev invariant at q = 1. We expect that the Taylor series of state-
integrals at b =
√
M/N can be expressed in terms of the loop invariants of Garoufalidis–
Dimofte [ Dim14b]. We plan to study this in a later publication.
Theorem 1.1 follows from a lemma from complex analysis regarding integrals of quas i-
periodic functions 2.3. This lemma is used twice, once to evaluate the quantum dilogarithm
in terms of the cyclic dilogarithm, and another time to evaluate the st ate-integralIA,B(b).

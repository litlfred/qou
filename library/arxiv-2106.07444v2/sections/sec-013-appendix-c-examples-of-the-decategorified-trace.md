---
doc_id: arxiv-2106.07444v2
doc_title: "FROM THE HECKE CATEGORY TO THE UNIPOTENT LOCUS"
section_id: sec-013-appendix-c-examples-of-the-decategorified-trace
section_title: "Appendix C. Examples of the Decategorified Trace"
section_number: null
pages: 82-84
source_pdf: 2106.07444v2.pdf
source_sha256: 5acca39c07bcdddd
toc_source: outline
doc_brief: "FROM THE HECKE CATEGORY TO THE UNIPOTENT LOCUS — Let W be the Weyl group of a split semisimple group G. Its Hecke category HW can be built from pure perverse sheaves on the double ﬂag variety of G."
---
In this appendix, we list some values of ⟨−⟩q and ⟨−⟩0
q. Throughout, we rely on
Table 8.1 in [GP] and the descriptions of {−, −} in [L84-1, Ch. 4].
Type A1. Here, W = S2 and ˆ
W = {1, ε}. Writing σ for the positive generator of
BrW = Br2, we have:
⟨σm⟩q = (q
1
2 )m + (−q−1
2 )mε,
⟨σm⟩0
q =
1
1 −q2 ((1 −(−q)m+1) + (q + (−q)m)ε).
For instance, we have ⟨σ2k+1⟩0
q = (1 + q2 + · · · + q2k) + (q + q3 + · · · + q2k−1)ε for
all k ≥1.
Type A2. Here, W = S3. We write S = {s, t} and ˆW = {1, φ, ε}, where φ(1) = 2.
The following table lists (ψ, ⟨σw⟩q)W for all w ∈W and ψ ∈ˆW:
1
σs, σt
σst, σts
σsts
1
1
q
1
2
q
q
3
2
φ
2
q
1
2 −q−1
2
−1
0
ε
1
−q−1
2
q−1
−q−3
2
We deduce that:
⟨σw⟩0
q =











(1 −q)−2(1 + 2φ + ε)
w = 1
(1 −q)−1(1 + φ)
w ∈{s, t}
1
w ∈{st, ts}
(1 −q)−1(1 −q + q2 + qφ)
w = w0
Type BC2. Here, W is the dihedral group of the square. We write S = {s, t} and
ˆW = {1, δ, φ, εδ, ǫ}, where δ(1) = 2 and φ(1) = 2 and δ(s) = 1. The following table
lists (ψ, ⟨σw⟩q)W for all w and ψ:
1
σs
σt
σst, σts
σsts
σtst
σw0
1
1
q
1
2
q
1
2
q
q
3
2
q
3
2
q2
δ
1
q
1
2
−q−1
2
0
−q−1
2
q
1
2
−1
φ
2
q
1
2 −q−1
2
q
1
2 −q−1
2
−1
0
0
0
εδ
1
−q−1
2
q
1
2
0
q
1
2
−q−1
2
−1
ε
1
−q−1
2
−q−1
2
q−1
−q−3
2
−q−3
2
q−2
We deduce that:
⟨σw⟩0
q =

























(1 −q)−2(1 + δ + 2φ + εδ + ε)
w = 1
(1 −q)−1(1 + δ + φ)
w = s
(1 −q)−1(1 + εδ + φ)
w = t
1
w ∈{st, ts}
(1 −q)−1(1 −q + q2 + qεδ + qφ)
w = sts
(1 −q)−1(1 −q + q2 + qδ + qφ)
w = tst
1 + q2 + qφ
w = w0
Note that this is the smallest W for which {−, −} is nontrivial.
FROM THE HECKE CATEGORY TO THE UNIPOTENT LOCUS
83
An Iterated Torus Braid. Let W = S4.
We write S = {s, t, u} and ˆ
W =
{1, φ, ψ, εφ, ε}, where φ(1) = 3 and ψ(1) = 2 and φ(s) = 1. Let
β = (σsσtσu)6σs ∈BrW = Br4.
Using SageMath, we calculated:
⟨β⟩q = q
19
2 −q
7
2 φ + (q
1
2 −q−1
2 )ψ + q−7
2 εφ −q−19
2 ε.
The nonzero coeﬃcients of ⟨β⟩0
q are listed below:
q0
q1
q2
q3
q4
q5
q6
q7
q8
q9
q10 q11 q12 q13 q14 q15 q16
1
1
1
1
2
1
3
1
3
1
3
1
2
1
1
1
φ
1
1
2
2
4
3
5
3
5
3
4
2
2
1
1
ψ
1
2
1
3
1
4
1
3
1
2
1
εφ
1
1
2
2
3
2
3
2
2
1
1
ε
1
1
1
(34)
This table oﬀers a vivid illustration of Theorem 6. By Proposition 7.4.3, the rows
of the table for 1, φ, εφ, and ε list the coeﬃcients of the HOMFLY polynomial of
the link closure ˆβ, up to shifting by a2iq−8 for various i.
Remark C.0.1. As it happens, ˆβ is the link of the complex plane curve singularity
given by y = x
3
2 + x
7
4 . In particular, it is an iterated torus knot.
Remark C.0.2. Let G = SL4. By Theorem 7, it should be possible to decompose
⟨β⟩0
q into a Z[q]-linear combination of total Springer representations Qu, as we run
over representatives u of GF -orbits in UF .
The GF -orbits are indexed by the partitions of the integer 4. Let the orbit of
the identity correspond to the partition (1, 1, 1, 1) ⊢4. Then the Qu are:
Q4 = 1,
Q3,1 = 1 + qφ,
Q2,2 = 1 + qφ + q2ψ,
Q2,1,1 = 1 + (q + q2)φ + q2ψ + q3εφ,
Q1,1,1,1 = 1 + (q + q2 + q3)φ + (q2 + q4)ψ + (q3 + q4 + q5)εφ + q6ε.
Using (34), we ﬁnd that:
⟨β⟩0
q = q16Q1 + (q10 + q11 + q12 + q13 + q14)Q3,1
+ (q6 −q7 + q8 + q10 + q12)Q2,2
+ (q3 + q4 + q5 + 2q6 + 2q7 + 2q8 + q9 + q10)Q2,1,1
+ (1 + q2 + q4)Q1,1,1,1.
It is curious that the entries in (34) are all positive, whereas the decomposition into
Qu’s contains a (single) negative term.
84
MINH-TÂM QUANG TRINH

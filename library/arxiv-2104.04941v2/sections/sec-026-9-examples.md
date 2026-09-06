---
doc_id: arxiv-2104.04941v2
doc_title: "FOCK–GONCHAROV COORDINATES FOR SEMISIMPLE LIE GROUPS S. GILLES"
section_id: sec-026-9-examples
section_title: "Examples"
section_number: 9
pages: 44-53
source_pdf: 2104.04941v2.pdf
source_sha256: 84426ed37754aa78
doc_brief: "FOCK–GONCHAROV COORDINATES FOR SEMISIMPLE LIE GROUPS S. GILLES — Fock and Goncharov [FG06b] introduced cluster ensembles, p roviding a framework for coordi- nates on varieties of surface"
---
Here we provide examples, in consistent notation, of Q, µrot, µﬂip , and M for various types (for F4 see
the examples of Section 5). Our notation is intended to agree with that of [Zic19], with the caveat that the
mutations we present are longer but do not require vertex ren aming (see Section 5.7). All Dynkin diagrams
are taken from [Kna96, Figure 2.4], equivalently [Bou02, Pl ates II–IX] (ignoring the extending nodes). In
each example, α = (h1,h 2,h 3,u ), where the coordinates of hi are {hij }, as in Example 5.20.
These results were obtained by the latex-Q, print-murot, print-muflip, and print-M commands of
[Gil20].
9.1. A5. We use the Dynkin diagram . The Coxeter element is c = { 3, 2, 4, 1, 5 }, and the partitions are
T0 = { 3 },T1 = { 2, 4 }, T2 = { 1, 5 }. The Dynkin-type quiver follows.
3
2
4
1
5
QA5 is given in Figure 38.
µ rot =
{
v31, v21, v41, v11, v51, v32, v22, v42, v12, v52, v31, v21, v41, v11, v51, v31, v21, v41, v11, v51, v31, v21, v41, v11,
v51, v31, v21, v41, v11, v51, v31, v21, v41, v11, v51, v32, v22, v42, v12, v52, v32, v22, v42, v12, v52, v32, v22, v42,
v12, v52, v32, v22, v42, v12, v52, v31, v32, v31, v32, v31, v21, v41, v22, v42, v21, v41, v22, v42, v21, v41, v11, v51,
v12, v52, v11, v51, v12, v52, v11, v51
}
µ ﬂip =
{
w15, w55, w25, w45, w35, w14, w54, w24, w44, w34, w15, w55, w25, w45, w35, w12, w52, w22, w42, w32, w11,
w51, w21, w41, w31, w12, w52, w22, w42, w32, w35, w25, w45, w15, w55, w34, w24, w44, w14, w54, w33, w23,
w43, w13, w53, w32, w22, w42, w12, w52, w31, w21, w41, w11, w51, w35, w25, w45, w15, w55, w34, w24, w44,
w14, w54, w33, w23, w43, w13, w53, w32, w22, w42, w12, w52, w35, w25, w45, w15, w55, w34, w24, w44, w14,
w54, w33, w23, w43, w13, w53, w35, w25, w45, w15, w55, w34, w24, w44, w14, w54, w35, w25, w45, w15, w55,
44
v31v32
v21v22
v41v42
v11v12
v51v52
B3
B2
B4
B1
B5
C3
C2
C4
C1
C5
A3
A2
A4
A1
A5
Figure 38. Q for A5.
w11, w51, w12, w52, w13, w53, w14, w54, w15, w55, w11, w51, w12, w52, w13, w53, w14, w54, w11, w51, w12,
w52, w13, w53, w11, w51, w12, w52, w11, w51, w15, w55, w14, w54, w13, w53, w12, w52, w11, w51, w21, w41,
w22, w42, w23, w43, w24, w44, w25, w45, w21, w41, w22, w42, w23, w43, w24, w44, w21, w41, w22, w42, w23,
w43, w21, w41, w22, w42, w21, w41, w25, w45, w24, w44, w23, w43, w22, w42, w21, w41, w31, w32, w33, w34,
w35, w31, w32, w33, w34, w31, w32, w33, w31, w32, w31, w35, w34, w33, w32, w31, w14, w54, w15, w55, w14,
w54, w15, w55, w14, w54, w24, w44, w25, w45, w24, w44, w25, w45, w24, w44, w34, w35, w34, w35, w34, w11,
w51, w12, w52, w11, w51, w12, w52, w11, w51, w21, w41, w22, w42, w21, w41, w22, w42, w21, w41, w31, w32,
w31, w32, w31
}
M(α) gives
A1 =h11 A2 =h12 A3 =h13 A4 =h14 A5 =h15
B1 =h21 B2 =h22 B3 =h23 B4 =h24 B5 =h25
C1 =h35 C2 =h34 C3 =h33 C4 =h32 C5 =h31
v31 = ∆ w6ω3(u) ·h23 v32 = ∆ w11ω3(u) ·h23
v21 = ∆ w7ω2(u) · h13h22
h14
v22 = ∆ w12ω2(u) · h13h22
h14
v41 = ∆ w8ω4(u) · h13h24
h12
v42 = ∆ w13ω4(u) · h13h24
h12
v11 = ∆ w9ω1(u) · h13h21
h15
v12 = ∆ w14ω1(u) · h14h21
h15
v51 = ∆ w10ω5(u) · h13h25
h11
v52 = ∆ w15ω5(u) · h12h25
h11
9.2. B3. We use the Dynkin diagram . This is linear, so the Coxeter element and partitions are tr iv-
iallyc = { 1, 2, 3 } andT0 = { 1 },T 1 = { 2 },T 2 = { 3 }. The Dynkin-type quiver follows (recall Remark 5.3).
1 2 3
QB3 is given in Figure 39.
µ rot =
{
v11, v21, v31, v12, v22, v32, v11, v21, v31, v11, v12, v11, v12, v11, v21, v22, v21, v22, v21, v31, v32, v31, v32, v31
}
µ ﬂip =
{
w35, w25, w15, w34, w24, w14, w35, w25, w15, w32, w22, w12, w31, w21, w11, w32, w22, w12, w15, w25, w35,
w14, w24, w34, w13, w23, w33, w12, w22, w32, w11, w21, w31, w15, w25, w35, w14, w24, w34, w13, w23, w33,
w12, w22, w32, w15, w25, w35, w14, w24, w34, w13, w23, w33, w15, w25, w35, w14, w24, w34, w15, w25, w35,
w31, w32, w33, w34, w35, w31, w32, w33, w34, w31, w32, w33, w31, w32, w31, w35, w34, w33, w32, w31, w21,
w22, w23, w24, w25, w21, w22, w23, w24, w21, w22, w23, w21, w22, w21, w25, w24, w23, w22, w21, w11, w12,
w13, w14, w15, w11, w12, w13, w14, w11, w12, w13, w11, w12, w11, w15, w14, w13, w12, w11, w34, w35, w34,
45
v11v12
v21v22
v31v32
B1
B2
B3
C1
C2
C3
A1A2A3
Figure 39. Q for B3.
v11v12v13
v21v22v23
v31v32v33
v41v42v43
v51v52v53
B1
B2
B3
B4
B5
C1
C2
C3
C4
C5
A1A2A3
A4
A5
Figure 40. Q for D5.
w35, w34, w24, w25, w24, w25, w24, w14, w15, w14, w15, w14, w31, w32, w31, w32, w31, w21, w22, w21, w22,
w21, w11, w12, w11, w12, w11
}
M(α) gives
A1 =h11 A2 =h12 A3 =h13
B1 =h11 B2 =h12 B3 =h13
C1 =h11 C2 =h12 C3 =h13
v11 = ∆ w4ω1 (u) ·h21 v21 = ∆ w5ω2(u) · h11h22
h12
v31 = ∆ w6ω3(u) · h11h23
h13
v12 = ∆ w7ω1 (u) · h12h21
h11
v22 = ∆ w8ω2(u) ·h11h22 v32 = ∆ w9ω3(u) · h12h23
h13
9.3. D5. Based on the Dynkin diagram , the following quiver is of well-rooted Dynkin type for D5
(recall that σG is trivial for type D2n and non-trivial for type D2n+1). It admits an induced Coxeter element
c = { 1, 2, 3, 4, 5 }, with partitions
T0 = { 1 }, T 1 = { 2 }, T 2 = { 3 }, T 3 = { 4, 5 }.
1 2 3
4
5
QD5 is given in Figure 40.
46
µ rot =
{
v11, v21, v31, v41, v51, v12, v22, v32, v42, v52, v11, v21, v31, v41, v51, v13, v23, v33, v43, v53, v12, v22, v32, v42,
v52, v11, v21, v31, v41, v51, v11, v21, v31, v41, v51, v11, v21, v31, v41, v51, v11, v21, v31, v41, v51, v11, v21, v31,
v41, v51, v11, v21, v31, v41, v51, v12, v22, v32, v42, v52, v12, v22, v32, v42, v52, v12, v22, v32, v42, v52, v12, v22,
v32, v42, v52, v12, v22, v32, v42, v52, v13, v23, v33, v43, v53, v13, v23, v33, v43, v53, v13, v23, v33, v43, v53, v13,
v23, v33, v43, v53, v13, v23, v33, v43, v53, v11, v12, v13, v11, v12, v11, v13, v12, v11, v21, v22, v23, v21, v22, v21,
v23, v22, v21, v31, v32, v33, v31, v32, v31, v33, v32, v31, v41, v51, v42, v52, v43, v53, v41, v51, v42, v52, v41, v51,
v43, v53, v42, v52, v41, v51
}
µ ﬂip =
{
w47, w57, w37, w27, w17, w46, w56, w36, w26, w16, w47, w57, w37, w27, w17, w45, w55, w35, w25, w15, w46,
w56, w36, w26, w16, w47, w57, w37, w27, w17, w43, w53, w33, w23, w13, w42, w52, w32, w22, w12, w43, w53,
w33, w23, w13, w41, w51, w31, w21, w11, w42, w52, w32, w22, w12, w43, w53, w33, w23, w13, w17, w27, w37,
w47, w57, w16, w26, w36, w46, w56, w15, w25, w35, w45, w55, w14, w24, w34, w44, w54, w13, w23, w33, w43,
w53, w12, w22, w32, w42, w52, w11, w21, w31, w41, w51, w17, w27, w37, w47, w57, w16, w26, w36, w46, w56,
w15, w25, w35, w45, w55, w14, w24, w34, w44, w54, w13, w23, w33, w43, w53, w12, w22, w32, w42, w52, w17,
w27, w37, w47, w57, w16, w26, w36, w46, w56, w15, w25, w35, w45, w55, w14, w24, w34, w44, w54, w13, w23,
w33, w43, w53, w17, w27, w37, w47, w57, w16, w26, w36, w46, w56, w15, w25, w35, w45, w55, w14, w24, w34,
w44, w54, w17, w27, w37, w47, w57, w16, w26, w36, w46, w56, w15, w25, w35, w45, w55, w17, w27, w37, w47,
w57, w16, w26, w36, w46, w56, w17, w27, w37, w47, w57, w41, w51, w42, w52, w43, w53, w44, w54, w45, w55,
w46, w56, w47, w57, w41, w51, w42, w52, w43, w53, w44, w54, w45, w55, w46, w56, w41, w51, w42, w52, w43,
w53, w44, w54, w45, w55, w41, w51, w42, w52, w43, w53, w44, w54, w41, w51, w42, w52, w43, w53, w41, w51,
w42, w52, w41, w51, w47, w57, w46, w56, w45, w55, w44, w54, w43, w53, w42, w52, w41, w51, w31, w32, w33,
w34, w35, w36, w37, w31, w32, w33, w34, w35, w36, w31, w32, w33, w34, w35, w31, w32, w33, w34, w31, w32,
w33, w31, w32, w31, w37, w36, w35, w34, w33, w32, w31, w21, w22, w23, w24, w25, w26, w27, w21, w22, w23,
w24, w25, w26, w21, w22, w23, w24, w25, w21, w22, w23, w24, w21, w22, w23, w21, w22, w21, w27, w26, w25,
w24, w23, w22, w21, w11, w12, w13, w14, w15, w16, w17, w11, w12, w13, w14, w15, w16, w11, w12, w13, w14,
w15, w11, w12, w13, w14, w11, w12, w13, w11, w12, w11, w17, w16, w15, w14, w13, w12, w11, w45, w55, w46,
w56, w47, w57, w45, w55, w46, w56, w45, w55, w47, w57, w46, w56, w45, w55, w35, w36, w37, w35, w36, w35,
w37, w36, w35, w25, w26, w27, w25, w26, w25, w27, w26, w25, w15, w16, w17, w15, w16, w15, w17, w16, w15,
w41, w51, w42, w52, w43, w53, w41, w51, w42, w52, w41, w51, w43, w53, w42, w52, w41, w51, w31, w32, w33,
w31, w32, w31, w33, w32, w31, w21, w22, w23, w21, w22, w21, w23, w22, w21, w11, w12, w13, w11, w12, w11,
w13, w12, w11
}
M(α) gives
A1 =h11 A2 =h12 A3 =h13 A4 =h14 A5 =h15
B1 =h21 B2 =h22 B3 =h23 B4 =h24 B5 =h25
C1 =h31 C2 =h32 C3 =h33 C4 =h35 C5 =h34
v11 = ∆ w6ω1(u) ·h21 v12 = ∆ w11ω1(u) · h12h21
h11
v13 = ∆ w16ω1(u) · h13h21
h11
v21 = ∆ w7ω2(u) · h11h22
h12
v22 = ∆ w12ω2(u) ·h22 v23 = ∆ w17ω2(u) · h11h13h22
h12
v31 = ∆ w8ω3(u) · h11h23
h13
v32 = ∆ w13ω3(u) · h11h12h23
h13
v33 = ∆ w18ω3(u) ·h12h23
v41 = ∆ w9ω4(u) · h11h24
h15
v42 = ∆ w14ω4(u) · h12h24
h15
v43 = ∆ w19ω4(u) · h13h24
h15
v51 = ∆ w10ω5 (u) · h11h25
h14
v52 = ∆ w15ω5(u) · h12h25
h14
v53 = ∆ w20ω5(u) · h13h25
h14
9.4. G2. Based on the Dynkin diagram , (with c = { 1, 2 } and trivial linear partitioning) we use the
following quiver for Dynkin type.
1 2
QG2 is given in Figure 41.
µ rot =
{
v11, v21, v12, v22, v11, v21, v11, v12, v11, v12, v11, v21, v22, v21, v22, v21
}
µ ﬂip =
{
w25, w15, w24, w14, w25, w15, w22, w12, w21, w11, w22, w12, w15, w25, w14, w24, w13, w23, w12, w22, w11,
w21, w15, w25, w14, w24, w13, w23, w12, w22, w15, w25, w14, w24, w13, w23, w15, w25, w14, w24, w15, w25,
w21, w22, w23, w24, w25, w21, w22, w23, w24, w21, w22, w23, w21, w22, w21, w25, w24, w23, w22, w21, w11,
47
v11v12
v21v22
B1
B2
C1
C2
A1
A2
Figure 41. Q for G2.
v21v22v23v24v25
v41v42v43v44v45
v31v32v33v34v35
v51v52v53v54v55
v11v12v13v14v15
v61v62v63v64v65
B2
B4
B3
B5
B1
B6
C2
C4
C3
C5
C1
C6
A2A4
A3
A5
A1
A6
Figure 42. Q for E6.
w12, w13, w14, w15, w11, w12, w13, w14, w11, w12, w13, w11, w12, w11, w15, w14, w13, w12, w11, w24, w25,
w24, w25, w24, w14, w15, w14, w15, w14, w21, w22, w21, w22, w21, w11, w12, w11, w12, w11
}
M(α) gives
A1 =h11 A2 =h12
B1 =h21 B2 =h22
C1 =h31 C2 =h32
v11 = ∆ w3ω1(u) ·h21 v21 = ∆ w4ω2 (u) · h3
11h22
h12
v12 = ∆ w5ω1(u) ·h11h21 v22 = ∆ w6ω2 (u) · h3
11h22
h12
9.5. E6. Based on the Dynkin diagram , the following quiver is of well-rooted Dynkin type for E6.
It admits an induced Coxeter element c = { 2, 4, 3, 5, 1, 6 }, with partitions T0 = { 2 },T 1 = { 4 },T 3 =
{ 3, 5 },T 4 = { 1, 6 }.
2 4
5
3
6
1
QE6 is given in Figure 42.
µ rot =
{
v21, v41, v31, v51, v11, v61, v22, v42, v32, v52, v12, v62, v21, v41, v31, v51, v11, v61, v23, v43, v33, v53, v13, v63,
v22, v42, v32, v52, v12, v62, v21, v41, v31, v51, v11, v61, v24, v44, v34, v54, v14, v64, v23, v43, v33, v53, v13, v63,
v22, v42, v32, v52, v12, v62, v21, v41, v31, v51, v11, v61, v25, v45, v35, v55, v15, v65, v24, v44, v34, v54, v14, v64,
48
v23, v43, v33, v53, v13, v63, v22, v42, v32, v52, v12, v62, v21, v41, v31, v51, v11, v61, v21, v41, v31, v51, v11, v61,
v21, v41, v31, v51, v11, v61, v21, v41, v31, v51, v11, v61, v21, v41, v31, v51, v11, v61, v21, v41, v31, v51, v11, v61,
v21, v41, v31, v51, v11, v61, v21, v41, v31, v51, v11, v61, v22, v42, v32, v52, v12, v62, v22, v42, v32, v52, v12, v62,
v22, v42, v32, v52, v12, v62, v22, v42, v32, v52, v12, v62, v22, v42, v32, v52, v12, v62, v22, v42, v32, v52, v12, v62,
v22, v42, v32, v52, v12, v62, v23, v43, v33, v53, v13, v63, v23, v43, v33, v53, v13, v63, v23, v43, v33, v53, v13, v63,
v23, v43, v33, v53, v13, v63, v23, v43, v33, v53, v13, v63, v23, v43, v33, v53, v13, v63, v23, v43, v33, v53, v13, v63,
v24, v44, v34, v54, v14, v64, v24, v44, v34, v54, v14, v64, v24, v44, v34, v54, v14, v64, v24, v44, v34, v54, v14, v64,
v24, v44, v34, v54, v14, v64, v24, v44, v34, v54, v14, v64, v24, v44, v34, v54, v14, v64, v25, v45, v35, v55, v15, v65,
v25, v45, v35, v55, v15, v65, v25, v45, v35, v55, v15, v65, v25, v45, v35, v55, v15, v65, v25, v45, v35, v55, v15, v65,
v25, v45, v35, v55, v15, v65, v25, v45, v35, v55, v15, v65, v21, v22, v23, v24, v25, v21, v22, v23, v24, v21, v22, v23,
v21, v22, v21, v25, v24, v23, v22, v21, v41, v42, v43, v44, v45, v41, v42, v43, v44, v41, v42, v43, v41, v42, v41, v45,
v44, v43, v42, v41, v31, v51, v32, v52, v33, v53, v34, v54, v35, v55, v31, v51, v32, v52, v33, v53, v34, v54, v31, v51,
v32, v52, v33, v53, v31, v51, v32, v52, v31, v51, v35, v55, v34, v54, v33, v53, v32, v52, v31, v51, v11, v61, v12, v62,
v13, v63, v14, v64, v15, v65, v11, v61, v12, v62, v13, v63, v14, v64, v11, v61, v12, v62, v13, v63, v11, v61, v12, v62,
v11, v61, v15, v65, v14, v64, v13, v63, v12, v62, v11, v61
}
µ ﬂip =
{
w1b, w6b, w3b, w5b, w4b, w2b, w1a, w6a, w3a, w5a, w4a, w2a, w1b, w6b, w3b, w5b, w4b, w2b, w19, w69, w39, w59,
w49, w29, w1a, w6a, w3a, w5a, w4a, w2a, w1b, w6b, w3b, w5b, w4b, w2b, w18, w68, w38, w58, w48, w28, w19,
w69, w39, w59, w49, w29, w1a, w6a, w3a, w5a, w4a, w2a, w1b, w6b, w3b, w5b, w4b, w2b, w17, w67, w37, w57,
w47, w27, w18, w68, w38, w58, w48, w28, w19, w69, w39, w59, w49, w29, w1a, w6a, w3a, w5a, w4a, w2a, w1b,
w6b, w3b, w5b, w4b, w2b, w15, w65, w35, w55, w45, w25, w14, w64, w34, w54, w44, w24, w15, w65, w35, w55,
w45, w25, w13, w63, w33, w53, w43, w23, w14, w64, w34, w54, w44, w24, w15, w65, w35, w55, w45, w25, w12,
w62, w32, w52, w42, w22, w13, w63, w33, w53, w43, w23, w14, w64, w34, w54, w44, w24, w15, w65, w35, w55,
w45, w25, w11, w61, w31, w51, w41, w21, w12, w62, w32, w52, w42, w22, w13, w63, w33, w53, w43, w23, w14,
w64, w34, w54, w44, w24, w15, w65, w35, w55, w45, w25, w2b, w4b, w3b, w5b, w1b, w6b, w2a, w4a, w3a, w5a,
w1a, w6a, w29, w49, w39, w59, w19, w69, w28, w48, w38, w58, w18, w68, w27, w47, w37, w57, w17, w67, w26,
w46, w36, w56, w16, w66, w25, w45, w35, w55, w15, w65, w24, w44, w34, w54, w14, w64, w23, w43, w33, w53,
w13, w63, w22, w42, w32, w52, w12, w62, w21, w41, w31, w51, w11, w61, w2b, w4b, w3b, w5b, w1b, w6b, w2a,
w4a, w3a, w5a, w1a, w6a, w29, w49, w39, w59, w19, w69, w28, w48, w38, w58, w18, w68, w27, w47, w37, w57,
w17, w67, w26, w46, w36, w56, w16, w66, w25, w45, w35, w55, w15, w65, w24, w44, w34, w54, w14, w64, w23,
w43, w33, w53, w13, w63, w22, w42, w32, w52, w12, w62, w2b, w4b, w3b, w5b, w1b, w6b, w2a, w4a, w3a, w5a,
w1a, w6a, w29, w49, w39, w59, w19, w69, w28, w48, w38, w58, w18, w68, w27, w47, w37, w57, w17, w67, w26,
w46, w36, w56, w16, w66, w25, w45, w35, w55, w15, w65, w24, w44, w34, w54, w14, w64, w23, w43, w33, w53,
w13, w63, w2b, w4b, w3b, w5b, w1b, w6b, w2a, w4a, w3a, w5a, w1a, w6a, w29, w49, w39, w59, w19, w69, w28,
w48, w38, w58, w18, w68, w27, w47, w37, w57, w17, w67, w26, w46, w36, w56, w16, w66, w25, w45, w35, w55,
w15, w65, w24, w44, w34, w54, w14, w64, w2b, w4b, w3b, w5b, w1b, w6b, w2a, w4a, w3a, w5a, w1a, w6a, w29,
w49, w39, w59, w19, w69, w28, w48, w38, w58, w18, w68, w27, w47, w37, w57, w17, w67, w26, w46, w36, w56,
w16, w66, w25, w45, w35, w55, w15, w65, w2b, w4b, w3b, w5b, w1b, w6b, w2a, w4a, w3a, w5a, w1a, w6a, w29,
w49, w39, w59, w19, w69, w28, w48, w38, w58, w18, w68, w27, w47, w37, w57, w17, w67, w26, w46, w36, w56,
w16, w66, w2b, w4b, w3b, w5b, w1b, w6b, w2a, w4a, w3a, w5a, w1a, w6a, w29, w49, w39, w59, w19, w69, w28,
w48, w38, w58, w18, w68, w27, w47, w37, w57, w17, w67, w2b, w4b, w3b, w5b, w1b, w6b, w2a, w4a, w3a, w5a,
w1a, w6a, w29, w49, w39, w59, w19, w69, w28, w48, w38, w58, w18, w68, w2b, w4b, w3b, w5b, w1b, w6b, w2a,
w4a, w3a, w5a, w1a, w6a, w29, w49, w39, w59, w19, w69, w2b, w4b, w3b, w5b, w1b, w6b, w2a, w4a, w3a, w5a,
w1a, w6a, w2b, w4b, w3b, w5b, w1b, w6b, w11, w61, w12, w62, w13, w63, w14, w64, w15, w65, w16, w66, w17,
w67, w18, w68, w19, w69, w1a, w6a, w1b, w6b, w11, w61, w12, w62, w13, w63, w14, w64, w15, w65, w16, w66,
w17, w67, w18, w68, w19, w69, w1a, w6a, w11, w61, w12, w62, w13, w63, w14, w64, w15, w65, w16, w66, w17,
w67, w18, w68, w19, w69, w11, w61, w12, w62, w13, w63, w14, w64, w15, w65, w16, w66, w17, w67, w18, w68,
w11, w61, w12, w62, w13, w63, w14, w64, w15, w65, w16, w66, w17, w67, w11, w61, w12, w62, w13, w63, w14,
w64, w15, w65, w16, w66, w11, w61, w12, w62, w13, w63, w14, w64, w15, w65, w11, w61, w12, w62, w13, w63,
w14, w64, w11, w61, w12, w62, w13, w63, w11, w61, w12, w62, w11, w61, w1b, w6b, w1a, w6a, w19, w69, w18,
w68, w17, w67, w16, w66, w15, w65, w14, w64, w13, w63, w12, w62, w11, w61, w31, w51, w32, w52, w33, w53,
w34, w54, w35, w55, w36, w56, w37, w57, w38, w58, w39, w59, w3a, w5a, w3b, w5b, w31, w51, w32, w52, w33,
w53, w34, w54, w35, w55, w36, w56, w37, w57, w38, w58, w39, w59, w3a, w5a, w31, w51, w32, w52, w33, w53,
w34, w54, w35, w55, w36, w56, w37, w57, w38, w58, w39, w59, w31, w51, w32, w52, w33, w53, w34, w54, w35,
w55, w36, w56, w37, w57, w38, w58, w31, w51, w32, w52, w33, w53, w34, w54, w35, w55, w36, w56, w37, w57,
w31, w51, w32, w52, w33, w53, w34, w54, w35, w55, w36, w56, w31, w51, w32, w52, w33, w53, w34, w54, w35,
w55, w31, w51, w32, w52, w33, w53, w34, w54, w31, w51, w32, w52, w33, w53, w31, w51, w32, w52, w31, w51,
w3b, w5b, w3a, w5a, w39, w59, w38, w58, w37, w57, w36, w56, w35, w55, w34, w54, w33, w53, w32, w52, w31,
w51, w41, w42, w43, w44, w45, w46, w47, w48, w49, w4a, w4b, w41, w42, w43, w44, w45, w46, w47, w48, w49,
49
w4a, w41, w42, w43, w44, w45, w46, w47, w48, w49, w41, w42, w43, w44, w45, w46, w47, w48, w41, w42, w43,
w44, w45, w46, w47, w41, w42, w43, w44, w45, w46, w41, w42, w43, w44, w45, w41, w42, w43, w44, w41, w42,
w43, w41, w42, w41, w4b, w4a, w49, w48, w47, w46, w45, w44, w43, w42, w41, w21, w22, w23, w24, w25, w26,
w27, w28, w29, w2a, w2b, w21, w22, w23, w24, w25, w26, w27, w28, w29, w2a, w21, w22, w23, w24, w25, w26,
w27, w28, w29, w21, w22, w23, w24, w25, w26, w27, w28, w21, w22, w23, w24, w25, w26, w27, w21, w22, w23,
w24, w25, w26, w21, w22, w23, w24, w25, w21, w22, w23, w24, w21, w22, w23, w21, w22, w21, w2b, w2a, w29,
w28, w27, w26, w25, w24, w23, w22, w21, w17, w67, w18, w68, w19, w69, w1a, w6a, w1b, w6b, w17, w67, w18,
w68, w19, w69, w1a, w6a, w17, w67, w18, w68, w19, w69, w17, w67, w18, w68, w17, w67, w1b, w6b, w1a, w6a,
w19, w69, w18, w68, w17, w67, w37, w57, w38, w58, w39, w59, w3a, w5a, w3b, w5b, w37, w57, w38, w58, w39,
w59, w3a, w5a, w37, w57, w38, w58, w39, w59, w37, w57, w38, w58, w37, w57, w3b, w5b, w3a, w5a, w39, w59,
w38, w58, w37, w57, w47, w48, w49, w4a, w4b, w47, w48, w49, w4a, w47, w48, w49, w47, w48, w47, w4b, w4a,
w49, w48, w47, w27, w28, w29, w2a, w2b, w27, w28, w29, w2a, w27, w28, w29, w27, w28, w27, w2b, w2a, w29,
w28, w27, w11, w61, w12, w62, w13, w63, w14, w64, w15, w65, w11, w61, w12, w62, w13, w63, w14, w64, w11,
w61, w12, w62, w13, w63, w11, w61, w12, w62, w11, w61, w15, w65, w14, w64, w13, w63, w12, w62, w11, w61,
w31, w51, w32, w52, w33, w53, w34, w54, w35, w55, w31, w51, w32, w52, w33, w53, w34, w54, w31, w51, w32,
w52, w33, w53, w31, w51, w32, w52, w31, w51, w35, w55, w34, w54, w33, w53, w32, w52, w31, w51, w41, w42,
w43, w44, w45, w41, w42, w43, w44, w41, w42, w43, w41, w42, w41, w45, w44, w43, w42, w41, w21, w22, w23,
w24, w25, w21, w22, w23, w24, w21, w22, w23, w21, w22, w21, w25, w24, w23, w22, w21
}
M(α) gives
A1 =h11 A2 =h12 A3 =h13 A4 =h14 A5 =h15 A6 =h16
B1 =h21 B2 =h22 B3 =h23 B4 =h24 B5 =h25 B6 =h26
C1 =h36 C2 =h32 C3 =h35 C4 =h34 C5 =h33 C6 =h31
v21 = ∆ w7ω2(u) ·h22 v41 = ∆ w8ω4(u) · h12h24
h14
v31 = ∆ w9ω3(u) · h12h23
h15
v51 = ∆ w10ω5(u) · h12h25
h13
v11 = ∆ w11ω1(u) · h12h21
h16
v61 = ∆ w12ω6 (u) · h12h26
h11
v22 = ∆ w13ω2(u) · h14h22
h12
v42 = ∆ w14ω4(u) ·h12h24 v32 = ∆ w15ω3 (u) · h12h14h23
h15
v52 = ∆ w16ω5(u) · h12h14h25
h13
v12 = ∆ w17ω1(u) · h14h21
h16
v62 = ∆ w18ω6 (u) · h14h26
h11
v23 = ∆ w19ω2(u) ·h22 v43 = ∆ w20ω4(u) ·h2
12h24 v33 = ∆ w21ω3 (u) · h12h14h23
h15
v53 = ∆ w22ω5(u) · h12h14h25
h13
v13 = ∆ w23ω1(u) · h12h21
h16
v63 = ∆ w24ω6 (u) · h12h26
h11
v24 = ∆ w25ω2(u) ·h14h22 v44 = ∆ w26ω4(u) ·h12h14h24 v34 = ∆ w27ω3 (u) · h12h14h23
h15
v54 = ∆ w28ω5(u) · h12h14h25
h13
v14 = ∆ w29ω1(u) · h14h21
h16
v64 = ∆ w30ω6 (u) · h14h26
h11
v25 = ∆ w31ω2(u) · h14h22
h12
v45 = ∆ w32ω4(u) ·h12h24 v35 = ∆ w33ω3 (u) · h14h23
h15
v55 = ∆ w34ω5(u) · h14h25
h13
v15 = ∆ w35ω1(u) · h15h21
h16
v65 = ∆ w36ω6 (u) · h13h26
h11
9.6. E7. Based on the Dynkin diagram , the following quiver is of well-rooted Dynkin type for
E7. It admits an induced Coxeter element c = { 1, 2, 3, 4, 5, 6, 7 }, with partitions
T0 = { 1 }, T 1 = { 2 }, T 2 = { 3 }, T 3 = { 4, 5 }, T 4 = { 6 }, T 5 = { 7 }.
1 2 3
4
5 6 7
QE7 is given in Figure 43. The mutations are too long to be reasona bly presented.
50
v71v72v73v74v75v76v77v78
v61v62v63v64v65v66v67v68
v51v52v53v54v55v56v57v58
v41v42v43v44v45v46v47v48
v21v22v23v24v25v26v27v28
v31v32v33v34v35v36v37v38
v11v12v13v14v15v16v17v18
B7
B6
B5
B4
B2
B3
B1
C7
C6
C5
C4
C2
C3
C1
A7A6A5A4
A2
A3A1
Figure 43. Q for E7.
9.7. E8. Based on the Dynkin diagram , the following quiver is of well-rooted Dynkin type for
E8. It admits an induced Coxeter element c = { 1, 2, 3, 4, 5, 6, 7, 8 }, with partitions
T0 = { 1 },T 1 = { 2 },T 2 = { 3 },T 3 = { 4 },T 4 = { 5 },T 5 = { 6, 7 },T 6 = { 8 }.
1 2 3 4 5
6
7 8
QE8 is given in Figure 44. The mutations are too long to be reasona bly presented.
9.8. D2 =A1 ×A1. Using the Dynkin diagram , we use the following quiver.
1 2
The quiver QG is shown in Figure 45.
µ rot =
{ }
µ ﬂip =
{
w11, w21
}
And M is given the edge coordinate assignment only. Since σD2 is trivial, this is direct.
A1 =h11 A2 =h12
B1 =h21 B2 =h22
C1 =h31 C2 =h32
9.9. A3 ×C2. To demonstrate Lemma 8.1 for a less trivial type, consider G =G1 ⊕G2, with G1 of type A3
and G2 of type C2. The Dynkin diagram for G is . The quiver QG is the disjoint union of QA3 and
QC2 as shown in Figure 46. We label the simple roots as shown in the Dynkin type quiver.
2
1
3
4 5
µ rot =
{
v21, v11, v31, v21, v11, v31, v21, v11, v31, v21, v11, v31, v41, v51
}
µ ﬂip =
{
w13, w33, w23, w11, w31, w21, w23, w13, w33, w22, w12, w32, w21, w11, w31, w23, w13, w33, w22, w12, w32,
w23, w13, w33, w11, w31, w12, w32, w13, w33, w11, w31, w12, w32, w11, w31, w13, w33, w12, w32, w11, w31,
51
v81 v82 v83 v84 v85 v86 v87 v88 v89 v8a v8b v8c v8d v8e
v71 v72 v73 v74 v75 v76 v77 v78 v79 v7a v7b v7c v7d v7e
v61 v62 v63 v64 v65 v66 v67 v68 v69 v6a v6b v6c v6d v6e
v51 v52 v53 v54 v55 v56 v57 v58 v59 v5a v5b v5c v5d v5e
v41 v42 v43 v44 v45 v46 v47 v48 v49 v4a v4b v4c v4d v4e
v21 v22 v23 v24 v25 v26 v27 v28 v29 v2a v2b v2c v2d v2e
v31 v32 v33 v34 v35 v36 v37 v38 v39 v3a v3b v3c v3d v3e
v11 v12 v13 v14 v15 v16 v17 v18 v19 v1a v1b v1c v1d v1e
B8
B7
B6
B5
B4
B2
B3
B1
C8
C7
C6
C5
C4
C2
C3
C1
A8 A7 A6 A5 A4
A2
A3 A1
Figure 44. Q for E8.
52
01
2
B1
B2
A2A1
C1
C2
Figure 45. Q for D2 =A1 ×A1.
v21
v11
v31
B2
B1
B3
C2
C1
C3
A2
A1
A3
v41
v51
B4
B5
C4
C5
A4A5
Figure 46. Q for A3 ×C2.
w21, w22, w23, w21, w22, w21, w23, w22, w21, w53, w43, w51, w41, w43, w53, w42, w52, w41, w51, w43,
w53, w42, w52, w43, w53, w51, w52, w53, w51, w52, w51, w53, w52, w51, w41, w42, w43, w41, w42, w41, w43,
w42, w41
}
To construct M, as described in Lemma 8.1, the coordinates on u are exactly divided between two
elements of N− corresponding to A3 and C2. Let (wk)1 be the word wk for A3, and (wk)2 be the word wk
for C2 (with the indices of each component sαi increased by 3). Then appropriate i and j in ∆ (wk)iωj (u)
will allow extracting coordinates of u in ways corresponding to the factors Gi.
A1 =h11 A2 =h12 A3 =h13 A4 =h14 A5 =h15
B1 =h21 B2 =h22 B3 =h23 B4 =h24 B5 =h25
C1 =h33 C2 =h32 C3 =h31 C4 =h34 C5 =h35
v21 = ∆ (w4)1ω2(u) ·h22 v11 = ∆ (w5)1ω1(u) · h12h21
h13
v31 = ∆ (w6)1ω3(u) · h12h23
h11
v41 = ∆ (w3)2ω4(u) ·h24 v51 = ∆ (w4)2ω5(u) · h2
14h25
h15

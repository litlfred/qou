---
doc_id: arxiv-2104.04941v2
doc_title: "FOCK–GONCHAROV COORDINATES FOR SEMISIMPLE LIE GROUPS S. GILLES"
section_id: sec-021-56-the-map-m
section_title: "The map M"
section_number: 5.6
pages: 29-33
source_pdf: 2104.04941v2.pdf
source_sha256: 84426ed37754aa78
doc_brief: "FOCK–GONCHAROV COORDINATES FOR SEMISIMPLE LIE GROUPS S. GILLES — Fock and Goncharov [FG06b] introduced cluster ensembles, p roviding a framework for coordi- nates on varieties of surface"
---
association to the Lie group G. More speciﬁcally, the vertices of Q should be associated to coordinates on
Conf ∗
3(G/N+).
Recall that Conf ∗
3(G/N+) ∼= H 3 ×H (N− ∩w0G0) by Lemma 4.3. So let α ∈ Conf ∗
3(G/N+) be given by
α = (h1,h 2,h 3,u ). By abuse of notation, we denote the coordinate in T A
Q by the name of the vertex to which
it is associated, and regard
T A
Q =
~T A
A
/bracehtipdownleft/bracehtipupright/bracehtipupleft/bracehtipdownright
{Ai } ×
~T A
B
/bracehtipdownleft/bracehtipupright/bracehtipupleft/bracehtipdownright
{Bi } ×
~T A
C
/bracehtipdownleft/bracehtipupright/bracehtipupleft/bracehtipdownright
{Ci } ×
~T A
V
/bracehtipdownleft/bracehtipupright/bracehtipupleft/bracehtipdownright
{vij }.
We will deﬁne Y : Conf ∗
3(G/N+) →T A
Q and a let M be in terms of Y .
Deﬁnition 5.18. Letk(i,j ) = i +rj. (This has the property that vij is the k(i,j )th vertex added to Q0 in
the algorithm of Section 5.2.) Alternately, the preﬁx of w−1
0 used to place vertex vij inQ0 via the algorithm
of [BFZ05, Section 2] has length (m + 1)−k, and is equal to wk(i,j) by Deﬁnition 2.18. Using Deﬁnition 2.16,
YA :α ↦→ {Ai = ∆ ωi(h1) }
YB :α ↦→ {Bi = ∆ ωi(h2) }
YC :α ↦→ {Ci = ∆ ωi(h3) }
YV :α ↦→ {vij = ∆ wk(i,j)ωi(u) }
Y :α ↦→YA(α) ⊕YB(α) ⊕YC (α) ⊕YV (α)
We then deﬁne a monomial map m :T A
Q →T A
Q (using Deﬁnitions 2.6 and 2.21) as
m :Ai ↦→Ai
m :Bi ↦→Bi
m :Ci ↦→Ci
m :vij ↦→vij · ∆ ωi (σG(h−1
1 )h2) · ∆
wk(i,j) ωi
⊕ (σG(h1))
We deﬁne M =m ◦Y .
Remark 5.19. The map M is a birational equivalence, following from [FZ99, Section 2.7].
29
~µP =µ



w4b,w3b,w2b,w1b,
w4a,w3a,w2a,w1a, w 4b,w3b,w2b,w1b,
w49,w39,w29,w19, w 4a,w3a,w2a,w1a, w 4b,w3b,w2b,w1b,
w48,w38,w28,w18, w 49,w39,w29,w19, w 4a,w3a,w2a,w1a, w 4b,w3b,w2b,w1b,
w47,w37,w27,w17, w 48,w38,w28,w18, w 49,w39,w29,w19, w 4a,w3a,w2a,w1a, w 4b,w3b,w2b,w1b,
w45,w35,w25,w15,
w44,w34,w24,w14, w 45,w35,w25,w15,
w43,w33,w23,w13, w 44,w34,w24,w14, w 45,w35,w25,w15,
w42,w32,w22,w12, w 43,w33,w23,w13, w 44,w34,w24,w14, w 45,w35,w25,w15,
w41,w31,w21,w11, w 42,w32,w22,w12, w 43,w33,w23,w13, w 44,w34,w24,w14, w 45,w35,w25,w15



~µFlipcore =µ



w1b,w2b,w3b,w4b,w1a,w2a,w3a,w4a,w19,w29,w39,w49,w18,w28,w38,w48,w17,w27,w37,w47,w16,w26,w36,w46,
w15,w25,w35,w45,w14,w24,w34,w44,w13,w23,w33,w43,w12,w22,w32,w42,w11,w21,w31,w41,
w1b,w2b,w3b,w4b,w1a,w2a,w3a,w4a,w19,w29,w39,w49,w18,w28,w38,w48,w17,w27,w37,w47,w16,w26,w36,w46,
w15,w25,w35,w45,w14,w24,w34,w44,w13,w23,w33,w43,w12,w22,w32,w42,
w1b,w2b,w3b,w4b,w1a,w2a,w3a,w4a,w19,w29,w39,w49,w18,w28,w38,w48,w17,w27,w37,w47,w16,w26,w36,w46,
w15,w25,w35,w45,w14,w24,w34,w44,w13,w23,w33,w43,
w1b,w2b,w3b,w4b,w1a,w2a,w3a,w4a,w19,w29,w39,w49,w18,w28,w38,w48,w17,w27,w37,w47,w16,w26,w36,w46,
w15,w25,w35,w45,w14,w24,w34,w44,
w1b,w2b,w3b,w4b,w1a,w2a,w3a,w4a,w19,w29,w39,w49,w18,w28,w38,w48,w17,w27,w37,w47,w16,w26,w36,w46,
w15,w25,w35,w45,
w1b,w2b,w3b,w4b,w1a,w2a,w3a,w4a,w19,w29,w39,w49,w18,w28,w38,w48,w17,w27,w37,w47,w16,w26,w36,w46,
w1b,w2b,w3b,w4b,w1a,w2a,w3a,w4a,w19,w29,w39,w49,w18,w28,w38,w48,w17,w27,w37,w47,
w1b,w2b,w3b,w4b,w1a,w2a,w3a,w4a,w19,w29,w39,w49,w18,w28,w38,w48,
w1b,w2b,w3b,w4b,w1a,w2a,w3a,w4a,w19,w29,w39,w49,
w1b,w2b,w3b,w4b,w1a,w2a,w3a,w4a,
w1b,w2b,w3b,w4b,



~µO3 =µ



w41,w42,w43,w44,w45,w46,w47,w48,w49,w4a,w4b,
w41,w42,w43,w44,w45,w46,w47,w48,w49,w4a,
w41,w42,w43,w44,w45,w46,w47,w48,w49,
w41,w42,w43,w44,w45,w46,w47,w48,
w41,w42,w43,w44,w45,w46,w47,
w41,w42,w43,w44,w45,w46,
w41,w42,w43,w44,w45,
w41,w42,w43,w44,
w41,w42,w43,
w41,w42,
w41,
w4b,w4a,w49,w48,w47,w46,w45,w44,w43,w42,w41,
w31,w32,w33,w34,w35,w36,w37,w38,w39,w3a,w3b,
w31,w32,w33,w34,w35,w36,w37,w38,w39,w3a,
w31,w32,w33,w34,w35,w36,w37,w38,w39,
w31,w32,w33,w34,w35,w36,w37,w38,
w31,w32,w33,w34,w35,w36,w37,
w31,w32,w33,w34,w35,w36,
w31,w32,w33,w34,w35,
w31,w32,w33,w34,
w31,w32,w33,
w31,w32,
w31,
w3b,w3a,w39,w38,w37,w36,w35,w34,w33,w32,w31,
w21,w22,w23,w24,w25,w26,w27,w28,w29,w2a,w2b,
w21,w22,w23,w24,w25,w26,w27,w28,w29,w2a,
w21,w22,w23,w24,w25,w26,w27,w28,w29,
w21,w22,w23,w24,w25,w26,w27,w28,
w21,w22,w23,w24,w25,w26,w27,
w21,w22,w23,w24,w25,w26,
w21,w22,w23,w24,w25,
w21,w22,w23,w24,
w21,w22,w23,
w21,w22,
w21,
w2b,w2a,w29,w28,w27,w26,w25,w24,w23,w22,w21,
w11,w12,w13,w14,w15,w16,w17,w18,w19,w1a,w1b,
w11,w12,w13,w14,w15,w16,w17,w18,w19,w1a,
w11,w12,w13,w14,w15,w16,w17,w18,w19,
w11,w12,w13,w14,w15,w16,w17,w18,
w11,w12,w13,w14,w15,w16,w17,
w11,w12,w13,w14,w15,w16,
w11,w12,w13,w14,w15,
w11,w12,w13,w14,
w11,w12,w13,
w11,w12,
w11,
w1b,w1a,w19,w18,w17,w16,w15,w14,w13,w12,w11,



,
~µO4=µ



w47,w48,w49,w4a,w4b,
w47,w48,w49,w4a,
w47,w48,w49,
w47,w48,
w47,
w4b,w4a,w49,w48,w47,
w37,w38,w39,w3a,w3b,
w37,w38,w39,w3a,
w37,w38,w39,
w37,w38,
w37,
w3b,w3a,w39,w38,w37,
w27,w28,w29,w2a,w2b,
w27,w28,w29,w2a,
w27,w28,w29,
w27,w28,
w27,
w2b,w2a,w29,w28,w27,
w17,w18,w19,w1a,w1b,
w17,w18,w19,w1a,
w17,w18,w19,
w17,w18,
w17,
w1b,w1a,w19,w18,w17,



~µO5=µ



w41,w42,w43,w44,w45,
w41,w42,w43,w44,
w41,w42,w43,
w41,w42,
w41,
w45,w44,w43,w42,w41,
w31,w32,w33,w34,w35,
w31,w32,w33,w34,
w31,w32,w33,
w31,w32,
w31,
w35,w34,w33,w32,w31,
w21,w22,w23,w24,w25,
w21,w22,w23,w24,
w21,w22,w23,
w21,w22,
w21,
w25,w24,w23,w22,w21,
w11,w12,w13,w14,w15,
w11,w12,w13,w14,
w11,w12,w13,
w11,w12,
w11,
w15,w14,w13,w12,w11,



Figure 24. The ﬂip for F4.
Example 5.20. Continuing from Example 5.16, let α = (h1,h 2,h 3,u ). Let hij = ∆ ωj (hi). Then YV
produces the following:
A1 =h11, A 2 =h12, ..., C 4 =h34, v 11 = ∆ w5ω1 (u), v 12 = ∆ w6ω2(u), ..., v 45 = ∆ w24ω4(u).
To compute the monomial map, refer to ﬁgure Figure 25. For exa mple, to calculate m(v23), we have i = 2,
so ∆ ωi(σG(h−1
1 )h2) = h22
h12
. For the second factor, k =k(2, 3) = 2 + 4 · 3 = 14 . Taking the numerator of the
i = 2,k = 14 entry gives t2
1t2, so ∆ w14ωi
⊕ (σG(h1)) = h2
11h12. This gives m(v23) = v23 · h22
h12
·h2
11h12, and M(α)
has v23 = ∆ w14ω2 (u) ·h2
11h22.
Repeating this for all others, M(α) has coordinates as given in Figure 26.
30
i 1 2 3 4 1 2 3 4 1 2 3 4
k = 1 1
t1
1
t2
1
t3
1
t4
9 t2
t3
t1t2
t3t4
t2
1t2
2
t2
3t4
t2
2
t3t4
17 t1t2
t3
t1t2
2
t3t4
t2
1t2
2
t3t4
t2
2
t3
2 t1
t2
1
t2
1
t3
1
t4
10 t1
t4
t1t2
t3t4
t2
1t2
2
t2
3t4
t2
2
t3t4
18 t2
t4
t1t2
2
t3t4
t2
1t2
2
t3t4
t2
2
t3
3 t1
t2
t1
t3
1
t3
1
t4
11 t1
t4
t2
1t2
t3t4
t2
1t2
2
t2
3t4
t2
2
t3t4
19 t2
t4
t1t2
t4
t2
1t2
2
t3t4
t2
2
t3
4 t1
t2
t1
t3
t2
1
t3t4
1
t4
12 t1
t4
t2
1t2
t3t4
t2
1t2
2
t3t2
4
t2
2
t3t4
20 t2
t4
t1t2
t4
t2
2
t4
t2
2
t3
5 t1
t2
t1
t3
t2
1
t3t4
t2
1
t3
13 t1
t4
t2
1t2
t3t4
t2
1t2
2
t3t2
4
t2
1
t4
21 t2
t4
t1t2
t4
t2
2
t4
t3
t4
6 t2
t3
t1
t3
t2
1
t3t4
t2
1
t3
14 t1t2
t3
t2
1t2
t3t4
t2
1t2
2
t3t2
4
t2
1
t4
22 t1 t1t2
t4
t2
2
t4
t3
t4
7 t2
t3
t1t2
t3t4
t2
1
t3t4
t2
1
t3
15 t1t2
t3
t1t2
2
t3t4
t2
1t2
2
t3t2
4
t2
1
t4
23 t1 t2
t2
2
t4
t3
t4
8 t2
t3
t1t2
t3t4
t2
1t2
2
t2
3t4
t2
1
t3
16 t1t2
t3
t1t2
2
t3t4
t2
1t2
2
t3t4
t2
1
t4
24 t1 t2 t3 t3
t4
Figure 25. For type F4, ∆ wkωi,wkωi(A) for abstract A =∏ r
i=1χ∗
i (ti).
A1 =h11 A2 =h12 A3 =h13 A4 =h14
B1 =h11 B2 =h12 B3 =h13 B4 =h14
C1 =h11 C2 =h12 C3 =h13 C4 =h14
v11 = ∆ w5ω1(u) ·h21 v21 = ∆ w6ω2(u) · h11h22
h12
v31 = ∆ w7ω3(u) · h2
11h23
h13
v41 = ∆ w8ω4(u) · h2
11h24
h14
v12 = ∆ w9ω1(u) · h12h21
h11
v22 = ∆ w10ω2(u) ·h11h22 v32 = ∆ w11ω3 (u) · h2
11h2
12h23
h13
v42 = ∆ w12ω4 (u) · h2
12h24
h14
v13 = ∆ w13ω1 (u) ·h21 v23 = ∆ w14ω2(u) ·h2
11h22 v33 = ∆ w15ω3 (u) · h2
11h2
12h23
h13
v43 = ∆ w16ω4 (u) · h2
11h24
h14
v14 = ∆ w17ω1 (u) ·h12h21 v24 = ∆ w18ω2(u) ·h11h12h22 v34 = ∆ w19ω3 (u) · h2
11h2
12h23
h13
v44 = ∆ w20ω4 (u) · h2
12h24
h14
v15 = ∆ w21ω1 (u) · h12h21
h11
v25 = ∆ w22ω2(u) ·h11h22 v35 = ∆ w23ω3 (u) · h2
12h23
h13
v45 = ∆ w24ω4 (u) · h13h24
h14
Figure 26. M(α) for type F4.
Remark 5.21. There is good reason to suspect that this construction is not unique up to mutation equivalency
of the quivers. It is certainly not unique if one relaxes the c onstruction of M as a monomial map applied
to generalized minors. For example, during our investigati on M was considered as Conf ∗
3(G/N+) × ⟨σG⟩ →
T A
Q × ⟨σG⟩, where µrot∗ acted by +1 on the second factor. An inﬁnite family of M maps were found,
depending on this factor of [τ ] ∈ ⟨σG⟩ to varying extent.
5.7. The signiﬁcance of the “twisting” mutations. The quiver mutations µrot and µﬂip are intended
to compose easily without requiring renaming the vertices o f the quiver. For example, µrot2(Q) should be
identical to µrot−1(Q).
Unfortunately, quiver mutations that yield equivalent see ds do not necessarily preserve the positions of
those seeds. For example, consider the classic “pentagon re currence”, which happens to be equivalent to ~µRS
on a row which is of Dynkin type A2. The switching of positions is exactly the the action of σA2 on the
Dynkin diagram.
31
x
v1
y
v2
1+y
x
v1
y
v2
1+y
x
v1
1+x+y
xy
v2
1+x
y
v1
1+x+y
xy
v2
x
v1
1+x
y
v2
1+x+y
xy
v1
1+x
y
v2
µ1 µ2 µ1
µ2 µ1
∼=
Figure 27. The pentagon recurrence.
The ~µOi parts of µrot and µﬂip , distinguishing them from µrotTw and µﬂipTw , are exactly to address
these actions of σG. If desired, shorter mutations may be used at the expense of s lightly more complicated
identiﬁcations between variables.
6. Construction for An
The An case was studied in detail in [GTZ15]. We merely restate the c onclusions in language consistent
with the above.
Remark 6.1. That the algorithm of Section 5 does not work for A2n can be seen in a few diﬀerent ways,
which are interconnected.
• There is no general formula for a Coxeter element c that yields a longest-word presentation w0 =
cc · · ·c.
• The Coxeter number for A2n is odd.
• The action of σG forA2n preserves no simple roots, therefore there can be no tree par titioning with
a unique root node.
Proposition 6.2. ForG of type An, Theorem 4.19 holds.
Proof. For the construction ofQ, take the quiver consisting of mutable vertices {vij : 1 ≤j ≤n, 1 ≤i ≤n −j }
and frozen vertices {Ai,B i,C i : 1 ≤i ≤n }, all of weight 1. We consider
Ai =v0,i, B i =vi,n+1−j, C i =vi,0.
The edges are given by
σ(a,b ) =



c(a,b ) a =vi,j,b =vi+1,j or a =vi,j,b =vi−1,j+1 or a =vi,j,b =vi,j−1
−c(a,b ) a =vi+1,j,b =vi,j or a =vi−1,j+1,b =vi,j or a =vi,j−1,b =vi,j
0 else,
and c(a,b ) is 1
2 if a and b are both Ais, both Bis, or both Cis, and is 1 otherwise.
The mutation µrot =µ { } is trivial.
Since the mutable portion of QAn is not rectangular, we need another convention for describi ng coordinates
of Q0– 2 in order to describe µﬂip . We present this by example in Figure 28. □
Mechanically, the inclusion of the left QAn intoQ0– 2 is the following:
Ai ↦→Di, B i ↦→Ei, C i ↦→wi,n, v i,j ↦→wi,j+n,
and for the right QAn intoQ0– 2, the following:
Ai ↦→wi,n, B i ↦→Fi, C i ↦→Gi, v i,j ↦→wj,n+1−i,
32
A1
A2
A3
C1 C2 C3
B1
B2
B3
v11
v12
v21
A1 A2 A3
C1
C2
C3
B1
B2
B3
v11
v12
v21
D1
D2
D3
E1
E2
E3 F1
F2
F3
G1
G2
G3
w15
w14
w24
w13
w23
w33
w11
w12
w22
Ψ −1
02
Figure 28. Quivers for type A3, also showing naming convention for Q0– 2.
The mutation µﬂip is then the “diamond sequence”:
t(ℓ,j ) = ℓ + 1
2 −
⏐⏐⏐⏐j − ℓ + 1
2
⏐⏐⏐⏐
~µRect(ℓ) =
ℓ∏
k=1
n−ℓ∏
j=0
µ
{
wt(ℓ,k)+j,2k+n−(ℓ+1)
}
µﬂip =
n∏
ℓ=1
~µRect(ℓ)
The map M is constructed as in Deﬁnition 5.18. Where needed, the prese ntation of the longest word is
given by
i = (1, 2,...,n, 1, 2,...,n − 1, ..., 1, 2, 1).
7. Proof of Theorem 4.19 for simple G

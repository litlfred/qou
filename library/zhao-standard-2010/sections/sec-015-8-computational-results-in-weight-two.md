---
doc_id: zhao-standard-2010
doc_title: "Standard Relations of Multiple Polylogarithm Values at Roots of Unity"
section_id: sec-015-8-computational-results-in-weight-two
section_title: "Computational results in weight two"
section_number: 8
pages: 21-29
source_pdf: Zhao_standard_2010.pdf
source_sha256: 94a70847c2937ba7
toc_source: inferred
doc_brief: "Standard Relations of Multiple Polylogarithm Values at Roots of Unity — Let N be a positive integer."
---
Computational results in weight two
In this section we combine the analysis in the previous sections and the theory
developed by Deligne and Goncharov [17] to present a detailed computation in
weight two and level N ≤169.
Let G := ι(Lie Uω) be the motivic fundamental Lie algebra (see [17, (5.12.2)])
associated to the motivic fundamental group of P1 −({0, ∞}∪µN). As pointed
out in §6.13 of op. cit. one may safely replace G(µN)(ℓ) by G throughout [20].
Then it follows from the proof of [17, 5.25] that if conjecture [17, 5.27(c)] is
true, which we assume in the following, then
d(2, N) = D(2, N) −dim ker(βN),
(38)
where βN : V2 G−1,−1 −→G−2,−2 is given by Ihara’s bracket βN(a∧b) = {a, b}
deﬁned by (5.13.6) of op. cit. Here G•,• is the associated graded of the weight
and depth gradings of G (see [20, §2.1]). Let k(N) := dim ker(βN). Then
δ1(N) := dim G−1,−1 =

1,
if N = 1 or 2;
ϕ(N)/2 + ν(N) −1,
if N ≥3,
(39)
by [20, Thm. 2.1]. Thus
i(N) := dim Im(βN) = δ1(N)(δ1(N) −1)/2 −k(N).
(40)
Documenta Mathematica 15 (2010) 1–34
22
Jianqiang Zhao
N
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
δ1
1
1
1
1
2
2
3
2
3
3
5
3
6
4
5
4
i
0
0
0
0
0
1
1
1
3
3
5
3
8
6
10
6
k
0
0
0
0
1
0
2
0
0
0
5
0
7
0
0
0
δ2
0
0
1
1
2
2
4
3
6
5
10
5
14
9
14
10
sr
0
0
1
1
2
2
4
4
6
6
10
8
14
12
16
16
D
1
2
4
4
9
8
16
9
16
15
36
15
49
24
35
25
SR
1
2
4
4
8
8
14
10
16
16
31
18
42
27
37
31
d
1
2
4
4
8
8
14
9
16
15
31
15
42
24
35
25
N
17
18
19
20
21
22
23
24
25
26
27
28
29
δ1
8
4
9
5
7
6
11
5
10
7
9
7
14
i
16
6
21
10
21
15
33
10
40
21
36
21
56
k
12
0
15
0
0
0
22
0
5
0
0
0
35
δ2
24
9
30
14
27
20
44
14
50
27
45
27
70
sr
24
18
30
24
32
30
44
32
50
42
54
48
70
D
81
24
100
35
63
48
144
35
121
63
100
63
225
SR
69
33
85
45
68
58
122
53
116
78
109
84
190
d
69
24
85
35
63
48
122
35
116
63
100
63
190
N
30
31
32
33
34
35
36
37
38
39
40
41
δ1
6
15
8
11
9
13
7
18
10
13
9
20
i
15
65
28
55
36
78
21
96
45
78
36
120
k
0
40
0
0
0
0
0
57
0
0
0
70
δ2
19
80
36
65
44
90
27
114
54
90
44
140
sr
48
80
64
80
72
96
72
114
90
112
96
140
D
47
256
81
143
99
195
63
361
120
195
99
441
SR
76
216
109
158
127
201
108
304
156
217
151
371
d
47
216
81
143
99
195
63
304
120
195
99
371
N
42
43
44
45
46
47
48
49
121
125
169
δ1
8
21
11
13
12
23
9
21
55
50
78
i
28
133
55
78
66
161
36
175
1155
1200
2288
k
0
77
0
0
0
92
0
35
330
25
715
δ2
34
154
65
90
77
184
44
196
1210
1250
2366
sr
96
154
120
144
132
184
128
196
1210
1250
2366
D
79
484
143
195
168
576
99
484
3136
2601
6241
SR
141
407
198
249
223
484
183
449
2806
2576
5526
d
79
407
143
195
168
484
99
449
2806
2576
5526
Table 1: Upper bounds of d(2, N) by the standard relations and [17, 5.25].
Documenta Mathematica 15 (2010) 1–34
Relations of Multiple Polylogarithm Values
23
Since dim G−2,−1 = ϕ(N)/2 if N > 2 and 0 otherwise the dimension of the
degree two part of G is
δ2(N) := dim G−2,−1 + dim G−2,−2 =

i(N),
if N = 1 or 2;
ϕ(N)/2 + i(N),
if N ≥3.
(41)
Let sr(N) be the upper bound of δ2(N) obtained by the standard relations.
This can be computed by the method described in [30, §2]. Let SR(N) be the
upper bound of d(2, N) similarly obtained by the standard relations. In Table
1 we use MAPLE to provide the following data: k(N), sr(N), and SR(N).
Then we can calculate δ1(N), i(N) and δ2(N) by (39), (40) (41), respectively.
From (38) we can check the consistency by verifying
sr(N) −δ2(N) = SR(N) −d(2, N) = SR(N) −D(2, N) + k(N)
which gives the number of linearly independent non-standard relations (as-
suming the conjecture in [17, 5.27(c)]). In Table 1 we provide some computa-
tional data of the above quantities. To save space we write D = D(2, N) and
d = d(2, N).
Definition 8.1. We call the level N standard if either (i) N = 1, 2 or 3, or
(ii) N is a prime power pn (p ≥5). Otherwise N is called non-standard.
Remark 8.2. We now make the following comments in the weight two case from
Table 1.
(a) When p ≥11 the vector space ker βp contains a subspace isomorphic to the
space of cusp forms of weight two on X1(p) which has dimension (p−5)(p−7)/24
(see [20, Lemma 2.3 & Theorem 7.8]). So it must contain another piece which
has dimension (p −3)/2 since dim(ker βp) = (p2 −1)/24 by [30, (6)]. One may
wonder if this missing piece has any signiﬁcance in geometry and/or number
theory.
(b) If N is a 2-power or a 3-power then D(2, N) should be sharp. See Re-
mark 5.4.
(c) If N has at least two distinct prime factors then D(2, N) seems to be sharp,
though we don’t have any theory to support it.
(d) Suppose the conjecture in [17, 5.27(c)] is true.
Then by [17, 5.27], (b)
and (c) is equivalent to saying that the kernel of βN is trivial if the level N is
non-standard. We believe this is also a necessary condition on N for βN to be
trivial.
(e) If the level N > 3 is standard then βN is unlikely to be injective. We con-
jecture that non-standard relation doesn’t exist (i.e., SR(N) is sharp), though
for prime power levels we only have veriﬁed this for the ﬁrst four prime square
levels N = 52, 72, 112, 132, and the ﬁrst cubic power level N = 53.
The equation dim βp = (p2 −1)/24 (see [30, (6)]) together with Theorem 8.6
conﬁrms Remark 8.2(e) for prime levels if we assume a variant of Grothendieck’s
period conjecture [17, 5.27(c)].
The next result partially conﬁrms Remark
8.2(e) in the case when the level is a prime square.
Documenta Mathematica 15 (2010) 1–34
24
Jianqiang Zhao
Theorem 8.3. If p ≥5 is a prime then ker βp2̸ = 0 and
d(2, p2) < D(2, p2) = (p2 −p + 2)2/4.
Proof. By the proof of Delign-Goncharov’s bound D(2, p2) in [17, 5.25] we only
need to show ker βp2̸ = 0. In the following we adopt the same notation as in
[17] and [30].
Fix a primitive p2th root of unity µ. Put e(a) = eµa for all integer a. Deﬁne
gk,j = e(pk + j) + e(p2 −pk −j) + e(pj) + e(p2 −pj)
for 0 ≤k < (p −1)/2, 1 ≤j ≤p −1, and for k = (p −1)/2, 1 ≤j ≤(p −1)/2.
One only needs to prove the following
Claim. Let h = (p −3)/2. Then one has
h
X
k=0
h
X
l=k
p−2
X
j=2
{gk,1, gl,j} +
h+1
X
k=0
h+1
X
j=2
{gk,1, gh+1,j}
+
h
X
k=0
h
X
l=k+1
p−2
X
j=2
{gk,p−1, gl,j} +
h
X
k=0
h+1
X
j=2
{gk,p−1, gh+1,j}
−
h
X
k=0
h
X
l=k
p−2
X
j=2
{gk,j, gl,p−1} −
h
X
k=0
h
X
l=k
p−2
X
j=2
{gk,j, gl+1,1} = 0.
There are h(2h + 3)2 = hp2 distinct terms on the left, each with coeﬃcient ±1.
The proof of the claim is straight-forward by a little tedious change of indices
and regrouping.
−
h
X
k=0
h
X
l=k
p−2
X
j=2
{gk,j, gl+1,1} =
h
X
k=0
k
X
l=0
p−2
X
j=2
{gk+1,1, gl,j} =
h+1
X
k=1
k−1
X
l=0
p−2
X
j=2
{gk,1, gl,j}.
Then the expression in the claim becomes
h
X
k=1
h
X
l=0
p−2
X
j=2
{gk,1, gl,j} +
h
X
l=0
p−2
X
j=2
{g0,1, gl,j} +
h
X
l=0
p−2
X
j=2
{gh+1,1, gl,j}
+
h+1
X
k=0
h+1
X
j=2
{gk,1, gh+1,j} +
h
X
k=0
h
X
l=0
p−2
X
j=2
{gk,p−1, gl,j} +
h
X
k=0
h+1
X
j=2
{gk,p−1, gh+1,j}
=
h+1
X
k=0
h
X
l=0
p−2
X
j=2
{gk,1, gl,j} +
h+1
X
k=0
h+1
X
j=2
{gk,1, gh+1,j}
+
h
X
k=0
h
X
l=0
p−2
X
j=2
{gk,p−1, gl,j} +
h
X
k=0
h+1
X
j=2
{gk,p−1, gh+1,j}.
Let us write {a, b} = {e(a), e(b)}. By deﬁnition
Documenta Mathematica 15 (2010) 1–34
Relations of Multiple Polylogarithm Values
25
{gk,1, gl,j}
={pk + 1, pl + j} + {−pk −1, pl + j} + {p, pl + j} + {−p, pl + j}
+{pk + 1, −pl −j} + {−pk −1, −pl −j} + {p, −pl −j} + {−p, −pl −j}
+{pk + 1, pj} + {−pk −1, pj} + {p, pj} + {−p, pj}
+{pk + 1, −pj} + {−pk −1, −pj} + {p, −pj} + {−p, −pj}
={pk + 1, pl + j} + {p(p −k) −1, pl + j} + {p, pl + j} + {−p, pl + j}
+{pk + 1, p(p −1 −l) + p −j} + {p(p −k) −1, p(p −1 −l) + p −j}
+ {p, p(p −1 −l) + p −j} + {−p, p(p −1 −l) + p −j}
+{pk + 1, pj} + {p(p −k) −1, pj} + {p, pj} + {−p, pj}
+{pk + 1, p(p −j)} + {p(p −k) −1, p(p −j)}+{p, p(p −j)}+{−p, p(p −j)}.
Then
h+1
X
k=0
h
X
l=0
p−2
X
j=2
{gk,1, gl,j} =
h+1
X
k=0
h
X
l=0
p−2
X
j=2
{pk + 1, pl + j} + {p(p −k) −1, pl + j}
+{pk + 1, p(p −1 −l) + j} + {p(p −k) −1, p(p −1 −l) + j}
+{p, pl + j} + {−p, pl + j} + {p, p(p −1 −l) + j} + {−p, p(p −1 −l) + j}
+2{pk + 1, pj} + 2{p(p −k) −1, pj} + 2{p, pj} + 2{−p, pj}
=
h+1
X
k=0
p−1
X
l=0,l̸=h+1
p−2
X
j=2
{pk + 1, pl + j} +
p
X
k=h+2
p−1
X
l=0,l̸=h+1
p−2
X
j=2
{pk −1, pl + j}
+
h+1
X
k=0
p−1
X
l=0,l̸=h+1
p−2
X
j=2

{p, pl + j} + {−p, pl + j}

+ 2(h + 1)
h+1
X
k=0
p−2
X
j=2
{pk + 1, pj}
+2(h + 1)
p
X
k=h+2
p−2
X
j=2
{pk −1, pj} + 2(h + 2)(h + 1)
p−2
X
j=2

{p, pj} + {−p, pj}

.
Thus
h+1
X
k=0
h
X
l=0
p−2
X
j=2
{gk,1, gl,j} +
h+1
X
k=0
h+1
X
j=2
{gk,1, gh+1,j}
=
h+1
X
k=0
p−1
X
l=0
p−2
X
j=2
{pk + 1, pl + j} +
p
X
k=h+2
p−1
X
l=0
p−2
X
j=2
{pk −1, pl + j}
+p + 1
2
p−1
X
l=0
p−2
X
j=2

{p, pl + j} + {−p, pl + j}

+ p
h+1
X
k=0
p−2
X
j=2
{pk + 1, pj}
+p
p
X
k=h+2
p−2
X
j=2
{pk −1, pj} + p(p + 1)
2
p−2
X
j=2

{p, pj} + {−p, pj}

.
Documenta Mathematica 15 (2010) 1–34
26
Jianqiang Zhao
Similarly,
h
X
k=0
h
X
l=0
p−2
X
j=2
{gk,p−1, gl,j} +
h
X
k=0
h+1
X
j=2
{gk,p−1, gh+1,j}
=
h+1
X
k=1
p−1
X
l=0
p−2
X
j=2
{pk −1, pl + j} +
p−1
X
k=h+2
p−1
X
l=0
p−2
X
j=2
{pk + 1, pl + j}
+p −1
2
p−1
X
l=0
p−2
X
j=2

{p, pl + j} + {−p, pl + j}

+ p
h+1
X
k=1
p−2
X
j=2
{pk −1, pj}
+p
p−1
X
k=h+2
p−2
X
j=2
{pk + 1, pj} + p(p −1)
2
p−2
X
j=2

{p, pj} + {−p, pj}

.
Altogether the expression in the claim is reduced to
X :=
p−1
X
k=0
p−1
X
l=0
p−2
X
j=2
{pk + 1, pl + j} +
p
X
k=1
p−1
X
l=0
p−2
X
j=2
{pk −1, pl + j}
+p
p−1
X
l=0
p−2
X
j=2

{p, pl + j} + {−p, pl + j}

+ p
p−1
X
k=0
p−2
X
j=2
{pk + 1, pj}
+p
p
X
k=1
p−2
X
j=2
{pk −1, pj} + p2
p−2
X
j=2

{p, pj} + {−p, pj}

.
To see this last expression can be reduced to 0 we recall that by deﬁnition [17,
(5.13.6)]
{a, b} = {ea, eb} = [ea, eb] + ∂a(eb) −∂b(ea),
where ∂a is the derivation deﬁned by ∂a(e0) = 0 and ∂a(eζ) = [−[ζ](ea), eζ]
for any p2th root of unity ζ (see [17, (5.13.4)]). Thus by abuse of notation
[x, y] = [e(x), e(y)] we get
X =
p−1
X
k=0
p−1
X
l=0
p−2
X
j=2

[pk + 1, pl + j] −[p(k + l) + j + 1, pl + j]
+ [p(k + l) + j + 1, pk + 1]

(42)
+
p
X
k=1
p−1
X
l=0
p−2
X
j=2

[pk −1, pl + j] −[p(k + l) + j −1, pl + j]
+ [p(k + l) + j −1, pk −1]

(43)
+p
p−1
X
l=0
p−2
X
j=2

[p, pl + j] −[p(l + 1) + j, pl + j] + [p(l + 1) + j, p]
Documenta Mathematica 15 (2010) 1–34
Relations of Multiple Polylogarithm Values
27
+[−p, pl + j] −[p(l −1) + j, pl + j] + [p(l −1) + j, −p]

(44)
+p
p−1
X
k=0
p−2
X
j=2

[pk + 1, pj] −[p(j + k) + 1, pj] + [p(j + k) + 1, pk + 1]

(45)
+p
p
X
k=1
p−2
X
j=2

[pk −1, pj] −[p(j + k) −1, pj] + [p(j + k) −1, pk −1]

(46)
+p2
p−2
X
j=2

[p, pj] −[p(j + 1), pj] + [p(j + 1), p] + [−p, pj]
−[p(j −1), pj] + [p(j −1), −p]

.
(47)
Now by skew-symmetry of Lie bracket
(42) + (43)
=
p−1
X
k=0
p−1
X
l=0
p−2
X
j=2
[pk + 1, pl + j] +
p−1
X
k=0
p−1
X
l=0
p−2
X
j=2
[pk + j, pl + j + 1]
−
p−1
X
k=0
p−1
X
l=0
p−1
X
j=3
[pk + 1, pl + j] +
p
X
k=1
p−1
X
l=0
p−2
X
j=2
[pk −1, pl + j]
−
p
X
k=1
p−1
X
l=0
p−3
X
j=1
[p(k + l) + j, pl + j + 1] +
p
X
k=1
p−1
X
l=0
p−3
X
j=1
[pl + j, pk −1]
=
p−1
X
k=0
p−1
X
l=0
[pk + 1, pl + 2] +
p−1
X
k=0
p−1
X
l=0
[pk + p −2, pl + p −1]
−
p−1
X
k=0
p−1
X
l=0
[pk + 1, pl + p −1] +
p
X
k=1
p−1
X
l=0
[pk −1, pl + p −2]
−
p
X
k=1
p−1
X
l=0
[pk + 1, pl + 2] +
p
X
k=1
p−1
X
l=0
[pl + 1, pk −1] = 0.
Similarly we can easily ﬁnd that (44) = (45) = (46) = (47) = 0. This ﬁnishes
the proof of the theorem.
Remark 8.4. The theorem corrects a misprint in the statement of [30, Thm. 2].
In the three cases (w, N) = (2, 8), (2, 10) and (2, 12) we see that SR(N) >
d(w; N) = D(w; N). By numerical computation we have
Conjecture 8.5. We have
d(2, 8) = 9,
d(2, 10) = d(2, 12) = 15,
Documenta Mathematica 15 (2010) 1–34
28
Jianqiang Zhao
and the following relations are the linearly independent non-standard relations:
let LN(−) = LN(1, 1|−) and L(2)
N (−) = LN(2|−), then
37L8(1, 1) =34L(2)
8 (5) + 112L8(3, 1) + 11L8(3, 0) + 37L(2)
8 (1) −2L8(2, 6)
+ 3L8(7, 3) −111L8(5, 7) + 38L8(7, 7) −8L8(5, 5),
(48)
7L10(5, 2) =72L(2)
10 (1) + 265L(2)
10 (7) −7L10(2, 5) + 64L10(9, 8) + 14L10(5, 6)
−467L10(4, 2) + 467L10(8, 6) −164L10(9, 4) + 166L10(7, 9)
−260L10(8, 1) −66L10(3, 9) −7L10(6, 9) + 7L10(6, 5).
(49)
L12(8, 7) =5L(2)
12 (5) + 8L12(8, 10) −6L12(10, 11) −8L12(9, 11) + L12(10, 9)
−15L12(8, 1) + 5L12(9, 10) + 5L12(6, 1) −L12(1, 1)
+ 6L12(8, 11) −11L12(6, 11) + 8L12(8, 3) −L12(11, 8),
(50)
60L12(8, 11) =38L12(8, 7) + 348L12(10, 11) + 502L12(9, 11)
−492L12(10, 9) + 600L12(8, 1) −552L12(9, 10)
−154L12(11, 10) + 20L12(6, 1) + 261L12(6, 11)
−502L12(8, 3) + 221L12(11, 8) −319L12(8, 10),
(51)
221L12(1, 1) =1854L12(8, 10) + 562L12(8, 7) −1018L12(10, 11)
−2416L12(9, 11) + 319L12(10, 9) −4270L12(8, 1)
+ 2293L12(9, 10) + 956L12(11, 10) + 1110L12(6, 1)
+ 2416L12(8, 11) −3305L12(6, 11) + 2416L12(8, 3).
(52)
When N is a non-standard level we ﬁnd that very often there are non-standard
relations among MPVs. For examples, the ﬁve relations in Conjecture 8.5 are
discovered only through numerical computation. On the other hand, we expect
that the standard relations are enough to produce all the linear relations when
N is standard. In weight two, when N is a prime the answer is conﬁrmed by
the next theorem if one assumes a variant of Grothendieck’s period conjecture.
Computations above provided the primary motivation of this result at the
initial stage of this work.
Theorem 8.6. ([30]) Let p ≥5 be a prime. Then
d(2, p) ≤(5p + 7)(p + 1)
24
.
If the conjecture in [17, 5.27(c)] is true then the equality holds and the standard
relations in MPV(2, p) imply all the others.
Proof. See the proof of [30, Thm. 1].
It follows from [30, (6)] that the kernel βp has dimension
k(p) = p2 −1
24
for all prime p ≥5. From the data in Table 1 we have
Documenta Mathematica 15 (2010) 1–34
Relations of Multiple Polylogarithm Values
29
Conjecture 8.7. (a) For all prime p ≥5 kernel βp2 has dimension
k(p2) = p(p −1)(p −2)(p −3)
24
.
As a consequence, the upper bound of d(2, p2) produced by the standard relations
is
d(2, p2) ≤5p4 −6p3 + 19p2 −18p + 24
24
.
(b) The standard relations produce all the linear relations and the upper bound
in (a) is sharp.
Conjecture 8.8. (a) For all prime p ≥5 kernel βp3 has dimension
k(p3) = p2(p −1)(p −2)(p −3)(p −4)
24
.
As a consequence, the upper bound of d(2, p3) produced by the standard relations
is
d(2, p3) ≤5p6 −2p5 −29p4 + 74p3 −48p2 + 24
24
.
(b) The standard relations produce all the linear relations and the upper bound
in (a) is sharp.

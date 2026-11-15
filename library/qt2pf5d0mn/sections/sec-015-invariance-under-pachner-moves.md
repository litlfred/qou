---
doc_id: qt2pf5d0mn
doc_title: "UC Santa Barbara"
section_id: sec-015-invariance-under-pachner-moves
section_title: "Invariance under Pachner Moves"
section_number: null
pages: 83-100
source_pdf: qt2pf5d0mn.pdf
source_sha256: 4c8581c3b46398e3
toc_source: outline
doc_brief: "UC Santa Barbara — 19 sections: Front matter; Abstract; Introduction"
---
Ik
I′
k
k = 4
02345
01245
01234
12345
01345
01235
k = 3
0124
0234
0245
0135
1235
1345
k = 2
024
135
Table 4.1: Comparison of T and T ′ for 3-3 move
pachner move. The typical pachner moves for n = 4 are as follows:
(02345)(01245)(01234)
(3,3)
←→
(12345)(01345)(01235)
(02345)(01245)(01234)(12345)
(2,4)
←→
(01345)(01235)
(02345)(01245)(01234)(12345)(01345)
(1,5)
←→
(01235)
4.4
Invariance under Pachner Moves
We prove that the partition function ZD(M; T ) deﬁned in Section 3.1 is invariant
under pachner moves. Since in Section 4.2 it has been shown that ZD(M; T ) does not
depend on the ordering of the vertices, we only need to consider typical pachner moves
of types 3-3, 2-4, and 1-5. Let T , T ′ be two ordered triangulations whose vertices are
ordered in such a way that they only diﬀer by a typical pachner move. In each of the
cases, let Ik = T k \ (T ′)k be the set of k-simplices which belong to T but not T ′, and
similarly let I′
k = (T ′)k \ T k. Tables 4.1, 4.2, and 4.3 list the diﬀerences between T and
T ′ corresponding to each typical pachner move 3-3, 2-4, and 1-5, respectively. Without
loss of generality, assume the 4-simplices 02345, 01245, 01234 in T are positive, while
12345, 01345, 01235 in T ′ are positive. Thus if any of 12345, 01345, 01235 are in T , they
must be negative.
By a complete set of representatives we mean a set of objects which contains exactly
74
Section 4.4
Invariance under Pachner Moves
Ik
I′
k
k = 4
02345
01245
01234
01345
01235
12345
k = 3
0124
0234
0245
0135
2345
1245
1234
k = 2
024
245
234
124
k = 1
24
Table 4.2: Comparison of T and T ′ for 2-4 move
Ik
I′
k
k = 4
02345
01245
01234
12345
01235
01345
k = 3
0124
0234
0245
2345
1245
1234
0134
0145
1345
0345
k = 2
024
245
234
124
034
014
134
045
145
345
k = 1
24
04
14
34
45
k = 0
4
Table 4.3: Comparison of T and T ′ for 1-5 move
75
Section 4.4
Invariance under Pachner Moves
one representative for each isomorphism class of simple objects. For the rest of the section,
a summation variable concerning simple objects in the category is always assumed to run
through an arbitrary complete set of representatives, unless otherwise stated. Recall that
an extended coloring is a map ˆF = (g, f, t), which assigns a group element to each 1-
simplex, an isomorphism class of simple objects to each 2-, and 3-simplex, such that these
assignments satisfy some restrictions, see Deﬁnition 3.1.6. Then to deﬁne the partition
function, a representative is arbitrarily chosen for each 2- and 3-simplex with an extended
coloring. The partition function is a sum over all extended colorings, see Equation 3.3.
In light of the observations above, we can rephrase the deﬁnition of the partition function
as follows.
We let each 1-simplex run through the set of all elements in G, and let each 2-, 3-
simplex run through an arbitrary complete set of representatives (i.e., each 2-, 3-simplex
has its own complete set). Then an extended coloring can be viewed as a choice of value
for 1-, 2-, and 3-simplices, so that the resulting conﬁguration satisﬁes the restriction in
Deﬁnition 3.1.6. If a conﬁguration is not an extended coloring, we set its contribution to
zero. As before, we denote the color of a simplex by the simplex itself. Then Equation
3.3 can be rewritten as Equation 4.25, where we have omitted the dependence of ˆZϵ(σ)(σ)
ˆF.
ZD(M; T ) =
X
T 1,T 2,T 3
(D2/|G|)|T 0|
(D2)|T 1|
Q
α∈T 2 dα
Q
τ∈T 3 dτ
Y
σ∈T 4
ˆZϵ(σ)(σ)
(4.25)
By Equation 4.25, to prove ZD(M; T ) = ZD(M; T ′), it suﬃces to show that Equa-
tions 4.26, 4.27, and 4.28 hold, corresponding to the typical pachner move 3-3, 2-4, 1-5,
respectively, where all simplices which do not present among the summation are assumed
to have a ﬁxed coloring on them.
76
Section 4.4
Invariance under Pachner Moves
X
I2,
I3
d024
d0124d0234d0245
ˆZ+(01234) ˆZ+(01245) ˆZ+(02345)
=
X
I′
2,
I′
3
d135
d0135d1235d1345
ˆZ+(01235) ˆZ+(01345) ˆZ+(12345)
(4.26)
X
I1,
I2,
I3
1
D2
Q
α∈I2
dα
Q
τ∈I3
dτ
ˆZ+(01234) ˆZ+(01245) ˆZ+(02345) ˆZ−(12345)
=
X
I′
3
1
d0135
ˆZ+(01235) ˆZ+(01345)
(4.27)
X
I0,I1,I2,I3
(D2/|G|)|I0|
(D2)|I1|
Q
α∈I2
dα
Q
τ∈I3
dτ
ˆZ+(01234) ˆZ+(01245) ˆZ+(02345) ˆZ−(12345) ˆZ−(01345)
= ˆZ+(01235)
(4.28)
The above three equations are to be proved in Section 4.4.1, 4.4.2, and 4.4.3, respec-
tively. In the proof, the following simple lemmas will be heavily used. For the section of
invariance proof under pachner moves, we take one more convention that all diagrams of
morphisms in ﬁgures are assumed to have their top and bottom identiﬁed, namely, the
diagrams in ﬁgures are actually the trace of the morphisms drawn.
Lemma 4.4.1 (Merging Formula) Let A, B be two objects of D, and {eA,B,i : i ∈
I}, {eB,A,j : j ∈I} be a basis of Hom(A, B) and Hom(B, A), respectively, such that
⟨eA,B,i, eB,A,j⟩= αiδi,j, then for F ∈Hom(A, B), G ∈Hom(B, A), we have ⟨G, F⟩=
77
Section 4.4 Invariance under Pachner Moves

Figure 4.8: Trace Identity (2)

~ AG, e4,2,) (F. en,ai). Specifically, the following special examples will be used in the
ier *
invariance proof.

1. Let F € Hom(a®@ b,c @ d), G € Hom(c@ d,a® b), then

1 B x
(GF) = 30 (PF, Bina) (Gs Bixea):

2. Let F € Hom(a@b@c,d®e® f), Ge Hom(d®e® f,a®b@c), then

d, a E
(GF) =) FAP. (Id ® Bb) © (Binge ® 1))(G, (Bine ® Id) 0 (Id ® Bh, 9).
vey

The identities in Part 1 and Part 2 are also illustrated in Figure and Figure
respectively.

Lemma 4.4.2 Let g,g' € G and a,b,c,d,e be simple objects of D such that a® b € Cog,

then the equality is Figure [4.9 holds.
78
Section 4.4
Invariance under Pachner Moves
P
c∈Cg,d∈Cg′,
e∈Cgg′
dcdd
de
a
b
c
d
e
c
d
a
b
e
=
D2
|G|
a
a
b
b
Figure 4.9: Dimension Identity
Proof:
LHS =
X
c,d,e
dcdd
de
N e
cdBe
ab,ab
=
X
e∈Cgg′
X
c∈Cg
dc
de
Be
ab,ab
X
d∈Cg′
dd∗N d∗
e∗c
=
X
e∈Cgg′
X
c∈Cg
d2
cde∗
de
Be
ab,ab
=
X
e∈Cgg′
D2
|G|Be
ab,ab
= D2
|G|Ida⊗b
4.4.1
Invariance under 3-3 move
In this subsection and the next two subsections, picture calculus is used heavily. For
the partition functions deﬁned in Figure 3.3, we will omit the labels on 2-simplices, and
only keep those on 3-simplices. Given a colored 3-simplex (0123), we will use the the
short notation illustrated in Figure 4.10. From this notation, it is direct to work out the
color of each edge in the ﬁgures representing partition functions. The idea of proof is to
express each side of the equation as a weighted sum of diagrams, combine these diagrams
into one using the Merging Formula, and show that the resulting diagrams for two side
of the equation are homotopic and thus represent the same morphism.
Proposition 4.4.3 Let T , T ′ be two ordered triangulations which diﬀer by a typical 3-3
79
Section 4.4
Invariance under Pachner Moves
0123
−
+
=
023
012
23
013
123
0123
0123
+
−
=
013
123
023
012
23
0123
Figure 4.10: Short notations for basis elements
pachner move, see Table 4.1 for their comparison. Then the identity in Equation 4.26
holds, assuming all simplices which do not present among the summation variables have
been assigned a ﬁxed coloring.
Proof:
The proof is best illustrated using picture calculus and Lemma 4.4.1. Note
that the top and bottom of each diagram (see below) are identiﬁed, so within each
diagram morphisms are cyclically ordered, namely, one can move a morphism on the
bottom to the top and vice versa. Also, the summation terms are written below the
diagrams. It is direct to check that the ﬁnal diagrams in both LHS and RHS represent
the same morphism, which justiﬁes the equation.
Below we give a brief explanation of each “= ” sign.
LHS:
1 By deﬁnition.
2 Apply 45 to the ﬁrst diagram. Move the top two morphisms involving 0245, 0234
in the third diagram to the bottom.
3 Apply Lemma 4.4.1 to the second and third diagram.
4 Isotope the second diagram.
5 Apply Lemma 4.4.1.
RHS:
1 By deﬁnition.
80
Section 4.4
Invariance under Pachner Moves
2 Apply Lemma 4.4.1 to the ﬁrst and third diagram.
3 Apply Lemma 4.4.1 to the two diagrams.
4 Isotope the diagram. Note that the group element acting on 0123 changes from 35
to 45 34 due to braiding.
81
Section 4.4
Invariance under Pachner Moves
LHS 1=
P
I2,I3
d024
d0124d0234d0245
P
I2,I3
d024
d0124d0234d0245
0234
−
+
0124
−
+
1234
+
−
0134
+
−
0123
34
+
−
0245
−
+
0125
−
+
1245
+
−
0145
+
−
0124
45
+
−
0345
−
+
0235
−
+
2345
+
−
0245
+
−
0234
45
+
−
2=
0234
45
−
+
0124
45
−
+
1234
45
+
−
0134
45
+
−
0123
+
−
45 34
0245
−
+
0125
−
+
1245
+
−
0145
+
−
0124
45
+
−
0245
+
−
0234
45
+
−
0345
−
+
0235
−
+
2345
+
−
3=
P
024,0124,0234
d024
d0124d0234
P
024,0124,0234
d024
d0124d0234
0234
45
−
+
0124
45
−
+
1234
45
+
−
0134
45
+
−
0123
+
−
45 34
0125
−
+
1245
+
−
0145
+
−
0124
45
+
−
0234
45
+
−
0345
−
+
0235
−
+
2345
+
−
4=
0234
45
−
+
0124
45
−
+
1234
45
+
−
0134
45
+
−
0123
+
−
45 34
0125
−
+
1245
+
−
0145
+
−
0124
45
+
−
0234
45
+
−
0345
−
+
0235
−
+
2345
+
−
5=
0125
−
+
1245
+
−
0145
+
−
1234
45
+
−
0134
45
+
−
0123
+
−
45 34
0345
−
+
0235
−
+
2345
+
−
82
Section 4.4
Invariance under Pachner Moves
RHS 1=
P
I′
2,I′
3
d135
d0135d1235d1345
0235
−
+
0125
−
+
1235
+
−
0135
+
−
0123
35
+
−
0345
−
+
0135
−
+
1345
+
−
0145
+
−
0134
45
+
−
1345
−
+
1235
−
+
2345
+
−
1245
+
−
1234
45
+
−
2=
P
135,0135,1345
d135
d0135d1345
0235
−
+
0125
−
+
2345
+
−
1245
+
−
1234
45
+
−
1345
−
+
0135
+
−
0123
35
+
−
0345
−
+
0135
−
+
1345
+
−
0145
+
−
0134
45
+
−
3=
0235
−
+
0125
−
+
2345
+
−
1245
+
−
1234
45
+
−
0145
+
−
0134
45
+
−
0345
−
+
0123
35
+
−
4=
0235
−
+
0125
−
+
2345
+
−
1245
+
−
1234
45
+
−
0145
+
−
0134
45
+
−
0345
−
+
0123
+
−
45 34
83
Section 4.4
Invariance under Pachner Moves
4.4.2
Invariance under 2-4 move
Proposition 4.4.4 Let T , T ′ be two ordered triangulations which diﬀer by a typical 2-4
pachner move, see Table 4.2 for their comparison. Then the identity in Equation 4.27
holds, assuming all simplices which do not present among the summation variables have
been assigned a ﬁxed coloring.
Proof:
LHS:
1 By deﬁnition.
2 Use the result of the LHS in the proof of Equation 4.26.
3 Apply Lemma 4.4.1 to the two diagrams.
4 Move the morphism involving 2345 and the braiding above it from the top to the
bottom.
5 Isotope the diagram.
6 Apply Lemma 4.4.2. Note that after summing over the variables 245, 234, 2345, the
factor remained is
1
|G|, which is cancelled with the variable 24.
RHS:
1 By deﬁnition.
2 Move the morphism involving 0123 in the ﬁrst diagram from the top to the bottom.
3 Apply Lemma 4.4.1 to the two diagrams.
4 Isotope the diagram.
5 Isotope the diagram.
84
Section 4.4
Invariance under Pachner Moves
LHS 1=
P
I1,I2,I3
1
D2
Q
α∈I2
dα
Q
τ∈I3
d−1
τ
P
24
245,234,124
2345,1245,1234
1
D2
d245d234d124
d2345d1245d1234
0234
−
+
0124
−
+
1234
+
−
0134
+
−
0123
34
+
−
0245
−
+
0125
−
+
1245
+
−
0145
+
−
0124
45
+
−
0345
−
+
0235
−
+
2345
+
−
0245
+
−
0234
45
+
−
1234
45
−
+
1245
−
+
2345
−
+
1235
+
−
1345
+
−
2=
0125
−
+
1245
+
−
0145
+
−
1234
45
+
−
0134
45
+
−
0123
+
−
45 34
0345
−
+
0235
−
+
2345
+
−
1234
45
−
+
1245
−
+
2345
−
+
1235
+
−
1345
+
−
3=
85
Section 4.4
Invariance under Pachner Moves
P
24
245,234
2345
1
D2
d245d234
d2345
P
24
245,234
2345
1
D2
d245d234
d2345
P
24
245,234
2345
1
D2
d245d234
d2345
0125
−
+
2345
−
+
1235
+
−
1345
+
−
0145
+
−
0134
45
+
−
0123
+
−
4534
0345
−
+
0235
−
+
2345
+
−
4=
2345
+
−
0125
−
+
2345
−
+
1235
+
−
1345
+
−
0145
+
−
0134
45
+
−
0123
+
−
45 34
0345
−
+
0235
−
+
5=
2345
+
−
2345
−
+
0125
−
+
1235
+
−
1345
+
−
0145
+
−
0134
45
+
−
0123
+
−
45 34
0345
−
+
0235
−
+
6=
0125
−
+
1235
+
−
1345
+
−
0145
+
−
0134
45
+
−
0123
+
−
4534
0345
−
+
0235
−
+
86
Section 4.4
Invariance under Pachner Moves
RHS 1=
P
0135
1
d0135
P
0135
1
d0135
0235
−
+
0125
−
+
1235
+
−
0135
+
−
0123
35
+
−
0345
−
+
0135
−
+
1345
+
−
0145
+
−
0134
45
+
−
2=
0123
35
+
−
0235
−
+
0125
−
+
1235
+
−
0135
+
−
0345
−
+
0135
−
+
1345
+
−
0145
+
−
0134
45
+
−
3=
0345
−
+
0123
35
+
−
0235
−
+
0125
−
+
1235
+
−
1345
+
−
0145
+
−
0134
45
+
−
4=
0345
−
+
0123
35
+
−
0235
−
+
0125
−
+
1235
+
−
1345
+
−
0145
+
−
0134
45
+
−
5=
0345
−
+
0123
35
+
−
0235
−
+
0125
−
+
1235
+
−
1345
+
−
0145
+
−
0134
45
+
−
87
Section 4.4
Invariance under Pachner Moves
4.4.3
Invariance under 1-5 move
Proposition 4.4.5 Let T , T ′ be two ordered triangulations which diﬀer by a typical 1-5
pachner move, see Table 4.3 for their comparison. Then the identity in Equation 4.28
holds, assuming all simplices which do not present among the summation variables have
been assigned a ﬁxed coloring.
Proof:
LHS:
1 By deﬁnition.
2 Use the result of the LHS in the proof of Equation 4.27.
3 Apply Lemma 4.4.1 to the two diagrams.
4 Apply Lemma 4.4.2.
5 The strand labeled by 345 can be isotoped to an isolated loop, and thus it con-
tributes a factor d345.
Note that the resulting diagram is equal to the RHS of
Equation 4.28 after a cyclic shift of morphisms.
88
Section 4.4
Invariance under Pachner Moves
LHS 1=
P
I1,I2,I3
D2
|G|
1
(D2)|I1|
Q
α∈I2
dα
Q
τ∈I3
d−1
τ
0234
−
+
0124
−
+
1234
+
−
0134
+
−
0123
34
+
−
0245
−
+
0125
−
+
1245
+
−
0145
+
−
0124
45
+
−
0345
−
+
0235
−
+
2345
+
−
0245
+
−
0234
45
+
−
1234
45
−
+
1245
−
+
2345
−
+
1235
+
−
1345
+
−
0134
45
−
+
0145
−
+
1345
−
+
0135
+
−
0345
+
−
2=
89
Section 4.4
Invariance under Pachner Moves
P
04,14,34,45
J2:={034,014,134,
045,145,345}
J3:={0134,0145,
1345,0345}
D2
|G|
1
(D2)4
Q
α∈J2
dα
Q
τ∈J3
dτ
P
04,14,34,45
J′
2:={034,134,
045,145,345}
J′
3:={1345,0345}
D2
|G|
1
(D2)4
Q
α∈J′
2
dα
Q
τ∈J′
3
dτ
P
04,14,
34,45
345
(D2
|G|)3 d345
(D2)4
P
04,14,
34,45
345
(D2
|G|)3 d2
345
(D2)4
= 1
0125
−
+
1235
+
−
1345
+
−
0145
+
−
0134
45
+
−
0123
+
−
45 34
0345
−
+
0235
−
+
0134
45
−
+
0145
−
+
1345
−
+
0135
+
−
0345
+
−
3=
0125
−
+
1235
+
−
1345
+
−
1345
−
+
0135
+
−
0345
+
−
0123
+
−
45 34
0345
−
+
0235
−
+
4=
345
0125
−
+
1235
+
−
0135
+
−
0123
+
−
45 34
0235
−
+
5=
0125
−
+
1235
+
−
0135
+
−
0123
+
−
35
0235
−
+
90
Chapter 5

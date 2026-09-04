---
doc_id: arxiv-1508.05448v1
doc_title: "Concentration of Measure Techniques and Applications"
section_id: sec-020-56-four-square-problem
section_title: "Four Square Problem"
section_number: 5.6
pages: 115-122
source_pdf: 1508.05448v1.pdf
source_sha256: 57d2c717d8ec74d0
doc_brief: "Concentration of Measure Techniques and Applications — 23 sections: Biographical Sketch; Acknowledgments; Abstract"
---
We would now like to give an idea as to how the q-Stirling’s formula arises in the
problem of bounding the ﬂuctuations of the length of the longest increasing subse-
107
Figure 5.2: Length of the longest increasing subsequence of a Mallows permutation of length 10 , 000
with q = 0.99
Figure 5.3: Length of the longest increasing subsequence of a Mallows permutation of length 10 , 000
with q = 0.88
108
R11
R21
R12
R22
Figure 5.4: An example of a decomposition of [0 , 1]2 into four rectangles R11, R12, R21, R22.
quence in a Mallows random permutation. This work is ongoing, but an important
step is discussed in this section. A random permutation (Mallows or otherwise), can
be viewed as a set of points in a rectangle, in the following way:
Consider n points (xi,yi) in the rectangle [0, 1]× [0, 1] in R2 with all coordinates
distinct. The set of points speciﬁes a permutationπ∈Sn by the rule: ”The point with
the ith smallest y coordinate has the π(i)th smallest x-coordinate”. Hence, given a
set of points in a box, we can obtain a permutation from these points. Depending on
how the points are distributed in the box, we can obtain permutations with diﬀerent
distributions. As an example, if the points are uniformly distributed in the box, we
obtain a uniform random permutation.
To begin to bound the ﬂuctuation of a Mallows random permutation, we assume
that we haven points in the unit square distributed so that they give a Mallows ran-
dom permutation. We then divide the square into a large number of small subsquares.
If the size of each subsquare is small enough, the points in the subsquare will be ap-
proximately uniformly distributed. We then hope to couple our model to a model of
Deuschel and Zeitouni [Deuschel and Zeitouni, 1999] to bound the ﬂuctuations.
This argument will not be presented here. For now, we will simply look at the di-
vision of the unit square into four subrectangles to illustrate the use of theq-Stirling’s
formula. Suppose that we divide the unit square into four rectanges, which we refer
109
to asR11, R12, R21, R22. See ﬁgure 5.4. Assuming that we have n total points in the
square, letn11 denote the number of points inR11,n12 denote the number of points in
R12, and so on. We then have n11 +n12 +n21 +n22 =n. Denote the area of rectange
Rij as pij. Consider the distribution of the points ( x1,y 1), (x2,y 2),..., (xn,yn) in the
square. If the points are distributed uniformly (i.e. if q = 1), then the probability of
the event
∩n
i,j=1{#{k : (Xk,Yk)∈Rij =nij}}
is given by the usual multinomial formula
n!
n11!n12!n21!n22!pn11
11 pn12
12 pn21
21 pn22
22 (5.6)
For 0<q < 1 andq⁄= 1 (in other words, a Mallows random permutation), the correct
probability is obtained by multiplying the above expression by the factor
qn12n21 [n11 +n12]![n11 +n21]![n12 +n22]![n21 +n22]!
(n11 +n12)!(n11 +n21)!(n12 +n22)!(n21 +n22)!· (n11)!(n12)!(n21)!(n22)!
[n11]![n12]![n21]![n22]! · n!
[n]!.
(5.7)
where [a]! denotes the q factorial as deﬁned earlier. Combining 5.6 and 5.7 and using
the notation{n}! := [n]!/n!, we have
P
(
∩n
i,j=1{#{k : (Xk,Yk)∈Rij =nij}
)
=
n!∏2
i,j=1(nij)!
( 2∏
i,j=1
p
nij
ij
)
{n11 +n12}!{n11 +n21}!{n12 +n22}!{n21 +n22}!
{n11}!{n12}!{n21}!{n22}!{n11 +n12 +n21 +n22}!qn21n12
(5.8)
This formula is somewhat involved, but it is explicit. By applying the q-Stirling’s
formula, we can obtain the exact asymptotics for the probability distribution in the
limit n→∞ , with q =e−β/n.
110
Recall that Stirling’s formula says that
n!∼en lnn−n√
2πn
and the q-Stirling’s formula states that for q =e−β/n,
ln
([n]!
n!
)
=nA(β) +B(β) +Rn(β)
where
A(β) =
∫ 1
0
ln
(1−e−βx
βx
)
dx
B(β) = β
2 + 1
2 ln
(1−e−βx
βx
)
and Rn(β) is a remainder term which goes to zero as n→∞ . Before we can apply
these asymptotics to equation 5.8, we need a preliminary lemma.
Lemma 5.6.1. Forq =e−β/n,
ln({nij}!) =nijA
(nij
n β
)
+B
(nij
n β
)
+Rnij
(nij
n β
)
This lemma is easily proved using the q-Stirling’s formula and rewriting q as
q =e−β′/nij, where β′ = nijβ
n .
To break down the asymptotics of 5.8 a bit, let
Wq ={n11 +n12}!{n11 +n21}!{n12 +n22}!{n21 +n22}!
{n11}!{n12}!{n21}!{n22}!{n11 +n12 +n21 +n22}!qn21n12
In addition, let νij = nij
n . For this analysis, we will assume that all νij are order 1,
so that we are not letting any of the squares be too small. If this is the case, we can
make the approximation
ln{nij}!≈nνijA(βvij)
111
Using this assumption, we have the following lemma
Lemma 5.6.2. Forν11,ν 12,ν 21,ν 22 > 0, we have
lim
n→∞
1
n ln(Wq) =−βν12ν21 + (ν11 +ν12)A(β[ν11 +ν12]) + (ν11 +ν21)A(β[ν11 +ν21])
+ (ν12 +ν22)A(β[ν12 +ν22]) + (ν21 +ν22)A(β[ν21 +ν22])
−ν11A(βν11)−ν12A(βν12)−ν21A(βν21)−ν22A(βν22)−A(β) (5.9)
Proof. By deﬁnition,
lim
n→∞
1
n ln(Wq)
= lim
n→∞
1
n ln
(
qν12nν21n{ν11n +ν12n}!{ν11n +ν21n}!{ν12n +ν22n}!{ν21n +ν22n}!
{ν11n}!{ν12n}!{ν21n}!{ν22}!{ν11n +ν12n +ν21n +ν22n}!
)
Using the q-Stirling formula and the previous lemma, we get
= lim
n→∞
1
n(ln (qν12nν21n)+(ν11n+ν12n)A(β(ν11+ν12))+··· +(ν21n+ν22n)A(β(ν21+ν22))
−ν11nA(βν11)−ν12nA(βν12)−ν21nA(βnu21)−ν22nA(βν22)
− (ν11n +ν12n +ν21n +ν22n)A(β(ν11 +ν12 +ν21 +ν22))) (5.10)
Distributing then and taking the limit immediately gives us what we need except for
the ﬁrst and last terms. Consider just
lim
n→∞
ln(qν12nν21n)
Since q =e−β/n, this is
= lim
n→∞
1
ne−β(ν12nν21)
= 1
n(−βν12nν21) =−βν12ν21
112
This gives us the ﬁrst term in our lemma. The last term is equal to
lim
n→∞
1
n(ν11n +ν12n +ν21n +ν22n)A(β(ν11 +ν12 +ν21 +ν22))
= lim
n→∞
(ν11 +ν12 +ν21 +ν22)A(β(ν11 +ν12 +ν21 +ν22))
=A(β)
since∑2
i,j=1νij = 1. Putting all terms together proves the lemma.
It is worth noting that the asymptotics for
1
n lnWq
given by this lemma give us an equation analogous (and very similar) to equation (6)
in [Starr and Walters, 2015].
Combining these asymptotics with the asymptotics for
n!∏2
i,j=1(nij)!
( 2∏
i,j=1
p
nij
ij
)
gives
P
(
∩n
i,j=1{#{k : (Xk,Yk)∈Rij =nij}
)
=
√
2πn∏2
i,j=1
√2πnij
e
˜A (5.11)
where
˜A =n(ln(n)−
n∑
i,j=1
νij ln(nij)
−βν12ν21 + (ν11 +ν12)A(β[ν11 +ν12]) + (ν11 +ν21)A(β[ν11 +ν21])
+ (ν12 +ν22)A(β[ν12 +ν22]) + (ν21 +ν22)A(β[ν21 +ν22])
−ν11A(βν11)−ν12A(βν12)−ν21A(βν21)−ν22A(βν22) (5.12)
113

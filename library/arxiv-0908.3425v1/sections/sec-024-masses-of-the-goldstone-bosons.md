---
doc_id: arxiv-0908.3425v1
doc_title: "Chiral Perturbation Theory: Introduction and Recent Resul ts in the One-Nucleon Sector S. Scherer"
section_id: sec-024-masses-of-the-goldstone-bosons
section_title: "Masses of the Goldstone bosons"
section_number: null
pages: 42-46
source_pdf: 0908.3425v1.pdf
source_sha256: 5e88d45bbc1c1b9b
doc_brief: "Chiral Perturbation Theory: Introduction and Recent Resul ts in the One-Nucleon Sector S. Scherer — We provide an introduction to the basic concepts of chiral pe rturbation theory and discuss some"
---
A discussion of the masses at O(q4) is one of the simplest applications of chiral perturbation theory
beyond the tree level. For that purpose let us consider L2 + L4 for QCD with ﬁnite quark masses but in
the absence of external ﬁelds. We restrict ourselves to the l imit of isospin symmetry, i.e., mu =md = ˆm.
In order to determine the masses we calculate the self energi es Σ( p2) of the Goldstone bosons.
Let
∆ φF (p) = 1
p2 −M 2
φ,2 +i0+, φ =π,K,η, (152)
denote the Feynman propagator containing the lowest-order masses,
M 2
π,2 = 2B0 ˆm, M 2
K,2 =B0( ˆm +ms), M 2
η,2 = 2
3B0 ( ˆm + 2ms).
(The subscript 2 refers to chiral order 2.) The proper self-e nergy insertions, −iΣ φ(p2), consist of one-
particle-irreducible diagrams only, i.e., diagrams which do not fall apart into two separate pieces when
cutting an arbitrary internal line. At chiral order D = 4, the contributions to −iΣ φ,4(p2) are those
shown in Fig. 8. In general, the full (unrenormalized) propa gator may be summed using a geometric
series (see Fig. 9):
i∆ φ(p) = i
p2 −M 2
φ,2 +i0+ + i
p2 −M 2
φ,2 +i0+ [−iΣ φ(p2)] i
p2 −M 2
φ,2 +i0+ + · · ·
= i
p2 −M 2
φ,2 − Σ φ(p2) +i0+. (153)
The physical mass, including the interaction, is deﬁned as t he pole of Eq. (153),
M 2
φ −M 2
φ,2 − Σ φ(M 2
φ) != 0, (154)
where the precision of the determination of M 2
φ depends on the precision of the calculation of Σ φ.
For our particular application with exactly two external me son lines, the relevant interaction La-
grangians can be written as
Lint = L4φ
2 + L2φ
4 , (155)
where
L4φ
2 = 1
24F 2
0
{
Tr([φ,∂ µφ]φ∂µφ) +B0Tr(Mφ4)
}
, (156)
42
p, 3 p, 3
k, j
2
Figure 10: Contribution of the pion loops to the π0 self energy.
L2φ
4 = −1
2
(
aππ0π0 +bπ∂µπ0∂µπ0
)
−aππ+π− −bπ∂µπ+∂µπ−
−aKK +K − −bK∂µK +∂µK − −aKK 0 ¯K 0 −bK∂µK 0∂µ ¯K 0
−1
2
(
aηη2 +bη∂µη∂ µη
)
. (157)
The constants aφ and bφ are given by
aπ = 64B2
0
F 2
0
[
(2 ˆm +ms) ˆmL6 + ˆm2L8
]
,
bπ = −16B0
F 2
0
[(2 ˆm +ms)L4 + ˆmL5],
aK = 32B2
0
F 2
0
[
(2 ˆm +ms)( ˆm +ms)L6 + 1
2 ( ˆm +ms)2L8
]
,
bK = −16B0
F 2
0
[
(2 ˆm +ms)L4 + 1
2 ( ˆm +ms)L5
]
aη = 64B2
0
3F 2
0
[
(2 ˆm +ms)( ˆm + 2ms)L6 + 2( ˆm −ms)2L7 + ( ˆm2 + 2m2
s)L8
]
,
bη = −16B0
F 2
0
[
(2 ˆm +ms)L4 + 1
3 ( ˆm + 2ms)L5
]
. (158)
At O(q4) the self energies are of the form
Σ φ,4(p2) = Aφ +Bφp2, (159)
where the constants Aφ and Bφ receive a tree-level contribution from L4 and a one-loop contribution
with a vertex from L2 (see Fig. 8). For the tree-level contribution of L4 this is easily seen, because the
Lagrangians of Eq. (157) contain either exactly two derivat ives of the ﬁelds or no derivatives at all. For
example, the contact contribution for the η reads
−iΣ tree
η,4 (p2) = −i(aη +bηp2).
For the one-loop contribution the argument is as follows. Th e Lagrangian L4φ
2 contains either two
derivatives or no derivatives at all which, symbolically, c an be written as φφ∂φ∂φ and φ4, respectively.
The ﬁrst term results in M 2 or p2, depending on whether the φ or the ∂φ are contracted with the
external ﬁelds. The “mixed” situation vanishes upon integr ation. The second term, φ4, does not
generate a momentum dependence.
As a speciﬁc example, we evaluate the pion-loop contributio n to the π0 self energy (see Fig. 10) by
applying the Feynman rule of Eq. (120) for a =c = 3, pa =pc =p, b =d =j, and pb =pd =k:
43
1
2
∫ d4k
(2π)4
i
3F 2
0
[−4p2 − 4k2 + 5M 2
π,2] i
k2 −M 2
π,2 +i0+,
where 1/2 is a symmetry factor. Since the integral diverges, we consi der its extension to n dimensions.
In addition to the loop-integral of Eq. (134), we need
µ4−ni
∫ dnk
(2π)n
k2
k2 −M 2 +i0+ =µ4−ni
∫ dnk
(2π)n
k2 −M 2 +M 2
k2 −M 2 +i0+,
where we have added 0 = −M 2 +M 2 in the numerator. We make use of
µ4−ni
∫ dnk
(2π)n = 0
in dimensional regularization which is “shown” as follows. Consider the (more general) integral
∫
dnk(k2)p, (160)
substitute k =λk′ (λ> 0), and relabel k′ =k
=λn+2p
∫
dnk(k2)p.
Since λ >0 is arbitrary and, for ﬁxed p, the result is to hold for arbitrary n, Eq. (160) is set to zero
in dimensional regularization. We emphasize that the vanis hing of Eq. (160) has the character of a
prescription. The integral does not depend on any scale and i ts analytic continuation is ill deﬁned in
the sense that there is no dimension n where it is meaningful. It is ultraviolet divergent for n + 2p ≥ 0
and infrared divergent for n + 2p ≤ 0.
We then obtain
µ4−ni
∫ dnk
(2π)n
k2
k2 −M 2 +i0+ =M 2I(M 2,µ 2,n ),
with I(M 2,µ 2,n ) of Eq. (134). The pion-loop contribution to the π0 self energy is thus
i
6F 2
0
(−4p2 +M 2
π,2)I(M 2
π,2,µ 2,n ),
which is indeed of the type discussed in Eq. (159) and diverge s as n → 4.
After analyzing all loop contributions and combining them w ith the tree-level contributions of Eqs.
(158), the constants Aφ and Bφ of Eq. (159) are given by
Aπ = M 2
π,2
F 2
0
{
−1
6I(M 2
π,2) − 1
6I(M 2
η,2) − 1
3I(M 2
K,2)
/bracehtipupleft /bracehtipdownright/bracehtipdownleft /bracehtipupright
loop contribution
+32[(2 ˆm +ms)B0L6 + ˆmB0L8]/bracehtipupleft /bracehtipdownright/bracehtipdownleft/bracehtipupright
tree-level contribution
}
,
Bπ = 2
3
I(M 2
π,2)
F 2
0
+ 1
3
I(M 2
K,2)
F 2
0
− 16B0
F 2
0
[(2 ˆm +ms)L4 + ˆmL5],
AK = M 2
K,2
F 2
0
{
1
12I(M 2
η,2) − 1
4I(M 2
π,2) − 1
2I(M 2
K,2) + 32
[
(2 ˆm +ms)B0L6 + 1
2 ( ˆm +ms)B0L8
] }
,
BK = 1
4
I(M 2
η,2)
F 2
0
+ 1
4
I(M 2
π,2)
F 2
0
+ 1
2
I(M 2
K,2)
F 2
0
− 16B0
F 2
0
[
(2 ˆm +ms)L4 + 1
2 ( ˆm +ms)L5
]
,
Aη = M 2
η,2
F 2
0
[
−2
3I(M 2
η,2)
]
+ M 2
π,2
F 2
0
[ 1
6I(M 2
η,2) − 1
2I(M 2
π,2) + 1
3I(M 2
K,2)
]
+M 2
η,2
F 2
0
[16M 2
η,2L8 + 32(2 ˆm +ms)B0L6] + 128
9
B2
0( ˆm −ms)2
F 2
0
(3L7 +L8),
Bη = I(M 2
K,2)
F 2
0
− 16
F 2
0
(2 ˆm +ms)B0L4 − 8M 2
η,2
F 2
0
L5, (161)
44
where, for simplicity, we have suppressed the dependence on the scale µ and the number of dimensions
n in the integrals I(M 2,µ 2,n ) [see Eq. (134)]. Both the integrals I and the bare coeﬃcients Li (with
the exception of L7) have 1/(n − 4) poles and ﬁnite pieces. In particular, the coeﬃcients Aφ and Bφ
are not ﬁnite as n → 4 showing that they do not correspond to observables.
The masses at O(q4) are determined by solving Eq. (154) with the predictions of Eq. (159) for the
self energies,
M 2
φ =M 2
φ,2 +Aφ +BφM 2
φ,
from which we obtain
M 2
φ = M 2
φ,2 +Aφ
1 −Bφ
=M 2
φ,2(1 +Bφ) +Aφ + O(q6),
because Aφ = O(q4) and {Bφ,M 2
φ,2} = O(q2). Expressing the bare coeﬃcients Li in Eq. (161) in terms
of the renormalized coeﬃcients by using Eq. (141), the resul ts for the masses of the Goldstone bosons
at O(q4) read [Gasser and Leutwyler, 1985]
M 2
π,4 = M 2
π,2
{
1 + M 2
π,2
32π2F 2
0
ln
(
M 2
π,2
µ2
)
− M 2
η,2
96π2F 2
0
ln
(
M 2
η,2
µ2
)
+ 16
F 2
0
[(2 ˆm +ms)B0(2Lr
6 −Lr
4) + ˆmB0(2Lr
8 −Lr
5)]
}
, (162)
M 2
K,4 = M 2
K,2
{
1 + M 2
η,2
48π2F 2
0
ln
(
M 2
η,2
µ2
)
+ 16
F 2
0
[
(2 ˆm +ms)B0(2Lr
6 −Lr
4) + 1
2 ( ˆm +ms)B0(2Lr
8 −Lr
5)
] }
,
(163)
M 2
η,4 = M 2
η,2
[
1 + M 2
K,2
16π2F 2
0
ln
(
M 2
K,2
µ2
)
− M 2
η,2
24π2F 2
0
ln
(
M 2
η,2
µ2
)
+ 16
F 2
0
(2 ˆm +ms)B0(2Lr
6 −Lr
4) + 8M 2
η,2
F 2
0
(2Lr
8 −Lr
5)
]
+M 2
π,2
[
M 2
η,2
96π2F 2
0
ln
(
M 2
η,2
µ2
)
− M 2
π,2
32π2F 2
0
ln
(
M 2
π,2
µ2
)
+ M 2
K,2
48π2F 2
0
ln
(
M 2
K,2
µ2
)]
+ 128
9
B2
0( ˆm −ms)2
F 2
0
(3Lr
7 +Lr
8). (164)
First of all, we note that the expressions for the masses are ﬁ nite. The inﬁnite parts of the coeﬃcients
Li of the Lagrangian of Gasser and Leutwyler exactly cancel the divergent terms resulting from the
integrals. This is the reason why the bare coeﬃcients Li must be inﬁnite. Furthermore, at O(q4) the
masses of the Goldstone bosons vanish, if the quark masses ar e sent to zero. This is, of course, what we
had expected from QCD in the chiral limit but it is comforting to see that the self interaction in L2 (in
the absence of quark masses) does not generate Goldstone bos on masses at higher order. At O(q4), the
squared Goldstone boson masses contain terms which are anal ytic in the quark masses, namely, of the
formm2
q multiplied by the renormalized low-energy coupling consta ntsLr
i . However, there are also non-
analytic terms of the type m2
q ln(mq)—so-called chiral logarithms—which do not involve new par ameters.
Such a behavior is an illustration of the mechanism found by L i and Pagels [Li and Pagels, 1971], who
noticed that a perturbation theory around a symmetry which i s realized in the Nambu-Goldstone mode
results in both analytic as well as non-analytic expression s in the perturbation. Finally, the scale
dependence of the renormalized coeﬃcients Lr
i of Eq. (141) is by construction such that it cancels the
scale dependence of the chiral logarithms. Thus, physical o bservables do not depend on the scale µ. It
45
is straightforward to verify this statement by diﬀerentiat ing Eqs. (162) - (164) with respect to µ and
by making use of
dLr
i (µ)
dµ = − Γ i
16π2µ,
where the Γ i are given in Table 7.

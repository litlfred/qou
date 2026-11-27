---
doc_id: arxiv-2010.12819v2
doc_title: "The action of the Virasoro algebra in quantum spin chains. I. The non-rational case"
section_id: sec-045-f-the-chiral-antichiral-commutator
section_title: "F The chiral-antichiral commutator"
section_number: null
pages: 53-55
source_pdf: 2010.12819v2.pdf
source_sha256: ddc0493d60d48e77
toc_source: outline
doc_brief: "The action of the Virasoro algebra in quantum spin chains. I. The non-rational case — We investigate the action of discretized Virasoro generators, built out of generators of the lattice"
---
In [1] the limit of [ Lp+n + ¯L−p−n, L−p + ¯Lp] was checked, and was found to be correct. Meanwhile in Section
7 and Appendix E we found strong evidence for [ Lp+n + ¯L−p−n, L−p− ¯Lp] having the correct limit up to the
central term. In order to isolate the chiral-antichiral commutator [ Lp+n, ¯L−p] it remains to ﬁnd the behaviour
of [Lp+n− ¯L−p−n, L−p− ¯Lp]. We shall proceed in the same manner as in Section 7 and Appendix E. However,
while we there showed ﬁgures for two diﬀerent cases at n = 0, once case at n =−1 and two at n =−2, we shall
here only reproduce the ﬁgures corresponding to one of the cases atn = 0 and the case atn =−1. This is partly
to save space, and partly (for the n =−2 cases) due to increasingly disruptive ﬁnite size eﬀects—as was already
noted in Appendix E, such eﬀects become generally more pronounced for products of several Temperley-Lieb
generators.
Similarly to (116) we ﬁrst expand the commutator under investigation. We obtain the expression
[Lp+n− ¯L−p−n, L−p− ¯Lp]
=−2i
(N
2π
)2( γ
π sinγ
)4{
sin
(4πp + 2πn
N
) N∑
j=1
e2iπn(j+3/2)/N[[ej,ej+1], [ej+2,ej+3]]
+e−iπn/N sin
(2πp +πn
N
) N∑
j=1
e2iπn(j+3/2)/N
(
−[ej,ej+1]− [ej+1,ej+2] +
√
Q(ejej+1ej+2−ej+2ej+1ej)
)}
.
(196)
Provided that the matrix elements of the combinations of Temperley-Lieb operators appearing above are of
order O(1/Nr) with r > 0 for the ﬁrst row and r > 1 for the second row, we may restrict our attention to
leading order terms the trigonometric functions as well as the exponential in the second row. To be concise, let
us denote
r1 = [[ej,ej+1], [ej+2,ej+3]]
r2 =−[ej,ej+1]− [ej+1,ej+2] +
√
Q(ejej+1ej+2−ej+2ej+1ej).
(197)
We plot the matrix elements of r1 andr2 forn = 0,−1 in Figures 11,12.We ﬁnd that r> 1 in both cases. With
this in mind we keep only leading terms in the expansion:
[Lp+n− ¯L−p−n, L−p− ¯Lp] = (2p +n)(−i)N
2π
( γ
π sinγ
)4 N∑
j=1
e2iπn(j+3/2)/N(2r1 +r2) + O
( 1
Nr−1
)
. (198)
We now compare (198) to what is denoted ˆh(4) in [1], using this time the result KS (2.59) 18
−i N
2π
( γ
π sinγ
)4 N∑
j=1
e2iπn(j+3/2)/N6 [[ej,ej+1], [ej+2,ej+3]]
+ 6
√
Q[ej(ej+1ej+2 +ej+2ej+1)] + (Q + 2)[ej,ej+1]↦→
(
Ln− ¯L−n
)
.
(199)
We note that as is the case for P in (29), also denoted by ˆh(2) in [1], the ground state expectation value of ˆh(4)
is zero. For this reason we do not need to introduce normal ordering in (199). It turns out that the ground state
expectation values of r1,r 2 are also zero, as are some other matrix elements that are for this reason excluded
from the ﬁgures below.
As before we deﬁne a remainder, here given by the diﬀerence between the summand in (198) and (199):
R(4) =−4 [[ej,ej+1], [ej+2,ej+3]]− 6
√
Q[ej(ej+1ej+2 +ej+2ej+1)]− (Q + 2)[ej,ej+1]
− [ej,ej+1]− [ej+1,ej+2] +
√
Q(ejej+1ej+2−ej+2ej+1ej).
(200)
For the limit of (196) to be correct we need the remainder to decay as O(1/Nr) with r >2. We see in Figures
11,12 that the numerical results support this. Together with the previous results for [Lp+n + ¯L−p−n, L−p+ ¯Lp]
and [Lp+n+ ¯L−p−n, L−p− ¯Lp] we can conclude that the numerical results strongly indicate that [Lp+n, ¯L−p] ↦→ 0.
Again we show the ﬁgures only for n = 0,−1 in the interest of saving space, but we note that at n =−2 the
ﬁnite size eﬀects are signiﬁcantly smaller for R(4) than they are for r1 and r2, and the numerical results for
R(4) show a clear r> 2 slope for n =−2 already at the sizes we can access.
18Generalized to n⁄= 0 in the same way as in KS (3.33).
53
Figure 11: Absolute value of matrix elements, plotted using the same conventions as in Figure 3 but with the
choice of|u⟩ =|v⟩.
Figure 12: Absolute value of matrix elements, plotted using the same conventions as in Figure 3. In case of
choices of|v⟩ showing particularly strong ﬁnite size eﬀects (|Sz = 1,e = 1⟩ and|p = 1⟩ in upper two plots) the
linear ﬁt is performed using only the two leftmost points.
54

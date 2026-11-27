---
doc_id: arxiv-2010.12819v2
doc_title: "The action of the Virasoro algebra in quantum spin chains. I. The non-rational case"
section_id: sec-021-52-numerical-results-for-l-1
section_title: "Numerical results for L-1"
section_number: 5.2
pages: 23-25
source_pdf: 2010.12819v2.pdf
source_sha256: ddc0493d60d48e77
toc_source: outline
doc_brief: "The action of the Virasoro algebra in quantum spin chains. I. The non-rational case — We investigate the action of discretized Virasoro generators, built out of generators of the lattice"
---
We now show the ﬁrst non-zero matrix elements of the matrix L−1[N] for increasingly large system size N and
compare with the values we would expect from CFT computations. In this example we consider Sz = 1,e = 0
at φ = 1/10,x = π. (Recall (1): q = eiγ = eiπ/(x+1), and (2): eφ = φ
2π ). For non-zero matrix elements, the
lattice momentum must shift by p→p−n =p + 1 between the two Bethe states.
We shall consider the block between states in the momentum sectors p = 0 (denoted |u1⟩,|u2⟩,... ) and
p = 1 (denoted |v1⟩,|v2⟩,... ). The set of Bethe integers for the lowest-energy state in the p = 0 sector,
which we denote by |u1⟩, allows us to identify it with a primary state Vα,¯α, which by (66) has a chiral charge
α =− 1
40πα+ +α0− 1
2α− = 0.56495148. The other states we consider will be its descendants. At N = 10 we
ﬁnd the three lowest states in each sector, sorted by energy, for the following Bethe integers: 10
p = 0:
|u1⟩↔
{
−3
2,−1
2, 1
2, 3
2
}
↔◦◦••|••◦◦ ↔ primary state Vα,¯α
|u2⟩↔
{
−5
2,−1
2, 1
2, 5
2
}
↔◦•◦•|•◦•◦ ↔ chiral and anti-chiral level 1
|u3⟩↔
{
−5
2,−3
2, 3
2, 5
2
}
↔◦••◦|◦••◦ ↔ chiral and anti-chiral level 2
(102)
p = 1:
|v1⟩↔
{
−5
2,−1
2, 1
2, 3
2
}
↔◦•◦•|••◦◦ ↔ chiral level 1
|v2⟩↔
{
−5
2,−3
2, 1
2, 5
2
}
↔◦••◦|•◦•◦
|v3⟩↔
{
−7
2,−1
2, 1
2, 5
2
}
↔•◦◦•|•◦•◦



↔ chiral level 2 and anti-chiral level 1
(103)
These patterns extend to larger N by padding with ﬁlled circles in the middle. Taking the example of |u2⟩ we
ﬁnd◦•◦•|•◦•◦ → ◦•◦••|•◦•◦ → ◦•◦••|••◦•◦ → ... .
Recall the state space (72). Since there is only one state at level 1 we can immediately identify |v1⟩ with
a−1Vα,¯α and|u2⟩ with a−1¯a−1Vα,¯α. Meanwhile at level 2 there are two states, and the states |v2⟩ and|v3⟩
will correspond to an orthonormal basis for the two-dimensional vector space of a2
−1¯a−1Vα,¯α and a−2¯a−1Vα,¯α.
Finally|u3⟩ corresponds to one basis vector in an orthonormal basis for the four-dimensional vector space of
states at chiral and anti-chiral level 2, the other three basis vectors being found by considering scaling states of
higher energy.
Conjectures for the matrix elements:
• As in Section 3.4 we haveL−1Vα,¯α =
√
2αa−1Vα,¯α, leading to the conjectured value⟨a−1Vα,¯α|L−1|Vα,¯α⟩ =√
2α = 0.79896205 for the matrix element ( L−1[N])v1,u1 at N →∞ . We can also ﬁnd this value by
considering the norm squared ⟨L−1Vα,¯α|L−1Vα,¯α⟩ =⟨Vα,¯α|L†
−1L−1Vα,¯α⟩, where L†
−1 =L1 + 2
√
2α0a1 by
(74). Using (71) and (73) we ﬁnd L†
−1L−1Vα,¯α = 2α2Vα,¯α.11
• The latter method carries over most easily to the next two matrix elements that we wish to consider:
(L−1[N])v2,u2 and ( L−1[N])v3,u2. We ﬁnd the norm squared ⟨L−1a−1Vα,¯α|L−1a−1Vα,¯α⟩ = 2(1 + 2α2).
Since|v2⟩ and|v3⟩ provide a basis, we expect to recover the full norm
√
2(1 + 2α2) = 1 .81016041 by
combining the projections on these states as
√
(L−1[N])2v2,u2 + (L−1[N])2v3,u2 at N→∞ .
• All other matrix elements among the states in (102) and (103) are conjectured to be zero in the limit,
since the chiral levels do not match.
10Here we see an example of half-integer “Bethe integers”, since this is the maximally packed symmetric distribution around zero
for four roots.
11In general, the calculations of this type that are seen in this paper have been performed by adapting the Mathematica notebook
“Virasoro” by M. Headrick, available at http://people.brandeis.edu/~headrick/Mathematica/index.html.
23
Using the form factors computed in Appendix B we can obtain the matrix elements ( L−1[N])viuj for
increasingly large system size N. We then perform a polynomial extrapolation in 1/N to approximate the value
at N→∞ . This is shown in table 1 for i = 1,j = 1 and i = 2,j = 1.
N ⟨v1|L−1|u1⟩ ⟨v2|L−1|u1⟩
10 0.73934396 0.01866525
12 0.75628984 0.0178073
14 0.76689996 0.01621625
16 0.77397144 0.01457925
18 0.77891781 0.01309015
20 0.78251286 0.01178876
22 0.78520823 0.01066614
24 0.7872816 0.00969992
26 0.78891124 0.00886622
28 0.79021581 0.00814359
30 0.79127676 0.0075138
32 0.79215151 0.00696179
34 0.79288148 0.00647521... ... ...
... ... ...
36 0.79349714 0.00604396
38 0.79402136 0.00565977
40 0.79447152 0.00531584
42 0.79486106 0.00500654
44 0.79520048 0.0047272
46 0.79549811 0.0044739
48 0.79576061 0.00424336
50 0.79599334 0.00403281
52 0.7962007 0.00383989
54 0.79638628 0.00366257
56 0.79655307 0.00349914
58 0.79670354 0.00334811
60 0.79683979 0.00320817... ... ...
... ... ...
62 0.79696357 0.00307821
64 0.79707638 0.00295725
66 0.79717949 0.00284442
68 0.79727401 0.00273896
70 0.79736087 0.00264022
72 0.79744089 0.0025476
74 0.79751479 0.00246056
76 0.79758317 0.00237865
78 0.79764659 0.00230144
80 0.79770552 0.00222856
p25 0.79896913 -4 .846· 10−5
p30 0.79896944 -5 .025· 10−5
p35 0.79896858 -4 .558· 10−5
conj 0.79896205 0
Table 1: Matrix elements ( L−1[N])viuj for i = 1,j = 1 and i = 2,j = 1, where the scaling states |uj⟩ and|vi⟩
follow the patterns of Bethe integers shown in (102) and (103). The numerical values are given for the case of
Sz = 1,e = 0,x = π,φ = 1/10 for system size N up to 80, after which polynomial extrapolations pn(1/N) of
degrees n = 25, 30, 35 to all the data points are made in order to approximate the value at N→∞ .
The other seven matrix elements between the Bethe states listed above are found in the same fashion, and
we do not write out the corresponding columns in Table 1. The results of the extrapolation p35 for all nine
matrix elements are:
L−1[N]
N→∞
−−−−→
p35
p = 0 p = 1 ...




0 0 ... p = 0


0.79896858 −3.49· 10−6 −5.407· 10−5 ...
−4.558· 10−5 1.80729191 −2.66· 10−6
−1.722· 10−5 0.1039298 2 · 10−8
... ...

 0 p = 1
... ...
...
(104)
We compare the extrapolation of ( L−1)v1,u1 to the conjectured value of 0.79896205, and we compare the total
contribution of the extrapolations of ( L−1)v2,u2 and (L−1)v3,u2,
√
1.807291912 + 0.10392982 = 1.81027773, to
the conjectured value of 1 .81016041. All other matrix elements are conjectured to be zero. We see that we
overall obtain a precision of at least around 10 −4 by considering system sizes up to N = 80.
We conclude this section with a note on the six matrix elements that are conjectured to be zero, whose
values are small but non-zero at ﬁnite size. We shall call such matrix elements “parasitic couplings”. They play
an important role when considering products and commutators of Koo-Saleur generators. Consider a matrix
element of the product of two Koo-Saleur generators, which can be decomposed into a sum over all Bethe states
as⟨a|LnLm|b⟩ =∑
x⟨a|Ln|x⟩⟨x|Lm|b⟩. Even if each parasitic coupling disappears in the limit N→∞ , the
number of parasitic couplings in the sum will grow rapidly, and may yield a ﬁnite contribution. Until this is
further explored, one cannot assume that limits of products give the same results as products of limits. As a
particular example, this non-interchangeability of limits applies when the products under consideration form a
commutator of two generators. Indeed, the issue of limits and commutators was raised already in [1], where
it was shown that the limit of commutators must sometimes diﬀer from the commutators of limits. We shall
return to this discussion in Section 7.
24

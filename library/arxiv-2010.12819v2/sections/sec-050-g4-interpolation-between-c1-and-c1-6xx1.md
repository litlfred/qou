---
doc_id: arxiv-2010.12819v2
doc_title: "The action of the Virasoro algebra in quantum spin chains. I. The non-rational case"
section_id: sec-050-g4-interpolation-between-c1-and-c1-6xx1
section_title: "G.4 Interpolation between c=1 and c=1-6x(x+1)"
section_number: null
pages: 57-61
source_pdf: 2010.12819v2.pdf
source_sha256: ddc0493d60d48e77
toc_source: outline
doc_brief: "The action of the Virasoro algebra in quantum spin chains. I. The non-rational case — We investigate the action of discretized Virasoro generators, built out of generators of the lattice"
---
x(x+1)
We have seen that the “ordinary” XXZ chain corresponds to λ = 0 in (201)–(202). Here we instead consider
λ =t sinγ
2 , varyingt between 0 and 1 to obtain values of the central charge between c = 1 and c = 1− 6
x(x+1).20
On the lattice we deﬁne
Mj(t) =−σ−
j σ+
j+1−σ+
j σ−
j+1− cosγ
2 σz
jσz
j+1−ti sinγ
2 (σz
j−σz
j+1) + cosγ
2 , (216)
such that
Mj(t) =


0 0 0 0
0 q−1 + (1−t) q−q−1
2 −1 0
0 −1 q− (1−t) q−q−1
2 0
0 0 0 0

 =
{
fj if t = 0,
ej if t = 1. (217)
20With α0⁄= 0 it is necessary for conformal charges to be quantized in terms of the screening charges α± in order to obtain a
nonzero four-point function of the corresponding ﬁeld [31]. For this reason the interpolation may not be physical, since it breaks
the relation between α0 and α±.
57
⟨a−1u|L−1|u⟩ ⟨ ¯a−1u| ¯L−1|u⟩
N ⟨u|L1|a−1u⟩ ⟨ u| ¯L1|¯a−1u⟩
8 0.18927529 0.18927529
10 0.19199126 0.19199126
12 0.19341304 0.19341304
14 0.1942385 0.1942385
16 0.19475441 0.19475441
18 0.19509508 0.19509508
20 0.19532981 0.19532981
22 0.1954971 0.1954971
p7 0.19601147 0.19601147
conj 0.19603173 0.19603173
⟨a−1u|LXXZ
−1 |u⟩ ⟨ ¯a−1u| ¯LXXZ
−1 |u⟩
N ⟨u|LXXZ
1 |a−1u⟩ ⟨u| ¯LXXZ
1 |¯a−1u⟩
8-22 O(10−15) O(10−15)
conj 0 0
⟨a−1uq2|LXXZ
−1 |uq±2⟩ ⟨ ¯a−1uq2| ¯LXXZ
−1 |uq±2⟩
N ⟨uq±2|LXXZ
1 |a−1uq2⟩ ⟨uq±2| ¯LXXZ
1 |¯a−1uq2⟩
8 0.18692177 0.18692177
10 0.19029496 0.19029496
12 0.1921169 0.1921169
14 0.19320597 0.19320597
16 0.193906 0.193906
18 0.19438114 0.19438114
20 0.1947176 0.1947176
22 0.19496405 0.19496405
p7 0.19602359 0.19602359
conj 0.19603173 0.19603173
Table 12: Matrix elements of L±1, ¯L±1, LXXZ
±1 and ¯LXXZ
±1 with the same conventions as in Table 3, in the
sector of Sz = 0 at x = π. We call |u⟩ the primary state at e = 0 and periodic boundary conditions eφ = 0
corresponding to the module W0,1 (top), and|uq±2⟩ the primary state at|e| = 1 and twisted boundary conditions
|eφ| =−α−/α+ corresponding to the modules W0,q2 and W0,q−2(bottom) for which the results are the same. In
the latter case, the results for L±1 and ¯L±1 are given in Table 10.
Again, twisted boundary conditions correspond to modifying the oﬀ-diagonal elements of Mj(t) as in (22) and
(205). We call the corresponding Koo-Saleur generators Lt
n and ¯Lt
n.
As seen from 202, we expect the central charge to be quadratic as a function of t,
c(t) = 1− 24(tα0)2. (218)
To explore this numerically we consider matrix elements
⟨1|Lt
2 Lt
−2|1⟩. (219)
We thus need to interpolate the identity state 1 continuously as we varyt. Both Sz ande taking integer values
only, we are left with varying the twist φ. We may start the interpolation either from the known identity state
Sz = 0, e= 0, eφ = 0 at t = 0, c= 1 or from the known identity state Sz = 0,|e| = 1, eφ = α−/α+ at
t = 1, c= 1− 6
x(x+1). In these cases the result of applying LXXZ
−1 or L−1, respectively, yields identically zero
on the lattice thanks to the structure of the modules of the respective algebras. It turns out that these two
approaches yield identical results: the “unsmeared” twist φ = 2πeφ being deﬁned modulo 2 π, combined with
the conjecture (66) depending only on the combination e−eφ, means that shifting e from 0 to 1 is equivalent
to choosing a diﬀerent representative in the equivalence class for φ.21 We choose here to start from the identity
state at t = 0, with e = eφ = Sz = 0. Within the conjecture (66) the background charge α0 is replaced by
tα0, meaning that as t increases we must increase the twist as eφ = 2tα0/α+ to keep α = 0. Following this
procedure we obtain the values of the central charge at a function of t shown in Figure 13. We note that the
eﬀects of “parasitic couplings” seem to be more pronounced for the case of the “ordinary” XXZ chain at t = 0.
That is, we ﬁnd once more that these eﬀects are the strongest for the largest value of c.
21We note that while all representatives are equivalent on the level of the “unsmeared” twist, one does need to be careful with
the choice of representative when numerically “smearing out” the twist.
58
Figure 13: Finite-size estimate for the central charge c as a function of interpolation parameter t at x = π,
using the same conventions as in Figure 2. The generators Lt
n are deﬁned below (217).
References
[1] W. Koo and H. Saleur, Nucl. Phys. B 426, 459–504 (1994); arXiv:hep-th/9312156.
[2] L. Grans-Samuelsson, L. Liu, Y. He, J.L. Jacobsen and H. Saleur, J. High Energ. Phys. 2020, 109 (2020);
arXiv:2007.11539.
[3] A. Milsted and G. Vidal, Phys. Rev. B 96, 245105 (2017); arXiv:1706.01436.
[4] Y. Zou, A. Milsted and G. Vidal, Phys. Rev. Lett. 121, 230402 (2018); arXiv:1710.05397.
[5] L. Lootens, R. Vanhove and F. Verstraete, Cardy states, defect lines and chiral operators of coset CFTs
on the lattice, arXiv:1907.02520.
[6] D. Chelkak, A. Glazman and S. Smirnov, Discrete stress-energy tensor in the loop O(n) model,
arXiv:1604.06339.
[7] V.F.R. Jones, J. Phys. A: Math. Theor. 51, 104001 (2018); arXiv:1706.00515.
[8] V. Gurarie and A.W.W. Ludwig, J. Phys. A: Math. Gen. 35, L377–L384 (2002); arXiv:cond-mat/9911392.
[9] J. Dubail, J.L. Jacobsen and H. Saleur, Nucl. Phys. B 834, 399–422 (2010); arXiv:1001.1151.
[10] R. Vasseur, J.L. Jacobsen and H. Saleur, Nucl. Phys. B 851, 314–345 (2011); arXiv:1103.3134.
[11] R. Vasseur, A. Gainutdinov, J.L. Jacobsen and H. Saleur, Phys. Rev. Lett. 108, 161602 (2012);
arXiv:1110.1327.
[12] V. Pasquier and H. Saleur, Nucl. Phys. B 330, 523–556 (1990).
[13] D. Aasen, R.S.K. Mong and P. Fendley, J. Phys. A: Math. Theor. 49, 354001 (2016); arXiv:1601.07185.
[14] N. Read and H. Saleur, Nucl. Phys. B 777, 316–351 (2007); arXiv:hep-th/0701117.
[15] A.M. Gainutdinov, J.L. Jacobsen and H. Saleur, J. High Energ. Phys. 2018, 117 (2018);
arXiv:1712.07076.
[16] Y. Ikhlef, J.L. Jacobsen and H. Saleur, Phys. Rev. Lett. 116, 130601 (2016); arXiv:1509.03538.
[17] Y. Zou, A. Milsted and G. Vidal, Phys. Rev. Lett. 124, 040604 (2020); arXiv:1901.06439.
[18] M. Picco, S. Ribault and R. Santachiara, SciPost Phys. 1, 009 (2016); arXiv:1607.07224.
[19] J.L. Jacobsen and H. Saleur, J. High Energ. Phys. 2019, 84 (2019); arXiv:1809.02191.
[20] Y. He, L. Grans-Samuelsson, J.L. Jacobsen and H. Saleur, J. High Energ. Phys. 2020, 156 (2020);
arXiv:2002.09071.
[21] Y. He, J.L. Jacobsen and H. Saleur, Geometric four-point functions in the 2D critical Q-state Potts model:
The interchiral conformal bootstrap , J. High Energ. Phys. (in press); arXiv:2005.07258.
59
[22] A. Gainutdinov, N. Read and H. Saleur, Nucl. Phys. B 871, 245–288 (2013); arXiv:1112.3403.
[23] A. Gainutdinov, N. Read and H. Saleur, Nucl. Phys. B 871, 289–329 (2013); arXiv:arXiv:1112.3407.
[24] A. Gainutdinov, N. Read and H. Saleur, Comm. Math. Phys. 341, 35–103 (2016); arXiv:1207.6334.
[25] M. Shokrian-Zini and Z. Wang, Comm. Math. Phys. 363, 877–953 (2018); arXiv:1706.08497.
[26] A.A. Belavin, A.M. Polyakov and A.B. Zamolodchikov, Nucl. Phys. B 241, 333–380 (1984).
[27] L. Grans-Samuelsson, J.L. Jacobsen, L. Liu and H. Saleur, The action of the Virasoro algebra in quantum
spin chains. II. The root of unity case , in preparation.
[28] A. Gainutdinov, N. Read, H. Saleur and R. Vasseur, J. High Energ. Phys. 2015, 114 (2015);
arXiv:1409.0167.
[29] J.J. Graham and G.I. Lehrer, L’Ens. Math. 44, 173 (1998).
[30] P.P. Martin and H. Saleur, Comm. Math. Phys. 158, 155–190 (1993).
[31] Vl.S. Dotsenko and V. Fateev, Nucl. Phys. B 240, 312 (1984).
[32] P. Pearce, J. Rasmussen and E. Tartaglia, J. Stat. Mech. 1405 (2014) P05001; arXiv:1312.6763.
[33] A. Lafay, A.M. Gainutdinov, J.L. Jacobsen,Uq(sln) web models and Zn spin interfaces; arXiv:2101.00282.
[34] A. Gainutdinov, H. Saleur and I. Tipunin, J. Phys. A: Math. Theor. 47, 495401 (2014); arXiv:1212.1378.
[35] H.N.V. Temperley and E.H. Lieb, Proc. Roy. Soc. Lond. A 322, 251–280 (1971).
[36] P.P. Martin and H. Saleur, Lett. Math. Phys. 30, 189–206 (1994).
[37] U. Grimm and V. Rittenberg, Int. J. Mod. Phys. B 4, 969 (1990).
[38] P. Di Francesco, H. Saleur and J.-B. Zuber, J. Stat. Phys. 49, 57–79 (1987).
[39] J.L. Jacobsen, Conformal ﬁeld theory applied to loop models, in A.J. Guttmann (ed), Polygons, polyominoes
and polycubes, Lecture Notes in Physics 775, 347–424 (Springer, Heidelberg, 2009).
[40] S. Lukyanov and V. Terras, Nucl. Phys. B 654, 323 (2003); arXiv:hep-th/0206093.
[41] B. Feigin and D.B. Fuchs, Funct. Anal. Appl. 16, 114–126 (1982).
[42] B. Feigin and D.B. Fuchs, Funct. Anal. Appl. 17, 241–242 (1983).
[43] S. Lukyanov, Phys. Rev. B 59, 11163–11164 (1999); arXiv:cond-mat/9809254.
[44] T. Hikihara, A. Furusaki and S. Lukyanov, Phys. Rev. B 96, 134429 (2017); arXiv:1706.02538.
[45] R. Couvreur, J.L. Jacobsen and H. Saleur, Phys. Rev. Lett. 119, 040601 (2016); arXiv:1611.08506.
[46] G.A. Kotousov and S.L. Lukyanov, Nucl. Phys. B 947, 114748 (2019); arXiv:1906.07081.
[47] F. Alcaraz, M.N. Barber and M.T. Batchelor, Ann. of Phys. 182, 280 (1988).
[48] E. Granet and J.L. Jacobsen, J. High Energ. Phys. 2020, 178 (2020).; arXiv:1910.07797.
[49] Z. Bajnok, E. Granet, J.L. Jacobsen and R.I. Nepomechie, J. High Energ. Phys. 2020, 177 (2020);
arXiv:1910.07805.
[50] O. Shevchuk, “Classiﬁcation of States in the XXZ model”, Master’s thesis published at the “Science in
Progress” webpage of Universiteit van Amsterdam (2012).
[51] N.A. Slavnov, Algebraic Bethe ansatz , Lecture notes for a course given in the Scientiﬁc and Educational
Center of Steklov Mathematical Institute in Moscow (2018); arXiv:1804.07350
[52] R. Bondesan, J. Dubail, A. Faribault and Y. Ikhlef, J. Phys. A: Math. Theor. 48, 065205 (2015);
arXiv:1409.8590.
[53] A. Doikou and R.I. Nepomechie, Parity and charge conjugation symmetries and S matrix of the XXZ
chain, in Statistical physics on the eve of the twenty-ﬁrst century (World Scientiﬁc, Singapore, 1999);
arXiv:hep-th/9810034.
60
[54] V.G. Kac and A.K. Raina, Highest weight representations of inﬁnite dimensional Lie algebras , World
Scientiﬁc, Singapore (1987).
[55] K. Johnson, Nuovo Cimento 20 773 (1961).
[56] G. Kato, M. Shiroishi, M. Takahashi and K. Sakai, J. Phys. A: Math. Gen. 36 L337 (2003);
arXiv:cond-mat/0304475.
[57] M. Takahashi, J. Phys. C: Solid State Phys. 10 1289 (1977).
[58] N. Kitanine, J.M. Maillet and V. Terras, Form factors of the XXZ Heisenberg spin-1/2 ﬁnite chain Nucl.
Phys. B 554 647–678 (1999); arXiv:math-ph/9807020.
[59] C. Candu and H. Saleur, Nucl. Phys. B 808, 441–486 (2009); arXiv:0801.0430.
61

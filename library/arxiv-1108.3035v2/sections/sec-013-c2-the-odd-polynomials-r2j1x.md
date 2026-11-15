---
doc_id: arxiv-1108.3035v2
doc_title: "Random Matrix Theory for the Hermitian Wilson Dirac Operator and the chGUE – GUE Transition"
section_id: sec-013-c2-the-odd-polynomials-r2j1x
section_title: "C.2 The odd polynomials R2j+1(x)"
section_number: null
pages: 24-27
source_pdf: 1108.3035v2.pdf
source_sha256: 935bf1bd3e13821b
toc_source: outline
doc_brief: "Random Matrix Theory for the Hermitian Wilson Dirac Operator and the chGUE – GUE Transition — We introduce a random two-matrix model interpolating between a chiral Hermitian (2n + ν) × (2n+ν) matrix"
---
The odd polynomials R2j+1(x)
In this subsection we construct the odd set of skew orthogonal polynomials directly from the even
ones by diﬀerentiation. Instead we could have computed the R2j+1(x) again from the supersymmetric
method as in the previous subsection, using the relation [38] R2n+1(x) = ⟨det[x −/D5](x + Tr /D5)⟩2n.
Based on our result above eq. (C.10) for ν = 0 R2n(x) = ⟨det[x −/D5]⟩2n we deﬁne
R2j+1(x)
≡
−2a2w(x)−1 d
dx
h
w(x)R2j(x)
i
,
(C.11)
w(x)
≡
exp[−x2/(4a2)] .
(C.12)
In the following we will show by direct computation that these satisfy the skew-orthogonality relations
eq. (4.8) with respect to the scalar product
⟨h, g⟩
=
Z
dxdy w(x)w(y)F(x −y)h(y)g(x) ,
(C.13)
F(x)
=
e
x2(1−a2)
8a2
"
erf
x
√
1 −a2
√
8a2
+
m
p
2a2(1 −a2)

+ erf
x
√
1 −a2
√
8a2
−
m
p
2a2(1 −a2)
#
.
Because the polynomials obviously have parity, Rj(−x) = (−)jRj(x), and because the weight is
antisymmetric, F(−x) = −F(x), it holds
⟨R2j, R2l⟩= 0 = ⟨R2j+1, R2l+1⟩.
(C.14)
Furthermore, the even polynomials are skew-orthogonal to all polynomials of lower degree, as can be
seen from eq. (C.4),
⟨R2j, R2l+1⟩= 0 , for j > l.
(C.15)
It remains to investigate the remaining cases. For j < l we have
⟨R2j, R2l+1⟩
=
−2a2
Z
dxdyw(y)F(x −y)R2j(y) d
dx
h
w(x)R2l(x)
i
=
−2a2
Z
dxdyw(x)w(y)dF(x −y)
dy
R2j(y)R2l(x)
=
2a2
Z
dxdyw(x)F(x −y)R2l(x) d
dy
h
w(y)R2j(y)
i
= 0 .
(C.16)
After a ﬁrst integration by parts with respect to x we have used dF (x−y)
dx
= −dF (x−y)
dy
, and a second
integration by parts with respect to y yields zero after using eq. (C.15).
It remains to compute the only nonvanishing product for j = l:
⟨R2j, R2j+1⟩
=
2a2
Z
dxdyw(x)w(y)dF(x −y)
dx
R2j(y)R2l(x)
=
Z
dxdyw(x)w(y)1 −a2
2
(x −y)F(x −y)R2j(y)R2l(x)
+
r
2a2(1 −a2)
π
e
−
m2
2a2(1−a2)
Z
dxdyw(x)w(y)

e
m(x−y)
2a2
+ e
−m(x−y)
2a2

R2j(y)R2l(x)
=
a2(1 −a2)
Z
dxdy
dw(x)
dx
w(y) −w(x)dw(y)
dy

F(x −y)R2j(x)R2j(y)
+2
r
2a2(1 −a2)
π
e
−
m2
2(1−a2)
Z
dxw(x −m)R2j(x)
Z
dyw(y + m)R2j(y) .
(C.17)
In the ﬁrst step we simply integrate by parts. We then observe that the ﬁrst line in the last equation
is proportional to ⟨R2j, R2j+1⟩because when the derivatives also act on the polynomials R2j(x) and
R2j(y) this gives zero as the polynomials R2j are skew-orthogonal to all lower order polynomials.
Putting this term on the left hand side and using parity we obtain
a2⟨R2j, R2j+1⟩= 2
r
2a2(1 −a2)
π
e
−
m2
2(1−a2)
Z
dxw(x −m)R2j(x)
2
.
(C.18)
In a last step we have to evaluate the integral over the weighted even polynomials. Using eq. (C.10)
we have
Z
dxw(x −m)R2j(x)
=
j! (2(1 −a2))j
(−)j√π
Z ∞
−∞
dx e−(x−m)2
4a2
Z ∞
−∞
dt e−t2Lj
(x + 2iat)2 −m2
2(1 −a2)

=
j! (2(1 −a2))j
(−)j√π
1
2a
Z ∞
−∞
dxds e−s2+x2
4a2 Lj
x2 + 2isx −s2 + 2m(x + is)
2(1 −a2)

=
j! (2(1 −a2))j
(−)j√π
2aπ .
(C.19)
In the last but one line we can change to complex coordinates z = x+is and to an integration over the
full complex plane. Because of the argument of Ln(z(z + 2m)/2(1 −a2)) the angular integration will
give zero for all powers of the argument z, except for the constant term z0 which is unity, Ln(0) = 1.
Collecting all factors we thus obtain
rj = ⟨R2j, R2j+1⟩= 8
√
2π a 22j(j!)2(1 −a2)2j+ 1
2 e
−
m2
2(1−a2) .
(C.20)
References
[1] E. V. Shuryak and J. J. M. Verbaarschot, Nucl. Phys. A 560, 306 (1993) [hep-th/9212088].
[2] J. J. M. Verbaarschot and I. Zahed, Phys. Rev. Lett. 70, 3852 (1993) [hep-th/9303012];
J. J. M. Verbaarschot, Phys. Rev. Lett. 72, 2531 (1994) [hep-th/9401059].
[3] J. J. M. Verbaarschot, “Applications of Random Matrix Theory to QCD”, chapter 32 in The
Oxford Handbook of Random Matrix Theory, Oxford University Press, Oxford (2011), Eds. G.
Akemann, J. Baik, and P. Di Francesco [arXiv:0910.4134];
P. H. Damgaard, “Chiral Random Matrix Theory and Chiral Perturbation Theory”, Lectures at
the XIV Mexican School on Particles and Fields 2010, arXiv:1102.1295v1 [hep-ph].
[4] G. Akemann, P. H. Damgaard, U. Magnea and S. Nishigaki, Nucl. Phys. B 487, 721 (1997)
[hep-th/9609174];
E. Kanzieper and V. Freilikher, Phil. Mag. B 77, 1161 (1998) [cond-mat/9704149v1];
A.B.J. Kuijlaars and M. Vanlessen, Commun. Math. Phys. 243 (2003) 163 [math-ph/0305044].
[5] P. H. Damgaard and S. M. Nishigaki, Nucl. Phys. B 518, 495 (1998) [hep-th/9711023].
[6] T. Wilke, T. Guhr, and T. Wettig, Phys. Rev. D 57, 6486 (1998) [hep-th/9711057].
[7] S. M. Nishigaki,
P. H. Damgaard,
and T. Wettig,
Phys. Rev. D 58, 087704 (1998)
[hep-th/9803007];
P. H. Damgaard and S. M. Nishigaki, Phys. Rev. D 63, 045012 (2001) [hep-th/0006111].
[8] T. Nagao and P. J. Forrester, Nucl. Phys. B 509, 561 (1998).
[9] G. Akemann and P. H. Damgaard, Phys. Lett. B 583, 199 (2004) [hep-th/0311171].
[10] P. H. Damgaard, J. C. Osborn, D. Toublan and J. J. M. Verbaarschot, Nucl. Phys. B 547, 305
(1999) [hep-th/9811212];
D. Toublan and J. J. M. Verbaarschot, Nucl. Phys. B 603, 343 (2001) [hep-th/0012144];
K. Splittorﬀand J. J. M. Verbaarschot, Phys. Rev. Lett. 90, 041601 (2003) [cond-mat/0209594];
Nucl. Phys. B 683, 467 (2004) [hep-th/0310271]; Nucl. Phys. B 695, 84 (2004) [hep-th/0402177];
Y. V. Fyodorov and G. Akemann, JETP Lett. 77, 438 (2003) [Pisma Zh. Eksp. Teor. Fiz. 77,
513 (2003)] [cond-mat/0210647];
F. Basile and G. Akemann, JHEP 0712, 043 (2007) [arXiv:0710.0376 [hep-th]].
[11] J. Gasser and H. Leutwyler, Phys. Lett. B 184, 83 (1987) .
[12] G. Akemann, F. Basile, and L. Lellouch, JHEP 0812 , 069 (2008) [arXiv:0804.3809 [hep-lat]];
P. H. Damgaard, T. DeGrand and H. Fukaya, JHEP 0712, 060 (2007) [arXiv:0711.0167 [hep-lat]].
[13] P. H. Damgaard and H. Fukaya, JHEP 0901 , 052 (2009) [arXiv:0812.2797 [hep-lat]].
[14] C. Lehner, J. Bloch, S. Hashimoto, and T. Wettig JHEP 05, 115 (2011) [arXiv:1101.5576v2
[hep-lat]].
[15] G. Akemann, J. C. Osborn, K. Splittorﬀ, and J.J.M. Verbaarschot Nucl. Phys. B 712, 287 (2005)
[hep-th/0411030].
[16] P. H. Damgaard, U. M. Heller, K. Splittorﬀ, and B. Svetitsky, Phys. Rev. D 72 , 091501 (2005)
[hep-lat/0508029].
[17] G. Akemann, P. H. Damgaard, J. C. Osborn and K. Splittorﬀ, Nucl. Phys. B 766, 34 (2007);
Erratum-ibid. B 800, 406 (2008) [hep-th/0609059].
[18] R. G. Edwards, U. M. Heller, J. E. Kiskis, and R. Narayanan, Phys. Rev. Lett. 82, 4188
(1999)[hep-th/9902117].
[19] H. Fukaya et al. [JLQCD and TWQCD collaborations], Phys. Rev. D 83, 074501 (2011)
[arXiv:1012.4052 [hep-lat]].
[20] P. H. Damgaard, K. Splittorﬀand J. J. M. Verbaarschot, Phys. Rev. Lett. 105, 162002 (2010).
[arXiv:1001.2937 [hep-th]].
[21] G. Akemann, P. H. Damgaard, K. Splittorﬀ, and J. J. M. Verbaarschot, Phys. Rev. D 83, 085014
(2011) [arXiv:1012.0752v2 [hep-lat]].
[22] M. Goltermann, “Applications of chiral perturbation theory to lattice QCD”, Lectures at Les
Houches School ”Modern perspectives in lattice QCD” 2009 arXiv:0912.4042v4 [hep-lat];
S. R. Sharpe, “Applications of Chiral Perturbation theory to lattice QCD”, Lectures at ILFTN
Workshop ”Perspectives in Lattice QCD” 2005 hep-lat/0607016v2.
[23] S. R. Sharpe, Phys. Rev. D 74, 014512 (2006) [hep-lat/0606002].
[24] A. Shindler, Phys. Lett. B 672, 82 (2009) [arXiv:0812.2251 [hep-lat]];
O. B¨ar, S. Necco, and S. Schaefer, JHEP 0903, 006 (2009) [arXiv:0812.2403 [hep-lat]].
[25] S. Necco, A. Shindler, JHEP 1104 , 031 (2011) [arXiv:1101.1778 [hep-lat]].
[26] G. Akemann, P. H. Damgaard, K. Splittorﬀ, and J. J. M. Verbaarschot, Proceedings of the XXVIII
International Symposium on Lattice Field Theory, PoS (Lattice 2010) 079 [arXiv:1011.5121v1
[hep-lat]].
[27] K. Splittorﬀand J. J. M. Verbaarschot, arXiv:1105.6229v1 [hep-lat].
[28] A. Pandey and M. L. Mehta, Commun. Math. Phys. 87, 449 (1983);
M. L. Mehta and A. Pandey, J. Phys. A: Math. Gen. 16 2655 (1983).
[29] M. L. Mehta, Random Matrices, Academic Press, Third Edition, London (2004).
[30] P. J. Forrester, T. Nagao, and G. Honner, Nucl. Phys. B 553, 601 (1999) [cond-mat/9811142v1];
M. Katori and H. Tanemura, Probab. Th. Rel. Fields 138, 113 (2007) [arXiv:math/0506187].
[31] Harish–Chandra, Am. J. Math. 79 (1957) 87;
C. Itzykson and J. B. Zuber, J. Math. Phys. 21, 411 (1980).
[32] T. Nagao and P. Forrester, Nucl. Phys. B 530 [PM] (1998), 742; Nucl. Phys. B 563, 547 (1999);
T. Nagao, Nucl. Phys. B 602, 622 (2001); J. Stat. Phys. 129, 1137 (2007) [arXiv:0708.2036[math-
ph]].
[33] E. Br´ezin and S. Hikami, Phys. Rev. E 57, 4140 (1998) [cond-mat/9804023v1].
[34] M. Kieburg and T. Guhr, J. Phys. A: Math. Theor. 43, 075201 (2010) [arXiv:0912.0654].
[35] I. S. Gradshteyn and I. M. Ryzhik, Table of Integrals, Series, and Products, Academic Press,
Sixth Edition, SanDiego (2000).
[36] M. Kieburg and J. J. M. Verbaarschot, private communication.
[37] B. Schlittgen and T. Wettig, J. Phys. A: Math. Gen. 36, 3195 (2003) [math-ph/0209030v2].
[38] G. Akemann, M. Kieburg, and M. J. Phillips, J. Phys.
A: Math. Theor. 43, 375207 (2010)
[arXiv:1005.2983v2 [math-ph]].
[39] G. Akemann, M. J. Phillips, and H.-J. Sommers, J. Phys. A: Math. Theor. 42, 012001 (2009)
[arXiv:0810.1458v1 [math-ph]].

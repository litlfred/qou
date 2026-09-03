---
doc_id: arxiv-1001.2937v3
doc_title: "Microscopic Spectrum of the Wilson Dirac Operator"
section_id: sec-003-2-strzuu1ˆa2stru2u2
section_title: "Str(Z[U−U−1])−ˆa2Str(U2+U−2)"
section_number: 2
pages: 3-4
source_pdf: 1001.2937v3.pdf
source_sha256: ab44349bc21634ff
doc_brief: "Microscopic Spectrum of the Wilson Dirac Operator — 4 sections: Str(M[U−U−1])+i 1; Str(Z[U+U−1])+ˆa2Str(U2+U−2); Str(M[U+U−1])+ 1"
---
is now convergent. Repeating the steps leading to (7)
with this convergent integral, we ﬁnd a resolvent for an
operator that, unlike D5, is not Hermitian. We believe
that the absence of solutions in the p-regime [12] for W8 <
0 has the same origin.
The ensemble with the structure of the matrix ˜DW
belongs to one of the classes in the non-Hermitian clas-
siﬁcation of [19] (the γ5-Hermiticity is there referred to
as Q-symmetry). In the microscopic scaling limit, the
partition function (10) has the determinantal structure
Zν
Nf ( ˆm, ˆz; ˆa) = det[Zν+i−j
Nf=1 ( ˆm, ˆz; ˆa)]i,j=1...Nf (12)
where
Zν
1 =
Z π
−π
dθ
2π eiθνe ˆm cos(θ)+iˆz sin(θ)−2ˆa2 cos(2θ). (13)
This form suggests that the partition function is a τ-
function of an integrable system of Toda type and that
an eigenvalue representation can be obtained.
The simplest quantity to compute from (12) is the chi-
ral condensate, Σ( ˆm) = ∂ˆm log Z.
For ν = 0 there is
a striking similarity to the chiral condensate for QCD
at non-zero isospin chemical potential µ. The conden-
sate is constant for large ˆm and drops roughly linearly
to zero inside a well deﬁned region (the Aoki phase and
the pion condensed phase, respectively). This is not ac-
cidental: The microscopic spectrum of DW at a̸ = 0
forms a thin strip along the imaginary axis just as the
continuum Dirac operator does at µ̸ = 0. In both cases,
the chiral condensate can be interpreted as the electric
ﬁeld at m of point charges at the position of the eigen-
values. Also the convergence requirements of the graded
partition function (5) have direct analogues at nonzero
chemical potential [20].
The Density of Real Modes.
The analytical result for
the quenched average spectral density of the real eigen-
values, denoted by ρν
Wreal, also follows from the generat-
ing function (5) (a derivation will be given in [21]). A
plot of ρν
Wreal for ν = 4 versus ˆζ ≡ζΣV is shown in
Fig. 3. The real eigenvalues, ζi, of DW repel each other
and the |ν| = 4 real modes are clearly visible. We have
checked that the distribution is in agreement with the
chiral Random Matrix Theory (10). This illustrates that
in the label ν introduced in (3) corresponds to the num-
ber of real eigenvalues. For large ν we ﬁnd that ρν
Wreal
approaches a semi-circle. We suggest that analyzing just
these real eigenmodes of DW may provide a new useful
tool in lattice QCD.
4
-4
-2
0
2
4
ξ
0
0.2
0.4
0.6
0.8
1
ρ
ν
Wreal(ξ;a)
ν=4 ,  a=0.2
FIG. 3: The quenched density of the real eigenvalues of DW .
Distribution of Tail States.
For |ˆx −ˆm|/ˆa2 ≫1 and
8ˆa2 ≪1 the tail of the spectral density inside the gap
follows from a saddle point analysis. For ˆx > 0 we ﬁnd
ρ5(ˆx) ∼exp[−(ˆx −ˆm)2/16ˆa2],
(14)
and a similar result for ˆx < 0. This result applies to the
tail of the blue and (marginally) of the red curve in Fig. 1.
Reinstating physical parameters we ﬁnd that the width
parameter, σ, in (14) is given by σ2 = 8a2W8/(V Σ2) so
that, in the microscopic domain and suﬃciently small ˆa,
σ scales with 1/
√
V . Such a scaling has been observed
for Nf = 2 in [13, 22].
Tail states may also be studied in their own right and
for applications in condensed matter physics. In particu-
lar, in the thermodynamic limit, ˆm, ˆx, ˆa2 ≫1, the aver-
age level density of D5 can be obtained by a saddle point
analysis. For 8ˆa2/ ˆm < 1 it vanishes inside [−ˆxc, ˆxc] with
ˆxc given by ˆxc = 8ˆa2 
( ˆm/8ˆa22/3 −1]3/2. It has exactly
the same form as for superconductors with magnetic im-
purities [2]. In the scaling limit where V 2/3(xc −x) is
kept ﬁxed, the spectral density can be computed inside
the gap by a saddle point approximation of (5), and it
agrees with universal Random Matrix Theory results for
the so-called soft edge. Such universal behaviour has also
been found in condensed matter systems [2, 3].
Conclusions. Using a graded chiral Lagrangian for Wil-
son fermions at ﬁnite lattice spacings, we have obtained
an analytical form for the Wilson Dirac spectrum at ﬁxed
number, ν, of real eigenvalues. These results, and their
extensions to dynamical fermions, should be useful for
lattice simulations at ﬁnite volume. We have shown how
the leading low-energy constant for Wilson fermions, W8,
can be extracted from lattice spectra of the Wilson Dirac
operator in the ǫ-regime.
The problem can also be reformulated in terms of a
new chiral Random Matrix Theory that describes spec-
tral correlation functions of the Wilson Dirac operator
in the appropriate scaling regime.
These results open
a new domain of Random Matrix Theory where chiral
ensembles merge with Wigner-Dyson ensembles. Essen-
tial to this study is an analysis of the gap of the Wilson
Dirac operator at ﬁnite mass. Lattice QCD simulations
depend crucially on control of this gap and its variation
as a function of the lattice spacing. As we have stressed,
our results are not only important for understanding the
ﬁnite lattice spacing eﬀects of Wilson fermions near the
chiral limit, but may have interesting applications to tail
states in condensed matter systems.
Acknowledgments: This work was supported by U.S.
DOE Grant No. DE-FG-88ER40388 (JV) and the Dan-
ish Natural Science Research Council (KS). We thank B.
Simons, M. L¨uscher and P. de Forcrand for discussions.
[1] I.M. Lifshitz, Sov. Phys. Usp. 7, 549 (1965).
[2] A. Lamacraft and B. D. Simons, Phys. Rev. Lett. 85,
4783 (2000); Phys. Rev. B 64, 014514 (2001).
[3] C.W.J. Beenakker, Lect. Notes in Phys. 667 131 (2005).
[4] E.V. Shuryak and J.J.M. Verbaarschot, Nucl. Phys.
A560, 306 (1993); J.J.M. Verbaarschot, Phys. Rev. Lett.
72, 2531 (1994).
[5] G. Akemann, P. H. Damgaard, U. Magnea and S. Nishi-
gaki, Nucl. Phys. B 487, 721 (1997).
[6] P. H. Damgaard,
J. C. Osborn,
D. Toublan and
J. J. M. Verbaarschot, Nucl. Phys. B 547, 305 (1999).
[7] J. Gasser and H. Leutwyler, Phys. Lett. B 188, 477
(1987); H. Leutwyler and A. V. Smilga, Phys. Rev. D
46, 5607 (1992).
[8] S. Aoki, Phys. Rev. D 30, 2653 (1984).
[9] S. R. Sharpe and R. L. Singleton, Phys. Rev. D 58,
074501 (1998); Rupak and N. Shoresh, Phys. Rev.
D
66, 054503 (2002); O. Bar, G. Rupak and N. Shoresh,
Phys. Rev.
D 70, 034508 (2004); S. R. Sharpe and
J. M. S. Wu, Phys. Rev. D 70, 094029 (2004); M. Golter-
man, S. R. Sharpe and R. L. Singleton, Phys. Rev. D 71,
094503 (2005).
[10] F. Farchioni et al., Eur. Phys. J. C 39, 421 (2005);
C. Michael and C. Urbach, PoS LAT2007, 122 (2007);
P. Boucaud et al., Comput. Phys. Com. 179, 695 (2008).
[11] K. M. Bitar, U. M. Heller and R. Narayanan, Phys. Lett.
B 418, 167 (1998).
[12] S. R. Sharpe, Phys. Rev. D 74, 014512 (2006).
[13] L. Del Debbio, L. Giusti, M. Luscher, R. Petronzio and
N. Tantalo, JHEP 0602, 011 (2006).
[14] A. Shindler, Phys. Lett. B 672, 82 (2009) O. Bar,
S. Necco and S. Schaefer, JHEP 0903, 006 (2009).
[15] R. Kaiser, H. Leutwyler, Eur. Phys. J. C 17, 623 (2000).
[16] S. R. Sharpe, Phys. Rev. D 79, 054503 (2009).
[17] K. Splittorﬀand J. J. M. Verbaarschot, Phys. Rev. Lett.
90, 041601 (2003).
[18] L. Giusti and M. Luscher, JHEP 0903, 013 (2009).
[19] U. Magnea, arXiv:0707.0418v2 [math-ph].
[20] K. Splittorﬀand J. J. M. Verbaarschot, Nucl. Phys. B
683, 467 (2004); Nucl. Phys. B 757, 259 (2006).
[21] G. Akemann, P.H. Damgaard, K. Splittorﬀand J.J.M.
Verbaarschot, to appear.
[22] L. Del Debbio, L. Giusti, M. Luscher, R. Petronzio and
N. Tantalo, JHEP 0702, 082 (2007).

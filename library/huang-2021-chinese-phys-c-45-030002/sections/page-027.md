---
doc_id: huang-2021-chinese-phys-c-45-030002
doc_title: "The AME 2020 atomic mass evaluation (I). Evaluation of input data, and adjustment procedures"
section_id: page-027
section_title: "Page 27"
section_number: null
pages: 27-27
source_pdf: Huang_2021_Chinese_Phys._C_45_030002.pdf
source_sha256: 1dd3329ed87476c8
toc_source: undetermined
doc_brief: "The AME 2020 atomic mass evaluation (I). Evaluation of input data, and adjustment procedures — 343 sections: Page 1; Page 2; Page 3"
---
Chinese Physics C
Vol. 45, No. 3 (2021) 030002
where
y1
=
Mr
(
R q
qr
−C
)
,
(14)
y2
=
me q(1−R),
(15)
y3
=
Ar
( q
qr
R−A
Ar
)
,
(16)
and
y4
=
R q
qr
(Br −Dr)−(B −D).
(17)
To ﬁx relative orders of magnitude, Mr is generally
smaller than 0.1 u, R−C is a few 10−4, (1−R) is usu-
ally smaller than unity (and typically 0.2 for a 20% mass
change), R−A
Ar varies from 1 to 100×10−6, (Br −Dr) is
generally smaller than 0.1 µu, and Ar is typically 100 u
for atomic mass A = 100.
The four terms y1, y2, y3,
and y4 take values of the order of 10 µu, 100 µu, 10 to
10000 µu, and 0.1 µu, respectively.
The associated precision dy is written:
dy
=
dy1 +dy2 +dy3 +dy4 ,
(18)
where
dy1
=
q
qr
Mr dR+
(
R q
qr
−C
)
dMr ≃dR×105 µu,
(19)
dy2
=
me q dR ≃dR×103 µu,
(20)
dy3
=
q
qr
Ar dR ≃dR×108 µu,
(21)
and
dy4
=
q
qr
(Br −Dr) dR+R q
qr
(dBr −dDr)
−(dB −dD) ≃dR×10−1 µu.
(22)
Consequently, only the 3rd term contributes signiﬁ-
cantly to the precision of the measurement, and so we
write: dy
=
dy3.
If the two frequencies are measured with a typical
precision of 10−7 for ions at A = 100, then the precision
on the frequency ratio R is 1.4×10−7 and the precision
on the mass is approximatively 14 µu.
Next we will illustrate how to calculate the molec-
ular binding energy for the most precise Penning trap
experiment.
A.1
Bond Dissociation Energy
The bond dissociation energy D is a quantity which
signiﬁes the strength of a chemical bond. The bond dis-
sociation energy for a bond A–B, which is broken through
reaction:
AB →A + B
is deﬁned as the standard enthalpy change at a speciﬁed
temperature[35]:
Do(AB) = ∆Hf o
0 (A)+∆Hf o
0 (B)−∆Hf o
0 (AB),
(23)
where ∆Hf o
0 is the standard heat of formation and its
value is available for a large number of atoms and com-
pounds on Nist Chemistry Webbook [36]. All Do values
refer to the gaseous state at temperature either 0 K or
298 K. When data on the standard heat of formation is
absent at 0 K, Do(AB) will be converted to Do
298(AB) by
the approximation:
Do
298(AB) ≈Do(AB)+3.72 kJ/mol.
(24)
Unlike diatomic molecules which involve only one bond,
polyatomic molecules have several bonds and their D’s
are the sum of all the single bonds. For example, if one
wants to know the dissociation energy of CH4, one needs
to calculate the dissociation energy of the four bonds
CH3–H, CH2–H, CH–H, and C–H, respectively:
Do(CH3 −H) = ∆Hf o
0 (CH3)+∆Hf o
0 (H)−∆Hf o
0 (CH4),
Do(CH2 −H) = ∆Hf o
0 (CH2)+∆Hf o
0 (H)−∆Hf o
0 (CH3),
Do(CH−H) = ∆Hf o
0 (CH)+∆Hf o
0 (H)−∆Hf o
0 (CH2),
Do(C−H) = ∆Hf o
0 (C)+∆Hf o
0 (H)−∆Hf o
0 (CH).
(25)
Summing over all four bonds above, we can obtain:
Do(CH4) = D(CH3 −H)+D(CH2 −H)
+D(CH−H)+D(C−H)
= ∆Hf o
0 (C)+4×∆Hf o
0 (H)−∆Hf o
0 (CH4).
The dissociation energy can be generalized for a poly-
atomic molecule which has the form AnBkCi:
Do(AnBkCi) = n∆Hf o
0 (A)+k∆Hf o
0 (B)+i∆Hf o
0 (C)
−∆Hf o
0 (AnBkCi).
(26)
The ionization energies for molecules are available on
Nist Atomic Spectra Database [37]. We now illustrate
this treatment with one example.
A.1.1
13C2H+
2 and 14N+
2 mass doublet
In the work of [2004Ra33], a cyclotron frequency ra-
tio R = 0.999421460888(7) of relative precision 7×10−12
has been obtained for ions 13C2H+
2 and 14N+
2 . We ﬁrst
calculate Do(C2H2) by applying Eq. 26:
Do(C2H2) = 2×∆Hf o
0 (C)+2×∆Hf o
0 (H)−∆Hf o
0 (C2H2)
= 2×716.68+2×218.998−227.40
= 1641.956 kJ/mol
= 17.018 eV.
Do(N2) = 944.9 kJ/mol = 9.793 eV is obtained from
Ref. [38], since ∆Hf o
0 (N2) is not on the list of [36]. Com-
bining the ionization energy B(C2H2) = 11.400 eV and
B(N2) = 15.581 eV, we obtain the mass diﬀerence:
13C+H−14 N = 8105.862995(98) µu.
030002-26

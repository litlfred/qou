---
doc_id: huang-2021-chinese-phys-c-45-030002
doc_title: "The AME 2020 atomic mass evaluation (I). Evaluation of input data, and adjustment procedures"
section_id: page-026
section_title: "Page 26"
section_number: null
pages: 26-26
source_pdf: Huang_2021_Chinese_Phys._C_45_030002.pdf
source_sha256: 1dd3329ed87476c8
toc_source: undetermined
doc_brief: "The AME 2020 atomic mass evaluation (I). Evaluation of input data, and adjustment procedures — 343 sections: Page 1; Page 2; Page 3"
---
Chinese Physics C
Vol. 45, No. 3 (2021) 030002
very precise (n,γ) reactions with β+, β−and ε de-
cay energies versus direct Penning-trap data [2011Go23].
We ﬁnally decided at that time to provisionally not
use the new Penning trap result and called for more
measurements in order to clarify this issue.
In the
Ame2016 evaluation, we were aware of the experimen-
tal results for 102Pd and 103Pd from the Esr mass mea-
surements through a private communication [2014Ya.A].
Their results support the Shiptrap datum, although
with relatively large uncertainties.
We therefore de-
cided to discard two pieces of data: 102Rh(β−)102Pd and
103Pd(ε)103Rh, and to use the Shiptrap result. The lo-
cal consistency was then restored.
The treatment is now further supported by the recent
results from Jyfltrap [2019Ne04]. The mass diﬀerence
of 102Pd and 102Ru was measured using both the Time-of-
Flight and the Phase-Imaging Ion Cyclotron Resonance
techniques. The obtained result is around 8 times more
precise and in excellent agreement with the value ob-
tained at Shiptrap, verifying the reliability of the Pen-
ning trap mass spectrometry. This issue is thus consid-
ered to be resolved.
7
General information
The full content of the present issue is accessible on-
line at the Amdc website [27].
In addition to several
graphs representing the mass surface, beyond the main
ones given in Part II, are available on the Amdc website.
Tables of masses (Part II, Table I) and nuclear re-
action and separation energies (Part II, Table III) are
available in Ascii format to simplify their input to com-
puter programs. The headers of these ﬁles give informa-
tion on the formats. The ﬁrst ﬁle, named mass.mas20,
contains the table of masses. The next two ﬁles corre-
spond to the table of reaction and separation energies,
in two parts of 6 entries each, as in Part II, Table III:
rct1.mas20 for S2n, S2p, Qα, Q2β, Qεp and Qβn (odd
pages in this issue); and rct2.mas20 for Sn, Sp, Q4β,
Qd,α, Qp,α and Qn,α (facing even pages).
8
Acknowledgments
This work is supported in part by the National Key
Research and Development Program of China (Grant No.
2016YFA0400504), the Strategic Priority Research Pro-
gram of Chinese Academy of Sciences (CAS, Grant No.
XDB34000000), the U.S. Department of Energy, Oﬃce
of Science, Oﬃce of Nuclear Physics, under Contract No.
DE-AC02-06CH11357.
W.J.H. acknowledges ﬁnancial
support by the Max-Planck-Society. S.N. acknowledges
the support of the RIKEN Pioneering Project Funding.
We wish to thank our many colleagues who provided
answers to our questions regarding speciﬁc experimen-
tal data, as well as those who sent us preprints of their
work prior to publication. Continuing interest, discus-
sions, suggestions and encouragements from D. Lunney
are highly appreciated.
Appendix A
Converting frequency ratios
to linear equations
Primary data from Penning-trap measurement are
typically given in the form of a frequency ratio, which
is converted to a linear equation of atomic masses in
the Ame. The code of a Fortran program for convert-
ing frequency ratios to linear equations was given in
Ame2016 [2]. Here we just describe the principle of this
method.
In the following, quantities with the subscript r de-
scribe the characteristics of the reference ion in the Pen-
ning trap. Equivalent quantities, with no subscript, de-
scribe characteristics of the ion being measured.
In Ame2012 [24], the frequency ratio was described
as:
R = fr
f =
M−me q+B
Mr −me qr +Br
qr
q ,
(9)
This function is only valid for atoms. When molecules
are involved, an extra term for the molecular binding en-
ergy should be included. Therefore in Ame2016 [2], the
equation was rewritten as:
R = fr
f =
M−D−me q+B
Mr −Dr −me qr +Br
qr
q ,
(10)
where q is the charged state of the given ion, D is the
molecular binding energy (dissociation energy), B is the
electron binding energy, me is the mass of the electron
and M the total atomic mass. All masses and energies
are in atomic mass units u and so, u=1. This expression
can be written in terms of the mass excess M and atomic
mass number A:
A+M−D−meq+B = R q
qr
(Ar+Mr−Dr−meqr+Br) (11)
or, alternatively:
M −R q
qr
Mr = meq(1−R)
+
Ar( q
qr
R−A
Ar
)
+
R q
qr
(Br −Dr)−(B −D).
The general aim is to establish some quantity y and
its associated precision dy. We deﬁne C to be a trun-
cated, three-digit decimal approximation of the ratio A
to Ar, and then we can write:
y
=
M −C Mr
(12)
and so
y
=
y1 +y2 +y3 +y4 ,
(13)
030002-25

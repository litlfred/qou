---
doc_id: klein-few-body-systems-in-lattice-effective-field-theory-the
doc_title: "Few-body systems in lattice effective field theory"
section_id: sec-054-uncertainty-analysis
section_title: "Uncertainty analysis"
section_number: null
pages: 95-97
source_pdf: klein-few-body-systems-in-lattice-effective-field-theory-thesis.pdf
source_sha256: 7ecafdd08255d5c6
doc_brief: "Few-body systems in lattice effective field theory — 58 sections: Introduction and Motivation; The standard model of particle phy; Lattice QCD"
---
From the deﬁnition of χ2 given in Eq. (5.46), we note thatχ2 is a function of the LO and NLO coupling
constants
χ2
LO =χ2
(
C1S 0
, C3S 1
,
)
, (C.1)
χ2
N2LO =χ2 (C1,..., C10
), (C.2)
....
χ2 can be expanded around its minimum, giving
χ2 =χ2
min + 1
2
∑
i, j
hi j(Ci− Cmin
i )(C j− Cmin
j ) +..., (C.3)
where the Hessian matrix is denoted by
hi j≡ ∂2χ2
∂Ci∂C j
, (C.4)
and Cmin
i denotes the result of theχ2 ﬁt. Then the error (or variance-covariance) matrix is deﬁned as
Ei j≡ 1
2
[h−1]
i j, (C.5)
while the error of any ﬁt parameter is given by its standard deviation,
σi =
√
Eii. (C.6)
Following Ref. [116] we again ﬁnd a very largeχ due to the underestimation of the PW A errors. Hence
we have to rescaleχ2 in the case of the phase shift calculation to get reasonable error estimates. In this
case, we rescaleχ2 by
χ2→ Ndof
χ2
χ2
min
, (C.7)
such thatχ2/Ndof≈ 1 in the minimum [165, 166].
In the analysis, we also have to propagate the errors of the LECs to physical observables like phase shifts
89
Appendix C Uncertainty analysis
or binding energies. For a given observableO, we assign an uncertainty according to
∆O≡
√
(JT
O)iEi j(JO) j, (C.8)
where
(JO)i≡ ∂O
∂Ci
, (C.9)
is the Jacobian vector ofO with respect to the Ci.
90
APPENDIX D

---
doc_id: arxiv-2506.10206v2
doc_title: "Analytic dilogarithm identities"
section_id: sec-003-11-preliminaries
section_title: "Preliminaries"
section_number: 1.1
pages: 2-3
source_pdf: 2506.10206v2.pdf
source_sha256: d0631a9abd9b1da3
doc_brief: "Analytic dilogarithm identities — We introduce dilogarithm identities through a beta integral-based technique that we apply to provide analytic proofs of previously conjectured dilogarithm relations"
---
The Γ-function is among the most fundamental and ubiquitous special functions and may be
defined via the Euler integral Γ(x) :=
R∞
0 ux−1e−udu forℜ(x)> 0 [32, §2]. The beta integral
is of basic importance as a special function, in much the same way as the Γ-function, and
may be defined so that
B(p,q ) :=
Z 1
0
tp−1(1−t)q−1dt (2)
forℜ(p)> 0 andℜ(q)> 0 [32, §2.16], so that
B(p,q ) = Γ(p)Γ(q)
Γ(p +q), (3)
again forℜ(p) > 0 andℜ(q) > 0. Our main family of dilogarithm identities is derived, as
below, using (2) together with the families of sextic integrals shown in Section 2 below.
The dilogarithm function is a central object of study in our work and is given by the
m = 2 case of the polylogarithm function such that Lim(x) :=P∞
n=1
xn
nm for complex x such
that|x|≤ 1. For a full review of background material on the dilogarithm, we again refer to
the seminal monographs due to Lewin concerning this function [20, 23, 24]. By writing
L(x) := 6
π2

Li2(x) + 1
2 lnx ln(1−x)

(4)
to denote the Rogers L-function, a version of the five-term (Abel) functional equation such
that
L(x) +L(y) =L(xy) +L
x(1−y)
1−xy

+L
y(1−x)
1−xy

2
is to be applied in our work. Other fundamental functional equations for the dilogarithm
that are to arise in our work include the duplication formula such that

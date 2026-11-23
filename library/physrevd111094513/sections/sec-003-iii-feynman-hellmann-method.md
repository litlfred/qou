---
doc_id: physrevd111094513
doc_title: "Lattice QCD calculation of the Compton amplitude subtraction function"
section_id: sec-003-iii-feynman-hellmann-method
section_title: "III. FEYNMAN-HELLMANN METHOD"
section_number: null
pages: 3-4
source_pdf: PhysRevD.111.094513.pdf
source_sha256: c05dfaef1f1c2f98
toc_source: outline
doc_brief: "Lattice QCD calculation of the Compton amplitude subtraction function — 16 sections: Lattice QCD calculation of the Com; I. INTRODUCTION; II. BACKGROUND"
---
The Feynman-Hellmann (FH) method is a powerful tool
that presents an alternative to the direct calculation of three-
and four-point functions in lattice QCD. In particular,
Feynman-Hellmann has proven particularly important in
the case of matrix elements with two current insertions such
as the Compton amplitude [28–32].
Here we summarize the main aspects of our application
of the Feynman-Hellmann method, noting that the full
details can be found in Ref. [29]. The starting point is to
perturb the action, S, by introducing external fields that
couple to the valence quarks of the nucleon. For a particular
choice of external field, Eq. (8), the ground-state energy of
the nucleon in the external field can be related to the
Compton amplitude, and thus the subtraction function, as
demonstrated in Ref. [29]. To access the flavor-diagonal
piece and the flavor-mixed piece of the Compton ampli-
tude, we perturb the action by
SðλÞ ¼ S þ λq
Z
d3zðeiq·z þ e−iq·zÞVq
μðzÞ;
SðλÞ ¼ S þ
X
q
λq
Z
d3zðeiq·z þ e−iq·zÞVq
μðzÞ;
ð8Þ
respectively, noting that q is the 3-momentum carried by
the external current, and Vq
μ ¼ ZV ¯ψqγμψq is the local
Euclidean vector current of the quark q ¼ u, d for some
choice of Lorentz index μ and with ZV denoting the
renormalization constant.
We implement these action modifications on the level of
quark propagators,
Sq
λqðzn −zmÞ ¼ ½M −λqO−1
n;m;
ð9Þ
where M is the fermion matrix, n, m are lattice sites and λq
is the FH coupling.
With the quark propagator in Eq. (9), the perturbed
proton correlators for different flavor combinations are
written generally, up to spin/color structure, as
Gðλu; λdÞ ∼hSu
λuSu
λuSd
λdi;
ð10Þ
where, for example, the flavor combination uu is given by
Gðλu; 0Þ ∼hSu
λuSu
λuSdi, with Sd denoting the unperturbed
down-quark propagator. Applying the general principles of
Refs. [29,30], we can write the ground state energy of the
nucleon in the external field as
Eðλu; λdÞ ¼ mp −λ2u
2mp
Suu
1 ðQ2Þ −λ2
d
2mp
Sdd
1 ðQ2Þ
−λuλd
2mp
½Sud
1 ðQ2Þ þ Sdu
1 ðQ2Þ þ    ;
ð11Þ
noting that the ellipsis denotes terms of higher order in λ,
Sud
1 ðQ2Þ ¼ Sdu
1 ðQ2Þ, and where Sqq0
1 ðQ2Þ is the contribution
to the subtraction function from
Tqq0
μν ðp; qÞ ¼ i
Z
d4z eiq·zhNðpÞjT fVq
μðzÞVq0
ν ð0ÞgjNðpÞi:
ð12Þ
This Feynman-Hellmann relation is only strictly valid
when the sink momentum is p ¼ 0. Information on the
p ≠0 case can be found in Ref. [29]. By definition q4 ¼ 0
in the FH procedure, and hence the probe scale is given by
Q2 ¼ jqj2. As explained further in the following section, in
our calculations we imposed a sink momentum of p ¼ 0
which, with q4 ¼ 0, ensures ω ¼ 0.
The proton subtraction function, up to disconnected
contributions, is then constructed via
Sp
1ðQ2Þ ¼
X
q;q0¼u;d
QqQq0Sqq0
1 ðQ2Þ
¼ 4
9Suu
1 ðQ2Þ þ 1
9Sdd
1 ðQ2Þ −2
9ðSud
1 ðQ2Þ þ Sdu
1 ðQ2ÞÞ:
ð13Þ
In terms of the diagrams in Fig. 2, the different flavor
combinations receive the contributions,
(i) uu: type I—V,
(ii) dd: type I, III—V
(iii) ud: type II—IV.
This distinction is particularly relevant to our discussion of
lattice artifacts. In the present work, we only consider
modifications to the action on the quark propagators, but
not the shift in the fermion determinant which will affect
the gauge field sampling. Our calculation therefore only
considers diagrams of type I and type II in Fig. 2. In
addition, type III and type IV contributions can be ignored
in the present calculation, as they vanish at the SU(3)
symmetric point. Since heavier quark contributions only
appear in the final three types of Fig. 2, Eq. (13) need only
include the up and down quark contributions.

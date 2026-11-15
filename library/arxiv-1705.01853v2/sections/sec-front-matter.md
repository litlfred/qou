---
doc_id: arxiv-1705.01853v2
doc_title: "Line Operators in the Standard Model"
section_id: sec-front-matter
section_title: "Front matter"
section_number: null
pages: 1-4
source_pdf: 1705.01853v2.pdf
source_sha256: 895e0b22c93bca1b
toc_source: inferred
doc_brief: "Line Operators in the Standard Model — There is an ambiguity in the gauge group of the Standard Model."
---
arXiv:1705.01853v2  [hep-th]  12 Jun 2017
Preprint typeset in JHEP style - HYPER VERSION
Line Operators in the Standard Model
David Tong
Department of Applied Mathematics and Theoretical Physics,
University of Cambridge, UK
d.tong@damtp.cam.ac.uk
Abstract: There is an ambiguity in the gauge group of the Standard Model. The
group is G = SU(3) × SU(2) × U(1)/Γ, where Γ is a subgroup of Z6 which cannot
be determined by current experiments. We describe how the electric, magnetic and
dyonic line operators of the theory depend on the choice of Γ. We also explain how the
periodicity of the theta angles, associated to each factor of G, diﬀer.
Contents
1.
Introduction
1
2.
A Review of Line Operators
3
3.
Line Operators in the Standard Model
7
3.1
Theta Angles
10
3.2
Electroweak Symmetry Breaking
12
4.
Summary
14
1. Introduction
At the parochial distance scales accessible by experiment, the world in which we live is
governed by the Standard Model. The gauge sector is one of the most beautiful con-
structs in theoretical physics, involving an intricate interplay between chiral fermions
to ensure the cancellation of anomalies. Indeed, the matter content in one generation
forms what is arguably the simplest non-Abelian four-dimensional chiral gauge theory.
Despite the fact that the Standard Model is built around the idea of gauge symme-
try, there is a little-advertised ambiguity in the choice of gauge group. We learn in
kindergarten that we should take
˜G = U(1) × SU(2) × SU(3)
But this is not quite accurate. Experimental considerations tell us only that the gauge
group is
G = ˜G/Γ
where Γ is a discrete group. As we review below, the matter content of the Standard
Model is invariant under a suitably chosen Z6 subgroup of ˜G. For this reason, it is
sometimes stated that one should take the gauge group to include the quotient Γ = Z6.
1
This, however, is putting the cart before the horse. At present, we can only say that
the gauge group involves a quotient by Γ, which is a subgroup of Z6, i.e.
Γ = Z6, Z3, Z2 or 1
Each of these possibilities deﬁnes a diﬀerent theory and, ultimately, gives rise to diﬀer-
ent physics. The obvious questions are: which describes our world? And how can we
tell?
These are diﬃcult questions to answer. Correlation functions of local operators in
R1,3 depend only on the Lie algebra of the gauge group and are unaﬀected by global
issues such as the choice of Γ. This means that no current experiment can distinguish
between the four possibilities1. Nonetheless, the physics in ﬂat space can depend in
subtle ways on Γ (and in more dramatic ways when spacetime has interesting topology).
The purpose of this paper is to describe the crudest diﬀerences between the theories:
the spectrum of line operators and the periodicities of theta angles.
The fact that the spectrum of line operators depends on the global structure of
the gauge group was emphasised by Aharony, Seiberg and Tachikawa [1]. The line
operators can be thought of as heavy electric and magnetic test particles which can be
used to probe the dynamics of the gauge ﬁelds. Roughly speaking, taking a quotient
restricts the allowed electric line operators but, in doing so, relaxes the constraint of
Dirac quantisation and so frees up the allowed magnetic line operators. The ﬁrst goal
of this paper is to classify the allowed line operators for each choice of Γ.
The authors of [1] also explained why the periodicity of θ-angles depends on the
global structure of the gauge group. The second goal of this paper is to understand
how the ranges of the various θ-angles in the Standard Model are aﬀected by the choice
of Γ. The θ-angle for SU(3) is much discussed and the smallness of its (un)observed
value, θ3 ≲10−10, is one of the great open problems in particle physics. In contrast
there is seemingly no mystery about the θ-angle for SU(2) since the existence of the
anomalous global B + L symmetry means that it can always be rotated away. (As we
will see in Section 3, this argument needs a small correction.)
Finally, there is also a θ-angle for U(1)Y hypercharge. This has received very little
attention in the literature and with good reason, for Abelian gauge groups have no ﬁnite
1The theoretical prejudice of uniﬁcation suggests that Γ = Z6, since only then is G is a subgroup of
SU(5) or Spin(10). It may well be true that this is the way Nature works. However, the philosophy of
this paper is to admit our ignorance of the ultra-violet, and instead use our knowledge of the infra-red
to restrict what we may ultimately ﬁnd as we explore higher energies.
2
action conﬁgurations carrying topological charge. This means that, unlike their non-
Abelian counterparts, the electric spectrum and correlation functions do not depend
on θY .
Nonetheless, Abelian θ-angles can change the physics in more subtle ways.
This happens, for example, in the magnetic sector through the Witten eﬀect [2, 3]. It
also happens when θ-angles vary in space or, relatedly, in the presence of boundaries.
Indeed, much of the rich and beautiful phenomenology of topological insulators can be
understood as a domain wall between θem = 0 and θem = π [4, 5]. We will see below
that the periodicity of θY is determined by Γ and that, after electroweak symmetry
breaking, this aﬀects the periodicity of the electromagnetic theta angle, which is a
particular combination of θ2 and θY .
The paper is organised as follows. Section 2 is a review of the results of [1], speciﬁcally
how the line operators and associated theta angles diﬀer for SU(N) and SU(N)/ZN.
Section 3 contains all the main results of the paper, including how the line operators and
θ-angles in the Standard Model depend on the choice of discrete quotient Γ. Particular
attention is paid to the values of θ for which the gauge sector is invariant under CP or,
equivalently, under time reversal. We also describe the fate of the line operators un-
der electroweak symmetry breaking, since this determines the allowed electromagnetic
charges of particles.
The distinctions between the diﬀerent gauge groups G = ˜G/Γ described here are
rather formal in nature. We end in Section 4 with some speculations on how these
distinctions may manifest themselves physically.

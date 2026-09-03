---
doc_id: arxiv-2105.09342v1
doc_title: "A Unitary Matrix Model for q-deformed Plancherel Growth"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-4
source_pdf: 2105.09342v1.pdf
source_sha256: 57ae12327da7b9a1
doc_brief: "A Unitary Matrix Model for q-deformed Plancherel Growth — In this paper we construct a unitary matrix model that captures the asymptotic growth of Young diagrams under q-deformed Plancherel measure."
---
2 q-deformed Plancherel growth 4
3 A unitary matrix model for q-deformed Plancherel growth 7
3.1 Solution class 1: No-gap solution . . . . . . . . . . . . . . . . . . . . . . . . 10
3.2 q-deformed automodel class . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
3.3 The unitary matrix model from the droplet picture . . . . . . . . . . . . . . 12
4 Asymptotic analysis of q-deformed Plancherel growth of second kind 15
Email addresses: suvankar@iiserb.ac.in (Suvankar Dutta), debangshu0@gmail.com (Debangshu
Mukherjee), neetuj@iiserb.ac.in (Neetu), sanhita18@iiserb.ac.in (Sanhita Parihar)
arXiv:2105.09342v1  [hep-th]  19 May 2021
5 The Hilbert space 17
5.1 Moments of Young diagrams and conserved charges . . . . . . . . . . . . . . 18
6 Conclusion 19
Appendix A q analog of GWW phase transition 20
Appendix B Explicit computation of the partition function 22
Appendix C Calculation of automodel density for the second class ` a la
Strahov 23
Appendix C.1 Computing Hconst(h),Hλ(h) and Hseries(h) . . . . . . . . . . . . 25
Appendix D Droplet quantisation 26
1. Introduction
The powerful techniques of random matrix models have been applied to numerous ﬁelds in
physics and mathematics. Quantum gravity in 2D, knot theory, integrable systems, number
theory, topological string theory, algebraic geometry are a few from the list of many. In
this paper, we study the asymptotic growth of Young diagrams, equipped with q analog of
Plancherel measure and show that one can write a unitary matrix model (UMM) to capture
such growth processes. The matrix model is a q analog of Gross-Witten-Wadia (GWW)
matrix model. The model exhibits a third order phase transition which isq-deformed version
of GWW phase transition. We observe that the no-gap phase of this UMM captures the
q-deformed Plancherel growth of Young diagrams. This is an extension of our earlier work
on asymptotic growth of Young diagrams under ordinary Plancherel measure [1].
Growth of Young diagrams is an important and interesting subject to study in mathe-
matics. All the Young diagrams with k boxes can be obtained by adding one box to all the
diagrams with k− 1 boxes in all possible allowed ways. Such a growth process is similar to
the growth of a 2 dimensional crystal. See ﬁg. 1. One can write a grand canonical partition
function for this process [1, 2]. Usually the growth depends on the probability of placing
a crystal unit or box at diﬀerent possible positions. A standard probability one assigns to
such a growth process is called Plancherel probability. It is proportional to the square of
the number of possibilities to obtain the shape of the crystal (Young diagram) with total k
number of units (boxes). It is easy to show that this number is equal to the dimension of
the corresponding Young diagram. Vershik and Kerov [3], and independently, Logan and
Shepp [4] studied such growth processes and showed that a growth under Plancherel measure
terminates at a universal shape, when the diagrams are scaled appropriately as the number
of boxes becomes large. The boundary of the terminal diagram becomes a smooth curve
and follows the arc sin law, known as the limit shape . Kerov [5] showed that the Young
diagrams growing with the Plancherel transition probability follow a dynamical equation,
called the automodel equation. This equation is an inviscid Burger’s equation. The limit
2
45o
Figure 1: 2D Crystal growth and growth of rotated Young diagrams. A crystal unit is compared with a
single box in the Young diagram. Single crystals are falling from sky under gravity and being deployed at
possible stable positions.
shape is a unique solution of the automodel equation in far future with a Young diagram
with no boxes as an initial condition in the far past.
The partition function of UMM admits a description in terms of representations of uni-
tary group. In the large N limit, there exists a correspondence between dominant eigenvalue
distributions and Young diagrams associated with unitary representations. Such a relation
allows a droplet description for diﬀerent large N phases of the matrix model under consid-
eration. This was ﬁrst observed in [6] in the context of GWW model, and later in [7, 8] for
a generic class of UMM. From the shapes of these 2D droplets, one can ﬁnd the dominant
Young diagrams corresponding to the largeN phases of UMM. Thus, the evolution or growth
of Young diagrams follows from the evolution of large N phases of a UMM. It was shown in
[1] that the Plancherel growth of Young diagrams is captured by GWW model. Evolution
of no-gap phase of GWW model with respect to a parameter of the model exactly matches
with the evolution of Young diagrams in the automodel class of Kerov. The limit shape was
identiﬁed with GWW transition point. A Hilbert space description of Plancherel growth
was also discussed in [1]. In this paper, we extend the analysis to q analog of Plancherel
growth.
There are diﬀerent ways to considerq-deformation of the Plancherel growth. The one that
follows from the deformation of the Markov-Krein correspondence was considered by Strahov
[9]. In this construction, the probability associated to a Young diagram is proportional to
the product of ordinary dimension and q dimension of the diagram. Strahov [9] showed that
the deformed inviscid Burger’s equation (generalisation of automodel equation) has a ﬁxed
point and the ﬁxed point is the q-deformed limit shape of Young diagrams. However, the
explicit form of the limit shape was not given. There exists another class of q-deformed
Plancherel probability which appears in diﬀerent contexts in topological string theory. In
this case, the q-probability of a Young diagram is proportional to the square of q-dimension
of the diagram. One can write a partition function for such a growth process. The partition
function is similar to that of topological string theory partition function on certain Calabi-
Yau threefolds [10–13] and Gromov-Witten invariants ofP1 [2, 14]. Theq-Plancherel measure
3
also appears in the partition function of N = 2 supersymmetric four dimensional gauge
theory in Ω-background, when expressed as a sum over partitions [11] 1. In this paper, we
mainly focus on this particular growth process. The goal is to write a unitary matrix model
which captures theq-deformed asymptotic growth of Young diagrams and set-up a mapping
between the diagrams in the automodel class and the physical Hilbert space.
We summarise our main observations :
• We write down the partition function for a growth process equipped with q-deformed
Plancherel measure considered in [2, 10–13]. One can exactly calculate the partition
function using the normalisation properties of the measure. However, in order to get
a handle on the asymptotic behaviour of the Young diagrams we introduce a “fake”
N dependence in the problem, following [1]. We restrict the sum over representations
to only those Young diagrams which have maximum N number of rows. In case of
ordinary Plancherel growth, the equivalence between the partition function and GWW
model was exact and follows from the properties of characters of the symmetric group
[1]. However, in the q-deformed version, the equivalence is not straight forward. We
use the droplet picture of [6, 8] to ﬁgure out the corresponding unitary matrix model.
It turns out to be a U(N) single plaquette model. We study the phase structure of
the q-deformed partition function, in the large N limit, which is analogous to that
of the GWW model. The model exhibits a third order phase transition which is
q analog of the GWW phase transition. The growth of Young diagrams under q-
deformed Plancherel measure is captured by the gap-less phase of the UMM. The
limiting or terminal diagram corresponds to the q-deformed GWW transition point.
We also ﬁnd the automodel class in this case and write the automodel equation satisﬁed
by the members in this class. Following [1, 15], we construct the Hilbert space by
quantising the phase space droplets and set up a correspondence between q-deformed
automodel diagrams and coherent states in the Hilbert space. Finally, we elaborate the
connection between moments of Young diagrams and the inﬁnite number of commuting
Hamiltonians obtained from the large N droplets.
• We also discuss the growth process equipped with q-deformed Plancherel measure
considered in [9]. In the large N limit, the saddle point equation turns out to be
a Riemann-Hilbert equation with a complicated kernel. We prescribe a method to
solve such Riemann-Hilbert problem perturbatively in the deformation parameter.
We obtain the dominant representations in the large N limit corrected up to ﬁrst
order in the deformation parameter, and observe that both the growth processes are
qualitatively same up to ﬁrst order in the deformation parameter.

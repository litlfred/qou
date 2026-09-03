---
doc_id: arxiv-1909.06797v5
doc_title: "Quantum Mechanics of Plancherel Growth"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-5
source_pdf: 1909.06797v5.pdf
source_sha256: 87095d7e46ebe286
---
2 Review 1 : Droplet description of unitary matrix models 5
2.1 The large N droplets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
Email addresses: arghya.chattopadhyay@gmail.com (Arghya Chattopadhyay), suvankar@iiserb.ac.in
(Suvankar Dutta), debangshu0@gmail.com (Debangshu Mukherjee), neetuj@iiserb.ac.in (Neetu)
arXiv:1909.06797v5  [hep-th]  14 Apr 2021
3 Review 2 : Plancherel Growth of Y oung diagrams 9
3.1 The Universal Diagram and Automodel . . . . . . . . . . . . . . . . . . . . . . 10
3.2 Fluctuations of automodel diagrams . . . . . . . . . . . . . . . . . . . . . . . . 12
4 Partition Function for Y oung lattice 13
4.1 A connection between Young lattice and Gross-Witten-Wadia model . . . . . . . 13
5 Large N analysis of partition function : an alternate proof of the limit shape theorem 15
5.1 Large N solutions and automodel diagrams . . . . . . . . . . . . . . . . . . . . 16
5.2 A connection with automodel . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
6 The Hilbert space for Plancherel growth 19
6.1 Droplet quantisation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
7 Conclusion 25
Appendix A Analysing Unitary Matrix Models 26
Appendix A.1 Eigenvalue analysis . . . . . . . . . . . . . . . . . . . . . . . . . . 26
Appendix A.2 Young diagram analysis . . . . . . . . . . . . . . . . . . . . . . . . 27
Appendix A.3 Finding the connection between two pictures . . . . . . . . . . . . . 28
Appendix B Spectral curve 30
Appendix C Asymmetric solutions 31
1. Introduction
The theory of random matrices has wide applications both in physics and mathematics. A particu-
lar class of random matrix model namely the unitary matrix model (UMM) plays a pivotal role in
understanding the various thermodynamic properties, phase structure and dynamics of gauge theo-
ries in diverse dimensions. In this paper we explore yet another interesting application of UMM in
the ﬁeld of asymptotic growth of Young diagrams in representation theory. Using the techniques
of unitary matrix models we provide a Hilbert space description of this growth of Young diagrams
- the Plancherel growth.
Young diagrams provide a convenient diagrammatic way to describe the representations of sym-
metric group and general linear groups. There are diﬀerent notations in literature to depict a Young
diagram. In this paper we follow the “English notation”. In this notation, boxes are arranged in
horizontal rows with the condition that number of boxes in a row is always less than or equal to
that in the row above. In general as one goes to higher and higher dimensional representations the
number of boxes in Young diagram increases. For our purpose we classify the Young diagrams in
terms of total number of boxes. Let us denote the set of all Young diagrams with k boxes byYk.
All the diagrams inYk+1 can be obtained by adding one box to each diagram inYk in all possible
allowed ways. See ﬁgure 1. Such a process is called growth process of Young diagrams. One can
construct all possible Young diagrams at any arbitrary levelk starting from null diagram (∅), means
2
Figure 1: Growth of Young diagrams.
no box. For a restricted growth process, one can assign a probability to every transition. Denoting
a particular Young diagram at level k byλk we associate a transition probabilityPtransition(λk,λ k+1)
for a transition fromλk toλk+1
Ptransition(λk,λ k+1) = 1
k + 1
dimλk+1
dimλk
(1.1)
ifλk+1 is obtained fromλk by adding one box, otherwisePtransition(λk,λ k+1) = 0. A growth process,
following the above probability measure, is called Plancherel growth process (see [1, 2] for a
comprehensive review). Note that the probability to get a diagram at level k + 1 from a diagram at
level k does not depend on the history of transition from level k− 1 to k. Thus, the growth process
is Markovian. It was shown by Vershik and Kerov [3] and independently by Logan and Shepp
[4] that Young diagrams following Plancherel growth process converge to a universal diagram in
the large k limit when the diagrams are normalised (scaled) appropriately such that the area of
the diagram is unity. The boundary of such normalised diagram becomes smooth under scaling.
A universal Young diagram means the boundary curve takes a particular form, which is called
the limit shape . The limit shape follows the famous arcsin law [3, 5]. In the continuum (large
k) limit Kerov introduced a di ﬀerential model to capture the growth of Young diagrams [1, 5].
He associated a ‘time’parameter with the continuous diagrams to study the evolution of these
diagrams. It turns out that Young diagrams equipped with Plancherel measure follow an evolution
equation which is a ﬁrst order partial di ﬀerential equation. The model was named as automodel
[1, 5]. The class of diagrams following such a growth or evolution equation is called automodel
class. The limit shape is a unique solution of the automodel equation in far future with∅ as initial
condition in far past.
Random matrix models oﬀer an independent way to analyse the growth processes of Young dia-
3
grams. Partition function of unitary matrix models can be written as a sum over representations of
the unitary group [6, 7]. In the largeN limit, one can rescale the Young diagrams appropriately and
ﬁnd the representations that dominate the partition function via saddle point analysis [7]. These
dominant representations are indeed asymptotic Young diagrams. Growth of such continuous rep-
resentations depends on the action and parameters of the model under consideration. However,
such problems demands further investigation and study which to the best of our knowledge is
lacking either in mathematics or physics literature 1. In this paper we try to understand whether
one can write down a unitary matrix model which can describe the asymptotic growth of Young
diagrams. To our surprise, we ﬁnd that the Plancherel growth process is actually captured by the
simple Gross-Witten-Wadia(GWW) model. GWW model is one of the well studied and exactly
solvable model in unitary random matrix theory. It is therefore quite interesting to see that the
strong coupling (no-gap) phase of GWW model is also capable of capturing the Plancherel growth
of Young diagrams. In fact we show that the matrix model computation oﬀers a direct and simple
proof of the limit shape theorem of Kerov. In this paper, we go further and map the growth process
with the evolution of free Fermi droplets in 2 dimensions in the context of unitary matrix model
[7]. By quantising these droplets we also construct a Hilbert space associated with such a growth
process and show that diﬀerent diagrams in the automodel class are mapped to coherent states in
the Hilbert space. Therefore, our analysis maps the growth process of Young diagrams to the evo-
lution of classical or coherent states in the Hilbert space in the large N limit. Large N ﬂuctuations
about the automodel diagrams [9] are mapped to quantum ﬂuctuations of coherent states.
The salient observations of this paper are following.
• Following [8] we compare the growth of Young diagrams with that of 2-dimensional crys-
tals. We consider ensemble of Young diagrams with inﬁnite members. Assigning Plancherel
probability for a particular diagram we write down a grand canonical partition function for
such an ensemble.
• The partition function can be computed exactly if we sum over all possible representations
of symmetric group S k for a given box number k. However that does not seem to be very
exciting. To capture the growth process from the partition function we impose acut-oﬀ N on
the number of rows of the Young diagrams. This essentially restricts us to a sub-ensemble
where all the diagrams have maximum N number of rows. As a beneﬁt, we are now allowed
to study the system under saddle point approximation in the large N limit.
• We next show that the above partition function is same as the partition function of S U(N)
GWW model where the rank of the gauge group is same as the cut-oﬀ. We use the Frobenius
formula to establish the equality.
• We observe that the no-gap phase of GWW model is mapped to the automodel class of
Kerov. The coupling constant of GWW model plays the role of time in automodel class.
The limit shape corresponds to the GWW transition point.
1A matrix model analysis of such growth process has been discussed in [8] - an asymptotic shape of large diagram
has been computed which matches with the limit shape of [3–5, 9].
4
• We next focus on the free Fermi droplet description of the growth process. Large N phases
of Unitary matrix models admit a droplet description [7]. We quantise these droplets and
construct the Hilbert space. We show that di ﬀerent Young diagrams in automodel class are
mapped to coherent states in the Hilbert space. Evolution of Young diagrams are, there-
fore, mapped to evolution of these coherent states. Thus our analysis explicitly maps the
Plancherel growth to the evolution of classical states in the Hilbert space.
• The Hilbert space description of the growth process also allows us to map the largeN ﬂuctu-
ations about the automodel diagrams to the quantum ﬂuctuations of coherent states. In this
paper we explicitly discuss this mapping.
The plan of the paper is following. In Section 2, we review earlier works where we map a particular
class of unitary matrix models to two dimensional droplets made of fermions in phase space.
Subsequently in Section 3, we discuss Plancherel growth of Young diagrams in details following
the works of [3]. The growth process is mapped to the evolution of a grand canonical ensemble
in Section 4. Section 5 is devoted to the analysis of the partition function that we set up for the
Plancherel growth process of Young diagrams. We provide an alternate proof of the limit shape
theorem of Kerov and Vershik. In Section 6, following a quantization procedure, we provide a
Hilbert space description of the growth process. Appendix A provides some details of the analysis
of a generic class of UMMs in terms of eigenvalues analysis as well as Young diagrams. It further
discusses a connection between the two pictures. In Appendix B we discuss the spectral curve for
the no-gap solution of the unitary matrix model. Finally, Appendix C discusses an asymmetric
solution that comes up in the context of GWW model which has connections with the growth
process that we discuss in this work.

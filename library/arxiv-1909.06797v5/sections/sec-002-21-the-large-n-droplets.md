---
doc_id: arxiv-1909.06797v5
doc_title: "Quantum Mechanics of Plancherel Growth"
section_id: sec-002-21-the-large-n-droplets
section_title: "The large N droplets"
section_number: 2.1
pages: 7-10
source_pdf: 1909.06797v5.pdf
source_sha256: 87095d7e46ebe286
doc_brief: "Quantum Mechanics of Plancherel Growth — Growth of Young diagrams, equipped with Plancherel measure, follows the automodel equation of Kerov."
---
Droplet description of large N phases is based on the fact that the partition function of UMM has
two equivalent descriptions - in eigenvalue basis and in Young diagram basis. It is well known
that eigenvalues of unitary matrices behave like position of free fermions [15]. On the other
hand, hook lengths of Young diagrams are like momenta of these fermions [7, 16]. A relation
between these two pictures oﬀers droplet or phase space description for diﬀerent classical phases
[7, 17, 18].
It was ﬁrst observed in [7] that the eigenvalue and the Young diagram distributions are functional
inverses of each other for a particular class of unitary matrix model, namely the (a, b) model whose
phase structure is similar to that of GWW model. Later in a series of papers [17–19] such relations
were proved for a generic class of UMM. The details of the calculation is given in Appendix A.3.
Here we present the main result.
In the large N limit, the connection between eigenvalue density ρ(θ) and hook number h is given
by
h2− 2S (θ)h + S 2(θ)−π2ρ2(θ) = 0 (2.7)
where
S (θ) = 1
2 +
∑
n
βn cos nθ. (2.8)
Using this equation one can also deﬁne a spectral curve for the generic UMM. See Appendix
B.
The relation (2.7) allows us to provide a phase space picture for diﬀerent large N phases of UMM
in terms of free fermi droplets (two dimensional distributions). These distributions /droplets are
similar to Thomas-Fermi distributions [20, 21]. Equation (2.7) has two possible solutions h±(θ)
given by
h±(θ) = S (θ)±πρ(θ). (2.9)
Using this relation we deﬁne a distribution functionω(h,θ ) in (h,θ ) plane
ω(h,θ ) = Θ
((h− h−(θ))(h+(θ)− h)
2
)
(2.10)
such that ω(h,θ ) = 1 for h−(θ) < h < h+(θ) and zero otherwise. Eigenvalue distribution, by
construction, can be obtained by integrating out h for a givenθ and is given by
ρ(θ) = 1
2π
∫
dhω(h,θ ) = h+(θ)− h−(θ)
2π . (2.11)
The distribution also satisﬁes the normalisation condition
1
2π
∫
dh dθω (h,θ ) = 1. (2.12)
7
The function S (θ) can also be written in terms of phase space geometry
S (θ) = 1
2πρ
∫ ∞
0
dh h ω(h,θ ) = h+(θ) + h−(θ)
2 . (2.13)
Integratingω(h,θ ) overθ for a given h gives a distribution of hook numbers h
w(h) = 1
2π
∫
dθω (h,θ ) with
∫
dh w(h) = 1. (2.14)
w(h) captures the information about largeN representations. Sinceω2(h,θ ) =ω(h,θ ), it is actually
the shape (i.e. boundary) of this distribution function which captures information about di ﬀerent
large N phases of the theory. We call such two dimensional distributions large N droplets.
The matrix model, we are considering, has no dynamics. Di ﬀerent large N phases, obtained by
solving the saddle point equation, are possible minimum free energy conﬁgurations of the model.
Hence the corresponding droplets are static - the shapes are not changing with time. To incorporate
dynamics into the picture, we follow anad hoc way : identify large N droplets with Thomas-Fermi
distribution at zero temperature and obtain the single particle Hamiltonian by comparing the two2.
In this way it is possible to incorporate time in our system.
Comparing the distribution function (2.10) with Fermi distribution at zero temperature
∆(p, q) = Θ(µ− h(p, q)) (2.15)
(µ is chemical potential and h(p, q) is single particle Hamiltonian density) we ﬁnd that the single
particle Hamiltonian density is given by
h(h,θ ) = h2
2 − S (θ)h + g(θ)
2 +µ, where g(θ) = h+(θ)h−(θ). (2.16)
Total Hamiltonian3 can be obtained by integrating h(h,θ ) over the phase space
Hh = 1
2πℏ
∫
dθ
∫
dhω(h,θ ) h(h,θ ). (2.18)
We have taken into account the fact that one state occupies a phase space area of 2 πℏ in semi-
classical approximation. It needs to modify the normalisation of phase space density
1
2πℏ
∫
dhdθω(h,θ ) = N, with ℏN = 1 (2.19)
where, N is total number of states available inside a droplet. The classical limit corresponds to
ℏ→ 0, N→∞ with ℏN = 1.
2One can also construct similar droplet description for time dependent unitary matrix model. In that case time
evolution of these droplets are inherent [22]
3One can show that [18] integrating over h, the total Hamiltonian (without the ℏ factor) is same as the collective
ﬁeld theory Hamiltonian of Jevicki and Sakita [23]
Hh =−
∫
dθ
( S 2ρ
2 + π2ρ3
6 + Ve f f (θ)ρ
)
+µ (2.17)
with an eﬀective potential.
8
3. Review 2 : Plancherel Growth of Y oung diagrams
The Markovian growth process of large Young diagrams can be given a statistical interpretation
described through a partition function. In order to achieve that we deﬁne a Young lattice [8]
Y =
∞⋃
k=0
Yk. (3.1)
All the members ofYk have same number of boxes but diﬀerent shapes.Yk can be thought of as
an ensemble of Young diagrams with the same macroscopic variable k. Hence, we can deﬁne a
partition function for the grand canonical ensemble (3.1)
QY =
∞∑
k=0
zkZYk (3.2)
where z is called fugacity (z > 0) andZYk is the canonical partition function for Yk, given by
ZYk =
∑
λk
P(λk)δ(k−|λk|). (3.3)
P(λk) is the probability associated with the ensemble memberλk - a Young diagram withk number
of boxes.
To make the growth process meaningful it is customary to assign a probability for each diagram at
level k in the Young latticeY. There is a natural way to assign probability to di ﬀerent diagrams.
We count the total number of inequivalent paths one can follow to come to a particular diagram at
level k starting from∅. See ﬁgure 1. It turns out that the Plancherel measure is proportional to the
square of that number. The proportionality constant is ﬁxed by the normalization condition. To
calculate the number of paths heading to a diagramλk we look at growth of Young tableaux rather
than Young diagrams. Starting from ∅ we keep on adding one box at each level with increasing
number. Therefore the readers can easily convince themselves that at each levelk we have diﬀerent
Young tableaux and a particular tableaux can be reached from∅ by a unique path only. Thus the
number of paths available to reach a particular Young diagramλk is equal to the number of standard
Young tableaux fλk of that given shape. It is well known that [24, 25],
∑
λk∈Yk
( fλk)2 = k!. (3.4)
Hence we get the Plancherel measureP(λk) for a diagramλk
P(λk) =
f 2
λk
k!. (3.5)
This deﬁnition of Plancherel probability is equivalent to what we deﬁned in equation (1.1). One
can show that
P(λk) =
∑
paths
k−1∏
i=0
Ptransition(λi,λ i+1). (3.6)
9
We useP(λk) to write the partition function for the growth process. The number fλk is equal to the
dimension of the representationλk, i.e.
fλk = dimλk. (3.7)
and thus we have,
P(λk) = (dimλk)2
k! . (3.8)
It was observed in [3, 4] that a Young lattice equipped with Plancherel measure terminates to a
universal class of diagram in the limit k→∞ when the diagrams are scaled properly.

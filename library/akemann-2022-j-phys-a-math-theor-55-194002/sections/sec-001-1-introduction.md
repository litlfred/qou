---
doc_id: akemann-2022-j-phys-a-math-theor-55-194002
doc_title: "Consecutive level spacings in the chiral Gaussian unitary ensemble: from the hard and soft edge to the bulk"
section_id: sec-001-1-introduction
section_title: "Introduction"
section_number: 1
pages: 3-5
source_pdf: Akemann_2022_J._Phys._A__Math._Theor._55_194002.pdf
source_sha256: 3753499c4b23f189
toc_source: outline
doc_brief: "Consecutive level spacings in the chiral Gaussian unitary ensemble: from the hard and soft edge to the bulk — 20 sections: Front matter; Consecutive level spacings in the ; Introduction"
---
One of the cornerstonesin applying randommatrix theory is the local level spacing distribution.
It provides a statistical description of the spacing between consecutive eigenvalues. For that
purpose,the mean level density around the point where we zoom in has to be unfolded,meaning
it is mapped to be approximately constant, see [1]. Then, the energies are measured in units
of this constant. This procedure applies to the bulk of the spectrum. The spacing distribution
continues to be a popular tool in today’s applications, ranging from quantum spin chains [2],
quantum circuits [3], chemical isotopes [4] and graphene [5] to classical integrable systems
[6] and theoretical studies [7], which are all from past year. We refer to [1, 8] for a list of more
topics and references therein.
Let us also look back at the classical papers where the spacing distribution has
been proposed in the study of quantum systems displaying chaotic behaviour, the Bohi-
gas–Giannoni–Schmit conjecture [9], cf [10]: quantum systems that are fully chaotic follow
random matrix statistics. This field of research has been subsumed and influenced by Haake’s
famous book [11] in several editions. Let us mention an important mathematical contribution
of Haake in this context. Together with Dietz [12], he has carried out a precise expansion of the
true spacing distribution for the classical random matrix ensembles for comparison with data,
that we will use as well. This expansion is the one developed by Pad´e [13], who introduced an
expansion in rational functions instead of polynomials, as it is common for the Taylor expan-
sion. This approximation for the level spacing distribution by Dietz and Haake goes beyond the
frequently used Wigner surmise. At the same time, it proves a practical expression compared
to a truncation of the infinite product of Fredholm determinant eigenvalues in Mehta’s book
[14], given in terms of an integral over spheroidal functions. In parallel, Haake has pursued an
impressive research programme to prove random matrix statistics from a semi-classical expan-
sion, culminating in [15]. This has lead to a much deeper understanding of chaotic quantum
systems.
A second example where the random matrix approximation is very well understood is the
low-energy Dirac operator spectrum in quantum chromodynamics (QCD) introduced in [16],
which has motivated our study. Here, the spectral edge representing a hard edge is focussed
on, zooming into the origin where the lowest eigenvalues are located. Without going into detail
of the vast literature on the application to QCD, and on comparing to lattice data from first
principle lattice QCD simulations, cf [17, 18], let us focus on random matrix questions. In
this field, typically the local density correlation functions, given by the universal Bessel-kernel
[19], and the distributions of the smallest eigenvalues [20–22] are employed for comparison.
However, few works have applied the level spacing distribution as a measure for random matrix
statistics, both at the hard edge [23–25] and in the bulk of the spectrum [26]. Averaging over
several consecutive spacings, a good agreement was found at the hard edge below the chiral
phase transition. Only in the vicinity of the phase transition deviations from the bulk spacing
were found [23, 24, 27, 28]. It came as a surprise to us, that no analytical results were available
at the hard edge for the spacing distribution, and that at least on average the bulk spacing leads
to a good description.
In the present article, we will provide a closed form analytical expression for the spacing
distribution in the chiral Gaussian unitary ensemble (χGUE) that is relevant for QCD with
three colours in the fundamental representation, and other strongly interacting field theories
which lie in the same universality class. We consider the spacing between two consecutive
eigenvalues close to the origin, beginning with the smallest and second smallest eigenvalue.
2
J. Phys. A: Math. Theor. 55 (2022) 194002
G Akemann et al
Our derivation follows ideas from the computation of the distribution of individual eigenval-
ues at the hard edge, starting with the smallest one [20–22]. The resulting spacings depend on
several parameters of the ensemble, the number of exact zero eigenvalues ν, that is related
to the gauge field topology, and a fixed number of (light) quark flavours Nf with masses
m f . Our results hold for finite matrix size n and in the asymptotic microscopic scaling limit
n →∞. It provides an alternative to the somewhat heavy machinery of analysing the Fredholm
determinant of the underlying integral kernel, that typically leads to an expression including
Painlev´e V differential equations [29]. In contrast, we will obtain expressions in terms of k-fold
integrals over a determinant of Bessel-functions of size Nf + ν + k for the kth spacing.
Moreover,we will find that, both at finite (even small) matrix dimension n, as well as asymp-
totically at large n, the spacings at the hard edge are very close to the GUE bulk spacing
distribution, including a very weak dependence on ν and Nf. The deviations range from one
percent to only a few per mill when varying the parameters. Hence a comparison to QCD lat-
tice data, that we also undertake, does not allow to discriminate between the two, even for the
smallest to second smallest eigenvalue spacing at k = 1. The situation at the soft edge is very
similar, where the random matrix eigenvalue density vanishes as a square root. Here, appar-
ently so far only the local Airy-kernel [30] and distribution of the largest eigenvalue [31] were
studied, but not the spacing distribution. Even if we cannot offer analytical results in the soft-
edge case, our numerical investigation suggests that also the spacing between the largest and
second largest eigenvalue is very close to the bulk spacing. This is numerically corroborated
at the inner soft edge when ν ≫1, too.
Let us emphasise that we are studying the transition between two different local random
matrix statistics, that is in our case the Bessel-kernel and sine-kernel statistics. Those statistics
also appear in the transition ensembles between the χGUE and GUE, where the former ensem-
ble has chiral symmetry. Such a transition has been studied on the level of correlation functions
[32, 33], where it is very pronounced and relevant for the Wilson Dirac operator spectrum [34].
In contrast, for the observable of consecutive level spacings the difference between the two
ensembles turns out to be tiny at the origin (the hard edge), and we are almost immediately
in the bulk. The transition between different random matrix symmetry classes is a classical
question and has been studied in the bulk [35] and at the edges [36]. We will not touch upon
another transition, between quantum chaotic and integrable behaviour which is generically
Poisson, compare [11].
The remaining article is organised as follows. In section 2, we study the limit from the hard
and soft edge to the bulk, by taking the large argument asymptotic of the universal Bessel-
and Airy-kernel, respectively, that yields the universal sine-kernel in the bulk. This provides a
convergence rate at the level of the density correlation functions. Section 3 discusses general
expressions for the gap probability and kth spacing distributions in terms of a k-fold integral
over the ratio of partition functions with Nf + ν + 2k flavours. These are then evaluated in
section 4 for the χGUE at finite matrix dimension n, yielding compact determinantal expres-
sions of the size of Nf + ν + k flavours. In section 5, we take the large-n limit at fixed ν and
Nf which is known to be universal. The convergence of our analytical results for the hard edge
spacing towards the bulk spacing is illustrated for quenched (Nf = 0) and unquenched settings
(Nf̸ = 0), and compared to the approximation of the bulk spacing through the Wigner sur-
mise. Section 6 contains the comparison to data from lattice QCD, and in section 7 we present
our conclusions. In appendix A we collect the exact expression for the GUE bulk spacing
distribution from [12].
3
J. Phys. A: Math. Theor. 55 (2022) 194002
G Akemann et al

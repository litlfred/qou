---
doc_id: arxiv-hep-th-9711057v2
doc_title: "The microscopic spectrum of the QCD Dirac operator with finite quark masses"
section_id: sec-000-i-introduction
section_title: "INTRODUCTION"
section_number: I
pages: 1-2
source_pdf: 9711057v2.pdf
source_sha256: acf5cdd7fe848f43
doc_brief: "The microscopic spectrum of the QCD Dirac operator with finite quark masses — 7 sections: INTRODUCTION; RANDOM-MATRIX THEORY FOR FINITE QU; CALCULATION OF OBSERVABLES"
---
The low-lying eigenvalues of the QCD Dirac operator are of great importance for the understanding of the sponta-
neous breaking of chiral symmetry in QCD. In Euclidean space, the Dirac operator reads i/D = i/∂+ g(λa/2)/Aa, where
g is the coupling constant, λa are the generators of SU(N)-color, and Aa
µ are the gauge ﬁelds. The corresponding
eigenvalue equation is i/Dψi = λiψi with real eigenvalues λi. Because the Dirac operator anticommutes with γ5, the
eigenvalues either occur in pairs ±λi or are zero. Let ρ(λ) = ⟨P
i δ(λ −λi)⟩A be the eigenvalue density of the Dirac
operator averaged over gauge ﬁeld conﬁgurations. The Banks-Casher formula, ⟨¯ψψ⟩= πρ(0)/V [1], relates the order
parameter of chiral symmetry breaking, ⟨¯ψψ⟩, to the density of eigenvalues of the Dirac operator near zero virtuality.
Here, it is essential that the thermodynamic limit be taken before the chiral limit. Note also that ρ(λ) is normalized
to the space-time volume V . In the real world chiral symmetry is spontaneously broken and ⟨¯ψψ⟩̸ = 0. This implies
that the low-lying Dirac eigenvalues must be spaced like ∼1/V . Therefore, it is natural to magnify this region of the
spectrum by a factor of V . This was ﬁrst suggested by Shuryak and Verbaarschot [2] who introduced the so-called
microscopic spectral density deﬁned by
ρs(z) = lim
V →∞
1
V Σ ρ
 z
V Σ

,
(1)
where Σ is the absolute value of the chiral condensate. Based on an analysis of sum rules derived by Leutwyler and
Smilga [3] for the inverse powers of the Dirac eigenvalues in a ﬁnite volume, Shuryak and Verbaarschot conjectured
that the microscopic spectral density should be a universal quantity which depends only on global symmetries, the
number of ﬂavors Nf, and the topological charge ν.
What is the meaning of universality in this statement?
In
principle, one could compute ρs directly from full QCD. In practice, of course, the complexity of the QCD Lagrangian
makes this impossible. However, if ρs is universal, one can try to compute it in another theory which is simpler than
QCD but has the same symmetries. The simplest theory in which such a calculation is possible is random-matrix
theory (RMT). Whether the results obtained in RMT correctly describe the microscopic spectrum of full QCD is a
question that can only be answered by empirical evidence, most importantly by large-scale lattice QCD simulations.
Let us brieﬂy recall how a chiral random-matrix model is constructed. In a chiral basis in Euclidean space, the
Dirac operator has a block structure since it only couples states of opposite chirality. In RMT, the matrix of the
Dirac operator is replaced by a random matrix W with suitable symmetry properties,
 im
i/D
(i/D)†
im

→

im
W
W †
im

,
(2)
where we have also added a quark mass m. If W has N + ν rows and N columns, then the Dirac matrix in (2)
(without the mass term) has N positive and N negative eigenvalues, respectively, and ν zero modes (we assume ν ≥0
and ν ≪N). We can identify ν with the topological charge and 2N + ν ≈2N with the volume V . In full QCD with
Nf ﬂavors, the weight function used in averaging over gauge ﬁeld conﬁgurations contains the gluonic action in the
form exp(−Sgl) and Nf fermion determinants. In the random-matrix model, the gluonic part of the weight function
is replaced by a convenient distribution of the random matrix W, usually a Gaussian distribution of the individual
matrix elements (which are uncorrelated). Since the fermion determinants can be expressed as products over the Dirac
eigenvalues they can also be taken into account in the random-matrix model. The symmetries of W are determined
1
by the anti-unitary symmetries of the Dirac operator. They were classiﬁed by Verbaarschot in Ref. [4]. Depending on
the number of colors and the representation of the fermions the matrix elements of W are real, complex, or quaternion
real. The corresponding random-matrix ensembles are called chiral Gaussian orthogonal (chGOE), unitary (chGUE),
and symplectic (chGSE) ensemble, respectively. The microscopic spectral density has been computed analytically in
all three ensembles for all Nf and ν in the chiral limit [5–7].
Evidence in support of the conjecture that ρs is a universal function has been accumulated in a number of recent
studies which we list here.
The moments of ρs generate the Leutwyler-Smilga sum rules [5].
The result for ρs
is insensitive to the probability distribution of the random matrix [8,9]. Lattice data for the valence quark mass
dependence of the chiral condensate could be understood using the analytical expression for ρs [10,11]. The functional
form of ρs does not change at ﬁnite temperature [12]. The analytical result for ρs is found in the Hofstadter model
for universal conductance ﬂuctuations [13]. For an instanton liquid, ρs shows quite good agreement with the random-
matrix result [14]. Recently, a high-statistics lattice calculation directly demonstrated agreement between the random-
matrix results and lattice data, not only for ρs but also for the distribution of the smallest eigenvalue and for the
microscopic spectral two-point correlator [15]. (This study was done for gauge group SU(2) with staggered fermions
in the quenched approximation.) We believe that the universality of ρs is now ﬁrmly established.
One of the most interesting and most important problems of present-day lattice simulations is the inclusion of
dynamical fermions. This is essential for a realistic description of hadronic properties. Unfortunately, it is compu-
tationally expensive to include the fermion determinants in a Monte-Carlo simulation. Moreover, the computational
cost increases with lower quark mass, thus it is extremely diﬃcult to take the chiral limit on the lattice. Any analytical
insight into the distribution of the Dirac eigenvalues in the presence of massive dynamical quarks will therefore be
helpful. It is the purpose of this work to extend the random-matrix results obtained in the chiral limit to the general
case of massive quarks to be able to compare with actual lattice calculations. This issue was ﬁrst discussed in Ref. [16].
The most interesting case of QCD with 3 colors and fermions in the fundamental representation corresponds to the
chGUE of RMT on which we concentrate here. In what range of the quark mass can we expect the random-matrix
results to be in agreement with full QCD? Gasser and Leutwyler [17] have shown that in the range 1/Λ ≪L ≪1/mπ
the dependence of the ﬁnite-volume QCD partition function on the quark mass m is determined solely by global
symmetries (Λ is a typical hadronic scale, L is the linear size of the Euclidean box, and mπ ∼
√
mΛ is the pion mass).
The partition function was computed for equal quark masses using an eﬀective Lagrangian in Ref. [3] and for the
general case of diﬀerent quark masses in the framework of chiral RMT in Ref. [18]. The condition L ≪1/mπ sets an
upper limit of 1/
√
V Λ2 on the quark mass. A lower limit of 1/(V Λ3) on the quark mass is set by the requirement
that the chiral condensate be non-zero in a ﬁnite volume. To obtain non-trivial results for the dependence of the
various quantities we compute on m, the quark mass has to be rescaled by the same factor 1/(V Σ) as the eigenvalues,
cf. Eq. (1). For large quark masses, our results reduce to those obtained in the quenched approximation.
This paper is organized as follows. In Sec. II we discuss the random-matrix model and construct the orthogonal
polynomials and the partition function which are needed in the course of the calculation. Physical observables such as
the microscopic spectral density and the distribution of the smallest eigenvalue are computed in Sec. III. Section IV
is a short summary.
After completion of this work we learned that very recently a similar calculation was performed simultaneously and
independently by P.H. Damgaard and S. Nishigaki [19]. In this work, the authors also give a universality proof for
more general distributions of the random matrix and construct spectral sum rules for the massive Dirac operator (see
also Ref. [20]) but do not address the distribution of the smallest eigenvalue. Wherever the two manuscripts overlap
the results are identical.

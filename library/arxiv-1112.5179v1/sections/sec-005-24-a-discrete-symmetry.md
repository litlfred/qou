---
doc_id: arxiv-1112.5179v1
doc_title: "3-Manifolds and 3d Indices"
section_id: sec-005-24-a-discrete-symmetry
section_title: "A discrete symmetry"
section_number: 2.4
pages: 12-13
source_pdf: 1112.5179v1.pdf
source_sha256: b58af08336c40994
toc_source: outline
text_source: latex
latex_prose_ratio: 0.958
latex_coverage_ratio: 1.0
doc_brief: "3-Manifolds and 3d Indices — We identify a large class R of three-dimensional N = 2 superconformal ﬁeld the- ories."
---
[]{#sec:kappa label="sec:kappa"}

We could define standard discrete symmetries $C$, $P$, and $T$ acting on theories $\mathcal{T}$ and their indices, though in general the 3d SCFT's in class $\mathcal{R}$ will not be invariant under any of these "symmetries" alone. To see which discrete symmetries stand a chance at preserving a theory $\mathcal{T}$ and its index, it is useful to consider more closely the Hilbert space $\mathcal{H}_m$ of $\mathcal{T}$ on $S^2$ in the presence of magnetic flux $m$. Suppose further that $\mathcal{T}$ is in class $\mathcal{R}$, and has a $UV$ Lagrangian description as an abelian Chern-Simons-matter theory with superpotential.

The Hilbert space $\mathcal{H}_m$ is graded by charges $(E,R,j_3,e)$. Since states come in complete multiplets of the $SU(2)$ Lorentz group, changing the sign of $j_3$ should preserve $\mathcal{H}_m$. We could also try to flip the sign of the $U(1)$ R-charge $R$. In a Lagrangian, this is accomplished by Hermitian conjugation, switching chiral multiplets and antichirals, which has the additional effect of flipping the flavor charge $e\to -e$. However, this overall charge conjugation still does not preserve the theory in a magnetic flux background. In order for antiparticles to behave the same way as the original particles, it is also necessary to replace $m\to -m$.

It appears that the simultaneous reversal of charges

$$\rho \;:\; (E,R,j_3,e,m)\;\to\;(E,-R,-j_3,-e,-m)$$

is a true symmetry of the graded Hilbert spaces $\mathcal{H}_m$. In fact, there exists a simple geometric operation that also realizes $\rho$ in the context of the index. If we put the Euclidean version of $\mathcal{T}$ on $S^2\times S^1$, with appropriate magnetic flux and global Wilson lines so as to calculate the index, then $\rho$ corresponds to reflecting $S^2$ through its equator (along the $j_3$ axis) and reversing time. The spatial reflection flips $m$, while the time reversal flips $j_3$ and effectively $R$ and $e$. The effective negation of $R$ and $e$ happens because the fugacities in R-charge and flavor Wilson lines change sign. Altogether, this reversal of time and space is just the Euclidean analogue of $CPT$ symmetry.

The outcome is that we would expect the index to be invariant under $\rho$. Naively, from [\[Izeta\]](#Izeta){reference-type="eqref" reference="Izeta"}, this means

$$\label{kind}
\begin{equation}\label{kzeta}
\mathcal{I}_\mathcal{T}(m;q,\zeta) \;\overset{\rho}{=}\; \mathcal{I}_\mathcal{T}(-m;q^{-1};\zeta^{-1})\,, \end{equation}

or in a charge basis,

\begin{equation}\label{kme}
\mathcal{I}_\mathcal{T}(m,e;q) \;\overset{\rho}{=}\; \mathcal{I}_\mathcal{T}(-m,-e;q^{-1})\,.\end{equation}$$

However, [\[kind\]](#kind){reference-type="eqref" reference="kind"} are only true in a formal sense. In order to account for the infinite cancellations between bosons and fermions in $\mathcal{H}_m$, the index should really be defined with a regulator as in [\[IH\]](#IH){reference-type="eqref" reference="IH"}. Upon applying $\rho$, the "Hamiltonian" appearing in the regulator changes, $H = E-R-j_3\to E+R+j_3$, so that the boson-fermion cancellations in $\mathcal{H}_{-m}$ should be counted differently than would be implied by the right-hand sides of [\[kind\]](#kind){reference-type="eqref" reference="kind"}. Therefore, as written, the equalities [\[kind\]](#kind){reference-type="eqref" reference="kind"} are not actually correct. This fact is most striking if (say) we choose a superconformal R-charge assignment; then the indices on the left-hand side are series in positive powers of $q$ while the indices on the right-hand side are series in $q^{-1}$. Typically there is no analytic continuation from one to the other.

[^1]

Making sense of $\rho$ symmetry for indices requires a reorganization of the cancellations in the spaces $\mathcal{H}_m$, effectively turning the series in $q^{-1}$ on the right-hand sides of [\[kind\]](#kind){reference-type="eqref" reference="kind"} into series in $q$. One way to implement this reorganization is to separate $\mathcal{H}_m$ into Fock spaces that can be "inverted." For example, the reorganization in the Fock space of a free boson would correspond to rewriting the generating function of single-particle states as

$$\frac{1}{1-q^{-1}} \to \frac{-q}{1-q}\,.$$

This reorganization will be realized in Section [\[sec:tetkappa\]](#sec:tetkappa){reference-type="ref" reference="sec:tetkappa"} for the simple tetrahedron theory $\mathcal{T}_\Delta$. For more complicated theories in class $\mathcal{R}$, the mathematics of plethystic logarithms and exponentials (*cf.* [@Hanany-pleth]) may help to convert indices $\mathcal{I}_\mathcal{T}(-m,-e;q^{-1})$ to series in $q$.

Although $\rho$ symmetry only holds formally for the index, it is still powerful enough to relate algebras of operators on the index (which do not feel the re-organization of Hilbert spaces). We will see this beginning in Section [\[sec:ops\]](#sec:ops){reference-type="ref" reference="sec:ops"} below, and find a geometric meaning for $\rho$ acting in operator algebras in Section [\[sec:3d4d\]](#sec:3d4d){reference-type="ref" reference="sec:3d4d"}. In Section [\[sec:CS\]](#sec:CS){reference-type="ref" reference="sec:CS"}, we will show that when $\mathcal{T}$ is a 3-manifold theory $T_M$, $\rho$ coincides with complex conjugation in $SL(2,{\mathbb C})$ Chern-Simons theory on $M$.

[^1]: For example, we will see later that the index of the tetrahedron theory, as a function of $q$, has a natural boundary at $|q|=1$. We expect this to hold true for more general theories in class $\mathcal{R}$.

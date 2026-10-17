---
doc_id: arxiv-1112.5179v1
doc_title: "3-Manifolds and 3d Indices"
section_id: sec-007-3-the-tetrahedron-index
section_title: "The tetrahedron index"
section_number: 3
pages: 16-18
source_pdf: 1112.5179v1.pdf
source_sha256: b58af08336c40994
toc_source: outline
text_source: latex
latex_prose_ratio: 0.958
latex_coverage_ratio: 0.993
---
[]{#sec:T1 label="sec:T1"}

The basic building block used to construct the theory $T_M$ for any 3-manifold $M$ is the theory $T_\Delta$ associated to a single ideal tetrahedron. More precisely, we should call the theory

$$T_{\Delta,\Pi_Z}\,, \label{tetthy}$$

since it depends on a polarization for the boundary of the tetrahedron. As discussed in Sections 2 and 4 of [@DGG], we make a specific choice of polarization $\Pi_Z$ (see also Section [\[sec:tetdiff\]](#sec:tetdiff){reference-type="ref" reference="sec:tetdiff"} below). Then $T_\Delta$ consists of a single free $\mathcal{N}=2$ chiral multiplet $\phi$, coupled to a background $U(1)$ gauge multiplet with a level $-\tfrac12$ Chern-Simons interaction.

In order to calculate the index of $T_\Delta$, we must specify the R-charge and fermion number assignments for the theory on $S^2\times S^1$. We take $R_\phi=F_\phi=0$, and also require that the vacuum in a flux sector of any negative charge $m$ has $R_{\rm vac}=F_{\rm vac}=0$. Then, by following the rules for constructing indices in [@KW-index; @IY-index], we find

$$\mathcal{I}_\Delta(m;q,\zeta) \,\equiv\, \mathcal{I}_{T_\Delta,\Pi_Z}(m;q,\zeta) \,=\,  (-q^{\frac12})^{\frac12(m+|m|)}\zeta^{-\frac12(m+|m|)} \prod_{r=0}^\infty \frac{1- q^{r+\frac12|m|+1}\zeta^{-1}}{1-q^{r+\frac12|m|}\zeta}\,. \label{Iztet}$$

It turns out that this expression simplifies nicely to

$$\mathcal{I}_\Delta(m;q,\zeta) =\prod_{r=0}^\infty \frac{1- q^{r-\frac12m+1}\zeta^{-1}}{1-q^{r-\frac12m}\zeta}\,. \label{Iztet2}$$

The various ingredients in [\[Iztet\]](#Iztet){reference-type="eqref" reference="Iztet"} can be given an intuitive explanation. The denominator in the product arises from bosonic creation operators of flavor charge $1$ and spin $r+\tfrac{|m|}{2}$ acting on the vacuum. The spin starts from $\tfrac{|m|}{2}$ due to the nontrivial magnetic flux on $S^2$. The numerator arises similarly from fermionic creation operators of flavor charge $-1$ and spin $r+\tfrac{|m|}{2}+1$.

In addition to the product, the prefactor $(-q^{\frac12})^{\frac12(|m|+m)}\zeta^{-\frac12(m+|m|)}$ in [\[Iztet\]](#Iztet){reference-type="eqref" reference="Iztet"} turns out to be both subtle and important. It depends on the energy, R-charge, and flavor charge of the ground state in a non-trivial flux sector, which have been calculated carefully in *e.g.* [@BKW-monopoles]. First, the flavor charge of the flux vacuum is affected by the quantization of (anti)fermions in the chiral multiplet, and receives from that a contribution $-\tfrac12|m|$. This is corrected by the Chern-Simons coupling $k=-\tfrac12$ to $-\tfrac12(m+|m|)$. In order to determine the R-charge $R_{\rm vac}$ and fermion number $F_{\rm vac}$, we can shift conventions so that $R_\phi=F_\phi=1$ for the free chiral boson. Then $R=F=0$ for the fermion zero-mode whose quantization determines the quantum numbers of the vacuum, implying $R_{\rm vac}=F_{\rm vac}=0$. In terms of the index [\[Iztet\]](#Iztet){reference-type="eqref" reference="Iztet"}, we can easily perform the shift to $R_\phi=F_\phi=1$ by setting $\zeta\to (-q^{\frac12})\zeta$. Then it is easy to see that the vacuum acquires $R_{\rm vac}=F_{\rm vac}=0$ as expected.

It is important to remark a subtle sign difference between our prescription for the index of a chiral multiplet and the prescription that can be found in the literature [@IY-index; @KW-index]. After aligning the choices of R-charge and CS terms, the difference boils down to the prefactor $(-1)^{\frac12(|m|+m)}$. This prefactor affects in a minimal way the checks of mirror symmetry that have already been done in the literature, as it only affects the overall sign of the index in a given charge sector. However, only with our definition of the chiral index can such signs be matched universally via an appropriate shift of $F$. This deeply affects the calculation of the index in theories whose superpotentials have monopole operators --- which is standard in class $\mathcal{R}$.

Let us also write the index in an electric-magnetic charge basis, as in Section [\[sec:actions\]](#sec:actions){reference-type="ref" reference="sec:actions"}. By using several standard identities for $q$-series, we find

$$\mathcal{I}_\Delta(m;q,\zeta) \,=\, \sum_{e\in {\mathbb Z}} \mathcal{I}_\Delta(m,e;q)\zeta^e\,,$$

with

$$\mathcal{I}_\Delta(m,e;q) \,=\, \sum_{n=\lfloor e\rfloor}^\infty
 \frac{(-1)^n q^{\frac12 n(n+1)-\big( n+\frac 12e\big) m}}{(q)_n\,(q)_{n+e}}\,, \label{Imetet}$$

where $\lfloor e \rfloor \equiv \tfrac12(|e|-e)$ and $(q)_n \equiv (1-q)(1-q^2)\cdots (1-q^n)$. The sum in [\[Imetet\]](#Imetet){reference-type="eqref" reference="Imetet"} can be thought of as defining a formal power series in $q$; for fixed charge $\gamma=(m,e)$, only finitely many terms in the sum are necessary for calculating $\mathcal{I}_\Delta(m,e;q)$ to a desired order in $q$. The series [\[Imetet\]](#Imetet){reference-type="eqref" reference="Imetet"} also appears to converge to a well-defined analytic function of $q$ for $|q|<1$.

In anticipation of the interpretation of the tetrahedron index as a geometric invariant of an ideal tetrahedron $\Delta$ itself (and connections to the classical Bloch group), we can take the "classical limit" $q =e^\hbar \to 1$ and $m\to \infty$ with $q^m$ fixed. Let us set $q^{\frac m2}\zeta=z$, remembering that $\zeta$ is a pure phase, so that $z$ becomes a complex number. Then

$$\label{tetasymp}
\mathcal{I}_\Delta(m;q,\zeta) \;=\; \prod_{r=0}^\infty \frac{1-q^{r+1}z^{-1}}{1-q^r \,\overline z^{-1}}\;\;\overset{\hbar\to 0}{\sim}\;\; \exp\left( \frac{2V_\Delta(z)}{i\hbar}+\ldots\right)\,,$$

where the function

$$V_\Delta(z) \equiv -{\rm Im}\,{\rm Li}_2(z^{-1})$$

is closely related to the hyperbolic volume of a tetrahedron with shape parameter $z$. In fact, the actual volume can be written as ${\rm Vol}_\Delta(z) = V_\Delta(z) + \arg(1-z^{-1})\log|z|$ , *cf.* [@Thurston-1980].

## Parity and $\rho$ symmetry {#sec:tetkappa}

Several identities satisfied by the tetrahedron index can be understood via discrete symmetries acting on $T_\Delta$. Let's first consider the action of parity $\mathbf{P}$ on $T_\Delta$. In is not an exact symmetry because it inverts the sign of the Chern-Simons level, from $k=-\tfrac12$ to $k=\tfrac12$. However, this can be compensated for by subtracting a Chern-Simons term, *i.e.* applying $T^{-1}\in Sp(2,{\mathbb Z})$. In the $S^2\times S^1$ background, it actually turns out that the R-charge and fermion number of the vacuum must also be shifted, so that altogether we get

$$\label{PonT}
T_\Delta\;\simeq\; \sigma_m^R\sigma_m^F T^{-1}\circ \mathbf{P}\,T_\Delta\,.$$

Acting on the index, $\mathbf P$ simply sends $m\to -m$, so [\[PonT\]](#PonT){reference-type="eqref" reference="PonT"} implies

$$\mathcal{I}_\Delta(m,e;q) = \big(-q^{\frac12}\big)^m\mathcal{I}_\Delta(-m,e+m;q)\,.
\label{tetPem}$$

This identity can be checked explicitly (see Appendix [\[app:ST\]](#app:ST){reference-type="ref" reference="app:ST"}), most easily after converting to the fugacity basis.

The $\rho$ symmetry of Section [\[sec:kappa\]](#sec:kappa){reference-type="ref" reference="sec:kappa"} is more universal than parity, but also more subtle to implement. Naively, it sends $\mathcal{I}_\Delta(m;q,\zeta)$ to $\mathcal{I}_\Delta(-m;q^{-1},\zeta^{-1})$; but the latter does not make sense for $|q|<1$. In order to properly apply the symmetry, we need to reorganize the Hilbert space $\mathcal{H}_{-m}$, and to reinterpret $\mathcal{I}_\Delta(-m;q^{-1},\zeta^{-1})$ as a series in $q$. For the tetrahedron, this is actually straightforward.

Let us set $z=q^{\frac m2}\zeta$, $\overline z=q^{\frac m2}\zeta^{-1}$, noting that $\rho$ acts on $z$ by complex conjugation. Then

$$\begin{aligned}
 \mathcal{I}_\Delta(-m;q^{-1},\zeta^{-1}) &\,=\, \prod_{r=0}^\infty \frac{1-q^{-r-1}\,\overline z^{-1}}{1-q^{-r} z^{-1}}  \,=\, \exp\left(\, \sum_{n=1}^\infty \frac{-q^{-n}\overline z^{-n}+z^{-n}}{n(1-q^{-n})} \right) \notag \\
 &\simeq\; \exp\left(\, \sum_{n=1}^\infty \frac{-q^n z^{-n}+z^{-n}}{n(1-q^n)}  \right)\label{tetreorg} \\
 &\,=\, \prod_{r=0}^\infty \frac{1-q^{r+1}z^{-1}}{1-q^r \,\overline z^{-1}} = \mathcal{I}_\Delta(m;q,\zeta)\,. \notag
\end{aligned}$$

The necessary reorganization of cancellations happened in the middle step [\[tetreorg\]](#tetreorg){reference-type="eqref" reference="tetreorg"}, and established the $\rho$ symmetry. Note that this is *not* analytic continuation, since neither of the exponentials here make sense on the unit circle $|q|=1$ --- the expressions diverge at every root of unity.

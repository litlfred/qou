---
doc_id: arxiv-1112.5179v1
doc_title: "3-Manifolds and 3d Indices"
section_id: sec-001-2-actions-on-the-3d-index
section_title: "Actions on the 3d index"
section_number: 2
pages: 7-11
source_pdf: 1112.5179v1.pdf
source_sha256: b58af08336c40994
doc_brief: "3-Manifolds and 3d Indices — We identify a large classR of three-dimensionalN = 2 superconformal ﬁeld the- ories."
text_source: latex
latex_prose_ratio: 0.925
latex_coverage_ratio: 0.974
---
[]{#sec:actions label="sec:actions"}

Let us consider a 3d $\mathcal{N}=2$ SCFT $\mathcal{T}$ with flavor symmetry $U(1)^N$. The generalized supersymmetric index was defined in [@KW-index], following [@KMMR-index; @BBMR-index; @Kim-index; @IY-index; @KSV-index], as a trace

$$\label{IH}
\mathcal{I}_\mathcal{T}( m;q,\zeta) \;=\;
{\rm Tr}_{\mathcal{H}_{ m}} (-1)^Fe^{-\beta(E-R-j_3)}  q^{\frac{E+j_3}{2}} \zeta^{ e}$$

over a superselection sector of the Hilbert space of the 3d theory on $S^2$. Specifically, the Hilbert space $\mathcal{H}_m$ is labelled by the magnetic flux $m = (m_1,...,m_N)\in {\mathbb Z}^N$ on $S^2$ for $N$ background $U(1)$ gauge fields coupled to the flavor symmetry, $$m_i \; := \; \int_{S^2} \frac{F_i}{2 \pi} \,.
\label{mflux}$$ By standard arguments [@Witten-constraints], the index [\[IH\]](#IH){reference-type="eqref" reference="IH"} receives contributions only from states with energy $E = R + j_3$, where $R$ is the R-charge of a state

[^1]

and $j_3$ is the spin on $S^2$, with respect to a fixed, chosen axis. With this in mind, we can write the index more simply as

$$\label{Izeta}
\mathcal{I}_\mathcal{T}( m;q,\zeta) \;=\;
{\rm Tr}_{\mathcal{H}_{ m}} (-1)^F q^{\tfrac{R}{2} + j_3} \zeta^{ e}$$

The fugacity $\zeta$ measures the flavor charge $e\in {\mathbb Z}^N$ of states, and we use a shorthand notation $\zeta^e = \zeta_1^{e_1}\cdots \zeta_N^{e_N}$.

It is also often convenient to work with the index at fixed magnetic flux $m$ and at fixed electric charge $e$. We therefore collect $e$ and $m$ into a symplectic charge vector

$$\gamma = {m \choose e}$$

and define

$$\label{chargeindex}
\mathcal{I}_\mathcal{T}(\gamma;q)\; \equiv \; \mathcal{I}_\mathcal{T}(m,e;q)
 := {\rm Tr}_{\mathcal{H}_{m,e}} (-1)^F q^{\tfrac{R}{2} + j_3}.$$

Thus, $\displaystyle\mathcal{I}_\mathcal{T}(m;q,\zeta) = \sum_{e\in {\mathbb Z}^N}\mathcal{I}_\mathcal{T}(m,e;q)\,\zeta^e$, or conversely $\displaystyle\mathcal{I}_\mathcal{T}(m,e;q) = {\oint} \frac{d^N\zeta}{(2\pi i)^N
 \zeta^{e+1}} \mathcal{I}_\mathcal{T}(m;q,\zeta)\,,$ where $\zeta^{e+1}=\zeta_1^{e_1+1}\cdots\zeta_N^{e_N+1}$ and integration is done on the unit circle.

We note that even though the theory $\mathcal{T}$ is superconformal, the R-charge used to calculate the index need not coincide with the superconformal R-charge. The index is typically computed from a UV description of the theory, by a deformed Lagrangian on $S^2$ that preserves a half of the usual superconformal symmetries no matter how $R$ is defined [@IY-index; @FestucciaSeiberg]. The powers of $q$ produced by such a calculation could be unconstrained. However, if the UV theory flows to a IR SCFT whose R-symmetry is not accidental, there will be a R-symmetry redefinition that makes the powers of $q$ nonnegative. This is because the quantity $E+j_3$ in [\[IH\]](#IH){reference-type="eqref" reference="IH"} (and so $\tfrac R2+j_3$ when restricted to $E=R+j_3$) is nonnegative in superconformal theories, *cf.* [@Minwalla-restrictions]. Conversely, the absence of a such redefinition --- which we have yet to encounter in class $\mathcal{R}$ --- would signal a breakdown of the naive expectations for the RG flow of the UV theory.

[^2]

Finally, we should comment on the precise meaning of $(-1)^F$ in the trace. The most natural choice would be $(-1)^{2 j_3}$, but it is not the choice that is (implicitly) made in the literature on the refined index: in the presence of odd magnetic flux, the angular momentum on $S^2$ of a particle of odd electric charge is shifted by a half-integral amount, but no extra $(-1)$ sign is usually inserted compared to the index in even flux sectors. This is equivalent to a definition $$(-1)^F = (-1)^{2 j_3 + e\cdot m}\,.$$ The difference between the two conventions is fairly minimal: it is just an overall sign change $(-1)^{e\cdot m}$ of $\mathcal{I}_\mathcal{T}(m,e;q)$, or a redefinition of the fugacity $\zeta \to (-1)^m \zeta$ in $\mathcal{I}_\mathcal{T}( m;q,\zeta)$. In this paper we will stick to the modified form of $F$, mostly for reasons of notational convenience and backwards compatibility. We will return to some of these subtleties in later sections.

## The $Sp(2N,{\mathbb Z})$ action {#sec:Sp}

In [@Witten-SL2], an $Sp(2N,{\mathbb Z})$ action on 3d SCFT's with $N$ $U(1)$ flavor symmetries was introduced.

[^3]

The index [\[chargeindex\]](#chargeindex){reference-type="eqref" reference="chargeindex"} in the charge basis transforms very transparently under this action. Namely, for $g\in Sp(2N,{\mathbb Z})$, we have

[^4]

$$\label{Spem}
\boxed{\phantom{\int}\mathcal{I}_{g\circ \mathcal{T}}(g\,\gamma;q) = \mathcal{I}_\mathcal{T}(\gamma;q)\,.\phantom{\int}}$$

For simplicity, we can illustrate the action [\[Spem\]](#Spem){reference-type="eqref" reference="Spem"} for $N=1$ (*i.e.* a single $U(1)$ flavor symmetry) by looking at the action of the two generators $T$ and $S$ of $Sp(2,{\mathbb Z})\simeq SL(2,{\mathbb Z})$.

A $T$ transformation simply adds one unit of Chern-Simons coupling for the background $U(1)$ gauge field. The effect of the CS coupling for the flavor symmetry background gauge field is simply to shift the flavor charge of a state by an amount proportional to the magnetic flux. Therefore

$$\label{Tsim}
\mathcal{I}_{T\circ \mathcal{T}}(m,e+m;q) = \mathcal{I}_\mathcal{T}(e,m;q)\,,$$

which is compatible with the matrix representing $T$, $$T ~: \qquad
{m \choose e} \; \mapsto \;
{1 \quad 0 \choose 1 \quad 1} {m \choose e}\,.$$

An $S$ transformation makes the background gauge field dynamical, and adds a supersymmetric FI term for it. This effectively couples the resulting theory to a background $U(1)$ for a *new* flavor symmetry, whose conserved current is the magnetic flux of the old, now gauged, flavor symmetry. Thus, the new electric charge is the old magnetic flux. Gauging the old flavor symmetry also means that we should project onto states of zero gauge charge. However, turning on a magnetic flux $m'$ for the new flavor symmetry shifts the gauge charge of a state by $m'$, so in effect we project onto states of gauge charge $-m'$. Altogether we find

$$\label{Ssim}
\mathcal{I}_{S \circ \mathcal{T}}(-e,m;q) = \mathcal{I}_\mathcal{T}(m,e;q)\,,$$

which is compatible with the matrix representing $S$,

$$S ~: \qquad
{m \choose e} \; \mapsto \;
{0 \; -1 \choose 1\; \quad 0}  {m \choose e}\,.$$

From these matrix representations, it is easy to check that $\mathcal{I}_{(ST)^3\circ \mathcal{T}}(\gamma;q) = \mathcal{I}_\mathcal{T}(\gamma;q)$, and $\mathcal{I}_{S^2\circ\mathcal{T}}(\gamma;q)=\mathcal{I}_{\mathcal{T}}(-\gamma;q)$, as expected from the group relations $(ST)^3=\rm{id.}$ and $S^2 = C,$ where $C$ acts as charge conjugation.

The $T$ and $S$ transformations [\[Tsim\]](#Tsim){reference-type="eqref" reference="Tsim"}--[\[Ssim\]](#Ssim){reference-type="eqref" reference="Ssim"} could also be written in a "fugacity" basis for the index [\[Izeta\]](#Izeta){reference-type="eqref" reference="Izeta"}. We find

$$\begin{aligned}
 \mathcal{I}_{T\circ\mathcal{T}}(m;q,\zeta) &= \zeta^{m}\,\mathcal{I}_{\mathcal{T}}(m;q,\zeta)\,, \\

 \mathcal{I}_{S\circ \mathcal{T}}(m';q,\zeta') &= \sum_{m\in {\mathbb Z}}\oint \frac{d\zeta}{2\pi i \zeta}\, \zeta'{}^{m}\zeta^{m'}\,\mathcal{I}_{\mathcal{T}}(m;q,\zeta)\,,
\end{aligned}$$

with the integration done, as usual, on the unit circle. In this form, it is easier to see that the transformations agree with the general rules of [@KW-index; @IY-index] for gauging flavor symmetries and adding Chern-Simons terms to the index.

## Affine shifts {#sec:aff}

As mentioned above, the R-charge used in the index does not need to coincide with the R-charge that appears in the superconformal algebra. We can take $R$ to be any R-symmetry charge. If we redefine the R-charge by a flavor symmetry, then different choices are related by $R \to R -\alpha_e \cdot e$ for some vector $\alpha_e$. Under such a shift, the index varies accordingly as

$$\mathcal{I}_\mathcal{T}(m,e;q) \to q^{-\tfrac{1}{2} \alpha_e \cdot e} \mathcal{I}_\mathcal{T}(m,e;q)\,.$$

There is also a certain degree of latitude in choosing the R-charge of the vacuum in a non-trivial flux sector of the theory. It is thus natural to also consider redefinitions $R \to R +\alpha_m \cdot m$, under which

$$\mathcal{I}_\mathcal{T}(m,e;q) \to q^{\tfrac{1}{2}  \alpha_m \cdot m} \mathcal{I}_\mathcal{T}(m,e;q)\,.$$

Altogether, we can collect

$$\alpha = {\alpha_e \choose \alpha_m}\,,$$

and write

$$\boxed{\phantom{int}
\mathcal{I}_{\sigma^R(\alpha) \circ \mathcal{T}}(\gamma;q) = q^{\frac{1}{2} \langle \alpha, \gamma \rangle} \mathcal{I}_\mathcal{T}(\gamma;q) \phantom{\int}}$$

where $\sigma^R(\alpha) \circ \mathcal{T}$ denotes the theory with the new R-charge $R+\langle \alpha, \gamma \rangle$. Here the symplectic product $\langle \alpha, \gamma \rangle$ equals $\alpha_m \cdot m - \alpha_e \cdot e$.

Similar shifts can happen in the definition of the fermion number charge $F$. This would not be the case if we had defined $(-1)^F = (-1)^{2 j_3}$, as $j_3$ is a generator in a non-Abelian symmetry group. But the symplectic group acts on $(-1)^{e\cdot m}$ in a rather interesting way. Indeed, $s(\gamma) = (-1)^{e \cdot m}$ is a "quadratic refinement of the charge lattice", *i.e.* a $Z_2$-valued function of charges with the property $$s(\gamma) s(\gamma') = s(\gamma + \gamma') (-1)^{\langle \gamma, \gamma' \rangle}\,.$$ Any two such refinements differ by a factor of the form $(-1)^{\langle \alpha, \gamma \rangle}$ for some $\alpha$.

Thus, we will just introduce a fermion-number shift operation

$$\boxed{\phantom{\int} \mathcal{I}_{\sigma^F(\alpha) \circ T}(\gamma;q) = (-1)^{\langle \alpha, \gamma \rangle} \mathcal{I}_\mathcal{T}(\gamma;q) \phantom{\int}}$$

that modifies the choice of quadratic refinement used in $F$. Note that $[\sigma^F(\alpha)]^2=1$ for any $\alpha$. Such shifts in the definition of $R$ and $F$ are often important when comparing mirror descriptions of the same theory. In particular, a symplectic transformation will change the choice of quadratic refinement from $s(\gamma)$ to $s(g \gamma)$, which will have to be brought back to $s(\gamma)$ by a fermion number shift.

In the following, we will often find that $R$ and $F$ shifts happen simultaneously, with the same parameter $\alpha$. This is ultimately due to the fact that the UV description of the theories often have a natural R-charge assignment such that $(-1)^F = (-1)^R$, *i.e.* $(-1)^{R + 2 j_3 + e \cdot m} =1$ when acting on all the chiral fields in the Lagrangian.

[^5]

Mathematically, the shifts in $R$ and $F$ generate an abelian group of translations ${\mathbb Z}^{2N}\times ({\mathbb Z}_2)^{2N}$ that acts on the index. This abelian group can naturally be combined with the symplectic group $Sp(2N,{\mathbb Z})$ to generate an affine symplectic group $Sp(2N,{\mathbb Z}) \ltimes ({\mathbb Z}\times {\mathbb Z}_2)^{2N}$. One can check that the expected group relations are satisfied. For example, taking $N=1$, if we denote the generators of unit electric and magnetic shifts by $\sigma_e^R,\,\sigma_e^F$ and $\sigma_m^R,\,\sigma_m^F$, respectively, then

$$\label{affrels}
\begin{equation}S\sigma_e^R = \sigma_m^R S\,, \quad\qquad
S\sigma_m^R = (\sigma_e^R){}^{-1}S\,,\end{equation}
\begin{equation}T^{-1}(\sigma_e^R)^{-1}T\sigma_e^R = \sigma_m^R\,,\quad\qquad T\sigma_m^R = \sigma_m^R T\,, \end{equation}$$

and similarly for $\sigma^F_{e,m}$. The abelian $({\mathbb Z}\times {\mathbb Z}_2)^{2N}$ subgroup of the affine symplectic group does act in the obvious way by translations on the vector $(m,e)$. However, we will see momentarily that there exists another object, a certain algebra of operators associated with the index, on which this abelian subgroup *is* represented by translations.

[^1]: Although we consider superconformal theories here, $R$ does not have to be the same as the R-charge that enters into the superconformal algebra, *cf.* [@IY-index].

[^2]: This is a possibly more refined version of the requirement of positive monopole operator dimensions used to discuss the IR behavior of $\mathcal{N}=4$ gauge theories [@GW-Sduality].

[^3]: We refer the reader to [@Witten-SL2], as well as [@DGG], for details of $Sp(2N,{\mathbb Z})$ transformations on SCFT's. Our notation here closely follows that in [@DGG].

[^4]: Note that the $Sp(2N,{\mathbb Z})$ transformation acts non-trivially on the $(-1)^{e \cdot m}$ factor we included in the definition of the fermion number. We will return to this in Section [0.2](#sec:aff){reference-type="ref" reference="sec:aff"}.

[^5]: It is interesting to remark that in the context of four-dimensional ${\cal N}=2$ gauge theory, wall-crossing considerations lead to the conjecture that $(-1)^{R + 2 j_3}$ should always be equal to a quadratic refinement of the charge lattice when acting on BPS states [@GMNIII].

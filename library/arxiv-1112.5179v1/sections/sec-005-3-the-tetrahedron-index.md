---
doc_id: arxiv-1112.5179v1
doc_title: "3-Manifolds and 3d Indices"
section_id: sec-005-3-the-tetrahedron-index
section_title: "The tetrahedron index"
section_number: 3
pages: 16-18
source_pdf: 1112.5179v1.pdf
source_sha256: b58af08336c40994
text_source: latex
latex_prose_ratio: 0.605
latex_coverage_ratio: 0.978
doc_brief: "3-Manifolds and 3d Indices — We identify a large classR of three-dimensionalN = 2 superconformal ﬁeld the- ories."
---
[]{#sec:T1 label="sec:T1"}

The basic building block used to construct the theory $T_M$ for any 3-manifold $M$ is the theory $T_\Delta$ associated to a single ideal tetrahedron. More precisely, we should call the theory

$$\begin{equation}
T_{\Delta,\Pi_Z}\,, \label{tetthy}
\end{equation}$$

since it depends on a polarization for the boundary of the tetrahedron. As discussed in Sections 2 and 4 of [@DGG], we make a specific choice of polarization $\Pi_Z$ (see also Section [0.3](#sec:tetdiff){reference-type="ref" reference="sec:tetdiff"} below). Then $T_\Delta$ consists of a single free $\mathcal{N}=2$ chiral multiplet $\phi$, coupled to a background $U(1)$ gauge multiplet with a level $-\tfrac12$ Chern-Simons interaction.

In order to calculate the index of $T_\Delta$, we must specify the R-charge and fermion number assignments for the theory on $S^2\times S^1$. We take $R_\phi=F_\phi=0$, and also require that the vacuum in a flux sector of any negative charge $m$ has $R_{\rm vac}=F_{\rm vac}=0$. Then, by following the rules for constructing indices in [@KW-index; @IY-index], we find

$$\begin{equation}
\mathcal{I}_\Delta(m;q,\zeta) \,\equiv\, \mathcal{I}_{T_\Delta,\Pi_Z}(m;q,\zeta) \,=\,  (-q^{\frac12})^{\frac12(m+|m|)}\zeta^{-\frac12(m+|m|)} \prod_{r=0}^\infty \frac{1- q^{r+\frac12|m|+1}\zeta^{-1}}{1-q^{r+\frac12|m|}\zeta}\,. \label{Iztet}
\end{equation}$$

It turns out that this expression simplifies nicely to

$$\begin{equation}
\mathcal{I}_\Delta(m;q,\zeta) =\prod_{r=0}^\infty \frac{1- q^{r-\frac12m+1}\zeta^{-1}}{1-q^{r-\frac12m}\zeta}\,. \label{Iztet2}
\end{equation}$$

The various ingredients in [\[Iztet\]](#Iztet){reference-type="eqref" reference="Iztet"} can be given an intuitive explanation. The denominator in the product arises from bosonic creation operators of flavor charge $1$ and spin $r+\tfrac{|m|}{2}$ acting on the vacuum. The spin starts from $\tfrac{|m|}{2}$ due to the nontrivial magnetic flux on $S^2$. The numerator arises similarly from fermionic creation operators of flavor charge $-1$ and spin $r+\tfrac{|m|}{2}+1$.

In addition to the product, the prefactor $(-q^{\frac12})^{\frac12(|m|+m)}\zeta^{-\frac12(m+|m|)}$ in [\[Iztet\]](#Iztet){reference-type="eqref" reference="Iztet"} turns out to be both subtle and important. It depends on the energy, R-charge, and flavor charge of the ground state in a non-trivial flux sector, which have been calculated carefully in *e.g.* [@BKW-monopoles]. First, the flavor charge of the flux vacuum is affected by the quantization of (anti)fermions in the chiral multiplet, and receives from that a contribution $-\tfrac12|m|$. This is corrected by the Chern-Simons coupling $k=-\tfrac12$ to $-\tfrac12(m+|m|)$. In order to determine the R-charge $R_{\rm vac}$ and fermion number $F_{\rm vac}$, we can shift conventions so that $R_\phi=F_\phi=1$ for the free chiral boson. Then $R=F=0$ for the fermion zero-mode whose quantization determines the quantum numbers of the vacuum, implying $R_{\rm vac}=F_{\rm vac}=0$. In terms of the index [\[Iztet\]](#Iztet){reference-type="eqref" reference="Iztet"}, we can easily perform the shift to $R_\phi=F_\phi=1$ by setting $\zeta\to (-q^{\frac12})\zeta$. Then it is easy to see that the vacuum acquires $R_{\rm vac}=F_{\rm vac}=0$ as expected.

It is important to remark a subtle sign difference between our prescription for the index of a chiral multiplet and the prescription that can be found in the literature [@IY-index; @KW-index]. After aligning the choices of R-charge and CS terms, the difference boils down to the prefactor $(-1)^{\frac12(|m|+m)}$. This prefactor affects in a minimal way the checks of mirror symmetry that have already been done in the literature, as it only affects the overall sign of the index in a given charge sector. However, only with our definition of the chiral index can such signs be matched universally via an appropriate shift of $F$. This deeply affects the calculation of the index in theories whose superpotentials have monopole operators --- which is standard in class $\mathcal{R}$.

Let us also write the index in an electric-magnetic charge basis, as in Section [\[sec:actions\]](#sec:actions){reference-type="ref" reference="sec:actions"}. By using several standard identities for $q$-series, we find

$$\begin{equation}
\mathcal{I}_\Delta(m;q,\zeta) \,=\, \sum_{e\in {\mathbb Z}} \mathcal{I}_\Delta(m,e;q)\zeta^e\,,
\end{equation}$$

with

$$\begin{equation}
\mathcal{I}_\Delta(m,e;q) \,=\, \sum_{n=\lfloor e\rfloor}^\infty
 \frac{(-1)^n q^{\frac12 n(n+1)-\big( n+\frac 12e\big) m}}{(q)_n\,(q)_{n+e}}\,, \label{Imetet}
\end{equation}$$

where $\lfloor e \rfloor \equiv \tfrac12(|e|-e)$ and $(q)_n \equiv (1-q)(1-q^2)\cdots (1-q^n)$. The sum in [\[Imetet\]](#Imetet){reference-type="eqref" reference="Imetet"} can be thought of as defining a formal power series in $q$; for fixed charge $\gamma=(m,e)$, only finitely many terms in the sum are necessary for calculating $\mathcal{I}_\Delta(m,e;q)$ to a desired order in $q$. The series [\[Imetet\]](#Imetet){reference-type="eqref" reference="Imetet"} also appears to converge to a well-defined analytic function of $q$ for $|q|<1$.

In anticipation of the interpretation of the tetrahedron index as a geometric invariant of an ideal tetrahedron $\Delta$ itself (and connections to the classical Bloch group), we can take the "classical limit" $q =e^\hbar \to 1$ and $m\to \infty$ with $q^m$ fixed. Let us set $q^{\frac m2}\zeta=z$, remembering that $\zeta$ is a pure phase, so that $z$ becomes a complex number. Then

$$\begin{equation}
\label{tetasymp}
\mathcal{I}_\Delta(m;q,\zeta) \;=\; \prod_{r=0}^\infty \frac{1-q^{r+1}z^{-1}}{1-q^r \,\overline z^{-1}}\;\;\overset{\hbar\to 0}{\sim}\;\; \exp\left( \frac{2V_\Delta(z)}{i\hbar}+\ldots\right)\,,
\end{equation}$$

where the function

$$\begin{equation}
V_\Delta(z) \equiv -{\rm Im}\,{\rm Li}_2(z^{-1})
\end{equation}$$

is closely related to the hyperbolic volume of a tetrahedron with shape parameter $z$. In fact, the actual volume can be written as ${\rm Vol}_\Delta(z) = V_\Delta(z) + \arg(1-z^{-1})\log|z|$ , *cf.* [@Thurston-1980].

## Parity and $\rho$ symmetry {#sec:tetkappa}

Several identities satisfied by the tetrahedron index can be understood via discrete symmetries acting on $T_\Delta$. Let's first consider the action of parity $\mathbf{P}$ on $T_\Delta$. In is not an exact symmetry because it inverts the sign of the Chern-Simons level, from $k=-\tfrac12$ to $k=\tfrac12$. However, this can be compensated for by subtracting a Chern-Simons term, *i.e.* applying $T^{-1}\in Sp(2,{\mathbb Z})$. In the $S^2\times S^1$ background, it actually turns out that the R-charge and fermion number of the vacuum must also be shifted, so that altogether we get

$$\begin{equation}
\label{PonT}
T_\Delta\;\simeq\; \sigma_m^R\sigma_m^F T^{-1}\circ \mathbf{P}\,T_\Delta\,.
\end{equation}$$

Acting on the index, $\mathbf P$ simply sends $m\to -m$, so [\[PonT\]](#PonT){reference-type="eqref" reference="PonT"} implies

$$\begin{equation}
\mathcal{I}_\Delta(m,e;q) = \big(-q^{\frac12}\big)^m\mathcal{I}_\Delta(-m,e+m;q)\,.
\label{tetPem}
\end{equation}$$

This identity can be checked explicitly (see Appendix [\[app:ST\]](#app:ST){reference-type="ref" reference="app:ST"}), most easily after converting to the fugacity basis.

The $\rho$ symmetry of Section [\[sec:kappa\]](#sec:kappa){reference-type="ref" reference="sec:kappa"} is more universal than parity, but also more subtle to implement. Naively, it sends $\mathcal{I}_\Delta(m;q,\zeta)$ to $\mathcal{I}_\Delta(-m;q^{-1},\zeta^{-1})$; but the latter does not make sense for $|q|<1$. In order to properly apply the symmetry, we need to reorganize the Hilbert space $\mathcal{H}_{-m}$, and to reinterpret $\mathcal{I}_\Delta(-m;q^{-1},\zeta^{-1})$ as a series in $q$. For the tetrahedron, this is actually straightforward.

Let us set $z=q^{\frac m2}\zeta$, $\overline z=q^{\frac m2}\zeta^{-1}$, noting that $\rho$ acts on $z$ by complex conjugation. Then

$$\begin{align}
 \mathcal{I}_\Delta(-m;q^{-1},\zeta^{-1}) &\,=\, \prod_{r=0}^\infty \frac{1-q^{-r-1}\,\overline z^{-1}}{1-q^{-r} z^{-1}}  \,=\, \exp\left(\, \sum_{n=1}^\infty \frac{-q^{-n}\overline z^{-n}+z^{-n}}{n(1-q^{-n})} \right) \notag \\
 &\simeq\; \exp\left(\, \sum_{n=1}^\infty \frac{-q^n z^{-n}+z^{-n}}{n(1-q^n)}  \right)\label{tetreorg} \\
 &\,=\, \prod_{r=0}^\infty \frac{1-q^{r+1}z^{-1}}{1-q^r \,\overline z^{-1}} = \mathcal{I}_\Delta(m;q,\zeta)\,. \notag
\end{align}$$

The necessary reorganization of cancellations happened in the middle step [\[tetreorg\]](#tetreorg){reference-type="eqref" reference="tetreorg"}, and established the $\rho$ symmetry. Note that this is *not* analytic continuation, since neither of the exponentials here make sense on the unit circle $|q|=1$ --- the expressions diverge at every root of unity.

## Triality {#sec:tri}

Experimentally, we observe that the tetrahedron index enjoys yet another more interesting discrete symmetry of order three:

$$\begin{equation}
\mathcal{I}_\Delta(m,e;q) = \big(-q^{\frac12}\big)^{-e}\mathcal{I}_\Delta(e,-e-m;q)=\big(-q^{\frac12}\big)^{m}\mathcal{I}_\Delta(-e-m,m;q)\,. \label{tettri}
\end{equation}$$

For a visual demonstration of this symmetry, let us define ${\rm lead}(m,e)$ to be the leading power of $q$ that appears in $\mathcal{I}_\Delta(m,e;q)$ when written as a series in $q$. For example,

$$\begin{equation}
\begin{array}{ll}
 \mathcal{I}_\Delta(0,0;q) = 1-q-2q^2-2q^3-2q^4+q^6+5q^7+...\qquad &\Rightarrow\quad {\rm lead}(0,0)=0\,, \\[.1cm]
 \mathcal{I}_\Delta(1,0;q) = -q-q^2+q^4+3q^5+4q^6+6q^7+6q^8+...\qquad &\Rightarrow \quad {\rm lead}(1,0)=1\,, \\[.1cm]
 \mathcal{I}_\Delta(1,2;q) = -q^2-q^3-q^4-q^5+q^7+3q^8+5q^9+... \qquad &\Rightarrow\quad {\rm lead}(1,2) = 2\,,
\end{array}
\end{equation}$$

*etc.* It can be shown from [\[Imetet\]](#Imetet){reference-type="eqref" reference="Imetet"} that ${\rm lead}(m,e)\geq 0$ for all $m,e$. A graph of ${\rm lead}(m,e)$ appears in Figure [1](#fig:lead){reference-type="ref" reference="fig:lead"}, which clearly hints at a ${\mathbb Z}_3$ "rotation" symmetry in the index as in [\[tettri\]](#tettri){reference-type="eqref" reference="tettri"}. We will describe a method of proving [\[tettri\]](#tettri){reference-type="eqref" reference="tettri"} in Section [0.3](#sec:tetdiff){reference-type="ref" reference="sec:tetdiff"}, using difference equations for the index.

<figure id="fig:lead" data-latex-placement="htb">
<img src="lead" style="width:3.8in" />
<figcaption>Leading powers of <span class="math inline"><em>q</em></span> in the index. The graph interpolates smoothly between integer points.</figcaption>
</figure>

In order to acquire further intuition for the triality symmetry of $\mathcal{I}_\Delta$, it is instructive to observe that [\[tettri\]](#tettri){reference-type="eqref" reference="tettri"} can be written as

$$\begin{equation}
\mathcal{I}_\Delta(m,e;q) = \mathcal{I}_{\sigma_eST\circ \Delta}(m,e;q)=\mathcal{I}_{(\sigma_eST)^2\circ\Delta}(m,e;q)\,, \label{tetST}
\end{equation}$$

where $ST\in Sp(2,{\mathbb Z})$ and $\sigma_e \equiv \sigma_e^R\sigma_e^F$ are affine symplectic transformations of the tetrahedron theory, as described in Section [\[sec:actions\]](#sec:actions){reference-type="ref" reference="sec:actions"}. The transformation $\sigma_eST$ has order three. Then we recall from [@DGG] that the tetrahedron SCFT $T_\Delta$ is invariant

[^1]

under the cyclic action of $\sigma_eST$, due to 3d $\mathcal{N}=2$ mirror symmetry [@IS; @AHISS; @dBHOY; @dBHO]. In other words, the following UV theories flow to the same IR fixed point:

$$\begin{equation}
\begin{array}{r@{\quad}l}
T_\Delta\,: & \text{free chiral with global $U(1)$ symmetry at CS level $-\tfrac12$}\\[.2cm]
\sigma_eST\circ T_\Delta\,: & \text{gauged $U(1)$ theory at CS level $+\tfrac12$, coupled to a single chiral}\,.
\end{array}
\end{equation}$$

Since these theories are mirror symmetric their indices must be the same, and that is precisely what we see in [\[tettri\]](#tettri){reference-type="eqref" reference="tettri"} and [\[tetST\]](#tetST){reference-type="eqref" reference="tetST"}.

## Difference equations {#sec:tetdiff}

A final interesting property of the tetrahedron index is the fact that it obeys two difference equations. In terms of operators $\hat x_{\pm}=\exp(\hat X_\pm)$ and $\hat p_\pm =\exp(\hat P_\pm)$ as defined in Section [\[sec:ops\]](#sec:ops){reference-type="ref" reference="sec:ops"}, these are

$$\begin{equation}
\big(\hat p_++\hat x_+^{-1}-1\big)\mathcal{I}_\Delta = 0\,,\qquad
  \big(\hat p_-+\hat x_-^{-1}-1\big)\mathcal{I}_\Delta = 0\,.
\label{teteqs}
\end{equation}$$

For example, writing these out in the charge basis we find

$$\label{teteqsem}
\begin{align}
 q^{\frac e2}\mathcal{I}_\Delta(m+1,e)+q^{-\frac m2}\mathcal{I}_\Delta(m,e+1)-\mathcal{I}_\Delta(m,e) = 0\,, \\
 q^{\frac e2}\mathcal{I}_\Delta(m-1,e)+q^{-\frac m2}\mathcal{I}_\Delta(m,e-1)-\mathcal{I}_\Delta(m,e) = 0\,,
\end{align}$$

for all $m,e$. These equations are compatible with the $\rho$ symmetry of the index, which interchanges the two $(\pm)$ sets of operators. The validity of [\[teteqs\]](#teteqs){reference-type="eqref" reference="teteqs"} can be checked easily by writing the index in a fugacity basis, and using the product formula [\[Iztet2\]](#Iztet2){reference-type="eqref" reference="Iztet2"}. Also, in the semi-classical regime [\[tetasymp\]](#tetasymp){reference-type="eqref" reference="tetasymp"} each of the difference equations [\[teteqs\]](#teteqs){reference-type="eqref" reference="teteqs"} turns into a differential equation, equivalent to the standard property of the dilogarithm function, $z\tfrac{d}{dz} \text{Li}_2 (z) =  \log (1-z^{-1})$.

Equations [\[teteqs\]](#teteqs){reference-type="eqref" reference="teteqs"} may look familiar from the study of "quantum Lagrangians" and $S^3_b$ partition functions in [@DG-Sdual; @DGG]. As anticipated in Section [\[sec:ops\]](#sec:ops){reference-type="ref" reference="sec:ops"}, these are the *same* difference equations obeyed by the $S^3_b$ partition function of $T_\Delta$, with an appropriate identification of the operators $\hat x_\pm,\,\hat p_\pm$. We will try to explain the reason behind this in Section [\[sec:3d4d\]](#sec:3d4d){reference-type="ref" reference="sec:3d4d"}. In essence, the same universal algebra of line operators is acting on both the index and the $S^3_b$ partition functions; Ward identities for the line operators then lead to [\[teteqs\]](#teteqs){reference-type="eqref" reference="teteqs"}.

::: wrapfigure
r2in ![image](tet){width="1.8in"}
:::

In terms of the tetrahedron $\Delta$ itself, Equations [\[teteqs\]](#teteqs){reference-type="eqref" reference="teteqs"} are two copies of the quantized Lagrangian $\hat \mathcal{L}_\Delta$ that describes which flat $SL(2,{\mathbb C})$ connections on the boundary $\partial\Delta$ can be extended as flat connections in the interior of $\Delta$. To see this, recall

[^2]

from [@Dimofte-QRS; @DGG] that the set of flat connections on $\partial\Delta$, *a.k.a.* the phase space $\mathcal{P}_{\partial\Delta}$, is described by three ${\mathbb C}^*$--valued edge coordinates $z,z',z''$, subject to the condition that $zz'z''=-1$. Upon quantization, these coordinates form an algebra of operators with $q$-commutation relations

$$\begin{equation}
\hat z\hat z'=q \hat z'\hat z\,,\qquad \hat z'\hat z''=q\hat z''\hat z'\,,\qquad \hat z''\hat z=q\hat z\hat z''\,,
\end{equation}$$

and a central constraint

$$\begin{equation}
\hat z''\hat z'\hat z= -1\,. \label{zconst}
\end{equation}$$

(For logarithms of the $\hat z$'s, written in uppercase letters, the constraint reads $\hat Z+\hat Z'+\hat Z''=i\pi+\hbar/2$.) Similarly, the classical Lagrangian $\mathcal{L}_\Delta = \{z''+z^{-1}-1=0\}$, describing flat connections in the interior of $\Delta$, becomes promoted to a quantum operator (*cf.* [@gukov-2003])

$$\begin{equation}
\hat\mathcal{L}_\Delta = \hat z''-\hat z^{-1}-1\,, \label{tetLag}
\end{equation}$$

which must annihilate any putative wavefunction of the tetrahedron, in any representation. It should then be clear that Equations [\[teteqs\]](#teteqs){reference-type="eqref" reference="teteqs"} are just two copies of [\[tetLag\]](#tetLag){reference-type="eqref" reference="tetLag"}, with opposite quantization parameters $\hbar$ and $-\hbar$. Indeed, using the classical complex variables $z=q^{\frac m2}\zeta,\, \overline z=q^{\frac m2}\zeta^{-1}$, or logarithmically $Z = \tfrac m2\hbar+i\theta,\,\overline Z=\tfrac m2\hbar-i\theta$ (*cf.* [\[XPz\]](#XPz){reference-type="eqref" reference="XPz"}), we find that we can identify $(\hat P_+,\hat X_+) = (\hbar \partial_Z,Z)$ and $(\hat P_-,\hat X_-)=(-\hbar \partial_{\overline Z},\overline Z)$.

The Lagrangian [\[tetLag\]](#tetLag){reference-type="eqref" reference="tetLag"} is invariant under cyclic permutations $\hat z\to \hat z'\to\hat z''\to \hat z$ in the operator algebra for the tetrahedron. That is, the equation $\hat \mathcal{L}_\Delta\,\psi=0$ for any putative wavefunction $\psi$ can be written using any pair of consecutive variables $(\hat z'',\hat z)$, $(\hat z,\hat z')$, or $(\hat z',\hat z'')$, thanks to the constraint [\[zconst\]](#zconst){reference-type="eqref" reference="zconst"}. Moreover, the generator of the ${\mathbb Z}_3$ cyclic symmetry is none other than our familiar affine $Sp(2,{\mathbb Z})$ element $\sigma_eST$, *cf.* [\[tetST\]](#tetST){reference-type="eqref" reference="tetST"}, acting on logarithms of the $\hat z$ operators. For example, if we identify $(\hat P_+,\hat X_+) = (\hat Z'',\hat Z)$ and $(\hat P_+',\hat X_+')=(\hat Z,\hat Z')$, then

$$\begin{equation}
\label{XPST}
\begin{pmatrix} \hat X_+' \\ \hat P_+ '\end{pmatrix}
 = \sigma_eST \begin{pmatrix} \hat X_+ \\ \hat P_+ \end{pmatrix}
 = \begin{pmatrix} -1 & -1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} \hat X_+ \\ \hat P_+ \end{pmatrix}+\begin{pmatrix} i\pi+\tfrac\hbar2 \\ 0 \end{pmatrix}\,.
\end{equation}$$

Together with the intertwining property [\[intertwine\]](#intertwine){reference-type="eqref" reference="intertwine"} for the index, the cyclic symmetry of the quantized Lagrangian guarantees that $\mathcal{I}_\Delta$, $\mathcal{I}_{\sigma_eST\circ \Delta}$, and $\mathcal{I}_{(\sigma_eST)^2\circ\Delta}$ all satisfy the *same* equations [\[teteqs\]](#teteqs){reference-type="eqref" reference="teteqs"}. This constitutes the basis for a proof that $\mathcal{I}_\Delta = \mathcal{I}_{\sigma_eST\circ \Delta} = \mathcal{I}_{(\sigma_eST)^2\circ\Delta}$, as in [\[tetST\]](#tetST){reference-type="eqref" reference="tetST"}, since the solutions to the difference equations are unique given appropriate boundary conditions. Details appear in Appendix [\[app:ST\]](#app:ST){reference-type="ref" reference="app:ST"}.

[^1]: The decoration of the symplectic transformation $ST$ by an R-charge and fermion number shift $\sigma_e=\sigma^R_e\sigma^F_e$ is correlated with the precise definition of the tetrahedron theory in the twisted $S^2\times S^1$ geometry, as discussed above [\[Iztet\]](#Iztet){reference-type="eqref" reference="Iztet"}. Had we chosen different $R$ and $F$ assignments for $T_\Delta$, the affine shift would look slightly different.

[^2]: Throughout this paper, we will be quite brief with details of flat connections and 3d geometry. We direct the reader to the summary of triangulations in Section 2 of [@DGG] and references therein (especially the classic [@Thurston-1980; @NZ]) for some potentially useful background.

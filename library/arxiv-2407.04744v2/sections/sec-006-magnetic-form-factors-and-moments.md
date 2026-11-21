---
doc_id: arxiv-2407.04744v2
doc_title: "Magnetic structure of A ≤ 10 nuclei using the Norfolk nuclear models with quantum Monte Carlo methods"
section_id: sec-006-magnetic-form-factors-and-moments
section_title: "Magnetic form factors and moments"
section_number: null
pages: 5-5
source_pdf: 2407.04744v2.pdf
source_sha256: fc6fda3138296fb1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.959
latex_coverage_ratio: 0.976
doc_brief: "Magnetic structure of A ≤ 10 nuclei using the Norfolk nuclear models with quantum Monte Carlo methods — 26 sections: Magnetic structure of A 10 nuclei ; Introduction; Theory"
---
[]{#sec:multipole label="sec:multipole"}

The magnetic form factors are extracted from elastic electron scattering differential cross section data (see Ref. [@Donnelly1984] for a review). For this work we use the definition given in Ref. [@Donnelly1984], *i.e.*, $$\begin{aligned}
F_M^2(q)= \frac{1}{2 J+1} \sum_{L=1}^{\infty}\left|\left\langle J ||M_L(q)|| J\right\rangle\right|^2\,,\label{eq:fm}
\end{aligned}$$ where we express the magnetic form factor as a function of the reduced matrix elements (RMEs) of the magnetic multipole operators ($M_L$), and $J$ is the total angular momentum of the nucleus.

The calculation of the magnetic multipole expansion is carried out using standard techniques [@Walecka1995] implemented to expand the current operator $\bfj(\bfq)$. As the reference frame, we adopt the one where $\hat{\bm{z}}$ is the spin-quantization axis of the nucleus, and the direction of $\hat{\bfq}$ is defined by the angles $\theta$ and $\phi$, the polar and azimuthal angles with respect to this axis, respectively. In what follows, we define $q=|\bfq|$. The current, in terms of the magnetic and electric multipoles, $M_{L M_L}$ and $E_{L M_L}$, reads $$\begin{aligned}
\mathrm{j}_{\lambda}(\mathbf{q})= & \int d \mathbf{x}\, e^{i \mathbf{q} \cdot \mathbf{x}} \hat{\mathbf{e}}_{\lambda} \cdot \mathbf{j}(\mathbf{x}) \\
= & -\sum_{L \geq 1,M_L} \sqrt{2 \pi(2 L+1)} i^L D_{M_L, \lambda}^L(-\phi,-\theta, \phi)\\
&\times  \left[\lambda M_{L M_L}(q)+E_{L M_L}(q)\right], \label{eq:jmultipole}
\end{aligned}$$ where $\lambda=\pm1$, and $D_{M_L, \lambda}^L$ are the Wigner rotation matrices [@Edmonds1957]. The unit vector $\hat{\mathbf{e}}_{q \lambda}$ indicates the linear combination $$\hat{\mathbf{e}}_{\lambda=\pm1}=\mp\frac{\hat{\mathbf{e}}_{1}\pm\hat{\mathbf{e}}_{2}}{\sqrt{2}}\,,$$ where $\hat{\mathbf{e}}_{3}=\hat{\bfq}$, $\hat{\mathbf{e}}_{2}=\hat{\bm{z}}\times\hat{\bfq}$, and $\hat{\mathbf{e}}_{1}=\hat{\mathbf{e}}_{2}\times\hat{\mathbf{e}}_{3}$. Note that, for elastic scattering, the electric multipole operators ($E_L$) vanish because of time reversal invariance [@Forest1966], and the sum over $L$ runs only on odd values because of parity conservation.

As observed in Ref. [@Carlson2015], in VMC and GFMC calculations, it is more efficient to compute the matrix elements of $\bfj(\bfq)$ between states of a specific spin configuration $M_J$ (usually $M_J=J$) and then adjust the direction of $\hat{\bfq}$ to isolate the single RME contributions. In our case, it is very convenient to select $\bfq$ to be in the $x-z$ plane. This makes $\phi=0$, and $\hat{\mathbf{e}}_2=\hat{\bm y}$. Leveraging this selection and making use of the Wigner-Eckart theorem in Eq. ([\[eq:jmultipole\]](#eq:jmultipole){reference-type="ref" reference="eq:jmultipole"}), the matrix element reduces to [@Carlson2015] $$\begin{aligned}\label{eq:mej}
 \left\langle J J \left|\mathrm{j}_{y}(\mathbf{q})\right| J J\right\rangle
= &\sqrt{4 \pi}\sum_{L \geq 1} i^{L+1}  \frac{\langle J J, J -\!J| L 0 \rangle}{\sqrt{L(L+1)}} \\
&\times P^1_L(\cos \theta)\left\langle J|| M_L(q) \| J\right\rangle\,.
\end{aligned}$$

The various multipole contribution to the magnetic form factor for the nuclei considered in this work are summarized in Table [1](#tab:tab_multi){reference-type="ref" reference="tab:tab_multi"}. The number of independent matrix elements with different directions of $\bfq$ (*i.e.*, of different $\theta$'s) that have to be computed is equal to the number of multipoles allowed. Clearly, any independent choice of the directions are equivalent; in Appendix [\[sec:app1\]](#sec:app1){reference-type="ref" reference="sec:app1"} we present the explicit formulas obtained for our specific choices.

::: {#tab:tab_multi}
   $J^\pi$                                Nuclei                                    Multipoles
  --------- ------------------------------------------------------------------ ---------------------
   $1/2^+$                    ${}^3\text{He}$,${}^3\text{H}$                           $M_1$
    $1^+$                            ${}^6\text{Li}$                                   $M_1$
   $3/2^-$                   ${}^7\text{Li}$, ${}^7\text{Be}$                      $M_1$, $M_3$
    $2^+$                    ${}^8\text{Li}$, ${}^8\text{B}$                       $M_1$, $M_3$
   $3/2^-$   ${}^9\text{Li}$, ${}^9\text{C}$, ${}^9\text{Be}$, ${}^9\text{B}$      $M_1$, $M_3$
    $3^+$                           ${}^{10}\text{B}$                           $M_1$, $M_3$, $M_5$

  : Multipole contributions to the magnetic form factors for the nuclei considered in this work.
:::

From the small $q$ behaviour of the magnetic form factor it is possible to extract the magnetic (dipole) moment of the nucleus. Starting from the definition of the magnetic moment, it is possible to show that [@Carlson2015] $$\left\langle J|| M_1(q)|| J\right\rangle \simeq \frac{i}{\sqrt{2 \pi} \langle J J,J -\!J |1 0\rangle} \frac{q}{2 m_N} \mu \,.$$ Therefore, considering that the higher-order multipoles have a negligible contribution to the magnetic moment at small $q$ we can select the matrix element computed for $\theta=\pi/2$ (any choice is equivalent) and so the magnetic moment becomes $$\mu = \lim_{q\to 0} -i \frac{2m_N}{q}\mel{JJ}{\mathrm{j}_y(q \hat{\bm x})}{JJ}\,.
\label{eq:mm}$$ To extract $\mu$, we evaluate $\mel{JJ}{\mathrm{j}_y(q\bfxh)}{JJ}$ for $q \in [0.00,0.25]$ fm$^{-1}$ and fit the results to a polynomial, similarly to what was done for the multipole analysis of the $^6$He $\beta$-decay spectrum in Ref. [@King:2022zkz]. The linear coefficient is then used to determine the quantity of interest.

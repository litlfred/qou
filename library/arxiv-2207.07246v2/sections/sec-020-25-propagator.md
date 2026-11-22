---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-020-25-propagator
section_title: "Propagator"
section_number: 2.5
pages: 42-45
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.916
latex_coverage_ratio: 0.992
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 73 sections: Front matter; ABSTRACT; ACKNOWLEDGEMENTS"
---
[]{#propagator label="propagator"} Efficiently sampling the imaginary time propagator $e^{-H \Delta \tau}$ by using a short-time approximated propagator $U(\Delta \tau)$ is important for PIMC. Due to the fact that the local chiral N$^2$LO interaction contains the spin-orbit term $v_{LS}(r_{ij})$ in Eq.([\[vlsrij\]](#vlsrij){reference-type="ref" reference="vlsrij"}), the approximated short-time propagator $U(\Delta \tau)$ for $e^{-H \Delta \tau}$ is calculated as, $$\begin{aligned}
U(\Delta \tau) & \equiv
e^{-\frac{\mathcal{V}^\dagger}{2} \Delta \tau }
\mathcal{G}
e^{-T \Delta \tau} e^{-\frac{\mathcal{V}}{2} \Delta \tau }
= e^{-H \Delta \tau} + \mathcal{O}(\Delta \tau^2),
\label{propagatorN2LOVTV}
\end{aligned}$$ where $\mathcal{V}$ is the NN potential only with the first 6 operators in Eq.([\[AV6\'\]](#AV6'){reference-type="ref" reference="AV6'"}) plus the EM force in Eq.([\[VEMpp\]](#VEMpp){reference-type="ref" reference="VEMpp"}), $$\mathcal{V}  =  \sum_{i<j} \left[\sum_{p=1}^6 v_p(r_{ij}) O_{ij}^p + V^{EM}_{ij}(r_{ij}) \right]
\equiv \sum_{i<j} \mathcal{V}_{ij} .
\label{PER}$$

For $e^{-\frac{\mathcal{V}}{2}\Delta \tau }$, we pick an order of each $ij$ pair and calculate it using the following approximation, $$e^{-\frac{\mathcal{V}}{2} \Delta \tau }
= e^{\frac{-\mathcal{V}_{A-1 A} \Delta t}{2}}
e^{\frac{-\mathcal{V}_{A-2 A} \Delta t}{2}}
...
e^{\frac{-\mathcal{V}_{13}  \Delta t}{2}}
e^{\frac{-\mathcal{V}_{12} \Delta t}{2}}
+ \mathcal{O}(\Delta \tau)^2 ,
\label{propagatorv6half}$$ where the $\mathcal{O}(\Delta \tau)^2$ terms are due to $\mathcal{V}_{ij}$ do not commute with each other for different $ij$ pairs, and $e^{-\frac{\mathcal{V}^\dagger}{2} \Delta \tau}$ is the Hermitian conjugate of the $e^{-\frac{\mathcal{V}}{2}\Delta \tau }$ approximation which is the reverse order of Eq.([\[propagatorv6half\]](#propagatorv6half){reference-type="ref" reference="propagatorv6half"}). Note that the first 6 operators in $V^{NN}_{ij}$ in Eq.([\[AV6\'\]](#AV6'){reference-type="ref" reference="AV6'"}), $V^{NN}_{ij}$ commutes with the $V_{ij}^{EM}$, so we have, $$e^{ - \frac{\mathcal{V}_{ij }}{2}\Delta \tau}
=  e^{ - \frac{\sum_{p=1}^6 v_p(r_{ij}) O_{ij}^p }{2}\Delta \tau}
 e^{ - \frac{V^{EM}_{ij} }{2}\Delta \tau} .
 \label{propeV6eVem}$$

The first 6 operators in $V^{NN}_{ij}$ are the same AV6' operators and they form a group. $e^{ - \sum_{p=1}^6 v_p(r_{ij}) O_{ij}^p  \Delta \tau}$ in Eq.([\[propeV6eVem\]](#propeV6eVem){reference-type="ref" reference="propeV6eVem"}) can be linearized by the original 6 operators $O^p_{ij}$ in the following way, $$e^{ - \sum_{p=1}^6 v_p(r_{ij}) O_{ij}^p \Delta \tau }  =
 \sum_{p=1}^6 u^p_{ij} (r_{ij}) O^p_{ij} ,
\label{eVlinear}$$ where the six coefficients $u^p_{ij} (r_{ij})$ can be solved once $r_{ij}$ is given[^1].

The symbol $\mathcal{G}$ is the approximated short-time propagator for the spin-orbit term $e^{-V_{LS} \Delta \tau }$ to the linear order[^2], $$\mathcal{G} \equiv 1 -\sum_{i<j} v_{LS}(\hat{r}_{ij}) \Delta \tau
= e^{-V_{LS} \Delta \tau } + \mathcal{O}(\Delta \tau^2).
\label{defdownarrow}$$

The approximated short-time propagator $U(\Delta \tau)$ in our basis is calculated as,

::: flalign
& R' S' \| U() \| R S\
&= R' \| S' \| e\^- e\^-T e\^- \| R \| S\
&= S' \| e\^- { R' \| e\^-T \| R } e\^- \| S\
&= S' \| e\^- e\^- \| S G\^f\_R'R. []{#propagatorN2LORS label="propagatorN2LORS"}
:::

The symbol $G^f_{R'R}$ in Eq.([\[propagatorN2LORS\]](#propagatorN2LORS){reference-type="ref" reference="propagatorN2LORS"}) means the products of the free particle propagator of each particle in the system, $$G^f_{R'R}  \equiv
\langle R' | e^{-T \Delta \tau}  | R \rangle
= \prod_{i=1}^{A}  \langle \bm{r}'_i | e^{-\frac{p_i^2 \Delta \tau}{2m}    } | \bm{r}_i \rangle
\equiv  \left( \frac{m}{2\pi \Delta \tau \hbar^2} \right)^{\frac{3A}{2}}  e^{  -\frac{ (R'-R)^2 }{2 \Delta \tau \frac{\hbar^2}{m}}  } ,
\label{propagatorFree}$$ and $(R'-R)^2$ is calculated as,

$$\begin{aligned}
\!\!\!\!\! (R'\!-\!R)^2 \!  = \!
\sum_{i=1}^A  (\bm{r}_i'-\bm{r}_i)^2
=\sum_{i=1}^A \left[ (x'_i\!-\!x_i)^2 \!+\! (y'_i\!-\!y_i)^2 \!+\! (z'_i\!-\!z_i)^2 \right] . \label{Rdiffdef}
\end{aligned}$$

The symbol $\bm{\mathcal{G}}$ in Eq.([\[propagatorN2LORS\]](#propagatorN2LORS){reference-type="ref" reference="propagatorN2LORS"}) is the effective $\mathcal{G}$ which is written as, $$\bm{\mathcal{G}} =
1 - \left(\frac{-m}{4i  \hbar^2 } \right)\sum_{i<j} v_7(r'_{ij}) \left[ \bm{r}'_{ij} \times \frac{\Delta \bm{r}^{R',R}_{ij}}{\Delta \tau}
\cdot (\bm{\sigma}_i+\bm{\sigma}_j) \right] \Delta \tau  ,
\label{defdownarroweff}$$ where $r'_{ij}$ is the distance between particle $i$ and $j$ in configuration $R'$, $\bm{r}'_{ij}\equiv \bm{r}_i-\bm{r}_j$ in $R'$, and $\Delta \bm{r}^{R',R}_{ij} \equiv \Delta \bm{r}^{R',R}_i-\Delta \bm{r}^{R',R}_j$ where $\Delta \bm{r}^{R',R}_i \equiv \bm{r}^{R'}_i - \bm{r}^R_i$ and $\Delta \bm{r}^{R',R}_j \equiv \bm{r}^{R'}_j - \bm{r}^R_j$, and the symbol $\bm{r}^{R'(R)}_{i(j)}$ simply means the $\bm{r}_{i(j)}$ in configuration $R'(R)$. Note that Eq.([\[defdownarroweff\]](#defdownarroweff){reference-type="ref" reference="defdownarroweff"}) does not explicitly contain $\Delta \tau$ anymore. However, as will be shown in chapter [\[compalgorithm\]](#compalgorithm){reference-type="ref" reference="compalgorithm"}, $\Delta \bm{r}^{R',R}_{ij}$ will essentially have the order of $\Delta \tau$ because $\bm{r}^{R'}_j$ will be effectively sampled around $\bm{r}^{R}_j$ from a gaussian function whose variance is the order of $\Delta \tau$.

[^1]: See Appendix [\[secAV6\'linear\]](#secAV6'linear){reference-type="ref" reference="secAV6'linear"} for details about linearizing the AV6' operators in the propagator. In order to save time, in the code all the $u^p(r)$ are tabulated for the relevant range of $r$ before performing the Monte Carlo simulations. And the interpolations of the table are done by Lagrange 4-point interpolation polynomials.

[^2]: The three body interaction $V_{3b}=\sum_{i<j<k}V_{ijk}$ may be added in the same way as the spin-orbit term in Eq.([\[propagatorN2LOVTV\]](#propagatorN2LOVTV){reference-type="ref" reference="propagatorN2LOVTV"}) to the linear order, such that $$\mathcal{G}\equiv 1 -\sum_{i<j} v_{LS}(\hat{r}_{ij}) \Delta \tau -\sum_{i<j<k}V_{ijk} \Delta \tau .$$ For light nuclei this linear approximation may be sufficient because the three-body force and the spin-orbit force usually have opposite sign and similar strength, so $\mathcal{G}$ is close to 1 and the fluctuation in the propagator will not be too big. Better approximations for the 3-body propagator are straightforward since they do not contain derivatives.

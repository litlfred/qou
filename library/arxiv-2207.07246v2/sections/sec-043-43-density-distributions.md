---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-043-43-density-distributions
section_title: "Density Distributions"
section_number: 4.3
pages: 105-110
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.923
latex_coverage_ratio: 0.985
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 73 sections: Front matter; ABSTRACT; ACKNOWLEDGEMENTS"
---
The ground state of $^4$He is an angular momentum $J=0$ state and is spherically symmetric. We can use the one-particle number density $\rho(r)$ to describe the probability density for one particle to be at distance $r$ from the nuclei's center of mass. With this convention we normalize it as $$\int 4 \pi r^2 \rho(r) dr = 1 .$$ The distribution $\rho(r)$ can be extracted from high energy electron-nucleus scattering experiments, and is related with the electric form factor by Fourier transform ([@Xuzizong2009book; @Lynn2019ann]). The label of a particle does not matter, so we can just take particle 1 as the reference particle, and the operator $\hat{\rho}(r)$ can be written as[^1],

::: flalign
\(r\) = ( r - \| \_1 - \_j=1\^A \_j \| ). []{#rhordef label="rhordef"}
:::

Note that due to the kinetic energy operator $T$ in the Hamiltonian $H$, $\hat{\rho}(r)$ does not commute with $H$. Therefore it cannot be calculated very accurately by diffusion based QMC method. But it can be calculated directly by PIMC. The ground state expectation value for the one-particle number density $\rho(r)$ is,

::: flalign
\(r\) &= Re \_0 \| \_0 \
&= Re \_T\| e\^-H \...e\^-H e\^-H \...e\^-H \| \_T . []{#rhor1 label="rhor1"}
:::

Eq.([\[rhor1\]](#rhor1){reference-type="ref" reference="rhor1"}) can be recast into the form of Eq.([\[OABP\]](#OABP){reference-type="ref" reference="OABP"}) in section [\[Recast\]](#Recast){reference-type="ref" reference="Recast"}. We put the operator $\hat{\rho}(r)$ at the middle bead M, the corresponding $g^V_{lr,M}(\mathcal{R})$ can be written as, $$\begin{aligned}
g^V_{lr,M}(\mathcal{R})  = \langle \psi^l_{M\!-\!1}  (\mathcal{R}) | \bm{\mathcal{G}} e^{\frac{- \mathcal{V}_M  \Delta \tau }{2}}
\delta \left( r - \big| \hat{\bm{r}}_1 - \frac{1}{A}\sum_{j=1}^A \hat{\bm{r}}_j   \big|   \right)
   e^{\frac{- \mathcal{V}^\dagger_M  \Delta \tau }{2}} \bm{\mathcal{G}}  | \psi^r_{M\!+\!1} (\mathcal{R}) \rangle,
\label{gVRlrrhodef}
\end{aligned}$$ while the other functions remain the same as in section [\[Recast\]](#Recast){reference-type="ref" reference="Recast"}.

The $\delta$ function in $\rho(r)$ cannot be directly sampled. However it can be integrated. We can expand in a histogram basis and the width of each bin is $h$, and $r$ can be represented by $r_k$ when $r\in [kh,kh+h)$ and $k$ is an integer. The basis of the histogram can be represented by $b_k$ which is 1 when $r\in [kh,kh+h)$ and 0 otherwise. $\rho(r_k)$ can be represented by a number $a_k$ such that, $$\begin{aligned}
a_k=\frac{\int \rho(r) b_k d\bm{r}}
{\frac{4}{3} \pi h^3 [(k+1)^3-k^3  ] }.
\label{rhobkintgrel}
\end{aligned}$$ Considering Eq.([\[rhor1\]](#rhor1){reference-type="ref" reference="rhor1"}) and Eq.([\[OABP\]](#OABP){reference-type="ref" reference="OABP"}) in section [\[Recast\]](#Recast){reference-type="ref" reference="Recast"}, $a_k$ can be written as, $$\begin{aligned}
a_k =\frac{\sum_l\sum_r \int d \mathcal{R}
\left\{\frac{3\int A_{lr}  (\mathcal{R})  b_k d\bm{r}}{4 \pi h^3 [(k+1)^3-k^3  ] } \right\}
P_{lr} (\mathcal{R}) }{ \sum_l\sum_r \int d \mathcal{R} B_{lr} (\mathcal{R}) P_{lr} (\mathcal{R})  }
\label{akABP},
\end{aligned}$$ so we just need to sample $\frac{3\int A_{lr}  (\mathcal{R})  b_k d\bm{r}}{4 \pi h^3 [(k+1)^3-k^3  ] }$ to get $a_k$. Note that $A_{lr} (\mathcal{R}) = \frac{Re[ g^V_{lr,M}(\mathcal{R})]}{|Re[ f^V_{lr}(\mathcal{R})]|  }$, and Eq.([\[gVRlrrhodef\]](#gVRlrrhodef){reference-type="ref" reference="gVRlrrhodef"}) of $g^V_{lr,M}(\mathcal{R})$ contain the $\delta$ function, so the integral $\int A_{lr}  (\mathcal{R})  b_k d\bm{r}$ becomes,

::: flalign
& A\_lr () b_k d\
&= \|Re\[ f()\_lr\]\| \
&=

&&
:::

Note that $\frac{Re[ f(\mathcal{R})_{lr}]}{|Re[ f(\mathcal{R})_{lr}]|  }$ is either 1 or -1, so $\frac{3\int A_{lr}  (\mathcal{R})  b_k d\bm{r}}{4 \pi h^3 [(k+1)^3-k^3  ] }$ just becomes either $\frac{3}{4 \pi h^3 [(k+1)^3-k^3  ] }$, $\frac{-3}{4 \pi h^3 [(k+1)^3-k^3  ] }$ or 0.

<figure id="rho">
<embed src="Figures/rho.eps" />
<figcaption>The ground state one-particle number density distributions of <span class="math inline"><sup>4</sup></span>He based on the AV6’ interaction.</figcaption>
</figure>

<figure id="rhoN2LO">
<embed src="Figures/rhoN2LO.eps" />
<figcaption>The ground state one-particle number density distributions of <span class="math inline"><sup>4</sup></span>He based on the local chiral N<span class="math inline"><sup>2</sup></span>LO interaction.</figcaption>
</figure>

The sampling of $a_k$ histogram value is then straightforward. We define a one-dimensional array $A(n)$ and initialize it to zero. We sample according to $P_{lr} (\mathcal{R})$ as described in chapter [\[compalgorithm\]](#compalgorithm){reference-type="ref" reference="compalgorithm"}, and each time when we take a sample, we look at the configuration of the middle bead $M$. At bead $M$, there always exists an integer $k$ such that $r_k=| {\bm{r}}_1 - \frac{1}{A}\sum_{j=1}^A {\bm{r}}_j|$. At the same time, the $k$th element in $A(k)$ takes a sample of $\frac{3 {Re[ f(\mathcal{R})_{lr}]}/{|Re[ f(\mathcal{R})_{lr}]|  } }{4 \pi h^3 [(k+1)^3-k^3  ] }$, so $A(k)=A(k)+\frac{3 {Re[ f(\mathcal{R})_{lr}]}/{|Re[ f(\mathcal{R})_{lr}]|  } }{4 \pi h^3 [(k+1)^3-k^3  ] }$. For any other element $j$ in array $A(n)$, they each take a sample of 0 and so $A(j)$ remain the same. We continue sampling according to $P_{lr} (\mathcal{R})$ and continue. Once we have enough $N$ samples, then each of the $a_k$ can be evaluated by $a_k=A(k)/N$ with corresponding error bar. As shown in Fig. [1](#rho){reference-type="ref" reference="rho"}, $\rho(r_k)$ are given by these values. We can see from Fig. [1](#rho){reference-type="ref" reference="rho"} for AV6' interaction and Fig. [2](#rhoN2LO){reference-type="ref" reference="rhoN2LO"} for the local chiral N$^2$LO interaction that for different total imaginary time, the particle number density distribution of $^4$He are almost identical. These are further evidence that we have reached the ground state.

From Eq.([\[rhoravedef\]](#rhoravedef){reference-type="ref" reference="rhoravedef"}) and Eq.([\[rhordef\]](#rhordef){reference-type="ref" reference="rhordef"}), we can further define the single-proton number density $\hat{\rho}_p$ and the single-neutron number density $\hat{\rho}_n$ as $$\begin{aligned}
\!\!\! \hat{\rho}_{p(n)}(r) \!=\! \delta \! \left( r - \left| \hat{\bm{r}}_1 - \frac{1}{A}\sum_{j=1}^A \hat{\bm{r}}_j  \right|   \right) \! P^1_{p(n)}
\!=\! \frac{1}{A} \sum_{i=1}^{A} \delta \! \left( r - \left| \hat{\bm{r}}_i - \frac{1}{A}\sum_{j=1}^A \hat{\bm{r}}_j  \right|   \right) \! P^i_{p(n)}.
\end{aligned}$$ where $P^i_{p}=\frac{1+\tau_{1z}}{2}$ and $P^i_{n}=\frac{1-\tau_{1z}}{2}$ are the proton and neutron projection operator for nucleon with label $i$. Since $P^i_{p}+P^i_{n}=1$, we have $$\begin{aligned}
 \hat{\rho}(r) = \hat{\rho}_{p}(r) + \hat{\rho}_{n}(r) .
\end{aligned}$$ The sampling method of $\hat{\rho}_{p}(r)$ and $\hat{\rho}_{n}(r)$ is similar with that of $\hat{\rho}(r)$. In Fig. [1](#rho){reference-type="ref" reference="rho"} and Fig. [2](#rhoN2LO){reference-type="ref" reference="rhoN2LO"}, ${\rho}_{p}(r)$ and ${\rho}_{n}(r)$ are also presented. As expected from the rms radii results, in $^4$He the two protons and the two neutrons are distributed evenly, and ${\rho}_{p}(r)$ and ${\rho}_{n}(r)$ are almost identical.

<figure id="rho234AVN2LO">
<embed src="Figures/rho234AVN2LO.eps" style="width:95.03%" />
<figcaption>The ground state one-particle number density distributions of <span class="math inline"><em>A</em> ≤ 4</span> light nuclei based on the AV6’ interaction and the local chiral N<span class="math inline"><sup>2</sup></span>LO interaction. The lines are a guide to the eye.</figcaption>
</figure>

In Fig. [3](#rho234AVN2LO){reference-type="ref" reference="rho234AVN2LO"} all the density distributions for $A \leq 4$ light nuclei are presented. For $^2$H the ${\rho}_{p}(r)$ and ${\rho}_{n}(r)$ are identical, and as $r$ decreases, the density distributions based on the AV6' interaction decrease rapidly which are different from those based on the local chiral N$^2$LO interaction. This is because, as shown in Fig. [\[AV6N2LOradial\]](#AV6N2LOradial){reference-type="ref" reference="AV6N2LOradial"}, for the two-nucleon system the central part becomes the dominant part as $r$ decreases, and the AV6' interaction has a much more repulsive central radial function than the chiral one, this makes the proton and the neutron highly unlikely to be very close to each other and the center of mass, which means density distributions will rapidly decrease as $r$ decreases. For $^3$H there is one proton and two neutrons, and at a given $r$, it is reasonable that the probability of finding a neutron ${\rho}_{n}(r)$ is always higher than that of finding a proton ${\rho}_{p}(r)$. $^3$H and its mirror nuclei $^3$He shows nearly the same ${\rho}(r)$ distribution, however their ${\rho}_{p}(r)$ and ${\rho}_{n}(r)$ distributions are as if they are exchanged, i.e., $^3$H's ${\rho}_{p}(r)$ is like the $^3$He's ${\rho}_{n}(r)$ and $^3$H's ${\rho}_{n}(r)$ is like $^3$He's ${\rho}_{p}(r)$.

[^1]: In the code, we actually calculate the averaged $\hat{\rho}(r)$ operator ([@Lynn2019ann]), $$\hat{\rho}(r) = \frac{1}{A} \sum_{i=1}^{A} \delta \left( r - \left| \hat{\bm{r}}_i - \frac{1}{A}\sum_{j=1}^A \hat{\bm{r}}_j  \right|  \right).
    \label{rhoravedef}$$ We use Eq.([\[rhordef\]](#rhordef){reference-type="ref" reference="rhordef"}) for illustration purpose.

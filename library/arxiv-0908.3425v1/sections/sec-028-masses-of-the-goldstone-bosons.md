---
doc_id: arxiv-0908.3425v1
doc_title: "Chiral Perturbation Theory: Introduction and Recent Results in the One-Nucleon Sector"
section_id: sec-028-masses-of-the-goldstone-bosons
section_title: "Masses of the Goldstone bosons"
section_number: null
pages: 42-46
source_pdf: 0908.3425v1.pdf
source_sha256: 5e88d45bbc1c1b9b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.923
latex_coverage_ratio: 0.996
doc_brief: "Chiral Perturbation Theory: Introduction and Recent Results in the One-Nucleon Sector — We provide an introduction to the basic concepts of chiral perturbation theory and discuss some recent"
---
[]{#sec_aop4 label="sec_aop4"} A discussion of the masses at ${\cal O}(q^4)$ is one of the simplest applications of chiral perturbation theory beyond the tree level. For that purpose let us consider ${\cal L}_2 + {\cal L}_4$ for QCD with finite quark masses but in the absence of external fields. We restrict ourselves to the limit of isospin symmetry, i.e., $m_u=m_d=\hat m$. In order to determine the masses we calculate the self energies $\Sigma(p^2)$ of the Goldstone bosons.

Let $$\label{3:3:3:propF}
\Delta_{\phi F}(p)=\frac{1}{p^2-M^2_{\phi,2}+i0^+},\quad \phi=\pi,K,\eta,$$ denote the Feynman propagator containing the lowest-order masses, $$M^2_{\pi,2}=2 B_0 \hat m,\quad
M^2_{K,2}=B_0(\hat m+m_s),\quad
M^2_{\eta,2}=\frac{2}{3} B_0\left(\hat m+2m_s\right).$$ (The subscript 2 refers to chiral order 2.) The proper self-energy insertions, $-i\Sigma_\phi(p^2)$, consist of one-particle-irreducible diagrams only, i.e., diagrams which do not fall apart into two separate pieces when cutting an arbitrary internal line. At chiral order $D=4$, the contributions to $-i\Sigma_{\phi,4}(p^2)$ are those shown in Fig. [1](#3:3:3:selfenergy){reference-type="ref" reference="3:3:3:selfenergy"}.

<figure id="3:3:3:selfenergy">
<div class="center">

</div>
<figcaption><span id="3:3:3:selfenergy" label="3:3:3:selfenergy"></span> Self-energy diagrams at <span class="math inline">${\cal O}(q^4)$</span>. Vertices derived from <span class="math inline">${\cal L}_{2n}$</span> are denoted by <span class="math inline">2<em>n</em></span> in the interaction blobs.</figcaption>
</figure>

In general, the full (unrenormalized) propagator may be summed using a geometric series (see Fig. [2](#3:3:3:fullprop){reference-type="ref" reference="3:3:3:fullprop"}):

<figure id="3:3:3:fullprop">
<div class="center">

</div>
<figcaption><span id="3:3:3:fullprop" label="3:3:3:fullprop"></span> Unrenormalized propagator as the sum of irreducible self-energy diagrams. Hatched and cross-hatched “vertices” denote one-particle-reducible and one-particle-irreducible contributions, respectively.</figcaption>
</figure>

$$\begin{aligned}
\label{3:3:3:prop1}
i\Delta_\phi(p)&=&\frac{i}{p^2-M^2_{\phi,2}+i0^+}+\frac{i}{p^2-M^2_{\phi,2}+i0^+}
[-i\Sigma_\phi(p^2)]\frac{i}{p^2-M^2_{\phi,2}+i0^+}+\cdots\nonumber\\
&=&
\frac{i}{p^2-M^2_{\phi,2}-\Sigma_\phi(p^2)+i0^+}.
\end{aligned}$$ The physical mass, including the interaction, is defined as the pole of Eq. ([\[3:3:3:prop1\]](#3:3:3:prop1){reference-type="ref" reference="3:3:3:prop1"}), $$\label{3:3:3:mdef}
M^2_\phi-M^2_{\phi,2}-\Sigma_\phi(M^2_\phi)\stackrel{!}{=}0,$$ where the precision of the determination of $M^2_\phi$ depends on the precision of the calculation of $\Sigma_\phi$.

For our particular application with exactly two external meson lines, the relevant interaction Lagrangians can be written as $${\cal L}_{\rm int}={\cal L}_2^{4\phi}+{\cal L}_4^{2\phi},$$ where $$\begin{aligned}
\label{3:3:3:l24phi} {\cal L}^{4\phi}_2&=&\frac{1}{24
F^2_0}\left\{\mbox{Tr}( [\phi,\partial_\mu \phi]\phi \partial^\mu
\phi) +B_0\mbox{Tr}({\cal M}\phi^4)\right\},\\
\label{3:3:3:l42phi}
{\cal L}_4^{2\phi}&=&
-\frac{1}{2}\left(a_\pi\pi^0\pi^0+b_\pi \partial_\mu\pi^0\partial^\mu\pi^0\right)
-a_\pi\pi^+\pi^--b_\pi\partial_\mu\pi^+\partial^\mu\pi^-\nonumber\\
&&-a_KK^+K^- - b_K\partial_\mu K^+\partial^\mu K^-
-a_KK^0\bar{K}^0 -b_K\partial_\mu K^0\partial^\mu\bar{K}^0\nonumber\\
&&-\frac{1}{2}\left(a_\eta\eta^2+b_\eta\partial_\mu\eta\partial^\mu\eta\right).
\end{aligned}$$ The constants $a_\phi$ and $b_\phi$ are given by $$\begin{aligned}
\label{3:3:3:ab}
a_\pi&=&\frac{64 B^2_0}{F^2_0}\left[(2\hat m+m_s)\hat mL_6+\hat m^2L_8\right],\nonumber\\
b_\pi&=&-\frac{16 B_0}{F^2_0}\left[(2\hat m+m_s)L_4+\hat mL_5\right],\nonumber\\
a_K&=&\frac{32B^2_0}{F^2_0}\left[(2\hat m+m_s)(\hat m+m_s)L_6+\frac{1}{2}(\hat m+m_s)^2L_8
\right],
\nonumber\\
b_K&=&-\frac{16 B_0}{F^2_0}\left[(2\hat m+m_s)L_4+\frac{1}{2}(\hat m+m_s)L_5\right]\nonumber\\
a_\eta&=&\frac{64 B^2_0}{3F^2_0}\left[(2\hat m+m_s)(\hat m+2m_s)L_6+2(\hat m-m_s)^2L_7
+(\hat m^2+2m_s^2)L_8\right],\nonumber\\
b_\eta&=&-\frac{16B_0}{F^2_0}\left[(2\hat m+m_s)L_4+\frac{1}{3}(\hat m+2m_s)L_5\right].
\end{aligned}$$ At ${\cal O}(q^4)$ the self energies are of the form $$\label{3:3:3:sigmaphi}
\Sigma_{\phi,4}(p^2)=A_\phi+B_\phi p^2,$$ where the constants $A_\phi$ and $B_\phi$ receive a tree-level contribution from ${\cal L}_4$ and a one-loop contribution with a vertex from ${\cal L}_2$ (see Fig. [1](#3:3:3:selfenergy){reference-type="ref" reference="3:3:3:selfenergy"}). For the tree-level contribution of ${\cal L}_4$ this is easily seen, because the Lagrangians of Eq. ([\[3:3:3:l42phi\]](#3:3:3:l42phi){reference-type="ref" reference="3:3:3:l42phi"}) contain either exactly two derivatives of the fields or no derivatives at all. For example, the contact contribution for the $\eta$ reads $$-i\Sigma_{\eta,4}^{\rm tree}(p^2)=-i(a_\eta + b_\eta p^2).$$

For the one-loop contribution the argument is as follows. The Lagrangian ${\cal L}_2^{4\phi}$ contains either two derivatives or no derivatives at all which, symbolically, can be written as $\phi\phi\partial\phi\partial\phi$ and $\phi^4$, respectively. The first term results in $M^2$ or $p^2$, depending on whether the $\phi$ or the $\partial \phi$ are contracted with the external fields. The "mixed" situation vanishes upon integration. The second term, $\phi^4$, does not generate a momentum dependence.

As a specific example, we evaluate the pion-loop contribution to the $\pi^0$ self energy (see Fig. [3](#4:9:pi0seloop){reference-type="ref" reference="4:9:pi0seloop"}) by applying the Feynman rule of Eq. ([\[3:2:4:mpipi\]](#3:2:4:mpipi){reference-type="ref" reference="3:2:4:mpipi"}) for $a=c=3$, $p_a=p_c=p$, $b=d=j$, and $p_b=p_d=k$:

<figure id="4:9:pi0seloop">
<div class="center">

</div>
<figcaption><span id="4:9:pi0seloop" label="4:9:pi0seloop"></span> Contribution of the pion loops to the <span class="math inline"><em>π</em><sup>0</sup></span> self energy.</figcaption>
</figure>

$$\label{3:3:3:diag}
\frac{1}{2}\int \frac{\mbox{d}^4k}{(2\pi)^4}\frac{i}{3F_0^2}
[-4p^2-4k^2+5 M^2_{\pi,2}]
\frac{i}{k^2-M_{\pi,2}^2+i0^+},$$ where $1/2$ is a symmetry factor. Since the integral diverges, we consider its extension to $n$ dimensions. In addition to the loop-integral of Eq. ([\[3:2:4:IMmun\]](#3:2:4:IMmun){reference-type="ref" reference="3:2:4:IMmun"}), we need $$\mu^{4-n}i\int \frac{\mbox{d}^n k}{(2\pi)^n}\frac{k^2}{k^2-M^2+i0^+}=
\mu^{4-n}i\int \frac{\mbox{d}^n k}{(2\pi)^n}\frac{k^2-M^2+M^2}{k^2-M^2+i0^+},$$ where we have added $0=-M^2+M^2$ in the numerator. We make use of $$\mu^{4-n}i\int \frac{\mbox{d}^n k}{(2\pi)^n}=0$$ in dimensional regularization which is "shown" as follows. Consider the (more general) integral $$\label{3:3:3:dnkk2p}
\int \mbox{d}^n k (k^2)^p,$$ substitute $k=\lambda k'\ (\lambda > 0)$, and relabel $k'=k$ $$=\lambda^{n+2p}\int \mbox{d}^n k (k^2)^p.$$ Since $\lambda>0$ is arbitrary and, for fixed $p$, the result is to hold for arbitrary $n$, Eq. ([\[3:3:3:dnkk2p\]](#3:3:3:dnkk2p){reference-type="ref" reference="3:3:3:dnkk2p"}) is set to zero in dimensional regularization. We emphasize that the vanishing of Eq. ([\[3:3:3:dnkk2p\]](#3:3:3:dnkk2p){reference-type="ref" reference="3:3:3:dnkk2p"}) has the character of a prescription. The integral does not depend on any scale and its analytic continuation is ill defined in the sense that there is no dimension $n$ where it is meaningful. It is ultraviolet divergent for $n+2p\geq 0$ and infrared divergent for $n+2p\leq 0$.

We then obtain $$\mu^{4-n}i\int \frac{\mbox{d}^n k}{(2\pi)^n}\frac{k^2}{k^2-M^2+i0^+}=
M^2 I(M^2,\mu^2,n),$$ with $I(M^2,\mu^2,n)$ of Eq. ([\[3:2:4:IMmun\]](#3:2:4:IMmun){reference-type="ref" reference="3:2:4:IMmun"}). The pion-loop contribution to the $\pi^0$ self energy is thus $$\frac{i}{6 F^2_0}(-4p^2+M^2_{\pi,2})I(M^2_{\pi,2},\mu^2,n),$$ which is indeed of the type discussed in Eq. ([\[3:3:3:sigmaphi\]](#3:3:3:sigmaphi){reference-type="ref" reference="3:3:3:sigmaphi"}) and diverges as $n\to 4$.

After analyzing all loop contributions and combining them with the tree-level contributions of Eqs. ([\[3:3:3:ab\]](#3:3:3:ab){reference-type="ref" reference="3:3:3:ab"}), the constants $A_\phi$ and $B_\phi$ of Eq. ([\[3:3:3:sigmaphi\]](#3:3:3:sigmaphi){reference-type="ref" reference="3:3:3:sigmaphi"}) are given by $$\begin{aligned}
\label{3:3:3:AB}
A_\pi&=&\frac{M^2_{\pi,2}}{F^2_0}\Bigg\{
\underbrace{-\frac{1}{6}I(M^2_{\pi,2})
-\frac{1}{6}I(M^2_{\eta,2})-\frac{1}{3}I(M^2_{K,2})}_{\mbox{loop contribution}}
\underbrace{+32[(2\hat m+m_s)B_0L_6+\hat mB_0L_8]}_{\mbox{tree-level contribution}}
\Bigg\},\nonumber\\
B_\pi&=&\frac{2}{3}\frac{I(M^2_{\pi,2})}{F^2_0}+\frac{1}{3}
\frac{I(M^2_{K,2})}{F^2_0}-\frac{16B_0}{F^2_0}\left[
(2\hat m+m_s)L_4+\hat m L_5\right],\nonumber\\
A_K&=&\frac{M^2_{K,2}}{F^2_0}\Bigg\{\frac{1}{12}I(M^2_{\eta,2})
-\frac{1}{4}I(M^2_{\pi,2})-\frac{1}{2}I(M^2_{K,2})+32\left[(2\hat m+m_s)B_0L_6+\frac{1}{2}(\hat m+m_s)
B_0L_8\right]\Bigg\},\nonumber\\
B_K&=&\frac{1}{4}\frac{I(M^2_{\eta,2})}{F^2_0}
+\frac{1}{4}\frac{I(M^2_{\pi,2})}{F^2_0}
+\frac{1}{2}\frac{I(M^2_{K,2})}{F^2_0}-16 \frac{B_0}{F^2_0}\left[(2\hat m+m_s)L_4+\frac{1}{2}(\hat m
+m_s)L_5\right],
\nonumber\\
A_\eta&=&\frac{M^2_{\eta,2}}{F^2_0}\left[-\frac{2}{3}I(M^2_{\eta,2})\right]
+\frac{M^2_{\pi,2}}{F^2_0}\left[\frac{1}{6}I(M^2_{\eta,2})
-\frac{1}{2}I(M^2_{\pi,2})
+\frac{1}{3}I(M^2_{K,2})\right]\nonumber\\
&&+\frac{M^2_{\eta,2}}{F^2_0}[16M^2_{\eta,2} L_8+32(2\hat m+m_s)
B_0L_6]+\frac{128}{9}\frac{B^2_0(\hat m-m_s)^2}{F^2_0}(3L_7+L_8),\nonumber\\
B_\eta&=&\frac{I(M^2_{K,2})}{F^2_0}-\frac{16}{F^2_0}(2\hat m+m_s)B_0L_4
-8\frac{M^2_{\eta,2}}{F^2_0}L_5,
\end{aligned}$$ where, for simplicity, we have suppressed the dependence on the scale $\mu$ and the number of dimensions $n$ in the integrals $I(M^2,\mu^2,n)$ \[see Eq. ([\[3:2:4:IMmun\]](#3:2:4:IMmun){reference-type="ref" reference="3:2:4:IMmun"})\]. Both the integrals $I$ and the bare coefficients $L_i$ (with the exception of $L_7$) have $1/(n-4)$ poles and finite pieces. In particular, the coefficients $A_\phi$ and $B_\phi$ are *not* finite as $n\to 4$ showing that they do not correspond to observables.

The masses at ${\cal O}(q^4)$ are determined by solving Eq. ([\[3:3:3:mdef\]](#3:3:3:mdef){reference-type="ref" reference="3:3:3:mdef"}) with the predictions of Eq. ([\[3:3:3:sigmaphi\]](#3:3:3:sigmaphi){reference-type="ref" reference="3:3:3:sigmaphi"}) for the self energies, $$M^2_\phi=M_{\phi,2}^2+A_\phi+B_\phi M^2_\phi,$$ from which we obtain $$M^2_\phi=\frac{M_{\phi,2}^2+A_\phi}{1-B_\phi}=M_{\phi,2}^2(1+B_\phi)+A_\phi+
{\cal O}(q^6),$$ because $A_\phi={\cal O}(q^4)$ and $\{B_\phi, M_{\phi,2}^2\}={\cal O}(q^2)$. Expressing the bare coefficients $L_i$ in Eq. ([\[3:3:3:AB\]](#3:3:3:AB){reference-type="ref" reference="3:3:3:AB"}) in terms of the renormalized coefficients by using Eq. ([\[3:3:1:lihi\]](#3:3:1:lihi){reference-type="ref" reference="3:3:1:lihi"}), the results for the masses of the Goldstone bosons at ${\cal O}(q^4)$ read [@Gasser:1984gg] $$\begin{aligned}
\label{3:3:3:mpi24}
M^2_{\pi,4}&=&M^2_{\pi,2}\Bigg\{1+\frac{M^2_{\pi,2}}{32\pi^2F^2_0}
\ln\left(\frac{M^2_{\pi,2}}{\mu^2}\right)-\frac{M^2_{\eta,2}}{96\pi^2F^2_0}
\ln\left(\frac{M^2_{\eta,2}}{\mu^2}\right)\nonumber\\
&&+\frac{16}{F^2_0}\left[(2\hat m+m_s)B_0(2L^r_6-L^r_4)
+\hat mB_0(2L^r_8-L^r_5)\right]\Bigg\},\\
\label{3:3:3:mk24}
M^2_{K,4}&=&M^2_{K,2}\Bigg\{1+\frac{M^2_{\eta,2}}{48\pi^2F^2_0}
\ln\left(\frac{M^2_{\eta,2}}{\mu^2}\right)\nonumber\\
&&+\frac{16}{F^2_0}\left[(2\hat m+m_s)B_0(2L^r_6-L^r_4)
+\frac{1}{2}(\hat m+m_s)B_0(2L^r_8-L^r_5)\right]\Bigg\},\nonumber\\
&&\\
\label{3:3:3:meta24}
M^2_{\eta,4}&=&M^2_{\eta,2}\left[1+\frac{M^2_{K,2}}{16\pi^2F^2_0}
\ln\left(\frac{M^2_{K,2}}{\mu^2}\right)
-\frac{M^2_{\eta,2}}{24\pi^2F^2_0}\ln\left(\frac{M^2_{\eta,2}}{\mu^2}\right)
\right.\nonumber\\
&&\left.+\frac{16}{F^2_0}(2\hat m+m_s)B_0(2L^r_6-L^r_4)
+8\frac{M^2_{\eta,2}}{F^2_0}(2L^r_8-L^r_5)\right]\nonumber\\
&&+M^2_{\pi,2}\left[\frac{M^2_{\eta,2}}{96\pi^2F^2_0}
\ln\left(\frac{M^2_{\eta,2}}{\mu^2}\right)
-\frac{M^2_{\pi,2}}{32\pi^2F^2_0}
\ln\left(\frac{M^2_{\pi,2}}{\mu^2}\right)
+\frac{M^2_{K,2}}{48\pi^2F^2_0}
\ln\left(\frac{M^2_{K,2}}{\mu^2}\right)\right]\nonumber\\
&&+\frac{128}{9}\frac{B^2_0(\hat m-m_s)^2}{F^2_0}
(3L^r_7+L^r_8).
\end{aligned}$$ First of all, we note that the expressions for the masses are finite. The infinite parts of the coefficients $L_i$ of the Lagrangian of Gasser and Leutwyler exactly cancel the divergent terms resulting from the integrals. This is the reason why the bare coefficients $L_i$ must be infinite. Furthermore, at ${\cal O}(q^4)$ the masses of the Goldstone bosons vanish, if the quark masses are sent to zero. This is, of course, what we had expected from QCD in the chiral limit but it is comforting to see that the self interaction in ${\cal L}_2$ (in the absence of quark masses) does not generate Goldstone boson masses at higher order. At ${\cal O}(q^4)$, the squared Goldstone boson masses contain terms which are analytic in the quark masses, namely, of the form $m^2_q$ multiplied by the renormalized low-energy coupling constants $L_i^r$. However, there are also non-analytic terms of the type $m^2_q \ln(m_q)$---so-called chiral logarithms---which do not involve new parameters. Such a behavior is an illustration of the mechanism found by Li and Pagels [@Li:1971vr], who noticed that a perturbation theory around a symmetry which is realized in the Nambu-Goldstone mode results in both analytic as well as non-analytic expressions in the perturbation. Finally, the scale dependence of the renormalized coefficients $L_i^r$ of Eq. ([\[3:3:1:lihi\]](#3:3:1:lihi){reference-type="ref" reference="3:3:1:lihi"}) is by construction such that it cancels the scale dependence of the chiral logarithms. Thus, physical observables do not depend on the scale $\mu$. It is straightforward to verify this statement by differentiating Eqs. ([\[3:3:3:mpi24\]](#3:3:3:mpi24){reference-type="ref" reference="3:3:3:mpi24"}) - ([\[3:3:3:meta24\]](#3:3:3:meta24){reference-type="ref" reference="3:3:3:meta24"}) with respect to $\mu$ and by making use of $$\frac{\mbox{d} L_i^r(\mu)}{\mbox{d}\mu}=-\frac{\Gamma_i}{16\pi^2\mu},$$ where the $\Gamma_i$ are given in Table [\[4:8:tableli\]](#4:8:tableli){reference-type="ref" reference="4:8:tableli"}.

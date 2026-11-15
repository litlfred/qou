---
doc_id: arxiv-0908.3425v1
doc_title: "Chiral Perturbation Theory: Introduction and Recent Results in the One-Nucleon Sector"
section_id: sec-026-the-oq4-lagrangian-of-gasser-and-leutwyler
section_title: "The O(q4) Lagrangian of Gasser and Leutwyler"
section_number: null
pages: 38-39
source_pdf: 0908.3425v1.pdf
source_sha256: 5e88d45bbc1c1b9b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.959
latex_coverage_ratio: 0.994
doc_brief: "Chiral Perturbation Theory: Introduction and Recent Results in the One-Nucleon Sector — We provide an introduction to the basic concepts of chiral perturbation theory and discuss some recent"
---
[]{#subsubsec_clop4 label="subsubsec_clop4"} The most general $\mbox{SU(3)}_L\times\mbox{SU(3)}_R$-invariant Lagrangian at ${\cal O}(q^4)$ is given by [@Gasser:1984gg] $$\begin{aligned}
\label{3:3:1:l4gl}
\lefteqn{{\cal L}_4=
L_1 \left\{\mbox{Tr}[D_{\mu}U (D^{\mu}U)^{\dagger}] \right\}^2
+ L_2 \mbox{Tr} \left [D_{\mu}U (D_{\nu}U)^{\dagger}\right]
\mbox{Tr} \left [D^{\mu}U (D^{\nu}U)^{\dagger}\right]}\nonumber\\
& & + L_3 \mbox{Tr}\left[
D_{\mu}U (D^{\mu}U)^{\dagger}D_{\nu}U (D^{\nu}U)^{\dagger}
\right ]
+ L_4 \mbox{Tr} \left [ D_{\mu}U (D^{\mu}U)^{\dagger} \right ]
\mbox{Tr} \left( \chi U^{\dagger}+ U \chi^{\dagger} \right )
\nonumber \\
& & +L_5 \mbox{Tr} \left[ D_{\mu}U (D^{\mu}U)^{\dagger}
(\chi U^{\dagger}+ U \chi^{\dagger})\right]
+ L_6 \left[ \mbox{Tr} \left ( \chi U^{\dagger}+ U \chi^{\dagger} \right )
\right]^2
\nonumber \\
& & + L_7 \left[ \mbox{Tr} \left ( \chi U^{\dagger} - U \chi^{\dagger} \right )
\right]^2
+ L_8 \mbox{Tr} \left ( U \chi^{\dagger} U \chi^{\dagger}
+ \chi U^{\dagger} \chi U^{\dagger} \right )
\nonumber \\
& & -i L_9 \mbox{Tr} \left [ f^R_{\mu\nu} D^{\mu} U (D^{\nu} U)^{\dagger}
+ f^L_{\mu\nu} (D^{\mu} U)^{\dagger} D^{\nu} U \right ]
+ L_{10} \mbox{Tr} \left ( U f^L_{\mu\nu} U^{\dagger} f_R^{\mu\nu} \right )
\nonumber \\
& & + H_1 \mbox{Tr} \left ( f^R_{\mu\nu} f^{\mu\nu}_R +
f^L_{\mu\nu} f^{\mu\nu}_L \right )
+ H_2 \mbox{Tr} \left ( \chi \chi^{\dagger} \right ).
\end{aligned}$$ The numerical values of the low-energy coupling constants $L_i$ are not determined by chiral symmetry. In analogy to $F_0$ and $B_0$ of ${\cal L}_2$ they are parameters containing information on the underlying dynamics and should, in principle, be calculable in terms of the (remaining) parameters of QCD, namely, the heavy-quark masses and the QCD scale $\Lambda_{\rm QCD}$. In practice, they parameterize our inability to solve the dynamics of QCD in the non-perturbative regime. So far they have either been fixed using empirical input or theoretically using QCD-inspired models, meson-resonance saturation [@Ecker:1988te] [@Pich:2008xj], and lattice QCD (see Ref. [@Necco:2009cq] for a recent overview).

By construction Eq. ([\[3:3:1:l4gl\]](#3:3:1:l4gl){reference-type="ref" reference="3:3:1:l4gl"}) represents the most general Lagrangian at ${\cal O}(q^4)$, and it is thus possible to absorb the one-loop divergences by an appropriate renormalization of the coefficients $L_i$ and $H_i$: $$\label{3:3:1:lihi}
L_i=L_i^r+\frac{\Gamma_i}{32\pi^2}R \quad (i=1,\cdots,10),\quad
H_i=H^r_i+\frac{\Delta_i}{32\pi^2}R\quad (i=1,2),$$ where $R$ has already been defined in Eq. ([\[3:2:5:R\]](#3:2:5:R){reference-type="ref" reference="3:2:5:R"}): $$R=\frac{2}{n-4}
-[\mbox{ln}(4\pi)+\Gamma'(1)+1],$$ with $n$ denoting the number of space-time dimensions and $\gamma_E=-\Gamma'(1)$ being Euler's constant. The constants $\Gamma_i$ and $\Delta_i$ are given in Table [1](#4:8:tableli){reference-type="ref" reference="4:8:tableli"}. Except for $L_3$ and $L_7$, the low-energy coupling constants $L_i$ and the "contact terms"---i.e., pure external field terms---$H_1$ and $H_2$ are required in the renormalization of the one-loop graphs. Since $H_1$ and $H_2$ contain only external fields, they are of no physical relevance.

::: center
::: {#4:8:tableli}
   Coefficient    Empirical Value         $\Gamma_i$
  ------------- ----------------- ------------------
     $L_1^r$         $0.4\pm 0.3$     $\frac{3}{32}$
     $L_2^r$        $1.35\pm 0.3$     $\frac{3}{16}$
     $L_3^r$        $-3.5\pm 1.1$                $0$
     $L_4^r$        $-0.3\pm 0.5$      $\frac{1}{8}$
     $L_5^r$         $1.4\pm 0.5$      $\frac{3}{8}$
     $L_6^r$        $-0.2\pm 0.3$   $\frac{11}{144}$
     $L_7^r$        $-0.4\pm 0.2$                $0$
     $L_8^r$         $0.9\pm 0.3$     $\frac{5}{48}$
     $L_9^r$         $6.9\pm 0.7$      $\frac{1}{4}$
   $L_{10}^r$       $-5.5\pm 0.7$     $-\frac{1}{4}$

  : Renormalized low-energy coupling constants $L_i^r$ in units of $10^{-3}$ at the scale $\mu=M_\rho$, see [@Bijnens:1994qh:9]. $\Delta_1=-1/8$, $\Delta_2=5/24$.
:::
:::

The idea of renormalization consists of adjusting the parameters of the counter terms of the most general effective Lagrangian so that they cancel the divergences of (multi-) loop diagrams. In doing so, one still has the freedom of choosing a suitable renormalization condition. For example, in the minimal subtraction scheme (MS) one would fix the parameters of the counter term Lagrangian such that they would precisely absorb the contributions proportional to $2/(n-4)$ in $R$, while the modified minimal subtraction scheme of ChPT ($\widetilde{\rm MS}$) would, in addition, cancel the term in the square brackets.

The renormalized coefficients $L_i^r$ depend on the scale $\mu$ introduced by dimensional regularization \[see Eq. ([\[3:2:4:IMmun\]](#3:2:4:IMmun){reference-type="ref" reference="3:2:4:IMmun"})\] and their values at two different scales $\mu_1$ and $\mu_2$ are related by $$\label{3:3:1:limu1mu2}
L^r_i(\mu_2)=L^r_i(\mu_1)
+\frac{\Gamma_i}{16\pi^2}\ln\left(\frac{\mu_1}{\mu_2}\right).$$ We will see that the scale dependence of the coefficients and the finite part of the loop-diagrams compensate each other in such a way that physical observables are scale independent.

A discussion of the two-flavor Lagrangian at ${\cal O}(q^4)$ [@Gasser:1983yg] can be found in Appendix D of Ref. [@Scherer:2002tk]. For the construction of the ${\cal O}(q^6)$ Lagrangian of even intrinsic parity, see Refs. [@Scherer:1994wi], [@Fearing:1994ga] and [@Bijnens:1999sh]. For a status report on mesonic chiral perturbation theory beyond the one-loop level, we refer the reader to Ref. [@Bijnens:2006zp].

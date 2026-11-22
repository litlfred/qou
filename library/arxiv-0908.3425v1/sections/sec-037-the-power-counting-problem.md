---
doc_id: arxiv-0908.3425v1
doc_title: "Chiral Perturbation Theory: Introduction and Recent Results in the One-Nucleon Sector"
section_id: sec-037-the-power-counting-problem
section_title: "The power-counting problem"
section_number: null
pages: 54-57
source_pdf: 0908.3425v1.pdf
source_sha256: 5e88d45bbc1c1b9b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.938
latex_coverage_ratio: 0.996
doc_brief: "Chiral Perturbation Theory: Introduction and Recent Results in the One-Nucleon Sector — We provide an introduction to the basic concepts of chiral perturbation theory and discuss some recent"
---
In the mesonic sector, the combination of dimensional regularization and the modified minimal subtraction scheme $\widetilde{\mbox{MS}}$ \[see Eq. ([\[3:3:1:lihi\]](#3:3:1:lihi){reference-type="ref" reference="3:3:1:lihi"})\] leads to a straightforward correspondence between the chiral and loop expansions. By studying the one-loop contributions of Fig. [1](#4:2:3:SEDia){reference-type="ref" reference="4:2:3:SEDia"} to the nucleon self energy, we will see that this correspondence, at first sight, seems to be lost in the baryonic sector.

In the following we will calculate the mass $m_N$ of the nucleon up to and including ${\cal O}(q^3)$. As in the case of the Goldstone bosons, the physical mass is defined through the pole of the full propagator, but here at $\slashed{p}=m_N$. In terms of the nucleon self energy $\Sigma(\slashed{p})$ we will solve the equation $$\label{4:2:3:MassDef}
m_N-m-\Sigma(m_N)=0,$$ where $m$ denotes the nucleon mass in the chiral limit.

According to the power counting specified above, we need to calculate the two types of one-loop contributions shown in Fig. [1](#4:2:3:SEDia){reference-type="ref" reference="4:2:3:SEDia"} together with the corresponding counter-term contribution and a tree-level contribution.

<figure id="4:2:3:SEDia">
<div class="center">

</div>
<figcaption><span id="4:2:3:SEDia" label="4:2:3:SEDia"></span> One-loop contributions to the nucleon self energy. The number 1 in the interaction blobs refers to <span class="math inline">${\cal L}_{\pi
N}^{(1)}$</span>.</figcaption>
</figure>

After renormalization, we would like to have the orders $D=n\cdot 1-2\cdot 1-1\cdot 1+2\cdot 1=n-1$ for the first loop diagram and $n\cdot 1-2\cdot 1+1\cdot 1=n-1$ for the second loop diagram.

The basic interaction Lagrangian obtained from expanding $\mathcal{L}_{\pi N}^{(1)}$ up to and including two pion fields reads $$\label{5:3:lpin}
{\cal L}_{\rm int}^{(1)}=-\frac{1}{2}\frac{{\texttt
g}_{A}}{F} \bar{\Psi}\gamma^\mu\gamma_5
\partial_\mu\phi_i\tau_i\Psi
-\frac{1}{4F^2}\bar{\Psi}\gamma^\mu\vec{\phi}
\times\partial_\mu\vec{\phi}\cdot\vec{\tau}\,\Psi.$$ The corresponding Feynman rules are given by

::: center
+:---------------------------------------------------------:+:-:+
| &                                                         |   |
|                                                           |   |
| $$\label{4:2:3:feynmanrule1}                              |   |
| -\frac{{\texttt g}_{A}}{2F}\,\slashed{k}\gamma_5\tau_a,$$ |   |
+-----------------------------------------------------------+---+
:::

From the next-to-leading-order $\pi N$ Lagrangian $\mathcal{L}_{\pi N}^{(2)}$ we only need one term, namely, $$\label{4:2:3:LpiN2}
\mathcal{L}_{\pi N}^{(2)}=c_1\,\mbox{Tr}(\chi U^\dagger +U\chi^\dagger)\bar{\Psi}\Psi+\cdots,$$ resulting in the constant tree-level contribution $$\Sigma^{\rm tree}_2=-4 c_1 M^2.$$ Moreover, there are no tree-level contributions from the Lagrangian $\mathcal{L}_{\pi N}^{(3)}$. The second diagram of Fig. [1](#4:2:3:SEDia){reference-type="ref" reference="4:2:3:SEDia"} is zero, because the contraction $\epsilon_{aac}=0$ in the Feynman rule of Eq. ([\[4:2:3:feynmanrule2\]](#4:2:3:feynmanrule2){reference-type="ref" reference="4:2:3:feynmanrule2"}) vanishes. In dimensional regularization, the first diagram of Fig. [1](#4:2:3:SEDia){reference-type="ref" reference="4:2:3:SEDia"} generates the contribution $$\label{4:2:3:Loop1}
-i\Sigma^{\rm loop}(\slashed{p})
=-i\frac{3\texttt{g}_{A}^2}{4F^2}\,
    i\mu^{4-n}\int\frac{\mbox{d}^nk}{(2\pi)^n}\frac{\slashed{k}
    (\slashed{p}-m-\slashed{k})\slashed{k}}
    {[(p-k)^2-m^2+i0^+](k^2-M^2+i0^+)}.$$ Using $\{\gamma_\mu, \gamma_\nu\}=2g_{\mu\nu}$, the numerator of the integrand is written as $$\label{Num}
    -(\slashed{p}+m)k^2+(p^2-m^2)\slashed{k}
    -\left[(p-k)^2-m^2\right]\slashed{k},$$ yielding the intermediate result $$\begin{aligned}
\label{4:2:3:LoopRes}
\Sigma^{\rm loop}(\slashed{p})&=&
  \frac{3\texttt{g}_{A}^2}{4F^2}\,
  \left\{-(\slashed{p}+m)\mu^{4-n}i\int\frac{\mbox{d}^nk}{(2\pi)^n}
  \frac{1}{(p-k)^2-m^2+i0^+}\right.\nonumber\\
&&-(\slashed{p}+m)M^2\mu^{4-n}i\int\frac{\mbox{d}^nk}{(2\pi)^n}
  \frac{1}{[(p-k)^2-m^2+i0^+](k^2-M^2+i0^+)}\nonumber\\
&&
+(p^2-m^2)\mu^{4-n}i\int\frac{\mbox{d}^nk}{(2\pi)^n}
  \frac{\slashed{k}}{[(p-k)^2-m^2+i0^+](k^2-M^2+i0^+)}\nonumber\\
&& \left.-\mu^{4-n}i\int\frac{\mbox{d}^nk}{(2\pi)^n}
\frac{\slashed{k}}{k^2-M^2+i0^+}\right\}.
\end{aligned}$$ The last term in Eq. ([\[4:2:3:LoopRes\]](#4:2:3:LoopRes){reference-type="ref" reference="4:2:3:LoopRes"}) vanishes since the integrand is odd in $k$. We use the following convention for scalar loop integrals, $$\label{scalarInt}
I_{N\cdots\pi\cdots}(p_1,\cdots,q_1,\cdots)
=\mu^{4-n}i\int\frac{\mbox{d}^nk}{(2\pi)^n}
    \frac{1}{[(k+p_1)^2-m^2+i0^+]\cdots[(k+q_1)^2-M^2+i0^+]\cdots}\,.$$ The vector integral in the third line of Eq. ([\[4:2:3:LoopRes\]](#4:2:3:LoopRes){reference-type="ref" reference="4:2:3:LoopRes"}) is determined using the ansatz $$\label{vecInt}
    \mu^{4-n}i\int\frac{\mbox{d}^nk}{(2\pi)^n}
  \frac{k_\mu}{[(p-k)^2-m^2+i0^+](k^2-M^2+i0^+)}=
  p_\mu \, C.$$ Multiplying Eq. ([\[vecInt\]](#vecInt){reference-type="ref" reference="vecInt"}) by $p^\mu$, one obtains for $C$, $$\label{C}
    C=\frac{1}{2p^2}\left[I_N-I_\pi+(p^2-m^2+M^2)I_{N\pi}(-p,0)\right].$$ In terms of the above convention for the scalar loop integrals the loop contribution to the nucleon self energy reads $$\begin{aligned}
\label{4:2:3:LoopResInt}
\Sigma^{\rm loop}(\slashed{p})
&=&-\frac{3\texttt{g}_{A}^2}{4F^2}\,\Bigg\{
(\slashed{p}+m)I_N+(\slashed{p}+m)M^2 I_{N\pi}(-p,0)\nonumber\\
&&-(p^2-m^2)\frac{\slashed{p}}{2p^2}
\left[I_N-I_\pi+(p^2-m^2+M^2)I_{N\pi}(-p,0)\right]\Bigg\}.
\end{aligned}$$ The explicit expressions for the integrals are given by $$\begin{aligned}
\label{Int}
  I_{\pi}&=&\frac{M^2}{16\pi^2}\left[R+\ln{\left(\frac{M^2}{\mu^2}\right)}\right],\quad
  I_{N}=\frac{m^2}{16\pi^2}
\left[R+\ln{\left(\frac{m^2}{\mu^2}\right)}\right],\nonumber\\
  I_{N\pi}(p,0)&=&\frac{1}{16\pi^2}
\left[R+\ln{\left(\frac{m^2}{\mu^2}\right)}-1
+
\frac{p^2-m^2-M^2}{p^2}\ln{\left(\frac{M}{m}\right)}
+\frac{2m M}{p^2}F(\Omega)\right],
\end{aligned}$$ where $R$ is given in Eq. ([\[3:2:5:R\]](#3:2:5:R){reference-type="ref" reference="3:2:5:R"}), $\Omega$ is defined as $$\Omega=\frac{p^2-m^2-M^2}{2m M},$$ and $$F(\Omega)=\left\{\begin{array}{l@{\quad}l}
\sqrt{\Omega^2-1}\ln{\left(-\Omega-\sqrt{\Omega^2-1}\right)}, &
\Omega\le -1,\\
\sqrt{1-\Omega^2}\;\arccos(-\Omega),&-1 \le\Omega\le 1,\\
\sqrt{\Omega^2-1}\ln{\left(\Omega+\sqrt{\Omega^2-1}\right)}
-i\pi\sqrt{\Omega^2-1}, & 1 \le \Omega\,.
\end{array}\right.$$ Because of the terms proportional to $R$, the result for the self energy contains divergences as $n\rightarrow 4$, so it has to be renormalized. The counter-term Lagrangian must produce structures which precisely cancel the divergences, because otherwise the result for the nucleon mass will not be finite. For convenience, we choose the renormalization parameter $\mu=m$.

<figure id="4:2:3:ren_diag">
<div class="center">

</div>
<figcaption><span id="4:2:3:ren_diag" label="4:2:3:ren_diag"></span> Renormalized one-loop self-energy diagram.</figcaption>
</figure>

In the modified minimal subtraction scheme $\widetilde{\mbox{MS}}$ all the contributions proportional to $R$ are canceled by corresponding contributions generated by the counter-term Lagrangian of Eq. ([\[4:2:1:lcounterterm\]](#4:2:1:lcounterterm){reference-type="ref" reference="4:2:1:lcounterterm"}), but also by counter-term Lagrangians resulting from higher-order terms of Eq. ([\[4:2:full_lagrangian\]](#4:2:full_lagrangian){reference-type="ref" reference="4:2:full_lagrangian"}). Operationally this means that we simply drop all terms proportional to $R$ and indicate the renormalized coupling constants by a subscript $r$. Again, this is possible, because we include in the Lagrangian all of the infinite number of interactions allowed by symmetries [@Weinberg:1995mt]. The renormalized diagram is depicted in Fig. [2](#4:2:3:ren_diag){reference-type="ref" reference="4:2:3:ren_diag"}, where the cross generically denotes counter-term contributions. The $\widetilde{\rm MS}$-renormalized self-energy contribution then reads $$\label{4:2:3:SErenorm}
\Sigma^{\rm
loop}_r(\slashed{p})=-\frac{3\texttt{g}_{Ar}^2}{4F^2}\,\Bigg\{
(\slashed{p}+m)M^2
I_{N\pi}^r(-p,0)
-(p^2-m^2)\frac{\slashed{p}}{2p^2}
\left[(p^2-m^2+M^2)I_{N\pi}^r(-p,0)-I_\pi^r\right]\Bigg\},$$ where the superscript $r$ on the integrals means that the terms proportional to $R$ have been dropped. Writing $\slashed{p}+m=2m+(\slashed p-m)$ and comparing the first term of Eq. ([\[4:2:3:LoopResInt\]](#4:2:3:LoopResInt){reference-type="ref" reference="4:2:3:LoopResInt"}) with Eq. ([\[4:2:3:SErenorm\]](#4:2:3:SErenorm){reference-type="ref" reference="4:2:3:SErenorm"}), we note that among other terms, the $\widetilde{\rm MS}$ renormalization involves (even in the chiral limit) an infinite renormalization yielding the relation between the bare and the renormalized mass [@Gasser:1987rb] $$m_B=m+\frac{3\texttt{g}_{Ar}^2}{32\pi^2 F^2}m^3 R+\cdots.$$ Using $$I_{N\pi}^r(-p,0)=-\frac{1}{16\pi^2}+\cdots,$$ we see that the $\widetilde{\rm MS}$-renormalized self energy produces a contribution of ${\cal O}(q^2)$ which is in conflict with the power counting assigned above. For a long time this was interpreted as the absence of a systematic power counting in the relativistic formulation of ChPT.

We can now solve Eq. ([\[4:2:3:MassDef\]](#4:2:3:MassDef){reference-type="ref" reference="4:2:3:MassDef"}) for the nucleon mass, $$m_N=m+\Sigma^{\rm tree}_{2r}(m_N)+\Sigma^{\rm loop}_r(m_N)=m-4c_{1r}M^2+\Sigma^{\rm loop}_r(m_N).$$ We have for the difference $m_N-m={\cal O}(q^2)$. Since our calculation is only valid up to ${\cal O}(q^3)$, it is sufficient to determine $\Sigma^{\rm loop}_r(m_N)$ to that order. In fact, using $\arccos{(-\Omega)}=\frac{\pi}{2}+\cdots,$ the expansion of $I_{N\pi}^r$ is given by $$\label{4:2:3:INpExp}
    I_{N\pi}^r=\frac{1}{16\pi^2}\left(-1+\frac{\pi M}{m}+\cdots\right),$$ from which we obtain for the nucleon mass in the $\widetilde{\rm MS}$ scheme [@Gasser:1987rb], $$\label{4:2:3:MassMStilde}
    m_N=m-4c_{1r}M^2+
    \frac{3\texttt{g}_{Ar}^2M^2}{32\pi^2F^2}m
    -\frac{3\texttt{g}_{Ar}^2M^3}{32\pi^2F^2}.$$ The solution to the power-counting problem is the observation that the term violating the power counting, namely, the third on the right-hand side of Eq. ([\[4:2:3:MassMStilde\]](#4:2:3:MassMStilde){reference-type="ref" reference="4:2:3:MassMStilde"}), is *analytic* in the quark mass and can thus be absorbed in counter terms. In addition to the $\widetilde{\rm MS}$ scheme we have to perform an additional *finite* renormalization. For that purpose we rewrite $$\label{4:2:3:cRenorm}
    c_{1r}=c_1+\delta c_1,\quad \delta c_1 =\frac{3 m {\texttt g}_A^2}{128 \pi^2 F^2}+\cdots$$ in Eq. ([\[4:2:3:MassMStilde\]](#4:2:3:MassMStilde){reference-type="ref" reference="4:2:3:MassMStilde"}) which then gives the final result for the nucleon mass at ${\cal O}(q^3)$: $$\label{4:2:3:MassFinal}
    m_N=m-4c_{1}M^2
    -\frac{3\texttt{g}_{A}^2M^3}{32\pi^2F^2}.$$ To summarize, we have shown that the validity of a power-counting scheme is intimately connected with a suitable renormalization condition. In the case of the nucleon mass, the $\widetilde{\rm MS}$ scheme alone does not suffice to bring about a consistent power counting. We will shortly outline two methods, the infrared renormalization [@Becher:1999he] and the extended on-mass-shell renormalization [@Fuchs:2003qc], which both produce a systematic power counting in a manifestly Lorentz-invariant framework.

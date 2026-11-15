---
doc_id: arxiv-0908.3425v1
doc_title: "Chiral Perturbation Theory: Introduction and Recent Results in the One-Nucleon Sector"
section_id: sec-024-power-counting-scheme
section_title: "Power-counting scheme"
section_number: null
pages: 35-37
source_pdf: 0908.3425v1.pdf
source_sha256: 5e88d45bbc1c1b9b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.955
latex_coverage_ratio: 0.982
doc_brief: "Chiral Perturbation Theory: Introduction and Recent Results in the One-Nucleon Sector — We provide an introduction to the basic concepts of chiral perturbation theory and discuss some recent"
---
The Lagrangian ${\cal L}_{\rm eff}$ of mesonic chiral perturbation theory is organized as a string of terms with an increasing number of derivatives and quark-mass terms, $$\label{3:2:3:ll2l4}
{\cal L}_{\rm eff}={\cal L}_2 + {\cal L}_4 + {\cal L}_6 +\cdots,$$ where the subscripts refer to the order in the momentum and quark-mass expansion. The index 2, for example, denotes either two derivatives or one quark-mass term. In terms of Feynman rules, derivatives generate four-momenta. A quark-mass term counts as two derivatives because of Eqs. ([\[3:2:2:mpi2\]](#3:2:2:mpi2){reference-type="ref" reference="3:2:2:mpi2"}) - ([\[3:2:2:meta2\]](#3:2:2:meta2){reference-type="ref" reference="3:2:2:meta2"}) ($M^2\sim m_q$) in combination with the on-shell condition $p^2=M^2$. We will generically count a small four-momentum---or the corresponding derivative---and a Goldstone-boson mass as of ${\cal O}(q)$. The chiral orders in Eq. ([\[3:2:3:ll2l4\]](#3:2:3:ll2l4){reference-type="ref" reference="3:2:3:ll2l4"}) are all even \[${\cal O}(q^{2k})$, $k\geq 1$\], because Lorentz indices of derivatives always have to be contracted and quark-mass terms count as ${\cal O}(q^2)$.

Besides the knowledge of the most general Lagrangian, we need a method which allows one to assess the importance of different renormalized diagrams contributing to a given process. For that purpose we analyze a given diagram under a simultaneous re-scaling of all *external* momenta, $p_i\mapsto t p_i$, and the light-quark masses, $m_q\mapsto t^2 m_q$ (corresponds to $M^2\mapsto t^2 M^2$). The chiral dimension $D$ of a given diagram is defined as $$\label{3:2:3:mr1} {\cal M}(tp_i, t^2 m_q,t\mu)=t^D {\cal M}(p_i,m_q,\mu)={\cal
O}(q^D).$$ For small enough momenta (and masses) contributions with increasing $D$ become less important. The chiral dimension is given by $$\begin{aligned}
\label{3:2:3:mr2a} D&=&n N_L-2N_I+\sum_{k=1}^\infty 2k N_{2k}\\&=&
2+(n-2)N_L+\sum_{k=1}^\infty 2(k-1)N_{2k} \label{3:2:3:mr2b}
\\
&\geq&2\,\,\,{\rm in\,\, 4\,\, dimensions,}\nonumber
\end{aligned}$$ where $n$ is the number of space-time dimensions, $N_L$ the number of independent loops, $N_I$ the number of internal Goldstone boson lines, and $N_{2k}$ the number of vertices from ${\cal L}_{2k}$. Equation ([\[3:2:3:mr2b\]](#3:2:3:mr2b){reference-type="ref" reference="3:2:3:mr2b"}) establishes a relation between the momentum and loop expansion, because at each chiral order, the maximum number of loops is bounded from above. In other words, we have a perturbative scheme in terms of external momenta and masses which are small compared to some scale \[here: $\Lambda_\chi=4\pi F_0={\cal O}$ (1 GeV)\]. Examples of the application of the power-counting formula are shown in Fig. [1](#3:2:3:figure:power_counting){reference-type="ref" reference="3:2:3:figure:power_counting"}.

<figure id="3:2:3:figure:power_counting">
<div class="center">

</div>
<p><span class="math display"><em>D</em> = 4 ⋅ 2 − 2 ⋅ 3 + 2 ⋅ 2 = 6.</span></p>
<div class="center">

</div>
<p><span class="math display"><em>D</em> = 4 ⋅ 2 − 2 ⋅ 3 + 2 ⋅ 1 + 4 ⋅ 1 = 8.</span></p>
<div class="center">

</div>
<p><span class="math display"><em>D</em> = 4 ⋅ 4 − 2 ⋅ 5 + 2 ⋅ 2 = 10.</span></p>
<figcaption><span id="3:2:3:figure:power_counting" label="3:2:3:figure:power_counting"></span> Application of the power-counting formula of Eq. (<a href="#3:2:3:mr2a" data-reference-type="ref" data-reference="3:2:3:mr2a">[3:2:3:mr2a]</a>) in <span class="math inline"><em>n</em> = 4</span> dimensions.</figcaption>
</figure>

In order to prove the power-counting formula we start from the Feynman rules for evaluating the S-matrix element and investigate the behavior of the individual building blocks. Internal lines are described by a propagator in $n$ dimensions which under re-scaling behaves as $$\int \frac{\mbox{d}^n k}{(2\pi)^n} \frac{i}{k^2-M^2+i0^+}
\to \int \frac{\mbox{d}^n k}{(2\pi)^n}
\frac{i}{t^2(k^2/t^2-M^2+i0^+)}
\stackrel{\mbox{$k=tk'$}}{=}t^{n-2}
\int \frac{\mbox{d}^n k'}{(2\pi)^n} \frac{i}{k'^2-M^2+i0^+}.$$ Vertices with $2k$ derivatives or $k$ quark-mass terms re-scale as $$\delta^n(q) q^{2k}\to t^{2k-n}\delta^n(q) q^{2k},$$ since $p\to tp$ if $q$ is an external momentum, and $k=tk'$ if $q$ is an internal momentum (see above). These are the rules to calculate $S \sim \delta^n(P) \cal M$. We need to add $n$ to compensate for the overall momentum-conserving delta function. Applying these rules, the scaling behavior of the contribution to $\cal M$ of a given diagram reads $$D=n+(n-2)N_I+\sum_{k=1}^\infty N_{2k} (2k-n).$$ The relation between the number of independent loops, the number of internal lines, and the total number of vertices $N_V=\sum_{k=1}^\infty N_{2k}$ is given by $N_L=N_I-(N_V-1)$. The product of $N_V$ momentum-conserving $\delta$ functions contains overall momentum conservation. Therefore, one has $N_V-1$ rather than $N_V$ restrictions on the internal momenta. Applying $$-n \sum_{k=1}^\infty N_{2k}=-n N_V=n(N_L-N_I-1)$$ results in Eq. ([\[3:2:3:mr2a\]](#3:2:3:mr2a){reference-type="ref" reference="3:2:3:mr2a"}): $$D=n N_L-2N_I+\sum_{k=1}^\infty 2k N_{2k}.$$ On the other hand, applying $$-n \sum_{k=1}^\infty N_{2k}= -2 \sum_{k=1}^\infty N_{2k}
+(n-2)(N_L-N_I-1),$$ results in Eq. ([\[3:2:3:mr2b\]](#3:2:3:mr2b){reference-type="ref" reference="3:2:3:mr2b"}): $$D=2+\sum_{k=1}^\infty2(k-1)N_{2k}+(n-2)N_L.$$ In particular, diagrams containing loops are suppressed due to the term $2 N_L$ in four dimensions.

Note that a minimal $k>0$ is important. Otherwise, an infinite number of diagrams containing vertices from ${\cal L}_0$ would have to be summed (see Fig. [2](#3:2:5:minimalk:fig){reference-type="ref" reference="3:2:5:minimalk:fig"}). This is for example the case when dealing with the nucleon-nucleon interaction.

<figure id="3:2:5:minimalk:fig">
<div class="center">
<p><span class="math display">$$D=0-0+2k=2k=\left\{
\begin{array}{l}
0\,\,\mbox{for}\,\,k=0,\\
2\,\,\mbox{for}\,\,k=1.
\end{array}\right.$$</span></p>
</div>
<div class="center">
<p><span class="math display">$$D=4-2\cdot 2+2\cdot (2k)=4k=\left\{
\begin{array}{l}
0\,\,\mbox{for}\,\,k=0,\\
4\,\,\mbox{for}\,\,k=1.
\end{array}\right.$$</span></p>
</div>
<figcaption><span id="3:2:5:minimalk:fig" label="3:2:5:minimalk:fig"></span> The loop diagram is only suppressed if <span class="math inline">$k_{\rm min} &gt; 0$</span>.</figcaption>
</figure>

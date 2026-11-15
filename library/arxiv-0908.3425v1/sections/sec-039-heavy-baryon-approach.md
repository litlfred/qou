---
doc_id: arxiv-0908.3425v1
doc_title: "Chiral Perturbation Theory: Introduction and Recent Results in the One-Nucleon Sector"
section_id: sec-039-heavy-baryon-approach
section_title: "Heavy-baryon approach"
section_number: null
pages: 57-59
source_pdf: 0908.3425v1.pdf
source_sha256: 5e88d45bbc1c1b9b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.978
latex_coverage_ratio: 0.985
doc_brief: "Chiral Perturbation Theory: Introduction and Recent Results in the One-Nucleon Sector — We provide an introduction to the basic concepts of chiral perturbation theory and discuss some recent"
---
[]{#hb label="hb"} The first solution to the power-counting problem was provided by the heavy-baryon formulation of ChPT [@Jenkins:1990jv], [@Bernard:1992qa]. The basic idea consists in dividing an external nucleon four-momentum into a large piece close to on-shell kinematics and a soft residual contribution: $p = m v +k_p$, $v^2=1$, $v^0\ge 1$ \[often $v^\mu = (1,0,0,0)$\]. The relativistic nucleon field is expressed in terms of velocity-dependent fields, $$\Psi(x)=e^{-im v \cdot x} ({\cal N}_v +{\cal H}_v),$$ with $${\cal N}_v=e^{+im v\cdot x}\frac{1}{2}(1+v\hspace{-.5em}/)\Psi,\quad
{\cal H}_v=e^{+im v\cdot x}\frac{1}{2}(1-v\hspace{-.5em}/)\Psi.$$ Using the equation of motion for ${\cal H}_v$, one can eliminate ${\cal H}_v$ and obtain a Lagrangian for ${\cal N}_v$ which, to lowest order, reads [@Bernard:1992qa] $$\widehat{\cal L}^{(1)}_{\pi N}=\bar{\cal N}_v(iv\cdot D + \texttt{g}_A S_v\cdot u)
{\cal N}_v+{\cal O}(1/m),\quad S^\mu_v=\frac{i}{2}\gamma_5\sigma^{\mu\nu}v_\nu.$$ The result of the heavy-baryon reduction is a $1/m$ expansion of the Lagrangian similar to a Foldy-Wouthuysen expansion [@Foldy:1949wa]. In higher orders in the chiral expansion, the expressions due to $1/m$ corrections of the Lagrangian become increasingly complicated [@Fettes:2000gb].

<figure id="4:3:1:fig:schannel">
<div class="center">

</div>
<figcaption><span class="math inline"><em>s</em></span>-channel pole diagram of <span class="math inline"><em>π</em></span>N scattering.</figcaption>
</figure>

Moreover---and what is more important---the approach sometimes generates problems regarding analyticity which can be illustrated by considering the example of pion-nucleon scattering [@Becher:2000mb]. The invariant amplitudes describing the scattering amplitude develop poles for $s=m_N^2$ and $u=m_N^2$. For example, the singularity due to the nucleon pole in the $s$ channel (see Fig. [1](#4:3:1:fig:schannel){reference-type="ref" reference="4:3:1:fig:schannel"}) is understood in terms of the relativistic propagator $$\label{relprop}
\frac{1}{(p+q)^2-m_N^2}=\frac{1}{2p\cdot q+M_\pi^2},$$ which, of course, has a pole at $2p\cdot q=-M_\pi^2$ or, equivalently, $s=m_N^2$. Analogously, a second pole results from the $u$ channel at $u=m_N^2$. Although both poles are not in the physical region of pion-nucleon scattering, analyticity of the invariant amplitudes requires these poles to be present in the amplitudes. Let us compare the situation with a heavy-baryon type of expansion, where, for simplicity, we choose as the four-velocity $p^\mu=m_N v^\mu$, $$\label{4:3:1:relpropv}
\frac{1}{2p\cdot q+M_\pi^2}=
\frac{1}{2m_N}\frac{1}{v\cdot q+ \frac{M_\pi^2}{2m_N}}
=\frac{1}{2 m_N}\frac{1}{v\cdot q}\left(1-\frac{M_\pi^2}{2 m_N v\cdot q}
+\cdots\right).$$ Clearly, to any finite order the heavy-baryon expansion produces poles at $v\cdot q=0$ instead of a simple pole at $v\cdot q=-M_\pi^2/(2 m_N)$ and will thus not generate the (nucleon) pole structures of the invariant amplitudes unless an infinite number of diagrams is summed. For a comprehensive overview of calculations performed in the heavy-baryon framework the reader is referred to Ref. [@Bernard:1995dp].

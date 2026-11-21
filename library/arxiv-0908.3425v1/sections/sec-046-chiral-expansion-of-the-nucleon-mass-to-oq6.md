---
doc_id: arxiv-0908.3425v1
doc_title: "Chiral Perturbation Theory: Introduction and Recent Results in the One-Nucleon Sector"
section_id: sec-046-chiral-expansion-of-the-nucleon-mass-to-oq6
section_title: "Chiral expansion of the nucleon mass to O(q6)"
section_number: null
pages: 67-68
source_pdf: 0908.3425v1.pdf
source_sha256: 5e88d45bbc1c1b9b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.961
latex_coverage_ratio: 0.984
doc_brief: "Chiral Perturbation Theory: Introduction and Recent Results in the One-Nucleon Sector — We provide an introduction to the basic concepts of chiral perturbation theory and discuss some recent"
---
So far, essentially all of the manifestly Lorentz-invariant calculations have been restricted to the one-loop level. One of the exceptions is the chiral expansion of the nucleon mass which, in the framework of the reformulated infrared regularization, has been calculated up to and including ${\cal O}(q^6)$ [@Schindler:2006ha; @Schindler:2007dr]: $$\label{Mass:Exp}
    m_N = m +k_1 M^2 +k_2 \,M^3 +k_3 M^4 \ln\frac{M}{\mu}
+ k_4 M^4  + k_5 M^5\ln\frac{M}{\mu} + k_6 M^5 + k_7
M^6 \ln^2\frac{M}{\mu}+ k_8 M^6 \ln\frac{M}{\mu} + k_9 M^6.$$ We refrain from displaying the lengthy expressions for the coefficients $k_i$ but rather want to discuss a few general implications [@Schindler:2007dr]. Chiral expansions like Eq. ([\[Mass:Exp\]](#Mass:Exp){reference-type="ref" reference="Mass:Exp"}) currently play an important role in the extrapolation of lattice QCD results to physical quark masses. Unfortunately, the numerical contributions from higher-order terms cannot be calculated so far since, starting with $k_4$, most expressions in Eq. ([\[Mass:Exp\]](#Mass:Exp){reference-type="ref" reference="Mass:Exp"}) contain unknown low-energy coupling constants (LECs) from the Lagrangians of ${\cal O}(q^4)$ and higher. The coefficient $k_5$ is free of higher-order LECs and is given in terms of the axial-vector coupling constant $\texttt{g}_A$ and the pion-decay constant $F$: $$k_5 = \frac{3 \texttt{g}_A^2}{1024\pi^3 F^4}\,\left(16\texttt{g}_A^2-3\right).$$ While the values for both $\texttt{g}_A$ and $F$ should be taken in the chiral limit, we evaluate $k_5$ using the physical values $g_A=1.2695(29)$ and $F_\pi=92.42(26)$ MeV. Setting $\mu=m_N$, $m_N=(m_p+m_n)/2=938.92$ MeV, and $M=M_{\pi^+}=139.57$ MeV we obtain $k_5 M^5 \ln(M/m_N) = -4.8$ MeV. This amounts to approximately $31$% of the leading non-analytic contribution at one-loop order, $k_2 M^3$. Figure [1](#Mass:k2k5Low){reference-type="ref" reference="Mass:k2k5Low"} shows the pion mass dependence of the term $k_5 M^5 \ln(M/m_N)$ (solid line) in comparison with the term $k_2
M^3$ (dashed line) for pion masses below $400\,\mbox{MeV}$ which is considered a region where chiral extrapolations are valid (see, e.g., Refs. [@Meissner:2005ba], [@Djukanovic:2006xc]).

<figure id="Mass:k2k5Low">
<div class="center">

</div>
<figcaption>Pion mass dependence of the term <span class="math inline"><em>k</em><sub>5</sub><em>M</em><sup>5</sup>ln (<em>M</em>/<em>m</em><sub><em>N</em></sub>)</span> (solid line) for <span class="math inline"><em>M</em> &lt; 400 MeV</span>. For comparison also the term <span class="math inline"><em>k</em><sub>2</sub><em>M</em><sup>3</sup></span> (dashed line) is shown.<span id="Mass:k2k5Low" label="Mass:k2k5Low"></span></figcaption>
</figure>

We see that already at $M \approx 360\,\mbox{MeV}$ the term $k_5 M^5 \ln(M/m_N)$ becomes as large as the leading non-analytic term at one-loop order, $k_2 M^3$, indicating the importance of the fifth-order terms at unphysical pion masses. Our results for the renormalization-scheme-independent terms agree with the heavy-baryon ChPT results of Ref. [@McGovern:1998tm].

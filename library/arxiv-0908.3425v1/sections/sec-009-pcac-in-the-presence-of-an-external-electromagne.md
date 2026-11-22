---
doc_id: arxiv-0908.3425v1
doc_title: "Chiral Perturbation Theory: Introduction and Recent Results in the One-Nucleon Sector"
section_id: sec-009-pcac-in-the-presence-of-an-external-electromagne
section_title: "PCAC in the presence of an external electromagnetic field"
section_number: null
pages: 15-16
source_pdf: 0908.3425v1.pdf
source_sha256: 5e88d45bbc1c1b9b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.957
latex_coverage_ratio: 0.974
doc_brief: "Chiral Perturbation Theory: Introduction and Recent Results in the One-Nucleon Sector — We provide an introduction to the basic concepts of chiral perturbation theory and discuss some recent"
---
[]{#subsec_pcacpeef label="subsec_pcacpeef"} Finally, the technique of coupling the QCD Lagrangian to external fields also allows us to determine the current divergences for rigid external fields, i.e., fields which are *not* simultaneously transformed. For the sake of simplicity we restrict ourselves to the two-flavor sector. (The generalization to the three-flavor case is straightforward.)

Consider a *global* chiral transformation only and assume that the external fields are *not* simultaneously transformed. In this case the divergences of the currents read [@Fuchs:2003vw] $$\begin{aligned}
\label{2:1:7:divv}
\partial_\mu V^\mu_i&=&i\bar{q}\gamma^\mu[\frac{\tau_i}{2},v_\mu]q
+i\bar{q}\gamma^\mu\gamma_5[\frac{\tau_i}{2},a_\mu]q
-i\bar{q}[\frac{\tau_i}{2},s]q-\bar{q}\gamma_5[\frac{\tau_i}{2},p]q,\\
\label{2:1:7:diva}
\partial_\mu A^\mu_i&=&i\bar{q}\gamma^\mu\gamma_5[\frac{\tau_i}{2},v_\mu]q
+i\bar{q}\gamma^\mu[\frac{\tau_i}{2},a_\mu]q
+i\bar{q}\gamma_5\{\frac{\tau_i}{2},s\}q
+\bar{q}\{\frac{\tau_i}{2},p\}q.
\end{aligned}$$

As an example, let us consider the QCD Lagrangian for a finite light quark mass $\hat{m}=m_u=m_d$ in combination with a coupling to an external electromagnetic field ${\cal A}_\mu$ \[see Eq. ([\[2:1:6:rlasu2\]](#2:1:6:rlasu2){reference-type="ref" reference="2:1:6:rlasu2"}), $a_\mu=0=p$\]. The expressions for the divergence of the vector and axial-vector currents, respectively, are given by [@Fuchs:2003vw] $$\begin{aligned}
\label{2:1:7:divvsc}
\partial_\mu V^\mu_i&=&-\epsilon_{3ij}e{\cal A}_\mu \bar{q}\gamma^\mu
\frac{\tau_j}{2}q=-\epsilon_{3ij}e{\cal A}_\mu V^\mu_j,\\
\label{2:1:7:divasc}
\partial_\mu A^\mu_i
&=&-e {\cal A}_\mu \epsilon_{3ij} \bar{q}\gamma^\mu
\gamma_5 \frac{\tau_j}{2} q+2\hat m i\bar{q}\gamma_5 \frac{\tau_i}{2}q
=-e {\cal A}_\mu \epsilon_{3ij} A^\mu_j+\hat m P_i,
\end{aligned}$$ with the isovector pseudoscalar density $P_i=i\bar{q}\gamma_5 \tau_i q$. In fact, Eq. ([\[2:1:7:divasc\]](#2:1:7:divasc){reference-type="ref" reference="2:1:7:divasc"}) is incomplete, because the third component of the axial-vector current, $A^\mu_3$, has an anomaly which is related to the decay $\pi^0\to\gamma\gamma$. The full equation reads $$\label{2:1:7:divascfull}
\partial_\mu A^\mu_i
=\hat m P_i-e {\cal A}_\mu \epsilon_{3ij} A^\mu_j
+\delta_{i3}
\frac{e^2}{32\pi^2}\epsilon_{\mu\nu\rho\sigma}{\cal F}^{\mu\nu}
{\cal F}^{\rho\sigma}, \quad \epsilon_{0123}=1,$$ where ${\cal F}_{\mu\nu}=\partial_\mu{\cal A}_\nu-\partial_\nu{\cal A}_\mu$ is the electromagnetic field strength tensor.

We emphasize the formal similarity of Eq. ([\[2:1:7:divasc\]](#2:1:7:divasc){reference-type="ref" reference="2:1:7:divasc"}) to the (pre-QCD) PCAC (Partially Conserved Axial-Vector Current) relation obtained by Adler [@Adler:1965:5:5] through the inclusion of the electromagnetic interactions with minimal electromagnetic coupling. Since in QCD the quarks are taken as truly elementary, their interaction with an (external) electromagnetic field is of such a minimal type. In Adler's version, the right-hand side of Eq. ([\[2:1:7:divascfull\]](#2:1:7:divascfull){reference-type="ref" reference="2:1:7:divascfull"}) contains a renormalized field operator creating and destroying pions instead of $\hat m P_i$. From a modern point of view, the combination $\hat m P_i/(M_\pi^2 F_\pi)$ serves as an interpolating pion field. Furthermore, the anomaly term is not yet present in Ref. [@Adler:1965:5:5].

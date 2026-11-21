---
doc_id: arxiv-1608.02961v3
doc_title: "Perturbative and nonperturbative aspects of complex Chern-Simons Theory Contents"
section_id: sec-003-22-holomorphic-polarizations-and-cft
section_title: "Holomorphic polarizations and CFT"
section_number: 2.2
pages: 9-10
source_pdf: 1608.02961v3.pdf
source_sha256: ef3805c23133b8f2
toc_source: outline
text_source: latex
latex_prose_ratio: 0.934
latex_coverage_ratio: 0.992
doc_brief: "Perturbative and nonperturbative aspects of complex Chern-Simons Theory Contents — We present an elementary review of some aspects of Chern-Simons theory with complex gauge group SL(N, C)."
---
Often in geometric quantization of Chern-Simons theory, one uses a holomorphic polarization instead of the real polarization above. In Chern-Simons theory with compact gauge group (\DIcf\ \cite{DIaxelrod-witten}), this means to choose a complex structure `$\tau$' on a surface $\Sigma$, to write the connection one-form as $A = A_zdz+A_{\bar z}d\bar z$ in local complex coordinates, and, when quantizing, to define the Hilbert space to consist of sections of the line bundle $\CalL\to \CalP[\Sigma]$ that are covariantly constant with respect to $A_{\bar z}$.

Naively, it may appear that choosing such a complex polarization needlessly complicates the problem. However, a complex polarization has three great advantages. First, it allows one to ask analyze the Hilbert space varies with the choice of complex structure. Locally the variation is trivial, expressed formally by saying that the bundle of Hilbert spaces over the space of complex structures (\DIie\ over the Teichm\"uller space of $\Sigma$) has a projectively flat connection. However, globally, one derives an action of the mapping class group of $\Sigma$ on the Chern-Simons Hilbert space. Second, and related to this idea, a holomorphic polarization allows one to identify the Hilbert space of Chern-Simons theory with the space of conformal blocks in a particular boundary CFT. In the case of compact Chern-Simons theory, the boundary CFT is a famously WZW model \cite{DIWit-Jones}. The projectively flat connection on Teichm\"uller space is the Knizhnik-Zamolodchikov connection of the CFT. Finally, for generic surfaces $\Sigma$ a real polarization as above simply isn't available! Thus, using a holomorphic polarization is the only way to go.

In the case of complex Chern-Simons theory, there are actually multiple choices of complex polarizations. If we write a complex connection and its conjugate as $\CalA = \CalA_z dz+\CalA_{\bar z}d\bar z$, $\ol \CalA = \ol\CalA_z dz+\ol\CalA_{\bar z}d\bar z$, then we can ask that sections of $\CalL$ be covariantly constant with respect to

\DIbe\text{(A)} \quad  \CalA_{\bar z}\,,\quad \ol \CalA_{z} \qquad \text{or}\qquad \text{(B)} \;\; \text{(some components of)} \; \;  \ol\CalA_{\bar z}\,,\quad \ol \CalA_{z}\,.
\DIee

The first choice was analyzed by Witten \cite{DIWitten-cx}, and leads to a boundary CFT whose conformal blocks must contain contributions from both chiral and anti-chiral sectors. This polarization plays a central role in the relation between $SL(2,\BC)$ Chern-Simons theory and quantum Hall systems \cite{DIVafa-FQHE, DIDGV-FQHE}. The second choice is related to Liouville theory coupled to parafermions \cite{DINT-para, DICJ-AGT}.

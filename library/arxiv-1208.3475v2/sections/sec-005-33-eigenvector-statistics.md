---
doc_id: arxiv-1208.3475v2
doc_title: "Poisson - Random Matrix transition in the QCD Dirac spectrum"
section_id: sec-005-33-eigenvector-statistics
section_title: "Eigenvector statistics"
section_number: 3.3
pages: 5-5
source_pdf: 1208.3475v2.pdf
source_sha256: d53fc4eefa070ba3
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.886
latex_coverage_ratio: 0.991
doc_brief: "Poisson - Random Matrix transition in the QCD Dirac spectrum — 12 sections: Front matter; Introduction; Simulation details"
---
Besides the spectrum the spatial profile of the corresponding eigenvectors also contains important information concerning their localization properties. A quantity that is widely used in this context is the inverse participation ratio (IPR) defined as [@wegner]

$$P_\psi = \sum_x \vert \psi(x) \vert^{4},
   \label{eq:IPR}$$

where $\psi$ is an eigenvector normalized as

$$\sum_x \vert \psi(x) \vert^2 = 1.$$

The qualitative physical meaning of the IPR can be easily seen by noting that an eigenmode that spreads uniformly in a four-volume $v$ and is zero everywhere else has $\mbox{IPR}=1/v$. The IPR$^{-1}$ thus measures the volume occupied by an eigenmode. Alternatively one can use the participation ratio, $\mbox{PR}=\mbox{IPR}^{-1} \cdot V$, where $V$ is the total volume of the system. This measures the fraction of the total volume occupied by the eigenmode.

The behavior of the IPR and the PR in the thermodynamic limit can be used to distinguish between localized and delocalized modes. By definition a part of the spectrum consists of localized modes if their average IPR remains finite as the volume goes to infinity. This also implies that their average PR vanishes in the thermodynamic limit. In contrast delocalized modes have vanishing IPR which usually implies non-vanishing PR.

In Fig. [1](#fig:particip){reference-type="ref" reference="fig:particip"} we plot how the average participation ratio of eigenmodes changes throughout the spectrum on ensembles C1-C4. The four data sets correspond to different spatial sizes but otherwise identical parameters. It is clearly seen that the average PR for the low eigenmodes decreases as the volume is increased; the average PR here tends to zero in the thermodynamic limit. This suggests that these eigenmodes are localized. They fill a vanishing fraction of the total box volume in the thermodynamic limit. Higher up in the spectrum the average PR becomes a volume independent constant of order unity, which means that these eigenmodes are delocalized. They fill a non-zero fraction of the total box volume in the thermodynamic limit.

<figure id="fig:particip">
<div class="center">
<embed src="particip.eps" />
</div>
<figcaption><span id="fig:particip" label="fig:particip"></span> Average <span class="math inline"><em>P</em><em>R</em></span> of the eigenvectors for lattices with the same temperature and lattice spacing but with four different aspect ratios.<span class="math inline"><em>N</em><sub><em>t</em></sub> = 4</span></figcaption>
</figure>

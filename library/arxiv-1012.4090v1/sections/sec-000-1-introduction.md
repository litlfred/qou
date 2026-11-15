---
doc_id: arxiv-1012.4090v1
doc_title: "Generalized Skyrme Crystals"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-1
source_pdf: 1012.4090v1.pdf
source_sha256: 02fe4a5eb36ff0ed
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.946
doc_brief: "Generalized Skyrme Crystals — This letter deals with triply-periodic (crystalline) solutions in a family of Skyrme systems, namely where the ﬁeld takes values in the squashed 3-sphere."
---
In the basic SU(2) Skyrme model, the solution with the lowest energy-per-charge $E_N$ is the triply-periodic skyrme crystal [@MS04]. For a given value of the topological charge (winding number, or baryon number) $N$, there are in general many isolated $N$-skyrmion solutions, *i.e.* local minima of the energy; but the belief is that for $N\gg1$, the lowest-energy solution will resemble a chunk of the skyrme crystal.

However, in the Skyrme-Faddeev system, where the field takes values in $S^2$ and the topological charge $N$ is the Hopf number, the situation is less clear. If there were a triply-periodic crystalline solution with $E_N=c$ (where $c$ is a constant independent of $N$), as in the Skyrme case, then a large crystalline chunk would have $E_N\sim c$. But we know [@Y04] that there exist solutions with $E_N\sim N^{-1/4}$, so such a crystal chunk certainly could not be the global energy minimum among fields of charge $N$, although it could be a local minimum. In general, it seems to be the case that Hopf solitons tend to clump into a tangle; various examples, for low values of $N$, may be seen in [@BS99; @HS99; @HJS04; @S07; @JH09].

The aim of this letter is to explore this difference in behaviour, by investigating triply-periodic crystalline solutions in a system which interpolates between the two cases above. This generalized Skyrme system was introduced in [@W04]; it is labelled by a parameter $\alpha\in[0,1]$, in such a way that $\alpha=0$ gives the 'pure' Skyrme model, whereas $\alpha=1$ gives the Skyrme-Faddeev model. In particular, we wish to see what happens to the skyrme crystal as the system deforms away from the basic Skyrme case.

The interpolating system is very natural geometrically. For simplicity, let us restrict to static fields in all of what follows. Let $\Sigma$ be a compact 3-dimensional, oriented, connected Riemannian manifold. Then for fields $\Phi:\mathbb R^3\to\Sigma$, the Skyrme energy functional $E[\Phi]$ has a natural definition, depending in particular on the metric of $\Sigma$ [@M87]. With the usual boundary condition $\Phi(x^j)\to \Phi_0$ as $|x^j|\to \infty$, where $\Phi_0$ is some specified point on $\Sigma$, the topological charge $N$ is defined to be the degree of the map $\Phi$. Our system is obtained by taking $\Sigma$ to be the squashed 3-sphere (Berger sphere): the standard 3-sphere squashed along its Hopf fibres by a factor $1-\alpha$. If $\alpha=0$, there is no squashing: the target space is just the round sphere SU(2), and we have the Skyrme model. In the degenerate case $\alpha=1$, the 3-sphere becomes a 2-sphere, the winding number $N$ becomes the Hopf number, and we have the Skyrme-Faddeev model.

The system has a potential condensed-matter interpretation in which the two complex fields $(Z_1,Z_2)$ represent two flavours of Cooper pairs [@BFN02]. The parameter $\alpha$ then appears as the coefficient of a term $J_{\mu} J^{\mu}$, where $J_{\mu}={\rm i}Z^\dagger\,\partial_{\mu}Z$ is the current density. In particular, arrays might be of interest in this context.

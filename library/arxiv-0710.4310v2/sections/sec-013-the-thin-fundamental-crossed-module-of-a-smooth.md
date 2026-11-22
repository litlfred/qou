---
doc_id: arxiv-0710.4310v2
doc_title: "On Two-Dimensional Holonomy"
section_id: sec-013-the-thin-fundamental-crossed-module-of-a-smooth
section_title: "The thin fundamental crossed module of a smooth manifold"
section_number: null
pages: 15-16
source_pdf: 0710.4310v2.pdf
source_sha256: 9a7757f998b7f680
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.966
doc_brief: "On Two-Dimensional Holonomy — We deﬁne the thin fundamental categorical group P2(M, ∗) of a based smooth manifold (M, ∗) as the categorical group whose objects are rank-1 homotopy classes of based"
---
[]{#fcm label="fcm"} Since $\Pc_2(M,*)$ is a categorical group, it defines a crossed module $\Pi_2^{2,1}(M,*)$, which we call the *thin fundamental crossed module of $M$.* Let us explain how to construct $\Pi_2^{2,1}(M,*)$ directly. Define a group $\pi_2^{2,1}(M,*)$ as being given by $$\pi_2^{2,1}(M,*)=\left \{[\G] \in \P_2(M,*) \colon \d_d({[\G]})=[*]\right \}$$ with the product law being the horizontal composition. Note that the map $\d \doteq \d_u \colon \pi_2^{2,1}(M,*)\to \pi_1^1(M,*)$ is therefore a group morphism. In addition $\pi_1^1(M,*)$ acts on $\pi_2^{2,1}(M,*)$ on the left as follows: $$[\g] \tr [\G]=\id_{[\g]} \circ_h [\G] \circ_h\id_{[\g^{-1}]},$$ where $[\G]\in {\pi_2^{2,1}(M,*)}$ and $[\g] \in \pi_1^1(M,*).$ Here if $[\g]$ is a 1-track then $\id_{[\g]}$ denotes the 2-track such that $\id_{[\g]}(s,t)=\g({t})$, where $s,t \in [0,1]$.

The following theorem follows from the well-known equivalence between the category of categorical groups and the category of crossed modules which was referred to in [\[CCG\]](#CCG){reference-type="ref" reference="CCG"}; see [@BM; @BL; @BMo; @P]. For a graphical proof see [@BHS 6.2].

::: Theorem
The boundary map $\d \colon \pi_2^{2,1}(M,*)\to \pi_1^1(M,*)$, together with the left action of $\pi_1^1(M,*)$ on $\pi_2^{2,1}(M,*)$, defines a crossed module, which we denote by $\Pi_2^{2,1}(M,*)$.
:::

In [\[CCG\]](#CCG){reference-type="ref" reference="CCG"} we showed how to construct a categorical group from any crossed module. The way we defined $\Pi_2^{2,1}(M,*)$ from the categorical group $\Pc_2(M,*)$ shows how to go in the reverse direction.

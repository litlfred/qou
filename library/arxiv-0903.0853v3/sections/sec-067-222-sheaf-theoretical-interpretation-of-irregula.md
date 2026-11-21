---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-067-222-sheaf-theoretical-interpretation-of-irregula
section_title: "Sheaf theoretical interpretation of irregularity"
section_number: 22.2
pages: 115-118
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.929
latex_coverage_ratio: 0.988
doc_brief: "Local analytic classification of q-difference equations — 114 sections: Front matter; The problem; The generalized Riemann problem an"
---
[]{#subsection:sheaftheoreticirregularity label="subsection:sheaftheoreticirregularity"}

We interpret here in sheaf theoretical terms the formula relating irregularity and the dimension of $\dim {\mathcal{F}}(P_{1},\ldots,P_{k})$ given in subsection [\[subsection:algebraicirregularity\]](#subsection:algebraicirregularity){reference-type="ref" reference="subsection:algebraicirregularity"}.\
Actually, the irregularity of $\underline{\text{End}}(M_{0})$ comes from its positive part: $$\label{not97}
\underline{\text{End}}^{> 0}(M_{0}) = 
\bigoplus_{1 \leq i < j \leq k} \underline{\text{Hom}}(P_{i},P_{j}).$$ For each pure component $P_{i,j} := \underline{\text{Hom}}(P_{j},P_{i})$, the computations of sections [\[section:isoformalclasses\]](#section:isoformalclasses){reference-type="ref" reference="section:isoformalclasses"} and [\[section:indextheorems\]](#section:indextheorems){reference-type="ref" reference="section:indextheorems"} give: $$\dim \Gamma^{0}(P_{i,j}) - \dim \Gamma^{1}(P_{i,j}) = 
r_{i} r_{j} (\mu_{j} - \mu_{i}).$$ As we know, ${\mathcal{F}}(P_{1},\ldots,P_{k}) = {\mathcal{F}}(M_{0})$ is isomorphic to the first cohomology set of the sheaf $\Lambda_I(M_{0})$. Also, in the previous section, we have seen that this is an affine space with underlying vector space the first cohomology space of the sheaf $\lambda_I(M_{0})$ of their Lie algebras. And the latter, from its description as $\bigoplus_{\delta \geq 1} \lambda^{(\delta)}$, is the vector bundle associated to the $q$-difference module $\underline{\text{End}}^{> 0}(M_{0})$. So the irregularity is actually an Euler-Poincaré characteristic.

# Examples of the Stokes phenomenon {#chapter:examplesStokes}

In the study of $q$-special functions, one frequently falls upon series that are *convergent* solutions of *irregular* $q$-difference equations, the latter thus also admitting *divergent* solutions; and this should be so, since Adams lemma[^1] ensures us that irregular equations always have *some* convergent solutions. However, in most works, only convergent solutions have been considered, although the other ones are equally interesting[^2]\
The touchstone of any theory of the Stokes phenomenon is Euler series. We shall therefore concentrate on one of its $q$-analogs, the $q$-Euler or Tshakaloff series $\text{\tencyr\cyracc Ch}(z)$ (see equation [\[eqn:Tshakaloff\]](#eqn:Tshakaloff){reference-type="eqref" reference="eqn:Tshakaloff"}, page ). The simplest $q$-difference equation satisfied by $\text{\tencyr\cyracc Ch}$ is the $q$-Euler equation $z \sigma_qf - f = -1$. We shall detail the Stokes phenomenon for a family of similar equations in [\[section:qEuler\]](#section:qEuler){reference-type="ref" reference="section:qEuler"} and we shall apply it to some confluent basic hypergeometric series. Then we shall show how such equations naturally appear in some well known historical cases: that of Mock Theta functions in [\[section:MockTheta\]](#section:MockTheta){reference-type="ref" reference="section:MockTheta"}, that of the enumeration of class numbers of quadratic forms in [\[section:QuadForms\]](#section:QuadForms){reference-type="ref" reference="section:QuadForms"}; this has been exploited by the third author in [@CZMTF; @CZMORD].

[^1]: In its original form, Adams lemma [@Adams; @MarotteZhang; @LDVS] says that, for any analytic $q$-difference operator, the power series appearing in the solutions related to the *biggest* slope have a strictly positive radius of convergence: see for instance the $q$-Euler equation in paragraph [\[subsection:qEuler\]](#subsection:qEuler){reference-type="ref" reference="subsection:qEuler"}. Adams lemma was used implicitly in paragraph [\[subsection:slopefiltration\]](#subsection:slopefiltration){reference-type="ref" reference="subsection:slopefiltration"} through its consequences: existence of an analytic factorisation and definition of the slope filtration.

[^2]: This was of course well known to Stokes himself when he studied the Airy equation, as well as to all those who used divergent series in numerical computations of celestial mechanics, leading to Poincaré work on asymptotics. But, of course, one should above all remember Euler, who used divergent series for numerically computing $\zeta(2) = \pi^{2}/6$, in flat contradiction to the opinion expressed by Bourbaki in "Topologie Générale", IV, p. 71.

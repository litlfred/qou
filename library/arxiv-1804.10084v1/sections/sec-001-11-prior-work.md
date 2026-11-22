---
doc_id: arxiv-1804.10084v1
doc_title: "Concentration of Lipschitz Functions of Negatively Dependent Variables"
section_id: sec-001-11-prior-work
section_title: "Prior work"
section_number: 1.1
pages: 1-2
source_pdf: 1804.10084v1.pdf
source_sha256: 716da9708f06d930
toc_source: outline
text_source: latex
latex_prose_ratio: 0.91
latex_coverage_ratio: 0.965
doc_brief: "Concentration of Lipschitz Functions of Negatively Dependent Variables — We explore the question whether Lipschitz functions of random variables under various forms of negative correlation satisfy"
---
Negatively dependent random variables arise naturally in scenarios motivated by statistical physics as well as computer science. Newman studied the asymptotic behavior of ensembles of random variables under a certain notion of negative dependence, and proved a central limit theorem in this setting [@Newman84]. Panconesi and Srinivasan [@PancoSrini97] proved that random variables under the condition of *negative cylinder dependence* (see Section [\[sec:neg-dep\]](#sec:neg-dep){reference-type="ref" reference="sec:neg-dep"} for definitions) satisfy Chernoff-Hoeffding concentration bounds, just like independent random variables. It was shown that negative cylinder dependence is exhibited by random variables arising in various randomized rounding scenarios which led to several applications [@PancoSrini97; @GKPS06; @AgeevS04; @CVZ10]. We note that from the point of view of this paper, these concentration results are somewhat special as they only apply to *linear* functions of negatively dependent variables.

The notion of negative dependence was studied systematically by Pemantle [@Pemantle00] who proposed several alternative notions of negative dependence and investigated their relative merits and relationships. In particular, he posed the question whether there is a robust notion of negative dependence, closed under natural operations, and allowing one to replicate some of the theory enjoyed by independent random variables or positively dependent variables (such as the FKG inequality).

Meanwhile, Dubhashi and Ranjan [@DubhashiRanjan98] studied in depth the scenario of *balls and bins*, and proved that the respective random variables satisfy several notions of negative dependence. Among other results, they stated a concentration bound for any Lipschitz function of random variables satisfying the property of *negative regression*. This was a rare example of a concentration inequality for non-linear functions of negatively dependent variables that can be found in the literature --- unfortunately, it turns out that their proof was erroneous (see Appendix [\[app:error\]](#app:error){reference-type="ref" reference="app:error"} for details). Later, Farcomeni [@Farcomeni08] studied concentration bounds under a weaker notion of negative dependence (which reduces to negative cylinder dependence in the case of $\{0,1\}$ random variables) and claimed a concentration inequality for Lipschitz functions of such variables. Unfortunately, his proof again turned out to be incorrect, as reported by [@PemPeres14]. In that work, Pemantle and Peres [@PemPeres14] proved a concentration bound for Lipschitz functions under *strong Rayleigh measures*, a strong notion of negative dependence which implies all the other notions discussed in this paper. Their proof relies on the theory of stable polynomials [@BBL09].

Let us mention that special-purpose tail inequalities have been proved for submodular functions and matrix norms under a particular randomized rounding scheme on matroid polytopes [@CVZ09; @HarveyOlver14]. While this is a natural setting where negatively dependent variables arise, it is not known how to generalize these concentration bounds to any general notion of negative dependence.

#### Organization.

In Section [\[sec:neg-dep\]](#sec:neg-dep){reference-type="ref" reference="sec:neg-dep"}, we survey several notions of negative dependence and their relationships. In Section [\[sec:neg-reg-result\]](#sec:neg-reg-result){reference-type="ref" reference="sec:neg-reg-result"}, we provide a corrected proof of the concentration bound for Lipschitz functions of random variables under the assumption of negative regression. This is the main contribution of this paper.

In Appendix [\[app:error\]](#app:error){reference-type="ref" reference="app:error"}, we explain where the proof of [@DubhashiRanjan98] fails and discuss a counterexample that motivated our proof.

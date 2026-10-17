---
doc_id: arxiv-1804.10084v1
doc_title: "Concentration of Lipschitz Functions of Negatively Dependent Variables"
section_id: sec-005-4-discussion-and-conclusion
section_title: "Discussion and conclusion"
section_number: 4
pages: 8-9
source_pdf: 1804.10084v1.pdf
source_sha256: 716da9708f06d930
toc_source: outline
text_source: latex
latex_prose_ratio: 0.984
latex_coverage_ratio: 0.525
doc_brief: "Concentration of Lipschitz Functions of Negatively Dependent Variables — We explore the question whether Lipschitz functions of random variables under various forms of negative correlation satisfy"
---
Let us discuss briefly the notion of negative regression and how it relates to other notions of negative dependence. It is fair to say that most known examples that satisfy negative association or negative regression actually satisfy the strong Rayleigh property as well. For example, random variables arising in the context of random spanning trees, determinantal point processes and exclusion dynamics processes are in this category. However, there are ensembles of random variables satisfying negative regression and not stronger notions of negative dependence. We want to mention a few examples here.

#### Random variables conditioned on their sum.

It is known that if $X_1,\ldots,X_n$ are independent, then the probability measure of $(X_1,\ldots,X_n)$ conditioned on $\sum_{i=1}^{n} X_i = k$ is strongly Rayleigh, for any fixed $k$. The probability measure conditioned on $\sum_{i=1}^{n} X_i \in \{ k, k+1 \}$ is still strongly Rayleigh. Conditioning on $\sum_{i=1}^{n} X_i \in [a,b]$ does not preserve the strong Rayleigh condition in general [@BBL09]. However, such ensembles still satisfy negative regression [@Pemantle00]. More generally, ensembles produced from independent random variables by taking products, "external fields\" and "rank rescaling\" satisfy negative regression; we refer the reader to [@Pemantle00] for a precise statement and proof.

#### Variables of large influence.

As we remarked, [@PemPeres14] also handles the case of random variables satisfying the stochastic covering property and homogeneity, i.e. the condition $\sum_{i=1}^{n} X_i = k$. The case of conditioning on $\sum_{i=1}^{n} X_i \in [a,b]$ is not covered by their theorem, although we believe that their method would still apply. However, what seems significantly beyond the scope of stochastic covering is the case of random variables where one variable can have a large effect on the remaining variables. (Under stochastic covering, conditioning on one variable can change the expected sum of the remaining variables by at most $1$.) An example of such a measure is our counterexample in Appendix [\[app:error\]](#app:error){reference-type="ref" reference="app:error"}; this counterexample illustrates what the issue was in the previously claimed proof, and also this is the main hurdle that our proof had to overcome.

 

The main question that this paper leaves open is whether similar concentration bounds still hold for Lipschitz functions of negatively associated variables.

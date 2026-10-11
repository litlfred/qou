---
doc_id: arxiv-1712.03058v3
doc_title: "Iterated filtering methods for Markov process epidemic models Theresa Stocks1 1Department of Mathematics, Stockholm University, Sweden This manuscript is a preprint of a Chapter to"
section_id: sec-009-151-the-problem-of-interest
section_title: "The problem of interest"
section_number: 1.5.1
pages: 12-12
source_pdf: 1712.03058v3.pdf
source_sha256: ba48c5bbb2467374
doc_brief: "Iterated filtering methods for Markov process epidemic models Theresa Stocks1 1Department of Mathematics, Stockholm University, Sweden This manuscript is a preprint of a Chapter to appear in the Handb"
text_source: latex
latex_prose_ratio: 0.971
latex_coverage_ratio: 0.991
---
Typical infectious disease data collected by public health authorities often consists of reported incidences in given time periods. Other important characteristics of an epidemic such as recovery times of the individual or contact network are not observed. The method presented is a useful tool to analyze routinely collected surveillance data because it gives insights into the mechanism of disease spread which is crucial if one wants to e.g. assess the risk of emerging pathogens or evaluate the impact of control measures such as vaccination.\
In this section we describe how to carry out inference for the parameters of a POMP where the underlying disease transmission model is assumed to be a simple Markovian SIR model, given that we observe the number of newly reported cases aggregated by week. We use the algorithm presented in Section [\[iterated_filtering\]](#iterated_filtering){reference-type="ref" reference="iterated_filtering"} for a simulated data set and illustrate how the algorithm performs.\
In order to keep things simple, in the specific example of this section, we assume that the time of reporting coincides with the time of infection. Of course, this assumption does not hold for all diseases but the method presented here can be easily adopted to other settings, e.g. when the time of reporting coincides with the time of removal.\
The implementation of the following example is made available at [@theresa_git].

---
doc_id: arxiv-1712.03058v3
doc_title: "Iterated ﬁltering methods for Markov process epidemic models"
section_id: sec-002-12-likelihood-based-inference
section_title: "Likelihood-based inference"
section_number: 1.2
pages: 3-3
source_pdf: 1712.03058v3.pdf
source_sha256: ba48c5bbb2467374
toc_source: outline
doc_brief: "Iterated ﬁltering methods for Markov process epidemic models — Dynamic epidemic models have proven valuable for public health decision makers as they provide useful insights into the understanding"
---
Section 1.3 we introduce the model class of partially observed Markov pro-
cesses and explain how to formulate and evaluate the likelihood of such
models with particle ﬁlters.
In Section 1.4 we present the iterated ﬁlter-
ing algorithm and demonstrate its use by a simple example in Section 1.5.
In Section 1.6 we discuss possible extensions of this example and, in Sec-
tion 1.7, illustrate how the method can be applied to a real-world problem
which accommodates most of the complications mentioned. Both examples
are accompanied by source code and instructions which can be found online
at Stocks (2017). We ﬁnish the chapter by outlining advantages and disad-
vantages of the method presented and point the interested reader to further
literature, see Section 1.8.
1.2
Likelihood-based inference
We start by outlining the key aspects of likelihood-based inference that will
be relevant to us. This is an extensive topic and for readers new to this
area we refer to e.g. Pawitan (2001) or Held and Sabanés Bové (2013) for a
comprehensive overview on likelihood-based inference.

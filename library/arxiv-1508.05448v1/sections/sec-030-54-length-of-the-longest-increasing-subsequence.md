---
doc_id: arxiv-1508.05448v1
doc_title: "Concentration of Measure Techniques and Applications"
section_id: sec-030-54-length-of-the-longest-increasing-subsequence
section_title: "Length of the Longest Increasing Subsequence"
section_number: 5.4
pages: 110-112
source_pdf: 1508.05448v1.pdf
source_sha256: 57d2c717d8ec74d0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.938
latex_coverage_ratio: 1.0
doc_brief: "Concentration of Measure Techniques and Applications — 36 sections: Front matter; Biographical Sketch; Acknowledgments"
---
Consider a permutation $\pi\in S_n$. An increasing subsequence $i_1,i_2,\dots,i_k$ of a permutation $i\mapsto \pi(i)$ is a subsequence such that $i_1<\dots<i_k$ and $\pi(i_1)<\pi(i_2)<\dots<\pi(i_k)$. We will be concerned with determining the length of the longest increasing subsequence in a given permutation. Denote the length of the longest increasing subsequence of $\pi$ by $\ell(\pi)$.

The following example is due to [@ADHamm]. Consider the permutation given by $$7\;\;\;2\;\;\;8\;\;\;1\;\;\;3\;\;\;4\;\;\;10\;\;\;6\;\;\;9\;\;\;5$$ where $\pi(1)=4$, $\pi(2)=2$, $\pi(3)=5$, etc. Then a longest increasing subsequence is given by $$1\;\;\;3\;\;\;4\;\;\;6\;\;\;9$$ In this case $\ell(\pi)=5$.\
Notice that the longest increasing subsequence is not necessarily unique. $$2\;\;\;3\;\;\;4\;\;\;6\;\;\;9$$ is also an increasing subsequence of length $5$. The longest increasing subsequence problem goes back to Ulam [@Ulam]. Ulam asked what is the distribution of the length of the longest monotone (increasing or decreasing) subsequence of a uniform random permutation. While we will not go into the history here, a detailed account of Ulam's problem and Monte Carlo methods can be found in [@Hammersley]. Quite a bit of progress has been made concerning the distribution of the length of the longest increasing subsequence, provided that the permutation is uniformly distributed. Hammersley [@Hammersley] showed that $\mathbb{E}\ell(\pi)\sim c\sqrt{n}$, where $n$ is the length of the permutation and $c$ is a constant. Vershik and Kerov [@VershikKerov] and Logan and Shepp [@LS] proved that the constant $c$ is equal to $2$. Their methods of proof relied on hard analysis of the asymptotics of Young tableau. Aldous and Diaconis [@AldousDiaconis] give an interacting particle process argument for $c=2$. In addition, Baik, Deift, and Johansson [@BDJ] showed that the fluctuations of the length of the longest increasing subsequence for a uniform permutation are Tracy-Widom, on the order of $n^{1/6}$. More specifically, they show that $$\frac{\ell_n-2\sqrt{n}}{n^{1/6}}\xrightarrow{d} \chi$$ where $\chi$ is a random variable with Tracy Widom distribution. The distribution function for the Tracy Widom distribution is $$F(t)=\exp\left(-\int_t^{\infty}(x-t)u^2(x)dx\right)$$ where $u(x)$ is the solution of the Painlevé equation $$u_{xx}=2u^3+xu$$ See [@BDJ] for more background on the Tracy Widom distribution.

Much less is known about the distribution of the length of the longest increasing subsequence of a random permutation distributed according to the Mallows measure. In [@MS], Mueller and Starr proved a weak law of large numbers result analogous to the Vershik-Kerov and Logan-Shepp results for the uniform case. To continue this work, we would like to bound the fluctuations of the length of the longest increasing subsequence of a Mallows permutation. As a first step in this direction, we use the modified Fisher-Yates algorithm to generate a random Mallows permutation, then use an algorithm called patience sorting to compute the length of the longest increasing subsequence of the generated permutation.

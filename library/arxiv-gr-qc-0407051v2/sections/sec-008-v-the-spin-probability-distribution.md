---
doc_id: arxiv-gr-qc-0407051v2
doc_title: "Black hole entropy from Quantum Geometry"
section_id: sec-008-v-the-spin-probability-distribution
section_title: "THE SPIN PROBABILITY DISTRIBUTION"
section_number: V
pages: 12-14
source_pdf: 0407051v2.pdf
source_sha256: 2de07e909b17c5a5
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 1.0
doc_brief: "Black hole entropy from Quantum Geometry — Quantum Geometry (the modern Loop Quantum Gravity using gra phs and spin-networks instead of the loops) provides microscopic d egrees of freedom that"
---
Given any value $a$ of the classical horizon area, and the $N(a)$ quantum states of the horizon labeled by all the finite sequences $(m_1,...,m_n)$ of the non-zero half-integers such that ([\[N(a)\]](#N(a)){reference-type="ref" reference="N(a)"}) one can fix any arbitrary $$\begin{equation}
0\not=m\in\frac{1}{2}{\mathbb{Z}}
\end{equation}$$ and consider the subset of states corresponding to the sequences such that $$\begin{equation}
m_1=m .
\end{equation}$$ Denote the number of the elements of this subset by $N_{(a)}(m)$. The ratio $$\begin{equation}
P_{(a)}(m)\ :=\ \frac{N_{(a)}(m)}{N(a)}
\end{equation}$$ can be considered as the probability that the first puncture is labeled by $m_1=m$. The question is, what $P_{(a)}(m)$ is when $a$ is large compared to the minimal area $a_m$ created at the puncture[^1], $$\begin{equation}
a_m\ =\ 8\pi\gamma{\ell}_{\rm Pl}^2\sqrt{|m|(|m|+1)}.
\end{equation}$$ (Notice, that the answer could make no probabilistic sense, if the $\lim_{a\rightarrow \infty}P_{(a)}(m)$ were $0$ for all the values of $m$, for example.) The number $N_{(a)}(m)$ defined above can be also thought of as a number of all the finite sequences $(m_2,...,m_n)$ such that $$\begin{equation}
\sum_{i=2}^nm_i\ =\ -m,\ \ \ \ \sum_{i=2}^n\sqrt{|m_i|(|m_i|+1)}\ \le\
\frac{a-a_m}{8\pi\gamma{\ell}_{\rm Pl}^2}.\label{Na(m)}
\end{equation}$$ By the same randon walk argument as the one used above in the treatment of the number ${N'}^-_k$ (as before, see [@meis] for a proof) we have $$\begin{equation}
N_{(a)}(m) \ =\ e^{-\frac{m^2}{a-a_m}}N(a-a_m) + ...
\end{equation}$$ where the other terms can be neglected when we go to the limit $a\rightarrow\infty$. Since the number $N(a)$ is given by exponentiating ([\[me\]](#me){reference-type="ref" reference="me"}), we can see that in the limit $a\rightarrow \infty$ $$\begin{equation}
P_{(a)}(m)\ \rightarrow\ e^{-2\pi\gamma_{\rm M}\sqrt{|m|(|m|+1)}}\ =: P(m).
\end{equation}$$ Now, the equality ([\[g\]](#g){reference-type="ref" reference="g"}) means that the limits $P(m)$ of the probabilities still sum to $1$, $$\begin{equation}
\sum_{0\not=m\in\frac{1}{2}{\mathbb{Z}}}P(m)\ =\ 1.
\end{equation}$$

That (limit) probability distribution $P(m)$ can also be written in terms of the entropy $S(a_m)$ corresponding to the area $a_m$, namely $$\begin{equation}
P(m)\ =\  e^{-S(a_m)},
\end{equation}$$ regardless of whether we fix the value of $\gamma$ by the agreement with the Bekenstein-Hawking entropy or not.

**Acknowledgments** We benefited a lot from the discussions with Abhay Ashtekar, John Baez, Alejandro Corichi, Kirill Krasnov and Marek Napiórkowski. Krzysztof Meissner, the referee of the diploma thesis of one us (MD), helped us to understand the relevance and irrelevance of the constraint on the quantum excitations of the C-S field. JL was partially supported by Polish Committee for Scientific Research (KBN) under grant number 2P03B 12724.

[^1]: This issue has been raised recently by John Baez.

---
doc_id: arxiv-gr-qc-0407051v2
doc_title: "Black hole entropy from Quantum Geometry"
section_id: sec-007-iv-the-entropy-calcula-tions
section_title: "THE ENTROPY CALCULA TIONS"
section_number: IV
pages: 9-12
source_pdf: 0407051v2.pdf
source_sha256: 2de07e909b17c5a5
text_source: latex
latex_prose_ratio: 0.98
latex_coverage_ratio: 0.995
doc_brief: "Black hole entropy from Quantum Geometry — Quantum Geometry (the modern Loop Quantum Gravity using gra phs and spin-networks instead of the loops) provides microscopic d egrees of freedom that"
---
To find an upper bound for the number $N(a)$ introduced in the previous section (recall that $a=4\pi\gamma{\ell}_{\rm Pl}^2k$, and $k\in {\mathbb{N}}$), consider the set $M^+_k$ of all the finite sequences $(m_1,...,m_n)$ of non-zero elements of $\frac{1}{2}{\mathbb{Z}}$ which satisfy the inequality in ([\[mzero\]](#mzero){reference-type="ref" reference="mzero"}), but do not necessarily sum to zero,that is, $$\begin{equation}
M^+_k\ :=\ \{ (m_1,...,m_n)\ \Big|\ n\in{\mathbb{N}},\
0\not=m_1,...,m_n\in\frac{1}{2}{\mathbb{Z}},\
\sum_{i=1}^n |m_i|\ \le\ \frac{k}{2}\}\,.
\end{equation}$$ Let $N^+_k$ be the number of elements of $M^+_k$ plus $1$ (the empty sequence). Certainly, $$\begin{equation}
N(a)\ \le\ N^+_k
\end{equation}$$ Next, since $k$ is arbitrarily fixed integer, let it become a variable of the sequence $(N^+_0,N^+_1,...,N^+_k,...)$. To establish a recurrence relation satisfied by the sequence $(N^+_0,N^+_1,...,N^+_k,...)$, notice that if $(m_1,...,m_n)\in M^+_{k-1}$, then both $(m_1,...,m_n,\frac{1}{2}),\
(m_1,...,m_n,
-\frac{1}{2})\in M^+_{k}$. In the same way, for arbitrary natural $0<l\le k$, $$\begin{equation}
(m_1,...,m_n)\in M^+_{k-l}\ \Rightarrow\ (m_1,...,m_n,\pm\frac{1}{2}l)
\in M^+_k.
\end{equation}$$ Obviously, if we consider all $0<l\le k$, and all the sequences $(m_1,...,m_n)\in  M^+_{k-l}$, then the resulting $(m_1,...,m_n,\pm\frac{1}{2}l)$ form the entire set $M^+_k$. Also, for two different $l\not= l'$, $$\begin{equation}
(m_1,...,m_n,\pm\frac{1}{2}l)\ \not=\ (m_1,...,m_n,\pm\frac{1}{2}l').
\end{equation}$$ This proves the following recurrence relation, $$\begin{equation}
N^+_k\ =\ 2N^+_{k-1} + ... + 2N^+_0 + 1.\label{rec+}
\end{equation}$$ The (unique) solution is $$\begin{equation}
N^+_k\ =\ 3^k.
\end{equation}$$ In conclusion, $$\begin{equation}
N(a) \le 3^k\, .\label{N+}
\end{equation}$$

To find a lower bound for $N(a)$, we use the inequality $$\begin{equation}
\sqrt{|m_i|(|m_i|+1)}\ \le\ |m_i|+\frac{1}{2},
\end{equation}$$ and consider the number $N^-_k$ equal to $1$ plus the number of elements in the set $$\begin{equation}
M^-_k\ :=\ \{ (m_1,...,m_n)\ \Big|\ n\in{\mathbb{N}},\
0\not=m_1,...,m_n\in\frac{1}{2}{\mathbb{Z}},\
\sum_{i=1}^n (|m_i|+\frac{1}{2})\ \le\ \frac{k}{2}\}\,
\end{equation}$$ Notice that this time, ignoring the constraint that the elements $m_i$ of each sequence sum to zero ([\[mzero\]](#mzero){reference-type="ref" reference="mzero"}) makes an in-equivalence relation between $N(a)$ and $N^-_k$ a priori not known. But let us postpone this problem for a moment. Using the same construction as above, we find the recurrence relation satisfied by $N^-_k$, $$\begin{equation}
N^-_k\ =\ 2N^-_{k-2}+...+2N^-_0 + 1.\label{rec-}
\end{equation}$$ The unique solution is $$\begin{equation}
N^-_k\ =\ \frac{2}{3}2^k + \frac{(-1)^k}{3}\, .\label{N-}
\end{equation}$$ A lower bound for $N(a)$ is the number ${N'}^-_k$ of the elements of $M^-_k$ which additionally satisfy $m_1+...+m_n=0$, $$\begin{equation}
{N'}^-_k \ \le N(a).
\end{equation}$$ A statistical physics argument giving the value of the desired number ${N'}^-_k$ is as follows (this argument is due to Meissner, who also provided an exact proof in [@meis]). We can think of each sequence $(m_1,...,m_n)$ as of a sequence of random steps on a line. The total length of each path is bounded by $k$ owing to the inequality in the definition of the set $M^-_k$. The number of sequences in $M^-_k$ of a given, fixed value of the sum $$\begin{equation}
m_1+...+m_n = \delta
\end{equation}$$ depends on $\delta$. The average value of $\delta$ is $\bar{\delta}=0$. For large values of $k$, the number of the paths corresponding to the random walk distance $\delta$ should be given by the Gaussian function $\frac{C}{\sqrt{k}} e^{-\frac{\delta^2}{\beta k}}\, \ \, N^-_k$. In particular, the value $$\begin{equation}
{N'}^-_k\ = \frac{C}{\sqrt{k}}N^-_k
\end{equation}$$ corresponds to $\delta=0$.

Summarizing, $$\begin{equation}
\frac{C}{\sqrt{k}}N^-_k\ \le\ N(a)\le N^+_k,
\end{equation}$$ where the numbers $N^-_k$ and $N^+_k$ were calculated in ([\[N+\]](#N+){reference-type="ref" reference="N+"},  [\[N-\]](#N-){reference-type="ref" reference="N-"}). Therefore the entropy is bounded in the following way $$\begin{equation}
\frac{\ln 2}{4\pi\gamma{\ell}_{\rm Pl}^2}a + o({a}) \le  S(a) \le
\frac{\ln 3}{4\pi\gamma{\ell}_{\rm Pl}^2}a. \label{entroest}
\end{equation}$$

We are in a position now, to compare our results with those of [@abk]. The mistake made in [@abk] in the combinatorial formulation (see (44) in that paper) is an assumption, that one can order the $j_i$ labels in ([\[phys\]](#phys){reference-type="ref" reference="phys"}) such that $j_1\le ...
\le j_n$, and impose this as a constraint on 'admissible' states we count. As a consequence, the number of the states contributing to the entropy was underestimated: the analysis of [@abk] implied that for large $a$ the leading contribution to the number of sequences comes only from the sequences $(m_1,...,m_n)=(\pm
\frac{1}{2},...,\pm \frac{1}{2})$. The resulting number $S_{\rm
ABCK}(a)$ proposed for the value of the entropy was $$\begin{equation}
S_{\rm ABCK}(a)\ =\ \frac{\ln 2}{4\pi\sqrt{3}\gamma{\ell}_{\rm Pl}^2}a + O(a).
\label{entropyabk}
\end{equation}$$ The comparison with our ([\[entroest\]](#entroest){reference-type="ref" reference="entroest"}) shows that *the contribution from the higher half integers $|m_i|>\frac{1}{2}$ can not be neglected.*

The next consequence of the estimate ([\[entroest\]](#entroest){reference-type="ref" reference="entroest"}) is a necessary condition for the agreement of the entropy $S(a)$ with the Bekenstein-Hawking entropy $a\,/\,4{\ell}_{\rm Pl}^2$; the condition is that the value of the Barbero-Immirzi parameter $\gamma$ is bounded in the following way, $$\begin{equation}
\frac{\ln 2}{\pi}\ \le\ \gamma\ \le \frac{\ln 3}{\pi}.\label{gammabound}
\end{equation}$$ On the other hand, the value proposed for the Barbero-Immirzi parameter by counting the sequences $(\pm 1/2,...,\pm 1/2)$ was $$\begin{equation}
\gamma_{\rm ABCK} \ =\ \frac{\ln 2}{\pi\sqrt{3}}.\label{gammaabk1}
\end{equation}$$

In the accompanying paper [@meis] the recurrence relations ([\[rec-\]](#rec-){reference-type="ref" reference="rec-"},[\[rec+\]](#rec+){reference-type="ref" reference="rec+"}) are generalized to an appropriate generalized recurrence relation satisfied by the desired number $N(a)$ itself. Next, the combinatorial problem formulated in the previous section is solved completely. The method is remarkably powerful. The result of [@meis] is $$\begin{equation}
S(a)\ =\ \frac{\gamma_{\rm M}}{\gamma}\frac{a}{4{\ell}_{\rm Pl}^2} - \frac{1}{2}\ln a + O(1), \label{me}
\end{equation}$$ where $\gamma_{\rm M}$ is a constant defined by the following equation $$\begin{equation}
\frac{1}{2}-\sum_{0\not=j\in\frac{1}{2}{\mathbb{N}}}
e^{-2\pi\gamma_{\rm M}\sqrt{j(j+1)}}=0.  \label{g}
\end{equation}$$ The numerical value of $\gamma_{\rm M}$ is calculated in [@meis].

An interesting historical remark is (it has been unraveled to us recently, after our results were derived) that before coming to their final result ([\[entropyabk\]](#entropyabk){reference-type="ref" reference="entropyabk"}, [\[gammaabk1\]](#gammaabk1){reference-type="ref" reference="gammaabk1"}), Ashtekar, Baez and Krasnov had established certain estimate. The inequality had been $$\begin{equation}
S_{\rm bh}(a)\ \le\  \ \frac{\gamma_0}{\gamma}\frac{a}{4{\ell}_{\rm Pl}^2} + O({a})
\end{equation}$$ where the constant $\gamma_0$ had been defined by the same equation as as $\gamma_{\rm M}$ above. But since this result emerged as an upper bound only, finally it was replaced by the improper one ([\[entropyabk\]](#entropyabk){reference-type="ref" reference="entropyabk"},[\[gammaabk1\]](#gammaabk1){reference-type="ref" reference="gammaabk1"}).

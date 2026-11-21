---
doc_id: arxiv-gr-qc-0407051v2
doc_title: "Black hole entropy from quantum geometry"
section_id: sec-002-3-the-combinatoric-formulation-of-the-problem
section_title: "The combinatoric formulation of the problem"
section_number: 3
pages: 7-9
source_pdf: 0407051v2.pdf
source_sha256: 2de07e909b17c5a5
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.964
latex_coverage_ratio: 1.0
doc_brief: "Black hole entropy from quantum geometry — Quantum Geometry (the modern Loop Quantum Gravity using graphs and spin-networks instead of the loops) provides microscopic degrees of freedom that account"
---
From now our treatment starts to differ from that of [@abk]. Our aim is to define the number of the quantum states of the horizon which contribute to the entropy in a form of a clear and precise combinatoric formula.

Recall that the classical area $a$ of the horizon is fixed as $$a\ =\ 4\pi\gamma{\ell}_{\rm Pl}^2 k,\ \ \ k\in {\mathbb{N}}.$$ Calculation of the horizon entropy consists in counting those quantum horizon states, elements of the Hilbert space ${\cal H}_{S,{\rm phys}}$ ([\[Sphys\]](#Sphys){reference-type="ref" reference="Sphys"}) labeled by the finite sequences defined in ([\[phi\]](#phi){reference-type="ref" reference="phi"}) (the number $n$ of the entries can be arbitrary) which correspond to subspaces ${\cal H}^{b(m),j,m}$ in ([\[phys\]](#phys){reference-type="ref" reference="phys"}) such that the area operator eigenvalue $a_S^j$ satisfies the following inequality[^1] $$a_S^j\ =\ 8\pi\gamma{\ell}_{\rm Pl}^2\sum_{i=1}^n\sqrt{j_i(j_i+1)}\ \le\ a.\label{main}$$ Combinatorially, the task amounts to counting the finite sequences $(b_1,...,b_n)$ of elements of ${\mathbb{Z}}_k$, such that the following two conditions $(i)$ and $(ii)$ are satisfied: $$(i)\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \sum_{i=1}^nb_i=0\, , \label{phi2}$$ $(ii)$ there exist two sequences: a sequence $(j_1,...,j_n)$ consisting of non-zero elements of $\frac{1}{2} {\mathbb{N}}$ which satisfies the inequality ([\[main\]](#main){reference-type="ref" reference="main"}), and a sequence $(m_1,...,m_n)$ such that $$\begin{aligned}
b_i &=& -2 m_i\ \ {\rm mod}\ \  k\, ,\ \label{phim}\\
\ \ {\rm and}\ \ m_i\ &\in&\ \{-j_i,-j_i+1,...,j_i\}\, ,\label{mj}
\end{aligned}$$ for every $i=1,,,n$.

This recipe can be simplified. It is easy to eliminate the $j_i$'s by noting that, given a sequence $(m_1,...,m_n)$, there is a sequence $(j_1,...,j_n)$ such that ([\[mj\]](#mj){reference-type="ref" reference="mj"}) and ([\[main\]](#main){reference-type="ref" reference="main"}) if and only if $$8\pi\gamma{\ell}_{\rm Pl}^2\sum_{i=1}^n\sqrt{|m_i|(|m_i|+1)}\ \le\ a.$$ Next, it follows from ([\[phi2\]](#phi2){reference-type="ref" reference="phi2"}, [\[phim\]](#phim){reference-type="ref" reference="phim"}) that $$\sum_{i=1}^n m_i\ =\ n'\frac{k}{2}\, ,$$ with some $n'\in {\mathbb{Z}}$. But then, $$\begin{aligned}
a\ =\ 4\pi\gamma{\ell}_{\rm Pl}^2k\ &\ge&\ 8\pi\gamma{\ell}_{\rm Pl}^2\sum_{i=1}^n
\sqrt{|m_i|(|m_i|+1)}>\\
   &>& 8\pi\gamma{\ell}_{\rm Pl}^2\sum_{i=1}^n|m_i|\ \ge\
8\pi\gamma{\ell}_{\rm Pl}^2|\sum_{i=1}^nm_i|\ =\ \\
\ &=&\ 4\pi\gamma{\ell}_{\rm Pl}^2k|n'|.
\end{aligned}$$ Hence $$\sum_{i=1}^nm_i=0, \ \ {\rm and\ \ also}\ \ \ \sum_{i=1}^n|m_i|\le\frac{k}{2}\, .
\label{mzero}$$ Finally, notice that given a sequence $(b_1,...,b_n)$ of elements of ${\mathbb{Z}}_k$ there is exactly one sequence $(m_1,...,m_n)$ of elements of $\frac{1}{2}{\mathbb{Z}}$ such that ([\[phim\]](#phim){reference-type="ref" reference="phim"}) and ([\[mzero\]](#mzero){reference-type="ref" reference="mzero"}) holds. In this way, we have derived the following formula for the entropy counting:

*The entropy $S$ of a quantum horizon of the classical area $a$ according to Quantum Geometry and the Ashtekar-Baez-Corichi-Krasnov [@abk] framework is $$S \ =\ \ln N(a),$$ where $N(a)$ is $1$ plus the number of all the finite sequences $(m_1,....,m_n)$ of non-zero elements of $\frac{1}{2}{\mathbb{Z}}$, such that the following equality and inequality are satisfied: $$\sum_{i=1}^nm_i\ =\ 0,\ \ \ \ \sum_{i=1}^n\sqrt{|m_i|(|m_i|+1)}\ \le\
\frac{a}{8\pi\gamma{\ell}_{\rm Pl}^2},\label{N(a)}$$ where $\gamma$ is the Barbero-Immirzi parameter of Quantum Geometry.*

The extra term $1$ above comes from the trivial sequence.

[^1]: Assuming just inequality instead of considering an interval $[a-\delta a,a+\delta a]$ simplifies the calculation. Knowing the result for all $a$ one can always consider the interval. The result, at least in our case, is the same.

---
doc_id: arxiv-2302.05903v2
doc_title: "On combinatorial generalization(s) of Borel transform: Averaging method in combinatorics of symmetric polynomials"
section_id: sec-003-derivation-of-various-sum-formulas-by-the-averag
section_title: "Derivation of various sum formulas by the averaging method"
section_number: null
pages: 4-5
source_pdf: 2302.05903v2.pdf
source_sha256: 9a17abd36cc8a317
toc_source: outline
text_source: latex
latex_prose_ratio: 0.971
latex_coverage_ratio: 0.952
doc_brief: "On combinatorial generalization(s) of Borel transform: Averaging method in combinatorics of symmetric polynomials — We elaborate on the recent suggestion to consider averaging of Cauchy identities"
---
The averaging method can be easily modified to handle more examples. Say, we can ask the average $\left<S_R\right>=1$ only for *even* diagrams $R$, i.e. with all rows of even lengths, and vanishes otherwise. The corresponding measure is still Gaussian, $$\begin{aligned}
\text{\bf Measure B}: \ \ \ \ \ \ \ \ \ \ \
\left\{\begin{array}{ccc}\left<S_R\right>^{\bf\!B}=1 && {\rm for\ even}\ R  \\
\left<S_R\right>^{\bf\!B}=0 && {\rm otherwise} \end{array} \right. :  \ \ \ \ \ \ \ \
d\mu^{\bf\!B} \sim \prod_{k=1}^\infty dp_k \exp\left(-\frac{p_{2k-1}^2}{2(2k-1)} - \frac{(p_{2k}-1)^2}{4k}\right)
\end{aligned}$$ and the counterpart of ([\[idlinSchur\]](#idlinSchur){reference-type="ref" reference="idlinSchur"}) is $$\begin{aligned}
\sum_{R\ even}S_R
= \sum_R S_R\underbrace{\left<S_R\right>^{\bf\!B}}_{\delta_{R,{\rm even}}}
= \left<e^{\sum_{k=1}^\infty \frac{p_k\bar p_k}{k}}\right>^{\bf\!B}_{\bar p}
= \prod_{k=1}^\infty \exp\left({p_k^2\over 2k}+{p_{2k}\over 2k}\right)
\end{aligned}$$ Let us demonstrate how to prove that $\left<S_R\right>^{\bf\!B}$ is non-zero and equal to 1 only for even partitions. To this end, we note that the measure ${\bf\!B}$ is obtained from ${\bf\!A}$ by the shift of times $p_k\to p_k-(-1)^k$. In other words, we have $$\begin{aligned}
\left<S_R\{p_k\}\right>^{\bf\!B}=\left<S_R\{p_k+(-1)^k\}\right>^{\bf\!A}=\sum_P
S_{R/P}\{(-1)^k\}\left<S_R\{p_k\}\right>^{\bf\!A}\stackrel{[8]}{=}\sum_P S_{R/P}\{(-1)^k\}=\sum_P
(-1)^{|R|+|P|}S_{R/P}\{1\}
\end{aligned}$$ The choice of $p_k=1$ is equivalent to choosing only one non-zero symmetric variable $x_1=1$, and the sum $\sum_P(-1)^{|P|}S_{R/P}\{1\}$ is not zero only when $R$ is an even partition, which follows from the representation of the skew Schur function $S_{R/P}=\sum_Tx^T$ with the sum running over all tableaux $T$ of shape $R-P$, see details in [@Mac Eq.(5.12)].

All further examples in this section are proved analogously. Note that **checking** this kind of claims is much easier than proving them: one can just calculate simple Gaussian averages of the Schur functions at any concrete example.

Now, in order to pick up only even *columns*, one need to make transposition, which is equivalent to changing signs of all the time variables: the relevant measure, which gives $\left<S_R\right>=1$ for all even-column diagrams and zero otherwise is $$\begin{aligned}
\text{\bf Measure C:} \ \ \ \ \ \ \ \
\left\{\begin{array}{ccc}\left<S_R\right>^{\!C}=1 && {\rm for\ even} \ R^\vee  \\
\left<S_R\right>^{\!C}=0 && {\rm otherwise} \end{array} \right. :  \ \ \ \ \ \ \ \ \ \ \
d\mu^{\bf\!C} \sim \prod_{k=1}^\infty dp_k\exp\left(-\frac{p_{2k-1}^2}{2(2k-1)} - \frac{(p_{2k}+1)^2}{4k}\right)
\end{aligned}$$ and $$\begin{aligned}
\sum_{R^\vee\ even}S_R =  \sum_R S_R\underbrace{\left<S_R\right>^{\bf\!C}}_{\delta_{R^\vee,{\rm even}}}
= \left<e^{\sum_{k=1}^\infty \frac{p_k\bar p_k}{k}}\right>^{\bf\!C}_{\bar p}
= \prod_{k=1}^\infty  \exp\left({p_k^2\over 2k}-{p_{2k}\over 2k}\right)
\end{aligned}$$ Likewise the average with $\left<S_R\right>^{\bf \!D} = (-1)^{\nu_R}(-1)^{3|R|/2}$ with $\nu_R = \sum_{i=1}^{l_R} (i-1)R_i$ is provided by the Gaussian measure $$\begin{aligned}
\text{\bf Measure D:} \ \ \
\left<S_R\right>^{\bf \!D} = (-1)^{\nu_R}(-1)^{3|R|/2}: \ \ \ \
d\mu^{\bf\!D} \sim \prod_{k=1}^\infty \exp\left(-\frac{p_{k}^2}{2k} + (-1)^k\sqrt{-1}\frac{p_{2k-1}}{2k-1}
- \frac{p_{4k-2}}{2k-1}\right) dp_k
\label{muexpcaj}
\end{aligned}$$ Then $$\begin{aligned}
\sum_R (-1)^{\nu_R} S_R\{p\} = \sum_R (-1)^{|R|/2} S_R\{p\} \left<S_R\right>^{\bf\!D}
&=& \left<\exp\left(\sum_{k=1}^\infty(-1)^{k/2}\frac{ p_k\bar p_k}{k}\right)\right>^{\bf \!D}_{\!\!\bar p} =\nonumber\\
&=&\prod_{k=1}^\infty \exp\left(-\frac{p_{2k-1}^2}{2(2k-1)} + \frac{p_{2k}^2}{4k} + \frac{p_{2k-1}}{2k-1}
 + \frac{p_{4k-2}}{2k-1}\right)
\end{aligned}$$ If $c_R$ counts the number of rows of odd length in $R$, then, introducing a formal parameter $t$, $$\begin{aligned}
\text{\bf Measure E:} \ \ \ \ \
\left<S_R\right>^{\bf \!E} = t^{c_R}: \ \ \ \ \ \ \ \ \ \ \
d\mu^{\bf \!E} \sim \prod_{k=1}^\infty \exp\left(-\frac{(p_{2k-1}-t^{2k-1})^2}{2(2k-1)} -
\frac{(p_{2k}-1+t^{2k})^2}{4k}\right) dp_k
\end{aligned}$$ and $$\begin{aligned}
\sum_Rt^{c_R}S_R=\prod_i{1\over 1-tx_i}\prod_{i<j}{1\over 1-x_ix_j}
=\exp\left\{\sum_{k=1}^\infty\left({p_k^2\over 2k}+t^{2k-1}{p_{2k-1}\over 2k-1}+(t^{2k}-1){p_{2k}\over 2k}\right)\right\}
\end{aligned}$$ Counting the number of columns of odd length is provided by the same formula with all the signs of $p_k$ inverted, see ([\[1\]](#1){reference-type="ref" reference="1"}) below.

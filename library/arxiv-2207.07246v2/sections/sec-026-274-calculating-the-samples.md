---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-026-274-calculating-the-samples
section_title: "Calculating the Samples"
section_number: 2.7.4
pages: 57-59
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.928
latex_coverage_ratio: 0.939
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 73 sections: Front matter; ABSTRACT; ACKNOWLEDGEMENTS"
---
The reason to recast Eq.([\[PIMCopexpdetailshorttimeapprox\]](#PIMCopexpdetailshorttimeapprox){reference-type="ref" reference="PIMCopexpdetailshorttimeapprox"}) into the form of Eq.([\[OABP\]](#OABP){reference-type="ref" reference="OABP"}) is because once we have the detailed form of Eq.([\[PlrR\]](#PlrR){reference-type="ref" reference="PlrR"}), the normalized probability distribution $P_{lr}(\mathcal{R})$, we can sample it by using suitable algorithms. And then after we take enough uncorrelated samples of $A_{lr} (\mathcal{R})$ and $B_{lr}(\mathcal{R})$ in Eq.([\[OABP\]](#OABP){reference-type="ref" reference="OABP"}) from the probability distribution $P_{lr} (\mathcal{R})$ in Eq.([\[PlrR\]](#PlrR){reference-type="ref" reference="PlrR"}), we have the corresponding average values $\langle A \rangle$ for $A_{lr} (\mathcal{R})$ and $\langle B \rangle$ for $B_{lr}(\mathcal{R})$ and their errors $\sigma_A$ and $\sigma_B$, finally $\langle \hat{O} (\Delta \tau) \rangle$ and its error bar $\sigma$ can be estimated by, $$\begin{aligned}
\langle \hat{O} (\Delta \tau)\rangle =
\frac{\sum_l\sum_r \int d \mathcal{R} A_{lr} (\mathcal{R}) P_{lr} (\mathcal{R}) }{ \sum_l\sum_r \int d \mathcal{R} B_{lr} (\mathcal{R}) P_{lr} (\mathcal{R})  }
=\frac{\langle A_{lr}(\mathcal{R}) \rangle }{\langle B_{lr}(\mathcal{R}) \rangle}
\bigg|_{ \{l,r,\mathcal{R}\} \in P_{lr}(\mathcal{R})  }
= \frac{\langle A \rangle}{\langle B \rangle}
\label{OABPdtave}
\end{aligned}$$ $$\begin{aligned}
\sigma =
\sqrt{ \left[ \frac{\partial (\langle A \rangle / \langle B \rangle )}{ \partial \langle A \rangle } \sigma_A \right]^2
+ \left[ \frac{\partial (\langle A \rangle / \langle B \rangle )}{ \partial \langle B \rangle } \sigma_B \right]^2  }
=
\sqrt{ \left( \frac{\sigma_A}{\langle B\rangle} \right)^2 + \left(\frac{ \langle A \rangle \sigma_B }{ \langle B \rangle^2 } \right)^2    }.
\label{OABerror}
\end{aligned}$$

Alternatively, we can also find $\langle \hat{O} \rangle$ and its error bar $\sigma$ from the block average of $A$ and $B$. For example we can arrange all the $N$ samples of $A$ and $B$ into much smaller blocks. Each block contain $n$ samples of $A$ and $B$. So there are $n_b=N/n$ blocks. We can mark each of the block average as $\bar{A}_n$ and $\bar{B}_n$. And the average of block average is the average value, namely $$\begin{aligned}
\langle \bar{A}_n \rangle &= \langle A \rangle, \\
\langle \bar{B}_n \rangle &= \langle B \rangle.
\end{aligned}$$ The standard deviation of the $n_b$ samples of $\bar{A}_n$ and $\bar{B}_n$ are $\sigma_{A_n}$ and $\sigma_{B_n}$. According to central limit theorem ([@Negele1998Quantum; @VesaPDF]), the independent block averages of $\bar{A}_n$ and $\bar{B}_n$ each forms a gaussian distribution $P(\bar{A}_n)$ and $P(\bar{B}_n)$ with average value $\langle A \rangle$ and $\langle B \rangle$ and their corresponding standard deviations are $$\begin{aligned}
\sigma_{P_{\bar{A}_n}} &= \frac{\sigma_{\bar{A}_n}}{\sqrt{n_b}}, \\
\sigma_{P_{\bar{B}_n}} &= \frac{\sigma_{\bar{B}_n}}{\sqrt{n_b}}.
\end{aligned}$$ Then we find that, $$\begin{aligned}
\left\langle\frac{\bar{A}_n}{ \bar{B}_n }\right\rangle &=
\int d \bar{A}_n d \bar{B}_n \frac{\bar{A}_n}{\bar{B}_n}
P(\bar{A}_n) P(\bar{B}_n) \nonumber \\
&=
\int d \bar{A}_n \bar{A}_n P(\bar{A}_n)
\int d \bar{B}_n \frac{1}{\bar{B}_n} P(\bar{B}_n) \nonumber \\
&=\langle A   \rangle \int d \bar{B}_n \frac{1}{\bar{B}_n} P(\bar{B}_n).
\label{OABclt1}
\end{aligned}$$ Note that when $\sigma_{P_{B_n}}$ is small, the gaussian distribution $P(\bar{B}_n)$ becomes a $\delta$ function $\delta( \bar{B}_n -\langle B \rangle  )$, so Eq.([\[OABclt1\]](#OABclt1){reference-type="ref" reference="OABclt1"}) in this case becomes, $$\begin{aligned}
\left\langle\frac{\bar{A}_n}{ \bar{B}_n }\right\rangle &=
\langle A   \rangle \int d \bar{B}_n \frac{1}{\bar{B}_n} \delta \left( \bar{B}_n -\langle B \rangle  \right)=
\frac{\langle A \rangle}{\langle B \rangle}
=\langle \hat{O} \rangle ,
\label{OABclt2}
\end{aligned}$$ and we can take the standard deviation of the mean of ${\bar{A}_n}/{ \bar{B}_n }$ as the error bar $\sigma$. In all cases we ensure that the number of samples is large enough that any bias from dividing two stochastic quantities is smaller than the statistical error.

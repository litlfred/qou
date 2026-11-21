---
doc_id: arxiv-0908.3425v1
doc_title: "Chiral Perturbation Theory: Introduction and Recent Results in the One-Nucleon Sector"
section_id: sec-043-dimensional-counting-analysis
section_title: "Dimensional counting analysis"
section_number: null
pages: 64-65
source_pdf: 0908.3425v1.pdf
source_sha256: 5e88d45bbc1c1b9b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.965
latex_coverage_ratio: 1.0
doc_brief: "Chiral Perturbation Theory: Introduction and Recent Results in the One-Nucleon Sector — We provide an introduction to the basic concepts of chiral perturbation theory and discuss some recent"
---
[]{#section_dimensional_counting_analysis label="section_dimensional_counting_analysis"} In this section we provide an illustration of the dimensional counting analysis [@Gegelia:1994zz] in terms of a specific example. To that end let us consider the one-loop integral of Eq. ([\[4:3:2:Hdef\]](#4:3:2:Hdef){reference-type="ref" reference="4:3:2:Hdef"}), $$H(p^2,m^2,M^2;n)=
-i\int \frac{\mbox{d}^n k}{(2\pi)^n} \frac{1}{k^2-2p\cdot k
+p^2-m^2+i0^+}\frac{1}{k^2-M^2+i0^+}.$$ One would like to know how the integral behaves for small values of $M$ and/or $p^2-m^2$ as a function of $n$. If we consider, for fixed $p^2\neq m^2$, the limit $M\to 0$, the integral $H$ can be represented as $$H(p^2,m^2,M^2;n)=\sum_i M^{\beta_i} F_i(p^2,m^2,M^2;n),
\label{ippsiexp}$$ where the functions $F_i$ are analytic in $M^2$ and are obtained as follows. First, one re-writes the integration variable as $k=M^{\alpha_i}\tilde k$, where $\alpha_i$ is an arbitrary non-negative real number. Next, one isolates the overall factor of $M^{\beta_i}$ so that the remaining integrand can be expanded in positive powers of $M^2$ and interchanges the integration and summation. The resulting series represents the expansion of $F_i(p^2,m^2,M^2;n)$ in powers of $M^2$. The sum of all possible re-scalings with subsequent expansions with non-trivial coefficients then reproduces the expansion of the result of the original integral.

To be specific, let us apply this program to $H$: $$H(p^2,m^2,M^2;n) = -i\int\frac{M^{n \alpha_i} \mbox{d}^n\tilde k}{(2\pi)^n}
\frac{1}{\tilde k^2 M^{2 \alpha_i}-2 p\cdot\tilde k M^{\alpha_i}+ p^2-m^2+i0^+}
\frac{1}{\tilde k^2 M^{2 \alpha_i} -M^2+i0^+}. \label{ippsichv}$$ From Eq. ([\[ippsichv\]](#ippsichv){reference-type="ref" reference="ippsichv"}) we see that the first fraction does not contribute to the overall factor $M^{\beta_i}$ for any $\alpha_i$. It will be expanded in (positive) powers of $(\tilde k^2 M^{2\alpha_i}
-2 p\cdot \tilde k M^{\alpha_i})$ except for $\alpha_i=0$. For $0<\alpha_i<1$, we re-write the second fraction as $$\frac{1}{M^{2 \alpha_i}} \ \frac{1}{(\tilde k^2-M^{2-2 \alpha_i}+i 0^+)}
=\frac{1}{M^{2 \alpha_i}}
\frac{1}{\tilde k^2+i0^+}\left(1+\frac{M^{2-2\alpha_i}}{\tilde k^2+i0^+}+\cdots
\right).
\label{1pr}$$ On the other hand, if $1<\alpha_i$ we re-write the second fraction as $$\frac{1}{M^{2}} \ \frac{1}{(\tilde k^2 M^{2 \alpha_i-2}-1+i 0^+) }
=-\frac{1}{M^{2}}\left(1+\tilde k^2 M^{2 \alpha_i-2}+\cdots\right).
\label{1pr2}$$ In both cases one obtains integrals of the type $\int \mbox{d}^n\tilde k \ \tilde k^{\mu_1}\cdots \tilde k^{\mu_m}$ as the coefficients of the expansion. However, such integrals vanish in dimensional regularization. Therefore, the only non-trivial terms in the sum of Eq. ([\[ippsiexp\]](#ippsiexp){reference-type="ref" reference="ippsiexp"}) correspond to either $\alpha_i=0$ or $\alpha_i=1$. Thus we obtain $$H(p^2,m^2,M^2;n)=H^{(0)}(p^2,m^2,M^2;n)+H^{(1)}(p^2,m^2,M^2;n),
\label{ippsidecomp}$$ where $$H^{(0)}(p^2,m^2,M^2;n)=-i\sum_{j=0}^{\infty}
\left( M^2\right)^j \int \frac{\mbox{d}^n k}{(2\pi)^n}
\frac{1}{k^2 -2 p\cdot k+ p^2-m^2+i0^+}
\frac{1}{(k^2 +i0^+)^{j+1}},
\label{ippsi2}$$ and $$H^{(1)}(p^2,m^2,M^2;n)=-i \frac{M^{n-2}}{p^2-m^2+i0^+}
\sum_{j=0}^{\infty}
\frac{(-1)^j M^j}{(p^2-m^2+i0^+)^j}
\int\frac{\mbox{d}^n\tilde k}{(2\pi)^n} \frac{\left(\tilde k^2 M-2 p\cdot\tilde
k\right)^j}{\tilde k^2-1+i0^+}. \label{ippsi1}$$ A comparison with the direct calculation of $H$ shows that the dimensional counting method indeed leads to the correct expressions [@Gegelia:1994zz]. While the loop integrals of Eq. ([\[ippsi1\]](#ippsi1){reference-type="ref" reference="ippsi1"}) have a simple analytic structure in $p^2-m^2$, the same technique can be repeated for the loop integrals of Eq. ([\[ippsi2\]](#ippsi2){reference-type="ref" reference="ippsi2"}) when $p^2-m^2\to 0$, now using the change of variable $k=(p^2-m^2)^{\gamma_i}
\tilde k$ with arbitrary non-negative real numbers $\gamma_i$.

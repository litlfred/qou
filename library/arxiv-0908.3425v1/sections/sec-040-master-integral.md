---
doc_id: arxiv-0908.3425v1
doc_title: "Chiral Perturbation Theory: Introduction and Recent Results in the One-Nucleon Sector"
section_id: sec-040-master-integral
section_title: "Master integral"
section_number: null
pages: 59-60
source_pdf: 0908.3425v1.pdf
source_sha256: 5e88d45bbc1c1b9b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.99
latex_coverage_ratio: 0.99
doc_brief: "Chiral Perturbation Theory: Introduction and Recent Results in the One-Nucleon Sector — We provide an introduction to the basic concepts of chiral perturbation theory and discuss some recent"
---
[]{#subsubsection_master_integral label="subsubsection_master_integral"} We have seen that the modified minimal subtraction scheme $\widetilde{\rm MS}$ does not produce the desired power counting. We will discuss the power-counting problem in terms of the dimensionally regularized one-loop integral $$\begin{aligned}
\label{4:3:2:Hdef}
H(p^2,m^2,M^2;n)
&\equiv& -i\int \frac{\mbox{d}^n
k}{(2\pi)^n} \frac{1}{[(k-p)^2-m^2+i0^+](k^2-M^2+i0^+)}\nonumber\\
&=&-i\int \frac{\mbox{d}^n k}{(2\pi)^n} \frac{1}{[k^2-2p\cdot k
+(p^2-m^2)+i0^+](k^2-M^2+i0^+)}.
\end{aligned}$$ We are interested in nucleon four-momenta close to the mass-shell condition, $p^2\approx m^2$, counting $p^2-m^2$ as ${\cal O}(q)$ and $M^2$ as ${\cal O}(q^2)$. In order to conform with Ref. [@Becher:1999he], we have omitted the factor $\mu^{4-n}$ and have reversed the overall sign in comparison with our previous definition of $I_{N\pi}$. Let us turn to the discussion of $H(p^2,m^2,M^2;n)$. To that end, we make use of the Feynman parametrization $$\label{4:3:2:feynmanparh}
{1\over ab}=\int_0^1 \mbox{d}z  {1\over [az+b(1-z)]^2}$$ with $a=(k-p)^2-m^2+i0^+$ and $b=k^2-M^2+i0^+$, interchange the order of integrations, and perform the shift $k\to k+zp$, to obtain $$H(p^2,m^2,M^2;n)=-i \int_0^1 \mbox{d}z\int\frac{\mbox{d}^n
k}{(2\pi)^n}\frac{1}{[k^2-A(z) +i0^+]^2},$$ where $$A(z)=z^2 p^2-z(p^2-m^2+M^2)+M^2.$$ Making use of $$\int \frac{\mbox{d}^n k}{(2\pi)^n} \frac{(k^2)^p}{(k^2-A)^q}
=\frac{i(-)^{p-q}}{(4\pi)^{\frac{n}{2}}}
\frac{\Gamma\left(p+\frac{n}{2}\right)\Gamma\left(q-p-\frac{n}{2}\right)}{
\Gamma\left(\frac{n}{2}\right)\Gamma(q)} A^{p+\frac{n}{2}-q}$$ with $p=0$ and $q=2$, we find $$\label{4:3:2:HPmMn}
H(p^2,m^2,M^2;n)=\frac{1}{(4\pi)^{\frac{n}{2}}}
\Gamma\left(2-\frac{n}{2}\right) \int_0^1 \mbox{d}z
[A(z)-i0^+]^{\frac{n}{2}-2}.$$ The relevant properties can nicely be displayed at the threshold $p^2_{\rm thr}=(m+M)^2$, where $A(z)=[z(m+M)-M]^2$ is particularly simple. The small imaginary part can be dropped in this case, because $A(z)$ is never negative. Splitting the integration interval into $[0,z_0]$ and $[z_0,1]$ with $z_0=M/(m+M)$, we have, for $n>3$, $$\begin{aligned}
\int_0^1 \mbox{d}z [A(z)]^{\frac{n}{2}-2}&=&\int_0^{z_0}\mbox{d}z [M-z(m+M)]^{n-4}
+\int_{z_0}^1\mbox{d}z [z(m+M)-M]^{n-4}\\
&=&\frac{1}{(n-3)(m+M)}(M^{n-3}+m^{n-3}),
\end{aligned}$$ yielding, through analytic continuation, for arbitrary $n$ $$\label{4:3:2:defhthr}
 H((m+M)^2,m^2,M^2;n)=
\frac{\Gamma\left(2-\frac{n}{2}\right)}{(4\pi)^{\frac{n}{2}}(n-3)}
\left(\frac{M^{n-3}}{m+M}+\frac{m^{n-3}}{m+M}\right).$$ The first term, proportional to $M^{n-3}$, is defined as the so-called infrared singular part $I$. Since $M\to 0$ implies $p^2_{\rm thr} \to m^2$ this term is singular for $n\leq 3$. The second term, proportional to $m^{n-3}$, is defined as the infrared regular part $R$. Note that for non-integer $n$ the infrared singular part contains non-integer powers of $M$, while an expansion of the regular part always contains non-negative integer powers of $M$ only.

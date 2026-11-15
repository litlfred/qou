---
doc_id: arxiv-0807.2679v1
doc_title: "A cabling formula for the colored Jones polynomial"
section_id: sec-002-proof-of-the-volume-conjecture-for-zero-volume-l
section_title: "Proof of the volume conjecture for zero volume links"
section_number: null
pages: 10-12
source_pdf: 0807.2679v1.pdf
source_sha256: 69ef10f8e70fc6f6
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.554
doc_brief: "A cabling formula for the colored Jones polynomial — We prove an explicit cabling formula for the colored Jones polynomial."
---
As an application of the cabling formula we just proved we will show that the volume conjecture holds true for all zero volume knots and links (corollary 1). Such links are related to cabling by the fact that all links of zero simplicial volume are obtained from the unknot by repeated cabling and connected sum [@Gordon].

In the volume conjecture the usual normalization of the colored Jones polynomial for knots is to divide by the value of the unknot. However, if a link has $s$ split components then the unnormalized Jones has at least an $s$ fold zero at the $N$-th root of unity [@vanderVeen]. We therefore choose to normalize it by dividing by $[N]^s$. For convenience we work with $A = q^{1/4}$ instead of $q$ so that for the volume conjecture we need to evaluate at $A = e^{\pi i/2N}$.

The unnormalized colored Jones polynomial of a link with $c$ components is a multi-sequence of Laurent polynomials in $A$ of the form $P_{\mathbf{N}}(A) = \sum_j a_{j,\mathbf{N}}A^j$, where $\mathbf{N} = (N_1,\hdots,N_c)$. We say that a multi-sequence is moderate if there exist $C,m>0$ such that $$\forall\ \mathbf{N}:\quad |\mathrm{maxdeg}P_{\mathbf{N}}|,|\mathrm{mindeg}P_{\mathbf{N}}|,|a_{j,\mathbf{N}}| < C|\mathbf{N}|^m$$ It is clear that the set of moderate sequences is closed under products and differentiation with respect to $A$.

To prove the volume conjecture for all zero volume links we first show that their unnormalized colored Jones polynomials are moderate. Since such links are obtained from the unknot by repeated cabling and connected sum, we need to show that $[N]$ is moderate (trivial) and that the set of moderate multi-sequences is closed under taking products and under an operation that generalizes cabling of links that we now define. Given two multi-sequences $P_{\mathbf{M}}(A)$ and $Q_{\mathbf{N},w}(A)$ define a new multi-sequence $R$ by $$R_{M_1,\hdots M_{i-1}, \mathbf{N},\hdots,M_c}(A) = \sum_{|w|\leq (|\mathbf{N}|-g)/2}Q_{\mathbf{N},2w}(A)P_{M_1,\hdots,M_{i-1},|2wp+1|,\hdots, M_c}(A)$$

The triangle inequality shows that that if $P$ and $Q$ are moderate then so is $R$. The cabling formula applied to the colored Jones polynomial $J$ of any link is an example of the above defined operation where $P = J$ and $Q_{\mathbf{N},w}(A)$ is a multi-sequence that does not depend on the link and is readily read off from the cabling formula or rather the version at the end of the last section. It is not hard to see that this $Q$ is indeed moderate.

Now that we know that the unnormalized colored Jones polynomial of a zero volume knot $J_{\mathbf{N}}(A)$ is moderate we conclude the proof of corollary 1 as follows. To evaluate the normalized Jones polynomial we will use 'l Hospital's rule after writing it as $$J_{N,\hdots,N}(A)/[N]^s = \tilde{J}_{N,\hdots,N}(A)/(A^{2N}-A^{-2N})^s$$ where $\tilde{J}$ = $(A^{2}-A^{-2})^sJ$ is again moderate. If we differentiate both numerator and denominator $s$ times with respect to $A$ and evaluate at $e^{\pi i/2N}$ we get $(\frac{e^{\pi i/2N}}{-4N})\frac{d^s}{dA^s}\tilde{J}_{N,\hdots,N}(e^{\pi i/2N})$. Since $\frac{d^s}{dA^s}\tilde{J}_{\mathbf{N}}$ is again moderate, it follows that: $$\lim_{N\to \infty}\frac{2\pi}{N}|\frac{J_{N,\hdots,N}}{[N]^k}(e^{\frac{\pi i}{2N}})| = 0$$

---
doc_id: arxiv-1907.03683v4
doc_title: "EXPLICIT DESCRIPTION OF CHRISTOFFEL DEFORMATIONS AND"
section_id: sec-017-33-proof-of-theorem-31
section_title: "Proof of Theorem 3.1"
section_number: 3.3
pages: 13-17
source_pdf: 1907.03683v4.pdf
source_sha256: eb8cc2ddfc8c0739
toc_source: outline
text_source: latex
latex_prose_ratio: 0.946
latex_coverage_ratio: 0.984
doc_brief: "EXPLICIT DESCRIPTION OF CHRISTOFFEL DEFORMATIONS AND — Christoﬀel deformation of a measure on the real line consists of multipying this measure by a squared polynomial having its roots in R."
---
We will use the following Lemma, which we prove at the end of this section. This Lemma gives simple asymptotic results on the Charlier polynomials involving Bessel functions and their derivatives. As far as we know, the asymptotics we give can not be found in the litterature in this simple form. However, one may consult [@ouwong] for a complete study of the asymptotics of Charlier polynomials.

::: lem
[]{#lemme1 label="lemme1"} For any $l \in \mathbb{Z}$ and any $u \in \mathbb{R}$, we have $$\begin{aligned}
\lim_{N \rightarrow \infty}\sqrt{\omega_{\alpha/N}(u+N)} C_{N+l}(u+N;\alpha/N)=J_{u-l}(2\sqrt{\alpha}),
\end{aligned}$$ and $$\begin{aligned}
\lim_{N \rightarrow \infty} \sqrt{\omega_{\alpha/N}(u+N)} \left( C'_{N+l}(u+n;\alpha/N) - \log \left(N/\sqrt{\alpha} \right) C_{N+l}(u+N;\alpha/N) \right) = L_{u-l}(2\sqrt{\alpha}).
\end{aligned}$$
:::

The proof of Theorem [\[thm1\]](#thm1){reference-type="ref" reference="thm1"} goes as follows. We use the formula from Proposition [\[propkernelcharlier\]](#propkernelcharlier){reference-type="ref" reference="propkernelcharlier"} for the kernel $K_N^{\alpha/N, k}$ and proceed to the analysis of each factor. First, a straightforward computation shows that: $$\label{limconstante}
\frac{c_{N-1}}{c_{N+2k}} \rightarrow \alpha^{\frac{2k+1}{2}}$$ when $N \rightarrow +\infty$ and where $c_n$ is the leading coefficient of the Charlier polynomial $C_n$. We now analyse the ratio $$\begin{aligned}
\sqrt{\omega_{\alpha/N}(x+N)\omega_{\alpha/N}(y+N)}\frac{D_N^k(x+N)D_{N-1}^k(y+N)-D_N^k(y+N)D_{N-1}^k(x+N)}{\left(\delta_N^k\right)^2(x-y)}.
\end{aligned}$$ To this end, we multiply both sides of this ratio by $$\begin{aligned}
m:=\prod_{i=1}^{k}\omega_{\alpha/N}(\tilde{u}_{i}+N)^2,
\end{aligned}$$ and in each determinant $D_N^k(.)$, $D_{N-1}^k(.)$ and $\delta_N^k$, we perform the following operations on rows $R_l$: $$\begin{aligned}
R_{k+i} \leftarrow R_{k+i}-\log \left( N/\alpha \right) R_{i}
\end{aligned}$$ for $i=1,...,k$. Let $M$ be the diagonal $2k \times 2k$ matrix: $$\begin{aligned}
M=& \text{diag} \left( \sqrt{\omega_{\alpha/N}(u_1)},...,\sqrt{\omega_{\alpha/N}(u_k)},\sqrt{\omega_{\alpha/N}(u_1)}, ...,\sqrt{\omega_{\alpha/N}(u_k)} \right).
\end{aligned}$$ Then $$\begin{aligned}
m=\det(M^2)=\det (M)^2.
\end{aligned}$$Let us denote by $\hat{\delta_N^k}$ the matrix such that $\det\left( \hat{\delta_N^k} \right)=\delta_N^k$ with changed rows as described above and use the same notation for the other determinants. We have: $$\begin{aligned}
m\left( \delta_N^k \right)^{2}=\det \left(M\hat{\delta_N^k} \right)^2
\end{aligned}$$ and each term of this matrix is precisely of the type we can analyse by Lemma [\[lemme1\]](#lemme1){reference-type="ref" reference="lemme1"}. In the same fashion, if we denote by $M_z$ the $(2k+1) \times (2k+1)$ matrix $$\begin{aligned}
M_z=\text{diag}\left(M,\sqrt{\omega_{\alpha/N}(z+N)}\right),
\end{aligned}$$ we have that $$\begin{gathered}
\sqrt{\omega_{\alpha/N}(x+N)\omega_{\alpha/N}(y+N)}\cdot m \cdot \left(D_{N}^k(x+N)D_{N-1}^k(y+N)-D_{N}^k(x+N)D_{N-1}^k(y+N) \right) \\
=\det (M_x) \det (M_y) \cdot \left(D_{N}^k(x+N)D_{N-1}^k(y+N)-D_{N}^k(x+N)D_{N-1}^k(y+N) \right) \\
= \det \left( M_x \hat{D}_N^k(x+N)\right) \det \left( M_y \hat{D}_{N-1}^k(y+N)\right)
\\
-\det \left(M_y \hat{D}_N^k(y+N) \right) \det \left( M_x \hat{D}_{N-1}^k(x+N) \right),
\end{gathered}$$ and again, we know the asymptotics for the components of each matrix thanks to Lemma [\[lemme1\]](#lemme1){reference-type="ref" reference="lemme1"}. Using the continuity of the determinant, we have established that, for all $x \neq y$ $$\begin{aligned}
\lim_{N \rightarrow +\infty} \sqrt{\omega_{\alpha/N}(x+N)\omega_{\alpha/N}(y+N)}&\frac{D_N^k(x+N)D_{N-1}^k(y+N)-D_N^k(y+N)D_{N-1}^k(x+N)}{\left(\delta_N^k\right)^k(x-y)}\\
&=\frac{A_{k,0}(x)A_{k,1}(y)-A_{k,0}(y)A_{k,1}(x)}{C_{k,0}(x-y)}.
\end{aligned}$$

The case $x=y$ goes as follows. For a $(2k+1)\times(2k+1)$ determinant $A$, and for $i=0,...,2k$ we denote by $[A]^i$ its $\left((i+1),(2k+1)\right)$ cofactor, i.e. the same determinant with the $(i+1)$-th column and the last line removed, multiplied by $(-1)^{i+1+2k+1}=(-1)^i$. We have $$\begin{gathered}
 \label{eqsym}
D_{N}^k(x+N)'D_{N-1}^k(x+N)-D_{N}^k(x+N)D_{N-1}^k(x+N)'\\
=\left(\sum_{i=0}^{2k}\left[D_N^k(x+N)\right]^iC_{N+i}'(x+N) \right)\left(\sum_{i=0}^{2k}\left[D_{N-1}^k(x+N)\right]^iC_{N-1+i}(x+N) \right)\\
-\left(\sum_{i=0}^{2k}\left[D_N^k(x+N)\right]^iC_{N+i}(x+N) \right)\left(\sum_{i=0}^{2k}\left[D_{N-1}^k(x+N)\right]^iC_{N-1+i}'(x+N) \right)\\
=\sum_{i,j=0}^{2k}\left[D_N^k(x+N)\right]^i\left[D_{N-1}^k(x+N)\right]^j
 \left(C_{N+i}'(x+N)C_{N-1+j}(x+N)-C_{N+i}(x+N)C_{N-1+j}'(x+N) \right).
\end{gathered}$$ Remark that the analysis of the cofactors has been done, and observe now that we have nice symmetries in this expression. Indeed, for any $i,j=0,...,2k$, second part of Lemma [\[lemme1\]](#lemme1){reference-type="ref" reference="lemme1"} entails: $$\begin{aligned}
C_{N+i}&'(x+N)C_{N-1+j}(x+N)-C_{N+i}(x+N)C_{N-1+j}'(x+N)\\
&=\omega_{\alpha/N}(x+N)^{-1/2}\\
&\times\left\{ \left(L_{x-i}(2\sqrt{\alpha})+\log\left(N/\sqrt{\alpha}\right)C_{N+i}(x+N)+o(1)\right)C_{N-1+j}(x+N)\right.\\
&\left.-C_{N+i}(x+N)\left(L_{x-1+j}(2\sqrt{\alpha})+\log\left(N/\sqrt{\alpha}\right)C_{N-1+j}(x+N)+o(1)\right)\right\}.
\end{aligned}$$ We see that the term involving the factor $\log(N/\sqrt{\alpha})$ vanishes. Multiplying ([\[eqsym\]](#eqsym){reference-type="ref" reference="eqsym"}) by $\omega_{\alpha/N}(x+N)$ and applying the first part of Lemma [\[lemme1\]](#lemme1){reference-type="ref" reference="lemme1"}, we are left with: $$\begin{aligned}
\omega_{\alpha/N}(x+N)&\left(D_{N}^k(x+N)'D_{N-1}^k(x+N)-D_{N}^k(x+N)D_{N-1}^k(x+N)'\right)\\
&=\sum_{i,j=0}^{2k}\left[D_N^k(x+N)\right]^i\left[D_{N-1}^k(x+N)\right]^j\\
&\times\left(L_{-x-i}(2\sqrt{\alpha})J_{-x+1-j}(2\sqrt{\alpha})-J_{-x-i}(2\sqrt{\alpha})L_{-x+1-j}(2\sqrt{\alpha}) + o(1)\right).
\end{aligned}$$ This sum can be factorized, and we obtain that: $$\begin{aligned}
\omega_{\alpha/N}(x+N)& \cdot m \cdot \left(D_{N}^k(x+N)'D_{N-1}^k(x+N)-D_{N}^k(x+N)D_{N-1}^k(x+N)'\right)
\end{aligned}$$ tends to $$\begin{aligned}
 A_{k,0}'(x)A_{k,1}(x)-A_{k,0}(x)A_{k,1}'(x)
\end{aligned}$$ as $N$ tends to $+\infty$, which is the desired result. Recalling ([\[limconstante\]](#limconstante){reference-type="ref" reference="limconstante"}), the Theorem is proved. $\square$\
\

::: proof
*Proof of Lemma [\[lemme1\]](#lemme1){reference-type="ref" reference="lemme1"}.* Following [@johanssonplancherel], we will use the integral representation for Charlier polynomials. Since the generating series for the normalized Charlier polynomials is: $$\begin{aligned}
\sum_{m=0}^{\infty} \left( \frac{\alpha}{N} \right)^{m/2}\frac{1}{\sqrt{m!}}C_m(x;\alpha/N)w^m=e^{-\alpha w / N}\left(1+w \right)^x,
\end{aligned}$$ we have by Cauchy's formula, for $r>1$: $$\begin{gathered}
 \label{form:intrepcharlier}
C_m(x;\alpha/N)= \sqrt{m!} \left( \frac{N}{\alpha} \right)^{m/2}  \left( \frac{1}{2i\pi} \int_{|w|=r} e^{-\alpha w/N} (1+w)^{x} w^{-m} \frac{dw}{w} \right. \\
 \left. - (-1)^m \frac{\sin \pi x}{\pi} \int_{1}^{r} e^{\alpha u /N} (u-1)^{x} u^{-m} \frac{du}{u} \right).
\end{gathered}$$ The second integral in ([\[form:intrepcharlier\]](#form:intrepcharlier){reference-type="ref" reference="form:intrepcharlier"}) arises as we take the principal branch of logarithm in order to define $(1+w)^x$ for $w \in \mathbb{C}\setminus (-\infty, -1]$, $x \in \mathbb{R}$. Performing the change of variables $w=Nz/\sqrt{\alpha}$, $u=Ns/\sqrt{\alpha}$, one obtains, for $r > \sqrt{\alpha}/N$: $$\begin{aligned}
C_{m}(x;\alpha/N)&=\sqrt{\frac{m!}{N^m}} \left( \frac{1}{2\pi}\int_{-\pi}^{\pi}e^{-\sqrt{\alpha}re^{i\theta}} \left( 1+ \frac{Nre^{i\theta }}{\sqrt{\alpha}} \right)^x \frac{d\theta}{(re^{i\theta})^m} \right. \\
&\left. -(-1)^m \frac{\sin \pi x}{\pi} \int_{\sqrt{\alpha} / N}^{r} e^{\sqrt{\alpha}s} \left( \frac{Ns}{\sqrt{\alpha}}-1 \right)^x s^{-m} \frac{ds}{s} \right).
\end{aligned}$$ This expression can be suitably factorized: $$\label{eq2}
\begin{split}
C_{m}(x;\alpha/N)&=e^{-\sqrt{\alpha}} \sqrt{\frac{m!}{N^m}} \left( 1+ \frac{N}{\sqrt{\alpha}} \right)^{x}\\
&\times \left( \frac{1}{2\pi} \int_{-\pi}^{\pi}e^{\sqrt{\alpha}(1-re^{i\theta})} \left(  \frac{\sqrt{\alpha}+Nre^{i\theta }}{\sqrt{\alpha}+N} \right)^x \frac{d\theta}{(re^{i\theta})^m} \right.\\
&\left. -(-1)^m \frac{\sin \pi x}{\pi} \int_{\sqrt{\alpha} / N}^{r} e^{\sqrt{\alpha}(s+1)} \left( \frac{Ns-\sqrt{\alpha}}{\sqrt{\alpha}+N} \right)^x s^{-m} \frac{ds}{s} \right).
\end{split}$$ Take $m=N+l$ and denote by $I_N^l(x)$ the sum of the integrals $$\label{eqintcharlier} \begin{split}
I_N^l(x)&:= \frac{1}{2\pi} \int_{-\pi}^{\pi}e^{\sqrt{\alpha}(1-re^{i\theta})} \left(  \frac{\sqrt{\alpha}+Nre^{i\theta }}{\sqrt{\alpha}+N} \right)^x \frac{d\theta}{(re^{i\theta})^{N+l}} \\
&-(-1)^{N+l} \frac{\sin \pi x}{\pi} \int_{\sqrt{\alpha} / N}^{r} e^{\sqrt{\alpha}(s+1)} \left( \frac{Ns-\sqrt{\alpha}}{\sqrt{\alpha}+N} \right)^x s^{-N-l} \frac{ds}{s}
\end{split},$$ for any $l \in \mathbb{Z}$, and define $$\begin{aligned}
A_{\alpha}^N(x)=e^{-2\sqrt{\alpha}}\frac{N!}{N^N}\left(1+\frac{N}{\sqrt{\alpha}} \right)^{2x} \omega_{\alpha/N}(x).
\end{aligned}$$ We have: $$\label{eq1}
\sqrt{\omega_{\alpha/N}(x)}C_{N+l}(x;\alpha/N)=\sqrt{\frac{(N+1)...(N+l)}{N^l}A_{\alpha}^N(x)}I_N^l(x).$$ Recall the integral representation for the Bessel function, which follows from ([\[defbessel\]](#defbessel){reference-type="ref" reference="defbessel"}): $$\label{eqintbessel}
J_{x}(2\sqrt{\alpha})= \frac{1}{2\pi}\int_{-\pi}^{\pi}e^{\sqrt{\alpha}(\frac{1}{r}e^{-i\theta}-re^{i\theta})}(re^{i\theta})^xd\theta-\frac{\sin\pi x}{\pi}\int_{0}^{r}e^{\sqrt{\alpha}(-1/s+s)}s^{x}\frac{ds}{s}.$$ We first show that the integrals ([\[eqintcharlier\]](#eqintcharlier){reference-type="ref" reference="eqintcharlier"}) converges to the integrals ([\[eqintbessel\]](#eqintbessel){reference-type="ref" reference="eqintbessel"}), with a speed of order at least $1/N$, showing that the integrands converge. For the first integrand, we have by definition: $$\begin{aligned}
e^{\sqrt{\alpha}(1-z)}&\left( \frac{\sqrt{\alpha}+Nz}{\sqrt{\alpha}+N} \right)^{x+N}z^{-N-l} \\
&= \exp \left( \sqrt{\alpha}(1-z) -(N+l)\log z +(x+N)(\log(\sqrt{\alpha} +Nz)-\log(\sqrt{\alpha} +N)) \right).
\intertext{Factorizing inside the logarithms leads to:}
e^{\sqrt{\alpha}(1-z)}&\left( \frac{\sqrt{\alpha}+Nz}{\sqrt{\alpha}+N} \right)^{x+N}z^{-N-l} \\
&=\exp \left( \sqrt{\alpha}(1-z) -(l-x)\log z +(x+N)\left(\log \left(1+\frac{ \sqrt{\alpha}}{Nz} \right) - \log \left( 1+ \frac{\sqrt{\alpha}}{N} \right) \right) \right) \\
&=\exp \left( \sqrt{\alpha}(1/z-z)+O(1/N) \right)z^{x-l},
\end{aligned}$$ where the last line follows from straightforward simplifications and first order expansions of the logarithms near $1$. In the same way, we have for the second integrand: $$\begin{aligned}
e^{\sqrt{\alpha}(s+1)} \left( \frac{Ns-\sqrt{\alpha}}{\sqrt{\alpha}+N} \right)^{x+N} s^{-N-l}=\exp \left(\sqrt{\alpha}(-1/s+s)+O(1/N)\right)s^{x-l}.
\end{aligned}$$ We have shown that there exists a constant $K=K(\alpha,x,r,l)$ such that: $$\begin{aligned}
\left|e^{\sqrt{\alpha}(1-z)}\left( \frac{\sqrt{\alpha}+Nz}{\sqrt{\alpha}+N} \right)^{x+N}z^{-N-l}- \exp \left( \sqrt{\alpha}(1/z-z) \right)z^{x-l}\right| \leq \frac{K}{N}, \\
\intertext{and}
\left|e^{\sqrt{\alpha}(s+1)} \left( \frac{Ns-\sqrt{\alpha}}{\sqrt{\alpha}+N} \right)^{x+N} s^{-N-l}- e^{\sqrt{\alpha}(-1/s+s)}s^{x-l}\right| \leq \frac{K}{N},
\end{aligned}$$ for all involved $z$ and $s$. This implies: $$\begin{aligned}
 | I_N^l(x+N)-J_{x-l}(2\sqrt{\alpha} )| \leq \frac{K}{N},
\end{aligned}$$ as announced. Since as $N \rightarrow +\infty$, we have that: $$\begin{aligned}
A_{\alpha}^N (x+N) \rightarrow 1,
\end{aligned}$$ and recalling ([\[eq1\]](#eq1){reference-type="ref" reference="eq1"}), we have established the first part of the Lemma.\
We now move to the proof of the second statement of the Lemma. Since the techniques are very similar, we will give less details in our computations. Differentating expression ([\[eq2\]](#eq2){reference-type="ref" reference="eq2"}), we obtain: $$\begin{aligned}
C_m'(x;\alpha/N)&=\log \left( 1+ \frac{N}{\sqrt{\alpha}} \right) C_m(x;\alpha/N)\\
&+ e^{-\sqrt{\alpha}} \sqrt{\frac{m!}{N^m}} \left( 1+ \frac{N}{\sqrt{\alpha}} \right)^{x} \frac{d}{dx} \left( I^{m-N}_{N} (x) \right).
\end{aligned}$$ We thus only need to proof that the derivative of the integrals converges to the derivative of the Bessel function. Derivations under the sign of the integrals give $$\begin{aligned}
\frac{d}{dx} \left( I^{l}_{N} (x)\right)&=\frac{1}{2\pi} \int_{-\pi}^{\pi}\log \left( \frac{\sqrt{\alpha}+Nre^{i\theta }}{\sqrt{\alpha}+N} \right)e^{\sqrt{\alpha}(1-re^{i\theta})} \left(  \frac{\sqrt{\alpha}+Nre^{i\theta }}{\sqrt{\alpha}+N} \right)^x \frac{d\theta}{(re^{i\theta})^{N+l}} \\
&-(-1)^{N+l} \frac{\sin \pi x}{\pi} \int_{\sqrt{\alpha} / N}^{r} \log \left( \frac{Ns-\sqrt{\alpha}}{\sqrt{\alpha}+N} \right) e^{\sqrt{\alpha}(s+1)} \left( \frac{Ns-\sqrt{\alpha}}{\sqrt{\alpha}+N} \right)^x s^{-N-l} \frac{ds}{s} \\
&-(-1)^{N+l} \frac{\cos \pi x}{\pi} \int_{\sqrt{\alpha} / N}^{r} e^{\sqrt{\alpha}(s+1)} \left( \frac{Ns-\sqrt{\alpha}}{\sqrt{\alpha}+N} \right)^x s^{-N-l} \frac{ds}{s},
\end{aligned}$$ and $$\begin{aligned}
L_{x}(2\sqrt{\alpha})&= \frac{1}{2\pi}\int_{-\pi}^{\pi}\log(re^{i\theta})e^{\sqrt{\alpha}(\frac{1}{r}e^{-i\theta}-re^{i\theta})}(re^{i\theta})^xd\theta\\
&-\frac{\sin\pi x}{\pi}\int_{0}^{r}\log(s)e^{\sqrt{\alpha}(-1/s+s)}s^{x}\frac{ds}{s} \\
&-\frac{\cos\pi x}{\pi}\int_{0}^{r}e^{\sqrt{\alpha}(-1/s+s)}s^{x}\frac{ds}{s}.
\end{aligned}$$ Analogous computations lead to: $$\begin{aligned}
\lim_{N \rightarrow +\infty} \frac{d}{dx} \left( I^{l}_{N} (x+N)\right) = L_{x-l}(2\sqrt{\alpha}).
\end{aligned}$$ This completes the proof of the Lemma. ◻
:::

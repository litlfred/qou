---
doc_id: arxiv-1207.4990v3
doc_title: "Toeplitz matrices and Toeplitz determinants under the impetus of the Ising model. Some history and some recent results"
section_id: sec-004-5-new-questions-for-sslt
section_title: "New questions for SSLT"
section_number: 5
pages: 27-29
source_pdf: 1207.4990v3.pdf
source_sha256: 02aa065f4f65b857
toc_source: outline
text_source: latex
latex_prose_ratio: 0.996
latex_coverage_ratio: 1.0
doc_brief: "Toeplitz matrices and Toeplitz determinants under the impetus of the Ising model. Some history and some recent results — 12 sections: Front matter; Setting the problem; Toeplitz meets Ising"
---
In view of the above calculations for $T\ge T_c$, the Ising problem raised new questions and challenges in Toeplitz theory. From [\[eq50\]](#eq50){reference-type="eqref" reference="eq50"}, $\left\langle \sigma_{1,1}\, \sigma_{1, 1+n}\right\rangle = D_n
\!\left(\varphi_{\text{ons}}\right)$ (similarly, from [\[eq27\]](#eq27){reference-type="eqref" reference="eq27"}, $\langle \sigma_{1,1}\, \sigma_{1+n,\, 1+n}\rangle = D_n \left(\varphi_{\text{diag}}\right)$), and so we want to know precisely how $D_n \!\left(\varphi_{\text{ons}}\right)$ behaves as $n\to\infty$ for $T\ge T_c$. But for $T>T_c$, we have $0< \gamma_1 <1 < \gamma_2$ (see [\[eq23\]](#eq23){reference-type="eqref" reference="eq23"}, [\[eq26\]](#eq26){reference-type="eqref" reference="eq26"}), and so in contrast to the case $T<T_c$, the winding number of $\varphi_{\text{ons}}$ is $-1 \neq 0$. And at $T=T_c$, we see from [\[eq25\]](#eq25){reference-type="eqref" reference="eq25"} that $\varphi_{\text{ons}} \!\left(e^{i\theta}\right)$ has a jump discontinuity at $\theta=0$. For such discontinuities the Fourier coefficients $\left(\log \varphi_{\text{ons}}\right)_k$ decay as $k^{-1}$ and so $\sum^\infty_{k=1} k\left|\left(\log \varphi_{\text{ons}}\right)_k\right|^2 =\infty$. In both cases SSLT, or more properly Theorem [\[theorem7\]](#theorem7){reference-type="ref" reference="theorem7"}, does not apply.

In 1966, in a tour de force in [@Wu], Wu gave the first derivation of the precise asymptotics of $\left\langle \sigma_{1,1},\, \sigma_{1, 1+n} \right\rangle = D_n\!\left(\varphi_{\text{ons}}\right)$ as $n\to\infty$, for $T\ge T_c$. For $T>T_c$, Wu showed that for $n\to\infty$ $$\label{eq64}
\begin{aligned}
\left\langle\sigma_{1,1}\,\sigma_{1, 1+n}\right\rangle &= (\pi n)^{-\frac{1}{2}} \; \gamma_2^{-n} \left(1-\gamma^2_1\right)^{\frac{1}{4}}
\left(1-\gamma^{-2}_2\right)^{-\frac{1}{4}} \left(1-\gamma_1 \gamma_2\right)^{-\frac{1}{2}}\\
& \times \left(1+\frac{A_1}{n} + \frac{A_2}{n^2} + \frac{A_3}{n^3} + \dots \right)
\end{aligned}$$ with explicit expressions for $A_1$, $A_2$ and $A_3$ in terms of $\gamma_1=z_1\,z_2^*$ and $\gamma_2 = z^*_2/z_1$, defined in [\[eq22\]](#eq22){reference-type="eqref" reference="eq22"}. As $T> T_c \Longleftrightarrow \gamma_2>1$, [\[eq64\]](#eq64){reference-type="eqref" reference="eq64"} agrees in the order of decay with [\[eq63\]](#eq63){reference-type="eqref" reference="eq63"} for $\ell=0$ and $m=n$, but now we have the precise rate and constants. For $T=T_c$, Wu obtained $$\label{eq65}
\begin{aligned}
\left\langle \sigma_{1,1}\, \sigma_{1, 1+n}\right\rangle &= e^{\frac{1}{4}}\: 2^{\frac{1}{12}}\:
A^{-3}\, n^{-\frac{1}{4}}\left(1+ \gamma_1\right)^{\frac{1}{4}} \, \left(1-\gamma_1\right)^{-\frac{1}{4}}\\
&\qquad \times \left(1+B_1\, n^{-2} + O(n^{-3})\right)
\end{aligned}$$ with an explicit expression for $B_1$ in terms of $\gamma_1$, and $A$ is again Glaisher's constant [\[Glai\]](#Glai){reference-type="eqref" reference="Glai"}. For $T<T_c$, Wu also obtained higher order terms in [\[eq15\]](#eq15){reference-type="eqref" reference="eq15"} [\[eq16\]](#eq16){reference-type="eqref" reference="eq16"}, i.e., as $n\to\infty$ $$\label{eq66}
\left\langle \sigma_{1,1}\, \sigma_{1, 1+n}\right\rangle = \left(1-k_{\text{ons}}^2\right)^{\frac{1}{4}}
\left(
1+\left(2\pi \, n^2\right)^{-1}\:\gamma^{2n}_2 \left(\gamma^{-1}_2- \gamma_2\right)^{-2} \left[1+\frac{c_1}{n}
+ \frac{c_2}{n^2} + \dots \right]\right)$$ with explicit expression for $c_1$ and $c_2$ in terms of $\gamma_1$ and $\gamma_2$. In particular as $\gamma_2<1$, we see that $\left\langle \sigma_{1,1}\, \sigma_{1, 1+n}\right\rangle \to \left(1-k^2_{\text{ons}}\right)^{\frac{1}{4}}
=M_0$ exponentially fast.

There is an interesting twist to the story of Wu's computation of [\[eq65\]](#eq65){reference-type="eqref" reference="eq65"} at $T_c$. As a warm-up problem at $T_c$, $\sinh \frac{2J_1}{k_B \,T_c} \;\sinh \frac{2J_2}{k_B\, T_c} =1$, he considered the limiting case when $J_1\to 0$ and $J_2\to\infty$ in such a way that $\gamma_1\downarrow 0$ and $\gamma_2 \uparrow 1$ in [\[eq21\]](#eq21){reference-type="eqref" reference="eq21"}, and hence $$\varphi_{\text{ons}}\!\left(e^{i\theta}\right) = \left(\frac{1-e^{-i\theta}}{1-e^{i\theta}}\right)^{\frac{1}{2}}=
e^{i(\pi-\theta)/2}, \qquad 0<\theta< 2\pi.$$ Wu recognized $\det\!\left(\left(\varphi_{\text{ons}}\right)_{j-k}\right)_{0\le j\:k\le n-1}$ as a Cauchy determinant and computed the asymptotics which we have recorded above in [\[eq60\]](#eq60){reference-type="eqref" reference="eq60"}. Wu was unaware at the time, just like Fisher before him, that he had serendipitously computed the correlation function along the diagonal at $T_c$! Had Kaufman and Onsager published their formula for $\left\langle \sigma_{1,1}\, \sigma_{1+n, 1+n}\right\rangle$, this comedy of errors would probably have been avoided.

In the symmetric situation, $J_1=J_2$, one finds that at $T_c$, $\gamma_1=3-2\sqrt{2}$ and so $\left(\frac{1+\gamma_1}{1-\gamma_1} \right)^{\frac{1}{4}}=2^{\frac{1}{8}}$. Substituting this relation into [\[eq65\]](#eq65){reference-type="eqref" reference="eq65"}, we obtain as $n\to\infty$ $$\label{eq67}
\left\langle \sigma_{1,1} \, \sigma_{1, 1+n}\right\rangle = e^{\frac{1}{4}} \: 2^{5/24}\, A^{-3}\,n^{-\frac{1}{4}}
\left(1+O\left(\frac{1}{n^2}\right)\right),\qquad J_1=J_2.$$ This relation and [\[eq60\]](#eq60){reference-type="eqref" reference="eq60"} are consistent with the formula (cf. [\[eq57\]](#eq57){reference-type="eqref" reference="eq57"}) $$\label{eq88p}
\left\langle \sigma_{1,1}\,\sigma_{1+\ell, 1+m}\right\rangle = e^{\frac{1}{4}} \: 2^{5/24}\, A^{-3}\:k^{-\frac{1}{4}}
\left(1+O\left(\frac{1}{k^2}\right)\right),\qquad J_1=J_2$$ where $k=\sqrt{\ell^2 +m^2} \to \infty$. This asymptotic formula was derived by Cheng and Wu [@ChenWu] in 1967 (they also consider $J_1\neq J_2$), but it was only established rigorously in the last year by H. Pinson [@Pin] using a Phragmen-Lindelof type argument to interpolate between [\[eq60\]](#eq60){reference-type="eqref" reference="eq60"} and [\[eq67\]](#eq67){reference-type="eqref" reference="eq67"}. Recently two additional independent proofs of the rotational symmetry of $\left\langle \sigma_{1,1}\,\sigma_{1+\ell, 1+m}\right\rangle$ as $k=\sqrt{\ell^2 +m^2} \to \infty$ have been given by Dubédat [@Dub] and by Chelkak, Hongler, and Izyurov [@CheHonIzy]. In [@Dub] the author proceeds by equating the product of two Ising correlators with a free field (bosonic) correlator. In [@CheHonIzy], the proof is based on convergence results for discrete holomorphic spinor variables pioneered by S. Smirnov. In earlier work, Smirnov used such variables to prove conformal invariance and to detect Schramm-Loewner evolution within the Ising model, in an appropriate scaling limit (for references, see [@CheHonIzy]). If $J_1\neq J_2$, one expects elliptical rather than rotational symmetry in the analog of [\[eq88p\]](#eq88p){reference-type="eqref" reference="eq88p"} (see [@ChenWu] and also [\[eq71\]](#eq71){reference-type="eqref" reference="eq71"} below, which is taken from [@WMTB]).

The full expansion of $\left\langle \sigma_{1,1}\, \sigma_{1+\ell, 1+m}\right\rangle$ as $\ell^2 +m^2 \to \infty$ at $T\neq T_c$ in terms of so-called form factors $f^{(j)}_{M,N}$, is discussed in detail in [@McC1], $$\begin{aligned}
\left\langle \sigma_{1,1}\, \sigma_{1+m, 1+\ell}\right\rangle &= (1-t)^{\frac{1}{4}} \left(1+\sum^\infty_{n=1}
f^{(2n)}_{m,\ell} \right)&\quad\text{for}\quad T<T_c \label{eq68}
\intertext{and}
\left\langle\sigma_{1,1}\,\sigma_{1+m, 1+\ell}\right\rangle &=(1-t)^{\frac{1}{4}} \sum^\infty_{n=0}
f^{(2n+1)}_{m,\ell}&\quad\text{for}\quad T>T_c. \label{eq69}
\end{aligned}$$ For $T< T_c$, $t=k^2_{\text{ons}}$ and for $T>T_c$, $t=k^{-2}_{\text{ons}}$. These expansions were first obtained by Wu, McCoy, Tracy and Barouch [@WMTB] in 1976, but explicit expressions for the form factors were only given in 1999 and 2000 by Nickel [@Nick1] [@Nick2].

The derivation of the form factor expansions [\[eq68\]](#eq68){reference-type="eqref" reference="eq68"} [\[eq69\]](#eq69){reference-type="eqref" reference="eq69"} for $\left\langle \sigma_{1,1}\, \sigma_{1+m, 1+\ell}\right\rangle$ was obtained in [@WMTB] using the Fredholm determinant representations of Cheng and Wu [@ChenWu]. In the special cases $m=0$, $\ell\to\infty$, or $m=\ell\to\infty$, Lyborg and McCoy [@LyMcC] used the finite Toeplitz determinant representations to derive form factor expansions as in [\[eq68\]](#eq68){reference-type="eqref" reference="eq68"} [\[eq69\]](#eq69){reference-type="eqref" reference="eq69"}, but the detailed form of the expansions they obtained differs from the general expansions obtained in [@WMTB]. It is an interesting, and still unresolved, question to reconcile the form factor expansions obtained in these two different ways. For recent results on the form factor expansion of the diagonal correlations $\left\langle \sigma_{1,1}\, \sigma_{1+m, 1+m}\right\rangle$ which utilize results from [@BorOk] and [@GerCase], see [@WiFo].

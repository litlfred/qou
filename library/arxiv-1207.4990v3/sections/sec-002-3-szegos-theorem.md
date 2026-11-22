---
doc_id: arxiv-1207.4990v3
doc_title: "Toeplitz matrices and Toeplitz determinants under the impetus of the Ising model. Some history and some recent results"
section_id: sec-002-3-szegos-theorem
section_title: "Szego's Theorem"
section_number: 3
pages: 12-23
source_pdf: 1207.4990v3.pdf
source_sha256: 02aa065f4f65b857
toc_source: outline
text_source: latex
latex_prose_ratio: 0.995
latex_coverage_ratio: 0.985
doc_brief: "Toeplitz matrices and Toeplitz determinants under the impetus of the Ising model. Some history and some recent results — 12 sections: Front matter; Setting the problem; Toeplitz meets Ising"
---
[]{#secSzego label="secSzego"} Here is Szegő's result [@Sz3] [@GreSz].

::: theorem
[]{#theorem3 label="theorem3"} Let $\varphi\!\left(e^{i\theta}\right)$ be a positive, $C^{1+\varepsilon}$, $\varepsilon>0$, function on $S^1$. Let $(\log \varphi)_k = \frac{1}{2\pi} \int^\pi_{-\pi} e^{-ik\theta} \log \varphi
\!\left(e^{i\theta}\right) d\theta$, $k\in \mathbb{Z}$, denote the Fourier coefficients of $\log \varphi\!\left(e^{i\theta}\right)$. Then $$\label{eq31}
\lim_{n\to \infty} \frac{D_n (\varphi)}{e^{n(\log\varphi)_0}} = e^{E(\varphi)}$$ where $$\label{eq33}
E(\varphi) = \sum^\infty_{k=1} k \left| \left(\log \varphi\right)_k \right|^2.$$ $\Box$
:::

Thus the $o(n)$ term in [\[eq5\]](#eq5){reference-type="eqref" reference="eq5"} is given by $E(\varphi) + o(1)$.

::: remark
Note that $$\label{eq32}
e^{(\log\varphi)_0}= \exp\left[\frac{1}{2\pi} \;\int^\pi_{-\pi} \log\varphi\!\left(e^{i\theta}\right)  d\theta\right]$$ is the geometric mean of $\varphi$.
:::

In contrast to [\[eq31\]](#eq31){reference-type="eqref" reference="eq31"}, Szegő's earlier result Theorem [\[theorem1\]](#theorem1){reference-type="ref" reference="theorem1"}, $\lim_{n\to\infty} \left(D_n(\varphi)\right)^{\frac{1}{n}} = e^{(\log\varphi)_0}$, is known simply as Szegő's First Theorem, or sometimes just Szegő's Theorem.

In the years that followed, there was considerable effort by many mathematicians to weaken the assumptions in Theorem [\[theorem3\]](#theorem3){reference-type="ref" reference="theorem3"}. Along the way, many new methods, quite different one from the other, were discovered to prove [\[eq31\]](#eq31){reference-type="eqref" reference="eq31"}. These developments are described in the outstanding recent monographs by Barry Simon [@Sim2] and Böttcher and Silbermann [@BottSilb3]: also see [@McC2] and [@Bott1] for earlier summaries. In [@Sim2], the contributions of Kac [@Kac], G. Baxter [@BaxG1], Hirschman [@Hir], and Devinatz [@Dev], in particular, are discussed, leading up through successively weaker assumptions to the definitive result of Ibragimov [@Ibr] in 1968 giving necessary and sufficient conditions on $\varphi\!\left(e^{i\theta}\right)$ for [\[eq31\]](#eq31){reference-type="eqref" reference="eq31"} to hold under the assumption of the positivity of $\varphi$.

::: theorem
[]{#theorem4 label="theorem4"} Let $\varphi\!\left(e^{i\theta}\right) \frac{d\theta}{2\pi}$ be a probability measure on $S^1$ and suppose that $\log\varphi\!\left(e^{i\theta}\right)$ is integrable. Then [\[eq31\]](#eq31){reference-type="eqref" reference="eq31"} is always true in the following sense: $\lim_{n\to \infty} \frac{D_n(\varphi)}{e^{n(\log\varphi)_0}}$ always exists and equals $e^{E(\varphi)}$, including the case where one, and hence both, are infinite. $\Box$
:::

One can consider Toeplitz matrices $T_n(d\mu)$ for general probability measures $d\mu(\theta)=
\varphi\!\left(e^{i\theta}\right) \frac{d\theta}{2\pi} +d\mu_s(\theta)$ on $S^1$, where $d\mu_s$ denotes the singular part of $d\mu$. We have $T_n (d\mu) = \{ \mu_{j-k}\}_{0\le j,\,k\le n-1}$, where $\mu_\ell= \int e^{-i \ell
\theta} \, d\mu(\theta)$, $\ell \in \mathbb{Z}$ and $D_n(d\mu)= \det \, T_n(d\mu)$. The following remarkable result generalizes Theorem [\[theorem1\]](#theorem1){reference-type="ref" reference="theorem1"}.

::: theorem
[]{#theorem5 label="theorem5"} Let $d\mu(\theta) = \varphi\! \left(e^{i\theta}\right) \, \frac{d\theta}{2\pi} + d\mu_s(\theta)$ be a probability measure as above. Then Szegő's Limit Theorem is always true in the following sense: $\lim_{n\to\infty} D_n (d\mu)^{\frac{1}{n}}$ always exists and equals $\exp\left[\int^\pi_{-\pi} \log \varphi\!\left(e^{i\theta}\right)\, \frac{d\theta}{2\pi}\right]$, including the case where one, and hence both, are zero. $\Box$
:::

Szegő proved the result when $d\mu_s=0$, whereas Verblunsky was able to handle the case $d\mu_s \neq 0$. Of course, as $\varphi\!\left(e^{i\theta}\right) \in L^1 \left(\frac{d\theta}{2\pi}\right)$, $\int^\pi_{-\pi} \log
\varphi\!\left(e^{i\theta}\right) \, \frac{d\theta}{2\pi}
< \infty$, and the integral can diverge, possibly, only to $-\infty$. The striking feature of Theorem [\[theorem5\]](#theorem5){reference-type="ref" reference="theorem5"} is that $\lim_{n\to\infty} D_n (d\mu)^{\frac{1}{n}}$ is independent of $d\mu_s$.

Is it possible that [\[eq31\]](#eq31){reference-type="eqref" reference="eq31"} remains true when $d\mu_s \neq 0$? Here the definitive result is due to Golinskii and Ibragimov.

::: theorem
[]{#theorem6 label="theorem6"} Let $d\mu(\theta)=\varphi\!\left(e^{i\theta}\right) \, \frac{d\theta}{2\pi} + d\mu_s(\theta)$ be a probability measure as above, and suppose $\log \varphi\!\left(e^{i\theta}\right) \in L^1\left(\frac{d\theta}{2\pi}\right)$. If $d\mu_s\neq 0$, then $$\label{eq34}
\lim_{n\to\infty} \frac{D_n (d\mu)}{\exp\left[n \int^\pi_{-\pi} \log \varphi\!\left(e^{i\theta}\right)\,\frac{d\theta}{2\pi}\right]}
=   +\infty$$ $\Box$
:::

In other words, if [\[eq31\]](#eq31){reference-type="eqref" reference="eq31"} were to hold with $E(\varphi) =\sum^\infty_{k=1} k \left|(\log \varphi)_k \right|^2
< \infty$, then necessarily $d\mu_s =0$.

In [@Sim2], Simon presents six different proofs of [\[eq31\]](#eq31){reference-type="eqref" reference="eq31"}. Some of these proofs require stronger conditions on $\varphi$ (see [@Sim2]). We now describe these methods in some detail (but without giving precise conditions on $\varphi$ in each case) in order to illustrate the extraordinary variety of mathematical areas and techniques that inter-relate with Szegő's Strong Limit Theorem. Our presentation follows [@Sim2]. After this presentation, we will also describe three additional proofs not covered in [@Sim2], together with some brief comments on Szegő's original proof (see Remark [\[22+++\]](#22+++){reference-type="ref" reference="22+++"}).

The first proof uses ideas and results from the theory of orthogonal polynomials on the unit circle (OPUC's). These polynomials were introduced by Szegő in the early 1920's [@Sz4] [@Sz5] in the course of his investigation of the eigenvalues $\lambda^{(n)}_1, \dots, \lambda^{(n)}_n$ of Toeplitz matrices $T_n$. The classical references for OPUC's are [@Sz5] [@Ge]. The OPUC's $p_k(z) = \chi_k \,
z^k + \dots, \chi_k >0$, associated with a probability measure $d\mu(\theta)$ on $S^1$ are formed by orthonormalizing $1, z, z^2, \dots, z^k, \dots$ with respect to $d\mu(\theta)$ in $L^2\left(S^1,\,
d\mu(\theta)\right)$, $$\label{eq35}
\int_{S^1} \overline{p_k\! \left(e^{i\theta}\right)} \, p_j\!\left(e^{i\theta}\right) \, d\mu(\theta) = \delta_{k,j}, \qquad k,\, j \ge 0 \ .$$ OPUC's are intimately related to Toeplitz determinants. For example $$\label{eq36}
\frac{D_{n+1} (d\mu)}{D_n (d\mu)} =\frac{1}{\chi_n^2}= \frac{1}{\chi_0^2}
\prod^{n-1}_{j=0} \left(1-|\xi_j|^2\right), \qquad n\ge 1$$ where $\xi_j \equiv -\left(\chi_{j+1}\right)^{-1} \;\overline{p_{j+1} (0)}$, $\; j\ge 0$, are the so-called *Verblunsky* coefficients. The $\xi_j$'s have modulus less than 1, and so $F(d\mu)\equiv \lim_{n\to \infty}
D_{n+1} (d\mu)/D_n(d\mu)$ always exists and equals $\chi_0^{-2}\prod^\infty_{j=0} \left(1-|\xi_j|^2\right)$. But then $\lim_{n\to\infty} \left(D_n(d\mu)\right)^{\frac{1}{n}}$ always exists, and has the same limit. So the proof of Szegő's Limit Theorem, boils down to showing that $$\label{eq37}
\frac{1}{\chi_0^2}\prod^\infty_{j=0} \left(1-|\xi_j|^2\right) = \exp\left[\frac{1}{2\pi}
\int^\pi_{-\pi} \log \varphi\!\left(e^{i\theta}\right) d\theta\right]$$ where $d\mu(\theta)=\varphi\!\left(e^{i\theta}\right)\, \frac{d\theta}{2\pi} + d\mu_s(\theta)$. In turn, one finds that $$\lim_{n\to\infty} \frac{D_n(d\mu)}{\left(F(d\mu)\right)^n} = \lim_{n\to\infty} 
\frac{\prod^{n-2}_{j=0} \left(1-|\xi_j|^2\right)^{-j-1}}{\prod_{j=n-1}^\infty (1-|\xi_j|^2)^n}$$ and the proof of SSLT for $d\mu_s=0$ reduces to showing that the limit on the RHS is just $e^{E(\varphi)}$. As we will see below, OPUC's play a crucial role in analyzing the Fisher-Hartwig conjecture for Toeplitz determinants with singular symbols $\varphi\!\left(e^{i\theta}\right)$.

The second proof utilizes a remarkable identity which gives an exact formula for $D_n(\varphi)$, $$\label{eq38}
D_n(\varphi) = e^{n(\log\varphi)_0 + E(\varphi)} \, \det \left(1-Q_n \, H(b)\, H(\widetilde{c})\, Q_n\right),
\quad n\ge 1$$ where $\det$ denotes the determinant in $\ell^+_2 = \ell_2(\mathbb{Z}_+)$, $\mathbb{Z}_+=\{0,1,\dots\}$, $Q_n$ is the orthogonal projection in $\ell^+_2$ onto $\ell^+_{2,n} = \{u= (u_0, u_1, \dots ) \in \ell^+_2\,:\; u_i=0
\text{ for } 0\le i <n\}$, and $H(b)$, $H(\widetilde{c})$ are the Hankel operators with kernels $\{b_{i+j+1}\}_{i,\, j\ge 0}, \, \{c_{-i -j-1}\}_{i,\, j \ge 0}$. Here $b\!\left(e^{i\theta}\right) = \sum_j b_j\, e^{ij\theta}$, $c\!\left(e^{i\theta}\right) = \sum_j c_j \, e^{ij\theta}$ are defined in terms of the *Szegő function* ${\cal D}(z) = \exp \left(\frac{1}{4\pi} \int^\pi_{-\pi}  \frac{e^{i\theta}+z}{e^{i\theta}-z}
\;\log \varphi\!\left(e^{i\theta}\right)d\theta\right)$, $$\label{eq39}
b\equiv \frac{\overline{\cal D}}{\cal D},\qquad c\equiv \frac{\cal D}{\overline{\cal D}}$$ where ${\cal D}={\cal D}(e^{i\theta})=\lim_{z\to e^{i\theta},|z|<1}{\cal D}(z)$. The point is that $H(b)\, H(\widetilde{c})$ is a trace-class operator in $\ell^+_2 = \ell^+_{2,\,0}$, and hence $Q_n\, H(b)\, H(\widetilde{c})\,Q_n~\to~0$ in trace-norm by abstract arguments as $n\to\infty$. But then $\det \left(1-Q_n \, H(b)\, H(\widetilde{c}) \, Q_n\right)\to 1$ as $n\to\infty$, by the continuity properties of the determinant. (For more information about the trace class and determinants, see [@BottSilb3] [@Sim3].) Thus SSLT is immediate, once one has proved [\[eq38\]](#eq38){reference-type="eqref" reference="eq38"}. Formula [\[eq38\]](#eq38){reference-type="eqref" reference="eq38"} is known as the Borodin-Okounkov formula and was proved [@BorOk] in 2000 in the context of combinatorics and random matrix theory. The formula evoked great interest, and meanwhile several new proofs and generalizations have been given (see, e.g., [@BasWid] [@BottWid1] and [@Sim2]). However, it turns out that it was already proven many years earlier by Geronimo and Case in 1979 in their work on inverse scattering theory [@GerCase]. The broader significance of this paper was not appreciated at the time. But more to the point, in a separate section in their paper titled "Szegő's Theorem", Geronimo and Case actually used [\[eq38\]](#eq38){reference-type="eqref" reference="eq38"} to prove SSLT. It is unfortunate that these developments were overlooked by the experts in the field.

The third and fourth methods utilize the following Heine-type multi-integral representation for $D_n(\varphi)$ (see, e.g., [@BottSilb3] [@Sim2]) $$\label{eq40}
D_n(\varphi) = \frac{1}{n!} \int^{2\pi}_0 \dots \int^{2\pi}_0 \prod_{0\le j < k \le n-1}
\left|e^{i\theta_j} - e^{i\theta_k} \right|^2 \prod^{n-1}_{j=0} \varphi\left(e^{i\theta j}\right)
\,\frac{d\theta_j}{2\pi} \ .$$ In the third method, due to Bump and Diaconis [@BumpDia], the authors observe that the RHS of [\[eq40\]](#eq40){reference-type="eqref" reference="eq40"} can be re-written via Weyl's integration formula as $\int_{\mathcal{U}(n)} e^{F_n(g)} \, dg$, where $dg$ denotes Haar measures on the unitary group $\mathcal{U}(n)$, and $F_n(g) = \sum^{n-1}_{j=0} \log\varphi\!\left(e^{i\theta_j(g)}\right)$, where $\left\{e^{i\theta_j(g)}\right\}$ are the eigenvalues of $g$. Substituting the Fourier expansion $\log \varphi \!\left(e^{i\theta}\right) = \sum^\infty_{k=-\infty}
(\log\varphi)_k \, e^{ik\theta}$, one obtains $$D_n(\varphi) = e^{n (\log \varphi)_0} \int_{\mathcal{U}(n)} \exp \left(\sum_{k\neq 0}
(\log \varphi)_k\,{\mathrm{tr}}\,(g^k)\right) dg$$ and after expanding out the exponential, one ends up with the representation $$\label{eq41}
D_n(\varphi) = e^{n(\log \varphi)_0} \int_{\mathcal{U}(n)} \overline{\left(\sum_t \eta_t \, T_t(g)\right)}
\left(\sum_s \eta_s \, T_s(g)\right) dg \ .$$ Here the sums are over all $k$-tuples of non-negative integers $t=(t_1, \dots, t_k)$, $s= (s_1, \dots, s_k)$, and for any $k$, $T_t(g)=\prod^k_{j=1} \left[\,{\mathrm{tr}}\,\left(g^j\right)\right]^{t_j}$, and the $\eta_t$'s, $\eta_s$'s are explicit constants depending on $\{(\log \varphi)_\ell\}$. The magic of the method is that one can use the theory of characters together with Frobenius-Schur-Weyl duality to compute $\int_{\mathcal{U}(n)} \overline{T_t(g)} \, T_s (g) \, dg$ explicitly, obtaining $$\label{eq42}
\int_{\mathcal{U}(n)} \overline{T_t(g)}\, T_s (g) = \delta_{ts}\; W(t)$$ where $W(t)= \prod^k_{j=1} \, j^{t_j}\, t_j!$, provided $\sum^k_{j=1} j\,t_j$ and $\sum^k_{j=1} \, j \, s_j$ are $\le n$. Substituting [\[eq42\]](#eq42){reference-type="eqref" reference="eq42"} into [\[eq41\]](#eq41){reference-type="eqref" reference="eq41"} and controlling the errors as $n\to \infty$, one immediately obtains [\[eq31\]](#eq31){reference-type="eqref" reference="eq31"}.

In the fourth proof, due to Johansson [@Joh1], one rewrites [\[eq40\]](#eq40){reference-type="eqref" reference="eq40"} with $\varphi\! \left(e^{i\theta}\right)
=e^{V(\theta)}$ in the form $$\label{eq43}
D_n \!\left(e^{V}\right) = \frac{1}{n!} \int e^{-2H_n \left(\theta_{0}, \dots, \theta_{n-1}\right)} \: \frac{d\theta_0}{2\pi}
\dots \frac{d\theta_{n-1}}{2\pi}$$ where $$\label{eq44}
H_n = -\frac{1}{2}\sum^{n-1}_{j=0} V(\theta_j) +\frac{1}{2}\sum_{0\le k< j \le n-1}  W\left(\theta_k-\theta_j\right)$$ and $$\label{eq45}
W(\theta) = -\log \left|e^{i\theta}-1\right|^2 \ .$$

This expression exhibits $n! D_n\!\left(e^{V}\right)$ as the partition function of a gas of 1-dimensional particles with 2-dimensional Coulomb interactions --- a "log-gas" in the terminology of Dyson. Dyson introduced this terminology in the context of his analysis [@Dy1] of Circular Ensembles of $n\times n$ random matrices. For such ensembles Dyson found that the distributions of the eigenvalues $\{e^{i\theta_j}\}_{j=0}^{n-1}$, $0\le\theta_j<2\pi$, of the matrices were given by $$\frac{1}{Z_{n,\beta}}\prod_{0\le j<k\le n-1} |  e^{i\theta_j}-e^{i\theta_k} |^\beta \frac{d\theta_0}{2\pi}\cdots
\frac{d\theta_{n-1}}{2\pi}.$$ Here $\beta=1$ for the orthogonal, $\beta=2$ for the unitary, and $\beta=4$ for the symplectic ensemble, and $$\label{partDy}
Z_{n,\beta}=\int_0^{2\pi}\frac{d\theta_0}{2\pi}\cdots \int_0^{2\pi}\frac{d\theta_{n-1}}{2\pi}
\prod_{0\le j<k\le n-1} |  e^{i\theta_j}-e^{i\theta_k} |^\beta$$ is the normalization constant. Dyson then noted that the distribution of the eigenvalues $\{e^{i\theta_j}\}_{j=0}^{n-1}$ was identical with the distribution of the positions $0\le\theta_j<2\pi$, $j=0,\dots,n-1$ of charges in a finite gas with 2-D Coulomb interactions at inverse temperature $\beta$ and with Gibbs measure $\frac{1}{Z_{n,\beta}}\exp\{-\beta H_n(\theta_0,\dots,\theta_{n-1})\} \frac{d\theta_0}{2\pi}\cdots\frac{d\theta_{n-1}}{2\pi}$, where $H_n(\theta_0,\dots,\theta_{n-1})=-\sum_{0\le j<k\le n-1}\log  |  e^{i\theta_j}-e^{i\theta_k} |$, and the partition function is given by [\[partDy\]](#partDy){reference-type="eqref" reference="partDy"}. As emphasized by Dyson [@Dy1], a consequence of this identification is that "...the thermodynamic notions of entropy, specific heat, etc., can be transferred from the Coulomb gas to the eigenvalue series. This will prove very useful, as it gives us a precise and well-understood language in which to describe the statistical properties of the eigenvalues". If the matrices $U$ in the ensembles carry a weight $e^{-\beta\,{\mathrm{tr}}\,Q(U)}$, then the energy in the corresponding Coulomb gas must be replaced by $$H_n(\theta_0,\dots,\theta_{n-1})=-\sum_{0\le j<k\le n-1}\log  |  e^{i\theta_j}-e^{i\theta_k} |+\sum_{j=0}^{n-1}Q(e^{i\theta_j})$$ where $Q$ now plays the role of an external force acting on the charges.

In operational terms, the identification implies, in particular, (see [@Dy2]) that the free energy $F\equiv -\beta^{-1}\log Z_{n,\beta}$ is approximated to leading order as $n\to\infty$ by the classical thermodynamic recipe, $F\sim F_T$, where $$\label{5.1}
\beta F_T=G_2+G_1+G_0.$$ Here $G_2$ is the macroscopic Coulomb energy $$\label{5.2}
G_2=-\frac{\beta}{2}\int\int\sigma(e^{i\theta})\sigma(e^{i\theta'})\log |e^{i\theta}-e^{i\theta'}|d\theta d\theta'+
\beta\int Q(e^{i\theta})\sigma(e^{i\theta})d\theta$$ and $G_1+G_0$ is the local free energy term $$\begin{aligned}
G_1&=\left(1-\frac{\beta}{2}\right)\int\sigma(e^{i\theta})\log\sigma(e^{i\theta})d\theta,\label{5.3}\\
G_0&=n\left[ \left(1-\frac{\beta}{2}\right) \log {2\pi\over n} +\log\Gamma\left(1+\frac{\beta}{2}\right)\right]
-\log\Gamma\left(1+\frac{\beta}{2}n\right).\label{5.4}
\end{aligned}$$ The function $\sigma(e^{i\theta})\ge 0$ is the macroscopic density of the gas and is chosen to minimize the functional on the right-hand side of [\[5.1\]](#5.1){reference-type="eqref" reference="5.1"} subject to the constraint $$\label{6.1}
\int\sigma(e^{i\theta})d\theta=n.$$ Dyson first applied these thermodynamic notions to compute [@Dy2] the probability $P_s$ that there are no eigenvalues for a random matrix in the interval $(0,2s/\pi)$, in the bulk scaling limit where the average distance between the eigenvalues is rescaled to 1, for the Gaussian Unitary Ensemble (see [@Meh]). Using these notions, he derived, for the first time, the leading order of $P_s$, $P_s\sim \exp\{-s^2/2\}$ as $s\to\infty$. (We return to this problem further on (see [\[eq133\]](#eq133){reference-type="eqref" reference="eq133"} et seq).) A year later in [@Dy3], Dyson showed how these notions play out in the context of SSLT. First Dyson noted, as explained above, that the Heine-type representation [\[eq40\]](#eq40){reference-type="eqref" reference="eq40"} immediately displayed $n! D_n\!\left(e^{V}\right)$ as the partition function of a log-gas as in [\[eq43\]](#eq43){reference-type="eqref" reference="eq43"}--[\[eq45\]](#eq45){reference-type="eqref" reference="eq45"} above. This connection between Toeplitz determinants and the Coulomb gas was first pointed out in an unpublished manuscript by G. Kreisel, which was made available to Dyson by courtesy of E. Wigner.[^1]

For $\beta=2$ the term $G_1=0$ and the constant $G_0=-\log n!$, and we have $$F_T=-\frac{1}{2}\int\int\sigma(e^{i\theta})\sigma(e^{i\theta'})\log |e^{i\theta}-e^{i\theta'}|d\theta d\theta'+
\int Q(e^{i\theta})\sigma(e^{i\theta})d\theta-\frac{1}{2}\log n!$$ The constrained minimum is obtained when $$Q(e^{i\theta})- \int\sigma(e^{i\theta'})\log|e^{i\theta}-e^{i\theta'}| d\theta'=\mbox{const}$$ on the unit circle. Solving this equation together with [\[6.1\]](#6.1){reference-type="eqref" reference="6.1"}, Dyson finds that for $Q(e^{i\theta})$ sufficiently smooth, $$F_T=-\frac{1}{2}\log n!+nQ_0-\sum_{k=-\infty}^\infty |k|Q_kQ_{-k}$$ where $\{Q_k\}$ are the Fourier coefficients of $Q(e^{i\theta})$. For $V=-\beta Q=-2 Q$, we obtain $$-\frac{1}{2}\log(n!D_n(e^{V}))=F\sim F_T=-\frac{1}{2}\log n!+nQ_0-\sum_{k=-\infty}^\infty |k|Q_kQ_{-k}$$ which is precisely SSLT, $D_n(e^{V})\sim\exp\{ nV_0+\sum_1^\infty k |V_k|^2\}$. There is an irony in this argument: on the one hand, SSLT was proved in response to a problem in statistical mechanics, but on the other hand, SSLT is obtained here by the methods of statistical mechanics. The above calculation is based on the (unproven) validity of the thermodynamic recipe [\[5.1\]](#5.1){reference-type="eqref" reference="5.1"}--[\[5.4\]](#5.4){reference-type="eqref" reference="5.4"}, [\[6.1\]](#6.1){reference-type="eqref" reference="6.1"}. Johansson's proof in [@Joh1] does not rely on the thermodynamic recipe. The proof in [@Joh1] starts with the identity $D_n(1)=1$ and develops a perturbation theory around $\varphi(z)=1$. Johansson notices that the minimum of the double sum in [\[eq44\]](#eq44){reference-type="eqref" reference="eq44"}, and thus the maximum of the integrand in [\[eq43\]](#eq43){reference-type="eqref" reference="eq43"} for $V\equiv 0$ is reached when the points $e^{i\theta_j}$, $j=0,\dots,n-1$, are uniformly distributed on the unit circle, i.e. when they are the vertices of a regular $n$-gon. For $\varphi(z)=e^{V(z)}\not\equiv 1$, normalize $\varphi$ by requiring $V_0=0$. If one adds the corresponding first sum with $V\not\equiv 0$ to [\[eq44\]](#eq44){reference-type="eqref" reference="eq44"}, the position of the maximum of the integrand in [\[eq43\]](#eq43){reference-type="eqref" reference="eq43"} becomes displaced, but in a sense only slightly if $n$ is large. For large $n$ Johansson introduces the following change of variables in [\[eq43\]](#eq43){reference-type="eqref" reference="eq43"}: $$\label{chvar}
\theta_j=\psi_j-\frac{1}{n}h(e^{i\psi_j}),\qquad j=0,\dots, n-1,$$ where $h(z)=-i\sum_{k=1}^{\infty}(V_k z^k-V_{-k}z^{-k})$ is the conjugate function to $V(z)$. The main contribution to the integral comes from a small neighborhood of a configuration where $\psi_j$'s are uniformly distributed on the unit circle. Due to this crucial fact, all the sums which appear (as a result of the change of variables [\[chvar\]](#chvar){reference-type="eqref" reference="chvar"}) in the exponent, apart from the main one, $\sum_{0\le k<j\le n-1}W(\psi_k-\psi_j)$, can be replaced by integrals with good precision and produce, as $n\to\infty$, the constant [\[eq33\]](#eq33){reference-type="eqref" reference="eq33"}, while the remaining $\frac{1}{n!}\int\exp(-\sum_{0\le k<j\le n-1}W(\psi_k-\psi_j))\prod_{k=0}^{n-1} \frac{d\psi_k}{2\pi}=D_n(1)=1$.

The fifth method is combinatorial and is due basically to Kac [@Kac]. At the start one renormalizes $\varphi\!\left(e^{i\theta}\right)$ so that $\sup_\theta\,\varphi\!\left(e^{i\theta}\right)=1$. Setting $h=1-\varphi$ and $w_\lambda
= 1-\lambda h$, $0\le \lambda\le 1$, we have $w_1= \varphi$. Under the additional assumption that $\inf_\theta\,\varphi
\!\left(e^{i\theta}\right) >0$, we clearly have $0\le h(\theta) \le \sup_\theta\, h(\theta) <1$. Using the identity $\log \det A
= \,{\mathrm{tr}}\,\log A$, one expands $\log D_n \left(1-\lambda h\right)$ for $0\le \lambda\le 1$ in a power series (note that $\|T_n(h)\| \le \|h\|_\infty <1$) $$\begin{aligned}
\label{eq45p}
\log D_n \left(1-\lambda h\right) &= -\sum^\infty_{m=1} \frac{\lambda^m}{m} \,\,{\mathrm{tr}}\,\left( \left[ T_n(h) \right]^m\right)\\
\intertext{and also}
\int \log \left(1-\lambda h\right)\, \frac{d\theta}{2\pi} &= -\sum^\infty_{m=1} \frac{\lambda^m}{m}
\int h^m(\theta)\, \frac{d\theta}{2\pi}\ .
\end{aligned}$$ On the other hand $$\label{eq45n}
\left(\log \left(1-\lambda h\right)\right)_k = - \int e^{-ik\theta} \sum^\infty_{m=1} \frac{\lambda^m}{m}
\, h^m(\theta) \, \frac{d\theta}{2\pi}$$ and so $$\label{eq45nn}
\sum^\infty_{k=1} k \left| \left(\log \left(1-\lambda h\right)\right)_k \right|^2  = \sum^\infty_{m=1}
s_m \, \frac{\lambda^m}{m}$$ where $$s_m = \sum^\infty_{k=1} k \sum^{m-1}_{\ell=1} \frac{m}{\ell (m-\ell)} \left(\int e^{-ik\theta}
\, h^\ell (\theta) \, \frac{d\theta}{2\pi} \right) \left(\int e^{ik\theta} \, h^{m-\ell}(\theta)\,
\frac{d\theta}{2\pi}\right).$$ Thus the strategy is to show $$\label{eq45pp}
\lim_{n\to\infty} - \left[ \,{\mathrm{tr}}\,\left(\left[T_n (h)\right]\right)^m -n \int h^m(\theta) \,\frac{d\theta}{2\pi} \right]=s_m.$$ Combinatorial issues arise when one tries to control the complicated multilinear sums in $\,{\mathrm{tr}}\,\left[T_n(h)\right]^m$.

The sixth method is based on a formula of Baik, Deift, McLaughlin, and Zhou (unpublished) for relative determinants $$\label{eq45ppp}
\log \frac{D_n \left(\varphi \psi\right)}{D_n \left(\psi\right)} = \int^1_0 dt \int_0^{2\pi}
\left[ \frac{d}{dt} \log \varphi_t\right] K_t(\theta) \, \varphi_t(\theta) \, \frac{d\theta}{2\pi}$$ where $\varphi$ and $\psi$ are two functions on $S^1$ and $\varphi_t = (1-t)+t\varphi$ and $K_t(\theta)$ is the *Christoffel-Darboux* kernel $$\label{eq45-4}
K_t(\theta) = \sum^{n-1}_{j=0} \left|p_j\!\left(e^{i\theta}, \, \varphi_t \, \psi\right)\right|^2$$ and $p_j\!\left(e^{i\theta},\, \varphi_t\, \psi\right)$ are the OPUC's associated with the weight $\varphi_t\!\left(e^{i\theta}\right) \psi\!\left(e^{i\theta}\right) \frac{d\theta}{2\pi}$. SSLT then follows by computing the (weak) limit of $\frac{1}{n} \, K_t(\theta)$ as $n\to \infty$. Thus, as in the first method, SSLT is seen here as following from properties of OPUC's $p_j\!\left(e^{i\theta}\right)$.

The mathematical challenge that is posed by SSLT can be viewed as follows. In functional analysis one commonly considers continuous maps $F$, say, from one fixed topological space $X$ to another fixed topological space $Y$. Then in order to verify that $\lim_{n\to\infty} F(x_n) = F(x)$ all one has to do is verify that $x_n \to x$ as $n\to\infty$ in the topology of $X$. In particular, if $X$ is the space of trace class operators on a separable Hilbert space $\mathcal{H}$, and $F(x)= \det
\left(1+x\right)$, then $F:X\to Y= \mathbb{C}$ and $\lim_{n\to\infty} \,\det \left(1+x_n\right) = \det \left(1+x\right)$ if $x_n\to x$ in trace norm. But SSLT is not of this standard type. Instead, one has $F:M(n, \mathbb{C})
\to \mathbb{C}$ taking $A_n \in M(n, \mathbb{C})$ to $F\!\left(A_n\right) = \det A_n$. So the initial space $X=X_n
=M(n,\mathbb{C})$ is changing with $n$ and it is not at all clear how to topologize the situation so that "$\lim_n F\!\left(A_n\right) = F\!\left(\lim A_n\right)$". If, for example, we let $X=M(\infty, \mathbb{C})$ be the inductive limit of the $M(n, \mathbb{C})$'s, then $T_n(\varphi)$ converges to the Toeplitz operator $T(\varphi)$ in the associated topology, but $T(\varphi)$ is not of the form $1+ \text{ trace class}$, and so $F\!\left(T(\varphi)\right) = \det\!\left(T(\varphi)\right)$ is not defined. In such situations when $X= X_n$, or $Y=Y_n$, is varying, there is no general procedure to follow and each problem must be addressed on an ad hoc basis. And when there is no preferred path to the solution of a problem, there are many paths, as we see from the six very different methods above. In this regard, the method of Borodin-Okounkov-Geronimo-Case is singled out: after factoring out $e^{n(\log\varphi)_0+E(\varphi)}$, one has $$\label{eq45-5}
\frac{\det \left(T_n (\varphi)\right)}{e^{n(\log\varphi)_0+E(\varphi)}} = \det\left(1-B_n\right)$$ where $B_n=Q_n\, H(b)\, H(\widetilde{c})\, Q_n$ is trace class in $\ell^+_2$ and $B_n\to 0$ in trace norm as $n\to\infty$. In other words, one of the paths is to renormalize the problem so that it assumes the standard form.

This pathway, to reduce SSLT to standard form, goes back to Harold Widom, who was the first to apply operator-theoretic methods to the problem of Toeplitz asymptotics. In [@Wid4], Widom gave yet another proof of [\[eq31\]](#eq31){reference-type="eqref" reference="eq31"}. This proof, which was found more than 35 years ago, has not lost its charm. We follow the presentation in [@Bott1]. It turns out that by a simple trick, the determinants of finite sections of the inverse Toeplitz operator $T(\varphi)^{-1}$ are easy to compute, $$\label{eq46}
\det P_n \, T(\varphi)^{-1}\, P_n = e^{-n(\log\varphi)_0}$$ where $P_n$ projects $u= \left(u_0, u_1, \dots, u_{n-1}, u_n, \dots \right) \in \ell^+_2$ to $\left(u_0,
u_1, \dots, u_{n-1}\right) \in \mathbb{C}^n$. Simple algebra shows that $$\label{eq46-1}
\begin{aligned}
\det T_n(\varphi) = & \det P_nT(\varphi)P_n=\det\!\left( P_n \, T^{-1} \left(\varphi^{-1}\right) P_n\right)\\
& \times \det\!\left(1+ \left(P_n \, T^{-1} \left(\varphi^{-1}\right) P_n\right)^{-1} \, P_n\,K\,P_n\right)
\end{aligned}$$ where $K\equiv T(\varphi)- T^{-1} \left(\varphi^{-1}\right)$ is trace-class. By [\[eq46\]](#eq46){reference-type="eqref" reference="eq46"}, $$\label{eq46-2}
\det P_n \, T^{-1} \left(\varphi^{-1}\right)P_n = e^{n(\log\varphi)_0}.$$ But $\left(P_n \, T^{-1} \left(\varphi^{-1}\right)P_n \right)^{-1} \, P_n$ can be shown to converge strongly as $n\to\infty$ in $\ell^+_2$ to $\left(T^{-1} \left(\varphi^{-1}\right)\right)^{-1} = T\left(\varphi^{-1}\right)$, and as $K$ is trace class, $R_n \equiv \left(P_n\, T^{-1} \left(\varphi^{-1}\right)P_n\right)^{-1} \, P_n \,
K\,P_n \to T\left(\varphi^{-1}\right)K$. We conclude that as $n\to\infty$ $$\label{eq46-3}
\frac{\det T_n(\varphi)}{e^{n(\log\varphi)_0}} = \det\!\left(1+R_n\right) \to \det\!\left(1 + T\left(\varphi^{-1}\right)K\right)
= \det\,T\left(\varphi^{-1}\right) T(\varphi).$$ Using the remarkable Helton-Howe-Pincus formula (see [@HeltHow]), $\det\!\left(e^A\, e^B\, e^{-A}\, e^{-B}\right)=e^{\mathrm{tr} [A,B]}$, if $A$, $B$ are bounded, and $[A,B]= AB-BA$ is trace class, one then shows that $\det \!\left(T\left(\varphi^{-1}\right)T(\varphi)\right) =e^{E(\varphi)}$, and [\[eq31\]](#eq31){reference-type="eqref" reference="eq31"} is proved.

Of all the methods to prove SSLT, perhaps the simplest and most direct was introduced by Basor and Helton in [@BasHelt]. As in [@Wid4], the method also proceeds by reducing SSLT to standard form. We follow [@BasHelt]: Suppose $\varphi$ has a Wiener-Hopf factorization $\varphi=\varphi_+\varphi_-$, where $\varphi_+$, $\varphi_+^{-1}$ are bounded analytic functions in $\{|z|<1\}$, and $\varphi_-$, $\varphi_-^{-1}$ are bounded analytic functions in $\{|z|>1\}$. Then by direct calculation, the Toeplitz operator $T(\varphi)$ has a factorization $T(\varphi)=T(\varphi_-)T(\varphi_+)$, furthermore, $$P_nT(\varphi_+)=P_nT(\varphi_+)P_n,\qquad T(\varphi_-)P_n=P_nT(\varphi_-)P_n.$$ As $T(\varphi_\pm)T(\varphi_\pm^{-1})=1$, we see that $T(\varphi_\pm)^{-1}$ exist and $T(\varphi_\pm)^{-1}=T(\varphi_\pm^{-1})$. We thus have $$P_nT(\varphi)P_n=P_nT(\varphi_+)P_nT(\varphi_+)^{-1}T(\varphi_-)T(\varphi_+)T(\varphi_-)^{-1}P_nT(\varphi_-)P_n$$ so that $$\begin{aligned}
D_n(\varphi)=&\det\!\left(P_nT(\varphi_+)P_n\right)\det\!\left(P_n\left\{T(\varphi_+)^{-1},T(\varphi_-)\right\}P_n\right)
\det\!\left(P_nT(\varphi_-)P_n\right)\\
=& \left((\varphi_+)_0(\varphi_-)_0\right)^n\det\!\left(P_n\left\{T(\varphi_+)^{-1},T(\varphi_-)\right\}P_n\right)
\end{aligned}$$ where $\left\{T(\varphi_+)^{-1},T(\varphi_-)\right\}= T(\varphi_+)^{-1}T(\varphi_-)T(\varphi_+)T(\varphi_-)^{-1}$ is the multiplicative commutator. However $\left\{T(\varphi_+)^{-1},T(\varphi_-)\right\}=1+T(\varphi_+)^{-1}\left[T(\varphi_-),T(\varphi_+)\right]T(\varphi_-)^{-1}$ and under mild smoothness conditions on $\varphi(e^{i\theta})$, the commutator $\left[T(\varphi_-),T(\varphi_+)\right]=T(\varphi_-)T(\varphi_+)-T(\varphi_+)T(\varphi_-)$ is trace class. For such $\varphi$, $\det\!\left(P_n\left\{T(\varphi_+)^{-1},T(\varphi_-)\right\}P_n\right)$ is equal to the Fredholm determinant $$\det\!\left(1+P_nT(\varphi_+)^{-1}\left[T(\varphi_-),T(\varphi_+)\right]T(\varphi_-)^{-1}P_n\right)$$ which converges by abstract theory as $n\to\infty$ to $$\begin{aligned}
\det\!\left(1+T(\varphi_+)^{-1}\left[T(\varphi_-),T(\varphi_+)\right]T(\varphi_-)^{-1}\right)=&
\det\!\left\{T(\varphi_+)^{-1},T(\varphi_-)\right\}\\
=&\det\!\left(T(\varphi_+)^{-1}T(\varphi_-)T(\varphi_+)T(\varphi_-)^{-1}\right)\\
=&\det\!T(\varphi^{-1})T(\varphi).
\end{aligned}$$ Again by the Helton-Howe-Pincus formula, we have $$\lim_{n\to\infty} \frac{D_n (\varphi)}{e^{n(\log\varphi)_0}} =\det\!T(\varphi^{-1})T(\varphi)=e^{E(\varphi)}$$ which proves SSLT under mild assumptions on $\varphi$ (see [@BasHelt] Theorem 2.1.).

In [@Dei1], the author gives yet another proof of [\[eq31\]](#eq31){reference-type="eqref" reference="eq31"} by expressing $D_n(\varphi)$ as a Fredholm determinant of the following form: $$\label{D1}
D_n(\varphi) = \det \left(1-V_n\right)$$ where $V_n$ is a trace class operator acting on $L^2(S^1)$ $$\begin{aligned}
\label{D2}
V_n \, f(z) &= \int_{|z'|=1} V_n \left(z, z'\right) f\left(z'\right) dz' \ , \qquad |z|=1,
\\
\intertext{with}\label{D3}
V_n \left(z, z'\right) &= \frac{z^n \left(z'\right)^{-n} - 1}{z-z'} \; \frac{1-\varphi \left(z'\right)}{2\pi i}\ .
\end{aligned}$$ The operator $V_n$ is oscillatory and does not converge as $n\to\infty$ in the trace-norm topology. However, $V_n$ has the special form of an *integrable operator*, that is, operators with kernels of the form $\sum_{j=1}^m\frac{f_j(z)g_j(z')}{z-z'}$, with $z$, $z'$ on some contour $\Gamma$ in $\mathbb{C}$, $m<\infty$, and $f_j$, $g_j$ are given functions on $\Gamma$. Such operators were first singled out as a distinguished class by Its, Izergin, Korepin and Slavnov[^2] (see [@Dei1] for a pedagogic presentation). Associated with the integrable operators there is a canonical Riemann-Hilbert Problem, which, in this case, is of oscillatory type. Such problems can be analyzed asymptotically by applying the nonlinear steepest descent method for Riemann-Hilbert Problems introduced by Deift and Zhou in [@DZ], and further developed in [@DVZ], and SSLT then follows (see [@Dei1]).

::: remark
[]{#22+++ label="22+++"} In the methods of Widom and Basor-Helton the existence of the limit of $\frac{D_n(\varphi)}{e^{n(\log\varphi)_0}}$ as $n\to\infty$ follows directly from general theorems in functional analysis: the identification of the limit with $e^{E(\varphi)}$ is a separate matter and uses other means (Helton-Howe-Pincus). The situation is similar regarding Szegő's original proof of SSLT (see [@Sz3] [@GreSz]): as $\varphi(e^{i\theta})>0$, the ratio $\frac{D_n(\varphi)}{e^{n(\log\varphi)_0}}$ is monotone increasing in $n$, so the existence of the limit (which may, a priori, be infinite) is immediate. Again the evaluation of the limit is a separate matter. Indeed, Szegő first computes the limit for a dense class of symbols $\{\widetilde\varphi\}$ for which $D_n(\widetilde\varphi)$ can be evaluated explicitly for $n$ sufficiently large, $n>n_\varphi$, and then obtains the general result by an approximation argument $\widetilde\varphi\to\varphi$.

By contrast, all the other methods we have described above prove the existence of the limit, and compute its value, both at the same time.
:::

We return now briefly to the 2-dimensional Ising model. One notes that Szegő's Theorem [\[theorem3\]](#theorem3){reference-type="ref" reference="theorem3"} does not actually apply to $\varphi_{\text{diag}}(\theta)$, say, in [\[eq28\]](#eq28){reference-type="eqref" reference="eq28"}, because the symbol is not real valued. Moreover, Szegő's proof of [\[eq31\]](#eq31){reference-type="eqref" reference="eq31"} depends in a crucial way on the positivity of $\varphi\!\left(e^{i\theta}\right)$ (see Remark [\[22+++\]](#22+++){reference-type="ref" reference="22+++"} above), and it was not at all clear at the time how to extend Theorem [\[theorem3\]](#theorem3){reference-type="ref" reference="theorem3"} to non-real symbols $\varphi$. So Onsager's lament that "...the mathematicians got there first", was in fact not true! The result in the 1950 unpublished draft of Kaufman and Onsager mentioned above, without "the epsilons and deltas and all of that", but allowing for non-real $\varphi$, was in fact the first to break the tape! Now although the symbol $\varphi_{\text{diag}} (\theta)$ is not real, for $0 <k_{\text{ons}} <1$ however, $\log\varphi_{\text{diag}} (\theta)$ is still smooth on $S^1$, in particular, the winding number of $\varphi_{\text{diag}} (\theta)$ on $S^1$ is zero. The first result for such symbols was proved by G. Baxter in 1963 [@BaxG2]. He showed that under certain technical conditions, if $\varphi\!\left(e^{i\theta}\right)$ is smooth, non-zero, and has zero winding number on $S^1$, then $$\label{eq47}
\lim_{n\to\infty} \frac{D_n (\varphi)}{e^{n(\log\varphi)_0}} =e^{\sum^\infty_{k=1}\, k \left(\log \varphi\right)_k
\left(\log \varphi\right)_{-k}}.$$ Note that for $\varphi_{\text{diag}}(\theta)$ in [\[eq28\]](#eq28){reference-type="eqref" reference="eq28"}, one has for $0<k_{\text{ons}} <1$, $\left(\log \varphi_{\text{diag}}\right)_\ell =  (\mbox{sgn } \ell) \, k^{|\ell|}_{\text{ons}}/ 2 |\ell|$ for $\ell \neq 0$ and $\left(\log \varphi_{\text{diag}}\right)_0=0$. Hence $\sum^\infty_{\ell=1} \ell
\left(\log \varphi\right)_{\ell} \left(\log \varphi\right)_{-\ell} = -\frac{1}{4}
\sum^\infty_1 \frac{\left(k^2_{\text{ons}} \right)^\ell}{\ell} = \frac{1}{4} \;\log \left(1-k^2_{\text{ons}}\right)$, which yields [\[eq15\]](#eq15){reference-type="eqref" reference="eq15"} via [\[eq29\]](#eq29){reference-type="eqref" reference="eq29"}.

In retrospect, many of the proofs of SSLT do extend directly to complex-valued symbols with smooth logarithm. This is true, in particular, for Kac's proof of [\[eq31\]](#eq31){reference-type="eqref" reference="eq31"} in 1954 [@Kac], as noted by Montroll, Potts and Ward in [@MPW] (see footnote 17, p. 316). Moreover, the proofs in [@Wid4] and in the text [@BottSilb3], for example, are all designed from the very beginning to cover complex-valued functions.

If $\varphi(e^{i\theta})$ is non-zero and continuous, say, on $S^1$, and has zero winding number, then $\varphi(e^{i\theta}) = e^{V(e^{i\theta})}$ for some continuous, periodic function $V(e^{i\theta})
=\log\varphi(e^{i\theta})$. The strongest version of SSLT with complex symbols $\varphi(e^{i\theta})$ is the following.

::: theorem
[]{#theorem7 label="theorem7"} Let $V(e^{i\theta})\in L^1(S^1)$ be a (possibly complex-valued) function on $S^1$ with Fourier coefficients $\left(V_k\right)_{k\in \mathbb{Z}}$ satisfying $$\label{eq48}
\sum^\infty_{k=-\infty} |k| \; \left|V_k\right|^2 < \infty \ ,$$ then $$\label{eq49}
\lim_{n\to\infty} \frac{D_n\!\left(e^V\right)}{e^{nV_0}}=
e^{\sum^\infty_1 k\, V_k\, V_{-k}}.$$ $\Box$
:::

Note that for $V(e^{i\theta})$ satisfying [\[eq48\]](#eq48){reference-type="eqref" reference="eq48"}, $e^{V(e^{i\theta})} \in L^p\!\left(S^1, \frac{d\theta}{2\pi}\right)$ for $1 \le p < \infty$ (see [@Sim2]). The proof of Theorem [\[theorem7\]](#theorem7){reference-type="ref" reference="theorem7"} is given by Johansson [@Joh1]. In particular, his argument for the extension of the result to complex-valued $V(z)$ proceeds by considering the analytic functions $$g_n (z) = D_n\!\left(e^{\left(\Re V + z \Im V\right)}\right)\bigl/ e^{n \left[(\Re V)_0 + z (\Im V)_0\right]}$$ and applying Vitali's Theorem. When $z$ is real, $\lim_{n\to\infty} g_n(z)$ is given by [\[eq47\]](#eq47){reference-type="eqref" reference="eq47"}, and to obtain [\[eq49\]](#eq49){reference-type="eqref" reference="eq49"} one just sets $z=i$.

Under the additional assumption that $V$ is in $L^\infty(S^1)$, Theorem [\[theorem7\]](#theorem7){reference-type="ref" reference="theorem7"} was already established in [@Wid4]. We also note that condition [\[eq48\]](#eq48){reference-type="eqref" reference="eq48"} can be replaced by certain "non-symmetric" requirements on the decay of the Fourier coefficients $V_k$ and $V_{-k}$, $k\ge  0$; see, for example, Theorem 10.32 and Corollary 10.42 of [@BottSilb3].

::: remark
[]{#remark3 label="remark3"} In [@Joh1], Johansson observes the following very interesting consequence of Theorem [\[theorem7\]](#theorem7){reference-type="ref" reference="theorem7"} (see also [@Joh2]). Let $V(e^{i\theta})$ be a real-valued function on $S^1$ with Fourier coefficients $\{V_k\}$ satisfying [\[eq48\]](#eq48){reference-type="eqref" reference="eq48"} and suppose $V_0= \int V(e^{i\theta}) \;\frac{d\theta}{2\pi} =0$. As in the Bump-Diaconis method for SSLT described above, equip the unitary group $\mathcal{U}(n)$ with Haar measure $dg$ and consider the random variable $F_n(g)=\sum^{n-1}_{j=0} V\left(e^{i\theta_j (g)}\right)=\,{\mathrm{tr}}\,V(g)$, where $\left\{e^{i\theta_j (g)}\right\}$ are the eigenvalues of $g \in \mathcal{U}(n)$. Then we have the following Central Limit Theorem: $$\label{eq51}
F_n  \text{ converges in distribution to } N\!\left(0, \sigma^2\right),\qquad \sigma= \left(2 \sum^\infty_{k=1}
\, k\left|V_k\right|^2\right)^{\frac{1}{2}}$$ where $N\!\left(0, \sigma^2\right)$ denotes the normal distribution with mean zero and variance $\sigma$. Indeed, for any real $t$ we have $$\int_{\mathcal{U}(n)} e^{i\,t\,F_n(g)}\, dg = D_n \!\left(e^{i\,t\,V}\right)$$ and so by Theorem [\[theorem7\]](#theorem7){reference-type="ref" reference="theorem7"}, as $n\to\infty$ $$\int_{\mathcal{U}(n)} e^{i\,t\,F_n(g)} \, dg \to e^{\sum^\infty_1\, k (itV)_k \: (itV)_{-k}}= 
e^{-\frac{t^2}{2} \left[2\left(\sum^\infty_1 k|V_k|^2\right)\right]}$$ from which we conclude [\[eq51\]](#eq51){reference-type="eqref" reference="eq51"}. One notes that as opposed to the standard Central Limit Theorem for independent random variables, the $\theta_j$'s are very strongly uniformly distributed and no $n^{-1/2}$ scaling is needed. A suitable scaling is needed in the more general "interpolating" situation considered by Duits and Johansson [@DJ] where $V(z)$ depends on $n$ (cf. Section [\[sec-ds\]](#sec-ds){reference-type="ref" reference="sec-ds"}). In [@DJ], for each $n\ge 1$, the authors consider sequences $\{ k_j(n)\}_{j\ge 1}$ of mutually distinct positive integers, and they show that for each $m\ge 1$, the random variables $\frac{1}{\sqrt{\min(k_j(n),n)}}\,{\mathrm{tr}}\,g^{k_j(n)}$, $j=1,\dots, m$, converge to independent standard complex normals. (This connects earlier results of Diaconis and Shahshahani for fixed $k_j$, and of Rains for $k_j(n)>n$: see [@DJ] for references.) Note an interesting difference in scaling for $k_j(n)\le n$ and for $k_j(n)>n$. In the latter case, the scaling is $n^{-1/2}$. The authors in [@DJ] obtained their results by proving an analogue of SSLT for symbols depending on $n$ in a special way, as follows. If $$V(n;z)=\sum_{|j|>0}\frac{\gamma_j z^{k_j(n)}}{\sqrt{\min(|k_j(n)|,n)}},$$ where $\sum_j|\gamma_j|<\infty$, the sequences $\{k_j(n)\}_{j\ge 1}$ are as above, and $k_{-j}(n)=-k_j(n)$, then $$\lim_{n\to\infty}D_n(e^{V(n;z)})=e^{\sum_{j=1}^{\infty}\gamma_j\gamma_{-j}}.$$
:::

[^1]: We note that already in the 1880's Stieltjes gave an electrostatic interpretation of the zeros of certain classical orthogonal polynomials (see [@Sz5], Section 6.7). For a discussion of logarithmic potentials from the viewpoint of potential theory, see the book of Saff and Totik [@SaTo].

[^2]: Some of the elements of the theory of integrable operators were already present in the earlier work [@Sakh].

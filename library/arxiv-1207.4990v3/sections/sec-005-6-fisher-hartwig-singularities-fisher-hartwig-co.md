---
doc_id: arxiv-1207.4990v3
doc_title: "Toeplitz matrices and Toeplitz determinants under the impetus of the Ising model. Some history and some recent results"
section_id: sec-005-6-fisher-hartwig-singularities-fisher-hartwig-co
section_title: "Fisher-Hartwig singularities. Fisher-Hartwig conjecture"
section_number: 6
pages: 29-36
source_pdf: 1207.4990v3.pdf
source_sha256: 02aa065f4f65b857
toc_source: outline
text_source: latex
latex_prose_ratio: 0.957
latex_coverage_ratio: 0.996
doc_brief: "Toeplitz matrices and Toeplitz determinants under the impetus of the Ising model. Some history and some recent results — 12 sections: Front matter; Setting the problem; Toeplitz meets Ising"
---
[]{#sectionFH label="sectionFH"} In addition to the new questions and challenges raised in Toeplitz theory by the Ising model for $T\ge T_c$, other kinds of singularities also began to appear. For example, in 1964, in his work on the ground state of the one-dimensional system of impenetrable bosons [@Len1] Lenard expressed the one-particle density matrix for the system as a Toeplitz matrix with a symbol $\varphi\!\left(e^{i\theta}\right)$ that vanished at some points on $S^1$ (see [\[eq81\]](#eq81){reference-type="eqref" reference="eq81"} and particularly Remark [\[Lenard\]](#Lenard){reference-type="ref" reference="Lenard"} below for further discussion). In 1968, in a major step in the development and generalization of SSLT, Fisher and Hartwig [@FisHart1] introduced a class of singular symbols for Toeplitz determinants, that allowed for zeros, (integrable) singularities, discontinuities and non-zero winding numbers.

The symbols of Fisher-Hartwig (FH) class have the following form (we use the notation in [@DIK1]) $$\label{eq74}
f(z) =e^{V(z)} \, z^{\sum^m_{j=0} \, \beta_j} \prod^m_{j=0} \left|z-z_j\right|^{2\alpha_j} \, g_{z_j,\, \beta_j}
\, (z) \, z_j^{-\beta_j}, \qquad  z=e^{i\theta},\quad 0 \le \theta<  2\pi,$$ for some $m=0, 1, 2, \dots,$ where $$\begin{aligned}
&z_j = e^{i\,\theta_j}, \qquad j=0,1,\dots, m, \qquad 0=\theta_0 < \theta_1 < \dots < \theta_m < 2\pi,
\label{eq75}\\
&g_{z_j\, \beta_j} (z) \equiv g_{\beta_j}(z) = \left\{
\begin{aligned}
e^{i\pi\beta_j}, \qquad &0 \le \arg \;z< \theta_j \ ,\\
e^{-i\pi\beta_j}, \qquad &\theta_j \le \arg \;z < 2\pi,
\end{aligned} \right. 
\label{eq76}\\
&\Re\alpha_j >-\frac{1}{2}, \qquad \beta_j \in \mathbb{C}, \qquad j=0, 1, \dots, m,
\label{eq77}
\end{aligned}$$ and $V\!\left(e^{i\theta}\right)$ is a sufficiently smooth function on $S^1$. Here the condition on $\Re\alpha_j$ insures integrability. Note that a Fisher-Hartwig singularity at $z_j, \;\;j=1, \dots, m$, consists of a root-type singularity $$\label{eq78}
\left|z-z_j \right|^{2\alpha_j} = \left| 2\sin \frac{\theta-\theta_j}{2}\right|^{2\alpha_j}$$ and a jump singularity $z^{\beta_j}\, g_{\beta_j} (z)$ at $z_j$ (observe that $z^{\beta_j} \, g_{\beta_j}(z)$ is continuous at $z=1$ for $j\neq 0$). For $j=0$, $z_0=1$, in addition to the root-type singularity [\[eq78\]](#eq78){reference-type="eqref" reference="eq78"} at $\theta_0=0$, one has $g_{z_0,\, \beta_0}(z) =e^{-i\pi \beta_0}$, $0\le \theta< 2\pi$ and so $z^{\beta_0}\; g_{z_0, \, \beta_0}(z)
= e^{i \,(\theta-\pi)\,\beta_0}, \; 0 \le \theta< 2\pi$, has a jump at $z=z_0=1$. The factors $z_j^{-\beta_j}$ are singled out to simplify comparison with the existing literature, in particular, [@FisHart1].

Here are some examples of FH symbols:

-   If $f\!\left(e^{i\theta}\right) =-i$ for $0 \le \theta<\pi$ and $+ i$ for $\pi \le \theta< 2\pi$ (cf [@BasTr]), then $z_0=1$, $z_1=-1=e^{i\pi}$, $\alpha_0 = \alpha_1=0$, $\beta_0 =\frac{1}{2}$ and $\beta_1=-\frac{1}{2}$, and $$\begin{aligned}
    f\!\left(e^{i\theta}\right) &= z^{\beta_0 + \beta_1} \; g_{1,\, \frac{1}{2}} (z) \;g_{-1, -\frac{1}{2}}(z)
    \; z_0^{-\beta_0} \; z_1^{-\beta_1} \\
    &= g_{1,\, \frac{1}{2}}(z)\; g_{-1, -\frac{1}{2}}(z) \; e^{i\pi/2}
    \end{aligned}$$

-   If $f\!\left(e^{i\theta}\right)$ is a sufficiently smooth function on $S^1$ (in particular, a trigonometric polynomial) with two zeros at $0 < \theta_1 < \theta_2 < 2\pi$ (cf [@BGrM], [@DIK2]), then with $z_1=e^{i\theta_1}$, $z_2=e^{i\theta_2}$, $\alpha_1=\alpha_2=1/2$, $\beta_1=\frac{1}{2}$, $\beta_2=-\frac{1}{2}$, $$\label{eqBG}
    \begin{aligned}
    f(z) &= e^{V(z)} \; z^{\beta_1 + \beta_2}\; \left|z-z_1\right| \left|z-z_2\right|\, g_{z_1,\; \frac{1}{2}} (z)
    \; g_{z_2, \, -\frac{1}{2}}(z) \left(\frac{z_1}{z_2}\right)^{-\frac{1}{2}} \\
    &= e^{V(z)} \,\left|z-z_1\right| \left|z-z_2\right| \, g_{z_1, \,\frac{1}{2}}(z) \; g_{z_2,\,-\frac{1}{2}}(z)
    \left(z_1/z_2\right)^{-\frac{1}{2}}
    \end{aligned}$$ for a suitable function $V\!\!\left(e^{i\theta}\right)$ on $S^1$.

-   The following symbol arose in Lenard's work in [@Len1] on impenetrable bosons mentioned above, $$\label{eq81}
    f\!\left(e^{i\theta}\right) = \left|z-e^{i\theta_1}\right| \left|z-e^{i\theta_2}\right|$$ where $\theta_1 \neq \theta_2\,(\text{mod } 2\pi)$. Here $z_1=e^{i\theta_1}$, $z_2=e^{i\theta_2}$, $\alpha_1=\alpha_2=1/2$ and $\beta_1=\beta_2=0$.

-   For the Ising model at $T< T_c$, the winding number of $\varphi_{\text{ons}}\!\left(e^{i\theta}\right)$ is zero and so $\varphi_{\text{ons}}
    (z) = e^{V(z)}$ for a suitable smooth function $V\!\!\left(e^{i\theta}\right)$ on $S^1$. For $T=T_c$, we have from [\[eq25\]](#eq25){reference-type="eqref" reference="eq25"} with $0< \gamma_1 < 1$, $$\label{eq82}
    \begin{aligned}
    \varphi_{\text{ons}}\! \left(e^{i\theta}\right) &=  \frac{1-\gamma_1 \, e^{i\theta}}{\left|1-\gamma_1 \, e^{-i\theta}\right|} \quad i\,e^{-i\theta/2},
    \qquad  0\le \theta< 2\pi,\\
    &= e^{V(z)} \; z^{\beta_0} \; g_{z_0, \, \beta_0}(z) \, z_0^{-\beta_0}
    \end{aligned}$$ where $z_0=1$, $\alpha_0=0$, $\beta_0=-\frac{1}{2}$ and $V\!\left(e^{i\theta}\right)$ is smooth on $S^1$. For $T>T_c$, we have from [\[eq24\]](#eq24){reference-type="eqref" reference="eq24"} with $0 < \gamma_1 <1< \gamma_2$, $$\label{106}
    \begin{aligned}
    \varphi_{\text{ons}} \!\left(e^{i\theta}\right) &= \frac{\left(1-\gamma_1\, e^{i\theta}\right) \left(\gamma_2-e^{i\theta}\right)}{\left|1-\gamma_1 \,e^{-i\theta}\right|
    \left|1-\gamma_2 \,e^{i\theta}\right|} \left(-e^{-i\theta}\right) \\
    &= e^{V(z)} \, z^{\beta_0}\, g_{z_0, \, \beta_0}(z) \, z_0^{-\beta_0}
    \end{aligned}$$ where $z_0=1$, $\alpha_0=0$, $\beta_0=-1$ and again $V(z)$ is smooth on $S^1$.

From the point of view of Toeplitz determinants with FH singularities, Wu was the first to obtain [@Wu] detailed asymptotic results for symbols with discontinuities as in [\[eq82\]](#eq82){reference-type="eqref" reference="eq82"} and for symbols with non-zero winding as in [\[106\]](#106){reference-type="eqref" reference="106"}. Lenard was the first to obtain [@Len1] [@Len2] detailed asymptotic results for symbols which have zeros on $S^1$ as in [\[eq81\]](#eq81){reference-type="eqref" reference="eq81"}. For symbols [\[eq74\]](#eq74){reference-type="eqref" reference="eq74"} with $\beta_j=0$ and $\alpha_j$ real, $\alpha_j>-\frac{1}{2}$, $j=0, \dots, m$, Lenard made a general conjecture [@Len2][^1] about the asymptotic form of $D_n(f)$, $$\label{eq83} 
D_n(f) \sim E\left(e^V, \, \alpha_0, \dots, \alpha_m, \, \theta_0, \dots, \theta_m\right) n^{\sum^m_{j=0} \alpha_j^2}
\, e^{n V_0}$$ as $n\to\infty$, where $V_0=\frac{1}{2\pi} \int^{2\pi}_0 V\!\left(e^{i\theta}\right)d\theta$ as in [\[eq32\]](#eq32){reference-type="eqref" reference="eq32"} [\[eq49\]](#eq49){reference-type="eqref" reference="eq49"}, and $E\!\left(f, \, \alpha_0, \dots, \alpha_m, \theta_0, \dots, \theta_m\right)$ is some (unspecified) constant. Moreover he was able to verify this conjecture for the case $f\!\left(e^{i\theta}\right)=\left|z-e^{i\,\theta_1}\right|
\left|z-e^{i\theta_2}\right|$ in [\[eq81\]](#eq81){reference-type="eqref" reference="eq81"}.

::: remark
[]{#Lenard label="Lenard"} As noted above, the symbol [\[eq81\]](#eq81){reference-type="eqref" reference="eq81"} arose in Lenard's study of impenetrable bosons [@Len1]. More precisely, Lenard considered $N$ free bosons in one dimension confined to a box of length $L$ with periodic boundary conditions and lying in the (symmetric) ground state of the system. According to the criterion of Penrose and Onsager [@PenOns], Bose-Einstein condensation takes place if the largest eigenvalue $\lambda_{N,L}^{(\mathrm{max})}$ of the density matrix $\rho_{N,L}(x,x')$ for the system is of order $N$ as $N\sim L\to\infty$. For the system at hand $\rho_{N,L}$ is translation invariant, $\rho_{N,L}(x,x')=\rho_{N,L}(x-x')$, so that the eigenvalues of $\rho_{N,L}$ are just the Fourier coefficients $\rho_{N,L}^{(n)}$ of $\rho_{N,L}(\cdot)$. A simple calculation shows that $\lambda_{N,L}^{(\mathrm{max})}=\rho_{N,L}^{(0)}$, the zeroth Fourier coefficient. Writing $\rho_{N,L}(\xi)=\frac{1}{L}R_N(2\pi\xi/L)$, we have that $$\label{r34-1}
\frac{\lambda_{N,L}^{(\mathrm{max})}}{N} =\frac{1}{2\pi N}\int_{-\pi}^{\pi}R_N(t)dt.$$ (Note that in this case $\lambda_{N,L}^{(\mathrm{max})}$ is actually independent of $L$.) Now it turns out that $$\label{34p3}
R_N(t)=D_{N-1}(f_t)$$ where $f_t$ is precisely a symbol of type [\[eq81\]](#eq81){reference-type="eqref" reference="eq81"}, $$\label{Lensym}
f_t\left(e^{i\theta}\right)=\left|e^{i\theta}-e^{it/2}\right|\,\left|e^{i\theta}-e^{-it/2}\right|.$$ (Formula [\[34p3\]](#34p3){reference-type="eqref" reference="34p3"} was also obtained independently by Dyson, see [@Len1].) At that point (April 10, 1963, according to a letter Lenard has kindly made available to the authors) Lenard asked Szegő for help in evaluating the Toeplitz determinant $D_{N-1}(f_t)$. On July 10, three months later, Szegő wrote back to Lenard with the information that, although he had not been able to obtain precise asymptotics, he had obtained the bound $$\label{r34-2}
\left| R_N(t)\right| \le \left|\frac{eN}{\sin(t/2)}\right|^{1/2}.$$ Substituting [\[r34-2\]](#r34-2){reference-type="eqref" reference="r34-2"} into [\[r34-1\]](#r34-1){reference-type="eqref" reference="r34-1"}, we see that $$\frac{\lambda_{N,L}^{(\mathrm{max})}}{N} =O\left(N^{-1/2}\right)\to 0,\quad\mbox{as}\quad N\to\infty.$$ In a letter of thanks to Szegő on July 23, Lenard describes the situation as follows: "This has great physical interest: It may be expressed as saying that for the model considered there is no Bose-Einstein condensation in momentum space".[^2]

Following a further suggestion contained in the above correspondence with Szegő in 1963, Lenard considered, in particular, symbols of the form $$\label{symJac}
f^{(\lambda,\mu)}(e^{i\theta})=|e^{i\theta}-e^{i\pi/2}|^\lambda|e^{i\theta}-e^{-i\pi/2}|^\mu,\qquad \lambda,\mu>0.$$ He started with the general formula for positive symbols $f\!\left(e^{i\theta}\right) >0$ $$\label{93}
D_n (f) = \prod^{n-1}_{k=0} \chi^{-2}_k$$ where $\chi_k>0$ is the leading coefficient of the orthonormal polynomial $p_k (z) =\chi_k\, z^k +
\dots, k \ge 0$, with respect to the weight of $d\mu=f\!\left(e^{i\theta}\right) d\theta/(2\pi)$ on $S^1$ as in [\[eq35\]](#eq35){reference-type="eqref" reference="eq35"}. For $f^{(\lambda,\mu)}(e^{i\theta})$ in [\[symJac\]](#symJac){reference-type="eqref" reference="symJac"}, the polynomials $p_k(z)$ can be expressed in terms of classical Jacobi polynomials on the interval $[-1,1]$. This then leads to explicit formulae for the $\chi_k$'s in terms of Euler's gamma functions.

After Lenard published the bound [\[r34-2\]](#r34-2){reference-type="eqref" reference="r34-2"} for the impenetrable boson problem (a Plasma Physics Laboratory preprint of [@Len1] appeared in 1963), Dyson [@Dy3] took up the problem of computing the asymptotics of

[\[r34-1\]](#r34-1){reference-type="eqref" reference="r34-1"} precisely as $N\to\infty$. In order to control the singularity in the symbol $f_t(e^{i\theta})=|e^{i\theta}-e^{it/2}||e^{i\theta}-e^{-it/2}|$, Dyson resorted to his interpretation of $D_{N-1}(f_t)$ as a Coulomb gas at inverse temperature $\beta=2$ with $N-1$ unit charges free to move around on the unit circle, but now with two additional half-charges. The probability of finding the half-charges at an angular distance $t$ apart is then proportional to $P(t)=|2\sin{t\over 2}|^{1/2}R_N(t)$. On physical grounds, Dyson then argued that for distances $t$ much greater than the "Debye length" $\lambda=2\pi/N$, the two half-charges are effectively screened off from each other, and so $P(t)=\text{const.}$ for $t>>\lambda$. In other words, $R_N(t)=k_N\left(\sin{t\over 2}\right)^{-1/2}$ for $t>>N^{-1}$, where $k_N$ is a constant. However, clearly $k_N=R_N(\pi)$, which can be evaluated explicitly as $N\to\infty$ since $$f_t(e^{i\theta})|_{t=\pi}=f^{(\lambda,\mu)}(e^{i\theta})|_{\lambda=\mu=1}$$ (see discussion of [\[symJac\]](#symJac){reference-type="eqref" reference="symJac"} above). Substituting the result into [\[r34-1\]](#r34-1){reference-type="eqref" reference="r34-1"} and neglecting the contribution from $|t|<N^{-1}$, Dyson obtained, as $N\to\infty$, $$\label{20.1}
\frac{\lambda_{N,L}^{(\mathrm{max})}}{N} \sim C N^{-1/2},\qquad C=\left({e\over\pi}\right)^{1/2}2^{-5/6}A^{-6}
\Gamma\left({1\over 4}\right)^2$$ where $A$ is again Glaisher's constant [\[Glai\]](#Glai){reference-type="eqref" reference="Glai"}. The crux of the above calculation is clearly the explicit evaluation of $R_N(\pi)$ as $N\to\infty$.

More detailed analysis of [\[r34-1\]](#r34-1){reference-type="eqref" reference="r34-1"} requires further study of the double-scaling limit as $t\to 1$, $N\to\infty$. We return to this issue in Section [\[sec-ds\]](#sec-ds){reference-type="ref" reference="sec-ds"}.
:::

Inspired by the work of Wu in [@Wu], and perhaps also influenced by the calculations of Lenard in [@Len1] [@Len2], Fisher and Hartwig [@FisHart1] made a conjecture about the asymptotic form of $D_n(f)$ for general symbols [\[eq74\]](#eq74){reference-type="eqref" reference="eq74"}, $$\label{eq84}
\begin{aligned}
D_n(f)  &= E\left(e^V, \, \alpha_0, \dots, \alpha_m, \, \beta_0, \dots, \beta_m,\, \theta_0, \dots, \theta_m\right)\\
&\quad \times \;n^{\sum^m_{j=0} \left(\alpha^2_j-\beta^2_j\right)} \, e^{n V_0}\left(1+o(1)\right),\qquad 
V_0=\frac{1}{2\pi} \int^{2\pi}_0 V\!\left(e^{i\theta}\right)d\theta
\end{aligned}$$ as $n\to\infty$, together with a conjecture on the general form of the constant $E$. In [@FisHart2], Hartwig and Fisher present various examples, heuristics and theorems in support of their conjecture.

In the remarkable paper [@Wid2], representing "a jump of several quanta in depth and sophistication" (see MathSciNet MR0331107), Widom verified Lenard's conjecture for complex $\alpha_j$ with $\Re \alpha_j > -\frac{1}{2},
\; j=0, \dots, m$, and $V\!\left(e^{i\theta}\right)$ suitably smooth, and obtained an explicit expression for the constant $$\label{eq85}
\begin{aligned}
E\left(e^V, \, \alpha_0, \dots, \alpha_m, \, \theta_0, \dots, \theta_m\right)
=&  E\!\left(e^V\right) \prod_{0\le j< k \le m} \left| e^{i\theta_j} -e^{i\theta_k} \right|^{-2\alpha_j\alpha_k} \\
& \times \prod^m_{j=0} e^{-\alpha_j \widehat{V}\left(e^{i\theta_j}\right)} \times \prod^m_{j=0} E_{\alpha_j}
\end{aligned}$$ where $$\begin{aligned}
{3}
&E\!\left(e^V\right) = e^{\sum^\infty_{k=1} k\, V_k\, V_{-k}}, \qquad &V_k &= \text{ Fourier coefficient of } V\!
\left(e^{i\theta}\right),\label{eq86}\\
&\widehat{V}\!\left(e^{i\theta}\right) = V\!\left(e^{i\theta}\right) - V_0&& \label{eq87}\\
\intertext{and}
&E_\alpha= G^2 (1+\alpha)/G(1+2\alpha), \qquad &G(z) &= \text{ Barnes G-function (see \cite{Bar}).} \label{eq88}
\end{aligned}$$ Formula [\[eq85\]](#eq85){reference-type="eqref" reference="eq85"} is consistent with and confirms the general form of the conjecture [@FisHart1] for the constant term in the case $\beta_0 = \beta_1 = \dots = \beta_m =0$.

In [@Bas1] Basor considered complex $\alpha_j$ with $\Re  \alpha_j >-\frac{1}{2}$, $\beta_j$ pure imaginary, $j=0, \dots, m$, and $V\!\left(e^{i\theta}\right)$ suitably smooth, and verified [\[eq84\]](#eq84){reference-type="eqref" reference="eq84"} with constant term, again consistent with the general conjecture in [@FisHart1], $$\label{eq89}
\begin{aligned}
&E \left(e^V, \alpha_0, \dots, \alpha_m, \beta_0, \dots, \beta_m, \theta_0, \dots, \theta_m\right)\\
&\quad =  E(e^V) \prod^m_{j=0} \left[b_+ (z_j)^{-\alpha_j + \beta_j}\, b_-(z_j)^{-\alpha_j-\beta_j} \right] \\
& \qquad \qquad \times \prod_{0\le j < k \le m} \left[ \left|z_j-z_k\right|^{2\left(\beta_j\beta_k-\alpha_j\alpha_k\right)}
\left(\frac{z_k}{z_j \, e^{i\pi}}\right)^{\alpha_j \beta_k-\alpha_k\beta_j}\right] \\
&\qquad \qquad\times \prod^m_{j=0} \frac{G\left(1+\alpha_j + \beta_j\right)  G \left(1+ \alpha_j - \beta_j\right)}{G\left(1+
2\alpha_j\right)} \ .
\end{aligned}$$ with $E\!\left(e^V\right)$ and $G(z)$ as above, and $$\label{eq90}
b_+(z) =e^{\sum^\infty_{k=1}  V_k\,z^k}, \qquad b_-(z)=e^{\sum^{-\infty}_{k=-1} V_k \, z^k}\ .$$ The branches in [\[eq89\]](#eq89){reference-type="eqref" reference="eq89"} are determined naturally, $b_+(z_j)^{-\alpha_j +\beta_j} =
e^{\left(-\alpha_j + \beta_j\right)\sum^\infty_{k=1} V_k z_j^k}$ etc, and $$\left(\frac{z_k}{z_j\,e^{i\pi}}\right)^{
\left(\alpha_j\beta_k-\alpha_k\beta_j\right)} = e^{i\left(\theta_k-\theta_j-\pi\right)\left(\alpha_j \beta_k-\alpha_k \beta_j\right)},
\qquad 0 \le \theta_j< \theta_k < 2\pi.$$

In the paper [@BasHelt] discussed above, Basor and Helton also introduce the first example of a so-called "separation" theorem of the following form: For symbols $\varphi$ and $\psi$ of a certain prescribed type, including FH symbols with disjoint singularities, they show that $$\lim_{n\to\infty}\frac{D_n(\varphi\psi)}{D_n(\varphi)D_n(\psi)}\equiv L(\varphi,\psi)$$ exists. Moreover, they provide an explicit form for $L(\varphi,\psi)$. Iterating this result, they are able to reduce the problem for general FH symbols to adding in pure FH singularities of the form $z^\beta |z-\widehat z|^{2\alpha}g_{\widehat z,\beta}(z)\widehat z^{-\beta}$, $|\widehat z|=1$, one at a time. They analyze the asymptotics of Toeplitz determinants with such pure (i.e., with $V\equiv 0$) FH singularities in the following way. In addition to the results described above, in [@Wid2] Widom also verified [\[eq84\]](#eq84){reference-type="eqref" reference="eq84"} for a single FH singularity with $|\Re\alpha|<\frac{1}{2}$ and $|\Re\beta |<\frac{1}{2}$, but without determining the exact value of the constant $E$. But then Basor's formula [\[eq89\]](#eq89){reference-type="eqref" reference="eq89"} for $E$ obtained in [@Bas1] for $\Re\alpha_j>-\frac{1}{2}$ and $\beta_j$ pure imaginary, together with Vitali's theorem, directly yields the desired explicit asymptotics for a single pure FH singularity with $|\Re\alpha|<\frac{1}{2}$ and $|\Re\beta |<\frac{1}{2}$. (In fact, as discovered later by Böttcher and Silbermann, see [\[eqBS\]](#eqBS){reference-type="eqref" reference="eqBS"} below, there exists an exact formula for a Toeplitz determinant with a single pure FH singularity in terms of the Barnes G-functions, which easily yields the asymptotics). In the end, Basor and Helton are able to verify [\[eq84\]](#eq84){reference-type="eqref" reference="eq84"} [\[eq89\]](#eq89){reference-type="eqref" reference="eq89"} for $\alpha_j$, $\beta_k$ in the open set $\{\max_{j,k}(|\alpha_j|,|\beta_k|)<\delta\}\subset\mathbb{C}^{2n}$ for some (small) $\delta>0$.

In [@Bas3], Basor showed using a separation theorem that [\[eq84\]](#eq84){reference-type="eqref" reference="eq84"} [\[eq89\]](#eq89){reference-type="eqref" reference="eq89"} also hold in the case $\alpha_j=0$, $|\Re\beta_j|<\frac{1}{2}$, $j=0,\dots,m$.

Böttcher and Silbermann [@BottSilb5] finally proved [\[eq84\]](#eq84){reference-type="eqref" reference="eq84"} with Basor's constant [\[eq89\]](#eq89){reference-type="eqref" reference="eq89"} under the assumption that $|\Re\alpha_j|<1/2$ and $|\Re\beta_j|<1/2$ for all $j$. This is the most general setting in which the conjecture [\[eq84\]](#eq84){reference-type="eqref" reference="eq84"} is true in its original form, that is, with the exponent of $n$ conjectured to be $\sum(\alpha_j^2-\beta_j^2)$, without the need to take care of degenerate situations and of the ambiguity in the $\beta$'s (see [\[eq97\]](#eq97){reference-type="eqref" reference="eq97"} below). We note that in [@BottSilb6] it had already been shown that [\[eq84\]](#eq84){reference-type="eqref" reference="eq84"} does not hold in general if $\alpha_j+\beta_j$ and $\alpha_j-\beta_j$ are nonnegative integers for all $j=0,\dots,m$, and a corrected version of the conjecture was proved in this case (this is a particular case of a formula conjectured by Basor and Tracy: see next section). The developments up to the 1990's are described in [@Bott1] and [@Ehr] and also in the books [@BottSilb2] [@BottSilb3]. We note that certain separation theorems also play a key role in the work of Böttcher and Silbermann. Another important element in their proofs is an explicit formula, noted above, for a Toeplitz determinant with a single, pure FH singularity found by the authors in [@BottSilb5] (see also [@BottWid2] [@BasChe] for later alternative derivations). Namely, if $V(z)\equiv 0$, $m=0$, then with $\alpha_0\equiv\alpha$, $\beta_0\equiv\beta$, $$\label{eqBS}
\begin{aligned}
D_n(f)=&\frac{G(1+\alpha+\beta)G(1+\alpha-\beta)}{G(1+2\alpha)}
\frac{G(n+1)G(n+1+2\alpha)}{G(n+1+\alpha+\beta)G(n+1+\alpha-\beta)},\\
&\Re\alpha>-{1\over 2},\qquad\alpha\pm\beta\neq -1,-2,\dots,\qquad n\ge 1.
\end{aligned}$$ The condition on $\alpha\pm\beta$ is needed because the $G$-function has zeros at $z=0,-1,-2,\dots$ The asymptotics for [\[eqBS\]](#eqBS){reference-type="eqref" reference="eqBS"} follow from the asymptotics of the $G$-function (see [@Bar]) $$\label{eq92} 
\begin{aligned}
\log G(t+a+1) &= \frac{1}{12} -\log A - \frac{3t^2}{4} - at + \frac{t+a}{2} \: \log (2\pi)\\
&\quad + \left( \frac{t^2}{2} + at + \frac{a^2}{2} - \frac{1}{12}\right) \log t+o(1), \qquad \text{as } \; t\to\infty
\end{aligned}$$ where again $A$ is Glaisher's constant [\[Glai\]](#Glai){reference-type="eqref" reference="Glai"}. The resulting asymptotics are consistent with [\[eq84\]](#eq84){reference-type="eqref" reference="eq84"} [\[eq89\]](#eq89){reference-type="eqref" reference="eq89"}.

In view of the Heine representation [\[eq40\]](#eq40){reference-type="eqref" reference="eq40"}, it is not surprising that the formula [\[eqBS\]](#eqBS){reference-type="eqref" reference="eqBS"} is related to the Selberg integral. In fact, independently of [@BottSilb5], a more general formula was obtained by Selberg himself: $$\label{Selb}\begin{aligned}
\int^{2\pi}_0 \dots \int^{2\pi}_0 &\prod_{0\le j < k \le n-1}
\left|e^{i\theta_j} - e^{i\theta_k} \right|^{2\gamma} \prod^{n-1}_{j=0} e^{i(\theta_j-\pi)\beta}\left|1-e^{i\theta_j}\right|^{2\alpha}
\,\frac{d\theta_j}{2\pi}\\
=&
\prod_{j=0}^{n-1}\frac{\Gamma(1+2\alpha+j\gamma)\Gamma(1+(j+1)\gamma)}
{\Gamma(1+\alpha+\beta+j\gamma)\Gamma(1+\alpha-\beta+j\gamma)\Gamma(1+\gamma)}
\end{aligned}$$ where $$\Re\alpha>-{1\over 2},\qquad \Re\gamma>-\min\left\{\frac{1}{n},\frac{\Re(2\alpha+1)}{n-1}\right\}.$$ In a published form, this formula first appeared in the thesis of Morris in 1982 (see [@ForWar] for a historic account). The interest in [\[Selb\]](#Selb){reference-type="eqref" reference="Selb"} was due to the efforts to prove one of Dyson's conjectures in the theory of random matrices in [@Dy1]. If we set $\gamma=1$ in [\[Selb\]](#Selb){reference-type="eqref" reference="Selb"}, and use the relation $G(z+1)=\Gamma(z)\, G(z)$, we recover [\[eqBS\]](#eqBS){reference-type="eqref" reference="eqBS"} from [\[eq40\]](#eq40){reference-type="eqref" reference="eq40"}.

The Barnes' function $G(z)$ is a basic object in analysis, bearing the same relation to the gamma function as the gamma function bears to the function $z$, $\Gamma(z+1)
=z \, \Gamma(z)$. Just as $\log \Gamma(z)$ is a sum of values of $\log z$, so $\log G(z)$ is the iterated sum. It is of interest to delineate some of the analytic pathways by which $G(z)$ appears in the asymptotics of $D_n(f)$.

The most direct example, a particular case of [\[eqBS\]](#eqBS){reference-type="eqref" reference="eqBS"}, arises for the diagonal correlation function $\left\langle\sigma_{1,1}\, \sigma_{1+n, 1+n}\right\rangle$ at $T_c$, where $\varphi_{\text{diag}}(\theta)=e^{i\left(\pi-\theta\right)/2}$, i.e. $V\equiv 0$, $m=0$, $\alpha_0=0$, $\beta_0=-1/2$, in [\[eq58\]](#eq58){reference-type="eqref" reference="eq58"} gives rise to the Cauchy determinant [\[Opure\]](#Opure){reference-type="eqref" reference="Opure"} which can be evaluated as in [\[eq53\]](#eq53){reference-type="eqref" reference="eq53"} in terms of a product of gamma functions, and hence in terms of $G$-functions, $\prod^{n-1}_{q=1} \Gamma(q+1)=G(n+1)/G(2)$, etc.

For a system of polynomials orthonormal with respect to a function $f$ on the unit circle, the leading coefficients $\chi_k$ are related to $D_n(f)$ by the product formula [\[93\]](#93){reference-type="eqref" reference="93"}. As we discussed above, in the case of $f$ given by [\[symJac\]](#symJac){reference-type="eqref" reference="symJac"} the coefficients $\chi_k$ are expressed in terms of gamma functions, and therefore $G$-functions appear in the product. More generally, there is a certain universality in the asymptotic behavior of orthogonal polynomials associated with FH symbols on $S^1$ (see [@DIK1] [@DIK3]), and, mutatis mutandis, for general FH symbols $f$, the $G$-functions enter the arena through the same stage door.

As noted above in [\[eq82\]](#eq82){reference-type="eqref" reference="eq82"}, at $T=T_c$, $\varphi_{\text{ons}}\!\left(e^{i\theta}\right)$ has a single FH singularity at $z_0=1$ with $\alpha_0=0$ and $\beta_0=-\frac{1}{2}$. The first confirmation of [\[eq84\]](#eq84){reference-type="eqref" reference="eq84"} [\[eq89\]](#eq89){reference-type="eqref" reference="eq89"} which allowed for these values was given in [@BottSilb4], where the authors proved the result for $m=0$, $\Re \alpha_0 \ge 0$, $\Re\left(\alpha_0 + \beta_0\right) >-1$ and $\Re\left(\alpha_0-\beta_0\right) > -1$. It is instructive to recover Wu's asymptotic formula [\[eq65\]](#eq65){reference-type="eqref" reference="eq65"} from [\[eq84\]](#eq84){reference-type="eqref" reference="eq84"} [\[eq89\]](#eq89){reference-type="eqref" reference="eq89"}. Here $V\!\left(e^{i\theta}\right)= \frac{1}{2} \log \left(\frac{1-\gamma_1\,e^{i\theta}}{1-\gamma_1 \, e^{-i\theta}}\right)$ and we find $V_0=0$ and $V_k=-\gamma_1^{|k|}/2k$ for $k \neq 0$. Thus $E\left(e^V\right)=e^{-\frac{1}{4} \sum^\infty_{k=1} \, k \,\gamma_1^{2k}/k^2} = \left(1-\gamma^2_1
\right)^{\frac{1}{4}}$. On the other hand $\left(b_+(1)\right)^{-\frac{1}{2}} \left(b_-(1)\right)^{\frac{1}{2}}=
e^{\frac{1}{4} \sum^\infty_{k=1}\gamma^k_1/ k} \, e^{\frac{1}{4} \sum^{-\infty}_{k=-1} \gamma_1^{|k|}/|k|} =
\left(1-\gamma_1\right)^{-\frac{1}{2}}$. But $G\left(\frac{1}{2}\right)=2^{\frac{1}{24}} \, e^{\frac{1}{8}}
\,\pi^{-1/4} \, A^{-3/2}$, where again $A$ is Glaisher's constant (see [@Bar]), and we have $G\left(\frac{3}{2}\right) = \Gamma \left(\frac{1}{2}\right)
G\left(\frac{1}{2}\right) =2^{\frac{1}{24}} \, e^{\frac{1}{8}}\, \pi^{\frac{1}{4}}\, A^{-3/2}$. Thus $G\left(\frac{1}{2}
\right) G\left(\frac{3}{2}\right)=2^{\frac{1}{12}} \, e^{\frac{1}{4}}\, A^{-3}$. Substituting these relations into [\[eq89\]](#eq89){reference-type="eqref" reference="eq89"}, we obtain $E\!\left(e^V, 0, \frac{1}{2}, \theta_0=0\right)=2^{\frac{1}{12}} \, e^{\frac{1}{4}}\, A^{-3}
\left(1+\gamma_1\right)^{\frac{1}{4}} \left(1-\gamma_1\right)^{-\frac{1}{4}}$, and as $n^{-\beta^2_0} = n^{-\frac{1}{4}}$, we arrive at precisely the leading order term in [\[eq65\]](#eq65){reference-type="eqref" reference="eq65"}.

The **definitive result** for the leading order asymptotics of Toeplitz determinants with FH singularities was obtained by Ehrhardt in his PhD thesis at TU Chemnitz in 1997 (see [@Ehr]). Let $|||\beta|||$ denote the seminorm $$\label{eq91}
|||\beta|||= \max_{j,k} \left|\Re \beta_j - \Re \beta_k\right|$$ where $1\le j, \, k \le m$ if $\alpha_0= \beta_0=0$, and $0\le j, \, k\le m$ otherwise. If $m=0$, set $|||\beta|||=0$. Note that in the case of a single singularity, we always have $|||\beta|||=0$. If $V\!\left(e^{i\theta}\right)$ is $C^\infty$ on $S^1$, $|||\beta|||<1$, $\Re \alpha_k>-\frac{1}{2}$ and $\alpha_j \pm \beta_j
\neq -1, -2, \dots$ for $j,\, k=0,1, \dots, m$, then Ehrhardt proved the Fisher-Hartwig conjecture [\[eq84\]](#eq84){reference-type="eqref" reference="eq84"} with Basor's constant [\[eq89\]](#eq89){reference-type="eqref" reference="eq89"}. As above, the conditions on $\alpha_j \pm \beta_j$ ensure that Basor's constant is non-zero and [\[eq89\]](#eq89){reference-type="eqref" reference="eq89"} indeed provides the leading order asymptotics for $D_n(f)$ as $n\to \infty$. A key element in Ehrhardt's proof is a suitably generalized version of the separation theorem in [@BasHelt].[^3]

An independent proof of Ehrhardt's result was given recently in [@DIK3] where only a finite degree of smoothness is needed for $V\!\left(e^{i\theta}\right)$. In [@DIK3], estimates for the error term in the asymptotics are also provided. If $V(z)\in C^{\infty}$ on $S^1$, the asymptotics [\[eq84\]](#eq84){reference-type="eqref" reference="eq84"} [\[eq89\]](#eq89){reference-type="eqref" reference="eq89"} hold with error term $$o(1)=O(n^{|||\beta|||-1}).$$ Note that the smallness of the error term breaks down if $|||\beta|||\ge 1$. We will consider this situation in detail in the next section. The main steps of the method of [@DIK3] are as follows. First, the authors derive differential identities for the logarithmic derivatives of $D_n(f)$, in particular, for $${\partial\over\partial\alpha_j}\log D_n(f),\qquad {\partial\over\partial\beta_j}\log D_n(f),$$ in terms of the associated OPUC's of degrees $n$ and $n+1$ only. Second, the authors obtain the asymptotics of these OPUC's using their Riemann-Hilbert representation and the steepest descent analysis of the Riemann-Hilbert problem for large $n$. Third, the asymptotic formulas so obtained are substituted into the RHS of the differential identities, and the final result [\[eq84\]](#eq84){reference-type="eqref" reference="eq84"} [\[eq89\]](#eq89){reference-type="eqref" reference="eq89"} is obtained by integration.[^4] In [@DIK1], [@DIK3] the authors also note various uniformity properties of the large $n$ asymptotics for Toeplitz determinants in the parameters, such as $\alpha_j$, $\beta_j$, on which $f$ depends. This issue becomes important in discussions of double-scaling limits (cf Section [\[sec-ds\]](#sec-ds){reference-type="ref" reference="sec-ds"}).

For the Ising model at $T> T_c$, we see from [\[106\]](#106){reference-type="eqref" reference="106"} that $z_0=1,\, \alpha_0=0$ and $\beta_0=-1$, and so $\alpha_0 + \beta_0=-1$. Thus [\[eq84\]](#eq84){reference-type="eqref" reference="eq84"} [\[eq89\]](#eq89){reference-type="eqref" reference="eq89"} do not provide the leading order asymptotics for $\left\langle\sigma_{1,1}\,\sigma_{1,1+n}\right\rangle$ in this case. One must analyze lower order terms, in fact go "beyond all orders" in the language of Kruskal, to capture the exponential decay in Wu's result [\[eq64\]](#eq64){reference-type="eqref" reference="eq64"} (see Remark [\[degen\]](#degen){reference-type="ref" reference="degen"} below).

[^1]: Note that although [@Len2] was published in 1972, a preliminary unpublished version of the paper was already in existence in 1968 (see [@FisHart1]).

[^2]: This confirms an earlier result of Schultz [@Sch] proving the absence of condensation. Schultz used other methods which produced the (weaker) bound $O(N^{-4/\pi^2})$.

[^3]: Note that the RHS of [\[eq84\]](#eq84){reference-type="eqref" reference="eq84"} and [\[eq89\]](#eq89){reference-type="eqref" reference="eq89"} make sense for any $\alpha_j$, $2\alpha_j\neq -1,-2,\dots$. In fact, [\[eq84\]](#eq84){reference-type="eqref" reference="eq84"} [\[eq89\]](#eq89){reference-type="eqref" reference="eq89"} still hold in this case. This extension to the left of the lines $\Re\alpha_j=-1/2$ is explained in [@Ehr] and corresponds to replacing the symbol $f$ by an appropriate distribution.

[^4]: Note that if one just used the formula [\[93\]](#93){reference-type="eqref" reference="93"} instead of the differential identities, then the product $\prod_{k=0}^{n_0}\chi_k^{-2}$ for small $n_0$, and hence the constant factor $E$ in [\[eq84\]](#eq84){reference-type="eqref" reference="eq84"}, would remain undetermined.

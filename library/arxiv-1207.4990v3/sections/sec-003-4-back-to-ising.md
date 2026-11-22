---
doc_id: arxiv-1207.4990v3
doc_title: "Toeplitz matrices and Toeplitz determinants under the impetus of the Ising model. Some history and some recent results"
section_id: sec-003-4-back-to-ising
section_title: "Back to Ising"
section_number: 4
pages: 23-27
source_pdf: 1207.4990v3.pdf
source_sha256: 02aa065f4f65b857
toc_source: outline
text_source: latex
latex_prose_ratio: 0.992
latex_coverage_ratio: 0.992
doc_brief: "Toeplitz matrices and Toeplitz determinants under the impetus of the Ising model. Some history and some recent results — 12 sections: Front matter; Setting the problem; Toeplitz meets Ising"
---
[]{#section4 label="section4"} After Onsager announced formula [\[eq15\]](#eq15){reference-type="eqref" reference="eq15"} for $M_0$ in 1948, and again in 1949, but did not provide a proof, three years went by until a derivation of the formula was found by Yang in a tour de force in 1952 [@Yan1]. Yang's method is based on results of Kaufman and Onsager, but his approach is different, and he does not explicitly use Toeplitz determinants. In his Selected Papers in 2005 ([@Yan2]), Yang described the long and winding road that led him to the Kaufman-Onsager formula [\[eq15\]](#eq15){reference-type="eqref" reference="eq15"}. The story has much charm:

"I was thus led to a long calculation, the longest in my career. Full of local, tactical tricks, the calculation proceeded by twists and turns. There were many obstructions. But always, after a few days, a new trick was somehow found that pointed to a new path. The trouble was that I soon felt I was in a maze and was not sure whether in fact, after so many turns, I was anywhere nearer the goal than when I began. This kind of strategic overview was very depressing, and several times I almost gave up. But each time something drew me back, usually a new tactical trick that brightened the scene, even though only locally.

Finally, after about six months of work off and on, all the pieces suddenly fitted together, producing miraculous cancellation, and I was staring at the amazingly simple final result."

::: remark
[]{#remark2 label="remark2"} Let $E_\Lambda(\sigma)$ denote the interaction energy in a rectangular box $\Lambda$ of size $M\times N$ as in [\[eq6\]](#eq6){reference-type="eqref" reference="eq6"} above, and let $E_{\Lambda, h}(\sigma)= E_\Lambda(\sigma) - h \sum_{(i,j)\in \Lambda} \sigma_{i,j}$ denote the energy in the presence of a magnetic field of strength $h$. Let $Z_{\Lambda, h} = \sum_\sigma e^{-E_{\Lambda, h}
(\sigma)/k_B\, T}$ denote the associated partition function, and let $F_{\Lambda, h} = -\frac{k_B \, T}{MN} \log
Z_{\Lambda, h}$ denote the associated free energy in the box $\Lambda$. What Yang proved in [@Yan1] was that, for $T<T_c$, $$\begin{aligned}
M_Y &\equiv -\lim_{h\downarrow 0}\; \lim_{|\Lambda| \to \infty} \frac{F_{\Lambda, h/N} - F_{\Lambda, 0}}{h/N}\\
&= \left(1-k^2_{\text{ons}}\right)^{\frac{1}{8}} = M_0 \equiv \lim_{n\to \infty} \left\langle \sigma_{1,1} \;
\sigma_{1,n}\right\rangle^{\frac{1}{2}}.
\end{aligned}$$ (In [@Yan1], Yang only considered the case $J_1=J_2$. Yang's method was extended to the general case $J_1 \neq J_2$ by Chang [@Cha].)
:::

As noted and emphasized by Schultz, Mattis and Lieb [@ScML] in 1964, neither $M_Y$ nor $M_0$ coincide, a priori, with the physically fundamental definition of the spontaneous magnetization $M_{\text{phys}}$, viz., $$\begin{aligned}
M_{\text{phys}}  &\equiv -\lim_{h\downarrow 0} \; \lim_{|\Lambda| \to \infty}
\frac{\partial\, F_{\Lambda, h}}{\partial h}\\
&= \lim_{h \downarrow 0} \; \lim_{|\Lambda|\to\infty} \frac{1}{MN}
\left[ \frac{\sum_\sigma\left(\sum_{(i,j)\in \Lambda} \sigma_{i,j}\right) e^{-\frac{1}{k_B\,T} \, E_{\Lambda, h} (\sigma)}}{
\sum_\sigma e^{-\frac{1}{k_B\,T} \, E_{\Lambda,h}(\sigma)}} \right].
\end{aligned}$$ Only some years later was it shown that indeed for $T< T_c$ $$M_{\text{phys}} = M_Y = M_0 = \left(1-k^2_{\text{ons}}\right)^{\frac{1}{8}}$$ (see, in particular, [@LebM-Lof], [@BGJ-LS]).

In 1955 an important technical advance was made by Potts and Ward [@PotWar] when they showed, in particular, that the correlation function $\left\langle \sigma_{1,1}\, \sigma_{1,n}\right\rangle$ along a row for the 2-D Ising model could be expressed in terms of a *single* Toeplitz determinant, rather than a sum of two Toeplitz determinants as in [\[eq17\]](#eq17){reference-type="eqref" reference="eq17"}. They were unable at the time to verify that their solution agreed with [\[eq17\]](#eq17){reference-type="eqref" reference="eq17"}: This was done later in 1963 [@MPW] by Montroll, Potts and Ward, who also used recent ideas of Kasteleyn on the Pfaffian approach to the dimer and Ising problems to give a new and simpler proof of the formula in [@PotWar]. The formula in [@PotWar] [@MPW] is the following $$\label{eq50}
\left\langle \sigma_{1,1} \, \sigma_{1, 1+n} \right\rangle =  D_n\!\left(\varphi_{\text{ons}}\right)$$ where $\varphi_{\text{ons}}\!\left(e^{i\theta}\right)$ is the Onsager function defined in [\[eq21\]](#eq21){reference-type="eqref" reference="eq21"}. Through discussions with Mark Kac, Montroll et al. were aware of SSLT. Furthermore they knew, as noted above, how to extend Szegő's result via Kac's method to the case where the symbol is complex. For $T< T_c$, Montroll, Potts and Ward noted that $0< \gamma_1, \gamma_2 <1$ by [\[eq26\]](#eq26){reference-type="eqref" reference="eq26"}, and so $\varphi_{\text{ons}}^{\pm 1} \!\left(e^{i\theta}\right) \neq 0$ and $\varphi_{\text{ons}}$ has no winding on $S^1$. As in the computation for $\varphi_{\text{diag}}\!\left(e^{i\theta}\right)$ above, we find $$\begin{aligned}
\left(\log \varphi_{\text{ons}}\right)_\ell &= -\left(\frac{\gamma_1^\ell}{2\ell} - \frac{\gamma_2^\ell}{2\ell}\right), \qquad
\ell \ge 1\\
\left(\log \varphi_{\text{ons}}\right)_{-\ell} &= \left(\frac{\gamma_1^\ell}{2\ell} - \frac{\gamma_2^\ell}{2\ell}\right), \qquad
\ell \ge 1
\end{aligned}$$ and $\left(\log \varphi_{\text{ons}}\right)_0 =0$. This implies $\sum^\infty_{\ell=1} \ell \left(\log\varphi_{\text{ons}}\right)_\ell \, \left(\log \varphi_{\text{ons}}\right)_{-\ell}
=\frac{1}{4} \, \log \frac{\left(1-\gamma_1^2\right)\left(1-\gamma_2^2\right)}{\left(1-\gamma_1 \gamma_2\right)^2}$ and after some elementary algebra using [\[eq22\]](#eq22){reference-type="eqref" reference="eq22"}, we again obtain [\[eq15\]](#eq15){reference-type="eqref" reference="eq15"}, but now via [\[eq16\]](#eq16){reference-type="eqref" reference="eq16"} (cf. the discussion following [\[eq47\]](#eq47){reference-type="eqref" reference="eq47"}).

We now consider the spontaneous magnetization for the Ising model for temperatures $T \ge T_c$. As $k_{\text{ons}} \uparrow 1$ when $T\uparrow T_c$, one anticipates from [\[eq15\]](#eq15){reference-type="eqref" reference="eq15"} that at $T=T_c$ the spontaneous magnetization $M_0$ is zero. In [@KauOns], Kaufman and Onsager proceed in the following way. They derive an approximate formula for $b_k$ in [\[eq19\]](#eq19){reference-type="eqref" reference="eq19"} ($b_k = \sum_{-k}$ in the notation of [@KauOns]) at $T=T_c$ $$\label{eq52}
b_k \sim \frac{2}{\pi\,(2k+1)} \qquad\text{ as }\qquad k\to \infty.$$ They then take [\[eq52\]](#eq52){reference-type="eqref" reference="eq52"} as an equality for all $k\ge 0$, and substitute this relation into [\[eq17\]](#eq17){reference-type="eqref" reference="eq17"} to obtain an approximate asymptotic formula for $\left\langle \sigma_{1,1}\, \sigma_{1, 1+n}\right\rangle$ in the form of a linear combination $c^{*2}_2\, W_n - s^*_2\, \widetilde{W}_n$ of two Cauchy determinants $W_n$ and $\widetilde{W}_n =W_{-n}$. Such determinants can be evaluated explicitly in terms of gamma functions[^1] $$\begin{aligned}
\left|W_n\right| &= \frac{2}{\pi} \prod^{n-1}_{q=1} \frac{\Gamma(q+1)\, \Gamma(q+1)}{\Gamma \left(q+\frac{1}{2}\right)
\Gamma \left(q+\frac{3}{2}\right)}, \label{eq53}\\
\left|\widetilde{W}_n\right| &= \frac{2}{3\pi} \prod^{n-1}_{q=1} \frac{\Gamma (q+1) \, \Gamma(q+1)}{
\Gamma \left(q-\frac{1}{2}\right)\Gamma\left(q+\frac{5}{2}\right)}\label{eq54}
\end{aligned}$$ and Kaufman and Onsager observe that both $W_n$ and $\widetilde{W}_n\to 0$ as $n\to\infty$, with $\widetilde{W}_n$ decaying at a much faster rate than $W_n$. They conclude that at $T=T_c$ $$\label{eq55}
\left\langle \sigma_{1,1}\, \sigma_{1, 1+n}\right\rangle \sim (-1)^n c^{*2}_2 W_n \to 0 \qquad \text{ as }\quad n\to \infty$$ and so $M_0=0$. In 1959, Fisher [@Fis1] picks up on these calculations, and using Stirling's formula in [\[eq53\]](#eq53){reference-type="eqref" reference="eq53"} he shows via [\[eq55\]](#eq55){reference-type="eqref" reference="eq55"} that as $n\to\infty$ $$\label{eq56}
\left\langle \sigma_{1,1} \, \sigma_{1, 1+n}\right\rangle \sim C\: n^{-1/4}, \qquad T=T_c$$ for some (undetermined) constant $C$. This is the first derivation of an explicit decay rate for the correlation function at $T_c$. Fisher argues further that off the lattice axes, [\[eq56\]](#eq56){reference-type="eqref" reference="eq56"} may be generalized (in the case $J_1=J_2$) to $$\label{eq57}
\left\langle \sigma_{1,1}\, \sigma_{1+ \ell, 1+m}\right\rangle \sim C(\theta) \, k^{-1/4}, \qquad T=T_c$$ where $\tan\theta= \ell/m$ and $k=\left(\ell^2 +m^2\right)^{\frac{1}{2}} \to \infty$, and $C(\theta)$ depends mildly on $\theta$ (see more below). As Fisher learned later from Onsager himself (see reference 8 in [@Fis1]; also, cf. the reference preceding [\[eq27\]](#eq27){reference-type="eqref" reference="eq27"} above to [@Dom2]), the analogue of formula [\[eq55\]](#eq55){reference-type="eqref" reference="eq55"} is in fact *exact* for correlations along the diagonal: $$\label{Opure}
\left\langle \sigma_{1,1} \,\sigma_{1+n, 1+n}\right\rangle=(-1)^n W_n,\qquad T=T_c.$$ Indeed from [\[eq27\]](#eq27){reference-type="eqref" reference="eq27"} , [\[eq28\]](#eq28){reference-type="eqref" reference="eq28"}, for $k_{\text{ons}}=1$ at $T_c$, $$\begin{aligned}
\varphi_{\text{diag}}(\theta) &= \frac{1-e^{-i\theta}}{\left|1-e^{i\theta}\right|} = e^{i(\pi-\theta)/2}\ ,&\qquad &0<\theta<2\pi
\label{eq58}\\
\intertext{and so }
\left(\varphi_{\text{diag}}\right)_k &= \frac{2}{\pi} \; \frac{1}{2k+1}\ , &\qquad &k\in \mathbb{Z}
\label{eq59}
\end{aligned}$$ which agrees with [\[eq52\]](#eq52){reference-type="eqref" reference="eq52"} (note from [\[eq17\]](#eq17){reference-type="eqref" reference="eq17"} that $W_n$ is a Toeplitz determinant with shifted entries $b_{k-1}$, and to observe [\[Opure\]](#Opure){reference-type="eqref" reference="Opure"} one can write $W_n$ as a determinant of the transposed matrix). If one repeats Fisher's calculation and keeps track of the constant, one obtains the exact asymptotics at $T=T_c$, $$\label{eq60}
\left\langle \sigma_{1,1}\, \sigma_{1+n, 1+n}\right\rangle = e^{\frac{1}{4}} \, A^{-3}\, 2^{\frac{1}{12}}\, n^{-1/4}
\;\left(1-\frac{1}{64}\; \frac{1}{n^2} + \dots \right) \quad\text{as}\quad n\to\infty$$ where $$\label{Glai}
A=e^{\frac{1}{12}}\, e^{-\zeta'(-1)}$$ is Glaisher's constant, $\zeta=\text{Riemann's zeta function}$. Formula [\[eq60\]](#eq60){reference-type="eqref" reference="eq60"} was first obtained by T. T. Wu in [@Wu] in serendipitous circumstances, as we describe below. The full expansion of [\[eq60\]](#eq60){reference-type="eqref" reference="eq60"} to all orders was first given in [@AuYPer1], together with a similar result, in the symmetric case $J_1=J_2$, for the next-to-diagonal correlation functions.

For $T>T_c$, Fisher notes in [@Fis1] that one can use the matrix viewpoint in [@Ons1] to show that as $k=\sqrt{\ell^2 + m^2} \to \infty$ $$\label{eq61}
\left\langle \sigma_{1,1}\, \sigma_{1+\ell, 1+m}\right\rangle \sim B \,k^{-\frac{1}{4}} \; e^{-f_k(T)}$$ for some $\theta$-dependent constant $B=B(\theta)$, where to leading order as $k\to\infty$ $$\label{eq62}
f_k(T) \sim k\, g(T).$$ As $T\downarrow T_c$, $g(T) \downarrow 0$. These calculations show, in particular, that $M_0=0$ for $T>T_c$. If one includes logarithmic correction terms in [\[eq62\]](#eq62){reference-type="eqref" reference="eq62"}, one obtains (see [@Fis2]) for $T>T_c$ $$\label{eq63}
\left\langle \sigma_{1,1}\, \sigma_{1+\ell, 1+m}\right\rangle \sim C(\theta, T) \;\frac{e^{-k\,g(T)}}{k^{1/2}}\;
\left(1+O(1)\right)$$ as $k\to\infty$. This is the first derivation of an explicit decay rate for the correlation function at $T>T_c$. In [@KauOns] the authors show how the conclusion $M_0=0$ also follows from their determinantal formulae, at least for $T>T_c$ sufficiently large. In [@Kad], Kadanoff obtains a decay rate for $T>T_c$ of the same form as in [\[eq63\]](#eq63){reference-type="eqref" reference="eq63"}, but only in the double scaling limit $T-T_c \downarrow 0$, $k\to\infty$ such that $\left|T-T_c\right| \, k=c =
\text{ constant}$. In [@Rya], Ryazanov obtains the $k^{-1/4}$ decay rate at $T=T_c$, and he also obtains the general form [\[eq63\]](#eq63){reference-type="eqref" reference="eq63"}, at least in the case that $T$ is large, $T>>T_c$. The double scaling limit, $T\to T_c$ and $k\to\infty$, for the Ising model is an important issue, to which we will return at various points in this paper. The importance of this issue rests in the fact that many believe in universality for spin models in the sense that the double scaling limit for the spin-spin correlation function in the Ising model also gives precisely the same limit (modulo lattice-dependent factors) for a wide class of "non-integrable" two-dimensional models with short range interactions.

::: remark
[]{#remark4 label="remark4"} The result that $M_{\text{phys}}$, the physically fundamental spontaneous magnetization defined above, is in fact zero for all $T>T_c$, was proven rigorously only many years later by Lebowitz in [@Leb] in (1972). The proof in [@Leb] uses a variety of techniques from statistical mechanics, but as shown in [@LebM-Lof] [@BGJ-LS], $M_{\text{phys}} = M_0=\lim_{n\to\infty} \left\langle \sigma_{1,1}\, \sigma_{1,1+n}
\right\rangle^{\frac{1}{2}}$ for all $T>0$, and so the proof that $M_{\text{phys}}=0$ for $T>T_c$ (in fact, for $T\ge T_c$) follows, a posteriori, from a proof that $\lim_{n\to \infty} D_n\!\left(\varphi_{\text{ons}}\right)=0$, $T\ge T_c$.
:::

::: remark
[]{#4+ label="4+"} In the isotropic case, $J_1=J_2$, explicit expressions for the correlation functions $\left\langle\sigma_{1,1}\,\sigma_{1+m, 1+\ell}\right\rangle$ for values of $(m,\ell)$ other than $(0,\ell)$, $(m,0)$, or $(m,m)$, were derived by Shrock and Ghosh [@ShGh]. In particular, they obtained expressions in the cases $(m,\ell)=(2,1)$, $(3,1)$, $(3,2)$, $(4,1)$, $(4,2)$, and $(4,3)$, in terms of complete elliptic integrals $K$ and $E$. They also inferred a general structural formula for arbitrary $\left\langle\sigma_{1,1}\,\sigma_{1+m, 1+\ell}\right\rangle$ in terms of these elliptic integrals $K$ and $E$.

In further developments, Au-Yang, Jin, and Perk [@AuYPer2] [@AuYJPer] showed that the next-to-diagonal correlations $\left\langle\sigma_{1,1}\,\sigma_{1+n, n}\right\rangle$ have a "bordered" Toeplitz determinant form, that is, an $n\times n$ Toeplitz determinant with the last column replaced by a certain explicit vector $(b_{n-1},b_{n-2},\dots,b_0)^T$. This representation is then used to express $\left\langle\sigma_{1,1}\,\sigma_{1+n, n}\right\rangle$ in terms of a solution to the Painlevé VI equation by Witte in [@Wi].
:::

[^1]: Formulae [\[eq53\]](#eq53){reference-type="eqref" reference="eq53"} [\[eq54\]](#eq54){reference-type="eqref" reference="eq54"} differ slightly from the corresponding formulae in [@KauOns].

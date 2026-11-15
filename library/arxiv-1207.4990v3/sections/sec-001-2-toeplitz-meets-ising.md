---
doc_id: arxiv-1207.4990v3
doc_title: "Toeplitz matrices and Toeplitz determinants under the impetus of the Ising model. Some history and some recent results"
section_id: sec-001-2-toeplitz-meets-ising
section_title: "Toeplitz meets Ising"
section_number: 2
pages: 9-12
source_pdf: 1207.4990v3.pdf
source_sha256: 02aa065f4f65b857
toc_source: outline
text_source: latex
latex_prose_ratio: 0.979
latex_coverage_ratio: 0.993
doc_brief: "Toeplitz matrices and Toeplitz determinants under the impetus of the Ising model. Some history and some recent results — 12 sections: Front matter; Setting the problem; Toeplitz meets Ising"
---
What precisely was this "last problem" that Kaufman and Onsager had to face in order to compute the limit in [\[eq16\]](#eq16){reference-type="eqref" reference="eq16"}? It is here that we make contact with the theory of Toeplitz matrices. In [@KauOns] Kaufman and Onsager expressed $\langle \sigma_{1,1} \, \sigma_{1,1+n}\rangle$ as a sum of two Toeplitz determinants as follows (in the notation of [@MPW]): $$\label{eq17}
\begin{aligned}
(-1)^n \left\langle \sigma_{1,1} \,\sigma_{1, 1+n}\right\rangle &= c^{*\,2}_2 \det
\begin{pmatrix}
b_{-1}  & b_{-2} & b_{-3}  & \dots & b_{-n} \\
b_{0}  & b_{-1} & b_{-2}  & \dots & b_{1-n} \\
b_{1}  & b_{0} & b_{-1}  & \dots & b_{2-n} \\
\vdots & \vdots & \vdots & & \vdots\\
b_{n-2}  & b_{n-3} & b_{n-4}  & \dots & b_{-1}
\end{pmatrix} \\[6mm]
&-s^{*2}_2 \det
\begin{pmatrix}
b_1  & b_2 & b_3  & \dots & b_n \\
b_{0}  & b_1 & b_2  & \dots & b_{n-1} \\
b_{-1}  & b_{0} & b_{1}  & \dots & b_{n-2} \\
\vdots & \vdots & \vdots &\vdots\;\vdots\;\vdots & \vdots\\
b_{2-n}  & b_{3-n} & b_{4-n}  &  & b_{1}
\end{pmatrix}
\end{aligned}$$ where $$\label{eq18}
c^*_2 = \cosh\, K^*_2, \quad s^*_2 = \sinh \, K^*_2, \quad e^{-2K^*_2} = \tanh\, \frac{J_2}{k_B T}$$ $$\label{eq19}
b_j = \frac{1}{\pi} \int^{\pi}_0 \cos \left( {\hat{\delta}} (\theta) - j \theta\right) d\theta$$ $$\label{eq20}
\cos \hat{\delta}(\theta) =  \sin \left(\delta^*(\theta) \right) \sin \theta\cosh 2K^*_2 - \cos \left(\delta^* (\theta)\right)
\cos \theta$$ and $\varphi_{\text{ons}}\! \left(e^{i\theta}\right) = e^{i\delta^*(\theta)}$ is a function introduced previously by Onsager in [@Ons1] $$\label{eq21}
\varphi_{\text{ons}}\! \left(e^{i\theta}\right)= \left[ \left( \frac{1-\gamma_1 \, e^{i\theta}}{1-\gamma_1 \, e^{-i\theta}}\right)
\left( \frac{1-\gamma_2 \, e^{-i\theta}}{1-\gamma_2 \, e^{i\theta}}\right) \right]^{\frac{1}{2}}$$ $$\label{eq22}
\begin{aligned}
&\text{where }\qquad \qquad \gamma_1 = z_1 \,z^*_2, \qquad \gamma_2 =z^*_2/z_1 \\
&z_1 = \tanh \frac{J_1}{k_B\, T}, \quad z_2 = \tanh \frac{J_2}{k_B \,T}, \quad z^*_2 =
\frac{1-z_2}{1+z_2},
\end{aligned}$$ The branch in [\[eq21\]](#eq21){reference-type="eqref" reference="eq21"} is chosen so that $\varphi_{\text{ons}}\! \left(e^{i\pi}\right) =e^{i\delta^*(\pi)} >0$.

::: remark
[]{#remark1 label="remark1"} As noted in [@MPW], there is a sign error in formula [\[eq17\]](#eq17){reference-type="eqref" reference="eq17"} in [@KauOns].
:::

So the problem that Kaufman and Onsager had to face to compute $M_0$ via [\[eq16\]](#eq16){reference-type="eqref" reference="eq16"}, was the purely mathematical problem of computing the asymptotics of $n\times n$ Toeplitz determinants as $n\to \infty$. At the time, however, all that was known was Szegő's result [\[eq5\]](#eq5){reference-type="eqref" reference="eq5"} with unknown error term $o(n)$. But to compute [\[eq16\]](#eq16){reference-type="eqref" reference="eq16"}, this error term is precisely what one needs to know!

Note that $$\label{eq23}
0 < \gamma_1 < 1 \qquad\text{ and }\qquad \gamma_1 < \gamma_2.$$ If $\gamma_2 \neq 1$, we see that $$\label{eq24}
\varphi_{\text{ons}}\! \left(e^{i\theta}\right) = \frac{\left(1-\gamma_1 \, e^{i\theta}\right) \left(1-\gamma_2 \,e^{-i\theta}\right)}{
\left|\left(1-\gamma_1 \, e^{-i\theta}\right) \left(1-\gamma_2\, e^{i\theta}\right)\right|}$$ and hence $\varphi_{\text{ons}}\! \left(e^{i\theta}\right)$ is a smooth, single-valued function on the unit circle $S^1$. On the other hand, if $\gamma_2=1$, then $$\label{eq25}
\varphi_{\text{ons}}\! \left(e^{i\theta}\right) = i\, e^{-i\theta/2} \,\frac{\left(1-\gamma_1 \, e^{i\theta}\right)}{\left|1-\gamma_1 \, e^{-i\theta}\right|}, \qquad
\qquad 0< \theta< 2\pi.$$ Simple algebra shows that for $\hat{\chi}_i = J_i/k_BT, \;i=1,2$, $$\begin{aligned}
\gamma_2 \gtrless 1 \Longleftrightarrow  \sinh \left(\hat{\chi}_1 + \hat{\chi}_2 \right)
- \cosh \left(\hat{\chi}_1-\hat{\chi}_2\right)
\lessgtr 0 \\
\intertext{and}
\sinh^2 \left(\hat{\chi}_1 + \hat{\chi}_2 \right) - \cosh^2 \left(\hat{\chi}_1 - \hat{\chi}_2\right) = k^{-1}_{\text{ons}} -1
\end{aligned}$$ where $k_{\text{ons}} = \left(\sinh\, 2\hat{\chi}_1 \;\sinh\,2\hat{\chi}_2\right)^{-1}$ as in [\[eq15\]](#eq15){reference-type="eqref" reference="eq15"}. Thus $$\label{eq26}
\gamma_2 \gtrless 1 \Longleftrightarrow  k_{\text{ons}} \gtrless 1.$$ In other words, sub-critical (resp. super-critical) temperatures, $T< T_c$ (resp. $T>T_c$) correspond to $z^*_2 < z_1$ (resp. $z^*_2 > z_1$). And, of course, $T=T_c \Longleftrightarrow
z^*_2 = z_1$.

It turns out that in their initial (unpublished) calculations to compute $M_0$, Kaufman and Onsager did not actually use [\[eq17\]](#eq17){reference-type="eqref" reference="eq17"}. What happened is described by Onsager in [@Ons2] and [@Ons3] (see also [@Bax] for more details, particularly concerning the Wiener-Hopf calculation below). In addition to [\[eq17\]](#eq17){reference-type="eqref" reference="eq17"}, Kaufman and Onsager had derived, but apparently did not publish (see private communication to C. Domb [@Dom2 p. 201]), an expression for the 2-point correlation function along a diagonal $\langle \sigma_{1,1}, \sigma_{1+n,\, 1+n}\rangle$, which is much simpler than [\[eq17\]](#eq17){reference-type="eqref" reference="eq17"}. Only one Toeplitz determinant is involved, $$\label{eq27}
\langle \sigma_{1,1}\, \sigma_{1+n,\, 1+n}\rangle = D_n \left(\varphi_{\text{diag}}\right)$$ where[^1] $$\label{eq28}
\varphi_{\text{diag}}\!\left(e^{i\theta}\right) = \left( \frac{1-k_{\text{ons}} \, e^{-i\theta}}{1-k_{\text{ons}}
\,e^{i\theta}} \right)^{\frac{1}{2}}$$ and again $k_{\text{ons}}$ is given as in [\[eq15\]](#eq15){reference-type="eqref" reference="eq15"} and $\varphi_{\text{diag}} (e^{i\pi})>0$. The same physical arguments as in [\[eq16\]](#eq16){reference-type="eqref" reference="eq16"} yield $$\label{eq29}
M_0 =\lim_{n\to \infty} \left\langle \sigma_{1,1} \, \sigma_{1+n, 1+n} \right\rangle^{\frac{1}{2}}.$$ Onsager then realized that the eigenvalue equation for the Toeplitz matrix $T\!\left(\varphi_{\text{diag}}\right)$, $$u_k = \frac{1}{\lambda} \sum^{n-1}_{j=0} \left(\varphi_{\text{diag}}\right)_{k-j} \, u_j,\qquad 0\le k \le n-1$$ was a discrete analog of the Milne integral equation $$\label{eq30}
f(x)  = \int^\infty_0 A(x-y)\, f(y)dy, \qquad x>0$$ which arises, with a particular, explicit function $A(\cdot)$, in radiative equilibrium theory (see, for example [@DymMc]). Milne's equation can be solved using the Wiener-Hopf method, a technique with which Onsager was familiar from lectures that Wiener had given earlier in the Mathematics Department at Yale. So Onsager tried the Wiener-Hopf technique on the above eigenvalue equation for $T (\varphi_{\text{diag}})$,

to obtain the eigenvalues $\lambda=\lambda^{(n)}_\ell$, $1\le \ell \le n$, and then computed $D_n (\varphi_{\text{diag}})= \prod^n_{\ell=1} \, \lambda^{(n)}_\ell$. Letting $n\to \infty$, formula [\[eq15\]](#eq15){reference-type="eqref" reference="eq15"} for $M_0$ then emerged. This was the basis for the first announcements of the result in 1948 and 1949. So why didn't Kaufman and Onsager publish the details of their calculation? The situation was as follows. As in the case of Milne's equation, the Wiener-Hopf method requires very detailed knowledge of the kernel $(\varphi_{\text{diag}})_{j-k}$, in the case of Ising. Onsager sensed that there was another prize to be had: What about Toeplitz determinants with general symbols $\varphi$? And so, before Kaufman and Onsager could get around to publishing their calculation, Onsager began looking for a method to evaluate asymptotically Toeplitz determinants with general symbols. We quote Onsager [@Ons3]: " ...and lo and behold I found it. It was a general formula for the evaluation of Toeplitz matrices. The only thing I did not know was how to fill out the holes in the mathematics and show the epsilons and deltas and all of that, and the limiting processes; I did not know just how it should be done and what mathematicians really knew about limiting processes in that ball park." As it turned out, by that point, mathematicians knew a lot! Before it was clear what conditions to place on the symbol, Kaufman and Onsager spoke to Kakutani and then Kakutani spoke to Szegő. Szegő then revisited his calculations from 1915, and in 1952 [@Sz3] evaluated the $o(n)$ term in [\[eq5\]](#eq5){reference-type="eqref" reference="eq5"} for a very general class of symbols $\varphi$. This celebrated result is the Szegő Strong Limit Theorem mentioned above. Faced with Szegő's general result, Kaufman and Onsager published neither their first, nor their second method. As Onsager noted [@Ons2], " ...the mathematicians got there first." In the long history of mathematics and physics, it is most unusual for a physicist to be scooped out of a formula by a mathematician!

There is, however, more to the story. On the web (see [@Bax]) there is the draft of a paper titled "Long-Range Order" from 1950 (never published), without names attached but almost certainly by Onsager and Kaufman, that describes their more general method and obtains the result [\[eq15\]](#eq15){reference-type="eqref" reference="eq15"} for $M_0$. Here the authors use formulae [\[eq16\]](#eq16){reference-type="eqref" reference="eq16"} and [\[eq17\]](#eq17){reference-type="eqref" reference="eq17"}. There is also an earlier letter [@Kau2] written on April 12, 1950, from Onsager to Kaufman containing some of the calculations from the above draft. Presumably to allay any concerns about priority, Onsager assures Kaufman at the end of the letter that "There will be time for all these things." As one reads [@Ons2] [@Ons3], one senses the faint hint of regret that Onsager must have felt for such optimism. In a letter from Kaufman to Onsager, written on May 12, 1950, a month after the letter [@Kau2], Kaufman says "Here is a draft of Crystal Statistics IV". In [@Bax], Baxter makes a strong case that the above paper from 1950 is indeed Kaufman's draft of Crystal Statistics IV. However, this may not be so. On the Onsager archive in Trondheim (see footnote [\[foot3\]](#foot3){reference-type="ref" reference="foot3"}) under "Selected research material and writings", item 17.121, one finds the paper "Long-Range order" discussed by Baxter. Although, again, no names are attached, this establishes the provenance of the paper beyond any reasonable doubt, as suspected by Baxter. Item 17.121, however, also contains a second, completely separate paper called "Crystal statistics IV. Long-Range Order in a Binary Crystal", and both Kaufman's and Onsager's names are attached.[^2] The "Long-range" paper describes, as noted above, the second method of Kaufman-Onsager for general symbols, and the second paper describes their first Wiener-Hopf type method. However, it is unfinished and it ends abruptly. So when Kaufman wrote to Onsager "Here is the draft of Crystal Statistics IV", which of these two drafts did she mean? Either way, the evidence that Kaufman/Onsager knew how to evaluate the asymptotics of Toeplitz determinants (in two ways!) is now clear and written down in their own hand.

[^1]: In [@Dom2], the symbol is $\overline{\varphi_{\text{diag}}}$, not $\varphi_{\text{diag}}$. However, the determinant is the same, $D_n(\overline{\varphi_{\text{diag}}})=\det T_n(\overline{\varphi_{\text{diag}}})=
    \det\overline{T_n(\varphi_{\text{diag}})^T}=\overline{\det T_n(\varphi_{\text{diag}})^T}=
    \det T_n(\varphi_{\text{diag}})^T=\det T_n(\varphi_{\text{diag}})=D_n(\varphi_{\text{diag}})$.

[^2]: The authors thank H. Holden for locating this paper on the Trondheim archive.

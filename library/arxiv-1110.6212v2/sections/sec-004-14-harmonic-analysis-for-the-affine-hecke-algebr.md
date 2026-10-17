---
doc_id: arxiv-1110.6212v2
doc_title: "On calibrated representations and the Plancherel Theorem for aﬃne Hecke algebras"
section_id: sec-004-14-harmonic-analysis-for-the-affine-hecke-algebr
section_title: "Harmonic analysis for the affine Hecke algebra"
section_number: 1.4
pages: 5-7
source_pdf: 1110.6212v2.pdf
source_sha256: 1923b6a0bfdc810f
toc_source: outline
text_source: latex
latex_prose_ratio: 0.939
latex_coverage_ratio: 0.965
doc_brief: "On calibrated representations and the Plancherel Theorem for aﬃne Hecke algebras — This paper has two main purposes."
---
Suppose now that $q_0,q_1,\ldots,q_n>1$. Define an involution $*$ on $\mathscr{H}_L$ and the *canonical trace functional* $\mathrm{Tr}:\mathscr{H}_L\to\mathbb{C}$ by $$\begin{aligned}
\bigg(\sum_{w\in W_L}c_wT_w\bigg)^*=\sum_{w\in W_L}\overline{c_w}T_{w^{-1}}\quad\textrm{and}\quad \mathrm{Tr}\bigg(\sum_{w\in W_L}c_wT_w\bigg)=c_1.
\end{aligned}$$ An induction on $\ell(v)$ shows that $\mathrm{Tr}(T_uT_v^*)=\delta_{u,v}$ for all $u,v\in W_L$, and so $$\begin{aligned}
\mathrm{Tr}(h_1h_2)=\mathrm{Tr}(h_2h_1)\qquad\textrm{for all $h_1,h_2\in\mathscr{H}_L$}.
\end{aligned}$$ Thus $(h_1,h_2)=\mathrm{Tr}(h_1h_2^*)$ defines an Hermitian inner product on $\mathscr{H}_L$. Let $\|h\|_2=\sqrt{(h,h)}$. The algebra $\mathscr{H}_L$ acts on itself by left multiplication, and the corresponding operator norm is $$\|h\|=\sup\{\|hx\|_2\,:\,x\in\mathscr{H}_L,\|x\|_2\leq 1\}.$$ Let $\overline{\mathscr{H}_L}$ denote the completion of $\mathscr{H}_L$ with respect to this norm. Thus $\overline{\mathscr{H}_L}$ is a non-commutative $C^*$-algebra. This algebra is 'liminal'. Even better, all irreducible representations of $\overline{\mathscr{H}_L}$ are finite dimensional, and so by [@dixmier §8.8] there exists a probability measure $\mu$ such that $$\begin{aligned}
\label{eq:plancherelgeneral}\mathrm{Tr}(h)=\int_{\mathrm{spec}(\overline{\mathscr{H}_L})}\chi_{\pi}(h)d\mu(\pi)\qquad\textrm{for all $h\in\overline{\mathscr{H}_L}$.}
\end{aligned}$$ The measure $\mu$ is the *Plancherel measure*. Only those representations of $\mathscr{H}_L$ which extend to the completion $\overline{\mathscr{H}_L}$ appear in the Plancherel Theorem. It is known [@opdamhanalysis Corollary 6.2] that these are the *tempered* representations of $\mathscr{H}_L$ (see [@opdamhanalysis §2.7] for the definition).

If $t\in\mathrm{Hom}(L,\mathbb{C}^{\times})$ we write $t^{\lambda}=t(\lambda)$. The Weyl group $W_0$ acts on $\mathrm{Hom}(L,\mathbb{C}^{\times})$ by the formula $(wt)^{\lambda}=t^{w^{-1}\lambda}$. Following [@opdamtrace], define a function $G_t:\mathscr{H}_L\to\mathbb{C}$ by $$\begin{aligned}
\label{eq:Gdefn}
G_t(h)=\sum_{\mu\in L}t^{-\mu}\mathrm{Tr}(x^{\mu} h)
\end{aligned}$$ whenever the series converges. From [@opdamtrace] we have the following (see also [@opdamhanalysis (3.9)]).

::: thm
[]{#thm:prelim_main label="thm:prelim_main"} The series $G_t(h)$ is absolutely convergent for all $h\in\mathscr{H}_L$ whenever $|t^{\alpha_i^{\vee}}|<q_i^{-1}$ for $(R,i)\neq (BC_n,n)$ and $|t^{\alpha_n^{\vee}}|<q_0^{-1}q_n^{-1}$ for $(R,i)=(BC_n,n)$. Moreover, $$\begin{aligned}
\label{eq:prelim_main1}
G_t(h)=\frac{g_t(h)}{q_{w_0}c(t)c(t^{-1})d(t)}
\end{aligned}$$ where for each fixed $h$ the function $g_t(h)$ has a analytic continuation in the $t$-variable to $\mathrm{Hom}(L,\mathbb{C}^{\times})$. Moreover, $g_t(h)$ satisfies

1.  $g_t(h)$ is a polynomial in $\{t^{\lambda}\mid \lambda\in L\}$ (for fixed $h\in\mathscr{H}_L$),

2.  $g_t(1)=d(t)$ for all $t\in\mathrm{Hom}(L,\mathbb{C}^{\times})$, and

3.  $g_t(x^{\lambda}hx^{\mu})=t^{\lambda+\mu}g_t(h)$ for all $\lambda,\mu\in L$ and all $h\in\mathscr{H}_L$.
:::

::: remark
[]{#rem:explicit label="rem:explicit"} (a) Note that $t^{\lambda}g_t(\tau_w)=g_t(\tau_w x^{\lambda})=g_t(x^{w\lambda}\tau_w)=t^{w\lambda}g_t(\tau_w),$ and so if $wt\neq t$ then $$g_t(\tau_wx^{\lambda})=\delta_{w,1}t^{\lambda}d(t).$$ Then by condition 1 in the theorem this formula holds for all $t\in\mathrm{Hom}(L,\mathbb{C}^{\times})$.

\(b\) The three conditions in the theorem completely determine $g_t(h)$. For example consider the $\tilde{A}_2$ case. It is sufficient to calculate $g_t(T_w)$ for each $w\in W_0$, because $g_t(T_wx^{\lambda})=t^{\lambda}g_t(T_w)$. Write $Q=q^{\frac{1}{2}}-q^{-\frac{1}{2}}$. Applying $g_t$ to the Bernstein relation $T_1x^{\alpha_1^{\vee}}=x^{-\alpha_1^{\vee}}T_1+Q(1+x^{\alpha_1^{\vee}})$ gives $$g_t(T_1)=Q(1-t^{-\alpha_1^{\vee}})^{-1}d(t)=Q(1-t^{-\alpha_2^{\vee}})(1-t^{-\alpha_1^{\vee}-\alpha_2^{\vee}}).$$ Similarly, $g_t(T_2)=Q(1-t^{-\alpha_1^{\vee}})(1-t^{-\alpha_1^{\vee}-\alpha_2^{\vee}})$, $g_t(T_1T_2)=g_t(T_2T_1)=Q^2(1-t^{-\alpha_1^{\vee}-\alpha_2^{\vee}})$, and $g_t(T_1T_2T_1)=Q^3+Q(1-t^{-\alpha_1^{\vee}})(1-t^{-\alpha_2^{\vee}})$, making ([\[eq:prelim_main1\]](#eq:prelim_main1){reference-type="ref" reference="eq:prelim_main1"}) completely explicit in type $\tilde{A}_2$.
:::

Let $$\begin{aligned}
\label{eq:f}
f_t(h)=\frac{g_t(h)}{d(t)}.
\end{aligned}$$ Note that $f_t(h)$ may have poles at points where $t^{\alpha^{\vee}}=1$ for some $\alpha\in R_0$. Fix a $\mathbb{Z}$-basis $\lambda_1,\ldots,\lambda_n$ of $L$. From ([\[eq:Gdefn\]](#eq:Gdefn){reference-type="ref" reference="eq:Gdefn"}) and ([\[eq:prelim_main1\]](#eq:prelim_main1){reference-type="ref" reference="eq:prelim_main1"}) we have $$\begin{aligned}
\label{eq:prelim_main}
\mathrm{Tr}(h)=\frac{1}{q_{w_0}}\int_{a_1\mathbb{T}}\cdots\int_{a_n\mathbb{T}} \frac{f_t(h)}{c(t)c(t^{-1})}\,dt_1\cdots dt_n
\end{aligned}$$ where $t_i=t^{\lambda_i}$, $dt_i$ is Haar measure on the circle group $\mathbb{T}$, and where $a_1,\ldots,a_n>0$ are chosen such that if $t\in\mathrm{Hom}(L,\mathbb{C}^{\times})$ with $|t^{\lambda_i}|=a_i$ for each $i$ then $|t^{\alpha_i^{\vee}}|<q_i^{-1}$ (if $(R,i)\neq (BC_n,n)$) and $|t^{\alpha_n^{\vee}}|<q_0^{-1}q_n^{-1}$ (if $(R,i)=(BC_n,n)$). Formula ([\[eq:prelim_main\]](#eq:prelim_main){reference-type="ref" reference="eq:prelim_main"}) appears in [@opdamhanalysis Theorem 3.7], and is the starting point of the Plancherel Theorem.

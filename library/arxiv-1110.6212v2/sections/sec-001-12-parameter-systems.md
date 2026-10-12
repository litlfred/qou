---
doc_id: arxiv-1110.6212v2
doc_title: "On calibrated representations and the Plancherel Theorem f or affine Hecke algebras James Parkinson ∗"
section_id: sec-001-12-parameter-systems
section_title: "Parameter systems"
section_number: 1.2
pages: 3-8
source_pdf: 1110.6212v2.pdf
source_sha256: 1923b6a0bfdc810f
doc_brief: "On calibrated representations and the Plancherel Theorem f or affine Hecke algebras James Parkinson ∗ — This paper has two main purposes."
text_source: latex
latex_prose_ratio: 0.948
latex_coverage_ratio: 0.982
---
Let $q_0,q_1,\ldots,q_n\in\mathbb{C}^{\times}$ be such that $q_i=q_j$ whenever $s_i$ and $s_j$ are conjugate in $W_Q$. We call the sequence $(q_i)$ a *parameter system*. By [@bourbaki IV, §5, No.5, Prop 5] the product $$q_w=q_{i_1}\cdots q_{i_{\ell}}\quad\textrm{(where $w=s_{i_1}\cdots s_{i_{\ell}}\in W_Q$ is reduced)}$$ does not depend on the particular reduced expression for $w$. If $\alpha\in W_0\alpha_i\cap W_0\alpha_j$ then $s_i$ and $s_j$ are conjugate in $W_0$, and hence for $\alpha\in R_0$ we define $$q_{\alpha}=q_i\qquad\textrm{if $\alpha\in W_0 \alpha_i$}.$$

Let $\mathbb{C}[L]=\mathbb{C}\textrm{-span }\{x^{\lambda}\mid \lambda\in L\}$ be the group algebra of $L$, with the group operation written multiplicatively as $x^{\lambda}x^{\mu}=x^{\lambda+\mu}$. In the field of fractions of $\mathbb{C}[L]$ let (for $\alpha\in R_0$) $$\begin{aligned}
c_{\alpha}(x)=\begin{cases}\displaystyle{\frac{1-q_{\alpha}^{-1}x^{-\alpha^{\vee}}}{1-x^{-\alpha^{\vee}}}}&\textrm{if $\alpha\in R_1$}\\
\displaystyle{\frac{(1-q_0^{-1/2}q_n^{-1/2}x^{-\alpha^{\vee}/2})(1+q_0^{1/2}q_n^{-1/2}x^{-\alpha^{\vee}/2})}{1-x^{-\alpha^{\vee}}}}&\textrm{if $\alpha\in R_2$.}
\end{cases}
\end{aligned}$$ (Note that if $\alpha\in R_2$ then $2\alpha\in R$, and so $(2\alpha)^{\vee}=\alpha^{\vee}/2$ is in $L$.) Choose relatively prime elements $n_{\alpha}(x)$ and $d_{\alpha}(x)$ in $\mathbb{C}[L]$ so that $$c_{\alpha}(x)=\frac{n_{\alpha}(x)}{d_{\alpha}(x)}.$$ For example, $\alpha\in R_2$ and $q_n^{1/2}=q_0^{1/2}$ then $n_{\alpha}(x)=1-q_n^{-1}x^{-\alpha^{\vee}/2}$ and $d_{\alpha}(x)=1-x^{-\alpha^{\vee}/2}$.

Similarly, let $$\begin{aligned}
c_{\alpha}'(x)=\begin{cases}
\displaystyle{\frac{1-q_{\alpha}^{-1}}{1-x^{-\alpha^{\vee}}}}&\textrm{if $\alpha\in R_1$}\\
\displaystyle{\frac{1-q_n^{-1}+q_n^{-1/2}(q_0^{1/2}-q_0^{-1/2})x^{-\alpha^{\vee}/2}}{1-x^{-\alpha^{\vee}}}}&\textrm{if $\alpha\in R_2$}.
\end{cases}
\end{aligned}$$ Then, with $d_{\alpha}(x)$ as above, $$c_{\alpha}'(x)=\frac{n_{\alpha}'(x)}{d_{\alpha}(x)}$$ for some $n_{\alpha}'(x)\in\mathbb{C}[L]$ with $n_{\alpha}'(x)$ and $d_{\alpha}(x)$ relatively prime.

Let $$\begin{aligned}
c(x)&=\prod_{\alpha\in R_0^+}c_{\alpha}(x),&n(x)&=\prod_{\alpha\in R_0^+}n_{\alpha}(x),&d(x)&=\prod_{\alpha\in R_0^+}d_{\alpha}(x).
\end{aligned}$$ The expression $c(x)=n(x)/d(x)$ is the *Macdonald $c$-function*. We write $c_i(x)$, $c_i'(x)$, $n_i(x)$, $n_i'(x)$, and $d_i(x)$ for $n_i(x)$ for $c_{\alpha_i}(x)$, $c_{\alpha_i}'(x)$, $n_{\alpha_i}(x)$, $n_{\alpha_i}'(x)$, and $d_{\alpha_i}(x)$ (respectively).

## Affine Hecke algebras

Standard references for affine Hecke algebras include [@lusztig], [@macblue] and [@ram1]. With the above notation, the *affine Hecke algebra* $\mathscr{H}_L$ with *parameters* $q_0,\ldots,q_n$ is the algebra over $\mathbb{C}$ with vector space basis $\{T_w\mid w\in W_L\}$ and relations $$\begin{aligned}
T_uT_v&=T_{uv}&&\textrm{if $\ell(uv)=\ell(u)+\ell(v)$}\\
T_{i}^2&=1+(q_i^{\frac{1}{2}}-q_i^{-\frac{1}{2}})T_i&&\textrm{for all $i=0,1,\ldots,n$},
\end{aligned}$$ where we write $T_i=T_{s_i}$.

The above presentation is the *Coxeter* presentation of $\mathscr{H}_L$. There is a second important presentation which exploits the semidirect product structure $W_L=L\rtimes W_0$. This is the *Bernstein presentation*, given by ([\[eq:rel1\]](#eq:rel1){reference-type="ref" reference="eq:rel1"})--([\[eq:rel4\]](#eq:rel4){reference-type="ref" reference="eq:rel4"}) below. Each $\lambda\in L$ can be written as $\lambda=\mu-\nu$ with $\mu,\nu\in L\cap P^+$, and we define $$x^{\lambda}=T_{t_{\mu}}T_{t_{\nu}}^{-1}.$$ It is not hard to see that this is well defined, and in particular $x^{\lambda}=T_{t_{\lambda}}$ if $\lambda$ is dominant.

It can be shown [@macblue] that $\mathscr{H}_L$ has vector space basis $\{T_wx^{\lambda}\mid \lambda\in L,w\in W_0\}$ and relations $$\begin{aligned}
\label{eq:rel1}T_i^2&=1+(q_i^{\frac{1}{2}}-q_i^{-\frac{1}{2}})T_i&&\textrm{for $i=1,\ldots,n$}\\
\label{eq:rel2}T_iT_jT_i\cdots&=T_jT_iT_j\cdots\quad\textrm{($m_{ij}$ factors)}&&\textrm{for $1\leq i<j\leq n$}\\
\label{eq:rel3}x^{\lambda}x^{\mu}&=x^{\lambda+\mu}&&\textrm{for all $\lambda,\mu\in L$}\\
\label{eq:rel4}T_ix^{\lambda}-x^{s_i\lambda}T_i&=q_i^{\frac{1}{2}}c_i'(x)(x^{\lambda}-x^{s_i\lambda})&&\textrm{for $1\leq i\leq n$ and $\lambda\in L$.}
\end{aligned}$$ Thus we see a copy of the group algebra $\mathbb{C}[L]$ of the lattice $L$ inside of $\mathscr{H}_L$. The relation ([\[eq:rel4\]](#eq:rel4){reference-type="ref" reference="eq:rel4"}) is the *Bernstein relation*. Since $s_i\lambda=\lambda-\langle \lambda,\alpha_i\rangle\alpha_i^{\vee}$ and $\langle\lambda,\alpha_i\rangle\in\mathbb{Z}$ the "fraction" $c_i'(x)(x^{\lambda}-x^{s_i\lambda})$ that appears in the Bernstein relation is actually an element of $\mathbb{C}[L]$.

It is well known (see, for example, [@macblue (4.2.10)]) that the centre of $\mathscr{H}_L$ is $$\mathbb{C}[L]^{W_0}=\{f\in\mathbb{C}[L]\mid w\cdot f=f\textrm{ for all $w\in W_0$}\}.$$ This has powerful implications for the representation theory of $\mathscr{H}_L$. For example it forces the irreducible representations to be finite dimensional (since the centre acts on irreducible representations by scalars, and it is evident that $\mathscr{H}_L$ is finite dimensional over $\mathbb{C}[L]^{W_0}$).

It is natural to seek modifications $\tau_w$ of $T_w$ which satisfy a "simplified Bernstein relation" $$\begin{aligned}
\label{eq:simpbernstein}
\tau_w x^{\lambda}=x^{w\lambda}\tau_w\qquad\textrm{for all $w\in W_0$ and $\lambda\in L$}.
\end{aligned}$$ Define elements $\tau_1,\ldots,\tau_n\in\mathscr{H}_L$ by $$\tau_i=d_i(x)T_i-q_i^{\frac{1}{2}}n_i'(x).$$ The Bernstein relation gives $\tau_ix^{\lambda}=x^{s_i\lambda}\tau_i$, and it can be shown (see [@ramcalib Proposition 2.7] for example) that for $w\in W_0$ the product $$\tau_w=\tau_{i_1}\cdots \tau_{i_{\ell}}\quad\textrm{is independent of the choice of reduced expression $w=s_{i_1}\cdots s_{i_{\ell}}$.}$$ Thus the elements $\tau_w$, $w\in W_0$, satisfy ([\[eq:simpbernstein\]](#eq:simpbernstein){reference-type="ref" reference="eq:simpbernstein"}), and a direct calculation gives the useful formula $$\begin{aligned}
\label{eq:tausquared}
\tau_i^2=q_i\,n_i(x)n_i(x^{-1})\in\mathbb{C}[L].
\end{aligned}$$

## Harmonic analysis for the affine Hecke algebra

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

# Representations of affine Hecke algebras

Let $M$ be a finite dimensional $\mathscr{H}_L$-module. For each $t\in\mathrm{Hom}(L,\mathbb{C}^{\times})$ let $$\begin{aligned}
M_t&=\{v\in M\mid x^{\lambda}\cdot v=t^{\lambda}v\quad\textrm{for all $\lambda\in L$}\}\\
M_t^{\mathrm{gen}}&=\{v\in M\mid \textrm{for each $\lambda\in L$ there is a $k>0$ such that $(x^{\lambda}-t^{\lambda})^k\cdot v=0$}\}
\end{aligned}$$ be the *$t$-weight space* and the *generalised $t$-weight space* respectively. Each finite dimensional $\mathscr{H}_L$-module $M$ decomposes into a direct sum of generalised $t$-weight spaces $$M=\bigoplus_{t\in\mathrm{supp}(M)}M_t^{\mathrm{gen}}$$ where $\mathrm{supp}(M)=\{t\in\mathrm{Hom}(L,\mathbb{C}^{\times})\mid M_t^{\mathrm{gen}}\neq 0\}$ is the *support* of $M$.

A finite dimensional $\mathscr{H}_L$-module $M$ is *calibrated* if $$M_t^{\mathrm{gen}}=M_t\qquad\textrm{for all $t\in\mathrm{supp}(M)$}.$$ (In the literature this is also refereed to as *tame*). The main purpose of the first half of this paper is to construct calibrated irreducible representations of general affine Hecke algebras. We suspect that a complete classification of calibrated representations along the lines of the $1$-parameter case is possible (perhaps with some restrictions like $W_t=W_{(t)}$), although such a classification requires detailed information about the representation theory of rank $2$ (multi-parameter) affine Hecke algebras, and this would take us beyond the scope of the present paper. Thus the focus of this paper is on construction, and the question of classification will be pursued in later work.

The elements $\tau_i\in\mathscr{H}_L$, considered as operators on a representation, are often called *intertwining operators* because of the following fundamental and important fact.

::: lemma
[]{#lem:bijection label="lem:bijection"} Let $1\leq i\leq n$. Let $M$ be a finite dimensional $\mathscr{H}_L$-module, and suppose that $t\in\mathrm{supp}(M)$. Then as operators, $$\tau_i:M^{\mathrm{gen}}_t\to M^{\mathrm{gen}}_{s_it}\qquad\textrm{and}\qquad\tau_i:M_{s_it}^{\mathrm{gen}}\to M_t^{\mathrm{gen}}.$$ Moreover, $n_i(t)n_i(t^{-1})\neq 0$ if and only if each operator is bijective.
:::

::: proof
*Proof.* Let $m\in M_t^{\mathrm{gen}}$. By ([\[eq:simpbernstein\]](#eq:simpbernstein){reference-type="ref" reference="eq:simpbernstein"}) we compute $$(x^{\lambda}-(s_it)^{\lambda})^k\tau_i\cdot m=\tau_i(x^{s_i\lambda}-t^{s_i\lambda})^k\cdot m=0$$ for sufficiently large $k$. Thus $\tau_i\cdot m\in M_{s_it}^{\mathrm{gen}}$. For the final claim, note that by ([\[eq:tausquared\]](#eq:tausquared){reference-type="ref" reference="eq:tausquared"}) the operator $\tau_i^2:M_t^{\mathrm{gen}}\to M_t^{\mathrm{gen}}$ is given by $\tau_i^2\cdot m=q_in_i(t)n_i(t^{-1})m$. ◻
:::

By Schur's Lemma (see [@varadarajan]) the centre $\mathbb{C}[L]^{W_0}$ of $\mathscr{H}_L$ acts on an irreducible module $M$ by scalars. It follows that there exists $t\in \mathrm{Hom}(L,\mathbb{C}^{\times})$ such that $$p(x)\cdot v=p(t)v\qquad\textrm{for all $p(x)\in\mathbb{C}[L]^{W_0}$ and all $v\in M$.}$$ The element $t$ is only defined up to $W_0$ orbits. The orbit $W_0t$ is called the *central character* of $M$, although as is customary we will usually refer to any $t'\in W_0t$ as 'the' central character of $M$. A central character $t\in\mathrm{Hom}(L,\mathbb{C}^{\times})$ is called *regular* if $t^{\alpha^{\vee}}\neq 1$ for all $\alpha\in R_0$.

---
doc_id: arxiv-0707.3799v3
doc_title: "Equivariant Satake category and Kostant-Whittaker reduction"
section_id: sec-014-42-de-symmetrized-kostant-functor-κℏ
section_title: "De-symmetrized Kostant functor κℏ"
section_number: 4.2
pages: 15-16
source_pdf: 0707.3799v3.pdf
source_sha256: 0b29cbced7939f72
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.823
latex_coverage_ratio: 0.928
doc_brief: "Equivariant Satake category and Kostant-Whittaker reduction — 24 sections: Front matter; Introduction; Notation and statements of the res"
---
We denote by $\pi$ the projection $\check{\mathfrak t}{}^*\to\check{\mathfrak t}{}^*/W$, and we denote by $(\pi,\Id,\Id)$ the projection $\check{\mathfrak t}{}^*\times(\check{\mathfrak t}{}^*/W)\times{\mathbb A}^1
\to\check{\mathfrak t}{}^*/W\times\check{\mathfrak t}{}^*/W\times{\mathbb A}^1$. For $V\in Rep({\check{G}})$ we are going to describe $(\pi,\Id,\Id)^*\phi(V)\in Coh(\check{\mathfrak t}{}^*\times(\check{\mathfrak t}{}^*/W)\times{\mathbb A}^1)$.

To this end we consider the universal Verma module $\CM_\hbar(-\rho)=
U_\hbar\otimes_{U_\hbar(\check{\mathfrak b}{})}\mathsf k[\hbar][\check{\mathfrak t}{}](-\rho)$, and $\mathsf k[\hbar][\check{\mathfrak t}{}](-\rho)$ is a $U_\hbar(\check{\mathfrak b}{})$-module which factors through the $U_\hbar(\check{\mathfrak t}{})=\mathsf k[\hbar][\check{\mathfrak t}{}]$-module where $t\in\check{\mathfrak t}{}$ acts by multiplication by $t-\hbar\rho(t)$ (recall that $\rho$ is the halfsum of positive roots of $\check{\mathfrak g}{}$). For an $\hbar$-Harish-Chandra bimodule $M$ we set $\varkappa_\hbar(M):=\CM_\hbar(-\rho)\overset{L}{\otimes}_{U_\hbar}M
\overset{L}{\otimes}_{U_\hbar(\check{\mathfrak n}{}_-)_2}\psi=
\mathsf k[\hbar][\check{\mathfrak t}{}](-\rho)\overset{L}{\otimes}_{U_\hbar(\check{\mathfrak b}{})_1}M
\overset{L}{\otimes}_{U_\hbar(\check{\mathfrak n}{}_-)_2}\psi$. This is an ${\mathcal O}(\check{\mathfrak t}{}^*\times(\check{\mathfrak t}{}^*/W)\times{\mathbb A}^1)$-module: the action of ${\mathcal O}(\check{\mathfrak t}{}^*\times{\mathbb A}^1)=U_\hbar(\check{\mathfrak t}{})$ comes from the fact that $U_\hbar(\check{\mathfrak t}{})$ normalizes $U_\hbar(\check{\mathfrak b}{})$, and the action of ${\mathcal O}(\check{\mathfrak t}{}^*/W\times{\mathbb A}^1)$ is the action of the center $Z(U_\hbar)$ of the second copy of $U_\hbar$, as before.

For $V\in Rep({\check{G}})$ we set $\varphi(V):=\varkappa_\hbar(Fr(V))$.

::: lem
[]{#mit label="mit"} For $V\in Rep({\check{G}})$ we have a canonical isomorphism $\varphi(V)\simeq(\pi,\Id,\Id)^*\phi(V)$.
:::

*Proof* : We denote by $\CW_\hbar^-:=U_\hbar\otimes_{U_\hbar(\check{\mathfrak n}{}_-)}\psi$ the Whittaker $U_\hbar$-module. By a theorem of Kostant, $\End_{U_\hbar}(\CW_\hbar^-)=Z(U_\hbar)$, and the category $\CA$ of $(U_\hbar(\check{\mathfrak n}{}_-),\psi)$-integrable $U_\hbar$-modules is equivalent to the category of $Z(U_\hbar)$-modules (here a $U_\hbar(\check{\mathfrak n}{}_-)$-module $L$ is called $(U_\hbar(\check{\mathfrak n}{}_-),\psi)$-integrable if the action of $\check{\mathfrak n}{}_-$ on $L\otimes(-\psi)$ is locally nilpotent). Namely, a $(U_\hbar(\check{\mathfrak n}{}_-),\psi)$-integrable $U_\hbar$-module $L$ goes to the $Z(U_\hbar)$-module $Hom_{U_\hbar}(\CW_\hbar^-,L)$. Conversely, a $Z(U_\hbar)$-module $R$ goes to $\CW_\hbar^-\otimes_{Z(U_\hbar)}R$. In particular, $\CW_\hbar^-$ goes to the free module $Z(U_\hbar)$.

For an $\hbar$-Harish-Chandra bimodule $M$ we will construct a canonical isomorphism $\kappa_\hbar(M)\simeq 
Hom_{U_\hbar}(\CW_\hbar^-,M\otimes_{U_\hbar}\CW_\hbar^-)$. In effect, $L\mapsto M\otimes_{U_\hbar}L$ is a right-exact endofunctor of the category of $(U_\hbar(\check{\mathfrak n}{}_-),\psi)$-integrable $U_\hbar$-modules. Under Kostant's equivalence, this endofunctor goes to the convolution with the $Z(U_\hbar)$-bimodule $X$ which corresponds by Kostant to our endofunctor applied to $\CW_\hbar^-$. In other words, $X=Hom_{U_\hbar}(\CW_\hbar^-,M\otimes_{U_\hbar}\CW_\hbar^-)$. We have a tautological isomorphism $X\otimes_{Z(U_\hbar)}\CW_\hbar^-{\stackrel{\sim}{\longrightarrow}}
M\otimes_{U_\hbar}\CW_\hbar^-$. This yields the desired isomorphism $X{\stackrel{\sim}{\longrightarrow}}\kappa_\hbar(M)$. In particular, for a free $\hbar$-Harish-Chandra bimodule $M=Fr(V)$, we obtain $\phi(V)\otimes_{Z(U_\hbar)}\CW_\hbar^-{\stackrel{\sim}{\longrightarrow}}
V\otimes_{\mathsf k}\CW_\hbar^-$.

Now let us compute $(\CM_\hbar(-\rho)\otimes V\otimes \CW_\hbar^-)\otimes_{U_\hbar}
\mathsf k[\hbar]=
(\CM_\hbar(-\rho)\otimes(V\otimes \CW_\hbar^-))\otimes_{U_\hbar}\mathsf k[\hbar]{\stackrel{\sim}{\longrightarrow}}
(\CM_\hbar(-\rho)\otimes(\CW_\hbar^-\otimes_{Z(U_\hbar)}\phi(V)))
\otimes_{U_\hbar}\mathsf k[\hbar]{\stackrel{\sim}{\longrightarrow}}(\pi,\Id,\Id)^*\phi(V)$. The last isomorphism arises from $(\CM_\hbar(-\rho)
\otimes\CW_\hbar^-)\otimes_{U_\hbar}\mathsf k[\hbar]{\stackrel{\sim}{\longrightarrow}}
U_\hbar(\check{\mathfrak t}{})={\mathcal O}(\check{\mathfrak t}{}^*)$, since $\CM_\hbar(-\rho)=U_\hbar\otimes_{U_\hbar(\check{\mathfrak b}{})}
\mathsf k[\hbar][\check{\mathfrak t}{}](-\rho)$, and $\CW_\hbar^-=U_\hbar\otimes_{U_\hbar(\check{\mathfrak n}{}_-)}\psi$.

On the other hand, $(\CM_\hbar(-\rho)\otimes V\otimes \CW_\hbar^-)\otimes_{U_\hbar}
\mathsf k[\hbar]=
((\CM_\hbar(-\rho)\otimes V)\otimes \CW_\hbar^-)
\otimes_{U_\hbar}\mathsf k[\hbar]{\stackrel{\sim}{\longrightarrow}}
(\CM_\hbar(-\rho)\otimes V)\overset{L}{\otimes}_{U_\hbar(\check{\mathfrak n}{}_-)_2}\psi{\stackrel{\sim}{\longrightarrow}}
\mathsf k[\hbar][\check{\mathfrak t}{}](-\rho)\overset{L}{\otimes}_{U_\hbar(\check{\mathfrak b}{})_1}(U_\hbar\otimes V)
\overset{L}{\otimes}_{U_\hbar(\check{\mathfrak n}{}_-)_2}\psi=\varphi(V)$.

This completes the proof of the lemma. $\Box$

## Canonical filtration on $\varphi(V)$ {#canon}

For $V\in Rep({\check{G}})$ we have $\varphi(V)=(\CM_\hbar(-\rho)\otimes V)
\otimes_{U_\hbar(\check{\mathfrak n}{}_-)}\psi$. Note that $\CM_\hbar(-\rho)\otimes V$ has a canonical filtration with associated graded $\bigoplus_\lambda\CM_\hbar(\lambda-\rho)\otimes\ _\lambda V$, where $\lambda$ is a weight of $\check{\mathfrak t}{}$, and $_\lambda V$ is the corresponding weight space of $V$; furthermore, $\CM_\hbar(\lambda-\rho)=
U_\hbar\otimes_{U_\hbar(\check{\mathfrak b}{})}\mathsf k[\hbar][\check{\mathfrak t}{}](\lambda-\rho)$, and $\mathsf k[\hbar][\check{\mathfrak t}{}](\lambda-\rho)$ is a $U_\hbar(\check{\mathfrak b}{})$-module which factors through the $U_\hbar(\check{\mathfrak t}{})=\mathsf k[\hbar][\check{\mathfrak t}{}]$-module where $t\in\check{\mathfrak t}{}$ acts by multiplication by $t+\hbar\lambda(t)-\hbar\rho(t)$.

It follows that $\varphi(V)$ has a canonical filtration with associated graded $\bigoplus_\lambda
(\CM_\hbar(\lambda-\rho)\otimes_{U_\hbar(\check{\mathfrak n}{}_-)}\psi)\otimes\ _\lambda V$. Note that $\CM_\hbar(\lambda-\rho)\otimes_{U_\hbar(\check{\mathfrak n}{}_-)}\psi$ is a ${\mathcal O}(\check{\mathfrak t}{}^*\times(\check{\mathfrak t}{}^*/W)\times{\mathbb A}^1)$-module since $\CM_\hbar(\lambda-\rho)$ is a $U_\hbar(\check{\mathfrak t}{})-Z(U_\hbar)$-bimodule. To describe $\CM_\hbar(\lambda-\rho)\otimes_{U_\hbar(\check{\mathfrak n}{}_-)}\psi$ as a coherent sheaf on $\check{\mathfrak t}{}^*\times(\check{\mathfrak t}{}^*/W)\times{\mathbb A}^1$, we denote by $(\Id,\pi,\Id)$ the projection from $\check{\mathfrak t}{}^*\times\check{\mathfrak t}{}^*\times{\mathbb A}^1$ to $\check{\mathfrak t}{}^*\times(\check{\mathfrak t}{}^*/W)\times{\mathbb A}^1$, and we denote by $\Gamma_\lambda\subset
\check{\mathfrak t}{}^*\times\check{\mathfrak t}{}^*\times{\mathbb A}^1$ the subscheme defined by the equations $\Gamma_\lambda=\{(t_1,t_2,a):\ t_2=t_1+a\lambda\}$. Then $\CM_\hbar(\lambda-\rho)\otimes_{U_\hbar(\check{\mathfrak n}{}_-)}\psi=
(\Id,\pi,\Id)_*{\mathcal O}(\Gamma_\lambda)$.

We have proved the following

::: lem
[]{#Mit label="Mit"} For $V\in Rep({\check{G}})$, the ${\mathcal O}(\check{\mathfrak t}{}^*\times(\check{\mathfrak t}{}^*/W)\times{\mathbb A}^1)$-module $\varphi(V)$ has a canonical filtration with associated graded $\bigoplus_\lambda
(\Id,\pi,\Id)_*{\mathcal O}(\Gamma_\lambda)\otimes\ _\lambda V$. In particular, $\varphi(V)$ is flat as an ${\mathcal O}(\check{\mathfrak t}{}^*\times{\mathbb A}^1)$-module.
:::

$\Box$

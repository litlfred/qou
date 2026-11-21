---
doc_id: arxiv-0911.3569v1
doc_title: "MULTIVARIATE STABLE POLYNOMIALS: THEORY AND APPLICATIONS"
section_id: sec-019-72-a-conjecture-of-liggett-and-pemantle
section_title: "A conjecture of Liggett and Pemantle."
section_number: 7.2
pages: 20-22
source_pdf: 0911.3569v1.pdf
source_sha256: 4e7c15c9724fb453
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.96
doc_brief: "MULTIVARIATE STABLE POLYNOMIALS: THEORY AND APPLICATIONS — Univariate polynomials with only real roots – while special – do occur often enough that their properties can lead to interesting"
---
In the early 2000s, Liggett and Pemantle arrived independently at
the following conjecture, now a theorem.

\begin{theorem}[Theorem 5.2 of \cite{BBL}]
If the initial distribution $\varphi_0$ of a SEP is deterministic (\emph{i.e.}
concentrated on a single state) then $\varphi_t$ is NA for all $t\geq 0$.
\end{theorem}
\begin{proof}
This amounts to finding a class $\Stab$ of probability distributions
such that:\\
(1)\ deterministic distributions are in $\Stab$,\\
(2)\ being in $\Stab$ implies NA, and\\
(3)\ time evolution of the SEP preserves membership in $\Stab$.

Borcea, Br\"and\'en, and Liggett \cite{BBL} identified such a 
class:\ $\varphi$ is in $\Stab$ if and only if the partition function
$Z(\varphi)$ is homogeneous, multiaffine, and real stable.
(Notice that if $\varphi$ is in $\Stab$ then $\varphi^{\a}$ is in 
$\Stab$ for all $\a\in\RR^{\Lambda}$ with $\a>\zero$, by scaling.)
We proceed to check the three claims above.

Claim (1) is trivial, since if $\varphi(S)=1$ then 
$Z(\varphi)=\x^{S}$, which is clearly homogeneous, multiaffine, and real
stable.

To check claim (2) we verify the hypotheses of the Feder-Mihail 
Theorem.  Hypotheses (i) and (ii) hold since $Z(\varphi)$ is 
multiaffine and homogeneous.  By specialization and contraction,
(iii) holds.  To check (iv), let $\a\in\RR^{\Lambda}$ with $\a>\zero$,
let $\{i,j\}\subseteq \Lambda$, and consider the probability 
distribution $\varphi^{\a}$ on $\Omega$.  The occupation 
probability for site $i$ is
$$
\Pr[\E_{\{i\}}] = \sum_{S\in\{0,1\}^\Lambda:\ S(i)=1}
\frac{\varphi(S)\a^{S}}{Z(\varphi;\a)}
=
a_{i} \frac{\partial_{i}Z(\varphi;\a)}{Z(\varphi;\a)},
$$
and similarly for $\Pr[\E_{\{j\}}]$.  Likewise,
$\Pr[\E_{\{i,j\}}] =
a_{i}a_{j}Z(\varphi;\a)^{-1} \cdot \partial_{i}\partial_{j} Z(\varphi;\a)$.
Now
$$
\Pr[\E_{\{i,j\}}]  - \Pr[\E_{\{i\}}]\cdot \Pr[\E_{\{j\}}] 
=
- \frac{a_{i}a_{j}}{Z(\varphi;\a)^{2}} \cdot \Delta_{ij} Z(\varphi;\a) \leq 0,
$$
by Theorem 3.1.  Thus $\varphi^{\a}$ is NC.
By the Feder-Mihail Theorem, every $\varphi$ in $\Stab$ is NA.

To check claim (3) we need some of the theory of continuous time Markov 
chains.  The time evolution of a Markov chain $\MM$ with finite
state space $\Omega$ is governed by a one-parameter semigroup $T(t)$
of transformations of $\RR^\Omega$.  For a function $F\in\RR^\Omega$
and time $t\geq 0$ and state $S\in \Omega$, $(T(t)F)(S)$ is the
expected value of $F$ at time $t$, given that the initial distribution
of $\MM$ is concentrated at $S$ with probability one at time $0$.
In particular, $\varphi_{t} = T(t)\varphi_{0}$ for all $t\geq 0$, and
all initial distributions $\varphi_{0}$.
In the case of the SEP we are considering, the infinitesimal generator
$\L$ of the semigroup $T(t)$ is given by
$$
\L = \sum_{\{i,j\}\in E} \lambda_{ij} \left( \tau_{ij} - 1 \right).
$$
For each $\{i,j\}\in E$, this replaces each $S\in\Omega$
by $S\circ\tau_{ij}$ at the rate $\lambda_{ij}$.

In preparation for Section 7.3, it is useful to regard $\L$ as an element
of the real semigroup algebra $\Alg=\RR[\EE]$ of the semigroup
$\EE$ of all endofunctions $\ff:\Omega\goesto\Omega$ (with the
operation of functional composition).  The left action of $\EE$ on
$\Omega$ is extended to a left action of $\Alg$ on $\CC[\x]$ as usual:\
for $\ff\in\EE$ and $S\in\Omega$, $\ff(\x^S) = \x^{\ff(S)}$,
extended bilinearly to all of $\Alg$ and $\CC[\x]$.  A permutation
$\sigma\in\S(\Lambda)$ is identified with the endofunction $\ff_\sigma:S
\mapsto S\circ\sigma^{-1}$, so this action of $\Alg$ agrees with
the action of $\S(m)$ in Section 4.2.  A left action of $\Alg$ on $\RR^\Omega$
is defined by $Z(\ff(F))=\ff(Z(F))$ for all $\ff\in\EE$ and $F\in\RR^\Omega$,
and linear extension.  More explicitly, for $\ff\in\EE$, $F\in\RR^\Omega$,
and $S\in\Omega$,
$$
(\ff(F))(S) = F(\ff^{-1}(S)) =
\sum \{F(S'):\ S'\in\Omega\ \ \mathrm{and}\ \ \ff(S')=S\}.
$$

Consider an element of $\Alg$ of the form
$\L = \sum_{i=1}^N \lambda_i (\ff_i-1)$ with all $\lambda_i>0$.
Let $\lambda_i\leq L$ for all $i\in[N]$, and let $K=\sum_{i=1}^N \lambda_i$.
The power series
$$
\exp(t\L) = \e^{-Kt}\sum_{n=0}^{\infty}\frac{t^{n}}{n!}
\left[
\sum_{i=1}^N \lambda_i \ff_i
\right]^{n}
=\sum_{\ff\in\EE} P_{\ff}(t)\cdot\ff
$$
in $\Alg[[t]]$ is such that for each $\ff\in\EE$,
$P_{\ff}(t)\in\RR[[t]]$ is dominated coefficientwise by $\exp((LN-K)t)$.  Thus
$\exp(t\L)\in\Alg[[t]]$ converges for all $t\geq 0$.
The semigroup of transformations generated by $\L$ is $\exp(t\L)$.

To check claim (3) we will show that the semigroup $T(t)$ of the SEP
preserves stability for all $t\geq 0$:\ that is,
if $Z(\varphi_0)$ is stable then $Z(\varphi_t)=T(t)Z(\varphi_0)$
is stable for all $t\geq 0$.
This reduces to the case of a single pair $\{i,j\}\in E$, as follows.
If $\MM_{1}$ and $\MM_{2}$ are Markov chains
on the same finite state space, with semigroups $T_{1}(t)$ and $T_{2}(t)$
generated by $\L_{1}$ and $\L_{2}$, then the semigroup generated by
$\L_{1}+\L_{2}$ is
$$
T(t) = \lim_{n\goesto\infty} \left[ T_{1}(t/n) T_{2}(t/n) \right]^{n},
$$
by the Trotter product formula.  By Hurwitz's Theorem, It follows that
if $T_{i}(t)$ preserves stability for all $t\geq 0$ and $i\in\{1,2\}$,
then $T(t)$ preserves stability for all $t\geq 0$.  By repeated application
of this argument, in order to show that the SEP semigroup $T(t)=\exp(t\L)$
preserves stability for all $t\geq 0$ it is enough to show that
for each $\{i,j\}\in E$, $T_{ij}(t) = \exp(t\lambda_{ij}(\tau_{ij}-1))$
preserves stability for all $t\geq 0$.  Now, since $\tau_{ij}^{2}=1$,
$$
T_{ij}(t)
=
\left(\frac{1+\e^{-2\lambda_{ij}t}}{2}\right)+
\left(\frac{1-\e^{-2\lambda_{ij}t}}{2}\right)\cdot\tau_{ij}.
$$
By Lemma 4.3, this preserves stability for all $t\geq 0$.
This proves Theorem 7.1.
\end{proof}

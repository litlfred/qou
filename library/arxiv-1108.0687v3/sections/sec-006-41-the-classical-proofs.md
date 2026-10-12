---
doc_id: arxiv-1108.0687v3
doc_title: "Concentration of Lipschitz functionals of determinantal a nd other strong Rayleigh measures"
section_id: sec-006-41-the-classical-proofs
section_title: "The classical proofs"
section_number: 4.1
pages: 9-14
source_pdf: 1108.0687v3.pdf
source_sha256: 66ba88e13a429a0a
doc_brief: "Concentration of Lipschitz functionals of determinantal a nd other strong Rayleigh measures — Let {X1,...,X n} be a collection of binary valued random variables and let f : {0, 1}n → R be a Lipschitz"
text_source: latex
latex_prose_ratio: 0.957
latex_coverage_ratio: 0.993
---
To prove bounds such as [\[eq:chernoff\]](#eq:chernoff){reference-type="eqref" reference="eq:chernoff"}, one obtains an upper bound for ${\mathbb E}e^{\lambda S_n}$, and then applies Markov's inequality, choosing $\lambda$ optimally. Underlying the bounds on ${\mathbb E}e^{\lambda S_n}$ are corresponding bounds for compensated increments. Let $\Delta$ denote a variable with mean zero. Three classical exponential bounds are as follows.

$$\begin{aligned}
|\Delta| \leq 1 & \Rightarrow &
   {\mathbb E}e^{\lambda \Delta} \leq e^{\lambda^2 / 2}
   \label{eq:delta 1} \\[1ex]
\Delta \in [r,s] & \Rightarrow &
   {\mathbb E}e^{\lambda \Delta} \leq e^{\lambda^2 (s-r)^2 / 8}
   \label{eq:delta 2} \\[1ex]
\Delta \in [r,s] & \Rightarrow &
{\mathbb E}e^{\lambda \Delta}
   \leq \exp \left [ (e^\lambda - 1 - \lambda) \; |rs| \right ] \, ,
   \label{eq:delta 3}
\end{aligned}$$ when $|r-s| \leq 1$. These are used together with the following two special cases of Markov's inequality. $$\begin{aligned}
{\mathbb E}e^{\lambda X} \leq e^{c \lambda^2 / 2} & \Longrightarrow
   & {\mathbb P}(X \geq a) \leq e^{-a^2 / (2c)}
   \label{eq:AH 2} \\[1ex]
{\mathbb E}e^{\lambda X} \leq e^{b \, (e^\lambda - \lambda - 1)}
   & \Longrightarrow &
   {\mathbb P}(X > a) \leq e^a \left ( \frac{b}{a+b} \right )^{a+b}
   \leq \exp \left [ - \frac{a^2}{2 (a+b)} \right ]
   \label{eq:pois2}
\end{aligned}$$

These inequalities have appeared many times in the literature. Inequalities [\[eq:delta 1\]](#eq:delta 1){reference-type="eqref" reference="eq:delta 1"} and [\[eq:AH 2\]](#eq:AH 2){reference-type="eqref" reference="eq:AH 2"} constitute the classical Azuma-Hoeffding inequality and imply $$\begin{aligned}
{\mathbb E}e^{\lambda (S_n - \mu_n)} & \leq & e^{\lambda^2 n / 2}
   \, ; \label{eq:AH 1} \\[1ex]
{\mathbb P}(S_n - \mu_n \geq a) & \leq & e^{-a^2 / (2n)} \, .  \label{eq:AH 3}
\end{aligned}$$ This is valid for any martingale with differences bounded by 1; an exposition can be found in [@alon-spencer Theorem 7.2.1].

The improvement to [\[eq:delta 2\]](#eq:delta 2){reference-type="eqref" reference="eq:delta 2"} is present already in [@hoeffding], though the exposition in [@mcdiarmid89] is clearer (see Lemma 5.8 therein). When the increments of $S_n - \mu_n$ are compensated Bernoullis, one may take $b-a = 1$ rather than 2, resulting in an improvement by a factor of 4 in the exponent, $$\label{eq:quadratic}
{\mathbb E}e^{\lambda (S_n - \mu_n)} \leq e^{\lambda^2 n / 8} \, .$$ which together with [\[eq:AH 2\]](#eq:AH 2){reference-type="eqref" reference="eq:AH 2"} yields [\[eq:chernoff\]](#eq:chernoff){reference-type="eqref" reference="eq:chernoff"}.

Finally, [\[eq:delta 3\]](#eq:delta 3){reference-type="eqref" reference="eq:delta 3"} and induction yield $$\label{eq:exp pois}
{\mathbb E}e^{\lambda (S_n - \mu_n)} \leq e^{(e^\lambda - \lambda - 1) \, V_n}
   \leq e^{(e^\lambda - \lambda - 1) \, \mu_n}$$ where $V_n := \sum_{k=1}^n p_k (1 - p_k)$ is the variance of $S_n$; together with [\[eq:pois2\]](#eq:pois2){reference-type="eqref" reference="eq:pois2"} this implies [\[eq:pois\]](#eq:pois){reference-type="eqref" reference="eq:pois"}; these results appear, for instance, in [@freedman75 (1.3)--(1.6)].

To prove the generalization to Lipschitz functions, let $$M_k := {\mathbb E}\left ( f(X_1 , \ldots , X_n) {\, | \, } X_1 , \ldots , X_k
   \right ) - {\mathbb E}f(X_1 , \ldots , X_n) \, .$$ It is immediate that $\{ M_k \}$ is a martingale and that conditional on $X_1 , \ldots , X_{k-1}$, the two possible values of $M_k$ differ by at most 1. Hence, conditional on $X_1 , \ldots , X_{k-1}$, the increment $\Delta_k := M_k - M_{k-1}$ is constrained to an interval of length at most 1. Applying [\[eq:delta 2\]](#eq:delta 2){reference-type="eqref" reference="eq:delta 2"} then yields [\[eq:gen 1\]](#eq:gen 1){reference-type="eqref" reference="eq:gen 1"}.

The extension of inequalities [\[eq:chernoff\]](#eq:chernoff){reference-type="eqref" reference="eq:chernoff"}--[\[eq:two-sided\]](#eq:two-sided){reference-type="eqref" reference="eq:two-sided"} to negatively cylinder dependent random variables is established by examining the power series for $e^{\lambda S_n}$. This may be expanded into positive sums of expectations of products of powers of the variables $\{ X_j : 1 \leq j \leq n \}$. Negative cylinder dependence implies that these are bounded from above by the corresponding products of expectations. Therefore, [\[eq:quadratic\]](#eq:quadratic){reference-type="eqref" reference="eq:quadratic"} and [\[eq:exp pois\]](#eq:exp pois){reference-type="eqref" reference="eq:exp pois"} hold when the assumption of independence is replaced by negative cylinder dependence, whence the probability inequalities [\[eq:chernoff\]](#eq:chernoff){reference-type="eqref" reference="eq:chernoff"} and [\[eq:pois\]](#eq:pois){reference-type="eqref" reference="eq:pois"} hold as well. This and more is shown in [@panconesi-srinivasan Theorem 3.4], specializing their more general negative cylinder property to $\lambda = 1$. We remark that only the first inequality [\[eq:cyl 1\]](#eq:cyl 1){reference-type="eqref" reference="eq:cyl 1"} in the definition of negative cylinder dependence is used to obtain bounds on ${\mathbb E}e^{\lambda S_n}$ for $\lambda > 0$, which suffices for the upper tail bounds. Lower tail bounds require these inequalities for $\lambda < 0$, for which the second inequality [\[eq:cyl 2\]](#eq:cyl 2){reference-type="eqref" reference="eq:cyl 2"} is required.

## Proof of Theorems  and 

Theorem [\[th:main\]](#th:main){reference-type="ref" reference="th:main"} is a special case of Theorem [\[th:cont homog\]](#th:cont homog){reference-type="ref" reference="th:cont homog"}. This is because any probability measure $\mu$ on ${\mathcal B}_n$ may be viewed as the law of a point process on the $n$ element set $[n]$, where the random counting measure ${\cal Z}(\omega)$ is defined by ${\cal Z}(\omega) (S) = \sum_{j \in S} \omega_j$. Informally, the points of the process are the coordinates of the ones in the sample $\omega$. With this interpretation, the SCP on ${\mathcal B}_n$ is inherited from the SCP for the point process ${\cal Z}$, whence Theorem [\[th:cont homog\]](#th:cont homog){reference-type="ref" reference="th:cont homog"} with $S = \mathbb{R}$ (or any other standard Borel space containing $[n]$) implies Theorem [\[th:main\]](#th:main){reference-type="ref" reference="th:main"}. It remains to prove Theorem [\[th:cont homog\]](#th:cont homog){reference-type="ref" reference="th:cont homog"}.

Let $(\Omega , {\mathcal F}, {\mathbb P})$ be a probability space on which is constructed the generalized sampling scheme described in Lemma [\[lem:k step\]](#lem:k step){reference-type="ref" reference="lem:k step"}. Let ${\mathcal F}_j := \sigma (X_1 , \ldots , X_j)$ and let $$\label{eq:mart}
M_j := {\mathbb E}(f {\, | \, } {\mathcal F}_j) - {\mathbb E}f \, .$$ denote the martingale of sequential revelation. Applying the method of bounded differences is now mostly a matter of bookkeeping. At a sample point where $X_i = x_i, 1 \leq i \leq k$, the quantity $M_j$ may be written as the integral of $f$ against the law of the point process $${\cal Z}_{x_1 , \ldots , x_j} + \sum_{i=1}^j \delta_{x_i} \, .$$ By the SCP, we have ${\cal Z}_{x_1 , \ldots , x_j} \triangleright
{\cal Z}_{x_1 , \ldots , x_{j+1}}$ whence $$d_\infty \left ( {\cal Z}_{x_1 , \ldots , x_j} + \sum_{i=1}^j \delta_{x_i}
   \;\; , \;\; {\cal Z}_{x_1 , \ldots , x_{j+1}} + \sum_{i=1}^{j+1} \delta_{x_i}
   \right ) \leq 2 \, .$$ By the Lipschitz assumption on $f$, it follows that $|M_{j+1} - M_j| \leq 2$. We now apply the basic Azuma-Hoeffding inequality [\[eq:AH 3\]](#eq:AH 3){reference-type="eqref" reference="eq:AH 3"} to $\{ M_j / 2 \}_{1 \leq j \leq k}$ yielding $${\mathbb P}(f - {\mathbb E}f \geq a) = {\mathbb P}\left ( \frac{M_k}{2} > \frac{a}{2} \right )
   \leq \exp \left ( - \frac{a^2}{8 k} \right ) \, .$$ $\hfill \Box$

## Proof of Theorem 

In this section we assume ${\mathbb P}$ is the law of a strong Rayleigh measure on ${\mathcal B}_n$ with finite mean ${\mathbb E}N = \mu$. We also let $f$ denote an arbitrary but fixed Lipschitz-1 function on configurations and define a function $\phi$ on $\mathbb{Z}^+$ by $$\phi (k) := {\mathbb E}(f {\, | \, } N = k) \, .$$

::: lem
[]{#lem:bernoulli label="lem:bernoulli"} The variable $N$ is distributed as the sum of independent Bernoullis.
:::

In the definition of the strong Rayleigh property, setting the variables $z_1 , \ldots , z_n$ equal produces a univariate polynomial with no roots in the upper half plane. As pointed out at the beginning of Section 3 of [@borcea-branden-liggett], such a polynomial with real coefficients must have all its roots real. Since the coefficients are nonnegative, this implies it is the generating function for a convolution of Bernoullis.

$\hfill \Box$

::: lem
[]{#lem:N concentration label="lem:N concentration"} The variable $N$ satisfies $${\mathbb E}e^{\lambda (N - \mu)} \leq \exp \left [ \mu(e^\lambda - 1 - \lambda)
   \right ]$$ and consequently for any $a > 0$, $${\mathbb P}\left ( N \geq \mu+ \frac{a}{2} \right ) \leq
   \exp \left ( - \frac{(a/2)^2}{2 (\mu+ a/2)} \right ) \, .$$
:::

By Lemma [\[lem:bernoulli\]](#lem:bernoulli){reference-type="ref" reference="lem:bernoulli"} $N$ is distributed as the sum of independent Bernoullis, which implies the first inequality; this implies the second inequality by [\[eq:pois2\]](#eq:pois2){reference-type="eqref" reference="eq:pois2"}. $\hfill \Box$

::: lem
[]{#lem:phi lipschitz label="lem:phi lipschitz"} The function $\phi$ is Lipschitz-1.
:::

By Proposition [\[pr:k cover\]](#pr:k cover){reference-type="ref" reference="pr:k cover"} in the case of strong Rayleigh measures on ${\mathcal B}_n$

we know that ${\mathbb P}_{k+1} \triangleright{\mathbb P}_k$. By definition of the stochastic covering relation, $(\phi (k+1) , \phi (k))$ may be written as ${\mathbb E}(f(\eta) , f(\xi))$ where $d(\eta , \xi) = 1$ almost surely. The conclusion then follows from the fact that $f$ is Lipschitz-1. $\hfill \Box$

::: lem
[]{#lem:phi concentration label="lem:phi concentration"} The random variable $\phi (N)$ satisfies the concentration inequality $${\mathbb E}e^{\lambda (\phi (N) - {\mathbb E}\phi (N))} \leq
   e^{\mu(e^\lambda - 1 - \lambda)} \, .$$ Consequently, the upper tails of $\phi (N)$ obey the bound $${\mathbb P}(\phi (N) - {\mathbb E}\phi (N) > t) \leq
   e^{-\frac{t^2}{2 (t + \mu)}} \, .$$
:::

Pursuant to Lemma [\[lem:bernoulli\]](#lem:bernoulli){reference-type="ref" reference="lem:bernoulli"}, let $\{ Y_j \}$ be a finite or countably infinite collection of independent Bernoulli variables whose sum has the same law as $N$; we may therefore prove the statements with $N$ replaced by $\sum_j Y_j$. Write $\phi (\sum_j Y_j) - {\mathbb E}\phi (\sum_j Y_j)$ as the final term of a martingale $\{ M_\ell \}$ where $M_\ell := {\mathbb E}( \phi (\sum_j Y_j) {\, | \, } {\mathcal F}_\ell) - {\mathbb E}\phi$ and ${\mathcal F}_\ell := \sigma (Y_1 , \ldots , Y_\ell)$. If the number of Bernoullis is infinite, the final term is a limit almost surely and in $L^2$. The martingale $\{ M_\ell \}$ is a binary martingale, meaning that conditional on ${\mathcal F}_\ell$, the distribution of $M_{\ell+1}$ is concentrated on two values. In other words, $$(M_{\ell+1} {\, | \, } {\mathcal F}_\ell) = p \delta_r + (1-p) \delta_s$$ where $p$ is the mean of the Bernoulli variable $Y_{\ell+1}$. More importantly, $r = \int f \, d\mu$ and $s = \int f \, d\nu$ where $\mu$ is the conditional law of $\sum_j Y_j$ given the values of $Y_1 , \ldots , Y_\ell$ (which are measurable with respect to ${\mathcal F}_\ell$) and given $Y_{\ell + 1} = 1$, and $\nu$ is the conditional law of $\sum_j Y_j$ given the values of $Y_1 , \ldots , Y_\ell$ and given $Y_{\ell + 1} = 0$. Clearly $\mu$ and $\nu$ are probability measures on $\mathbb{Z}^+$ satisfying $d_\infty (\mu , \nu) \leq 1$, whence because $\phi$ is Lipschitz-1, we see that $|r-s| \leq 1$. From [\[eq:delta 3\]](#eq:delta 3){reference-type="eqref" reference="eq:delta 3"} we then obtain $${\mathbb E}\left ( e^{\lambda (M_{\ell+1} - M_\ell)} {\, | \, } {\mathcal F}_\ell \right )
   \leq \exp \left ( p (1-p) (e^\lambda - 1 - \lambda) \right ) \, .$$ The lemma follows by induction. $\hfill \Box$

The event $\{ f - {\mathbb E}f > a \}$ is contained in the union of three events: $$\left \{ N > \mu+ \frac{a}{2} \right \} \cup
   \left \{ \phi (N) - {\mathbb E}f > \frac{a}{2} \right \} \cup
   \left \{ f - \phi (N) > \frac{a}{2} \, , \, N \leq \mu+
      \frac{a}{2} \right \}  \, .$$ Thus ${\mathbb P}(f - {\mathbb E}f > a)$ is bounded above by the sum of the corresponding probabilities. Each of the first two pieces is bounded above by $\exp [- a^2 / (4(a + 2\mu))]$: the first follows from Lemma [\[lem:N concentration\]](#lem:N concentration){reference-type="ref" reference="lem:N concentration"} and the second uses Lemma [\[lem:phi concentration\]](#lem:phi concentration){reference-type="ref" reference="lem:phi concentration"}, noting that ${\mathbb E}\phi
= {\mathbb E}\; {\mathbb E}(f {\, | \, } N) = {\mathbb E}f$. The last piece is bounded above by $\exp [- a^2 / (16 (a + 2\mu))]$. To see this, observe that the measures ${\mathbb P}_k$ are all strong Rayleigh (this is [@borcea-branden-liggett Corollary 4.18]). For any $k \leq \mu+ a/2$, we can apply Theorem [\[th:main\]](#th:main){reference-type="ref" reference="th:main"} to the homogeneous measure ${\mathbb P}_k$, obtaining $${\mathbb P}\left ( f - \phi (N) > \frac{a}{2} {\, | \, } N = k \right )
   \leq \exp \left ( - \frac{(a/2)^2}{8 k} \right )
   \leq \exp \left ( - \frac{a^2}{16 (a + 2 \mu)} \right ) \, .$$ Reassembling these gives the upper bound $${\mathbb P}\left ( f - \phi (N) > \frac{a}{2} \, , \, N \leq \mu+
   \frac{a}{2} \right )
   \leq \exp \left ( -\frac{a^2}{16 (a + 2 \mu)} \right ) \, .$$ This last piece has the worst bound; using it for all three pieces gives the first inequality of the theorem; we remark that the better upper bound of $2 \exp [- a^2 / (4(a + 2\mu))] +
\exp [- a^2 / (16 (a + 2\mu))]$ is in fact valid.

For the two-sided bound, we need to consider two more events in addition to the three already considered, namely the events $\{ \phi (N) - {\mathbb E}\phi (N) < -a/2 \}$ and $\{ f - \phi (N) < -a/2, N \leq
\mu+ a/2 \}$. The arguments for these two extra events are exactly analogous to two of the three arguments we have already seen, leading to a bound of $\exp [ - a^2 / (16 (a + 2 \mu)) ]$ for each of the two new summands and establishing the two-sided bounds. $\hfill \Box$

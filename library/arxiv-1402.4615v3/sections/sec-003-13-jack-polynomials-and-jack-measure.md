---
doc_id: arxiv-1402.4615v3
doc_title: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS"
section_id: sec-003-13-jack-polynomials-and-jack-measure
section_title: "Jack polynomials and Jack measure"
section_number: 1.3
pages: 5-7
source_pdf: 1402.4615v3.pdf
source_sha256: b6e7c795cd1a7cd2
toc_source: outline
text_source: latex
latex_prose_ratio: 0.961
latex_coverage_ratio: 0.987
doc_brief: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS — In this paper, we consider a deformation of Plancherel measure linked to Jack polynomials."
---
To explain our intermediate results and the main steps of the proof, we first need to review the connection between Jack measure and Jack polynomials.

### Jack polynomials

In a seminal paper [@Jack1970/1971], Jack introduced a family of symmetric functions $J^{(\alpha)}_\lambda$ depending on an additional parameter $\alpha$. These functions are now called *Jack polynomials*. For some special values of $\alpha$, they coincide with some established families of symmetric functions. Namely, up to multiplicative constants, for $\alpha=1$, Jack polynomials coincide with Schur polynomials, for $\alpha=2$, they coincide with zonal polynomials, for $\alpha=1/2$, they coincide with symplectic zonal polynomials, for $\alpha = 0$, we recover the elementary symmetric functions and finally their highest degree component in $\alpha$ are the monomial symmetric functions. Moreover, Jack polynomials for $\alpha=-(k+ 1)/(r+ 1)$ verify some interesting annihilation conditions [@Feigin2002] and the general $\alpha$ case (with some additional, technical assumptions) is relevant in Kadell's work in relation with generalizations of Selberg's integral [@Kadell1997].

Over the time it has been shown that several results concerning Schur and zonal polynomials can be generalized in a rather natural way to Jack polynomials (Section (VI.10) of Macdonald's book [@Macdonald1995] gives a few results of this kind), therefore Jack polynomials can be viewed as a natural interpolation between several interesting families of symmetric functions.

### A characterization of Jack measure

Expanding Jack polynomials $J_\lambda^{(\alpha)}$ in power-sum symmetric function basis, we define the coefficients $\theta_{\rho}^{(\alpha)}(\lambda)$ by: $$\label{eq:jack-characters}
J_\lambda^{(\alpha)}=\sum_{\substack{\rho: \\
|\rho|=|\lambda|}} 
\theta_{\rho}^{(\alpha)}(\lambda)\ p_{\rho}.$$ In the case $\alpha=1$, Jack polynomials specialize to $$J_\lambda^{(1)} = \frac{n!}{\dim(\lambda)} s_\lambda,$$ where $s_\lambda$ is the Schur function and $\dim(\lambda)$ is the dimension of the symmetric group representation associated to $\lambda$. Hence, using Frobenius formula [@Macdonald1995 page 114], we can express $\theta_{\rho}^{(1)}(\lambda)$ in terms of irreducible character values of the symmetric group. Namely $$\theta_\rho^{(1)}(\lambda)=\frac{n!}{z_\rho} \, \frac{\chi^{\lambda}_\rho}{\dim(\lambda)},$$ where $\chi^{\lambda}_\rho$ is the character of the irreducible representation indexed by $\lambda$ evaluated on a permutation of cycle-type $\rho$ and $z_\rho$ is the standard numerical factor $\prod_i i^{m_i(\rho)} m_i(\rho)!$, where $m_i(\rho)$ is the number of parts of $\rho$ equal to $i$. By analogy to this, we use in the general case the terminology *Jack characters* for $\theta_{\rho}^{(\alpha)}(\lambda)$ (while they do not have any representation theoretical interpretation, they share a lot of property with characters of the symmetric groups).

The following property, which corresponds to the case $\pi=(1^n)$ of [@MatsumotoOddJM Equation (8.4)], characterizes Jack measure: $$\mathbb{E}_{\mathbb{P}_n^{(\alpha)}}( \theta^{(\alpha)}_\rho(\lambda) ) =
\delta_{\rho,(1^n)},
\label{eq:expect_Jack_character}$$ where $\lambda$ is a random Young diagram with $n$ boxes distributed according to $\mathbb{P}_n^{(\alpha)}$.

### A central limit theorem for Jack characters

As in the case $\alpha=1$, an important intermediate result, which may be of independent interest, is an *algebraic* central limit theorem. Namely we prove that Jack characters for hooks (*i.e.* $\rho$ is a hook) have joint Gaussian fluctuations.

::: theorem
[]{#theo:FluctuationsJackCharacters label="theo:FluctuationsJackCharacters"} Choose a sequence $\left(\Xi_k \right)_{k=2,3,\dots}$ of independent standard Gaussian random variables. Let $(\lambda_{(n)})_{n \ge 1}$ be a sequence of random Young diagrams of size $n$ distributed according to Jack measure. Define the random variable $$W_k(\lambda_{(n)}) = \frac{\sqrt{k} \, \theta^{(\alpha)}_{(k,1^{n-k})}(\lambda_{(n)})}{ n^{k/2}}.$$ Then, as $n \to \infty$, we have: $$\left( W_k \right)_{k=2,3,\dots}
\xrightarrow{d} \left( \Xi_k \right)_{k=2,3,\dots},$$ where $\xrightarrow{d}$ means convergence in distribution of the finite-dimensional laws.
:::

In the case $\alpha=1$, this theorem was proved independently by Kerov [@Kerov1993gaussian; @IvanovOlshanski2002] and Hora [@HoraFluctuationsCharacters]. With the method developed here, one can even give an upper bound on the speed of convergence of the distribution function:

::: theorem
We use the same notation as in Theorem [\[theo:FluctuationsJackCharacters\]](#theo:FluctuationsJackCharacters){reference-type="ref" reference="theo:FluctuationsJackCharacters"}. Then, for any integer $d \ge2$ and real numbers $x_2,\cdots,x_d$, $$\big|\mathbb{P}( W_2 \le x_2, \cdots, W_d \le x_d) - \mathbb{P}(\Xi_2 \le x_2, \cdots, \Xi_d \le x_d) \big|
     = O(n^{-1/4}),$$ where the constant hidden in the Landau symbol $O$ is *uniform* on $x_2,\cdots,x_d$, but depends on $d$. []{#theo:SpeedConvergence label="theo:SpeedConvergence"}
:::

In the case $\alpha=1$ and $d=2$, the study of the speed of convergence of $W_2$ towards a Gaussian variable has been initiated by Fulman in [@FulmanFluctuationChA2], who proved a bound of order $n^{-1/4}$. This bound has then been improved to $n^{-1/2}$ in two different works [@SpeedCvCharacters1; @SpeedCvCharacters2]. Fulman then generalized the $n^{-1/4}$ bound to any $W_i$, in the cases $\alpha=1$ and $\alpha=2$, using the representation-theoretical backgrounds for these particular values of $\alpha$, see [@FulmanSpeedCvRepresentations]. Some ideas from these papers are fundamental here, as explained below.

The main novelty in Theorem [\[theo:SpeedConvergence\]](#theo:SpeedConvergence){reference-type="ref" reference="theo:SpeedConvergence"} is of course the fact that our result holds for any value of the parameter $\alpha$. But, even in the cases $\alpha=1$ and $\alpha=2$, a bound for the speed convergence of a vector of random variables and not only for real-valued random variables seems to be new.

::: remark
[]{#rem:Fluct_NonHook label="rem:Fluct_NonHook"} We are not able to describe the fluctuations of Jack character $\theta^{(\alpha)}_\rho$ when $\rho$ is not a hook. This is discussed in Subsection [\[subsect:Fluct_NonHook\]](#subsect:Fluct_NonHook){reference-type="ref" reference="subsect:Fluct_NonHook"}.
:::

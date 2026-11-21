---
doc_id: arxiv-2201.05665v1
doc_title: "HAROLD WIDOM’S WORK IN RANDOM MATRIX THEORY"
section_id: sec-006-5-the-asymmetric-simple-exclusion-process-harold
section_title: "The asymmetric simple exclusion process. Harold Widom's papers 133,134,135"
section_number: 5
pages: 10-14
source_pdf: 2201.05665v1.pdf
source_sha256: bad7bde03d199a73
toc_source: outline
text_source: latex
latex_prose_ratio: 0.959
latex_coverage_ratio: 0.976
doc_brief: "HAROLD WIDOM’S WORK IN RANDOM MATRIX THEORY — This is a survey of Harold Widom’s work in random matrices."
---
The asymmetric simple exclusion process (ASEP) was introduced (in the probability literature) in Spitzer's 1970 work [@Sp]. It is a continuous time Markov process of interacting particles on the integer lattice ${\Bbb Z}$. A particle at a location $x$ waits an exponential time with parameter one (independently of all other particles). When that time has elapsed, the particle flips a coin and with probability $p$ attempts to jump one position to the right, and with probability $q=1-p$ attempts to jump one position to the left. These jumps are achieved only if the destination site is unoccupied at that time. Due to the memoryless property of the exponential distribution, this defines a Markov process. See Figure [2](#fig:asep){reference-type="ref" reference="fig:asep"} for an illustration of ASEP. Since its appearance, the ASEP model has attracted immense attention in both the mathematical and physics communities, due to the fact that this is one of the simplest nontrivial processes modeling nonequilibrium phenomena.

<figure id="fig:asep">

<figcaption>In the ASEP, particles jump left and right according to exponential clocks with rates <span class="math inline"><em>q</em></span> and <span class="math inline"><em>p</em></span>. All jumps are independent, and those that would lead to collisions are excluded (the grey <span class="math inline">×</span>).</figcaption>
</figure>

When $p=0$, the model is known as TASEP, with the $T$ standing for "totally" since now particles only march to the left. In the paper [@Joh2], building on [@BDJ], an important relation of the particle probabilities of the totally asymmetric process (TASEP, $p=0$) to the distribution function of the largest eigenvalue in the Laguerre unitary random matrix ensemble was discovered. Relying on tools from random matrix theory (namely, orthogonal polynomials and Fredholm determinants) [@Joh2] shows that the limiting particle distribution in TASEP is given by the Tracy-Widom $\beta=2$ distribution (see also [@PS]). The decade after [@BDJ] saw incredible developments in the analysis of models like TASEP and the longest increasing subsequence whose analysis reduces to studying asymptotics of determinants (these models are called "determinantal", see [@BorodinDet]).

The extension of this result to ASEP when $q\neq p>0$ posed an enormous challenge since ASEP, as opposed to TASEP, is not determinantal and a direct relationship to random matrices is no longer available. The extraordinary series of papers [@133; @134; @135], nevertheless provides this extension by building on the relationship between ASEP and the Heisenberg XXZ spin chain and exploiting the ideas of the coordinate Bethe Ansatz[^1]. These works broke new ground as the first instance of a non-determinantal model for which the Tracy-Widom distributions was demonstrated.

The starting point for Tracy and Widom's work on ASEP is an exact formula for the transition probability of the $N$-particle ASEP. For $N\in {\Bbb N}$, consider a system of $N$ particles on ${\Bbb Z}$. For two vectors of ordered integers, $\vec{x} = \{x_1<\cdots< x_N\}$, and $\vec{y} = \{ y_1<\cdots< y_N\}$, let $P_{\vec{y}}(\vec{x};t)$ denote the probability that ASEP starts in state $\vec{y}$ at time zero, and is in state $\vec{x}$ at time $t$. This function solves the "Master equation" (or Kolmogorov forward equation). When $N=1$, this equation reads $$\frac{d}{dt}P_{y}(x;t) = \Delta_{p,q} P_{y}(x;t),\qquad P_{y}(x;0)=\mathbf{1}_{x=y}$$ where $\Delta_{p,q}$ acts in the $x$ variable as $\Delta_{p,q}f(x) = pf(x-1) + qf(x+1)-f(x)$. This equation can be solved explicitly using the Fourier transform, yielding $$P_{y}(x;t) = \frac{1}{2\pi i} \int \xi^{x-y-1} e^{\epsilon(\xi)t} d\xi,\qquad \epsilon(\xi) = p\xi^{-1} +q \xi -1$$ where $\xi$ is integrated along the complex unit circle centered at $0$.

When $N\geq 2$, the Master equation becomes more complicated. When the $x_i$ are well-spaced (at least distance two apart), the right-hand side becomes the sum of $N$ terms, each involving $\Delta_{p,q}$ acting on each of the $x_i$ variables. However, when the $x_i$ neighbor each other, certain terms need to be excluded (corresponding to the excluded jumps in ASEP). Thus, the system becomes non-constant coefficient and non-separable and so there is no a priori reason to expect such a simple contour integral formula as above.

There is hope, however. The generator of ASEP (the operator on the right-hand side of the Master equation) is related by a similarity transform to the Hamiltonian of the XXZ quantum spin chain, itself a special limit of the six-vertex model. These models have a long history in the realm of exactly solvable models in statistical mechanics, e.g. [@Baxter], and it was known since [@Lieb] that the coordinate Bethe ansatz can be used to diagonalize the six-vertex model transfer matrix. For the six-vertex model and XXZ spin chain, one has to assume boundary conditions (e.g. work on a torus). However, since the generator of ASEP is stochastic, one can work directly on the full space ${\Bbb Z}$. This actually leads to a significant simplification to the Bethe ansatz---there are no longer complicated Bethe equations! Instead, one has to develop an analog of the classical Plancherel theory, now for the Bethe ansatz eigenfunctions. This is essentially accomplished by [@133] as well as [@BCPS].

<figure id="fig:asep">

<figcaption>Harold Widom with his long-time collaborator, Craig Tracy at Oberwolfach in May 2009. Seen on the blackboard is calculations related to their work on ASEP. Photo courtesy of the Archives of the Mathematisches Forschungsinstitut Oberwolfach.</figcaption>
</figure>

The following formula was proved in [@133]. The $N=2$ case had previously appeared in work of Rákos and Schütz [@RakosSchutz]. Provided $p\neq 0$, $$\label{eq:tranprob}
P_{\vec{y}}(\vec{x};t) = \sum_{\sigma \in S_N} \frac{1}{(2\pi i)^N}\int\cdots \int A_{\sigma} \prod_{j=1}^{N} \xi_{\sigma(j)}^{x_j-y_{\sigma(j)}-1} e^{\epsilon(\xi_j)t} d\xi_j.$$ Here, the sum $\sigma\in S_N$ is taken over all permutations $\sigma$ on $N$ elements; the $\xi_j$ variables are complex and integrated over contours which are assumed to be circles around the origin with radii small enough so as not to contain any poles of the $A_\sigma$ term; this $A_{\sigma}$ term is given by the formula $$A_{\sigma} = \prod \left\{S_{\alpha\beta}:\{\alpha,\beta\}\textrm{ is an inversion of }\sigma\right\},\qquad S_{\alpha\beta} = - \frac{p+q \xi_{\alpha} \xi_{\beta} - \xi_{\alpha}}{p+q \xi_{\alpha} \xi_{\beta} - \xi_{\beta}}.$$ where the product is of terms $S_{\alpha\beta}$ over all pairs $1\leq \alpha<\beta\leq N$ such that $\sigma(\alpha)>\sigma(\beta)$.

This sum over the symmetric group may seem reminiscent of the expansion formula for determinants. In the special case when $p=1$ (which is the same at taking $p=0$, up to some symmetry), there is factorization and $A_\sigma = (-1)^{\sigma} \prod_{j=1}^{N} (1-\xi_{\sigma(j)})^{\sigma(j)-j}$. This implies that for $p=1$, $$P_{\vec{y}}(\vec{x};t)=\det\left(\frac{1}{2\pi i} \int (1-\xi)^{j-i} \xi^{x_i-y_j-1}e^{\epsilon(\xi)t} d\xi\right)_{i,j=1}^{N}$$ which recovers one aspect of the determinantal structure for TASEP, see [@Schutz].

Returning to ([\[eq:tranprob\]](#eq:tranprob){reference-type="ref" reference="eq:tranprob"}), just like in random matrix eigenvalue measures, the challenge now becomes how to extract large $N$ asymptotics for marginals of this measure on point configurations. Random matrix methods, though informative to this aim, were not directly applicable. The paper [@133] extracted summation formulas for the marginal distribution of $x_m$ for general $N$ and initial data $\vec{y}$. Taking $y_i=i$ and then taking $N$ to infinity led Tracy and Widom to study "step" initial condition for ASEP in which initially every positive integer site is occupied. The paper [@133] closed with an infinite summation formula for the marginal distribution of the location of the $m^{th}$ left-most particle at time $t$, for any $m$. This formula was further manipulated in [@134] into an integral transform of a Fredholm determinant. They had discovered a hidden determinantal structure in this model---one which would then allow them to extract asymptotics in [@135]. It should be remarked that the analysis of the Fredholm determinant in [@135] was itself quite novel, requiring a number of ingenious operator manipulations.

Let us now record the main result of the asymptotics performed in [@135]. In fact, in [@139], a more general class of initial data was considered in which sites in ${\Bbb N}$ are inititally occupied according to independent Bernoulli coin flips with probability $\rho\in (0,1]$ of having a particle. The case $\rho=1$ recovers the step initial data.

Assume that $0\leq p < q$ and put $\gamma := q-p$. Denote also $\sigma =  m/t \leq 1$ and define the constants, $$c_1 := -1 + 2\sqrt{\sigma}, \quad c_2 := \sigma^{-1/6}\Bigl(1 - \sqrt{\sigma}\Bigr)^{2/3}.$$ Then [@135; @139] shows that (cf. ([\[betaedge\]](#betaedge){reference-type="ref" reference="betaedge"}) and ([\[bdj\]](#bdj){reference-type="ref" reference="bdj"})), $$\label{asep1}
\lim_{t \to \infty}\textrm{Prob}\left(\frac{x_m\Bigl(t/\gamma\Bigr) - c_1t}{c_2t^{1/3}} \leq s\right)
= F_2(s), \quad \textrm{when}\quad 0 < \sigma < \rho^2,$$ and $$\label{asep2}
\lim_{t \to \infty}\textrm{Prob}\left(\frac{x_m\Bigl(t/\gamma\Bigr) - c_1t}{c_2t^{1/3}} \leq s\right)
= F_1(s)^2, \quad \textrm{when}\quad \sigma = \rho^2, \quad \rho < 1.$$

We emphasize again that ASEP is not a determinantal process and hence none of the usual "integrable techniques", such as the orthogonal polynomial approach, the Riemann-Hilbert method, the Borodin-Okounkov formula, or the theory of integrable Fredholm operators are readily applicable. In spite of the absence of such tools, the Tracy-Widom distributions still arise!

Besides demonstrating that the Tracy-Widom distribution is universal for ASEP regardless of the choice of parameters (provided $p\neq q$), the work in [@133; @134; @135] demonstrated that non-determinantal models could still be solved, albeit with different techniques.

Over the decade or so since Tracy and Widom's initial work on ASEP, there have been a number of developments in the field of integrable probability in this direction. This is too vast a subject to try to survey here, so we simply refer to a few existing surveys [@BorodinWheelerAggarwal; @BorodinICM; @BorodinGorin; @BorodinPetrov1; @BorodinPetrov2; @BorodinWheeler; @CorwinKPZ; @CorwinTwoASEP; @CorwinICM; @CorwinBAMS; @OConnell; @QuastelSpohn; @Zygouras1812.07204] and mention some general topics: Kardar-Parisi-Zhang universality class, replica method, Markov duality, quantum Toda Hamiltonian, Macdonald processes (and limits to Whittaker, Jack, Hall-Littlewood or Schur processes), stochastic vertex models, spin $q$-Whittaker and Hall-Littlewood functions. The list goes on, as does the influence of Tracy and Widom's work on ASEP and random matrices.

[^1]: This method dates back to 1931 work of Hans Bethe [@Bethe] in studying the Heisenberg XXX spin chain [@Heis].

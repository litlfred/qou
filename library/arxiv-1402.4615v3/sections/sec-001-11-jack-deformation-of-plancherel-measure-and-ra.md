---
doc_id: arxiv-1402.4615v3
doc_title: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS"
section_id: sec-001-11-jack-deformation-of-plancherel-measure-and-ra
section_title: "Jack deformation of Plancherel measure and random matrices"
section_number: 1.1
pages: 1-5
source_pdf: 1402.4615v3.pdf
source_sha256: b6e7c795cd1a7cd2
toc_source: outline
text_source: latex
latex_prose_ratio: 0.879
latex_coverage_ratio: 0.945
doc_brief: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS — In this paper, we consider a deformation of Plancherel measure linked to Jack polynomials."
---
[]{#subsect:JackPlancherel label="subsect:JackPlancherel"}

Random partitions occur in mathematics and physics in a wide variety of contexts, in particular in the Gromov-Witten and Seiberg-Witten theories, see [@OkounkovRandomPartitions] for an introduction to the subject. Another aspect which makes them attractive is the link with random matrices. Namely, some classical models of random matrices have random partition counterparts, which display the same kind of asymptotic behaviour.

In this paper, we consider the following probability measure on the set of partitions (or equivalently, Young diagrams) of size $n$: $$\label{eq:JackMeasure}
\mathbb{P}_n^{(\alpha)} ( \lambda ) = \frac{\alpha^n n!}{j_\lambda^{(\alpha)}},$$ where $j_\lambda^{(\alpha)}$ is a deformation of the square of the hook products: $$j_\lambda^{(\alpha)} = \prod_{\Box \in \lambda} \bigg(\alpha a(\Box) + \ell(\Box)
+1\bigg)
\bigg(\alpha a(\Box) + \ell(\Box)+\alpha\bigg).$$ Here, $a(\Box) := \lambda_j - i$ and $\ell(\Box) := \lambda_i' - j$ are respectively the arm and leg length of the box $\Box = (i,j)$ (the same definitions as in [@Macdonald1995 Chapter I]).

When $\alpha=1$, the measure $\mathbb{P}_n^{(\alpha)}$ specializes to the well-known *Plancherel measure* for the symmetric groups. In general, it is called *Jack deformation of Plancherel measure* (or Jack measure for short), because of its connection with the celebrated Jack polynomials that we shall explain later. It has appeared recently in several research papers [@BorodinOlshanskiJackZMeasure; @FulmanFluctuationChA2; @MatsumotoJackPlancherelFewRows; @OlshanskiJackPlancherel; @MatsumotoOddJM] and it is presented as an important area of research in Okounkov's survey on random partitions [@OkounkovRandomPartitions Section 3.3].

Recall that Plancherel measure has a combinatorial interpretation: it is the push-forward of the uniform measure on permutations by Robinson-Schensted algorithm (we keep only the common shape of the tableaux in the output of RS algorithm). A similar description holds for Jack measure for $\alpha=2$ (and $\alpha=1/2$ by symmetry): it is the push-forward of the uniform measure on fixed point free involutions by RS algorithm (in this case, the resulting diagram has always even parts and we divide each part by 2) -- see [@MatsumotoJackPlancherelFewRows Section 3].

Thus Jack measure can be considered as an interpolation between these two combinatorially relevant models of random partitions.

### $\alpha = 1$ case: Plancherel measure and GUE ensemble

There is a strong connection between Plancherel measure and the *Gaussian unitary ensemble* (called *GUE*) in random matrix theory. The Gaussian unitary ensemble is a random Hermitian matrix with independent normal entries. The probability density function for the eigenvalues of that matrix (of the size $d \times d$) is proportional to the weight $$\label{eq:BetaDensity}
e^{-\beta/2 \sum x_i^2} \prod_{i < j \leq d}(x_i-x_j)^\beta$$ with $\beta = 2$ (see [@AndersonGuionnetZeitouni2010]). Consider the scaled spectral measure of the GUE ensemble $$\mu^{(2)}_d := \frac{1}{d}\left(\delta_{x_1} + \cdots + \delta_{x_d}\right),$$ where $x_1 \geq \dots \geq x_d$ are eigenvalues of our random matrix and $\delta$ is the notation for Dirac operator. Then the famous *Wigner law* states that, as $d \to \infty$, the spectral measure tends almost surely to a *semicircular law*, i.e. to a probability measure $\mu_{S-C} := \frac{\sqrt{4-x^2}}{2\pi}1_{[-2,2]}(x)dx$ supported on the interval $[-2,2]$ (see [@AndersonGuionnetZeitouni2010]). The second order asymptotics is also known and one can observe Gaussian fluctuations around the limiting distribution (see [@Johansson1998]). Informally speaking, looking at the scaled spectral measure of GUE as a generalized function $$\mu^{(2)}_d(x) = \frac{1}{d}\left(\delta_{x-x_1} + \cdots + \delta_{x-x_d}\right),$$ we have that $$\mu^{(2)}_d(x) \sim \mu_{S-C}(x) + \frac{1}{d}\widetilde{\Delta}^{(2)}(x),$$ as $d \to \infty$, where $\tilde{\Delta^{(2)}}(x)$ is an explicit Gaussian process on the interval $[-2,2]$ with values in the space of generalized functions $(\mathbb{C}^\infty(\mathbb{R}))'$.

<figure id="FigOmega">

<figcaption>Young diagram <span class="math inline"><em>λ</em> = (4,3,1)</span> and the graph of the associated function <span class="math inline"><em>ω</em>(<em>λ</em>)</span>.</figcaption>
</figure>

It was also discovered that a similar phenomenon holds for the Plancherel measure. The first order asymptotics for the Plancherel measure was found by Vershik and Kerov [@KerovVershikLimitYD] and, independently, by Logan and Shepp [@LoganShepp1977]. They noticed that a Young diagram $\lambda$ can be encoded by a continuous piecewise-affine function $\omega(\lambda)$ from $\mathbb{R}$ to $\mathbb{R}$: this encoding is represented in Figure [1](#FigOmega){reference-type="ref" reference="FigOmega"} and formally defined in Section [\[SubsectContinuousYD\]](#SubsectContinuousYD){reference-type="ref" reference="SubsectContinuousYD"}. Then they proved that for appropriately scaled Young diagrams $\overline{\lambda_{(n)}}$ of size $n$ distributed according to the Plancherel measure (the bar encodes the scaling), one has the convergence in probability $$\sup\limits_{x \in \mathbb{R}} \left|\omega({\overline{\lambda_{(n)}}})(x) - \Omega(x) \right| \stackrel{(P)}{\longrightarrow} 0$$ where the limit shape $\Omega$ is given by $$\label{eq:DefOmega}
    \Omega(x) = \begin{cases}
    |x| & \text{if }|x| \geq 2;\\
    \frac{2}{\pi} \left( x \cdot \arcsin \frac{x}{2} + \sqrt{4-x^2} \right) 
    & \text{otherwise.}
\end{cases}$$ There is a strong connection between this limit shape and the semicircular law $\mu_{S-C}$, namely the so-called *transition measure* of $\Omega$, seen as a *continuous Young diagram*, is the semicircular law $\mu_{S-C}$ -- see [@Biane1998 Section 1.2].

The problem of the second order asymptotics was stated as an open question in late seventies and was solved by Kerov [@Kerov1993] who proved that, exactly as in the GUE case, the fluctuations around the limit shape are Gaussian. Informally Kerov's result can be presented as follows $$\omega\big({\overline{\lambda_{(n)}}}\big)(x) \sim \Omega(x) + \frac{2}{\sqrt{n}} \Delta^{(1)}_\infty(x)$$ where $\Delta^{(1)}_\infty$ is the Gaussian process on $[-2,2]$ with values in $(\mathcal{C}^\infty(\mathbb{R}))'$ defined by: $$\Delta^{(1)}_\infty(2\cos(\theta)) =\frac{1}{\pi} \sum_{k=2}^\infty \frac{\xi_k}{\sqrt{k}} \sin(k \theta).$$ The detailed proof of this remarkable theorem can be found in [@IvanovOlshanski2002]. Although they are not equal, the Gaussian processes $\Delta^{(1)}_\infty$ (which describe bulk fluctuations of Young diagram under Plancherel measure) and $\widetilde{\Delta}^{(2)}$ (which describe bulk fluctuations of the GUE) have quite similar definition.

Remarkably, the similarity between the Plancherel measure and the GUE ensemble does not only take place at the level of bulk fluctuations but also \"at the edge\". To be more precise, it was proved that the distribution of finitely many (properly scaled) first rows of random Young diagrams (with respect to the Plancherel measure) is the same as the distribution of the same number of (properly scaled) largest eigenvalues of the GUE ensemble, as $n \to \infty$ (see [@BaikDeiftJohansson1999; @Okounkov2000; @BorodinOkounkovOlshanski2000; @Johansson2001a; @Johansson2001; @BaikDeiftRains2001] for details).

### General $\alpha$-case and Gaussian $\beta$-ensembles

There are two famous analogues of the GUE ensembles in random matrix theory: *Gaussian orthogonal ensembles (GOE)* and *Gaussian symplectic ensembles (GSE)* (see [@Mehta2004]). The GOE ensemble (GSE ensemble, respectively) is a random real symmetric matrix (complex self-adjoint quaternion matrix, respectively) with independent normal entries (with mean $0$ and well-chosen variance). The density function for the distribution of eigenvalues of GOE (GSE, respectively) is, up to normalization, the function given by equation [\[eq:BetaDensity\]](#eq:BetaDensity){reference-type="eqref" reference="eq:BetaDensity"} with parameter $\beta = 1$ ($\beta = 4$, respectively). Therefore, it is tempting to introduce *Gaussian $\beta$-ensemble* (G$\beta$E, also called $\beta$-Hermite ensemble) that has a distribution density function proportional to [\[eq:BetaDensity\]](#eq:BetaDensity){reference-type="eqref" reference="eq:BetaDensity"} for any positive real value of $\beta$.

The G$\beta$E ensembles are well-studied objects. For the first order of asymptotic behaviour of the spectral measure $$\mu^{(\beta)}_d := \frac{1}{d}\left(\delta_{\frac{\beta}{2}x_1} + \cdots + \delta_{\frac{\beta}{2}x_d}\right),$$ where $x_1 \geq \cdots \geq x_d$ are eigenvalues of the G$\beta$E of size $d\times d$, Johansson [@Johansson1998] showed that the Wigner law holds, i.e., as $d\to \infty$, one has the almost-sure convergence $$\label{eq:first-order-GBE}
    \mu^{(\beta)}_d \to \mu_{S_C}.$$ A central limit theorem for the G$\beta$E was proved by Dumitriu and Edelman [@DumitriuEdelman2006]. Here, we can observe Gaussian fluctuations around the limit shape, similarly to the GUE case. Additionally, a surprising phenomenon takes place: the Gaussian process that describes the second order asymptotic is translated by a deterministic shift, which disappears for $\beta = 2$ (see [@DumitriuEdelman2006] for details).

A natural question is to find a discrete counterpart for G$\beta$E. Some results of Matsumoto [@MatsumotoJackPlancherelFewRows] suggest that a good candidate for such probability measure on the set of Young diagrams is *Jack measure* given by [\[eq:JackMeasure\]](#eq:JackMeasure){reference-type="eqref" reference="eq:JackMeasure"}, where the relation between parameters $\alpha$ and $\beta$ is $\beta = \frac{2}{\alpha}$. Matsumoto was studying a restriction of Jack measure to the set of Young diagrams of size $n$ with at most $d$ rows. His main result states that the joint distribution of that suitably normalized $d$ rows is the same as the joint distribution of the eigenvalues of $d$-dimensional traceless G$\beta$E with $\beta = \frac{2}{\alpha}$, as $d$ is fixed and $n \to \infty$.

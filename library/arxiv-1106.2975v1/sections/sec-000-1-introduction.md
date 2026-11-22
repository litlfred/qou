---
doc_id: arxiv-1106.2975v1
doc_title: "The Polyanalytic Ginibre Ensembles"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 2-8
source_pdf: 1106.2975v1.pdf
source_sha256: 7e966c7392b70ae0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.974
latex_coverage_ratio: 0.986
doc_brief: "The Polyanalytic Ginibre Ensembles — For integers n, q = 1, 2, 3, . . ., let Poln,q denote the C-linear space of polynomials in z and ¯z, of degree ≤n −1 in z and of degree ≤q −1 in ¯z."
---
We will write use standard notation, such as $\partial X$ and $\mathrm{int}(X)$ for the boundary and the interior of a subset $X$ of the complex plane ${\mathbb C}$. The complex conjugate of a complex number $z$ is usually written as $\bar z$. We write ${\mathbb R}$ for the real line, ${\mathbb D}:=\{z\in{\mathbb C}:|z|<1\}$ for the open unit disk, and ${\mathbb D}^e:=\{z\in{\mathbb C}:|z|>1\}$ for the open exterior (punctured) disk. The characteristic function of a set $E$ is written $1_E$. We write $${\mathrm d}A(z)=\pi^{-1}{\mathrm d}x {\mathrm d}y,\quad\text{where}\,\,\,
z=x+{\mathrm i}y\in{\mathbb C},$$ for the normalized area measure in ${\mathbb C}$, and use the standard Wirtinger derivatives $$\partial_z:=\tfrac12(\partial_x-{\mathrm i}\partial_y),\,\,\,
\bar\partial_z:=\tfrac12(\partial_x+{\mathrm i}\partial_y),
\quad\text{where}\,\,\, z=x+{\mathrm i}y.$$ We also write $\Delta$ for the (quarter) Laplacian $$\Delta_z:=\partial_z\bar\partial_z=\tfrac14(\partial_x^2+\partial_y^2).$$

Given a locally compact topological space $\mathrm{X}$ with a Radon measure $\mu$, a determinantal projection process (in the sequel just determinantal process) is a random configuration of $n$ points defined by the following probability measure on $\mathrm{X}^n$: $${\mathrm d}P(z_1,\ldots,z_n) = \frac{1}{n!} \det[K_n(z_i, z_j)]_{i,j=1}^n 
{\mathrm d}\mu(z_1)\cdots{\mathrm d}\mu(z_n). 
\label{eq-probdist}$$ Here, $K_n$ is the integral kernel of a projection operator to an $n$-dimensional subspace of $L^2(\mathrm{X},\mu)$. It is customary to identify all the permutations of the points and think the process as a random measure $\sum_{j=1}^n \delta_{z_j}$ on $\mathrm{X}$.

A general definition of a determinantal process was introduced by Macchi [@macchi], who wanted to model fermions in quantum mechanics. Indeed, for any determinantal process, the probability density vanishes whenever any two points in the $n$-tuple $(z_1,...,z_n)$ coincide (fermions are forbidden to be in the same state). We interpret this as saying that the points in the $n$-tuple repel each other. Point processes of this kind appear in several contexts, e.g., in random matrix theory and combinatorics (for general surveys, s [@hkpv], [@bor]; we should also mention the books [@mehta], [@deift], [@deiftgioev], [@AGZ]).

Our main motivating example comes from the theory of random normal matrices. This topic has in recent years been subject to rather active investigation by physicists as well as by mathematicians. For an introduction, see, e.g., [@zabro]. So, we shall use $\mathrm{X}=\mathbb{C}$ and ${\mathrm d}\mu(z)= \mathrm e^{-mQ(z)}{\mathrm d}A(z)$, for a positive weight function $Q$ satisfying some mild regularity and growth conditions; $m$ is a positive real parameter, and ${\mathrm d}A(z)=\pi^{-1}{\mathrm d}x {\mathrm d}y$ is the normalized area measure. Let us write $L^2(\mathbb{C}, \mathrm e^{-mQ}):=L^2(\mathrm{X},\mu)$ in this situation. The determinantal projection process is associated with an $n$-dimensional subspace of $L^2({\mathbb C}, \mathrm e^{-mQ})$, and we will use the space $\mathrm{Pol}_{n}$ of all polynomials in $z$ of degree $\le n-1$; we write $\mathrm{Pol}_{m,n}$ to indicate that we have supplied $\mathrm{Pol}_{n}$ with the Hilbert space structure of $L^2(\mathbb{C}, \mathrm e^{-mQ})$. The density of the process is then given by the reproducing kernel $K_{m,n}$ of the space $\mathrm{Pol}_{m,n}$. So, we are talking about the probability measure $${\mathrm d}P(z_1,\ldots,z_n) = \frac{1}{n!} \det[K_{m,n}(z_i, z_j)]_{i,j=1}^n 
\mathrm e^{-m\{Q(z_1)+\cdots+Q(z_n)\}}{\mathrm d}A(z_1)\cdots{\mathrm d}A(z_n). 
\label{eq-probdist2}$$ In terms of the *correlation kernel* $$\Zhe_{m,n}(z,w):=K_{m,n}(z,w)\mathrm e^{-\frac12m\{Q(z)+Q(w)\}}, 
\label{eq-kernel-zhe}$$ which is the an integral kernel of an orthogonal projection $L^2({\mathbb C})$, the expression [\[eq-probdist2\]](#eq-probdist2){reference-type="eqref" reference="eq-probdist2"} simplifies to $${\mathrm d}P(z_1,\ldots,z_n) = \frac{1}{n!} \det\big[\Zhe_{m,n}(z_i, z_j)
\big]_{i,j=1}^n {\mathrm d}A(z_1)\cdots{\mathrm d}A(z_n). 
\label{eq-probdist2.5}$$ The process described by [\[eq-probdist2\]](#eq-probdist2){reference-type="eqref" reference="eq-probdist2"} and [\[eq-probdist2.5\]](#eq-probdist2.5){reference-type="eqref" reference="eq-probdist2.5"} represents the eigenvalues of a random normal matrix picked from the distribution $$\frac{1}{Z_{m,n}}\,\mathrm e^{-m\,\mathrm{tr}[Q(M)]} 
{\mathrm d}\mathrm{vol}_{\mathrm{nm}(n)}(M),
\label{eq-ginQ}$$ where ${\mathrm d}\mathrm{vol}_{\mathrm{nm}(n)}(M)$ is the natural Riemannian volume form on the $n\times n$ normal matrices inherited from the metric of ${\mathbb C}^{n^2}$; $Z_{m,n}$ is the normalization constant needed to make the total mass equal to $1$. We are interested in the limiting behaviour of the process as $m,n\to+\infty$ while $n=m\tau+\mathrm{O}(1)$ for some positive real number $\tau$. Without loss of generality, we will consider only $\tau=1$.

Let $\mathcal{N}_+$ and $\mathcal{N}_{+,0}$ be the set of points defined by $$\mathcal{N}_+:=\big\{w\in{\mathbb C}:\,\Delta Q(w)>0\big\},\quad
\mathcal{N}_{+,0}:=\big\{w\in{\mathbb C}:\,\Delta Q(w)\ge0\big\}.$$ In the arXiv preprint [@HedMak1], which will appear later in the expanded form [@HedMak2], the function $\widehat{Q}$ was defined as a certain envelope of $Q$, namely the largest subharmonic function in ${\mathbb C}$ which is $\le Q$ everywhere and has the growth bound $$\widehat{Q}(z)=\log|z|^2+\mathrm{O}(1),\quad\text{as}\,\,\,|z|\to+\infty.$$ It is known that $\Delta \widehat{Q}=1_{\mathcal S}\Delta Q$ for some compact set $\mathcal S$ (see, e.g., [@HedMak2]). We assume that $\mathcal S$ is the minimal compact with this property, and call $\mathcal S$ a *spectral droplet*. We then have $\mathcal{S}\subset \mathcal{N}_{+,0}$. The point process [\[eq-probdist2\]](#eq-probdist2){reference-type="eqref" reference="eq-probdist2"} has the following property: as $m,n\to+\infty$ while $n=m+\mathrm{O}(1)$, the points will tend to accumulate on the set $\mathcal{S}$ with density $\Delta Q$ there. Moreover, the set $\mathcal{S}\cap\mathcal{N}_+$ is rather regular for real-analytic $Q$, as the Sakai theory applies (cf. [@HedShi]). Typically we then expect a real-analytic boundary, with the exception of cusps and contact (or kissing) points. Let us refer to the set $\mathrm{int}(\mathcal{S}\cap\mathcal{N}_{+})$ as *the bulk*. The results of [@ahm1], [@ahm2] show that for bulk points $z$, the local blow-up process at $z$, with coordinates $(\xi_1,\ldots\xi_n)$, $$\xi_j:=m^{1/2}[\Delta Q(z)]^{1/2}(z_j-z),$$ where $(z_1,\ldots,z_n)$ are from the process [\[eq-probdist2\]](#eq-probdist2){reference-type="eqref" reference="eq-probdist2"}, converges weakly to the translation invariant Ginibre$(\infty)$ process, as $m,n\to+\infty$ while $n=m+\mathrm{o}(1)$. The associated generating kernel is the reproducing kernel $(\xi,\eta)\mapsto\mathrm e^{\xi\bar\eta}$ of the Bargmann-Fock space. This has the flavor of a universality result. The corresponding statement in the Gaussian unitary ensemble (GUE) case is the universality of the sine kernel for bulk. We observe here that the sine kernel is the reproducing kernel for the Paley-Wiener space (a subspace of $L^2({\mathbb R})$ consisting of entire functions). As for the two boundary points in the GUE model, the Tracy-Widom distribution appears, which is generated by the Airy kernel. The Airy kernel is reproducing for another Hilbert space of entire functions. This suggests that for real-analytic $Q$ and $z\in\partial\mathcal{S}\cap
\mathcal{N}_+$, there should exist a local blow-up $$\xi_j:=m^\theta(z_j-z),$$ where $\theta=\theta(z)$ is a suitable positive real, such that as $m,n\to+\infty$ while $n=m+\mathrm{o}(1)$, the process $(\xi_1,\ldots,\xi_n)$ would converge to a determinantal process whose generating kernel is the reproducing kernel of a Hilbert space of entire functions. We verify this in the context of the Ginibre ensemble (i.e., with $Q(z)=|z|^2$), and identify the associated Hilbert space with a closed subspace of the Bargmann-Fock space characterized by slow growth in a half-plane. In that case, $\theta=\frac12$ as in the case of interior points.

In [@ahm1], [@ahm2], Ameur, Hedenmalm, and Makarov study the Berezin measure ${\mathrm d}B_{m,n}^{\langle z\rangle}$ and Berezin density $\berd_{m,n}^{\langle z\rangle}$: $${\mathrm d}B_{m,n}^{\langle z\rangle}(w):=\berd_{m,n}^{\langle z\rangle}(w)
{\mathrm d}A(w),\quad
 \berd_{m,n}^{\langle z\rangle}(w):= 
\frac{|K_{m,n}(z,w)|^2}{K_{m,n}(z,z)}\mathrm e^{-mQ(w)},$$ which arise in the study of the Berezin transform. The Berezin measure is a probability measure, which makes it more stable than the reproducing kernel $K_{m,n}$ of $\mathrm{Pol}_{m,n}$ itself as we let $m,n \to+\infty$. In terms of the point process [\[eq-probdist2\]](#eq-probdist2){reference-type="eqref" reference="eq-probdist2"}, $\berd_{m,n}^{\langle z\rangle}$ measures the amount of repulsion from $z$ caused by placing one of the points at $z$. For bulk points $z$, we have the convergence ${\mathrm d}B^{\langle z\rangle}_{m,n}\to{\mathrm d}\delta_z$ in the weak-star sense of measures, as $m,n\to+\infty$ while $n=m+\mathrm{o}(1)$. Here, ${\mathrm d}\delta_z$ is the Dirac point mass at $z$. In fact, there is a better result: the blow-up Berezin density $$\hat{\berd}_{m,n}^{\langle z\rangle}(\xi)=\frac{1}{m \Delta Q(z)}\,
\berd^{\langle z\rangle}_{m,n}\bigg(z+ \frac{\xi}{\sqrt{m \Delta Q(z)}}\bigg)$$ converges to the standard Gaussian $\mathrm e^{-|\xi|^2}$. This corresponds to the convergence of the local blow-up of the point process to the Ginibre$(\infty)$ process (cf. [@ahm1], [@ahm2]). On the other hand, for points $z$ outside the spectral droplet, i.e., for $z\in{\mathbb C}\setminus\mathcal{S}$, the Berezin measure ${\mathrm d}B^{\langle z\rangle}_{m,n}$ converges in the weak-star sense of measures to harmonic measure at $z$ with respect to the exterior domain ${\mathbb C}\setminus\mathcal{S}$ as $m,n\to+\infty$ while $n=m+\mathrm{o}(1)$ (see [@ahm1] for $Q=|z|^2$, and [@ahm2] for the general result).

It is convenient to think of the point process [\[eq-probdist2\]](#eq-probdist2){reference-type="eqref" reference="eq-probdist2"} in terms of the $k$-point intensities $$\det\big[\Zhe_{m,n}(z_i,z_j)\big]_{i,j=1}^{k}
=\det\big[K_{m,n}(z_i,z_j)
\mathrm e^{-\frac{1}{2}m[Q(z_i)+Q(z_j)]}\big]_{i,j=1}^{k}.$$ We notice quickly that the intensities are unchanged if the kernel changed to $$K^\chi_{m,n}(z,w):=\chi(z)\bar\chi(w)K_{m,n}(z,w),$$ provided that $\chi$ is measurable with $|\chi(z)|\equiv1$ (we can call this a "guage transformation"). This can help in the asymptotical analysis of local blow-ups. For $k=2$, we get the $2$-point intensity $$\begin{gathered}
\big\{K_{m,n}(z_1,z_1)K_{m,n}(z_2,z_2)-|K_{m,n}(z_1,z_2)|^2\big\}
\mathrm e^{-mQ(z_1)-mQ(z_2)}
\\
=K_{m,n}(z_1,z_1)\mathrm e^{-mQ(z_1)}\bigg\{K_{m,n}(z_2,z_2)\mathrm e^{-mQ(z_2)}
-\frac{|K_{m,n}(z_1,z_2)|^2}{K(z_1,z_1)}\mathrm e^{-mQ(z_2)}\bigg\},
\end{gathered}$$ where we recognize the Berezin density as a correction to the product of the two $1$-point densities, where the $1$-point intensity is $$K_{m,n}(z_1,z_1)\,\mathrm e^{-mQ(z_1)}.$$ So, as far as the $2$-point intensity goes, we just need the $1$-point intensity and the Berezin density. Since the $1$-point intensity is just the restriction to $z_1=z_2$ of the Berezin density, the Berezin density is all we need to describe the $2$-point intensity. We will be a little lazy and just work with the Berezin density in the context of local blow-ups, although the asymptotics of the $k$-point intensity would strictly speaking require a little more work. So, although we state our many of our assertions regarding local blow-ups in terms of the Berezin density, we maintain that they generalize to statements about the point processes (cf. [@ahm2]).

The case $Q(z)= |z|^2$ of [\[eq-ginQ\]](#eq-ginQ){reference-type="eqref" reference="eq-ginQ"} (or [\[eq-probdist2\]](#eq-probdist2){reference-type="eqref" reference="eq-probdist2"} is known as the *Ginibre ensemble*. The (probability generating or reproducing) kernel is now particularly simple: $$K_{m,n}(z,w)= m\sum_{j=0}^{n-1} \frac{(mz \bar{w})^j}{j!}.$$ Here, $\mathcal{S}=\bar{\mathbb D}$, the closed unit disk. We will consider a family of generalizations of the Ginibre ensemble, the *polyanalytic Ginibre ensembles*, which are defined by the reproducing kernels $K_{m,n,q}$ of the subspaces $$\mathrm{Pol}_{m,n,q} := \mathrm{span}\,
\big\{ z^j\overline{z}^k:\, 0\le j\le n-1,\,\,0\leq k \leq q-1\big\}$$ supplied with the Hilbert space structure of $L^2({\mathbb C},\mathrm e^{-m|z|^2})$. The parameter value $q=1$ corresponds to the standard Ginibre process. In general, we now project to the $nq$-dimensional subspace of the *polyanalytic polynomials*, where the degree in $\bar z$ is $\le q-1$, and the degree in $z$ is $\le n-1$. Note that the dimension of the subspace is now $nq$ and not $n$. We can think of the case $q>1$ as permitting more Landau levels than the lowest one (there are two similar models, see [@AIM], [@Mou], [@vas]; see also [@abreu]). We will keep the polyanalyticity degree $q$ fixed in the process, while we let both $m,n$ tend to infinity. We remark here that we have noticed that Tomoyuki Shirai is interested in a similar model [@tshi].

As for the point process, the points generally repel each other, but for $q>1$, they also tend to avoid certain geometric configurations, such as circles and lines. We have run a simulation in Figure [1](#fig-1){reference-type="ref" reference="fig-1"}.

![The polyanalytic Ginibre process with the kernel $K_{m,n,q}$ with $m=n=61$ and $q=3$. The simulation is based on the algorithm by Hough, Krishnapur, Peres, and Virág [@hkpv].](183points.jpg){#fig-1 width="100mm"}

Macroscopically, we find that the behavior of the polyanalytic Ginibre ensemble is similar to that of the Ginibre ensemble. If we measure this in terms of the Berezin measure, we have that as $m,n\to+\infty$ while $n=m+\mathrm{O}(1)$, $${\mathrm d}B_{m,n,q}^{\langle z\rangle}\to{\mathrm d}\delta_z\,\,\,\text{for}\,\,\,
z\in\bar{\mathbb D},\quad
{\mathrm d}B_{m,n,q}^{\langle z\rangle}\to{\mathrm d}\omega_z\,\,\,\text{for}\,\,\,
z\in{\mathbb D}^e,$$ where $\omega_z$ is the harmonic measure of $z$ with respect to the exterior disk ${\mathbb D}^e$. Here, $K_{m,n,q}$ is the reproducing kernel for $\mathrm{Pol}_{m,n,q}$, and we use the notation $${\mathrm d}B_{m,n,q}^{\langle z\rangle}(w):=
\berd_{m,nq}^{\langle z\rangle}(w){\mathrm d}A(w),\quad
 \berd_{m,n,q}^{\langle z\rangle}(w):= 
\frac{|K_{m,n,q}(z,w)|^2}{K_{m,n,q}(z,z)}\mathrm e^{-mQ(w)},$$ for the corresponding Berezin measure and Berezin density. Interestingly, the microscopic behavior of the Berezin measure ${\mathrm d}B^{\langle z\rangle}_{m,n,q}$ is quite different for $q>1$ compared with the Ginibre case $q=1$. In terms of the blow-up Berezin density ($\Delta Q(z)=\Delta|z|^2\equiv1$ here) $$\hat{\berd}_{m,n,q}^{\langle z\rangle}(\xi)=m^{-1}\,
\berd^{\langle z\rangle}_{m,n,q}(z+m^{-1/2}\xi),$$ we have the following asymptotics as $m,n\to+\infty$ while $n=m+\mathrm{O}(1)$: $$\hat{\berd}_{m,n,q}^{\langle z\rangle}(\xi)\longrightarrow q^{-1}
L^{1}_{q-1}(|\xi|^2)^2\mathrm e^{-|\xi|^2}\quad\text{for}\,\,\, z\in{\mathbb D},$$ where $L^{1}_{q-1}$ denotes the (generalized) Laguerre polynomial of degree $q-1$ with parameter $1$. It is well-known that the Laguerre polynomial $L^{1}_{q-1}$ has exactly $q-1$ strictly positive roots, which implies that the Berezin density will exhibit a typical *Fresnel-type ring pattern*. This resembles what happens in the one-dimensional GUE case, where the zero density points for the Berezin density come from the zeros of the sine kernel. Actually, the analogy is more than a superficial similarity. If we consider rather big values of $q$, and scale down to local distance $(mq)^{-1/2}$, with $$\tilde{\berd}_{m,n,q}^{\langle z\rangle}(\xi')=(mq)^{-1}\,
\berd^{\langle z\rangle}_{m,n,q}\big(z+(mq)^{-1/2}\xi'\big),$$ then by the above we have, for $z\in{\mathbb D}$, $$\hat{\berd}_{m,n,q}^{\langle z\rangle}(\xi)\longrightarrow q^{-2}
L^{1}_{q-1}(q^{-1}|\xi'|^2)^2\mathrm e^{-q^{-1}|\xi'|^2},$$ as $m,n\to+\infty$ with $n=m+\mathrm{O}(1)$. Next, if we let $q\to+\infty$, we get that $$q^{-2}
L^{1}_{q-1}(q^{-1}|\xi'|^2)^2\mathrm e^{-q^{-1}|\xi'|^2}\longrightarrow
\bigg\{\sum_{i=0}^{+\infty}\frac{(-1)^i|\xi'|^{2i}}{i!(i+1)!}\bigg\}^2
=\frac{J_1(2|\xi'|)^2}{|\xi'|^2},$$ where $J_1$ is the standard Bessel function. The identity $$\frac{J_1(2|\xi'|)}{|\xi'|}=\int_{\mathbb D}\mathrm e^{2{\mathrm i}\operatorname{Re}[\xi'\bar\zeta]}{\mathrm d}A(\zeta)$$ shows that we are dealing with a planar analogue of the sine kernel (the sine kernel is the Fourier transform of the characteristic function of the interval $[-1,1]$, the one-dimensional unit ball).

We also investigate the local behaviour of the Berezin transform when $|z|=1$, i.e., when $z$ is on the boundary of the bulk. Using the same blow-up scale as with an interior point, we show that the blow-up Berezin density $\hat{\berd}^{\langle z\rangle}_{m,n,q}(\xi)$ tends to a limit which can be expressed in terms of Hermite polynomials (see Theorem [\[thm-5.10\]](#thm-5.10){reference-type="ref" reference="thm-5.10"}). Here, too, there is a ring-like pattern in the interior direction, but it is not so pronounced as it is for interior points (the bulk). We express the $1$-point intensity near a boundary point in terms of a sum of squares of Hermite polynomials. The Wigner semi-circle law then gives the asymptotic behavior of the $1$-point function, which tells us the intensity of the process. We find that for big $q$, but much bigger $m,n$ with $m=n+\mathrm{O}(1)$, the $1$-point function is nontrivial in the annulus $$1-q^{1/2}m^{-1/2}\le|z|\le1+q^{1/2}m^{-1/2};$$ inside it is essentially constant, and outside it more or less vanishes. Near the outward boundary of the annulus at the scale $(mq)^{-1/2}$, we expect the statistics of the point process to be related with the well-known Airy process.

Analogous results to [@ahm1] are obtained on complex manifolds by Berman [@berman1]. We note that the polyanalytic Ginibre processes can also be viewed as processes in $\mathbb{C}^2$ with the rather singular weight $\mathrm e^{-|z_1|^2}\delta_0(z_1-\bar z_2)$, where $\delta_0$ is unit point mass at $0$. Berman considers reproducing kernels of polynomial subspaces as the total degree of the polynomials tends to infinity. In contrast, here we discuss the case where one variable has bounded degree and the degree of the other variable goes to infinity.

It is well known in the theory of random matrices that $$\frac{1}{n!} \det[K_{m,n,1}(z_i, z_j)]_{i,j=1}^n 
= \frac{1}{Z_{m,n,1}} |\Delta(z_1,...,z_n)|^2,$$ where $\Delta(z_1,...,z_n)= \Pi_{i,j:i<j} (z_j-z_i)$ is the van der Monde determinant. A point configuration in a compact set which maximizes the van der Monde determinant is known to be a good choice of nodes for Lagrange interpolation [@st]. Instead of considering points confined to a compact set, one can add a weight to prevent the points from going off to infinity. This leads to the same expression which arises in the context of random eigenvalues.

We turn to the polyanalytic case. One shows that $$\frac{1}{(nq)!} \det[K_{m,n,q}(z_i,z_j)]_{i,j=1}^{nq} 
= \frac{1}{Z_{m,n,q}}| \Delta_q(z_1,...,z_{nq})|^2,$$ where $Z_{m,n,q}$ is a normalization constant $$Z_{m,n,q}:=
\int_{{\mathbb C}^{nq}}|\Delta_q(z_1,...,z_{nq})|^2
\mathrm e^{-m \sum_{j=1}^{nq}Q(z_j)}
{\mathrm d}A(z_1) \dots {\mathrm d}A(z_{nq})$$ and $$\Delta_q(z_1,...,z_{nq}) = 
\mathrm{det} \left( 
\begin{array}{ccc}
1 & \dots  & 1 
\\
z_1 & \dots & z_{nq} 
\\
\vdots & \dots & \vdots 
\\
z_1^{n-1} & \dots & z_{nq}^{n-1} 
\\
\bar{z}_1&\dots &  \bar{z}_{nq}
\\
\bar{z}_1z_1&\dots &  \bar{z}_{nq}z_{nq}
\\ 
\vdots & \dots & \vdots 
\\
\bar{z}_1^{q-1}&\dots &  \bar{z}_{nq}^{q-1}
\\
\vdots & \dots & \vdots 
\\
\bar{z}_1^{q-1}z_1^{n-1}&\dots &  \bar{z}_{nq}^{q-1}
z_{nq}^{n-1}
\\ 
\end{array} 
\right).$$ So, $\Delta_q(z_1,...,z_{nq})$ is the polyanalytic analogue of the van der Monde determinant. As in the case $q=1$ (which gives the usual van der Monde determinant), the expression $|\Delta_q(z_1,...,z_{nq})|^2$ measures how good the configuration is for Lagrange interpolation by polyanalytic polynomials. So, the polyanalytic Ginibre ensemble is a way to produce random Lagrange interpolation sets, using the Gaussian weight for confinement.

In [@rv] and [@ahm2], the authors showed that the fluctuations of eigenvalues of random normal matrices tend to Gaussian free field. The fluctuations of the polyanalytic Ginibre process will be discussed in a separate paper -- the limit is again the Gaussian free field, but the variance depends on the degree of polyanalyticity.

One could naturally address all the questions discussed in this article with a more general weight $Q$. We conjecture that the spectral droplet will be the same as in the analytic case. It is also likely that the blow-up of the Berezin density at a bulk point $z$ will have a universal limit, which we here computed to be $q^{-1}L^{\langle1\rangle}_{q-1}(|\xi|^2)^2\mathrm e^{-|\xi|^2}$.

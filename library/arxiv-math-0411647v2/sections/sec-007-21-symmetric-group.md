---
doc_id: arxiv-math-0411647v2
doc_title: "Asymptotics of characters of symmetric groups, genus expansion and free probability"
section_id: sec-007-21-symmetric-group
section_title: "Symmetric group"
section_number: 2.1
pages: 7-13
source_pdf: 0411647v2.pdf
source_sha256: d79f96b416cb28da
toc_source: outline
text_source: latex
latex_prose_ratio: 0.859
latex_coverage_ratio: 0.986
doc_brief: "Asymptotics of characters of symmetric groups, genus expansion and free probability — The convolution of indicators of two conjugacy classes on the symmetric group Sq is usually a complicated linear"
---
There are many equivalent definitions of the transition measure of a Young diagram [@VershikKerov1995asymptoticbehavior; @Kerov1993transition; @Kerov1999differential; @OkounkovVershik1996; @Biane1998; @Okounkov2000randompermutations] and for the sake of completeness we shall recall them in the following. Nevertheless, we shall use in this article only the description from Section [\[subsec:transition1\]](#subsec:transition1){reference-type="ref" reference="subsec:transition1"}.

### Transition measure of a Young diagram---the eigenvalues approach

[]{#subsec:biane label="subsec:biane"} The following description of the transition measure is due to Biane [@Biane1998] and probably it is the simplest one.

Consider an element $\Gamma\in {\mathcal{M}}_{q+1}\big( {\mathbb{C}}({{S}}_{q}) \big)$ given by $$\label{eq:macierzjucysia}
\Gamma=\left[
\begin{matrix}   0 & (1,2) & (1,3) & \dots & (1,q) & 1 \\
 (1,2) & 0 & (2,3) & \dots  & (2,q) & 1 \\
(1,3) & (2,3) & 0  & \dots  & (3,q) & 1 \\
 \vdots & \vdots & \vdots & \ddots  & \vdots & \vdots \\
 (1,q) & (2,q) & (3,q) & \dots  & 0 & 1 \\
 1 & 1 & 1 & \dots & 1 & 0
 \end{matrix} \right],$$

where $(i,j)\in{{S}}_{q}$ denotes the transposition exchanging $i$ and $j$.

Let $\rho^{\lambda}:{\mathbb{C}}({{S}}_{q})\rightarrow {\mathcal{M}}_k({\mathbb{C}})$ be an irreducible representation of ${{S}}_{q}$ corresponding to the Young diagram $\lambda$. We apply map $\rho^{\lambda}$ to every entry of the matrix $\Gamma\in {\mathcal{M}}_{q+1}({{S}}_{q})$ and denote the outcome by $\rho^{\lambda}(\Gamma)\in {\mathcal{M}}_{q+1}\big( {\mathcal{M}}_{k}({\mathbb{C}}) \big)= {\mathcal{M}}_{(q+1)
k} ({\mathbb{C}})$. Alternatively, if we treat $\Gamma$ as an element of ${\mathcal{M}}_{q+1}({\mathbb{C}}) \otimes {\mathbb{C}}({{S}}_{q})$ then $\rho^{\lambda}(\Gamma)= (1
\otimes \rho^{\lambda}) \Gamma\in {\mathcal{M}}_{q+1}({\mathbb{C}}) \otimes
{\mathcal{M}}_k({\mathbb{C}})={\mathcal{M}}_{(q+1)k}({\mathbb{C}})$.

Let $\zeta_1,\dots,\zeta_{(q+1)k}\in{\mathbb{R}}$ be the eigenvalues of the matrix $\rho^{\lambda}(\Gamma)\in {\mathcal{M}}_{(q+1) k} ({\mathbb{C}})$; then the transition measure of the Young diagram $\lambda$ is the probability measure on ${\mathbb{R}}$ which (up to a normalization) is the counting measure of eigenvalues of $\rho^{\lambda}(\Gamma)$: $$\mu^{\lambda}=\frac{\delta_{\zeta_1}+ \cdots + \delta_{\zeta_{(q+1)k}}}{(q+1)k}.$$

### Generalized Young diagrams

Let $\lambda$ be a Young diagram. We assign to it a piecewise affine function $\omega^\lambda:{\mathbb{R}}\rightarrow{\mathbb{R}}$ with slopes $\pm 1$, such that $\omega^\lambda(x)=|x|$ for large $|x|$ as it can be seen on the example from Figure [2](#fig:young2){reference-type="ref" reference="fig:young2"}. By comparing Figure [1](#fig:young1){reference-type="ref" reference="fig:young1"} and Figure [2](#fig:young2){reference-type="ref" reference="fig:young2"} one can easily see that the graph of $\omega^\lambda$ can be obtained from the graphical representation of the Young diagram by an appropriate mirror image, rotation and scaling by the factor $\sqrt{2}$. We call $\omega^\lambda$ the generalized Young diagram associated with the Young diagram $\lambda$ [@Kerov1993transition; @Kerov1998interlacing; @Kerov1999differential]. Alternatively, we can encode the Young diagram $\lambda$ using the sequence of local minima of $\omega^\lambda$ (denoted by $x_1,\dots,x_m$) and the sequence of local maxima of $\omega^\lambda$ (denoted by $y_1,\dots,y_{m-1})$, which form two interlacing sequences of integers [@Kerov1998interlacing].

The class of generalized Young diagrams consists of all functions $\omega:{\mathbb{R}}\rightarrow{\mathbb{R}}$ which are Lipschitz with constant $1$ and such that $\omega(x)=|x|$ for large $|x|$ and of course not every generalized Young diagram can be obtained by the above construction from some Young diagram $\lambda$.

The setup of generalized Young diagrams is very useful in the study of the asymptotic properties since it allows us to define easily various notions of convergence of the Young diagram shapes.

<figure id="fig:young1">
<embed src="figure01.eps" />
<figcaption>Young diagram associated with a partition <span class="math inline">8 = 4 + 3 + 1</span>.</figcaption>
</figure>

<figure id="fig:young2">
<embed src="figure02.eps" />
<figcaption>Generalized Young diagram associated with a partition <span class="math inline">8 = 4 + 3 + 1</span>.</figcaption>
</figure>

### Transition measure---the analytic approach

[]{#subsec:transitionanalytic label="subsec:transitionanalytic"} To any generalized Young diagram $\omega$ we can assign the unique probability measure $\mu^{\omega}$ on ${\mathbb{R}}$, called transition measure of $\omega$, which fulfills $$\label{eq:definicja3} \log \int_{{\mathbb{R}}} \frac{1}{z-x}
d\mu^{\omega}(x)=- \frac{1}{2} \int_{{\mathbb{R}}} \log (z-x) \omega''(x) dx$$ for every $z\notin{\mathbb{R}}$ [@OkounkovVershik1996; @Biane1998; @Okounkov2000randompermutations]. A great advantage of this definition is that after applying integration by parts one can easily see that the map $\omega\mapsto\mu^{\omega}$ is continuous in many reasonable topologies.

The generalized Young diagram $\omega^{p \lambda}:x \mapsto p
\omega^{\lambda}\big( \frac{x}{p} \big)$ corresponds to the Young diagram $\lambda$ geometrically scaled by factor $p>0$; it is easy to see that [\[eq:definicja3\]](#eq:definicja3){reference-type="eqref" reference="eq:definicja3"} implies that the corresponding transition measure $\mu^{p \lambda}$ is a dilation of $\mu^{\lambda}$: $$\label{eq:skalowanie} \mu^{p \lambda}= D_p \mu^{\lambda}.$$

The above definition [\[eq:definicja3\]](#eq:definicja3){reference-type="eqref" reference="eq:definicja3"} becomes simpler in the case of the (usual) Young diagrams $$\int_{{\mathbb{R}}} \frac{1}{z-x} d\mu^{\lambda}(x) =
\frac{\prod_{1\leq i \leq m-1} (z-y_i)}{\prod_{1\leq i\leq m}
(z-x_i)}$$ and implies that the transition measure is explicitly given by $$\mu^\lambda = \sum_{1\leq k\leq n}
\frac{\prod_{1\leq i\leq n-1} (x_k-y_i)  }{\prod_{i\neq k}
(x_k-x_i)} \delta_{x_k}.$$

### Transition measure---the representation theoretic approach

It is possible to find another interpretation of transition measure in the language of representation theory [@OkounkovVershik1996; @Biane1998; @Okounkov2000randompermutations]: let us consider the representation $[\lambda]\uparrow_{{{S}}_{q}}^{{{S}}_{q+1}}$ of ${{S}}_{q+1}$ induced from the representation $[\lambda]$ of ${{S}}_{q}$. By the branching rule $[\lambda]\uparrow_{{{S}}_{q}}^{{{S}}_{q+1}}$ decomposes as a direct sum of representations corresponding to the Young diagrams obtained from $\lambda$ by adding one box. It is possible to add a box exactly at the minima $x_k$. The measure $\mu_\lambda$ assigns a mass to each point $x_k$ which is proportional to the dimension of the irreducible representation of ${{S}}_{q+1}$ corresponding to the diagram $\lambda$ augmented in point $x_k$.

### Partial permutations

The following notion was introduced and studied by Ivanov and Kerov [@IvanovKerov1999]. A partial permutation of the set $A$ is a pair $\alpha=(d,w)$, where $d\subseteq A$ and $w:A\rightarrow A$ is any bijection such that $d(x)=x$ for every $x\in A\setminus d$. Set $d$ is called the support of $\alpha$. The set of partial permutations of $A$ will be denoted by $\widetilde{{{S}}_{A}}$. Given two partial permutations $(d_1,w_1)$, $(d_2,w_2)$ we consider their product $(d_1,w_1)\cdot
(d_2,w_2):=(d_1 \cup d_2, w_1 w_2)$; given this multiplication the set $\widetilde{{{S}}_{A}}$ of partial permutations becomes a semigroup. By ${{S}}_{A}$ we denote the permutation group of the set $A$. There is an important homomorphism of semigroups $\widetilde{{{S}}_{A}}\rightarrow{{S}}_{A}$ given by forgetting the support $(d,w)\mapsto w$; therefore every partial permutation can be regarded as a (usual) permutation as well.

For $A\subseteq B$ there is a homomorphism $\theta^B_A:{\mathbb{C}}(\widetilde{{{S}}_{B}})\rightarrow {\mathbb{C}}(\widetilde{{{S}}_{A}})$ of partial permutation algebras given by $$\theta^B_A (d,w)=\begin{cases} (d,w) & \text{if } d
\subseteq A, \\ 0 & \text{otherwise}.\end{cases}$$ By ${\mathbb{C}}(\widetilde{{{S}}_{\infty}})$ we denote the projective limit of algebras ${\mathbb{C}}(\widetilde{{{S}}_{\{1,\dots,q\}}})$ with respect to the morphisms $\theta$.

### Abelian algebras in the language of probability theory

Usually as a primary object of the probability theory one considers a Kolmogorov space $(\Omega,{\mathcal{M}},P)$---where $\Omega$ is a set, ${\mathcal{M}}$ is a $\sigma$--field of measurable sets and $P$ is a probability measure--- but equally well we may consider an Abelian algebra ${\mathfrak{A}}$ of all random variables on $\Omega$ with all moments finite and the expected value ${\mathbb{E}}_{\mathbb{C}}:{\mathfrak{A}}\rightarrow{\mathbb{C}}$. More generally, if $\mathcal{M}'$ is a $\sigma$--subfield of $\mathcal{M}$ we may consider an algebra ${\mathfrak{B}}$ of $\mathcal{M}'$--measurable random variables and a conditional expectation ${\mathbb{E}}_{\mathfrak{B}}:{\mathfrak{A}}\rightarrow{\mathfrak{B}}$. In this way the probability theory becomes a theory of Abelian algebras ${\mathfrak{A}}$ equipped with a linear functional ${\mathbb{E}}_{\mathbb{C}}$ or, more generally, a theory of pairs of Abelian algebras ${\mathfrak{B}}\subset{\mathfrak{A}}$ and maps ${\mathbb{E}}_{\mathfrak{B}}:{\mathfrak{A}}\rightarrow{\mathfrak{B}}$.

By turning the picture around we may regard any Abelian algebra ${\mathfrak{A}}$ equipped with a linear map ${\mathbb{E}}$ as an algebra of random variables even if ${\mathfrak{A}}$ does not arise from any Kolmogorov space (this observation was a starting point of the non--commutative probability theory [@MeyerQuantumprobability]). Now we can use the probability theoretic language when speaking about ${\mathfrak{A}}$: elements of ${\mathfrak{A}}$ can be called random variables and the numbers ${\mathbb{E}}(X^k)$ can be called moments of the random variable $X\in{\mathfrak{A}}$. Similarly we shall interpret pairs of Abelian algebras ${\mathfrak{B}}\subset{\mathfrak{A}}$ equipped with a map ${\mathbb{E}}:{\mathfrak{A}}\rightarrow{\mathfrak{B}}$.

In the classical probability theory any real--valued random variable $X$ can be alternatively viewed as a selfadjoint multiplication operator on the algebra ${\mathfrak{A}}$ and according to the spectral theorem can be written as an operator--valued integral $X=\int_{\mathbb{R}}z \
dQ(z)$, where $Q$ denotes the spectral measure of $X$. It is easy to see that the distribution $\mu$ of the random variable $X$ and the spectral measure of the operator $X$ are related by equality $\mu(F)={\mathbb{E}}_{\mathbb{C}}[ Q(F)]$ for any Borel set $F\subseteq{\mathbb{R}}$. This simple observation can be used in our new setup to define a distribution $\mu$ of an element $X=X^{\star}\in{\mathfrak{A}}$ to be a ${\mathfrak{B}}$--valued measure on ${\mathbb{R}}$ such that $\mu(F)={\mathbb{E}}_{\mathfrak{B}}[ Q(F)]$ for any Borel set $F\subseteq{\mathbb{R}}$. If $X$ is bounded then its distribution can be alternatively described by the moment formula $$\int_{\mathbb{R}}x^n \ d\mu(x)={\mathbb{E}}_{\mathfrak{B}}(X^n).$$

### Symmetric group in the language of probability theory {#subsec:symmetricgroupprobability}

Let $A$ be a finite set and let $\ast$ be an extra distinguished element such that $\ast\notin
A$. In the following, if not stated otherwise, we set $A=\{1,2,\dots,q\}$. Group ${{S}}_{A}$ will be regarded as a subgroup of ${{S}}_{A\cup \{\ast\}}$. In our case the role of the algebra ${\mathfrak{A}}$ of random variables will be played by some Abelian subalgebra of ${\mathbb{C}}({{S}}_{A\cup\{\ast\} })$ and the role of the smaller algebra ${\mathfrak{B}}$ will be played by the center of ${\mathbb{C}}({{S}}_{A})$. The conditional expectation ${\mathbb{E}}_{{\mathbb{C}}({{S}}_{A})} :{\mathbb{C}}({{S}}_{A\cup\{\ast\}})\rightarrow
{\mathbb{C}}({{S}}_{A})$ will be given by the orthogonal projection, i.e. $${\mathbb{E}}_{{\mathbb{C}}({{S}}_{A})}(\sigma)=\begin{cases} \sigma & \text{if } \sigma\in{{S}}_{A} \\
0 & \text{if } \sigma\notin{{S}}_{A} \end{cases}=
\begin{cases} \sigma & \text{if } \sigma(\ast)=\ast, \\
0 & \text{if } \sigma(\ast)\neq \ast.\end{cases}$$ In the rest of this article, when it does not lead to confusions, instead of ${\mathbb{E}}_{{\mathbb{C}}({{S}}_{A})}$ we shall simply write ${\mathbb{E}}$.

Suppose that some finite--dimensional representation $\rho:{{S}}_{A}\rightarrow {\mathcal{M}}_k({\mathbb{C}})$ is given. This allows us to define a scalar--valued expectation ${\mathbb{E}}_{\mathbb{C}}:{\mathbb{C}}({{S}}_{A\cup\{\ast\}})\rightarrow{\mathbb{C}}$ by $$\label{eq:wartoscoczekiwanahihihi} {\mathbb{E}}_{\mathbb{C}}(X)=\frac{1}{k} \mathop{\mathrm{Tr}}
\rho\big({\mathbb{E}}_{{\mathbb{C}}({{S}}_{A})}(X)\big)$$ and to consider the distribution $\mu^{\rho}$ of a random variable $X\in{\mathbb{C}}({{S}}_{A\cup\{\ast\}})$ with respect to this new expectation; in this new setup $\mu^{\rho}$ is a usual (scalar--valued) probability measure on ${\mathbb{R}}$.

### Jucys--Murphy element. Transition measure---the algebraic approach. The algebra $\mathfrak{P}$

[]{#subsec:transition1 label="subsec:transition1"} In the group algebra ${\mathbb{C}}({{S}}_{A\cup\{\ast\}})$ we consider the Jucys--Murphy element $$J= \sum_{a\in A} (a \ast),$$ where $(i j)$ denotes the transposition exchanging $i$ and $j$. We define moments of the Jucys--Murphy element by $$M^{\mathop{\mathrm{JM}}}_k={\mathbb{E}}(J^k)= \sum_{a_1,\dots,a_k\in A } {\mathbb{E}}[ (a_1 \ast) \cdots
(a_k \ast) ] \in {\mathbb{C}}({{S}}_{A}). \label{eq:wielkasuma}$$ In Section [\[subsec:momentmap\]](#subsec:momentmap){reference-type="ref" reference="subsec:momentmap"} of we shall consider an extension of this concept.

For a given Young diagram $\lambda\vdash |A|$ we consider $\rho=\rho^\lambda$ to be an irreducible representation of ${{S}}_{A}$ corresponding to $\lambda$ and consider the distribution $\mu^{\lambda}:=\mu^{\rho^{\lambda}}$ of the element $J$ with respect to the expected value [\[eq:wartoscoczekiwanahihihi\]](#eq:wartoscoczekiwanahihihi){reference-type="eqref" reference="eq:wartoscoczekiwanahihihi"}.

We call $\mu^{\lambda}$ the transition measure of $\lambda$ [@VershikKerov1995asymptoticbehavior; @Kerov1993transition; @OkounkovVershik1996; @Biane1998; @Okounkov2000randompermutations]. This definition is very algebraic and for this reason it will be our favorite definition of the transition measure.

We can treat the moments $M^{\mathop{\mathrm{JM}}}_k$ of the Jucys--Murphy element as elements of the partial permutations algebra ${\mathbb{C}}(\widetilde{{{S}}_{A}})$; in order to do this we treat every non--zero summand on the right--hand side of [\[eq:wielkasuma\]](#eq:wielkasuma){reference-type="eqref" reference="eq:wielkasuma"} as a partial permutation with the support $\{a_1,\dots,a_k\}$. It is easy to check that for $A\subseteq B$ the morphism $\theta^B_A$ maps $M^{\mathop{\mathrm{JM}}}_k\in{\mathbb{C}}(\widetilde{{{S}}_{B}})$ to $M^{\mathop{\mathrm{JM}}}_k\in{\mathbb{C}}(\widetilde{{{S}}_{A}})$ hence the projective limit of the elements $M^{\mathop{\mathrm{JM}}}_k\in{\mathbb{C}}(\widetilde{{{S}}_{q}})$ exists and will be denoted by the same symbol $M^{\mathop{\mathrm{JM}}}_k\in{\mathbb{C}}(\widetilde{{{S}}_{\infty}})$.

We denote by $\mathfrak{P}$ the algebra generated by elements $M^{\mathop{\mathrm{JM}}}_k\in{\mathbb{C}}(\widetilde{{{S}}_{\infty}})$. It is easy to check that $\mathfrak{P}$ is commutative. Elements of $\mathfrak{P}$ can be also regarded as elements of ${\mathbb{C}}(\widetilde{{{S}}_{q}})$ and ${\mathbb{C}}({{S}}_{q})$.

### Gradation on $\mathfrak{P}$ {#subsec:degree1}

Since we would like to study asymptotic properties of Young diagrams, we need to specify what kind of scaling we are interested in.

Let a sequence of Young diagrams $(\lambda_N)$ be given, $\lambda_N\vdash N$. It is natural to consider generalized Young diagrams which correspond to geometrically scaled diagrams $\frac{1}{\sqrt{N}} \lambda_N$ (observe that all such scaled diagrams have the same area equal to $2$). Suppose that the shape of the scaled diagrams converges in some sense toward a generalized Young diagram $\lambda$. In many natural topologies this implies the convergence of scaled moments of the transition measure, cf [\[eq:skalowanie\]](#eq:skalowanie){reference-type="eqref" reference="eq:skalowanie"}

$$\begin{gathered}
\lim_{N\rightarrow\infty} \frac{1}{N^{k/2}} {\mathbb{E}}_{\mathbb{C}}(M^{\mathop{\mathrm{JM}}}_k)=
 \lim_{N\rightarrow\infty} {\mathbb{E}}_{{\mathbb{C}}} \left[ \left( \frac{1}{N^{1/2}} J \right)^k \right]=
\\
\lim_{N\rightarrow\infty} \frac{1}{N^{k/2}} \int_{\mathbb{R}}x^k
d\mu^{\lambda_N}(x) =  \int_{\mathbb{R}}x^k d\mu^{\lambda}(x).
\end{gathered}$$ In the study of asymptotic properties of some elements of the group algebra ${\mathbb{C}}({{S}}_{N})$ we would like to group summands which have asymptotically the same growth for large $N$ and for this reason $M^{\mathop{\mathrm{JM}}}_k$ can be treated as a monomial in ${\sqrt{N}}$ of degree $k$.

More formally, we consider a gradation on $\mathfrak{P}$ by setting $$\label{eq:gradation} \deg M^{\mathop{\mathrm{JM}}}_k=k.$$ In Corollary [\[cor:algebraicallyfree\]](#cor:algebraicallyfree){reference-type="ref" reference="cor:algebraicallyfree"} we will show that $M^{\mathop{\mathrm{JM}}}_2,M^{\mathop{\mathrm{JM}}}_3,\dots\in{\mathbb{C}}(\widetilde{{{S}}_{\infty}})$ are algebraically free and therefore this gradation is well defined. This gradation coincides with the weight gradation considered by Ivanov and Olshanski [@IvanovOlshanski2002].

### Normalized conjugacy class indicators {#subsec:definicjasigma}

Let integer numbers $k_1,\dots,k_m\geq 1$ be given. We define the normalized conjugacy class indicator

$\Sigma_{k_1,\dots,k_m}\in{\mathbb{C}}({{S}}_{A})$ as follows [@KerovOlshanski1994; @BianeCharacters]:

$$\label{eq:definicjasigma} \Sigma_{k_1,\dots,k_m}=

\sum_{a} (a_{1,1},a_{1,2},\dots,a_{1,{k_1}}) \cdots
(a_{m,1},a_{m,2},\dots,a_{m,k_m}),$$

where the sum runs over all one--to--one functions $$a:\big\{ \{r,s\}: 1\leq r\leq m, 1\leq s\leq {k_r}\big\}\rightarrow A$$ and $(a_{1,1},a_{1,2},\dots,a_{1,{k_1}}) \cdots
(a_{m,1},a_{m,2},\dots,a_{m,k_m})$ is a product of disjoint cycles. Of course, if $|A|<k_1+\cdots+k_m$ then the above sum runs over an empty set and $\Sigma_{k_1,\dots,k_m}=0$. If any of the numbers $k_1,\dots,k_m$ is equal to $0$ we set $\Sigma_{k_1,\dots,k_m}=0$.

In other words, let $k_1'\geq \cdots \geq k_m'$ be the sequence $k_1,\dots,k_m$ sorted decreasingly; we consider a Young diagram $(k_1',\dots,k_m')$ and all ways of filling it with the elements of the set $A$ in such a way that no element appears more than once. Each such a filling can be interpreted as a permutation when we treat rows of the Young tableau as disjoint cycles.

We can also treat $\Sigma_{k_1,\dots,k_m}$ as a an element of the partial permutations algebra ${\mathbb{C}}(\widetilde{{{S}}_{A}})$; in order to do this, we treat every summand $(a_{1,1},a_{1,2},\dots,a_{1,{k_1}})
\cdots (a_{m,1},a_{m,2},\dots,a_{m,k_m})$ as a partial permutation with support $\{ a_{ij} : 1\leq i\leq m, 1\leq j\leq {k_i}  \}$. It is easy to check that for $A\subseteq B$ the morphism $\theta^B_A$ maps $\Sigma_{k_1,\dots,k_m}\in{\mathbb{C}}(\widetilde{{{S}}_{B}})$ to $\Sigma_{k_1,\dots,k_m}\in{\mathbb{C}}(\widetilde{{{S}}_{A}})$ hence the projective limit of the elements $\Sigma_{k_1,\dots,k_m}\in{\mathbb{C}}(\widetilde{{{S}}_{q}})$ exists and will be denoted by the same symbol $\Sigma_{k_1,\dots,k_m}\in{\mathbb{C}}(\widetilde{{{S}}_{\infty}})$. It is easy to check that elements $\Sigma_{k_1,\dots,k_m}\in{\mathbb{C}}(\widetilde{{{S}}_{\infty}})$ commute.

### Filtration

We consider a filtration on the commutative algebra generated by $\Sigma_{k_1,\dots,k_m}\in{\mathbb{C}}(\widetilde{{{S}}_{\infty}})$ by setting $$\label{eq:filtration} \deg
\Sigma_{k_1,\dots,k_m}=(k_1+1)+(k_2+1)+\cdots+(k_m+1).$$ It is easy to check that the elements from the family $\Sigma_{k_1,\dots,k_m}\in{\mathbb{C}}(\widetilde{{{S}}_{\infty}})$ indexed by integer $m\geq 0$ and $k_1\geq \cdots \geq k_m\geq 1$ are linearly independent and therefore this definition makes sense but it is not clear that this formula indeed defines a filtration; we shall prove it in Corollary [\[cor:filtration\]](#cor:filtration){reference-type="ref" reference="cor:filtration"}. The reason for studying this filtration is that---as we shall see in Theorem [\[theo:kontrolastopnia\]](#theo:kontrolastopnia){reference-type="ref" reference="theo:kontrolastopnia"}---elements $M^{\mathop{\mathrm{JM}}}_k\in{\mathbb{C}}(\widetilde{{{S}}_{\infty}})$ and $\Sigma_{k_1,\dots,k_m}\in{\mathbb{C}}(\widetilde{{{S}}_{\infty}})$ generate the same commutative algebra denoted by $\mathfrak{P}$ and filtration [\[eq:filtration\]](#eq:filtration){reference-type="eqref" reference="eq:filtration"} is induced by the gradation [\[eq:gradation\]](#eq:gradation){reference-type="eqref" reference="eq:gradation"}.

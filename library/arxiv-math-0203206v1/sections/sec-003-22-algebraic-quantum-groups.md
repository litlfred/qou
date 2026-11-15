---
doc_id: arxiv-math-0203206v1
doc_title: "arXiv:math/0203206v1 [math.QA] 20 Mar 2002"
section_id: sec-003-22-algebraic-quantum-groups
section_title: "Algebraic Quantum Groups"
section_number: 2.2
pages: 6-9
source_pdf: 0203206v1.pdf
source_sha256: 371611f719e6f53c
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.996
latex_coverage_ratio: 0.988
doc_brief: "arXiv:math/0203206v1 [math.QA] 20 Mar 2002 — We give a pedagogical survey of those aspects of the abstract representation theory of quantum groups which are related to the Tannaka-Krein"
---
In this subsection we briefly outline those aspects of the theory of aqg that will be needed in the sequel. For the details and proofs, see the original references [@VD2; @VD].

Every algebra will be a (not necessarily unital) associative algebra over the complex field ${\mathbb C}$. The identity map on a set $V$ will be denoted by $\iota$. If $V$ and $W$ are linear spaces, $V'$ denotes the linear space of linear functionals on $V$ and $V \otimes W$ denotes the linear space tensor product of $V$ and $W$. The *flip map* $\sigma$ from ${V \otimes W}$ to ${W \otimes V}$ is the linear map sending ${v\otimes w}$ onto ${w\otimes v}$, for all $v\in V$ and $w\in W$. If $V$ and $W$ are Hilbert spaces, ${V\otimes W}$ denotes their Hilbert space tensor product; we denote by $B(V)$ and $B_0(V)$ the C\*-algebras of bounded linear operators and compact operators on $V$, respectively. If $V$ and $W$ are algebras, ${V \otimes W}$ denotes their algebra tensor product. If $V$ and $W$ are C\*-algebras, then ${V\otimes W}$ will denote their C\*-tensor product with respect to the minimal C\*-norm.

An algebra $A$ is *non-degenerate* if for any $a\in A$ such that $ab=0$ for all $b\in A$ or $ba=0$ for all $b\in A$, we have $a=0$. Obviously, all unital algebras are non-degenerate. If $A$ and $B$ are non-degenerate algebras, so is $A\otimes B$. From now on *all* algebras are assumed to be non-degenerate.

Let $A$ be a $*$-algebra and denote by $\mathrm{End}\,A$ the unital algebra of linear maps from $A$ to itself. Let $$M(A)= \{ x\in\mathrm{End}\,A \ | \ \exists y\in\mathrm{End}\,A\ \mbox{such that}\ 
     x(a)^* b = a^* y(b) \quad \forall a,b \in A \}.$$ Then $M(A)$ is a unital subalgebra of $\mathrm{End}\,A$. The linear map $y$ associated to a given $x\in M(A)$ is uniquely determined by non-degeneracy and we denote it by $x^*$. The unital algebra $M(A)$ becomes a $*$-algebra when endowed with the involution ${x \mapsto x^*}$. This unital $*$-algebra is called the *multiplier algebra* of $A$.

Suppose that $A$ is an ideal in a $*$-algebra $B$. For $b \in B$, define $L_b \in M(A)$ by $L_b(a)=b a$, for all $a \in A$. Then the map $L\colon B \rightarrow M(A)$, $b \mapsto L_b$, is a homomorphism. If $A$ is an *essential* ideal in $B$ in the sense that an element $b$ of $B$ is necessarily equal to zero if $b a=0$, for all $a\in A$, or $a
b=0$, for all $a\in A$, then $L$ is injective. In particular, $A$ is an essential ideal in itself (by non-degeneracy) and therefore we have an injective homomorphism $L\colon A \rightarrow M(A)$. We identify the image of $A$ under $L$ with $A$. Then $A$ is an essential ideal of $M(A)$. (In fact, $M(A)$ is the 'largest' algebra containing $A$ as an essential ideal.) Obviously, $M(A) = A$ iff $A$ is unital.

If $A$ and $B$ are $*$-algebras, then it is easily verified that $A\otimes B$ is an essential self-adjoint ideal in $M(A)\otimes M(B)$. Hence, by the preceding remarks, there exists a canonical injective $*$-homomorphism from $M(A)\otimes M(B)$ into $M(A\otimes B)$. We use this to identify $M(A)\otimes M(B)$ as a unital $*$-subalgebra of $M(A\otimes B)$. In general, these algebras are not equal. A linear map $\pi \colon A \to B$ is said to be *non-degenerate* if $\pi(A)B=B$ and $B\pi(A)=B$. Here, as elsewhere, $\pi(A)B$ denotes the linear span of ${\{\pi(a)b\mid a\in A,\  b\in B\}}$. Whenever $\pi$ is non-degenerate and multiplicative (resp. non-degenerate and antimultiplicative), there exists a unique extension to a unital homomorphism (resp. antihomomorphism) ${\overline{\pi} \colon M (A) \rightarrow M (B)}$. We shall henceforth use the same symbol $\pi$ to denote the original map and its extension $\overline{\pi}$. A *representation* of a $*$-algebra is a non-degenerate homomorphism $\pi:A\rightarrow B(K)$, where $K$ is a Hilbert space.

If $\omega$ is a linear functional on $A$ and $x \in M(A)$, we define the linear functionals $x \omega$ and $\omega x$ on $A$ by setting $(x \omega)(a) = \omega(a x)$ and $(\omega x)(a) =
\omega(x a)$, for all $a \in A$. We need the leg numbering notation. Take three $*$-algebras $A$, $B$, $C$. It can be shown that there exists a non-degenerate $*$-homomorphism $\theta_{13} : A \otimes C \rightarrow M(A \otimes B \otimes C)$ such that $\theta_{13}(a \otimes c) = a \otimes 1 \otimes c$, for all $a \in A$, $c \in C$. Thus, it has a unique extension to $M(A \otimes C)$. Set $x_{13} = \theta_{13}(x)$, for all $x \in M(A \otimes C)$. The other variants of the leg numbering notation are defined similarly.

The triple product $A\otimes A\otimes A$ is an essential ideal of both $M(A\otimes A)\otimes A$ and $A\otimes M(A\otimes A)$, thus $M(M(A\otimes A)\otimes A)\subset M(A\otimes A\otimes A)$ and $M(A\otimes M(A\otimes A))\subset M(A\otimes A\otimes A)$.

::: defin
[]{#def-mult-hopf-alg label="def-mult-hopf-alg"} A multiplier Hopf $*$-algebra $(A, \Delta)$ consists of a $*$-algebra $A$ and a $*$-homomorphism $\Delta$ from $A$ into $M(A\otimes A)$ such that

1.  $(\Delta\otimes \iota)\Delta= (\iota \otimes \Delta)\Delta$.

2.  The linear mappings $T_1,  T_2$ from $A \otimes A$ into $M(A \otimes A)$ such that $$\begin{aligned}
    \ T_1(a \otimes b) &=& \Delta(a)(b \otimes 1), \\
      T_2(a \otimes b) &=& \Delta(a)(1 \otimes b) 
    \end{aligned}$$ for all $a, b \in A$, are bijections from $A \otimes A$ to $A \otimes A$.
:::

Here the (unique) extension of $\Delta\otimes \iota: A\otimes A\rightarrow M(A\otimes A\otimes A)$ to $M(A\otimes A)$ is understood and similarly for $\iota \otimes \Delta$. Condition (ii) implies that $\Delta(a)(b\otimes 1), \Delta(a)(1\otimes b)\in M(A\otimes A)$ lie in fact in $A\otimes A$.

We say that two multiplier Hopf $*$-algebras $(A_1, \Delta_1 )$ and $(A_2, \Delta_2 )$ are *isomorphic*, and write $(A_1, \Delta_1 )\cong (A_2, \Delta_2 )$, if there exists a bijective $*$-homomorphism $\theta : A_1\rightarrow A_2$ such that $(\theta\otimes\theta )\Delta_1 =\Delta_2\theta$.

The following result shows that multiplier Hopf $*$-algebras share most properties with Hopf algebras. Let $m: A\otimes A\rightarrow A$ denote the linear extension of the multiplication map. Note that $m$ is a $*$-homomorphism iff $A$ is commutative.

::: prop
[]{#p-converse label="p-converse"} Let $(A,\Delta)$ be a multiplier Hopf $*$-algebra. There exist a unique $*$-homomorphism $\varepsilon: A\rightarrow{\mathbb C}$ and a unique invertible antimultiplicative $S\in\mathrm{End}\,A$ such that

1.  $\displaystyle(\varepsilon\otimes\iota)(\Delta(a)(1\otimes b)) = ab$,

2.  $\displaystyle(\iota\otimes\varepsilon)(\Delta(a)(b\otimes 1)) = ab$,

3.  $\displaystyle m(S\otimes\iota)(\Delta(a)(1\otimes b)) = \varepsilon(a)b$,

4.  $\displaystyle m(\iota\otimes S)(\Delta(a)(b\otimes 1)) = \varepsilon(a)b$

for all $a,b\in A$. We call $\varepsilon$ the counit and $S$ the coinverse. Conversely, if $(A\otimes 1)\Delta(A)\subset A\otimes A$ and $(A\otimes 1)\Delta(A)\subset A\otimes A$ and there exist linear maps $\varepsilon :A\rightarrow{\mathbb C}$ and $S:A\rightarrow A$ satisfying properties 1-4 with $S$ invertible, then $(A,\Delta)$ is a multiplier Hopf $*$-algebra.
:::

We denote $m_{\mbox{\scriptsize op}}=m\sigma$ and $\Delta_{\mbox{\scriptsize op}}=\sigma\Delta$ where $\sigma(a\otimes b)=b\otimes a$ is the flip $*$-automorphism of $A\otimes A$ and $M(A\otimes A)$. $A_{\mbox{\scriptsize op}}$ denotes the vector space $A$ with multiplication $m_{\mbox{\scriptsize op}}$. The following result follows easily from the uniqueness of the counit and coinverse.

::: prop
The antipode $S$ is invertible and

1.  $\displaystyle S^{-1}(a)=S(a^*)^*\quad\forall a\in A$.

2.  $\displaystyle(S\otimes S)(\Delta(a)(1\otimes b)) = (1\otimes S(b))\Delta_{\mbox{\scriptsize op}}S(a) \quad\forall a,b\in A$.

3.  $\displaystyle\varepsilon S=\varepsilon$.

4.  $(A_{\mbox{\scriptsize op}}, \Delta)$ and $(A,\Delta_{\mbox{\scriptsize op}})$ are multiplier Hopf $*$-algebras with counit $\varepsilon$ and coinverse $S^{-1}$.
:::

::: defin
A linear functional $\omega$ on a multiplier Hopf $*$-algebra $(A,\Delta)$ is called

1.  positive iff $\omega(a^*a)\geq 0\quad\forall a\in A$,

2.  faithful iff it is positive and $\omega(a^*a) = 0 \Rightarrow a =0 \quad \forall a\in A$,

3.  left-invariant iff $(\iota\otimes\omega )(\Delta(a)(b\otimes 1)) = \omega(a)b \ \ \forall a,b \in A$,

4.  right-invariant iff $(\omega\otimes\iota)((1\otimes b)\Delta(a)) = \omega(a)b \ \ \forall a,b \in A$.
:::

Thus $\omega$ is left-invariant iff $\omega S$ is right-invariant.

::: defin
An aqg is a multiplier Hopf $*$-algebra $(A, \Delta)$ which admits a non-zero left-invariant positive linear functional $\varphi$.
:::

::: thm
[]{#thm-faithful label="thm-faithful"} Let $(A, \Delta)$ be an aqg with positive left-invariant functional $\varphi$. Then

1.  $\varphi$ is faithful.

2.  If $\omega$ is a left-invariant functional, there exists $c\in{\mathbb C}$ such that $\omega=c\varphi$.

3.  If $\omega$ is a right-invariant functional, there exists $c\in{\mathbb C}$ such that $\omega=c\varphi S$.
:::

An immediate consequence is that the $*$-operation is positive, viz. $a^*a=0\ \Rightarrow\ a=0$, which clearly is stronger than non-degeneracy. Furthermore, there exists a unique complex number $\mu$ such that $\varphi S^2 = \mu \varphi$. It can be proved that $|\mu| = 1$, but it has recently been discovered that $\mu\neq 1$ for the quantum group version of $ax+b$ [@VD3]. Every aqg $(A,\Delta)$ has the property that to any $a\in A$, there exists $c\in A$ such that $ac=ca=a$. Two aqg are said to be *isomorphic* if they are isomorphic as multiplier Hopf $*$-algebras and we use the same notation $\cong$ to denote this.

Set $\psi = \varphi S$. Then $\psi$ is a non-zero right-invariant linear functional on $A$. However, in general, $\psi$ will not be positive. It is known that there exists a non-zero positive right-invariant linear functional on $A$. To $\varphi$ there existence a unique automorphism $\rho$ on $A$ such that $\varphi(ab) =
\varphi(b\rho (a))$, for every $a, b \in A$. We refer to this as the weak KMS-property of $\varphi$. Moreover, we have $\Delta\rho = (S^2 \otimes \rho)\Delta$ and $\rho(\rho(a^*)^*) = a$, for every $a \in A$. Also there exists an automorphism $\rho'$ for the right-invariant functional $\psi$, that is, $\rho'$ is an automorphism on $A$ such that $\psi(ab) = \psi(b\rho '(a))$, for every $a, b \in A$.

It is possible to introduce a modular function for aqg. It is an invertible element $\delta$ in $M(A)$ such that $(\varphi \otimes \iota)(\Delta(a)(1\otimes b)) = \varphi(a)\delta b$, for every $a, b \in A$. This modular function satisfies

$$\Delta(\delta) = \delta \otimes \delta, \quad \varepsilon (\delta) = 1, \quad S(\delta) = \delta^{-1}.$$

As in the classical case we have $$\varphi(S(a)) = \varphi(a\delta)=\mu\varphi (\delta a) \quad \forall a\in A.$$

We now discuss duality within the category of aqg. Define a subspace $\hat A$ of $A'$ by $$\hat A = \{\varphi a \ | \ a \in A\} = \{a \varphi\  | \ a \in A \}.$$ Then $\hat A$ is a non-degenerate $*$-algebra under the definitions:

1.  For every $\omega_1, \omega_2 \in \hat A$ and $a \in A$, we have $(\omega_1 \omega_2)(a) = (\omega_1 \otimes \omega_2)(\Delta(a))$.

2.  For every $\omega \in \hat A$ and $a \in A$, define $\omega^*(a) = \overline {\omega(S(a)^*)}$.

The comultiplication $\hat \Delta$ is defined on $\hat A$ by $\hat \Delta(\omega)(x \otimes y) = \omega(xy)$, for every $\omega \in \hat A$ and $x, y \in A$. For this to make sense, $M(A \otimes A)$ should be embedded in $(A \otimes A)'$ in a proper way. A definition of the comultiplication $\hat \Delta$ that does not use such an embedding can be found in [@ku-e]. Then $(\hat A, \hat \Delta)$ is a multiplier Hopf $*$-algebra with counit $\hat \varepsilon$ and the antipode $\hat S$ given by:

1.  $\hat \varepsilon(\omega) = \omega(1)$, for every $\omega \in \hat A$.

2.  $\hat S(\omega)(a) = \omega(S(a))$, for every $\omega \in \hat A$ and $a \in A$.

Define $\hat a = a\varphi \in \hat A$, for $a \in A$. The map $A \rightarrow \hat A$ sending $a$ to $\hat a$ is a bijection, and is referred to as the Fourier transform. Next define the linear functional $\hat{\psi}$ on $\hat A$ by setting $\hat{\psi}(\hat a) = \varepsilon(a)$, for every $a \in A$. It is possible to prove that $\hat\psi$ is right-invariant, and that $\hat \psi(\hat a ^* \hat a)=\varphi (a^* a)$, for every $a \in A$. It follows that $\hat \psi$ is a non-zero positive linear functional on $\hat A$, and that the dual $(\hat A, \hat \Delta)$ is an aqg. Let $\hat{\rho}$ denote the automorphism of $\hat{A}$ such that $\hat{\psi}(\hat a\hat b)=\hat{\psi}(\hat b\hat{\rho}(\hat a ))$, for all $a,b\in A$. The aqg version of Pontryagin's duality theorem takes the following form:

::: thm
[]{#dual label="dual"} Let $(A, \Delta)$ be an aqg. Then the double dual $(\hat{A} \hspace{-.55ex}\hat{\rule{0ex}{2.0ex}}\hspace{.55ex}, \hat{\Delta} \hspace{-.95ex}\hat{\rule{0ex}{2.05ex}}\hspace{.95ex})$ is an aqg isomorphic to $(A, \Delta)$. More precisely, there exists a canonical $*$-isomorphism $\theta : A \rightarrow \hat {\hat A}$ such that $\theta(a)(\omega) = \omega(a)$, for all $a \in \hat A$, and that satisfies the equation $(\theta \otimes \theta)\Delta= \hat {\hat \Delta} \theta$.
:::

Note that an aqg $(A,\Delta)$ is commutative iff $(\hat{A},\hat{\Delta})$ is cocommutative.

We shall need to consider an object associated to an aqg called its analytic extension. See [@KD] for full details. If $A$ is a C\*-algebra, then $M(A)$ denotes the usual multiplier algebra of $A$, and $*$-homomorphism between C\*-algebras are assumed to be non-degenerate in the usual operator algebraic sense. We need first to recall the concept of a GNS pair. Suppose given a positive linear functional $\omega$ on a $*$-algebra $A$. Let $H$ be a Hilbert space, and let ${\Lambda\colon A\to H}$ be a linear map with dense range for which $(\Lambda(a),\Lambda(b))=\omega(b^*a)$, for all $a,b\in A$. Then we call $(H,\Lambda)$ a *GNS pair* associated to $\omega$. As is well known, such a pair always exists and is essentially unique.

If $\varphi$ is a left Haar integral on an aqg $(A,\Delta)$, and $(H,\Lambda)$ is an associated GNS pair, then it can be shown that there is a unique $*$-homomorphism ${\pi\colon A\to B(H)}$ such that $\pi(a)\Lambda(b)=\Lambda(a b)$, for all ${a,b\in A}$. Moreover, $\pi$ is faithful and non-degenerate. We let $A_r$ denote the norm closure of $\pi(A)$ in $B(H)$. Thus, $A_r$ is a non-degenerate C\*-subalgebra of $B(H)$. There exists a unique non-degenerate $*$-homomorphism ${\Delta_{\mathrm{r}}: A_r \rightarrow M(A_r\otimes A_r)}$ such that, for all $a \in A$ and all $x \in A \otimes A$, we have ${\Delta_{\mathrm{r}}(\pi(a)) (\pi \otimes \pi) (x)} = {(\pi \otimes \pi) (\Delta (a)x)}$ and ${(\pi \otimes \pi)
(x)\Delta_{\mathrm{r}}(\pi(a))} = {(\pi \otimes \pi) (x \Delta (a))}$.

Define a linear map $\hat{\Lambda} :\hat{A}\rightarrow H$ by setting $\hat{\Lambda}(\hat {a})=\Lambda (a)$, for all $a\in{\cal A}$. Since $\hat{\psi} (\hat{b}^*\hat{a})
=\varphi (b^*a)=(\Lambda(a),\Lambda(b))$, for all $a,b\in A$, it follows that $(H,\hat{\Lambda})$ is a GNS-pair associated to $\hat{\psi}$. It can be shown that it is unitarily equivalent to the GNS-pair for a left Haar integral $\hat{\varphi}$ of $(\hat
A,\hat \Delta)$. Hence, we can use $(H,\hat\Lambda)$ to define a representation of the analytic extension $(\hat{A}_r, \hat \Delta_{\mathrm{r}})$ of $(\hat A, \hat \Delta)$ on the space $H$. There is a unique $*$-homomorphism $\hat{\pi}_r :\hat{A}\rightarrow B(H)$ such that $\hat{\pi}_r (a )\hat{\Lambda}(b )=\hat{\Lambda}(a b)$, for all $a,b\in\hat{A}$. Moreover, $\hat\pi$ is faithful and non-degenerate. Let $\hat A_r$ be the norm closure of $\hat{\pi}_r (A)$ in $B(H)$, so $\hat A_r$ is a non-degenerate C\*-subalgebra of $B(H)$. There exist a unique $*$-homomorphism $\hat{\Delta}_r: \hat{A}_r \rightarrow M(\hat{A}_r\otimes\hat{A}_r)$ such that, for all $a \in \hat{A}$ and $x \in \hat{A} \otimes \hat{A}$, $\hat{\Delta}_r(\hat\pi(a)) (\hat\pi \otimes \hat\pi) (x) =
(\hat\pi \otimes \hat\pi) (\hat{\Delta} (a)x)$ and $(\hat\pi \otimes \hat\pi) (x)\hat \Delta_r (\hat\pi(a))=(\hat\pi\otimes\hat\pi)(x\hat{\Delta}(a))$.

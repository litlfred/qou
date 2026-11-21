---
doc_id: arxiv-1905.11619v2
doc_title: "L2-COHOMOLOGY, DERIVATIONS AND QUANTUM MARKOV SEMI-GROUPS ON q-GAUSSIAN ALGEBRAS"
section_id: sec-009-41-q-gaussian-algebras
section_title: "q-Gaussian algebras"
section_number: 4.1
pages: 10-11
source_pdf: 1905.11619v2.pdf
source_sha256: f634f9ec4357d5f3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.908
latex_coverage_ratio: 0.962
doc_brief: "L2-COHOMOLOGY, DERIVATIONS AND QUANTUM MARKOV SEMI-GROUPS ON q-GAUSSIAN ALGEBRAS — We study (quasi-)cohomological properties through an analysis of quantum Markov semi-groups."
---
Let $H_{\mathbb{R}}$ be a finite dimensional real Hilbert space with complexification $H = H_{\mathbb{R}}\otimes \mathbb{C}$. We denote by $I$ the complex conjugation on $H$ and we extend it to $H^{\otimes n}$ by $I(v_1\otimes\dots\otimes v_n):= Iv_n\otimes\dots\otimes Iv_1$. Let $q \in (-1, 1)$ and consider the symmetrization operator on $H^{\otimes n}$ given by $$P_q^n(\xi_1 \otimes \ldots \otimes \xi_n) = \sum_{\sigma \in S_n}  q^{i(\sigma)} \xi_{\sigma(1)} \otimes \ldots \otimes \xi_{\sigma(n)},$$ where $i(\sigma)$ is the number of inversions in $\sigma$. Recall that an inversion is a pair $(a,b) \in \{ 1, \ldots, n \}$ with $a < b$ and $\sigma(a) > \sigma(b)$. For $q \in (-1, 1)$ we set new inner products on $H^{\otimes n}$ by $$\langle \xi, \eta \rangle_q =   \langle P_q^n \xi, \eta \rangle,$$ and we refer to the Hilbert space with this $q$-deformed inner product as $H_q^{\otimes n}$. Also set the $q$-Fock space $F_q(H) = \mathbb{C} \Omega \oplus (\oplus_{n=1}^\infty H_q^{\otimes n})$, with $\Omega$ a unit vector called the vacuum vector. Note that the conjugation $I$ extends to an antiunitary operator on $F_q(H)$; a typical permutation does not preserve the $q$-deformed inner product, so it is a special feature of the permutation reversing the order. We set the left creation operator for $\xi \in H$, $$l_q(\xi) \eta_1 \otimes \ldots \otimes \eta_n = \xi \otimes \eta_1 \otimes \ldots \otimes \eta_n,$$ and the annihilation operator $l_q^\ast(\xi) = l_q(\xi)^\ast$. These operators are bounded and extend to $F_q(H)$ for $q \in (-1, 1)$. We define the **$q$-Gaussian algebra** as $$\Gamma_q := \Gamma_q(H_{\mathbb{R}}) := \mathcal{A}_q'', \qquad \mathcal{A}_q := \ast{\rm -alg} \{ \: l_q(\xi) + l_q(\xi)^\ast \mid \xi \in H_{\mathbb{R}}\}.$$ We let $\varphi_{\Omega}$ be the (tracial) vacuum state on $\Gamma_q(H_{\mathbb{R}})$ given by $\varphi_{\Omega}(x) = \langle x \Omega, \Omega \rangle$. $\Omega$ is a separating and cyclic vector for $\Gamma_q(H_{\mathbb{R}})$ and so $\varphi_{\Omega}$ is faithful and $F_q(H)$ is the standard Hilbert space of $\Gamma_q$. In this setting $\Omega$ is a tracial vector and further $\Gamma_q$ is a II$_1$-factor [@RicardCMP].

For vectors $\xi_1, \ldots, \xi_n \in H$ there exists a unique operator $W_q(\xi_1 \otimes \ldots \otimes \xi_n) \in \Gamma_q(H_{\mathbb{R}})$ such that, $$W_q(\xi_1 \otimes \ldots \otimes \xi_n) \Omega = \xi_1 \otimes \ldots \otimes \xi_n.$$ We call these operators **elementary Wick operators** or **elementary Wick words**. The **Ornstein-Uhlenbeck** quantum Markov semi-group is then defined by[^1] $$\Phi_t ( W_q(\xi_1 \otimes \ldots \otimes \xi_n)) = e^{-t n}  W_q(\xi_1 \otimes \ldots \otimes \xi_n).$$ It comes with a generator (the quantum Dirichlet form) given by the number operator $$\Delta (\xi_1 \otimes \ldots \otimes \xi_n) = n \xi_1 \otimes \ldots \otimes \xi_n.$$ We determine the cohomology as follows.

::: thm
[]{#CartanEilenberg label="CartanEilenberg"} For any $\mathcal{A}_q$-$\mathcal{A}_q$-bimodule $H$ we have $H^n(\mathcal{A}_q, H) = 0$ for $n \geq 2$.
:::

::: proof
*Proof.* Let $e_1, \ldots, e_m$ be an orthonormal basis of $H_{\mathbb{R}}$. We claim that algebraically $\mathcal{A}_q$ is isomorphic to the $\ast$-algebra of non-commutative polynomials in $m$ self-adjoint variables $X_1, \ldots X_m$ by the identification $X_i := W_q(e_i)$. Indeed, let $P$ be a non-commutative polynomial and suppose that $P(X_1, \ldots, X_m) = 0$. Let $Q(X_1, \ldots, X_n) = X_{i_1} \ldots X_{i_d}$ be a monomial occuring in $P$ of highest degree $d$. Then, from Lemma [\[Lem=WickProduct\]](#Lem=WickProduct){reference-type="ref" reference="Lem=WickProduct"} below, we find $Q(X_1, \ldots, X_n) = W_q(X_{i_1} \otimes \ldots \otimes X_{i_d}) + A$ where $A$ is a linear combination of Wick operators $W_q(\xi_1 \otimes \ldots \otimes \xi_k)$ of tensors of order $k < d$. If $P(X_1, \ldots, X_m) = 0$ we must therefore have that $Q(X_1, \ldots, X_m) =0$. By induction we conclude that $P =0$.

Now in [@CartanEilenberg p. 192] it is shown that for the algebra of non-commutative polynomials, the Hochschild cohomology with coefficients in any bimodule is 0. Alternatively, see [@Kassel Eqn. (5.11)] for an explicit short exact projective resolution which also yields this result. ◻
:::

[^1]: It extends to the $q$-Gaussian algebra by [@BKS Theorem 2.11].

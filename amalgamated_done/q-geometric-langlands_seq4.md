<!-- FILE_START: q-opers-intro.md -->
We turn to the spectral side of the conjecture and the canonical objects that realise it. We introduce the $q$-oper: a $\check{G}_q$-bundle on $X$, equipped with a reduction to the Borel subgroup and a $q$-flat connection in oper position. This object provides the rigid spectral data dual to the automorphic $q$-Hecke eigensheaves. The fibre functor maps every $q$-oper to a $q$-Hecke eigensheaf, with the eigenvalue determined by the oper coordinates. This concretely realises the abstract Tannakian mediation.
<!-- FILE_END: q-opers-intro.md -->

<!-- FILE_START: q-oper.md -->
For $\check{G}_q = \mathrm{SU}_{q^{-1}}(2)$, a $q$-oper on a brane curve $X$ is a rank-$2$ $q$-flat bundle with an invariant line subbundle $\mathcal{L} \subset \mathcal{V}$ satisfying a transversality condition: $\nabla_q(\mathcal{L}) \not\subset \mathcal{L} \otimes \Omega^1_q$. This geometric data is equivalent to a $q$-deformed Sturm--Liouville operator $\partial_q^2 + t(z)$, where $t(z) \in H^0(X, \Omega_q^{\otimes 2})$. This operator provides the rigid spectral data dual to $q$-Hecke eigensheaves.

We generalize this to arbitrary groups. Let $\check{G}_q$ be the $q$-Langlands dual group ([q-Langlands dual](#def:q-langlands-dual)) and let $\check{\mathfrak{b}}_q \subset \check{\mathfrak{g}}_q$ be a Borel subalgebra. A **$q$-oper** on $X$ is a $q$-flat connection ([q-flat connection](#def:q-flat-connection))

$$
  (\mathcal{P}_{\check{G}_q}, \nabla_q)
$$

on a $\check{G}_q$-bundle $\mathcal{P}_{\check{G}_q} \to X$, equipped with a $\check{B}_q$-reduction $\mathcal{P}_{\check{B}_q} \subset \mathcal{P}_{\check{G}_q}$. This data must satisfy the **$q$-oper condition**: the $q$-connection $\nabla_q$ is strictly transverse to the Borel reduction. Specifically, for each simple root $\alpha_i$ of $\check{G}_q$, the component of $\nabla_q$ along $\check{\mathfrak{g}}_{-\alpha_i}$ must not vanish:

$$
  \mathrm{pr}_{-\alpha_i}(\nabla_q \bmod \check{\mathfrak{b}}_q)
  \neq 0.
$$

We denote the moduli stack of $q$-opers by $\mathrm{Op}_{\check{G}_q}(X)$.
<!-- FILE_END: q-oper.md -->

<!-- FILE_START: q-oper-hecke.md -->
We explicitly construct $q$-Hecke eigensheaves from $q$-opers. Every $q$-oper $(\mathcal{P}_{\check{G}_q}, \nabla_q) \in \mathrm{Op}_{\check{G}_q}(X)$ defines a point $\nabla_q \in \mathrm{LocSys}_{\check{G}_q}(X)$. The $q$-Geometric Langlands equivalence ([$q$-GL conjecture](#conj:q-geometric-langlands)) maps the corresponding skyscraper sheaf $\delta_{\nabla_q}$ to a $q$-Hecke eigensheaf $\mathcal{M}_{\nabla_q}$ on $\mathrm{Bun}_{G_q}(X)$:

$$
  \mathcal{M}_{\nabla_q} = \mathbb{L}_q^{-1}(\delta_{\nabla_q}).
$$

The eigenvalue $q$-local system is the $q$-oper connection itself. For each point $x \in X$ and dominant weight $\lambda$, the Hecke action yields

$$
  \mathbf{T}_{x,\lambda}^{(q)}(\mathcal{M}_{\nabla_q})
  \simeq
  \mathcal{M}_{\nabla_q} \otimes
  V_\lambda^{(q)}(\nabla_q)_x.
$$

The transversality condition defining the $q$-oper ensures that $\mathcal{M}_{\nabla_q}$ is irreducible as a $q$-$\mathcal{D}$-module. Transversality to the Borel subgroup prevents the existence of non-trivial sub-$q$-$\mathcal{D}$-modules.
<!-- FILE_END: q-oper-hecke.md -->

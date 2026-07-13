<!-- FILE_START: q-gl-conjecture-intro.md -->
We state the central conjecture and its supporting structure. We define the $q$-Langlands dual group $\check{G}_q$, absorbing the substrate parameter into the spectral side. We then state the $q$-Geometric Langlands correspondence: an equivalence between $q$-$\mathcal{D}$-modules on $\mathrm{Bun}_{G_q}$ and quasi-coherent sheaves on $\mathrm{LocSys}_{\check{G}_q}$ over the non-torsion locus $\mathbb{G}_m^{\mathrm{nt}}$. The obstruction classes $\kappa_n \in H^2(\mathcal{S}, \mathbb{G}_m)$ measure the failure of $d_q^2 = 0$ and calibrate this conjecture. 

The Kummer filtration on $q$-local systems interprets the reduction $\kappa_0 \bmod n$ as a lifting obstruction, pinning the correspondence to the locus where $[n]_q \neq 0$. Finally, the rigid fibre functor $\tau$ implements the equivalence via Tannaka–Krein reconstruction.
<!-- FILE_END: q-gl-conjecture-intro.md -->

<!-- FILE_START: q-langlands-dual.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with quantum gauge group $G_q$ ([quantum gauge group](#def:quantum-gauge-group)). The **$q$-Langlands dual group** $\check{G}_q$ relates to $G_q$ by root system duality:

$$
  \check{G}_q = G_{q^{-1}}^{\vee}.
$$

Here, $(-)^\vee$ denotes the classical Langlands dual. The parameter $q$ maps to $q^{-1}$. For $G_q = \mathrm{SU}_q(2)$ ([quantum $\mathrm{SU}(2)$](#def:quantum-su2)), this yields:

$$
  \check{G}_q = \mathrm{SU}_{q^{-1}}(2) \cong \mathrm{SO}_{q^{-1}}(3).
$$

The root system of $\mathrm{SU}(2)$ is self-dual. The inversion $q \mapsto q^{-1}$ interchanges the two eigenvalues of the braiding: $q \leftrightarrow -q^{-1}$. This exchanges the symmetric and antisymmetric channels of the Iwahori--Hecke algebra. It represents the categorical manifestation of exchanging roots and coroots. In the $\mathbb{G}_m$-family picture, the Langlands involution is the inversion automorphism $\iota(q) = q^{-1}$. This preserves the torsion subgroups $\mu_n$ and acts as the identity on $\mu_2$.
<!-- FILE_END: q-langlands-dual.md -->

<!-- FILE_START: q-gl-conjecture.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe. Let $X$ be its brane curve, $G_q$ its quantum gauge group, and $\check{G}_q$ its $q$-Langlands dual ([q-Langlands dual](#def:q-langlands-dual)). The **$q$-Geometric Langlands correspondence** asserts an equivalence of $\infty$-categories:

$$
  \mathbb{L}_q \colon
  \mathcal{D}_q\text{-}\mathrm{mod}(\mathrm{Bun}_{G_q}(X))
  \xrightarrow{ \sim }
  \mathrm{QCoh}(\mathrm{LocSys}_{\check{G}_q}(X)).
$$

This equivalence is parametrised by the non-torsion locus $q \in \mathbb{G}_m^{\mathrm{nt}}(k)$ and satisfies five properties:

1. **Hecke compatibility**: For every $q$-Hecke operator $\mathbf{T}_{x,\lambda}^{(q)}$ ([q-Hecke operator](#def:q-hecke-operator)), $\mathbb{L}_q$ intertwines the action on the left with the action of $V_\lambda^{(q)}$ on $\mathrm{LocSys}_{\check{G}_q}(X)$:
   $$
     \mathbb{L}_q \circ \mathbf{T}_{x,\lambda}^{(q)}
     \simeq
     V_\lambda^{(q)}(-)_x \otimes \mathbb{L}_q.
   $$
2. **Fibre-functor factorisation**: Tannaka--Krein reconstruction determines $\mathbb{L}_q^{\mathrm{Tannakian}}$, and the equivalence factors through the fibre functor $\tau$:
   $$
     \mathbb{L}_q = \tau^* \circ \mathbb{L}_q^{\mathrm{Tannakian}}.
   $$
3. **$q$-Oper locus**: The equivalence $\mathbb{L}_q$ restricts to a bijection between $q$-opers ([q-oper](#def:q-oper)) and $q$-Hecke eigensheaves ([q-Hecke eigensheaf](#def:q-hecke-eigensheaf)):
   $$
     \mathrm{Op}_{\check{G}_q}(X)  \hookrightarrow 
     \mathrm{LocSys}_{\check{G}_q}(X)
     \quad\xrightarrow{\mathbb{L}_q^{-1}}\quad
     \{\text{$q$-Hecke eigensheaves}\}.
   $$
4. **Kummer constraint**: The equivalence $\mathbb{L}_q$ forms a well-defined $\mathbb{G}_m$-family on $\mathbb{G}_m^{\mathrm{nt}}$. At roots of unity $q \in \mu_n$, the quantum dimension $[n]_q = 0$ vanishes, the Frobenius pairing degenerates, and $\mathbb{L}_q$ breaks down. The obstruction ([Kummer filtration](#rem:kummer-filtration-obstruction)) persists at all Kummer levels $n \nmid \chi(A)$.
5. **Classical limit**: As $q \to 1$, $\mathbb{L}_q$ recovers the classical Geometric Langlands equivalence ([classical limit](#conj:q-gl-classical-limit)).
<!-- FILE_END: q-gl-conjecture.md -->

<!-- FILE_START: q-gl-obstruction-calc.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with $\chi(A) \neq 0$ and obstruction class $\kappa_0 = e(\xi) \in H^2(\mathcal{S}, \mathbb{G}_m)$ ([quantum characteristic classes](#def:quantum-characteristic-classes)).

1. The **intrinsic $q$-curvature** of a $q$-flat connection $\nabla_q$ on a $G_q$-bundle over $X$ is
   $$
     \mathcal{F}_q^{\mathrm{intr}}
     = 
     \mathrm{HKR}^{-1}(\kappa_0)
      \in 
     HH^2(\mathcal{U}_q, \mathrm{Ad}).
   $$
   This curvature is non-zero whenever $\kappa_0 \neq 0$. The non-vanishing of $d_q^2$ forces $q$-flat connections to carry intrinsic curvature.
2. A $q$-connection $\nabla_q$ is $q$-flat ([q-flat connection](#def:q-flat-connection)) when its connection-dependent curvature $\mathcal{F}_q^{\mathrm{conn}}$ vanishes. Lifting $q$-flat connections through the brane tower requires $\kappa_0 \equiv 0 \pmod n$ at the target level.
3. At Kummer level $n$, the obstruction $\kappa_0 \bmod n$ vanishes if and only if $n \mid \chi(A)$. Thus, $q$-flat $G_q$-connections lift to level $n$ only when $n$ divides $|\chi(A)|$.
4. For $\chi(A) \neq 0$, the condition $\kappa_0 \not\equiv 0 \pmod n$ holds at a density-$1$ set of Kummer levels $n \in \mathbb{Z}_{>0}$. The obstruction persists perpetually. The $q$-local systems exist as objects with intrinsic curvature, but their brane tower lifts are obstructed at cofinitely many levels.
<!-- FILE_END: q-gl-obstruction-calc.md -->

<!-- FILE_START: q-gl-kummer-filtration.md -->
The Kummer tower $\mu_1 \subset \mu_2 \subset \cdots \subset \mu_\infty \subset \mathbb{G}_m$ ([Kummer filtration](#rem:kummer-filtration-obstruction)) induces a descending filtration on the moduli of $q$-local systems. For each $n \geq 1$, we define the **level-$n$ sublocus**:

$$
  \mathrm{LocSys}_{\check{G}_q}^{(n)}(X)
  \subset
  \mathrm{LocSys}_{\check{G}_q}(X).
$$

This sublocus consists of $q$-local systems $\mathcal{L}_q$ whose $q$-monodromy $\Omega_q(\varrho)$ ([q-local system](#def:q-local-system)) is $n$-divisible in $\mathrm{End}(\tau(\mathcal{L}_q))$ for every contractible $\varrho$.

1. $\mathrm{LocSys}_{\check{G}_q}^{(1)}(X) = \mathrm{LocSys}_{\check{G}_q}(X)$ (all $q$-local systems).
2. The $q$-GL equivalence $\mathbb{L}_q$ ([$q$-GL conjecture](#conj:q-geometric-langlands)) restricts to each filtered piece:
   $$
     \mathbb{L}_q^{(n)} \colon
     \mathcal{D}_q^{(n)}\text{-}\mathrm{mod}(\mathrm{Bun}_{G_q})
     \xrightarrow{ \sim }
     \mathrm{QCoh}(\mathrm{LocSys}_{\check{G}_q}^{(n)}(X)).
   $$
   Here, $\mathcal{D}_q^{(n)}$ consists of $q$-$\mathcal{D}$-modules whose Hecke eigenvalues have $n$-divisible monodromy.
3. The sublocus $\mathrm{LocSys}_{\check{G}_q}^{(n)}$ admits lifts through the brane tower only when $n \mid \chi(A)$ ([obstruction calculation](#prop:q-gl-obstruction-calc)). At levels $n \nmid \chi(A)$, the perpetual obstruction prevents full lifting.
4. The $q$-GL equivalence $\mathbb{L}_q$ is well-defined as a $\mathbb{G}_m$-family on $\mathbb{G}_m^{\mathrm{nt}} = \mathbb{G}_m \setminus \mu_\infty$. The correspondence is intrinsically a non-torsion phenomenon.
<!-- FILE_END: q-gl-kummer-filtration.md -->

<!-- FILE_START: q-gl-fiber-functor.md -->
Assume the [$q$-Geometric Langlands conjecture](#conj:q-geometric-langlands). The fibre functor $\tau$ of the QOU determines the equivalence $\mathbb{L}_q$ uniquely up to natural isomorphism:

$$
  \mathbb{L}_q(\mathcal{M})(\mathcal{L}_q)
  \simeq
  \mathrm{Hom}_{\mathbf{Rep}(\check{G}_q)}
  \big(\tau(-),
  \mathrm{Hecke}_q(\mathcal{M}, \mathcal{L}_q)\big).
$$

Here, $\mathrm{Hecke}_q(\mathcal{M}, \mathcal{L}_q)$ is the tensor functor $V_\lambda^{(q)} \mapsto \mathbf{T}_{x,\lambda}^{(q)}(\mathcal{M}) \otimes \mathcal{L}_q(V_\lambda^{(q)})_x^*$. This functor encodes all Hecke eigenvalue data simultaneously. The rigidity of $\tau$ ([fibre-functor rigidity](#rem:fibre-functor-rigidity)) forces the uniqueness of $\mathbb{L}_q$. A unique natural isomorphism connects any two equivalences compatible with both the Hecke eigensheaf structure and the fibre functor.
<!-- FILE_END: q-gl-fiber-functor.md -->


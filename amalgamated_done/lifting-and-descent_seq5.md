<!-- FILE_START: direct-limit-intro.md -->
The brane tower carries a coherent QOU structure at every level. The categorical lifting machinery ensures these levels assemble seamlessly. We now pass to the colimit and study the emergent algebra.

We define the direct limit algebra $\mathcal{A}_\infty = \varinjlim_n \mathrm{End}_{\mathbf{C}}(A_n)$. In the smooth case, this recovers $\varinjlim \Gamma(J^1\mathcal{S}_n, \mathrm{SU}_{q_n}(2))$. We interpret this colimit through three lenses: Lusztig's integral form, the profinite jet shell, and Yekutieli's twisted-deformation stack. We then identify the unique $G_q$-invariant vacuum state functional on $\mathcal{A}_\infty$. Twisted quantization glues the local algebras globally across the tower via the obstruction class. The admissible Gröbner-style ordering lifts to the colimit, providing the well-founded order essential for downstream sections.

We use this vacuum state and global gluing to define categorical mass in the *Mass in the Brane Tower* section.
<!-- FILE_END: direct-limit-intro.md -->

<!-- FILE_START: direct-limit-algebra.md -->
Let $(\mathbf{C}, A, \tau)$ be a [quantum observable universe](#def:quantum-observable-universe) with substrate parameter $q$ and [recursive brane tower](#def:recursive-brane-tower) $\{A_n\}_{n \geq 0}$. The **direct limit algebra** of the quantum observable universe is the colimit in the category of $R$-algebras:
$$
  \mathcal{A}_\infty
  = 
  \varinjlim_{n}
  \mathrm{End}_{\mathbf{C}}(A_n),
$$
taken over the tower of endomorphism algebras with transition maps induced by the canonical embeddings $A_n \hookrightarrow A_{n+1}$.

In the archimedean realisation ([$\mathbb{C}$-quantum observable universe](#ex:c-quantum-observable-universe)), applying the fibre functor $\tau$ yields $\mathcal{A}_\infty \cong \varinjlim\Gamma(J^1 \mathcal{S}_n, \mathrm{SU}_{q_n}(2))$.
<!-- FILE_END: direct-limit-algebra.md -->

<!-- FILE_START: direct-limit-algebra-su2.md -->
We construct the [direct limit algebra](#def:direct-limit-algebra) $A_\infty$ for $G = \mathrm{SU}(2)$ from the [brane tower for SU(2)](#ex:recursive-brane-tower-su2).

**The tower.** The recursive brane tower yields a sequence of jet-level endomorphism algebras:
$$
  \mathrm{End}(\mathcal{O}(\mathrm{SU}(2)))
   \hookrightarrow 
  \mathrm{End}(J^1\mathcal{O}(\mathrm{SU}(2)))
   \hookrightarrow 
  \mathrm{End}(J^2\mathcal{O}(\mathrm{SU}(2)))
   \hookrightarrow  \cdots
$$
Jet prolongation maps $\ell_n \colon \mathrm{End}(J^n\mathcal{O}(\mathrm{SU}(2))) \hookrightarrow \mathrm{End}(J^{n+1}\mathcal{O}(\mathrm{SU}(2)))$ connect the levels. At level $n$, the algebra is $(3 + 3n)$-dimensional: $3$ dimensions from $\mathfrak{su}(2)$ and $3n$ dimensions from the $n$-th order cotangent directions.

**The direct limit.** The direct limit algebra is:
$$
  A_\infty
  =  \varinjlim_n \mathrm{End}(J^n\mathcal{O}(\mathrm{SU}(2)))),
$$
the union of all finite-order jet endomorphisms. An element of $A_\infty$ acts on jets of some finite order.

**Identification with differential operators.** Every element of $A_\infty$ is a finite-order left-invariant differential operator on $\mathrm{SU}(2)$. The direct limit coincides with the algebra $\mathcal{D}(\mathrm{SU}(2))^{\mathrm{SU}(2)}$ of left-invariant differential operators. By the Poincaré–Birkhoff–Witt theorem, this is isomorphic to the universal enveloping algebra $U(\mathfrak{su}(2))$:
$$
  A_\infty  \cong  U(\mathfrak{su}(2))
   \cong  \mathbb{C}\langle e_1, e_2, e_3 \rangle
  \big/ \bigl(e_a e_b - e_b e_a - \epsilon_{abc} e_c\bigr).
$$

**Filtration.** The jet order induces a filtration $A_\infty^{(0)} \subset A_\infty^{(1)} \subset \cdots$ with $A_\infty^{(n)} = \mathrm{End}(J^n\mathcal{O}(\mathrm{SU}(2)))$. The associated graded algebra is the symmetric algebra $\mathrm{gr}(A_\infty) \cong \mathrm{Sym}(\mathfrak{su}(2)^*) \cong \mathbb{C}[x_1, x_2, x_3]$ of polynomial functions on $\mathfrak{su}(2)$.
<!-- FILE_END: direct-limit-algebra-su2.md -->

<!-- FILE_START: direct-limit-lusztig.md -->
We explicitly realise the algebra $\mathcal{A}_\infty$ ([direct limit algebra](#def:direct-limit-algebra)) as the Lusztig integral form of the quantised enveloping algebra $\mathcal{U}_q(\mathfrak{su}(2))$ \[lusztig1993]. At each level $n$, we obtain the fibre algebra $\mathrm{SU}_{q_n}(2)$ by specialising the $\mathbb{Z}[q,q^{-1}]$-form $\mathcal{U}^{\mathbb{Z}}_q(\mathfrak{su}(2))$ ([substrate parameter](#def:substrate-parameter)) along $q \mapsto q_n \in k^{\times}$. The direct limit inherits the divided power basis $(E^{(m)}, F^{(m)}, K^{\pm 1})$ from the integral form. This ensures that the quaternionic jet embedding ([quaternionic spectral resolvents](#def:quaternionic-spectral-resolvents)) remains robust under the arithmetic :refterm[descent]{#descent} to $M_0$. The $q$-deformed scaling function $\exp_q(r) - 1$ (equation [eq:q-exp](#eq:q-exp)) regulates the transition between the divided power bases of the space-like and time-like resolvents.

The Gröbner--Shirshov normal-form theorem applied to $\mathrm{Dist}(G)$ \[fred2005] guarantees the flatness of this specialisation: the divided-power basis remains a basis after $q \mapsto q_n$. In the $p$-adic setting, the ([Witt vector lift](#def:witt-vector-lift)) converts this algebraic flatness into a geometric statement. The formal group $\widehat{G}$ over $\mathbb{Z}_p$ reduces modulo $p$ to the commutative formal group $H$ over $\mathbb{F}_p$. The divided-power basis of $\mathrm{Dist}(\widehat{G})$ restricts to the PBW basis of $\mathrm{Dist}(H)$.
<!-- FILE_END: direct-limit-lusztig.md -->

<!-- FILE_START: jet-shell.md -->
In the limit $n \to \infty$, the infinite jet bundle $J^\infty E = \varprojlim J^k E$ becomes the *jet shell* of the universe. This pro-finite structure encodes all finite-level brane data. The algebra $\mathcal{A}_\infty$ ([direct limit algebra](#def:direct-limit-algebra)) acts on sections of the jet shell.
<!-- FILE_END: jet-shell.md -->

<!-- FILE_START: stack-like-structure.md -->
The direct limit algebra $\mathcal{A}_\infty$ ([direct limit algebra](#def:direct-limit-algebra)) is a global "stack-like" version of the local $\mathrm{SU}_q(2)$ deformations. At each point $p \in M$, the fibre algebra $\mathcal{O}_{q(p)}(\mathrm{SU}(2))$ defines a local twisted deformation \cite{yekutieli2008}. The direct limit assembles these into a global object on the jet shell $J^\infty E$ ([jet shell](#rem:jet-shell)).
<!-- FILE_END: stack-like-structure.md -->

<!-- FILE_START: vacuum-state.md -->
Let $(\mathbf{C}, A, \tau)$ be a [quantum observable universe](#def:quantum-observable-universe). Let $q$ denote the substrate parameter. Let $\mathcal{A}_\infty$ be its [direct limit algebra](#def:direct-limit-algebra). Let $G_q = \mathrm{Aut}^{\otimes}(\tau)$ be the [quantum gauge group](#def:quantum-gauge-group), acting on $\mathcal{A}_\infty$ by conjugation. There exists a unique $R$-linear functional $\varphi \colon \mathcal{A}_\infty \to R$ that is $G_q$-invariant:
$$
  \varphi(g \cdot a) = \varphi(a)
  \quad\text{for all } g \in G_q,
  a \in \mathcal{A}_\infty.
$$
In the archimedean realisation, $G_q = \mathrm{SU}_q(2)$ and $\varphi$ is the unique $\mathrm{SU}(2)$-invariant state on the $C^*$-algebraic direct limit.
<!-- FILE_END: vacuum-state.md -->

<!-- FILE_START: vacuum-state-su2.md -->
We explicitly construct the [vacuum state](#prop:vacuum-state) $\varphi$ for the [direct limit algebra](#def:direct-limit-algebra) of $\mathrm{SU}(2)$. We replace the abstract direct-limit existence argument with a closed-form formula.

**Step 1: the Frobenius trace at finite level.** At level $n$ of the brane tower, the endomorphism algebra $\mathrm{End}(A_n)$ carries the Frobenius trace:
$$
  \mathrm{tr}_n(\alpha)
  = (\varepsilon \circ \alpha \circ \eta)(\mathbf{1}),
$$
where $\eta \colon \mathbb{C} \to A_n$ is the unit and $\varepsilon \colon A_n \to \mathbb{C}$ is the counit. For $A_n = \mathcal{O}(\mathrm{SU}(2))$ with its Peter–Weyl decomposition, this evaluates to:
$$
  \mathrm{tr}_n(f)
  = \sum_{j=0}^{n} (2j+1) \int_{\mathrm{SU}(2)}
    f(g)\,\overline{\chi_j(g)}\,dg
  \cdot \delta_{j,0}
  = \int_{\mathrm{SU}(2)} f(g)\,dg.
$$
The map $\mathrm{tr}_n$ is the Haar integral restricted to representations of spin $\leq n$.

**Step 2: the $q$-deformed Haar integral.** In the quantum group $\mathcal{O}_q(\mathrm{SU}(2))$, the Haar state $\varphi$ is the unique $\mathrm{SU}_q(2)$-invariant linear functional normalised by $\varphi(1) = 1$. Its action on the matrix coefficients $t^j_{m,m'}$ is:
$$
  \varphi(t^j_{m,m'}) = \delta_{j,0}\,\delta_{m,0}\,\delta_{m',0}.
$$
On products, we compute the Haar state via the Woronowicz--Peter--Weyl orthogonality:
$$
  \varphi\bigl((t^j_{m,n})^* \cdot t^{j'}_{m',n'}\bigr)
  = \frac{\delta_{jj'}\,\delta_{mm'}\,\delta_{nn'}}{[2j+1]_q},
$$
where $[k]_q = (q^k - q^{-k})/(q - q^{-1})$ is the quantum integer.

**Step 3: uniqueness verification.** Any $G_q$-invariant functional $\psi$ satisfies $\psi \circ \mathrm{Ad}(g) = \psi$ for all $g \in G_q$. By the quantum Schur lemma, $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ (the adjoint $V_1$ contains no trivial summand). The $G_q$-fixed subalgebra of $\mathcal{A}_\infty$ is $\mathbb{C}$. Normalising $\psi(1) = 1$ forces $\psi = \varphi$. $\square$

**Convergence rate.** The Frobenius traces $\mathrm{tr}_n$ converge to $\varphi$ exponentially. For $f \in A_n$ with spin content $\leq J$:
$$
  |\mathrm{tr}_n(f) - \varphi(f)| = 0
  \quad\text{for all } n \geq J.
$$
The convergence is exact after finitely many steps. The discrete Peter–Weyl decomposition eliminates the need for an $\epsilon$-$\delta$ argument.

**Bring's surface specialisation.** On Bring's QOU at the specific substrate parameter $q_0$ (recorded in the archimedean witness ledger), the Haar state evaluates to:
$$
  \varphi(t^j_{m,m'})
  = \frac{\delta_{j,0}\,\delta_{m,0}\,\delta_{m',0}}{1},
  \qquad
  [2j+1]_{q_0}
  = \frac{q_0^{2j+1} - q_0^{-(2j+1)}}{q_0 - q_0^{-1}}.
$$
For $j = \frac{1}{2}$, we have $[2]_{q_0} = q_0 + q_0^{-1} \approx 2.012$. For $j = 1$, we have $[3]_{q_0} = q_0^2 + 1 + q_0^{-2} \approx 3.041$. These quantum dimensions determine the normalisation of the vacuum state at each spin level.
<!-- FILE_END: vacuum-state-su2.md -->

<!-- FILE_START: global-gluing.md -->
Let $(\mathbf{C}, A, \tau)$ be a [quantum observable universe](#def:quantum-observable-universe) with substrate parameter $q$. The local deformations of the Frobenius–Hopf object $A$ induce a twisted associative deformation. This admits a unique global gluing via Yekutieli's twisted quantization map \cite{yekutieli2008, yekutieli2010}. The direct limit algebra $\mathcal{A}_\infty$ ([direct limit algebra](#def:direct-limit-algebra)) forms a well-defined global section of a sheaf of twisted deformation algebras on the underlying site $\mathcal{S}$. The [vacuum state](#prop:vacuum-state) is well-defined globally despite local non-commutativity. In the archimedean realisation, this manifests as the global gluing of the local algebras $\mathcal{O}_{q(p)}(\mathrm{SU}(2))$ over the manifold $M$.
<!-- FILE_END: global-gluing.md -->

<!-- FILE_START: ordering-jet-compatibility.md -->
**Proposition.**
*Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with braiding-induced ordering $\prec_c$ on the Hecke basis of $A$ ([temporal braiding](#def:quantum-observable-universe), axiom 5). Let $A_0 = A \hookrightarrow A_1 \hookrightarrow A_2 \hookrightarrow \cdots$ be the recursive brane tower ([recursive brane tower](#def:recursive-brane-tower)), with $A_{n+1} = J^1(A_n)$ ([jet prolongation](#prop:jet-prolongation)). We have:*

1. **(Extension.)** *At each level $n$, the jet prolongation $\ell_n \colon A_n \hookrightarrow A_{n+1}$ induces an admissible ordering $\prec_{n+1}$ on the Hecke basis of $A_{n+1}$. This extends $\prec_n$: if $a, b \in A_n$ and $a \prec_n b$, then $\ell_n(a) \prec_{n+1} \ell_n(b)$.*

2. **(Compatibility with multiplication.)** *The ordering $\prec_{n+1}$ satisfies left and right compatibility. If $a \prec_{n+1} b$, then $c \cdot a \prec_{n+1} c \cdot b$ and $a \cdot d \prec_{n+1} b \cdot d$ for all $c, d \in A_{n+1}$ ([admissible system](#unital-groebner-bases:def:admissible-system)).*

3. **(Well-foundedness.)** *Each $\prec_n$ is well-founded. There are no infinite descending chains in the Hecke basis of $A_n$.*

4. **(Direct limit.)** *The direct limit algebra $\mathcal{A}_\infty = \varinjlim \mathrm{End}(A_n)$ ([direct limit algebra](#def:direct-limit-algebra)) carries a filtered admissible ordering $\prec_\infty = \bigcup_n \prec_n$. Every element $a \in \mathcal{A}_\infty$ has a well-defined leading monomial $\mathrm{LM}(a)$ with respect to $\prec_\infty$. The Gröbner--Shirshov reduction algorithm terminates on every element of $\mathcal{A}_\infty$ that belongs to a finite level $A_n$.*
<!-- FILE_END: ordering-jet-compatibility.md -->

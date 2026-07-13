<!-- FILE_START: qu-consequences-intro.md -->
We now read off the consequences of the QU axioms and the Frobenius pairing. In $\mathrm{SU}(2)$, the coordinate ring $\mathcal{O}(\mathrm{SU}(2))$ carries a comultiplication built from the group-multiplication rule. The involution is the conjugate-transpose adjoint on $\mathbf{Rep}(\mathrm{SU}(2))$. These structures are categorical; they follow directly from the Frobenius pairing.

First, the Frobenius relation. The comultiplication $\Delta_\mu$ dual to $\mu$ under the Frobenius pairing satisfies $(\mu \otimes \mathrm{id}) \circ (\mathrm{id} \otimes \Delta_\mu) = \Delta_\mu \circ \mu$. The $\mathrm{SU}(2)$ picture verifies this identity on $\mathcal{O}(\mathrm{SU}(2))$. Second, the involutive $\ast$-structure: a contravariant endofunctor $\dagger$ assembled from the antipode and the Frobenius form. Its positivity—where $f^{\dagger} \circ f$ is positive in $\mathrm{End}(\mathbf{1})$—is the categorical analogue of the $C^*$-axiom.

Three observations place these results in context. The symbols $\dagger$, $\ast$, and the physicist's adjoint denote distinct structures. Tannaka--Krein duality lets the fibre functor $\tau$ reconstruct the group itself. Finally, the QU axioms are independent over arbitrary rings.
<!-- FILE_END: qu-consequences-intro.md -->

<!-- FILE_START: frobenius-relation.md -->
Let $(\mathbf{C}, A, \tau)$ be a [quantum universe](#def:quantum-universe). Denote by $\Delta_\mu$ the comultiplication on $A$ dual to $\mu$ under the [Frobenius pairing](#def:frobenius-pairing). This compatibility makes $A$ a Frobenius algebra. The *Frobenius relation* holds:

```tex
\begin{equation}\label{eq:frobenius-relation}
\begin{gathered}
\begin{tikzcd}[row sep=2.5em, column sep=3.5em]
  A \otimes A
    \ar[r, "\mathrm{id} \otimes \Delta_\mu"]
    \ar[d, "\mu"']
  & A \otimes A \otimes A
    \ar[d, "\mu \otimes \mathrm{id}"]
  \\
  A \ar[r, "\Delta_\mu"']
  & A \otimes A
\end{tikzcd}
\\[-0.5em]
\text{\small Frobenius relation: } (\mu \otimes \mathrm{id}) \circ (\mathrm{id} \otimes \Delta_\mu) = \Delta_\mu \circ \mu
\end{gathered}
\end{equation}
```

Sliding a multiplication past a comultiplication yields the same result as composing them.
<!-- FILE_END: frobenius-relation.md -->

<!-- FILE_START: frobenius-relation-su2.md -->
We verify the [Frobenius relation](#prop:frobenius-relation) for $A = \mathcal{O}(\mathrm{SU}(2))$.

**Setup.** $A$ carries pointwise multiplication $\mu(f \otimes g) = f \cdot g$ and comultiplication $\Delta(f)(x, y) = f(xy)$.

**Concrete verification.** Evaluate both sides of $(\mu \otimes \mathrm{id}) \circ (\mathrm{id} \otimes \Delta) = \Delta \circ \mu$ on $f, h \in A$ at $(x, y, z)$.

- **Left side.** $(\mathrm{id} \otimes \Delta)(f \otimes h)(x, y, z) = f(x) h(yz)$. Applying $\mu \otimes \mathrm{id}$ gives $(f \cdot h_1)(x) h_2(z)$, where $\Delta(h) = \sum h_1 \otimes h_2$.
- **Right side.** $\Delta(\mu(f \otimes h))(x, z) = f(xz) h(xz)$.

Both sides evaluate to $f(xz) h(xz)$ because $\sum h_1(x) h_2(z) = h(xz)$.

**Interpretation.** Multiplying two functions and decomposing the product gives the same result as decomposing one function and then multiplying. The pointwise multiplication of functions is compatible with composing group elements.
<!-- FILE_END: frobenius-relation-su2.md -->

<!-- FILE_START: involutive-structure.md -->
Let $(\mathbf{C}, \otimes, \mathbf{1})$ be an $R$-linear rigid monoidal category. An **involutive structure** on $\mathbf{C}$ is a contravariant endofunctor $\dagger \colon \mathbf{C}^{\mathrm{op}} \to \mathbf{C}$ satisfying:

1. **Identity on objects:** $X^{\dagger} = X$.
2. **Involutivity:** $f^{\dagger\dagger} = f$:

   ```tex
   \begin{equation}\label{eq:involutivity-cd}
   \begin{tikzcd}[column sep=5em]
     X \ar[r, bend left=30, "f = f^{\dagger\dagger}"]
     & Y \ar[l, bend left=30, "f^{\dagger}"]
   \end{tikzcd}
   \end{equation}
   ```

3. **Monoidal compatibility:** $(\mathrm{id}_X \otimes f)^{\dagger} = \mathrm{id}_X \otimes f^{\dagger}$:

   ```tex
   \begin{equation}\label{eq:monoidal-dagger-cd}
   \begin{tikzcd}[row sep=2.5em, column sep=3em]
     X \otimes Y \ar[r, "\mathrm{id} \otimes f"]
       \ar[d, "(\mathrm{id} \otimes f)^{\dagger}"']
     & X \otimes Z \ar[d, "\mathrm{id} \otimes f^{\dagger}"] \\
     X \otimes Z \ar[r, equal]
     & X \otimes Z
   \end{tikzcd}
   \end{equation}
   ```

4. **Contravariance:** $(g \circ f)^{\dagger} = f^{\dagger} \circ g^{\dagger}$:

   ```tex
   \begin{equation}\label{eq:dagger-contravariance}
   \begin{tikzcd}[column sep=3em]
     X \ar[r, "f"] & Y \ar[r, "g"] & Z
   \end{tikzcd}
   \quad\xmapsto{\dagger}\quad
   \begin{tikzcd}[column sep=3em]
     Z \ar[r, "g^{\dagger}"] & Y \ar[r, "f^{\dagger}"] & X
   \end{tikzcd}
   \end{equation}
   ```

For the Hopf algebra $A$ in a quantum universe, the antipode $S$ provides an involutive structure via $f^{\dagger} = \int_A \circ \mu(S(f) \otimes -)$.
<!-- FILE_END: involutive-structure.md -->

<!-- FILE_START: positive-definite-dagger.md -->
A positive-definite dagger gives categorical states genuine squared lengths. Let $(\mathbf{C}, A)$ be a [quantum universe](#def:quantum-universe) whose endomorphism ring $\mathrm{End}(\mathbf{1}) \cong R$ is a formally-real ordered field. Assume a [Frobenius pairing](#def:frobenius-pairing) and a pivotal antipode $S$ that is self-adjoint for the pairing.

Define the *Frobenius dagger* on morphisms by:

$$
  f^{\dagger} =  \int_A \circ\, \mu(S(f) \otimes -).
$$

The Frobenius dagger satisfies $S^2 = \mathrm{id}$ and restricts to $S = \dagger$ on $\mathrm{End}(\mathbf{1})$. The functor $\dagger$ is a positive-definite [involutive structure](#def:involutive-structure). For every non-zero morphism $f \colon \mathbf{1} \to X$, the composite $f^{\dagger} \circ f$ is a positive element of $R$.
<!-- FILE_END: positive-definite-dagger.md -->

<!-- FILE_START: positive-dagger-su2.md -->
We verify [positive-definiteness](#prop:positive-definite-dagger) in $\mathbf{Rep}(\mathrm{SU}(2))$.

**The dagger involution.** On $\mathbf{Rep}(\mathrm{SU}(2))$, the dagger sends $f \colon V \to W$ to its conjugate transpose $f^\dagger = \bar{f}^{T} \colon W \to V$.

**Positive-definiteness on $V = \mathbb{C}^2$.** The fundamental representation $V = \mathbb{C}^2$ carries the standard Hermitian inner product $\langle v, w \rangle = v^\dagger w$. The $\mathrm{SU}(2)$-action preserves this inner product.

For any endomorphism $f \colon V \to V$, the composite $f^\dagger f$ satisfies:

$$
\langle f^\dagger f  v, v \rangle = \| f v \|^2 \geq 0.
$$

Thus $f^\dagger f$ has real non-negative eigenvalues. By Schur's lemma, $f = \lambda \mathrm{id}$, forcing $f^\dagger f = |\lambda|^2 \mathrm{id}$. 

**Interpretation.** Positive-definiteness makes $\mathbf{Rep}(\mathrm{SU}(2))$ a $C^*$-tensor category. This is the categorical shadow of the compactness of $\mathrm{SU}(2)$.
<!-- FILE_END: positive-dagger-su2.md -->

<!-- FILE_START: dagger-notation.md -->
Three notations for "adjoint" coexist:

- $f^{\dagger}$ denotes the **Frobenius adjoint**: the involution derived from the Frobenius pairing. This is the categorical structure.
- $f^{\ast}$ denotes **complex conjugation**. On $\mathcal{O}(G)$, it acts as $f^{\ast}(g) = \overline{f(g)}$.
- $A^{\dagger}_{\mathrm{phys}}$ denotes the **physicist's adjoint** on a Hilbert space.

In the categorical setting, only $\dagger$ is defined.
<!-- FILE_END: dagger-notation.md -->

<!-- FILE_START: tannaka-krein-overview.md -->
Tannaka--Krein duality recovers the gauge group from the fibre functor $\tau$. It comprises four statements:

1. **Reconstruction.** The group $G$ emerges from $\tau$: $G \cong \mathrm{Aut}^{\otimes}(\tau)$.
2. **Equivalence.** The functor $\tau$ establishes a monoidal equivalence $\mathbf{C} \simeq \mathrm{Rep}(G)$.
3. **Rigidity.** Any two fibre functors are isomorphic, reconstructing the same group up to inner automorphism.
4. **Constraint propagation.** Algebraic conditions on $\tau$ propagate to $G$. The volume constraint cuts the automorphism group from $\mathrm{GL}$ down to $\mathrm{SL}$.

**Origin of $q$.** The deformation parameter $q$ is not imposed. When the braiding $c_{V,V}$ is non-symmetric, $q$ is the eigenvalue of $c_{V,V}$ on $S^2 V$. Woronowicz's reconstruction recovers $\mathrm{SU}_q(2)$ with this categorically determined $q$.
<!-- FILE_END: tannaka-krein-overview.md -->

<!-- FILE_START: axiom-independence.md -->
Are the four axioms of a quantum universe independent?

**Axioms 1 and 3.** Over a characteristic-zero field, Deligne's theorem shows every symmetric :refterm[monoidal category]{#monoidal-category} admits a fibre functor. However, we require only braided structure over a commutative ring. Axiom 3 is independent.

**Axiom 2.** A general Hopf algebra need not carry a non-degenerate Frobenius form. The Frobenius condition $A \cong A^{\vee}$ is strictly stronger than the Hopf axioms.

**Axiom 4.** For smooth algebraic groups, Kähler differentials exist automatically. For quantum groups ($q \neq 1$), differential calculi need not exist or be unique. Axiom 4 is independent.

In full generality, all four axioms are independent.
<!-- FILE_END: axiom-independence.md -->

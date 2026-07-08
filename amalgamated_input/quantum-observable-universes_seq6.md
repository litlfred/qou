<!-- FILE_START: vectors-hadrons-intro.md -->
Having established the weight decomposition of forms, we now develop the trace and basis machinery for intertwiner spaces of tensor powers of the fundamental representation. We introduce the adjoint trace on endomorphisms, derived from the Frobenius pairing and the fibre-adjoint involution. This trace inherits cyclicity from the Frobenius relation and non-degeneracy from the positive-definiteness of the dagger. Next, we construct the Pawlowski--Leitner canonical basis on $\mathrm{Hom}_{\mathrm{SU}(2)}(V_j, V_{1/2}^{\otimes n})$. Indexed by standard Young tableaux with at most two rows, this basis emerges from contractions with the volume form along the unital Gröbner--Shirshov route, its dimension governed by the hook-length formula. Finally, we use the adjoint trace to equip the PawLei basis with an orthogonal inner product. This pairing coincides with the Frobenius form restricted to $\mathrm{End}(V_j)$, ensuring that fibre integration commutes with the intertwiner expansion of hadron states.
<!-- FILE_END: vectors-hadrons-intro.md -->

<!-- FILE_START: adjoint-trace.md -->
The Frobenius pairing and the fibre-adjoint involution together equip every hom-space $\mathrm{Hom}_{\mathbf{C}}(X, Y)$ with a canonical sesquilinear form. We define the adjoint trace on endomorphisms of $V$ by

$$
  \mathrm{tr}_{\mathrm{Ad}}(f)
  = 
  \int_A \!\circ \mu \circ (f \otimes \mathrm{id}_{V^{\vee}})
    \circ \mathrm{coev}_V
   \in 
  \mathrm{Hom}(\mathbf{1}, \mathbf{1}) \cong R,
$$

where $\mathrm{coev}_V \colon \mathbf{1} \to V \otimes V^{\vee}$ is the coevaluation map and $\mu$ is the Frobenius multiplication.

This trace is cyclic, $\mathrm{tr}_{\mathrm{Ad}}(f \circ g) = \mathrm{tr}_{\mathrm{Ad}}(g \circ f)$, inherited directly from the Frobenius relation. It is also non-degenerate, as the induced pairing $\langle f, g \rangle_{\mathrm{Ad}} = \mathrm{tr}_{\mathrm{Ad}}(f^{\dagger} \circ g)$ inherits non-degeneracy from the Frobenius integral and positivity from the dagger structure. In the archimedean limit $G = \mathrm{SU}(2)$, the adjoint trace recovers the Killing form on $\mathfrak{su}(2)$: $\mathrm{tr}_{\mathrm{Ad}}(f) = \mathrm{tr}(\mathrm{ad}(f)) = -2\mathrm{tr}_{\mathbb{C}^2}(f)$.
<!-- FILE_END: adjoint-trace.md -->

<!-- FILE_START: pawlowski-leitner-basis.md -->
Let $V_{1/2} \cong \mathbb{C}^2$ be the fundamental representation of $G = \mathrm{SU}(2)$. For each simple object $V_j$ and tensor power $V_{1/2}^{\otimes n}$ with $n \geq 2j$, the intertwiner space $\mathrm{Hom}_{\mathrm{SU}(2)}\!\bigl(V_j, V_{1/2}^{\otimes n}\bigr)$ admits a canonical PawLei basis. This basis is indexed by standard Young tableaux of shape $\lambda \vdash n$ having at most two rows and satisfying $\lambda_1 - \lambda_2 = 2j$.

The construction relies on the PBW theorem over commutative rings: the unital Gröbner--Shirshov basis for $U(\mathfrak{su}(2))$ provides a monomial basis for the enveloping algebra. The intertwiner basis is then derived by contraction with the volume form.

```tex
\begin{equation}\label{eq:pawlei-basis-diagram}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  \mathbf{1} \ar[r, "\epsilon^{\vee}"]
  & \Lambda^2 V_{1/2} \ar[r, hook]
  & V_{1/2}^{\otimes n} \ar[r, "\pi_j"]
  & V_j
\end{tikzcd}
\end{equation}
```

The volume form $\epsilon \colon \Lambda^2 V_{1/2} \to \mathbf{1}$ and its dual $\epsilon^{\vee}$ act as contraction operators. Each PawLei basis element is formed by applying a tableau-specified sequence of contractions to the highest-weight vector $e_+^{\otimes (j+m)} \otimes e_-^{\otimes (j-m)}$, followed by row symmetrization.

The dimension of the intertwiner space follows the hook-length formula:

$$
  \dim\mathrm{Hom}_{\mathrm{SU}(2)}\!\bigl(V_j, V_{1/2}^{\otimes n}\bigr)
  = 
  \frac{(2j+1) n!}{(\tfrac{n}{2}+j+1)!(\tfrac{n}{2}-j)!}
$$

for $n \equiv 2j \pmod{2}$, and vanishes otherwise.
<!-- FILE_END: pawlowski-leitner-basis.md -->

<!-- FILE_START: pawlowski-leitner-inner-product.md -->
The adjoint trace induces an inner product on the intertwiner spaces. For $\phi, \psi \in \mathrm{Hom}_{\mathrm{SU}(2)}(V_j, V_{1/2}^{\otimes n})$, we define:

$$
  \langle \phi, \psi \rangle_{\mathrm{PL}}
  = 
  \mathrm{tr}_{\mathrm{Ad}}\!\bigl(\phi^{\dagger} \circ \psi\bigr)
  = 
  \int_A \!\circ \mu \circ (\phi^{\dagger} \circ \psi \otimes \mathrm{id}) \circ \mathrm{coev}_{V_j}.
$$

```tex
\begin{equation}\label{eq:pawlei-inner-product-diagram}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  \mathbf{1} \ar[r, "\mathrm{coev}_{V_j}"]
  & V_j \otimes V_j^{\vee}
    \ar[r, "\phi^{\dagger} \circ \psi \otimes \mathrm{id}"]
  & A \otimes V_j^{\vee}
    \ar[r, "\int_A \circ \mu"]
  & \mathbf{1}
\end{tikzcd}
\end{equation}
```

The PawLei basis $\{T_{\lambda}\}$ is strictly orthogonal under this pairing: $\langle T_{\lambda}, T_{\mu} \rangle_{\mathrm{PL}} = \delta_{\lambda\mu} \|T_{\lambda}\|^2$, where the squared norm is a positive rational computable directly from the hook lengths of $\lambda$.

This orthogonality guarantees two physical structures. First, any categorical hadron state of valence $n$ admits a unique, orthogonal expansion into partial-wave amplitudes. Second, the inner product coincides with the restriction of the Frobenius pairing to $\mathrm{End}(V_j) \subset A$. This compatibility ensures that integration over the gauge fibre commutes with the decomposition of physical states. This realization specializes to the archimedean limit, evaluating physical observables numerically at the substrate parameter $q_0$.
<!-- FILE_END: pawlowski-leitner-inner-product.md -->


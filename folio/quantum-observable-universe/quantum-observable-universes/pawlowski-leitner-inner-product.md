The adjoint trace induces an inner product on the intertwiner spaces. For $\phi, \psi \in \mathrm{Hom}_{\mathrm{SU}(2)}(V_j, V_{1/2}^{\otimes n})$, define:

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

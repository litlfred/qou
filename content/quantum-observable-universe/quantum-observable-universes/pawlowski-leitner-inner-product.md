The [adjoint trace](#rem:adjoint-trace) induces a canonical inner
product on intertwiner spaces. For
$\phi, \psi \in \mathrm{Hom}_{\mathrm{SU}(2)}(V_j, V_{1/2}^{\otimes n})$, define

$$
  \langle \phi, \psi \rangle_{\mathrm{PL}}
  = 
  \mathrm{tr}_{\mathrm{Ad}}\!\bigl(\phi^{\dagger} \circ \psi\bigr)
  = 
  \int_A \!\circ \mu \circ
    (\phi^{\dagger} \circ \psi \otimes \mathrm{id})
    \circ \mathrm{coev}_{V_j}.
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
\qquad\text{(PawLei inner product)}
\end{equation}
```

The [PawLei basis](#prop:pawlowski-leitner-basis)
$\{T_{\lambda}\}$ is *orthogonal* with respect to this pairing:

$$
  \langle T_{\lambda}, T_{\mu} \rangle_{\mathrm{PL}}
  = 
  \delta_{\lambda\mu} \|T_{\lambda}\|^2,
$$

where the norm-squared $\|T_{\lambda}\|^2$ is a positive rational
number computable from the hook lengths of the tableau $\lambda$.

This orthogonality has two consequences for the QOU framework:

1. **Decomposition of hadron states.** A
   [categorical hadron](#def:hadron) of valence $n$ can be
   uniquely expanded in the PawLei basis, with
   coefficients that are the partial-wave
   amplitudes.
2. **Compatibility with the Frobenius form.** The inner product
   $\langle{-},{-}\rangle_{\mathrm{PL}}$ agrees with the restriction
   of the [Frobenius pairing](#def:frobenius-pairing) to
   $\mathrm{End}(V_j) \subset A$, ensuring that integration over the
   fibre and decomposition into basis elements commute.

The algebraic foundations (PBW bases over commutative rings) are
established in \cite{leitnerpawloski2004}; norm formulas follow from
the Temperley--Lieb calculus and $6j$-symbols.

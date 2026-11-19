**Construction via pullback.** The Frobenius self-duality $A \xrightarrow{ \sim } A^{\vee}$ induces an identification $\Omega^1(A)^{\vee} \cong \Omega^1(A)$. Composing with the exterior square gives the *Poisson bivector object*

$$
\Pi  :=  \Lambda^2\bigl(\Omega^1(A)^{\vee}\bigr)
 \cong  \Lambda^2\bigl(\Omega^1(A)\bigr)
=  \Omega^2(A).
$$

A global section $\pi \colon \mathbf{1} \to \Pi$ defines a *Poisson bracket* on $A$ by the composite:

```tex
\begin{equation}\label{eq:poisson-bracket-pullback}
\begin{tikzcd}[row sep=1.5em, column sep=2.2em]
  A \otimes A
    \ar[r, "d \otimes d"]
  & \Omega^1(A) \otimes \Omega^1(A)
    \ar[r, "\wedge"]
  & \Omega^2(A)
    \ar[r, "\langle \pi{,} {-} \rangle"]
  & A
\end{tikzcd}
\end{equation}
```

Anti-symmetry $\{f, g\} = -\{g, f\}$ of the bracket of an internal Poisson object is automatic, because $\pi$ factors through the exterior square.

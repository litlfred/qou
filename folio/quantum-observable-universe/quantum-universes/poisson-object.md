Let $(\mathbf{C}, A, \tau)$ be a [quantum universe](#def:quantum-universe) with [Frobenius pairing](#def:frobenius-pairing) $\int_A \circ \mu \colon A \otimes A \to \mathbf{1}$ and [higher forms](#def:higher-forms) $\Omega^k(A)$. The quantum universe is equipped with an internal Poisson structure. 

An **internal Poisson object** on $A$ is a morphism

$$
\pi \colon \mathbf{1} \longrightarrow \Lambda^2\bigl(\Omega^1(A)^{\vee}\bigr)
$$

in $\mathbf{C}$ (a *bivector*). It contracts a pair of differentials to a scalar, defining the bracket $\{f, g\} := \langle \pi, df \wedge dg \rangle$ for $f, g \colon \mathbf{1} \to A$.

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

**Axioms.** The morphism $\pi$ must satisfy:

1. **Jacobi identity.** The Jacobiator vanishes: $\{f, \{g, h\}\} + \{g, \{h, f\}\} + \{h, \{f, g\}\} = 0$, equivalently $[\pi, \pi]_{\mathrm{SN}} = 0$.
2. **Leibniz rule.** $\{f, gh\} = \{f, g\}h + g\{f, h\}$, ensuring the bracket is a biderivation.

Anti-symmetry $\{f, g\} = -\{g, f\}$ is automatic because $\pi$ factors through the exterior square. The triple $(A, \mu, \pi)$ is a *Poisson algebra object* in $\mathbf{C}$.

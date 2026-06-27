Let $(\mathbf{C}, A, \tau)$ be a
[quantum universe](#def:quantum-universe) with
[Frobenius pairing](#def:frobenius-pairing)
$\int_A \circ \mu \colon A \otimes A \to \mathbf{1}$ and
[higher forms](#def:higher-forms) $\Omega^k(A)$.

An **internal Poisson object** on $A$ is a morphism

$$
\pi \colon \mathbf{1} \longrightarrow \Lambda^2\bigl(\Omega^1(A)^{\vee}\bigr)
$$

in $\mathbf{C}$ (a *bivector*), subject to the conditions below.

**Construction via pullback.**
The Frobenius self-duality $A \xrightarrow{ \sim } A^{\vee}$
induces an identification $\Omega^1(A)^{\vee} \cong \Omega^1(A)$
(dualising the bimodule of Kähler differentials through the
non-degenerate pairing).  Composing with the exterior square gives
the *Poisson bivector object*

$$
\Pi  :=  \Lambda^2\bigl(\Omega^1(A)^{\vee}\bigr)
 \cong  \Lambda^2\bigl(\Omega^1(A)\bigr)
=  \Omega^2(A).
$$

A global section $\pi \colon \mathbf{1} \to \Pi$ then defines a
*Poisson bracket* on $A$ by the composite

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

where $d$ is the universal derivation, $\wedge$ the exterior product,
and the contraction $\langle \pi, {-} \rangle$ is the pullback of
$\pi$ through the Frobenius isomorphism.  Explicitly,
$\{f, g\} := \langle \pi, df \wedge dg \rangle$ for
$f, g \colon \mathbf{1} \to A$.

**Axioms.** The morphism $\pi$ must satisfy:

1. **Jacobi identity.** The Jacobiator
   $\{f, \{g, h\}\} + \{g, \{h, f\}\} + \{h, \{f, g\}\} = 0$
   vanishes, equivalently the Schouten--Nijenhuis condition
   $[\pi, \pi]_{\mathrm{SN}} = 0$ on the bivector.

2. **Leibniz rule.** $\{f, gh\} = \{f, g\}h + g\{f, h\}$,
   ensuring the bracket is a biderivation with respect to the
   multiplication $\mu$ on $A$.

Anti-symmetry $\{f, g\} = -\{g, f\}$ is automatic: since $\pi$
factors through $\Lambda^2(\Omega^1(A)^{\vee})$ (the exterior
square, not the full tensor square), the bracket inherits the
anti-symmetry of the wedge product.

The triple $(A, \mu, \pi)$ is then a *Poisson algebra object* in
$\mathbf{C}$.

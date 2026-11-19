Let $(\mathbf{C}, A, \tau)$ be a [quantum universe](#def:quantum-universe) with [Frobenius pairing](#def:frobenius-pairing) $\int_A \circ \mu \colon A \otimes A \to \mathbf{1}$ and [higher forms](#def:higher-forms) $\Omega^k(A)$.

An **internal Poisson object** on $A$ is a morphism

$$
\pi \colon \mathbf{1} \longrightarrow \Lambda^2\bigl(\Omega^1(A)^{\vee}\bigr)
$$

in $\mathbf{C}$ (a *bivector*). It contracts a pair of differentials to a scalar, defining the bracket $\{f, g\} := \langle \pi, df \wedge dg \rangle$ for $f, g \colon \mathbf{1} \to A$.

**Axioms.** The morphism $\pi$ must satisfy:

1. **Jacobi identity.** The Jacobiator vanishes: $\{f, \{g, h\}\} + \{g, \{h, f\}\} + \{h, \{f, g\}\} = 0$, equivalently $[\pi, \pi]_{\mathrm{SN}} = 0$.
2. **Leibniz rule.** $\{f, gh\} = \{f, g\}h + g\{f, h\}$, ensuring the bracket is a biderivation.

The triple $(A, \mu, \pi)$ is a *Poisson algebra object* in $\mathbf{C}$.

The classical Bloch group $\mathcal{B}(\mathbb{C})$ is
defined by the five-term relation of the dilogarithm
$\mathrm{Li}_2$.  The **quantum Bloch group**
$\mathfrak{B}(q)(R)$ replaces this with the **pentagon
identity** of the quantum dilogarithm $\Phi_q$:

$$
  \Phi_q(u)\,\Phi_q(v)
  \;=\;
  \Phi_q(v)\,\Phi_q(uv)\,\Phi_q(u)
  \qquad \text{where } uv = qvu
$$

This identity is the **Yang–Baxter equation in
exponential form**.

The connection to the QOU framework — why $\Phi_1$ is a quantum
dilogarithm, the Kashaev invariant, and the pre-archimedean
refinement of $\mathfrak{B}(q)$ over the Habiro ring — is developed
in [the follow-on remark](#rem:quantum-bloch-group-framework-connection). A functorial setting for state-sum invariants built from quantum dilogarithms is quantum hyperbolic field theory: for each odd $N$ it assigns to a $3$-manifold with a framed tangle and a $PSL(2,\mathbb{C})$-character a tensor built from matrix dilogarithms \cite[\S1, \S2.1]{baseilhac-benedetti2007}.

**Branch ambiguity and the extended Bloch group (literature).** The ordinary Bloch group $\mathcal{B}(\mathbb{C})$ carries the single-valued Bloch–Wigner function, which recovers only the volume. The multivaluedness of $\mathrm{Li}_2$ is removed by passing to the extended Bloch group $\widehat{\mathcal{B}}(\mathbb{C})$ of Goette and Zickert, as surveyed in \cite[\S3]{arxiv-2304.12545v1}: generators are pairs $[u,v]$ with $e^u + e^v = 1$, the relations are a lifted version of the five-term relation, and the regulator $\sum_j [u_j,v_j] \mapsto \sum_j \bigl(L(v_j) + \tfrac12 u_j v_j - \tfrac{\pi^2}{6}\bigr)$, with $L(v) = \mathrm{Li}_2(1-e^v)$, is well defined modulo $4\pi^2$ on that relation. It is the extended group, not the ordinary one, on which a complex-valued dilogarithm invariant is single-valued. The survey is a secondary source: the lifted five-term relation is stated there without proof, and the primary papers of Goette and Zickert are not in the bibliography. Neumann's original construction is registered \cite[\S1]{neumann2004}. No Lean declaration in this corpus states the lifted relation; the Lean file on the extended-Bloch volume leg uses only the Bloch–Wigner function $D$, which lives on the ordinary group.

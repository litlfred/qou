An archimedean QOU $(\mathbf{C}, \varTheta, G, \mathcal{S})$ ([quantum observable universe](#def:quantum-observable-universe)) uses $K = \mathbb{R}$, a real Lie group $G$, and a real vector bundle $\mathcal{S}$. A surreal QOU uses $K = \mathbf{No}$ with all axioms relaxed to hold up to an infinitesimal $\varepsilon$:

| Axiom | Archimedean | Surreal |
|---|---|---|
| Frobenius pairing | $\int_A \circ \mu = \mathrm{id}$ | $= \mathrm{id} + O(\varepsilon)$ |
| Observability | $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ | $\leq \varepsilon$ |
| Volume | $g_{\mathbf{1}} = \mathrm{id}$ | $= (1 + \varepsilon) \mathrm{id}$ |
| Vacuum | $\mathrm{Geom}(\bigcirc) = 0$ | $= \varepsilon$ |

**Conjecture.** The standard-part map $\mathrm{St}$ sends every surreal QOU to an archimedean QOU.

More precisely, there is a functor $\mathrm{St}_{\mathrm{QOU}} : \mathbf{QOU}_{\mathbf{No}}^{\varepsilon} \longrightarrow \mathbf{QOU}_{\mathbb{R}}$ defined by applying $\mathrm{St}$ to all hom-spaces. The functor is essentially surjective, and the composition $\mathrm{St}_{\mathrm{QOU}} \circ \iota$ is the identity.

If the conjecture holds, the surreal lift carries strictly more information than the archimedean theory. Each archimedean QOU has a fibre of surreal QOUs above it. The additional information is infinitesimal physics: first-order quantum corrections to the Frobenius pairing, observability cohomology, volume normalisation, and vacuum. Whether such corrections are physical or only mathematical is open.

This conjecture is the categorical counterpart of [classical limit as standard-part](#conj:classical-limit-stpart). The two conjectures are likely equivalent modulo functoriality.

If true, the $\varepsilon$-relaxation is a strict generalisation of the main paper. The main paper's QOU axioms are recovered via $\mathrm{St}_{\mathrm{QOU}}$. Every theorem in the main paper has a surreal counterpart, potentially with non-trivial first-order corrections that vanish under $\mathrm{St}$.

The proof reduces to [classical-limit-stpart](#conj:classical-limit-stpart). First, show $\mathrm{St}_{\mathrm{QOU}} = (\mathrm{St}, \mathrm{St}, \mathrm{St}, \mathrm{St})$. Second, reduce each component: $\mathbf{C} = \mathrm{Rep}_{\mathbf{No}}(\mathrm{SU}_q(2))$ recovers $\mathrm{Rep}_{\mathbb{R}}(\mathrm{SU}(2))$, $\varTheta$ acts entry-wise, $G$ is the standard-part of an algebraic group object, and $\mathcal{S}$ is the standard-part of the fibre. Third, verify each $\varepsilon$-relaxed axiom becomes strict under $\mathrm{St}$. Finally, essential surjectivity is automatic by setting $\varepsilon = 0$. Falsification requires an $\varepsilon$-relaxed surreal QOU whose standard-part violates a strict QOU axiom.

# Unified Categorical Mass Formula: The Canonical Derivation

The QOU framework derives the mass of an atomic vortex $\varrho \colon \mathbf{1} \to A$ directly from the topological structure of its knot representative. Rather than relying on an additive phenomenological expansion (like the retracted six-term brane tower), the canonical derivation extracts the mass by evaluating the **Frobenius pairing** of the knot operator through a strict, categorical chain.

This document walks step-by-step through the canonical derivation chain — from the categorical action to the Frobenius pairing — to establish the unified mass formula.

## 1. Categorical Action
Let $\varrho$ be a vortex with topological braid representative $\beta \in B_n$. The foundational physics is encoded in how the braid group acts on the quantum tensor space $V^{\otimes n}$. This is captured by the R-matrix representation:
$$ \rho_n \colon B_n \to \mathrm{Aut}_{\mathbf{C}}(V^{\otimes n}) $$
This action is the origin of all topological confinement properties.

## 2. Non-Abelian Stokes & The Hecke Algebra
By the non-abelian Stokes theorem (Yekutieli), the curvature 2-form of this categorical action descends to the Iwahori-Hecke algebra $H_n(R, q)$. The braid crossings $\sigma_i$ are constrained by the Hecke quadratic relation:
$$ \sigma_i^2 = (q - q^{-1})\sigma_i + 1 $$
This algebra forms the mathematical substrate. All subsequent derivations operate strictly within $H_n(q)$ over $\mathbb{Q}(q)$, without empirical fitting.

## 3. Alexander–Markov Trace
By the theorems of Alexander and Markov, any knot $K$ formed by the closure of a braid $\beta$ admits a unique trace $\mathrm{tr}_M$ that is invariant under both braid moves and stabilization. This trace, $\mathrm{tr}_M \colon H_n(q) \to \mathbb{Q}(q)$, evaluates the knot operator $\mathcal{B}_K$ independent of its specific braid representation.

## 4. Bring Weight Identification & Particle Content
The specific subspace $H_3(q)$ has dimension 6, perfectly matching the 6 embeddable torus knots in $\Sigma_4$ (the Bring surface). This structural correspondence rigidly fixes the elementary particle content of the framework (e.g., the proton corresponds to the Borromean knot $\mathcal{B}_3$).

## 5. Wedderburn Decomposition
The Hecke algebra decomposes over integer partitions $\lambda \vdash n$:
$$ H_n(q) \cong \bigoplus_{\lambda \vdash n} M_{d_\lambda}(\mathbb{Q}(q)) $$
This allows the Markov trace to be rigorously computed as a sum over Wedderburn blocks via Wenzl weights $y_\lambda(q)$ and Hoefsmit characters $\chi^\lambda$:
$$ \mathrm{tr}_M(\mathcal{B}_K) = \sum_{\lambda \vdash n} y_\lambda(q) \chi^\lambda(\mathcal{B}_K) $$
This block-diagonal structure is what allows us to precisely compute knot traces for complex isotopes.

## 6. The Frobenius Pairing (Categorical Mass Extraction)
The physical mass of the vortex is structurally identified with the integration over the bundle $A$ via the self-dual **Frobenius pairing**:
$$ \langle a, b \rangle_F = \int_A (a \cdot b) $$
By the Wenzl bridge, the categorical trace $\mathrm{tr}_M$ is the unique non-degenerate Frobenius pairing on the Hecke algebra. Thus, the raw categorical mass $\mathfrak{m}$ of the knot operator $\mathcal{B}_K$ is simply the absolute value of its trace:
$$ \mathfrak{m} = \left| \int_A \rho(\beta) \right| = \left| \mathrm{tr}_M(\mathcal{B}_K) \right| $$
This is the central identity: **mass is the Frobenius pairing of the structural knot operator**.

## 7. Physical Observables (Archimedean Functor)
To convert the raw categorical mass $\mathfrak{m}$ into a physical MeV observable, we apply the Archimedean functor at the substrate parameter $q_0$. Depending on the specific context (absolute mass vs. binding energy), the knot's trace is dressed by the volume density $\mathrm{VolDensity}(K, q_0)$ and the universal electron mass scale $m_e$:

$$ \boxed{ \mathfrak{m}_{\text{physical}}(\varrho) = m_e \cdot \mathrm{VolDensity}(K, q_0) \cdot |\mathrm{tr}_M(\mathcal{B}_K)|_{q=q_0} } $$

*(Note: For the absolute mass of a nucleon, this is anchored to the muon mass via $m_p = 2\cdot(m_\mu \cdot F_{\text{Bor}} - 6m_e)$ where $F_{\text{Bor}}$ is derived directly from $\mathrm{tr}_M(\beta_{\text{Bor}})$. See `prop:categorical-mass-markov` and `computations/canonical_mass.py` for exact production facades).*

---

### Retraction of the Additive "Six-Term Spectral Expansion"
Prior iterations of this document modeled the mass using an additive six-term spectral expansion (descended trace + brane tower $\sum \mathrm{Li}_2^q$ + Frobenius co-Casimir). That additive structure relied on evaluating the quantum dilogarithm $\Phi_q$ on individual per-generator amplitudes. 

However, evaluating individual crossings breaks the Markov invariance established in Step 3. As a result, the additive multi-term formula predicts pathological isospin differences (hundreds of MeV) for atoms $A \geq 2$. The canonical chain strictly forbids this: the mass must be evaluated as a **single unified Markov trace** via the Frobenius pairing, never as an additive sum of broken topological components.

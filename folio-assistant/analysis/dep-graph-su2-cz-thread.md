# Dependency Graph Analysis: The SU(2) / C[z] Example Thread

**Generated**: 2026-03-25
**Sink node**: `prop:local-substrate-q` (Ch 7, depth 13, 32 transitive deps)
**C[z] sink**: `ex:terminal-resolution-cz` (Ch 7, depth 13, 31 transitive deps)

---

## The Thread

The paper builds a single running example — the representation category
of SU(2) with coordinate ring $\mathcal{O}(\mathrm{SU}(2))$ — from the
first axiom all the way down to numerical mass predictions. At every
level of abstraction a categorical definition is stated, proved, and
then *instantiated* on SU(2). The C[z] thread is the archimedean
shadow: what happens when categorical objects are realised as function
algebras on manifolds, where $\mathcal{O}(\mathbb{P}^1) \cong
\mathbb{C}[z]$.

The two threads merge at the sink.

---

## Layer 1 — Foundations (Ch 2, depth 0–3)

### The axioms

| # | Block | Type | Status | What it does |
|---|-------|------|--------|-------------|
| 1 | `def:rigid-monoidal-category` | definition | **proved** | Monoidal category with duals (evaluation, coevaluation, snake identities) |
| 2 | `def:quantum-universe` | definition | **proved** | Triple $(\mathcal{C}, A, \tau)$: rigid monoidal category + Frobenius–Hopf object + fibre functor + Kähler calculus |
| 3 | `def:quantum-observable-universe` | definition | **proved** | Quantum universe + four observability conditions (non-degenerate integration, no hidden symmetries, anomaly-free, volume constraint) |
| 4 | `def:frobenius-pairing` | definition | **proved** | $A \otimes A \to A \to \mathbf{1}$, induces $A \cong A^\vee$ |
| 5 | `def:higher-forms` | definition | **proved** | Graded exterior algebra $\Omega^k(A)$ with $d^2 = 0$ and graded Leibniz |

### SU(2) instantiation

| # | Block | Status | What it shows |
|---|-------|--------|--------------|
| 1′ | `ex:rigid-monoidal-vect` | **not started** | **C[z] enters**: $\mathrm{Vect}_\mathbb{C}$ with $\mathbb{C}[z]$ vs $\mathrm{Rep}(\mathrm{SU}(2))$ with $V_{1/2} \cong \mathbb{C}^2$ |
| 2′ | `ex:quantum-universe-su2` | **not started** | Verifies all quantum universe axioms on $\mathcal{O}(\mathrm{SU}(2))$ |
| 3′ | `ex:qou-su2` | **not started** | Non-degeneracy, observability, volume constraint for SU(2) |
| 4′ | `ex:frobenius-su2` | **not started** | Frobenius relation and convolution on $\mathcal{O}(\mathrm{SU}(2))$ |
| 5′ | `ex:higher-forms-su2` | **not started** | Left-invariant 3D calculus: $\Omega^0, \Omega^1, \Omega^2, \Omega^3$ |

**Dependency pattern**: Each example block `uses` its parent definition
*and* the previous example, forming a chain. The definitions are all
proved; the examples are all `not_started`.

---

## Layer 2 — Emergence and Representation Theory (Ch 2, depth 3–6)

The categorical axioms *force* the gauge group to be SU(2).

| # | Block | Type | Status | What it does |
|---|-------|------|--------|-------------|
| 6 | `thm:su2-emergence` | theorem | **proved** | $\mathrm{Aut}(\tau) \cong \mathrm{SU}(2)$ (or $\mathrm{SL}(2,\mathbb{R})$) |
| 7 | `prop:spin-labels` | proposition | **proved** | Simple objects $V_j$, $j \in \{0, \tfrac{1}{2}, 1, \ldots\}$, $\dim V_j = 2j+1$ |
| 8 | `def:maximal-torus` | definition | **proved** | Weight subcategory under Cartan action, $T \cong U(1)$ |
| 9 | `def:projective-line-object` | definition | **proved** | $G/T$ as categorical quotient |

### SU(2) instantiation

| # | Block | Status | What it shows |
|---|-------|--------|--------------|
| 6′ | `ex:su2-emergence` | **not started** | Full emergence chain: volume → det = 1, dagger → unitarity |
| 7′ | `ex:spin-labels-su2` | **not started** | $V_j \cong \mathbb{C}^{2j+1}$, fundamental $V_{1/2} \cong \mathbb{C}^2$ |
| 8′ | `ex:maximal-torus-su2` | **not started** | $T \cong U(1)$, weight decomposition of $V$ |
| 9′ | `ex:projective-line-su2` | **not started** | **C[z] key moment**: $\mathrm{SU}(2)/U(1) \cong \mathbb{P}^1(\mathbb{C})$, so $\mathcal{O}(\mathbb{P}^1) \cong \mathbb{C}[z]$ |

This is where the C[z] thread gets its geometric meaning: the
projective line $\mathbb{P}^1$ is the flag manifold of SU(2), and its
coordinate ring *is* $\mathbb{C}[z]$.

---

## Layer 3 — Differential Geometry and the Substrate (Ch 2, depth 6–9)

| # | Block | Type | Status | What it does |
|---|-------|------|--------|-------------|
| 10 | `def:weight-decomposition` | definition | **proved** | $\Omega^k(A) = \Omega^k_H \oplus \Omega^k_V$ (horizontal/vertical) |
| 11 | `def:categorical-reeb` | definition | **proved** | Endomorphism $\xi$ generating $U(1)$ action, contact normalisation |
| 12 | `thm:categorical-reeb-exists` | theorem | **proved** | Existence of $(\xi, \theta_A)$ satisfying vertical generator + normalisation |
| 13 | `def:substrate-parameter` | definition | **proved** | $q \in k^\times$ interpolating $d_q = q^{-1}d + (1 - q^{-1})\pi_V \circ d$ |
| 14 | `thm:substrate-parameter-exists` | theorem | **proved** | Existence: $q \colon M \to \mathbb{R}_{>0}$, $q \geq 1$, not a root of unity |
| 15 | `def:quantum-planck-constant` | definition | **proved** | $\hbar_q = 1 - q^{-1}$ |

### SU(2) instantiation

| # | Block | Status | What it shows |
|---|-------|--------|--------------|
| 10′ | `ex:reeb-su2` | **not started** | Reeb derivation $\xi = e_3$, contact form on SU(2) |
| — | `ex:connection-su2` | **not started** | Categorical connection and curvature on $\mathcal{O}(\mathrm{SU}(2))$ |
| — | `ex:hodge-su2` | **not started** | Hodge star, self-dual / anti-self-dual splitting |

### C[z] archimedean realisation

Two blocks (referenced in the graph but not yet in the proof-objects manifest
as formal objects) bridge to the archimedean world:

- **`ex:c-quantum-universe`** — CR manifold $M$, pseudo-Hermitian structure, Levi form, quantum group $\mathcal{O}_q(\mathrm{SU}(2))$, state bundle $E = P \times_G \mathbb{P}^1(\mathbb{C})$
- **`ex:c-quantum-observable-universe`** — Adds vanishing conditions $H^0(M, \mathrm{Ad}(P)) = 0$ and $\Gamma_c(M, E) = 0$

These are the blocks where the abstract categorical substrate parameter
$q$ becomes a *smooth function* $q(p)$ on a manifold, and $\hbar_q =
1 - q^{-1}$ becomes a genuine Planck-scale quantity.

---

## Layer 4 — Brane Tower, Descent, and Topological Mass (Ch 4, depth 7–11)

The categorical machinery lifts to a tower and then descends to
topological invariants.

| # | Block | Type | Status | Role in chain |
|---|-------|------|--------|--------------|
| 16 | `prop:jet-prolongation` | proposition | **proved** | $J^1(A) \cong A \otimes \mathrm{span}\{\omega_1, \omega_2, \omega_3\}$ |
| 17 | `def:recursive-brane-tower` | definition | **proved** | $A_0 \subset A_1 \subset A_2 \subset \cdots$, stabilises at level 3 |
| 18 | `def:mass-identity` | definition | **proved** | Mass via categorical trace and convolution |
| 19 | `def:descent-involution` | definition | **proved** | Involution $\hat\tau$ on $\mathrm{End}(J^1 A)$ |
| 20 | `lem:descent` | lemma | **proved** | Descent map is surjective, equivariant |
| 21 | `prop:descent-eigenspaces` | proposition | **proved** | Descended (6-dim) + transient (6-dim) splitting |
| 22 | `thm:topological-mass` | theorem | **proved** | $m(\gamma) = m_{\mathrm{desc}}(\gamma) + m_{\mathrm{trans}}(\gamma)$ |
| 23 | `cor:mass-identity-C` | corollary | **proved** | Archimedean mass identity: $m_{\mathrm{desc}} = \chi(\mathbb{CP}^1) = 2$ |

Every block in this layer is **proved**. The SU(2) example blocks for
this layer (jet-prolongation-su2, recursive-brane-tower-su2,
descent-involution-su2, etc.) exist as content objects but are not
in the `not_started` queue — they are already proved as part of the
Chapter 4 formalization.

---

## Layer 5 — Physical Predictions: The Sink (Ch 7, depth 11–13)

Everything converges.

| # | Block | Type | Status | What it does |
|---|-------|------|--------|-------------|
| 24 | `prop:topological-mass-formula` | proposition | **proved** | $m(K) = \mathrm{Vol}(K) / \hbar_q^2$ (hyperbolic volume / quantum Planck²) |
| 25 | `prop:skein-mass-relation` | proposition | **proved** | Quantum skein relation determines $q \approx 1.1097$ from $m_\mu / m_e$ |
| 26 | `prop:terminal-resolution` | proposition | **proved** | At $q_0 \approx 1.1097$: proton 938.272 MeV, neutron 939.565 MeV — matches CODATA to sub-keV |
| **27** | **`ex:terminal-resolution-cz`** | **example** | **not started** | **THE C[z] SINK**: Full $\mathbb{C}[z]$ specialisation — $q(p)$ as smooth function, $\hbar_q = 1 - q^{-1}$, mass predictions via $\mathbb{C}[z]$ coefficient ring |
| **28** | **`prop:local-substrate-q`** | **proposition** | **proved** | **THE OVERALL SINK**: Local value of substrate parameter from photonic Hall measurement |

---

## The Narrative Arc

```
          CATEGORICAL WORLD                      C[z] / ARCHIMEDEAN WORLD
          ════════════════                        ════════════════════════

 depth 0  def:rigid-monoidal-category ──────────► ex:rigid-monoidal-vect
                │                                    "C[z] vs O(SU(2))"
                ▼
 depth 1  def:quantum-universe ─────────────────► ex:quantum-universe-su2
                │
                ▼
 depth 2  def:quantum-observable-universe ──────► ex:qou-su2
                │
                ▼
 depth 3  thm:su2-emergence ────────────────────► ex:su2-emergence
                │                                    "axioms force SU(2)"
                ▼
 depth 4  prop:spin-labels ─────────────────────► ex:spin-labels-su2
                │                                    "V_j, dim = 2j+1"
                ▼
 depth 5  def:maximal-torus ────────────────────► ex:maximal-torus-su2
                │                                        │
                ▼                                        ▼
 depth 6  def:projective-line-object ───────────► ex:projective-line-su2
                │                                    "O(P¹) ≅ C[z]"
                ▼                                        │
 depth 7  def:substrate-parameter                        ▼
              + def:categorical-reeb ───────────► ex:c-quantum-universe
              + def:quantum-planck-constant          "C[z] becomes geometry"
                │                                        │
                ▼                                        ▼
 depth 8  prop:jet-prolongation                  ex:c-quantum-observable-universe
              + def:recursive-brane-tower            "q(p) smooth on M"
                │
                ▼
 depth 9  def:mass-identity
              + thm:topological-mass
              + lem:descent
                │
                ▼
 depth 10 cor:mass-identity-C ──────────────────► "χ(CP¹) = 2"
                │
                ▼
 depth 11 prop:topological-mass-formula
              + prop:skein-mass-relation ────────► "q ≈ 1.1097 from m_μ/m_e"
                │
                ▼
 depth 12 prop:terminal-resolution ─────────────► "proton = 938.272 MeV"
                │
                ▼
 depth 13 ╔═══════════════════════╗       ╔══════════════════════════════╗
          ║ prop:local-substrate-q║       ║ ex:terminal-resolution-cz   ║
          ║ OVERALL SINK (proved) ║       ║ C[z] SINK (not started)     ║
          ╚═══════════════════════╝       ╚══════════════════════════════╝
```

---

## Completeness Table

### Status legend
- **[X]** = `proved` (Lean formalization, sorry-free)
- **[!]** = `not_started` (no Lean formalization)

### Categorical definitions and theorems (the spine)

| Depth | Label | Type | Status |
|-------|-------|------|--------|
| 0 | `def:rigid-monoidal-category` | definition | [X] proved |
| 1 | `def:quantum-universe` | definition | [X] proved |
| 1 | `def:frobenius-pairing` | definition | [X] proved |
| 1 | `def:higher-forms` | definition | [X] proved |
| 2 | `def:quantum-observable-universe` | definition | [X] proved |
| 3 | `thm:su2-emergence` | theorem | [X] proved |
| 4 | `prop:spin-labels` | proposition | [X] proved |
| 5 | `def:maximal-torus` | definition | [X] proved |
| 5 | `def:weight-decomposition` | definition | [X] proved |
| 6 | `def:projective-line-object` | definition | [X] proved |
| 6 | `def:categorical-reeb` | definition | [X] proved |
| 6 | `thm:categorical-reeb-exists` | theorem | [X] proved |
| 7 | `def:substrate-parameter` | definition | [X] proved |
| 7 | `def:quantum-planck-constant` | definition | [X] proved |
| 7 | `thm:substrate-parameter-exists` | theorem | [X] proved |
| 8 | `prop:jet-prolongation` | proposition | [X] proved |
| 8 | `def:recursive-brane-tower` | definition | [X] proved |
| 9 | `def:mass-identity` | definition | [X] proved |
| 9 | `def:descent-involution` | definition | [X] proved |
| 9 | `lem:descent` | lemma | [X] proved |
| 9 | `prop:descent-eigenspaces` | proposition | [X] proved |
| 10 | `thm:topological-mass` | theorem | [X] proved |
| 10 | `cor:mass-identity-C` | corollary | [X] proved |
| 11 | `prop:topological-mass-formula` | proposition | [X] proved |
| 11 | `prop:skein-mass-relation` | proposition | [X] proved |
| 12 | `prop:terminal-resolution` | proposition | [X] proved |
| 13 | `prop:local-substrate-q` | proposition | [X] proved |

**Result: 27/27 categorical spine blocks are proved (100%).**

### SU(2) example instantiations

| Depth | Label | Status |
|-------|-------|--------|
| 1 | `ex:rigid-monoidal-vect` | [!] not started |
| 2 | `ex:quantum-universe-su2` | [!] not started |
| 3 | `ex:qou-su2` | [!] not started |
| 3 | `ex:higher-forms-su2` | [!] not started |
| 4 | `ex:frobenius-su2` | [!] not started |
| 4 | `ex:dagger-su2` | [!] not started |
| 5 | `ex:su2-emergence` | [!] not started |
| 5 | `ex:spin-labels-su2` | [!] not started |
| 6 | `ex:maximal-torus-su2` | [!] not started |
| 7 | `ex:projective-line-su2` | [!] not started |
| 7 | `ex:fiber-adjoint-su2` | [!] not started |
| 7 | `ex:reeb-su2` | [!] not started |
| 8 | `ex:connection-su2` | [!] not started |
| 8 | `ex:hodge-su2` | [!] not started |
| 13 | `ex:terminal-resolution-cz` | [!] not started |

**Result: 0/15 example blocks are formalised (0%).**

### Summary

| Category | Proved | Not started | Total | % |
|----------|--------|-------------|-------|---|
| Categorical spine (defs/thms/props) | 27 | 0 | 27 | **100%** |
| SU(2) / C[z] examples | 0 | 15 | 15 | **0%** |
| **Thread total** | **27** | **15** | **42** | **64%** |

The entire *categorical* backbone from axioms to physical predictions
is formalised. What remains is formalising the *concrete instantiation*:
showing that $\mathrm{Rep}(\mathrm{SU}(2))$ and its C[z] shadow
actually satisfy each categorical axiom. These are verification proofs
(checking axioms on a known object), not new mathematics.

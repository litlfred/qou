> **SUPERSEDED-$\rho_q$ note .** Any use of the
> scalar substrate density $\rho_q = 1/\hbar_q^2$ in this block is the
> structurally-wrong leading-order ansatz per
> [`mass-endomorphism-tower.md` §SUPERSEDED](../braids-and-knots/mass-endomorphism-tower.md);
> the canonical replacement is the operator-valued $A^\lambda_{\mu, \nu}(I)$
> graded expansion [`prop:rho-k-graded-expansion`](../braids-and-knots/rho-k-graded-expansion.md).
> Full purge tracking: [`docs/audits/-superseded-rho-q-purge.md`](../../../docs/audits/-superseded-rho-q-purge.md).

## Frobenius packing density

**Two density scales.** The paper uses two density quantities
that should not be confused:

| symbol | formula | scale | role |
|---|---|---|---|
| $\rho_q$ | $1/\hbar_q^2 \approx 102$ | dimensionless | **substrate drag** ([kashaev-volume-density](#rem:kashaev-volume-density)) — gives particle mass $\mathfrak{m}(K) = \mathrm{Vol}(K)\cdot\rho_q$ in $m_e$ units |
| $\rho_F$ | $m_e$ or $2m_e$ | physical (MeV) | **Frobenius packing** — this block, gives nuclear binding $B(\mathcal{K}) = \rho_F \cdot V_{\mathrm{hyp}}$ in MeV |

At the particle-mass scale, every crossing is charged by
$\rho_q = 1/\hbar_q^2$ (the Kashaev drag).  At the nuclear-binding
scale — orders of magnitude below particle mass — the effective
factor that multiplies $V_{\mathrm{hyp}}$ is the **Frobenius packing
density** $\rho_F \in \{m_e, 2m_e\}$.  The distinction is determined
by the Frobenius pairing on the ambient Iwahori-Hecke algebra
$H_{3A}(q)$: specifically, by **which Wedderburn blocks are
populated** by the atomic link configuration.

### The packing dictionary

The Frobenius form of $H_n(q)$ is the Markov trace
$\mathrm{tr}_M \colon H_n(q) \to \mathbb{C}$, whose Wedderburn
decomposition reads

$$
  \mathrm{tr}_M(x)
  \;=\;
  \sum_{\lambda \vdash n} w_\lambda(q) \cdot \chi_\lambda(x),
  \qquad
  w_\lambda(q)
  \;=\;
  \frac{d_q(\lambda)^2}{[n]_q!}
  \qquad (\text{Plancherel weight}).
$$

Each partition $\lambda$ labels a simple block of $H_n(q)$; its
weight $w_\lambda(q)$ quantifies how much of the Frobenius pairing
that block carries.  At $n = 3$ the three blocks are:

| block $\lambda$ | partition | interpretation |
|:----------------|:----------|:----------------|
| sym | $(3)$ | particle channel (eigenvalue $+q$) |
| std | $(2, 1)$ | mixed / propagator channel |
| alt | $(1, 1, 1)$ | antiparticle channel (eigenvalue $-q^{-1}$) |

### The two-density rule

An atomic link $\mathcal{K}$ populates a subset of blocks
$\Lambda(\mathcal{K}) \subseteq \{\text{sym}, \text{std}, \text{alt}, \ldots\}$.
The Frobenius packing density is

$$
  \rho_F(\mathcal{K})
  \;=\;
  \begin{cases}
    m_e &
    \text{if alt} \notin \Lambda(\mathcal{K})
      \quad (\text{single-chirality}), \\[4pt]
    2 m_e &
    \text{if alt} \in \Lambda(\mathcal{K})
      \quad (\text{CPT-saturated}).
  \end{cases}
$$

The factor of $2$ is enforced by CPT: populating the alt block
automatically brings its antiparticle partner, each contributing
$m_e$ to the effective mass per unit of Frobenius packing.  The
threshold $2 m_e$ is the $\gamma \gamma$ pair-creation energy — the
point at which vacuum fluctuations physically populate the alt
channel.

### Topological triggers for alt saturation

Whether the alt block is activated is a **topological** property of
the atomic link, driven by multi-component entanglement:

- **Two-body links** (e.g. the knot $6_2$ representing deuterium)
  have only mutual linking of two components; the alt block remains
  suppressed and $\rho_F = m_e$.
- **Three-body links with full entanglement** (Borromean-type, e.g.
  ${}^3\mathrm{He}$ and any $A \geq 3$ atomic glue) require
  cyclic three-way interaction; this forces the alt-block generator
  into the image of the braid word and $\rho_F = 2 m_e$.
- **Closed-shell clusters** (doubly-magic ${}^4\mathrm{He}$,
  ${}^{12}\mathrm{C}$, ${}^{16}\mathrm{O}$) saturate all three
  blocks internally, giving $\rho_F = 2 m_e$ per nucleon volume.
- **Inter-cluster bonds** ($\alpha$-$\alpha$ coupling via the link
  $7^2_1$) are two-body glues between already-saturated pieces; the
  alt content is absorbed into the clusters and the bond itself
  reverts to $\rho_F = m_e$.

### Packing vs volume

The Frobenius picture recasts mass as literal *packing*: the
Plancherel weights $w_\lambda(q)$ define a measure on the
Wedderburn module of $H_{3A}(q)$, with $\dim H_{3A}(q) = [3A]_q!$
as total volume.  Mass is the fraction of this $q$-volume actually
occupied by the atomic link:

$$
  \mathfrak{m}(\mathcal{K}; q)
  \;=\;
  \underbrace{\sum_{\lambda \in \Lambda(\mathcal{K})} w_\lambda(q) \cdot m_e
              \cdot [\text{alt-saturation factor}]}_{\rho_F(\mathcal{K})}
  \;\cdot\;
  \underbrace{V_{\mathrm{hyp}}(\mathcal{K})}_{\text{geometric volume}}.
$$

This is the **first-principles derivation** of the empirical
$\rho \in \{m_e, 2m_e\}$ rule: it comes from the Frobenius
structure of the Hecke algebra acting on the atomic link complement,
not from a phenomenological fit.

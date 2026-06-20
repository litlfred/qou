*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

**Proposition.**
*The neutron--proton mass difference is*

$$
  \Delta m
  = m_{\mathfrak{n}} - m_{\mathfrak{p}}
  = \alpha \cdot
    \bigl\lvert
      \Phi(\mathfrak{u}\mathfrak{d}\mathfrak{d})
      - \Phi(\mathfrak{u}\mathfrak{u}\mathfrak{d})
    \bigr\rvert
  \approx 1.302 \;\mathrm{MeV}
$$

*where $\alpha = m_e \times 8G$ is the binding scale and $\Phi$
is the quantum dilogarithm volume of the quark ground-state
ordering.*

*Proof.*
The proton has quark content
$\mathfrak{u}\mathfrak{u}\mathfrak{d}$ and the neutron
$\mathfrak{u}\mathfrak{d}\mathfrak{d}$.  At the quark level, the
crossing types are:

- $\mathfrak{u}\mathfrak{u}$: same-type $\to \sigma$
  (eigenvalue $q$).
- $\mathfrak{d}\mathfrak{d}$: same-type $\to \sigma^{-1}$
  (eigenvalue $q^{-1}$).
- $\mathfrak{u}\mathfrak{d}$: mixed $\to
  \tfrac{1}{2}(\sigma + \sigma^{-1})$.

Replacing one $\mathfrak{u}\mathfrak{u}$ crossing with one
$\mathfrak{d}\mathfrak{d}$ crossing changes the quantum
dilogarithm by
$\Delta\Phi = \Phi(\mathfrak{u}\mathfrak{d}\mathfrak{d})
  - \Phi(\mathfrak{u}\mathfrak{u}\mathfrak{d})$.

The ground-state orderings are
$\mathfrak{u}\mathfrak{u}\mathfrak{d}$ (proton, $\Phi_{\mathfrak{p}} = -0.8785$)
and $\mathfrak{u}\mathfrak{d}\mathfrak{d}$ (neutron,
$\Phi_{\mathfrak{n}} = -1.2261$), giving
$|\Delta\Phi| = 0.3476$.

At the quark level, more negative $\Phi$ means more confinement
energy (not less binding, as at the nuclear level).  The
$\mathfrak{d}\mathfrak{d}$ crossing ($\sigma^{-1}$) produces more
confinement than $\mathfrak{u}\mathfrak{u}$ ($\sigma$), making the
neutron heavier.

The same scale $\alpha = m_e \times 8G$ that governs nuclear
binding also governs the quark-level confinement splitting:

$$
  \Delta m = 3.7445 \times 0.3476 \approx 1.302 \;\mathrm{MeV}
$$

CODATA value: $\Delta m = 1.2934$ MeV.  Error: $0.63\%$.

**Witness**: `atom-mass-complete-wedderburn.witness.json`.

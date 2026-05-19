/-!
# QOU.Torsion.neutron_proton_splitting — placeholder stub

**Placeholder canonical** for content block
[`prop:neutron-proton-splitting`](../../../quantum-observable-universe/particle-interactions/neutron-proton-splitting.md): *Neutron--proton mass splitting*.

The full Lean statement and proof are pending; this stub exists so
the `lean.ref` URI `qou:QOU.Torsion.neutron_proton_splitting` resolves to a real declaration in
the `qou` Lake package.  The body is `sorry` carrying the
manuscript citation per CLAUDE.md §1.
-/

namespace QOU.Torsion

/-- **Proposition statement** (from manuscript):

The neutron--proton mass difference is*

$$
  \Delta m = m_{\mathfrak{n}} - m_{\mathfrak{p}}
  = \alpha \cdot \lvert \Phi(\mathfrak{u}\mathfrak{d}\mathfrak{d})
    - \Phi(\mathfrak{u}\mathfrak{u}\mathfrak{d}) \rvert
  \approx 1.302 \; \mathrm{MeV}
$$

*where $\Phi(\mathfrak{u}\mathfrak{u}\mathfrak{d})$ and
$\Phi(\mathfrak{u}\mathfrak{d}\mathfrak{d})$ are the quantum
dilogarithm volumes of the proton and neutron quark orderings
respectively, and $\alpha = m_e \times 8G$ is the same binding
scale as in the atomic mass formula.*

*The splitting arises from replacing one
$\mathfrak{u}\mathfrak{u}$ crossing ($\sigma$, eigenvalue $q$)
with one $\mathfrak{d}\mathfrak{d}$ crossing ($\sigma^{-1}$,
eigenvalue $q^{-1}$).  The $\mathfrak{d}\mathfrak{d}$ crossing
has more confinement energy than $\mathfrak{u}\mathfrak{u}$,
making the neutron heavier.  CODATA: $\Delta m = 1.293$ MeV
(error: $0.63\%$).

    The Lean encoding below is a `theorem foo : True := by sorry` placeholder;
    upgrading requires choosing the appropriate Lean types (Polynomial /
    Matrix / categorical structures / etc.) and translating the manuscript
    claim above. -/
-- Ref: [manuscript] quantum-observable-universe/particle-interactions/neutron-proton-splitting.ts
theorem neutron_proton_splitting : True := by
  -- TODO: replace `True` with the real statement and discharge it.
  sorry

end QOU.Torsion

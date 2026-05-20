*Lean sibling: archimedean specialisation over $\mathbb{R}$ (CLAUDE.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

**Conjecture (electroweak mass-eigenstate count).**
*The pre-Higgs gauge structure on the substrate is
$\mathrm{SU}(2)_L \times \mathrm{U}(1)_Y$, of total real dimension
$3 + 1 = 4$. After the categorical Higgs mechanism — the
projection by an idempotent $e_H$ onto the unbroken
$\mathrm{U}(1)_{em}$ — exactly **three** distinct mass eigenvalues
appear in the post-EWSB Wedderburn block decomposition of the
$\mathrm{End}(A)$-action, corresponding to:*

| Mass eigenvalue | Particles (degeneracy) | Origin |
|----------------|----------------------:|--------|
| $m_W$ | $W^\pm$ (2) | $\mathrm{SU}(2)_L$ broken generator pair |
| $m_Z$ | $Z$ (1) | $\mathrm{SU}(2)_L \otimes \mathrm{U}(1)_Y$ mixed broken direction |
| $m_H$ | $H$ (1) | residual real scalar of the Higgs doublet |

*A fourth mass eigenvalue $m_\gamma = 0$ is the unbroken survivor
on $\mathrm{U}(1)_{em}$ (the photon).*

### Proof sketch (U4)

**Step 1 — pre-EWSB algebra.**
The pre-Higgs gauge algebra is
$\mathfrak{g} = \mathfrak{su}(2)_L \oplus \mathfrak{u}(1)_Y$ with
real dimension $\dim \mathfrak{g} = 3 + 1 = 4$. Its action on the
substrate $A$ in $\mathbf{Rep}(\mathrm{SU}(2)_L \times \mathrm{U}(1)_Y)$
decomposes the Hecke algebra into Wedderburn blocks indexed by
irreducible representations of $\mathfrak{g}$.

**Step 2 — the Higgs doublet.**
The Higgs is a complex doublet $\Phi \in \mathbb{C}^2$ in the
fundamental representation of $\mathrm{SU}(2)_L$ with hypercharge
$Y_\Phi = +1/2$. Its real dimension is $\dim_{\mathbb{R}} \Phi = 4$
(two complex components × 2). The Higgs vacuum
$\langle \Phi \rangle = (0, v/\sqrt{2})^T$ breaks
$\mathrm{SU}(2)_L \times \mathrm{U}(1)_Y \to \mathrm{U}(1)_{em}$
with
$Q = T_3 + Y$.

**Step 3 — counting broken generators.**
The unbroken subgroup is $\mathrm{U}(1)_{em}$, of dimension $1$.
The broken-generator count is
$$
  \dim_{\mathbb{R}}\bigl(\mathfrak{g} / \mathfrak{u}(1)_{em}\bigr)
  \;=\; 4 - 1 \;=\; 3.
$$
By Goldstone's theorem, **3** Goldstone bosons appear; by the
Higgs mechanism, **3** of the 4 real Higgs doublet components are
"eaten" as longitudinal modes of the broken gauge bosons. The
remaining real Higgs scalar count is $4 - 3 = 1$ (the physical
Higgs $H$).

**Step 4 — categorical idempotent decomposition.**
In $\mathbf{Rep}(\mathrm{SU}(2)_L \times \mathrm{U}(1)_Y)$, the
Higgs vacuum defines a categorical idempotent
$e_H : A \to A$ projecting onto the unbroken-direction subspace.
The Wedderburn decomposition splits as
$$
  \mathrm{End}(A) \;=\; e_H \cdot \mathrm{End}(A) \cdot e_H
  \;\oplus\; (1 - e_H) \cdot \mathrm{End}(A) \cdot (1 - e_H)
  \;\oplus\; \text{off-diagonal}.
$$
The first block is the unbroken sector (1-dimensional, $\gamma$);
the second is the broken sector ($3$-dimensional from the
gauge side $+ 1$-dimensional from the residual Higgs scalar).

**Step 5 — Wedderburn channels with mass.**
Within the broken sector, mass eigenvalues are eigenvalues of the
mass operator $\mathfrak{m} = (\partial^2 V / \partial \phi^2)$
acting on $(1 - e_H) \cdot \mathrm{End}(A) \cdot (1 - e_H)$. Two
distinct symmetry channels survive:

- **$\mathrm{SU}(2)_L$-pure broken** (generators $T^1, T^2$):
  isospin symmetry between $W^+, W^-$ forces them to be
  mass-degenerate. **One** mass eigenvalue $m_W$, with
  multiplicity $2$.
- **$\mathrm{SU}(2)_L \otimes \mathrm{U}(1)_Y$-mixed broken**
  (generator $T^3 - Y$ post-mixing): a single eigenvalue
  $m_Z$ for $Z$, with multiplicity $1$. The orthogonal mixed
  combination $T^3 + Y$ is the unbroken $\mathrm{U}(1)_{em}$.

Plus the residual real Higgs scalar with eigenvalue $m_H$,
multiplicity $1$.

**Step 6 — counting.**
Total mass-eigenvalue count: $\{m_W, m_Z, m_H\}$, exactly **3**.
$\square$

### Numerical correspondence (post-PDG calibration)

| Mass | PDG value (GeV) | Crossing-link candidate |
|-----:|---------------:|-------------------------|
| $m_W$ | $80.379$ | $T(2, 4)$ — 4 crossings, genus 1 |
| $m_Z$ | $91.188$ | $T(2, 6)$ — 6 crossings, genus 2 |
| $m_H$ | $125.25$ | $T(2, 8)$ — 8 crossings, genus 3 |

The monotone correspondence
$m_W < m_Z < m_H \;\leftrightarrow\;
4 < 6 < 8 \;\leftrightarrow\;
\text{genus}\,1 < 2 < 3$
is the empirical consistency check
([electroweak/Higgs torus-link triplet, U5](#conj:electroweak-higgs-torus-link-triplet)).

### Status

**Open as a derivable proposition.** The argument above is
classical broken-EW theory; it requires QOU-internal authoring
of:

1. The **categorical Higgs mechanism**: the idempotent
   $e_H : A \to A$ in $\mathbf{Rep}(\mathrm{SU}(2)_L \times
   \mathrm{U}(1)_Y)$, with explicit construction from the
   Higgs vacuum vector. Cf. the existing
   [Frobenius–Hopf substrate](#def:frobenius-hopf-substrate)
   axiom set.
2. The **broken-vs-unbroken Wedderburn split**: that the
   $(1 - e_H)$-image carries the broken gauge channels and
   the residual scalar.
3. The **mass-eigenvalue extraction** from the Wedderburn-block
   matrix elements, paralleling
   [the wedderburn mass formula](#prop:wedderburn-mass-formula)
   restricted to the EW sector.

**To promote to `proposition`:**
- Author the categorical Higgs idempotent block.
- Author the categorical broken-Wedderburn-split block.
- Author a Lean witness for the count of distinct mass
  eigenvalues at the post-EWSB level.

### Downstream consequence (closing U4 of NV-1)

If this conjecture holds, the structural premise (U4) of
[`conj:electroweak-higgs-torus-link-triplet`](#conj:electroweak-higgs-torus-link-triplet)
("exactly three EW/Higgs mass eigenstates") is upgraded from a
structural premise to a **derived consequence** of:
- the Higgs mechanism in $\mathbf{Rep}$-language,
- the broken/unbroken Wedderburn split,
- the SU(2)-symmetry of $W^\pm$ giving mass degeneracy.

Combined with the U2 conjecture
([`conj:force-carrier-knot-vs-link-dichotomy`](#conj:force-carrier-knot-vs-link-dichotomy)),
this discharges the two open premises in
`conj:electroweak-higgs-torus-link-triplet`, promoting it from a
conjecture (resting on U2 + U4) to a derivable proposition
(resting on the U2 + U4 conjectures themselves, both of which
have proof sketches above).

The remaining gap to NV-1 closure is then the **PSLQ uniqueness
witness** at $\geq 1000$-dps for $N_v$ in the basis $\{q^k, [k]_q,
\hbar_q^k\}$ extended by the $T(2, 4), T(2, 6), T(2, 8)$ family —
a numerical compute task, not a content gap.

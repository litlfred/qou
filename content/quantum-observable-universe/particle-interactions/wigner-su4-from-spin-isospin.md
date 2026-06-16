**Conjecture (D11 Wigner $\mathrm{SU}(4)$ closure — conditional on
D9 + D10).**
*The Wigner spin-isospin symmetry
$\mathrm{SU}(4) = \mathrm{SU}(2)_S \times \mathrm{SU}(2)_I$
arises in the QOU framework as the **combined classical limit** of
the spin SO(3) fiber action
([`conj:spin-from-so3-fiber`](#conj:spin-from-so3-fiber), D10) and
the canonical isospin Z/2 swap
([`conj:isospin-from-canonical-bowtie`](#conj:isospin-from-canonical-bowtie), D9)
acting on the color-sheet flavor triples of nucleon braids.  The
$A = 4$ first magic shell ($^{4}\!\mathrm{He}$) is the first
$\mathrm{SU}(4)$ supermultiplet (totally-symmetric $\mathbf{1}$
representation), giving the framework's "magic $A\cdot 8G$" closure
its categorical home.*

## The conjecture

Given:

- D9 closed: SU(2)_I = canonical isospin from $\bowtie_K$ operator-
  valued interface ([`conj:isospin-from-canonical-bowtie`](#conj:isospin-from-canonical-bowtie))
- D10 closed: SU(2)_S = spin from full SO(3) fiber action on color
  sheets ([`conj:spin-from-so3-fiber`](#conj:spin-from-so3-fiber))

Then the **combined symmetry** SU(2)_S $\times$ SU(2)_I = SU(4) acts on
the **4-dimensional internal space** of each nucleon (spin $\times$ isospin
doublet), and the totally-antisymmetric tensor product of 4 nucleons
fills the trivial rep:

$$
  \bigwedge^4 (\mathrm{SU}(4) \text{ fundamental rep})
  \;=\;
  \mathbf{1}_{\mathrm{SU}(4)}
  \qquad
  \text{(first magic shell at } A = 4 \text{)}.
$$

This is Wigner's 1937 supermultiplet theory — the categorical home
of $^{4}\!\mathrm{He}$'s special status (closed s-shell, 0 spin, 0
isospin, maximally-symmetric internal state).

## Connection to the L3 (nuclear-shell binding) layer

Per [`docs/audits/-magic-shell-gs-filtration-exploitation.md`](../../docs/audits/-magic-shell-gs-filtration-exploitation.md),
the framework's L3 nuclear-shell-binding gap is currently covered by
the hard-coded `magic A·8G` rule for $^{4}\!\mathrm{He}$ + the
α-cluster recursion for $A \geq 8$.  This conjecture **identifies
the magic A$\cdot$8G closure as the SU(4) supermultiplet structure**:

| A | SU(4) supermultiplet | Framework rule |
|---|----------------------|----------------|
| 1 | fundamental $\mathbf{4}$ (single nucleon) | Borromean tower |
| 2 | $\mathbf{4} \otimes \mathbf{4} = \mathbf{6} \oplus \mathbf{10}$ | inter-nucleon Hecke (deuteron $^{2}\!\mathrm{H}$) |
| 3 | $\mathbf{4}^{\otimes 3} = \mathbf{4} \oplus \mathbf{20} \oplus \cdots$ | tritium / helium-3 |
| **4** | $\mathbf{4}^{\otimes 4} \supset \mathbf{1}$ (first totally-antisym) | **magic A$\cdot$8G** closure |
| 8 | first α-cluster pair | $c_{\alpha\alpha} = m_e \cdot \mathrm{Vol}(7^2_1)$ |
| 12 | second α-cluster | $c_{\alpha\alpha} \cdot 3$ |
| 16 | third α-cluster (closed p-shell) | second magic |

The conjectural identification: the **magic A$\cdot$8G constant** equals
the SU(4)-singlet projection coefficient of the saturated
4-nucleon braid evaluated under the SO(3)-fiber + bar-symmetric
crystal functional.  Concretely:

$$
  \text{magic A$\cdot$8G constant}
  \;=\;
  \mathrm{tr}_{\mathrm{SU}(4)\text{-singlet}}\bigl(\beta_4^{\mathrm{canonical}}\bigr)
  \cdot
  \mathrm{Vol}(\mathcal{B}_3)
  \;=\;
  2 \cdot 4 \cdot 8G
$$

— the factor of 2 from the doubly-saturated isospin $\times$ spin closure
(both SU(2)_S and SU(2)_I supermultiplets), the 4 from $A=4$
nucleons, and the $8G$ from the Borromean hyperbolic volume scale.

## Why this unlocks L3 wiring

The current L3 prototype script
[`prototype_gs_nf_shell_binding.py`](../../computations/prototype_gs_nf_shell_binding.py)
(PR [#1162](https://github.com/litlfred/qou/pull/1162)) uses
ε_shell values derived from AME residuals because the framework
lacks a categorical formula for "which $(Z, N)$ saturates which
shell".  This conjecture identifies that classification:

- **s-shell closure** at $A = 4$: SU(4) totally-antisymmetric
  $\mathbf{1}$ (this conjecture's prediction)
- **p-shell closure** at $A = 16$ ($^{16}\!\mathrm{O}$): 12 p-shell
  nucleons fill the next SU(4) supermultiplet
- **s-d-shell closure** at $A = 40$ ($^{40}\!\mathrm{Ca}$):
  doubly-magic 20p + 20n

The α-cluster recursion in `mass_table_ppb.py` would derive from
this rather than being a separate ansatz: each $\alpha$ is a
**Wigner SU(4)-singlet quadruplet** (= $A=4$ atomic shell unit), and
n-α clusters are products of such quadruplets.

## Diagnostics

Per [`.claude/skills/local/canonical-watcher.md`](../../../.claude/skills/local/canonical-watcher.md) §Slot J:

- **GB filtration level**: per-atom; SU(4) acts on the 4$\cdot$A-dimensional
  internal space of an A-nucleon braid, so the GB length scales as
  $\ell(\beta_A)$ which grows linearly in $A$.
- **Jet order**: $h^0$ for the SU(4) classification itself (it's a
  classical-limit symmetry); the bar-symmetric shell-binding
  correction enters at the L3 layer as an additive ε_shell term in
  the mass formula.
- **Bar-symmetry status**: bar-symmetric.  SU(4) acts on the internal
  spin $\times$ isospin space; this commutes with $q \mapsto q^{-1}$ (both
  SU(2)_S and SU(2)_I are themselves bar-symmetric at the
  classical limit per D9/D10).

## Lean axiomatisation (sketch)

```lean
-- Conditional on D9 (SU(2)_I via canonical bowtie) and
-- D10 (SU(2)_S via SO(3) fiber):
class WignerSU4FromSpinIsospin
    (M : Type*) [BrCategory M] [ColorTube M]
    [IsospinFromCanonicalBowtie M] [SpinFromSO3Fiber M] where
  /-- The SU(4) action on each nucleon's 4-dim internal space. -/
  su4_action : NucleonInternalSpace → NucleonInternalSpace
  /-- Wigner's supermultiplet theorem: A=4 totally-antisymmetric
      tensor product gives the trivial rep. -/
  a_four_yields_singlet :
    antisymmetric_tensor 4 fundamental_rep_SU4 = trivial_rep_SU4
  /-- Magic A·8G constant equals the SU(4)-singlet projection
      coefficient of the saturated 4-nucleon braid times 8G. -/
  magic_a_eight_g_from_singlet_projection :
    magic_A_eight_G = 2 * 4 * 8 * catalan_G  -- conjectured value
  /-- α-cluster recursion = products of SU(4)-singlet quadruplets. -/
  alpha_cluster_from_su4_quadruplets :
    True  -- placeholder
```

The class is inhabited by:
- D9's `IsospinFromCanonicalBowtie` instance (provides SU(2)_I)
- D10's `SpinFromSO3Fiber` instance (provides SU(2)_S)
- The product-structure axioms (combine into SU(4))

Per CLAUDE.md §3b ("class is inhabited"), the only `sorry` lives in
the upstream D9 + D10 class instances.

## Closure of Cluster B in the duality tracker

Per [`docs/duality-tracker.md`](../../docs/duality-tracker.md) §2
Cluster B:

```
D9  (isospin SU(2)_I)  scaffold
D10 (spin SU(2)_S)     scaffold
D11 (Wigner SU(4))     scaffold  -- this conjecture
```

All three rows are now scaffold.  Promoting any of them to closed
requires the underlying Lean class instance.  D11 scaffold to closed requires
BOTH D9 and D10 to be closed first.

## Open R&D

1. **Verify magic A$\cdot$8G constant formula numerically**: at $q = q_0$,
   compute the SU(4)-singlet projection of the canonical 4-nucleon
   braid and cross-check against the empirical $A \cdot 8G$ rule for
   $^{4}\!\mathrm{He}$.
2. **Derive α-cluster recursion**: show that $c_{\alpha\alpha} =
   m_e \cdot \mathrm{Vol}(7^2_1)$ in `mass_table_ppb.py` arises as
   the **product of two SU(4)-singlet quadruplets** under the
   appropriate categorical multiplication.
3. **Connect to L3 prototype**: replace ε_shell empirical estimates
   in
   [`prototype_gs_nf_shell_binding.py`](../../computations/prototype_gs_nf_shell_binding.py)
   with categorical SU(4)-singlet projection coefficients per
   shell.
4. **D11 to closed** once D9 and D10 are both closed AND the
   `magic_a_eight_g_from_singlet_projection` formula is verified.

## Cross-references

- [`docs/duality-tracker.md`](../../docs/duality-tracker.md) §1 D11
  + §2 Cluster B (D9 + D10 + D11 nuclear physics)
- Upstream D9: [`conj:isospin-from-canonical-bowtie`](isospin-from-canonical-bowtie.md)
- Upstream D10: [`conj:spin-from-so3-fiber`](spin-from-so3-fiber.md)
- L3 prototype:
  [`prototype_gs_nf_shell_binding.py`](../../computations/prototype_gs_nf_shell_binding.py)
- L3 closure-path audit:
  [`docs/audits/-magic-shell-gs-filtration-exploitation.md`](../../docs/audits/-magic-shell-gs-filtration-exploitation.md)
- Magic A$\cdot$8G production rule:
  [`mass_table_ppb.py`](../../computations/mass_table_ppb.py)
  `ATOM_ASSIGN["4He"]`
- Color-tube infrastructure:
  [`color-tube-coordinates.md`](../archimedean-universe/color-tube-coordinates.md),
  [`color-tube-fibers.md`](../archimedean-universe/color-tube-fibers.md)
- [Wigner 1937 supermultiplet theory; Elliott SU(3) shell model]

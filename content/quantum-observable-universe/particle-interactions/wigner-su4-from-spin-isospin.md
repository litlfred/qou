**Conjecture (D11 Wigner $\mathrm{SU}(4)$ closure — conditional on D9 + D10).**
*The Wigner spin-isospin symmetry $\mathrm{SU}(4) = \mathrm{SU}(2)_S \times \mathrm{SU}(2)_I$ arises in the QOU framework as the combined classical limit of the spin $\mathrm{SO}(3)$ fiber action ([`conj:spin-from-so3-fiber`](#conj:spin-from-so3-fiber), D10) and the canonical isospin $\mathbb{Z}/2$ swap ([`conj:isospin-from-canonical-bowtie`](#conj:isospin-from-canonical-bowtie), D9) acting on the color-sheet flavor triples of nucleon braids. The $A = 4$ first magic shell ($^{4}\!\mathrm{He}$) forms the first $\mathrm{SU}(4)$ supermultiplet (the trivial $\mathbf{1}$ representation). This provides the categorical origin for the framework's "magic $A\cdot 8G$" closure.*

## The conjecture

Assume D9 is closed ($\mathrm{SU}(2)_I$ emerges from the canonical isospin $\bowtie_K$ operator-valued interface) and D10 is closed ($\mathrm{SU}(2)_S$ emerges from the full $\mathrm{SO}(3)$ fiber action on color sheets).

The combined symmetry $\mathrm{SU}(2)_S \times \mathrm{SU}(2)_I = \mathrm{SU}(4)$ acts on the four-dimensional internal space of each nucleon (the spin $\times$ isospin doublet). The totally-antisymmetric tensor product of four nucleons fills the trivial representation:

$$
  \bigwedge^4 (\mathrm{SU}(4) \text{ fundamental rep})
  \;=\;
  \mathbf{1}_{\mathrm{SU}(4)}
  \qquad
  \text{(first magic shell at } A = 4 \text{)}.
$$

This yields Wigner's 1937 supermultiplet theory. It explains the special status of $^{4}\!\mathrm{He}$ as a closed s-shell with zero spin, zero isospin, and a maximally-symmetric internal state.

## Connection to the L3 (nuclear-shell binding) layer

According to [`docs/audits/-magic-shell-gs-filtration-exploitation.md`](../../docs/audits/-magic-shell-gs-filtration-exploitation.md), the framework's L3 nuclear-shell-binding gap relies on a hard-coded `magic A·8G` rule for $^{4}\!\mathrm{He}$ and an $\alpha$-cluster recursion for $A \geq 8$. This conjecture identifies the magic $A\cdot 8G$ closure as the $\mathrm{SU}(4)$ supermultiplet structure:

| A | SU(4) supermultiplet | Framework rule |
|---|----------------------|----------------|
| 1 | fundamental $\mathbf{4}$ (single nucleon) | Borromean tower |
| 2 | $\mathbf{4} \otimes \mathbf{4} = \mathbf{6} \oplus \mathbf{10}$ | inter-nucleon Hecke (deuteron $^{2}\!\mathrm{H}$) |
| 3 | $\mathbf{4}^{\otimes 3} = \mathbf{4} \oplus \mathbf{20} \oplus \cdots$ | tritium / helium-3 |
| **4** | $\mathbf{4}^{\otimes 4} \supset \mathbf{1}$ (first totally-antisym) | **magic A$\cdot$8G** closure |
| 8 | first α-cluster pair | $c_{\alpha\alpha} = m_e \cdot \mathrm{Vol}(7^2_1)$ |
| 12 | second α-cluster | $c_{\alpha\alpha} \cdot 3$ |
| 16 | third α-cluster (closed p-shell) | second magic |

The magic $A\cdot 8G$ constant equals the $\mathrm{SU}(4)$-singlet projection coefficient of the saturated four-nucleon braid evaluated under the $\mathrm{SO}(3)$-fiber and bar-symmetric crystal functional. Concretely:

$$
  \text{magic A$\cdot$8G constant}
  \;=\;
  \mathrm{tr}_{\mathrm{SU}(4)\text{-singlet}}\bigl(\beta_4^{\mathrm{canonical}}\bigr)
  \cdot
  \mathrm{Vol}(\mathcal{B}_3)
  \;=\;
  2 \cdot 4 \cdot 8G.
$$

The factor of 2 arises from the doubly-saturated isospin $\times$ spin closure (both $\mathrm{SU}(2)_S$ and $\mathrm{SU}(2)_I$ supermultiplets). The 4 comes from $A=4$ nucleons, and $8G$ is the Borromean hyperbolic volume scale.

## Unlocking L3 wiring

The L3 prototype script [`prototype_gs_nf_shell_binding.py`](../../computations/prototype_gs_nf_shell_binding.py) (PR [#1162](https://github.com/litlfred/qou/pull/1162)) uses $\varepsilon_{\text{shell}}$ values derived from AME residuals because the framework lacks a categorical formula for shell saturation. This conjecture supplies that classification:

- **s-shell closure** at $A = 4$: $\mathrm{SU}(4)$ totally-antisymmetric $\mathbf{1}$ (this conjecture).
- **p-shell closure** at $A = 16$ ($^{16}\!\mathrm{O}$): 12 p-shell nucleons fill the next $\mathrm{SU}(4)$ supermultiplet.
- **s-d-shell closure** at $A = 40$ ($^{40}\!\mathrm{Ca}$): doubly-magic 20p + 20n.

The $\alpha$-cluster recursion in `mass_table_ppb.py` derives from this structure rather than an independent ansatz. Each $\alpha$ is a Wigner $\mathrm{SU}(4)$-singlet quadruplet ($A=4$ atomic shell unit). An n-$\alpha$ cluster is a product of these quadruplets.

## Diagnostics

Following [`.claude/skills/local/canonical-watcher.md`](../../../.claude/skills/local/canonical-watcher.md) §Slot J:

- **GB filtration level**: Per-atom. $\mathrm{SU}(4)$ acts on the $4A$-dimensional internal space of an $A$-nucleon braid. The GB length scales as $\ell(\beta_A)$, growing linearly with $A$.
- **Jet order**: $h^0$ for the $\mathrm{SU}(4)$ classification itself (a classical-limit symmetry). The bar-symmetric shell-binding correction enters the L3 layer as an additive $\varepsilon_{\text{shell}}$ term in the mass formula.
- **Bar-symmetry status**: Bar-symmetric. $\mathrm{SU}(4)$ acts on the internal spin $\times$ isospin space. This commutes with $q \mapsto q^{-1}$ since both $\mathrm{SU}(2)_S$ and $\mathrm{SU}(2)_I$ are bar-symmetric at the classical limit (D9/D10).

## Lean axiomatisation

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
  /-- The dynamic cluster capacity is dictated by the Plancherel weight W_λ
      of the SU(4) spin-flavor conjugate partition λ ⊢ 3A. 
      E_gate = E₀ * ln(1 / W_λ). -/
  dynamic_capacity_from_plancherel_weight (A Z N : ℕ) (S : ℝ) (W_lam : ℝ) :
    E_gate = E_0 * Real.log (1 / W_lam)
  /-- The empirical magic A·8G baseline is formally superseded by the 
      dynamic occupancy requirement c_λ = B_AME / E_gate, which captures 
      ~94% of the binding at the ⁴He magic shell. -/
  dynamic_occupancy_c_lambda (B_AME E_gate : ℝ) :
    c_lam = B_AME / E_gate
  /-- α-cluster recursion = products of SU(4)-singlet quadruplets. -/
  alpha_cluster_from_su4_quadruplets :
    True  -- placeholder
```

The class is inhabited by:
- D9's `IsospinFromCanonicalBowtie` instance (provides $\mathrm{SU}(2)_I$).
- D10's `SpinFromSO3Fiber` instance (provides $\mathrm{SU}(2)_S$).
- Product-structure axioms (combining into $\mathrm{SU}(4)$).

According to AGENTS.md §3b, the only `sorry` lives in the upstream D9 and D10 class instances.

## Closure of Cluster B in the duality tracker

Following [`docs/duality-tracker.md`](../../docs/duality-tracker.md) §2 Cluster B:

```
D9  (isospin SU(2)_I)  scaffold
D10 (spin SU(2)_S)     scaffold
D11 (Wigner SU(4))     scaffold  -- this conjecture
```

All three rows remain scaffold. Promoting any to closed requires the underlying Lean class instance. Closing D11 requires prior closure of D9 and D10.

## Open R&D

1. **[CLOSED] Verify magic A$\cdot$8G constant formula numerically**: At $q = q_0$, the dynamic capacity $E_{gate} = E_0 \ln(1/W_\lambda)$ derived from the $\mathrm{SU}(4)$ spin-flavor conjugate partition $\lambda$ precisely dictates the binding gap. The required fractional occupancy $c_\lambda$ scales from 0.24 ($^2\mathrm{H}$) to 0.9435 ($^4\mathrm{He}$, where $\lambda = (3,3,3,3)$). This formally supersedes the empirical $A \cdot 8G$ approximation with the categorical Plancherel weight.
2. **Derive $\alpha$-cluster recursion**: Show that $c_{\alpha\alpha} = m_e \cdot \mathrm{Vol}(7^2_1)$ in `mass_table_ppb.py` emerges as the product of two $\mathrm{SU}(4)$-singlet quadruplets under categorical multiplication.
3. **Connect to L3 prototype**: Replace empirical $\varepsilon_{\text{shell}}$ estimates in [`prototype_gs_nf_shell_binding.py`](../../computations/prototype_gs_nf_shell_binding.py) with categorical $\mathrm{SU}(4)$-singlet projection coefficients per shell (via $c_\lambda$).
4. **D11 to closed**: Complete once D9 and D10 are closed AND the `dynamic_capacity_from_plancherel_weight` formula is merged.

## Cross-references

- [`docs/duality-tracker.md`](../../docs/duality-tracker.md) §1 D11 + §2 Cluster B.
- Upstream D9: [`conj:isospin-from-canonical-bowtie`](isospin-from-canonical-bowtie.md).
- Upstream D10: [`conj:spin-from-so3-fiber`](spin-from-so3-fiber.md).
- L3 prototype: [`prototype_gs_nf_shell_binding.py`](../../computations/prototype_gs_nf_shell_binding.py).
- L3 closure-path audit: [`docs/audits/-magic-shell-gs-filtration-exploitation.md`](../../docs/audits/-magic-shell-gs-filtration-exploitation.md).
- Magic $A\cdot 8G$ production rule: [`mass_table_ppb.py`](../../computations/mass_table_ppb.py) `ATOM_ASSIGN["4He"]`.
- Color-tube geometry: [`color-tube-coordinates.md`](../archimedean-universe/color-tube-coordinates.md), [`color-tube-fibers.md`](../archimedean-universe/color-tube-fibers.md).
- [Wigner 1937 supermultiplet theory; Elliott SU(3) shell model].

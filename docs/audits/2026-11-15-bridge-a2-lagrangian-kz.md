# Bridge A, step A2: the Lagrangian's connection and the KZ connection

Date: 2026-11-15. Bean `qou-d0qq`. Audit: `derivation-chain-audit-2026-11-15.md` §2.5 (G2.1), §8 step 8.
Lean: `folio/quantum-observable-universe/lean/QOU/Mass/LagrangianKZIdentification.lean` (sorry-free;
`#print axioms` shows only `propext`, `Classical.choice`, `Quot.sound`).

## Result in one paragraph

The corpus's connection `∇` cannot be identified with KZ *as the corpus stands*, because it lives on
the algebra `A` of one universe and has no `n`-body base. With three explicit postulates (P1–P3
below) the identification is exact, not just up to gauge, and it is proved algebraically. The Dirac
operator `𝒟 = q⁻¹∇ + ℏ_q ι_ξ∇` is an invertible reweighting of `∇`, so it has the same flat
sections and the same monodromy. The only analytic input, Riemann–Hilbert, is needed only to leave
the Arnold class, and it is carried as one hypothesis structure.

## What is proved (Lean, any field unless noted)

1. **`𝒟` is `∇` reweighted.** Pointwise `𝒟 = P ∘ ∇` with `P φ = q⁻¹ φ + ℏ_q · η ⊗ φ(ξ)`, `η(ξ) = 1`.
   * `dirac_reeb`: the Reeb component is unchanged, `(𝒟s)(ξ) = (∇s)(ξ)`.
   * `dirac_transverse`: transverse components are scaled by `q⁻¹`.
   * `dirac_left_inverse`: `P` is inverted by the weights `(q, 1 − q)`.
   * `dirac_eq_zero_iff`: `𝒟s = 0 ⇔ ∇s = 0`. Flat sections, hence monodromy, agree.
   * `reweight_sum_eq_one_of_reeb`: `q⁻¹ + ℏ_q = 1` is *exactly* the condition that the Reeb
     component is preserved. This is the algebraic content of the corpus's "convex pair".
   * `reweight_comp_fibre`: `P` commutes with every fibre map, so `𝒟` is as isospin-blind as `∇`.
2. **Residues determine an Arnold-class form** (`arnoldCoeff_injective`, any infinite field). For
   `ω_M = Σ_{i<j} M_ij d log(z_i − z_j)` the functions on `Conf_n` determine every `M_ij`.
   The proof is partial-fraction uniqueness (`partialFraction_unique`) plus separation by
   functionals. `arnoldForm_eq_half_dlog` matches the sibling file's form exactly.
3. **Identification** `eq_kz_iff`: an Arnold-class form equals `ω_KZ = ℏ Σ Ω_ij d log(z_i − z_j)`
   on all of `Conf_n` iff its residues are `ℏ Ω_ij`.
4. **Constant gauge** `const_gauge_iff`: `g ω_M g⁻¹ = ω_N` iff `N_ij = g M_ij g⁻¹` for all `i ≠ j`.
5. **Euler/Reeb part** `arnold_euler`: `ι_E ω_M = ½ Σ_{i≠j} M_ij`, a constant. With item 1,
   `(𝒟s)(E) = E·s − ½ Σ_{i≠j} M_ij s`. The Reeb part of `𝒟` on the KZ sector is the total pair
   Casimir with no `q` weight; only the transverse part carries `q⁻¹`.
6. **Riemann–Hilbert, isolated** (`RiemannHilbertInput`, `gauge_equiv_kz_iff_monodromy`): a
   regular-singular flat connection is KZ up to gauge iff its monodromy is conjugate to the KZ
   monodromy, which by Drinfeld–Kohno (sibling A4 thread) is the `R`-matrix representation.

## The three postulates the corpus does not yet derive

* **P1, `n`-body base.** The `n`-particle sector is the trivial bundle `V^{⊗n}` over `Conf_n(ℂ)`,
  and the corpus's Reeb field `ξ` is the Euler field (its rotation part is the Reeb field of the
  link sphere). Nothing in `def:categorical-lagrangian` mentions `Conf_n`.
* **P2, two-body locality.** The connection form is in the Arnold class: a sum of pair terms with
  constant residues. This is what turns "residues" into "the connection".
* **P3, the residue.** The pair residue is `ℏ Ω_ij` (for `𝔰𝔩₂` fundamentals, `ℏ(s_ij − ½)`,
  matching `KohnoTwoPoint`).

Given P1–P3: `∇ = ∇_KZ` on the nose (item 3), flat for every `n` (sibling
`InfinitesimalPureBraid.casimir_curvature_zero`), vacuum ⇔ flat (`YangMillsVacuumFlat`), and `𝒟`
has the same flat sections (item 1). The 2026-10-11 verdict "as the corpus stands, it is not" is
confirmed and sharpened: what is missing is exactly P1–P3, and nothing else.

## Caution on the coordinator's phrasing

"A flat connection with Casimir residues is KZ up to gauge" is **not** a theorem in general. Inside
the Arnold class it holds with equality (item 3). Outside it, local data (residues up to
conjugacy) do not in general fix the gauge class: non-rigid Fuchsian systems with the same local
monodromy classes need not be gauge equivalent (Katz). The correct general statement goes through
monodromy (item 6). Whether residues equal to `Ω_ij` in a fixed trivialisation on every diagonal
already force the gauge class is left open; it is not needed if P2 is adopted.

## For Bridge B

The reweighting gives the corpus's two weights a geometric meaning: `q⁻¹` on directions
transverse to the Euler field, `1` on the Euler (Reeb) direction. On `𝒟²`, transverse–transverse
terms carry `q⁻²`, Reeb–Reeb terms `1`, mixed terms `q⁻¹`. This is a candidate origin for the
dressing ratios in `h1_hierarchy_origin.md`; it is **not** checked here, and it is stated only as
a lead.

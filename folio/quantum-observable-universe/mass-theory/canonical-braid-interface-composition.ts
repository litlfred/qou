import { definition } from "../../schema/builders";

/**
 * Inter-nucleon interface composition of the canonical atomic braid
 * β(Z, N) at H_{3A}(q), in the standard pppnnn ordering convention.
 *
 * The atomic braid β(Z, N) ∈ H_{3(Z+N)}(q) contains A − 1
 * inter-nucleon interface generators at positions σ_{3k+2}
 * (k = 0, ..., A − 2).  Each interface is one of three Hecke types:
 *
 *   - **pp interface** (proton ↔ proton): bare σ generator
 *   - **pn interface** (heterogeneous): averaged Δ_I = σ − h/2
 *     (the δ = 0 convention; the canonical colour-tube-weighted
 *     interface factor is σ − h(1/2 − δ/4), differing by hδ/4 —
 *     the counts below are independent of this choice)
 *   - **nn interface** (neutron ↔ neutron): inverse σ⁻¹
 *
 * Under the canonical pppnnn ordering (all Z protons first, then
 * all N neutrons), the interface counts are closed forms in (Z, N):
 *
 *   n_pp(Z, N) = max(0, Z − 1)
 *   n_nn(Z, N) = max(0, N − 1)
 *   n_pn(Z, N) = 1 if Z ≥ 1 and N ≥ 1 else 0
 *   total      = n_pp + n_pn + n_nn = A − 1
 *
 * This block formalises the empirical decomposition observed in
 * PR #656 v6 probe and lifts it from `interpretation` to a typed
 * structural definition.  Downstream propositions (e.g.
 * `Δ_coupling` residual fits) cite this definition when working
 * with the per-interface contributions.
 */
export default definition({
  label: "def:canonical-braid-interface-composition",
  title:
    "Canonical-braid interface composition $(n_{pp}, n_{pn}, n_{nn})$ for atom $(Z, N)$ in pppnnn ordering",
  uses: ["conj:flavor-split-substrate-mass"],
  cites: [],
  lean: {
    ref: "qou:QOU.BraidKnot.InterfaceComposition",
    validation: "stub",
  },
  tags: [
    "canonical-braid",
    "interface-composition",
    "pp-pn-nn",
    "z-n-asymmetry",
    "hecke",
    "infrastructure",
  ],
  computation: {
    engine: "python",
    script:
      "computations/interface_composition.py",
    witness:
      "computations/canonical-braid-interface-composition.witness.json",
    status: "verified",
  },
});

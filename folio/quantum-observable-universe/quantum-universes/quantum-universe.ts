import { definition } from "../../schema/builders";

export default definition({
  label: "def:quantum-universe",
  title: "Quantum Universe",
  tags: ["category-theory", "quantum"],
  lean: { ref: "qou:QOU.QuantumUniverse",
    validation: "not_checked",
  },
  // `def:frobenius-hopf-substrate` dropped from uses[] 2026-08-09 (decision
  // 5). It was a POINTER, not an editorial dependency: axiom 2 below spells
  // out the whole Frobenius–Hopf datum inline (μ, Δ, η, ε, S and the
  // categorical action ρ_V), so a reader can follow this definition without
  // having read the substrate block. The prose anchor
  // [Frobenius–Hopf algebra](#def:frobenius-hopf-substrate) stays in the .md —
  // that is legitimate storytelling.
  //
  // Relocating the substrate block instead would not have helped: the uses[]
  // graph carries a genuine 3-cycle
  //   def:quantum-universe → def:frobenius-hopf-substrate
  //     → def:frobenius-pairing → def:quantum-universe
  // (frobenius-hopf-substrate.ts:9, frobenius-pairing.ts:10), and no
  // placement orders a cycle — co-locating its members would only hide the
  // cross-chapter edge from the classifier rather than fix it. The block also
  // sits in the path of the decision-1/decision-2 errata (its axiom 4 IS the
  // non-degeneracy that convention D violates), so it must not be relocated
  // in the same round as its mathematical restatement.
  uses: ["def:rigid-monoidal-category", "def:frobenius-hopf-substrate", "def:snake-identity"],
  examples: ["ex:quantum-universe-su2"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/quantum-universe-0.svg", blockIndex: 0, hash: "7d5b5776ad75" },
  ],

});

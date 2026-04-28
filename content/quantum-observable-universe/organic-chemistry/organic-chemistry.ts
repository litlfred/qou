import { chapter, section } from "../../schema/builders";

/**
 * Chapter 10: Organic Chemistry from Hopf Chains.
 *
 * Carbon's half-filled second shell (4 open linking sites) gives it
 * unique chain-forming ability.  This chapter develops the theory of
 * molecular Hopf chains and threaded rings, introduces the threading
 * link T(2,N) whose Alexander polynomial halves the crossing energy,
 * and compares the predicted C₆ chain → benzene barrier to experiment
 * with no free parameters.
 */
export default chapter({
  title: "Organic Chemistry from Hopf Chains",
  label: "chap:organic-chemistry",
  sections: [
    // ── §1. The molecular crossing-energy quantum ────────────────────
    section({
      title: "The molecular crossing-energy quantum",
      label: "sec:molecular-crossing-quantum",
      blocks: [
        "molecular-crossing-quantum",
        "prf-molecular-crossing-quantum",
        "trefoil-volume-electronic-scale",
        "prf-trefoil-volume-electronic-scale",
      ],
    }),

    // ── §2. Covalent bonding as shared sub-Hopf links ────────────────
    section({
      title: "Covalent bonding as shared sub-Hopf links",
      label: "sec:covalent-bonding",
      blocks: [
        "covalent-bond-types",
        "carbon-valence",
      ],
    }),

    // ── §3. Molecular Hopf chains and rings ──────────────────────────
    section({
      title: "Molecular Hopf chains and rings",
      label: "sec:molecular-chains-rings",
      blocks: [
        "molecular-hopf-chain",
        "threading-link",
        "molecular-hopf-ring",
        "chain-spring-modes",
        "ring-closure-barrier",
      ],
    }),

    // ── §4. Topological invariants of T(2,N) ─────────────────────────
    section({
      title: "Topological invariants of $T(2,N)$",
      label: "sec:t2n-invariants",
      blocks: [
        "alexander-T2N-closed-form",
        "prf-alexander-T2N-closed-form",
        "T2N-components",
        "prf-T2N-components",
        "threading-half-weight",
        "prf-threading-half-weight",
      ],
    }),

    // ── §5. Energy predictions for even-N rings ──────────────────────
    section({
      title: "Energy predictions for even-$N$ rings",
      label: "sec:even-N-energy-predictions",
      blocks: [
        "ring-closure-barrier-quantitative",
        "prf-ring-closure-barrier-quantitative",
        "even-N-barrier-spectrum",
        "prf-even-N-barrier-spectrum",
        "c6-energy-comparison",
        "prf-c6-energy-comparison",
        "benzene-resonance-from-threading",
        "prf-benzene-resonance-from-threading",
      ],
    }),

    // ── §6. Odd-N rings and the Hückel bridge ────────────────────────
    section({
      title: "Odd-$N$ rings and the Hückel bridge",
      label: "sec:odd-N-and-huckel",
      blocks: [
        "torus-knot-T2-odd-alexander",
        "odd-N-ring-barrier",
        "prf-odd-N-ring-barrier",
        "huckel-from-T2N-invariant",
        "prf-huckel-from-T2N-invariant",
      ],
    }),

    // ── §7. Carbon chains and benzene ────────────────────────────────
    section({
      title: "Carbon chains and benzene",
      label: "sec:carbon-chains-benzene",
      blocks: [
        "carbon-chain-c6",
        "benzene-ring",
        "chain-ring-energy",
        "chain-ring-comparison",
        "benzene-resonance-verification",
      ],
    }),

    // ── §8. Organic chain taxonomy ───────────────────────────────────
    section({
      title: "Organic chain taxonomy",
      label: "sec:organic-taxonomy",
      blocks: [
        "organic-chain-taxonomy",
        "hydrogen-capacity",
        "prf-hydrogen-capacity",
        "bond-order-energy-formula",
        "prf-bond-order-energy-formula",
      ],
    }),

    // ── §9. Heteroaromatic extension ─────────────────────────────────
    section({
      title: "Heteroaromatic extension",
      label: "sec:heteroaromatic",
      blocks: [
        "heteroaromatic-alexander",
        "prf-heteroaromatic-alexander",
      ],
    }),
  ],
});

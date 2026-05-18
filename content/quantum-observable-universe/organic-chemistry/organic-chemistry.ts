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
    // ── §1. Covalent bonding as shared sub-Hopf links ────────────────
    section({
      title: "Covalent bonding as shared sub-Hopf links",
      label: "sec:covalent-bonding",
      blocks: [
"covalent-bonding-intro",
        "covalent-bond-types",
        "carbon-valence",
      ],
    }),

    // ── §2. Molecular Hopf chains and rings ──────────────────────────
    section({
      title: "Molecular Hopf chains and rings",
      label: "sec:molecular-chains-rings",
      blocks: [
"molecular-chains-rings-intro",
        "molecular-hopf-chain",
        "threading-link",
        "molecular-hopf-ring",
        "chain-spring-modes",
        "ring-closure-barrier",
      ],
    }),

    // ── §3. Carbon chains and benzene ────────────────────────────────
    section({
      title: "Carbon chains and benzene",
      label: "sec:carbon-chains-benzene",
      blocks: [
"carbon-chains-benzene-intro",
        "carbon-chain-c6",
        "benzene-ring",
        "chain-ring-energy",
        "chain-ring-comparison",
      ],
    }),

    // ── §4. Organic chain taxonomy ───────────────────────────────────
    section({
      title: "Organic chain taxonomy",
      label: "sec:organic-taxonomy",
      blocks: [
"organic-taxonomy-intro",
        "organic-chain-taxonomy",
      ],
    }),
  ],
});

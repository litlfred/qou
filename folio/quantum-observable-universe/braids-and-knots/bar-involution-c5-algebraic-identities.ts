import { remark } from "../../schema/builders";

export default remark({
  label: "rem:bar-involution-c5-algebraic-identities",
  interprets: "def:bar-involution",
  title:
    "Bar-symmetric algebraic identities: half-step factorization of $h$, Hoefsmit-Quantum-2 ($b^2 = 1 - 1/[2]_q^2$), and the $c_5$ closed form",
  uses: [
    "def:bar-involution",
    "prop:c5-involution-leibniz-decomposition",
    "prop:silver-ratio-beta-decay-null",
  ],
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-08-09",
      body:
        "**Corrected: the second factor is not $1/z$.** This remark " +
        "previously identified $q^{1/2}+q^{-1/2}$ as $1/z$. Written that " +
        "way, the identity escaped every search for the convention-C " +
        "formula for $z$, which is why the excision needed a second pass to " +
        "reach it \u2014 the number was right there under a name that did " +
        "not match what was being looked for. The prose above states the " +
        "distinction; that an earlier version asserted the identification " +
        "is recorded here per \u00a74d.",
    },
  ],
  tags: [
    "bar-invariance",
    "c5",
    "hoefsmit-quantum-2",
    "skein",
    "wedderburn",
  ],
  computation: {
    engine: "python+mpmath",
    script: "computations/probes/markov_bond_rule_forces_pairwise_probe.py",
    witness: [
      "computations/probes/markov-bond-rule-forces-pairwise.witness.json",
      "computations/probes/option-e-v9-bar-symmetric-test-probe.witness.json",
    ],
    status: "verified",
  },
});

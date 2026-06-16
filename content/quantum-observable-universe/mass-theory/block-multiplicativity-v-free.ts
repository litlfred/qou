import { remark } from "../../schema/builders";

export default remark({
  label: "rem:block-multiplicativity-v-free",
  interprets: "prop:atomic-mass-gb-nf",
  title:
    "Block-multiplicativity of per-generator $\hat{V}$ on the disjoint Hecke product",
  lean: {
    ref: "qou:QOU.BraidKnot.BlockMultiplicativityVFree",
    validation: "not_checked",
  },
  uses: [
    // broken-ref removed (Phase 7): def:ew-interface-knot
    "prop:atomic-mass-gb-nf",
    "thm:jones-markov-trace",
  ],
  computation: {
    engine: "python",
    script:
      "computations/binding_block_multiplicative.py",
    witness:
      "computations/binding-block-multiplicative.witness.json",
    status: "verified",
  },
  tags: [
    "wedderburn",
    "block-multiplicativity",
    "disjoint-hecke-product",
    "constituent-vacuum",
    "interface-knot",
    "scaling",
  ],
  authorNotes: [
    {
      kind: "status",
      body: "**Conjecture** — empirically verified to 4 digits at $A \\in \\{2, 3\\}$,\nclassical-limit ($q = 1$) proven via Plancherel duality. Lean class\n[`qou:QOU.BraidKnot.BlockMultiplicativityVFree`](https://github.com/litlfred/qou/blob/claude/log-delta-categorical-derivation/content/quantum-observable-universe/lean/QOU/BraidKnot/BlockMultiplicativityVFree.lean)\naxiomatises the q-deformed identity as a Lean *class hypothesis*\n(`q_schur_duality_holds_at` predicate field, per CLAUDE.md §3b-cond)\n— **not a `sorry`**. The file contains 0 sorries; the open\nq-deformation step is encoded as a typeclass constraint that\ndownstream theorems consume via `[Instance]`. Downstream\nconsequences (the closed-form $B^{(1)}_{\\text{dim}}$) are then\nfully verified by Lean modulo this single class-axiomatised\nconjectural input.\n\nFalsifiability: a single H_12 (${}^{4}$He) computation showing $V^{(12)}_g$ on\na proton block differs from $V^{(6)}_g$ on the same proton block by\nmore than $10^{-3}$ at $q_0$ refutes the conjecture. The ${}^{4}$He H_12\ncharacter sum requires $> 12$ GB RAM on commodity hardware and\n~5 minutes; deferred to a Rust geck_pfeiffer kernel port\nor a larger-RAM host.",
    },
  ],
});

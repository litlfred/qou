import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:block-multiplicativity-v-free",
  title:
    "Block-multiplicativity of per-generator $\\hat{V}$ on the disjoint Hecke product",
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
    witness: [
      "computations/binding-block-multiplicative.witness.json",
      "computations/probes/h2_gg_electron/h2-gg-electron.witness.json",
    ],
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
      body: "**Conjecture** — empirically verified to 4 digits at $A \\in \\{2, 3\\}$,\nclassical-limit ($q = 1$) proven via Plancherel duality. Lean class\n[`qou:QOU.BraidKnot.BlockMultiplicativityVFree`](https://github.com/litlfred/qou/blob/claude/log-delta-categorical-derivation/folio/quantum-observable-universe/lean/QOU/BraidKnot/BlockMultiplicativityVFree.lean)\naxiomatises the q-deformed identity as a Lean *class hypothesis*\n(`q_schur_duality_holds_at` predicate field, per AGENTS.md §3b-cond)\n— **not a `sorry`**. The file contains 0 sorries; the open\nq-deformation step is encoded as a typeclass constraint that\ndownstream theorems consume via `[Instance]`. Downstream\nconsequences (the closed-form $B^{(1)}_{\\text{dim}}$) are then\nfully verified by Lean modulo this single class-axiomatised\nconjectural input.\n\nFalsifiability: a single H_12 (${}^{4}$He) computation showing $V^{(12)}_g$ on\na proton block differs from $V^{(6)}_g$ on the same proton block by\nmore than $10^{-3}$ at $q_0$ refutes the conjecture. The ${}^{4}$He H_12\ncharacter sum requires $> 12$ GB RAM on commodity hardware and\n~5 minutes; deferred to a Rust geck_pfeiffer kernel port\nor a larger-RAM host.",
    },
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "**§7c base-ring note — deliberate two-sided placement.** The Lean " +
        "sibling's mathematical content is **already generic**: " +
        "`blockFactorProduct`, `blockFactorProduct_add`, " +
        "`blockFactorProduct_proton` and `blockFactorProduct_neutron` are all " +
        "stated over `{R : Type*} [CommSemiring R]` and closed by `ring` / " +
        "`simp`. The file's single `ℝ` is the empirical ratio check " +
        "`(0.7084 : ℝ) / 0.6005 < 1.2 ∧ (0.7084 : ℝ) / 0.6005 > 1.15` — a " +
        "comparison of **computed V̂ values** against a numeric window, i.e. " +
        "exactly the \"experimental / numerical evaluation\" `ℝ` row of §7c. " +
        "Generic construction plus its numerical realisation, coexisting on " +
        "purpose; the mixed-signal flag records the coexistence rather than a " +
        "misplacement.",
    },
  ],
});

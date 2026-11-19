import { table } from "../../schema/builders";
export default table({
  label: "tbl:q-beta-spectral-bridge-table-data",
  title: "Numerical evaluation of $\\mathfrak{Q}_\\beta$ spectral-bridge invariants at the proton-anchored parameter $q_0$",
  uses: ["prop:q-beta-spectral-bridge"],
  tags: ["extracted-table"],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-09-05",
      body: "**⚠ Retraction (2026-09-05).** A caveat here said $h^2 = 0.04370621823290131$\n\"carries a retired $q_0$\" and that this table was internally inconsistent.\n**Both are withdrawn.** $h^2$ is exactly $(h)^2$ as published — they agree to\n$9.0\\times10^{-18}$ — and every value in the table reproduces from the quoted\n$q_0$ with the proposition's own $z$. The earlier claim came from matching\n$h^2$ against closed forms at three candidate pins, where the significant-figure\nbucketing was too coarse to separate them. The table is self-consistent; what\nis not is its relationship to the producer, above.",
    },
    {
      kind: "caveat",
      date: "2026-09-05",
      body: "**⚠ The provenance sentence that stood here was false, and the divergence it\nhid is 21 %** (measured 2026-09-05, `qou-i229`). It read: *\"Values are the\ndisplayed digits of the 50-dps witness `q-beta-spectral-bridge.witness.json`,\nregenerated from the canonical CAL-2 pinning `q-pinning-50-digit.witness.json`.\"*\nThe witness contains **none** of these values and declares\n`q0Anchor: proton`, not the canonical CAL-2 (muon) pinning.\n\n| | this table | the witness |\n|---|---|---|\n| $q_0$ | $1.109978595557335$ | $1.1099785827513808\\ldots$ (proton) |\n| $z$ | $0.4993203340335613$ | $0.6126880371464652\\ldots$ |\n| $\\ln(1+zh)$ | $0.09929139859972778$ | $0.1205248238414840\\ldots$ |\n| predicted bridge | $1.897907634269324$ | $1.5660730493910099\\ldots$ |\n\nEach side reproduces its own numbers exactly, so this is **two different\ncomputations**, not drift: the bridge ratio differs by $21.2\\,\\%$.\n\n**Which side is stale: the table, not the producer.** An earlier version of\nthis note said the producer had drifted from the stated definition. That is\n**backwards and withdrawn.** The proposition's\n$z = 1/(\\sqrt q + 1/\\sqrt q)$ is convention **C**, *excised* by the owner\nruling of 2026-08-09; the producer's $q^3/(q^2+1)$ is convention **D**, which\nthe registry records as the definitional convention for `qbeta-decay` per the\nruling of 2026-08-15. So the producer moved to the ruled convention and the\nproposition was left behind — the ordinary C→D content lag, not its inverse.\nMigration tracked as `qou-cds1`.\n\nThe table does faithfully follow its proposition:\n[`prop:q-beta-spectral-bridge`](#prop:q-beta-spectral-bridge) *defines*\n$z := 1/(\\sqrt q + 1/\\sqrt q)$, which is what these values use;\n`q_beta_spectral_bridge_witness.py` computes $q^3/(q^2+1)$ instead — and\nstores it under the field name `z_markov_jones`, while the proposition calls\n*its* $z$ \"the Markov–Jones parameter\". **The same name for two formulas is\nwhat hid this**, and both of the witness's assertions PASS, because a producer\nchecking itself against itself cannot see that it has drifted from the block\nit names in `contentBlock`.\n\nWhich $z$ is right is an authoring question and is **not** settled here; the\n$\\mathfrak{Q}_\\beta$ figures differ by $\\sim 0.05$ MeV between the two\nreadings. Nothing in this table, the proposition or the producer has been\nchanged — only this sentence, which was false under either reading.\n`the_qbeta_bridge_table_and_its_witness_compute_different_z_probe.py`.",
    },
  ],
});

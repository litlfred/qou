import { table } from "../../schema/builders";
export default table({
  label: "tbl:hecke-log-decomposition-table-data",
  title: "Hecke logarithmic decomposition",
  tags: ["extracted-table"],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-08-08",
      body:
        "**This table has no source block.** It carried " +
        "`uses: [\"prop:hecke-log-decomposition\"]`, and no block with that " +
        "label exists anywhere in the corpus — the chapter manifest lists only " +
        "this extracted table. The reference was dropped rather than " +
        "re-pointed: `uses[]` is the editorial relation, so guessing a " +
        "plausible parent would fabricate the edge that ordering metrics are " +
        "computed from.\n\n" +
        "The title had the same defect, reading `Data table from " +
        "prop:hecke-log-decomposition` — an internal label in published prose. " +
        "Replaced with the subject it names.\n\n" +
        "What is actually missing is the proposition this table was extracted " +
        "from. Until it is written the table stands alone, which is what the " +
        "block now says rather than pointing at nothing.",
    },
    {
      kind: "status",
      date: "2026-09-05",
      body: "**Refreshed to the live muon pin, 2026-09-05** (`qou-i229`, owner-approved).\nAll seven rows moved together. Producer:\n[`retired_q0_refresh_to_live_muon_pin_probe.py`](computations/probes/retired_q0_refresh_to_live_muon_pin_probe.py)\n(5/5).\n\nThe table previously read\n\n| figure | was | now |\n|---|---|---|\n| $h(q_0)$ | $0.20906032199$ | $0.20906032215$ |\n| $\\hbar_q(q_0)$ | $0.09908172644$ | $0.09908172651$ |\n| $1 + q_0$ | $2.10997859556$ | $2.10997859564$ |\n| $\\log(1/h(q_0))$ | $1.56513244670$ | $1.56513244593$ |\n| $\\log(1/\\hbar_q(q_0))$ | $2.31181024982$ | $2.31181024912$ |\n| $\\log(1 + q_0)$ | $0.74667780313$ | $0.74667780319$ |\n\ncomputed at $q_0 = 1.1099785955541805\\ldots$ — the **CODATA-2018 vintage of\nthe muon pin**, recovered by inverting CAL-2 at $m_\\mu/m_e = 206.7682830$. The\n2026-08-15 substrate fix that moved to the NIST table reached `computations/`\nand `tools/` and not `content/`. New pin\n$q_0 = 1.10997859564273904668\\ldots$, from `q-pinning-50-digit.witness.json`;\nthe shift is $8.0 \\times 10^{-11}$ relative and nothing physical moves.\n\n**All seven rows, not the three a sweep found.** An earlier pass substituted\nonly the flagged figures and was reverted: the unflagged rows are $q_0$-derived\ntoo — they merely had *some* provenance, so the no-provenance sweep never saw\nthem — and refreshing one column while its siblings stay behind leaves a table\nthe reader cannot recompute from itself, which is worse than the stale value.\n\n**Three rows were also wrong at their own anchor**, independently of the pin:\n$1 + q_0$ ($2.10997859556$ against $\\ldots555$), $\\log(1/\\hbar_q)$\n($\\ldots982$ against $\\ldots985$) and $\\log(1 + q_0)$ ($\\ldots313$ against\n$\\ldots315$) — $1$–$3 \\times 10^{-11}$, neither the rounding nor the\ntruncation of the retired value. Corrected here by construction.",
    },
  ],
});

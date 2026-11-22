import { table } from "../../schema/builders";
export default table({
  label: "tbl:q-beta-form-a-n1-symbolic-table-data",
  title: "Symbolic form of $Q_\\beta$ at $A$, $N=1$",
  tags: ["extracted-table"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-09-05",
      body: "**Refreshed to the live muon pin, 2026-09-05** (`qou-i229`, owner-approved) —\n**partially.** Producer:\n[`retired_q0_refresh_to_live_muon_pin_probe.py`](computations/probes/retired_q0_refresh_to_live_muon_pin_probe.py)\n(5/5).\n\n| figure | was | now |\n|---|---|---|\n| $q_0$ (header) | $1.109978595554181$ | $1.109978595642739$ |\n| $\\hbar_q$ | $0.099081726435699$ | $0.099081726507578$ |\n| $1 + \\hbar_q^2$ | $1.009817188513479$ | $1.009817188527722$ |\n\nThe old pin was the **CODATA-2018 vintage of the muon anchor**; the shift is\n$8.0 \\times 10^{-11}$ relative. The per-braid ceiling $\\hbar_q^4/(1-\\hbar_q^2)\n= 97.3$ ppm is unchanged at its stated precision.\n\n**⚠ The $E_0$ and $\\mathfrak{Q}_\\beta$ rows are NOT refreshed, deliberately.**\nThey are producer outputs of the $q_\\beta$ channel, whose values depend on the\n**trace convention** as well as on $q_0$ — and that channel's C→D migration is\ntracked separately as `qou-cds1`, where the $\\mathfrak{Q}_\\beta$ figures move by\n$\\sim 0.05$ MeV. Refreshing a pin underneath a convention that is itself about\nto change would produce numbers nobody has checked. Those rows must be\nregenerated from the producer under D, in one pass, not substituted here.\n\nSo this table currently mixes a **refreshed** $\\hbar_q$ against\n**unrefreshed** $E_0$ and $\\mathfrak{Q}_\\beta$. That is the state the\nper-block rule warns about, and it is accepted here only because the remaining\nrows need a convention decision rather than an arithmetic one — recorded so it\nis not mistaken for completion.",
    },
    {
      kind: "caveat",
      date: "2026-08-08",
      body:
        "**This table has no source block.** It carried " +
        "`uses: [\"prop:q-beta-form-a-n1-symbolic\"]`, and no block with that " +
        "label exists in the corpus. Dropped rather than re-pointed, for the " +
        "same reason recorded on `tbl:hecke-log-decomposition-table-data`: " +
        "`uses[]` is editorial, and an invented parent is worse than none.\n\n" +
        "The title read `Data table from prop:q-beta-form-a-n1-symbolic`, " +
        "carrying the internal label into published prose; replaced with the " +
        "quantity it tabulates.",
    },
  ],
});

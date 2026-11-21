import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:q-beta-spectral-bridge",
  lean: {
    ref: "qou:QOU.Interactions.q_beta_spectral_bridge",
    validation: "not_checked",
  },
  title:
    "$\\mathfrak{Q}_\\beta$ spectral bridge: Form A (NF counit) and Form B (transfer-matrix log-ratio) are the same observable in different bases",
  uses: ["prop:neutron-qvalue-symbolic"],
  cites: [
    "wenzl1988",
    "jones1985",
  ],
  computation: {
    engine: "mpmath",
    script: "computations/gram-matrix-dual.py",
    witness: "computations/gram-matrix-dual.witness.json",
    status: "verified",
  },
  tags: [
    "q-beta",
    "spectral-bridge",
    "basis-change",
    "markov-parameter",
    "eigenfunction-dampening",
    "beta-decay",
    "prediction",
  ],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-21",
      body:
        "**Demoted from prop: to conj: (owner card, 2026-11-21, \"Demote both\").** " +
        "The Lean `q_beta_spectral_conditional` returns `Q_beta_A = Q_beta_B` from a class field, and Form A is the retired z = 1 cell. " +
        "The proof block is now the sketch rem:q-beta-spectral-bridge-sketch. Issue #8911, PR #8912.",
    },
    {
      kind: "refined-framing",
      date: "2026-09-05",
      body: "**Migrated C → D, 2026-09-05** (`qou-i229` → `qou-cds1`, owner-approved:\n*\"refresh and migrate\"*). The definition above read\n$z := 1/(\\sqrt q + 1/\\sqrt q) = 0.4993\\ldots$ — convention **C** of the\n[trace-convention registry](../../../docs/coordination/trace-convention-registry.md),\nmarked there *EXCISED 2026-08-09*\n([reconciliation](#rem:markov-z-reconciliation)). It is now\n$z = q^3/(q^2+1) = 0.6127\\ldots$, convention **D**, which the registry records\nas this channel's **definitional** convention per the owner ruling of\n2026-08-15 (*\"convention D is convention. excise convention C\"*), with C\n**structurally excluded** — in D the loop values satisfy $z\\,z_- = 1/[2]_q^2$\nand the framing ratio is the monomial $a = q^2$, while C admits no such\nfactorisation.\n\n**The table was migrated from the producer, not by hand.** Every value in\n[the data table](#tbl:q-beta-spectral-bridge-table-data) now comes from\n`q-beta-spectral-bridge.witness.json`, which has computed $q^3/(q^2+1)$ all\nalong — the divergence measured here on 2026-09-05 was 21 % between a C-frame\ntable and a D-frame producer, with both witness assertions passing because a\nproducer checking itself against itself cannot see that it has drifted from the\nblock it names.\n\n**The anchor moved too, and that is also executed rather than decided.** The\ntable was on muon pin A; the producer is on the **proton** pin, migrated\n2026-08-29 under `qou-cds3` with the authorisation recorded there — AGENTS.md\n§\"q₀ anchor convention\", *\"we want proton unless for an explicit reason … fix\nall, even if not visible\"*. So both axes were already ruled and the block\nsimply had not followed.\n\n**What moved.** $\\mathfrak{Q}_\\beta^{\\mathrm{A}}$ is essentially unchanged at\n$0.7836$ MeV, but $\\mathfrak{Q}_\\beta^{\\mathrm{B}}$ moves $0.8324 \\to 0.8234$\nMeV and the A/B disagreement **improves** from $0.0487$ to $0.0398$ MeV against\nthe same $h^2 E_0 = 0.183$ MeV bound. The bridge ratio moves $1.898 \\to 1.566$,\nwhich is the $1/z$ term following the convention.\n\nAnalysis: [`docs/audits/2026-09-05-which-z-does-the-qbeta-spectral-bridge-intend.md`](../../../docs/audits/2026-09-05-which-z-does-the-qbeta-spectral-bridge-intend.md).",
    },
    {
      kind: "status",
      body: "* **Superseded 2026-11-21:** Form A is no longer the canonical predictor. It is the retired $z = 1$ cell (AGENTS.md, Q_β scoping note of 2026-09-05), and the owner ruled on 2026-11-20 that Q_β is derived from γγ pair production, with the T³ weight-split value as the scored cell (`docs/coordination/owner-rulings.md`). The $+0.168\\%$ figure belongs to that retired cell.\n* Form B is mathematically equivalent via the bridge above; it is\n  retained because the eigenfunction basis is the natural one for\n  $N \\geq 1$ truncation analysis and for the general atom-level\n  binding cascade (where the brane-tower truncation is non-trivial).\n* The exponential-remainder bound is the open conjectural input\n  (conj:archimedean-remainder-exponential-decay);\n  the Taylor-expansion algebra above is unconditional.",
    },
  ],
});

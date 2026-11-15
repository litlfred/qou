import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
    {
      kind: "caveat",
      date: "2026-10-10",
      body:
        "**Convention-C site, and no detector in the repo can see it.** Measured against `main`: " +
        "`4993/10000` is the rounded $z_C$, so the convention survives here as an *integer numerator* " +
        "folded into the closed form's coefficients — there is no `z` symbol, no `Real.sqrt`, and no " +
        "`markovZ`-shaped definition anywhere in the sibling `.lean`. Both `convention-c-producer-audit.py` " +
        "and `scripts/lean-markov-convention-audit.py` report the file clean, verified by running them; " +
        "a structural scan of the whole tree for this spelling finds this declaration and its provenance " +
        "audit doc and nothing else. Recorded as a detector blind spot alongside the re-derivation under " +
        "$z_D$ in bean `qou-wgta`, whose critical item 2 this is — the other three criticals it names " +
        "(`borromean_binding_recompute.py`, `y_lambda_wenzl_bridge.py`, `hecke/hecke_symbolic.py`) are all " +
        "fixed. The coefficients are `10000·(z q² + 2q − z)`, `5000·(q² − 2z q − 1)` and " +
        "`10000·(q² − z q − 1)` at `z = z_C`; do **not** substitute $z_D$ into them to improve the " +
        "residual, which would pick a convention by its miss.",
    },
    {
      kind: "status",
      date: "2026-11-15",
      body:
        "**Switched to convention D (owner ruling 2026-11-15: replace convention-C values with " +
        "convention D even if worse).** This supersedes the 2026-10-10 caveat's instruction not to " +
        "substitute $z_D$. The Lean closed form is now written in `z` and evaluated at " +
        "`zD = q0^3/(q0^2+1)`; the pins are Phi(uud) = -0.614886, Phi(udd) = -0.896395 (50 dps), " +
        "model value 1.0541 MeV, -18.5 % vs CODATA. The convention-C 1.302 MeV (+0.64 %) stays in " +
        "the prose only as a labelled historical comparison.",
    },
  ],
  label: "prop:neutron-proton-mass-splitting",
  title: "Neutron--proton mass splitting from quark crossing change",
  lean: { ref: "qou:QOU.NeutronProtonSplitting.splitting_value",
    validation: "not_checked",
  },
  uses: ["thm:wedderburn-mass-formula"],
});

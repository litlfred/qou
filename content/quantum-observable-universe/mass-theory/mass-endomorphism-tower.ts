import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:mass-endomorphism-tower",
  title:
    "Proton--electron mass ratio from the $\\Phi_q$ tower",
  lean: { ref: "qou:QOU.MassEndomorphism.proton_electron_ratio",
    validation: "not_checked",
  },
  uses: [
    "rem:kashaev-volume-density",
    "rem:photon-channel-wedderburn-chain",
  ],
  computation: {
    engine: "mpmath",
    script: "computations/habiro/habiro_exact_mass_endomorphism.py",
    witness: "computations/habiro/habiro-exact-mass-endomorphism.witness.json",
    status: "experimental",
  },
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-06-22",
      body:
        "**Trace-convention + dilog reconciliation (z-Habiro thread).** " +
        "Reconciled against the channel-level audit (PR #2481) and the " +
        "Phi_q-wire refutation verdict (2026-06-18). (1) The descended term " +
        "|prod V_i^full| is the REGULAR-REPRESENTATION (Wedderburn) trace " +
        "tr_reg = sum_lambda (d_lambda^2/|S_3|) chi_lambda — the trace of the " +
        "left-multiplication endomorphism (def:hecke-mass-element) — NOT the " +
        "Jones-Markov trace tr_M = prod V_i^std (they differ ~10% at q_0: " +
        "tr_reg ~ 0.960 vs tr_M ~ 1.065 for the proton); the term-1 label is " +
        "corrected in the body. (2) The boxed proposition and the production " +
        "pipeline (canonical_plus_multibrane, tower_mode=li2q) use the bounded " +
        "symmetric -Li_2^q(-|V_i|); the explanatory term-bullets, the Application " +
        "section, and the block title still display the SUPERSEDED Faddeev Phi_q " +
        "(the root-of-unity face — it blows up to 1e2-1e6 at the physical " +
        "|V_i^full| and is diagnostic-only). Updating those displays to li2q " +
        "awaits an mp recompute. (3) Weights are the q-deformed (dim_q)^2/[3]_q! " +
        "per the production code, not the classical d_lambda^2/|S_3|. See the " +
        "bounded-Rogers-continuation direction doc + the 2026-06-18 verdict.",
      see: "docs/audits/2026-06-22-zhabiro-bounded-rogers-continuation-direction.md",
    },
  ],
});

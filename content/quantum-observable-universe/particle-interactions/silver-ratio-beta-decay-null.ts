import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:silver-ratio-beta-decay-null",
  proofs: ["prf:silver-ratio-beta-decay-null"],
  lean: {
    ref: "qou:QOU.ParticleInteractions.SilverRatioBetaDecayNull",
    validation: "not_checked",
  },
  title:
    "**Silver-ratio $\\beta$-decay null**: at $q = 1 \\pm \\sqrt{2}$, the categorical $\\beta$-decay $Q$-value vanishes; the Hecke generator $\\sigma$ has eigenvalues = $1 \\pm \\sqrt{2}$ (silver-ratio self-referential fixed point); proton and neutron Markov-traces become categorically indistinguishable",
  uses: ["rem:per-block-hopf-jones-absorption-pattern"],
  cites: [
    "wenzl1988",
    "hoefsmit1974",
  ],
  tags: [
    "lean-infrastructure",
    "silver-ratio",
    "beta-decay-null",
    "hecke-quadratic",
    "pell-lucas",
    "categorical-degeneracy",
  ],
  computation: {
    engine: "python",
    script: "computations/qbeta/qbeta_silver_ratio_pell_lucas_ck.py",
    witness: [
      "computations/qbeta/qbeta-silver-ratio-pell-lucas-ck.witness.json",
    ],
    status: "experimental",
  },
  authorNotes: [
    {
      kind: "status",
      body: "The silver-ratio observation:\n\n1. **Identifies the algebraic landscape of $\\mathfrak{Q}_\\beta$**: silver-ratio\n   (Pell-Lucas), NOT cyclotomic (as in FSC = $q \\cdot [9]_q \\cdot [10]_q$)\n   or simple q-rational (as in $G_q = q^2/(q-1)^4$).\n2. **Provides a clean test point** for $c_k$ closed forms:\n   evaluating at $q = 1 + \\sqrt{2}$ should give Pell-Lucas-clean\n   rationals if the form is categorically correct.\n3. **Flags $c_5$ as the loose rung**: 4/5 c_k pass the silver-ratio\n   Pell-Lucas test; $c_5$ fails. This is consistent with the\n   2.4% residual gap for $c_5$ at $q_0$ noted in\n   [`docs/audits/-c-k-comprehensive-reference.md`](../../../docs/audits/-c-k-comprehensive-reference.md).\n4. **Hints at categorical source**: the Hecke quadratic's\n   self-referential fixed point structure at silver ratio\n   ($\\sigma$-eigenvalues = $q^{\\pm 1}$) suggests $c_k$ derivations\n   should pass through the Pell recursion $a_{n+1} = 2a_n + a_{n-1}$\n   acting on the V_(2,1) seminormal basis.",
    },
    {
      kind: "status",
      body: "This is a **structural identification**, not a derivation of $c_k$\nfrom first principles. The silver-ratio limit gives a clean test\npoint and identifies the relevant algebraic landscape (Pell-Lucas\nextension of $\\mathbb{Q}$), but the actual closed forms for\n$c_4..c_7$ remain empirical conjectures (see\n[`prop:qbeta-c-k-closed-forms`](#prop:qbeta-c-k-closed-forms)).",
    },
  ],
});

import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:rho-k-h3a-refinement",
  title:
    "$H_{3A}$ Wedderburn refinement of the categorical density $\\rho_K$ beyond leading-order",
  lean: {
    ref: "qou:QOU.BraidKnot.rho_k_h3a_refinement",
    validation: "not_checked",
  },
  uses: [
    // conj:hoefsmit-scattering-pipeline removed (qou-tm3c): the statement supposes the refinement balance and divides by |tr_M|; the Hoefsmit pipeline is not used.
    "prop:y-lambda-closed-form-wenzl-bridge",
  ],
  cites: ["wenzl1988", "hoefsmit1974", "kassel1995"],
  tags: [
    "rho-k",
    "wedderburn",
    "H_3A",
    "plancherel",
    "wenzl-bridge",
    "hoefsmit",
    "1ppb",
    "derivation",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The Lean sibling records that refutation as `not_rhoKH3ARefinementNaive`." },
    {
      kind: "note",
      date: "2026-09-04",
      body:
        "**Archimedean specialisation (§7c).** The Lean sibling states the atom-data tuple over `ℝ` rather than a generic `{R : Type*} [CommRing R]`. This is the §7c-correct side of the wall: `ρ_K(q₀)`, `ρ_K^LO`, `y_λχ^λ(β_K)` and `|tr_M(β_K)|` are archimedean evaluations at the substrate anchor, and both the quotient form and the leading-order collapse turn on the ordering hypothesis `0 < |tr_M|`, which a generic commutative ring cannot state. It replaces `Float`, which carries no field structure in Lean — no algebra was possible on it, which is why the conditional theorem could only ever have been a self-assuming projection. Recorded per §4d; the migration is bean `qou-tmmt`.",
    },
  ],
  computation: {
    engine: "mpmath",
    script: "computations/rho_k_h3a_refinement.py",
    witness: "computations/rho-k-h3a-refinement.witness.json",
    status: "experimental",
  },
});

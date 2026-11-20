import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:qbeta-c-k-closed-forms",
  lean: {
    ref: "qou:QOU.BraidKnot.QBetaCKClosedForms",
    validation: "not_checked",
  },
  title:
    "Closed-form conjectures for $c_4, c_5, c_6, c_7$ in the $\\mathfrak{Q}_\\beta$ precision ladder (convention-C frame)",
  uses: ["rem:per-block-hopf-jones-absorption-pattern"],
  cites: [
    "khovanov2000",
    "khovanov-rozansky2008",
    "khovanovlauda2009",
    "wenzl1988",
    "hoefsmit1974",
    "jones1985",
  ],
  tags: [
    "lean-infrastructure",
    "open-rd",
    "precision-ladder",
    "empirical-conjecture",
    "khovanov-rozansky",
    "klr-canonical-basis",
  ],
  computation: {
    engine: "python",
    script: "computations/qbeta/qbeta_decay_sdp_full_ck.py",
    witness: [
      "computations/qbeta/qbeta-decay-sdp-full-ck-derivation.witness.json",
    ],
    status: "experimental",
  },
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): We formalize these coefficients as conjectures. This permits downstream claims to use the conditional-class exception, as implemented in [$\\mathfrak{Q}_\\beta$ categorical-derivation precision ladder](#prop:q-beta-categorical-precision-ladder) via the Lean class `QBetaPrecisionLadderCoefficients`." },
    {
      kind: "status",
      body: "Per AGENTS.md §3b-cond conditional-class exception, the existing\n[`prop:q-beta-categorical-precision-ladder`](#prop:q-beta-categorical-precision-ladder)\nLean class `QBetaPrecisionLadderCoefficients` (which axiomatises\nthe c_k values as class fields) is the correct integration point.\nDownstream provable claims taking\n`[QBetaPrecisionLadderCoefficients q]` as a hypothesis are\n**rigorous conditional results** modulo this conjecture.\n\nThe current canonical instance `qBetaPrecisionLadderCoeffsCanonical`\non main provides the empirical closed forms; this conjecture block\nstates the conditions under which those instance values are\n**proved** rather than **fit**.",
    },
    {
      kind: "caveat",
      date: "2026-09-14",
      body:
        "Provenance for the rewritten **Precision** and **Evidence** sections. " +
        "(1) Convention C was excised by the owner ruling of 2026-08-15; z = 1 was " +
        "ruled **inadmissible** on 2026-09-08. (2) The live dashboard figure for " +
        "𝔔_β — 1.668e+8 ppb against the 7.797 ppb target, miss 2.139e+7 — is the " +
        "`Q_beta` row of `per-observable-100x-status.witness.json`; it is the ruled " +
        "z_D base with ZERO c_k rungs, a different object from the +6.02 ppb " +
        "five-rung figure on the retired z = 1 cell. (3) The c₃ value −2.0098 " +
        "recorded in the Evidence table is the pre-PR-#1422 figure; the live " +
        "convention-C extractions are proton −2.06934257711516783787971951725, " +
        "muon CODATA-2022 −2.019860311874005, muon CODATA-2018 −2.020200233. " +
        "Proton is named in the block per the owner directive of 2026-08-07 " +
        "(production compute defaults to the proton pin). (4) The other five table " +
        "entries have no live producer: measured 2026-09-14, no file under " +
        "`computations/` carries −1.1435, −1.2229, +3.4976 or +57.149. Tracked as " +
        "bean `qou-00ot`; the convention re-derivation is `qou-cds1`.",
      see:
        "computations/per-observable-100x-status.witness.json",
    },
  ],
});

import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:mass-endomorphism",
  title: "Mass endomorphism conjecture",
  lean: {
    ref: "qou:QOU.MassEndomorphism.MassEndomorphism",
    validation: "not_checked",
  },
  // prop:hecke-mass-trace and conj:brane-tower-z-habiro removed from
  // uses[] (2026-06-01 detangler Bucket-A): the conjecture only
  // *mentions* them narratively ("its Markov trace gives the mass
  // (…)"; "the [brane-tower] conjecture has two independent claims") —
  // it does not build its claim ON them. Prose links retained in the
  // .md. Reclassifies two cross-chapter logical forward-refs to
  // storytelling. See docs/coordination/forward-ref-defect-triage-2026-06-01.md.
  uses: [
    "def:qz-bicompletion",
    "def:motivic-substrate",
    "def:archimedean-realization-functor",
  ],
  tags: [
    "tier:keystone",
    "mass",
    "endomorphism",
    "quantum-dilogarithm",
    "volume-conjecture",
    "higgs",
    "brane-tower",
    "habiro-ring",
    "open-problem",
  ],
  cites: [
    "kashaev1997",
    "murakami-murakami2001",
  ],
  computation: {
    engine: "mpmath",
    script: "computations/derive_m_baryon_volume_form.py",
    witness: "computations/m-baryon-volume-form.witness.json",
    status: "verified",
  },
});

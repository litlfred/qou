import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:sw-period-residue-sum",
  lean: {
    ref: "qou:QOU.Brings.sw_period_eq_residue_sum",
    validation: "validated",
  },
  title: "The Seiberg–Witten period is an algebraic residue sum",
  cites: ["donagi1997"],
  uses: [
    "prop:mi-sw-abelianisation",
    "rem:brings-smoothness",
  ],
  proofs: ["prf:sw-period-residue-sum"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): Vanishing at every jet level — see `QOU.Brings.period_eq_zero_of_total_residue_vanishes`. Keystone label: the keystone `conj:sw-prolongation-period-eq-mean-qdim` still needs. The $z$-derivative coefficient map is — the operator `ddz` that `QOU.Brings.RamificationParityMonodromy` already defines for this exact setting —" },
  ],
});

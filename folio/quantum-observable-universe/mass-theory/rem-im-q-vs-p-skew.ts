import { remark } from "../../schema/builders";

export default remark({
  label: "rem:im-q-vs-p-skew",
  title: "Im(q) is not the EM / P_skew channel — distinct mechanisms",
  interprets: "prop:lusztig-vs-hermitian-bar",
  uses: [
    "prop:lusztig-vs-hermitian-bar",
    "prop:categorical-mass-markov",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): - [`crossing-energy-interpretation.md`](../observations/crossing-energy-interpretation.md) — `sinh(log q)` = Coulomb channel identification" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): - [`bar-involution.md`](../braids-and-knots/bar-involution.md) — bar projection definition" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): Per\n[`crossing-energy-interpretation.md`](../observations/crossing-energy-interpretation.md)," },
    {
      kind: "refined-framing",
      date: "2026-05-25",
      body:
        "**Promoted from chat correction (PR #1127).** During the complex-q discussion " +
        "an initial framing claimed 'Im(q) is the framework's hidden EM / antimatter channel'. " +
        "This was incorrect and is corrected in this remark. The bar-projection mechanism " +
        "(P_avg keeps cosh, P_skew discards sinh) and the modulus-projection mechanism " +
        "(`m = |tr_M|`) are DIFFERENT — the former operates on real q, the latter on complex q. " +
        "P_skew has real content at real q; Im(q) is a separate complex-q degree of freedom. " +
        "Companion audit: " +
        "[`docs/audits/2026-05-24-m-mu-over-m-e-operator-rederivation.md`](../../../docs/audits/2026-05-24-m-mu-over-m-e-operator-rederivation.md) " +
        "(Phase 3 finding §Implications).",
    },
  ],
  tags: [
    "bar-involution",
    "modulus-projection",
    "complex-q",
    "em-channel",
    "im-q",
    "p-skew",
    "structural-clarification",
  ],
});

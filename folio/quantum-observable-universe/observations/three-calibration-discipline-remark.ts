import { remark } from "../../schema/builders";

export default remark({
  label: "rem:three-calibration-discipline",
  title: "Homogeneity of the derivation chain under the calibration discipline",
  interprets: "def:three-calibration-discipline",
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): Its content is the class field `mass_factorisation` of `qou:QOU.Observations.ThreeCalibrationDiscipline`." },
    {
      kind: "note",
      date: "2026-11-15",
      body: "**Excised (owner, 2026-11-15, D-W2).** The description of $\\mathfrak{Q}_\\beta$ as the bar-odd $\\sinh$ partner of the bar-even $\\cosh$ meson scale $m_\\pi$ was removed. No $\\mathfrak{Q}_\\beta$ functional on record has a definite bar parity under $q \\mapsto q^{-1}$: not Form A, not the $z = 1$ trace, and not the ruled $z_D$ trace. The two traces carry only an overall factor $h = q - q^{-1}$. No number, Lean declaration or producer depended on the label. Whether a bar-odd projection of the ruled trace carries such a role is bean `qou-hlx8`. Measurement: `docs/audits/2026-11-15-one-sided-weak-vertex.md` §4.",
      see: "https://github.com/litlfred/qou/blob/main/docs/audits/2026-11-15-one-sided-weak-vertex.md",
    },
  ],
});

import { definition } from "../../schema/builders";

export default definition({
  label: "def:down-quark",
  title: "Down quark",
  tags: ["quark", "down", "unknot", "borromean", "fermion", "color-tube"],
  lean: { ref: "qou:QOU.Archimedean.DownQuark",
    validation: "not_checked",
  },
  uses: ["def:up-quark", "def:coulomb-charge"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The reversal is an exact mirror, and `QOU.Archimedean.quark_crossing_asymmetry` formalizes it: the two orientations differ by a sign." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): See `QOU.Braiding.mirror_odd_neutral_neutron_forces_zero`." },
  ],
});

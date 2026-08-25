import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:strangelet-crossing-energy",
  lean: { ref: "qou:QOU.Observations.strangelet_crossing_energy", validation: "not_checked" },
  title:
    "Crossing energy of strange quark matter is purely strong",
  // Clause 1 asserts this charge vanishes per baryon-number unit.
  // def:crossing-energy, which clause 2 reduces at Q = 0, is NOT listed:
  // it is reached through def:coulomb-charge.
  uses: ["def:coulomb-charge"],
  tags: [
    "strangelet",
    "strange-quark-matter",
    "crossing-energy",
    "coulomb-charge",
    "electromagnetic-neutrality",
    "witten",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "**§7c base-ring note (archimedean specialisation).** " +
        "Two things pin this one. (1) Its scalars are **physical**: " +
        "`E_bind_uds` and `E_bind_udd` are binding energies per baryon and " +
        "`Q_uds` is the Coulomb charge of the `uds` Borromean triple. (2) Its " +
        "context `extends QOU.Shared.MarkovTraceContext`, so the base ring " +
        "cannot be moved here in isolation — that shared parent is extended " +
        "by 16 classes and is tracked as the separate cross-cutting item " +
        "(bean `qou-mtcx`), the same `extends`-edge blast radius that blocked " +
        "`qmn_recursive_memoized`. The block therefore sits on the " +
        "archimedean side of the §7c wall, and any change is a parent-class " +
        "refactor rather than a per-block one.",
    },
  ],
});

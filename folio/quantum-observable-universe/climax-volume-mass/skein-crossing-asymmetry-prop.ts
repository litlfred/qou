import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:skein-crossing-asymmetry",
  title: "Crossing asymmetry and per-crossing Coulomb correction",
  tags: ["skein", "crossing", "coulomb", "asymmetry", "r-matrix"],
  lean: { ref: "qou:QOU.Braiding.skein_crossing_asymmetry",
    validation: "not_checked",
  },
  uses: ["def:coulomb-charge"],
  authorNotes: [
    { kind: "note", body: "Archimedean specialisation over R (§7c)." },
    {
      kind: "status",
      body: "The companion Lean `skein_crossing_asymmetry` currently encodes a placeholder (`: True`); the intended statement ($q > 1 \\Rightarrow \\tfrac{1}{2}(q - q^{-1}) > 0$) is sketched in-file and deferred via `sorry` (`-- Ref: [leitner2026]`).",
    },
  ],
});

import { remark } from "../../schema/builders";

export default remark({
  label: "rem:regime-table",
  title: "Master regime table for the aether parameter $q$",
  tags: [
    "regime",
    "limits",
    "summary",
    "reference",
  ],
  interprets: "def:substrate-parameter",
  cites: ["abdo2009", "amelinocamelia2013"],
  uses: [
    "def:quantum-planck-constant",
    "def:information-speed-of-light",
    "def:operational-entropy",
    "rem:hausdorff-dimension-recurrence",
    "def:gravitational-constant",
    "rem:dsr-planck-scale-phenomenology",
    "conj:dispersion-suppression-scale",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-24",
      body: "Bean qou-d93c: resolved the `rem:`/`def:` link-text mismatches (`rem:operational-entropy` -> `#def:operational-entropy`, `rem:gravitational-constant` -> `#def:gravitational-constant`) and declared all referenced blocks and bibliography keys.",
    },
  ],
});

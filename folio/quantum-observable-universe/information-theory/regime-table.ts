import { remark } from "../../schema/builders";

export default remark({
  label: "rem:regime-table",
  title: "Master regime table for the aether parameter $q$",
  authorNotes: [
    {
      kind: "note",
      body: "Downstream citations of regime values should reference rem:regime-table rather than duplicating rows; per-section tables project relevant rows from this master table.",
    },
  ],
  tags: [
    "regime",
    "limits",
    "summary",
    "reference",
  ],
  interprets: "def:substrate-parameter",
  uses: ["def:information-speed-of-light"],
  computation: {
    engine: "python+mpmath",
    script: "computations/q_pinning_50_digit.py",
    witness: "computations/q-pinning-50-digit.witness.json",
    status: "verified",
  },
});

import { proof } from "../../schema/builders";

export default proof({
  label: "prf:depth-2-identification-bloch-suslin",
  title: "Proof of depth-2 identification (Bloch–Suslin)",
  uses: ["prop:depth-2-identification-bloch-suslin"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-24",
      body: "Bean qou-df74 verified on origin/main (d7e1269e1e0): the earlier duplicated inline Proposition heading on `prop:depth-2-identification-bloch-suslin` is already absent (`0` duplicated headings), while the `(forall draft nabla # +)` tokens seen in raw `pdftotext` dumps come from the intentional right-margin `\\blockannot` (`\\marginnote`) icon strip in `paper-preamble.tex` (already stripped in standalone block previews via `stripAnnotations()` in `generate-block-tex.ts`).",
    },
  ],
});

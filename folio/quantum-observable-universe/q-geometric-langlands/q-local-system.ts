import { definition } from "../../schema/builders";

export default definition({
  label: "def:q-local-system",
  lean: { ref: "qou:QOU.QLocalSystem", validation: "not_checked" },
  title: "$q$-Local system",
  uses: [
    // The q != 1 non-vanishing that keeps L_q from reducing to a classical
    // flat bundle. def:substrate-parameter, fixed in the same opening
    // sentence, is omitted: it is already reached through
    // rem:kummer-filtration-obstruction.
    "prop:categorical-dq-squared",
    "rem:kummer-filtration-obstruction",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ([q-flat connection](#def:q-flat-connection))" },
  ],
  tags: ["geometric-langlands", "local-system", "q-deformation"],
});

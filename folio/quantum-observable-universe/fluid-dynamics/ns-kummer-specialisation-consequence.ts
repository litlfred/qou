import { remark } from "../../schema/builders";

export default remark({
  label: "rem:ns-kummer-specialisation-consequence",
  title: "Consequence for NS regularity",
  interprets: "prop:ns-kummer-specialisation",
  uses: ["thm:qu-to-qou"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ; see the disclaimer in [the Descartes NS theorem](#thm:ns-singularity-descartes)" },
  ],
  tags: ["kummer", "obstruction", "navier-stokes", "blowup"],
});

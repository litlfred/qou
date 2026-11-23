import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:skein-coulomb-enhancement",
  label: "rem:skein-coulomb-enhancement-interpretation",
  title: "Magnitude, transition classes, and what the QOU predicts",
  uses: [
    "prop:skein-coulomb-enhancement",
    "prop:hadron-half-life",
    "def:electron-knot",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): The leading-order predictions ([verification](#ex:hadron-half-life-verification)) inherently include $F_q$ through the nucleus-specific matrix element. The $\\sim 10$--$17\\%$ residual in the verification table stems entirely from discrete nuclear structure effects." },
  ],
});

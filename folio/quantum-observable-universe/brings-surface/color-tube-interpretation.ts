import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:color-tube-coordinates",
  label: "rem:color-tube-interpretation",
  title: "Interpretation of the color tube",
  uses: [
    "def:color-tube-coordinates",
    "rem:brings-qou-4tuple",
    "rem:spectral-dynamics",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): It anchors the $U(1)$ longitudinal backbone ([spectral dynamics](#rem:spectral-dynamics)) in the shifted frame." },
  ],
});

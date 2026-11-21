import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:pawlowski-leitner-inner-product",
  title: "Inner product on intertwiner spaces",
  lean: { ref: "qou:QOU.PawLeiInnerProduct",
    validation: "not_checked",
  },
  uses: [
    "prop:pawlowski-leitner-basis",
    "rem:adjoint-trace",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): This realization specializes to the archimedean limit, evaluating physical observables numerically at the substrate parameter $q_0$." },
  ],
  tags: ["inner-product", "intertwiner", "orthogonality", "pawlowski-leitner"],
  cites: [
    "leitnerpawloski2004",
  ],
});

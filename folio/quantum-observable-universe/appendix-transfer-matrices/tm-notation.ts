import { prose } from "../../schema/builders";

export default prose({
  label: "tm-notation",
  title: "Notation and conventions",
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-08-09",
      body: "Canonical Convention D sets $z(q) = q^3/(q^2+1) = q^2/[2]_q$; legacy worked decimals downstream in this appendix were evaluated under Convention C ($1/(q^{1/2}+q^{-1/2})$).",
    },
  ],
  tags: [
    "transfer-matrix",
    "notation",
    "hecke-algebra",
    "appendix",
    "self-contained",
  ],
});

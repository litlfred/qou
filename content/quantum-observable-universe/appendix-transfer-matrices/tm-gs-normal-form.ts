import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:tm-gs-normal-form",
  title:
    "Hecke-only Gröbner--Shirshov reduction of the nucleus element",
  uses: [
    "def:hecke-normal-form",
  ],
  cites: ["jones1987", "bergman1978"],
  tags: [
    "transfer-matrix",
    "groebner",
    "normal-form",
    "hecke-algebra",
    "inductive",
    "appendix",
  ],
});

import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:coxeter-strong-exchange",
  lean: {
    ref: "qou:QOU.Machinery.CoxeterParabolic.strong_exchange",
    validation: "not_checked",
  },
  title:
    "Strong exchange for Coxeter systems, via the reflection cocycle",
  tags: [
    "coxeter",
    "hecke-algebra",
    "exchange-property",
    "reflection-cocycle",
  ],
  uses: [],
  cites: ["kassel1995", "jones1987"],
});

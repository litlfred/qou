import { remark } from "../../schema/builders";

export default remark({
  label: "rem:mass-ordering-corrected",
  title:
    "Mass ordering $\\mathfrak{m}_{\\mathfrak{n}} > \\mathfrak{m}_{\\mathfrak{p}}$ with corrected trace",
  interprets: "prop:corrected-markov-trace",
  tags: [
    "mass-ordering",
    "proton",
    "neutron",
    "fermionic",
  ],
  uses: [
    "prop:corrected-markov-trace",
  ],
});

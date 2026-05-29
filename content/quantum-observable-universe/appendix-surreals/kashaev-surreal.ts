import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:kashaev-surreal",
  title:
    "Kashaev volume conjecture as a surreal standard-part identity",
  lean: { ref: "qou:QOU.AppendixSurreals.KashaevSurreal", validation: "stub" },
  tags: [
    "surreal-numbers",
    "kashaev",
    "volume-conjecture",
    "hyperbolic-volume",
    "standard-part",
    "open-problem",
    "reformulation",
  ],
  uses: ["rem:kashaev-volume-density"],
  cites: [
    "kashaev1997",
    "murakami-murakami2001",
    "berarducci-mantova2018",
  ],
});

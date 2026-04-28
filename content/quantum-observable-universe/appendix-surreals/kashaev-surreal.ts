import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:kashaev-surreal",
  title:
    "Kashaev volume conjecture as a surreal standard-part identity",
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

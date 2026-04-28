import { remark } from "../../schema/builders";

export default remark({
  label: "rem:penrose-ccc",
  title: "Relation to Penrose's Conformal Cyclic Cosmology",
  tags: [
    "penrose", "ccc", "conformal-cyclic-cosmology",
    "aeon", "jet-horizon",
  ],
  interprets: "def:aeon",
  uses: ["conj:aeon-boundary-generates-chart"],
  cites: ["penrose2010"],
});

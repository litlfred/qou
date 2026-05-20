import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:double-slit-massive-pattern",
  lean: { ref: "qou:QOU.Experimental.double_slit_massive_pattern",
    validation: "not_checked",
  },
  title: "Massive-particle interference pattern",
  uses: [
    "def:double-slit-q-phase",
    "rem:q-laplacian-expansion",
    "def:q-hodge-star",
  ],
  tags: ["double-slit", "interference", "massive-particle", "q-laplacian"],
  cites: [
    "bach2013",
  ],
});

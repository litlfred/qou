import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:q-motivic-transfer",
  title: "$q$-Motivic transfer principle",
  uses: [
    "def:q-motivic-zeta",
    "def:qou-motivic-measure",
    "conj:q-geometric-langlands",
  ],
  cites: ["denef2001", "cluckers2008"],
  tags: ["motivic-integration", "transfer-principle", "classical-limit"],
});

import { remark } from "../../schema/builders";

export default remark({
  label: "rem:tqft-context",
  cites: ["atiyah1988", "baez1995", "freed2010", "kock2004", "lurie2009", "turaev2010", "witten1988"],
  title: "TQFT context",
  tags: ["tqft", "cobordism"],
  uses: [
    "def:quantum-universe",
    "def:quantum-observable-universe",
    "ex:c-quantum-observable-universe",
  ],
});

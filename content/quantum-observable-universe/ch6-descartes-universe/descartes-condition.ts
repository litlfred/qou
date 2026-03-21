import { definition } from "../../schema/builders";

export default definition({
  label: "def:descartes-condition",
  title: "Descartes condition",
  tags: ["descartes-universe", "euler-characteristic"],
  uses: [
    "def:quantum-observable-universe",
    "thm:qu-to-qou",
  ],
});

import { definition } from "../../schema/builders";

export default definition({
  label: "def:exceptional-divisor",
  title: "Exceptional divisor at $p$",
  tags: ["descartes-universe", "exceptional-divisor", "blow-up"],
  uses: [
    "def:descartes-condition",
  ],
});

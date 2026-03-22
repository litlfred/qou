import { definition } from "../../schema/builders";

export default definition({
  label: "def:exceptional-divisor",
  lean: { decl: "QOU.ExceptionalDivisor" },
  status: "not_started",
  title: "Exceptional divisor at $p$",
  tags: ["descartes-universe", "exceptional-divisor", "blow-up"],
  uses: [
    "def:descartes-condition",
  ],
});

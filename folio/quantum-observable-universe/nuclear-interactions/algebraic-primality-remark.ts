import { remark } from "../../schema/builders";

export default remark({
  label: "rem:algebraic-primality-remark",
  title: "Algebraic primality as a magic-number surrogate",
  interprets: "def:algebraic-primality",
  uses: [
    "def:algebraic-primality",
  ],
});

import { remark } from "../../schema/builders";

export default remark({
  label: "rem:ks-multiplicativity-via-markov",
  title:
    "Algebraic shortcut: Kontsevich--Soibelman's multiplicative invariant from the Markov property",
  interprets: "thm:markov-trace-factorization",
  uses: [
    "thm:markov-trace-factorization",
    "unital-groebner-bases:cor:pbw",
  ],
  cites: ["kontsevich-soibelman-2008", "bergman1978"],
});

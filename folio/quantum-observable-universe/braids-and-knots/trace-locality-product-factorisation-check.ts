import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:trace-locality-meets-gs-non-locality",
  label: "rem:trace-locality-product-factorisation-check",
  title: "Product factorisation over the normal form: what has been checked",
  cites: ["wenzl1988"],
  tags: ["markov-trace", "groebner-shirshov", "wedderburn", "locality"],
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-11-15",
      body:
        "Moved here from part (3) of `prop:trace-locality-meets-gs-non-locality` on owner ruling (2026-11-15). The former proof of part (3) left the vertex volumes undefined and used multiplicativity of the trace, which does not hold; it also wrote the Wedderburn decomposition over the convention-C field Q(q^{1/2}) and cited Wenzl 1988 together with a manuscript theorem number. What survives is a finite computation, recorded here as one.",
    },
  ],
});

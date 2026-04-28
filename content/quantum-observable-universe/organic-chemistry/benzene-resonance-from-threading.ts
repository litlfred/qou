import { corollary } from "../../schema/builders";

export default corollary({
  label: "cor:benzene-resonance-from-threading",
  title: "Benzene resonance energy from the threading link",
  tags: [
    "benzene",
    "resonance",
    "aromatic-stabilisation",
    "alexander-polynomial",
    "threading",
    "corollary",
  ],
  lean: { ref: "qou:QOU.Organic.benzeneResonanceFromThreading",
    validation: "not_checked",
  },
  uses: [
    "prop:ring-closure-barrier-quantitative",
    "prop:threading-half-weight",
    "lem:alexander-T2N-closed-form",
  ],
  cites: [],
});

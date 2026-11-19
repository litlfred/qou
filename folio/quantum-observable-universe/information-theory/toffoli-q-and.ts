import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:toffoli-transfer-matrix",
  label: "rem:toffoli-q-and",
  title: "The q-AND as a Toffoli gate at the Planck scale",
  tags: [
    "toffoli",
    "q-AND",
    "planck-time",
    "reversible-computation",
    "CCNOT",
    "braiding",
    "universality",
  ],
  uses: ["prop:toffoli-transfer-matrix"],
  cites: [
    "bennett1973",
    "fredkin1982",
    "toffoli1980",
  ],
  computation: {
    engine: "python+mpmath",
    script: "computations/q_pinning_50_digit.py",
    witness: "computations/toffoli-lp-stability.witness.json",
    status: "verified",
  },
});

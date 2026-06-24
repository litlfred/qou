import { proposition } from "../../schema/builders";

/**
 * Wedderburn trace identity: the sum of squared q-dimensions
 * equals the q-factorial.
 */
export default proposition({
  label: "prop:wedderburn-trace-identity",
  proofs: ["prf:wedderburn-trace-identity"],
  title: "Wedderburn trace identity for $H_n(q)$",
  tags: [
    "wedderburn",
    "q-factorial",
    "q-dimension",
    "hecke-algebra",
    "trace",
    "partition",
  ],
  lean: { ref: "qou:QOU.BraidKnot.wedderburn_trace_identity",
    validation: "not_checked",
  },
  uses: ["prop:three-parameters-wedderburn"],
});

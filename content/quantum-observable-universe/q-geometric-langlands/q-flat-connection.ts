import { definition } from "../../schema/builders";

export default definition({
  label: "def:q-flat-connection",
  lean: { ref: "qou:QOU.QFlatConnection", validation: "not_checked" },
  title: "$q$-Flat connection",
  uses: [
    // The connection this definition constrains: a q-connection
    // nabla_q : V -> Omega^1_q (x) V, whose total curvature it splits.
    "def:categorical-q-connection",
    // prop:categorical-dq-squared is NOT listed although the prose cites it
    // (the d_q^2 != 0 obstruction q-flatness is defined against): it is
    // reached through def:q-local-system, which declares it directly.
    // Immediate neighbours only.
    "def:q-local-system",
  ],
  tags: ["geometric-langlands", "connection", "q-deformation"],
});

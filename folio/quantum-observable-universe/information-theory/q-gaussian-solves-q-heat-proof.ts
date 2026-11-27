import { proof } from "../../schema/builders";

export default proof({
  label: "prf:q-gaussian-solves-q-heat",
  title: "Proof of q gaussian solves q heat",
  uses: ["prop:q-gaussian-solves-q-heat"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): **Non-Reeb-invariant extensions.** For a general initial datum with non-trivial Reeb-fibre dependence, the fundamental solution includes additional modes from $\\Delta_\\xi$. These modes form the Peter--Weyl decomposition ([Peter--Weyl heat kernel](#prop:q-heat-kernel-peter-weyl)). The Reeb-invariant sector corresponds to the zeroth Peter--Weyl component $j = 0$, where $\\lambda_0(q) = 0$.\n" },
  ],
});

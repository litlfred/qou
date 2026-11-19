import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:explicit-central-idempotent",
  title:
    "Explicit central primitive idempotents $e_\\lambda$ via Murphy elements",
  lean: {
    ref: "qou:QOU.MassEndomorphism.MurphyLagrangeCentralIdempotents.murphyHeckeCentralIdem_idem",
    sorryFree: true,
    validation: "leanok",
  },
  uses: [
    "prop:jucys-murphy-central-elements-qou",
    "prop:hecke-baer-star-generic",
    "lem:explicit-central-idempotent-lagrange",
  ],
  cites: ["murphy1981", "dipper-james1986", "ram1997"],
  tags: [
    "central-idempotent",
    "murphy-elements",
    "lagrange-interpolation",
    "hecke-algebra",
    "explicit-formula",
    "computability",
  ],
  computation: {
    engine: "mpmath",
    script: "computations/probes/explicit_central_idempotent_probe.py",
    witness: "computations/probes/explicit-central-idempotent-probe.witness.json",
    status: "verified",
  },
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-19",
      body: "Proved unconditionally for all `n` in `QOU.MassEndomorphism.MurphyLagrangeCentralIdempotents` (`murphyHeckeCentralIdem_sum_eq_one`, `murphyHeckeCentralIdem_mul`, `murphyHeckeCentralIdem_idem`, `murphyHeckeCentralIdem_comm`) by pulling back the seminormal diagonal evaluation of the multiplicative Murphy–Lagrange projectors across `heckeProduct_bijective`.",
    },
  ],
});

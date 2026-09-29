import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:pentagon-uv-commutation",
  title:
    "Pentagon identity at adjacent jet levels: $\\widehat U \\widehat V = q\\,\\widehat V \\widehat U$",
  tags: [
    "pentagon",
    "quantum-dilogarithm",
    "quantum-torus",
    "hecke-algebra",
    "jet-tower",
    "brane-tower",
  ],
  lean: {
    ref: "qou:QOU.QuantumBloch.pentagon_uv_commutation",
    validation: "not_checked",
  },
  uses: [
    "def:quantum-bloch-group",
    "lem:vhat-pair-commutation-trace",
    "prop:jet-tower-convergence",
    "prop:descended-level-zero",
  ],
  cites: ["kassel1995", "faddeev1994", "kashaev1997"],
  authorNotes: [
    {
      kind: "status",
      body: "**Provable.** The level-internal half (scalars commute) is\n[`lem:vhat-pair-commutation-trace`](#lem\\:vhat-pair-commutation-trace).\nThe inter-level half (operator lift, $\\widehat U \\widehat V =\nq\\,\\widehat V \\widehat U$) is the operator content of the\nbrane-tower :refterm[descent]{#descent} involution; explicit Lean formalization\ndeferred to the :refterm[descent]{#descent} involution's quantization, where\n$\\hat\\tau_n$ is realized as a level-shift operator on\n$A_{n+1} = A_n \\otimes \\Omega^1(A_n)$.",
    },
  ],
});

import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:deuteron-binding-dressing-proton-net",
  lean: {
    ref: "qou:QOU.Mass.binding_dressing_eq_qbeta_over_h",
    validation: "not_checked",
  },
  title:
    "The deuteron binding dressing $(1-\\tfrac{h}{2})$ is the proton NF net coefficient",
  uses: [
    "conj:borromean-quark",
    "prop:neutron-qvalue-symbolic",
  ],
  authorNotes: [
    {
      kind: "status",
      date: "2026-07-04",
      body:
        "**Algebra Lean-formalized (conditional on `conj:borromean-quark`); " +
        "magnitude observation-tier, NOT wired.** The identities " +
        "$\\Delta(\\mathrm{net}) = -h\\,\\mathrm{net}(p)$, " +
        "$\\mathfrak{Q}_\\beta = \\mathfrak{E}_0\\,h\\,\\mathrm{net}(p)$ and " +
        "$\\mathfrak{E}_0\\,\\mathrm{net}(p)\\,\\Delta\\mathrm{tr} = " +
        "\\mathfrak{Q}_\\beta\\,\\Delta\\mathrm{tr}/h$ are exact in the field " +
        "(`QOU.Mass.DeuteronBindingDressing`, three theorems, `ring`/" +
        "`field_simp`). The physical identification $B_D \\approx$ AME " +
        "($+0.12\\%$) is a near-match conditional on the same " +
        "`conj:borromean-quark` the $Q$-value already assumes — recorded " +
        "tiered, not a wired binding law (the $\\Delta_\\lambda$ gate " +
        "stands). Lean not machine-verified locally (Mathlib cache " +
        "unavailable in sandbox); CI confirms.",
    },
  ],
  tags: [
    "binding",
    "deuteron",
    "bar-parity",
    "q-value",
    "conditional",
    "observation-tier",
  ],
  computation: {
    engine: "python+mpmath",
    script: "computations/probes/probe_d_dressing_is_proton_net.py",
    witness: "computations/probes/probe-d-dressing-is-proton-net.witness.json",
    status: "verified",
  },
});

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
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The identities are exact and formalized in `QOU.Mass.DeuteronBindingDressing`." },
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
    {
      kind: "note",
      date: "2026-08-09",
      body:
        "Lean sibling: archimedean specialisation over $\\mathbb{R}$ " +
        "(AGENTS.md §7c). The $\\mathbb{R}$ is inherited from the " +
        "`BorromeanQuark` class (`QOU.ParticleInteractions." +
        "neutron_qvalue_symbolic`) and is load-bearing **here**, not just " +
        "upstream: the $Q$-value ansatz is stated with an absolute value, " +
        "$\\mathfrak{Q}_\\beta = |\\Delta(\\mathrm{net})| \\cdot " +
        "\\mathfrak{E}_0$, and `qbeta_eq_E0_h_net_p` discharges it via " +
        "`abs_of_nonpos` using the class's substrate-regime *order* " +
        "hypotheses $0 < h$ and $h < 2$ (which give " +
        "$\\mathrm{net}(p) = 1 - h/2 > 0$). Strip the order and the " +
        "$|\\cdot|$ cannot be resolved, so the theorem does not survive to " +
        "a generic `CommRing`. Two further constructs need at least a " +
        "field: `binding_dressing_eq_qbeta_over_h` divides by $h$ " +
        "(`field_simp`, $h \\neq 0$), and $\\mathfrak{E}_0 = m_e/(q(q-1))$ " +
        "divides by $q(q-1)$. What *is* pre-archimedean is the first " +
        "identity, $\\Delta(\\mathrm{net}) = -h\\,\\mathrm{net}(p)$ " +
        "(`delta_net_eq_neg_h_net_p`), proved by `ring` alone with no " +
        "order and no division — it would restate verbatim over any " +
        "commutative ring carrying $h$, and it is the structural content " +
        "the block actually claims (dressing $\\leftrightarrow$ " +
        "$Q$-value separated by the single Hecke factor $h$).",
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

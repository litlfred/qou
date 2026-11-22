import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:borromean-quark",
  title:
    "Quarks as Borromean-linked unknots in the exceptional divisor",
  lean: {
    ref: "qou:QOU.ParticleInteractions.BorromeanQuark",
    validation: "not_checked",
  },
  authorNotes: [
    {
      kind: "note",
      date: "2026-07-04",
      body:
        "**Lean carrier (re-pointed 2026-07-04).** `lean.ref` now targets " +
        "`QOU.ParticleInteractions.BorromeanQuark` — the **genuinely open** " +
        "carrier: a content-bearing class (single-wrap NF net coefficients " +
        "`net_p = 1 − h/2`, `net_n = 1 − 3h/2 + h²/2`, and the `Q_β` energy-" +
        "scale ansatz) with **no instance**, i.e. the honest un-discharged " +
        "state (AGENTS.md §3b-tax). **Scope of this carrier (partial).** It " +
        "formalizes ONLY the *per-nucleon net-coefficient / β-decay* " +
        "sub-aspect of the conjecture — NOT the Borromean-confinement claim " +
        "(Brunnian property ⇒ colour confinement) nor the mass-from-volume " +
        "claim; those remain un-formalized (the latter's degenerate carrier " +
        "is the Archimedean one). No single Lean carrier currently captures " +
        "the whole conjecture; the ref points at the one with genuine, " +
        "un-discharged mathematical content. It previously pointed at " +
        "`QOU.Archimedean.BorromeanQuark`, whose `instance canonical` is " +
        "**definitionally discharged** (`volume_calibrates_mass := rfl` on a " +
        "field that IS the conclusion; `is_baryon_realisation` = mere " +
        "existence of the partition structures) — a self-assuming projection " +
        "that does NOT prove the physical Borromean claim and would mislead " +
        "a reader into thinking the keystone is closed. The Archimedean " +
        "carrier survives for the mass-from-volume aspect " +
        "(`baryon_mass_from_volume`); a follow-up should de-degenerate it " +
        "(remove the hollow instance / restructure to carry inputs, not the " +
        "conclusion) in a Lean-enabled session. Closure distance: Tier A " +
        "(discrete identification) — the net coefficients are derived " +
        "(typed-crossing + Hecke NF + `nf-qvalues.witness.json`); the one " +
        "research-grade residual is `conj:qbeta-trace-counit-convergence` " +
        "(non-perturbative tower convergence).",
    },
  ],
  tags: [
    "tier:keystone",
    "borromean",
    "quark",
    "unknot",
    "neutrino",
    "color-confinement",
    "exceptional-divisor",
    "hyperbolic-volume",
  ],
  cites: ["dgkmsv2013"],
  uses: [
    "prop:skein-generation",
    "rem:skein-generation-hadron-reading",
    "def:neutrino-knot",
    "prop:bn-mtc-action",
  ],
});

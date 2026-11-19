import { algorithm } from "../../schema/builders";

export default algorithm({
  authorNotes: [
    {
      kind: "note",
      body: "An earlier version of the q₀ pin carried a fitted Habiro 4-loop dressing; it was dropped 2026-07-04.",
    },
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "Working-channel pointers pulled out of the published prose for the " +
        "owner-gated $c_4$ reconcile (46 vs 4143/90): PR #3280, finding 5 of " +
        "`docs/audits/2026-07-03-deuteron-from-scratch-error-ledger.md` (which " +
        "also carries the per-stage attribution of the 1.4 ppb muon-identity " +
        "reconcile), and bean `2i8g`.",
    },
    {
      kind: "note",
      date: "2026-11-19",
      body: "Formalization and helper identifiers moved out of published prose: the Borromean trace closed form is verified in `BorromeanMarkovTrace.lean`; the GPMT cumulant helpers feed `QOU.Nuclear.AlphaSimplexCoordinationDerivation`; deprecated absolute-mass helpers in `computations/canonical_mass.py` are `vol_density_per_block` and `linking_weight_family_a`.",
    },
  ],
  label: "alg:mass-identity",
  title: "Nucleon mass ratio $m_p = 2\\,(m_\\mu F_{\\mathrm{Bor}} - 6 m_e) \\cdot R_{\\mathrm{s5bb}}$ (muon-anchored Hecke energy)",
  uses: [
    "prop:mass-identity-exists",
    "prop:mass-identity-unique",
    "thm:knot-mass-formula-unified",
  ],
  cites: ["martelli2016"],
  computation: {
    engine: "python+mpmath",
    script: "computations/canonical_mass.py",
    witness: "computations/m-p-substrate-identity-50dps.witness.json",
    status: "verified",
  },
  tags: [
    "mba",
    "step-9a",
    "mass-identity",
    "muon-anchor",
    "canonical-chain",
  ],
});

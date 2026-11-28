import { table } from "../../schema/builders";

/**
 * Reader-facing introduction summary of the ruled gamma-gamma hadron and H_6(q)
 * nuclear junction invariants evaluated at proton-anchored q_0 = 1.109978582751380808
 * (bean qou-intr). Backed by QOU/PhotonU1NeutralCut.lean,
 * QOU/MassTheory/NucleusBondValence.lean,
 * computations/probes/gg_photon_cut/u1-neutral-cut-d2.witness.json,
 * computations/probes/gg_deuteron_bond/gg-deuteron-bond.witness.json,
 * computations/master-atlas-80dps.witness.json, and
 * docs/audits/2026-11-28-ka-b4-pauli-wigner-saturation-synthesis.md.
 */
export default table({
  label: "tbl:intro-gg-hadron-highlights",
  title: "Highlights of the two-photon hadron and nuclear junction datum",
  uses: [
    "prop:gamma-gamma-generates-particles",
    "def:borromean-baryon",
    "rem:meson-to-proton-via-borromean",
    "prose:master-atlas-calibration-jacobian",
    "tbl:master-atlas-hadrons",
    "app:knot-periodic-table",
  ],
  cites: ["codata2022", "pdg2024", "ame2020tables"],
  tags: ["introduction", "hadrons", "gamma-gamma", "summary-table"],
});

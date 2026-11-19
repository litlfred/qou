import { prose } from "../../schema/builders";

export default prose({
  label: "prose:notation-collisions",
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-19",
      body:
        "Lean and repository provenance preserved from the notation-collision register: " +
        "(1) `QOU.QBeta.normalisedQuadCoeff_eq` proves $\\tilde c_2 = c_2 - 1/8$ independently of phase $\\alpha$; " +
        "(2) `partitionEuler3_eq` records $\\sum_{\\lambda \\vdash 3} \\Delta_\\lambda = -2$; " +
        "(3) `tr(id_A)` vs $\\chi_{\\mathrm{eu}}$ disambiguation follows owner ruling 2026-09-15 (bean `qou-2uf0`, probe `computations/audits/trace_id_quantum_dimension_probe.py`, legacy `climax-volume-mass/vertex-algebra-relations.lean`); " +
        "(4) curvature-rank / GB-depth / triangulation-size scope notes correspond to beans `qou-wjbd` (`docs/audits/2026-08-26-no-shift-rescues-the-word-partition-bridge.md`), `computations/snappy_cusp_seeding.py`, and `computations/eigenvalue_reeb_extension_h4_h5.py`; " +
        "(5) $w_\\lambda(q)$ vs $w_\\lambda(1)$ census in `docs/audits/scripts/wlambda_normalisation_census.py`; " +
        "(6) $\\mathcal{A} \\in H_{A+Z}(q)$ vs $\\mathcal{B}_K \\in H_{3A}(q)$ scoping follows owner rulings 2026-09-12 and 2026-10-10 (bean `qou-jgg0`, `docs/audits/2026-09-12-phi3-column-discriminates-the-strand-count.md`); " +
        "(7) `QOU.QBeta.FaddeevModularDouble` ($\\Phi_b$, evaluator `computations/qbeta/phi_b_evaluator.py`) vs legacy `QOU.Machinery.FaddeevQuantumDilogContext` ($\\Phi_q$); " +
        "(8) bar-parity grading theorems in `QOU.BraidKnot.CrossingEnergyBarParity` (`eSym_coef`, `eSym_mirror`, `bar_neg_of_both`); " +
        "(9) nuclear saturation in `QOU.Mass.CoordinationSaturation`; " +
        "(10) one-dimensional sense census in `computations/audits/one_dimensional_sense_audit.py` (`AlphaShiftOneDimChannel`).",
    },
  ],
});

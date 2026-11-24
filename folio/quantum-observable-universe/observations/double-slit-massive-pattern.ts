import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
    {
      kind: "note",
      date: "2026-11-24",
      body: "Bean qou-4qxj: added 80-dps (50-dps serialized, proton anchor, zero float64, zero fitted parameters) cross-check against the 150-bin digitized Fig. 3e profile (N = 6,235 electrons) of Bach, Pope, Liou, and Batelaan (2013) in `computations/observations/bach2013_double_slit_profile_crosscheck.py` (`bach2013_double_slit_profile_crosscheck.witness.json`). Documents both the uncalibrated electrostatic quadrupole zoom + blob-localization trough pedestal in Fig. 3e and the 5x horizontal axis factor in `simulators/double_slit_simulator.html` (`+-2.5584` vs `+-0.51168 mrad`). Parameter-free local vacuum `q_local(y) -> 1` matches `q = 1` Fraunhofer to `8.06e-6` pointwise and matches the magnification-invariant `m = +-2` envelope `sinc^2(5*pi/14) = 0.644816...` against observed `0.6552` (`1.58%`), whereas naive uniform `q = q_0` lifts `m = +-2` to `0.702572...` and worsens 5-order peak-position RMS on the physical `theta_sim/5` scale from `0.00708 mrad` to `0.02987 mrad`.",
    },
  ],
  label: "prop:double-slit-massive-pattern",
  lean: { ref: "qou:QOU.Experimental.double_slit_massive_pattern",
    validation: "not_checked",
  },
  title: "Massive-particle interference pattern",
  uses: [
    "def:double-slit-q-phase",
    "rem:q-laplacian-expansion",
    "def:q-hodge-star",
  ],
  computation: {
    engine: "mpmath",
    script: "computations/observations/bach2013_double_slit_profile_crosscheck.py",
    witness: "computations/observations/bach2013_double_slit_profile_crosscheck.witness.json",
    status: "verified",
  },
  tags: ["double-slit", "interference", "massive-particle", "q-laplacian"],
  cites: [
    "bach2013",
  ],
});

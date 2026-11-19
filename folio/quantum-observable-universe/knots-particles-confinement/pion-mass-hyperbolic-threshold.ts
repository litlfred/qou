import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:meson-scale-independence",
  label: "rem:pion-mass-hyperbolic-threshold",
  title: "Why $m_\\pi$ is a calibration: the pion sits below the hyperbolic threshold",
  tags: ["pion", "meson", "hyperbolic-volume", "calibration", "mass"],
  uses: [
    "prop:meson-scale-independence",
    "prop:pion-half-figure-eight",
    "fundamental-knots-operator-basis",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-24",
      body:
        "Sharpens `prop:meson-scale-independence`'s proof rather than " +
        "disputing it. That proof derives Vol = 0 from the Hopf-link binding " +
        "topology, which is correct but reads as a fact about one link. The " +
        "structural fact is that the pion is the n = 1 rung of the " +
        "(σ₁σ₂⁻¹)^n ladder whose n = 2 and n = 3 rungs are the figure-eight " +
        "(Higgs, Vol 2.0299) and the Borromean rings (nucleon, 8G), and " +
        "hyperbolic volume switches on only at n = 2. Everything below the " +
        "threshold is a torus knot or the unknot.",
    },
    {
      kind: "note",
      date: "2026-08-24",
      body:
        "Also records a correction the operator-basis table invites. It " +
        "labels its Vol = 0 rows 'the massless, force-carrying sector', but " +
        "the electron is in that sector as the trefoil and is the mass unit " +
        "of the framework. Vol = 0 means mass not derivable *from volume*, " +
        "not mass zero. The two mass calibrations (CAL-1 m_e, CAL-3 m_π) are " +
        "exactly the two Vol = 0 particles, which is why there are two rather " +
        "than one or three.",
    },
  ],
  computation: {
    engine: "mpmath",
    script: "computations/derive_m_baryon_volume_form.py",
    witness: "computations/m-baryon-volume-form.witness.json",
    status: "verified",
  },
});

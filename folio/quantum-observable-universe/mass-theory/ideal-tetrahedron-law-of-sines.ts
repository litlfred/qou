import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:ideal-tetrahedron-law-of-sines",
  title:
    "The law of sines for an ideal tetrahedron: $\\lVert z \\rVert = " +
    "\\sin\\theta_2 / \\sin\\theta_3$",
  tags: [
    "hyperbolic-volume",
    "ideal-tetrahedron",
    "dilogarithm",
    "kummer",
    "law-of-sines",
  ],
  lean: {
    ref: "qou:QOU.Knot.IdealTet.norm_eq_sin_div_sin",
    validation: "leanok",
  },
  uses: ["thm:rivin-concavity-one-tetrahedron"],
  cites: ["thurston1978", "neumann-zagier1985", "milnor1982"],
  computation: {
    engine: "mpmath",
    script: "computations/all_nuclides_sdp_admissibility_mp.py",
    witness: [
      "computations/all-nuclides-sdp-admissibility-mp.witness.json",
      "computations/qbeta-5two-route73-law-of-sines-radial.witness.json",
    ],
    status: "verified",
  },
});

import { remark } from "../../schema/builders";

export default remark({
  label: "rem:breit-wheeler-vertex",
  title: "Breit--Wheeler vertex: photon polarisation states as Hecke generators on the exceptional divisor",
  interprets: "def:exceptional-divisor",
  uses: ["def:vertex-operator"],
  tags: [
    "breit-wheeler", "photon", "polarisation",
    "pair-creation", "exceptional-divisor", "reeb-bundle",
    "hecke-generator", "trefoil",
  ],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-11-15",
      body:
        "**Selection rule re-scoped as a model statement (owner F1(a), bean `qou-ccst`, PR #7825).** " +
        "Tree-level QED gives nonzero pair production for parallel linear polarisations: " +
        "`computations/probes/breit_wheeler_qed_linear_polarization_probe.py` (exact spin-summed |M|², " +
        "e = m_e = 1, E = 5/4, rational on-shell momenta) gives 9/2 parallel vs 25/2 perpendicular along the beam axis, " +
        "and nonzero parallel values at every point tested. The horizontal/vertical labels are qualified, not replaced " +
        "(F2 open): `QOU.StandardModel.PolarizationHecke.no_automorphism_to_orthogonal_pair` and " +
        "`computations/probes/polarization_axes_h3_probe.py` (Bloch cos θ = −(q⁴+1)/(q²+1)²).",
    },
  ],
});

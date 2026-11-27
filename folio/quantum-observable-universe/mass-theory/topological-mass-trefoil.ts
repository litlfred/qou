import { example } from "../../schema/builders";

export default example({
  label: "ex:topological-mass-trefoil",
  title: "Topological mass of the trefoil knot (electron)",
  interprets: "conj:topological-mass-formula",
  uses: [
    "conj:topological-mass-formula",
    "rem:torus-knot-zero-volume-via-reeb",
  ],
  cites: ["murakami2004a"],
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-08-29",
      body: "Reconciled to the 2026-06-30 owner ruling (muon = $T(2,5)$, $4_1$ = Higgs — NOT the muon): the sentence reading Vol$(4_1)/\\hbar_q^2 \\approx 207.1$ as 'the muon-to-electron mass ratio' now states the CAL-2 identity with $4_1$ as the Higgs knot supplying the coupling scale. The Li$_2(q^{-2})/\\hbar_q^2$ 'interpolation' claim is retracted: Murakami math/0405126 (murakami2004a) proves torus-knot colored-Jones asymptotics have no volume-type limit (inverse-Alexander vs Chern-Simons-phase branches, discontinuous at real $r$), so the dilogarithm is not an analytic continuation of the volume; the $\\approx 112$ value is kept only as the natural-units rendering of CAL-1 per calibration-inputs. Resolves the contradiction logged in topological-field-ansatz-table-data.qa.json.",
      see: "docs/audits/2026-06-30-muon-knot-id-phi-q-evidence.md",
    },
  ],
  computation: {
    engine: "mpmath",
    script: "computations/q_pinning_50_digit.py",
    witness: "computations/q-pinning-50-digit.witness.json",
    status: "verified",
  },
  tags: ["mass", "trefoil", "electron", "example"],
});

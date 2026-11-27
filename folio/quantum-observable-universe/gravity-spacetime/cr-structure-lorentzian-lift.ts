import { prose } from "../../schema/builders";

export default prose({
  label: "prose:cr-structure-lorentzian-lift",
  uses: [
    "rem:rieffel-metric-quotient-faithfulness",
    "ex:rieffel-quotient-temperley-lieb",
    "prop:gram-degeneracy-blocks-connes",
  ],
  cites: [
    "nurowski-trautman2002",
    "lewandowski-nurowski-tafel1990",
    "fefferman1976",
    "lee1986",
    "leibniz-clarke1717",
    "earman1989",
    "barbour-bertotti1982",
    "rieffel1999",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-23",
      body:
        "The horizontal invariance of the CR condition under $d_q$ is formalised in " +
        "`QOU.QuantumObservableUniverse.QExteriorCR.dq_cr_iff`.",
    },
    {
      kind: "note",
      date: "2026-11-24",
      body:
        "Stop 3 of the three-stop Leibniz relational spine (bean qou-wywz), cross-referencing " +
        "Gap 4A's canonical Fefferman–Lee circle-bundle SL_4 Sylvester inertia `(3, 1, 0)` and " +
        "Sparling–Graham null-fibre vacuum obstruction `Ric(K, K) = 1/2 ≠ 0` " +
        "(`QOU.GravitySpacetime.FeffermanLorentzianHorizonEntropy`, bean qou-3ucg), while " +
        "keeping dynamical Einstein perturbation equations explicitly conjectural.",
    },
  ],
});

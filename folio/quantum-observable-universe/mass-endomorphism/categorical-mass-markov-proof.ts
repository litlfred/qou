import { proof } from "../../schema/builders";

export default proof({
  label: "prf:categorical-mass-markov",
  title: "Proof of categorical mass markov",
  uses: ["prop:categorical-mass-markov", "def:mass-identity"],
  computation: {
    engine: "sympy",
    script: "computations/markov/markov_trace_canonical.py",
    // The body already told the reader to reproduce with this script. It just
    // could not be DECLARED, because the script emitted no witness -- so the
    // nine values in its convention C-vs-D table were traceable only by
    // coincidence, matching decimals in `alpha-k-jones-markov-h3` and
    // `gram-matrix-dual`, neither of which is what the block cites (qou-ft3p).
    witness: [
      "computations/markov/markov-trace-canonical.witness.json",
    ],
    status: "verified",
    requires: ["mpmath", "sympy"],
  },
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-08-09",
      body: "**Convention change, 2026-08-09 (owner ruling; bean `qou-wgta` item 19).**\nThis table published **convention C** ($z = 1/(q^{1/2}+q^{-1/2}) \\approx 0.499$),\nwhich has been excised. Measured at the proton pin $q_0 =\n1.1099785827513808\\ldots$, 12 significant figures:\n\n<!-- literal-source: C column is preserved history, no producer (qou-ft3p) -->\n| quantity | convention C (was) | convention D (now) |\n|:---|---:|---:|\n| $z$ | $0.499320334184$ | $0.612688037146$ |\n| $z^2$ | $0.249320796129$ | $0.375386630862$ |\n| $hz^2+z$ | $0.551443414318$ | $0.691166478358$ |\n| $4_1$ | $0.182304485938$ | $0.280195642273$ |\n\nThe **convention-C column has no producer by design**: C was excised by the\nowner ruling of 2026-08-09, so nothing in the repo computes it and no\nwitness can carry it. The **convention-D column is witnessed** by\n`computations/markov/markov-trace-canonical.witness.json` (6 assertions at\n$10^{-40}$) — the script this note already names below as the reproducer,\nwhich until now emitted no witness at all (bean `qou-ft3p`).\n\n$h$ is convention-independent. The $4_1$ closed form is new here: it was\n\"(see witness)\", and the witness held the C value. Reproduce with\n`python3 computations/markov/markov_trace_canonical.py`, whose prop-table\ncheck now gates at $10^{-40}$ rather than $10^{-9}$.",
    },
    {
      kind: "note",
      body: "Lean declarations: Step 1 in `QOU.Torsion.MassTraceIdentity` (`frobeniusForm_massIntegrand_of_frobeniusForm_eq_counit`), Step 2 in `QOU.Torsion.MassTraceMarkov` (`braidTrace_wordBraid`) over `QOU.IwahoriHecke.{QTraceCyclic, MarkovPeel, NegativePeel, MarkovNormalized}`, braid-class descent in `QOU.Torsion.MassTraceMarkovClass` (`jonesTot_isMarkovInvariant`, `exists_wordBraid`, `massClass_wordBraid`), convention-D three-row vanishing in `QOU.SchurWeyl.ocneanuWeight_conventionD_eq_zero_of_three_rows`, two-row positivity in `QOU.QBeta.TemperleyLiebTower`, unit-modulus prune in `QOU.Mass.KZUnitModulusPrune.exp_I_ne_real_gt_one`, two-point KZ exchange in `QOU.Mass.KohnoTwoPoint.trace_weight_exchange_pow`, and pullback question in `QOU.Mass.KZPullbackGenerators`.",
    },
  ],
});

import { proof } from "../../schema/builders";

export default proof({
  label: "prf:qbeta-canonical-markov-weights-explicit-instance",
  title: "Proof of qbeta canonical markov weights explicit instance",
  uses: ["prop:qbeta-canonical-markov-weights-explicit-instance"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-09-03",
      body: "The first bullet of \"It does not establish\" read *\"Identifying the canonical inhabitant remains open\"* until 2026-09-03, when `QOU.BraidKnot.CanonicalMarkovWeightsH3.canonicalInstance` and its derivation from `QOU.SchurWeyl.HeckeMarkov3` (`canonical_y3_eq_markovWeight0`, `canonical_y21_eq_markovWeight2`, `markovWeight1_at_markovZD`, `canonicalInstance_eq_ocneanuWeight` in `QOU.BraidKnot.QBetaCanonicalMarkovWeightsDerived`) landed, paired with demoting `explicitInstance` from `instance` to `def` and guarded by `delta_tau_M_canonical_resolves_to_canonical`. Measurement: `computations/probes/canonical_markov_weights_h3_are_sl2_dimensions.py` (11/11). The Ocneanu-family and hook-content Lean results it relies on (`WenzlWeightVanishing`, `SchurWeyl/OcneanuWeight*`, `WenzlWeightLevelR`) were prior art from PRs #5242 and #5575 and were credited late.",
    },
  ],
});

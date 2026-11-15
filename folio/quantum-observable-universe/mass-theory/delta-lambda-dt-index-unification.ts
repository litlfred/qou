import { proposition } from "../../schema/builders";

/**
 * The per-partition binding weight Δ_λ = (−1)^{n(λ)}·dim V_λ is not merely a
 * definition: both of its factors are IDENTIFIED with independently-defined
 * objects. The magnitude is a DT / 3d-index Euler characteristic, and the sign
 * is the geometric longest-element sign, via n(λ) = Σ_i C(λ'_i, 2).
 *
 * Lean: dtEuler_eq_deltaLambda_unconditional (sorry-free, all n, no n ≤ 5
 * restriction on either leg). This block surfaces a theorem that was proved in
 * the Lean layer but had no content-block statement — which is why
 * alg:delta-lambda-closure had no provable to cite.
 *
 * SCOPE: this is the per-partition VALUE only. The many-body binding MAGNITUDE
 * remains open (six ansätze failed on the deuteron; the missing term is a
 * separate additive extensive object). This proposition must not be read as
 * closing that gate.
 */
export default proposition({
  label: "prop:delta-lambda-dt-index-unification",
  title:
    "$\\Delta_\\lambda = (-1)^{n(\\lambda)}\\dim V_\\lambda$ is a DT/3d-index Euler characteristic with geometric chirality",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.dtEuler_eq_deltaLambda_unconditional",
    validation: "not_checked",
  },
  uses: [
    "conj:binding-manybody-eq-jet-filtration",
  ],
  tags: [
    "delta-lambda",
    "dt-index",
    "springer-dimension",
    "chirality",
    "value-proved",
    "magnitude-open",
  ],
});

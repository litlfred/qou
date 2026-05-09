import { remark } from "../../schema/builders";

/**
 * LP-dual binding-energy shadow price y_0* is exactly equal for
 * mirror nuclei (T ↔ ³He) at every tested q, in both 2-row and
 * height-6 Wedderburn strata.
 *
 * This is a STRUCTURAL CONSEQUENCE of Frobenius self-duality on
 * the categorical level: matter ↔ antimatter, equivalently
 * proton ↔ neutron (Z ↔ N), corresponds to a transposition of
 * partition labels under the Hopf antipode.  The LP-dual
 * y_0(Z, N) inherits the Z ↔ N symmetry: y_0(Z, N) = y_0(N, Z).
 *
 * Empirical (witness alpha-5-lp-dual-crystal):
 *
 *   2-row stratum at q_0:
 *     y_0*(T) = y_0*(³He) = 570.6762 (exact equality to 4 d.p.)
 *     y_0*(D)              =  10.3125
 *
 *   ht=6 stratum at q_0:
 *     y_0*(T) = y_0*(³He) =  26.8242 (exact equality)
 *     y_0*(D)              =   0.4704
 *
 *   q-sweep (2-row, T vs ³He):
 *     q = 1.110: 570.6762 = 570.6762
 *     q = 1.050: 247.9348 = 247.9348
 *     q = 1.001: 127.6918 = 127.6918
 *
 *   At every q tested, T and ³He are EXACTLY equal.
 *
 * Crucially, the LP-dual is NOT atom-independent in the trivial
 * "constant" sense — it depends on (A, |Z − N|).  This is
 * exactly the BW formula structure: total mass depends on
 * A and on the isospin third-component T_3 = (Z − N) / 2 as
 * |Z − N|.  The QOU LP-dual reproduces this empirically.
 *
 * The "atom-independence" claim of the simplest closed form was
 * therefore TOO STRONG.  The correct claim is: y_0*(A, T_3) is
 * a *derivable* function of (A, T_3), with the LP solving for
 * it per atom.
 */
export default remark({
  label: "rem:lp-dual-isospin-invariance",
  title:
    "LP-dual binding-energy shadow price is isospin-invariant: $y_0^*(Z,N) = y_0^*(N,Z)$",
  interprets: "prop:mass-formula-iterative-lp-dual",
  uses: [
    "prop:mass-formula-iterative-lp-dual",
    "prop:frobenius-self-duality-forces-lp-dual-extraction",
    "rem:alpha-5-jm-central-empirical-findings",
    "prop:antiparticle-crossing-reversal",
  ],
  tags: [
    "lp-duality",
    "isospin-invariance",
    "shadow-price",
    "mirror-nuclei",
    "tritium-helium-3",
    "frobenius-self-duality",
    "empirical-finding",
    "positive-result",
  ],
});

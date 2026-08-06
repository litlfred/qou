import { remark } from "../../schema/builders";

/**
 * Meson mass splitting via q-deformation.
 *
 * Explains how the crossing energy E_×(q) and quantum dimensions
 * split the mass degeneracy of the meson octet. The hexagonal
 * weight pattern is q-independent; the dynamics (mass, transitions)
 * are q-dependent.
 *
 * ANTI-FITTING: The Gell-Mann-Okubo relation is stated as an
 * open cross-check, not claimed as derived. Conditional on N=3 and Y.
 */
export default remark({
  label: "rem:meson-mass-splitting",
  title: "Meson mass splitting from q-deformed dynamics",
  md: "meson-mass-splitting.md",
  interprets: "prop:meson-octet-decomposition",
  uses: [
    "prop:a2-from-three-strands",
    "rem:q-deformation-weight-lattice",
    "prop:meson-octet-decomposition",
  ],
});

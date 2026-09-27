import { remark } from "../../schema/builders";

export default remark({
  label: "rem:glossary-weierstrass-projection",
  title: "Weierstrass projection $\\wp_q(z)$",
  tags: [
    "glossary",
    "weierstrass",
    "elliptic-function",
    "descartes",
    "projection",
    "lattice",
  ],
  // The ref carries the MODULE path `QOU/Archimedean/WeierstrassProjection.lean`
  // plus the declaration name. The previous `QOU.Archimedean.weierstrassProjection`
  // resolved to the *wrong* file: its module prefix is `QOU.Archimedean`, and
  // `QOU/Archimedean.lean` exists but contains no Weierstrass declaration —
  // a silent mis-resolution rather than a visible break.
  //
  // Target: `opaque weierstrassProjection : R_q → R_q → ℂ → ℂ`, the declaration
  // that names ℘_q — this block's headline is a Definition, so the def is the
  // right target. The block's differential equation is the separate
  // `weierstrass_diff_eq` in the same module.
  lean: { ref: "qou:QOU.Archimedean.WeierstrassProjection.weierstrassProjection",
    validation: "not_checked",
  },
  uses: [
    "prop:descartes-elliptic-curve",
  ],
  defines: ["weierstrass-projection"],
});

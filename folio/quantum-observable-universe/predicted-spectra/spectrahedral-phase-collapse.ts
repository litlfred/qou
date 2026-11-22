import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:spectrahedral-phase-collapse",
  title: "Spectrahedral collapse and conformal rigidity",
  lean: {
    ref: "qou:QOU.Archimedean.spectrahedral_phase_collapse",
    validation: "not_checked",
  },
  computation: {
    engine: "sympy",
    script: "computations/probes/spectrahedral_phase_collapse_frame_probe.py",
    witness:
      "computations/probes/spectrahedral-phase-collapse-frame-probe.witness.json",
    status: "verified",
  },
  tags: [
    "spectrahedron",
    "sdp",
    "aeon-initiation",
    "phase-collapse",
    "convention-c",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): — convention D is a root of the determinant as a polynomial in $z$, which is `QOU.Interactions.GramMatrixH3Symbolic.gramMatrixD_det_eq_zero` (with" },
    {
      kind: "caveat",
      date: "2026-08-24",
      body:
        "**Convention-C scope (bean `qou-zf9n`).** The Lean sibling proves this " +
        "over `QOU.Interactions.GramMatrixH3Symbolic.gramMatrix`, which is the " +
        "convention-C Gram (`z = u/(u^2+1)`, `u = sqrt q`). Convention D " +
        "(`z = q^3/(q^2+1)`) is canonical as of the owner ruling of 2026-08-15, " +
        "and in that frame the determinant vanishes identically for every `q` " +
        "(`gramMatrixD_det_eq_zero`, sorry-free). The theorem is true, " +
        "non-vacuous and permanent as a C-frame result; its phase-transition " +
        "*reading* is frame-dependent and must never be restated as a property " +
        "of the canonical Gram. Scope-limited negative in the (a)/(b) sense — " +
        "it rules out this determinant route to a canonical phase transition, " +
        "not a canonical phase transition by some other route.",
    },
    {
      kind: "note",
      date: "2026-08-24",
      body:
        "**The statement was understating itself.** Computed exactly over " +
        "`Q(u)`, `det G_C` has TWO positive real zeros, not one: `u = 1/psi` " +
        "with multiplicity 5, and `u = 1` (i.e. `q = 1`, the classical limit) " +
        "with multiplicity 1. The earlier text named only the supergolden " +
        "point. The remaining real root of the factorisation, `u = -psi` from " +
        "`(u^3 + u^2 + 1)^5`, is negative and so outside the regime. Also " +
        "checked for a collision: `gramMatrix_det_ne_zero` carries the " +
        "hypothesis `1 < u` and both zeros lie at or below 1, so the two Lean " +
        "results are consistent, and the substrate `u_0 = 1.0536` sits above " +
        "both.",
    },
    {
      kind: "note",
      date: "2026-08-24",
      body:
        "The probe parses the 36 Gram entries out of the committed `.lean` " +
        "rather than retyping them, so it tests the artefact under review and " +
        "cannot drift from it, and it recovers `det G_D = 0` independently of " +
        "the Lean proof. Arithmetic is exact over `Q(u)` and `Q(q)` — no float " +
        "anywhere. Determinants go through `DomainMatrix` over the fraction " +
        "field; sympy's `Matrix.det()` on rational-function entries exhausts " +
        "memory on this 6x6 (measured: OOM-killed).",
    },
  ],
});

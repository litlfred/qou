import { remark } from "../../schema/builders";

/**
 * What the Reeb triad does and does not supply.
 *
 * The bracket is a theorem; reading it as a physical gauge symmetry is an
 * interpretation, and this block keeps the two apart. It also records where
 * that SU(2) is already spent — the electroweak sector — so the triad is not
 * counted twice.
 */
export default remark({
  interprets: "lem:bring-cone-reeb-quaternionic-twist",
  label: "rem:tetraplectic-su2-gauge-reading",
  title: "The Reeb triad as an internal $\\mathrm{SU}(2)$, and what it is not",
  lean: {
    ref: "qou:QOU.Tetraplectic.su2L_su2R_commute",
    sorryFree: true,
    validation: "not_checked",
  },
  uses: [
    "lem:bring-cone-reeb-quaternionic-twist",
    "def:quaternionic-spectral-resolvents",
  ],
  cites: ["morita1982", "fothleitner2003"],
  tags: [
    "tetraplectic",
    "su2",
    "left-right-symmetric",
    "electroweak",
    "gauge-structure",
    "scope-limit",
    "reeb-triad",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-24",
      body:
        "**\u00a77c base-ring note (archimedean specialisation).** " +
        "`QuaternionicElectroweak.lean` is deliberately mixed. The group " +
        "content — `IsSU2`, the `su2L`/`su2R` actions, their norm " +
        "preservation and `su2L_su2R_commute` — is stated over a generic " +
        "`{R : Type*} [CommRing R]`, because unit-quaternion multiplication " +
        "needs no ordering. Only `u1Y \u03b8` specialises to \u211d, and it " +
        "must: it is built from `Real.cos` / `Real.sin`, so the circle it " +
        "traces inside $\\mathrm{SU}(2)$ is an archimedean object. The " +
        "\u211d there is forced by the statement rather than chosen, which " +
        "is the \u00a77c \"archimedean realisation consumes the generic " +
        "construction\" case rather than a file that wants splitting.",
    },
    {
      kind: "caveat",
      date: "2026-08-24",
      body:
        "**The \"3\" here is the wrong 3 for colour, and this must not be " +
        "elided** (bean `qou-8p1g`). Three Reeb fields is " +
        "$\\dim \\mathfrak{su}(2) = 3$, the *adjoint* of $\\mathrm{SU}(2)$; " +
        "colour needs a $3$-dimensional *fundamental* of $\\mathrm{SU}(3)$. " +
        "Separately, `QuaternionicElectroweak.lean` already allocates this " +
        "same structure to the electroweak sector, so it is not available to " +
        "be re-spent. What would change the verdict is going to $m \\geq 2$ " +
        "(real dimension $\\geq 8$), where the tetraplectic condition has " +
        "content — that is open, not assumed.",
    },
  ],
});

import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:ns-kummer-specialisation",
  lean: { ref: "qou:QOU.FluidDynamics.ns_kummer_specialisation", validation: "not_checked" },
  title:
    "Kummer specialisation: the NS obstruction survives $q = 1$ for $\\gcd(\\chi(A), n) \\neq n$",
  uses: [
    "thm:qu-to-qou",
    "rem:three-euler-characteristics",
    "lem:bring-cone-reeb-quaternionic-twist",
    "def:reeb-bundle",
    "rem:substrate-gm-torsion",
    "prop:ns-obstruction-computation",
    "conj:qou-p-neq-np",
    "thm:ns-singularity-descartes",
    "rem:skein-filtration-trichotomy",
  ],
  cites: ["aaronsonwigderson2009", "grochow2017"],
  tags: [
    "kummer",
    "specialisation",
    "etale",
    "obstruction",
    "divisibility",
    "euler-characteristic",
  ],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-17",
      body:
        "**RESOLVED 2026-11-17 — the integer is chi_eu, under a stated hypothesis.** The block read `tr(kappa_0) = chi(A)`. The integer that controls the Kummer tower is the evaluation `e(xi)[S]`, which equals `chi_eu(S)` by Poincare-Hopf exactly when `xi` is the unit tangent bundle of `S` (`thm:qu-to-qou` item 2). That hypothesis is now stated. It is NOT supplied by `def:reeb-bundle` (the Hopf fibration over the fibre `S_p = S^2`, Euler number -1); for Bring it holds for the canonical-cone link `UT(Sigma_4)`, Euler number -6 (`lem:bring-cone-reeb-quaternionic-twist`). No trace of `A` enters. Whether every QOU's base circle bundle is `UT(M_0)` is open (bean `qou-qhcr`). PR #8365.",
    },
  ],
});

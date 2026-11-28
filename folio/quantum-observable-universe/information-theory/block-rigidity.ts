import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:block-rigidity",
  title: "Derivations and automorphisms respect the blocks",
  lean: { ref: "qou:QOU.Information.derivation_centralIdempotent_eq_zero" },
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-28",
      body:
        "Lean: `QOU/InformationTheory/BlockRigidity.lean` — `derivation_centralIdempotent_eq_zero`, `derivation_mul_centralIdempotent`, `algEquiv_centralIdempotent`, `conj_central`, `not_inner_of_moves_central`. Generic `CommRing R`, any `Ring A` with `Algebra R A`; no field or characteristic hypothesis. The Goldman–Iwahori facts in the last paragraph are `QOU.GoldmanIwahori.theta`, `theta_not_inner`, `trivialChar_theta_gen` (`QOU/Core/HeckeGoldmanIwahori.lean`).",
    },
  ],
  tags: ["inner-automorphism", "outer-automorphism", "derivation", "Wedderburn"],
  uses: ["sec:skein-trace-bandwidth-intro"],
});

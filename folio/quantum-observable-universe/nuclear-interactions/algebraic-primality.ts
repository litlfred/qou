import { definition } from "../../schema/builders";

export default definition({
  label: "def:algebraic-primality",
  title: "Algebraic primality of a strand count",
  lean: {
    ref: "qou:QOU.Interactions.AlgebraicPrimality.IsAlgebraicallyPrime",
    validation: "not_checked",
  },
  uses: [],
  tags: [
    "magic-numbers",
    "primality",
    "tensor-irreducibility",
    "confinement-sdp",
    "naming",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-24",
      body: "Formalisation twin-audit (`qou-x60n`): `2026-09-05-archimedean-twins-are-instantiations-probe.lean` (`algPrime_arch_iff_generic`) proves equivalence of the `n ≥ 1` and `n ≠ 0` formulations of `IsAlgebraicallyPrime`.",
      see: "docs/audits/2026-09-05-archimedean-twins-are-instantiations-probe.lean",
    },
  ],
});

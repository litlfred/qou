import { definition } from "../../schema/builders";

export default definition({
  label: "def:information-speed-of-light",
  title: "Speed of light as Lieb--Robinson velocity",
  tags: [
    "speed-of-light",
    "information-theory",
    "lieb-robinson",
    "causal-structure",
    "q-connection",
  ],
  lean: { ref: "qou:QOU.Information.speedOfLight",
    validation: "not_checked",
  },
  uses: [
    "ex:q-connection",
    "def:operational-entropy",
    "rem:light-cone-affine",
  ],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-11-24",
      body: "Formalisation twin-audit (`qou-x60n`): `2026-09-05-archimedean-twin-is-the-generic-at-R-probe.lean` proves the `ℝ`-valued library twin `1 / (q - 1)` agrees with the generic unit-typed sibling for `q ≠ 1` but silently evaluates to `0` at classicality `q = 1`.",
      see: "docs/audits/2026-09-05-archimedean-twin-is-the-generic-at-R-probe.lean",
    },
    {
      kind: "caveat",
      date: "2026-11-24",
      body: "Formalisation reachability audit (`qou-x60n`): `2026-09-05-two-of-the-four-junk-points-are-unreachable-probe.lean` (`speedOfLight_zero_at_classicality`) proves `q = 1` satisfies `ArchimedeanAetherField.field_ge_one`, confirming `1 / (q - 1) = 0` at `q = 1` is reachable.",
      see: "docs/audits/2026-09-05-two-of-the-four-junk-points-are-unreachable-probe.lean",
    },
  ],
});

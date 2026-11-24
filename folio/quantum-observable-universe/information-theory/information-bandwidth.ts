import { definition } from "../../schema/builders";

export default definition({
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-11-24",
      body: "Formalisation twin-audit (`qou-x60n`): `2026-09-05-archimedean-twins-are-instantiations-probe.lean` proves `informationBandwidth` in `MathConstants.lean` instantiates the generic sibling for `q ≠ 1` but evaluates to `0` at reachable classicality `q = 1`.",
      see: "docs/audits/2026-09-05-archimedean-twins-are-instantiations-probe.lean",
    },
    {
      kind: "caveat",
      date: "2026-11-24",
      body: "Formalisation reachability audit (`qou-x60n`): `2026-09-05-two-of-the-four-junk-points-are-unreachable-probe.lean` confirms the `q = 1` division-by-zero point in the `ℝ` bandwidth twin is reachable under `1 ≤ q`.",
      see: "docs/audits/2026-09-05-two-of-the-four-junk-points-are-unreachable-probe.lean",
    },
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "def:information-bandwidth",
  title: "Information bandwidth per Planck time",
  tags: [
    "information-bandwidth",
    "information-theory",
    "bremermann",
    "speed-of-light",
    "operational-entropy",
  ],
  lean: { ref: "qou:QOU.Information.informationBandwidth",
    validation: "not_checked",
  },
  uses: [
    "def:information-speed-of-light",
    "def:operational-entropy",
  ],
});

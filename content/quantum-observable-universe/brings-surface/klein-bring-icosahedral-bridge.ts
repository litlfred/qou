import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:klein-bring-icosahedral-bridge",
  lean: {
    ref: "qou:QOU.KleinBringBridge.KleinBringIcosahedralBridge",
    validation: "not_checked",
  },
  title:
    "Klein icosahedral–quintic bridge: the $(2,3,5)$ force symmetries assemble the Bring ED into the icosahedral $\\mathbb{P}^1$ with quotient $S^2(2,3,5)$",
  uses: [
    "def:brings-surface",
    "rem:brings-curve",
    "rem:braid-group-action",
    "rem:fivefold-symmetry",
    "def:hyperelliptic-quintic",
    "prop:bring-trefoil-cinquefoil-channel",
  ],
  cites: ["bring1786", "klein1888", "bolza1887"],
  tags: [
    "bring-curve",
    "icosahedral",
    "klein-quintic",
    "bring-radical",
    "triangle-2-3-5",
    "s5-so3-keystone",
    "poincare-sphere",
  ],
  authorNotes: [
    {
      kind: "status",
      date: "2026-06-28",
      body: "**primary conjecture (open QOU wiring).** Classical skeleton (Bring–Jerrard root variety, $(2,3,5)\\cong A_5$, Klein's icosahedral solution) is established; the open content is the single-sphere $A_5$ assembly of the three force operations + the identification $\\mathrm{ED}/A_5 \\cong S^2(2,3,5)$ = keystone Seifert base. Lean sibling `KleinBringIcosahedralBridge` is a §3b-tax primary-conjecture class (content-bearing, no instance) over a proved arithmetic skeleton; authored in a sandbox without a Lean toolchain — **not yet `lean`-direct verified**.",
    },
  ],
});

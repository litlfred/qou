import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:collatz-contact-boundary",
  lean: { ref: "qou:QOU.BringsSurface.collatz_contact_boundary", validation: "not_checked" },
  title:
    "The $[2]_q$-contact boundary on the Reeb bundle",
  uses: [
    "def:two-q-adic-valuation",
    "def:collatz-contact-boundary",
    "conj:q-collatz",
    "prop:root-of-unity-truncation",
  ],
  tags: [
    "collatz",
    "contact-order",
    "adic-valuation",
    "reeb-bundle",
    "kummer",
    "boundary",
    "divisor",
    "hopf-fibration",
  ],
  authorNotes: [
    { kind: "status", date: "2026-11-28", body: "False as stated (2026-11-28): the fundamental cycle converges with <v>=1<2; the threshold 2 double-counts the halving built into the odd step, and a degree count gives lim <v> <= 1 on every domain-stable orbit with infinitely many odd steps. Kept as a record; see sec:collatz-intro item 7." },
    { kind: "status", date: "2026-11-21", body: "Demoted from `conj:collatz-contact-boundary` (owner, #8526, 2026-11-21; bean qou-tm3c). The block states the $q$-Collatz conjecture as the contact condition ('equivalently'). Only the sufficiency direction is argued, and the Lean proves facts about $\\chi_A$ that do not bear on convergence." },
  ],
});

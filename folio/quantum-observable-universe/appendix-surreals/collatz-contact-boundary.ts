import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:collatz-contact-boundary",
  lean: { ref: "qou:QOU.AlgebraicSubstrate.collatz_contact_boundary", validation: "not_checked" },
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
    { kind: "status", date: "2026-11-21", body: "Demoted from `conj:collatz-contact-boundary` (owner, #8526, 2026-11-21; bean qou-tm3c). The block states the $q$-Collatz conjecture as the contact condition ('equivalently'). Only the sufficiency direction is argued, and the Lean proves facts about $\\chi_A$ that do not bear on convergence." },
  ],
});

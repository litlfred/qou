import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:dim-master-pentagon",
  title:
    "Ding–Iohara–Miki master Pentagon as unified ancestor of Macdonald + $q$-dilog Pentagons",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.DimMasterPentagon",
    validation: "not_checked",
  },
  uses: [
    "prop:macdonald-hook-telescope",
    "conj:pachner-pentagon-borromean",
    "conj:borromean-bloch-group-element",
  ],
  cites: [
    "ding-iohara1997",
    "miki2007",
    "feigin-hashizume2009",
  ],
  tags: [
    "tier:S",
    "dim-algebra",
    "master-pentagon",
    "duality-d17",
    "macdonald",
    "q-dilogarithm",
    "research-grade",
    "axiom-class",
    "open-problem",
  ],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-11-24",
      body: "Formalisation audit (`qou-x60n`): `2026-08-23-free-prop-field-triviality-probe.lean` records that bare `Prop`-valued fields on `DimMasterPentagon` were trivially inhabited by `⟨True⟩`.",
      see: "docs/audits/2026-08-23-free-prop-field-triviality-probe.lean",
    },
  ],
});

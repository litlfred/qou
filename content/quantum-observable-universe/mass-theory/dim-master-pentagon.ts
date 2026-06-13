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
    "non-scholarly-voice-exception",
  ],
});

import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:bar-involution-invariance",
  title:
    "Bar-involution invariance of Plancherel weights and Type-B-folded normal forms",
  lean: {
    ref: "qou:QOU.ParticleInteractions.bar_involution_invariance",
    validation: "not_checked",
  },
  uses: ["conj:cpt-orbit-closure-density"],
  cites: [
    "kashiwara1991",
    "khovanovlauda2009",
    "brundankleshchev2009",
  ],
  tags: [
    "bar-involution",
    "type-b-fold",
    "plancherel-weight",
    "invariance",
    "cpt",
    "witness-test",
    "crystal-basis-shortcut",
  ],
  computation: {
    engine: "mpmath",
    script: "computations/audits/brundan_kleshchev_audit.py",
    witness: "computations/audits/brundan-kleshchev-audit.witness.json",
    status: "verified",
  },
  authorNotes: [
    {
      kind: "note",
      body: "Archimedean specialisation over R (§7c).",
    },
  ],
});

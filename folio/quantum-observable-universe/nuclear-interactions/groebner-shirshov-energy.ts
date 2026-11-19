import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:groebner-shirshov-energy",
  title:
    "Energy as a Gröbner--Shirshov invariant of the nuclear braid",
  tags: [
    "groebner-shirshov",
    "hecke-algebra",
    "energy",
    "braid-word",
    "normal-form",
    "division-algorithm",
    "topological-invariant",
  ],
  lean: { ref: "qou:QOU.Archimedean.groebner_shirshov_energy",
    validation: "not_checked",
  },
  uses: [
    "def:hecke-normal-form",
    "unital-groebner-bases:thm:main-theorem",
  ],
  computation: {
    engine: "python+mpmath",
    script: "computations/probes/groebner_shirshov_confluence_lyapunov_and_radical_probe.py",
    witness: ["computations/probes/groebner-shirshov-confluence-lyapunov-and-radical-probe.witness.json"],
    status: "verified",
  },
  authorNotes: [
    {
      kind: "note",
      body: "Archimedean specialisation over R (§7c).",
    },
  ],
});

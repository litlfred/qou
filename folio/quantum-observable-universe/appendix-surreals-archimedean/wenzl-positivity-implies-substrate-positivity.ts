import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:wenzl-positivity-implies-substrate-positivity",
  title:
    "Wenzl positivity at $q_0$ implies aether $C^*$-Frobenius positivity",
  lean: {
    ref: "qou:QOU.AppendixSurreals.WenzlPositivityImpliesSubstratePositivity",
    validation: "not_checked",
  },
  uses: [
    "conj:os-reflection-positivity-from-reeb",
    "def:frobenius-hopf-substrate",
    "def:archimedean-realization-functor",
    "def:adelic-substrate",
  ],
  cites: [
    "wenzl1988",
    "wenzl1990",
    "kazhdanwenzl1993",
  ],
  tags: [
    "tier:P",
    "wenzl-positivity",
    "c-star-frobenius",
    "muger-positivity",
    "yang-mills",
    "mass-gap",
    "millennium-problem",
    "derivation-of-axiom",
    "open-problem",
  ],
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-10-10",
      body: "This paragraph previously said unitarity \"explains why\" the substrate has $q = q_0$ and that $q_0$ is \"locked by the unitarity requirement\". Both claims contradicted this block's own statement of Wenzl's criterion, under which the admissible range is all of $\\mathbb{R}_{>0}$. The conjecture itself is unchanged.",
    },
    {
      kind: "status",
      body: "Three ingredients separate the conjecture from a theorem:\n\n1. **Müger–BKLR Frobenius framework, transcribed to the QOU\n   substrate.** Müger's theory of $C^*$-Frobenius algebras (2003)\n   and Bischoff–Kawahigashi–Longo–Rehren's framework for unitary\n   tensor categories (2015) establish the implication\n   \"unitary $C^*$-tensor category $\\Rightarrow$ every Frobenius\n   algebra has positive antipode-twisted pairing\" in full\n   generality. Transcribing this to the QOU\n   [Frobenius–Hopf substrate](#def:frobenius-hopf-substrate)\n   is largely a formal exercise — the substrate is a *standard*\n   Frobenius algebra in the categorical setting, not an exotic one.\n\n2. **Wenzl's positivity at the specific value $q = q_0 \\approx\n   1.10998$.** The criterion is stated for $q \\in \\mathbb{R}_{>0}$\n   uniformly; specialising at $q_0$ is immediate.\n\n3. **Mathlib infrastructure.** Neither Müger / BKLR nor Wenzl's\n   positivity is in Mathlib; a complete Lean proof requires\n   transcribing the relevant tensor-category positivity machinery.\n   The conjecture is packaged as the typeclass\n   `QOU.AppendixSurreals.WenzlPositivityImpliesSubstratePositivity`,\n   bridging the existing `OSReflectionPositivity` typeclass on the\n   downstream side and a future\n   `WenzlPositivityAt(q₀)` typeclass on the upstream side.",
    },
  ],
  computation: {
    engine: "mpmath",
    script: "computations/m_p_substrate_identity_50dps.py",
    witness: "computations/m-p-substrate-identity-50dps.witness.json",
    status: "verified",
  },
});

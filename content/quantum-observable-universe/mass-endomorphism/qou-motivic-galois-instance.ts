import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:qou-motivic-galois-instance",
  title:
    "QOU $\\mathrm{MotivicGaloisCharacter}$ instance via Habiro $\\to \\mathrm{Frob}_p$",
  tags: [
    "motivic-galois",
    "frobenius",
    "habiro",
    "qou-substrate",
    "instance",
  ],
  uses: [
    "def:motivic-galois-character",
  ],
  cites: ["habiro2002", "yekutieli2010", "tate1967"],
  computation: {
    engine: "python",
    script: "computations/probes/habiro_frobenius_probe.py",
    witness:
      "computations/probes/habiro-frobenius-probe.witness.json",
    status: "verified",
  },
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-08-22",
      body:
        "Demoted definition() to conjecture() (label def: to conj:). What this block " +
        "asserts is that the QOU brane-tower substrate carries a MotivicGaloisCharacter " +
        "whose local Frobenius is the Habiro evaluation Frob_p = f(u)|_{u = zeta_{2p}}. " +
        "The evaluation formula is explicit and total in p, but that it lands in " +
        "Z[zeta_{2p}] and assembles into an instance is supported by numerics alone, so " +
        "the claim is conjectural and the builder now says so. The `axiom` tag went with " +
        "the demotion: the axiom it named was the co-located .lean's bare `axiom`, deleted " +
        "2026-08-12, and nothing has carried one since.",
    },
    {
      kind: "status",
      date: "2026-08-22",
      body:
        "Lean: none, and the previous lean.ref " +
        "`qou:QOU.LiftingDescent.QOUInstance.qouMotivicGaloisChar` was dangling — no such " +
        "module and no such declaration exists anywhere in the tree, and no declaration " +
        "carries this block's \\label. Dropped rather than repointed. Writing the instance " +
        "is not currently worth doing: since 2026-08-12 MotivicGaloisCharacter has exactly " +
        "one field, `frobenius_at : Nat.Primes -> Mhat`, pure data with no propositional " +
        "obligation, so an instance supplying any total function would typecheck and would " +
        "assert nothing. The real formalisation target is the Habiro cyclotomic expansion " +
        "f(u) and its evaluation at roots of unity, which is substantial machinery this " +
        "tree does not have. Nothing downstream is blocked: MotivicPerpetualObstruction " +
        "takes [MotivicGaloisCharacter ...] as an explicit hypothesis, and " +
        "MotivicGaloisCharacterTrivial already witnesses the class satisfiable.",
    },
    {
      kind: "caveat",
      date: "2026-08-22",
      body:
        "What the witness does and does not show " +
        "(habiro-frobenius-probe.witness.json, computed 2026-05-03, commitSha 610a6aa2, " +
        "marked auditOnly against docs/audits/2026-05-02-m-iso-l-function-handoff.md): " +
        "9 primes (2..23) times 5 atoms (p, D, T, 3He, n). Every atom reports " +
        "all_truncated_primes_compatible: true with primes_failing_compatibility: [], so " +
        "nothing measured disagrees. But every atom also reports " +
        "step2_full_trace_compatible: false with n_primes_data_exhausted: 0 — the " +
        "Pochhammer truncation fires inside the available data at all 9 primes, so " +
        "full-trace compatibility was never reached rather than reached and failed. " +
        "Compatible where checked; unestablished beyond that. The top-level summary's " +
        "step2_all_atoms_compatible: true summarises the truncated check only.",
    },
  ],
});

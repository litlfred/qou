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
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): **Lean status.** There is no Lean formalization of this instance. The\nmodule `QOU.LiftingDescent.MotivicPerpetualObstructionFromTrace`\n(prime-ideal collapse, $C = a_0(-1) + 2 a_1(-1)$) proves statements\nabout the perpetual obstruction and constructs no\n`MotivicGaloisCharacter`; it is a different result." },
    {
      kind: "status",
      date: "2026-08-23",
      body: "There is no Lean formalization of this\ninstance. The co-located `.lean` file — which contained a bare `axiom`\nlaundering the perpetual obstruction into the `MotivicGaloisCharacter`\nclass — was deleted on 2026-08-12 and has no replacement. The\n`lean.ref` this block carried until today,\n`QOU.LiftingDescent.QOUInstance.qouMotivicGaloisChar`, named a module\nand a declaration that exist nowhere in the Lake tree.\n\nWhat does exist is\n`lean/QOU/LiftingDescent/MotivicPerpetualObstructionFromTrace.lean`\n(Route A: prime-ideal-collapse, $C = a_0(-1) + 2 a_1(-1)$),\nand it is a *different* result: it proves statements about the\nobstruction, and constructs no `MotivicGaloisCharacter`. The 2026-08-12\nnote here read as though it were the replacement. The block was a definition until 2026-08-23 and was restated as a conjecture because the per-prime coherence is neither proved nor formalised.",
    },
    {
      kind: "note",
      date: "2026-08-23",
      body:
        "Reclassified `definition()` → `conjecture()`, `def:` → `conj:` (bean " +
        "`qou-s0ip`, option 2). This block was the single `✗` error in " +
        "`run-validate` on `main` for at least a day: the `lean-file-exists` " +
        "constraint applies to `definition` and nothing else, and this block " +
        "had no co-located `.lean`, no module at its `lean.ref`, and no " +
        "declaration carrying its label. The other ~33 unformalised refs are " +
        "advisory only because their builders are not `definition`.",
    },
    {
      kind: "note",
      date: "2026-08-23",
      body:
        "Why `conjecture` and not a Lean stub. `MotivicGaloisCharacter` has " +
        "one field, `frobenius_at : Nat.Primes → Mhat` — pure data, no " +
        "propositional obligation — so an instance is writable with no proof " +
        "burden, and that is exactly why writing one would be wrong: " +
        "supplying `frobenius_at` means inventing the Habiro → Frob_p map in " +
        "Lean. The class's own docstring records that its propositional field " +
        "was removed on 2026-08-12 because encoding it as a class field " +
        "forced every instance to either prove it or launder an axiom; " +
        "fabricating the data field now is the same laundering (bean " +
        "`qou-ffwk`).",
    },
    {
      kind: "note",
      date: "2026-08-23",
      body:
        "Dropped `lean: { ref: \"qou:QOU.LiftingDescent.QOUInstance." +
        "qouMotivicGaloisChar\", validation: \"not_checked\" }`. Neither the " +
        "module `QOU.LiftingDescent.QOUInstance` nor the declaration " +
        "`qouMotivicGaloisChar` exists anywhere in the Lake tree, so the ref " +
        "resolved by none of the three resolver candidates. Recorded here " +
        "rather than carried as a pointer to nothing.",
    },
    {
      kind: "note",
      date: "2026-08-23",
      body:
        "Dropped the `axiom` tag. It described the co-located `.lean` that " +
        "carried a bare `axiom` laundering the perpetual obstruction into " +
        "`MotivicGaloisCharacter`; that file was deleted on 2026-08-12, so " +
        "the tag pointed at an artefact that no longer exists.",
    },
    {
      kind: "note",
      date: "2026-08-23",
      body:
        "What would promote this back to `definition()`: a Lean instance " +
        "whose `frobenius_at` is the Habiro evaluation `f(u)|_{u = ζ_{2p}}` " +
        "landing in `Mhat`, i.e. the cross-prime coherence the prose asserts " +
        "made formal. The numeric side already exists — " +
        "`habiro_frobenius_probe.py` is a verified computation with a " +
        "witness — so what is missing is the lift, not the data (bean " +
        "`qou-s0ip` option 1).",
    },
  ],
});

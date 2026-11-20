import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:mass-endomorphism-tower",
  title:
    "Proton--electron mass endomorphism tower (convention D, $\\mathrm{Li}_2^q$): the mass formula is positive under a genuine norm and bounded dilogarithm",
  lean: { ref: "qou:QOU.MassEndomorphism.mass_endomorphism_positive",
    validation: "validated",
  },
  // rem:kashaev-volume-density dropped from uses[] 2026-11-20 (owner choice, bean qou-tm3c):
  // not cited in the statement or proof. A remark carries no premise; the edge only put this block
  // downstream of a conjecture.
  uses: ["rem:photon-channel-wedderburn-chain"],
  computation: {
    engine: "mpmath",
    script: "computations/habiro/habiro_exact_mass_endomorphism.py",
    witness: "computations/habiro/habiro-exact-mass-endomorphism.witness.json",
    status: "experimental",
  },
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-20",
      body:
        "**Which trace and which weights (bean qou-j11h, from #2481).** " +
        "Read from the producer `computations/habiro/habiro_exact_mass_endomorphism.py`: " +
        "the descended term is the regular-representation reading (each V_i^full is a " +
        "Wedderburn-weighted sum over the three n=3 blocks), not the Jones-Markov trace. " +
        "The weights are q-deformed `dim_q(lambda)^2/[3]_q!` with the symmetric " +
        "q-dimension (`dim_q((2,1)) = [2]_q`), then divided by their sum so they add to 1. " +
        "They are not the classical `d_lambda^2/|S_3|` that item (1) of the 2026-06-22 note " +
        "names; item (3) of that note is the one that matches the code. This is a record of " +
        "what the producer does, not a ruling on which weights the proposition should use " +
        "(the Molien ruling covers Phi_k only). The Lean sibling is trace- and weight-agnostic: " +
        "V_i is data. On 2026-11-20 its pair sum was changed from adjacent pairs to all pairs " +
        "i<j, to match this block's boxed formula and the producer; the two agree for at most " +
        "two generators. lean-direct exit 0; both theorems use only propext, Classical.choice " +
        "and Quot.sound.",
    },
    {
      kind: "refined-framing",
      date: "2026-08-29",
      body:
        "**Re-formalized (convention D + Li_2^q; bean qou-p046).** The prior " +
        "`proton_electron_ratio` theorem carried a provably-FALSE `sorry`: " +
        "`frobeniusNorm : R -> R` was an arbitrary unconstrained function, so at " +
        "n=0 the mass reduced to `frobeniusNorm(1)` (empty product = 1, empty " +
        "sums = 0), and `frobeniusNorm := fun _ => -1` refutes the claimed " +
        "`q > 1 -> massPoly > 0`. That theorem is REMOVED and replaced by two " +
        "PROVED, sorry-free results — `mass_endomorphism_nonneg` and " +
        "`mass_endomorphism_positive`: the mass formula is >= 0 (and > 0 when its " +
        "descended trace term is > 0) under an explicit `MassPositivityHyp` — a " +
        "genuine (non-negative) Frobenius norm plus the bounded-Rogers dilog sign " +
        "`Li_2^q(-x) <= 0` for x >= 0. Two further legacy defects were fixed in " +
        "the same pass: (1) the Markov parameter `markovParamPoly v = " +
        "1/(v + v^-1) = sqrt(q)/(q+1)` was EXCISED convention C — replaced by " +
        "`markovZD q = q^3/(q^2+1)` (convention D, owner ruling 2026-08-15); " +
        "(2) the Faddeev `quantumDilogPoly q z = 1 - q^-1 z` (the `Phi_q` " +
        "truncation, refuted 2026-06-18 for isospin-symmetry incompatibility and " +
        "mirror-nucleus pathologies) was replaced by an ABSTRACT bounded " +
        "`Li_2^q : R -> R` passed in as data — matching the .md's abstract " +
        "`Li_2^q`, with no series formalised. The Lean now matches the .md boxed " +
        "formula (descended term minus the two `Li_2^q` sums, `z^2` pair weight, " +
        "convention D). Verified `lean`-direct exit 0, axiom-clean " +
        "(propext, Classical.choice, Quot.sound; no `sorryAx`). The numerical " +
        "proton-electron ratio is NOT a Lean claim — it stays the compute " +
        "witness (`habiro_exact_mass_endomorphism.py`).",
      see: "docs/audits/2026-08-15-owner-ruling-convention-d-proton-color.md",
    },
    {
      kind: "refined-framing",
      date: "2026-06-22",
      body:
        "**Trace-convention + dilog reconciliation (z-Habiro thread).** " +
        "Reconciled against the channel-level audit (PR #2481) and the " +
        "Phi_q-wire refutation verdict (2026-06-18). (1) The descended term " +
        "|prod V_i^full| is the REGULAR-REPRESENTATION (Wedderburn) trace " +
        "tr_reg = sum_lambda (d_lambda^2/|S_3|) chi_lambda — the trace of the " +
        "left-multiplication endomorphism (def:hecke-mass-element) — NOT the " +
        "Jones-Markov trace tr_M = prod V_i^std (they differ ~10% at q_0: " +
        "tr_reg ~ 0.960 vs tr_M ~ 1.065 for the proton); the term-1 label is " +
        "corrected in the body. (2) The boxed proposition and the production " +
        "pipeline (canonical_plus_multibrane, tower_mode=li2q) use the bounded " +
        "symmetric -Li_2^q(-|V_i|); the explanatory term-bullets, the Application " +
        "section, and the block title still display the SUPERSEDED Faddeev Phi_q " +
        "(the root-of-unity face — it blows up to 1e2-1e6 at the physical " +
        "|V_i^full| and is diagnostic-only). Updating those displays to li2q " +
        "awaits an mp recompute. (3) Weights are the q-deformed (dim_q)^2/[3]_q! " +
        "per the production code, not the classical d_lambda^2/|S_3|. See the " +
        "bounded-Rogers-continuation direction doc + the 2026-06-18 verdict.",
      see: "docs/audits/2026-06-22-zhabiro-bounded-rogers-continuation-direction.md",
    },
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "**§7c base-ring note (order-tier specialisation).** " +
        "This block's Lean file **already implements the §7c split " +
        "explicitly** and the order-sensitive half is the point of the block. " +
        "`QOU.MassEndomorphism.Pre` is pre-archimedean and generic (`{R : " +
        "Type u} [Field R]`, with the `q`-dilogarithm and Frobenius norm as " +
        "abstract `R -> R` data); the order-tier positivity theorems " +
        "(`mass_endomorphism_nonneg` / `mass_endomorphism_positive`) are " +
        "specialised to an ordered field (`[Field R] [LinearOrder R] " +
        "[IsStrictOrderedRing R]`) because the non-negativity `0 <= massPoly` " +
        "genuinely needs the ordering. That order typeclass is forced by the " +
        "statement rather than chosen. See the 2026-08-29 note for the removal " +
        "of the earlier `ℝ`-side `proton_electron_ratio` sorry (which this " +
        "note previously described).",
    },
  ],
});

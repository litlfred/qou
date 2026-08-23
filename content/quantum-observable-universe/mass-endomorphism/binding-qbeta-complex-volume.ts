import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:binding-qbeta-complex-volume",
  title:
    "Complex-volume unification: binding $\\mathfrak{E}_{\\mathrm{bind}}$ and $\\beta$-decay $\\mathfrak{Q}_\\beta$ are $\\operatorname{Re}$/$\\operatorname{Im}$ of one $\\mathfrak{V}=E_0\\,\\mathrm{tr}_M((\\Pi_{\\text{free}}-\\mathbf{1})\\circ\\mathcal{M})$",
  lean: {
    // Primary Lean ref (schema `LeanRefSchema.ref` is a single string).
    // The two secondary formalisation artifacts —
    // `QOU.Mass.ComplexVolumeZeta4Partner.SingleFrakVAssembly` and
    // `QOU.QBeta.StageC.StageCSigma3Lift` — are named in the authorNotes below.
    ref: "qou:QOU.MassEndomorphism.ComplexVolumeMatch",
    validation: "not_checked",
  },
  uses: [
    "prop:categorical-mass-markov",
    "conj:block-multiplicativity-v-free",
  ],
  cites: [
    "neumann-zagier1985",
    "kashaev1997",
  ],
  computation: {
    engine: "python",
    script:
      "computations/qbeta/qbeta_ck_sseries_operator_match_probe.py",
    witness:
      "computations/qbeta/qbeta-ck-sseries-operator-match.witness.json",
    status: "failed",
    // status was "verified" until 2026-08-23; the cited witness's own
    // `allPassed` is false (c2_gate). Per ComputationStatus,
    // "failed" = script ran, witness does NOT match expected values.
    // Nothing compared the two until scripts/check-computation-status.py.,
  },
  tags: [
    "tier:keystone",
    "complex-volume",
    "chern-simons",
    "binding-energy",
    "beta-decay",
    "mass-endomorphism",
    "bar-parity",
    "unification",
    "fibre-level",
  ],
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-07-06",
      body: "**Stage-C Casoratian kill-test.** The single-recurrence holomorphic tie hypothesis (that one Askey-Wilson recurrence carries both the even and odd ladders) forces a constant sign on the rung Casoratian. A categorical $\sigma_3$-lift must provide genuine level-4 rungs that respect this sign constraint, as codified by `QOU.QBeta.StageC.StageCSigma3Lift` (which refutes any lift yielding an incompatible Casoratian $W_3$).",
    },
    {
      kind: "refined-framing",
      date: "2026-07-06",
      body: "**Open single-$\mathfrak{V}$ assembly constraint.** The assembly of the observable binding/Q_β into a single complex fibre object `frakV` is constrained by the $\zeta_4$-partner relation. A candidate assembly must be $\zeta_4$-faithful (supported entirely on the $\pm i$ characters); a nonzero orbit sum or sign isotype falsifies it. This constraint is carried by `QOU.Mass.ComplexVolumeZeta4Partner.SingleFrakVAssembly`, advancing the formalization of the physical match gap.",
    },
    {
      kind: "refined-framing",
      date: "2026-06-16",
      body: "**The unification is definitional + proved; only the physical match is conjectural.** Define `$\mathfrak{V}$ = E₀·tr_M((Π_free−1)∘𝓜) ∈ ℂ` on any confined knot K — **categorically, no braid words**. `𝓜 ∈ End_𝐂(X_K)` is the mass endomorphism, `tr_M` the categorical Markov trace (per §7a, NOT the fibre functor τ), `Π_free` the idempotent projector onto the factorized sub-object (constituents un-linked; same R-matrix, inter-constituent confining crossings dropped). The 'free' value is `tr_M(Π_free∘𝓜)`, the 'confined' value `tr_M(𝓜)`; their difference = the projection defect (no overloaded Δ, no word notation, no new trace symbol). 'Knot' not 'atom' (nucleus is one instance). `$\\mathfrak{E}$_bind := Re $\mathfrak{V}$`, `$\\mathfrak{Q}$_β := Im $\mathfrak{V}$`; then `$\\mathfrak{E}$_bind + i·$\\mathfrak{Q}$_β = $\mathfrak{V}$` is a **theorem** (`QOU.MassEndomorphism.complex_volume_unification`, via `Complex.re_add_im`, sorry-free). The open content (the `ComplexVolumeMatch` class) is that the *measured* binding and $\\mathfrak{Q}$_β equal these definitional Re/Im at one normalisation. **Fibre-level caveat:** `Im(q₀)=0` at the archimedean level — the complex structure is fibre-level; `$\\mathfrak{E}$_bind, $\\mathfrak{Q}$_β` are real observable shadows (real-q Vol channel vs root-of-unity CS channel), exactly as `Vol` and `CS` are separately real. **Compute corroboration (this PR):** the bar-even net-route gives precision-ladder `c₂≈−8`, the bar-odd tr_M brane-tower gives `c₂=−1` — two real components of one complex c₂ ([Stage B verdict](../../../docs/audits/2026-06-16-hoefsmit-stage-b-attempt-verdict.md)).",
    },
    {
      kind: "note",
      date: "2026-06-16",
      body: "**Story/structure follow-up (owner-flagged).** This collapses the mass-binding and β-decay chapters into one derivation (compute `$\mathfrak{V}$(K)` once; Re = every binding, Im = every Q-value). A chapter/section reorg + one-voice pass is warranted so the paper tells the single complex-volume story rather than two disjoint ones — tracked as a follow-up, not done in this PR.",
    },
  ],
});

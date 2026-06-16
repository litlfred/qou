import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:binding-qbeta-complex-volume",
  title:
    "Complex-volume unification: binding $\\mathfrak{B}$ and $\\beta$-decay $\\mathfrak{Q}_\\beta$ are $\\operatorname{Re}$/$\\operatorname{Im}$ of one $\\mathfrak{W}=E_0\\,\\mathrm{tr}_M((\\Pi_{\\text{free}}-\\mathbf{1})\\circ\\mathcal{M})$",
  lean: {
    ref: "qou:QOU.MassEndomorphism.ComplexVolumeMatch",
    validation: "not_checked",
  },
  uses: [
    "prop:categorical-mass-markov",
    "rem:block-multiplicativity-v-free",
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
    status: "verified",
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
      date: "2026-06-16",
      body: "**The unification is definitional + proved; only the physical match is conjectural.** Define `𝔚 = E₀·tr_M((Π_free−1)∘𝓜) ∈ ℂ` on any confined knot K — **categorically, no braid words**. `𝓜 ∈ End_𝐂(X_K)` is the mass endomorphism, `tr_M` the categorical Markov trace (per §7a, NOT the fibre functor τ), `Π_free` the idempotent projector onto the factorized sub-object (constituents un-linked; same R-matrix, inter-constituent confining crossings dropped). The 'free' value is `tr_M(Π_free∘𝓜)`, the 'confined' value `tr_M(𝓜)`; their difference = the projection defect (no overloaded Δ, no word notation, no new trace symbol). 'Knot' not 'atom' (nucleus is one instance). `𝔅 := Re 𝔚`, `𝔔_β := Im 𝔚`; then `𝔅 + i·𝔔_β = 𝔚` is a **theorem** (`QOU.MassEndomorphism.complex_volume_unification`, via `Complex.re_add_im`, sorry-free). The open content (the `ComplexVolumeMatch` class) is that the *measured* binding and Q_β equal these definitional Re/Im at one normalisation. **Fibre-level caveat:** `Im(q₀)=0` at the archimedean level — the complex structure is fibre-level; `𝔅, 𝔔_β` are real observable shadows (real-q Vol channel vs root-of-unity CS channel), exactly as `Vol` and `CS` are separately real. **Compute corroboration (this PR):** the bar-even net-route gives precision-ladder `c₂≈−8`, the bar-odd tr_M brane-tower gives `c₂=−1` — two real components of one complex c₂ ([Stage B verdict](../../../docs/audits/2026-06-16-hoefsmit-stage-b-attempt-verdict.md)).",
    },
    {
      kind: "note",
      date: "2026-06-16",
      body: "**Story/structure follow-up (owner-flagged).** This collapses the mass-binding and β-decay chapters into one derivation (compute `𝔚(K)` once; Re = every binding, Im = every Q-value). A chapter/section reorg + one-voice pass is warranted so the paper tells the single complex-volume story rather than two disjoint ones — tracked as a follow-up, not done in this PR.",
    },
  ],
});

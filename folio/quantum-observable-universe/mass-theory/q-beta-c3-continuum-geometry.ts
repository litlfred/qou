import { remark } from "../../schema/builders";

// Manifest restored 2026-08-23 (bean `qou-cauj`). The .md, the .qa.json and the
// .lean all landed in the bulk import `52c68267f2`; the .ts did not, so the
// block has never been registered — and, because no manifest means no gate ever
// built it, its sibling .lean sat BROKEN (two errors) in the corpus unnoticed.
// Both are fixed and it is now sorry-free: `#print axioms` on all five
// declarations returns {propext, Classical.choice, Quot.sound}.
//
// `remark` interpreting `prop:q-beta-c3-hopf-three-fold-markov`: the .md's own
// framing is "the canonical q=1 shadow is J_Hopf(1) = -2 … the question is
// whether the residual gap admits a continuum-geometric description", which is
// that proposition's residual. It matches the sibling
// `rem:q-beta-c3-hopf-three-fold-markov-context`, the family's established
// interpretive shape. The .lean is a genuine sibling formalisation (the two
// geometry lemmas), not a shadowing stub, so §0a is satisfied.
//
// The dated CORRECTION banner moved out of the scholarly prose to authorNotes
// per §4d; the correction's substance was already restated inline in the body
// ("scope-limited, not exact"; "What stands is the hyperbolic geometry"), so
// nothing scholarly was lost.
export default remark({
  label: "rem:q-beta-c3-continuum-geometry",
  title:
    "The $c_3$ mass gap and continuum hyperbolic geometry: the $\\pi/3$ Lobachevsky saddle as geometric envelope",
  interprets: "prop:q-beta-c3-hopf-three-fold-markov",
  tags: [
    "mass-theory",
    "q-beta",
    "c3",
    "continuum-limit",
    "hyperbolic-volume",
    "faddeev",
  ],
  uses: ["prop:q-beta-c3-hopf-three-fold-markov"],
  lean: {
    ref: "qou:QOU.MassTheory.ContinuumGeometry.vol_4_1_is_twice_tetrahedron_at_saddle",
    validation: "leanok",
  },
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): [Borel–Padé extrapolation](#def:ecalle-borel-resummation)" },
    {
      kind: "note",
      date: "2026-08-15",
      body:
        "**Convention frame.** The convention-C scoping in the body is required by the owner ruling of 2026-08-15, which makes convention D (`z = q^3/(q^2+1)`) canonical and leaves every `c_k` conclusion C-conditional until the ladder is re-derived (bean `qou-cds1`). The scope statement is scholarly and stays in prose; the ruling's date and tracker live here.",
    },
    {
      kind: "note",
      date: "2026-08-23",
      body:
        "**§7c archimedean specialisation, acknowledged.** The sibling `.lean` is `\u211d`-valued throughout — `Real.log`, `Real.sin`, `deriv`, `MeasureTheory` interval integrals — and that is not gratuitous: the Lobachevsky potential `-\u222b log|2 sin(t/2)|`, its FTC derivative, and the `\u03c0/3` saddle are archimedean constructions with no generic-`R` form. This block sits on the archimedean side of the substrate wall by construction, which is what `wall-side-correct` asks be stated rather than left implicit.",
    },
    {
      kind: "refined-framing",
      date: "2026-07-11",
      body:
        "**the `c_3 → −Vol(4₁)` identification is over-scoped.** `−Vol(4₁) ≈ −2.02988` is **anchor-blind** and misses **both** substrate anchors (muon **+0.479%**, proton **−1.907%**) while the actual $c_3$ **swings 2.43%** (muon −2.0202, proton −2.0693); at the muon (CAL-2) pin it is **6.9× worse** than the precision ladder's own `−Vol(4₁)+u−(10/3)u²` near-match. So the \"continuum limit is exactly −Vol(4₁), rigorously banishing all algebraic truncations\" claim is **not** supported — it makes the muon fit worse and fails cross-anchor (§8 guard). Moreover, `c_3 → −2 = J_Hopf(q=1)` is the **canonical** q=1 shadow (registry **KC10 / KC20** `C_Hopf(2)=−2`), **not** a \"hallucination.\" The hyperbolic geometry below is real and kept (`Vol(4₁)=2·Cl₂(π/3)`, Lobachevsky saddle at `π/3`); only the $c_3$ **identification** and the \"exact/rigorous\" tier are corrected.",
    },
  ],
});

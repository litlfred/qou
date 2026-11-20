import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:wedderburn-weight-canonical",
  title:
    "Canonical q-deformed Wedderburn-block weight $\\tilde w_\\lambda$ and named scalings (BW, LP for all $\\lambda$)",
  tags: [
    "wedderburn",
    "weight",
    "canonical",
    "bw",
    "shadow-price",
    "wenzl-bridge",
    "self-conjugate",
    "consolidation",
  ],
  uses: [
    "prop:wedderburn-as-noncomm-fourier",
    "prop:plancherel-weight-boundedness",
  ],
  cites: ["jones1985", "wenzl1988", "kassel1995", "orellana1998"],
  lean: { ref: "qou:QOU.BraidKnot.wedderburnWeightCanonical" },
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): the manifest title and the Lean both say $\\tilde w_\\lambda$, and they are correct." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): > **Disposition: dropped from the class signature.** Of the three options — restrict the field to $\\lambda = (1)$, drop it, or demote the block to a conjecture — the author chose to drop. The field `y_eq_self_conjugate` and its projection theorem `y_self_conjugate` are removed from the Lean; `y` remains in the class as data only, and the class is inhabitable at the honest values. The two definitional scalings and `beta_mul_h_eq_neg_C` are unchanged. Weakening the field to make the class inhabitable would have been laundering, which is why the choice waited for the author. Measurement: [`wenzl_bridge_self_conjugate_premise_is_false.py`](https://github.com/litlfred/qou/blob/main/computations/probes/wenzl_bridge_self_conjugate_premise_is_false.py), whose first check now guards the drop." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): > **What this does *not* invalidate, which is most of the block.** `y_eq_self_conjugate` was previously a Lean **class field** — assumed, not proved — so nothing in the corpus was ever *proved* wrong by its falsity. What followed, while it stood, was that the class had no inhabitant carrying the intended $y$ and $\\tilde w$ together, so any `[WedderburnWeightCanonical R]`-conditional result was vacuous at the intended instance rather than false. **`WedderburnWeightCanonical.beta_mul_h_eq_neg_C`, the file's one real theorem, is untouched** — its proof uses `beta_eq` and `C_eq` only and never reads the `y` field, so the BW and LP scalings $\\beta_\\lambda = -\\tfrac12 \\tilde w_\\lambda$ and $C_\\lambda = \\tilde w_\\lambda \\cdot h/2$ stand as definitional. The block's own off-stratum statement, that $y_\\lambda$ and $\\tilde w_\\lambda$ are genuinely distinct families, is correct — and on this evidence correct on the stratum too." },
    {
      kind: "status",
      date: "2026-09-04",
      body:
        "**Wenzl-bridge field dropped (owner ruling, option A).** The class field `y_eq_self_conjugate` " +
        "($y_\\lambda = \\tilde w_\\lambda$ on $\\kappa_\\lambda = 0$) was measured false at every " +
        "self-conjugate partition with $n \\le 6$ except $(1)$, in both conventions (2026-09-02). It and its " +
        "projection theorem are removed; `y` stays as data only; the BW/LP scalings and " +
        "`beta_mul_h_eq_neg_C` are unchanged. The refutation record stays in the prose above.",
    },
    {
      kind: "status",
      date: "2026-10-10",
      body:
        "**`computation` field removed (owner, 2026-10-10).** It declared `status: \"verified\"` against " +
        "`bw_wenzl_shadow_equivalence.py`, a deprecated producer (now on the `cat/cat-harness/fsh-guts` branch) " +
        "whose check was the Wenzl-bridge field dropped above, so nothing remained for it to verify. The " +
        "witness `docs/audits/2026-05-01-p1-3a-bw-equivalence.witness.json` is kept as a historical record.",
    },
  ],
});

import { proposition } from "../../schema/builders";

/**
 * Color SU(3) from octonionic G₂ stabilization.
 *
 * Derives color SU(3) ⊂ G₂ = Aut(𝕆) via the Günaydin–Gürsey
 * decomposition 7 = 1 ⊕ 3 ⊕ 3̄. The 3/3̄ are complex conjugates
 * (non-self-dual), passing the Sym² gate that eliminates the
 * corpus's icosahedral T₁.
 *
 * ANTI-FITTING: The G₂ → SU(3) stabilizer is a theorem of
 * octonionic algebra (Günaydin–Gürsey 1973), not imported physics.
 * QOU's contribution is connecting this to the Bring surface / S₅
 * machinery via the McKay correspondence A₅ → E₈.
 */
export default proposition({
  label: "prop:color-su3-from-g2",
  title: "Color $\\mathrm{SU}(3)$ from octonionic stabilization",
  // def:octonion-algebra was authored 2026-08-29 (beans qou-7arp / qou-8fl1);
  // the NOTE that used to sit here, recording its absence, is discharged.
  // It sits immediately above this block in sec:color-algebra, so the edge
  // reads backward.
  uses: ["def:octonion-algebra"],
  // lean.ref repointed 2026-09-03 (bean qou-lvux / qou-8fl1 item 3).
  //
  // Previously `QOU.Eightfold.Sym2Gate.sym2_dim_3 : 3*(3+1)/2 = 6`, an
  // arithmetic tautology that derived nothing this block claims (AGENTS.md
  // "Strict Lean Discipline" item 5). The block's one load-bearing Lean-able
  // sentence is its last: "a self-dual 3 would carry a singlet in Sym² and
  // fail the gate" — i.e. passing the Sym² gate at dimension three forces
  // complex type. That is exactly
  //   QOU.Eightfold.Sym2GateFSTrichotomy.gate_forces_complex_of_dim_three
  // (sorry-free; hypotheses: the gate passes, quaternionic irreps have even
  // dimension, dim = 3; conclusion: a complex-type irrep is present), with
  // `real_triple_fails_gate` as the T₁ corollary.
  //
  // What is still NOT backed, and must not be read as machine-checked:
  //  - the headline (PSL(2,7) colour from the octonionic G₂ via the Fano
  //    plane) has no Lean formalisation anywhere in the corpus;
  //  - the scope-(b) marked-pair obstruction (S₄ has no orbit of size ≤ 2 on
  //    P²) is verified in exact arithmetic by `s4_marked_pair_obstruction.py`,
  //    not in Lean;
  //  - that the Günaydin–Gürsey triple IS complex type remains the cited
  //    literature input (gunaydin-gursey1973); the theorem says what complex
  //    type buys, not that this triple has it.
  cites: ["gunaydin-gursey1973"],
  lean: { ref: "qou:QOU.Eightfold.Sym2GateFSTrichotomy.gate_forces_complex_of_dim_three" },
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): and machine-verified in exact $\\mathbb{Z}[i]$ arithmetic\n(`s4_genus3_competitor_fermat.py`: element-order profile" },
  ],
});

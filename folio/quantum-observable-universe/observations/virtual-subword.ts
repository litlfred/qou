import { definition } from "../../schema/builders";

export default definition({
  label: "def:virtual-subword",
  title: "Virtual subword, entanglement across a cut, and connected parts",
  lean: { ref: "qou:QOU.VirtualSubword.IsVirtual", validation: "not_checked" },
  uses: [
    "rem:virtual-particles-exceptional-divisor",
    "thm:jones-markov-trace",
  ],
  cites: ["jones1985"],
  tags: [
    "virtual-particles", "entanglement", "observable", "class-function",
    "conjugation", "linking-number", "borromean", "braid-word",
    "cumulant", "mobius-inversion", "connected-part", "jones-polynomial",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-16",
      body: "Owner ruling 2026-11-16: virtual photons do not exist in QOU. This block replaces 'virtual exchange' by two word-level notions: a virtual subword (invisible to every observable) and a prior entangled pair (a pure subword with nonzero cross sum). Formalised sorry-free in the sibling `.lean` (lean-direct with `-DautoImplicit=false`, axioms propext / Classical.choice / Quot.sound). PR #8128, bean `qou-a1hh`.",
    },
    {
      kind: "note",
      date: "2026-11-16",
      body: "Connected part: `connected`, `connected_pair`, `connected_eq_zero_of_split` in the sibling `.lean`, sorry-free. The Borromean value is computed exactly by `computations/probes/gg_twist_reading3/borromean_jones_cumulant_probe.py` (Kauffman state sum in sympy, 4/4 checks). The t to q dictionary is left open: at the proton q0 the cumulant is -8.914e-5 for t = q0 and -1.439e-3 for t = q0^2. The trace-level statement behind `IsVirtual` (a and b agree under every trace iff a - b is in the commutator span; conjugates are unseen) is proved generally in PR #8134 as `QOU.BraidsAndKnots.ClosureUnseen.unseen_iff` / `unseen_conj` (block prop:closure-unseen-subword). Add it to `uses` once #8134 merges.",
    },
  ],
});

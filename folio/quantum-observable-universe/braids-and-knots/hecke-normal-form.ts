import { definition } from "../../schema/builders";

export default definition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
    {
      kind: "refined-framing",
      date: "2026-09-13",
      body: "**Confluence claim corrected (bean `qou-43co`).** This block previously read *\"This reduction is confluent, making the normal form independent of rule order\"* of the **three-rule** system. That is false, and the folio's own sorry-free Lean refutes it: `UGB.GrobnerShirshov.Hecke.NotAGSBasis.hecke_not_gs_basis_four` (machine-checked at $n = 4$) and `hecke_is_gs_basis_false`. The axiom `hecke_is_gs_basis` was deleted for being false, not merely unproved.\n\nTwo further defects in the same three lines, both fixed here. The Yang--Baxter arrow pointed the **wrong way** — it read $\\sigma_i\\sigma_{i+1}\\sigma_i \\to \\sigma_{i+1}\\sigma_i\\sigma_{i+1}$, whose left side is shortlex *smaller*, contradicting its own parenthetical *\"(in the shortlex-decreasing direction)\"* and the Lean, where `yb_lm` gives $\\mathrm{lm} = \\sigma_3\\sigma_2\\sigma_3$. As written the rule increased the word and could not terminate. Far commutativity carried **no orientation** at all, leaving it symmetric and likewise non-terminating; the Lean fixes $i > j + 1$.\n\n**Epistemic tiers of what now stands.** (i) The three-rule system is not a GS basis — *refuted*, sorry-free, machine-checked at $n = 4$. (ii) The completed system is a GS basis — *proved*, `heckeCompleted_isGrobnerShirshovBasis`, unconditional, every $n \\geq 1$ and every `HeckeParams` (bean `qou-auq3`, 2026-08-24). (iii) Uniqueness of normal forms — `heckeCompleted_normalForm_unique`, *proved* up to `CoeffEq` with no axiom beyond Lean's standard three. Both Diamond-Lemma inputs were library axioms until 2026-11-20: `reduction_well_founded` (`Basic.lean`) is now a theorem (bean `qou-2q7r`), and `local_confluence` (`CompositionLemma.lean`), which was false as stated and so inconsistent (`LocalConfluenceSupportRefutation.lean`), is now a theorem up to `CoeffEq` derived from the Diamond Lemma in `DiamondLemma.lean` (Bergman 1978 Thm 1.2; bean `qou-lc7q`). The GS-basis criterion in (ii) does *not* depend on them.\n\n**Attribution, deliberately split (bean `qou-qspu`).** `[bokut2001]` is cited here for the **completion family** only, which is what `HeckeCompletion.lean` attributes to Bokut & Shiao. It is a theorem about Coxeter *groups* at $q = 1$ and does **not** license the $H_n(q)$ GS-basis statement; that statement is carried here by the folio's own Lean, not by the citation. The primary for the deformed type-A case is Kang--Lee--Lee--Oh, *Hecke algebras, Specht modules and Gröbner--Shirshov bases*, J. Algebra **252** (2002) 258--292, which this folio does not hold — tracked as `qou-qspu`. `[kimlee2018]` is the held secondary exhibiting the same completion phenomenon on the Temperley--Lieb quotient (its Prop. 3.1 quotes Kang--Lee--Lee--Oh Prop. 6.2).\n\n**Stale header noted, not fixed here.** `HeckeCompletion.lean`'s own §\"What is **not** established here\" still lists the completed-system GS basis as unproved, 18,663 lines above the theorem that proves it.",
    },
  ],
  label: "def:hecke-normal-form",
  title: "Hecke normal form in $H_n(q)$",
  lean: { ref: "qou:QOU.Braiding.HeckeNormalForm",
    validation: "not_checked",
  },
  uses: ["rem:hecke-algebra-from-braiding"],
  cites: ["bokut2001", "kimlee2018"],
  tags: [
    "hecke-algebra",
    "normal-form",
    "groebner-shirshov",
    "canonical-basis",
  ],
});

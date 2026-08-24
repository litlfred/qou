import { definition } from "../../schema/builders";

/**
 * The tetraplectic structure on the affine cone over Bring's curve.
 *
 * Bring's curve B ⊂ P⁴ has an affine cone C(B) ⊂ ℂ⁵ — a complex surface,
 * so a real 4-manifold. Foth's tetraplectic condition on a 4m-manifold is a
 * closed 4-form Ω with Ω^m non-degenerate; here m = 1, so the condition is a
 * nowhere-vanishing volume form and nothing more. Averaging over the curve's
 * S₅ × ℤ₂ symmetry makes that volume form invariant, which is what lets
 * L²(M, Ω) decompose into S₅ irreducibles indexed by partitions of 5.
 *
 * That decomposition is the whole point: it is the bridge from a continuous
 * integral over the cone to the discrete Young-diagram data the rest of the
 * framework runs on.
 */
export default definition({
  label: "def:bring-cone-tetraplectic-structure",
  title:
    "Tetraplectic structure on the affine cone $C(\\mathcal{B})$ over Bring's curve",
  uses: ["def:brings-surface"],
  cites: ["foth2002"],
  tags: [
    "tetraplectic",
    "bring-cone",
    "s5-symmetry",
    "invariant-volume-form",
    "young-diagram",
    "archimedean-universe",
  ],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-08-24",
      body:
        "**At $m = 1$ the tetraplectic condition is vacuous, and the block " +
        "says so rather than trading on the name.** Foth's machinery — " +
        "tri-momentum maps, $\\Omega^m$ non-degeneracy — only bites at " +
        "$m \\geq 2$, i.e. real dimension $\\geq 8$. On the Bring cone every " +
        "4-form is closed automatically, so what is actually being fixed is " +
        "an $S_5$-invariant measure. The name is Foth's; the content in play " +
        "here is the invariance, not the tetraplectic condition (bean " +
        "`qou-8p1g`).",
    },
  ],
});

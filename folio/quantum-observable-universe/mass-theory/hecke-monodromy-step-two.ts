import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:hecke-monodromy-step-two",
  title:
    "The Hecke quadratic is the q-deformed branch-point monodromy of the colour cubic (Step 2 of the canonical chain as a conjecture)",
  lean: {
    ref: "qou:QOU.Mass.HeckeMonodromy",
    validation: "not_checked",
  },
  computation: {
    engine: "python",
    script: "computations/probes/colour_cubic_branch_monodromy_probe.py",
    witness: "computations/probes/colour-cubic-branch-monodromy.witness.json",
    status: "verified",
  },
  uses: ["conj:lifted-crossing-locality"],
  cites: ["kohno1987", "drinfeld1985", "jones1987"],
  tags: [
    "tier:keystone",
    "step-2",
    "non-abelian-stokes",
    "hecke-quadratic",
    "monodromy",
    "picard-lefschetz",
    "kz-connection",
    "axiom-class",
    "open-problem",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): exactly as an instance of `QOU.Mass.KZPullbackGenerators` is on the other." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): (probe `colour_cubic_abelian_twist_holonomy_probe`, 8/8)" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): Constructing the connection itself, and hence an instance of the class, remains open." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): and from that class the Hecke quadratic is derived rather than assumed." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): That hypothesis now has a name, `QOU.Mass.KZPullbackGenerators`: each substrate generator" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): ## Lean structure\n\nThe class `QOU.Mass.HeckeMonodromy` is stated for a tower over a commutative ring $R$ with a unit $q$, and carries items 1 and 2 as its four fields (`quad`, `braid`, `far_comm`, and `shadow_at_one`, which says $\\varepsilon(q) = 1$). Derived from it without further hypotheses: `hecke_factor` (the eigenvalue factorisation), `shadow_involution`, `shadow_hecke_at_one`, `shadow_kills_h`, and `shadow_coxeter` (the shadow generators satisfy the Coxeter presentation of $S_n$: involution, braid relation, far commutation, so $\\varepsilon \\circ \\varrho$ is a permutation representation, as the computed $S_3$ requires). If $q - q^{-1}$ is a unit of $R$, the shadow ring is zero (`subsingleton_of_isUnit_h`); the rank-one model over $\\mathbb{Z}[q, q^{-1}]$ with $\\varepsilon$ the evaluation at $q = 1$ satisfies every field with shadow ring $\\mathbb{Z}$ (`HeckeMonodromy.LaurentModel`). The classical shadow itself is proved unconditionally in `QOU.Mass.HeckeQuadraticClassicalShadow` (the swap is an involution satisfying the $q = 1$ quadratic), and the unit-modulus obstruction in `QOU.Mass.KZUnitModulusPrune`. Two facts the probe measured about the discriminant are theorems in `QOU.Mass.ColourCubicDiscriminant` and its archimedean companion: the sextic is reciprocal, $z^6 D(z^{-1}) = D(z)$, and it is the sum of squares $(4z^3 + 3z^2 + 3z + 4)^2 + 2z^2(z^2 + 1)$, so it has no real root and every branch point is non-real (`no_real_branch_point`)." },
    {
      kind: "status",
      date: "2026-09-06",
      body: "Replaces the dangling `prop:hecke-spectral-sequence` that two Lean docstrings cited. Cheat-sheet §2a (2026-08-25) established that the curvature 2-form of Step 2 is stipulated, not computed; this block states the stipulation as a conjecture whose `q = 1` shadow is derived (Picard--Lefschetz on the colour cubic, probe 11/11, `HeckeQuadraticClassicalShadow.lean`) and whose deformation is the open hypothesis. The Lean class carries four content fields; `hecke_factor`, `shadow_hecke_at_one`, `shadow_kills_h` are derived from it sorry-free.",
    },
  ],
});

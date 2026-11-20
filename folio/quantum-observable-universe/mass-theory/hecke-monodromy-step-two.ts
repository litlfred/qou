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
    {
      kind: "note",
      date: "2026-11-20",
      body:
        "Lean names moved out of the prose (voice drain, epic `qou-d4kh`): the structure is the class `QOU.Mass.HeckeMonodromy` (fields `quad`, `braid`, `far_comm`, `shadow_at_one`); derived: `hecke_factor`, `shadow_involution`, `shadow_hecke_at_one`, `shadow_kills_h`, `shadow_coxeter`, `subsingleton_of_isUnit_h`, model `HeckeMonodromy.LaurentModel`; unconditional shadow `QOU.Mass.HeckeQuadraticClassicalShadow`; obstruction `QOU.Mass.KZUnitModulusPrune`; discriminant `QOU.Mass.ColourCubicDiscriminant`, `no_real_branch_point`.",
    },
    {
      kind: "status",
      date: "2026-09-06",
      body: "Replaces the dangling `prop:hecke-spectral-sequence` that two Lean docstrings cited. Cheat-sheet §2a (2026-08-25) established that the curvature 2-form of Step 2 is stipulated, not computed; this block states the stipulation as a conjecture whose `q = 1` shadow is derived (Picard--Lefschetz on the colour cubic, probe 11/11, `HeckeQuadraticClassicalShadow.lean`) and whose deformation is the open hypothesis. The Lean class carries four content fields; `hecke_factor`, `shadow_hecke_at_one`, `shadow_kills_h` are derived from it sorry-free.",
    },
  ],
});

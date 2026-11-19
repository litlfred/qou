import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-09",
      body:
        "Lean sibling: archimedean specialisation over $\\mathbb{R}$ " +
        "(AGENTS.md §7c). The proposition is a *convergence* statement, so " +
        "there is no ring-generic form of it. " +
        "`QOU.Archimedean.VolumeTowerDecomposition` carries " +
        "`totalVolume : ℝ` with `0 < totalVolume`, a level series " +
        "`levelContribution : ℕ → ℝ`, and two fields that are irreducibly " +
        "analytic: `Summable (fun n => |levelContribution n|)` and " +
        "`HasSum levelContribution totalVolume`. Absolute summability needs " +
        "an absolute value and a limit; `HasSum` needs a topology. Its two " +
        "consequences are the same kind of object — `tendsto_zero` " +
        "($\\Phi_n \\to 0$ in `nhds 0`) and `eventually_small` (the " +
        "$\\varepsilon$–$N$ form). Replacing $\\mathbb{R}$ by a `CommRing` " +
        "would delete the content, not generalise it.\n\n" +
        "The quantity being decomposed is archimedean for an independent " +
        "reason: the volumes this file supplies are transcendental-analytic " +
        "constants. `vol_4_1` is the Lobachevsky evaluation " +
        "$\\mathrm{Vol}(4_1) = 2\\,\\mathrm{Cl}_2(\\pi/3) = 6\\,\\Lambda(\\pi/3)" +
        "\\approx 2.0298832$ (two regular ideal tetrahedra), and `vol_B3` is " +
        "the symbolic $8G$ with $G$ Catalan's constant, itself defined in the " +
        "file as the `tsum` $\\sum_k (-1)^k/(2k+1)^2$. The surrounding " +
        "irrationality and $\\mathbb{Q}$-independence classes " +
        "(`SingleVolumeIrrational`, `HyperbolicVolumeIndependence`, " +
        "`BorelZagierQOU`) quantify over rational linear and polynomial " +
        "combinations of those reals; transcendence has no statement over a " +
        "generic ring, since it is precisely a claim about the embedding into " +
        "$\\mathbb{R}$. The cosimplicial tower the decomposition indexes " +
        "(`QOU.Torsion.RecursiveBraneTower`) is the generic half and stays " +
        "where it is.\n\n" +
        "Corrected in the same pass: the file's `vol_4_1` docstring and its §1 " +
        /* <!-- literal-source: closed-form Clausen evaluation 3 * Cl_2(pi/3) = 3.04482485 --> */
        "summary both read $3\\,\\mathrm{Cl}_2(\\pi/3)$, which is $3.0448\\ldots$ " +
        "rather than the $2.0298\\ldots$ literal the definition carries.",
      see: "folio/quantum-observable-universe/lean/QOU/Archimedean/HyperbolicVolumeTranscendence.lean",
    },
  ],
  label: "prop:volume-tower-decomposition",
  title:
    "Tower-level decomposition of hyperbolic volume",
  tags: [
    "hyperbolic-volume",
    "cosimplicial",
    "brane-tower",
    "quantum-dilogarithm",
    "spectral-sequence",
  ],
  uses: [
    "prop:cosimplicial-crossed-groupoid",
    "prop:topological-mass-formula",
  ],
  lean: { ref: "qou:QOU.Archimedean.VolumeTowerDecomposition",
    validation: "not_checked",
  },
  computation: {
    engine: "mpmath",
    script: "computations/derive_m_baryon_volume_form.py",
    witness: "computations/m-baryon-volume-form.witness.json",
    status: "verified",
  },
});

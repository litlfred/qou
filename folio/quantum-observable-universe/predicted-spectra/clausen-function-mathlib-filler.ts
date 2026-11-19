import { remark } from "../../schema/builders";

export default remark({
  label: "rem:clausen-function-mathlib-filler",
  title:
    "Clausen function $\\mathrm{Cl}_2$ as repo-internal Mathlib filler",
  interprets: "rem:figure-8-archimedean-illustration",
  uses: ["prop:em-coupling-bring-zero-mode"],
  cites: ["thurston1978", "zagier1986"],
  computation: {
    engine: "mpmath",
    script: "computations/q_pinning_50_digit.py",
    witness: "computations/q-pinning-50-digit.witness.json",
    status: "verified",
  },
  tags: [
    "mathlib-filler",
    "clausen-function",
    "bloch-wigner",
    "hyperbolic-volume",
    "figure-8-knot",
    "borromean-rings",
    "catalan-constant",
    "lean-infrastructure",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-19",
      body: "Formalization provenance moved from prose and tables: `QOU/Archimedean/ClausenFunctionMathlibFiller.lean` provides `Cl_2 : ℝ → ℝ` via `tsum`, `Cl_2_zero` (`simp`), `Catalan_constant`, `Vol_figure_8`, `Vol_Borromean`, and sketches `Cl_2_reflection_2pi_open`, `Cl_2_pi_third_positive_open`. The integral definition, derivative `Cl_2'(θ) = -log(2 sin(θ/2))`, and Zagier series–integral bridge are machine-proved in `QOU/Knot/Clausen.lean`, and the figure-eight Kashaev volume limit is machine-proved in `QOU/Knot/FigureEightVolumeSqueeze.lean`. Upstream Mathlib gaps and conditional classes: `Real.dilog`/`Complex.dilog` (partial `LiTwo` in `dilogarithm-archimedean-limit.lean`), `BlochGroup F`, `BlochSuslinUniqueness`, `ArchimedeanLimit`, `BringZeroModeBlochClass`, `BringHyperbolicDecomposition`, `BWQIndependence`, and `BlochWignerInjective`.",
    },
  ],
});

## Pattern

Each Mathlib gap is a separate, scoped task. The Cl_2 filler
shows the cleanest case: one well-known function, defined as
a `tsum`, with two unconditional boundary lemmas and four
sketched-but-open extensions awaiting Fourier-series
infrastructure. The same pattern can be applied to:

* a `Real.dilog` filler (extending the existing `LiTwo` to the
  complex domain via `Complex.dilog`);
* a minimal `BlochGroup F` filler (free abelian group quotient by
  5-term pentagon relations) — substantial, ~200 lines.

These are not addressed here; the present file restricts to the
single-function $\mathrm{Cl}_2$ filler that directly supports the
α_EM and figure-8 chains.

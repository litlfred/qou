import QOU.Resurgence.StokesMatrixDescent
import QOU.Resurgence.WardFiltrationCounting

/-!
# `QOU.Resurgence` — umbrella

Aggregates the resurgent-bridge modules so the `QOU` Lake target compiles them
in CI (a standalone library file with no `.ts`/`.md` sidecar otherwise escapes
the umbrella build and can silently rot — Copilot review, PR #4525).
-/

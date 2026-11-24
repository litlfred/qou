import QOU.StandardModel.StokesMatrixDescent
import QOU.StandardModel.WardFiltrationCounting
import QOU.StandardModel.StokesPhaseSignChirality
import QOU.StandardModel.StokesConstantQDimCategoricity

/-!
# `QOU.Resurgence` — umbrella

Aggregates the resurgent-bridge modules so the `QOU` Lake target compiles them
in CI (standalone library files with no `.ts`/`.md` sidecar otherwise escape the
umbrella build and can silently rot — Copilot review, PRs #4525/#4538).
-/

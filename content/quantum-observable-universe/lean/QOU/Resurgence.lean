import QOU.Resurgence.StokesMatrixDescent
import QOU.Resurgence.WardFiltrationCounting
import QOU.Resurgence.StokesPhaseSignChirality
import QOU.Resurgence.StokesConstantQDimCategoricity

/-!
# `QOU.Resurgence` — umbrella

Aggregates the resurgent-bridge modules so the `QOU` Lake target compiles them
in CI (standalone library files with no `.ts`/`.md` sidecar otherwise escape the
umbrella build and can silently rot — Copilot review, PRs #4525/#4538).
-/

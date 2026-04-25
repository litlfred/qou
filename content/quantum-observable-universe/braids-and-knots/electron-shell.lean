/-!
# QOU.BraidKnot.ElectronShell

An electron shell of multiplicity `Z` around a nucleon-level atom
is a cabling `H_A(q) ↪ H_{A+Z}(q)` plus an SDP-selected binding
subword. Binding multiplicity `μ(S, q)` counts the active dual
blocks of the confinement SDP; `μ ≥ 2` at magic `Z` (noble gas) is
the multi-operator regime.

LaTeX: `\label{def:electron-shell}`
-/

import QOU.Basic

namespace QOU.BraidKnot

universe u

/-- Placeholder for the confined-particle type. -/
opaque NucleusTy : Type

/-- **Electron shell.** Cabled-strand representation: `Z` electrons
    added as extra strands in `H_{A+Z}(q)` with binding subword
    drawn from the confinement-SDP active support. -/
-- Ref: [manuscript] braids-and-knots/electron-shell
structure ElectronShell where
  /-- The nucleus particle the shell is attached to. -/
  nucleus : NucleusTy
  /-- Number of electrons in the shell. -/
  nElectrons : ℕ
  /-- Total strand count `A + Z` after cabling. -/
  nStrandsTotal : ℕ
  /-- Canonical binding subword as a formal Hecke word. -/
  bindingWord : String

/-- Binding multiplicity `μ(S, q)` — cardinality of the active dual
    support of the confinement SDP at substrate parameter `q`.
    `μ = 1` is the single-block regime; `μ ≥ 2` is the multi-operator
    regime that obtains at noble-gas `Z`. -/
-- Ref: [manuscript] particle-interactions/confinement-sdp
opaque bindingMultiplicity : ElectronShell → ℝ → ℕ

end QOU.BraidKnot

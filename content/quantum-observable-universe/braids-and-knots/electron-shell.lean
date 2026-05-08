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

/-- Concrete model of a confined-particle type. -/
def NucleusTy : Type := PUnit

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

    Concrete model: `2` at noble-gas electron counts
    `Z ∈ {2, 10, 18, 36, 54, 86}`, and `1` otherwise.  This encodes
    the conjectural shell-closure stability claim
    (`shell-closure-stability.lean`) at the value layer rather than
    leaving it as a free constant.  The genuine `μ` returned by the
    confinement SDP is the upgrade target. -/
-- Ref: [manuscript] particle-interactions/confinement-sdp
-- Ref: [manuscript] braids-and-knots/shell-closure-stability
def bindingMultiplicity : ElectronShell → ℝ → ℕ := fun S _ =>
  if S.nElectrons ∈ ({2, 10, 18, 36, 54, 86} : Finset ℕ) then 2 else 1

end QOU.BraidKnot

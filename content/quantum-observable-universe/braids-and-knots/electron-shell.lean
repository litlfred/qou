/-!
# QOU.BraidKnot.ElectronShell

An electron shell of multiplicity Z around a nucleon-level atom is
a cabling H_A(q) ↪ H_{A+Z}(q) plus an SDP-selected binding subword.
Binding multiplicity μ(S, q) counts the active dual blocks of the
confinement SDP; μ ≥ 2 at magic Z (noble gas) is the multi-operator
regime.

LaTeX: `\label{def:electron-shell}`
-/

import QOU.Basic

namespace QOU.BraidKnot

universe u

/-- **Electron shell.** Cabled-strand representation: Z electrons
added as extra strands in H_{A+Z}(q) with binding subword drawn
from the confinement SDP active support. -/
-- Ref: [manuscript] braids-and-knots/electron-shell
structure ElectronShell (R : Type u) [CommRing R] where
  nElectrons : Nat
  nStrandsTotal : Nat

end QOU.BraidKnot

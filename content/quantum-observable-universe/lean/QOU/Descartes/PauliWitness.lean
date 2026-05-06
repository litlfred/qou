import QOU.Descartes.PauliWitness.Witness2H
import QOU.Descartes.PauliWitness.Witness3H
import QOU.Descartes.PauliWitness.Witness3He
import QOU.Descartes.PauliWitness.Witness4H
import QOU.Descartes.PauliWitness.Witness4He
import QOU.Descartes.PauliWitness.Witness5He
import QOU.Descartes.PauliWitness.Witness5Li
import QOU.Descartes.PauliWitness.Witness6He
import QOU.Descartes.PauliWitness.Witness6Li
import QOU.Descartes.PauliWitness.Witness7Be
import QOU.Descartes.PauliWitness.Witness7Li
import QOU.Descartes.PauliWitness.Witness8Be
import QOU.Descartes.PauliWitness.Witness8Li
import QOU.Descartes.PauliWitness.Witness9B
import QOU.Descartes.PauliWitness.Witness9Be
import QOU.Descartes.PauliWitness.Witness10B
import QOU.Descartes.PauliWitness.Witness10Be
import QOU.Descartes.PauliWitness.Witness11B
import QOU.Descartes.PauliWitness.Witness11C
import QOU.Descartes.PauliWitness.Witness12B
import QOU.Descartes.PauliWitness.Witness12C

/-!
# Pauli Witness Computations

All 21 F_Pauli witness files for isotopes 2H – 12C.

Each module defines `tr_alt_<iso>`, `net_<iso>`, `F_Pauli_<iso>_denom`,
and `observable_<iso>` as exact Laurent polynomials in ℤ[t, t⁻¹]
(where `t = q^{1/2}`), computed by hecke-engine 0.8.0.

## Isotope coverage

| Isotope | Z | N | A | Module              |
|---------|---|---|---|---------------------|
| ²H      | 1 | 1 | 2 | `Witness2H`         |
| ³H      | 1 | 2 | 3 | `Witness3H`         |
| ³He     | 2 | 1 | 3 | `Witness3He`        |
| ⁴H      | 1 | 3 | 4 | `Witness4H`         |
| ⁴He     | 2 | 2 | 4 | `Witness4He`        |
| ⁵He     | 2 | 3 | 5 | `Witness5He`        |
| ⁵Li     | 3 | 2 | 5 | `Witness5Li`        |
| ⁶He     | 2 | 4 | 6 | `Witness6He`        |
| ⁶Li     | 3 | 3 | 6 | `Witness6Li`        |
| ⁷Be     | 4 | 3 | 7 | `Witness7Be`        |
| ⁷Li     | 3 | 4 | 7 | `Witness7Li`        |
| ⁸Be     | 4 | 4 | 8 | `Witness8Be`        |
| ⁸Li     | 3 | 5 | 8 | `Witness8Li`        |
| ⁹B      | 5 | 4 | 9 | `Witness9B`         |
| ⁹Be     | 4 | 5 | 9 | `Witness9Be`        |
| ¹⁰B     | 5 | 5 | 10| `Witness10B`        |
| ¹⁰Be    | 4 | 6 | 10| `Witness10Be`       |
| ¹¹B     | 5 | 6 | 11| `Witness11B`        |
| ¹¹C     | 6 | 5 | 11| `Witness11C`        |
| ¹²B     | 5 | 7 | 12| `Witness12B`        |
| ¹²C     | 6 | 6 | 12| `Witness12C`        |

## References
- [leitner2026] §7/descartes-universe (Pauli witness computation)
-/

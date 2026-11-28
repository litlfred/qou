# A derived p-shell Coulomb shape factor (5 ≤ A ≤ 16), replacing the imported ball

Date: 2026-11-28. Beans `qou-tcl3`, `qou-usft`. Follows PR #9866 (the length reduces to the
cell radius `c`) and PRs #9665/#9699 (the s-shell q-Hankel `f = 0.520011`).
Probe: `computations/probes/coulomb_pshell_shape/coulomb_pshell_shape_probe.py` (mpmath 60 dps,
7/7 checks). Lean: the shape factor `f² = E²M₂/Q⁵` is already defined and its dilation
invariance proved in `QOU/Nuclear/CoulombShellShapeFactor.lean`; this note evaluates it on a
new density and adds no theorem.

## 1. Pre-registration (written before any p-shell number was computed)

The same construction as the s-shell, with one rule extended: `ν = l + ½`, so the p-shell
(`l = 1`) uses `J_{3/2}`. The charge fills 0s with up to 2 protons and 0p with `Z − 2`. Both
orbitals sit on the same Jackson lattice at dilation index `n = 0`, and the alternates
`n_p = ±1` are reported but never selected.

## 2. Result

| Z | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|
| `f`, primary `n_p = 0` | 0.5141 | 0.5117 | 0.5105 | 0.5097 | 0.5092 | 0.5088 |
| `f`, `n_p = +1` | 0.5139 | 0.5115 | 0.5102 | 0.5094 | 0.5089 | 0.5086 |
| `f`, `n_p = −1` | 0.5161 | 0.5141 | 0.5128 | 0.5119 | 0.5113 | 0.5108 |

The imported uniform ball is 0.4648. The derived `f` runs smoothly from the s-shell's 0.5200
to 0.509, so **the jump of 1.119 at A = 5 disappears**. The lattice-index convention moves `f`
by at most 0.5 %.

## 3. Comparison only (AME2020 mirror splits; CAL-3 radius with `c = 1`, the open card)

| pair | AME ΔB | imported ball | derived p-shell |
|---|---|---|---|
| ³H/³He (s-shell, already derived) | 0.764 | n/a | 0.948 (+24.1 %) |
| ⁷Li/⁷Be | 1.644 | 1.917 (+16.6 %) | 2.101 (+27.8 %) |
| ¹¹B/¹¹C | 2.764 | 2.748 (−0.6 %) | 3.004 (+8.7 %) |
| ¹³C/¹³N | 3.003 | 3.119 (+3.9 %) | 3.408 (+13.5 %) |
| ¹⁵N/¹⁵O | 3.537 | 3.469 (−1.9 %) | 3.790 (+7.2 %) |

## 4. Reading it

1. **The derived shape looks worse than the ball, and that is not evidence for the ball.** This
   is the same situation PR #9691 met at A = 3. The ball is an assumed shape, and its smaller
   misses are two errors cancelling.
2. **With the derived shape the miss has one sign, + 7 % to + 28 %, from A = 3 to A = 15.** The
   sign change PR #9866 found between ⁷Li and ¹⁵N came from the imported ball, as it suspected.
   What is left is the same sign everywhere, which is what a length that is too short gives. So
   the lever now really is the single number `c` (owner card open). This note does not choose it.
3. **Not wired.** `coulomb_energy.shape_factor` still uses the ball above A = 4. Wiring would
   move 17 consumer witnesses and is left for the owner.

Scope (a). No measured value is in any proof or in `f`.

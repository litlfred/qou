# gg_four_strand — results (bean qou-a1hh; hypothesis only; nothing wired)

Pre-registration ba70b76ef7a, plus an amendment written before any readout: on 4 strands
only s ∈ {0, 1} is a vertex site, so there are 4 vertex types V0, B0, V1, B1, and lengths
run to m = 6 (5460 words). Convention D, proton q₀, base module at 40 dps.
Reading 3 alone = every character at levels 1..4 ≥ −1e-30.

## Check: T0 (restriction to sites {0} agrees with the 3-strand values): PASS

## R1 pass counts
| m | pass / words |
|---|---|
| 1 | 0 / 4 |
| 2 | 0 / 16 |
| 3 | 16 / 64 |
| 4 | 32 / 256 |
| 5 | 0 / 1024 |
| 6 | 518 / 4096 |

## R2: pass is NOT a function of length alone (E1 holds)
It is almost entirely a function of the **site pattern** (which site each vertex sits
on), and almost blind to orientation (V vs B):

- m = 3: patterns 000 and 111 pass for all 8 orientations each. One-site words only.
- m = 4: patterns 0101 and 1010 pass for all 16 orientations each.
- m = 6: patterns 000000, 111111 and the six cyclic rotations of 000111
  (000111, 001110, 011100, 111000, 110001, 100011) pass for all 64 orientations.
  Six other patterns (alternating-type) pass for exactly one orientation each:
  B0.V1.B0.V1.B1.V0, B0.V1.B1.V0.B0.V1, V1.B0.V1.B1.V0.B0, V1.B1.V0.B0.V1.B0,
  B1.V0.B0.V1.B0.V1 (χ_(3,1) = 0.42048999549) and B1.V0.B1.V0.B1.V0 (χ_(3,1) = 0.374693274178).

## Reading (scope a)
- Since the trace is cyclic, "rotations of 000111" is one class: three vertices on site 0
  followed by three on site 1. Site 0 spans strands 0–2, site 1 spans strands 1–3.
- Orientation (V/B, the chirality pair bit) does not decide passing except in the six
  single-orientation words. Site placement does.
- The site bit is a new binary label beyond V/B. Whether it is related to the σ₃-eigenline
  flavour of the n ≥ 4 doublet thread is not tested here.

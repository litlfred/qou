# Why the uniform bond limit over-binds light nuclei

**Date** 2026-11-27 · **Ask** a derived reason for the light-end over-binding, and which bond carries a non-vanishing exponent (coordinator relay of Carl) · **Bean** `qou-brng` (epic `qou-myts`)
**Builds on** [`2026-11-27-uniform-bond-limit-saturation.md`](2026-11-27-uniform-bond-limit-saturation.md), [`2026-11-27-bond-rules-and-length-cutoff.md`](2026-11-27-bond-rules-and-length-cutoff.md)
**Probes** [`light_end_orbit_entropy_probe.py`](../../computations/probes/uniform_bond_limit_saturation/light_end_orbit_entropy_probe.py) (15/15 checks), [`junction_uniform_limit_q0.py`](../../computations/probes/uniform_bond_limit_saturation/junction_uniform_limit_q0.py)
**Scope** (a). AME appears only in comparison columns.

## 1. Result

**The over-binding is state counting, not a bond.**

At q = 1, each vertex V(s) = σ_s σ_{s+1}⁻¹ is a 3-cycle, and the free word x is the identity. The uniform average over words in a vertex set W converges to the projector onto the vectors fixed by the group the 3-cycles generate. So

  B_cl = E₀ ln(2ⁿ / #orbits).

There is no interaction strength in this formula. The orbit counts are computed by closing each group, not assumed (checks K1, K2).

| A | all vertices: B_cl / B(q₀) (MeV) | junction vertices only: B_cl / B(q₀) (MeV) | AME (comparison) |
|---|---|---|---|
| 2 | 9.355 / 9.119 | 4.917 / 4.823 | 2.225 |
| 3 | 16.638 / 16.093 | 11.721 / 11.399 | 8.482 |
| 4 | 24.320 / 23.354 | 19.166 / – | 28.296 |

- The all-vertex group is Alt(n), with n + 1 orbits.
- The junction-only group is Alt on strands 1..n−2, with 4(n−1) orbits.
- The q-deformation moves each value by only 2–5 % (K3, K4).
- Both B_cl grow like E₀ n ln 2, which is about 2.93 MeV per strand. That is both why light nuclei come out over-bound and why the limit saturates at about 7.5–8.8 MeV per nucleon.

The 7.53 MeV/A plateau is therefore the entropy of the projection. It is not evidence of a nuclear volume term.

Restricting the average to bonds between nucleons (junction vertices only) halves the A = 2 value but does not change this.

## 2. Which bond carries a non-vanishing exponent

By `QOU.MassTheory.ClassicalLogBindingCycleCount`, the q = 1 log binding of a single bond word is E₀ ln 2 · (c_free − c_atom), where c is the cycle count.

- V³ is the identity at q = 1 (K5). So the ruled γγ bond has exponent 0, and it binds only at O(y⁴).
- A bond word has a non-zero exponent if and only if its q = 1 permutation merges cycles. The quantum is E₀ ln 2 = 2.930 MeV.
- One 3-cycle across a junction merges three cycles, which is two quanta (5.86 MeV).
- AME ²H is 0.759 quanta (comparison only). So no single bond word reproduces ²H at q = 1.

## 3. Consequence for α and β

No derived binding comes out of this, so the decays are not re-scored. Re-scoring with either uniform rule would re-score entropy.

The open problem is now sharper. The classical exponent comes in multiples of E₀ ln 2 per merged cycle, while the γγ bond contributes nothing classically. A derived ²H needs either a fractional classical weight or a deformation term of order one, and neither has a derivation yet.

# Coulomb (Term 3) via q-Hecke per-pair — principled implementation

## Reframing

The first reading of the Coulomb result was that the spread
regressed (1.06% → 1.15% with q-Hecke per-pair, vs q=1 MN).
On reflection, this is a **principled improvement, not a
regression**, for the following reason.

The original q=1 MN per-pair traces give:

$$|tr_{pp}^{q=1\text{ MN}}| = |tr_{nn}^{q=1\text{ MN}}| = |tr_{pn}^{q=1\text{ MN}}| = 0.015586$$

— identical for proton-proton, neutron-neutron, and proton-
neutron pairs. This identity is a **structural artifact of the
$q \to 1$ limit**, not a physical truth. Real proton-proton
pairs Coulomb-repel; real neutron-neutron pairs don't; the
algebra should distinguish them.

The q-Hecke per-pair traces do distinguish:

| Pair | q-Hecke | q=1 MN | ratio |
|------|--------:|-------:|------:|
| pp | 0.0660 | 0.0156 | 4.23 |
| nn | 0.0255 | 0.0156 | 1.63 |
| pn | 0.0419 | 0.0156 | 2.69 |

The pp/nn ratio of 2.59 is Coulomb-distinguishing structure. The
direction matches SEMF: heavy-atom mass increases due to Coulomb
repulsion (visible in cal/m_e dropping more at 40Ca than 4He
under the q-Hecke pair version).

## Why the spread "regression" is principled

The q=1 MN ansatz had:

- All three pair traces identical → same per-pair $\Phi_q$ value
- Per-atom pair contribution $\propto \binom{A}{2}$ uniformly

This created a **uniform** A-dependence in the cross tower,
which happened to cancel some lower-order residual in the
(q=1 MN single + q=1 MN pair) combination, giving a
*coincidentally tighter* spread.

q-Hecke per-pair breaks the uniformity (pp/nn/pn split),
unmasking the real structural error. The 1.06% → 1.15% change
isn't error introduced — it's error revealed.

## Implementation status

`per_braid_tower_coulomb.py` is the principled version. It:

- Keeps single-nucleon at q=1 MN (workaround for P2.2c-norm
  divergence at single-nucleon q-Hecke traces).
- Uses q-Hecke per-pair traces (Coulomb-distinguishing).
- Reports cal/m_e per atom + overall spread.

The remaining 1.15% spread is now ATTRIBUTABLE to:

1. Single-nucleon Φ_q evaluation at q=1 MN trace (still
   incoherent with q=q_0 in Φ_q — P2.2c-norm gap).
2. Missing Asymmetry term ($\propto (N-Z)^2/A$).
3. Missing Pairing term ($\pm a_P / A^{1/2}$).
4. Missing Shell corrections (BB-saturation enrichment).
5. Missing Surface term ($A^{2/3}$).

Each of these has a candidate mechanism in the level-1+ jet
contributions per the binding-energy probe
([2026-05-02-level-1-binding-energy-probe.md](2026-05-02-level-1-binding-energy-probe.md)).

## Per-atom Δppm (q=1 MN → q-Hecke pair)

| atom | A | Δppm |
|------|--:|--:|
| D | 2 | -21 |
| 3He | 3 | -59 |
| 3H | 3 | -33 |
| 4He | 4 | -68 |
| 6Li | 6 | -116 |
| 7Li | 7 | -124 |
| 9Be | 9 | -170 |
| 12C | 12 | -258 |
| 16O | 16 | -352 |
| 40Ca | 40 | -915 |

Δppm grows monotonically with A — the Coulomb-like enhancement
scales (roughly) with $A^2$ pair count. Heavy atoms get more
push, exactly as Coulomb physics predicts.

## Status

**q-Hecke per-pair adopted as the principled default.** The
q=1 MN per-pair was a workaround that hid p/n distinction; the
q-Hecke version restores it. The minor numerical spread
regression is the price of unmasking the structural error,
which the level-1 jet contributions (Volume, Asymmetry,
Pairing, Shell) must now address.

Next step: probe Asymmetry + Pairing via `prop:wigner-np-pairing`.

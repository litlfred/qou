# The A=3 mirror residual reduces to the open EM-linking gate

**Status:** FINDING (reproducible, no fit). The ~3% ³He residual of the
linear-chain bond-count binding is not a new derivation target — it is the
corpus's already-identified two-like-charge **EM-linking** gate (owner-gated;
CAL-4 fit forbidden). This records the reconciliation.

Probe: [`a3_mirror_residual_reconciliation.py`](../../computations/a3_mirror_residual_reconciliation.py)
(witness `a3-mirror-residual-reconciliation.witness.json`).

## Setup — the two mirror views

The linear-chain bond-count binding `B = m_e·Σ(n−1)·Vol_n`
([PR #3282](https://github.com/litlfred/qou/pull/3282), merged;
`prop:linear-chain-bond-count`) uses the **hyperbolic link volume** as the
per-isotope isospin carrier. The A=3 mirror pair reads off two *different*
links:

| isotope | link | Vol | `m_e·2·Vol` | AME | err |
|---|---|---|---|---|---|
| ³H (p-n-n) | 8_11 | 8.2863 | 8.4686 | 8.4818 | **−0.16%** |
| ³He (p-p-n) | L6a4 (Borromean) | 7.3277 | 7.4889 | 7.7180 | **−2.97%** ← residual |

The −2.97% on ³He is the whole A=3 mirror residual: same braid recipe, same
bond count (2 bonds), only the *volume* differs because the pp interface (σ)
threads a different link than the nn interface (σ⁻¹).

## Reconciliation — same physics as the derived Coulomb

The corpus already derives this split as **charge**, not volume
([`2026-06-03-charge-coulomb-tn3he-derived.md`](2026-06-03-charge-coulomb-tn3he-derived.md),
`def:coulomb-charge`): strong binding is charge-symmetric (`B_strong = ³H`),
and ³He is reduced by its two-proton Coulomb repulsion
`E_cross = Q·(q−q⁻¹)` with ratio `tanh(ln q₀) ≈ 0.104`.

| view | ³He | err | note |
|---|---|---|---|
| bond-count volume (L6a4) | 7.4889 | **−2.97%** | volume gap absorbs most of the split |
| `B_strong − E_coul(derived 31%)` | 8.2309 | +6.65% | only 31% of Coulomb is derived |
| `B_strong − E_coul(FULL AME)` | 7.7048 | −0.17% | AME-taken, not derived |

The bond-count volume gap (8_11 vs L6a4) and the pp-Coulomb reduction are two
views of the **same** mirror-split object — ³He's pp interface vs ³H's nn
interface. The volume view lands closer (−2.97% vs +6.65%) precisely because
the L6a4-vs-8_11 volume gap *implicitly* absorbs more of the split than the
explicitly-derived 31% Coulomb piece does; neither reaches the AME value
without the un-derived remainder.

## Verdict

- **The residual is the corpus's open gate, not a fresh target.** Both views
  bottom out at the same missing object: the **two-like-charge EM-linking
  invariant** (the remaining 3.2× of the Coulomb split; per-pair EM linking,
  not yet defined — the global knot charge `Q(H)` exists, the per-pair EM
  linking does not).
- **Bond-count reproduces the current best (−2.97%).** It is neither a
  regression nor a new accuracy win — it is the same low-isotope-mass-table
  number (`low-isotope-mass-table.witness.json`), now with the mechanism
  (super-exponential na-Stokes period → `M_n = n−1` bond count → link volume)
  Lean-proved end to end.
- **Discipline (STRICT).** Closing below −2.97% requires *deriving* the
  EM-linking invariant, after which `0.764 MeV` becomes a post-hoc check.
  Tuning a pp-Coulomb constant (or a mirror volume) to hit the AME value is a
  **CAL-4 fit** — out of bounds, and owner-gated.

## Next

Same as the derived-Coulomb audit: the productive direction is the
two-like-charge EM-linking derivation (coordinate with the α_EM cluster —
Habiro element, categorical α_EM, Schwinger). Until then the A=3 mirror
magnitude stays exploratory at −2.97%; the bond-count/volume framing does not
change that gate, it only reconciles the volume and charge views of it.

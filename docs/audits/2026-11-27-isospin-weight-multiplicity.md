# The isospin multiplicity term: a derived `1/A` with no `ln(2T+1)`

Date: 2026-11-27. Bean `qou-o8lo` (ledger gap G2), epic `qou-myts`. Follow-up to
[`2026-11-27-isospin-twist-writhe-scaling.md`](2026-11-27-isospin-twist-writhe-scaling.md),
which shows that the braid-channel `T(T+1)` term is exactly `0` on γγ-selected words. #9706
is closed (Carl, 2026-11-27); the #9685 algebra stays. Derive-only, nothing wired.

Lean: `QOU/Nuclear/IsospinWeightMultiplicity.lean`. Probe:
`computations/probes/isospin_weight_multiplicity_probe.py` (witness
`isospin-weight-multiplicity`).

## 1. Result (Lean, sorry-free)

| statement | Lean |
|---|---|
| two-row block dimension `d(N,k) = C(N,k) − C(N,k−1)` equals the hook value: `d·(N−k+1) = C(N,k)(N−2k+1)` | `twoRowDim_hook` |
| the weight count is the sum of block counts: `Σ_{j≤k} d(N,j) = C(N,k)` | `sum_twoRowDim` |
| one step from balance: `C(2M,M−s−1)(M+s+1) = C(2M,M−s)(M−s)` | `weight_step` |
| Gaussian suppression with no logarithm: `C(2M,M−s)(M+s+s²) ≤ C(2M,M)(M+s)` | `weight_le` |

`#print axioms` on `sum_twoRowDim`, `twoRowDim_hook`, `weight_le`: `[propext,
Classical.choice, Quot.sound]`. No real number, no log and no measured value is used.

## 2. Reading

A nucleus with `Z` protons and `N_n` neutrons has `n_u = 2Z + N_n` up and `n_d = Z + 2N_n`
down quarks on `3A` strands, so it fixes `T_z = (n_u − n_d)/2 = (Z − N_n)/2`, not `T`. The
number of states with that `T_z` is the **weight count** `C(3A, n_d)`, which by
`sum_twoRowDim` is the sum of the block dimensions over all blocks with `T ≥ |T_z|`.

The previous audit (§4) used the single lowest block, whose log is
`ln(2T+1) − 2T²/N`. The `ln(2T+1)` piece pulls the wrong way and dominated at ²⁰⁸Pb. **The
weight count has no `ln(2T+1)` piece**: summing over the blocks cancels it. What is left is
the Gaussian, with scale `s ~ √M` (`weight_le`), so any energy linear in `ln(count)` is a
function of `T_z²/N ∝ (N_n − Z)²/A`. This is the `(N−Z)²/A` shape, from counting alone.

## 3. What is not derived

**The energy map.** Nothing in the corpus turns a count into an energy. The probe uses
`B += α·ln(count)` with the proxy scale `α = 8G·m_e = 3.744 MeV`. The sign (a larger count
binds more) and the log are both assumptions. It is the entropy-like reading, and the
2026-08-07 options audit §A3 already called the `1/A` "Fermi-gas level density, a separate
dynamical input". A log-of-trace functional `ln tr(w)` would give `ln dim` on the identity, but
the corpus log law is `Σ ln|eigenvalue|`, which gives `0` there. This is the open step.

## 4. Size (comparison only; AME is not used to choose anything)

| variant | median \|ΔQ_β\|/Q_β (Table 3.4b, 1010 rows) |
|---|---|
| no term | 92.69 % |
| weight count `C(3A, n_d)` | 84.26 % |
| lowest block alone | 91.61 % |

| nucleus | weight-count share (MeV) | `−α·2T_z²/N` (MeV) | classical `−23(N−Z)²/A` (MeV) |
|---|---|---|---|
| ⁴⁸Ca | −0.827 | −0.832 | −30.7 |
| ⁵⁶Fe | −0.177 | −0.178 | −6.57 |
| ¹³²Sn | −4.83 | −4.84 | −178 |
| ²⁰⁸Pb | −5.80 | −5.81 | −214 |

The shape is right: the share tracks `−α·2T_z²/N` to within 1 %. The size is about **37
times** too small at the proxy scale `α`. With `N = 3A` the coefficient is
`α·2/(4·3) = α/6 ≈ 0.62 MeV` per `(N−Z)²/A` against ~23. The scale belongs to the
scale-unification thread. This is a scope-(a) result: the multiplicity term alone, at this
`α`, is not the symmetry energy. It does not exclude it.

## 6. The q-CLT and the Markov weighting (Carl, 2026-11-27: "use qCLT")

The probe counts are exact binomials at every `A`; "Gaussian" in §2 was only the name of
their large-`A` shape, i.e. the classical (`q = 1`) CLT. Two checks of the `q`-version:

1. **q-CLT.** The corpus limit object (`QOU.Observations.QCltCut`, a conjecture with no
   instance) is the q-Gaussian with moments in `ℤ[q]`. Its second moment is `1` at every `q`
   (`QOU.Core.QGaussianMoments.qGaussMoment_two`). So the leading `−2T_z²/N` term keeps its
   coefficient; `q` first enters through `m₄ = 2 + q` (against `3`), a `T_z⁴/N³` correction.
2. **Markov weighting.** Under convention D the Markov trace is the `U_q(sl₂)` quantum trace,
   which weights the `T_z` sector by `C(N,k)·q^{N−k}·qi^k`. Lean (same file, sorry-free):

   | statement | Lean |
   |---|---|
   | the sectors sum to `(q + qi)^N = [2]_q^N` | `markov_sector_sum` |
   | a sector times its mirror `T_z ↔ −T_z` is `C(N,k)²`, with no `q` | `markov_sector_mirror` |

   Checked numerically at `N = 6, 9, 12, 30`: `Σ_T d_T [2T+1]_q = Σ_k C(N,k) q^{N−2k} = [2]_q^N`.
   So the `q`-weighting multiplies each sector by an **odd** factor `q^{2T_z}`, and the even part,
   which a symmetry energy reads, is the classical count exactly. Under `B += α ln(weight)` the
   odd factor would add `2α ln q·T_z`, linear in `T_z` with no `1/A`. That is a separate channel,
   not a symmetry term, and it is not computed against data here.

Conclusion: neither the q-CLT nor the Markov weighting changes the `(N−Z)²/A` coefficient. The
factor of ~37 stays in the scale and in the open energy map.

## 5. Verification

- Lean: `lean -DautoImplicit=false -s 65536 QOU/Nuclear/IsospinWeightMultiplicity.lean` exit 0.
- Probe: `PYTHONPATH=computations python3 computations/probes/isospin_weight_multiplicity_probe.py`, 3/3 checks pass (row count, baseline median, `weight_le` re-checked for `M < 60`).
- No content block is touched, so no KG JSON-LD node changes. No measured value appears in any proof.

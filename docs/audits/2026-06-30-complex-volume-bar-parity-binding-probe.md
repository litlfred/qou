# Complex-volume 𝔙 probe: does the imaginary/bar-odd part fix the binding error? (2026-06-30)

**Branch**: `claude/formula-for-q-bzym14` · **PR**: [#3183](https://github.com/litlfred/qou/pull/3183)
**Owner question**: "are we forcing q real when we take `|·|`/the norm? Is there
an imaginary part of q we should calibrate to that might fix the remaining
mass-binding error?"
**Probe**: [`binding_bar_even_odd_probe.py`](../../computations/binding_bar_even_odd_probe.py)
(`binding-bar-even-odd-probe.witness.json`), plus the existing
[`complex_volume_witness.py`](../../computations/complex_volume_witness.py).

## The question, made precise

Production binding evaluates the Markov trace at the **real anchor q₀ only**
(and takes `|tr_M|`), discarding the bar-odd (`q ↔ q⁻¹`) shadow. Per
[`conj:binding-qbeta-complex-volume`](../../content/quantum-observable-universe/mass-endomorphism/binding-qbeta-complex-volume.md)
that shadow is `Im 𝔙 = Q_β`. Keeping **both** evaluations splits the binding

$$B(q) = E_0\ln\frac{\mathrm{tr}_M(W_{\text{free}};q)}{\mathrm{tr}_M(W_{\text{atom}};q)},\quad
B_{\text{even}}=\tfrac12[B(q_0)+B(q_0^{-1})],\quad B_{\text{odd}}=\tfrac12[B(q_0)-B(q_0^{-1})]$$

into the bar-even (cosh / `P_avg`, the corpus-canonical projection) and bar-odd
(sinh / `P_skew`) parts. `E_0 = m_e/(q_0(q_0-1)) ≈ 4.186` MeV (CAL-1+CAL-2).

## Results (50-dps)

| iso | B(q₀) raw | B_even (cosh) | B_AME | even err | raw err | B_odd (sinh) |
|---|---:|---:|---:|---:|---:|---:|
| 2H | 3.890 | 3.000 | 2.225 | 34.9% | 74.9% | 0.889 |
| 3H | 9.068 | 6.311 | 8.482 | 25.6% | 6.9% | 2.757 |
| 3He | 6.797 | 5.908 | 7.718 | 23.5% | 11.9% | 0.889 |
| 4He | 11.975 | 9.218 | 28.296 | 67.4% | 57.7% | 2.757 |

**MAE: B_even = 37.8%, B(q₀) raw = 37.8%.** Im channel (separately): Q_β,pred =
0.7836 vs CODATA 0.7823, **0.17%**.

## Findings

1. **The bar-even projection does NOT fix binding.** `B_even` leaves the same
   ~38% MAE as the raw real-anchor `B(q₀)` — it only *redistributes* the error
   (better for 2H, worse for 3H). So "the binding residual is a dropped
   bar-odd parity" is **refuted as the simple explanation**. The residual's
   real source is elsewhere — the open Δ_λ closure and/or the log-trace
   proxy form of `B`, not the choice of parity.

2. **But the bar-odd (imaginary) channel is real and structured.** `B_odd`
   depends **only on N** (the neutron number: 2H & 3He → 0.889; 3H & 4He →
   2.757), at the Q_β energy scale (~0.9–2.8 MeV). The imaginary part the owner
   sensed **is present and is neutron-organized** — physically the decay
   channel — confirming the complex structure of `conj:binding-qbeta-complex-volume`
   *qualitatively*. It is **not** numerically equal to the free-neutron `Q_β`
   (a different transition), and it is **not** the lever that closes binding.

3. **Askey/q-orthogonal ladder is visible.** `ln[tr_atom(q₀⁻¹)/tr_atom(q₀)]/ln q₀`
   shifts by a constant **≈ 6.68 per added neutron** (2H→3H and 3He→4He both
   −6.67), a clean per-nucleon q-power increment — consistent with the corpus's
   Rogers–Szegő / q-Hermite identification of the binding period
   (`docs/audits/2026-06-26-binding-period-qinvolution-qhermite-identification.md`,
   the proved `FollowsRogersSzego` class).

## Where the imaginary part *does* live, and the genuine next test

The single-normalization 𝔙 packaging is correct (`complex_volume_witness.py`):
one `E₀` gives `Im 𝔙 = Q_β` to 0.17% while `Re 𝔙 = binding` is 7–75% off. The
parity-split test here shows the gap is **not** a discrete bar-parity artifact.
The holomorphic tie the conjecture actually asserts is a **Cauchy–Riemann /
q-derivative** relation (the `recurrence_invol_descent` c_k-ladder: one
three-term recurrence with a bar-even multiplier yields *both* the binding and
Q_β ladders), not the `½[B(q₀)±B(q₀⁻¹)]` projection. The c_2 evidence — bar-even
net-route `c_2 ≈ −8.0` vs bar-odd brane-tower `c_2 = −1` — is the live signature
of two parities of one complex `c_2`. **The genuine next probe** is therefore:
test whether `(binding, Q_β)` satisfy the holomorphic c_k recurrence at one
normalization (an Askey–Wilson three-term recurrence), *not* whether a parity
projection of `B` matches AME.

## Askey note (a real absent connection)

The corpus already identifies the binding recurrence as **Rogers–Szegő /
q-Hermite** (proved Lean class) and the Δ_λ residual as **Askey–Racah**
(`docs/audits/2026-06-29-delta-lambda-imme-askey.md`). What is **absent**: the
**Rogers dilogarithm `Li_2^q` ↔ Rogers q-ultraspherical polynomial** duality —
the symmetric (Rogers) dilog used in the brane tower and the Rogers polynomial
recurrence are the functional/basis pair of the *same* compact (bar-even)
Askey world, while the **Faddeev** dilog is the non-compact (bar-odd) partner.
Making that identification explicit would tie the lepton-tower `Φ_q` work
(this PR) to the binding/Q_β complex-volume program under one Askey scheme.
This is a lead, not a result.

## Cross-references

- Conjecture: [`binding-qbeta-complex-volume.md`](../../content/quantum-observable-universe/mass-endomorphism/binding-qbeta-complex-volume.md)
- Existing 𝔙 compute: [`complex_volume_witness.py`](../../computations/complex_volume_witness.py)
- Rogers–Szegő identification: [`2026-06-26-binding-period-qinvolution-qhermite-identification.md`](2026-06-26-binding-period-qinvolution-qhermite-identification.md)
- Δ_λ Askey–Racah: [`2026-06-29-delta-lambda-imme-askey.md`](2026-06-29-delta-lambda-imme-askey.md)

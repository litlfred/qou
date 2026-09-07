---
# qou-tbk7
title: 'Z-resolved b3: build the (Z,N)-resolved binding construction the per-atom word already distinguishes (takeover of #7005)'
status: in-progress
type: task
priority: normal
created_at: 2026-09-07T18:06:40Z
updated_at: 2026-09-07T18:30:22Z
parent: qou-6g7j
---

PR #7005 (branch claude/binding-resolution-is-self-inflicted-2026-09-07, idle > 10 h) measured: AME knows the light bindings to 6.7–7.6 digits; b3 = B(3) − 3B(2) is resolved to ~6 digits per mirror partner but the A-only body-order construction averages ³H and ³He into a 53.6 % band (0.27 digits) — 5.81 digits lost to convention, none to experiment. atom_canonical_crossings(Z,N) returns DIFFERENT words for (1,2) and (2,1) (#6942). Task: build the Z-resolved construction — evaluate the body-order tower on the per-(Z,N) word rather than on A — and measure its resolution and its residual against AME for ²H, ³H, ³He, ⁴He. Report honestly: recoverable resolution says nothing about whether there is anything to recover. No fitting; no per-case dispatch; proton pin; convention D; mpmath end to end.

## Findings (takeover session, 2026-09-07) — probe `computations/probes/z_resolved_b3_mirror_split_probe.py`, 17/17, witness `z-resolved-b3-mirror-split-probe.witness.json` (q0Anchor proton)

**1. Resolution, measured exactly (Fraction propagation, σ² = σ₃² + 9σ₂²):**
b₃(³H) = 1808.0976 keV, σ 0.001500 → **6.081 digits**; b₃(³He) = 1044.3427 keV,
σ 0.001282 → **5.911**; split b₃(³H) − b₃(³He) = 763.7549 keV, σ 0.001006 → **5.880**.
#7005's ~6.1 inference confirmed as a measurement.

**2. Framework Z-resolved b₃ := B(Z,N) − 3B(1,1) on the per-(Z,N) word at the proton q₀,
convention D — NEGATIVE on every form, target POSITIVE (MeV):**

| form | b₃(³H) | b₃(³He) | split |
|---|---:|---:|---:|
| chain (production `_bond_type_L`, writhe-normalised) | −2.3587 | −3.1241 | +0.76532 |
| exact Markov trace `tr_m_atom_zn`, α·ln, un-normalised | −1.8685 | −3.6156 | +1.74707 |
| B_can⁰ = α(tr_free − tr_atom) | −1.3739 | −1.3042 | −0.06971 |
| **AME** | **+1.8081** | **+1.0443** | **+0.76375** |

Each form is pairwise-additive, so its "b₃" is the bond-heterogeneity term b_XX − 2b_pn,
not a connected cumulant — the pairwise wall (`PairwiseCumulantVanishing`,
`MayerThreeBodySign`, bean `qou-edt7`) in Z-resolved form. Chain ≡ exact + writhe shift
to 2e-50 at all four nuclides (verified).

**3. The A=3 split lands from q₀ alone:** chain split = b_nn − b_pp =
**α·ln(q₀³(1 + q₀ − q₀²)) = 0.7653202 MeV** vs AME 0.7637549 (+0.205 %, +1.565 keV,
1556 σ_exp — not an L2 match). Closed form uses z_D − h = 1/(q(q²+1)). The writhe factor
α·ln(1−h) = −0.9818 MeV is load-bearing; without it the split is 1.7471 (2.29×, the C-frame
"3×" of `2026-07-11-mirror-split-coulomb-diagnosis`).

**4. And it is a coincidence at A=3:** the chain split is the same constant at every
mirror pair, AME grows: 3H/3He 0.7638 (ratio 1.002), 7Li/7Be 1.6442 (0.465), 13C/13N
3.0028 (0.255). Already recorded in `coulomb_mirror_killswitch_probe` (0.002 MeV hit at
A=3 beside 0.65 / 1.59 MeV misses). B_can⁰ split has the WRONG sign, as
`mirror_penalty_decomposition_probe` / `c1_mirror_asymmetry_sign_probe` found.

**Verdict, scope (a):** the Z-resolved construction exists (0.1 s per A=3 word), has the
~6 digits, reproduces neither b₃ magnitude (wrong sign, all forms) and reproduces the A=3
split by a Z-independent coincidence. What it buys is a separation: the A-only b₃ mixes
the mirror bond difference (framework: predicted; data: Coulomb) with the connected
3-body term (framework ≤ 0; data > 0). The second is the open object. No ingredient
excluded; the 31 % `tanh(ln q₀)·B_pp` derivation and the EM-linking gate untouched.

Not done (cost): ⁶Li/⁷Li b-tower on the Z-resolved word — ⁷Li exact trace is 24 s, so
cheap, but the tower above b₃ needs A=5 (unbound) and the same pairwise wall applies;
left for a follow-up if wanted.

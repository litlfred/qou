# Δ_λ-route: the two remaining *selection/α-cluster* directions both closed (2026-06-17)

**Branch:** `claude/delta-lambda-selection-alpha-refuted-2026-06-17`
**Picks up:** the Δ_λ-route arc (#2405/#2417/#2426/#2430). After the operator
route was shown (#2430) to gate on the LP `𝓑₃`-selection, the two remaining
candidate paths — **(1) close the `𝓑₃`-selection gate**, **(2) the α-cluster
recursion (sidestep)** — were each probed (parallel worktree agents).
**Both are negative.** Discipline: derive-or-refute; no fit, nothing rewired.

## (1) `𝓑₃`-selection: no continuous variational principle selects the Borromean signature

`𝓑₃` must be selected as the confinement bound-state operator, but the
min-action LP returns the trivial `tr_M=0` vertex (the indefinite Gram, eig
`[−0.855,+0.102,+0.855×3,+3.48]`). Tested every corpus-grounded continuous
principle — **all negative.**

- **The SDP lead is refuted.** `solve_psd_operator_selection_sdp` enforces
  `diag(Gx) ≽ 0`, which is *mathematically identical* to the LP's componentwise
  `Gx ≥ 0` (`lp_dual_solver.py:487,531,588`; the negative Gram eigenvalue never
  enters a `diag(Gx)` constraint). It returns the **same trivial `tr_M=0`
  vertex**. The *genuine* dense PSD (`confinement-sdp.md`, `min⟨T,Φ⟩ s.t. Φ⪰0,
  tr Φ=1`) is **stated but not implemented** in `lp_dual_solver.py`; run directly
  (cvxpy) it concentrates on the smallest-cost **mesonic** channel (`L±`),
  `cos ≤ 0.06` to `𝓑₃` — never the Borromean baryon.
- **The decisive control — signature-cos.** `NF(𝓑₃)` is **99.8% the identity
  `γ`**; its Borromean signature (γ-orthogonal part) has norm only **0.065**. So
  raw `cos`-to-`𝓑₃` is dominated by `cos`-to-`γ` and misleads. Scoring on the
  cosine in the γ-orthogonal subspace
  ([`computations/probes/b3_selection_signature_cos.py`](../../computations/probes/b3_selection_signature_cos.py)):

  | principle | full-cos | **sig-cos** |
  |---|--:|--:|
  | LP / diag-PSD-SDP | −0.44 | **−0.015** |
  | stationary `xᵀGx, Σx=1` | +0.70 | **+0.018** |
  | stationary `xᵀGx, t·x=1` | +0.998 | **(pure γ)** |
  | min‖x‖², `t·x=1` | +0.72 | **+0.005** |
  | dense PSD SDP (any T) | ≤0.06 | ≤0.06 |

  **Every** high-full-cos candidate is just `γ` in disguise — the `+0.998` one is
  *literally* `x=(1,0,0,0,0,0)=γ`. **None reproduces the Borromean signature.**
- **The caveat's "min-|λ| vertex" is wrong** (`confinement-lp.md:94`): `𝓑₃` is
  not a G-eigenvector (best align `cos=0.80` with a degenerate `+0.855`, only
  `0.47` with the min-positive `+0.102`).
- **The corpus's actual selection is NOT the LP.**
  `confinement-operator-selection.md:48` selects `𝓑₃` by a **discrete
  candidate ranking + a topological-Borromean tiebreak** (an external physical
  input) — and `𝓑₃` does not even win `|Δnet|` there. The optimization the props
  advertise does not select it.

**Verdict (1):** real gap. The candidate fix is to **implement the genuine
dense per-block Wedderburn-projector SDP** (`confinement-sdp.md`, the unbuilt
object) with the correct `π_λ` + cost operator, or **promote the topological
(Borromean = no separable sub-link) criterion into the program** rather than
applying it as an after-the-fact tiebreak. Open.

## (2) α-cluster recursion: fit-blocked

`B(nα) = n·B(⁴He) + n_pairs·c_αα` with ⁴He from `B_magic = ρ_F·m_e·A·8G`.

- `8G = Vol(Borromean) = 7.3277` is **genuinely derived**; `B_magic(⁴He)=29.96`
  MeV (+5.87% vs AME). But `ρ_F=2`, `Vol=A·8G` are modelled assembly.
- **`c_αα` is fitted:** `_deprecated/jsj_alpha_clustering.py:90` fits it from ¹²C
  (`2.4249`); the "derived" `m_e·Vol(7²₁)=2.4270` matches that fit to **0.09%**
  (its own derivation script is self-described as an after-the-fact-match check,
  not a forward derivation).
- **`c_αα=0` fails:** `n·B_magic` runs **+5.9% → −6.8%**, error **changes sign at
  ¹²C**. The required `c_αα` is **non-constant** (216% spread, sign flip; ⁸Be
  needs a *negative* coupling — it is physically α–α unbound by ~90 keV). **No
  single coupling, fitted or derived, can reproduce the series.** Errors are
  2.5–6.8% (~10⁷ ppb), 7 orders above the CAL-2 floor.

**Verdict (2):** the α-cluster recursion is a near-match (one derived constant in
a modelled assembly with a fitted, non-constant coupling), **not a non-fit path**
— exactly the standing Δ_λ-gate situation ("the α-unit magnitude has no clean
combinatorial count"; `2026-06-16-b-sym-linear-chain-closed-form.md §6`).

## Net — the Δ_λ *selection/α-cluster* arc is bounded

> **Rescope note (2026-06-23).** "both closed" / "fully bounded" narrowed:
> Verdict (1) itself records a **real gap, Open** (candidate fix: the unbuilt
> dense per-block Wedderburn-projector SDP, or promoting the topological
> criterion into the program). What is closed is the *continuous-variational
> selection* approach and the *α-cluster sidestep* — not the Δ_λ gate. The
> on-scale log-free-energy functional (`B_sym`, 0.57–2.36× AME) is outside this
> arc. Numeric results unchanged. See
> [`2026-06-23-over-zealous-binding-closure-review.md`](2026-06-23-over-zealous-binding-closure-review.md).

The full arc (LP → quadratic → Bring → chirality → scalar-magnitude → operator
→ **𝓑₃-selection → α-cluster**) has closed every tractable lever:

- **sign = chirality** — proved (keystone).
- **scalar magnitude / trace functional** — refuted (#2417; the scalar trace
  factorizes exactly, zero cooperativity).
- **operator-cumulant scalar** — gated on `𝓑₃`-selection (#2430).
- **`𝓑₃`-selection by any continuous principle** — refuted here (1); rests on an
  external topological criterion.
- **α-cluster sidestep** — fit-blocked here (2).

The **only** non-refuted non-fit levers left are research-scale constructions:
**GAP-A-3** (substrate-derived `A(K)` × an *open* partition-projection `P_λ(K)`),
or **implementing the genuine dense Wedderburn-projector SDP** for `𝓑₃`-selection
(which, if it selects the Borromean signature, unlocks the operator-cumulant
scalar of #2430). Both are genuine open research; neither is a quick or fitted
closure. Recorded so the closed levers are not re-tried.

## Cross-links
- [`b3_selection_signature_cos.py`](../../computations/probes/b3_selection_signature_cos.py) — the signature-cos selection probe (this audit's (1)).
- `content/quantum-observable-universe/mass-theory/confinement-sdp.md` — the genuine dense PSD (the unbuilt candidate fix).
- `content/quantum-observable-universe/particle-interactions/confinement-operator-selection.md` — the actual discrete+topological selection.
- `docs/workplans/2026-06-17-operator-cumulant-cooperative-binding.md` (#2430) — the operator route that gates on (1).
- `docs/audits/2026-06-16-b-sym-linear-chain-closed-form.md §6` — the standing α-magnitude gate.

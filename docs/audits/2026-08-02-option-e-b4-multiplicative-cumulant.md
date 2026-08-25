# The multiplicative connected 4-body cumulant b₄ reaches only 6.3 % of the ⁴He target — scope-(a) undershoot, 0-fit

**Date:** 2026-08-02 · **Branch:** `claude/option-e-b4-cumulant-2026-08-02` ·
**Type:** FINDING — honest negative (scope-(a)) with a structural non-vacuity
sub-result. Δ_λ closure, Option-E **front 4** (interface-operator / 4-body
cumulant route). No fit, nothing wired.

- Probe: [`computations/deltalambda/b4_multiplicative_cumulant_probe.py`](../../computations/deltalambda/b4_multiplicative_cumulant_probe.py)
  (witness [`b4-multiplicative-cumulant.witness.json`](../../computations/deltalambda/b4-multiplicative-cumulant.witness.json),
  4/4 assertions pass, mpmath 50 dps, exit 0).
- Lean: [`content/quantum-observable-universe/lean/QOU/MassTheory/B4MultiplicativeCumulant.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/B4MultiplicativeCumulant.lean)
  (sorry-free, `lean`-direct exit 0, v4.24.0; no `sorry`/`native_decide`/trivial-true/axiom).

## 0. What this is, and how it differs from the siblings

Front 4 has two live A=4 framings this week; they attack **different objects**
and must not be conflated:

| framing | object | branch / file | verdict |
|---|---|---|---|
| **det surjectivity gate** | `b₄ = −ln det(I + m·S)` of the writhe **exchange matrix** `S` (spectrum `{±√5,±1}`) | `claude/a4-interface-magnitude-2026-08-02`, `A4InterfaceMagnitude.lean` | one-scalar gate, form **surjective** onto (0,∞), reaching-`m` = fit ⇒ WALL(scope-a) |
| **multiplicative joint cumulant** (this PR) | `b₄ = fourthDiff(B(A))` of the canonical binding `B = E₀·τ_vac·(1 − ∏ᵢ fᵢ)` | this branch, `B4MultiplicativeCumulant.lean` | magnitude **6.3 %** of target ⇒ scope-(a) undershoot |

The additive Möbius μ₄ (`helium4_mu4_cluster_moment_probe.py`, on main) is a
**third** object: the 64-subset joint block-trace moment via the 2⁶ H₁₂ traces
(`μ₄ = M(4) − Σμ₂ − Σμ₃`, `pyhecke_native`). This PR's multiplicative cumulant
uses the **closed-form** interface factors (`closed_form_tau_M`, mpmath) — no
`pyhecke_native` — so it is independently reproducible in any sandbox.

## 1. The construction (0-fit, `free_parameters = 0`)

Canonical multiplicative binding (`binding_canonical.py`,
`interface_4body_assembly_probe.py`) on the genuine many-body **complete graph**
K_A (all C(A,2) pairs):

    B(K) = E₀ · τ_vac · (1 − ∏ᵢ fᵢ),

with everything derived at the substrate q₀:

- `E₀ = m_e/(q₀(q₀−1)) ≈ 4.18598 MeV`
- `τ_vac = τ_p^Z · τ_n^N`, `τ_p ≈ 1.220363` (cached H₃ trace, phase5l),
  `τ_n = tr_M(D)/(τ_p·z) ≈ 1.194862` (solved)
- pair factors `z ≈ 0.499320` (Markov), `pp = z`, `nn = z − h`,
  `pn = z` (production) or `z − h/2` (bar-invariant), `h ≈ 0.209060` (Hecke)

The connected 4-body Ursell cumulant is the 4th forward finite difference
(`BodyOrderCumulant.fourthDiff`) of the binding sequence, with A=3 taken
isospin-symmetric:

    b₄ = B(4) − 4·B(3) + 6·B(2) − 4·B(1) + B(0),
    B(0)=B(1)=0,  B(2)=B(1p1n),  B(3)=½(B(1p2n)+B(2p1n)),  B(4)=B(2p2n, K₄).

The **target** applies the *same* finite difference to the AME bindings with
`B(3) = ½(B(³H)+B(³He)) = 8.0999 MeV`, giving `b₄^target ≈ 9.2434 MeV`.
**B_AME is diagnostic-only** — it forms the target, it never fits the framework.

## 2. Result — scope-(a) undershoot

| pn convention | B(A), A=0..4 (MeV) | framework b₄ | **fraction of target** |
|---|---|---:|---:|
| **z** (production marshalling) | 0, 0, 3.0561, 6.6435, 8.8203 | **0.5826 MeV** | **6.30 %** |
| z − h/2 (bar-invariant proj.) | 0, 0, 3.6941, 6.9163, 8.8691 | 3.3687 MeV | 36.4 % |

The production headline **6.30 %** reproduces the prior (uncommitted) session's
reported 6.3 % exactly. Both conventions **undershoot**; neither was tuned.

**Cause (structural).** `(1 − ∏ f)` **saturates**: with 6 bonds at K₄ the product
`∏f → 0` fast, so `B → E₀·τ_vac` and the only residual A-growth is the weak
`τ_p^Z τ_n^N`. The connected 4-body content of a saturating function is small.
This is the same saturation `interface_4body_assembly_probe.py` reported (the
complete-graph topology barely moves `B(⁴He)/B(D)` vs the linear chain).

## 3. Why this is NOT a scope-(b) exclusion — the multiplicative route DOES carry connected 4-body content

`BodyOrderCumulant.lean` proved the **additive** binding forms are *orthogonal*
to the 4-body channel: `fourthDiff_linear = 0` (1-body `B_vol`),
`fourthDiff_pairwise = 0` (2-body `B_sym`). The **multiplicative** `∏f` is an
exponential in the pair count C(A,2), hence **not** pairwise-additive, and its
cumulant is **generically nonzero**:

- `multBinding_b4` — closed form
  `b₄ = τ⁴(1−f⁶) − 4τ³(1−f³) + 6τ²(1−f)`.
- `multBinding_b4_at_f_one = 0`, `satBinding_b4 = 3 − 6f + 4f³ − f⁶`,
  `satBinding_b4_at_f_one = 0` — sanity vanishings (no coupling ⇒ no cumulant).
- `multBinding_b4_nonvacuous : fourthDiff (multBinding 1 0) = 3 ≠ 0` — the
  **contrast**: the multiplicative b₄ is nonzero where every additive form is 0.

So the multiplicative form is the structurally correct place to look for the
missing ⁴He b₄ — it is *not excluded*, it merely **undershoots in magnitude**.
The probe's guard mirrors the Lean: `fourthDiff` of the concrete 1-body-linear
and 2-body-pairwise sequences returns 0 to 40 dps.

## 4. I-par refinement — the pn factor is bar-mixed (retained = bar-even projection z)

`b4_connected_bar_parity_probe.py` (on main) established `z` bar-even, `h`
bar-odd, so `pn = z − h/2` is **bar-mixed** — the original I-par phrasing
"prove b₄ is bar-even" is too strong for the multiplicative route (unlike the
writhe-determinant route of `B4CumulantBarEven`, which is genuinely bar-even).
This PR formalises the split over a generic `CommRing` (doubled, to avoid
division):

- `twoPnFactor_bar_mixed`: the bar image differs by `2h` (bar-invariant iff `h=0`).
- `twoPnFactor_barEven_proj`: bar-even projection = the Markov weight `z`
  (retained binding — the production `pn = z` headline).
- `twoPnFactor_barOdd_proj`: bar-odd projection = `−h/2` (radiated, Q_β-like).

The production headline `pn = z` **is** the bar-even (retained-binding)
projection; the 6.30 % is therefore the retained-binding fraction. The
bar-invariant `pn = z − h/2` convention (36.4 %) carries the extra bar-odd
amplitude and is reported as the upper envelope.

## 5. Surviving gap

The multiplicative connected 4-body cumulant of the interface binding, **alone**,
supplies only ~6 % (retained) / ~36 % (bar-mixed) of the ⁴He `b₄`. The missing
~94 % / ~64 % must come from a **non-saturating** connected 4-body operator —
one whose 4-body cumulant grows rather than saturating. Candidates already on the
board (not re-attacked here): the `[1⁴]` exchange determinant with a categorical
principle fixing `m ∈ (0,1/√5)` strictly below the naive `z`
(`A4InterfaceMagnitude` one-scalar gate); the anti-self-adjoint GGM/Stokes
off-block the branching leaves free (`A3OffBlockDerivation`,
`conj:qdifference-kernel-prolongation-symbol`, bean `qou-jqof`). The saturation
of `(1 − ∏f)` is the structural reason a *multiplicative* interface product
cannot be that operator.

**Nothing wired.** `μ₄`/`b₄`/`B(⁴He)`/AME/CODATA/`q₀` never inverted;
`free_parameters = 0`. Bean records the gap.

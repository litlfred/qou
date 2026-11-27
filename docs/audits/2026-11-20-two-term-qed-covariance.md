# Two-term QED on the nucleon weight spaces: braid covariance settles the #8518 / #8367 inconsistency

**Date:** 2026-11-20
**Lean:** [`QOU/BraidsAndKnots/NucleonQEDCovariance.lean`](../../folio/quantum-observable-universe/lean/QOU/BraidsAndKnots/NucleonQEDCovariance.lean) (70 theorems, sorry-free, generic `[Field R]`)
**Probe:** [`computations/probes/nucleon_qed_covariance_probe.py`](../../computations/probes/nucleon_qed_covariance_probe.py) (exact `sympy` over `Q(q)`, `mpmath` 70 dps at the proton `q₀`, no witness)
**Context:** PR #8518 (merged; `NucleonWeightSpaceTwoTerm.lean`, audit `2026-11-18-two-term-qed-downstream-and-211ppb-audit.md`) and open PR #8367.

## 1. The inconsistency

PR #8518 inserts the **adjacent** pairwise charge operator `Q₁₂ + Q₂₃` on the
3-dimensional nucleon weight spaces `W_p = (2,1)` and `W_n = (1,2)`, evaluates it on
the Borromean word `V³ = (σ₁σ₂⁻¹)³`, and reads off a zero-parameter `M_p^QED`
(m_μ tension 211 → 8 ppb) and `Δm_QED` (70–78 % of the convention-D `Q_β` N=2 residual).
PR #8367 objects that the insertion is a selection: summed over all three pairs the
insertion is word-independent (`trace_QPair_diff_word`), the connected term exists only
because pair 1–3 is dropped, and the scale (`m_e` / `E₀` / `α_bind`) and weighting
(plain / `K_n/K_p` / `K_p³` / `q`) are chosen.

The question the owner asked: **resolve it by proof.** The resolving principle is
braid covariance. A charge insertion is a *local operator on the braid*; for its trace
against a braid word to be a function of the braid (rather than of where the strands
are labelled), it must commute with the crossing generators. That condition is checkable
and it is what the file proves things about.

## 2. What is proved (all sorry-free; `#print axioms` = `propext, Classical.choice, Quot.sound`)

Notation: `A₁, A₂` (resp. `B₁ = A₂`, `B₂ = A₁`) are the Hecke actions of `σ₁, σ₂` on
`W_p` (resp. `W_n`). `M q` and `N q = M q + q·1` with `N_{ij} = q^{i+j-3}`; `N` is the
rank-one operator on the trivial summand `(3)`, `N A_i = A_i N = q N`.

| | Lean | statement | hypotheses |
|---|---|---|---|
| **T1** | `commutant_A_iff`, `commutant_B_iff` | `O` commutes with both crossing generators ⇔ `∃ a b, O = a•1 + b•M q`; same set on `W_n` | `q ≠ 0` |
| **T2** | `QAdjp_not_comm_A₁/A₂`, `QAdjn_not_comm_B₁/B₂`, `QAdjp_not_mem_span` | `Q₁₂ + Q₂₃` commutes with **neither** generator on either weight space (defect entries `−2/3, 2/3, 1/3, −1/3`) and is not in `span{1, M}` | `2, 3 ≠ 0` (proton), `3 ≠ 0` (neutron) |
| **T3** | `trace_QAdjp_eq_neg_Q13p` (+ word / `V³` corollaries) | on `W_p`, `tr((Q₁₂+Q₂₃) X) = −tr(Q₁₃ X)` for **every** matrix `X` | none |
| | `trace_QAdjn_eq` | on `W_n`, `tr((Q₁₂+Q₂₃) X) = −(1/3) tr X − tr(Q₁₃ X)` | `3 ≠ 0` |
| **T4** | `covariant_trace`, `covariant_trace_word`, `covariant_trace_borromeanV3`, `covariant_trace_diff_word` | a covariant insertion gives `a·tr X + b·tr(M X)`; on positive words `b·q^{|w|}·tr N`; on `V³` (since `N V³ = N`) `b·tr N`; the `n−p` difference of any two covariant insertions depends on `w` only through `tr(w)` and `q^{|w|}` | `q ≠ 0` (+ `q²+1 ≠ 0` for `n−p`) |
| **T5** | `P3`, `P21`, `E`, `E_mem_span`, `E_idem`, `trace_E`, `E_of_comm` | isotypic idempotents `P_(3) = (q³/(q⁴+q²+1))•N`, `P_(2,1) = 1 − P_(3)` (idempotent, orthogonal, traces 1 and 2, commute with `A_i`); `E(Q) = tr(Q P_(3))•P_(3) + (tr(Q P_(2,1))/2)•P_(2,1)` lands in the commutant, is idempotent, preserves the trace, and is the identity on the commutant | `q ≠ 0`, `q⁴+q²+1 ≠ 0`, `2 ≠ 0` |
| **T6** | `E_QPairP`, `E_QPairN`, `E_QPair_Mcoeff_zero`, `trace_twoTerm_E_QPair_diff_word` | the permutation-complete `Q_pair` projects to `0` on `W_p` and `(−1/3)•1` on `W_n`; in the (unique, `coords_unique`) coordinates of `span{1, M}` its `M`-coefficient is **exactly 0**; the two-term splitting is `(q⁻¹ − q − c_em/3)·tr(w)` | as T5 |
| contrast | `E_QAdjp_eq` | `E(Q₁₂+Q₂₃)` on `W_p` = `α•1 + β•M` with `β = q³(q²−1)²/(3(q⁴+q²+1)²)`, `α = (q−1)³(q+1)³(2q²+1)/(9(q⁴+q²+1)²)` | as T5 + `3 ≠ 0` |

`E` is the matrix-trace-preserving expectation built from the two central idempotents.
Uniqueness of such an expectation (that any trace-preserving, commutant-valued,
commutant-fixing linear map equals `E`) is standard but is **not** proved in this file.

## 3. Consequences, with scope

1. **The adjacent insertion is not braid-covariant** — scope **(b)**, invariant T2
   (explicit non-commuting entries). Any number built from `tr((Q₁₂+Q₂₃)·w)` depends on
   the strand labelling, not only on the braid.
2. **The whole #8518 proton signal is minus the dropped pair** — scope **(b)**, T3 is an
   identity for every matrix. `(1/3)tr((Q₁₂+Q₂₃)V³) = −2(q−1)⁴(q+1)⁴(q⁴+q²+1)/(27q⁶)`
   and `(1/3)tr(Q₁₃V³)` is its exact negative. The connected "fourth-order" proton term is
   not a physical connected term; it is the label of the omitted pair, re-signed.
3. **The braid-covariant permutation-complete Coulomb insertion has `b = 0`** — scope
   **(b)**, T6. Its QED splitting is the scalar `−(c_em/3)·tr(w)`: word-dependent only
   through `tr(w)`, the same functional shape as the Cartan term. It can carry no
   `M`/trivial-isotypic structure and so cannot produce the #8518 connected numbers.
4. **A nonzero `M`-coefficient arises only from a pair subset** (`E_QAdjp_eq`, and
   `E(Q₁₃) = −E(Q₁₂+Q₂₃)` by T3 + linearity) — i.e. only by reintroducing the selection
   that #8367 objects to. Within **pairwise** charge insertions this is closed.
5. **Open, scope (a):** whether some *non-pairwise*, derived braid-covariant operator
   (e.g. a genuinely three-body or linking-weighted insertion) supplies a nonzero `b`
   with a *derived* coefficient. T1/T4 fix what such an operator can produce —
   `a·tr(w) + b·q^{|w|}·tr N` on positive words, `a·tr(V³) + b·tr N` on `V³` — and
   nothing more. Nothing here derives `b` or its scale.

## 4. What a derived two-term QED would need

- A **derived** coefficient `b` for the `M` (equivalently `N`, trivial-isotypic)
  component, from an operator that is braid-covariant by construction — not from a pair
  subset, and not from projecting a pair subset with `E` (that reproduces the selection).
- A **derived scale** `c_em`, the *same* scale as `Δm_QCD` (single-functional
  consistency, as the #8518 audit itself requires). The `m_e` / `E₀` / `α_bind` choice is
  still a choice; no file in this PR derives it.
- With `b = 0` (the only value derived for pairwise Coulomb), the derived two-term
  splitting is `(q⁻¹ − q − c_em/3)·tr(w)`, i.e. the QED term is a word-independent
  rescaling of the Cartan term once `c_em` is fixed.

## 5. Numbers at the proton `q₀ = 1.1099785827513808…` (70 dps; comparison only, nothing adopted)

From `nucleon_qed_covariance_probe.py`. keV figures use `m_e = 0.51099895069 MeV` only to
put them beside the #8518 figures; that scale is the #8518 choice, not a derived one.

| quantity | closed form | value |
|---|---|---|
| `(1/3)tr(V³)` | `−(q¹²−3q¹⁰+3q⁸−5q⁶+3q⁴−3q²+1)/(3q⁶)` | `0.99806193765998802891` |
| `tr N` (= `tr(N V³)`) | `(q⁴+q²+1)/q³` | `2.7421305742565559738` |
| `(1/3)tr((Q₁₂+Q₂₃)_p V³)` — #8518 "conn p" | `−2(q−1)⁴(q+1)⁴(q⁴+q²+1)/(27q⁶)` | `−0.00043068052000266024` |
| `(1/3)tr(Q₁₃,p V³)` — dropped pair | negative of the above | `+0.00043068052000266024` |
| `(1/3)tr(E(Q_pair)_p V³)` (T6) | `0` | `0` |
| `(1/3)tr(E(Q_pair)_n V³)` = covariant `n−p` | `−(1/9)tr(V³)` | `−0.33268731255332934297` |
| `(1/3)tr(E(Q₁₂+Q₂₃)_p V³)` (comparison) | `(q−1)⁶(q+1)⁶/(27q⁶)` | `3.0921861915192378071e-6` |
| #8518-style connected `n−p`, projected by `E` (comparison) | `−(q−1)⁶(q+1)⁶/(54q⁶)` | `−1.5460930957596189035e-6` |
| #8518 connected `n−p`, unprojected, recomputed | `(q−1)⁴(q+1)⁴(4q⁴+q²+4)/(27q⁶)` | `0.00064911296619550960` |

Read side by side: projecting the adjacent insertion onto its covariant part changes the
proton term from `−4.307e-4` to `+3.09e-6` (ratio `−0.00718`, sign flips, order
`(q²−1)⁶` instead of `(q²−1)⁴`); `m_e`-scaled that is `+0.00158 keV` against the #8518
`−0.2201 keV`. The connected `n−p` goes from `+6.491e-4` to `−1.546e-6` (ratio
`−0.00238`); `−m_e·(·)` is `+0.00079 keV` against the #8518 `−0.3317 keV`. So the
covariant part of the #8518 signal is ~0.2–0.7 % of it and of the opposite sign: the
8 ppb m_μ result and the 70–78 % `Q_β` closure come from the non-covariant remainder.

**Side finding (pin).** The #8518 audit quotes `−0.00043068071` and `+0.00064911326`
"at `q₀`". At the proton `q₀` these are `−0.00043068052` and `+0.00064911297`; the quoted
digits are the values at the **muon** `q₀ = 1.10997859564…` (recomputed:
`−0.000430680713834`, `+0.000649113259016`). The relative difference is `4.5e-7`, far
below anything the conclusions turn on, but the label is wrong.

## 6. Verification record

- `lean -DautoImplicit=false -s 65536 …/NucleonQEDCovariance.lean` → **exit 0** (53 s),
  against the restored olean cache (`cat/folio-assistant-sci/lake-cache/qou-v4-24-0`
  @ `a792c46d01b`) plus lean-direct oleans of `NucleonWeightSpace{Traces,SecondOrder,TwoTerm}`
  (each exit 0). No `lake build` was run.
- `#print axioms` on all 70 theorems: `[propext, Classical.choice, Quot.sound]`;
  `sorryAx` count 0. No `sorry`, `native_decide` or `axiom` in the file.
- Probe: 5/5 symbolic checks PASS.
- `scripts/precision-gates.sh --changed`: the probe emits no witness. The run reported
  RED on the q₀-anchor flip / refill / reference-literal / q₀-drift ratchets, which read
  witnesses this PR does not touch; I did not re-run the gates on bare `main` to confirm
  they are red there too. The witness files the gate run itself rewrote were reverted and
  are not in this PR.

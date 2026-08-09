# The q₀-free ≥3-row extensive cumulant: forward from the proved Δ_λ — reproduces μ₂=0, fails the sign-window and the magnitude ratio (scope-(a))

**Date:** 2026-08-08 · **Branch:** `claude/deltalambda-3body-extensive-2026-08-08`
**Bean:** `qou-prjo` (LEAD 1) · **Tier:** analysis / structural
**Probe:** [`computations/deltalambda/threerow_extensive_cumulant_forward_probe.py`](../../computations/deltalambda/threerow_extensive_cumulant_forward_probe.py)
**Witness:** `threerow-extensive-cumulant-forward.witness.json`
**Lean:** [`content/quantum-observable-universe/lean/QOU/MassTheory/ThreeRowExtensiveCumulant.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/ThreeRowExtensiveCumulant.lean)

`free_parameters = 0`. **No `q₀`, no AME inversion, nothing wired.** AME enters
only as fixed ratio *targets*, never inverted into a weight. This is the 7th-ansatz
danger zone; the result is a clean **scope-(a)** negative with one genuine 0-fit
structural match, reported as such.

---

## 0. TL;DR (four sentences)

1. Feed the **proved** ≥3-row signed-Springer-dimension content
   `s_k = Σ_{λ⊢k, ℓ(λ)≥3} (−1)^{n(λ)}·f^λ` (the Δ_λ of
   `dtEuler_eq_deltaLambda_unconditional`, restricted to the ≥3-row stratum —
   the stratum just measured to *dominate* binding, #4664) into the derived
   coordination-simplex `C(A,k)` cluster basis — **purely combinatorial, q₀-free.**
2. It **re-derives `μ₂ = 0` combinatorially** (`s₁ = s₂ = 0`), an *independent*
   derivation of the deuteron edge-coefficient zero that `AdditiveResidualSimplex`
   obtains from the graded-ladder self-reference — a genuine 0-fit structural match.
3. But the forward cumulants are `(ν₃, ν₄) = (−1, +2)` — the **opposite** sign-change
   order to the derived residual `(μ₃, μ₄) = (+0.4708, −4.591)` (the #4316 window
   `κ∈(3/2,3)` is `(+,−)`), and the forward magnitude ratio is exactly `|ν₄/ν₃| = 2`
   vs the derived `≈ 9.75`.
4. **Verdict: scope-(a).** The proved Δ_λ chirality parity supplies the deuteron
   `μ₂=0` but **not** the 3-body sign, the sign-change window, or the 4-body/3-body
   magnitude — so the many-body binding sign+magnitude is **not** a q₀-free
   combinatorial object; it lives in the archimedean (q₀-dependent) `y_λ·χ^λ`
   trace weighting. Surviving sub-question in §5.

---

## 1. The construction (forward, q₀-free)

The proved per-partition value is `Δ_λ = (−1)^{n(λ)}·dim V_λ = (−1)^{n(λ)}·f^λ`
(signed Springer dimension; `dtEuler_eq_deltaLambda_unconditional`, sorry-free,
general-n). Restrict it to the **≥3-row stratum** `ℓ(λ) ≥ 3` — the stratum #4664
measured to carry 26 % → 100 % of the binding sum as A goes 2 → 4 (binding is
≥3-row *dominated*, opposite to the two-row-dominated `tr_M`). Sum over partitions
of each cluster size `k`:

| k | ≥3-row partitions `λ` | `f^λ` | `n(λ)` | `Δ_λ` | `s_k` |
|---|---|---:|---:|---:|---:|
| 1 | — | | | | **0** |
| 2 | — | | | | **0** |
| 3 | `(1³)` | 1 | 3 | −1 | **−1** |
| 4 | `(2,1,1)`; `(1⁴)` | 3; 1 | 3; 6 | −3; +1 | **−2** |

(Python-verified in the companion probe; `s₅ = +4` recorded for completeness, not
used.) `s₁ = s₂ = 0` is **structural**: no partition of `k ≤ 2` has `≥ 3` rows.

**Extensive cluster functional.** Binding must be *additive/extensive* (a single
Markov trace over A strands is intensive and saturates —
`2026-06-02-binding-intensive-vs-extensive-derivation.md`). The size-consistent
cluster functional sums a per-cluster invariant over subsets:

```
B_ext(S) = Σ_{T ⊆ S, |T| ≥ 3} s_{|T|}      (homogeneous: = Σ_{k≥3} C(A,k)·s_k)
```

- `B_ext(2) = 0` — the deuteron carries **no** ≥3-body cluster content (any weight;
  `clusterF_eq_zero_of_card_le_two`, Lean, general).
- `B_ext(3) = C(3,3)·s₃ = −1`
- `B_ext(4) = C(4,3)·s₃ + C(4,4)·s₄ = 4·(−1) + 1·(−2) = −6`

Both readings of "extensive" are reported (I do **not** interpolate between them —
that would be the fit):

| reading | object | A=2 | A=3 | A=4 | `\|·(4)/·(3)\|` |
|---|---|---:|---:|---:|---:|
| **Y — extensive cluster sum** | `Σ_k C(A,k)·s_k` | 0 | −1 | −6 | **6.0** |
| **X — single A-body algebra** | `s_A` | 0 | −1 | −2 | **2.0** |

---

## 2. The 0-fit match: `μ₂ = 0`, re-derived combinatorially

Mayer-invert the single-algebra reading `S(A) = s_A` over the same `C(A,k)` basis
`AdditiveResidualSimplex` uses (`S(A) = ν₂C(A,2)+ν₃C(A,3)+ν₄C(A,4)`):

```
ν₂ = S(2)                 = 0
ν₃ = S(3) − 3·ν₂          = −1
ν₄ = S(4) − 6·ν₂ − 4·ν₃   = −2 + 4 = +2
```

`ν₂ = 0` **matches the derived `μ₂ = 0`** of `AdditiveResidualSimplex` — but derived
here from `s₁ = s₂ = 0` (no ≥3-row partition below A=3), *independently of* the
graded-ladder deuteron self-reference and *without any q₀*. This is the one genuine
0-fit positive: the "binding is ≥3-row-dominated" fact **implies** the deuteron
carries no many-body cluster term, so the deuteron binding is a separate 2-body
object (consistent with the pair-order √5·E_unit ladder,
`cumulant-mev-cluster-expansion.witness.json`).

---

## 3. The negatives (0-fit, ratio-only)

**(a) Wrong sign-change order.** Derived residual cumulants: `(μ₃, μ₄) = (+, −)`
(the #4316 sign window). Forward ≥3-row cumulants: `(ν₃, ν₄) = (−, +)` — the
**opposite** order. The signed-Springer-dimension *parity* does not reproduce the
derived 3-body/4-body sign change (`forward_sign_window_opposite`, Lean).

**(b) Wrong magnitude ratio.** Forward `|ν₄/ν₃| = 2` (exact, `ν₄ = −2·ν₃`); derived
`|μ₄/μ₃| ≈ 9.75`. Miss ≈ 4.9× (`forward_ratio_two`, Lean).

**(c) Direct AME ratio.** Neither reading hits the AME binding ratio 0-fit:

| ratio | AME2020 | Reading Y | Reading X |
|---|---:|---:|---:|
| `B(⁴He)/B(³H)` | **3.336** | 6.0 (+80%) | 2.0 (−40%) |

The two parameter-free readings **bracket** the AME ratio; no q₀-free convention
lands on it, and interpolating between them is the forbidden fit.

---

## 4. Why this is distinct from the corpus (anti-duplication)

The existing simplex/cluster probes are all **q₀-dependent** or invert the residual:

- `deltalambda-kappa-interface-residual-simplex` / `AdditiveResidualSimplex.lean` —
  same `C(A,k)` basis but fed `M(A) = ρ_strong − ρ_grad` (`ρ_grad = [A]_q!/[2]_q!`,
  q₀-dependent); μ_k are q₀-evaluated MeV.
- `ka_additive_cluster_derivation_probe.py` — per-knot Markov traces at q₀.
- `deltalambda-extensivity-gap-synthesis` — `B_base = m_e·|Σ y_λ χ^λ sgn·dim|`,
  q₀-weighted.

**This probe is the forward, q₀-free twin:** it feeds the *proved* `Δ_λ` ≥3-row
content — the thing actually derived from the drivers — into that basis and asks
whether the derived cluster cumulants are combinatorial. Answer: only `μ₂=0` is.

---

## 5. Surviving sub-question (sharp, honest)

The derived cluster cumulants carry (i) a `(+,−)` sign change at `(A=3,4)` and
(ii) `|μ₄/μ₃| ≈ 9.75`. The proved `Δ_λ` chirality parity supplies **neither** — it
gives `(−,+)` and `2`. The derived `μ_k` come from the q₀-dependent `y_λ·χ^λ` trace
weighting, and the sign the parity *does* supply is the wrong one. So:

> **Is the many-body binding sign-change window an irreducibly archimedean
> (q₀-dependent) feature — i.e. is a fully q₀-free closure of the `(+,−)` window
> provably impossible?** If yes, no combinatorial/categorical object can supply the
> sign, and the magnitude derivation must run through the q₀-dependent trace (the
> `μ₄` α-cluster residual via ρ_F cluster integrals, `AdditiveResidualSimplex` §S).

This is stated as the surviving question, **not** claimed as a proved scope-(b)
obstruction. Proving it would need: the sign of `Σ_{λ⊢k,ℓ≥3} y_λ(q)·χ^λ·Δ_λ` is
q-dependent and crosses zero between the combinatorial (`q→1`) limit and `q₀` — a
targeted next unit.

---

## 6. What is NOT claimed

- Not a magnitude closure. The deuteron/light-nucleus magnitude stays open.
- Not a refutation of the extensive-cumulant *program* — only that the **q₀-free
  ≥3-row signed-dimension content alone** does not supply sign+magnitude (scope-(a),
  per §before-declaring-refuted: this construction, alone, does not reproduce the
  ratios as-is).
- `μ₂ = 0` is the sole 0-fit structural win, and it re-derives an already-known
  fact by an independent (combinatorial, q₀-free) route.

## 7. Verification status (honest)

- **Python probe:** run, all 8 exact-integer assertions pass; witness emitted
  (`free_parameters=0`, no float64, AME as targets only).
- **Lean: MACHINE-VERIFIED, `lean`-direct exit 0, sorry-free (2026-08-09).**
  Supersedes this section's earlier "hand-audited / hard disk block" caveat, which
  was a **misdiagnosis** — the olean cone was reachable all along. Restoring
  `lake-cache/qou-v4-24-0` and running `lean`-direct (never `lake build`, which
  re-resolves deps and wipes the restored oleans) against the real
  `import Mathlib.Tactic` cone gives:

  ```text
  $ scripts/lean-verify.sh content/quantum-observable-universe/lean/QOU/MassTheory/ThreeRowExtensiveCumulant.lean
  ── lean-verify: …/ThreeRowExtensiveCumulant.lean ──
    ✓ exit 0 — checks
  ```

  No errors, no warnings, no `sorry`. `#print axioms` on all 11 declarations:

  ```text
  clusterF_eq_zero_of_card_le_two    [propext, Classical.choice, Quot.sound]
  Bext_two / Bext_three / Bext_four  [propext, Classical.choice, Quot.sound]
  Bext_ratio_four_three              [propext, Classical.choice, Quot.sound]
  Bext_deuteron_zero                 [propext, Classical.choice, Quot.sound]
  nu_values                          does not depend on any axioms
  forward_edge_coeff_zero            does not depend on any axioms
  forward_sign_window_opposite       does not depend on any axioms
  forward_ratio_two                  does not depend on any axioms
  forward_cumulants_not_derived_pattern  does not depend on any axioms
  ```

  **No `sorryAx` anywhere.** The five `decide`-backed lemmas are axiom-free
  outright (closed integer computation in the kernel, not `native_decide`).

- **Vacuity / self-assumption check (AGENTS.md §1a, §3b-tax, §Strict Lean
  Discipline).** No `: True`, no `X = X := rfl`, no empty `Prop` carrier, no
  `native_decide`, no `def`-disguised tautology. `clusterF_eq_zero_of_card_le_two`
  genuinely consumes its hypothesis `hS : S.card ≤ 2`. Two disclosures:

  1. **`sRow3` is a hand-entered lookup table, not a Lean-derived partition sum.**
     `def sRow3 : ℕ → ℤ | 3 => -1 | 4 => -2 | 5 => 4 | _ => 0` asserts the values
     `s_k = Σ_{λ⊢k, ℓ(λ)≥3} (−1)^{n(λ)} f^λ` by *definition*; the identity between
     the table and that partition sum is **checked in Python, not proved in Lean**.
     So every downstream conclusion here is Lean-proved *for this table*, and
     "sorry-free ≠ derived" applies at exactly that seam. Independently
     re-confirmed this session by a from-scratch hook-length recomputation:
     `s_{1..6} = 0, 0, −1, −2, 4, 16` and `Bext_{2,3,4,5} = 0, −1, −6, −16` —
     the table and the three `Bext` value lemmas are numerically correct. The
     scope-(a) verdict is unaffected (a *negative* does not become stronger by
     formalising the table), but a citing block must not read
     `forward_sign_window_opposite` as "Lean-proved that the ≥3-row Δ_λ stratum
     has (−,+) order" — what is Lean-proved is that `sRow3` does.
  2. **`Bext_deuteron_zero : Bext 2 = 0 := Bext_two`** is a verbatim alias of
     `Bext_two`. Not vacuous, but redundant; kept for the docstring's deuteron
     framing.

## References
- Proved value: `QOU.BraidsAndKnots.DeltaLambdaGeneralNUnconditional`
  (`dtEuler_eq_deltaLambda_unconditional`), audit
  `2026-08-02-deltalambda-value-proved-downstream-and-additive-term.md`.
- ≥3-row dominance: `2026-08-07-binding-is-three-row-dominated-hypothesis-refuted.md`.
- Companion q₀ simplex: `QOU.MassTheory.AdditiveResidualSimplex`,
  `deltalambda-kappa-interface-residual-simplex.witness.json`.
- Intensive-vs-extensive: `2026-06-02-binding-intensive-vs-extensive-derivation.md`.
- Pairwise cap: `2026-07-18-deltalambda-saturation-det-ceiling.md`.

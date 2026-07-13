# The exact D-ladder: no coupled ℚ(√3) recurrence + a crisp 2-adic parity grading

**Date:** 2026-07-13 · **Branch:** `claude/faddeev-phi-b-construction-wp7xau` ·
**PR:** #3737 · **Tier:** exact-arithmetic (rational linear algebra + p-adic
valuation; no floats, no PSLQ, no fit) · **Scope:** (a) — no `c_k` wired, no
tier change, registry untouched.

Advances the **exact D(ũ) ladder** (`S = h·D(ũ)`, the bar-odd c₃ S-leak;
`h = q − q⁻¹` the anchor-blind bar-odd carrier, `D` the bar-even ℚ(√3) ladder).
Builds directly on the merged structure hunt
([`2026-07-12-bar-odd-s-deformed-rung-followup.md`](2026-07-12-bar-odd-s-deformed-rung-followup.md) §Route 2, PR #3716)
and its divergence correction
([`2026-07-12-dladder-divergence-correction.md`](2026-07-12-dladder-divergence-correction.md)):
`D(ũ) = Σ_k d_k ũ^k` has exact coefficients `d_k = a_k + b_k√3` (`a_k, b_k ∈ ℚ`),
is super-exponentially divergent (q-Gevrey, radius → 0), and has no **classical**
P-finite recurrence for `a_k` or `b_k` **taken separately over ℚ**.

This audit reports two exact results the merged hunt did not.

## Result 1 — no *coupled* ℚ(√3) P-recurrence (the class #3716 skipped)

The merged probe tested P-finiteness of `a_k` and `b_k` **separately over ℚ**.
But `d_k` is a single ℚ(√3) object, and a recurrence *over ℚ(√3)*

$$\sum_{i=0}^{r} P_i(k)\,d_{k-i} = 0,\qquad P_i \in \mathbb{Q}(\sqrt3)[k],$$

does **not** reduce to separate ℚ-recurrences of the same order: applying the
√3-Galois conjugation couples the two rational components into a 2-vector
`v_k = (a_k, b_k)ᵀ` obeying a **matrix** recurrence

$$\sum_{i=0}^{r} M_i(k)\,v_{k-i} = 0,\qquad M_i(k) \in \mathrm{Mat}_2(\mathbb{Q}[k]),\ \deg_k \le D,$$

whose off-diagonal (√3-mixing) entries a separated scalar test structurally
cannot see. A coupled recurrence can therefore exist where both separated ones
fail — this is the exact ℚ(√3) P-finiteness question for `D(ũ)`.

**Probe** ([`qbeta_dladder_coupled_qsqrt3_recurrence_probe.py`](../../computations/qbeta/qbeta_dladder_coupled_qsqrt3_recurrence_probe.py)):
the exact rational null space of the integer constraint matrix over all valid
`k`. The recurrence has only `2·(r+1)·(D+1)` unknowns — the coefficients of the
two polynomials `A_i, B_i` in `P_i = A_i + B_i√3` — since the √3-algebra ties the
matrix diagonal to `A_i` and the off-diagonal to `B_i` (a correctness + efficiency
fix from the `@gemini-code-assist` review on PR #3737; an unconstrained
`Mat₂(ℚ[k])` would double the unknowns and force premature data-starvation
skips). With the correct count, the `d_1…d_21` already in hand cover a robust
window: **no coupled ℚ(√3) P-recurrence** for order `r ≤ 2` through degree
`D ≤ 4`, `r = 3` through `D ≤ 3`, and `r = 4` through `D ≤ 2` (all exact,
over-determined). This **extends** #3716's "not P-finite (separated)" to the
coupled ℚ(√3) case,
tightening the corpus's q-Gevrey / resurgent reading of the bar-odd S-leak: the
D-ladder is not (q-)holonomic of low order even as a coupled ℚ(√3) object.

*(This is the right refinement to run, not a re-open of a settled frontier: a
negative here further **constrains** the resurgent class; a positive would have
been an exact closed-form characterization. Either way it is decisive and
exact.)*

## Result 1b — not q-holonomic either, in the base its own denominators indicate

A polynomial-in-`k` recurrence (Results 1 + #3716) is the wrong class for a
q-Gevrey series; the natural object is a **q-difference (q-holonomic)**
recurrence, coefficients polynomial in `X^k`. The base is not free — it is fixed
by the arithmetic: the exact `d_k` have **3-power-dominated denominators**
(`v₃(den d_k) ~ 1.5·k`, the Ohtsuki–Habiro 3-smoothness), so the
structurally-indicated base is `X = 3`: a recurrence
`Σ_i P_i(3^k)·d_{k-i} = 0` has coefficients `3^{k·d}` that **exactly clear** those
denominators (at degree `E ≥ 2`, since `3^{2k}` dominates `3^{1.5k}`) — a
mechanism a polynomial-in-`k` coefficient cannot supply.

**Probe** ([`qbeta_dladder_q_holonomic_base3_probe.py`](../../computations/qbeta/qbeta_dladder_q_holonomic_base3_probe.py)):
the same genuine-ℚ(√3)-coupled kernel with monomials `X^{k d}` in place of
`k^d`, base `X ∈ {3, 1/3}` (the reciprocal `q ↔ q⁻¹` direction) plus the
classical `k` control. Because the exact entries `3^{k d}` are astronomically
large, the negative is certified by **full column rank modulo large primes**
(full rank mod `p` ⟹ full rank over ℚ ⟹ trivial nullspace) — rigorous and cheap;
an exact re-verification is triggered only on a rank deficiency. **No
q-holonomic recurrence** in base `3` or `1/3` (nor classical `k`) through
`r ≤ 3`, `E ≤ 3` (12 prime-certified full-rank cells per base).

So `D(ũ)` is **not (q-)holonomic even in the base its own denominators pointed
at** — the strongest form of the negative yet, and a genuine tightening of the
resurgent reading: the 3-adic structure is real (Result 2) but it is *not* the
signature of a q-difference equation. `D(ũ)`'s closed form, if any, is
transcendental / resurgent (Écalle acceleration chain, per the corpus's
q-Gevrey verdict), not (q-)holonomic.

## Resummation note — the singularity is Jackson q-Borel territory, not plain Borel (deferred)

A natural parallel-track idea (coordinated with the κ-tower resurgence program,
PR #3683) is to locate the D-ladder's Borel singularity with #3683's C1
conformal-Padé. **Recorded here so it is not repeated: the plain `∑ d_k ζ^k/k!`
Borel transform is the wrong tool for this series, and a "convergent ũ-plane
branch point at ρ≈0.143" reading is the finite-n shadow trap.** Both were checked
against the corpus and rejected:

- **Divergent, re-confirmed (not convergent).** The merged divergence correction
  ([`2026-07-12-dladder-divergence-correction.md`](2026-07-12-dladder-divergence-correction.md))
  establishes `D(ũ)` is super-exponentially divergent (radius → 0); the ratio
  `d_{k-1}/d_k ≈ 0.143` that *looks* like a finite radius is the `(k!)^{C}`
  (C ≈ 0.06) shadow it warns about. Re-verified here: the root test
  `|d_k|^{1/k}` **rises without plateau** (4.72 → 5.91 over k=6…21), the
  radius-→0 signature.
- **Plain Borel is the wrong transform.** For a **q-Gevrey** divergent series the
  resummation is **Jackson q-Borel** / an Écalle acceleration chain (per the
  corpus's alien-calculus audit), not the classical `÷k!` Borel — which
  over-suppresses a mild `C ≈ 0.06` super-exponential into a near-entire
  transform with no meaningful singularity (a conformal-Padé run on it returns
  only a spurious negative-axis pole, inconsistent with the constant-sign `d_k`
  Pringsheim constraint). The correct q-Borel/acceleration analysis is the
  resurgent-program territory of #3683 and is **deferred** there, not attempted
  with the wrong transform here.

This note is the honest scope boundary: the exact-arithmetic negatives (Results
1, 1b) and the grading (Result 2) stand on their own; the analytic resummation of
the divergent ladder is a separate, q-Borel undertaking.

**Update — the Borel–Leroy order scan (parallel/overlap with #3683, owner-authorized).**
The correct transform for a mild q-Gevrey series is **Borel–Leroy of fractional
order `s`** (`b_k = d_k/(k!)^s`), not the classical `÷k!`. Probe
[`qbeta_dladder_qborel_leroy_resummation_probe.py`](../../computations/qbeta/qbeta_dladder_qborel_leroy_resummation_probe.py)
scans `s` and measures the root-test slope of `|b_k|^{1/k}`. Findings (scope-(a)):

- **Third independent confirmation of divergence.** The slope is `+0.065` at
  `s=0` and **decreases monotonically** in `s` — a positive Borel–Leroy order is
  required to flatten the root test (after the ratio and log-fit methods, this is
  the third). Plain `÷k!` (order 1) over-suppresses.
- **The Gevrey order is not fixed (q-Gevrey confirmed).** The root-test slope
  crosses 0 near `s*≈0.20`, which **disagrees** with the audit's log-fit
  `C≈0.06`. The two estimators giving different orders **is** the q-Gevrey
  "no single Gevrey index" signature — consistent with the divergence-correction's
  drifting-`C` observation, not a contradiction.
- **The resummed singularity is not resolvable at k=21.** At `s*` the dlog-Padé
  radius (`≈0.156`) is inconsistent with the root-test radius (`≈0.32`) — the
  finite-n shadow again. **No instanton action is claimed.** A clean value needs
  the genuine q-Borel / Écalle acceleration (#3683's machinery) or more `d_k`.

So the q-Borel pass **sharpens the class** (mildly, non-fixed-order divergent —
now by three methods) but confirms the singularity itself is beyond reach at
accessible order — the honest boundary between what the exact `d_k` to k=21 can
settle and what the resurgent program must.

## Result 2 — the exact 2-adic parity grading (headline)

Writing `d_k = a_k + b_k√3` and reading the **2-adic valuation of the
denominators**, an exact ℤ/2 grading emerges — crisper than the merged hunt's
"the small-denominator part alternates by parity":

> **`v₂(den b_k) = 0` if and only if `k` is odd**, and the rational part is the
> mirror: **`v₂(den a_k) ≤ 1` if and only if `k` is even**.

Equivalently: **the 2-adically singular ℚ(√3)-component of `d_k` alternates with
`k`-parity** — it is the rational part `a_k` for odd `k`, the √3-part `b_k` for
even `k`. Holds **exactly** for every computed `k` (the committed run covers
`k = 1…21`; the higher-ORD extension on this PR pushes it further):

| k | parity | v₂(den a_k) | v₂(den b_k) | 2-singular part |
|---|--------|-------------|-------------|-----------------|
| 1 | odd  | 3  | 0  | a (rational) |
| 2 | even | 1  | 5  | b (√3) |
| 3 | odd  | 8  | 0  | a (rational) |
| 4 | even | 1  | 10 | b (√3) |
| 5 | odd  | 14 | 0  | a (rational) |
| 6 | even | 1  | 16 | b (√3) |
| ⋮ | ⋮ | ⋮ | ⋮ | ⋮ |
| 21 | odd | 61 | 0 | a (rational) |

The 3-adic and ≥5 (factorial-smooth, Ohtsuki–Habiro) parts grow in **both**
components (~linear in `k`) — those are the known 3-smooth normalization. What is
new and clean is the **2-adic** channel: it is *pure* — a component either
carries the full 2-power or is 2-integral — and it is graded exactly by `k`
parity.

**Interpretation.** This is the arithmetic shadow of the **sinh/cosh
(bar-odd / bar-even) split** that defines the whole bar-parity program
(`QOU.QBeta.bar_parity_decomposition`; the sinh/cosh = decay/mass faces). `sinh`
carries the odd Taylor tower, `cosh` the even; the 2-adic denominators of the
substrate expansion inherit that parity as a clean ℤ/2 valuation grading. It is
exactly the kind of **structural invariant** the formalize-first discipline asks
to be isolated before any wider numerical search — here it also *is* the exact
content that a Domb–Sykes radius (refuted) or a fitted singularity never was.

### Structural origin of the √3 and the 2-powers (verified from the construction)

The two arithmetic channels are traceable directly to the D-ladder build
(`build_d_ladder` in the merged structure probe), independent of any fit:

- **The √3 is the Hoefsmit `b`.** The ladder is assembled from
  `b_ser = ser_sqrt(q⁴ + q² + 1) / (q² + 1)` — the Hoefsmit branch-parameter.
  Its `ser_sqrt` of `q⁴ + q² + 1` is the *sole* radical in the construction, so
  every `√3` appearing in a `d_k` descends from it (`q⁴+q²+1` takes the value
  `3` at the branch point, giving the field generator `√3`). The bar-odd
  projection `O = (log R − (log R)∘φ)/2` with `φ: ũ ↦ −ũ` then sorts the radical
  by ũ-parity.
- **The 2-powers come from three explicit sources:** the factor `(q² + 1)`
  (value `2`) in `b_ser`; the `½` in the archimedean edge
  `α = ½(z−1)h − ½ũ`; and the `2q³` denominator of
  `Q_A = (2q + 1 − q²)(q+1)/(2q³)`. These are the only carriers of `2` in the
  numerator/denominator data, so the 2-adic valuation of each `d_k` is fixed by
  how these distribute across the even/odd ũ-tower — which is exactly the
  parity-graded pattern observed.

This **explains** the grading (why a ℤ/2 2-adic split exists at all, and why it
keys to ũ-parity via the bar-odd projection `φ`) without yet **proving** the
sharp `v₂(den b_k)=0 ⟺ k odd` law — that proof needs the `ser_sqrt`/`ser_div`
construction formalized (see below). Identifying the origin is the honest
intermediate step: the invariant is now structurally motivated, not merely
observed.

## Formalize-first note (the invariant, and what proving it needs)

The grading is a precise, exact, non-fitting statement. Formalizing it as a Lean
theorem requires the D-ladder *construction* (`O/h` via `ser_div`, the substrate
`ũ = b·ℏ_q²` expansion) to exist in Lean, which it does not yet — the current
Lean D-ladder object is `QOU.QBeta.BarOddLadderShape`, the phenomenology carrier
`S = A/u³`, not the coefficient construction. So this audit **states the
invariant precisely** (an exact, machine-checked arithmetic fact at every
computed order) as the formalization target, rather than laundering it through a
premature axiom. The natural Lean home is a `p`-adic valuation statement over the
coefficient sequence once the construction is formalized.

## Discipline

Scope-(a) throughout: exact rational linear algebra + `v₂` valuations, no floats,
no PSLQ, no fit, no `c_k` wired, no tier change. Adjacent **live sibling PR
#3683** runs Borel / alien-calculus resurgence on the **κ-tower** — a distinct
object; this audit is holonomicity + arithmetic grading of the **D-ladder**, the
complementary structural question. Nothing here closes `S` or changes any
precision leg.

## Cross-references
- Merged structure hunt: [`2026-07-12-bar-odd-s-deformed-rung-followup.md`](2026-07-12-bar-odd-s-deformed-rung-followup.md) §Route 2 (#3716).
- Divergence correction: [`2026-07-12-dladder-divergence-correction.md`](2026-07-12-dladder-divergence-correction.md).
- Bar-parity split: `QOU.QBeta.bar_parity_decomposition`; `qbeta_even_channel_bar_split_probe.py` (`S = h·D(u)`).
- Phenomenology carrier: `QOU.QBeta.BarOddLadderShape`.
- Adjacent resurgence sibling: PR #3683 (κ-tower Borel / alien calculus).

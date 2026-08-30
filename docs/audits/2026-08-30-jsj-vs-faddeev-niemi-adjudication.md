# Adjudicating #5817 vs #5812 — a category error of mine, and the real constraint underneath

**Date:** 2026-08-30 · **Branch:** `claude/jsj-signedness-adjudication-2026-08-30`
**Beans:** `qou-ygdo` (this doc), `qou-8igr` (the hinge), `qou-1w5h` (form-dependence)
**Scope:** (a) throughout. Nothing wired; no constant tuned; no fit proposed.

## 0 · BLUF

I flagged a tension between [#5817](https://github.com/litlfred/qou/pull/5817)
and [#5812](https://github.com/litlfred/qou/pull/5812) on 2026-08-26 and did not
adjudicate it. Adjudicated now, it splits three ways:

1. **The tension as I stated it was a category error. Retracted.** The two
   claims are about different objects.
2. **A real constraint does connect them, one step removed, and it is now
   Lean-proved** (5 declarations, sorry-free, axiom-clean).
3. **Its antecedent is form-dependent, and that is new.** The mixed-sign premise
   the #5812 exclusion rests on holds for two of the four committed binding
   forms and fails for the other two — and where it holds under `B_sym` it rests
   on **²H alone**.

Neither PR is wrong. The exclusion is **narrower than it reads** and should be
scoped to the form it is stated against.

## 1 · The retraction

I wrote, on both PRs: *"`conj:jsj-decomposition-linearity` is `Vol(𝒦(Z,N)) =
Z·Vol_p + N·Vol_n` — which is positive and additive in `Z, N`. If #5812's
generalisation holds as stated, a purely positive `Z·Vol_p + N·Vol_n` cannot be
the whole term."*

That is wrong in its premise. Reading the conjecture as landed:

> *the complement decomposes … into `Z` proton-block pieces and `N`
> neutron-block pieces with isotope-independent volume quanta `Vol_p` and
> `Vol_n`, and consequently `Vol(𝒦(Z,N)) = Z·Vol_p + N·Vol_n`*

This is a statement about **`Vol(𝒦)`, the carrier's hyperbolic volume** — not
about a correction added to `B`. #5812's exclusion is about **a correction to
`B`**. Different objects; neither refutes the other.

Worse for my framing: as *literally stated*, strict linearity in `(Z,N)` with
isotope-independent quanta is exactly the **unbound baseline** — mass equal to
the sum of the parts, i.e. **binding zero**. Binding is the *deviation* from
linearity, which would have to live in JSJ pieces the conjecture's own
decomposition hypothesis excludes ("exactly `Z` proton and `N` neutron pieces").
So the conjecture as written is not a candidate binding term at all; it is a
candidate *baseline*. #5817 says as much in its own §3 — the linearity is
currently "true and empty" because `Vol_p = Vol_n = 0`.

## 2 · The real constraint, and it is proved

The exclusion does reach a JSJ-sourced term, at one remove:

- Hyperbolic volume is **non-negative**, and JSJ additivity is a **sum** over
  pieces. So any JSJ-sourced term is a sum of non-negative summands.
- A non-negative family cannot agree pointwise with one that is strictly
  negative somewhere — the abstract content shared by the Faddeev–Niemi verdict
  and the Option-E PROBE-4 KL-positivity prune.
- Binding is read off volume through a **monotone** map (`m ∝ Vol·ρ`, and
  `B` = free − bound, so more bound-state volume means *less* binding). Under
  **either** monotonicity direction the contribution stays single-signed; only
  the sign flips.

[`JSJSingleSignedness.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/JSJSingleSignedness.lean)
— 5 declarations, `lean`-direct **exit 0**, warning-free, `#print axioms` clean
(`propext`, `Classical.choice`, `Quot.sound`; **no `sorryAx`**):

| declaration | content |
|---|---|
| `nonneg_ne_of_neg` | a non-negative family differs from one strictly negative somewhere |
| `jsj_sum_nonneg` | a finite sum of non-negative piece volumes is non-negative |
| `jsj_cannot_match_negative` | **the hinge** — a per-isotope JSJ volume sum cannot match a residual negative anywhere |
| `antitone_volume_gives_nonpos_binding` | added volume ⇒ non-positive binding contribution |
| `monotone_volume_gives_nonneg_binding` | the opposite convention ⇒ non-negative; single-signed either way |

The last two are the point: **the exclusion does not depend on which sign
convention the framework uses**, only on the `Vol → B` map being monotone at
all. Base ring is generic (`AddCommGroup` + `PartialOrder` +
`IsOrderedAddMonoid`), never `ℝ`, per §7c — ordering is genuinely required
because the content *is* about signs, but no archimedean construct appears.

**These theorems assert the implication, not the antecedent.** They say: *if*
the residual is mixed-sign, *then* a JSJ-volume-sourced term cannot supply it.

## 3 · The antecedent is form-dependent — the new result

Probe:
[`bsym_residual_sign_form_dependence_probe.py`](../../computations/probes/bsym_residual_sign_form_dependence_probe.py)
→ `bsym-residual-sign-form-dependence.witness.json`. `R := B_AME − B_form`,
mpmath at 60 dps, no float64 in the arithmetic.

**Cross-check first.** The probe re-forms `L_XY = −ln(z + d_XY) − (Δe/2)ln(1−h)`
in `mpf` (the production `_bond_type_L` casts to float at the return) and
reproduces the cluster-substructure verdict's per-bond energies exactly —
`αL_pp = 2.541586`, `αL_pn = 2.832825`, `αL_nn = 3.306906` — and #5812's
`R(²H) = −0.6083` against their quoted `−0.6074`.

| iso | A | `B_AME` | `R_sym` | `R_lin` | `R_law` | `R_magic` |
|---|--:|--:|--:|--:|--:|--:|
| ²H | 2 | 2.2246 | **−0.6083** | +1.7892 | +0.1419 | −12.7533 |
| ³H | 3 | 8.4818 | +2.3421 | +7.7867 | −0.9573 | −13.9850 |
| ³He | 3 | 7.7180 | +2.3436 | +7.0195 | −1.7675 | −14.7487 |
| ⁴He | 4 | 28.2957 | +19.6143 | +27.4196 | −5.4756 | −1.6600 |
| ⁶Li | 6 | 31.9940 | +17.4642 | +30.8953 | −309.3527 | −12.9395 |
| ⁷Li | 7 | 39.2451 | +21.4084 | +38.1391 | −936.2293 | −13.1774 |
| ⁷Be | 7 | 37.6008 | +20.5294 | +36.3263 | −1086.4808 | −14.8216 |

| form | mixed-sign? | negative | positive |
|---|---|--:|--:|
| `B_sym` | **yes** | 1 (**²H alone**) | 6 |
| `B_lin` | **no** | 0 | 7 |
| `B_law` | **yes** | 6 | 1 |
| `B_magic` | **no** | 7 | 0 |

**Two things follow.**

- The mixed-sign premise is **not a property of the physics alone**; it is a
  joint property of the physics and the choice of baseline form. Under `B_lin`
  the target is uniformly positive, so a non-negative correction is **not**
  excluded there; under `B_magic` it is uniformly negative.
- Where the premise does hold under `B_sym`, it hangs on **one isotope**. Six of
  seven residuals are positive; ²H alone carries the sign change.

**This does not void #5812's result, and the choice of `B_sym` is defensible** —
`B_sym` is the exact log-ratio binding while `B_lin` is its *linearisation*,
known to undershoot by `Δ_λ ≈ q₀^(10A−5)`, so `B_lin`'s uniform positivity is
largely its own truncation deficit rather than an independent signal. The
correct conclusion is a **scoping** one, not a refutation: the exclusion is
scope-(b) **conditional on `B_sym` (or `B_law`) being the baseline**, and its
²H-only dependence should be stated wherever it is cited.

The reason to care is on the record in that same PR: `B_sym`'s ²H value is the
one the dashboard docstring flags as over-binding by **1.75×** since the Reeb
override was removed, and #5812's own F1 records that an *earlier* ²H
impossibility claim was a **convention-C artifact that did not survive R1**. A
sign that has already been a convention artifact once, and that now carries an
entire scope-(b) exclusion by itself, is worth naming explicitly.

## 4 · Downstream

**⁴He.** The adjudication sharpens it. Three independent knobs are excluded at
⁴He specifically: **calibration** (survives a full 3-parameter recalibration at
−59.2 %, PR #5816), **clustering** (`r = 1.647031` identical across all four
pre-registered schemes by exact 18-digit string equality — ⁴He *is* the α, so
its edge set is `K₄` under every scheme), and **JSJ volume** (§2, given the
monotone hinge). ⁴He is also the pivot of the sign change under `B_sym`. So the
missing term must be large-positive at `A=4` while negative at `A=2` —
**non-monotone in `A`**, which kills every smooth single-charge functional at
once.

**`m_K/m_π` / CAL-3.** *No direct impact*: `m_π` does not appear in
`B = Q_β·(tr_M(W_free) − tr_M(W_atom))`, so nothing on the binding side
constrains CAL-3 identifiability (PR #5816). But there is an adverse **indirect**
implication for the proposal to make CAL-3 identifiable by widening the fit
objective with `m_K/m_π`: AGENTS.md's own red-team records that `m_K/m_π`'s
sub-100× result is manufactured by an EM correction whose **truncation order was
chosen against the data** and whose `α_em` is **conditional on an open Lean
`sorry`** — hence "1/5 scoreable ⇒ 0/5 unconditional". Anchoring CAL-3 on that
quantity would anchor it on something itself truncation-fitted and
sorry-conditional. **That option should stay closed on its own merits**, not
only because the fitted-ideal layer is paused.

## 5 · What is NOT claimed

That `conj:jsj-decomposition-linearity` is false (it remains **untested rather
than refuted**, stated for an object the compute does not build). That `B_sym`
is the wrong baseline. That #5812's exclusion is void — it is re-scoped, not
withdrawn. That the `Vol → B` map *is* monotone: that is the hinge's
**hypothesis**, carried explicitly in the Lean statements and not established
here. That any non-negative correction now works under `B_lin` — only that it is
not excluded *by this argument* there.

## 6 · Verification

- **Lean:** `lean`-direct **exit 0**, warning-free, against the restored
  `.lake/packages/*/.lake/build/lib/lean` oleans (v4.24.0); `#print axioms`
  clean on all five declarations. Library file, no `.qa.json` sidecar, so this
  is the only check on it.
- **Probe:** mpmath 60 dps end to end, no float64 in the arithmetic; the
  per-bond cross-check against the committed cluster verdict is asserted, not
  merely printed.
- **Exit codes were captured directly, not through a pipe.** Twice this session
  a `| tail` masked a non-zero status and I reported green in error; every exit
  code quoted here is the command's own.

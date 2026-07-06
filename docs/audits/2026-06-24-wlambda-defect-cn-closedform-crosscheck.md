# The `W_λ` defect cubic is EXACT, not empirical — closed form `C(n) = −n(n−1)(2n−13)/144` cross-checked against the actual `1−Z(n)`

**Date:** 2026-06-24
**Branch:** `claude/keystone-defect-cn-closedform-crosscheck-2026-06-24`
**Probe:** [`computations/keystone_wlambda_defect_cn_closedform_crosscheck.py`](../../computations/keystone_wlambda_defect_cn_closedform_crosscheck.py)
**Witness:** [`computations/keystone-wlambda-defect-cn-closedform-crosscheck.witness.json`](../../computations/keystone-wlambda-defect-cn-closedform-crosscheck.witness.json)

## The loop that was open

Three corpus artifacts described the `W_λ` partition-function defect `1 − Z(n)`
(`Z(n) = Σ_{λ⊢n} d_q(λ)²/[n]_q!`, balanced `[m]_q`, the q-Plancherel total mass) but
**never closed the loop between them**:

| Artifact | What it does | Gap |
|---|---|---|
| [`docs/audits/scripts/keystone_wlambda_Z_defect_n_scaling.py`](scripts/keystone_wlambda_Z_defect_n_scaling.py) | Computes `1−Z(n)` and extracts its small-h coefficient `C(n)` **EMPIRICALLY** | Explicitly: *"C(n) is reported EMPIRICALLY — no closed form is claimed"* (line 24). A **hook-moment ansatz** `C(n)=(1/n!)Σ dim·hook²` was **tested and REFUTED** (lines 177–178). |
| [`WLambdaDefectClosedForm.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/WLambdaDefectClosedForm.lean) | Proves `144·C(n) = −n(n−1)(2n−13)` ALGEBRAICALLY (from Identity I), sign-flip `n144C_pos` (2≤n≤6) / `n144C_neg` (7≤n) | Never cross-checked against the *actual* `Σ_λ d_q²/[n]_q!` defect — only derived symbolically from Identity I. |

So: one script said "no closed form" (having refuted a *different*, hook-moment guess), and a
Lean file proved a closed form from Identity I — but **nobody verified the Lean cubic against the
directly-computed defect.** A reader could not tell whether `−n(n−1)(2n−13)/144` was the real
small-h coefficient of `1−Z(n)` or an algebraic artifact of the Identity-I bookkeeping.

## What the cross-check does

For `n = 2..10` (spanning the n=7 sign flip), compute `Z(n,q) = Σ_{λ⊢n} d_q(λ)²/[n]_q!` directly
at 60 dps via q-hooks, set `h = q − 1/q`, and Richardson-extrapolate
`C_emp(n) = lim_{h→0}(1−Z(n))/h²` (two halvings, killing the `O(h²)` and `O(h⁴)` tails). Compare
to `C_cf(n) = −n(n−1)(2n−13)/144`.

## Result — EXACT to <2e-14, sign flip identical

| n | `C_empirical` | `C_closed_form` | rel err | sign |
|---:|---:|---:|---:|:--:|
| 2 | 0.125 | 0.125 | 2.4e-15 | + |
| 3 | 0.2916666… | 0.2916666… | 7.3e-15 | + |
| 4 | 0.4166666… | 0.4166666… | 1.6e-14 | + |
| 5 | 0.4166666… | 0.4166666… | 2.5e-14 | + |
| 6 | 0.2083333… | 0.2083333… | 3.7e-14 | + |
| **7** | **−0.2916666…** | **−0.2916666…** | 1.9e-15 | **−** |
| 8 | −1.1666666… | −1.1666666… | 2.5e-15 | − |
| 9 | −2.5 | −2.5 | 1.2e-14 | − |
| 10 | −4.375 | −4.375 | 8.3e-15 | − |

**Empirical sign flip at n=7 = closed-form sign flip at n=7.** All nine match below 1e-10
(actually below 4e-14). The closed form `C(n) = −n(n−1)(2n−13)/144` **IS** the exact small-h leading
coefficient of the real `W_λ` defect — not an empirical fit, and not the refuted hook-moment ansatz.

## Why the empirical script's "no closed form" was not wrong

The empirical script refuted **`C(n)=(1/n!)Σ dim·hook²`** — a hook-*moment* guess. That guess does
fail. The Identity-I cubic is a structurally different object (it comes from
`M(n)=n(3n−1)/2 = binom(n,2)+n²`, the per-partition content/hook decomposition Identity (A)
proved sorry-free in #2655, propagated to the Plancherel mean). The two are not in tension: one
ansatz is wrong, the *derived* cubic is right. This cross-check is the first artifact to state
that distinction with the numbers attached.

## Why this matters for the keystone

The full-Hecke geometric `W_λ` index program
([`docs/scope/2026-06-24-keystone-fullhecke-geometric-index-program.md`](../scope/2026-06-24-keystone-fullhecke-geometric-index-program.md))
lists **target (1)** as: *the index's 2nd heat-kernel coefficient must equal `144·C(n)` including the
n=7 sign flip.* Before this probe, target (1) rested on a Lean derivation whose contact with the
*actual* `W_λ` weights was unverified. Now the target is **pinned exactly** against the direct
computation: a geometric index that reproduces `W_λ` must produce the cubic
`−n(n−1)(2n−13)` and flip sign at n=7, and this is a **q₀-free** statement (it is the small-`h`
*leading* coefficient — the whole `h→0` limit, independent of the substrate anchor). It is the
sharpest single falsifiable gate the geometric construction (phase **G2**) has to clear.

## Discipline

- **No fit.** Every number is computed (q-hooks + mpmath, 60 dps); `q₀` never appears; the defect
  is read off by Richardson extrapolation, not tuned.
- **(a)/(b) framing.** This is a **positive** confirmation (the cubic matches), so the
  refuted/ruled-out scoping does not apply. The one *negative* in the neighbourhood — the
  hook-moment ansatz — was already correctly scoped by the empirical script (a specific ansatz
  fails; "no [hook-moment] closed form"), and this probe does **not** disturb it.
- **Formalize-first complement.** The cubic was Lean-proved first (`WLambdaDefectClosedForm`); this
  probe is the empirical confirmation that the proved object is the physical one — the forward
  direction of the formalize-first discipline (prove the invariant, *then* confirm it governs the
  compute).

## Sub-leading coefficient `D(n)` — a SECOND exact, q₀-free target

**Probe:** [`computations/keystone_wlambda_defect_dn_subleading.py`](../../computations/keystone_wlambda_defect_dn_subleading.py)
· **Witness:** [`computations/keystone-wlambda-defect-dn-subleading.witness.json`](../../computations/keystone-wlambda-defect-dn-subleading.witness.json)

Having pinned the **leading** (h²) coefficient, the natural question is whether the **next**
coefficient in `1 − Z(n) = C(n)·h² + D(n)·h⁴ + O(h⁶)` is also clean. It is. Extracting
`D(n) = lim_{h→0}(1 − Z(n) − C(n)·h²)/h⁴` by 4× Richardson at 120 dps (using the now-exact
`C(n)` to subtract), the forward finite differences of `D(n)` are **constant at order 6**
(`Δ⁶` spread `1.3e-21`) — an *unfitted* structural proof that `D(n)` is a degree-6 polynomial in `n`.
Interpolating the unique degree-6 polynomial from `n=2..8` and **validating on held-out `n=9,10`
(PASS, exact)** gives:

$$
D(n) = \frac{-100\,n^6 + 1572\,n^5 - 6745\,n^4 + 5070\,n^3 - 625\,n^2 + 828\,n}{1036800}
     = \frac{n(n-1)\,\bigl(-100\,n^4 + 1472\,n^3 - 5273\,n^2 - 203\,n - 828\bigr)}{1036800}.
$$

Structural features (consistency, not fit):

- **Denominator `1036800 = 50·144²`** — parallels `C(n)`'s `144`.
- **`D(n)` carries the same `n(n−1)` factor as `C(n)`** (`= −n(n−1)(2n−13)/144`), so both defect
  coefficients **vanish at `n = 0, 1`** — consistent with zero defect for the trivial / single-box
  partition (`Z(1) = 1` exactly).

**Implication.** The defect `1 − Z(n)` is the heat-kernel expansion the geometric index must
reproduce; its coefficients are the index's heat-kernel coefficients. We now have **two** clean
polynomial targets, both q₀-free:

| Target | coefficient | closed form | heat-kernel order |
|---|---|---|---|
| (1) | `C(n)` (h²) | `−n(n−1)(2n−13)/144` (Lean-proved, n=7 sign flip) | 2nd |
| (1′) | `D(n)` (h⁴) | `n(n−1)(−100n⁴+1472n³−5273n²−203n−828)/1036800` (interpolated + held-out validated) | 4th |

That **both** leading coefficients are clean low-degree polynomials in `n` is itself a structural
fact about the defect — and it sharpens the keystone gate from one falsifiable number per `n`
(phase G2) to two. `D(n)`'s closed-form polynomial is now **partially Lean-formalized**
([`WLambdaDefectSubleadingD.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/WLambdaDefectSubleadingD.lean),
sorry-free): the factored↔expanded `ring` identity (confirming the witness's
`int_coeffs_low_to_high`), the shared `n(n−1)` vanishing at `n=0,1`, the `1036800 = 50·144²`
denominator and the `144^k` denominator ladder (`144`, `50·144²`, `7350·144³`), and the value table
cross-checking `1036800·D(n)` for `n=2..10` (held-out `n=9,10` included). What stays **deferred** —
exactly parallel to `C(n)`'s general-`n` Identity I — is the *derivation* of `D(n)` from the defect:
`D(n)` was extracted numerically (`mp.taylor`, method-validated to `0.0` against proved-exact `C(n)`)
and interpolated with held-out validation; the symbolic `h⁴`-order collapse into named Plancherel
moments (the `h⁴` analogue of Identity I) is not yet in hand. The Lean file is honest about this in
its docstring — it formalizes the closed form's algebra and witness cross-check, not a derivation.

## The coefficient ladder — `deg c_{2k}(n) = 3k` (every coefficient is polynomial)

**Probe:** [`computations/keystone_wlambda_defect_coeff_ladder.py`](../../computations/keystone_wlambda_defect_coeff_ladder.py)
· **Witness:** [`computations/keystone-wlambda-defect-coeff-ladder.witness.json`](../../computations/keystone-wlambda-defect-coeff-ladder.witness.json)

`deg C = 3`, `deg D = 6` is the start of a **ladder**. Writing the defect
`1 − Z(n) = Σ_{k≥1} c_{2k}(n)·h^{2k}`, the probe extracts `c_2 = C`, `c_4 = D`, `c_6 = E` (the
h², h⁴, h⁶ Taylor coefficients via `mp.taylor`, method-validated against the exact `C(n)` to 0.0)
and finds, with each closed form interpolated + **held-out validated**:

| k | coeff | degree in n | `3k` | denominator | held-out |
|--:|:--|:--:|:--:|:--|:--|
| 1 | `C(n)` | **3** | 3 | `144` | n=6..14 PASS |
| 2 | `D(n)` | **6** | 6 | `1036800 = 50·144²` | n=9..14 PASS |
| 3 | `E(n)` | **9** | 9 | `21946982400 = 7350·144³` | n=12,13,14 PASS |

So **`deg c_{2k}(n) = 3k`** for k=1,2,3, and every denominator is `m_k·144^k` (`m_k ∈ {1, 50, 7350}`) —
the Identity-I `144` recurs at every order. (`E(n)` is a degree-9 integer polynomial; its full
coefficient list is in the witness.)

**Honest framing — this is expected, and that is the point.** The polynomiality is *not* a
surprising coincidence: the defect coefficients are symmetric functions of cell contents / hook
lengths averaged over the Plancherel measure, and such averages are **polynomial functions on the
set of Young diagrams** (Kerov–Olshanski; Kerov / Biane polynomials). So the framework's defect
expansion sits inside a known structural theory; the QOU-specific content is the **sharp degree
ladder `3k`** and the recurring `144^k` denominator. The degree-3k law is a **conjecture** on k=1,2,3
evidence (each rung rigorously polynomial + validated; the *general* law is the extrapolation) — a
proof should follow from the Identity-I / Kerov-polynomial structure, not from this probe.

**Consequence for the keystone.** If the law holds, the geometric `W_λ` index's **entire**
heat-kernel expansion is polynomial-in-`n` — an *unbounded* family of exact, q₀-free falsifiable
targets (the 2k-th heat-kernel coefficient = `c_{2k}(n)`), not merely the two of phase G2. The gate
is far more constraining than a single number-match could ever be.

## Cross-references

- [`computations/keystone_wlambda_defect_cn_closedform_crosscheck.py`](../../computations/keystone_wlambda_defect_cn_closedform_crosscheck.py) — this probe.
- [`docs/audits/scripts/keystone_wlambda_Z_defect_n_scaling.py`](scripts/keystone_wlambda_Z_defect_n_scaling.py) — the empirical defect script (the "no closed form" disclaimer this closes).
- [`WLambdaDefectClosedForm.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/WLambdaDefectClosedForm.lean) — the Lean closed form (`n144C`, `n144C_pos`, `n144C_neg`).
- [`docs/scope/2026-06-24-keystone-fullhecke-geometric-index-program.md`](../scope/2026-06-24-keystone-fullhecke-geometric-index-program.md) — target (1) is this cubic; phase G2 gates against it.
- [`docs/coordination/s5-so3-keystone.md`](../coordination/s5-so3-keystone.md) — keystone ledger.
- #2655 — Identity (A) `Σ h² = Σ c² + n²` proved sorry-free (the cubic's algebraic origin).

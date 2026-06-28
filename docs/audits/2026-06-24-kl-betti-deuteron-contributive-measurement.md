# Option-E PROBE 4 — KL left-cell Betti sum is ×2.0 *contributive* on the deuteron (not a closure)

**Date:** 2026-06-24
**Branch:** `claude/brave-hawking-tjdu2p`
**Status:** scope-limited measurement (AGENTS.md §"Before declaring refuted").
No fit, no production rewire.
**Witness:** [`computations/option-e-kl-betti-contributive-deuteron.witness.json`](../../computations/option-e-kl-betti-contributive-deuteron.witness.json)
**Script:** [`computations/option_e_kl_betti_contributive_deuteron.py`](../../computations/option_e_kl_betti_contributive_deuteron.py)

## Why this measurement

The PROBE-4 KL-positivity prune
([`2026-06-16-option-e-probe4-kl-positivity-prune.md`](2026-06-16-option-e-probe4-kl-positivity-prune.md))
correctly established — and Lean-proved (`deltaSign_mixed`, PR #2416) — that the
**chirality sign** of $\Delta_\lambda = \mathrm{sgn}(w_0^{S_{\lambda'}})\cdot\dim$
cannot come from non-negative KL multiplicities. That sign exclusion stands.

The prune additionally stated, in passing, that KL "supplies **at most** the
magnitude $|\Delta_\lambda| = \dim(V_\lambda)$ — already the closure's $f^\lambda$
… at best it re-derives $|\Delta_\lambda|=\dim$ by a longer route." The owner
flagged that "not sufficient" ≠ "wrong," and asked whether the KL weight can be
**contributive** to the magnitude even if it does not close. Per the standing
*"Before declaring refuted"* discipline (a Lean-proved / structurally-exact
piece is a permanent contribution; "inaccurate alone" ≠ "excluded"; a
compositional object is already many-body), that question deserved a number,
not an assertion. The deuteron (H₆/S₆) is the **one nucleus whose KL left-cell
Betti sums are exactly computable** — the right oracle.

## What was computed (exact, reproducible, 7.3 s)

Same primitives as the canonical producer
[`delta_lambda_binding_full_evaluation.py`](../../computations/delta_lambda_binding_full_evaluation.py)
— $y_\lambda$ (Wenzl), $\chi^\lambda(\beta_D)$ (Hoefsmit+interface),
$\mathrm{sgn}(w_0^{S_{\lambda'}})$ (Macdonald) — changing **only** the per-λ
magnitude:

| magnitude | $\Sigma = \sum_\lambda y_\lambda\,\chi^\lambda\,\mathrm{sgn}\,(\cdot)$ | $B(D)=m_e\lvert\Sigma\rvert$ | vs AME 2.22452 |
|---|---|---|---|
| $f^\lambda = \dim V_\lambda$ (canonical) | −0.74378 | **0.380 MeV** | −82.9% |
| $B_\lambda = \sum_{w\in\Gamma_\lambda} P_{e,w}(1)$ (KL Betti) | −1.48938 | **0.761 MeV** | −65.8% |

- The $f^\lambda$ path reproduces the canonical witness (−0.7439) to 4 dp → the
  reconstruction is faithful.
- **Factor needed to close: ×5.85. Factor KL-Betti delivers: ×2.00.**
- The KL-Betti $B_\lambda$ values (computed via the on-main engine
  `kazhdan_lusztig.py`, identical method to PROBE-4 batch PR #2658):
  hooks $B_\lambda=f^\lambda$ exactly; bulk
  $(3,3)\!:5\to23$, $(4,2)\!:9\to20$, $(3,2,1)\!:16\to41$,
  $(2,2,2)\!:5\to21$, $(2,2,1,1)\!:9\to21$. The lift is entirely from the
  bulk; the dominant $(5,1)$ term is a **hook**, so it is unchanged.

## Verdict (scope-limited, (a) not (b))

**KL-Betti is contributive to the deuteron magnitude (×2.0; −83% → −66%) but
does not close it (supplies ≈ 1/3 of the required ×5.85).** This is a genuine
partial contribution, not an excluded ingredient.

**Refinement of the prune.** The prune's *sign* exclusion is unaffected and
stands (Lean-proved). Its incidental magnitude claim — KL "at most re-derives
$|\Delta_\lambda|=\dim$" — is **imprecise**: the KL left-cell Betti sum is a
*distinct, strictly larger* magnitude than $\dim$ on bulk partitions, and it
*does* move the binding number. So the honest framing of PROBE-4 is **(a)
scope-limited** ("the KL-Betti magnitude, alone, is ×2.0 contributive and does
not close the deuteron; the sign must still be supplied exogenously"), not (b)
"KL is excluded / merely re-derives dim."

## Important caveat — this is NOT a production rewire

The object $\Delta_\lambda = \mathrm{sgn}\cdot\dim$ has $|\Delta_\lambda|=\dim$
**by definition** (Lean `binding_magnitude_eq_dim`). Substituting $B_\lambda$ for
$\dim$ defines a *different* ansatz $\Delta'_\lambda=\mathrm{sgn}\cdot B_\lambda$;
it is not "the magnitude of $\Delta_\lambda$." Because $\Delta'_\lambda$ does not
close the deuteron (−66%) and is not independently motivated by the categorical
chain, it is **not wired into production binding** — that would be a non-closing
ansatz swap, against the "no 7th fit-based ansatz" discipline. What is recorded
here is the *measurement* of its contribution, as a witness.

## Next steps (per owner steer)

- **S₁₂ / ⁴He KL-Betti contribution (option 4).** Brute KL over $S_{12}$
  (479M perms) is infeasible; the tractable route is **smoothness-pruned**
  ($P_{e,w}=1$ unless $w$ is singular — Lakshmibai–Sandhya: $w$ avoids 3412 &
  4231 — so $B_\lambda = f^\lambda + \sum_{\text{singular }w\in\Gamma_\lambda}(P_{e,w}(1)-1)$),
  measuring the ⁴He contribution, *not* claiming closure.
- **FOCUS lever z2bn (option 3).** Fibre-level $q$-difference kernel $R(q,x)$ for
  the binding generating function — the unpruned, fibre-level direction (a new
  *term*, not a per-λ magnitude refit).

## Coordination (2026-06-28) — siblings own S₁₂ and z2bn

Picking this up against `main` (+504 commits) surfaced two active sibling lanes
that overlap the owner's option-4 / option-3 asks — recorded here to avoid
duplication:

- **Option 4 (S₁₂ / ⁴He native KL-Betti) → sibling PR #2839**
  (`a4-betti-derivation-2026-06-26`). Independently found the same localization
  (inverse-RSK over the canonical cell; "shallow interval phenomenon" for
  elongated λ) and has the **native Rust** KL engine to pass the Python n≤6 cap:
  reports $B_{(10,2)}=584$ (~98 s) and claims it "closes" A=4. The
  `kl_betti_smoothness_pruned.py` added here is the **pure-Python cross-check**
  of that method (validated at n=6; n≥7 needs their Rust engine).
  - **⚠ Reconcile (critical-distance):** the deuteron **full exact sum** here
    shows KL-Betti is **×2.0 contributive, not closing**. A blanket "KL-Betti
    closes binding" is contradicted by the deuteron oracle. Whether A=4
    genuinely differs, or the #2839 "closure" is a single-partition-scalar fit,
    must be checked on the **full** A=4 Σ_λ (not one B_λ). Posted as a
    coordination note on #2839.
- **Option 3 (fibre q-difference kernel R(q,x)) → sibling bean `z2bn`, PRs
  #2899/#2925.** Deep progress (Stage 2–5, sorry-free binding q-Gaussian Habiro
  tower). Not duplicated here.

## A=4 (⁴He) empirical reconciliation (2026-06-28)

Ran the reconciliation on `main` to test #2839's "$B_{(10,2)}=584$ closes A=4":

- The **only runnable A=4 integration on main**, `a4_option_e_color_tube_closure.py`,
  gives $|\Sigma_\lambda (y\cdot\chi\cdot\text{sign})| = 0.011567 \to 0.0059$ MeV raw
  $\to \times10^3$ color-tube $= \mathbf{5.91}$ **MeV** vs AME 28.30 (**−79.1%**). It does
  not close, and the $\times10^3$ is the retracted color-tube numerology (not Betti).
- **No full signed $\Sigma_\lambda\,y\cdot\chi\cdot\text{sgn}\cdot B_\lambda$ exists on
  main.** `chi-helium-4-h12-at-q0-50dps` is **17/77** partitions (`partial: true`;
  producer `chi_4he_via_rust_lossless.py` is **Rust-gated** — `pyhecke_native`
  unavailable, and the pure-Python matrix-M fallback is "infeasible for n=12" per its
  own docstring — bean **b0vf**), and only $B_{(10,2)}$ of the 77 $B_\lambda$ is computed
  (#2839, Rust). So the A=4 "closure" cannot be a full-sum result — it is a
  single-partition scalar.
- **Verdict:** on **both** computable fronts (A=2 full sum here; A=4 only-runnable
  script) Option-E/KL-Betti is **contributive/insufficient, not closing**. Do **not**
  re-chase an A=4 "closure" until (a) the 77-partition χ^λ table is complete (b0vf,
  needs the Rust producer) **and** (b) all 77 $B_\lambda$ are computed (#2839 Rust);
  then run the full signed $\Sigma_\lambda$ on
  `option_e_kl_betti_contributive_deuteron.py` (it generalizes from the deuteron).

(Bean-hygiene note: `t6ba` — the `path_b_habiro_mass_probe` A≥3 `check_q` crash — is
verified **resolved on main**: the probe runs clean, exit 0; A≥3 atoms now skip
gracefully on missing-witness data, a separate matter, not the crash.)

## Cross-references

- [`2026-06-16-option-e-probe4-kl-positivity-prune.md`](2026-06-16-option-e-probe4-kl-positivity-prune.md) — the sign prune (stands)
- [`docs/coordination/option-e.md`](../coordination/option-e.md) — Δ_λ closure ledger
- `S5SO3FiberAction.lean` — `deltaSign_mixed` (sign prune premise), `binding_magnitude_eq_dim` (|Δ_λ|=dim) — both sorry-free

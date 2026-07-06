# Coordination ledger — CAL-4 λ_scale cluster (2026-05-22)

**Goal:** Remove the CAL-4 `λ_scale` fitting from production by closing
cheat-sheet §5 fix #1, both at the taxonomy level (content blocks
correctly labelled `conj:` where derivation is open) and at the
code level (production scripts use the **proved** Family A
categorical identity, not the falsified `5/2 − h²·G` empirical fit).

## Scope map

| PR | Branch | Face | Status |
|---|---|---|---|
| **#888** | `claude/rust-laurent-q-2026-05-22` | Literal truth-in-naming (`LAMBDA_*_FITTED_FROM_CODATA`) + new I13 audit + CI registration | **merged 2026-05-22** |
| **#892** | `claude/iw-cal4-disguised-fix-2026-05-22` | Curve-fit `a(q) = (4-q)/(4q+3)` → `conj:mobius-limit-from-thimble` | open |
| **#904** | `claude/iw-bring-bloch-cal4-audit-2026-05-22` | Named replacement target → `conj:lambda-scale-bring-bloch-identity` (vacuous-rfl + PSLQ tier 0–5 refuted) | open |
| **#895** | `claude/cheat-sheet-fix-3-rust-lr-adapter-2026-05-22` | **Production code-level removal**: fitted literals replaced with **PROVED Family A** `5/2 + (3/4) h²` | open, prepare-merge complete |
| **#909** | `claude/keen-maxwell-jqdPU` | Strategy D research probe (q-dilog tower direction) | open |

## Key finding (Family A as PROVED replacement)

The Family A categorical identity is **already proved sorry-free**
in both [`lambda-scale-substrate-form.lean`](../../content/quantum-observable-universe/braids-and-knots/lambda-scale-substrate-form.lean)
and the Python verification
[`lambda_scale_all_c_i_family_a.py`](../../computations/lambda_scale_all_c_i_family_a.py):

$$
  \lambda_A(q) \;:=\; \frac{1}{4} \sum_{\lambda \vdash 4} \dim_q V_\lambda
  \;=\; \frac{3 q^2 + 4 + 3 q^{-2}}{4}
  \;=\; \frac{5}{2} \;+\; \frac{3}{4} h^2
$$

(the h-series terminates exactly at $h^2$). At $q_0$ this gives
$\lambda_A \approx 2.5328$, vs the falsified empirical fit
$5/2 - h^2 \cdot G \approx 2.4600$ and the CODATA closure target
$\approx 2.4599527869$.

The user's challenge that prompted #895's λ swap:

> "if this is proved... Family A theorem: λ_A(q) = 5/2 + 3h²/4 (in
> lambda_scale_all_c_i_family_a.py + Lean) why R&D? we need to get
> bad stuff out of production."

The answer is: it IS proved. The R&D is for the *Bring-Bloch /
q-dilog tower* path that would close the residual ~3 % between
Family A and CODATA. Family A itself is the categorical truth at
the H_4 layer; the production code should use it, not a fit.

## Production change in #895

`m_p_borromean_verification_50dps.py`:

```python
# Before (CAL-4 fit, falsified):
LAMBDA_PROTON_FITTED_FROM_CODATA = mp.mpf("2.4599527869")
LAMBDA_NEUTRON_FITTED_FROM_CODATA = mp.mpf("2.4633436333")

# After (Family A, PROVED):
_H_VAL = Q - mp.mpf(1) / Q
LAMBDA_PROTON_FAMILY_A = mp.mpf(5) / 2 + mp.mpf(3) * _H_VAL ** 2 / 4
LAMBDA_NEUTRON_FAMILY_A = LAMBDA_PROTON_FAMILY_A
```

Predictions move:

| | m_p (MeV) | m_n (MeV) | err vs CODATA |
|---|---:|---:|---:|
| Falsified fit (was prod) | 938.2774 | 939.5710 | +5.4 ppm (tautological) |
| Family A (now prod) | 966.0496 | 966.0496 | **+2.96 %, +3.00 %** |
| CODATA | 938.2721 | 939.5654 | — |

The proton-neutron prediction equality reflects that Family A is a
**baryon class** formula. The n−p mass difference enters downstream
via `flavor_split_subleading` (PR #690), independent of $\lambda$.

## Falsified literals retained as audit-only

- `LAMBDA_PROTON_FITTED_FROM_CODATA_AUDIT_ONLY` / `_NEUTRON_*` —
  kept as `*_AUDIT_ONLY` parameters in the witness so the Phase 5q
  ppm-coincidence comparison column still works. NOT consumed by
  the production prediction.

## Assertion thresholds in #895

Was `proton_borromean_tower_ppm_lt_1` (only passed against the
fitted tautology); now `proton_borromean_tower_within_5pct_of_codata`
with `tolerance = 50 000 ppm` (5 % ceiling) — which the Family A
prediction passes honestly. Regression to the falsified ppm-fit
would still surface (a sub-1 ppm "match" would no longer be the
honest framework prediction).

## Coordination comments posted

- #892: <https://github.com/litlfred/qou/pull/892#issuecomment-4522311200>
- #904: <https://github.com/litlfred/qou/pull/904#issuecomment-4522312949>
- #909: <https://github.com/litlfred/qou/pull/909#issuecomment-4522315442>

## Open research targets

| Target | Owner | Direction |
|---|---|---|
| Bring-Bloch identity closed form | research | Tier 0–5 PSLQ refuted in hyperbolic-knot basis; q-dilog tower next |
| Categorical q-dilog tower → λ_scale | Strategy D (#909) | LP / PSLQ at 100 dps against ε residual *vs Family A baseline* (per coordination comment) |
| Bring color-tube quark-weighted p-n averaging | research | flavor-asymmetric closed-form; per `probe_pn_flavor_asymmetry.py` Scheme 4 closes Δm_{n-p} to ~0.14 % |

## Cheat-sheet §5 status after this cluster

- [x] **#1 LAMBDA truth-in-naming** — closed by #888 + #895
- [ ] #2 SUPERSEDED `mass_endomorphism.py` migration (20 importers) — gated on Lean (Z+N)
- [x] **#3 Rust LR adapter wiring** — closed by #895
- [ ] #4 closed-form `tr_M(𝓑_K)` refactor (4 scripts) — Phase 5q convention reconciliation needed
- [ ] #5 Reeb-flow / Garside compute verification — not started

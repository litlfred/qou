# α_EM B2 lift — Reality-realization consistency check 1 (2026-07-18)

**Bean:** `qou-tq20`, fourth tranche — the first numerical check of the
**Reality-realization** premise, the wall's final form after
[#3999](https://github.com/litlfred/qou/pull/3999) (instance constructor).

**Probe:** [`computations/alpha_em/alpha_em_reality_consistency_probe.py`](../../computations/alpha_em/alpha_em_reality_consistency_probe.py)
→ [`alpha-em-reality-consistency.witness.json`](../../computations/alpha_em/alpha-em-reality-consistency.witness.json)
— 4/4 PASS, sympy-exact.

**Scope guard (STRICT):** consistency, **not** a derivation; low-entropy
caveat stated; no fit; nothing wired; `1/(8π)` stays phase-4.

## The check

The open half of the Reality-realization premise is the τ-identification of
the canonical Markov channel weight with a geometric (period-derived)
operator on `H^{1,0}(Bring)`. First comparable invariant — the multiplicity
structure at the decategorification point:

| Side | Object | Dim vector |
|---|---|---|
| categorical | canonical Markov weights at n=2, q=1: `(¾, ¼)` (corpus `y_lambda_at`) | `4·y = (3, 1)` |
| geometric | principal polarization `M` (`τ_B = τ₀·M`, Braden–Disney-Hogg Thm 2.12): `spec(M) = {5:3, 1:1}`, det 125 — `Jac(Bring) ≅ E_{5τ₀}³ × E_{τ₀}` | isotypic `(3, 1)` |

**Match: exact.** The τ-image of the canonical Markov channel weight at q=1
has precisely the isotypic dimension structure of `H^{1,0}(Bring)`'s
canonical splitting.

## Honest assessment

- A (3,1) split of a 4-dim space is **low-entropy** — the match could not
  have failed in many ways. No tier change; the wall (the τ-identification
  itself) remains open.
- Its value: the identification **survives first contact** with the exact
  period data, and it produces the next **falsifiable** target: the
  identification predicts the geometric side carries a q-deformation of the
  (3,1) weights whose ratio is exactly the Markov `y_[2]/y_[1,1](q)` (= 3 at
  q=1, q-dependent away from it). Computing that deformation on the
  period side (Jacobian flat metric / theta data — the #3934/#3963 fronts)
  is the next comparison; a structured mismatch would refute the
  identification at scope-(a).
- The multiplier pair (5,1) in `spec(M)` is **recorded, not interpreted**.

## Position

```
qou-tq20: #3985 interface → #3992 ℂ-model → #3999 constructor →
          THIS consistency-1 (PASS) → next: period-side q-deformation
          (meets #3934 Epstein det′Δ / #3963 period-matrix fronts)
```

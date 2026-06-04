# c_11+ attempt — holonomic test + the data-level blocker (verdict)

**Date:** 2026-06-04
**PR:** (this branch — `claude/qbeta-ck-holonomic-c11-attempt-2026-06-04`)
**Status:** DONE — c_11+ blocked at the data level; multi-anchor is the unblock
**Builds on:** kernel deepening (#1839), c6-c10 cross-anchor falsification (on main)

## The attempt (formalize-first)

Step 2 (#1823) + the Lean grounding proved the c_k are **not** low-order
constant-coefficient C-finite ⇒ `F(u)` is **not** a low-degree rational. The
next structural class up — which **subsumes** the cosh-avatar /
generating-function hypothesis (#1824) — is **holonomic (D-finite)**: do the c_k
satisfy a *polynomial*-coefficient recurrence `∑_i p_i(n)·c_{n-i} = 0`? A
positive low-order fit would **predict c_11+** outright. This is a structural
class test, not a free fit (compute-author §3.3).

Probe:
[`qbeta_ck_holonomic_recurrence_guess.py`](../../folio-assistant/computations/qbeta/qbeta_ck_holonomic_recurrence_guess.py).

## Result

| window | order | deg | smallest-SV (normalised) | holonomic? |
|---|---|---|---|---|
| applied c2..c7 | 1 | 1 | 5.3e-3 | no |
| full c2..c10 | 1 | 1 | 1.2e-9 | no |
| full c2..c10 | 1 | 2 | 1.0e-11 | no |
| full c2..c10 | 2 | 1 | 5.2e-10 | no |

No clean low-order holonomic recurrence. The `~1e-11` values are the
**conditioning / noise floor** (the erratic free rung `c_10 ≈ 1e8` dominates the
matrix), **not** a D-finite signal — a true holonomic recurrence would give
`~1e-30` at 40 dps.

## The honest verdict — blocked at the DATA level

This is **not decisive** for `F`'s holonomicity, because the only **independent**
rungs are unreliable. Per the just-landed
[c6-c10 cross-anchor falsification](2026-06-04-c6-c10-crossanchor-biascorrected-falsification.md):

- the canonical extraction **imposes** closed forms at **c_2..c_7** (so their
  recovery is self-consistency, not independent data);
- **c_8..c_10** are extracted **freely from a single anchor** — and c_8 (first
  free rung) is erratic, breaking the Pell-Lucas continuation.

So the structural tests (constant-kernel, holonomic, generating-function) all run
into the **same wall**: there is no reliable, scale-comparable, independent c_8+
data to test against. A negative result is therefore consistent with *either* `F`
non-holonomic *or* free-rung extraction noise.

## The genuine unblock (the next keystone compute)

Reliable independent c_8+ (hence c_11+) require a **multi-anchor extraction**:
`R(q) = Q_β / (Q_A·cos α_eff)(q) = ∏_k (1 + c_k·u(q)^k)` evaluated at **several
q-anchors** (the c_k are fibre-level constants; `u(q) = b(q)·ℏ_q(q)²` varies). The
c_2..c_7 applied forms hold at every anchor, so the cross-anchor **residuals**
pin c_8, c_9, … independently — removing the single-anchor self-cancellation
that blocks the free rungs. This needs `Q_N2(q)` (the SDP-selected operator norm)
re-run at multiple anchors — the genuine keystone compute, and the prerequisite
for any structural identification (holonomic, generating-function, or otherwise).

## Net (the keystone is now precisely located AND its blocker named)

- **Refuted** (this campaign): real-q forms, root-of-unity, low-order rational
  (constant kernel), the SDP cos-factor zero, and now low-order holonomic on the
  current data.
- **Blocker** (newly precise): the free single-anchor c_8+ are unreliable; every
  structural test is starved of independent data.
- **Unblock** (newly precise): multi-anchor `Q_N2(q)` extraction → reliable c_8+
  → then re-run the holonomic / generating-function tests with teeth.

## Guards

TIERED; structural-class test (not a fit); ℏ_q/q₀ from canonical witnesses;
diagnostic-only; tiers governed by the
[c_k/d_k registry](../coordination/ck-dk-canonical-registry.md).

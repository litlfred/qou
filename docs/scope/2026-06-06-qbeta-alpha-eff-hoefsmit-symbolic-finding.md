# Q_β α_eff is already symbolic on `main`: `(z−1)·h/2` — finding + the narrowed open step

**Status:** corpus-grep finding + Lean-free symbolic probe (verified at both anchors). A **contribution to the KLR/crystal residue-A program** ([`docs/scope/2026-06-05-qbeta-residue-a-klr-crystal-kernel-scope.md`](2026-06-05-qbeta-residue-a-klr-crystal-kernel-scope.md), on `main`), supplying the "Symbolic α(q)" item that scope lists as open.
**Owner direction:** 2026-06-05/06 session (litlfred) — "Hoefsmit feeds the KLR kernel".
**Disciplines:** *corpus-grep* (before declaring α open, search the corpus — it was already computed), *formalize-first* (pin the precise structural gap before any wide symbolic search), *coordinate* (feeds the KLR program; does not claim the kernel derivation).

---

## 1. Finding — the symbolic α_eff is NOT open; it is on `main`

The KLR residue-A scope doc lists, under "the remaining work", *"Symbolic α(q) — extract from the operator-valued N=3 witness or derive from the Hoefsmit seminormal blocks of H₃(q)."* A corpus-grep shows this is **already done** in
[`probe_q_beta_operator_valued_N3.py`](../../folio-assistant/computations/probe_q_beta_operator_valued_N3.py)
(on `main`), in closed symbolic form:

```
z      = 1 / (√q + 1/√q)        # bar-EVEN  (= 1 / (2 cosh(η/2)))
h      = q − 1/q                 # bar-ODD   (= 2 sinh η, the Hecke parameter)
alpha  = (z − 1) · h / 2         # bar-ODD   single-wrap angle
ℏ_q    = (q − 1)/q,   u = b·ℏ_q² # ladder variable; b = Hoefsmit normalisation
Q_β/Q_A = cos( alpha − u/2 − u²/2 − u³/2 − … )       (N=3 candidate)
```

The companion probe
[`qbeta_alpha_eff_hoefsmit_symbolic_probe.py`](../../folio-assistant/computations/qbeta/qbeta_alpha_eff_hoefsmit_symbolic_probe.py)
re-derives `alpha` from these closed forms and reproduces the on-main N=3
witness value **exactly** (`alpha = −0.05233612…` at the proton anchor),
confirming the lift is faithful.

**Two consequences:**

1. **`alpha` is bar-ODD** — `(z−1)·h/2` with `z` bar-even and `h = q−q⁻¹`
   bar-odd. This **independently confirms, from the categorical (Hoefsmit)
   side**, the #1900 kernel constraint that the c_k-recursion leading
   coefficient `a_1 = −c_3 = √2·Φ₂` is bar-odd. Two independent routes
   (Reeb-`sinh` parity #1887/#1900, and the Hoefsmit single-wrap angle here)
   land on the same parity.
2. The "open symbolic α" item in the KLR scope can be **closed/retired** and
   replaced by the narrower open step below.

## 2. The narrowed open step — ladder-variable reconciliation

The #1887/#1900 reframe wrote `Q_β/Q_A = cos(Φ(u))`, `Φ(u) = Φ₁u + Φ₂u² + …`
with `Φ₁ = √2`, **`c_1 = 0`** (ladder starts at `k=2`) and `c_2 = −1`. The
on-main producer phase `alpha − u/2 − u²/2 − …` instead has a non-zero
constant `alpha` and a non-zero u¹ term. Normalising the base so `F(0)=1`:

```
F(u) = cos(alpha − u/2 − u²/2 − u³/2) / cos(alpha) = 1 + c_1 u + c_2 u² + …
```

the probe finds (values below rounded for display; the full-precision
per-anchor figures are the source of truth in
[`qbeta-alpha-eff-hoefsmit-symbolic-probe.witness.json`](../../folio-assistant/computations/qbeta/qbeta-alpha-eff-hoefsmit-symbolic-probe.witness.json),
computed at the default 65-dps compute precision; proton and muon agree to
the 6 figures shown and differ only at higher order):

| coeff | producer value (proton, rounded) | #1887 ladder value |
|-------|----------------|--------------------|
| `c_1` | `tan(alpha)/2 = −0.026192` (≠ 0) | `0` |
| `c_2` | `−0.151192` | `−1` |
| `c_3` | `−0.275101` | `≈ −2.069` |

The `c_1 = tan(alpha)/2` identity is checked on the raw `mpf` values
(assertion `c1_matches_tan_alpha_over_2`, tolerance `1e-30`), not on the
rounded display figures.

So the producer's `u = b·ℏ_q²` is **a different ladder variable** than the
#1887 reframe's `u`. The genuinely open piece is therefore **not** "derive
symbolic α" (done) but the **change of ladder variable** `u → ũ(u)` that
(a) kills the u¹ term (`c_1 → 0`) and (b) normalises `c_2 → −1`; under that
rescaling `Φ₂` follows from the symbolic `alpha = (z−1)·h/2` directly. This
is a one-variable reparametrisation problem, not a wide categorical search.

## 3. What this contributes to the KLR program (bounded)

| Deliverable | NOT claimed |
|---|---|
| corpus-grep finding: symbolic `α_eff = (z−1)·h/2` is on `main`, bar-odd (retires the KLR scope's "open symbolic α") | the kernel `R` / `F(q) ∈ Habiro(ℤ)` derivation |
| independent (Hoefsmit-side) confirmation of the #1900 bar-odd kernel parity | a value for `Φ₂` |
| the **narrowed** open step (ladder-variable reconciliation `u → ũ`), with the exact `c_1 = tan(alpha)/2` obstruction quantified | the reconciliation itself (next focused tranche) |
| symbolic probe + witness | any production wiring (Δ_λ gate held; no fit) |

The kernel `R` / categorification stays the KLR/SW-residue frontier; this PR
narrows its α-input from "open" to "reparametrise a known closed form".

## 4. References

- α_eff symbolic source (on `main`): [`probe_q_beta_operator_valued_N3.py`](../../folio-assistant/computations/probe_q_beta_operator_valued_N3.py).
- ladder reframe + kernel constraints (merged): PR #1887, PR #1900; [`docs/scope/2026-06-05-qbeta-phi2-ckrecursion-kernel-constraints.md`](2026-06-05-qbeta-phi2-ckrecursion-kernel-constraints.md).
- KLR residue-A program: [`docs/scope/2026-06-05-qbeta-residue-a-klr-crystal-kernel-scope.md`](2026-06-05-qbeta-residue-a-klr-crystal-kernel-scope.md).
- Ledger: [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md).

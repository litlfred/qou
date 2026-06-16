# Q_β α_eff is already symbolic on `main` = `(z−1)·h/2` (bar-odd); but it is a DISTINCT phase from the #1887 Φ(u)

**Status:** corpus-grep finding + two Lean-free symbolic probes (verified at both anchors). A **contribution to the KLR/crystal residue-A program** ([`docs/scope/2026-06-05-qbeta-residue-a-klr-crystal-kernel-scope.md`](2026-06-05-qbeta-residue-a-klr-crystal-kernel-scope.md), on `main`): the "Symbolic α(q)" item that scope lists as open is **already computed** (§1), and a reconciliation probe **refutes** the easy path of reading `Φ₂` off it (§2) — narrowing what the kernel work must still supply.
**Owner direction:** 2026-06-05/06 session (litlfred) — "Hoefsmit feeds the KLR kernel".
**Disciplines:** *corpus-grep* (before declaring α open, search the corpus — it was already computed), *formalize-first* (pin the precise structural gap before any wide symbolic search), *coordinate* (feeds the KLR program; does not claim the kernel derivation).

---

## 1. Finding — the symbolic α_eff is NOT open; it is on `main`

The KLR residue-A scope doc lists, under "the remaining work", *"Symbolic α(q) — extract from the operator-valued N=3 witness or derive from the Hoefsmit seminormal blocks of H₃(q)."* A corpus-grep shows this is **already done** in
[`probe_q_beta_operator_valued_N3.py`](../../computations/probe_q_beta_operator_valued_N3.py)
(on `main`), in closed symbolic form:

```
z      = 1 / (√q + 1/√q)        # bar-EVEN  (= 1 / (2 cosh(η/2)))
h      = q − 1/q                 # bar-ODD   (= 2 sinh η, the Hecke parameter)
alpha  = (z − 1) · h / 2         # bar-ODD   single-wrap angle
ℏ_q    = (q − 1)/q,   u = b·ℏ_q² # ladder variable; b = Hoefsmit normalisation
Q_β/Q_A = cos( alpha − u/2 − u²/2 − u³/2 − … )       (N=3 candidate)
```

The companion probe
[`qbeta_alpha_eff_hoefsmit_symbolic_probe.py`](../../computations/qbeta/qbeta_alpha_eff_hoefsmit_symbolic_probe.py)
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

## 2. Reconciliation REFUTED — α_eff is a distinct phase from the #1887 Φ(u)

The #1887/#1900 reframe wrote `Q_β/Q_A = cos(Φ(u))`, `Φ(u) = Φ₁u + Φ₂u² + …`
with (proved) **`c_1 = 0`** (ladder starts at `k=2`) and `c_2 = −1`, hence
`Φ₁ = √2`. The natural question: does `Φ₂` then drop out of the symbolic
`alpha = (z−1)·h/2`? A second probe
([`qbeta_alpha_eff_ladder_reconciliation_probe.py`](../../computations/qbeta/qbeta_alpha_eff_ladder_reconciliation_probe.py))
answers it decisively using the producer's **canonical** N=1/N=2 model
(`probe_q_beta_operator_valued_N3.py` lines 75–78), not the earlier line-144
exploratory candidate:

```
Q_N1 = Q_A·cos(alpha − u/2),   Q_N2 = Q_N1·(1 − u²),   u = b·ℏ_q²
G(u) = Q_N2 / [Q_A·cos(alpha)] = cos(alpha − u/2)(1 − u²)/cos(alpha)
     = 1 + c_1 u + c_2 u² + …
```

Taylor expansion gives (both anchors identical; full precision in
[`qbeta-alpha-eff-ladder-reconciliation-probe.witness.json`](../../computations/qbeta/qbeta-alpha-eff-ladder-reconciliation-probe.witness.json)):

| coeff | canonical α_eff model | #1887 ladder (proved) |
|-------|------------------------|------------------------|
| `c_1` | `tan(alpha)/2 = −0.026192` (≠ 0) | `0` |
| `c_2` | **`−9/8 = −1.125`** (α-independent, structural) | `−1` |
| leading phase coeff | `√(2·9/8) = 3/2` | `√2 = 1.41421…` |

Both coefficients mismatch, and `c_2 = −9/8` is **structural** (independent
of `q`/`alpha` — both anchors give `−1.12500000`). Crucially, **no single
ladder rescaling `ũ = λ·u` can reconcile both rungs**: choosing `λ = √(9/8) =
1.06066` to force `c̃_2 = −1` leaves `c̃_1 = c_1/λ = −0.024694 ≠ 0` (the u¹
rung survives). Fixing `c_1` *and* `c_2` needs two degrees of freedom; a
rescale has one. (Probe assertions `c2_is_structural_minus_9_over_8_both_anchors`
and `no_single_rescale_reconciles_both_rungs`, both pass.)

**Conclusion (decisive):** the on-main `alpha = (z−1)·h/2` is a **genuinely
different phase parametrisation** than the #1887 `Φ(u)` — it is the
single-wrap angle of the producer's `cos(alpha − u/2)(1 − u²)` N=2 model
(`c_2 = −9/8`), not the proved ladder (`c_2 = −1`). **`Φ₂` does NOT follow
from `(z−1)·h/2` by reparametrisation.** The easy path is closed; the exact
`Φ₂` remains the kernel-derivation (SW-residue / KLR) frontier. What survives
intact: `alpha` is bar-odd (§1), an independent confirmation of the #1900
bar-odd kernel parity.

## 3. What this contributes to the KLR program (bounded)

| Deliverable | NOT claimed |
|---|---|
| corpus-grep finding: symbolic `α_eff = (z−1)·h/2` is on `main`, bar-odd (retires the KLR scope's "open symbolic α") | the kernel `R` / `F(q) ∈ Habiro(ℤ)` derivation |
| independent (Hoefsmit-side) confirmation of the #1900 bar-odd kernel parity | a value for `Φ₂` |
| **decisive refutation**: the on-main α_eff phase (`c_2 = −9/8`, structural) is NOT the #1887 Φ(u) (`c_2 = −1`); no single rescale reconciles both rungs ⇒ `Φ₂` does not follow from `(z−1)·h/2` | a way to get `Φ₂` without the kernel |
| 2 symbolic probes + witnesses (6 assertions total) | any production wiring (Δ_λ gate held; no fit) |

The kernel `R` / categorification stays the KLR/SW-residue frontier. This PR's
net effect on it: the α-input is a **known closed form** (`(z−1)·h/2`,
bar-odd), but it is the single-wrap angle of the N=2 *approximation*, **not**
the proved ladder phase — so the kernel work must derive the exact `Φ(u)`
(or its `Φ₂`), it cannot recover it from the on-main `alpha` by
reparametrisation. The easy path is formally closed.

## 4. References

- α_eff symbolic source (on `main`): [`probe_q_beta_operator_valued_N3.py`](../../computations/probe_q_beta_operator_valued_N3.py).
- ladder reframe + kernel constraints (merged): PR #1887, PR #1900; [`docs/scope/2026-06-05-qbeta-phi2-ckrecursion-kernel-constraints.md`](2026-06-05-qbeta-phi2-ckrecursion-kernel-constraints.md).
- KLR residue-A program: [`docs/scope/2026-06-05-qbeta-residue-a-klr-crystal-kernel-scope.md`](2026-06-05-qbeta-residue-a-klr-crystal-kernel-scope.md).
- Ledger: [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md).

# Spectral bridge — the depth-2 binding kernel is extensive (z2bn lever-1)

**Date:** 2026-06-24
**Branch:** `claude/binding-recurrence-spectral-bridge-2026-06-24`
**Bean:** `z2bn` (Lever 1 [FOCUS] — fibre q-difference kernel `R(q,x)`)
**Connects:** the algebraic kernel (`binding_selection_rule_tau_closure.py`, #2612) ↔
the empirical saturation finding (PR #2703).

## The two facts being bridged

1. **(algebraic / #2612)** The fibre q-difference kernel for the binding generating
   function `G(x;q)=Σ Bₙ xⁿ` is depth-2, `R(q,x) = x² − τ·x + 1` (det = 1), with `τ`
   fixed **without fit** by the selection-rule anchors `a_D⁽ⁿ⁾ = lw(n−1)`:
   `a_D⁽²⁾=1`, `a_D⁽³⁾=(q+1)²/(3q)`, `a_D⁽⁴⁾=(3q²+4+3q⁻²)/4`, giving
   `τ = (a₂+a₄)/a₃` and `τ(q₀) = 2.6424`.
2. **(empirical / #2703)** The `|χ|` joint-trace binding **saturates** — it is nearly
   A-independent (³H 3.25 → ³He 3.47 → ⁴He 3.80 MeV) while `B_AME` explodes; ⁴He
   captures only 13 %. The missing binding is the **extensive (A-scaling)** part,
   which a saturating/intensive object cannot source (`productModel_3body_nonpos`).

## The bridge

The body-order recurrence `a_{n+2} = τ·a_{n+1} − a_n` has characteristic roots
`λ_± = (τ ± √(τ²−4))/2`. At `τ(q₀)=2.6424`:

| quantity | value |
|---|---:|
| `λ₊` (dominant) | **2.1846** |
| `λ₋` (sub-dominant) | 0.4577 |
| `λ₊·λ₋` (det) | 1.0000 |
| `a_D⁽²⁻⁹⁾` | 1, 1.34, 2.53, 5.36, 11.6, 25.3, 55.4, 121, 264 |
| ratio `a_{n+1}/a_n → λ₊` | 1.34 → 1.89 → 2.11 → 2.17 → 2.18 → **2.1846** |

**`λ₊ = 2.185 > 1` is the extensive-growth eigenvalue the saturating `|χ|` trace
lacks.** The `|χ|` joint trace sits at the degenerate `τ = 2` (`λ₊ = λ₋ = 1`)
no-growth boundary — A-independent, intensive. The kernel `R` has `τ = 2.6424 > 2`,
so its general solution grows geometrically `~λ₊ⁿ`: the exact extensive mechanism
PR #2703 found missing. The two results are two views of one fact.

## Formalized (formalize-first, sorry-free)

[`QOU/Mass/BindingRecurrenceSpectral.lean`](../../content/quantum-observable-universe/lean/QOU/Mass/BindingRecurrenceSpectral.lean)
(verified `lean`-direct, exit 0):

- `lambdaPlus_isRoot` — `λ₊` solves `x² − τx + 1 = 0`;
- `lambda_product_eq_one` — `λ₊·λ₋ = 1` (det = 1 ⇒ reciprocal roots);
- `lambdaPlus_gt_one` — **`τ > 2 ⇒ λ₊ > 1`** (extensive), whence `λ₋ < 1`.

So `τ(q₀) = 2.6424 > 2` ⇒ extensive. This is the structural invariant the kernel
must satisfy to source extensive binding — and the derived kernel satisfies it.

## Honest scope (not a closure)

This is a **structural connection**, not a derivation of `τ` or a binding closure:

- `τ` is still only **algebraically** fixed (selection-rule anchors); its
  **geometric** origin (the monodromy trace `tr B = 2.6424`) is the sibling
  `lever1-trB` / s5-so3-keystone object (#2488/#2524, owner-gated DG) — untouched here.
- The **magic-A ⁴He +5.87 %** miss stands, but it is a **separate object** from the
  body-order series. **Correction (2026-06-24):** an earlier version of this section
  called it "the finite-truncation residual of the geometric series" — that was an
  **over-claim**. The +5.87 % is the gap of the *separate doubly-magic formula*
  `B = 2·m_e·A·8G` (29.956 vs 28.296 MeV); the physical-body-order (`n ≤ A = 4`)
  jet-sum `m_e·Σ a_D⁽ⁿ⁾` is only ≈ 2.49 MeV (≈ 11× too small), and the series
  *diverges* (`λ₊ > 1`), so there is no finite total to truncate. The spectral-bridge
  result is unaffected — it concerns body-order *growth*, not the magic-A gap. See
  [`2026-06-24-magic-a-truncation-overclaim-correction.md`](2026-06-24-magic-a-truncation-overclaim-correction.md).
- The bridge is parameter-free but interpretive: it shows the *existing* kernel's
  dominant root **is** the extensive eigenvalue, resolving "what supplies extensive
  binding" (PR #2703's open question) in favour of `R`'s `λ₊ > 1`.

→ `computations/probes/binding_recurrence_spectral_bridge_probe.py` ·
`computations/binding-recurrence-spectral-bridge.witness.json` ·
`QOU/Mass/BindingRecurrenceSpectral.lean`

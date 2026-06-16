# Q_β derivation gap — actionable plan (2026-05-30)

## What's the gap

At canonical q₀:
- Q_β closes to **1247 ppb** at N=2 (c_2 = -1, Taylor-exact, Lean-proved).
- N=3, N=4, N=5 structural-conjecture forms (c_3 = J_Hopf, J−ℏ_q², J·b⁴, …) have q₀-dependent residuals 0.5–3% — **not** Taylor-exact at canonical q₀ — so don't clear the bar.
- The Q_β 100× target is **7.8 ppb**. Gap: 160× miss.

## What's already there (good)

- **Lean `habiro-expansion-atomic.lean`**: real `HabiroExpansion` structure with polynomial reconstruction; constant-case fully proved sorry-free; Habiro 2002 externals cited as axioms (`habiro_expansion_exists_axiom`, `habiro_expansion_unique_axiom`).
- **Lean `qPochhammer`** defined (`(1−u^k)` Pochhammer for any commutative ring).
- **Witness `habiro-coefficients-atomic.witness.json`**: integer Habiro coefficients `a_m ∈ ℤ[u]` for proton (M=8), neutron (M=8), deuteron (M=12), ³He (M=16), ⁴He (M=20). Integrality + finiteness verified computationally.
- **Lean `habiro-ring.lean`**: cyclotomic-completion construction `ℤ̂[q] = lim ℤ[q]/(q;q)_n`.
- **Content block `full-pole-structure-mass-trace.md`**: the canonical proposition `tr_M(T_w, q) = Σ a_m·(q;q)_m` is documented.

## What's broken (the actionable bugs)

### Bug 1: `habiro_exact_qbeta.py` uses the wrong Pochhammer + ignores `D(u)`

Reads `denom_in_u` from witness but doesn't divide by it; uses `(1−u^{2k})` Pochhammer instead of `(1−u^k)`. Result: produces 136 vs the correct 1.065 for proton tr_M.

**Fix:**
```python
def habiro_trM(atom_data, u_val):
    D = mpf(eval(atom_data['denom_in_u'].replace('u', f'({u_val})')))
    total = sum(mpf(eval(c['a_m'].replace('u', f'({u_val})')))
                * q_pochhammer(u_val, c['m'])
                for c in atom_data['habiro_coefficients'])
    return total / D

def q_pochhammer(u, m):
    r = mpf(1)
    for k in range(1, m + 1):
        r *= (1 - u ** k)   # <-- NOT (1 - u**(2k))
    return r
```

I verified at q₀: corrected formula gives `tr_M(proton) = 1.0653061442` matching the witness's `tr_M_at_q0 = 1.0653062286` to 6×10⁻⁸ (computational precision at the witness's own dps).

### Bug 2: Lean `habiro_evaluation_determined` proves only `True`

The theorem statement is `True := by trivial` — a placeholder. The actual content (Habiro evaluation matches the witness-cited a_m at q₀) is not formalized.

**Real Lean theorem needed:**
```lean
theorem habiro_evaluation_atomic (atom : AtomData) :
    tr_M atom.braid_word atom.q₀ =
      (∑ m ∈ Finset.range atom.M_max,
        atom.habiro_coeffs m * qPochhammer atom.u₀ m) / atom.D atom.u₀
```
where the witness-cited `habiro_coeffs` are imported via `axiom` (until the Habiro reconstruction algorithm is fully Lean-formalized).

### Bug 3: Q_β closed form from Habiro tr_M not in Lean

Given `tr_M(β_p)`, `tr_M(β_n)` from Habiro, what's the canonical closed-form Q_β? The narrative proposition `prop:neutron-qvalue-symbolic` says Q_β = m_e·|Δ(net)|·E_0, where `Δ(net) = h(h−2)/2` at single-wrap NF. This is **Form A** = 0.78364 (1677 ppm off CODATA).

The **higher-order correction** (the residual to compute precision) needs a Lean theorem that bridges Form A to the exact Habiro Δtr_M. This is the **last 1677 ppm**.

**This is the genuine open derivation step.**

## Two-phase plan

### Phase 1 (low risk, high value): fix Bug 1 + wire production

1. Fix `habiro_exact_qbeta.py` (denominator + Pochhammer).
2. Verify Q_β closes to compute precision via the Habiro path.
3. Wire `per_observable_100x_status.py` to use Habiro evaluation IF and ONLY IF it closes to compute precision at canonical q₀.

If Phase 1's verification shows Habiro Q_β IS compute-precision at canonical q₀, we have a true canonical derivation closing Q_β beyond the 100× target.

If it ISN'T compute-precision (i.e., even the Habiro path has a residual at canonical q₀), then the 1677 ppm gap really IS a structural open problem, and the strict-discipline Q_N2 wiring (current production) is the honest answer.

### Phase 2 (higher risk, longer): formal Lean closure

1. Bug 2: write `habiro_evaluation_atomic` Lean theorem importing witness-cited a_m via class-axiomatised pattern (§3b-cond).
2. Bug 3: derive Q_β = f(tr_M_p, tr_M_n) closed form (Form A is the leading term; the correction is the residual structural object).

Phase 2 is research-grade work; Phase 1 is a 1-day cleanup.

## Recommendation

**Do Phase 1 first.** It's mechanical, verifiable, and may already close Q_β. The current production reports 1247 ppb honestly; if Phase 1 finds Habiro Q_β IS compute-precision at canonical q₀, that's the canonical derivation that locks the dashboard to 7/7 honestly. If it isn't, the 1247 ppb stands as the substrate floor and we've documented why.

Phase 2 (Lean formalization) can follow Phase 1 once we know whether the math closes.

## Past wrong turns to avoid

- **Don't** wire structural conjectures (c_3 = -2, c_3 = J−ℏ_q², c_4 = c_3·b⁴) as derivations. They're q₀-dependent near-matches.
- **Don't** call witness regen "the fix". Witness regens at canonical q₀ shift the empirical c_k targets too — and the residuals reopen.
- **Don't** trust "PROVED" claims in commit messages without checking the Lean. Multiple "prove(1ppQ)" commits added `:= by sorry` or `:= trivial` placeholders, not real proofs.

## Files referenced

- `content/quantum-observable-universe/mass-theory/habiro-expansion-atomic.lean` — real Lean foundation, sorry-free for constant case
- `content/quantum-observable-universe/mass-theory/habiro-ring.lean` — cyclotomic-completion construction
- `content/quantum-observable-universe/braids-and-knots/habiro-precision-ladder-equivalence.lean` — currently scaffolds (3 theorems all `True := by trivial`)
- `computations/habiro/habiro_exact_qbeta.py` — has the bug
- `computations/habiro/habiro-coefficients-atomic.witness.json` — exact integer a_m for p, n, D, ³He, ⁴He
- `computations/per_observable_100x_status.py` — Q_β row currently Q_N2 (honest, post-discipline-lock)

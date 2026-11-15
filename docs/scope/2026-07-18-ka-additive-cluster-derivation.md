# k(A) extensivity via an additive Ursell-cluster derivation (bean qou-7uxa)

> **🛑 CORRECTION 2026-11-15 (tracker #7735, item J) — the −1.38 % / −2.61 %
> agreement does not survive the canonical traces.** Every magnitude quoted in
> this document was computed on typed nucleon traces `1.0653062 / 0.9232333`,
> which are the **retired convention-C** traces (bean `qou-am5t`), not the
> canonical borromean / convention-D / proton-pin traces
> (`atomic-tr-m-mpfr-50dps-proton.witness.json`: `0.6293284022 / 0.4751335172`).
> On the canonical traces, with the live μ targets:
>
> | | pred | target | rel err | 5 % gate |
> |---|---|---|---|---|
> | grounding probe, `(tr_p/tr_n)²` | 1.7544 | 1.3671 | **+28.3 %** | FAIL |
> | lead screen, best of 8 (`sum:inv`) | 1.2067 | 1.3671 | −11.7 % | FAIL |
>
> So the magnitude claim is a **scope-(a) negative**: this construction alone,
> on canonical traces, does not reproduce the T/³He split. What stands: the
> exact reduction to `(tr_p/tr_n)²` (Lean, `BondWeightIsospinSplit.lean`) and
> the correct sign (`tr_n < tr_p`). The fitted exponent is now 1.112, not ≈ 2.
> The text below is kept as the dated record of the analysis.


**Date:** 2026-07-18 · **Discipline:** formalize-first (AGENTS.md §Formalize-first
probe discipline; §Before declaring "refuted"). Different-context attack on the
single open GAP-A-3 gap, authorized parallel to the active #3808 front (owner:
"different context may find solution").

## Why now — the structure is settled additive

Two independent results converge on an **additive** cluster structure:

1. **R11-a (#3808, `263980b2d3`, 2026-07-17):** the 3-factor *multiplicative*
   closure `miss = E(k)·amp(A_light)·parity(k)` is **REFUTED** (the k=2 envelope
   grows with A_light, not separable). Verdict: "honest structure = **additive
   2-channel** (k=3-peaked 3-cluster ⊕ A_light-graded pairwise)".
2. **This session (merged #3841):** the per-knot `p ≠ n` **Mayer b₂** bond weight
   `w(a,b) = 1/(tr_M(a)·tr_M(b))` is a *categorically-grounded* pairwise object —
   the T/³He split reduces exactly to `(tr_p/tr_n)²` (Lean-proved,
   `QOU/MassTheory/BondWeightIsospinSplit.lean`), correct Coulomb sign, −1.38%.
   Grounding note: `docs/coordination/2026-07-17-perknot-pn-bond-resolution-ka-extensivity.md`.

The Ursell cluster expansion `B/m_e = Σ_k b_k` is additive by construction, and
the open magnitude gap is the connected `b₃/b₄`. My grounded b₂ is a concrete
**parameter-free** candidate for #3808's "A_light-graded pairwise" channel — a
*different starting point* (per-knot trace side) for the same additive target.

## The target

μ_ext(K) = B_AME/B_base, targets D 5.85, T 4.44, ³He 3.29, ⁴He 9.31
(`computations/deltalambda/deltalambda-extensivity-gap-synthesis.witness.json`),
non-monotone in A and bonds; ⁴He is the maximum. B_base = m_e·|Σ y_λ χ^λ sgn·dim|
(sign + magnitude closed, #3537).

## The derivation (formalize-first gated)

**Step 0 — cast the two channels additively.** Write the extensivity miss as
`μ_ext − μ_base = C₂(A) + C₃(A)`, with `C₂` the pairwise (b₂) channel and `C₃`
the connected 3-cluster (b₃) channel (⁴He may need `C₄`). Use B_base and the
per-knot traces already on main; no new fitted constants.

**Step 1 — fix the pairwise channel to the grounded b₂ (parameter-free).**
`C₂(A) = Σ_{bonds (a,b)} 1/(tr_M(a)·tr_M(b))` on the p≠n-distinct traces (the
merged, Lean-grounded object). No freedom here.

**Step 2 — read off the residual** $C_3(A) = (\mu_{\text{ext}} - \mu_{\text{base}}) - C_2(A)$
for D/T/³He/⁴He and test whether it is a **clean connected-3-cluster object** — the
connected triple Markov trace (full Mayer/Ursell cumulant, subtracting **both**
the $2{+}1$ and the $1{+}1{+}1$ disconnected partitions)

$$\mathrm{tr}_M(abc)_{\text{conn}} = \mathrm{tr}_M(abc) - \sum_{\text{2+1}} \mathrm{tr}_M(xy)\,\mathrm{tr}_M(z) + 2\,\mathrm{tr}_M(a)\,\mathrm{tr}_M(b)\,\mathrm{tr}_M(c)$$

(the $1{+}1{+}1$ term enters with the standard cumulant coefficient $+2$) — with
the $k=3$-peak structure #3808 found. It must be:
- **bar-EVEN** (I-par gate — the absolute scale is bar-even; a bar-odd residual
  is the p−n channel, wrong object). *Prove parity before fitting.*
- **genuinely connected** (I-conn — not a saturating pairwise product; else it
  is already inside C₂).
- **A-local / vanishing where required** (deuteron has no triple ⇒ C₃(D)=0 must
  be consistent).

**Step 3 — verdict, scope-(a/b).** If the residual is a parameter-free connected
triple trace reproducing the non-monotone μ_ext (crucially ⁴He as the max), that
is a **derivation lead** to verify (with a junk control). If it needs a free
constant or is bar-odd / disconnected, it is an honest scope-(a) negative that
*constrains* the 3-cluster channel — reported to #3808, not fitted.

## Guardrails

No new fitted constant; no BW (adhb gate); no reverse-engineering μ_ext; the b₂
channel is frozen to the merged grounded object. Coordinate with #3808 (post the
residual either way) rather than duplicate their k-ladder compute.

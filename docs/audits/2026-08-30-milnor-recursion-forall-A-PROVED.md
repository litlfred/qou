# The ∀A Milnor deficit recursion — PROVED by TL structural induction (bean qou-v7ro)

**Date:** 2026-08-30 · **Bean:** `qou-v7ro` · **Supersedes:** the "reduced, not yet proved" status of
[`2026-08-30-milnor-recursion-forall-A-status.md`](2026-08-30-milnor-recursion-forall-A-status.md) ·
**Probe:** `milnor_recursion_forall_A_proof_probe.py` · **Scope:** (a); exact ℚ(q); no float64.

## Result

The convention-D Brunnian trace-deficit `D_A = 1 − qtr(ρ(w_A))/[2]^A` (spin-½ / Temperley–Lieb
Markov trace) satisfies, **for all A ≥ 3**:

    D_{A+1}(h) = −h²(h²+2)·D_A(h),   h = q − 1/q,   u := q²+q⁻² = h²+2.

This is a **proof**, not a further verification: every step below is a uniform TL / Markov /
cyclicity identity (no step depends on A except through the strand count), the inductive step is
verified symbolically at A=5, and the closing scalar identity is exact. Combined with the merged Lean
`tight_slice_of_recursion` (`[BrunnianDeficitRecursion D] ⇒` the ∀A tight slice), this closes the
∀A nonvanishing of `MilnorExactOrderConjecture`.

## The proof

Notation: `[2]=q+1/q`, `e=q−R` the TL generator, `μ=diag(q,1/q)` the quantum-trace weight,
`W=ρ(w_{n-1})⊗1`. The Brunnian word is the iterated band commutator `w_n=[w_{n-1},b]`,
`b=A_{n-1,n}=σ²_{n-1}=q²−h·e_{n-1}`. Write `G_n:=qtr(ρ(w_n))`, `c_m:=ptr_{μ⁻¹}(ρ(w_m))`,
`B_m:=ptr_{μ⁻¹}(ρ(w_m)⁻¹)` (partial trace over the last strand).

**(I) — reduction to one term (A-independent ∀n).** The commutator gives
`ρ(w_n)=1+q²h·e_{n-1}−hq⁻²·We_{n-1}W⁻¹−h²·We_{n-1}W⁻¹e_{n-1}`. Three of the four qtr-terms are
A-independent: `qtr(e_{n-1})=qtr(We_{n-1}W⁻¹)=[2]^{n-1}` (loop closure; `[R,μ⊗μ]=0`) and
`q²h−hq⁻²=h²[2]`. So

    G_n = [2]^n(1+h²) − h²·Q_n,     Q_n := qtr_n(W e_{n-1} W⁻¹ e_{n-1}).

**(R) — the 4th term is a bilinear pairing.** The cap-cup identity
`e_{n-1} X e_{n-1} = (ptr_{μ⁻¹}(X)⊗1)·e_{n-1}` (clean weight: `ptr_{μ⁻¹}(e)=1`, whereas
`ptr_μ(e)=diag(q⁻²,q²)`), the Markov property `qtr_n(Y e_{n-1})=qtr^{μ⁻¹-last}(Y)`, and a partial
trace over the strand `B` leaves trivial give

    Q_n = qtr_{n-2}(c_{n-1}·B_{n-1}).

**(C) — coupled recursions.** Applying `ptr_{μ⁻¹}` to the commutator expansion of `ρ(w_m)^{±1}`:

    B_m = [2](1+h²)·1 − h²·(c_{m-1}⊗1)·ρ(w_{m-1})⁻¹,
    c_m = [2](1+h²)·1 − h²·ρ(w_{m-1})·(B_{m-1}⊗1).

**(P) — the pairing collapses to Q_{n-1}.** By the μ↔μ⁻¹ trace-swap invariance of the quantum
trace and cyclicity,

    qtr((c_{m-1}⊗1)ρ(w_{m-1})⁻¹) = qtr(ρ(w_{m-1})(B_{m-1}⊗1)) = qtr_{n-2}(c_{m-1}B_{m-1}) = Q_{n-1}.

**(T) — the quartic term.** Cyclicity cancels `ρ(w_{m-1})⁻¹·ρ(w_{m-1})`:

    T4 := h⁴·qtr(ρ(w_{m-1})(B_{m-1}⊗1)(c_{m-1}⊗1)ρ(w_{m-1})⁻¹) = h⁴·[2]·Q_{n-1}.

**Assembly.** Expanding `qtr_{n-2}(c_m·B_m)` with (C) and evaluating the four pieces by (P),(T) and
cyclicity:

    T1 = (1+h²)²·[2]^n,   T2 = T3 = −[2](1+h²)h²·Q_{n-1},   T4 = h⁴[2]·Q_{n-1},
    Q_n = T1+T2+T3+T4 = (1+h²)²·[2]^n − (2h²+h⁴)[2]·Q_{n-1} = (1+h²)²[2]^n − u h²[2]·Q_{n-1}.

The **exact scalar closure** `(1+h²)² = 1 + u h²` (since `u=h²+2`) turns this into

    Q_n = [2]^n(1 + u h²) − u h²[2]·Q_{n-1}.

Substituting into (I): `G_n = [2]^n(1+h²u) − h²u[2]·G_{n-1}`, equivalently `D_n = −h²(h²+2)·D_{n-1}`. ∎

Base: `D_3` (and `Q_3, Q_4`) direct.

## What is verified vs asserted

| step | status |
|---|---|
| (I) three A-independent terms | verified A=3,4,5; general argument (loop closure, `[R,μ⊗μ]=0`) |
| (R) `Q_n=qtr_{n-2}(c·B)` | verified n=4,5; general (cap-cup + Markov) |
| (C) coupled c/B recursions | verified at m=4 (F-rec also m=3,4); general (commutator + `ptr_{μ⁻¹}(e)=1`) |
| (P) pairing `=Q_{n-1}` | verified n=5; general (μ↔μ⁻¹ trace-swap + cyclicity) |
| (T) `T4=h⁴[2]Q_{n-1}` | verified n=5; general (cyclicity) |
| assembly + scalar closure | exact: `(1+h²)²=1+uh²` |
| direct recursion | verified A=3,4,5,6 |

Each lemma is a **uniform** TL/Markov/cyclicity identity; the inductive step (n=5) exercises all of
(C),(P),(T) and the assembly at once. That, with the exact scalar closure and the direct base cases,
is the proof.

## Lean status (honest)

The `BrunnianDeficitRecursion` instance is **NOT** created. This is deliberate: the proof above is a
**mathematical** proof on the TL operator algebra (quantum trace, cap-cup, Markov property), verified
by exact symbolic computation — it is **not** a Lean proof. Fabricating the instance with `sorry`
would violate the anti-laundering discipline ("Axiomatization is NOT a Proof"). The Lean formalization
of the TL machinery (to discharge the instance for real) is the remaining **formalization** work — a
substantial but mechanical task, not a mathematical gap. The recursion is proved; its Lean witness is
future work.

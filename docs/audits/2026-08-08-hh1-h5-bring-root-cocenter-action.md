# HH¹ at the Bring root — the outer class exists and is trace-visible (2026-08-08)

**Bean:** `qou-jcmw` · **Tier:** compute probe (modular-exact) · **Wired:** nothing.
**No fit, no free parameter, no AME inversion.**

> **🛑 Read [`2026-08-08-hh1-outer-class-bar-parity-prune-does-not-exist.md`](2026-08-08-hh1-outer-class-bar-parity-prune-does-not-exist.md)
> (bean `qou-qb8b`) first.** It landed on `main` earlier the same day and
> already establishes (i) that the bar-parity prune **cannot exist** — parity is
> normalization, not an invariant — and (ii) at `H₃`, that the outer class is
> **not trace-blind** (`tr_M ∘ Δ ≠ 0`), with a pinned trace-paired successor
> showing a nonzero **bar-odd** component. What is new here is narrower than
> the original text below implied: the **dimension count and cocenter rank at
> the actual Bring root `H₅(ζ₅)`** — the piece `qou-qb8b` explicitly left as
> *"remains worth doing"* — plus the finding that it is **cheap** (480 unknowns,
> not the 14 400 that audit estimated). The §3 parity discussion below is
> superseded; see [`2026-08-08-bar-parity-gate-is-vacuous-on-one-dim-hh1.md`](2026-08-08-bar-parity-gate-is-vacuous-on-one-dim-hh1.md) §1.

Runs the falsifiable prune named in
[`2026-08-08-qbeta-l2-assessment-post-week-landings.md` §5](2026-08-08-qbeta-l2-assessment-post-week-landings.md):

> *"compute `dim HH¹(H₅(ζ₅))` at the actual Bring root of unity — bean `qou-jcmw`,
> status `todo`, nobody on it — and test whether the outer class's action on the
> cocenter is bar-odd. If it is bar-**even**, the whole route dies to the same
> bar-parity invariant that killed the real resolvent, cheaply and decisively."*

It was expected to be a cheap kill. **It is not a kill.** Both prunes were
survived; the third is only partially answered, and the honest state is that the
route is still open.

---

## 0. Results

| # | Question | Answer | Rigour |
|---|---|---|---|
| 1 | `dim HH¹(H₅(ζ₅))` | **1** | modular upper bound = 1 (exact); lower bound multi-prime |
| 2 | Does the outer class act on the cocenter `HH₀`? | **Yes, rank 1** on a 7-dim `HH₀` | **exact** (see §2) |
| 3 | Is that action bar-odd? | **Θ-even** under the sign-twisted bar | scope-(a) — **not** a bar-parity result (§3) |

Supporting numbers, stable across `F_5021` and `F_60041`:

```
dim A = 120     dim [A,A] = 113     dim HH_0 = 7
q = zeta_5  ([5]_q = 0, non-semisimple):  dim Der = 114  dim Z = 7  dim HH^1 = 1
q = zeta_10 ([5]_q = 0, non-semisimple):  dim Der = 114  dim Z = 7  dim HH^1 = 1
q = 3       (semisimple control):         dim Der = 113  dim Z = 7  dim HH^1 = 0
```

Producers: [`hh1_hecke_h5_bring_root.py`](../../computations/hh1_hecke_h5_bring_root.py),
[`hh1_h5_cocenter_action.py`](../../computations/hh1_h5_cocenter_action.py),
[`hh1_h5_bar_parity.py`](../../computations/hh1_h5_bar_parity.py).

**Regression.** The general-`n` engine reproduces the merged hand-coded
[`hh1_hecke_outer_derivations.py`](../../computations/hh1_hecke_outer_derivations.py)
exactly at `n = 3` (HH¹ = 0 generic, 1 at `[2]_q = 0`, 1 at `[3]_q = 0`). That
producer's closing note — *"the Bring-specific residue is the H₅ computation
(PROBE A, next step)"* — is the step taken here.

## 1. Why the modular arithmetic is not a hedge

Every matrix entry lies in `ℤ[ζ]` (the Hecke parameter is `a = ζ − ζ⁻¹`), and
reduction along a prime above `p` is a ring homomorphism, so every minor reduces
and `rank_p ≤ rank_0`. Hence

```
dim Der_p >= dim Der_0,   dim Z_p >= dim Z_0  =>  dim Inn_p <= dim Inn_0
=>  dim HH^1_p  >=  dim HH^1_0
```

The modular value is an **upper bound** on the characteristic-0 dimension. Two
consequences, and they point in opposite directions:

- A modular **0** would have *proved* the characteristic-0 value is 0. That is
  the outcome the prune was hoping for, and it did not occur.
- The observed **1** bounds `dim HH¹(H₅(ζ₅)) ∈ {0, 1}` and no more. Two unrelated
  primes agreeing is evidence the bound is attained, not proof.

`dim Z = 7` is independently the expected value (`|Partitions(5)| = 7`, the rank
of the Geck–Rouquier centre basis), which is a consistency check on the engine
rather than a further assumption.

## 2. The trace-visibility result is exact, and it is the substantive one

Inner derivations act as **zero** on `HH₀ = A/[A,A]` (`ad_x(y) = [x,y] ∈ [A,A]`),
so the induced action of an `HH¹` class on the cocenter is canonically attached
to the class — no inner ambiguity. The test is therefore well-posed as stated:

```
D_0 = 0 on HH_0   <=>   D(A) is contained in [A,A]
```

Measured: `rank(D(A) mod [A,A]) = 1`, i.e. **`D₀ ≠ 0`**.

This direction is **exact**, not probabilistic: a containment *failure* is
witnessed by a nonzero minor, and minors only vanish under reduction, never
appear. So non-triviality mod `p` forces non-triviality in characteristic 0.

Since every trace factors through the cocenter
(`QOU/Information/CocenterTraceFactor.lean`), this says precisely:

> **The unique outer derivation of `H₅` at the Bring root is trace-visible — it
> can move `tr_M`.**

This is the `H₅` instance of a mechanism `qou-qb8b` had already established at
`H₃` (`tr_M ∘ Δ ≠ 0`, with the trace-paired number MIXED and carrying a nonzero
bar-odd part). It confirms at the Bring case what was shown on the toy — an
extension, not a discovery. It also closes the degree-mismatch worry the
08-08 assessment raised (c₃ lives in `HH₀`, derivations in `HH¹`): the bridge
`HH¹ ↷ HH₀` is nonzero here, so the two degrees do connect.

## 3. 🛑 What the parity computation does NOT say

The corpus's bar involution is **semilinear**: `q ↦ q⁻¹` together with
`T_i ↦ T_i⁻¹ = T_i − a`. Over a finite field with `q` specialized to a fixed root
`z`, the map `q ↦ q⁻¹` is unavailable — `F_p` has no automorphism carrying `z` to
`z⁻¹` — so **bar does not act on `H_z` at all**; it maps `H_z → H_{z⁻¹}`.

What does act is the composite with the sign twist `σ₋ : T_i ↦ −T_i` (an
isomorphism `H_{z⁻¹} → H_z`):

```
Theta := sigma_- . bar :  H_z -> H_z,     Theta(T_i) = a - T_i
```

verified in the producer to be an involutive `F_p`-algebra automorphism. Measured:
the cocenter action is **Θ-even** on both primes.

**This is not a bar-parity result and must not be recorded as one.** Converting
Θ-parity into bar-parity requires accounting for the sign twist's own
contribution, which needs the semilinear computation over `ℚ(ζ₅)` and is not
done here. Per AGENTS.md §"Before declaring refuted", writing *"the outer class
is bar-even, therefore the route is dead"* on this evidence would be a
scope-(b) structural exclusion asserted without the invariant that licenses it —
the exact failure mode that section exists to prevent. The honest statement is
scope-(a):

> The outer class's cocenter action is even under the sign-twisted bar. Whether
> it is even under bar itself is **open**.

## 4. Net effect on the c₃ front

The prune was proposed as cheap and decisive in either direction. It came back
**alive**, which is the more expensive outcome:

- The route's *source object* exists (`HH¹ = 1`) — not assumed, computed.
- The source object is *trace-visible* (`D₀ ≠ 0`, exact) — so it is not
  disqualified by the cocenter/derivation degree mismatch.
- The *parity gate* is unresolved, and resolving it is now a `ℚ(ζ₅)` semilinear
  computation rather than a finite-field one.

None of this makes c₃ derived, and nothing here touches the 1248 ppb residual.
What it changes is the status of one named lead: it was a candidate to discard
cheaply, and it is now a candidate that has to be worked or refuted properly.

**Still true and unchanged:** the HH¹ modules were built for the P≠NP residue,
not for c₃; nobody has shown the c₃ swing *is* this class; and the substrate
`q₀ ≈ 1.10998` is not a root of unity, so the relevant object remains a
Habiro-ring element evaluated at `q₀` rather than anything living at `ζ₅`
directly. Co-location is still not identification.

## 5. Next honest step — DONE, and the gate turned out to be vacuous

*Superseded same day by
[`2026-08-08-bar-parity-gate-is-vacuous-on-one-dim-hh1.md`](2026-08-08-bar-parity-gate-is-vacuous-on-one-dim-hh1.md).*

The ℚ(ζ₅) computation was run. The gate does not resolve in either direction,
because **bar parity is not a property of a one-dimensional class**: with
`dim_K HH¹ = 1`, `[D^bar] = μ·[D]` forces `μ·σ(μ) = 1`, Hilbert 90 gives
`μ = ν/σ(ν)`, and since `σ(a) = −a` the generators `ν·D` and `a·ν·D` of the *same
line* are respectively bar-even and bar-odd. Verified in exact ℚ(i) arithmetic on
`H₃`.

So §3's caveat was right to refuse the Θ-even reading, but for a stronger reason
than it knew: there is no bar-parity fact to recover. Free corollary — `im(D₀)`
and `ker(D₀)` are automatically bar-stable, since `B·D₀·B⁻¹` is a scalar multiple
of `D₀`.

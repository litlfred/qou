# 𝔙 = Vol + i·CS does NOT reintroduce a Cauchy–Riemann cross-constraint — the keystone-tower separation survives the holomorphy objection (Option-1 closure)

**Date:** 2026-06-19
**Branch:** `claude/admiring-pasteur-ysanxf`
**Goal:** 1ppQ — Q_β; keystone-tower triage (the "do 1 2 3" tranche)
**Disciplines:** *corpus-grep* (the 𝔙 block + Im-cancellation compute + separation
verdict inventoried before declaring anything open), *formalize-first* (a
one-paragraph structural argument forecloses a multi-session search — the forward
complement of corpus-grep), *critical-distance* (this is a **negative** result; it
closes a tempting direction).
**Status:** SYNTHESIS + CLOSURE. No production wiring; no registry tier change; no
new conjecture. Reconciles two corpus results that *appear* to be in tension and
forecloses the "get c₄ from the binding side via Cauchy–Riemann" program.

---

## 0. The tension this doc resolves

Two corpus results sit next to each other and look contradictory:

| result | claim | source |
|---|---|---|
| **§8 unification (2026-06-16)** | binding and Q_β are **Re/Im of one complex volume** `𝔙 = E₀·tr_M((Π_free−1)∘𝓜)`, the QOU analogue of Neumann–Zagier `Vol + i·CS` | [synthesis §8](2026-06-10-qbeta-ck-state-of-play-synthesis.md), [`conj:binding-qbeta-complex-volume`](../../content/quantum-observable-universe/mass-endomorphism/binding-qbeta-complex-volume.md) |
| **separation verdict (2026-06-18)** | the Q_β `c_k` ladder and the binding `Δ_λ` ladder are **distinct** and **do NOT cross-constrain**; the joint `J_ν⊕I_ν` lever is a NO-GO | [`2026-06-18-qbeta-qbessel-vs-zhabiro-binding-tower-separation.md`](2026-06-18-qbeta-qbessel-vs-zhabiro-binding-tower-separation.md) |

The natural worry (raised as the sharpened "Option 1" of the keystone-tower
triage, and the residual the separation doc did **not** address — it argues
*argument-vs-order recurrence*, never *holomorphy*):

> If `𝔙 = Vol + i·CS` is genuinely **holomorphic**, then — exactly as in real
> Neumann–Zagier, where `Vol + i·CS` is holomorphic in the shape parameter —
> **Cauchy–Riemann forces `Re` and `Im` to cross-constrain**. That would
> contradict "no cross-constraint," and would hand us a CR route to the
> below-floor `c₄` from the *better-determined* binding side.

If that worry held, it would **revive** the one-mechanism-both-legs program and
justify a multi-session CR attack. It does **not** hold. This doc shows why, on
four independent grounds, and records the negative consequence.

## 1. The verdict (one line)

**The Neumann–Zagier analogy is structural (one invariant carrying two real
channels), NOT an analogy of holomorphy-in-a-shared-complex-source. `𝔙`'s
complex structure is the *target / bar-involution*, evaluated as two real
observable shadows at two *different* archimedean loci; it is not a single
holomorphic function of one complex observable variable. So there is no
Cauchy–Riemann equation binding the binding channel to the Q_β channel — at the
observable level there is no holomorphic disk at all, and even at the fibre level
CR would act along the q/argument direction (the `c_k` side), orthogonal to the
binding `Δ_λ` *order*-tower. The separation verdict survives; there is no CR
shortcut to `c₄`.**

The two corpus results are therefore **consistent**: `𝔙` unifies the two legs as
*Re/Im of one fibre object with two real shadows*; it does **not** make them
*holomorphically cross-constrained*.

## 2. The four grounds

### (a) The "i" is the bar-involution / target ℂ — not holomorphy in a complex source q

The Lean formalisation
[`QOU.MassEndomorphism.ComplexVolumeUnification`](../../content/quantum-observable-universe/mass-endomorphism/binding-qbeta-complex-volume.lean)
is explicit and sorry-free: the *proofs* live over a generic `{R : Type*}
[CommRing R]` with a ring **involution** `σ` (the bar-involution `q ↦ q⁻¹`).
`σ`-even `x + σx` is binding (bar-even / `cosh`); `σ`-odd `x − σx` is `𝔔_β`
(bar-odd / `sinh`). The unification

```
𝔈_bind + i·𝔔_β = 𝔙          (complex_volume_unification)
```

is **`Complex.re_add_im`** — a definitional reconstruction of a complex number
from its real and imaginary parts — and `ℂ` with complex conjugation is named
*"just the archimedean realisation."* Nowhere is `𝔙` asserted to be a holomorphic
function of a complex variable `q`. The complex structure is **algebraic** (the
involution on a ring; `ℂ` is one instance), not **analytic** (a holomorphic map
`ℂ_q → ℂ`). Cauchy–Riemann is a statement about the latter and has no purchase on
the former: `re_add_im` holds for *every* `z`, with **no** relation between `Re z`
and `Im z` (formalised in §4 below).

### (b) The two channels are read at two *different* archimedean loci

The 𝔙 block's own table assigns the channels to different evaluation points:

| | real part (bar-even, `cosh`, **real q**) | imaginary part (bar-odd, `sinh`, **root-of-unity q**) |
|---|---|---|
| Neumann–Zagier | `Vol(K)` | `CS(K)` |
| QOU | `𝔈_bind` — binding | `𝔔_β` — β-decay |

Binding is the `cosh`/real-`q` evaluation; `𝔔_β` is the `sinh`/root-of-unity
evaluation (`λ ↦ iθ`, `cosh → cos`, `sinh → i sin`). Cauchy–Riemann relates
`Re` and `Im` of a holomorphic function **at one and the same point** of a 2-D
complex neighbourhood. Two channels read at **two different loci** (real axis vs
the unit circle) are not the `Re`/`Im` of one function at one point; there is no
single point at which a CR equation could tie them. This is the precise content
of the block's "`Vol` and `CS` are separately real" — they are two *separately
real* evaluations, not the live real/imaginary parts of one holomorphic germ.

### (c) At the observable level q₀ ∈ ℝ — there is no holomorphic disk

`Im(q₀) = 0` at the archimedean / observable level
(`lusztig_q_0_imaginary_part_zero`, asserted in
[`four_unwired_theorems_regression.py`](../../computations/four_unwired_theorems_regression.py);
the 𝔙 block's "fibre-level caveat (STRICT)"). The measured binding energies and
the measured `Q`-values are **real numbers at real (or root-of-unity) points**.
A function restricted to the real axis has **no** Cauchy–Riemann content — CR
requires a genuine 2-D complex neighbourhood, which the observable evaluation does
not provide. The companion compute
[`vhat_tower_im_cancellation.py`](../../computations/vhat_tower_im_cancellation.py)
makes the same point operationally: fibre-level imaginary parts are legitimate,
but the archimedean observable is forced real **by the τ-functor's Bloch–Wigner
image** (`D(z)` real by the Bloch–Suslin characterisation), *not* by a holomorphic
relation between two observable channels.

### (d) Even granting fibre-level holomorphy, CR acts in the wrong direction

Suppose, generously, that the *fibre* object `𝔙(q)` is holomorphic in a formal /
complex `q` (it may well be — imaginary parts are unconstrained at the fibre level
per CLAUDE.md "Im(q) at fibre vs observable level"). Write `𝔙 = U + iW`,
`U = Re`, `W = Im`. CR then relates the **q-derivatives** of `U` and `W`:
`∂_x U = ∂_y W`, `∂_y U = −∂_x W`. Now line up the two open ladders against this:

- The **Q_β `c_k`** are the Taylor coefficients of the `W` (Im) channel in
  `u_L = b·ℏ_q²` — i.e. **q-derivatives of `W` at the substrate, at a fixed
  knot**. This is the **argument** (q-difference) direction
  ([separation doc §2](2026-06-18-qbeta-qbessel-vs-zhabiro-binding-tower-separation.md):
  `c_{k+1}(1−q^{k+1})(1−aq^k) = −q^k c_k`).
- The **binding `Δ_λ`** are the values of the `U` (Re) channel along the
  **mass-number `A` tower** — the **order** three-term recurrence
  (`a(n+2) = b·a(n+1) − a(n)`, `Δ_λ(K) ≈ q₀^{10A−5}`), **across different knots
  at fixed q**, *not* a q-derivative direction at all.

CR ties `q`-derivatives of `W` to `q`-derivatives of `U` **at the same knot**. So
the most it could deliver is a relation between the `c_k` ladder and the
*q-variation of binding at a single fixed knot* — **not** the `Δ_λ` *tower* (which
is order-indexed across knots, the actual binding frontier). The genuinely open
binding object (`Δ_λ` order-tower, GAP-A / Option-E) lives in the direction CR
does not reach. Holomorphy therefore yields **no** cross-constraint between the
two *frontiers* — precisely the separation doc's "argument ≠ order," now seen from
the complex-analytic side: **CR is an argument-direction (q) relation; the binding
frontier is an order-direction (A) object.**

## 3. Consequence — the both-legs-via-CR program does NOT revive

- **No CR shortcut to `c₄` from binding.** The hoped-for "use the
  better-determined binding side to pin the below-floor `c₄` via Cauchy–Riemann"
  is foreclosed: (b)+(c) remove any observable CR; (d) shows fibre CR, even if it
  holds, reaches only the q-variation of binding at a fixed knot, not the `Δ_λ`
  order-tower. `c₄` stays gated where the corpus already puts it: the **σ₃-lift**
  (Stage C, §[option 2]) / the **fibre-level kernel `R(q,ξ)`** (the keystone).
- **The unification is preserved, correctly scoped.** `𝔙` *is* the right
  bookkeeping — one fibre object, two real shadows, "prove once / read both
  channels" (`invol_descent`, `recurrence_invol_descent`). What it is **not** is a
  holomorphic cross-constraint. The synthesis §8 framing and the separation
  verdict are both right, at their own levels.
- **This is a formalize-first prune.** A one-paragraph structural argument
  eliminates a multi-session CR attack on `c₄` before it is launched — the
  forward complement of the corpus-grep that found the pieces. It joins the
  precedent table (real-q `c_3` impossible; PSLQ entropy bound; argument-vs-order
  separation) of structural arguments that killed a numerical family up front.

## 4. Formal core (Lean, sorry-free)

The precise formal content of ground (a) — *the definitional unification imposes
no relation between the two channels* — is added to the 𝔙 Lean file as
`re_im_independent`:

```lean
/-- The definitional unification `𝔙 = 𝔈_bind + i·𝔔_β` (`re_add_im`) imposes
    **no** relation between the two channels: every pair `(a, b)` of real
    values is realised by some `𝔙`.  This is the formal core of the
    holomorphy-closure audit (2026-06-19): `re_add_im` is a real-linear
    reconstruction, not a Cauchy–Riemann constraint — `Re` and `Im` are
    independent real degrees of freedom, so knowing one constrains the other
    not at all.  (Holomorphy *would* relate them; §2(a)–(d) of the audit show
    no such holomorphy is available where the cross-constraint was hoped for.) -/
theorem re_im_independent (a b : ℝ) : ∃ z : ℂ, z.re = a ∧ z.im = b :=
  ⟨⟨a, b⟩, rfl, rfl⟩
```

Trivial as a theorem; its force is interpretive — it is the exact negation of "CR
ties them." The substantive separation is already carried by the existing
sorry-free Lean: `complex_volume_unification` (definitional), the
argument-recurrence `qbessel_second_order_recurrence`
([`QBesselContiguityRecurrence.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/QBesselContiguityRecurrence.lean))
vs the order-recurrence `two_root_geometric`
([`QLommelOrderRecurrence.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/QLommelOrderRecurrence.lean)).

## 5. Scope / non-claims

- This does **not** prove `𝔙` is non-holomorphic at the fibre level — it may be.
  The claim is that holomorphy, *if present*, does not produce the hoped-for
  cross-constraint between the two open **frontiers** (`c₄` and the `Δ_λ`
  order-tower).
- No tier change, no production wiring, no new conjecture. Q_β stays `c₂`-only in
  production; the `Δ_λ` gate stays Track-A-open.
- Records, for the keystone-tower triage, that **Option 1 (holomorphy gate) is
  CLOSED with a negative verdict** — the both-legs-via-CR program does not revive.

## 6. Cross-references

- [`2026-06-18-qbeta-qbessel-vs-zhabiro-binding-tower-separation.md`](2026-06-18-qbeta-qbessel-vs-zhabiro-binding-tower-separation.md) — the argument-vs-order separation this doc reconciles with §8
- [`2026-06-10-qbeta-ck-state-of-play-synthesis.md` §8](2026-06-10-qbeta-ck-state-of-play-synthesis.md) — the complex-volume `𝔙` unification
- [`conj:binding-qbeta-complex-volume`](../../content/quantum-observable-universe/mass-endomorphism/binding-qbeta-complex-volume.md) + [`.lean`](../../content/quantum-observable-universe/mass-endomorphism/binding-qbeta-complex-volume.lean) — the block + `ComplexVolumeUnification` (`re_add_im`, `invol_descent`)
- [`2026-06-16-hoefsmit-stage-b-attempt-verdict.md` §"reframe via 𝔙"](2026-06-16-hoefsmit-stage-b-attempt-verdict.md) — the "two c₂" as the Re/Im split
- CLAUDE.md "Im(q) at fibre vs observable level" — the fibre/archimedean wall this rests on

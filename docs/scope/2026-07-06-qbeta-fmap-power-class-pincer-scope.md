# Q_β f-map power-class pincer — formalize-first gate (scope)

**Date:** 2026-07-06
**Branch:** `claude/c3-derivation-q-beta-lhsg1a`
**Beans:** `571x` (milestone) + `ebf5`/`pusy`/`zqtv`/`2x2i`
**Owner directive:** "work on bar even ζ₄ and attack f-map" — i.e. the §4.3
formalization target of the
[refuted-class map](../audits/2026-06-04-qbeta-ck-refuted-class-map-and-open-axis.md)
(kernel/f-map constraints: bar-even, ζ₄, √u→u² lift), plus a structural attack
on the surviving non-linear f-map space.

## Discipline check (before anything runs)

- **Registry** ([`ck-dk-canonical-registry.md`](../coordination/ck-dk-canonical-registry.md)):
  no rung tier is touched; nothing is wired. Only c_2 = −1 is canonical; this
  session proposes **no c_k value** (no 7th ansatz, no Φ₂ fit).
- **Refuted-class map §2:** the class attacked here — *pure power maps*
  `f = A·(Δtr_M)^m` — is **not** a member of any refuted row. C13 refuted
  *linear / bar-even-projection* seedings only; the surviving f is known
  non-linear. Power maps are the minimal non-linear class, so they are the
  correct next structural target — **to refute or constrain, not to fit**.
- **C14 / keystone merge note:** this is NOT a new root-of-unity probe (that
  axis merged into the s5-so3 keystone `W_λ` build, bean `s5bb`). The work here
  is constraint-formalization + structural pruning of the f-map class — the
  §4.3 target — and coordinates with, not duplicates, the keystone thread.
- **Overlap with bean `5nx8`** (in-progress, `ComplexVolumeZeta4Partner.lean`):
  5nx8 owns the descent conjecture + the ζ₄-faithfulness class
  (`IsZeta4Faithful`, `SingleFrakVAssembly`). This session **consumes** that
  constraint (cites it, does not edit 5nx8's file) and adds the *character-parity
  prune* it enables on the f-map side. Coordination comment to be posted on the
  5nx8/keystone threads.

## Hypothesis class (§4.1)

Pure power maps `f(Δtr_M) = A·(Δtr_M)^m`, `m ∈ {1,…,6}`, `A` a single scale
normalisation (the C13 protocol — a scale fix is not a fit; anything beyond one
scale is out of scope). Candidate mechanism: `f` lifts the O(√u_L) trace
difference to the ladder rungs `c_k·u_L^k` by raw exponentiation.

## Invariants the class must satisfy (§4.2) — stated BEFORE the probe

Three independent gradings (do **not** conflate; cf. C13 note "bar-even ≠
even-in-ℏ"):

1. **Integer-u grading (unconditional).** The ladder is
   `Q_β/Q_base = ∏_{k≥2}(1 + c_k·u_L^k)` — only **integer** powers of
   `u_L = b·ℏ_q² = O(ε²)`, and **no u¹ rung** (c_1 = 0; PR #1602's
   u¹-cancellation). `Δtr_M = O(ε)` with a full (both-parity) ε-series
   (exact per-block closed forms, witness
   `qbeta-per-block-paper-closed-forms`). Hence:
   - `m` odd ⇒ leading order ε^m = u_L^{m/2} half-integer — **forbidden**;
   - `m = 2` ⇒ leading order ε² = u_L¹ — the forbidden c_1 rung, obstruction
     `[u¹] = a_1² ≠ 0`;
   - `m = 4, 6` ⇒ leading order OK (u_L², u_L³), but every **odd-ε**
     coefficient of `(Δtr_M)^m` must vanish or the half-integer-u obstruction
     fires at sub-leading order. Generic expectation: `[ε^{m+1}] ≠ 0`
     (the a_1^{m−1}·a_2 cross term).
2. **ζ₄ character parity (conditional on the single-𝔙 descent picture,
   `conj:binding-qbeta-complex-volume`).** Per bean 5nx8's Lean-certified
   constraint, any candidate assembly is supported on the two **faithful** ±i
   characters (`IsZeta4Faithful`). A product of `n₊` copies of (+i)- and `n₋`
   of (−i)-eigencomponents transforms with eigenvalue `i^{n₊−n₋}`; it is
   faithful iff `n₊−n₋` is **odd**, i.e. iff the **total degree `n₊+n₋` is
   odd** (same parity). Hence **every even-degree monomial in faithful
   carriers lands in the trivial/sign isotypes — ζ₄-forbidden** unless
   identically zero. In particular the order-permitted `m = 4, 6` powers are
   excluded on this arm.
3. **Bar parity (structural bookkeeping).** The recursion coefficients
   alternate bar-parity when fed bar-odd rates
   (`esymm_bar_parity`, proved in
   [`q-beta-c-k-recursion-from-habiro-q-difference.lean`](../../folio/quantum-observable-universe/mass-theory/q-beta-c-k-recursion-from-habiro-q-difference.lean)).
   Not load-bearing for the pincer; recorded so the three gradings stay
   distinct.

**The pincer:** arm 1 kills `m` odd and `m = 2` outright and generically kills
`m = 4, 6` at the first odd-ε subleading coefficient; arm 2 kills all even `m`
independently (conditionally on the descent picture). If both arms confirm,
the **entire pure-power class dies with zero anchor sweeps** — and the
surviving f-space is sharply characterized: `f` must be **non-monomial**
(odd-degree-supported in faithful carriers per arm 2, with the even-ε ladder
projection arising from a sum/recombination structure, not raw
exponentiation — consistent with the Habiro `(u;u)_m` basis being the natural
home).

## Formalization (§4.3)

Lean, sorry-free, generic base ring per §7c (no gratuitous ℝ/ℂ):

- `pow_eigen`: an eigenfunction `A(σz) = ζ·A(z)` has `A^n(σz) = ζ^n·A^n(z)`.
- `pow_even_not_faithful`: for `ζ² = −1` and `n` even, the generalized
  ζ₄-faithfulness of `A^n` forces `A^n ≡ 0` (orbit/sign-isotype sums collapse
  to `4·A^n`). Generic `(R, ζ, σ)` version + bridge to the concrete
  `IsZeta4Faithful` of `QOU.Mass.ComplexVolumeZeta4Partner` where feasible
  without touching 5nx8's file.

## Probe (§4.4 — only what formalization cannot settle)

`computations/probes/qbeta_fmap_power_class_prune.py` (sympy exact, no
anchors, no fits): reconstruct `Δtr_M(q)` from the exact per-block closed
forms, cross-check the pinned ℏ-Taylor `a_n` (C13 data:
`−5/4, −13/8, −33/16, −77/32, …`), then for `m = 2,…,6` verify the arm-1
obstructions **symbolically** (exact rationals). The probe is a
falsification/verification of stated invariants — it can only confirm or
refute the pincer, never produce a c_k value.

## Deliverables

1. This scope doc (the gate, committed before the probe).
2. Lean character-parity prune lemmas (sorry-free).
3. Probe + witness.
4. Refuted-class map: new row **C15** with verdict; ledger session-log entry;
   coordination comments (5nx8 / keystone threads).

## What this is NOT

- Not a c_3 value proposal. Not a wiring change. Not a root-of-unity scan.
- The registry and production stay untouched.

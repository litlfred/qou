# `w_3` is not closeable by anything in the corpus — it is a rank-2 boundary condition, not a gap

**Date:** 2026-08-29 · **Bean:** `qou-1xne` (spin-offs `qou-vkm6`, `qou-v8qx`) ·
**PR:** [#5967](https://github.com/litlfred/qou/pull/5967) ·
**Probe:** [`computations/w3_closeability_audit.py`](../../computations/w3_closeability_audit.py)
**Subject:** [`conj:binding-manybody-eq-jet-filtration`](../../content/quantum-observable-universe/mass-theory/binding-manybody-jet-filtration.md)
**Builds on (verified, not re-derived):** [`2026-08-26-n3-body-order-forcing.md`](2026-08-26-n3-body-order-forcing.md), bean `qou-hh9q`

## Question

The n=3 forcing audit established that the conjecture's two stated anchors leave
exactly one free parameter and that **A=3 defines the n=3 term rather than
testing it**. That result reproduces on today's `main`
(`binding_n3_forcing_probe.py`, exit 0). The next question is the one it leaves
open: **is `w_3` closeable at all, and by what?**

## Verdict

**Not by anything now in the corpus — and the obstruction is structural, not a
shortage of computation.**

`w_3` is a **required boundary condition of a rank-2 problem**, and the corpus
supplies exactly one boundary condition (n=2, the deuteron bond). This is why
every attempt to derive it from the two anchors fails on *counting* rather than
on precision, and why no amount of further anchor data helps.

The strongest statement is already on `main`, and it is a proper **scope-(b)**
exclusion with its invariant cited —
`QOU.Mass.BindingScalarKernelParityExclusion.no_scalar_kernel_on_carrier`
(sorry-free). The q-Borel-normalized carrier is pure isoclinic of Newton slope
`1/2`; every rank-1 q-difference module has integer slope; equivalently the
cleared q-Riccati's top degrees `1 + 2p` (odd-shaped) and `2u` (even) can never
coincide, since `2u − 2p = 1` is unsolvable over `ℤ`. So **no scalar `R(q,x)`
acts on the carrier at any depth** — the conjecture's own stated mechanism for
producing the weights cannot produce them — and a rank-2 recursion needs **two**
base cases. Its companion `kernel_coeff_existsUnique` (sorry-free) shows that an
unconstrained ansatz *reparametrises* the unknown rather than removing it.

What this audit adds is the measurement that **no other route supplies the
missing base case either**. Four were examined; all four are recorded as
**scope (a)** except where the Lean invariant above applies.

| route | verdict |
|---|---|
| **R1** the period `a_D^(3)` itself | **determined** — and a *different object* from `w_3` |
| **R2** the SL₂ depth-2 recurrence, `τ` | **circular** (consumes `a_D^(3)`), and refuted past n=5 |
| **R3** a third anchor at A>3 | **none exists** under any reading of the tower |
| **R4** the magic form read as the n=4 *term* | determines `w_3` — **negative**, predicting unbound tritium |

All numbers below are mpmath at dps 70 on the proton `q₀` pin; `float()` is
never called.

## R1 — `a_D^(3)` and `w_3` are two gaps, not one

It is natural to suspect that "`w_3` is free" merely restates "`a_D^(3)` is
unknown". **It does not**, and the distinction is load-bearing: collapsing them
would undercount the open work by one.

`a_D^(n) = S(n)/n` with `S(n) = Σ_{λ⊢n} dim_q λ` is a **closed form** in `q` and
`n` — a finite sum of q-hook dimensions over partitions — with no anchor input,
no fitted constant, and no knot argument:

| n | partitions | `a_D^(n)` at the proton pin |
|---|---|---|
| 2 | 2 | 1.0 |
| 3 | 3 | **1.3369656222357** |
| 4 | 5 | 2.5327796563994 |
| 5 | 7 | 5.3761377296793 |
| 6 | 11 | 13.559827125123 |

Its `q→1` limit is the involution number `I(n)/n`, which the corpus already
calls the classical binding period in
[`sw-classical-jet-exactness`](../../content/quantum-observable-universe/brings-surface/sw-classical-jet-exactness.md)
(Lean `involutionNumber_pos`). So `a_D^(3)` is **determined**.

What is not determined is the coefficient in front of it. The conjecture's
*displayed* equation carries no weight at all (`B_n = m_e·a_D^(n)`), and that
reading is refuted at the deuteron:

| iso | `B_pred = m_e·Σ a_D` | `B_AME` | err |
|---|---|---|---|
| ²H | 0.51099895 | 2.224566 | **−77.03 %** |
| ³H | 1.194187 | 8.481821 | −85.92 % |
| ⁴He | 2.4884347 | 28.295661 | −91.21 % |

So the gap is the **weight**, not the period. (This reproduces the forcing
audit's reading-U table to the digit, which is the intended cross-check.)

## R2 — the SL₂ route is circular, and the circularity is measurable

[`prop:sl2-prolongation-recurrence`](../../content/quantum-observable-universe/mass-theory/sl2-prolongation-recurrence.md)
derives `a_D^(n+2) = τ·a_D^(n+1) − a_D^(n)` from `det B = 1` (the Gauss–Manin
monodromy preserving the principal polarisation, hence `B ∈ Sp(2) = SL₂`) and
closes with: *"pinning θ is the last open number of the depth correspondence,
and is solvable from three residue weights via `τ = (a_D^(2) + a_D^(4))/a_D^(3)`."*

That formula is the **n=2 instance of the block's own recurrence, rearranged**,
so it consumes `a_D^(3)` as an input. Measured — substitute anything for
`a_D^(3)` and ask what the recurrence then says about `a_D^(4)`:

| `a_3` substituted | `τ` implied | `a_4` residual |
|---|---|---|
| 1.336965622 | 2.642386309 | **0.0** |
| 0.6684828111 | 5.284772619 | **0.0** |
| 4.010896867 | 0.8807954365 | **0.0** |
| 1.0 | 3.532779656 | **0.0** |
| 0.001 | 3532.779656 | **0.0** |

Zero to full working precision every time. `τ` carries **no information** about
`a_D^(3)`; it is a relabelling of it, so "the last open number" is not pinned by
this route.

Independently, the depth-2 form fails past the anchors it was solved on.
Iterating from the true `a_D^(2), a_D^(3)` with `τ = 2.64238630945`:

| n | recurrence | closed form `S(n)/n` | err |
|---|---|---|---|
| 4 | 2.532779656 | 2.532779656 | 0.0 % *(by construction)* |
| 5 | 5.355616667 | 5.37613773 | −0.38 % |
| 6 | 11.6188285 | 13.55982713 | **−14.31 %** |
| 7 | 25.3458167 | 37.36780738 | −32.17 % |
| 8 | 55.35461055 | 115.8262242 | **−52.21 %** |

This confirms
[`2026-06-25-sw-jet-prolongation-explicit-and-fork.md`](2026-06-25-sw-jet-prolongation-explicit-and-fork.md),
which settled the fork in favour of super-exponential growth and called the
depth-2 SL₂ form *"an n≤4 effective fit"* — a geometric recurrence cannot
produce factorial growth.

**That refutation is not recorded in the proposition block.** Grepped: neither
the fork, nor "super-exponential", nor "effective fit" appears in
`sl2-prolongation-recurrence.md` or its `-proof` sibling, so a reader of the
block alone would take the recurrence as the live prolongation law and `τ` as a
determination. Spun out as **`qou-vkm6`** — this needs *scoping*, not deletion:
the `det B = 1` polarisation argument stands and the form is correct where it
was solved (n ≤ 4).

## R3 — there is no third anchor

### 3a. Full tower — saturated at every order, so never predictive

Each isotope of mass number A supplies one datum **and** introduces one new
unknown `w_A`. The two columns move together:

| through A | unknowns `w_2..w_A` | isotope data | predictions | deficit vs the 2 stated anchors |
|---|---|---|---|---|
| 3 | 2 | 2 | **0** | 0 |
| 4 | 3 | 3 | **0** | 1 |
| 5 | 4 | 4 | **0** | 2 |
| 7 | 6 | 6 | **0** | 4 |

The predictions column is **zero at every order** — every datum is consumed
defining its own weight — while the deficit against the two anchors the
conjecture actually states as derived (n=2, n=4) *grows* with A. The full-tower
reading is separately refuted for A ≥ 5 (`binding_wn_multianchor_tower_refute.py`,
~+920 % at ⁶Li: super-exponential `a_D^(n)` against `B/A → const`).

### 3b. Few-body truncation — strictly worse

The corpus's own redirect is a truncation
`B(K) = m_e·[a_2 w_2 M_2(K) + a_3 w_3 M_3(K)]`. Now `w_2, w_3` are shared, but
each isotope carries its own multiplicity pair: **+1 equation, +2 unknowns**, so
the deficit grows from 3 (one isotope) to 7 (five isotopes).

A truncation therefore helps only if `M_n(K)` is **derived** from the canonical
braid's topology rather than extracted — and that is blocked upstream. The
deuteron's canonical knot/link is **undetermined**: none of the three candidates
is admissible, two excluded by component-count arity and one by AME-inversion
provenance
([`2026-08-21-deuteron-knot-assignment-adjudication.md`](2026-08-21-deuteron-knot-assignment-adjudication.md)).
No canonical braid ⇒ no bond count ⇒ no derived `M_n`.

### 3c. The A=3 mirror pair is a test, not a second equation

At the canonical derived `r₀ = ℏc/m_π`: `E_C(³H) = 0` identically,
`E_C(³He) = 0.84742184` MeV, giving `B_strong(³H) = 8.481821` and
`B_strong(³He) = 8.565480` MeV — a residual split of **−0.99 %**.

Under a **K-independent** `w_n` both partners give the *same* equation
`m_e(a_2 w_2 + a_3 w_3) = B_strong`, so the pair is one equation plus a
consistency test of K-independence; it cannot constrain `w_3` twice. Under a
**K-dependent** `w_n(K)` they are two equations in the two unknowns
`w_3(³H), w_3(³He)` — again no constraint. Either way, no third anchor.

The same argument disposes of the **mirror splitting** as a candidate
observable: under K-independence the model splitting is identically zero, so the
splitting measures the Coulomb model, not `w_3`.

## R4 — the one route that would have supplied a third equation

[`prop:magic-A-binding-formula`](../../content/quantum-observable-universe/mass-theory/magic-A-binding-formula.md)
gives `B = ρ_F·m_e·A·8G` with `ρ_F = 2`, and its own statement reads this as the
nucleus's **total** binding (it is compared to `B_AME(⁴He)` at +5.87 %). But if
it were instead the n=4 **term**, then A=4 would supply *two* independent facts —
the derived term and the measured total — `w_3` would be determined, and A=3
would be left as a genuine prediction. This is the only such route in the corpus.

Tested, with `Vol(L6a4) = 8G = 7.32772475342`, `B_magic = 29.95567728` MeV
against `B_AME(⁴He) = 28.295661` MeV:

| n=2 anchor convention | `w_4` | `w_3` | positivity | monotone | predicted `B(³H)` | bound? |
|---|---|---|---|---|---|---|
| derived bond | 23.145 | **−6.576** | NO | NO | **−1.6600 MeV** | **NO** |
| AME `B(²H)` | 23.145 | −5.686 | NO | NO | −1.6600 MeV | NO |
| derived bond, Coulomb-corrected total | 23.145 | −5.449 | NO | NO | −0.8901 MeV | NO |

The `B(³H)` prediction is **identical** in the first two rows because it reduces
to `B_total(⁴He) − B_magic`, the `w_2` terms cancelling. So the refutation does
not depend on the n=2 anchor convention: it is forced by the magic value
*exceeding* the measured ⁴He total, which leaves a negative remainder for the
n=2 and n=3 terms together.

**Scope (a), and against the *reading*** — not against the magic formula, whose
block reads it as the total. With that reading excluded, no route in the corpus
supplies a third equation.

## What would close it

Not a rearrangement of the two anchors. A genuinely new input:

1. **A per-knot period `a_D^(n)(K)`.** The conjecture *displays* one, but no such
   object exists: all ten `a_D` definitions in `computations/` take body order
   alone and return `S(n)/n`. Building one is the honest route to making n=3 a
   prediction (already recorded as a follow-up of `qou-hh9q`).
2. **A derived multiplicity `M_n(K)`** — blocked on the deuteron knot assignment.
3. **The ramified double cover**, named in the exclusion's own scope note:
   adjoining `q^{1/2}, x^{1/2}` makes the slope the integer 1, and *"a scalar
   kernel does exist on the double cover, relating half-shifts — i.e. even and
   odd body orders separately."* If the odd branch's seed is fixed by something
   already derived, `w_3` closes; if it is another free constant, the route
   renames `w_3` and should be recorded as such. **Untried, and the one route
   nothing measured here excludes** — bean `qou-v8qx`.

A `w_3` obtained by inverting AME at A=3 remains a **fit**, must be labelled one,
and may not be wired to production as canonical. No seventh ansatz is proposed
here, and none should be.

## Side finding — PR #5961 is not on `main`, and does not bear on `w_3`

`QOU.Knot.BodyOrderExpansion` and `esymm_eq_compl_sum` were described to this
session as newly landed. They are not: [#5961](https://github.com/litlfred/qou/pull/5961)
is **open and unmerged**, and neither symbol appears anywhere in the tree at
`main@e9efee94b7`.

Read from the PR head, its content is the elementary-symmetric expansion of the
bond product `∏(X + C d_e)` — the *combinatorial* structure of body orders,
discharging the `body_eq_graded` field that `lem:bond-order-eq-jet-degree`
assumes. It supplies **no magnitude and no weight**, so it **does not bear on
`w_3`**; establishing that was part of this audit's remit, and the answer is
negative. Its own body reaches a compatible conclusion (*"the weights live
elsewhere"*), though it argues from the weightless reading `B_n = m_e·a_D^(n)`,
which is the reading refuted at the deuteron in R1 above — worth flagging to
that branch rather than left implicit.

## Verification

CI auto-triggers are disabled repo-wide, so the agent's own verification is the
gate.

- `w3_closeability_audit.py` **exit 0**; `binding_n3_forcing_probe.py` re-run
  **exit 0** (the prior circularity result still holds on today's `main`).
- **NO-FLOAT64:** mpmath end-to-end at dps 70, `float()` never called, every
  constant via `mpf(str(...))`. Proton `q₀` pin.
- **The Lean claims above are read, not rebuilt.** `no_scalar_kernel_on_carrier`
  and `kernel_coeff_existsUnique` are pre-existing on `main` and are not
  modified here. "Sorry-free" is from source inspection — the only `sorry`
  substrings in that file are the phrase *"sorry-free"* inside its own
  docstring — plus the file's own claim. This session did **not** run
  `lean`-direct or `#print axioms` on it, and that verification belongs to
  whoever landed it, not to this branch.
- `scripts/precision-gates.sh --changed` run. Its reds (`q0-anchor flip`,
  `q0-value drift ratchet`) and the six regenerated audit witnesses are
  **pre-existing on `main`; none of the movement is this branch's** — the new
  probe appears in no diff and emits no witness. Two sibling branches
  (`claude/q0-gates-red-2026-08-29`, `claude/q0-defect-drain-2026-08-29`) are
  actively draining exactly those, so the churn was reverted rather than landed.
- No content blocks, no Lean, no witnesses, no production wiring touched.

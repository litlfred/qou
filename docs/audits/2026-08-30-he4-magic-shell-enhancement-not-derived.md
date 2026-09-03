# The ⁴He magic-shell enhancement is not derived — and the near-match is generic

**Date:** 2026-08-30 · **Branch:** `claude/magic-shell-enhancement-2026-08-30` · **PR:** #6315
· **Bean:** `qou-22vu`

## The question

[`bk-coordination-multiplicity.md`](../../content/quantum-observable-universe/mass-theory/bk-coordination-multiplicity.md)
reads the jet-filtration body-order multiplicity off AME2020 as
`M_need(A) = B_AME/(m_e·Vol_A)`, finds `M_need ≈ z = A−1` for the non-magic A=3 pair to
better than 3 % with no free parameter, and attributes doubly-magic ⁴He an extra
`M_need/z ≈ 2.52 ≈ a_D^(4)`, "the super-exponential Schur–Weyl period" — noting that this
factor over-shoots the A=3 pair by ≈ 30 %, "so it is a magic-shell enhancement rather than
a universal factor".

That 2.52 is the live fitted quantity standing between the jet filtration and a
parameter-free `B(⁴He)`. **Derive it, or establish honestly that it cannot be derived.**

## Verdict

**Not derived, and not currently derivable-and-checkable.** Four findings, in the order
they change what one should believe.

---

## 1. `a_D^(4)` *is* derived — the block's own label is half wrong

The block says the factor "is likewise **an AME read rather than a derived Schur-Weyl
period**". Half of that is backwards, and it is the half that matters.

`a_D^(n) = lw(n−1) = Σ_{λ⊢n} dim_q(λ)/n`
([`theta_wn_kernel_derive_or_refute.py:86`](../../computations/theta_wn_kernel_derive_or_refute.py),
PR #3270) is a Schur–Weyl q-dimension sum evaluated at the substrate q₀. **No AME, no
anchor, no free parameter.** Its `q = 1` limit is the exact rational `I(n)/n`, where `I` is
A000085, the involution numbers (`QOU.Mass.sum_numSYT_eq_involutionNumber`, sorry-free).

Re-measured this session at q₀ = 1.109978582751380807591669 (mpmath at
`set_compute_dps()`, `q = +Q_MP`; exact `Fraction` for the q=1 limits):

| n | `a_D^(n)` at q₀ | exact q=1 limit `I(n)/n` |
|---|---|---|
| 2 | `1.0` | `1` |
| 3 | `1.3369656222357074` | `4/3` |
| 4 | **`2.5327796563993915`** | **`5/2`** |
| 5 | `5.3761377296793154` | `26/5` |

So: `M_need/z = 2.5188914618` is the AME read; `a_D^(4) = 2.5327796564` is derived. What is
**not** derived is the *identification* of the two.

The comparison was already committed on `main` —
[`bk-crossing-coordination.witness.json`](../../computations/bk-crossing-coordination.witness.json)
carries `candidates_z_aD` beside `M_need`. Nothing here needed to be discovered; it needed
to be *read as a test*.

## 2. Because `z·a_D^(A)` is a-priori, it can be tested — and it fails

Zero free parameters means the law is falsifiable on every point, not just the one it was
noticed at.

| isotope | `M_need` | `z·a_D^(A)` | rel err |
|---|---:|---:|---:|
| ³H | `2.00311688` | `2.67393124` | **+33.49 %** |
| ³He | `2.06118960` | `2.67393124` | **+29.73 %** |
| ⁴He | `7.55667439` | `7.59833897` | **+0.5514 %** |

In MeV: `B(⁴He)_pred = 28.4516737527` against AME2020 `28.2956624` — **a miss of
+0.156 MeV**.

**The ≈ 30 % overshoot the block reports is exactly this**: `a_D^(3) = 1.3370` against the
A=3 pair's `M_need/z ≈ 1.00`. It is not a separate caveat; it is the same law being refuted
one value of `A` down.

**And 0.55 % is a discrepancy, not an agreement within errors.** Every input to
`M_need(⁴He)` is known to ≲ 1e-7 relative — AME2020 `B`, CODATA `m_e`, and an exact
hyperbolic volume. There is no experimental slack for 5.5e-3 to hide in. Against the
framework's own L2 target (`σ_pred ≤ σ_exp/100`) it is not close.

**So what the block actually does is *select*.** `z` when non-magic, `z·a_D^(A)` when magic
— one bit of choice between two parameter-free candidates, and ⁴He is the only datum that
selects it. One fitted bit, one point, zero residual constraint. This is the bean
`qou-ebs6` shape ("one parameter, two points, zero out-of-sample support") with the
denominator reduced by one.

## 3. Genericity: the offset is *in range*, not *forced*

AGENTS.md §"Defined residual ≠ derived decomposition" item 2 requires this check before a
near-match is treated as evidence: compute the window and report its width **before**
claiming the feature is evidence for your particular candidate.

Window `M_need/z · (1 ± 0.005514)` = `[2.505003, 2.532780]`, width `0.0278`. Over a
pre-registered parameter-free family of **3996** candidates — balanced q-brackets
`[a]/[b]`, `[a][b]/[c]`, `[a][b]/([c][e])` for indices ≤ 6; rationals `p/r` with `p,r ≤ 24`;
`q₀^k·p/r` for `|k| ≤ 6` — **7 land inside it**:

| candidate | value | gap to `M_need/z` |
|---|---|---|
| `q₀⁵·(3/2)` | `2.52734339537` | **0.336 %** |
| `q₀⁴·(5/3)` | `2.52992208303` | 0.438 % |
| `q₀³·(11/6)` | `2.50717836774` | 0.465 % |
| `a_D^(4)` | `2.53277965640` | **0.551 %** |

**All seven are closer to the AME read than `a_D^(4)` is.** A simpler expression —
`q₀⁵·3/2` — beats it by 1.6×, on the same single datum. The near-match therefore carries
no information favouring `a_D^(4)` specifically, exactly as the `S_leak` offset-window
check found for `c₃ + Vol(4₁)`.

The family was chosen to mirror the one the corpus itself uses for identifications of this
shape (cf. bean `qou-o16k`'s κ-normaliser table: `[2]_q[3]_q`, `[6]_q`, `[2]_q³`, flat 6,
flat 8), and fixed before the hits were inspected.

## 4. Scope-(b): the Wigner-SU(4) route cannot *size* the enhancement

Route 2 of the brief — "⁴He is `[1⁴]` in Wigner SU(4); `dim[1ⁿ] = C(4,n)` vanishes for
n ≥ 5, which the corpus uses to *locate* the A=4 turnover; can the same structure *size*
it?" — is now **structurally excluded**, with a proved invariant rather than a failed
probe.

[`QOU/Mass/WignerSU4RowBoundInactive.lean`](../../content/quantum-observable-universe/lean/QOU/Mass/WignerSU4RowBoundInactive.lean),
sorry-free, `lean`-direct exit 0, `#print axioms` clean on all eight declarations:

- **`rows_le`** — a partition of `n` has at most `n` parts, because every part is ≥ 1.
  *This one lemma is the whole content.*
- **`su4_inactive_of_le_four`** — hence for every `n ≤ 4`, *every* partition of `n` is
  SU(4)-admissible.
- **`su4_restricted_sum_eq`** — hence for every `n ≤ 4`, every weight function `w`, and
  every `AddCommMonoid`, the SU(4)-restricted Schur–Weyl sum **equals** the unrestricted
  one.
- **`su4_no_magic_enhancement`** — stated at `n = 3` and `n = 4` simultaneously: the
  restriction does the same nothing at both.
- **`su4_active_at_five`** — the bound is genuine and first bites at `n = 5`, witnessed by
  the all-ones partition. That *is* the `dim[1⁵] = 0` fact used to locate the turnover.

**The picture this gives is sharp**: the SU(4) row bound is a real constraint that is
inactive *precisely on the range where the enhancement lives*, and becomes active exactly
one step above it. It can mark A=4 as the last admissible order; it cannot attach a number
to it, because below n=5 it does not change any sum whatsoever.

Non-vacuity is checked rather than assumed — an `example` resolves the
`[Fintype (Nat.Partition 4)]` / `[DecidableEq]` binders by instance search, so the
statements apply rather than being conditionally empty.

**Scope of this exclusion is deliberately narrow.** It excludes the SU(4)-row-restriction
route to *sizing*, and nothing else: not other Schur–Weyl functionals, not
non-representation-theoretic consequences of the closed shell, and not the A=3 `z = A−1`
match, which is untouched.

## What blocks a derivation, precisely

Two blockers, of different kinds.

**(B1) `Vol_A` stops at A=4, so the selector has zero out-of-sample support — and cannot
acquire any on this axis.** [`binding_link_volumes.py`](../../computations/binding_link_volumes.py)
assigns links for ²H (Hopf), ³H (8₁₁), ³He (L6a4) and the ⁴He L6a4 base. There is no
nucleus→knot accessor for A ≥ 5; the knot-periodic-table appendix is knot-indexed, not
nucleus-indexed. ²H is degenerate — `Vol(Hopf) = 0` exactly, so `M_need` is undefined there
and the block itself says the coordination count is the non-vanishing replacement.

So the covered range holds **three usable points, of which exactly one is magic**. A
magic/non-magic selector fitted on one point cannot be validated now, and cannot be
validated by more work on this axis — only by extending `Vol_A` past A=4, which is a
different problem (and the block already says the heavier magic nuclei ¹⁶O and ⁴⁰Ca are
α-conjugate clusters, not single hyperbolic links).

**(B2) The 30 % A=3 overshoot consumes the remaining dataset.** With three usable points,
an explanation of the overshoot that costs one further free parameter has spent everything.
Any candidate that must be told `M_need/z` in order to check itself is not checkable here.

## Recommendation (my judgement, not a finding)

**Correct the block's label and leave the physics alone.** Specifically:

1. Say that `a_D^(4)` **is** a derived Schur–Weyl period and that the *identification* with
   `M_need/z` is what is unsupported — the current wording ("an AME read rather than a
   derived Schur-Weyl period") mislabels a derived quantity, which is the more damaging of
   the two possible errors: it invites a future agent to "derive" something already derived
   while leaving the actual gap unnamed.
2. State the miss as **+0.55 %** with the MeV figure, rather than `≈`.
3. Record that the composite rule is a one-bit selection on a single datum, and that the
   genericity window is occupied by closer parameter-free candidates.

I would **not** pursue a seventh candidate for the magnitude. Not because the space is
exhausted, but because **the dataset cannot distinguish candidates**: the window already
contains several parameter-free expressions closer than the named one, and there is no
second magic point to break the tie. Deriving a better-motivated 2.52 would be a real
result *only* if the derivation were fixed entirely a priori and then matched — and the
one candidate that meets that bar, `a_D^(4)`, has been tested and misses.

## What would change this

- **Extend `Vol_A` to a second magic nucleus.** ¹⁶O is the obvious target and is already
  named in the corpus (and in bean `qou-o16k`, for the independent κ question). A single
  additional magic point turns the selector from unfalsifiable into testable.
- **Derive the multiplicity from the jet filtration rather than reading it off.** The block
  collapses `B(K) = m_e Σ_{n=2}^{A} a_D^(n) w_n(K)` into `M_need·Vol_A`; the sum, not the
  collapse, is where a derivation would live. That is the open `w_n(K)` residue-weight
  question (input (3) of the `prop:jet-filtration-binding-extensive` scope note), not this
  one.

## Cross-references

- Producer: [`magic_shell_enhancement_derive_or_refute.py`](../../computations/magic_shell_enhancement_derive_or_refute.py)
  → `magic-shell-enhancement-derive-or-refute.witness.json`, 5/5.
- Lean: `QOU.Mass.WignerSU4RowBoundInactive`.
- Prior art read before starting (corpus-grep paths 1, 2, 3, 4, 6): beans `qou-k4dm`
  (the κ demotion — *"structural motivation attached afterwards does not convert an
  anchor-identified expression into a derived one"*), `qou-o16k` (κ has never met a second
  shell), `qou-ebs6` (the one-parameter/two-points shape), and
  [`2026-08-30-coordination-saturation-formalized.md`](2026-08-30-coordination-saturation-formalized.md).
- The `qou-brng` extensive-term frontier: this is the same intensive/extensive gap seen
  from the multiplicity side.

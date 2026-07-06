# ν_SDP from Markov-trace SDP saturation — the obstruction, and a critical-distance flag (2026-06-21)

**Status:** audit — capstone of the ν_SDP arc (#2552 → #2556). Exploratory, **no fit**.
Discharges the §Critical-distance license duty to flag suspected post-hoc
rationalization plainly. Owner-authorized "first-principles derivation of the
Markov-trace SDP saturation."

## What a first-principles ν_SDP would require

The kashaev block defines `ρ_F = ν_SDP =` *"the dimension of the saturating projection
of T_w's SDP solution in the irreducible-block decomposition `H_n(q) ≅ ⊕_λ
End(V_λ)`"* — a "MacMahon-style partition count" (driver x). A genuine derivation needs
a **canonical, well-posed, encoding-independent** SDP whose saturating projection has
dimension `1, 2, 2` for D, T, ³He **without hand-assignment**.

## The obstruction — no principled saturation yields 1, 2, 2

Every operational route has now been computed and falsified:

| route | D | T | ³He | reproduces 1,2,2? |
|-------|--:|--:|----:|:-----------------:|
| per-block PSD count (#2552) | 1 | 1 | 2 | ✗ |
| operator-selection SDP active-set (#2552) | 7 | — | — | ✗ |
| bar-fold support at H₆/H₉ (#2556) | 1 | 0 | 1 | ✗ |
| self-conjugate count `#sc(3A)` (#2556) | 1 | 2 | 2 | matches, but **mechanism refuted** (bar-fold support ≠ self-conj blocks) |
| **bare SDP saturation, q→1⁺ (well-posed)** | 1 | 1 | 1 | ✗ (single min-cost block) |
| **bare SDP saturation, q₀ (indefinite)** | 0 | 0 | 1 | ✗ (rail-degenerate) |

The last two rows are the new result
([`computations/probes/he_nu_sdp_saturation_obstruction.py`](../../computations/probes/he_nu_sdp_saturation_obstruction.py)
· witness `he-nu-sdp-saturation-obstruction.witness.json`; `y_λ` via Wenzl bridge,
`χ^λ` via `hoefsmit_numpy`):

- **q→1⁺** is the well-posed limit; the program reduces to a min-cost LP whose vertex
  saturates a **single block** (ν=1) for every atom. (Note: negative-norm blocks are
  present at q→1 *and* q₀ — `3/11`, `10/30` — so the indefiniteness is **structural**,
  not a q₀ artifact.)
- **q₀** the Frobenius Gram `diag(tr_M P_λ)` is indefinite, the bare program is
  unbounded / rail-degenerate (the #2552 pathology), and there is no
  encoding-independent saturation. Different Phase-B encodings give different answers
  (bar-fold→1,1,0; conservation→7; AME→consumes the experiment; LR-canonical→rails).

**No principled formulation of the Markov-trace SDP saturation reproduces ν_SDP =
1, 2, 2.** The saturation is either a single block (ν=1) or determined by an external
encoding choice. The confirmed values are recovered **only** by the
`manual-historical-volume-match` hand-assignment.

## Critical-distance assessment (stated plainly, per the standing red-team license)

- **`ρ_F = ν_SDP` is, at present, a *naming* of an underived value, not a derivation.**
  The "MacMahon-style SDP-multiplicity" categorical home is aspirational: across five
  independent operational definitions, none computes `1, 2, 2`. The one combinatorial
  rule that *matches* (`#self-conjugate(3A)`) has its mechanism refuted by the decisive
  H₉ test and predicts `⁴He = 3`, which the binding rejects.
- **`ρ_F = 2` for ⁴He looks fitted.** It is the value that lands magic-A at +5.87% vs
  AME (`ρ_F = 3` → +59%); it is extrapolated, not derived, and no SDP saturation
  produces it. This is a hidden one-parameter degree of freedom dressed in categorical
  language. It should be **labelled an acknowledged input** (CAL-style), not presented
  as a closed structural result, until a genuine derivation exists.
- **This is not a claim the identity is false.** `ρ_F` may well equal a correctly-posed
  ν_SDP that no one has yet defined. But the burden is a derivation that recovers
  D/T/³He without hand-assignment — and the obvious SDP-saturation route is now shown
  obstructed.

## What would constitute a genuine derivation (open)

A canonical regularising principle for the indefinite-Gram SDP that is **not** an
encoding choice — e.g. a representation-theoretic positivity restoration (a *derived*
color-flavor constraint, not the un-vetted 9-pair ansatz) under which the saturating
projection's dimension is computable and equals `1, 2, 2`. None exists in the corpus.
Until then, the ν_SDP / ρ_F line is **open**, and the magic-A ⁴He prefactor is an
acknowledged input.

## The constructive path is obstructed too — the *derived* LR constraint also rails

The one positivity restoration that is **not** an encoding choice — the per-nucleon
**Littlewood–Richardson branching** `H_n ⊃ H_3 × ⋯ × H_3` (the nucleons *are* 3-strand
bundles; the constraint rows are the verified integer LR coefficients, the production
default in `deuteron_real_sdp.py`) — was checked as the natural constructive candidate.
It **does not regularize the program**: for the deuteron the LR-constrained LP is still
unbounded, with four blocks rail-pinned at ±10⁶ `{(2,2,2),(2,2,1,1),(2,1,1,1,1),(1⁶)}`
and only `(3,2,1)=+0.53`, `(3,1,1,1)=−0.41` bounded. The LR rows constrain the trace
but leave the indefinite-Gram null directions free. (Its own production note concedes
the canonical encoding "does **not** yet reproduce the deuteron binding — that closure
is the open Δ_λ gate.")

So **every** derived constraint — bare, bar-fold, and LR-branching — fails to produce a
clean saturation; only the fitted/un-vetted encodings (AME-equality, which consumes the
experiment; the 9-pair ratio, fitted; color-flavor, un-vetted) bound the program, and
none reproduces `1, 2, 2`. The constructive path is obstructed.

## Verdict

The first-principles SDP-saturation derivation of ν_SDP is **obstructed** in every
principled formulation (q→1 well-posed → single block; q₀ indefinite → degenerate; the
derived LR / bar-fold constraints → rail). `ν_SDP = 1, 2, 2` is recovered only by
hand-assignment. Per the §Critical-distance license: **`ρ_F = ν_SDP` is an
underived naming, and `ρ_F = 2` for ⁴He is an acknowledged input that looks fitted**,
not a closed structural derivation — it should be labelled as such until a genuine
positivity-restoration derivation recovering D/T/³He exists. The ν_SDP / ρ_F line is
**open + flagged**.

## Cross-references

- [`2026-06-20-he4-nu-sdp-not-computed-definition-gate.md`](2026-06-20-he4-nu-sdp-not-computed-definition-gate.md) — #2552 (no computed definition).
- [`2026-06-20-nu-sdp-selfconjugate-candidate-and-binding-tension.md`](2026-06-20-nu-sdp-selfconjugate-candidate-and-binding-tension.md) — #2556 (self-conjugate candidate + H₉ refutation).
- [`conj:kashaev-density-equals-sdp-multiplicity`](../../content/quantum-observable-universe/mass-theory/kashaev-density-equals-sdp-multiplicity.md) — the `ρ_F = ν_SDP` identity.
- [`computations/deuteron_real_sdp.py`](../../computations/deuteron_real_sdp.py) — the indefinite-Gram SDP + six Phase-B encodings.

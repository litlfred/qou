# 𝓑_n−𝓑_p brane-tower: the §4a tower-convergence test hits a parity obstruction (2026-06-19)

**Date:** 2026-06-19
**Compute:**
[`bn_minus_bp_brane_tower_parity_probe.py`](../../computations/probes/bn_minus_bp_brane_tower_parity_probe.py)
(witness [`bn-minus-bp-brane-tower-parity.witness.json`](../../computations/bn-minus-bp-brane-tower-parity.witness.json)),
[`h6_deuteron_free_word_chi_lambda_probe.py`](../../computations/probes/h6_deuteron_free_word_chi_lambda_probe.py)
(witness [`h6-deuteron-free-word-chi-lambda.witness.json`](../../computations/h6-deuteron-free-word-chi-lambda.witness.json))
**Status:** derive-or-refute structural result, TIERED. Nothing wired; c₃/Q_β/binding stay cal-anchored.
**Follows:** PR #2485 (first live H₆ deuteron χ_λ; deferred the free reference + the χ_λ(𝓑_n−𝓑_p) difference + the tower test),
[`2026-06-17-jacobi-anger-physical-weight-n3.md`](2026-06-17-jacobi-anger-physical-weight-n3.md) §"The decisive tower test".

## Context — the deferred item-A follow-on

The §4a Jacobi–Anger tower test (doc
[`2026-06-13-reeb-phase-qbessel-identification.md`](2026-06-13-reeb-phase-qbessel-identification.md) §4a,
harness `qbeta_reeb_tower_jacobi_anger_physical_weight.py`) asks whether the bar-odd
brane-tower sector of `χ_λ(𝓑_n−𝓑_p)` is the Hahn–Exton q-Bessel matrix coefficient: its
`sinh((2m+1)η)` coefficients should be `2·J_{2m+1}(x)` at a single substrate-fixed `x`,
with the single-x over-determination residual shrinking toward 0 as the tower extends
`n = 3 → 6 → 9`. At `n=3` the physical-weight residual is **6.8%** on the
Lean-proved closed-form data; the **decisive gate** (per the 2026-06-17 doc, to be run
*before* any `lim spectrum = q-Bessel zeros` master-theorem Lean) is whether it shrinks
at `n=6, 9`.

The 2026-06-17 doc flagged the precise **blocker**: there is no H₆/H₉ `χ_λ(𝓑_n−𝓑_p)`
in the corpus — the explicit proton/neutron braids exist only at H₃ — and producing
them at higher levels is a *first-principles braid construction*, not a mechanical
evaluation. This note runs the formalize-first gate on the single most principled
embedding and reports a clean structural negative.

## The embedding — committed a priori (no scan-to-fit)

Per the formalize-first discipline (CLAUDE.md §"Formalize-first probe discipline"),
one principled embedding is committed **before** any residual is seen — there is no
scan over embeddings selecting the one that converges (that would be fitting the
embedding):

> **Canonical A-nucleon embedding.**
> `β_p^{(A)} = atom_canonical_crossings(A, 0, include_inter=False)` (A free protons),
> `β_n^{(A)} = atom_canonical_crossings(0, A, include_inter=False)` (A free neutrons),
> level `n = 3A`; difference object `χ_λ(β_n^{(A)} − β_p^{(A)})`, `λ ⊢ n`.

Rationale: it is the literal `A → A` generalization of the *same* canonical
word-builder that reproduces the Lean-proved H₃ closed forms at `A = 1` (intra-only,
matching the single-nucleon convention); `level = 3A` matches the brane-tower /
Hecke-level structure used throughout (`mass_at_3A_proper`, the n=6,9 levels the
2026-06-17 doc itself names).

## Results (exact symbolic Hoefsmit engine)

### 1. n=3 validates the pipeline

`χ_λ(β_n^{(1)} − β_p^{(1)})` reproduces, symbolically and exactly:
- the three Lean-proved closed forms
  (`chi-per-irrep-cyclotomic-closed-forms.lean`): `χ_(3)=-(q²+1)²(q²-1)/(4q)`, etc.;
- the canonical n=3 `BAR_ODD_COEFFS` `{(3):{3:-¼,5:-¼}, (2,1):{1:½,3:-½}, (1,1,1):{3:-¼,5:-¼}}`;
- the §4a physical-weight single-x residual **6.84%** at `x*≈4.5249` (matches the
  harness on `main`).

### 2. The conjugation invariant is parity-graded

Under conjugation `λ → λ'`, the bar-odd coefficient vector satisfies a single
level-wide sign relation `bar-odd(χ_{λ'}) = s·bar-odd(χ_λ)` with `s = (−1)^{A−1}`:

| level | A | sign s | example |
|---|---|---|---|
| n=3 | 1 | **+1** | `bar-odd(1,1,1) = +bar-odd(3)`; self-conj `(2,1)` keeps nonzero bar-odd |
| n=6 | 2 | **−1** | `bar-odd(1⁶) = −bar-odd(6)`, `bar-odd(2,2,2)=−bar-odd(3,3)`; self-conj `(3,2,1)` forced to **zero** bar-odd |

The sign **itself flips with A-parity** — a second, independent parity grading on top
of the order-parity alternation in §3. (It is a structural invariant, not refuted: the
canonical embedding satisfies it exactly at both levels with the predicted sign.) The
`s=−1` grading at n=6 forces every self-conjugate `λ` to vanishing bar-odd part, which
is part of why the odd-order tower content collapses there.

### 3. 🔴 The parity obstruction (the decisive finding)

The bar-odd **order-parity alternates with A**:

| level | A | bar-odd orders present | parity |
|---|---|---|---|
| n=3 | 1 | {1, 3, 5} | **odd** |
| n=6 | 2 | {2, 4, 6, 8, 10, 14, 16} | **even** |
| n=9 | 3 | (odd, cheap-subset confirmed) | **odd** |

The §4a Jacobi–Anger backbone is **odd-order only**:
`sinh(x·sinh η) = 2 Σ_{m≥0} J_{2m+1}(x)·sinh((2m+1)η)`. The companion
`cosh(x·sinh η) = J_0(x)+2Σ_{m≥1} J_{2m}(x)·cosh(2mη)` carries even orders but as
**cosh**, not sinh. So even-order *sinh* terms appear in **neither** expansion — no
single-x Jacobi–Anger form represents them.

Consequently, at `n=6` the odd-order tower coefficients `W₁ = W₃ = W₅ = 0` **vanish
identically** (every `λ ⊢ 6` contributes only even orders, and the `y_λ`-weighting
cannot create odd orders from even-order components). The §4a single-x solve
`W₃/W₁ = J₃(x)/J₁(x)` is therefore **0/0 — undefined**, not "shrinking" or "growing".

## Reading (TIERED)

1. **The naive tower extension does not work.** "Extend `χ_λ(𝓑_n−𝓑_p)` to `λ⊢6` via
   more nucleons and re-run §4a" — the obvious reading of the 2026-06-17 blocker,
   which expected odd orders up to 11 at n=6 — fails on a **parity obstruction** for
   the canonical same-type-nucleon embedding. This is a *proved* structural fact
   (exact symbolic), not a numerical near-miss.

2. **The blocker is sharpened, not closed.** A valid brane-tower embedding for the
   §4a q-Bessel tower must **preserve odd order-parity** across levels — extend
   `{1,3,5}` to `{1,3,5,7,9,11,…}` — which same-type nucleon stacking does **not**
   (its parity flips with A, and the A-even levels carry even-order sinh the odd
   Jacobi–Anger form cannot host). Candidate parity-preserving constructions (a
   single-nucleon braid *iterate* `β_p^k` on 3 strands; an odd cabling; a genuine
   brane-tower contraction map) are the genuine open work — but each must be derived,
   not chosen for convergence.

3. **This does not refute the §4a keystone itself.** The keystone is about the *true*
   brane-tower object, whatever it is. The finding refutes one candidate embedding and
   pins a necessary condition (odd-parity preservation) the true embedding must meet.
   `c₃`/Q_β stay cal-anchored regardless.

4. **Free-word χ_λ delivered.** The deuteron free reference (`include_inter=False`) at
   H₆ is now materialised alongside the #2485 bound χ_λ (bound values reproduce #2485
   exactly), with the per-partition `Δχ_λ` and Wenzl-weighted single-trace tr_M. The
   single-trace binding `B≈0.47 MeV` under-predicts AME 2.225 — expected; the per-
   isotope Δ_λ closure is the separate open frontier (CLAUDE.md §"Δ_λ gate").

## Winding iterate (item 2): the parity-preserving candidate, also refuted

**Compute:** [`bn_minus_bp_winding_iterate_probe.py`](../../computations/probes/bn_minus_bp_winding_iterate_probe.py)
(witness [`bn-minus-bp-winding-iterate.witness.json`](../../computations/bn-minus-bp-winding-iterate.witness.json)).

The natural next candidate is the **single-nucleon winding iterate** `β^k` on the same
3 strands — `β_p^k = atom_canonical_crossings(1,0,…)` concatenated `k` times, `β_n^k`
likewise. It stays in H₃ (`λ ⊢ 3` only) and raises the Laurent degree with `k`, so it
*can* reach high orders {7,9,11,…} without leaving the 3-strand setting.

**The root cause, now exact.** The Hoefsmit seminormal factors are degree-±1 in `q`,
so `χ_λ(word)` has Laurent-exponent parity `= (word length) mod 2`. The nucleon word
has **odd length (11 crossings)**, so:

| construction | length | parity of orders |
|---|---|---|
| winding `β^k` (H₃) | `11k` | `k mod 2` — alternates |
| A-nucleon strand tower (n=3A) | `11A` | `A mod 2` — alternates |

So **both** towers alternate parity for the *same* reason: an odd-length base word
repeated an integer number of times flips parity every step. This unifies the §3
obstruction with the winding case — it is not specific to "more nucleons", it is the
crossing-count parity.

**The odd-k subtower does not converge.** Restricting to odd `k` (where parity *is*
preserved, orders odd and filling {1,3,5,7,…}) gives the honest §4a convergence test.
The single-x over-determination residual does **not** shrink:

| k | word length | §4a single-x residual (max over orders ≥5) |
|---|---|---|
| 1 | 11 | 6.84% |
| 3 | 33 | **no single-x solution** near the Bessel ratios |
| 5 | 55 | ~100% |
| 7 | 77 | erratic (3426%) |

A genuine Hahn–Exton q-Bessel tower would shrink monotonically toward 0. This is a
clean **refutation** of the winding iterate as the §4a object.

**Combined verdict.** The §4a keystone's two most natural first-principles
embeddings — the A-nucleon strand tower and the single-nucleon winding tower — are
**both refuted**, under one root cause (odd base-word length ⇒ parity alternation). A
valid odd-parity-preserving tower would need **even-length** increments that still
inject new odd-degree content — which neither integer-repeat construction provides.
This neither closes nor refutes the §4a keystone itself (the *true* embedding, if any,
is neither of these two), but it removes the two obvious candidates and pins the
structural condition any survivor must meet.

## Discipline

- **Formalize-first.** The bar-involution + order-parity invariants were extracted
  symbolically and pruned the test *before* any expensive H₉ scan — exactly the gate
  the 2026-06-17 doc asked for "before any master-theorem Lean". Full p(9) symbolic
  is deferred (expensive and moot given the n=6 obstruction); only a cheap parity
  check was run at n=9.
- **No fit; single embedding committed a priori; nothing wired; TIERED.**
- **Corpus-grep clean** — the H₆/H₉ `χ_λ(𝓑_n−𝓑_p)` genuinely did not exist (the n=6
  hits were all `computations/_deprecated/`); this is the first live higher-level
  datum, and it is a structural negative on the obvious embedding.

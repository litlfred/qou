# ν_SDP derivation attempt — self-conjugate count candidate + the ⁴He tension (2026-06-20)

**Status:** audit — exploratory, **no fit**. Owner-authorized "derive ν_SDP"
follow-on to [`2026-06-20-he4-nu-sdp-not-computed-definition-gate.md`](2026-06-20-he4-nu-sdp-not-computed-definition-gate.md)
(#2552, which established ν_SDP has no computed operational definition).

## The lead

The kashaev block defines ν_SDP categorically as *"the dimension of the saturating
projection in the irreducible-block decomposition `H_n(q) ≅ ⊕_λ End(V_λ)`"* — a
"MacMahon-style partition-algebra count" (driver x). Two concrete observations:

1. **The principled bar-fold SDP gives a clean single-block support for D.** Of the
   six Phase-B encodings in [`deuteron_real_sdp.py`](../../computations/deuteron_real_sdp.py),
   only the **bar-involution fold** (§7b Type-B folding — the symmetry regulariser
   with *no invented weights*) is non-degenerate: its solution puts all occupation
   on the single block **(3,2,1)** = tr_M(β_D). The others rail to ±10⁶. And (3,2,1)
   is the **unique self-conjugate partition of 6**.
2. **The self-conjugate count matches every confirmed atom.**

> **candidate:  ν_SDP = #{ self-conjugate λ ⊢ 3A } = #{ partitions of 3A into
> distinct odd parts }**  (the classic Euler/MacMahon identity — exactly a
> "MacMahon-style partition count").

| atom | (Z,N) | n=3A | #self-conj | ν_confirmed |
|------|-------|-----:|-----------:|------------:|
| D | (1,1) | 6 | 1 | 1 ✓ |
| T | (1,2) | 9 | 2 | 2 ✓ |
| ³He | (2,1) | 9 | 2 | 2 ✓ |
| **⁴He** | (2,2) | 12 | **3** | — *(predicts)* |
| ⁶Li | (3,3) | 18 | 5 | — |
| ⁷Li | (3,4) | 21 | 8 | — |

T and ³He are both n=9 with ν=2, consistent with ν depending only on n=3A.

## Why it is NOT (yet) a derivation — two problems

**(1) The mechanism is refuted.** The justification that would make this a theorem
was: under the bar-fold, every conjugate pair `(λ,λ')` cancels in the Frobenius Gram
(`tr_M(P_λ) + tr_M(P_λ') = 0`, the §7b "sign-flip" signature), leaving only
self-conjugate blocks with definite norm. The actual H₆ Gram (the `frob_diag` of the
deuteron witness) **does not cancel** — every conjugate-pair sum is nonzero, e.g.
`tr_M(6) + tr_M(1⁶) = +0.059`, `tr_M(4,2) + tr_M(2,2,1,1) = +0.359`. The
negative-norm "forbidden" blocks `(3,1,1,1), (2,2,1,1), (1⁶)` are *small-negative*,
not the equal-and-opposite of their positive conjugates. So the deuteron bar-fold
landing on (3,2,1) is **not** explained by a self-conjugate-cancellation mechanism;
the count match lacks a derivation.

**(2) It conflicts with the ⁴He binding.** The candidate predicts `ν_SDP(⁴He)=3`,
but the magic-A binding `B = ρ_F·m_e·A·8G` needs `ρ_F=2` (`ρ_F=3` gives **+59%** vs
AME; `ρ_F=2` gives +5.87%). So under `ρ_F = ν_SDP`, the cleanest combinatorial rule
matching D/T/³He **contradicts** the ⁴He binding. Either `ν_SDP ≠ #self-conj`, or
`ρ_F ≠ ν_SDP` at the doubly-magic ⁴He. Both leave `ρ_F=2` unconfirmed — consistent
with #2552.

## Verdict

**Not a derivation.** A candidate count that matches all three confirmed atoms *and*
the deuteron bar-fold support, but with (i) no proven mechanism (the cancellation
hypothesis is refuted on the real Gram) and (ii) a direct conflict with the ⁴He
binding. The two-distinct-value match (n=6→1, n=9→2) is weak evidence on its own.

**Decisive test — RUN (2026-06-21), and it REFUTES the candidate.** Computed the T and
³He bar-fold SDP supports at H₉ (pipeline: `y_λ` via Wenzl bridge, `χ^λ(β)` via
`hoefsmit_numpy` + `atom_canonical_crossings`, bar-fold LP; validated by reproducing
the deuteron support {(3,2,1)} first):

| atom | n | self-conj | bar-fold **bounded** support | ν_canon |
|------|--:|-----------|------------------------------|--------:|
| D | 6 | {(3,2,1)} | **{(3,2,1)}** → 1 | 1 ✓ |
| ³He | 9 | {(5,1⁴),(3,3,3)} | **{(5,1⁴)}** → 1 (4 others ±10⁶ rails) | 2 ✗ |
| T | 9 | {(5,1⁴),(3,3,3)} | **∅** → 0 (all 8 entries railed) | 2 ✗ |

`|bar-fold support|` = (1, 1, 0) **≠** ν = (1, 2, 2). The bar-fold regularises *only*
the deuteron; at A≥3 the indefinite-Gram unboundedness returns (rail-pinned conjugate
pairs — the #2552 pathology), so the support does **not** equal the self-conjugate
blocks. The count match was **coincidence**. A weaker fact survives: the bounded support
is ⊆ self-conjugate blocks (but not all of them, and empty for T). **The self-conjugate
avenue is closed; ν_SDP derivation remains open.**

Probes: [`he_nu_sdp_selfconjugate_candidate.py`](../../computations/probes/he_nu_sdp_selfconjugate_candidate.py),
[`he_nu_sdp_barfold_h9_test.py`](../../computations/probes/he_nu_sdp_barfold_h9_test.py)
· witnesses `he-nu-sdp-selfconjugate-candidate.witness.json`, `he-nu-sdp-barfold-h9-test.witness.json`.

## Note on the (1+q)/2 thread

The adjacent "categorical (1+q)/2 binding wiring" is **already settled as a refuted
near-match** (PR #1707; bean `cbnf`): "0.11%" was a stale muon-anchor literal, at
canonical q₀ it is +0.12% sign-flipped, and four structural hypotheses were killed.
The bean explicitly directs *not* to re-attempt (1+q)/2 (a v10 ansatz = the fit-trap
the discipline forbids). The live non-fit direction is **GAP-A-3** `Δ_λ(K)=A(K)·P_λ(K)`
(A derived, `P_λ` open) — distinct from this ν_SDP/ρ_F line.

## Cross-references

- [`2026-06-20-he4-nu-sdp-not-computed-definition-gate.md`](2026-06-20-he4-nu-sdp-not-computed-definition-gate.md) — #2552, the parent finding.
- [`conj:kashaev-density-equals-sdp-multiplicity`](../../content/quantum-observable-universe/mass-theory/kashaev-density-equals-sdp-multiplicity.md) — the driver-x "MacMahon partition count" definition.
- [`computations/deuteron_real_sdp.py`](../../computations/deuteron_real_sdp.py) — the six Phase-B encodings (bar-fold = encoding 1).

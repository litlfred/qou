# §3b edge-audit: mass-endomorphism chapter (11 gaps)

Per-block determination of whether each §3b-cond gap is a **real
logical dependency** (→ add conditional banner + Lean `[Class]`
hypothesis) or a **spurious / backwards `uses[]` edge** (→ correct
the edge) or the block is **itself a conjecture** (→ demote).

Method: shortest `uses[]` path from each gap block to the conjecture
in its cone, then read the content to judge the edge.

## Findings

| Block | Path to conjecture | Verdict | Action |
|-------|--------------------|---------|--------|
| `prop:mass-endomorphism` | direct → `conj:knot-factor-frobenius-pairing` | **DEMOTE** — this block IS the mass-endomorphism conjecture (file `mass-endomorphism-conjecture.ts`); its `.md` lacks a "**Conjecture**" opener but it is open per its own Scope section | relabel `prop:`→`conj:mass-endomorphism`, update consumers |
| `prop:markov-trace-axiomatic-closed-form` | → hecke-markov-transition → q-pochhammer-partial-product → `conj:kashaev-volume-conjecture` | **SPURIOUS** — the axiomatic Markov-trace closed form is pure Hecke algebra; it does not depend on the Kashaev volume conjecture. The culprit is the `q-pochhammer-partial-product → kashaev-volume-conjecture` edge (a formal q-product cannot depend on a hyperbolic-volume conjecture; the Kashaev limit *uses* the q-Pochhammer, not vice versa) | remove the `kashaev-volume-conjecture` entry from `q-pochhammer-partial-product` uses[] |
| `prop:markov-trace-recursive-reducer` | → markov-trace-axiomatic-closed-form → … → kashaev | **SPURIOUS** (inherits the same bad edge) | fixed by the q-pochhammer edge correction |
| `prop:markov-trace-antipode-polynomial-symmetry` | → markov-trace-axiomatic-closed-form → … → kashaev | **SPURIOUS** (same) | fixed by the q-pochhammer edge correction |
| `prop:atomic-mass-gb-nf` | → rho-k-graded-expansion → conj-rho-k-pair-gen-canonical-form → q-integer-mass-formula | **SPURIOUS/backwards** — the GB normal form is upstream algebra the mass formula consumes; the `rho-k-graded-expansion → conj-rho-k-pair-gen-canonical-form` edge encodes "is refined by", not "depends on" | re-examine that edge; likely drop or redirect |
| `prop:qbeta-c-k-closed-forms` | direct → `conj:knot-factor-frobenius-pairing` | **REAL** — the c_k closed forms are computed via the Frobenius-pairing recovery `y_λ = ⟨K_n, e_λ⟩` that the conjecture asserts | add banner + Lean `[KnotFactorFrobeniusPairing]` |
| `prop:categorical-chain-convergence-mechanisms` | direct → `conj:knot-factor-frobenius-pairing` | **REAL** (same machinery) | add banner + class |
| `prop:categorical-neutrality-saturated-shells` | direct → `conj:knot-factor-frobenius-pairing` | **REAL** | add banner + class |
| `prop:homological-shell-condensation` | direct → `conj:knot-factor-frobenius-pairing` | **REAL** | add banner + class |
| `prop:hecke-baer-star-generic` | → … → `conj:gb-depth-period-correspondence` | **REVIEW** — Baer-star is algebraic infrastructure; likely spurious via a gb-depth edge | trace + judge |
| `prop:explicit-central-idempotent` | → … → `conj:bring-figure-eight-depth-2-witness` | **REVIEW** — central idempotents are pure Wedderburn algebra; likely spurious | trace + judge |

## Summary

| Verdict | Count | Discharge |
|---------|-------|-----------|
| REAL dependency | 4 | banner + Lean class hypothesis |
| SPURIOUS edge | 4 | correct one `uses[]` edge (fixes 3 via q-pochhammer) |
| DEMOTE (is a conjecture) | 1 | relabel + consumers |
| REVIEW | 2 | trace remaining path |

## Takeaway for the full 123

The mass-endomorphism sample shows the gaps are **roughly half spurious
edges, half real conditionals**, with occasional mislabeled conjectures.
Blind banner-stamping would have asserted false dependencies on ~half.
The full discharge is a per-cluster `uses[]` audit + targeted banner
additions — author-reviewable, not mechanical. One high-value fix
(`q-pochhammer-partial-product` losing its spurious kashaev edge)
discharges 3 gaps at once and likely many more across other chapters
that route through the same q-Pochhammer block.

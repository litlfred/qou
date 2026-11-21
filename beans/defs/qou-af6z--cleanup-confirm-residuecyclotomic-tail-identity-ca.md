---
# qou-af6z
title: 'Cleanup: confirm residue↔cyclotomic-tail identity carries OPEN banner (not ''proved'') in all siblings; add missing where absent'
status: todo
type: task
priority: normal
tags:
    - alien-habiro
    - reorg-2026-10-04
    - needs-owner
created_at: 2026-07-18T17:09:31Z
updated_at: 2026-11-21T12:35:00Z
parent: qou-j5ch
---

habiro-residue-sum-equivalence.md correctly says 'analytic identification of the residue contributions with the cyclotomic tail remains open' and machine-ε agreement is 'empirical witness' only. Verify siblings that cite/depend on it (full-pole-structure-mass-trace, gb-residue-spectral-sum, mass-endomorphism tower, tau-M blocks) do NOT upgrade the empirical machine-ε agreement to a proved analytic identity ('sorry-free ≠ derived' discipline). Grep + read; flag any that state it as proved. Verification pass.

## 2026-11-21: verification pass done, two flags (hecke-gs-conj sibling, session_01Qmmkt5sJX34MCerjRMERJN)
Read-only pass on main 2ae54ab40. Searched every `folio/**/*.md` that links `habiro-residue-sum-equivalence` or names the residue / cyclotomic-tail identity. The source block keeps its OPEN banner (`habiro-residue-sum-equivalence.md:30-31`, "The analytic identification of the residue contributions with the cyclotomic tail remains open"; machine-precision agreement labelled "Empirical witness").
Siblings that keep the scope: `gs-spectral-decomposition-existence.md:12` (conjectural, names the missing bridge), `gs-residue-at-root-existence.md:12`, `full-pole-structure-mass-trace-proof.md:31-38` (calls the residue sum a symbolic feeding lemma, not a global identity), `borromean-h4-categorical-derivation-context.md:10` (shares a framework only).
Flagged, upgrade the empirical agreement to an established result:
1. `mass-theory/phi-q-markov-residue-habiro-intro.md:1`: "This section … **establishes the equivalence** between the algebraic topological mass formula and the Habiro residue sum." Should say the equivalence is stated, with the analytic identification open and machine-precision agreement as the evidence.
2. `mass-endomorphism/tau-M-asymptotic-rep-theory-interpretation.md:23`: "this reproduces the N=1 coupling b **through the residue-sum equivalence**", which uses the open identity as an input without a conditional.
Also worth an owner look: the block's label kind is `prop:` while its own body says the identification is open; a `conj:` label or an explicit conditional statement would match.
Not edited: both are `.md` content edits (sidecar refresh + render-QA, and the label change is a rename). The fix is corpus-derived (the source block itself says open), so it qualifies for the ask-first exemption 2, but I left it for whoever owns the mass-theory prose. Left `todo` with the flags above.

Premise check vs `docs/coordination/owner-rulings.md` (main 2ae54ab40, 2026-11-21, owner request to drop old results): no superseded premise in the flagged text. The Borromean context block it touches already uses χ^{(2,1)} = 2 − 3h⁴ − h⁶ (current).

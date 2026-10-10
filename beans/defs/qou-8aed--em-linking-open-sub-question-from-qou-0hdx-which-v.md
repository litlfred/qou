---
# qou-8aed
title: 'EM-linking open sub-question (from qou-0hdx): WHICH volume enters the Freedman-He Vol^{-1/3} template for a proton-PAIR energy — the whole nucleus (Vol ~ A, 6.10% scatter) or the proton subsystem (Vol ~ Z, 5.17%)? Four points cannot discriminate; Z is physically defensible since the pp Coulomb domain is arguably the proton subsystem. Resolved by the same mirror-pair extension as qou-i6rg (A and Z decouple more strongly at higher A) or by deriving the template''s domain from the corpus braid geometry'
status: scrapped
type: task
priority: normal
created_at: 2026-08-01T21:03:34Z
updated_at: 2026-09-02T21:41:58Z
---

## SCRAPPED 2026-09-02 — unanswerable as posed: the template it asks about does not exist

This bean asks *which* volume enters "the Freedman–He `Vol^{-1/3}` template" for a
proton-pair energy — the whole nucleus (`Vol ~ A`, 6.10% scatter) or the proton
subsystem (`Vol ~ Z`, 5.17%).

**There is no `Vol^{-1/3}` in the Freedman–He link bound.** Verified against the
primary source `library/arxiv-0808.1533v1/sections/sec-001-energy-bound.md:203-216`
(Komendarczyk eq. 43, p. 26): the prefactor is `(pi/16)^{1/4}`, a pure constant, with
no volume factor of any kind. The `Vol^{-1/3}` is **Khesin Thm 3.6**, the bound for a
*single knotted torus*, misapplied to a multi-component configuration — the
misattribution recorded in Round 5 of
[`docs/audits/2026-08-01-em-linking-reads-round1.md`](docs/audits/2026-08-01-em-linking-reads-round1.md)
and in `computations/em-linking-fh-link-bound-correction.witness.json`.

So the A-vs-Z discrimination this bean proposes would be choosing between two
readings of a factor that is not in the theorem. The 6.10% / 5.17% scatter figures
in the title are measurements of a **bare power-law fit with no literature backing**,
not of a template — `H_FH_A` and `H_FH_Z` both revert to that status.

**Not deleted, re-scoped.** The measurements stand
(`computations/em-linking-crossing-number.witness.json`); only their warrant was
wrong. If the volume question is wanted for some other reason it needs re-posing
against a bound that actually carries a volume.

Parent `qou-0hdx` is scrapped the same day; its body carries the full verification
and names the one live successor (derive the per-component flux law — eq. (43)'s
topological factor is A-independent, so it relocates κ(A) into the flux rather than
explaining it).

---
# qou-2pp7
title: Cross-check 9811173v1.pdf at computations/binding_link_volumes.py
status: completed
pr: 8347
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:36:38Z
updated_at: 2026-11-21T14:58:49Z
parent: qou-8hur
---

Cross-check the corpus's computed link/knot hyperbolic volumes against the published a/b rational invariants for the same complements. This is a cross-check only: any agreement corroborates, and no external number may be adopted into a witness on the strength of a match.

**From the source**
- abstract (the a/b formula) + the census tables — For a hyperbolic 3-manifold whose invariant trace field has a single complex place, the volume equals a rational multiple a/b of a normalised Dedekind zeta value at 2 for that field; 152 distinct such zeta values are identified across the censuses, with 91 manifolds having volumes reducible to pairs of them.
  Use here: A published table of volume-to-zeta rational invariants to cross-check the corpus's link/knot volume computations and the Bring-natural number fields of the depth correspondence against.

Source: `library/arxiv-hep-th-9811173v1/9811173v1.pdf` — no `references.ts` entry yet
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/arxiv-hep-th-9811173v1/  ->  [broadhurst1998]
  Determinations of rational Dedekind-zeta invariants of hyperbolic manifolds and Feynman knots and links

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [broadhurst1998] as the citation key when you do it.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8347, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

## 2026-11-21T14:58:49Z cross-check result

Probe computations/probes/broadhurst_dedekind_zeta_volume_probe.py (branch claude/expo-cite-xcheck-wave2-2026-11-21, head 06a66eeb823). ALL PASS. No external number was adopted into any witness.
- Broadhurst's Z_K (eq ZK, via PARI zeta_K(2)) and his quadratic Clausen form (eq ZKq) agree to 60 digits for D = -3, -4, -7.
- The source's a/b = 1 (4_1, 5^2_1) and a/b = 2 (6^3_1) are reproduced with SnapPy volumes to 1e-60.
- Corpus binding-link-volumes witness: Vol_B3_8G = 8G gives a/b = 1/2 against Z_4 (rel 1.6e-17, limited by its 15 digits), and SnapPy L6a4 gives it exactly. The witness's 8_11 volume matches SnapPy to 10 digits.
- 8_11 (the witness's 3H knot): its shape field is degree 10 with 5 complex places. Broadhurst's single-complex-place formula does not apply, so his tables cannot cross-check that volume.
Harness note: cypari's Python-level lfun returns only ~19 digits regardless of realprecision, so the probe uses the string call. Documented as an amendment.
Premise finding: the witness's binding rows assign vol_eff = Vol(B3) to the deuteron (Hopf, Vol 0) and use census picks 8_11 and L6a4. AGENTS.md records owner ruling A (2026-08-29: the deuteron binding is not a volume term) and the 2026-09-05 retirement of census selection. That witness's binding rows therefore rest on superseded premises. Its volumes are correct.

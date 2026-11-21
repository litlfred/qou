---
# qou-u800
title: Remark interpreting 1202.4698.pdf at rem:q-dilogarithm-pentagon-associator
status: in-progress
pr: 8412
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-09T00:10:51Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-vva9
---

rem:q-dilogarithm-pentagon-associator asserts the dilogarithm-associator-6j identification without a semiclassical anchor. A remark can record that in the modular double the b -> 0 limit of the 6j symbol is a hyperbolic tetrahedron volume, and must state the applicability check: the tetrahedra are non-ideal (six free dihedral angles), so this does not by itself supply Vol(4_1) or any ideal-triangulation volume the corpus uses -- what would need checking is the ideal limit of eq (3.3).

**From the source**
- Sec 3.1-3.2, eqs (3.1)-(3.4) and (3.10)-(3.11) — The b-6j symbol has b -> 0 saddle-point asymptotics exp(W_pm(A)/(2 pi i b^2)) with W_pm(A) = U(z_pm, A) + Delta(A) - (5/3) pi^2 -+ 2 pi^2 phi, whose imaginary part is the tetrahedron-volume formula (3.3) quoted from its ref [MY, Thm 2]; the potential U(u, A) is an alternating sum of eight dilogarithms in the dihedral-angle variables A_k = exp(i eta_k), and the saddles are the two roots of dU/du = -2 pi i / u.
  Use here: The explicit associator-to-volume computation behind the identification rem:q-dilogarithm-pentagon-associator states structurally ('the quantum dilogarithm is the quantum associator, equivalently the 6j-symbol'). Cite it there as the modular-double realisation, together with the caveat that the tetrahedra are non-ideal, so the QOU ideal-triangulation volumes are a limit of this family and not an instance of it.

Source: `library/arxiv-1202.4698v3/1202.4698.pdf` — no `references.ts` entry yet
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/arxiv-1202.4698v3/  ->  [terashima-yamazaki2013]
  6j symbols for the modular double, quantum hyperbolic geometry, and supersymmetric gauge theories

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [terashima-yamazaki2013] as the citation key when you do it.


## Implementation Progress (PR #8412)
- Formalized in `folio/quantum-observable-universe/lean/QOU/QBeta/ModularSixJNormalSurfaceTripleLinkingRound69.lean` (wired into `folio/quantum-observable-universe/lean/QOU.lean`).
- Verified at 80-dps precision in `computations/probes/round69_modular_sixj_normal_surface_triple_linking_probe.py` with 2-commit witness `computations/probes/round69-modular-sixj-normal-surface-triple-linking.witness.json`.
- PR: https://github.com/litlfred/qou/pull/8412 (`ready: 83afa66fc31cdd276e7404f29767f2f41edefe60`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8412, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

## 2026-11-21 — cite-remarks bean drain (thread "Interpret citation remarks", issue litlfred/qou#8806)

rem:q-dilogarithm-pentagon-associator: semiclassical anchor citing terashima-yamazaki2013 (authors Teschner-Vartanov; key retained) §§3.1-3.2 eqs. (3.1)-(3.4), (3.10)-(3.11), with the non-ideal-tetrahedron applicability check.

Done on branch `claude/cite-remarks-2026-11-21` at 3b2491716; status stays in-progress until that branch merges.
Owner-ruling check (docs/coordination/owner-rulings.md, main 2ae54ab40): no superseded premise found; this is a citation item and touches none of the photon, electron, trace, convention, chi or T(2,n_s) rulings.

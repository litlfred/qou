---
# qou-985x
title: 'Extended Bloch group route: flattening supplies the canonical log-branch A1 lacked'
status: in-progress
pr: 8212
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-07T08:53:01Z
updated_at: 2026-10-04T15:19:03Z
parent: qou-r9ih
---

Owner steers 2026-08-07: 'should depend on knot' + 'sibling is using extended Bloch group'. Both land on the same object. A1 was killed by the ROAST because 'take the log / do not normalize' is a one-parameter family (branch-of-log ambiguity) => picking a member is a fit. Neumann's extended Bloch group resolves EXACTLY that: flattened shapes [z;p,q] with p,q in Z recording log z + p*pi*i and -log(1-z) + q*pi*i, FIXED by the gluing/parity equations, not chosen. R-hat descends to Vol + i*CS exactly (ordinary Bloch only gives CS mod pi^2/6). Converts A1 from unfalsifiable to derivable. Satisfies all three constraints: additive (sum over ideal tetrahedra BY CONSTRUCTION), super-pairwise (a tetrahedron has 4 vertices; the proved rho_A <= C(A,2) cap bounds PAIR counting, not tetrahedron counting), knot-dependent (Vol+iCS vs the bare normalization N^(n-1) which depends only on strand count). Bridge already in corpus: volume conjecture lim (2pi/N) log|<K>_N| = Vol. Corpus: Kashaev 760 files, volume conjecture 199, complex volume 148, Neumann 230, flattening 36, but 'extended Bloch' in ONE file. OWNER RULING: hyperbolicity of the light-nucleus closures is ASSUMED GRANTED ('assume it is there and work from there') -- caveat 1 stands down, work proceeds from there.


## Progress Update (2026-11-16T21:42:42Z)
- Implemented machine-checked Lean 4 theorem in `folio/quantum-observable-universe/lean/QOU/QBeta/ExtendedBlochFlatteningAndGaussianCell.lean` and 80-dps `mpmath` / exact rational witness `computations/probes/extended-bloch-flattening-and-gaussian-cell.witness.json`.
- Opened PR https://github.com/litlfred/qou/pull/8212 (`6f86defb7b9ef2d83e38ac9d5dd375a7109fbabd`); keeping `status: in-progress` until PR merges.

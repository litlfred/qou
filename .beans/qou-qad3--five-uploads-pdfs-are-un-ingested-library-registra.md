---
# qou-qad3
title: Five uploads/ PDFs are un-ingested — library/ registration backlog is no longer zero
status: in-progress
type: task
priority: high
created_at: 2026-08-24T14:07:59Z
updated_at: 2026-08-24T17:30:12Z
---

`qou-9ep0` recorded the library backlog as **drained to zero**: "every library
document now has a references.ts entry". That is no longer true. Five PDFs sit
in `uploads/`, **none** in `library/` (381 entries) and **none** referenced from
any `.ts`.

## The five, identified

| file | what it is |
|---|---|
| `0105186v2.pdf` | **Seidel, _A long exact sequence for symplectic Floer cohomology_**, arXiv:math/0105186v2 [math.SG], 71pp — added 2026-08-24 (`94594bf`) |
| `2111.12409v4.pdf` | Dolce & Zucconi, _On the generalisation of Roth's theorem_, arXiv:2111.12409v4 [math.NT] |
| `2605.19310v1.pdf` | Lewko, _A Fourier-free density-increment proof of Roth's theorem_, arXiv:2605.19310v1, 10pp |
| `noniterativeroth2.pdf` | Croot & Sisask, _A proof of Roth's theorem on arithmetic progressions_, 5pp |
| `roth_lemma.pdf` | book chapter, _Roth's Lemma_ (the polynomial index lemma), 21pp |

## TWO different Roth theorems — do not conflate

This is the trap in this batch and it is easy to walk into:

- **Diophantine approximation** (Thue–Siegel–Roth): `roth_lemma.pdf`,
  Dolce–Zucconi. Roth's *Lemma* is the polynomial-index lemma from that proof.
- **Additive combinatorics** (3-term APs in dense sets): Lewko, Croot–Sisask.

Same surname, unrelated statements. Any `references.ts` entry or citation that
says only "Roth's theorem" is ambiguous and should name which.

## Why they are not ingested

`scripts/migrate-uploads-to-library.py` is the **one-shot historical migration**
that renamed the whole intake tree; it is not the per-file route. The ongoing
path is folio-assistant `scripts/pdf-structure.py` → `library/<doc-id>/`
(`structure.json`, `sections/*.md`, `candidates.json`) → `references.ts` entry
via `library-propose-references.py` / `sync-references-library.py`.

## Environment blocker, and the workaround

`pdf-structure.py` needs `pypdf`, and this container has neither it nor
poppler. `pip install pypdf` succeeds but importing it **panics**: the
debian-installed `cryptography` 41.0.7 rust binding raises
`pyo3_runtime.PanicException`, and it cannot be uninstalled ("RECORD file not
found, installed by debian").

Workaround that works — stub the module before importing pypdf:

```python
import sys, types
for n in ["cryptography", "cryptography.hazmat", "cryptography.hazmat.bindings",
          "cryptography.hazmat.bindings._rust", "cryptography.hazmat.primitives"]:
    sys.modules.setdefault(n, types.ModuleType(n))
import pypdf   # 6.16.2, works
```

pypdf uses cryptography only for encrypted PDFs, so the stub is safe for these
five. Worth putting in `pdf-structure.py` behind a try/except, or the ingestion
step is blocked in every fresh container.

Ingestion half done on branch claude/mt7r-archimedean-eval-2026-08-24 (2026-08-24).

All **nine** flat PDFs are now ingested, not five — four more arrived in aa17903e09f (Smith 1006.1099v3, Pascaleff 1109.3255v2, Chanda 2301.08311v4, McLean ICM-2022 ch.5483) while this bean was open. `ls uploads/*.pdf` is now empty.

Each has library/<doc-id>/ with all five artefacts (PDF moved by git mv so history survives, structure.json, sections/, candidates.json, summary.json); INDEX.md regenerated; summarize-library.py --check exits 0. 460 formalisation candidates extracted across the nine.

**Your Seidel identification is confirmed** — and it was nearly lost. pdf-structure.py extracted its title as "Along exact sequence for symplectic Floer cohomology Paul Seidel": the space in "A long" was eaten and the byline ran into the title, so the paper the LES arc most wants would not have been found by searching INDEX.md for "long exact sequence". 8 of the 9 titles were wrong the same way — one predicate, folio-assistant bean gx86 has the taxonomy. All nine corrected as data against page 1; a pdf-structure.py re-run reverts them until gx86 is fixed.

**Still open, and it is the half this bean names:** none of the nine has a references.ts entry yet, so the library↔bib join is still broken for them. Ingestion makes them greppable and citable; it does not register them as sources.

Assessment of the four Floer papers for the qou-fngs arc is in docs/curved-dq-and-the-floer-cluster.md — the cluster is method, not content, and acting on it produced QOU.DqTwist.dq_sq_eq_curvature the same day.

---
# qou-qad3
title: Five uploads/ PDFs are un-ingested — library/ registration backlog is no longer zero
status: todo
type: task
priority: high
created_at: 2026-08-24T14:07:59Z
updated_at: 2026-08-24T14:07:59Z
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

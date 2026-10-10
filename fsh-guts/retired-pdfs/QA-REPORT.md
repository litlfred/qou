# Retired library PDFs: QA report

Copied from `litlfred/qou` `main` at `ee2b758144e4f96d003163ed3cbba93eaaa59d09`, checked 2026-10-10T18:29:40Z.

Owner, 2026-10-10: *"dont delelte the already download pdfs, put in fsh-guts (with a QA report). we still need to test for a bit."*

**Nothing has been removed from `main`.** This branch holds a second copy of every processed library PDF, so the removal from `main` can be tested and reversed. Each file sits at its `main` path under `fsh-guts/retired-pdfs/`, and is byte-identical (the same git blob).

## What was checked, per PDF

- **sha256**: the file's sha256 equals `source.sha256` in its entry's `structure.json`, so the derived sections are known to come from these bytes.
- **processed**: `sections/` holds at least one `.md`, so the text was extracted.
- **locator**: where a reader can get the paper without this copy (arXiv id, DOI, or neither).

## Counts

| | |
|---|---:|
| PDFs | 718 |
| bytes | 637,196,210 |
| sha256 matches and processed | 716 |
| sha256 does NOT match the record | 2 |
| unprocessed | 0 |
| arXiv locator | 526 |
| DOI only | 63 |
| no public locator | 129 |

For the 129 with no public locator, this branch and `main`'s history are the only copies.

## Findings

### The file is not the one its entry recorded (sha256 mismatch)

The sections in these entries were extracted from a different file than the one now present. Re-ingest before relying on the pairing.

| entry | file present | file recorded |
|---|---|---|
| `arxiv-1107.1559v1` | `1107.1559.pdf` | `1107.1559v1.pdf` |
| `arxiv-math-0405508v1` | `math0405508.pdf` | `0405508v1.pdf` |

### Same bytes, different filename

The sha256 matches, so these are the recorded files under another name, usually a browser's `(1)` suffix. Harmless, but `structure.json` names a file that is not there.

| entry | file present | file recorded |
|---|---|---|
| `arxiv-0802.1072v2` | `0802.1072v2.pdf` | `0802.1072v2 (1).pdf` |
| `arxiv-1202.5547v1` | `1202.5547v1 (1).pdf` | `1202.5547v1.pdf` |
| `arxiv-1406.7337v4` | `1406.7337v4.pdf` | `1406.7337v4 (1).pdf` |
| `arxiv-2406.05311v1` | `2406.05311v1.pdf` | `A_quantum_Murnaghan--Nakayama_rule_for_the_flag_ma.pdf` |
| `arxiv-math-0606435v2` | `0606435v2.pdf` | `0606435v2 (1).pdf` |

## Machine-readable

`qa.json` beside this file: one row per PDF with path, git blob, bytes, sha256, the recorded file and sha256, arXiv id, DOI, section count, whether the LaTeX source and licence records exist, and the verdict.


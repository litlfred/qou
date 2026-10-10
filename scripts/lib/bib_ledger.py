"""Read this folio's two bibliography judgement ledgers — the Python twin of the
platform's ONE reader, `folio-assistant/cat-harness/schemas/bib-attestations.ts`.

Since C9 stories B3/B4 (2026-10-05) the ledgers live in the attestation store,
one file per reference:

    test/attestations/bib-verification/reference/<ref id>.attestations.json
    test/attestations/bib-verification/source/<file>.attestations.json   (rows with id: null)
    test/attestations/bib-human-review/reference/<ref id>.attestations.json

and the old single files (`folio/bib-qa-verifications.json`,
`folio/schema/references.review.json`) are gone. The rules are the
platform's, restated here only because qou's Python scripts cannot import a
TypeScript module:

* the store's family directory present  -> read it, rows ordered by `position`;
* absent, legacy file present           -> read the legacy file and SAY SO;
* neither                               -> an empty ledger, and say so.

A store file that does not parse, names the wrong family, carries a
`verifier: "unknown"` marker that disagrees with its row, or repeats a
position raises `BibLedgerError`: a reader does not answer past a judgement it
cannot read.

This module only READS. The writers are the platform's (`writeSourceLedger`,
`writeHumanReviews`). `python3 scripts/lib/bib_ledger.py --parity` compares
this reader with the platform's (via `migrate-bib-attestations.ts --export`)
and exits 1 on any difference.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys

SUFFIX = ".attestations.json"
SCHEMA = "qa-attestations/v1"
LEDGER_HEADER = {
    "_schema": "source-ledger/v1",
    "_authoritative_for": (
        "Source document <-> reference join, source-verification status, and "
        "relevance triage. Bibliographic metadata lives ONLY in "
        "folio/schema/references.ts; this file stores no title, author, "
        "year, or DOI."
    ),
}


class BibLedgerError(RuntimeError):
    pass


def _declaration(repo: str) -> dict:
    for name in sorted(os.listdir(repo)):
        if not name.endswith(".json") or name.endswith(".config.json"):
            continue
        try:
            d = json.load(open(os.path.join(repo, name), encoding="utf-8"))
        except (OSError, ValueError):
            continue
        if isinstance(d, dict) and isinstance(d.get("directories"), list) \
                and os.path.splitext(name)[0] == d.get("name"):
            return d
    return {}


def attestations_root(repo: str) -> str:
    """The declared `attestations` directory, else the convention `test/attestations`."""
    for d in _declaration(repo).get("directories", []):
        kinds = d.get("graphTypologies") or d.get("graphKinds") or d.get("graphs") or []
        if "attestations" in kinds and isinstance(d.get("path"), str):
            return os.path.join(repo, d["path"].rstrip("/"))
    return os.path.join(repo, "test", "attestations")


def _files(fam_dir: str) -> list[str]:
    out = []
    for root, _dirs, names in os.walk(fam_dir):
        out += [os.path.join(root, n) for n in names if n.endswith(SUFFIX)]
    return sorted(out)


def _load(path: str, family: str) -> dict:
    try:
        d = json.load(open(path, encoding="utf-8"))
    except (OSError, ValueError) as e:
        raise BibLedgerError(f"bib attestation store unreadable at {path}: {e}") from e
    if not isinstance(d, dict) or d.get("$schema") != SCHEMA or d.get("family") != family:
        raise BibLedgerError(f"bib attestation store corrupt at {path}: not a {SCHEMA} {family} file")
    return d


def _ordered(rows: list[tuple[int, str, object]]) -> list[object]:
    rows.sort(key=lambda r: r[0])
    for a, b in zip(rows, rows[1:]):
        if a[0] == b[0]:
            raise BibLedgerError(f"bib attestation store corrupt: position {a[0]} held by both {a[1]} and {b[1]}")
    return [r[2] for r in rows]


def read_source_ledger(repo: str) -> tuple[dict, str]:
    """(ledger dict with `_schema`, `_authoritative_for`, `entries`; note naming its home)."""
    fam = os.path.join(attestations_root(repo), "bib-verification")
    legacy = os.path.join(repo, "folio", "bib-qa-verifications.json")
    if os.path.isdir(fam):
        files = _files(fam)
        rows: list[tuple[int, str, object]] = []
        for p in files:
            for rec in _load(p, "bib-verification").get("verifications", []):
                entry = rec.get("entry")
                if not isinstance(entry, dict) or not isinstance(rec.get("position"), int):
                    raise BibLedgerError(f"bib attestation store corrupt at {p}: malformed record")
                unknown = entry.get("verified_by") is None
                if unknown != (rec.get("verifier") == "unknown"):
                    raise BibLedgerError(f"bib attestation store corrupt at {p}: `verifier: unknown` disagrees with the row")
                rows.append((rec["position"], p, entry))
        entries = _ordered(rows)
        note = (f"source ledger: {len(entries)} row(s) from the attestation store "
                f"({os.path.relpath(fam, repo)}, {len(files)} file(s))")
        if os.path.exists(legacy):
            note += f"; the legacy {os.path.relpath(legacy, repo)} is still present and was NOT read"
        return {**LEDGER_HEADER, "entries": entries}, note
    if os.path.exists(legacy):
        led = json.load(open(legacy, encoding="utf-8"))
        return led, (f"source ledger: read from the LEGACY file {os.path.relpath(legacy, repo)} — "
                     "the attestation store has no bib-verification family yet")
    return {**LEDGER_HEADER, "entries": []}, "source ledger: none — no attestation store family and no legacy file"


def read_human_reviews(repo: str) -> tuple[dict, str]:
    """(reference id -> review, in recorded order; note naming its home)."""
    fam = os.path.join(attestations_root(repo), "bib-human-review")
    legacy = os.path.join(repo, "folio", "schema", "references.review.json")
    if os.path.isdir(fam):
        files = _files(fam)
        rows: list[tuple[int, str, object]] = []
        for p in files:
            d = _load(p, "bib-human-review")
            rid = (d.get("subject") or {}).get("id")
            for rec in d.get("reviews", []):
                rows.append((rec["position"], p, (rid, rec["review"])))
        reviews = dict(_ordered(rows))  # type: ignore[arg-type]
        note = (f"human reviews: {len(reviews)} from the attestation store "
                f"({os.path.relpath(fam, repo)}, {len(files)} file(s))")
        return reviews, note
    if os.path.exists(legacy):
        return (json.load(open(legacy, encoding="utf-8")).get("reviews", {}),
                f"human reviews: read from the LEGACY file {os.path.relpath(legacy, repo)}")
    return {}, "human reviews: none — no attestation store family and no legacy file"


def _parity(repo: str) -> int:
    script = os.path.join(repo, "folio-assistant", "cat-harness-tools", "scripts", "migrate-bib-attestations.ts")
    if not os.path.exists(script):
        print(f"parity: SKIPPED — the platform reader is not reachable at {script} "
              "(run scripts/setup-folio-assistant.sh)")
        return 2
    bad = 0
    for what, mine in (("verification", read_source_ledger(repo)[0]),
                       ("review", read_human_reviews(repo)[0])):
        r = subprocess.run(["bun", "run", script, "--repo", repo, "--export", what],
                           capture_output=True, text=True)
        if r.returncode != 0:
            print(f"parity: platform export of {what} failed: {r.stderr.strip()[-400:]}")
            return 2
        theirs = json.loads(r.stdout)
        same = json.dumps(mine) == json.dumps(theirs)
        print(f"parity {what}: {'identical' if same else 'DIFFERENT'}")
        bad += not same
    return 1 if bad else 0


if __name__ == "__main__":
    REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    if "--parity" in sys.argv:
        sys.exit(_parity(REPO))
    led, n1 = read_source_ledger(REPO)
    rev, n2 = read_human_reviews(REPO)
    print(n1)
    print(n2)

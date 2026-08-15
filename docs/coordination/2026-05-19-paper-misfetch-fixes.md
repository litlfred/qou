# Paper-Misfetch Items — Suggested Fixes

Per the bib-audit summary (`docs/coordination/2026-05-19-bib-audit-summary.md`)
and the user's "Address 5 deferred paper-misfetch items" pick from
the 🟡 multi-select. These items can't be auto-fixed; they need
either a content-side decision or a live network lookup.

## 1. `margolus1998` — URL fixed, awaiting re-fetch

**Status**: `paper-mismatch` in `content/bib-qa-verifications.json`.

**Problem**: My initial arxiv ID `cond-mat/9710043` was wrong category.
Correct id: `quant-ph/9710043` (Margolus-Levitin "The Maximum Speed of
Dynamical Evolution"). URL already fixed in `references.ts` commit
`87b9771ac`.

**Fix** (on your machine):
```bash
bash scripts/upload-bib-papers.sh --force   # uses --force I added in a3c0784c1
# OR equivalent:
rm library/margolus1998.pdf && bash scripts/upload-bib-papers.sh
```
**Cost**: 0 mental, 1 network round-trip.

## 2. `turaev2010` — URL removed, no action needed

**Status**: `partial` (no PDF; URL removed in commit `a3c0784c1`).

**Problem**: Turaev's "Quantum Invariants of Knots and 3-Manifolds"
is a de Gruyter monograph with no arxiv preprint. My `q-alg/9409028`
search hit was a phantom.

**Fix**: Already applied — URL removed; entry's DOI
`10.1515/9783110221831` (paywalled landing page) is the only resolver.
The 25 turaev2010 `-- Ref:` citations now carry title+publisher;
sufficient without a local PDF.

**No action needed.**

## 3. `zink2002` — Wrong numdam chapter URL

**Status**: `paper-mismatch`.

**Problem**: URL `numdam.org/item/AST_2002__278__R1_0/` resolves to the
PRELIMINARY PAGES (front matter, pp. I-XII) of Astérisque vol 278, NOT
Zink's chapter "The Display of a Formal p-Divisible Group" within that
volume.

**Fix path A (preferred)** — find the correct chapter URL:
1. Open `https://www.numdam.org/issue/AST_2002__278__/` (volume TOC).
2. Locate Zink's chapter; note its `AST_2002__278__<startpage>_0` id.
3. Update `references.ts` URL field to that id.

**Fix path B** — keep current entry, accept that local PDF is wrong:
- Mark URL field with a comment noting the volume-prelims confusion.
- The QOU citation in `witt-vector-lift.lean` is for "Dist(Ĝ) free
  ℤ_p-module structure" which IS in Zink's actual chapter §2. The
  citation INTENT is correct; just the local PDF is wrong.

**Recommended**: Fix path A. ETA: 3 minutes if numdam.org is accessible.

## 4. `blitvic2012` — Wrong arxiv id

**Status**: `paper-mismatch`.

**Problem**: `references.ts` URL `arxiv.org/abs/1205.4003` downloads
"Two-Parameter Non-Commutative Central Limit Theorem" by Blitvić,
but the bib title says "The (q,t)-Gaussian process". These are TWO
DIFFERENT papers by the same author.

**Fix path A** — update URL to the actual (q,t)-Gaussian paper:
The (q,t)-Gaussian process paper is at arxiv `1205.4203`
(`arXiv:1205.4203` — note the 4203 vs 4003 difference; likely a typo
in my original mirror search). Verify by searching
arxiv.org for "Blitvic q-t Gaussian process".

**Fix path B** — rename the bib title to match arxiv:1205.4003:
- Change `title: "The (q,t)-Gaussian process"` →
  `title: "Two-Parameter Non-Commutative Central Limit Theorem"`
- The .lean citation sites would then resolve to the correctly-named
  paper.

**Fix path C** — split into two keys:
- Keep `blitvic2012` as the (q,t)-Gaussian process; add a new
  `blitvic2012-clt` for the CLT paper at 1205.4003.
- Audit existing citation sites to figure out which uses which.

**Recommended**: Fix path A (update URL). Cheapest. ETA: 2 minutes.

## 5. `heisenberg1958` and `weil1948` — archive.org URL guesses fail

**Status**: `unfetchable` (both papers are public-domain book scans on
archive.org, but the `/download/<id>/<id>.pdf` URL pattern doesn't
match the actual filename).

**Problem**: My `gen-bib-papers-list.py` converts
`archive.org/details/<id>` to `archive.org/download/<id>/<id>.pdf`.
For klein1888 that worked (filename matched id). For
heisenberg1958 (`physicsphilosoph00heis`) the URL returns 401, and
weil1948 (`surlescourbesa00weil`) returns 503.

**Root cause**: archive.org items can have arbitrary PDF filenames
(`<id>_bw.pdf`, `<id>_text.pdf`, `<id>_djvu.pdf`, etc.). Without
consulting `archive.org/metadata/<id>` JSON to discover the real
filename, the guess fails.

**Fix path A** — extend `gen-bib-papers-list.py` to query the
metadata API. Pseudocode:
```python
import urllib.request, json
def archive_org_pdf(item_id: str) -> str | None:
    meta = json.loads(urllib.request.urlopen(
        f"https://archive.org/metadata/{item_id}").read())
    for f in meta.get("files", []):
        if f.get("name", "").endswith(".pdf") and f.get("format", "").startswith("Text"):
            return f"https://archive.org/download/{item_id}/{f['name']}"
    return None
```
ETA: 30 min including testing.

**Fix path B** — manually find the correct URL per item:
- `physicsphilosoph00heis` — try
  `https://archive.org/details/physicsphilosoph00heis` in browser;
  inspect "Download options" sidebar for PDF link.
- `surlescourbesa00weil` — same, but the 503 may also be a temporary
  rate-limit. Retry later.

**Fix path C** — accept that these are unfetchable:
- Heisenberg "Physics and Philosophy" and Weil "Sur les courbes
  algébriques" are old enough + culturally-significant enough that
  the existing bib title+publisher metadata is sufficient. Both
  citations in QOU are likely contextual rather than theorem-citing.
- Mark `unfetchable` and move on.

**Recommended**: Fix path A as a one-time improvement to
gen-bib-papers-list.py — fixes archive.org class of failures
permanently. Path B is acceptable as a stopgap. ETA: 30 min.

## Summary

| Item | Fix | Status |
|---|---|---|
| margolus1998 | Re-run `upload-bib-papers.sh --force` | URL already fixed; user runs |
| turaev2010 | No action | Already removed |
| zink2002 | Find correct numdam chapter URL on `numdam.org/issue/AST_2002__278__/` | needs your input |
| blitvic2012 | Update URL `1205.4003` → `1205.4203` (verify on arxiv) | needs your input |
| heisenberg1958 + weil1948 | Extend `gen-bib-papers-list.py` with archive.org metadata API; OR accept as unfetchable | needs your input |

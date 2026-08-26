# Satellite / cabling source ledger — links only, NOT ingested

Bean `qou-6tcn`, 2026-08-26.

> ## 🛑 CORRECTED 2026-08-26 — the premise of this file was false
>
> This ledger was opened because I reported the ingested library held **zero**
> sources on satellites, toroidal knots or cabling. **That was wrong.** I
> grepped `library/INDEX.md` — the one-line briefs — got zero hits, and stopped.
> AGENTS.md path 5 prescribes **three** tiers: `INDEX.md`, then `summary.json`,
> then `grep -rln <topic> library/<doc-id>/sections/`. I ran tier 1 only.
>
> Measured, **excluding** the 15 documents later ingested on the strength of my
> false report: `satellite` **12** documents, `cabling` **19**, `JSJ` **13**,
> `"essential torus"` **4**. `INDEX.md` really does have 0 hits — the briefs are
> *extractive*, assembled from abstracts and section titles, so a topic
> discussed in a body but absent from its abstract is invisible at tier 1. That
> is exactly why the checklist has three tiers. The failure is mine, not the
> index's.
>
> **The 15 documents are now ingested** (commit `6df6bd55f7`) and are worth
> having — the cabling-formula paper in particular was genuinely not held. But
> the gap this file was opened to fill was smaller than stated, and the sections
> below are kept as the record of what was requested and why.

## 🛑 What this file is, and what it is not

**It is a citation ledger.** Every entry below is an arXiv ID + title returned
verbatim by an out-of-band web search. The links are real.

**It was NOT an ingest when written — and it has since been superseded by one.**
As written, none of these documents was in `library/`, so path 5 could not reach
*them*. All 15 were ingested on 2026-08-26 (`6df6bd55f7`), and path 5 now
returns **42** documents for *satellite*, **61** for *cabling* and **11** for
*Hopfion* — figures that include the pre-existing documents my tier-1-only grep
had missed. Cite the library, not this file, for what the corpus holds.

**I have not read any of them.** Titles and IDs are as returned; the one-line
notes are from search-result summaries, not from the papers. Nothing here may be
used as a source for a claim — only as a pointer to where to look.

## Why the ingest could not be done

The sandbox proxy blocks every paper host. Measured this session, walking the
[`local/sandbox-egress`](../../.claude/skills/local/sandbox-egress.md) route
table rather than stopping at the first 403:

| host | result |
|---|---|
| `export.arxiv.org` (API) | `CONNECT tunnel failed, response 403` |
| `arxiv.org` | `000` (no connection) |
| `api.openalex.org` | `000` |
| `api.semanticscholar.org` | `000` |
| `api.crossref.org` | `000` |
| `raw.githubusercontent.com` | `301` — **open**, per the route table |
| WebSearch (MCP) | **open, out-of-band** — how these links were obtained |

Every `paper-search-mcp` backend returns `[]` for the same reason: they ride the
same proxy. So the PDFs cannot be fetched here, and
`scripts/migrate-uploads-to-library.py` has nothing to migrate. **Ingesting
these needs a session with egress, or the PDFs dropped into `uploads/` by hand.**

## Mathematics — cabling and satellite formulas for the Jones polynomial

Directly relevant to whether a satellite escapes the branch-convexity bound of
Addendum 23/24: these give the colored Jones of a cable in terms of the
companion's.

| arXiv | title |
|---|---|
| [0807.2679](https://arxiv.org/abs/0807.2679) | A cabling formula for the colored Jones polynomial |
| [0810.1697](https://arxiv.org/abs/0810.1697) | On the cable expansion formula |
| [1501.01574](https://arxiv.org/abs/1501.01574) | Knot Cabling and the Degree of the Colored Jones Polynomial |
| [1501.04614](https://arxiv.org/abs/1501.04614) | Knot Cabling and the Degree of the Colored Jones Polynomial II |
| [2104.14491](https://arxiv.org/abs/2104.14491) | Khovanov polynomials for satellites and asymptotic adjoint polynomials |
| [2303.08330](https://arxiv.org/abs/2303.08330) | A Cable Knot and BPS-Series II |

**Why this set matters here.** The `H₁₂` cable compute measures one cable
directly. A cabling formula would replace that measurement with a *closed form*
— the colored Jones of the companion at higher colour — which is the
formalize-first route and would generalise past the deuteron in one step
instead of one isotope at a time.

## Physics — toroidal knotted solitons

**The author's question has an answer, and it is yes.** The Faddeev–Skyrme /
Hopfion literature is exactly "mesonic toroidal forces": knotted solitons whose
topology is the Hopf map `S³ → S²`, carrying a **twisted toroidal** structure,
in an effective low-energy `SU(2)` model.

| arXiv | title |
|---|---|
| [0705.1468](https://arxiv.org/abs/0705.1468) | Knots in the Skyrme-Faddeev model |
| [nucl-th/0309051](https://arxiv.org/abs/nucl-th/0309051) | Reinterpretation of Faddeev-Niemi Knot in Skyrme Theory |
| [cond-mat/0112325](https://arxiv.org/abs/cond-mat/0112325) | Knots in Condensed Matters |
| [1007.2335](https://arxiv.org/abs/1007.2335) | Hopf solitons in the Nicole model |
| [1304.4737](https://arxiv.org/abs/1304.4737) | Toroidal domain walls as Hopfions |
| [1707.06608](https://arxiv.org/abs/1707.06608) | Fractional Hopfions in the Faddeev-Skyrme model with a symmetry breaking potential |
| [0809.4303](https://arxiv.org/abs/0809.4303) | Exact vortex solutions in an extended Skyrme-Faddeev model |
| [1012.4090](https://arxiv.org/abs/1012.4090) | Generalized Skyrme Crystals |
| [2602.15276](https://arxiv.org/abs/2602.15276) | Compact Q-balls and Q-shells within a CP^N Skyrme-Faddeev type model |

Three points from the search summaries, flagged as **unread** and to be checked
against the papers before any of them is used:

1. Faddeev and Niemi conjectured the Hopf solitons carry a **twisted toroidal**
   structure and form knotted configurations; numerics confirmed it, computing
   solutions up to Hopf charge sixteen **including a variety of torus knots**.
2. In low-energy QCD these solutions, as knots of the **gluon** field, are
   proposed to describe **glueballs** — a strong-sector object with toroidal
   topology, which is the shape the author's question was reaching for.
3. Via the **Cho–Faddeev–Niemi decomposition** the Skyrme–Faddeev model is
   conjectured to be the low-energy effective model for `SU(2)` Yang–Mills.

**Point 3 is the one to be careful with.** QOU's own fibre is pinned at rank two
(`exteriorSquareDim N = 1 ↔ N = 2`), so an `SU(2)` effective description is
suggestive of a connection rather than evidence for one — and a *suggestive
shape match* is exactly the class of observation the anti-numerology discipline
exists to slow down. Nothing here is wired, cited in a content block, or used
in any derivation.

## What would close this

1. Ingest the two groups into `library/` from a session with egress (or drop the
   PDFs into `uploads/` and run the pipeline). Only then does path 5 answer.
2. With the cabling papers in hand, replace the `H₁₂` measurement with the
   closed-form cabling formula and check the branch-convexity escape in general
   rather than at one isotope.

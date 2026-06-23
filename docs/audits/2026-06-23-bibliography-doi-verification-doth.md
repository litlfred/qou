# Bibliography DOI / metadata verification — bean `doth` (2026-06-23)

**Session:** nifty-cerf · **PR:** #2649 · **Source:** two background research
agents over the 22 marker-flagged entries in `content/schema/references.ts`
(7 `TODO:` + 15 `PLACEHOLDER:`).

## ⚠ Verification-confidence caveat (read first)

Both agents hit **HTTP 403 on every DOI landing page** (`doi.org`,
`api.crossref.org`, `link.springer.com`, `www.ams.org`, `projecteuclid.org`,
arXiv) — sandbox egress allowlist. **No DOI was resolved to its landing page.**
Confirmations below come from **authoritative search-result link titles /
author-site filenames / ADS bibcodes** (real artifacts), not rendered pages.
Model-generated search *summaries* proved unreliable (gave inconsistent
volumes/pages across runs) and were discarded. Anything not backed by a real
link artifact is marked **UNVERIFIED**.

**Implication:** the *findings* (a stored DOI's link title names a different
paper) are reliable; the *replacement* volume/page details often are not. Before
committing DOI swaps, resolve each DOI directly (add `doi.org`/`api.crossref.org`
to the allowlist, or verify off-sandbox).

## A. Stored DOI resolves to the WRONG paper (high-value bugs)

| Entry | Stored DOI | What the DOI's link title actually names | Intended paper (per stored title) |
|---|---|---|---|
| `kashiwara1990-cmp2` | `10.1007/BF02100009` | **Witten**, "On quantum gauge theories in two dimensions", CMP **141** (1991) | Kashiwara, "Crystal bases of the modified quantized enveloping algebra", **Duke MJ 73(2) (1994) 383–413**, DOI `10.1215/S0012-7094-94-07317-1` |
| `kashiwara1990-duke` | `10.1215/S0012-7094-90-06120-X` | a 1990 Duke vol-61 slot (Labesse-area base-change), **not Kashiwara** | Kashiwara, "The crystal base and Littelmann's refined Demazure character formula", **Duke MJ 71 (1993) 839–858**, DOI `10.1215/S0012-7094-93-07131-1` |
| `wenzl1988b` | `10.1007/BF01393839` | "Analytic formulas for the regulator of a number field", *Inventiones* — **not Wenzl, not Hecke** | UNKNOWN — correct Wenzl DOI not found; **needs author** |
| `faddeev1995` | `10.1007/BF01872779` | "Discrete Heisenberg-Weyl Group and modular group", *Lett. Math. Phys.* **34**, 249 (1995), L. D. Faddeev (ADS `1995LMaPh..34..249F`, arXiv hep-th/9504111) | **DOI is correct**; only the stored *title guess* ("modular quantum dilogarithm") was wrong |
| (DOI `10.1007/s00222-009-0204-8`, sitting near `drinfeld1985`) | — | "Blocks of cyclotomic Hecke algebras and Khovanov-Lauda algebras", *Inventiones* (2009), Brundan–Kleshchev | **Not Drinfeld 1985** — DOI is mis-placed; reassign to its real 2009 entry |

## B. Wrong author / id misidentification

| Entry | Finding |
|---|---|
| `carter-leal-saliola-2000` | arXiv math/0008040 is **single-author R. J. Marsh** ("Rectangle diagrams for the Lusztig cones…"). No Carter, no Leal, no Saliola. The id + author list are a misidentification. Journal-ref UNVERIFIED (possibly J. Algebra). Sibling math/0008035 is a *different* Marsh paper — do not conflate. |
| `pawlowski-leitner-rep` | **UNVERIFIED** — no citable id found for the "PL inner product ⟨φ,ψ⟩=tr_Ad(φ†∘ψ)" / SU(2)-intertwiner work. Sibling `leitnerpawloski2004` is **also mis-recorded**: arXiv math/0409565 is "Unital Grobner Bases over Arbitrary Ground Rings" by Leitner & **Robert** Pawloski (math.RA) — not "On the morphisms of non-commutative formal groups" by "Jan Pawłowski". Needs author knowledge (may be unpublished notes / thesis). **Do not fabricate.** |

## C. Year / title corrections (DOI absent or correct; references.ts-only)

| Entry | Correction | Confidence |
|---|---|---|
| `chlouveraki2016-hdr` | title → "Hecke algebras, generalisations and representation theory"; add URL `https://theses.hal.science/tel-01411063` (HAL `tel-01411063`); HDR UVSQ 2016 | HAL link confirmed |
| `halverson_ram_1998` | title "Murnaghan-Nakayama rules for characters of Iwahori-Hecke algebras of classical type"; TAMS **348**(10) 3967–3995, **year 1996** (not 1998); DOI→paper binding UNVERIFIED but "-96-" consistent | Arun Ram author-site filename `1996TAMSv348n10p3967.pdf` |
| `james1984representation` | James **& Kerber**, "The Representation Theory of the Symmetric Group", Encyclopedia of Math. & its Apps **Vol. 16**, Addison-Wesley, **1981** (not 1984) | Cambridge Core review link title |

## D. Textbooks — ISBN/identifier CONFIRMED (resolve PLACEHOLDER → settled)

- `bertsimas1997`: *Introduction to Linear Optimization*, Bertsimas & Tsitsiklis, Athena Scientific 1997, ISBN 1-886529-19-1 (978-1-886529-19-9).
- `majid1995`: *Foundations of Quantum Group Theory*, Majid, CUP 1995, ISBN 0521460328 (9780521460323).
- `murasugi1996`: *Knot Theory and Its Applications*, Murasugi, Birkhäuser 1996, ISBN 0817638172 (9780817638177).

## E. Still UNVERIFIED (keep a marker — honest open state)

- `wenzl1988c` DOI `10.1007/BF01388470` — never resolved; likely not Wenzl. Resolve manually.
- `wenzl1988b` — DOI proven wrong (regulator paper) but correct Wenzl DOI not found.
- `pawlowski-leitner-rep` (+ `leitnerpawloski2004` mis-record) — author input required.

## F. Pre-DOI archival sources (PLACEHOLDER label is mislabeled, not a TODO)

`abel1826` (Crelle), `frobenius1898` (Sitzungsberichte), `rogers1907` (PLMS),
`klein1884vorlesungen` — these predate DOIs; "verify page range" is the only
residual. Their "PLACEHOLDER" marker should become a settled archival note
(reword, don't keep flagging as actionable).

## Recommended disposition

1. **Apply now (unambiguous, references.ts-only):** §C (chlouveraki, halverson,
   james), §D (textbook ISBNs), §F (reword archival), `faddeev1995` title fix.
2. **Author decision (cross-file / id-rename / DOI-swap on snippet confidence):**
   §A Kashiwara DOI swaps + 3 `.lean` inline-DOI syncs; §A `wenzl1988b` /
   `s00222` reassignment; §B `carter-leal-saliola`→Marsh id rename (+2 cite
   sites); §B/§E `pawlowski-leitner` cluster.
3. **Before any DOI swap reaches `main`:** resolve the DOIs directly (allowlist
   `doi.org`) — current confidence is link-title level only.

# Borromean AJ — literature status (stage 1b): formulated-only for links, OPEN for 𝓑₃

**Date:** 2026-07-06
**Branch:** `claude/aj-conjecture-qou-uz5m6x` (PR #3434)
**Bean:** `ds4b` (Borromean stage 1b), unblocking context for `n920`
**Lineage:** follow-up to
[`2026-07-03-aj-conjecture-dialog-assessment.md`](2026-07-03-aj-conjecture-dialog-assessment.md)
§"the honest maximal scope" — the per-knot AJ table left 𝓑₃ as *"OPEN
(AJ for links is not settled; corpus stance unchanged)"* pending a
literature check. This audit is that check.

**Bottom line.** The corpus stance is **confirmed and sharpened**: the
AJ conjecture for *links* was only **formulated** in 2024 (Sawabe,
arXiv:2409.03802 — computes the Hopf and Whitehead annihilators and
states the link-AJ conjecture); **no AJ result and no published
recurrence/A_q-ideal exists for the Borromean rings**. The
`QuantumAPolynomial borromean` §3b class stays uninstantiated — and the
former framing "needs literature verification" upgrades to a positive
factual finding: *verified open*. The three citable Borromean facts are
q-holonomicity (theorem, all links), Habiro's explicit cyclotomic
formula, and the proved volume conjecture.

## Findings

### 1. q-holonomicity for links — THEOREM

Garoufalidis–Lê, *The colored Jones function is q-holonomic*, Geom.
Topol. 9 (2005) 1253–1293 (`garoufalidis-le-2005`, added).
Covers the multi-variable colored Jones of links. This is the existence
half of the AJ machinery and needs no framework input — consistent with
the dialog-assessment's §2 (the pasted dialog's "derivation" of
holonomicity from finite-dimensional $\mathbf H_3(q)$ was both wrong
and unnecessary).

### 2. AJ specialization — status ladder

| Scope | Status | Citation |
|---|---|---|
| 2-bridge knots (incl. twist knots) | **proved** | Lê 2006, Adv. Math. 207, 782–804 (`le2006`, added) |
| Figure-eight, strong AJ | **proved** | Nguyen–Tran 2021 (`nguyen-tran-2021`, already in corpus) |
| Links, formulation | **formulated only** (2024); Hopf + Whitehead annihilators computed | Sawabe, arXiv:2409.03802 (`sawabe2024`, added) |
| Borromean rings 𝓑₃ | **OPEN** — no formulated-and-proved AJ statement, no published recurrence ideal | — |

One search summary claimed Sawabe treats the Borromean rings; this
contradicts the quoted abstract (Hopf + Whitehead) and is treated as
**unresolved** until the paper body is read (blocked in-sandbox — see
§Verification limits). Do not cite `sawabe2024` as a Borromean
result.

### 3. What IS available for 𝓑₃

1. **Habiro's cyclotomic expansion** — the explicit colored-Jones
   formula for simple links including 𝓑₃, symmetric in the three
   colors: RIMS Kōkyūroku 1172 (2000) 34–43. The corpus's `habiro2000`
   entry is **confirmed** (PLACEHOLDER flag dropped; title pluralised).
   The exact formula is *not yet transcribed* into the corpus — the
   PDF is unreachable from this sandbox; transcription stays queued as
   bean `n920` (do **not** transcribe from memory).
2. **Volume conjecture for 𝓑₃ — proved** — Garoufalidis–Lê,
   *Asymptotics of the colored Jones function of a knot*, Geom. Topol.
   15 (2011) 2135–2180, appendix (`garoufalidis-le-2011`,
   added), using exactly Habiro's expansion.
3. **Twist-knot companion** — Masbaum, Algebr. Geom. Topol. 3 (2003)
   537–556 (`masbaum2003`, added): the published skein
   derivation of Habiro's formulas for twist knots (4₁ = K₋₁, trefoil
   = K₁) — the source behind the corpus's Masbaum cross-check (bean
   `xcyc`, completed 2026-07-04). Twist knots only; not Borromean.

### 4. Corpus corrections landed with this audit

- **`garoufalidis2004` DOI bug fixed**: the entry carried the spurious
  J. Diff. Geom. DOI `10.4310/JDG/1090425531`; corrected to the
  authoritative `10.2140/gtm.2004.7.291` (Geom. Topol. Monogr. 7,
  Casson Fest) in `content/schema/references.ts` and in the two
  `-- Ref:` comments in
  `stochastic-mechanics/phi-q-aj-machinery-identification.lean`.
- Five verified reference entries added (`garoufalidis-le-2005`,
  `le2006`, `garoufalidis-le-2011`, `sawabe2024`,
  `masbaum2003`); `habiro2000` confirmed.

## Verification limits (honesty banner)

All arXiv / ar5iv / Semantic Scholar / publisher-PDF fetches were
blocked by the sandbox egress policy (403 at the proxy; the
paper-search MCP tools returned empty sets for the same reason).
Every claim above rests on **multiply-corroborated WebSearch metadata
snippets**, not on read PDF bodies. Items explicitly *not* verified:
whether Sawabe's paper body mentions 𝓑₃; the exact Habiro Borromean
formula; Lê 2006's DOI; Hikami 2003 page range; whether
Detcherry–Garoufalidis (*A diagrammatic approach to the AJ Conjecture*,
Math. Ann., arXiv:1903.01732) touches links. A future session with
arXiv access should read `sawabe2024` and `math/0508100` Appendix A
before extending this audit.

## Disposition

- `phi-q-aj-machinery-identification` (.lean/.md): the "needs
  literature verification (Hikami/Habiro)" caveat on
  `QuantumAPolynomial borromean` can now cite this audit — the class
  stays **uninstantiated as a verified-open input**, which is the §3b
  honest state.
- Bean `ds4b` → completed. Bean `n920` (Habiro formula cross-check)
  stays deferred on PDF access — this audit adds the confirmed
  citation it was waiting on but not the formula body.
- No wiring, no status changes to any conjecture carrier, no new
  conjecture blocks.

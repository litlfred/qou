---
# qou-r44k
title: 'Five QOU-vs-QCD name collisions: saturation, shadowing, diffraction, S-matrix, Fourier transform'
status: completed
type: task
priority: normal
created_at: 2026-09-13T05:11:10Z
updated_at: 2026-09-13T10:33:35Z
---

## Measured 2026-09-13 (grep over content/ docs/ computations/ *.lean)

Five QCD terms mean something ELSE in this corpus. Each is a live trap for anyone
comparing QOU to a QCD measurement, and two of them nearly reached a user-facing
claim in one session.

| term | QCD meaning | what it means HERE | counts |
|---|---|---|---|
| `saturation` | small-x gluon recombination, `Q_s(x)` | (a) knot-genus saturation for `T(2,9)`; (b) NUCLEAR saturation = the `B/A` plateau (`QOU.Mass.CoordinationSaturation`); (c) "scales saturate" in the cosmology appendix | 124 content |
| `shadowing` | nuclear shadowing / Gribov screening | **100 %** LP-dual SHADOW PRICES (`y0_star`, `y_star`), plus "archimedean shadow" and the a1 "parity shadow". Nuclear shadowing: **0** | 23 content / 43 beans |
| `diffraction` | Pomeron exchange, diffractive dissociation | OPTICAL — Fraunhofer, Airy, double-slit | 11 content |
| `S-matrix` | scattering matrix | **modular** S-matrix of an MTC / Chern-Simons RT localization (vacuum row, `D = sum d_i^2`) | 121 comp / 11 lean |
| `Fourier transform` | momentum-space / impact-parameter conjugate | discrete FT on `C_n` (Lagrange resolvent), CATEGORICAL FT, adelic FT. None over R^2 | 25 content / 22 lean |

Also measured ZERO, corpus-wide: `parton`, `Bjorken`, `DGLAP`, `deep inelastic`,
`photoproduction`, `nuclear shadowing`, `Mandelstam`, `RG flow`, `energy dependence`,
`Color Glass`, `small-x`, `hot spot`, `impact parameter`, `transverse plane`,
`momentum space`.

## Why this is a bean and not a note
Two of the five (`S-matrix`, `Fourier transform`) were about to be stated as ABSENT
in a user-facing reply on the strength of a topic grep; they are present in large
numbers and mean something unrelated. That is the same detector-blindness class
AGENTS.md catalogues 35 rows of, one level up: the word matches, the referent does not.

## Default if nothing is done
Nothing changes. The next agent asked "can QOU explain <QCD result>" re-measures
this from scratch, or worse, finds "saturation" in 124 files and answers yes.

## Suggested disposition (agent judgement, owner call)
Add the five to `content/quantum-observable-universe/notation/notation-collisions.md`,
which already carries exactly this kind of rule ("`$c$` = color, never charm").
NOT done here - that is a content edit and this is a math repo.


## LANDED 2026-09-13 on `main` (merge `3cb26d4b9f8`)

`content/quantum-observable-universe/notation/notation-collisions.md` gains
§"QCD vocabulary: six words that mean something else here" — **saturation**
(knot genus / the `B/A` plateau, never the gluon `Q_s`), **shadowing** (the
100 % LP-dual *shadow prices*, never nuclear shadowing), **diffraction**
(optical), **S-matrix** (modular, of an MTC), **Fourier transform**
(cyclic / categorical / adelic), **alternating sign** (alternating sign
*matrices*, and the Ursell alternation — not a QCD term but the same trap).
Plus the measured-zero list: `parton`, `Bjorken`, `DGLAP`, `impact parameter`,
`transverse plane`, `momentum space`.

**Written as a rule because two of them were about to be reported ABSENT** off a
topic grep, while present in 100+ files meaning something else entirely. That is
the corpus-grep checklist's blind spot from the opposite side: the standard
failure is a grep that misses prior work written in different words; this is a
grep that *hits* on a word the corpus uses for something unrelated and reads as
coverage.

Render-QA by hand (the pipeline render is unavailable in this container, so
**this file was not machine-validated** and the commit says so): `$` count even,
no `$$`, braces balanced, no align-family env, unicode limited to U+2013/U+2014.

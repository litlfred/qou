# Literature review — "the q-difference kernel C1 is the Seiberg–Witten jet-prolongation symbol"

**Date:** 2026-07-20
**Scope:** external-literature assessment (NOT a corpus-open declaration; the
corpus-grep checklist gates open-item claims, not outside-view lit judgment).
**Tooling:** `mcp__paper-search-mcp__*` backends are firewalled in this
sandbox (403 CONNECT policy denials on semanticscholar/crossref/arxiv);
WebSearch (Anthropic-routed) returned real hits. **All arXiv IDs below are
WebSearch-sourced — verify before wiring into `references.ts`** (PDFs were not
opened in-sandbox).

## The core claim and the verdict

The keystone conjecture
[`conj:qdifference-kernel-prolongation-symbol`](../../content/quantum-observable-universe/mass-theory/qdifference-kernel-prolongation-symbol.md)
asserts the q-difference kernel `C1` (the proved q-lift
`[n+2]_q b_{n+2} = b_{n+1} + b_n`) **is** the symbol of the SW
jet-prolongation operator. Literature verdict:

- **No published paper states this identification.** Every *ingredient*
  is published; the *weld* is QOU-original.
- **Referee flag (notation).** "Symbol of a q-difference operator" already has
  a fixed technical meaning (Sauloy: the top-slope / Newton-polygon datum of
  the canonical slope filtration, `math/0210430`). QOU's bespoke "symbol =
  jet-prolongation" use is a **notation collision** a referee will catch. The
  claim should anchor to an established bridge, and remain a `conjecture` /
  `definition` with a derivation target — **not** a `theorem** — until the
  equality is derived. (It already is a `conjecture`; keep it.)

## Two mathematical halves that DO exist (the citable anchors)

Setting the word "symbol" aside, the two mathematical objects the claim welds
are both published:

### (1) Prolongation half — the Donagi–Markman cubic
Special / rigid-special-Kähler geometry on the SW base carries a symmetric
cubic form `c_{ijk} = ∂³F/∂aⁱ∂aʲ∂aᵏ` (third derivative of the prepotential
`F`). This is the second-order deformation / prolongation datum of the
special-geometry connection — mathematically "the SW prolongation," under a
different name. Anchors: Donagi, *Seiberg–Witten integrable systems*
(`alg-geom/9705010`); Donagi–Markman, *Cubics, integrable systems, and
Calabi–Yau threefolds*; Freed, *Special Kähler manifolds* (`hep-th/9712042`).

### (2) Difference-operator half — the quantum SW curve
Grassi–Gu–Mariño, *Non-perturbative approaches to the quantum Seiberg–Witten
curve* (`1908.07065`, JHEP 07 (2020) 106) quantize the classical SW curve into
an **actual difference operator** whose classical limit is the curve; its
WKB/quantum periods carry the prolongation data. This is the published place
where "prolongation on SW geometry" and "difference kernel" mathematically
touch — as **quantization ↔ classical limit**, not as an identity.

The honest QOU-original step is welding (1) and (2) into "the kernel *is* the
prolongation symbol"; it should **cite both** as anchors.

## Per-topic ranked hits

**T1 — q-difference modules, Newton polygon / slope "symbol":**
Sauloy `math/0210430` (canonical slope filtration = the established "symbol");
Ramis–Sauloy–Zhang `0903.0853` (local analytic classification — already in
corpus as `ramis-sauloy-zhang2013`); Sauloy `math/0507098` (Galois backdrop).

**T2 — SW prolongation / jet / period-as-residue:**
Donagi `alg-geom/9705010` (SW integrable system + Donagi–Markman cubic =
prolongation); GKMMM (Nucl. Phys. B `0550321396003586`) (SW differential,
periods, vanishing-residue meromorphic form); isomonodromy `hep-th/9603069`.

**T3 — Alien calculus / resurgence on SW periods; GGM 3d-index:**
Garoufalidis–Gu–Mariño `2007.10190` (resurgent structure of quantum knot
invariants); GGM *Peacock patterns* `2012.00062` (Stokes-matrix entries = the
integer 3d-index — the "integer-3 GGM 3d index"); Grassi–Gu–Mariño `1908.07065`
(quantum SW curve as difference operator; bridge-equation-style TBA).

**T4 — Colored Jones / AJ / q-difference recurrence:**
Garoufalidis–Lê 2005 (colored Jones is q-holonomic — the `[n+2]_q` kernel;
already `garoufalidis2004` + Lê in corpus); Nguyen–Tran `2006.02042` (**strong
AJ = recurrence ideal ↔ A-ideal** — the closest published "difference kernel ↔
curve", already `nguyen-tran-2021`); Garoufalidis *The AJ conjecture*.
**AJ is the closest existing "difference kernel ↔ curve" — but the curve is the
SL₂(ℂ) character variety, not the SW curve**, and the map is a q→1 limit, not a
"symbol."

**T5 — Gevrey-1/2 / q-Borel; involution numbers as a period:**
q-Borel `1806.05375` (already tracked alongside Zhang 1999); *Involutions and
their progenies* `1406.2356` (I(n) recurrence + Gevrey-1/2-flavored asymptotic
`I(n) ~ (n/e)^{n/2} e^{√n−1/4}/√2`); GGM–Wheeler *Resurgence, Habiro elements
and strange identities* `2304.07001` (directly relevant to QOU's Habiro Q_β/c_k
framing). **No paper identifies involution-number asymptotics with a
Bring-surface / quintic period** — a second candidate QOU-original contribution.

## Bibliography keys added / to add

Already in corpus (do not re-add): `ramis-sauloy-zhang2013`, `nguyen-tran-2021`,
`garoufalidis2004` (+ Garoufalidis–Lê), Zhang 1999 + q-Borel `1806.05375`.

Added this PR (high-confidence IDs): `donagi1997swintegrable`
(`alg-geom/9705010`), `grassi-gu-marino2019qsw` (`1908.07065`).

Deferred (verify IDs before adding): `sauloy2004filtration` (`math/0210430`, to
disambiguate "symbol"), `ggm2020peacock` (`2012.00062`), `ggmw2023habiro`
(`2304.07001`).

## Two candidate QOU-original contributions flagged
1. difference-kernel-as-**symbol-of-SW-prolongation** (the keystone claim);
2. involution-number asymptotics = **Bring-surface / quintic period**.
Both should be authored as `conjecture` / `definition` with explicit derivation
targets, not `theorem`, until derived — consistent with current corpus state.

# Internal-conjecture closure sweep (2026-07-02)

**Scope.** All live `kind: "conjecture"` content blocks in
`content/quantum-observable-universe/`, **excluding** the imported famous
open problems (§C.1 of
[`2026-06-07-conjecture-triage.md`](2026-06-07-conjecture-triage.md) —
Millennium / classical reframings, not QOU's to close). The question:
which QOU-native ("internal") conjectures can now be **closed** —
proved, refuted (with the (a)/(b) scope discipline), or discharged into
a §3b-cond conditional result — given corpus progress landed on `main`
**since the 2026-06-25 refresh** of the conjecture triage.

**Method.** Same discipline as the 2026-06-07/08/25 sweeps: per-block
corpus-grep checklist (docs/audits/, content/, computations/,
docs/coordination/) plus a targeted diff of post-2026-06-25 `main`
commits (sorry-free Lean landings, refutation probes, keystone
propositions) against the open-conjecture inventory.

**Status: COMPLETE.** Headline: **the closeable set remains ≈ empty.**
127 blocks swept (58 mass-theory + mass-endomorphism; 64 across the
other chapters; 5 imported-famous skipped in-scope + the surreal
appendix excluded per the standing owner retention decision). **0
CLOSEABLE-prove, 0 CLOSEABLE-refute, 1 stale-status** (fixed in this
PR). This independently re-confirms the 2026-06-25 refresh of
[`2026-06-07-conjecture-triage.md`](2026-06-07-conjecture-triage.md)
on the fresh post-06-25 evidence.

## Post-2026-06-25 evidence candidates (to check against conjectures)

- `d9af25c6` — self-duality ⇒ CS(4₁)=0 over generic (R,σ), sorry-free.
- `5d2da3f3` — Vol(4₁) saddle: structure proved sorry-free, limit as
  conditional class.
- `b1bb7482` — C=bar (H₂ leptons) vs C≠bar (H₃ mesons) → 3-calibration
  origin, sorry-free.
- `3b3093da` + `0b7e3716` — OV Identity (B) via Artin–Wedderburn; C₂
  centrality de-abstracted to an elementary combinatorial core.
- `a9c2d917` — keystone prop: self-dual Higgs (4₁) has real complex
  volume.
- `1c780914` / `9968b4c6` — keystone probes: bare support = H₄
  exponents; `[e]_q` value-map refuted; colored Σ(2,3,5) E₈-exponent
  family.
- `319a6c3c` / `29348231` — value-map screen: compact candidates
  refuted; q-Bessel radial-part target narrowed.

## Findings

### A. Per-commit evidence → conjecture-inventory map

Every post-06-25 landing was traced to its Lean/content artifact and
checked against the conjecture blocks whose claims overlap:

| Evidence | Landing | Conjecture impact |
|---|---|---|
| `a9c2d917` self-dual Higgs (4₁) real complex volume | **born `proposition`** (`prop:self-dual-higgs-real-volume`, `braids-and-knots/`), sorry-free `QOU.Knot.SelfDuality.higgs_complex_volume_real` | correctly kinded at birth; no drift |
| `d9af25c6` self-duality ⇒ CS(4₁)=0 over generic (R,σ) | `Knot/FigureEightSelfDuality.lean` theorems | backs the prop above; corroborates (does **not** discharge) `conj:binding-qbeta-complex-volume` |
| `5d2da3f3` Vol(4₁) saddle | structure sorry-free; limit carried as `class VolumeConjecture41 : Prop` — hypothesis-only, **no instance** anywhere in tree | sanctioned §3b treatment of the imported-famous Kashaev conjecture; no flip |
| `b1bb7482` C=bar (H₂) vs C≠bar (H₃) → 3-calibration origin | `Mass/LeptonMesonParitySplit.lean`, sorry-free | backs the already-`proposition` `prop:three-calibration-discipline`; not referenced by any `conj:` block |
| `3b3093da`+`0b7e3716` (+`6b49ccc4` post-sweep) Identity (B) Artin–Wedderburn, now fully sorry-free | `BraidKnot/IdentityBWedderburn.lean` / `IdentityBCentrality.lean` | library lemma — no `conj:` block states this identity; no carrier to flip |
| `e21bcded` Borel-resummation mechanism | `class BorelTransformConverges : Prop` — hypothesis-only, no instance | §3b conditional carrier, correctly open |
| `0bc388b6` gen-3 meson φ at 2167 ppm | **born `proposition`** (`prop:gen3-meson-phi-hecke-seifert`) | correctly kinded at birth |
| `1c780914` / `9968b4c6` / `319a6c3c` value-map screens | compute probes ([e]_q refuted, compact candidates refuted) | prune candidate space for the open s013 keystone; no block-stated claim refuted |

**§3b discharge check:** tree-wide grep for sorry-free `instance`
declarations of any post-06-25 conjecture carrier class
(`VolumeConjecture41`, `BorelTransformConverges`, …) returns none —
no conjecture is silently discharged-in-Lean-but-not-flipped.

### B. Resolved-drift sweep (127 blocks)

- **mass-theory/ + mass-endomorphism/ (58 swept, 1 skipped famous):**
  1 stale-status; the rest current. Known-honest set of the 06-07
  triage §E re-confirmed against post-06-25 evidence (in particular:
  the 06-29/06-30 route-refutation audits — flavor-split dilog, κ
  framing, Δ_λ A≥5 continuation — close *routes*, not block-stated
  conjecture cores, and are already correctly (a)-scoped).
- **Other chapters (64 swept across observations/,
  particle-interactions/, predicted-spectra/, brings-surface/,
  molecular-construction/, quantum-observable-universes/,
  q-geometric-langlands/, stochastic-mechanics/, fluid-dynamics/,
  gravity-spacetime/, information-theory/, lifting-and-descent/,
  appendix-qvalues/):** 0 drift. Adjudicated near-misses ruled
  current: `hecke-anyonic-substrate` + `reverse-limit-q-to-infinity`
  (sanctioned proved-fragment banner + open remainder),
  `inter-nucleon-channel-color-tube` (over-claim already fixed per the
  06-24 triage), `klein-bring-icosahedral-bridge` (06-28 audits
  advance-not-close, already (a)-scoped), `e-hartree-categorical-derivation`
  (tiered-honest).

### C. The one stale-status fix (this PR)

[`conj:lepton-mass-tower-canonical`](../../content/quantum-observable-universe/mass-theory/lepton-mass-tower-canonical.md)
— the `.ts` authorNotes (2026-05-24) still asserted **muon =
figure-eight 4₁** while the `.md` banner carries the 2026-06-30
owner ruling (**muon = T(2,5), 4₁ = Higgs**;
[`2026-06-30-muon-knot-id-phi-q-evidence.md`](2026-06-30-muon-knot-id-phi-q-evidence.md)).
Added a 2026-06-30 status authorNote mirroring the banner; flagged the
superseded sketch inline; restored three date-stripped
`docs/audits/…` link paths in the `.md` cross-references. The block
stays a correctly-classified open Tier-E conjecture — no kind-flip.

### D. Conclusion

No QOU-internal conjecture is closeable on current corpus evidence.
The status-tracking discipline (authorNotes, conditional banners,
§3b hypothesis-only carriers, (a)/(b) refutation scoping) is holding:
post-06-25 results that *could* have produced drift were all born
correctly kinded or correctly carried as conditional classes. The
residual drift found by 3 independent sweep passes over 127 blocks
was a single lagging authorNote.

**Method note.** Three parallel read-only sub-agents: (1) per-commit
evidence mapping over `git log --since=2026-06-25`, (2) mass-theory +
mass-endomorphism per-block corpus-grep, (3) all other chapters
per-block corpus-grep. Every flagged candidate was opened and read at
file level before verdict (the §E "already-honest" calibration of the
06-07 triage applied). Content-pipeline validation unavailable
in-sandbox (folio-assistant clone 403); TS manifest transpile-checked
with `bun build`, `.md` checked with the manual render-QA grep
battery.

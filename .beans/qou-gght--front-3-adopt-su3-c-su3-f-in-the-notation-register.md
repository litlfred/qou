---
# qou-gght
title: 'Front 3: adopt SU(3)_c / SU(3)_f in the notation register and sweep the eightfold chapter'
status: todo
type: task
created_at: 2026-09-03T04:37:53Z
updated_at: 2026-09-03T04:37:53Z
parent: qou-icj2
---


## 2026-09-03 — convention adopted and chapter swept (sub-agent, PR #6458; uncommitted, parent commits)

**Convention.** Colour SU(3) is `$\mathrm{SU}(3)_{\mathrm{c}}$`; flavour SU(3) is
`$\mathrm{SU}(3)_{\mathrm{f}}$` (roman lowercase subscripts, matching `h_{\mathrm{A}}`
and `\chi_{\mathrm{eu}}`). Bare `$\mathrm{SU}(3)$` is permitted only for a
representation-theoretic statement true of any SU(3). A sentence deliberately
comparing the two carries both subscripts. Reason: `eightfold-open-problems` item 4
asks whether the two are the same, different, or groupoid-dual; a shared glyph
presupposes an answer.

**Register.** One row added to `notation/notation-register-table7-data.md`
("Flavour vs colour $\mathrm{SU}(3)$", font "roman subscript", inserted above the
"Mass (categorical)" row). One bullet added to `notation/notation-collisions.md`
immediately after the `$H_q$ alone` bullet, in its style; it records the legacy
spellings `SU(3)_c` / `SU(3)_L` / `SU(3)_R` (`observations/color-superconductivity-borromean.md`,
chiral CFL sentence) and `SU(3)_color` (three `docs/` audit/ledger files) as legacy,
not swept.

**Per-site table** (32 sites, 12 files; `file:line → decision → reason`; line numbers post-edit):

| site | decision | reason |
|---|---|---|
| `a2-from-three-strands.md:10` | f | "flavour SU(3)" Schur–Weyl partner on the fibre |
| `color-su3-from-g2.md:176` | c | "adjoint of SU(3) / gluon octet" table row |
| `color-su3-from-g2.md:181` | c | Günaydin–Gürsey `SU(3) ⊂ G₂` |
| `decuplet-equal-spacing.md:65` | f | "every SU(3) multiplet" = flavour multiplets |
| `dictionary-flavor-layer.md:50` | f | "standard SU(3) flavour assignments" |
| `eightfold-intro.md:20` | f | "sl₃ of flavour SU(3)" |
| `eightfold-intro.md:35` | f | "every flavour-SU(3) statement" |
| `eightfold-intro.md:57` | c | "the color SU(3) gauge algebra from octonionic stabilisation" |
| `eightfold-intro.md:76` | **bare** | "SU(3) representation theory — cited, not re-derived" (ambient mathematics) |
| `eightfold-intro.md:82` | f | "does not derive flavour SU(3)" |
| `eightfold-intro.md:86` | **bare** | literally "true of any SU(3)" |
| `eightfold-open-problems.md:18` | **bare** | "standard SU(3) representation theory" for 3⊗3̄ = 8⊕1 |
| `eightfold-open-problems.md:29` | c | the cited SU(3)-irreducibility input is the octonionic SU(3) ⊂ G₂ decomposition |
| `eightfold-open-problems.md:31` | c | `S⁶ = G₂/SU(3)` |
| `eightfold-open-problems.md:32` | **both** | table row "Flavour vs. colour" now reads `(SU(3)_f vs. SU(3)_c)` |
| `eightfold-open-problems.md:60` | c | "a colour SU(3) candidate" |
| `eightfold-open-problems.md:63` | c | same input as line 29 |
| `eightfold-open-problems.md:65` | f | "whether it yields *flavour* SU(3) is untested" |
| `eightfold-open-problems.md:178` | c | `SU(3) ⊂ G₂ = Aut(𝕆)` |
| `eightfold-open-problems.md:182` | c | `S⁶ = G₂/SU(3)` |
| `eightfold-open-problems.md:187` | c | "The octonionic SU(3) is colour" (item 4, deliberate comparison, c half) |
| `eightfold-open-problems.md:188` | f | "requires flavour SU(3)" (item 4, f half) |
| `meson-mass-splitting.md:40` | f | plain-text `SU(3)` → `$\mathrm{SU}(3)_{\mathrm{f}}$`; GMO flavour physics |
| `meson-mass-splitting.md:52` | f | "first-order SU(3) breaking" via λ₈ = flavour breaking |
| `meson-octet-decomposition.md:6` | f | "the flavor SU(3) classification" |
| `meson-octet-decomposition.md:57` | **bare** | "a theorem of SU(3) representation theory" |
| `schur-weyl-eightfold.md:120` | c | "non-self-dual triple from SU(3) ⊂ G₂" |
| `schur-weyl-eightfold.md:135–136` | f (+c added) | "*flavour* SU(3)_f (not just colour SU(3)_c)" — deliberate comparison, so the parenthetical gained an explicit `_c` (one new occurrence) |
| `u-spin-coleman-glashow.md:1` | f | "the flavour SU(3) contains two further SU(2)" |
| `vector-meson-nonet.md:3` | f | "identical SU(3) content" of the two nonets |
| `vector-meson-nonet.md:7` | f | "no SU(3)-symmetric statement distinguishes them" |
| `vector-meson-nonet.md:33` | f | "not a failure of SU(3)" (GMO flavour symmetry) |

Counts: **11 c, 16 f, 4 bare-standard, 1 both** (= 32 sites); plus one added `_c` at
`schur-weyl-eightfold.md:136`. Post-edit occurrences: 30 subscripted, 4 bare.

**Left bare and why.** Four sites (`eightfold-intro.md:76`, `:86`,
`eightfold-open-problems.md:18`, `meson-octet-decomposition.md:57`) are statements
about SU(3) representation theory as ambient mathematics ("true of any SU(3)",
"a theorem of SU(3) representation theory"); the convention keeps those bare.

**Render-QA gate.**
- Preflight grep battery (balanced `$`/`$$`/`{}`/`\bigl`–`\bigr`/`\begin`–`\end`, no
  `\operatorname`, no `+`/`-`/`*`-leading line inside `$$`): clean on 12 of 13 files.
  `u-spin-coleman-glashow.md:12–13` flags `- \bigl(` / `+ \bigl(` inside a `$$`
  block — **pre-existing in HEAD**, not on a line I touched, and the pipeline renders
  it (below). Left as is; noted as a battery-vs-renderer disagreement.
- Pipeline render: `render-latex.ts` has no CLI entry, so I drove
  `markdownToLatex` + `validateLatexAst` directly (scratch script) on all 13 files:
  all 13 `valid`, 0 AST errors.
- `qa-sweep` (full criterion set, no `--only`) on all 13 blocks: 3–6 s each, all exit 0.
  Findings are all pre-existing (already at the same severity in the HEAD sidecars):
  `voice-unicode-crash` at `eightfold-open-problems.md:30` (`…` U+2026) and
  `notation-collisions.md:87` (`→` U+2192) — both lines present in HEAD;
  `voice-author-notes-pollution` (open-problems:30, collisions:41);
  `framework-canonical` (collisions:24, the `$H_q$` bullet);
  `detangler-no-forward-ref` (meson-mass-splitting.ts). My added lines carry only
  `—` (U+2014), which the existing bullets already use.
- `scripts/run-validate.ts content/quantum-observable-universe`: **exit 0**,
  14 pre-existing issues, none in `eightfold-way/` or `notation/`.

**Trap.** A concurrent parent-session edit (bean `qou-lvux`/`qou-8fl1`: lean.ref
repoint in `color-su3-from-g2.ts`, plus `docs/sm-eightfold-derivation-cheat-sheet.md`
and `.beans/qou-8fl1--*.md`) landed at 04:55Z, after my sweep of that block; I re-ran
`qa-sweep` on `color-su3-from-g2.md` so its sidecar ts-hash matches the live `.ts`.
Any further `.ts` edit there re-stales it.

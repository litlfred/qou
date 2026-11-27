# Owner-ruling consistency audit of the qou paper (2026-11-21)

**What this is.** A search of the paper's content blocks and Lean files for text
that contradicts the owner's standing rulings in
[`docs/coordination/owner-rulings.md`](../coordination/owner-rulings.md), with every
candidate site classified. Only clear-cut prose and docstring fixes were made. Everything
else is listed for a decision.

**Baseline.** `origin/main` at `bccf522bb5d`. Line numbers in the tables are line numbers
**at that commit**. The three fix commits on this branch add a line in three Lean
docstrings, so a few Lean line numbers are off by one on the branch tip.

**Scope searched.** `folio/quantum-observable-universe/**/*.md` and `**/*.lean`. Content
`.md` prose, Lean docstrings and comments, Lean statements and identifiers.
**Not searched:** `.ts` manifests (including `authorNotes`), `.jsonld`, `computations/`,
`docs/`, beans, the other two papers (`unital-groebner-bases`, `fred2005-formal-groups`),
and the rendered `chapters/*.tex`. `docs/audits/` and beans were excluded on purpose,
because they are dated records.

**Classes.**

- **A** — stale and clear-cut. The ruling decides the fix, it is a prose or docstring
  change, and no open PR touches the file. **Fixed on this branch.**
- **B** — stale, needs a decision. The fix would change a statement, a number, a
  definition, an identifier or the scoreboard, or the right wording is not obvious.
- **C** — in a file touched by an open PR. Left alone.
- **D** — fine: history, the backup model, explicitly scoped, or not about the ruling.

**Open PRs.** The snapshot is the 31 PRs in `/tmp/claude-0/openprs.txt`, taken at the
start of this session. File lists came from `gh pr diff --name-only`, and for #8702,
whose diff has more than 300 files, from the REST `pulls/8702/files` listing (510 files).
#8702 (voice L4 cross-chapter) touches 166 content `.md` files. It is the PR behind most
class-C rows.

**Method and its limits.** Every table comes from `grep` with several spellings per
ruling, and each spelling is given in the section. A grep finds only the spellings it was
given. In particular:

- The electron search keyed on `trefoil|T(2,3)|T_{2,3}|3_1|3₁|σ₀³|\sigma_0^3|\sigma_1^3|σ₁³`
  together with `electron|lepton|\mathfrak{e}`. It also matched a file **path** containing
  `electron`, so some rows in electron-named files carry no electron word on the line
  itself. A site that writes the electron as a trefoil in a spelling not listed here, for
  example `τ(2,3)` alone or `(2,3)-torus knot`, is missed unless another line of it matched.
- Classification was done by rules, then checked by hand: every A row, every
  B-E2/B-E3/B-E4 row and every D row. **The B-E1 rows were not all read one by one.** They
  are grouped under one decision, so a mis-filed B-E1 row changes no recommendation.
- The two-term search matched sentences of the form "mass/energy … is/equals … tr_M /
  Markov trace" within about 60 characters. A single-trace mass claim phrased differently
  is not in the table.

## Summary

| ruling | A (fixed) | B | C | D |
|---|---:|---:|---:|---:|
| 1. Electron = σ₀σ₁σ₀ (Hopf link); trefoil is the backup | 38 | 370 | 11 | 28 |
| 2. Two-term Lagrangian trace τ(ℒ) | 0 | 40 | 3 | 0 |
| 3. Photon fourth term σ₀σ₁⁻¹ | 0 | 0 | 3 | 51 |
| 4. Up quark is an unknot strand | 0 | 10 | 0 | 81 |
| 5. Q_β from γγ; 0.3254 MeV is Q_β, not m_n − m_p | 0 | 0 | 0 | 8 |

Counts are **lines** (sites), not files. The 38 class-A lines are in **29 files**: 24
content `.md` files and 5 Lean library modules. See "Fixes made" below.

The headline finding: **only the electron ruling has real stale text, and nearly all of it
is class B.** The trefoil-as-electron reading is built into the atomic and chemistry
chapters, the lepton tower, the β-decay skein, several Lean definitions and theorems
(`Calculations.electron_is_trefoil`, `KnotRegistry.trefoilEntry`,
`TrefoilCanonicalMassUnit`), and the introduction. Re-scoping that corpus as the backup
model is one decision for the owner, not a prose sweep. What *was* clear-cut is narrower.
The corpus already used `e⁻ = σ₀σ₁σ₀` as the normal-form basis word, and it called that
word "the trefoil" in 38 lines. The closure of `σ₀σ₁σ₀` on three strands has two
components (`QOU.BraidKnot.ElectronWordCandidates.numCycles_s0s1s0`, sorry-free), so that
label is false whatever the ruling says. Those 38 lines were relabelled.

## Fixes made (class A)

Three commits on `claude/ruling-consistency-audit-2026-11-21`:

1. `content: e⁻ = σ₀σ₁σ₀ is not "the trefoil"` — 23 content blocks. "trefoil" becomes
   "electron word e⁻" or "e⁻ channel", and "(trefoil)" becomes "(closure: Hopf link)".
2. `lean: docstrings stop calling e⁻ = σ₀σ₁σ₀ "the trefoil"` — `QBeta/GramSignature`,
   `QBeta/QBetaZeta4ResidueRefutation`, `BraidKnot/DeltaLambdaSignRule`,
   `BraidsAndKnots/NucleonWeightSpaceTwoTerm`.
3. `content+lean: two more e⁻ = σ₀σ₁σ₀ sites` — `four-term-pair-nucleon.md`,
   `QBeta/SilverAnchorGrounding`.

Rules followed:

- No number, statement, definition body, identifier or `.ts` field was changed.
- One borderline case: `def:breit-wheeler-pair-production` had `\text{ (trefoil)}` beside
  `e^- = \sigma_0\sigma_1\sigma_0` in its display. Only the parenthetical changed; the
  definition did not.
- **The ruling citation is not in the content prose.** Writing "(owner ruling …)" into a
  block's prose is a one-voice status leak (AGENTS.md §4d), and its correct home,
  `authorNotes`, is a `.ts` field this task did not touch. The citation is in the Lean
  docstrings, in each commit message, and here.

**Verification.**

- Lean: `scripts/lean-library-sweep.py --package QOU --only-exact <Module> --shadow
  /tmp/claude-0/shadow-audit --jobs 1` on each of the 5 modules: **5/5 ok, 0 RED**.
  `NucleonWeightSpaceTwoTerm` was built with its 2 dependencies.
- Content: a `$`/`{}` balance check on every added line, all balanced. The edits add no
  line that begins with `+`, `-` or `*` inside `$$`. **The pipeline render
  (`render-latex.ts`) was not run.**

## 1. Electron: σ₀σ₁σ₀ ∈ B₃, closure the Hopf link; trefoil σ₀³ ∈ B₂ is the backup

Spellings searched: `trefoil`, `T(2,3)`, `T_{2,3}`, `3_1`, `3₁`, `σ₀³`, `\sigma_0^3`,
`\sigma_1^3`, `σ₁³`, together with `electron`, `lepton`, `\mathfrak{e}`. Also: lines where
`σ₀σ₁σ₀` (any spelling) sits beside `trefoil`, `T_{2,3}` or `3_1`, and lines where
`trefoil` sits beside `L_±`, `NF`, `basis`, `channel` or `coefficient`.

Decision groups for class B:

- **B-E1 — the trefoil-electron model (281 lines).** The electron as `T_{2,3}` / `σ₁³` in
  `B₂`, and everything built on it:
  - electron shells (`electron-shells-hopf`, `noble-gas-*`, `helium-hopf-diagram`,
    `hydrogen-*`);
  - covalent bonds (`covalent-bond-shared-trefoil`, `molecular-*`);
  - the lepton tower `T(2,3) → T(2,5) → T(2,7)`, the β-decay skein (`beta-decay-skein*`),
    the knot tables and the periodic-table appendix;
  - the positron as the mirror trefoil;
  - quark "lepton partner `T_{2,3}`" labels. The up-quark ruling made these labels; they
    still name the electron as `T_{2,3}`.

  **Decision needed:** keep this corpus as the explicitly-scoped *backup* model (cheapest:
  one framing note per chapter, which the owner should place), or rewrite it on `σ₀σ₁σ₀`.
  A rewrite reopens the shell, bond and lepton-tower constructions, because `σ₀σ₁σ₀`
  lives in `B₃`, not `B₂`, and closes to two components. **Default if nothing is decided:**
  the text keeps presenting the backup as the electron.
- **B-E2 — Lean identifiers and definitions (62 lines).** Examples:
  `Calculations.electron_is_trefoil`, `KnotRegistry.trefoilEntry` (identity
  `.electron`), `DerivedCharacterCatalogue.trefoilTwoElectron*`,
  `TrefoilCanonicalMassUnit.TrefoilElectronMassConj`, `Interactions.TrefoilVanishing`
  (`b3_trefoil_zero`, about the `e⁻` coefficient), `ProtonTrefoilSign`,
  `hopfTrefoilNFCoeffs`, `NFBasis3.trefoil` (`-- e⁻ = σ₀σ₁σ₀`), `Flavor` tables.
  **Decision:** rename (it breaks importers, so it needs a sweep with builds) or re-scope
  the docstrings only.
- **B-E3 — `σ₀σ₁σ₀` named "trefoil" or `T_{2,3}` inside a statement or notation (25
  lines).** Examples:
  - `def:per-nucleon-channel-decomposition` defines "the trefoil operator
    `T_{2,3} = σ₀σ₁σ₀`", in its `.md` and its `.lean`;
  - `molecular-construction/electron-shell-braid-capacity.md:2`, a proposition statement,
    reads "each electron is a trefoil `T_{2,3} = σ₀σ₁…`";
  - `frobenius-gram-matrix-context.md:66`;
  - Lean comment lines in `TrefoilVanishing`.

  The label is false (two components), but the fix changes notation inside a statement,
  so it needs a decision.
- **B-E4 — introduction framing (2 lines).** `introduction/intro-particles-as-knots.md:15`
  says the trefoil "is the electron", and the same sentence says "the Hopf link is the
  strong binding of quarks". Putting the ruling in makes the Hopf link both the electron
  and the gluon. `introduction/chapter-overview.md:37` presents the trefoil electron and
  "higher torus knots" for μ and τ. That is the lepton tower, which is still trefoil-based.
  Both need owner wording.

### Sites

| site (path under `folio/quantum-observable-universe/`, line at `bccf522bb5d`) | quoted phrase | class | action |
|---|---|---|---|
| `appendix-knot-operations-archimedean/gluon-model-comparison.md:33` | `Quarks interact as single-crossing unknots, not as full trefoils (Definition 4.27.1): replacing each crossing …` | A | fixed: relabelled to electron word e⁻ / closure Hopf link |
| `appendix-knot-operations-archimedean/particle-nf-table-table-data.md:17` | `\| $e^-$ \| trefoil $3_1$ \| $\sigma_0\sigma_1\sigma_0$ \| — \| — \| — \| — \| — \| $+1$ \| $+1.000$ \|` | A | fixed: relabelled to electron word e⁻ / closure Hopf link |
| `appendix-knot-operations-archimedean/particle-nf-table-table-data.md:18` | `\| $e^+$ \| mirror $3_1$ \| $\sigma_0^{-1}\sigma_1^{-1}\sigma_0^{-1}$ \| $-0.218$ \| $+0.044$ \| $+0.044$ \| $…` | A | fixed: relabelled to electron word e⁻ / closure Hopf link |
| `appendix-knot-operations-archimedean/particle-nf-table.md:65` | `single-crossing unknot rather than a full trefoil word` | A | fixed: relabelled to electron word e⁻ / closure Hopf link |
| `appendix-knot-operations-archimedean/particle-nf-table.md:66` | `$\sigma_0\sigma_1\sigma_0$: the trefoil assignment triples` | A | fixed: relabelled to electron word e⁻ / closure Hopf link |
| `appendix-knot-operations/knot-operator-basis-table-table1-data.md:11` | `$e^- = \sigma_0\sigma_1\sigma_0$ (the trefoil). The operator $\gamma$` | A | fixed: relabelled to electron word e⁻ / closure Hopf link |
| `appendix-knot-periodic-table/knot-atom-diagrams-sim.md:7` | `- **Electrons**: outlined right trefoils $T_{2,3}^{\sigma}$ (hollow).` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `appendix-knot-periodic-table/knot-atom-diagrams.md:6` | `- **Outline trefoil** (unfilled): right trefoil $T_{2,3}^{\sigma}$ (electron).` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `appendix-knot-periodic-table/knot-atom-diagrams.md:27` | `1. **Hydrogen** ($Z = 1$): A single proton $\mathfrak{p}$ links to a single electron $T_{2,3}$. There are no s…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `appendix-knot-periodic-table/knot-centric-table-intro.md:5` | `electron trefoil resonance modes. Its most natural label is` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `appendix-knot-periodic-table/knot-centric-table-visualization-spec.md:14` | `trefoil-shell structure of its electrons, and the way both respond to` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `appendix-knot-periodic-table/knot-centric-table-visualization-spec.md:35` | `4. **Electron side panel**: show the trefoil writhe diagram:` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `appendix-knot-periodic-table/knot-centric-table.md:100` | `- **Electron knot**: trefoil writhe diagram showing occupied` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `appendix-knot-periodic-table/knot-periodic-table-sim.md:15` | `**electrons** as trefoil knots $T_{2,3} = 3_1$ (closure of` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `appendix-knot-periodic-table/knot-periodic-table.md:135` | `([Borromean baryon](#def:borromean-baryon)), electrons are trefoil` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `appendix-knot-periodic-table/recursive-atom-knot-atlas-open-problems.md:5` | `exactly in symbolic $q$ on the test braids $\sigma_1^3$ (electron) and` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `appendix-knot-periodic-table/recursive-atom-knot-atlas-registry.md:11` | `\| 'principled-derivation' \| Knot is the closure of an explicit $\sigma$-braid word in $H_{n_0}(q_0)$ from [C…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `appendix-knot-periodic-table/recursive-atom-knot-atlas-registry.md:49` | `Word: $\sigma_1^3$. Closure: the **trefoil knot** ($T_{2, 3}$, left-handed, or simplest nontrivial prime knot)…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `appendix-knot-periodic-table/recursive-atom-knot-atlas-registry.md:108` | `**Electron $e^-$** (trefoil)` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `appendix-knot-periodic-table/recursive-atom-knot-atlas-registry.md:242` | `\| Trefoil $3_1$ \| $\sigma_1^3$ \| electron \|` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `appendix-transfer-matrices/tm-knot-pairs.md:30` | `Strands: two up quarks, each an unknot strand of $\mathcal{B}_3$ with positive crossing orientation (lepton pa…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `appendix-transfer-matrices/tm-knot-pairs.md:40` | `Strands: two down quarks, each an unknot strand of $\mathcal{B}_3$ with negative crossing orientation (lepton …` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `appendix-transfer-matrices/tm-knot-pairs.md:50` | `Strands: one up and one down quark, unknot strands of opposite crossing orientation (lepton partners $T_{2,3}$…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `appendix-transfer-matrices/tm-knot-pairs.md:62` | `Knots: $K_1 = \varnothing$ (photon), $K_2 = T_{2,3}$ (electron).` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `appendix-transfer-matrices/tm-knot-pairs.md:109` | `Knots: $K_1 = T_{2,3}$, $K_2 = T_{2,5}$ (lepton partners; the quarks are unknot strands).` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `appendix-transfer-matrices/tm-notation-table3-data.md:11` | `\| Electron $e^-$ \| $T_{2,3}$ \| Positron $e^+$ \| $T_{2,3}^{\sigma}$ \|` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `braids-and-knots/braid-involutions-intro.md:1` | `The three-strand braid group $B_3$ admits two structural involutions that govern discrete symmetries of the pa…` | B-E3 | σ₀σ₁σ₀ named trefoil inside a statement, notation or identifier |
| `braids-and-knots/braid-twist-flip.lean:12` | `The trefoil-knot group is 'B₃ = ⟨σ₁,σ₂ \| σ₁σ₂σ₁ = σ₂σ₁σ₂⟩'; the branched-cover` | D | trefoil as a knot, not as the electron |
| `braids-and-knots/braid-twist-flip.md:12` | `Both are involutions ($\sigma_1^2=\sigma_2^2=\mathrm{id}$). They satisfy the **braid relation** $\sigma_1\sigm…` | D | trefoil as a knot, not as the electron |
| `braids-and-knots/feynman-eigenbasis.md:11` | `The framework supplies a natural eigenbasis from the braided monoidal structure. The braid group acts on $V^{\…` | B-E3 | σ₀σ₁σ₀ named trefoil inside a statement, notation or identifier |
| `braids-and-knots/fundamental-knots-operator-basis.md:6` | `\| electron $e^-$ \| trefoil $3_1 = T(2,3)$ \| torus \| $\sigma_1^3$ \| $\mathrm{Vol}=0$ \|` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `braids-and-knots/hecke-normal-form.lean:17` | `\| trefoil : NFBasis3 -- e⁻ = σ₀σ₁σ₀` | B-E2 | Lean identifier/def encodes e⁻ or electron as trefoil; rename or re-scope |
| `braids-and-knots/holonomy-trefoil.md:13` | `The fundamental group of the trefoil-knot complement has the presentation $\langle x,y\mid xyx=yxy\rangle \con…` | D | trefoil as a knot, not as the electron |
| `braids-and-knots/knot-notation-convention.md:1` | `Particles in this framework are identified with their knots. The notation is $\mathfrak{K}_x^{\pm}$, where $x$…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `brings-surface/archimedean-condition-genus-completeness-genus-ideal-characterisation-intro.md:1` | `The geometric truncation of two-strand torus knots at genus $g = 4$ has an exact algebraic counterpart in the …` | D | trefoil as a knot, not as the electron |
| `brings-surface/archimedean-condition-leptons-intro.md:1` | `Once the Descartes condition fixes the base genus at $g = 4$, the orientation strata of the Reeb flow on $\Sig…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `brings-surface/bring-trefoil-cinquefoil-channel.lean:7` | `# QOU.BringChiralCinquefoil — the trefoil + cinquefoil channel in Bring's Σ₄` | D | trefoil as a knot, not as the electron |
| `brings-surface/bring-trefoil-cinquefoil-channel.lean:26` | `LaTeX label: 'prop:bring-trefoil-cinquefoil-channel'` | D | trefoil as a knot, not as the electron |
| `brings-surface/bring-trefoil-cinquefoil-channel.lean:47` | `/-- **The trefoil + cinquefoil channel** (the provable scaffold).` | D | trefoil as a knot, not as the electron |
| `brings-surface/bring-trefoil-cinquefoil-channel.lean:54` | `-- Ref: [leitner2026] brings-surface/bring-trefoil-cinquefoil-channel` | D | trefoil as a knot, not as the electron |
| `brings-surface/bring-trefoil-cinquefoil-channel.lean:55` | `theorem bring_trefoil_cinquefoil_channel :` | B-E2 | Lean identifier/def encodes e⁻ or electron as trefoil; rename or re-scope |
| `brings-surface/brings-qou-4tuple.md:21` | `The instanton connection $A$ on $P$ is expressed in the resolvent basis $(w_1,\dots,w_4)$ ([Lagrange resolvent…` | B-E3 | σ₀σ₁σ₀ named trefoil inside a statement, notation or identifier |
| `brings-surface/descartes-knot-eigenbasis.lean:598` | `/-- Jones value of the trefoil in the mixed-symmetry (spin-1/2) channel at` | D | trefoil as a knot, not as the electron |
| `brings-surface/descartes-knot-eigenbasis.lean:606` | `the spin-3/2 channel and the trefoil's in the spin-1/2 channel.` | D | trefoil as a knot, not as the electron |
| `brings-surface/descartes-knot-eigenbasis.lean:682` | `unknot's symmetric-channel value and the trefoil's mixed-channel value are` | D | trefoil as a knot, not as the electron |
| `brings-surface/torus-knot-generators-interpretation.md:1` | `1. **Lepton generations.** Charged leptons correspond to $T_{2,3}$ (electron), $T_{2,5}$ (muon), and $T_{2,7}$…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `brings-surface/trivial-knot-photon-interpretation-table3-data.md:6` | `\| (12) \| $\varphi_1\sigma_1 \cdot \psi_{01}V$ \| $\varphi_1\psi_{01}\bigl(e^- - h\,L_-\bigr)$ \| **Vertical …` | A | fixed: relabelled to electron word e⁻ / closure Hopf link |
| `brings-surface/trivial-knot-photon-interpretation-table4-data.md:4` | `\| (14) \| $\varphi_{01}V \cdot \psi_0\sigma_0$ \| $\varphi_{01}\psi_0\bigl(e^- - h^2\sigma_0 - h\,\gamma\bigr…` | A | fixed: relabelled to electron word e⁻ / closure Hopf link |
| `climax-volume-mass/q-energy-terms-and-limits.md:15` | `At a single brane level, this equals $\|\mathrm{tr}_M(\rho(\beta))\|$ ([categorical mass as Markov trace](#pro…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `index-of-definitions/definition-index.md:101` | `\| [def:covalent-bond-shared-trefoil](#def:covalent-bond-shared-trefoil) \| Covalent bond as shared electron t…` | C | PR #8745; left |
| `index-of-definitions/definition-index.md:871` | `\| [prop:bring-trefoil-cinquefoil-channel](#prop:bring-trefoil-cinquefoil-channel) \| The trefoil $+$ cinquefo…` | C | PR #8745; left |
| `index-of-definitions/definition-index.md:1103` | `\| [conj:hydrogen-shell-writhe](#conj:hydrogen-shell-writhe) \| Electron shell number equals writhe level of t…` | C | PR #8745; left |
| `index-of-definitions/definition-index.md:1348` | `\| [ex:electron-knot-concrete](#ex:electron-knot-concrete) \| The electron as the trefoil knot on $\Sigma_4$ \…` | C | PR #8745; left |
| `index-of-definitions/definition-index.md:1354` | `\| [ex:topological-mass-trefoil](#ex:topological-mass-trefoil) \| Topological mass of the trefoil knot (electr…` | C | PR #8745; left |
| `information-theory/composite-crossing-parity.lean:19` | `- 3Z (electron trefoils)` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `information-theory/hydrogen-partition-function.lean:6` | `- Trefoil electron (Vol = 0, mass from vacuum drag)` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `information-theory/hydrogen-partition-function.md:1` | `**Setup.** Consider a monatomic hydrogen gas comprising $N$ atoms of $\mathcal{A}(1,0)$ at quantum temperature…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `information-theory/hydrogen-partition-function.md:28` | `- The proton mass dominates. The term $\mathrm{Vol}(\mathcal{B}_3) / \hbar_q^2$ accounts for $\sim 99.95\%$ of…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `information-theory/jet-planck-particle-spectrum.md:14` | `- **Electron** $e^- = T_{2,3}$` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `information-theory/jet-planck-particle-spectrum.md:17` | `Both appear at the same Planck step. The cubic jet produces both chiralities simultaneously. The same trefoil …` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `information-theory/jet-planck-steps-table1-data.md:6` | `\| 3 \| cubic \| 3 \| $3_1$ \| **Electron** $e^-$, **up** $u$ \| **Positron** $e^+$, **down** $u^{\sigma}$ \| …` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `information-theory/jet-planck-steps-table1-data.md:7` | `\| 3 \| cubic \| 3 \| $3_1^{\sigma}$ \| **Positron** $e^+$, **down** $d$ \| **Electron** $e^-$, $d^{\sigma}$ \…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `information-theory/mass-energy-electron-check.md:4` | `The electron (left trefoil $T_{2,3}$) has $n_c = 3$ positive crossings, so its crossing energy is $\mathfrak{E…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `information-theory/mass-energy-electron-check.md:6` | `Its energy is $\mathfrak{E}(e^-) = \mathfrak{m}_{e^-} \cdot c_q^2$, where $\mathfrak{m}_{e^-}$ is the framing-…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `introduction/chapter-overview.md:37` | `Specific knots map to particle identities: the unknot $0_1$ acts as the neutrino, the trefoil $3_1$ acts as th…` | B-E4 | intro framing; wording collides with Hopf-link=gluon / lepton tower |
| `introduction/intro-particles-as-knots.md:15` | `neutrino; a single over–under knot, the trefoil, is the electron; two` | B-E4 | intro framing; wording collides with Hopf-link=gluon / lepton tower |
| `knots-particles-confinement/binding-knots-visual-inventory-table1-data.md:5` | `\| Trefoil \| $3_1$ \| $\sigma_0^3 \in B_2$ \| electron $e^-$ \| [knot-particle-dictionary](#rem:knot-particle…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `knots-particles-confinement/binding-knots-visual-inventory.md:42` | `The trefoil knot is the simplest non-trivial knot, and the canonical **electron** identity. Its braid word $\s…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `knots-particles-confinement/categorical-meson.md:54` | `Both mesons carry identical Hopf link ($L_+ + L_-$) and trefoil ($e^-$) content, differing only in the single-…` | A | fixed: relabelled to electron word e⁻ / closure Hopf link |
| `knots-particles-confinement/categorical-meson.md:57` | `The dominant $L_+$ term (coefficient $\approx 1.044$) establishes the Hopf link binding. The trefoil component…` | A | fixed: relabelled to electron word e⁻ / closure Hopf link |
| `knots-particles-confinement/categorical-neutron-properties.md:24` | `Relative to the proton ($\mathrm{net} = +1.0065$), the additional down quark demands a larger $L_+$ compensati…` | A | fixed: relabelled to electron word e⁻ / closure Hopf link |
| `knots-particles-confinement/categorical-proton-properties.md:11` | `What survives unchanged is the *scope* of the enumeration. The integer LP dual enumerates all feasible gluon c…` | A | fixed: relabelled to electron word e⁻ / closure Hopf link |
| `knots-particles-confinement/categorical-proton-properties.md:14` | `Applying typed crossings and Hopf link stabilisation yields $\mathrm{net}(\mathfrak{p}) = +1.0065$. The domina…` | A | fixed: relabelled to electron word e⁻ / closure Hopf link |
| `knots-particles-confinement/categorical-proton.lean:10` | `orientation ('def:up-quark'); their lepton partners are T_{2,3} and its` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `knots-particles-confinement/confined-particle-examples.md:8` | `- *'electron': $\ell = 1$, $n_0 = 2$, $[K]_M = [\sigma_1^3]$ (trefoil $3_1$).*` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `knots-particles-confinement/electroweak-triplet-charge-spin-from-involution.lean:640` | `chirality-trefoil-electron-positron'): 'C = σ ↔ σ⁻¹' reverses every crossing, so` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `knots-particles-confinement/electroweak-triplet-charge-spin-from-involution.lean:653` | `chirality-trefoil-electron-positron': 'Q(𝔭^σ) = −Q(𝔭)'). -/` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `knots-particles-confinement/four-term-pair-nucleon-table1-data.md:8` | `\| $e^-$ \| $+0.002$ \| Trefoil channel (4-term only) \|` | A | fixed: relabelled to electron word e⁻ / closure Hopf link |
| `knots-particles-confinement/four-term-pair-nucleon.md:13` | `where $\varphi_{01}\sigma_0\sigma_1^{-1} = \varphi_{01}(L_+ - h\sigma_0)$ is the chiral pair-production vertex…` | A | fixed: relabelled to electron word e⁻ / closure Hopf link |
| `knots-particles-confinement/gluon-stabiliser-ledger.md:5` | `**The trefoil is inside it.** The natural worry is why the stabiliser may not be $e^- = \sigma_0\sigma_1\sigma…` | C | PR #8702; left |
| `knots-particles-confinement/gluon-stabiliser-ledger.md:9` | `**Nor is double counting.** The Hopf gluon does redistribute normal-form weight from $\sigma_1$ into the trefo…` | C | PR #8702; left |
| `knots-particles-confinement/knot-particle-dictionary-table1-data.md:4` | `\| Trefoil \| $T_{2,3}$ ($3_1$) \| $\sigma_0^3 \in B_2$ \| Electron $e^-$ \| $1$ \| $3$ \| Simplest stable vor…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `knots-particles-confinement/knot-particle-generation-table-data.md:4` | `\| $T_{2,3}$ \| Trefoil $3_1$ \| $1$ \| $3$ \| Electron (gen. 1); lepton partner of $\mathfrak{u}$, $\mathfrak…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `knots-particles-confinement/lepton-meson-parallel.md:12` | `\| **First generation** \| $\mathfrak{e}$: $n = 3$ (trefoil) \| $\pi$: quark pair $\bar{u}d$, 6 crossings \|` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `knots-particles-confinement/lepton-meson-torus-knot-dictionary-proof.md:2` | `The lepton assignment follows from the torus-knot mass tower \cite{jones1987}. The electron is the trefoil $T(…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `knots-particles-confinement/lepton-meson-torus-knot-dictionary-proof.md:4` | `The meson assignment uses the quark flavour–lepton partner relation. Each quark is an unknot strand carrying o…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `knots-particles-confinement/lepton-meson-torus-knot-dictionary-proof.md:23` | `\| Role of $4_1$ \| transition knot $T(2,3) \to T(2,5)$ giving mass ratio \| same transition, different evalua…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `knots-particles-confinement/lepton-meson-torus-knot-dictionary.lean:26` | `\| 0 => 3 -- electron: trefoil T(2,3)` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `knots-particles-confinement/nucleon-hecke-element-normal-form.md:14` | `The coefficients $c_\bullet \in \mathbb{Z}[q, q^{-1}]$ encode the particle content of the nucleon: the photon …` | A | fixed: relabelled to electron word e⁻ / closure Hopf link |
| `knots-particles-confinement/pion-mass-hyperbolic-threshold.md:15` | `**This is what forces the calibration set.** The three anchors are CAL-1 $= m_\mathfrak{e}$, CAL-2 $= P_{\math…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `knots-particles-confinement/quark-antiquark-production-reduction.md:8` | `The positive Hopf link $L_+ = \sigma_0\sigma_1$ applied to the trefoil $e^- = \sigma_0\sigma_1\sigma_0$ reduce…` | A | fixed: relabelled to electron word e⁻ / closure Hopf link |
| `knots-particles-confinement/quark-antiquark-production-reduction.md:19` | `The Hopf link operator $L_+$ transmutes the trefoil electron into a virtual crossing $\sigma_1$ plus residual …` | A | fixed: relabelled to electron word e⁻ / closure Hopf link |
| `knots-particles-confinement/quark-antiquark-production.lean:5` | `transmuting the leptonic trefoil channel into a hadronic channel.` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `knots-particles-confinement/quark-antiquark-production.lean:27` | `Applying the positive Hopf link 'L₊ = σ₀σ₁' to the trefoil electron` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `knots-particles-confinement/quark-antiquark-production.lean:37` | `def hopfTrefoilNFCoeffs {R : Type*} [CommRing R] (q : Rˣ) : R × R × R × R :=` | B-E2 | Lean identifier/def encodes e⁻ or electron as trefoil; rename or re-scope |
| `knots-particles-confinement/quark-antiquark-production.lean:43` | `operator: its action on the leptonic trefoil 'e⁻' yields the` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `knots-particles-confinement/quark-antiquark-production.lean:51` | `(hopfTrefoilNFCoeffs q).1 = 1` | B-E2 | Lean identifier/def encodes e⁻ or electron as trefoil; rename or re-scope |
| `knots-particles-confinement/quark-antiquark-production.lean:52` | `∧ (hopfTrefoilNFCoeffs q).2.1 = heckeH q` | B-E2 | Lean identifier/def encodes e⁻ or electron as trefoil; rename or re-scope |
| `knots-particles-confinement/quark-antiquark-production.lean:53` | `∧ (hopfTrefoilNFCoeffs q).2.2.1 = heckeH q` | B-E2 | Lean identifier/def encodes e⁻ or electron as trefoil; rename or re-scope |
| `knots-particles-confinement/quark-antiquark-production.lean:54` | `∧ (hopfTrefoilNFCoeffs q).2.2.2 = (heckeH q) ^ 2 := by` | B-E2 | Lean identifier/def encodes e⁻ or electron as trefoil; rename or re-scope |
| `knots-particles-confinement/quark-antiquark-production.lean:56` | `simp only [hopfTrefoilNFCoeffs]` | B-E2 | Lean identifier/def encodes e⁻ or electron as trefoil; rename or re-scope |
| `knots-particles-confinement/quark-antiquark-production.lean:66` | `(hopfTrefoilNFCoeffs q).2.1 = (hopfTrefoilNFCoeffs q).2.2.1 :=` | B-E2 | Lean identifier/def encodes e⁻ or electron as trefoil; rename or re-scope |
| `knots-particles-confinement/quark-antiquark-production.lean:76` | `(hopfTrefoilNFCoeffs q).1 = 1 ∧` | B-E2 | Lean identifier/def encodes e⁻ or electron as trefoil; rename or re-scope |
| `knots-particles-confinement/quark-antiquark-production.lean:77` | `(hopfTrefoilNFCoeffs q).2.2.2 = (heckeH q) ^ 2` | B-E2 | Lean identifier/def encodes e⁻ or electron as trefoil; rename or re-scope |
| `lean/AUDIT-REPORT.md:52` | `\| 'TrefoilVanishing.lean' \| 98 \| NF uniqueness via Wedderburn-Artin \|` | B-E2 | file name TrefoilVanishing names the e⁻ coefficient |
| `lean/AUDIT-REPORT.md:200` | `\| 'TrefoilVanishing.lean' \| B3 e- coeff = 0 \| 'b3_trefoil_zero : b3_nf_coefficients 5 = 0' \| **Exact** \|` | B-E3 | σ₀σ₁σ₀ named trefoil inside a statement, notation or identifier |
| `lean/QOU/Archimedean/ParticleKnots.lean:60` | `/-- The electron: trefoil knot 'T_{2,3}' in the lepton sector. -/` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `lean/QOU/Archimedean/TorusKnot.lean:74` | `/-- Electron: 'e = τ(2,3)' (trefoil), the up quark's lepton partner; the up` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `lean/QOU/Archimedean/lepton_continuant_generation_exclusion.lean:101` | `'σ'-coefficient of 'T(2,9)' is the product of 'T(2,3)''s coefficient` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `lean/QOU/Archimedean/metallic_character_knot.lean:8` | `*An atom '𝓐(p, n)' with electron cloud '𝓔 = p · T_{2,3}' partitioned` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `lean/QOU/BraidKnot/AJTrefoil.lean:7` | `**The AJ conjecture at the QOU electron knot (trefoil), stated concretely.**` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `lean/QOU/BraidKnot/DeltaLambdaSignRule.lean:451` | `• 'χ^{(2,1)}(σ₀σ₁σ₀) = 0' (trefoil element)` | A | fixed: relabelled to electron word e⁻ / closure Hopf link |
| `lean/QOU/BraidKnot/ElectronWordCandidates.lean:6` | `study found to separate the candidates 'σ₀σ₁σ₀' (the corpus's 'e⁻') and 'σ₀³'` | D | ruling's own record |
| `lean/QOU/BraidKnot/ElectronWordCandidates.lean:7` | `(the trefoil braid in 'B₂ ⊂ B₃').` | D | ruling's own record |
| `lean/QOU/BraidKnot/ElectronWordCandidates.lean:13` | `'σ₀σ₁σ₀', whose closure is the Hopf link, nor 'σ₀³', whose closure is the` | D | ruling's own record |
| `lean/QOU/BraidKnot/ElectronWordCandidates.lean:14` | `trefoil plus a split unknot) closes to a knot on three strands. Positive` | D | ruling's own record |
| `lean/QOU/BraidKnot/ElectronWordCandidates.lean:17` | `2. **'σ₀³' is a rescaled photon.** In any algebra where 'σ₀² = h σ₀ + 1'` | D | ruling's own record |
| `lean/QOU/BraidKnot/ElectronWordCandidates.lean:18` | `(the Hecke relation, 'h = q − q⁻¹'), 'σ₀³ = h·1 + (h² + 1)·σ₀'; when 'h' is a` | D | ruling's own record |
| `lean/QOU/BraidKnot/ElectronWordCandidates.lean:20` | `('1 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁⁻¹'). So in 'H₃(q)' the trefoil braid 'σ₀³' lies in` | D | ruling's own record |
| `lean/QOU/BraidKnot/ElectronWordCandidates.lean:144` | `/-- 'σ₀³' closes to two components on three strands (trefoil ⊔ unknot). -/` | D | ruling's own record |
| `lean/QOU/BraidKnot/ElectronWordCandidates.lean:148` | `/-- '(σ₀σ₁)²' closes to one component (the trefoil as 'T(3,2)'). -/` | D | ruling's own record |
| `lean/QOU/BraidKnot/ElectronWordCandidates.lean:152` | `/-! ### 2. 'σ₀³' is a rescaled photon -/` | D | ruling's own record |
| `lean/QOU/BraidKnot/ElectronWordCandidates.lean:156` | `/-- Under the Hecke relation 'σ₀² = h σ₀ + 1', 'σ₀³ = h·1 + (h² + 1)·σ₀'. -/` | D | ruling's own record |
| `lean/QOU/BraidKnot/ElectronWordCandidates.lean:164` | `/-- When 'h' is a unit (inverse 'u'), 'σ₀³ = h · γ((h² + 1)u, 0, 0)': the trefoil` | D | ruling's own record |
| `lean/QOU/BraidKnot/MesonFusionIndexSelection.lean:135` | `the lepton partner 'T(2,3), T(2,5), T(2,7)' of the generation-'g' quarks` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `lean/QOU/BraidKnot/MmuR9V9Closure.lean:312` | `/-- **Theorem 11 (proved).** Electron framing factor at T(2,3) trefoil:` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `lean/QOU/BraidKnot/QBetaKeystoneInteraction.lean:44` | `/-- The topological crossing number of the electron trefoil (3_1). -/` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `lean/QOU/BraidKnot/QBetaKeystoneInteraction.lean:50` | `/-- The Q_beta interaction factor driven by the T_{3,5} back-reaction on the electron trefoil. -/` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `lean/QOU/BraidKnot/knot_operator_transition.lean:15` | `*The 4th nucleon completes the trefoil topology ('T_{2,3}' = electron),` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `lean/QOU/BraidKnot/knot_operator_transition.lean:38` | `\| 3 => .trefoil -- 4th nucleon: trefoil (= T_{2,3} = electron)` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `lean/QOU/BraidsAndKnots/BorromeanPairwiseLinking.lean:170` | `trefoil — and the trefoil is 'T(2,3)', which the lepton–meson dictionary` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `lean/QOU/BraidsAndKnots/NucleonWeightSpaceTwoTerm.lean:696` | `2. On the Borromean nucleon 'V³ = (σ₀ σ₁⁻¹)³', the trefoil electron coefficient 'c_{e⁻}' is` | A | fixed: relabelled to electron word e⁻ / closure Hopf link |
| `lean/QOU/BraidsAndKnots/QIntegerAlexanderTorus.lean:51` | `'n = 1' gives 'T(2,3)' — the **trefoil**, which is the framework's electron` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `lean/QOU/BraidsAndKnots/QIntegerAlexanderTorus.lean:150` | `electron knot: 'Δ_{3₁}(q) = 1 − q + q²', and it is the framed difference` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `lean/QOU/CODATAChain.lean:219` | `- 'KnotRegistry.trefoilEntry' — electron = trefoil (3₁)` | B-E2 | Lean identifier/def encodes e⁻ or electron as trefoil; rename or re-scope |
| `lean/QOU/Calculations.lean:51` | `unknotEntry (.neutrino) and trefoilEntry (.electron), then` | B-E2 | Lean identifier/def encodes e⁻ or electron as trefoil; rename or re-scope |
| `lean/QOU/Calculations.lean:60` | `-- registry = [unknotEntry(.neutrino), trefoilEntry(.electron), figureEightEntry(.higgsField), ...]` | B-E2 | Lean identifier/def encodes e⁻ or electron as trefoil; rename or re-scope |
| `lean/QOU/Calculations.lean:64` | `/-- The registry entry for the electron is the trefoil.` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `lean/QOU/Calculations.lean:67` | `theorem electron_is_trefoil :` | B-E2 | Lean identifier/def encodes e⁻ or electron as trefoil; rename or re-scope |
| `lean/QOU/Calculations.lean:68` | `(lookupByIdentity .electron) = some trefoilEntry := by` | B-E2 | Lean identifier/def encodes e⁻ or electron as trefoil; rename or re-scope |
| `lean/QOU/Calculations.lean:70` | `-- registry = [unknotEntry, trefoilEntry, ...]; unknotEntry.identity = .neutrino ≠ .electron;` | B-E2 | Lean identifier/def encodes e⁻ or electron as trefoil; rename or re-scope |
| `lean/QOU/Calculations.lean:71` | `-- trefoilEntry.identity = .electron. All kernel-reducible ι-steps.` | B-E2 | Lean identifier/def encodes e⁻ or electron as trefoil; rename or re-scope |
| `lean/QOU/Eightfold/AmphichiralHolonomyIsSelfDual.lean:31` | `\| '3₁' trefoil \| electron \| chiral, but a **torus knot**: 'Vol = 0', complement Seifert-fibred, so no hyper…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `lean/QOU/Excitation/WritheIndexCharacterH2.lean:22` | `Every power 'σ^m', 'm ≥ 2', is non-reduced, the trefoil 'σ³' included; the normal form stays` | D | trefoil as a knot, not as the electron |
| `lean/QOU/Excitation/WritheIndexCharacterH2.lean:123` | `/-- The ground-state trefoil 'σ³' is already non-reduced: 'NF(σ³) = h + (h² + 1)σ'. -/` | D | trefoil as a knot, not as the electron |
| `lean/QOU/Interactions.lean:42` | `- ProtonTrefoilSign: sign analysis of trefoil coefficient` | B-E2 | Lean identifier/def encodes e⁻ or electron as trefoil; rename or re-scope |
| `lean/QOU/Interactions.lean:43` | `- TrefoilVanishing: B₃ trefoil coefficient = 0 (fully proved)` | B-E2 | Lean identifier/def encodes e⁻ or electron as trefoil; rename or re-scope |
| `lean/QOU/Interactions.lean:44` | `- TrefoilCanonicalMassUnit: trefoil as CAL-1 electron mass unit (conditional theorems)` | B-E2 | Lean identifier/def encodes e⁻ or electron as trefoil; rename or re-scope |
| `lean/QOU/Interactions/BetaReceptivity.lean:119` | `combined with b3_trefoil_zero : b3_nf_coefficients 5 = 0. -/` | B-E2 | Lean identifier/def encodes e⁻ or electron as trefoil; rename or re-scope |
| `lean/QOU/Interactions/DemandStability.lean:66` | `to beta decay: it can emit an electron (trefoil) to reduce` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `lean/QOU/Interactions/NucleonNFWitness.lean:80` | `-- The e⁻ coefficient is proved nonzero in HeckeEngine.lean (nf_proton4_trefoil).` | B-E2 | Lean identifier/def encodes e⁻ or electron as trefoil; rename or re-scope |
| `lean/QOU/Interactions/NucleonNFWitness.lean:91` | `Sign: NEGATIVE for q ∈ (1, 3/2] (ProtonTrefoilSign.lean) -/` | B-E2 | Lean identifier/def encodes e⁻ or electron as trefoil; rename or re-scope |
| `lean/QOU/Interactions/NucleonNFWitness.lean:96` | `Sign: ALWAYS NEGATIVE for q > 1 (ProtonTrefoilSign.lean)` | B-E2 | Lean identifier/def encodes e⁻ or electron as trefoil; rename or re-scope |
| `lean/QOU/Interactions/NucleonNFWitness.lean:99` | `analysis needed. This is why neutron_trefoil_neg holds` | B-E2 | Lean identifier/def encodes e⁻ or electron as trefoil; rename or re-scope |
| `lean/QOU/Interactions/ProtonTrefoilSign.lean:16` | `coefficient — it demands a trefoil (electron), which is the` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `lean/QOU/Interactions/TrefoilCanonicalMassUnit.lean:10` | `**The trefoil T(2,3) is the canonical mass unit for the electron.**` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `lean/QOU/Interactions/TrefoilCanonicalMassUnit.lean:21` | `The electron itself is identified with the trefoil knot 'T(2,3)':` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `lean/QOU/Interactions/TrefoilCanonicalMassUnit.lean:36` | `axiomatised as a content-bearing class 'TrefoilElectronMassConj', whose` | B-E2 | Lean identifier/def encodes e⁻ or electron as trefoil; rename or re-scope |
| `lean/QOU/Interactions/TrefoilCanonicalMassUnit.lean:42` | `Downstream theorems conditioned on '[TrefoilElectronMassConj …]' are` | B-E2 | Lean identifier/def encodes e⁻ or electron as trefoil; rename or re-scope |
| `lean/QOU/Interactions/TrefoilCanonicalMassUnit.lean:54` | `elaborate. Every "conditional on 'TrefoilElectronMassConj'" theorem in` | B-E2 | Lean identifier/def encodes e⁻ or electron as trefoil; rename or re-scope |
| `lean/QOU/Interactions/TrefoilCanonicalMassUnit.lean:56` | `identification 'trefoil ↔ electron'" the docstring claimed to encode` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `lean/QOU/Interactions/TrefoilCanonicalMassUnit.lean:94` | `- 'TrefoilVanishing' (e⁻ NF coefficient of B₃ is exactly zero)` | B-E2 | Lean identifier/def encodes e⁻ or electron as trefoil; rename or re-scope |
| `lean/QOU/Interactions/TrefoilCanonicalMassUnit.lean:122` | `/-- The trefoil e⁻ NF coefficient of B₃ is exactly zero (pulled from` | B-E3 | σ₀σ₁σ₀ named trefoil inside a statement, notation or identifier |
| `lean/QOU/Interactions/TrefoilCanonicalMassUnit.lean:142` | `/-- **Primary conjecture: the trefoil is the canonical mass unit for the electron.**` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `lean/QOU/Interactions/TrefoilCanonicalMassUnit.lean:148` | `CODATA electron mass, i.e. the trefoil is the mass **unit**. Since` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `lean/QOU/Interactions/TrefoilCanonicalMassUnit.lean:153` | `This is the open physical identification 'trefoil ↔ electron', not derived` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `lean/QOU/Interactions/TrefoilCanonicalMassUnit.lean:184` | `-- binding-knots-visual-inventory.md §"Trefoil = electron"` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `lean/QOU/Interactions/TrefoilCanonicalMassUnit.lean:185` | `class TrefoilElectronMassConj` | B-E2 | Lean identifier/def encodes e⁻ or electron as trefoil; rename or re-scope |
| `lean/QOU/Interactions/TrefoilCanonicalMassUnit.lean:187` | `/-- The topological mass of the trefoil equals the CODATA electron mass.` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `lean/QOU/Interactions/TrefoilCanonicalMassUnit.lean:201` | `-- binding-knots-visual-inventory.md §"Trefoil = electron"` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `lean/QOU/Interactions/TrefoilCanonicalMassUnit.lean:208` | `-- binding-knots-visual-inventory.md §"Trefoil = electron"` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `lean/QOU/Interactions/TrefoilCanonicalMassUnit.lean:218` | `theorem trefoil_strand_times_crossing_eq_six :` | B-E2 | Lean identifier/def encodes e⁻ or electron as trefoil; rename or re-scope |
| `lean/QOU/Interactions/TrefoilCanonicalMassUnit.lean:234` | `/-- **Theorem (conditional on 'TrefoilElectronMassConj').**` | B-E2 | Lean identifier/def encodes e⁻ or electron as trefoil; rename or re-scope |
| `lean/QOU/Interactions/TrefoilCanonicalMassUnit.lean:243` | `theorem trefoil_topological_mass_pos [ctx : TrefoilElectronMassConj T rho] :` | B-E2 | Lean identifier/def encodes e⁻ or electron as trefoil; rename or re-scope |
| `lean/QOU/Interactions/TrefoilCanonicalMassUnit.lean:248` | `/-- **Theorem (conditional on 'TrefoilElectronMassConj').**` | B-E2 | Lean identifier/def encodes e⁻ or electron as trefoil; rename or re-scope |
| `lean/QOU/Interactions/TrefoilCanonicalMassUnit.lean:258` | `theorem trefoil_cat_mass_normalised [ctx : TrefoilElectronMassConj T rho] :` | B-E2 | Lean identifier/def encodes e⁻ or electron as trefoil; rename or re-scope |
| `lean/QOU/Interactions/TrefoilCanonicalMassUnit.lean:266` | `/-- **Theorem (conditional on 'TrefoilElectronMassConj').** With the cat-unit` | B-E2 | Lean identifier/def encodes e⁻ or electron as trefoil; rename or re-scope |
| `lean/QOU/Interactions/TrefoilCanonicalMassUnit.lean:269` | `theorem trefoil_rho_absTrace_eq_one [TrefoilElectronMassConj T rho] :` | B-E2 | Lean identifier/def encodes e⁻ or electron as trefoil; rename or re-scope |
| `lean/QOU/Interactions/TrefoilCanonicalMassUnit.lean:275` | `/-- **Theorem (conditional on 'TrefoilElectronMassConj').**` | B-E2 | Lean identifier/def encodes e⁻ or electron as trefoil; rename or re-scope |
| `lean/QOU/Interactions/TrefoilCanonicalMassUnit.lean:280` | `theorem trefoil_mass_multiple_pos [TrefoilElectronMassConj T rho]` | B-E2 | Lean identifier/def encodes e⁻ or electron as trefoil; rename or re-scope |
| `lean/QOU/Interactions/TrefoilCanonicalMassUnit.lean:285` | `/-- **Theorem (conditional on 'TrefoilElectronMassConj').**` | B-E2 | Lean identifier/def encodes e⁻ or electron as trefoil; rename or re-scope |
| `lean/QOU/Interactions/TrefoilCanonicalMassUnit.lean:290` | `theorem mass_ratio_pos [TrefoilElectronMassConj T rho]` | B-E2 | Lean identifier/def encodes e⁻ or electron as trefoil; rename or re-scope |
| `lean/QOU/Interactions/TrefoilCanonicalMassUnit.lean:295` | `/-- **Theorem (conditional on 'TrefoilElectronMassConj').**` | B-E2 | Lean identifier/def encodes e⁻ or electron as trefoil; rename or re-scope |
| `lean/QOU/Interactions/TrefoilCanonicalMassUnit.lean:299` | `theorem trefoil_topological_mass_sq_pos [TrefoilElectronMassConj T rho] :` | B-E2 | Lean identifier/def encodes e⁻ or electron as trefoil; rename or re-scope |
| `lean/QOU/Interactions/TrefoilCanonicalMassUnit.lean:303` | `/-- **Theorem (conditional on 'TrefoilElectronMassConj').**` | B-E2 | Lean identifier/def encodes e⁻ or electron as trefoil; rename or re-scope |
| `lean/QOU/Interactions/TrefoilCanonicalMassUnit.lean:308` | `theorem trefoil_mass_times_crossings_pos [TrefoilElectronMassConj T rho] :` | B-E2 | Lean identifier/def encodes e⁻ or electron as trefoil; rename or re-scope |
| `lean/QOU/Interactions/TrefoilVanishing.lean:4` | `# The e⁻ (trefoil) NF coefficient of B₃ is exactly zero` | B-E3 | σ₀σ₁σ₀ named trefoil inside a statement, notation or identifier |
| `lean/QOU/Interactions/TrefoilVanishing.lean:28` | `- Each time σ₀σ₁σ₀ (= e⁻) appears, it's from the braid` | B-E3 | σ₀σ₁σ₀ named trefoil inside a statement, notation or identifier |
| `lean/QOU/Interactions/TrefoilVanishing.lean:29` | `relation σ₁σ₀σ₁ → σ₀σ₁σ₀. But the anti-symmetric structure` | B-E3 | σ₀σ₁σ₀ named trefoil inside a statement, notation or identifier |
| `lean/QOU/Interactions/TrefoilVanishing.lean:174` | `L₊² = L₋ + HA·e⁻ (from Hecke: σ₀σ₁σ₀σ₁ → ...)` | B-E3 | σ₀σ₁σ₀ named trefoil inside a statement, notation or identifier |
| `lean/QOU/Interactions/TrefoilVanishing.lean:196` | `Apply YB to σ₁σ₀σ₁ → σ₀σ₁σ₀:` | B-E3 | σ₀σ₁σ₀ named trefoil inside a statement, notation or identifier |
| `lean/QOU/Interactions/TrefoilVanishing.lean:197` | `= σ₀·σ₀σ₁σ₀ (wrong grouping)... Let me be precise.` | B-E3 | σ₀σ₁σ₀ named trefoil inside a statement, notation or identifier |
| `lean/QOU/Interactions/TrefoilVanishing.lean:199` | `σ₀σ₁σ₀σ₁: look at positions 0,1,2 = σ₀,σ₁,σ₀ → YB → σ₁,σ₀,σ₁` | B-E3 | σ₀σ₁σ₀ named trefoil inside a statement, notation or identifier |
| `lean/QOU/Interactions/TrefoilVanishing.lean:200` | `So σ₀σ₁σ₀σ₁ → σ₁σ₀σ₁·σ₁ = σ₁σ₀·σ₁² = σ₁σ₀·(HA·σ₁+1)` | B-E3 | σ₀σ₁σ₀ named trefoil inside a statement, notation or identifier |
| `lean/QOU/Interactions/TrefoilVanishing.lean:201` | `= HA·σ₁σ₀σ₁ + σ₁σ₀ = HA·e⁻ + L₋ (using YB: σ₁σ₀σ₁=σ₀σ₁σ₀=e⁻)` | B-E3 | σ₀σ₁σ₀ named trefoil inside a statement, notation or identifier |
| `lean/QOU/Interactions/TrefoilVanishing.lean:276` | `theorem b3_trefoil_zero : b3_nf_coefficients 5 = 0 := by rfl` | B-E2 | Lean identifier/def encodes e⁻ or electron as trefoil; rename or re-scope |
| `lean/QOU/KnotRegistry.lean:95` | `QOU identity: **Electron** (Generation 1). The trefoil's braid group` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `lean/QOU/KnotTheory.lean:127` | `In the QOU framework, the trefoil maps to the electron. -/` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `lean/QOU/Machinery/DerivedCharacterCatalogue.lean:327` | `/-! ### Trefoil (B_2) — electron -/` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `lean/QOU/Machinery/DerivedCharacterCatalogue.lean:329` | `/-- Trefoil '(2,)' electron: trivial rep on σ_1³ gives 'q³'. -/` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `lean/QOU/Machinery/DerivedCharacterCatalogue.lean:330` | `def trefoilTwoElectron : KnotPartitionAtomCell where` | B-E2 | Lean identifier/def encodes e⁻ or electron as trefoil; rename or re-scope |
| `lean/QOU/Machinery/DerivedCharacterCatalogue.lean:342` | `def trefoilTwoElectronChi {R : Type*} [CommRing R] (q : R) : R := q^3` | B-E2 | Lean identifier/def encodes e⁻ or electron as trefoil; rename or re-scope |
| `lean/QOU/Machinery/DerivedCharacterCatalogue.lean:344` | `instance {R : Type*} [CommRing R] : IsRMatrixDerived R trefoilTwoElectron where` | B-E2 | Lean identifier/def encodes e⁻ or electron as trefoil; rename or re-scope |
| `lean/QOU/Machinery/DerivedCharacterCatalogue.lean:345` | `storedChi := trefoilTwoElectronChi` | B-E2 | Lean identifier/def encodes e⁻ or electron as trefoil; rename or re-scope |
| `lean/QOU/Machinery/DerivedCharacterCatalogue.lean:346` | `rmatrixChi := trefoilTwoElectronChi` | B-E2 | Lean identifier/def encodes e⁻ or electron as trefoil; rename or re-scope |
| `lean/QOU/Machinery/DerivedCharacterCatalogue.lean:349` | `/-- Trefoil '(1,1)' electron: sign rep on σ_1³ gives '(−q⁻¹)³ = −q⁻³'. -/` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `lean/QOU/Machinery/DerivedCharacterCatalogue.lean:350` | `def trefoilOneOneElectron : KnotPartitionAtomCell where` | B-E2 | Lean identifier/def encodes e⁻ or electron as trefoil; rename or re-scope |
| `lean/QOU/Machinery/DerivedCharacterCatalogue.lean:362` | `def trefoilOneOneElectronChi {R : Type*} [Field R] (q : R) : R := -1 / q^3` | B-E2 | Lean identifier/def encodes e⁻ or electron as trefoil; rename or re-scope |
| `lean/QOU/Machinery/DerivedCharacterCatalogue.lean:364` | `instance {R : Type*} [Field R] : IsRMatrixDerived R trefoilOneOneElectron where` | B-E2 | Lean identifier/def encodes e⁻ or electron as trefoil; rename or re-scope |
| `lean/QOU/Machinery/DerivedCharacterCatalogue.lean:365` | `storedChi := trefoilOneOneElectronChi` | B-E2 | Lean identifier/def encodes e⁻ or electron as trefoil; rename or re-scope |
| `lean/QOU/Machinery/DerivedCharacterCatalogue.lean:366` | `rmatrixChi := trefoilOneOneElectronChi` | B-E2 | Lean identifier/def encodes e⁻ or electron as trefoil; rename or re-scope |
| `lean/QOU/Machinery/DerivedCharacterCatalogue.lean:504` | `/-- Trefoil '(1,1)' electron, division-free: '−(↑q⁻¹)³'. -/` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `lean/QOU/Machinery/DerivedCharacterCatalogue.lean:505` | `def trefoilOneOneElectronChiUnit (q : Rˣ) : R := -((↑q⁻¹ : R)) ^ 3` | B-E2 | Lean identifier/def encodes e⁻ or electron as trefoil; rename or re-scope |
| `lean/QOU/Mass/FigureEightGluingFromMonodromy.lean:17` | `'4₁' (the trefoil control 'σ₁σ₂σ₁σ₂ ↦ T₁T₂', trace '1', is 'trefoil_control_trace_one').` | B-E2 | Lean identifier/def encodes e⁻ or electron as trefoil; rename or re-scope |
| `lean/QOU/Mass/FigureEightGluingFromMonodromy.lean:69` | `/-- Control: the positive braid 'σ₁σ₂σ₁σ₂' (closure the trefoil) has monodromy 'T₁ T₂ = R · L⁻¹'` | D | trefoil as a knot, not as the electron |
| `lean/QOU/Mass/LagrangeResolventCyclicEigenvalue.lean:21` | `a stabilizer root of unity, exactly as claimed. (The trefoil colour channel uses` | D | trefoil as a knot, not as the electron |
| `lean/QOU/Mass/LagrangeResolventCyclicEigenvalue.lean:49` | `holds for the length-3 resolvent — the trefoil colour channel's S₃ sub-DFT,` | D | trefoil as a knot, not as the electron |
| `lean/QOU/MathlibExt/FaddeevQuantumDilogarithm.lean:142` | `knots 'T(2,3) = 3₁' (electron), 'T_{3,5}' (writhe mediator) — carry the bar-ODD` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `lean/QOU/Molecular/shell_filling_rule.lean:82` | `assignment of the 'Z' electron trefoils). -/` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `lean/QOU/Molecular/shell_filling_rule.lean:128` | `occupied sites: parallel electron trefoils have lower 'Φ₁' than` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `lean/QOU/Molecular/shell_filling_rule.lean:245` | `/-- Sites available to the 'Z' electron trefoils. -/` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `lean/QOU/ParticleInteractions/MesonFluxTubeReduction.lean:16` | `are the **crossing counts of their lepton partners** 'T(2,3), T(2,5), T(2,7)',` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `lean/QOU/ParticleInteractions/MesonFluxTubeReduction.lean:184` | `reflection"), instantiated on leptons as electron 'T(2,3)' /` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `lean/QOU/ParticleInteractions/MesonOperatorSelectionT3.lean:15` | `counts of their lepton partners** 'T(2,3), T(2,5), T(2,7)' — generation labels.` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `lean/QOU/ParticleInteractions/WeakIsospinT3Grading.lean:14` | `quark's **lepton partner** ('T(2,3)' the electron, 'T(2,5)' the muon, 'T(2,7)'` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `lean/QOU/QBeta/AfreeThetaConstraint.lean:152` | `carrying no new unknown. The corpus's one candidate, the electron/trefoil '3₁'` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `lean/QOU/QBeta/GramSignature.lean:18` | `'γ' the identity and 'e⁻ = σ₀σ₁σ₀' the trefoil. A Gram matrix of a trace pairing` | A | fixed: relabelled to electron word e⁻ / closure Hopf link |
| `lean/QOU/QBeta/QBetaZeta4ResidueRefutation.lean:173` | `'{𝟏, σ₀, σ₁, σ₀σ₁, σ₁σ₀, σ₀σ₁σ₀}' (knots unknot / virtual / Hopf / trefoil)` | A | fixed: relabelled to electron word e⁻ / closure Hopf link |
| `lean/QOU/QBeta/QBetaZeta4ResidueRefutation.lean:178` | `- **virtual (σ₀, σ₁; 1 crossing) → 0** and **trefoil (σ₀σ₁σ₀; 3 crossings) → 0**:` | A | fixed: relabelled to electron word e⁻ / closure Hopf link |
| `lean/QOU/QBeta/SilverAnchorGrounding.lean:16` | `GB-reduced trefoil coefficient, and 'Δ(net)(1+√2) = 82216 + 58136·√2 ≠ 0'` | A | fixed: relabelled to electron word e⁻ / closure Hopf link |
| `lean/QOU/StandardModel/ChiralFermionBraidWords.lean:13` | `> spectrum. The electron ('T_{2,3}') and neutrino ('K_{0₁} = T_{2,1}') are the` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `lean/QOU/StandardModel/LeptonNumberCarrierChirality.lean:20` | `\| 'e⁻' \| 'T(2,3)' (trefoil) \| '+1' \|` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `lean/QOU/StandardModel/LeptonNumberCarrierChirality.lean:21` | `\| 'e⁺' \| 'T(2,3)^σ' (mirror trefoil) \| '-1' \|` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `lean/QOU/StandardModel/WritheLevelParity.lean:331` | `leptons ('σ₁', 'σ₁³': one component, odd) and the Borromean baryon (three` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `lean/QOU/Torsion/antiparticle_crossing_reversal.lean:65` | `Let $T_{2,3}$ be the left trefoil (the electron generator) and` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `mass-endomorphism/mass-endomorphism-conjecture.md:142` | `**(a) Figure-eight $4_1$ as Higgs coupling.** The figure-eight knot $4_1 = (\sigma_0\sigma_1^{-1})^2$ is the g…` | C | PR #8702; left |
| `mass-endomorphism/qbeta-toroidal-harmonics-basis.md:1` | `**Proposition (Toroidal Harmonics Global Basis).** *The continuum limit of the discrete multiblock Habiro knot…` | B-E3 | σ₀σ₁σ₀ named trefoil inside a statement, notation or identifier |
| `mass-theory/atom-knot-mass-derivation-proof.md:104` | `the explicit $\sigma$-words are direct (electron $\sigma_1^3$ in` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `mass-theory/atom-knot-mass-derivation-table3-data.md:6` | `\| electron \| $\sigma_1^3 = T_{2,3}$ \| 0.577 \| 0.423 \| sign block $\rho_{(1,1)} = -q^{-3}$ negative (algeb…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `mass-theory/breit-wheeler-vertex-literature.md:3` | `**Braid-preon mapping.** The Bilson-Thompson topological preon model maps fermions to framed braids in $B_3$, …` | B-E3 | σ₀σ₁σ₀ named trefoil inside a statement, notation or identifier |
| `mass-theory/breit-wheeler-vertex.md:32` | `The product is the normal-form basis element $L_+$, a two-strand entangled state. Applying a substrate Reeb in…` | A | fixed: relabelled to electron word e⁻ / closure Hopf link |
| `mass-theory/breit-wheeler-vertex.md:36` | `The positron $e^+$ is supplied by the mirror process $\sigma_0^{-1}\sigma_1^{-1}\sigma_0^{-1}$. The complete v…` | A | fixed: relabelled to electron word e⁻ / closure Hopf link |
| `mass-theory/frobenius-gram-matrix-context.md:65` | `The electron dual $e^{-\vee}$ pairs with $T_{2,3}$ (trefoil)` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `mass-theory/frobenius-gram-matrix-context.md:66` | `with coefficient $1$ — the Frobenius dual selects the trefoil` | B-E3 | T_{2,3} label on the e⁻ dual inside a statement |
| `mass-theory/jet-filtered-knot-factor.md:4` | `At higher jet levels, the per-level invariant converges strictly to a topology-independent $q$-dimension-weigh…` | B-E3 | σ₀σ₁σ₀ named trefoil inside a statement, notation or identifier |
| `mass-theory/lepton-bring-surface-h3-3channel.md:17` | `Evaluating the electron $\sigma_1^3$ recovers the calibration $\hat V_e^{\mathrm{full}} \approx 0.586$. The ta…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `mass-theory/lepton-mass-tower-canonical.lean:16` | `- trefoil_reduction: σ_1³ = (h²+1)σ_1 + h via Hecke relation` | B-E2 | Lean identifier/def encodes e⁻ or electron as trefoil; rename or re-scope |
| `mass-theory/lepton-mass-tower-canonical.lean:80` | `/-- **THEOREM (algebraic).** Trefoil σ_1³ reduction in H_2(q):` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `mass-theory/lepton-mass-tower-canonical.lean:83` | `theorem trefoil_reduction` | B-E2 | Lean identifier/def encodes e⁻ or electron as trefoil; rename or re-scope |
| `mass-theory/lepton-mass-tower-canonical.lean:93` | `/-- **THEOREM (corollary).** Generalisation of trefoil reduction` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `mass-theory/lepton-mass-tower-canonical.lean:185` | `\| LeptonType.electron => 1 -- σ_1³ = T(2,3) trefoil` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `mass-theory/lepton-mass-tower-canonical.lean:199` | `ratio is determined by the torus-knot step T(2,3) → T(2,5) via` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `mass-theory/lepton-mass-tower-canonical.md:20` | `1. **Nonzero on torus knots.** The electron $T(2,3)$ and tau $T(2,7)$ are torus knots. Their hyperbolic volume…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `mass-theory/mass-element-nf.md:65` | `For the electron (trefoil, $\mathrm{Li}_2(q^{-2})/\hbar_q^2$` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `mass-theory/mass-element-nf.md:84` | `channels** ($\sigma_0, \sigma_1$), not by the trefoil` | A | fixed: relabelled to electron word e⁻ / closure Hopf link |
| `mass-theory/mass-from-generators.md:6` | `A single Hopf linking on the exceptional divisor generates leptonic mass. The Skein resolution of the crossing…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `mass-theory/mass-physical-face-intro.md:1` | `Specialising the six-term algebraic mass functional to the calibrated substrate parameter $q_0 \approx 1.1100$…` | B-E3 | σ₀σ₁σ₀ named trefoil inside a statement, notation or identifier |
| `mass-theory/meson-color-tube-uniqueness.md:8` | `The pair $\{T(2, 3), T(2, 4)\}$ is the smallest non-trivial torus-knot pair on the substrate's Hecke-algebra s…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `mass-theory/molecular-bond-binding-from-trefoil-insertion.lean:16` | `For 'n' inserted inverse trefoils (multiple bonds), each per-channel` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `mass-theory/molecular-bond-binding-from-trefoil-insertion.md:1` | `*A covalent bond functions categorically as an inverse trefoil $T^{-1}$ inserted between two atomic braids $\m…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `mass-theory/qbeta-odd-carrier-hopf-cubic.md:41` | `\| trefoil ($\sigma_0\sigma_1\sigma_0$) \| 3 \| $0$ \|` | A | fixed: relabelled to electron word e⁻ / closure Hopf link |
| `mass-theory/qbeta_c3_keystone_interaction.lean:11` | `/-- The topological crossing number of the electron trefoil (3_1). -/` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `mass-theory/qbeta_c3_keystone_interaction.lean:17` | `/-- The Q_beta interaction factor driven by the T_{3,5} back-reaction on the electron trefoil. -/` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `mass-theory/reidemeister-mass-invariance.md:46` | `$\mathrm{Vol}(T_{2,3}) = 0$) does not change when the electron` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `mass-theory/reidemeister-mass-invariance.md:137` | `electron is still a trefoil (knot type unchanged by R-I). But` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `mass-theory/skein-generation-hadron-reading.md:1` | `In the particle dictionary, a knot type is *fundamental* if it is the unknot or a torus knot: the unknot (neut…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `mass-theory/topological-field-ansatz-table-data.md:5` | `\| Electron \| Trefoil ($T_{2,3}$) \| Simplest stable vortex; gen. 1 ($\deg\alpha_V = 1$) \|` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `mass-theory/topological-mass-trefoil.md:2` | `*The two mass scales attached to the trefoil $\tau(2,3)$ (electron knot) and the figure-eight $4_1$ (Higgs kno…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `mass-theory/topological-mass-trefoil.md:10` | `is therefore not an analytic continuation of the volume. It survives only as the natural-units rendering of th…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `mass-theory/topological-mass-trefoil.md:18` | `This equals the muon-to-electron mass ratio through the CAL-2 identity $m_\mu/m_e = \mathrm{Vol}(4_1)/\hbar_q^…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `mass-theory/transfer-matrix-operator-properties.md:91` | `\| $e$-$\mathfrak{p}$ \| $T_{2,3}$ \| $\mathcal{B}_3$ \| Electron-nucleus Coulomb \|` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `mass-theory/transfer-matrix-operator-properties.md:92` | `\| $e$-$e$ \| $T_{2,3}$ \| $T_{2,3}$ \| Electron-electron repulsion \|` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `mass-theory/transfer-matrix-operator-properties.md:130` | `a curl is added to the electron trefoil, changing its writhe` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `molecular-construction/co2-computation-intro.md:1` | `With heteronuclear bonding in place, add a third atom. Carbon dioxide $CO_2$ as a molecular braid couples a ce…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `molecular-construction/covalent-bond-shared-trefoil.lean:2` | `-- Covalent bond as shared electron trefoil` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `molecular-construction/covalent-bond-shared-trefoil.lean:6` | `/-- A **covalent bond** of order k consists of k electron trefoils` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `molecular-construction/covalent-bond-shared-trefoil.md:2` | `*A **covalent bond of order $k$** between atoms $i$ and $j$ is the Hopf linking of $k$ electron trefoils acros…` | B-E3 | σ₀σ₁σ₀ named trefoil inside a statement, notation or identifier |
| `molecular-construction/electron-shell-braid-capacity.md:2` | `*In the [atomic braid](#def:atomic-braid) $\mathcal{A}(Z, N)$, each of the $Z$ electrons is a trefoil $T_{2,3}…` | B-E3 | σ₀σ₁σ₀ named trefoil inside a statement, notation or identifier |
| `molecular-construction/electron-shells-intro.md:1` | `Before molecules are assembled, atomic bonding capacity is determined. The electron shell translates atomic sh…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `molecular-construction/h2-computation-intro.md:1` | `The smallest covalent molecule comes next. The hydrogen molecule $H_2$ as a braid in $H_4(q)$ places two proto…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `molecular-construction/molecular-braid.lean:13` | `3. Hopf-linking shared electron trefoils` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `molecular-construction/molecular-braid.md:12` | `3. **Shared-electron Hopf linking.** For each covalent bond $b \in \mathcal{B}$ connecting atoms $i$ and $j$ w…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `molecular-construction/molecular-hecke-algebra-intro.md:1` | `This section extends the atomic constructor to multi-atom systems. The molecular braid joins pre-computed atom…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `molecular-construction/shell-filling-rule-aufbau-hund.md:5` | `2. Within the valence shell, electrons distribute to maximise the number of singly occupied sites (Hund's rule…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `molecular-construction/shell-filling-rule.md:1` | `*The ground-state electron configuration of atom $(Z, N)$ is the assignment of $Z$ electron trefoils to bondin…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `notation/notation-register-section-intro.md:1` | `**Reading convention: every object here is mathematical by default.** The symbols in these tables name *constr…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `nuclear-interactions/confinement-operator-selection-interpretation.md:12` | `- $e^- < 0$: **trefoil deficit**—the nucleon possesses a topological deficit corresponding to an electron. Thi…` | A | fixed: relabelled to electron word e⁻ / closure Hopf link |
| `nuclear-interactions/hydrogen-derived-nf.md:29` | `The $e^-$ coefficient flips from $-0.043$ (unbound proton) to $+0.080$ (hydrogen atom). The Hopf linking with …` | A | fixed: relabelled to electron word e⁻ / closure Hopf link |
| `nuclear-interactions/li6-derived-nf.md:27` | `4. The $e^-$ coefficient is positive. The nucleus absorbs the trefoil deficit. The positive $e^-$ means the nu…` | A | fixed: relabelled to electron word e⁻ / closure Hopf link |
| `nuclear-interactions/nucleon-nf-observability.md:19` | `- **$\ell = 3$**: The product $\sigma_0\sigma_1\sigma_0$ is the trefoil knot. It is observable.` | A | fixed: relabelled to electron word e⁻ / closure Hopf link |
| `nuclear-interactions/per-nucleon-channel-decomposition.lean:51` | `are the quadratic-root eigendata of 'T_{2,3} = σ₀σ₁σ₀' in the 2-dim` | B-E3 | σ₀σ₁σ₀ named trefoil inside a statement, notation or identifier |
| `nuclear-interactions/per-nucleon-channel-decomposition.md:17` | `The trefoil operator $T_{2,3} = \sigma_0 \sigma_1 \sigma_0$ in $H_3(q)$ has four eigenvalues corresponding to …` | B-E3 | σ₀σ₁σ₀ named trefoil inside a statement, notation or identifier |
| `nuclear-interactions/two-photon-pair-production.md:12` | `*One operator twists two strands into a left-handed trefoil (the electron $e^-$). The bar-conjugate operator s…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `observations/borromean-quark-table-data.md:4` | `\| 3 \| Trefoil \| Knot \| 1 \| 1 \| Electron (gen. 1) \|` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `observations/breit-wheeler-pair-creation-intro.md:1` | `At high photon energies, the Breit–Wheeler process $\gamma\gamma \to e^+e^-$ tests the elementary Hecke vertex…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `observations/building-block-knots-table1-data.md:5` | `\| Left trefoil \| $T_{2,3}$ \| $3_1$ \| $1$ \| $3$ \| ● \| $e^-$ (electron); lepton partner of $\mathfrak{u}$…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `observations/building-block-knots-table1-data.md:6` | `\| Right trefoil \| $T_{2,3}^{\sigma}$ \| $3_1^{\sigma}$ \| $1$ \| $3$ \| ○ \| $e^+$ (positron); lepton partne…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `observations/building-block-knots-table7-data.md:4` | `\| $e^-$ \| $T_{2,3}$ \| $3$ \| $0$ \| $3q = 3.330$ \| $3\mathfrak{E}_{\times}$ \| $3\mathfrak{E}_{\times}\mu_…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `observations/building-block-knots-table7-data.md:5` | `\| $e^+$ \| $T_{2,3}^{\sigma}$ \| $3$ \| $0$ \| $3q^{-1} = 2.703$ \| $3\mathfrak{E}_{\times}$ \| $3\mathfrak{E…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `observations/building-block-knots-table7-data.md:8` | `\| $u,d$ (quarks) \| $T_{2,3}$ \| $3$ \| $0$ \| $3q$ \| $3\mathfrak{E}_{\times}$ \| (bound; see below) \|` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `observations/building-block-knots.lean:181` | `The electron is the trefoil knot T_{2,3} with 3 crossings` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `observations/building-block-knots.md:40` | `- **Torus knots** ($\mathrm{Vol} = 0$): Mass comes from crossing energy. The trefoil yields $m_{e} = 3 \cdot \…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `observations/complex-chirality-rotation.lean:21` | `- '[leitner2026]' 'rem:chirality-trefoil-electron-positron'` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `observations/complex-chirality-rotation.md:21` | `The discrete electron/positron flip ([chirality remark](#rem:chirality-trefoil-electron-positron)) is the endp…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `observations/complexity-interpretation-intro.md:5` | `- **Virtual pairs, CP violation, and electron stability:** Excitations of the exceptional divisor account for …` | C | PR #8702; left |
| `observations/electron-immortality.md:5` | `The electron avoids beta decay through topological necessity. The electron trefoil $T_{2,3}$ possesses no inte…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `observations/electron-immortality.md:11` | `\| Electron \| $T_{2,3}$ \| None \| **No** \|` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `observations/electron-immortality.md:28` | `If the [cosmological chirality flip](#rem:cosmological-chirality-flip) holds, CMB radiation carries topologica…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `observations/hadron-half-life-verification-table1-data.md:3` | `\| $m_e$ (electron mass) \| $3m_e/3$ \| 3 crossings of trefoil $T_{2,3}$ \|` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `observations/hydrogen-knot-structure-table1-data.md:8` | `\| $e^-$ \| Trefoil $T_{2,3}$ \| 1 \| Electron \|` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `observations/hydrogen-knot-structure.md:11` | `\underbrace{T_{2,3}}_{e^-\text{ (electron)}}` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `observations/hydrogen-knot-structure.md:24` | `The proton's $938$ MeV derives entirely from the Borromean linking of three massless unknots. The electron's $…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `observations/hydrogen-knot-structure.md:28` | `The electron $T_{2,3}$ is Hopf-linked to the proton at the ground state ($n = 1$). The ionization energy is:` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `observations/mass-predictions-method-feynman-qou-comparison-intro.md:1` | `To benchmark the categorical trace calculus against standard perturbative quantum field theory, this section c…` | B-E3 | σ₀σ₁σ₀ named trefoil inside a statement, notation or identifier |
| `observations/pair-creation-energy.md:18` | `The electron is the left trefoil $T_{2,3}$ with $n_c = 3$ positive` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `observations/skein-mass-relation-proof.md:1` | `The electron is identified with the trefoil $3_1$. This torus knot has $\mathrm{Vol}_q(\beta_{3_1}) = 0$ in $\…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `observations/strangelet-intro.md:1` | `In the lepton-partner reading of the quark sector ([knot–particle dictionary](#rem:knot-particle-dictionary)),…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `observations/strangelet-merger-signature.md:4` | `When two neutron stars collide, tidal forces decompress the strangelet cores. As density drops below the hyper…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `observations/strangelet-witten-stability.md:11` | `Replacing down quarks (lepton partner $T_{2,3}^{\sigma}$, $3$ negative crossings) with strange quarks (lepton …` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `observations/strangelet-witten-stability.md:77` | `Witten posited a "strange force" mediating attraction between strangelets. In QOU, this is the $5$-crossing co…` | B-E1 | quark lepton-partner trefoil vs cinquefoil |
| `observations/symmetry-preserving-leptons.md:5` | `\text{electron} \;=\; T_{2,3},` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `observations/symmetry-preserving-leptons.md:16` | `\| electron \| $T_{2,3}$ \| $\mathbb{Z}_3$ \| yes (3-cycle) \| **symmetry-preserving** \|` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `observations/terminal-resolution-cz.lean:18` | `- Electron (trefoil 3₁): Vol(K) = 0, m_e = 0.511 MeV (baseline)` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `observations/terminal-resolution-cz.md:19` | `\| Electron ($3_1$) \| 0 (non-hyp.) \| $m_e$ (baseline) \| 0.511 MeV \|` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `observations/time-reversal-energy-barrier.md:1` | `The Feynman--Stueckelberg interpretation frames the [positron](#def:positron-knot) as a backward-traveling ele…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `observations/time-reversal-energy-barrier.md:4` | `The electron is the left trefoil $T_{2,3}$. No continuous deformation links $T_{2,3}$ to $T_{2,3}^{\sigma}$ ([…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `observations/time-reversal-energy-barrier.md:13` | `The proton is a [Borromean baryon](#def:borromean-baryon): $\mathfrak{p} = [\mathfrak{u}, \mathfrak{u}, \mathf…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `observations/trefoil-vortex-chirality-flip.md:1` | `Can a vortex tube reverse its circulation? ([chirality remark](#rem:chirality-trefoil-electron-positron)). Cla…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `organic-chemistry/carbon-valence.md:1` | `Carbon ($p = 6$) has electron cloud $6 \cdot T_{2,3}$ partitioned as` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `organic-chemistry/carbon-valence.md:16` | `2. **Symmetric energy landscape**: adding a trefoil and removing a trefoil cost comparable crossing energy. Ca…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/antineutrino-knot.md:18` | `The electron $T_{2,3}$ carries topological mass via crossing energy. The antineutrino $T_{1,0}^{\sigma}$ carri…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/antineutrino-knot.md:20` | `The $L_0^{\pm}$ smoothing strictly produces one fermion knot ($T_{2,3}$ or $T_{2,3}^{\sigma}$) and one (anti)n…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/antiparticle-crossing-reversal.lean:17` | `- [leitner2026] Ch. 6, §chirality-trefoil-electron-positron` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/antiparticle-crossing-reversal.lean:64` | `-- Ref: [leitner2026] Ch. 6, §chirality-trefoil-electron-positron` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/antiparticle-crossing-reversal.lean:73` | `-- Ref: [leitner2026] Ch. 6, §chirality-trefoil-electron-positron` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/antiparticle-crossing-reversal.lean:93` | `-- Ref: [leitner2026] Ch. 6, §chirality-trefoil-electron-positron` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/antiparticle-crossing-reversal.md:1` | `The left trefoil $T_{2,3}$ represents the electron generator. Its mirror image $T_{2,3}^{\sigma}$ has all cros…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/beta-decay-skein-properties.md:37` | `\| $3$ \| Electron $T_{2,3}$ (trefoil) \| $3$ positive crossings \|` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/beta-decay-skein-properties.md:45` | `Gröbner–Shirshov reduction partitions the $10$ crossings of $T_{3,5}$. The electron trefoil takes $3$. The neu…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/beta-decay-skein-properties.md:64` | `\| electron $T_{2,3}$ \| positron $T_{2,3}^{\sigma}$ \|` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/beta-decay-skein-properties.md:84` | `Gröbner–Shirshov reduction decomposes the $T_{3,5}$ braid $(\sigma_1 \sigma_2)^5$ into the lepton pair and a r…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/beta-decay-skein-properties.md:115` | `1. Extract the $3$-crossing electron trefoil from the $T_{3,5}$ decomposition.` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/beta-decay-skein.lean:13` | `- 3 crossings → electron trefoil T_{2,3}` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/beta-decay-skein.lean:46` | `/-- Crossings allocated to the electron trefoil T_{2,3}. -/` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/beta-decay-skein.lean:97` | `- 3 crossings → electron trefoil T_{2,3}` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/beta-decay-skein.lean:101` | `Produces: daughter nucleus + electron T_{2,3} + antineutrino K_{0_1}. -/` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/beta-decay-skein.lean:114` | `/-- The electron mass (trefoil T_{2,3}). -/` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/beta-decay-skein.lean:143` | `/-- The positron mass (mirror trefoil σ(T_{2,3})); same as electron mass. -/` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/breit-wheeler-pair-production-derivation.md:89` | `Activating $\varphi_{01} \neq 0$ recovers the full photon. The product of two photons spans all six normal-for…` | A | fixed: relabelled to electron word e⁻ / closure Hopf link |
| `predicted-spectra/breit-wheeler-pair-production-derivation.md:95` | `so the trefoil channel needs the vertex term of one photon and a single-crossing term of the other. For the ei…` | A | fixed: relabelled to electron word e⁻ / closure Hopf link |
| `predicted-spectra/breit-wheeler-pair-production.md:14` | `e^- = \sigma_0\sigma_1\sigma_0 \text{ (trefoil)}, \qquad` | A | fixed: relabelled to electron word e⁻ / closure Hopf link |
| `predicted-spectra/breit-wheeler-pair-production.md:15` | `e^+ = \sigma_0^{-1}\sigma_1^{-1}\sigma_0^{-1} \text{ (mirror trefoil)}.` | A | fixed: relabelled to electron word e⁻ / closure Hopf link |
| `predicted-spectra/chirality-trefoil-electron-positron.md:1` | `The left trefoil $T_{2,3}$ and right trefoil $T_{2,3}^{\sigma}$ represent the electron and positron. The chira…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/chirality-trefoil-electron-positron.md:5` | `Antihadron construction replaces every $T_{2,3}$ with $T_{2,3}^{\sigma}$ in the knot formula. Mirroring yields…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/chirality-trefoil-electron-positron.md:13` | `Here $u^{\sigma} = T_{2,3}^{\sigma}$ and $d^{\sigma} = (T_{2,3}^{\sigma})^{\sigma} = T_{2,3}$. The crossing en…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/chirality-trefoil-electron-positron.md:17` | `Traversing the exceptional divisor of the brane tower reverses the chirality of a trefoil. This maps $T_{2,3}$…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/electron-knot-example.md:1` | `The electron represents the simplest nontrivial torus knot embedded on $\Sigma_4$: the trefoil $T_{2,3}$. Its …` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/electron-knot-example.md:4` | `J_{T_{2,3}}(q) = -q^{-4} + q^{-3} + q^{-1}` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/electron-knot-example.md:7` | `This example records the trefoil geometry only. The electron mass $m_e$ is CAL-1, the leptonic mass-scale inpu…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/electron-knot.lean:7` | `# QOU.Archimedean.Electron — Trefoil T_{2,3} (lepton sector)` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/electron-knot.lean:9` | `The electron is the trefoil knot T_{2,3} in the lepton sector.` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/electron-knot.lean:28` | `/-- The electron trefoil is a torus knot T_{2,3}. -/` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/electron-knot.lean:36` | `/-- The trefoil has crossing number 3. -/` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/electron-knot.lean:43` | `/-- Torus knots are non-hyperbolic: Vol(T_{2,3}) = 0. -/` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/electron-knot.md:1` | `The **electron** corresponds to the trefoil knot $T_{2,3}$ in the lepton sector.` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/electron-knot.md:4` | `e^- = T_{2,3} \qquad \text{(trefoil, solid ●)}` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/electron-knot.md:7` | `It is the lepton partner of the [up quark](#def:up-quark) in the [knot–particle dictionary](#rem:knot-particle…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/electron-knot.md:9` | `The electron is drawn as a solid trefoil to denote the forward time direction.` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/electron-knot.md:11` | `Only the knot identification is fixed. The numerical value of $m_e$ is CAL-1, the leptonic mass-scale input us…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/electron-shells-hopf.lean:7` | `factorization of the multi-electron trefoil chain. A maximal` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/electron-shells-hopf.lean:9` | `trefoils; the noble gases are the atoms whose electron cloud` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/electron-shells-hopf.lean:27` | `at linking level 'n' consists of exactly '2n²' trefoils. -/` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/electron-shells-hopf.md:1` | `The electron configuration of atoms is derived from the **closed sub-Hopf link structure** of the multi-electr…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/electron-shells-hopf.md:5` | `A neutral atom with $Z$ protons binds $Z$ electrons. Each electron forms a trefoil $T_{2,3}$. The stable atom …` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/electron-shells-hopf.md:12` | `\underbrace{p \cdot T_{2,3}}_{\text{electron cloud}}.` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/electron-shells-hopf.md:15` | `The electron cloud $p \cdot T_{2,3}$ forms a chain of $p$ trefoils bound by Hopf links. An **electron shell** …` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/electron-shells-hopf.md:19` | `The helium electron cloud $T_{2,3} \oplus T_{2,3}$ forms a Hopf link of two trefoils. This pair acts as a **cl…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/electron-shells-hopf.md:25` | `The conjecture is that the maximum number of trefoils in a closed sub-Hopf link at level $n$ fixes the shell c…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/electron-shells-hopf.md:29` | `\| 1 \| 2 \| 2 \| He (= noble) \| $T_{2,3} \oplus T_{2,3}$ \|` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/electron-shells-hopf.md:30` | `\| 2 \| 8 \| 10 \| Ne (= noble) \| $8 \cdot T_{2,3}$ (Hopf $8$-chain) \|` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/electron-shells-hopf.md:31` | `\| 3 \| 18 \| 28 \| Ni (**not** noble) \| $18 \cdot T_{2,3}$ \|` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/electron-shells-hopf.md:32` | `\| 4 \| 32 \| 60 \| Nd (**not** noble) \| $32 \cdot T_{2,3}$ \|` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/electron-shells-hopf.md:44` | `2. **Absorption**: The photon energy opens a crossing in the electron sub-Hopf link. This elevates the trefoil…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/electron-shells-hopf.md:51` | `The stability of the electron–hadron interaction bounds the number of electron shells. The outermost trefoil m…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/electron-shells-hopf.md:64` | `1. **Shell capacity derivation**: Prove that the maximum number of trefoils in a closed sub-Hopf link at level…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/francium-extremal-metal.md:15` | `The inner $86$ trefoils form the radon core. These six fully closed sub-Hopf links interlock every curl. The $…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/francium-extremal-metal.md:21` | `2. **Maximal shell depth**: $n = 7$. The crossing energy scales as $\mathfrak{E}_{\mathrm{cross}} \propto 1/n^…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/francium-extremal-metal.md:36` | `Fluorine ($p = 9$) anchors the opposite end of the spectrum. It holds $\|R\| = 7$ trefoils out of a shell-$2$ …` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/fundamental-particles-intro.md:9` | `5. **Composite atomic shells and the periodic table:** Eigenvalues of the electron-strand transfer operator an…` | C | PR #8702; left |
| `predicted-spectra/fundamental-particles-intro.md:12` | `This opening section defines the first-generation lepton knot assignments—the electron and positron trefoils (…` | C | PR #8702; left |
| `predicted-spectra/hadron-half-life-proof.md:3` | `The torus knot $T_{3,5}$ mediates beta decay ([beta decay as crossing change](#def:beta-decay-skein), [force i…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/helium-hopf-diagram.md:1` | `The helium atom $\mathcal{A}(2, 2)$ provides the simplest closed electron shell. Its electron cloud comprises …` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/helium-hopf-diagram.md:53` | `The third electron links to the closed $1s^2$ sub-link at a higher linking level. It passes around the entire …` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/hydrogen-orbital-tables.md:24` | `Each orbital holds two electrons (spin up and spin down), representing the trefoil's two crossing orientations…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/hydrogen-orbitals.md:3` | `Hydrogen couples a large trefoil electron to a small Borromean proton. The proton occupies the center as a com…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/hydrogen-orbitals.md:5` | `The trefoil spins around the Borromean anchor. This motion sweeps out the electron cloud. The trefoil writhe a…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/hydrogen-orbitals.md:17` | `The Borromean volume pins the massive proton in place. The zero volume of the trefoil keeps the electron light…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/hydrogen-orbitals.md:31` | `The topological mass $m_e \approx 0.511$ MeV remains unchanged. Reidemeister moves preserve knot type (the Rei…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/hydrogen-shell-writhe.lean:8` | `The principal quantum number n of the electron trefoil in a hydrogen atom` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/hydrogen-shell-writhe.lean:69` | `Borromean-baryon model, the proton anchor of the electron trefoil` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/hydrogen-shell-writhe.md:2` | `Let $T_{2,3}$ be the electron trefoil ([electron knot](#def:electron-knot)) Hopf-linked to a proton anchor. Le…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/knot-formula-table-table2-data.md:5` | `\| Electron \| $e^-$ \| $T_{2,3}$ \| $1$ \| $3$ \|` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/knot-formula-table.md:15` | `Here $T_{2,3}^{\sigma}$ is the mirror trefoil $T_{2,-3}$; the mirror marks the down-type member of the doublet…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/knot-operator-selection-multichannel.md:16` | `\underbrace{d_{\yng(2,1)}(q) \cdot P_{T_{2,3}}}_{\text{trefoil (electron)}}` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/knot-operator-selection-proof.md:65` | `For the positron ($e^+ = \sigma_0^{-1}\sigma_1^{-1}\sigma_0^{-1}$), the demand profile is $\{-0.218\gamma, -0.…` | A | fixed: relabelled to electron word e⁻ / closure Hopf link |
| `predicted-spectra/lepton-continuant-recurrence-proof.md:22` | `\| $e^-$ \| $T_{2,3}$ \| $3$ \| $0.209$ \| $1.044$ \| $1.253$ \|` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/lepton-number-categorical-properties.md:6` | `- One charged lepton ($T_{2,3}$ or $T_{2,3}^{\sigma}$) with lepton number $+1$.` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/lepton-number-categorical-properties.md:55` | `closure of $\sigma_1^n$, so $\nu_e = \sigma_1$, $e^- = \sigma_1^3$, and the` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/lepton-number-categorical-properties.md:98` | `\| $e^-$ \| $T_{2,3}$ (trefoil) \| $+1$ \| $L_0^{-}$ charged component ($\beta^-$) \|` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/lepton-number-categorical-properties.md:99` | `\| $e^+$ \| $T_{2,3}^{\sigma}$ (mirror trefoil) \| $-1$ \| $L_0^{+}$ charged component ($\beta^+$) \|` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/lepton-number-categorical-properties.md:106` | `In the Descartes universe, the Euler characteristic $\chi_{\mathrm{eu}}(M_0) = -6$ constrains Bring's surface.…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/lepton-number-categorical.lean:23` | `- Charged leptons (trefoil components): L = +1 or -1` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/lepton-tower-witness-table-data.md:6` | `\| $3$ \| $0.209$ \| $1.044$ \| $\mathbf{1.253}$ \| $e^-$ (trefoil) \|` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/lepton-tower-witness.md:13` | `= \mathrm{net}(T_{2,7}) - \mathrm{net}(T_{2,3})` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/linking-relations-table-table1-data.md:3` | `\| $T_{2,3}$ \| $T_{2,3}$ \| $T_{2,3} \oplus T_{2,3}$ \| $2$ \| lepton-partner pair of $\mathfrak{u}\mathfrak{…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/linking-relations-table-table1-data.md:4` | `\| $T_{2,3}$ \| $T_{2,3}^{\sigma}$ \| $T_{2,3} \oplus T_{2,3}^{\sigma}$ \| $2$ \| lepton-partner pair of $\mat…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/linking-relations-table-table1-data.md:5` | `\| $T_{2,3}^{\sigma}$ \| $T_{2,3}^{\sigma}$ \| $T_{2,3}^{\sigma} \oplus T_{2,3}^{\sigma}$ \| $2$ \| lepton-par…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/linking-relations-table-table1-data.md:8` | `\| $T_{2,3}$ \| $T_{2,5}$ \| $T_{2,3} \oplus T_{2,5}$ \| $2$ \| lepton-partner pair of $\mathfrak{u}\mathfrak{…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/linking-relations-table-table1-data.md:9` | `\| $T_{2,3}$ \| $T_{2,5}^{\sigma}$ \| $T_{2,3} \oplus T_{2,5}^{\sigma}$ \| $2$ \| lepton-partner pair of $\mat…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/linking-relations-table-table2-data.md:9` | `\| $T_{2,3} \oplus T_{2,3}$ \| Skein at crossing \| $4_1$ \| lepton-partner pair of $\mathfrak{u}\mathfrak{u}$…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/linking-relations-table.md:35` | `In each case, the $L_0^{\pm}$ smoothing produces exactly one charged lepton (trefoil or mirror trefoil) and on…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/meson-formation-chain.md:14` | `To create a quark on the trefoil channel, the Hopf link $L_+ = \sigma_0\sigma_1$ from the colored photon norma…` | A | fixed: relabelled to electron word e⁻ / closure Hopf link |
| `predicted-spectra/mesons-nucleons-categorical-proton-unique-intro.md:1` | `Within the three-strand Borromean link topology, the orientation of the internal trefoil twist distinguishes t…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/metallic-character-knot-interpretation.md:4` | `In a metallic lattice, adjacent residual sub-links $R_a$ and $R_b$ merge their open linking sites. Outermost t…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/noble-gas-characterization-interpretation.md:2` | `Each trefoil $T_{2,3}$ is a $(2,3)$-torus knot. It winds twice around one axis and three times around the othe…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/noble-gas-characterization-proof.md:5` | `The reverse direction (inertness implies closed partition) follows from the shell conjecture. If the electron …` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/noble-gas-characterization.md:1` | `An atom $\mathcal{A}(p,n)$ constitutes a noble gas if and only if its electron cloud $p \cdot T_{2,3}$ decompo…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/noble-gas-characterization.md:4` | `Let $\mathcal{A}(p,n)$ be a stable atom with electron cloud $\mathcal{E} = p \cdot T_{2,3}$. The atom $\mathca…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/noble-gas-characterization.md:13` | `2. **Exhaustion**: Every electron belongs to an $S_i$. No unlinked trefoils remain.` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/noble-gas-ionization-affinity.md:7` | `A noble gas exhibits near-zero electron affinity. Attaching a new trefoil requires initiating a fresh sub-link…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/positron-knot.lean:7` | `# QOU.Archimedean.Positron — Mirror trefoil σ(T_{2,3}) (antiparticle of electron)` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/positron-knot.md:1` | `The **positron** corresponds to the mirror trefoil $T_{2,3}^{\sigma}$ in the lepton sector. It serves as the a…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/positron-knot.md:9` | `The positron is drawn as an outlined trefoil to denote reversed time direction. In the Reeb flow, crossing rev…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/q-chromaticity.md:1` | `The three color tubes of the Bring's surface ([color tube interpretation](#rem:color-tube-interpretation)) and…` | B-E3 | σ₀σ₁σ₀ named trefoil inside a statement, notation or identifier |
| `predicted-spectra/q-chromaticity.md:38` | `An individual quark is an unknot strand carrying one crossing letter within a single color tube; the trefoil $…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/shell-structure-eigenvalues.md:60` | `Shell $n$ of an atom is the $n$-th power of the transfer matrix at the electron-nucleus junction. Each power c…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/skein-coulomb-enhancement-interpretation.md:1` | `The leading-order half-life formula ([hadron half-life](#prop:hadron-half-life)) evaluates the Skein polynomia…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/skein-coulomb-enhancement.md:1` | `Let $(\mathbf{C}, A, \tau)$ be a Descartes universe with substrate parameter $q$. Consider the beta decay $\ma…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/skein-finiteness-bound-interpretation.md:30` | `The embeddability constraint immediately produces a finite list of allowed torus knots: $T_{2,3}$, $T_{2,5}$, …` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/spectral-decomposition-qvalue.md:27` | `**(ii)** *$\log_q(x) = \ln x / \ln q$ is the $q$-natural logarithm. It counts exceptional divisor levels along…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/torus-hopf-stability-proof.md:10` | `- **Proton** $\mathfrak{p} = [T_{2,3}, T_{2,3}, T_{2,3}^{\sigma}]_p \oplus \mathcal{L}_H$: The Coulomb charge …` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/torus-knot-prime-powers.md:16` | `\| $1$ \| $T_{3,2} = T_{2,3}$ (trefoil $3_1$) \| $1$ \| $3$ \| Yes \| Electron $e^-$ (lepton partner of $\math…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/torus-knot-prime-powers.md:31` | `The trefoil is the unique generator at the intersection of the $m = 2$ (leptonic) and $m = 3$ (quark) families…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/torus-knot-prime-powers.md:65` | `- $k = 1$: $T_{3,2}$ = trefoil. Lightest matter (the electron, lepton partner of the up quark).` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/unmapped-torus-knots.md:14` | `- $T_{2,3}$: electron $e^-$; lepton partner of the up quark $\mathfrak{u}$ (genus 1)` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `predicted-spectra/unmapped-torus-knots.md:27` | `\| $T_{2,3}$ \| $3$ \| $1$ \| Matter (electron; partner of the up quark) \|` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |
| `quantum-observable-universes/g-action-on-substrate.md:109` | `The anchor value $\mathcal{N}_{\rm sym}(q_0) \approx 213.11$ is defined as $N_v / \prod_{k=2,3,4} [2k]_q^2/[2]…` | B-E1 | trefoil-electron model; re-scope as backup or rewrite |

## 2. Two-term Lagrangian trace τ(ℒ) = τ(𝒟²) + τ(ψ*𝒟ψ)

Spellings searched: "mass/energy … is/equals/=/:=/given by … `\mathrm{tr}_M` / `tr_M` /
Markov trace" in `.md` and `.lean`. Also the two scored-Q_β sentences.

**No class-A fix was possible.** The ledger rules that the scoreboard and every β-decay
route use τ(ℒ). It does **not** say which term of τ(ℒ) the corpus's single-trace mass
`𝔪 = |tr_M(Φ_mass(β))|` (`prop:categorical-mass-markov`) or the scored
`|ε_flavour(V³)|·E₀` corresponds to, so there is no ruling-decided qualifier to insert.
`CategoricalLagrangianTwoTermBridge.lean` proves the split
`trace_lagrangian_two_term_split`; it does not identify `|tr_M(β)|` with `τ(𝒟²)`.

**Decision needed (B-T, one decision for every row):** name the term. For example:
"`|tr_M(Φ_mass(β))|` is the `τ(𝒟²)` term; the connected term `τ(ψ*𝒟ψ)` vanishes on
`V³` (option 2, 2026-11-20)". Once named, every row is a mechanical one-line qualifier.
**Default:** the text keeps stating a one-term trace as "the" mass. The numbers do not
move, because the connected term is 0 on `V³`.

#8723 (scoreboard) changes only `computations/per_observable_100x_status.py` and its
witness. **No open PR touches the two prose sites that describe the scored cell**
(`observations/mass-comparison-table.md:39`,
`nuclear-interactions/neutron-qvalue-symbolic.md:61`), so they will go stale against
#8723 when it lands, unless that PR or a follow-up edits them.

### Sites

| site (path under `folio/quantum-observable-universe/`, line at `bccf522bb5d`) | quoted phrase | class | action |
|---|---|---|---|
| `climax-volume-mass/branch-phase-mass-tower-witness.md:13` | `**Falsifiability witness.** The computation 'isospin-mass-tower-collapse' evaluates the multi-brane mass $\mat…` | B | mass/energy stated as one Markov trace |tr_M(·)| with no one-term / 𝒟²-term qualifier |
| `climax-volume-mass/mobius-energy-intro.md:1` | `Whereas [*The Mass Endomorphism*](#chap:mass-endomorphism) evaluates the algebraic trace $\mathrm{tr}_M(\Phi_{…` | B | mass/energy stated as one Markov trace |tr_M(·)| with no one-term / 𝒟²-term qualifier |
| `lean/QOU/BraidKnot/MassFormulaCategorical.lean:7` | `The QOU mass formula 'M(K) = ρ(K) · m_e · \|tr_M(T_w(K))\|' for` | B | mass/energy stated as one Markov trace |tr_M(·)| with no one-term / 𝒟²-term qualifier |
| `lean/QOU/BraidKnot/MassFormulaCategorical.lean:67` | `/-- **Categorical mass formula**: 'M(T_w) = ρ · m_e · \|tr_M(T_w)\|'` | B | mass/energy stated as one Markov trace |tr_M(·)| with no one-term / 𝒟²-term qualifier |
| `lean/QOU/BraidKnot/confined_knot_binding.lean:22` | `a binding-energy tautology 'E_bind = \|tr_M(β)\|·m_e·ρ_K' as a class` | B | mass/energy stated as one Markov trace |tr_M(·)| with no one-term / 𝒟²-term qualifier |
| `lean/QOU/Braiding/hecke_mass_trace.lean:5` | `# QOU.Braiding.hecke_mass_trace — '𝔪(ϱ_β) = \|tr_M(Φ_mass(β))\|'` | B | mass/energy stated as one Markov trace |tr_M(·)| with no one-term / 𝒟²-term qualifier |
| `lean/QOU/Braiding/hecke_mass_trace.lean:21` | `tr_M(Φ_mass(β)) = tr_M(Φ^desc(β)) + Σ_i tr_M(Φ^trans_i(β)).` | B | mass/energy stated as one Markov trace |tr_M(·)| with no one-term / 𝒟²-term qualifier |
| `lean/QOU/HeckeAlgebra/Common.lean:212` | `used in the QOU mass formula 'M = ρ · m_e · \|tr_M(T_w)\|'.` | B | mass/energy stated as one Markov trace |tr_M(·)| with no one-term / 𝒟²-term qualifier |
| `lean/QOU/HeckeAlgebra/MarkovTrace.lean:14` | `needed by the QOU mass formula 'M = ρ · m_e · \|tr_M(T_w)\|':` | B | mass/energy stated as one Markov trace |tr_M(·)| with no one-term / 𝒟²-term qualifier |
| `lean/QOU/Interactions/qbeta_counit_vs_trace.lean:22` | `The per-braid mass tower is built on 'tr_M'; the 'Q_β' ansatz uses 'ε'.` | B | mass/energy stated as one Markov trace |tr_M(·)| with no one-term / 𝒟²-term qualifier |
| `lean/QOU/Mass/KohnoWeighted.lean:25` | `* **The mass identity on the KZ side** ('braidTrace_eq_kz'): the normalised Markov trace of a` | B | mass/energy stated as one Markov trace |tr_M(·)| with no one-term / 𝒟²-term qualifier |
| `lean/QOU/MassEndomorphism/VolumeBridge.lean:17` | `categorical mass is the descended Markov trace '\|tr_M(ρ(β))\|'` | B | mass/energy stated as one Markov trace |tr_M(·)| with no one-term / 𝒟²-term qualifier |
| `mass-endomorphism/atomic-mass-gb-nf.lean:96` | `def atomic_mass_dimensionless (β_K : A) : ℝ := \|tr_M (NF_GS β_K)\|` | B | mass/energy stated as one Markov trace |tr_M(·)| with no one-term / 𝒟²-term qualifier |
| `mass-endomorphism/color-spacetime-s5-factorization.lean:16` | `* **mass** '= ‖tr_M‖' — the modulus;` | B | mass/energy stated as one Markov trace |tr_M(·)| with no one-term / 𝒟²-term qualifier |
| `mass-endomorphism/mass-endomorphism-conjecture.md:142` | `**(a) Figure-eight $4_1$ as Higgs coupling.** The figure-eight knot $4_1 = (\sigma_0\sigma_1^{-1})^2$ is the g…` | C | PR #8702; left |
| `mass-endomorphism/mass-endomorphism-opener-intro.md:4` | `3. The **categorical mass functional** $\mathfrak{m}(\varrho) = \|\mathrm{tr}_M(\rho(\beta))\| \cdot \mathrm{V…` | C | PR #8702; left |
| `mass-endomorphism/mass-modulus-em-phase-color-grading.md:40` | `- **Modular conjugation.** The Markov trace forms a trace on a finite von Neumann algebra \cite{jones1985}. Ev…` | B | mass/energy stated as one Markov trace |tr_M(·)| with no one-term / 𝒟²-term qualifier |
| `mass-endomorphism/recomputed-low-isotope-mass-table.md:88` | `- [Atomic mass as Markov trace of the Gröbner–Shirshov normal form](atomic-mass-gb-nf.md): The master mass for…` | B | mass/energy stated as one Markov trace |tr_M(·)| with no one-term / 𝒟²-term qualifier |
| `mass-endomorphism/rho-k-graded-expansion.md:6` | `One exposes the graded expansion of the categorical density $\rho_K$ by multiplying the GB-NF identity ([atomi…` | B | mass/energy stated as one Markov trace |tr_M(·)| with no one-term / 𝒟²-term qualifier |
| `mass-theory/categorical-higgs-mechanism.lean:192` | `* 'mass_formula' — each mass is the Hoefsmit-projected Markov trace of` | B | mass/energy stated as one Markov trace |tr_M(·)| with no one-term / 𝒟²-term qualifier |
| `mass-theory/categorical-higgs-mechanism.lean:195` | `mass vanishes: the Markov trace of the surviving 1-component knot` | B | mass/energy stated as one Markov trace |tr_M(·)| with no one-term / 𝒟²-term qualifier |
| `mass-theory/categorical-linking-operation.md:36` | `The Higgs mechanism lifts a gauge boson from $\mathrm{Hom}_R(\mathbf{1}, A)$ (unbroken 1-component knot) to $\…` | B | mass/energy stated as one Markov trace |tr_M(·)| with no one-term / 𝒟²-term qualifier |
| `mass-theory/feynman-qou-dictionary-table-data.md:5` | `\| Action functional $S[\phi]$ \| $q$-energy $\mathfrak{E}_q(\varrho) = \mathrm{tr}_M(\rho(\beta))$ \| [$q$-en…` | B | mass/energy stated as one Markov trace |tr_M(·)| with no one-term / 𝒟²-term qualifier |
| `mass-theory/flavor-split-habiro-derivation.md:16` | `The proton ($uud$) and neutron ($udd$) differ topologically by a single crossing reversal, which corresponds t…` | B | mass/energy stated as one Markov trace |tr_M(·)| with no one-term / 𝒟²-term qualifier |
| `mass-theory/hecke-charge-mass-duality.md:9` | `\| Vertical \| Stabilisation (along the tower) \| $\Phi_{\mathrm{mass}}(\beta)$ \| Mass $\mathfrak{m} = \lvert…` | B | mass/energy stated as one Markov trace |tr_M(·)| with no one-term / 𝒟²-term qualifier |
| `mass-theory/hecke-charge-mass-duality.md:39` | `categorical mass $\mathfrak{m} = \lvert \mathrm{tr}_M(\Phi_{\mathrm{mass}}(\beta)) \rvert$,` | B | mass/energy stated as one Markov trace |tr_M(·)| with no one-term / 𝒟²-term qualifier |
| `mass-theory/hecke-mass-trace.lean:8` | `The categorical mass equals the Frobenius norm of the Markov trace` | B | mass/energy stated as one Markov trace |tr_M(·)| with no one-term / 𝒟²-term qualifier |
| `mass-theory/hecke-mass-trace.lean:65` | `'tr_M(Φ_mass) = tr_M(Φ^desc) + tr_M(Φ^trans)'. -/` | B | mass/energy stated as one Markov trace |tr_M(·)| with no one-term / 𝒟²-term qualifier |
| `mass-theory/hecke-mass-trace.lean:107` | `/-- Linearity of tr_M: tr_M(Φ_mass) = tr_M(Φ^desc) + tr_M(Φ^trans). -/` | B | mass/energy stated as one Markov trace |tr_M(·)| with no one-term / 𝒟²-term qualifier |
| `mass-theory/hecke-mass-trace.lean:159` | `\|tr_M(Φ_mass)\| = Vol(K) / ℏ_q² when the Markov trace evaluates` | B | mass/energy stated as one Markov trace |tr_M(·)| with no one-term / 𝒟²-term qualifier |
| `mass-theory/knot-mass-formula-unified.lean:221` | `contributes '0'. Then the total mass is '1 + m_e · tr_M(C_{dim_q})' —` | B | mass/energy stated as one Markov trace |tr_M(·)| with no one-term / 𝒟²-term qualifier |
| `mass-theory/mass-ordering-corrected.md:9` | `Since categorical mass is $\mathfrak{m} = \|\mathrm{tr}_M\|$:` | B | mass/energy stated as one Markov trace |tr_M(·)| with no one-term / 𝒟²-term qualifier |
| `mass-theory/per-braid-mass-tower.lean:52` | `mass W = \|trM W\| + Σ_{ξ ∈ S_1} Φ_q (\|trM ξ\|)` | B | mass/energy stated as one Markov trace |tr_M(·)| with no one-term / 𝒟²-term qualifier |
| `mass-theory/phi-q-categorical-truncation-proof.md:18` | `[categorical mass = Markov trace](#prop:categorical-mass-markov)` | B | mass/energy stated as one Markov trace |tr_M(·)| with no one-term / 𝒟²-term qualifier |
| `mass-theory/quantum-dilogarithm-stratified-partial-argument.md:51` | `[categorical mass = Markov trace](#prop:categorical-mass-markov), the` | C | PR #8702; left |
| `mass-theory/rho-k-h3a-refinement.md:28` | `The mass formula $M(K) = \rho_K \cdot m_e \cdot \|\mathrm{tr}_M(\mathcal{B}_K)\|$ defines $\rho_K$, so the dec…` | B | mass/energy stated as one Markov trace |tr_M(·)| with no one-term / 𝒟²-term qualifier |
| `mass-theory/three-calibration-inputs-proof.md:34` | `gives every mass as $\mathfrak{m}(\varrho) = \|\mathrm{tr}_M(\rho(\beta))\|$` | B | mass/energy stated as one Markov trace |tr_M(·)| with no one-term / 𝒟²-term qualifier |
| `nuclear-interactions/neutron-qvalue-symbolic.md:61` | `The value scored on the L2 scorecard is not this one. The scored $\mathfrak{Q}_\beta$ applies the $T^3$ weight…` | B | scored Q_β described as the single trace |ε_flavour(V³)|·E₀; ruling says the scoreboard uses τ(ℒ) — needs the term identified (numbers unchanged under option 2) |
| `nuclear-interactions/qbeta-counit-transition.md:7` | `A static mass is a closed loop, read by $\mathrm{tr}_M$. A $\beta$-decay is a transition. The per-Hecke-step e…` | B | mass/energy stated as one Markov trace |tr_M(·)| with no one-term / 𝒟²-term qualifier |
| `nuclear-interactions/universal-ilp-algorithm.md:57` | `*Use the same energy functional $\Phi_1 = \ln\|\mathrm{tr}_M\|$ and the same Wedderburn-Artin weights at every…` | B | mass/energy stated as one Markov trace |tr_M(·)| with no one-term / 𝒟²-term qualifier |
| `observations/mass-comparison-table.md:21` | `The proton and neutron rows derive from the LO $\rho_K$ assembly. This assembly consumes $m_p$ and $m_n$ as CO…` | B | scored Q_β described as the single trace |ε_flavour(V³)|·E₀; ruling says the scoreboard uses τ(ℒ) — needs the term identified (numbers unchanged under option 2) |
| `observations/mass-comparison-table.md:39` | `The value scored on the L2 scorecard is a different functional on a different element: the $T^3$ weight split …` | B | scored Q_β described as the single trace |ε_flavour(V³)|·E₀; ruling says the scoreboard uses τ(ℒ) — needs the term identified (numbers unchanged under option 2) |
| `predicted-spectra/quantum-dilogarithm-volume.md:1` | `The nuclear binding energy is the quantum dilogarithm volume of the Markov trace, normalized by $\hbar_q^2$:` | B | mass/energy stated as one Markov trace |tr_M(·)| with no one-term / 𝒟²-term qualifier |

## 3. Photon: γ = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁·σ₀σ₁⁻¹

Spellings searched: four-term photon expressions (`1 + φ₀σ₀ …`, `1 + \varphi_0\sigma_0 …`)
without `σ₁⁻¹` / `\sigma_1^{-1}`. `φ₀₁` or `\varphi_{01}` beside `σ₀σ₁`, `\sigma_0\sigma_1`
or `L_+`. "vertex = σ₀σ₁" and "fourth term … σ₀σ₁" without the inverse. Lean `phi01 •
(σ₀ * σ₁)`.

**No stale site found.** Every content definition uses `σ₀σ₁⁻¹`. The Lean files that
still write `σ₀σ₁` either label it the superseded form (`Photon.lean:11-14`,
`Mass/PhotonTraceLemmas.lean:14`, `Mass/BorromeanPhotonFactorisation.lean:30`) or use the
**straight chart** `1 + (φ₀ − hφ₀₁)σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁`. That is the same photon in
different coordinates, and `QuarkState/PhotonPairNormalForm.lean:10,109` says so.

### Sites

| site (path under `folio/quantum-observable-universe/`, line at `bccf522bb5d`) | quoted phrase | class | action |
|---|---|---|---|
| `braids-and-knots/fundamental-knots-operator-basis.md:10` | `\| photon $\gamma$ \| — (not a knot) \| Hecke element \| $\mathbf{1} + \varphi_0\sigma_0 + \varphi_1\sigma_1 +…` | D | correct form σ₀σ₁⁻¹, or the straight-chart rewrite of it (φ₀ − hφ₀₁) |
| `brings-surface/knot-basis-color-content.md:6` | `is called a photon with color content. Its fourth term is the chiral vertex $\sigma_0\sigma_1^{-1} = \sigma_0\…` | D | correct form σ₀σ₁⁻¹, or the straight-chart rewrite of it (φ₀ − hφ₀₁) |
| `brings-surface/trivial-knot-photon-interpretation-table4-data.md:4` | `\| (14) \| $\varphi_{01}V \cdot \psi_0\sigma_0$ \| $\varphi_{01}\psi_0\bigl(e^- - h^2\sigma_0 - h\,\gamma\bigr…` | D | correct form σ₀σ₁⁻¹, or the straight-chart rewrite of it (φ₀ − hφ₀₁) |
| `brings-surface/trivial-knot-photon-interpretation-table4-data.md:6` | `\| (16) \| $\varphi_{01}V \cdot \psi_{01}V$ \| $\varphi_{01}\psi_{01}\bigl(\sigma_1\sigma_0^{-1} - h^2V + h^2\…` | D | correct form σ₀σ₁⁻¹, or the straight-chart rewrite of it (φ₀ − hφ₀₁) |
| `brings-surface/trivial-knot-photon-interpretation.md:11` | `Each photon is $\gamma(\varphi) = \mathbf{1} + \varphi_0\sigma_0 + \varphi_1\sigma_1 + \varphi_{01}V$, whose f…` | D | correct form σ₀σ₁⁻¹, or the straight-chart rewrite of it (φ₀ − hφ₀₁) |
| `introduction/chapter-overview.md:37` | `Specific knots map to particle identities: the unknot $0_1$ acts as the neutrino, the trefoil $3_1$ acts as th…` | D | correct form σ₀σ₁⁻¹, or the straight-chart rewrite of it (φ₀ − hφ₀₁) |
| `introduction/intro-particles-as-knots.md:43` | `\gamma = 1 + \varphi_0\sigma_0 + \varphi_1\sigma_1 + \varphi_{01}\,\sigma_0\sigma_1^{-1},` | D | correct form σ₀σ₁⁻¹, or the straight-chart rewrite of it (φ₀ − hφ₀₁) |
| `knots-particles-confinement/confinement-universality.md:9` | `*Let $\gamma_k = \mathbf{1} + \varphi_0\sigma_0 + \varphi_1\sigma_1 + \varphi_{01}\sigma_0\sigma_1^{-1}$ be a …` | D | correct form σ₀σ₁⁻¹, or the straight-chart rewrite of it (φ₀ − hφ₀₁) |
| `knots-particles-confinement/four-term-pair-nucleon.md:13` | `where $\varphi_{01}\sigma_0\sigma_1^{-1} = \varphi_{01}(L_+ - h\sigma_0)$ is the chiral pair-production vertex…` | D | correct form σ₀σ₁⁻¹, or the straight-chart rewrite of it (φ₀ − hφ₀₁) |
| `knots-particles-confinement/four-term-pair-nucleon.md:40` | `For quarks $(\mathfrak{u}_1, \mathfrak{d}_2, \mathfrak{d}_3)$, reduction yields $\mathrm{net}(\mathfrak{n}) \a…` | D | correct form σ₀σ₁⁻¹, or the straight-chart rewrite of it (φ₀ − hφ₀₁) |
| `knots-particles-confinement/nucleon-derivation-intro.md:1` | `Because every interaction factors into elementary two-strand crossings, one begins by defining the two fundame…` | D | correct form σ₀σ₁⁻¹, or the straight-chart rewrite of it (φ₀ − hφ₀₁) |
| `knots-particles-confinement/quark-antiquark-production-reduction.md:2` | `Each photon is the Hecke algebra element $\gamma = \mathbf{1} + \varphi_0\sigma_0 + \varphi_1\sigma_1 + \varph…` | D | correct form σ₀σ₁⁻¹, or the straight-chart rewrite of it (φ₀ − hφ₀₁) |
| `knots-particles-confinement/quark-antiquark-production.md:4` | `\gamma = \mathbf{1} + \varphi_0\sigma_0 + \varphi_1\sigma_1 + \varphi_{01}\sigma_0\sigma_1^{-1}` | D | correct form σ₀σ₁⁻¹, or the straight-chart rewrite of it (φ₀ − hφ₀₁) |
| `lean/QOU/BraidKnot/LongestWordNotTwoPhoton.lean:16` | `where 'γ' is the corpus photon '1 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁⁻¹'` | D | correct form σ₀σ₁⁻¹, or the straight-chart rewrite of it (φ₀ − hφ₀₁) |
| `lean/QOU/BraidsAndKnots/NucleonWeightSpaceTwoTerm.lean:794` | `/-- Switched four-term photon 'γ'(φ₀, φ₁, φ₀₁) = 1 + φ₀ σ₀ + φ₁ σ₁ + φ₀₁ (σ₀ σ₁⁻¹)' on the` | D | correct form σ₀σ₁⁻¹, or the straight-chart rewrite of it (φ₀ − hφ₀₁) |
| `lean/QOU/BraidsAndKnots/NucleonWeightSpaceTwoTerm.lean:799` | `/-- Switched four-term photon 'γ'(φ₀, φ₁, φ₀₁) = 1 + φ₀ σ₀ + φ₁ σ₁ + φ₀₁ (σ₀ σ₁⁻¹)' on the` | D | correct form σ₀σ₁⁻¹, or the straight-chart rewrite of it (φ₀ − hφ₀₁) |
| `lean/QOU/BraidsAndKnots/QEDHigherOrderCovariance.lean:66` | `'γ(φ) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁⁻¹', 'γ(0,0,qh)·γ(0,0,−q⁻¹h) = V³' on the proton weight space` | D | correct form σ₀σ₁⁻¹, or the straight-chart rewrite of it (φ₀ − hφ₀₁) |
| `lean/QOU/BraidsAndKnots/QEDHigherOrderCovariance.lean:497` | `'γ(φ) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁⁻¹' and 'β_Bor = γ(0,0,qh)·γ(0,0,−q⁻¹h)'. On the proton` | D | correct form σ₀σ₁⁻¹, or the straight-chart rewrite of it (φ₀ − hφ₀₁) |
| `lean/QOU/Interactions/GammaGammaPairChannels.lean:8` | `'γ(φ) · γ(ψ)' in 'H₃(q)', with 'γ(φ) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁⁻¹' ('def:photon'; the last` | D | correct form σ₀σ₁⁻¹, or the straight-chart rewrite of it (φ₀ − hφ₀₁) |
| `lean/QOU/KnotRegistry.lean:162` | `element of 'H₃(q)', 'γ = 𝟙 + φ₀·σ₀ + φ₁·σ₁ + φ₀₁·σ₀σ₁⁻¹' ('def:photon'; the last` | D | correct form σ₀σ₁⁻¹, or the straight-chart rewrite of it (φ₀ − hφ₀₁) |
| `lean/QOU/Mass/BorromeanPhotonFactorisation.lean:20` | `Each factor is a photon 'γ(φ) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁⁻¹' in the sense of` | D | correct form σ₀σ₁⁻¹, or the straight-chart rewrite of it (φ₀ − hφ₀₁) |
| `lean/QOU/Mass/PhotonTraceLemmas.lean:12` | `'γ(φ₀,φ₁,φ₀₁) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁⁻¹'; the expression 'photonSwitched'` | D | correct form σ₀σ₁⁻¹, or the straight-chart rewrite of it (φ₀ − hφ₀₁) |
| `lean/QOU/Mass/PhotonTraceLemmas.lean:15` | `it reads '1 + (φ₀ − hφ₀₁)σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁' ('photon_eq_straight'), so the` | D | correct form σ₀σ₁⁻¹, or the straight-chart rewrite of it (φ₀ − hφ₀₁) |
| `lean/QOU/Mass/PhotonTraceLemmas.lean:64` | `/-- **Coordinate change.** In the straight basis '1, σ₀, σ₁, σ₀σ₁' the photon` | D | correct form σ₀σ₁⁻¹, or the straight-chart rewrite of it (φ₀ − hφ₀₁) |
| `lean/QOU/ParticleInteractions/four_term_pair_nucleon.lean:41` | `'γ = 𝟙 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁⁻¹' (definitional; 'def:photon', last term the` | D | correct form σ₀σ₁⁻¹, or the straight-chart rewrite of it (φ₀ − hφ₀₁) |
| `lean/QOU/Photon.lean:3` | `γ(φ) = 𝟙 + φ₀·σ₀ + φ₁·σ₁ + φ₀₁·σ₀σ₁⁻¹.` | C | PR #8702; left |
| `lean/QOU/Photon.lean:14` | `'γ(φ₀, φ₁, φ₀₁) = 𝟙 + (φ₀ − hφ₀₁)σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁'` | C | PR #8702; left |
| `lean/QOU/Photon.lean:39` | `/-- **The photon** 'γ(φ) = 𝟙 + φ₀•σ₀ + φ₁•σ₁ + φ₀₁•(σ₀σ₁⁻¹)'. -/` | C | PR #8702; left |
| `lean/QOU/QBeta/DecayConjectures.lean:59` | `For the four-term photon 'γ(φ₀,φ₁,φ₀₁) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁⁻¹' and any second photon` | D | correct form σ₀σ₁⁻¹, or the straight-chart rewrite of it (φ₀ − hφ₀₁) |
| `lean/QOU/QBeta/FlavourWeightSplit.lean:25` | `With the photon 'γ(φ) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁·σ₀σ₁⁻¹' and the corpus-derived colour weights` | D | correct form σ₀σ₁⁻¹, or the straight-chart rewrite of it (φ₀ − hφ₀₁) |
| `lean/QOU/QuarkState/PhotonPairNormalForm.lean:10` | `with 'γ(φ) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁' ('rem:knot-basis-color-content', as written before the` | D | old form named as history |
| `lean/QOU/QuarkState/PhotonPairNormalForm.lean:109` | `/-- The photon in the **straight chart** '1 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁', built with` | D | correct form σ₀σ₁⁻¹, or the straight-chart rewrite of it (φ₀ − hφ₀₁) |
| `lean/QOU/QuarkState/PhotonPairNormalForm.lean:113` | `confirmed 2026-11-20). 'def:photon' is now '1 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁⁻¹' — 'photon'` | D | correct form σ₀σ₁⁻¹, or the straight-chart rewrite of it (φ₀ − hφ₀₁) |
| `lean/QOU/QuarkState/PhotonPairNormalForm.lean:159` | `/-- **'def:photon'**: 'γ(φ) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁·σ₀σ₁⁻¹', 'σ₁⁻¹ = σ₁ − h'. -/` | D | correct form σ₀σ₁⁻¹, or the straight-chart rewrite of it (φ₀ − hφ₀₁) |
| `lean/QOU/StandardModel/ChiralityPolarizationHopf.lean:49` | `'γ = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁⁻¹' ('def:photon', last term the chiral vertex by` | D | correct form σ₀σ₁⁻¹, or the straight-chart rewrite of it (φ₀ − hφ₀₁) |
| `mass-theory/borromean-two-photon-factorisation.md:18` | `*Each factor is a [photon](#def:photon) $\gamma(\varphi_0, \varphi_1, \varphi_{01}) = 1 + \varphi_0\sigma_0 + …` | D | correct form σ₀σ₁⁻¹, or the straight-chart rewrite of it (φ₀ − hφ₀₁) |
| `mass-theory/degree-one-braid-trivial-volume.lean:25` | `'γ(φ) = 𝟙 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁⁻¹' (owner ruling, bean 'qou-99qc'). Its` | D | correct form σ₀σ₁⁻¹, or the straight-chart rewrite of it (φ₀ − hφ₀₁) |
| `mass-theory/degree-one-braid-trivial-volume.md:11` | `*The same holds for a [photon](#def:photon) $\gamma(\varphi) = \mathbf{1} + \varphi_0\sigma_0 + \varphi_1\sigm…` | D | correct form σ₀σ₁⁻¹, or the straight-chart rewrite of it (φ₀ − hφ₀₁) |
| `mass-theory/pieri-photon-shift.lean:9` | `'γ(φ) = 𝟙 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁⁻¹' (owner ruling, bean 'qou-99qc',` | D | correct form σ₀σ₁⁻¹, or the straight-chart rewrite of it (φ₀ − hφ₀₁) |
| `mass-theory/pieri-photon-shift.md:2` | `*Let $\lambda = (\lambda_1, \lambda_2) \vdash n$ be a partition with at most two rows (the shapes seen by $\ma…` | D | correct form σ₀σ₁⁻¹, or the straight-chart rewrite of it (φ₀ − hφ₀₁) |
| `mass-theory/trace-flavour-no-go.md:16` | `- the [photon](#def:photon) $\gamma(\varphi_0, \varphi_1, \varphi_{01}) = 1 + \varphi_0\sigma_0 + \varphi_1\si…` | D | correct form σ₀σ₁⁻¹, or the straight-chart rewrite of it (φ₀ − hφ₀₁) |
| `observations/double-slit-intro.md:4` | `2. **Photons (exceptional-divisor flux modes):** A photon is a volumeless excitation on the exceptional diviso…` | D | correct form σ₀σ₁⁻¹, or the straight-chart rewrite of it (φ₀ − hφ₀₁) |
| `predicted-spectra/breit-wheeler-pair-production-derivation.md:3` | `This derives the Breit--Wheeler categorical pair production with the [photon](#def:photon) $\gamma(\varphi) = …` | D | correct form σ₀σ₁⁻¹, or the straight-chart rewrite of it (φ₀ − hφ₀₁) |
| `predicted-spectra/breit-wheeler-pair-production-derivation.md:22` | `where $\varphi_0, \varphi_1, \varphi_{01} \in R$. The generator $\sigma_0$ acts on the $(\sigma, r)$ plane and…` | D | correct form σ₀σ₁⁻¹, or the straight-chart rewrite of it (φ₀ − hφ₀₁) |
| `predicted-spectra/breit-wheeler-pair-production.lean:5` | `γ(φ) = 𝟙 + φ₀•σ₀ + φ₁•σ₁ + φ₀₁•σ₀σ₁⁻¹` | D | correct form σ₀σ₁⁻¹, or the straight-chart rewrite of it (φ₀ − hφ₀₁) |
| `predicted-spectra/breit-wheeler-pair-production.md:8` | `\gamma(\varphi) = \mathbf{1} + \varphi_0\sigma_0 + \varphi_1\sigma_1 + \varphi_{01}\,\sigma_0\sigma_1^{-1}.` | D | correct form σ₀σ₁⁻¹, or the straight-chart rewrite of it (φ₀ − hφ₀₁) |
| `predicted-spectra/breit-wheeler-pair-production.md:18` | `The $e^-$ channel of the product is its coefficient on $\sigma_0\sigma_1\sigma_0$, which is $\varphi_{01}\psi_…` | D | correct form σ₀σ₁⁻¹, or the straight-chart rewrite of it (φ₀ − hφ₀₁) |
| `predicted-spectra/gamma-gamma-generates-particles.lean:5` | `γ = 𝟙 + φ₀·σ₀ + φ₁·σ₁ + φ₀₁·σ₀σ₁⁻¹ (def:photon; the last term is the chiral` | D | correct form σ₀σ₁⁻¹, or the straight-chart rewrite of it (φ₀ − hφ₀₁) |
| `predicted-spectra/gamma-gamma-generates-particles.md:28` | `The two chiral operators are generated independently. The $L_+$ coefficient is the cross-color product $\varph…` | D | correct form σ₀σ₁⁻¹, or the straight-chart rewrite of it (φ₀ − hφ₀₁) |
| `predicted-spectra/meson-formation-chain.md:4` | `A $1.6\%$ energy gap separates the bare photon pair from the threshold $2\mathfrak{m}_e$. The color weights $\…` | D | correct form σ₀σ₁⁻¹, or the straight-chart rewrite of it (φ₀ − hφ₀₁) |
| `predicted-spectra/photon.md:4` | `\gamma(\varphi) \;=\; \mathbf{1} + \varphi_0\,\sigma_0 + \varphi_1\,\sigma_1 + \varphi_{01}\,\sigma_0\sigma_1^…` | D | correct form σ₀σ₁⁻¹, or the straight-chart rewrite of it (φ₀ − hφ₀₁) |
| `predicted-spectra/photon.md:7` | `A photon has three parameters and four terms. Its fourth term is the chiral pair-production vertex $V = \sigma…` | D | correct form σ₀σ₁⁻¹, or the straight-chart rewrite of it (φ₀ − hφ₀₁) |
| `predicted-spectra/photon.md:10` | `\gamma(\varphi_0, \varphi_1, \varphi_{01}) \;=\; \mathbf{1} + (\varphi_0 - h\varphi_{01})\,\sigma_0 + \varphi_…` | D | correct form σ₀σ₁⁻¹, or the straight-chart rewrite of it (φ₀ − hφ₀₁) |
| `quantum-observable-universes/photon-wavefront-example.md:1` | `This example traces the wavefront propagation equation $\mathcal{D}_\nabla\psi = 0$ through a double-slit expe…` | D | correct form σ₀σ₁⁻¹, or the straight-chart rewrite of it (φ₀ − hφ₀₁) |

## 4. Up quark: an unknot strand, not a knot type

Spellings searched: `up quark`, `up-quark`, `\mathfrak{u}`, `upQuark`, `u-quark` beside
`trefoil`, `T(2,3)`, `T_{2,3}`, `3_1`, `3₁`, "knot type" or "knot". Also tables with
`u` / `\mathfrak{u}` in a knot column, and Lean `.up =>`.

Most hits are compliant (D): "unknot strand", "lepton partner `T_{2,3}`", and the arrow
`u ← T_{2,3}`. The ruling-compliant reading is recorded in the
`lepton-meson-torus-knot-dictionary` `authorNotes` (2026-11-21). **Ten B sites assign the
quark the trefoil itself:**

- `information-theory/jet-planck-steps-table1-data.md:6,7,10,11,12` lists u/d, c/s and b
  as particles *at* knots 3₁, 5₁ and 7₁. The whole jet-step table would need rewriting.
- `observations/building-block-knots-table7-data.md:8` gives "u,d | `T_{2,3}` | 3 | 0 |
  3q", i.e. a crossing energy, which is a number.
- `observations/hopf-diquark.lean:46-48`: `Flavor.crossingCount` is
  `.up => 3 -- T_{2,3} trefoil`. That is a Lean definition.
- `brings-surface/cohomological-embedding-table2-data.md:5`: "τ(2,3) (trefoil) … on
  divisor: u/d".

### Sites

| site (path under `folio/quantum-observable-universe/`, line at `bccf522bb5d`) | quoted phrase | class | action |
|---|---|---|---|
| `appendix-knot-operations-archimedean/gluon-model-comparison.md:5` | `The three constituents are unknots; the Hopf link $\mathcal{L}_H$ binds them. Flavour is the crossing orientat…` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `appendix-knot-operations-archimedean/gluon-model-comparison.md:17` | `where $\mathrm{cx} = \mathrm{cx}(q_0,q_1) \cdot \mathrm{cx}(q_0,q_2) \cdot \mathrm{cx}(q_1,q_2)$ are the pairw…` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `appendix-knot-operations-archimedean/gluon-model-comparison.md:33` | `Quarks interact as single-crossing unknots, not as full trefoils (Definition 4.27.1): replacing each crossing …` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `appendix-knot-operations-archimedean/gluon-model-comparison.md:50` | `\mathfrak{p} = B_3 \cdot \sigma(\mathfrak{u},\mathfrak{u})` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `appendix-knot-operations-archimedean/gluon-model-comparison.md:51` | `\cdot \tfrac{1}{2}(\sigma + \sigma^{-1})(\mathfrak{u},\mathfrak{d})` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `appendix-knot-operations-archimedean/gluon-model-comparison.md:52` | `\cdot \tfrac{1}{2}(\sigma + \sigma^{-1})(\mathfrak{u},\mathfrak{d})` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `appendix-knot-operations-archimedean/particle-nf-table-table-data.md:19` | `\| $\mathfrak{u}$ \| unknot $(+)$ \| $\sigma_0$ \| — \| $+1$ \| — \| — \| — \| — \| $+1.000$ \|` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `appendix-knot-operations-archimedean/particle-nf-table.md:4` | `$\mathfrak{d}$--$\mathfrak{u}$ splitting (observation 2 below) shows up` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `appendix-knot-operations-archimedean/particle-nf-table.md:27` | `$\mathfrak{u} = \sigma$ (positive), $\mathfrak{d} = \sigma^{-1}$` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `appendix-knot-operations-archimedean/particle-nf-table.md:31` | `divisor ($\mathfrak{u} \leftarrow T_{2,3}$,` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `appendix-knot-operations-archimedean/particle-nf-table.md:37` | `1. **Up quark** $\mathfrak{u} = \sigma_0$ (positive crossing` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `appendix-knot-operations-archimedean/particle-nf-table.md:46` | `channel. This leakage is the origin of the $\mathfrak{d}$--$\mathfrak{u}$` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `appendix-knot-periodic-table/knot-periodic-table.md:11` | `where $\mathfrak{p} = [\mathfrak{u}, \mathfrak{u}, \mathfrak{d}]_p \oplus \mathcal{L}_H$ is the` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `appendix-knot-periodic-table/knot-periodic-table.md:12` | `proton (color-linked quark triple), $\mathfrak{n} = [\mathfrak{u}, \mathfrak{d}, \mathfrak{d}]_p \oplus \mathc…` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `appendix-knot-periodic-table/knot-periodic-table.md:17` | `proton, $\mathfrak{n}$ the neutron, with $\mathfrak{u}, \mathfrak{d}$` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `appendix-knot-periodic-table/knot-periodic-table.md:30` | `where $m_{\mathfrak{p}} = \mathcal{S}_{\mathfrak{u}\mathfrak{u}} + 2\mathcal{S}_{\mathfrak{u}\mathfrak{d}}$` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `appendix-knot-periodic-table/knot-periodic-table.md:31` | `and $m_{\mathfrak{n}} = 2\mathcal{S}_{\mathfrak{u}\mathfrak{d}} + \mathcal{S}_{\mathfrak{d}\mathfrak{d}}$ are` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `appendix-standard-model/sm-open-problems.md:11` | `\| Hypercharge $Y$ \| open: writhe map falsified; candidate second datum defined — the strand twist, with gaug…` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `appendix-transfer-matrices/tm-knot-pairs.md:30` | `Strands: two up quarks, each an unknot strand of $\mathcal{B}_3$ with positive crossing orientation (lepton pa…` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `appendix-transfer-matrices/tm-knot-pairs.md:108` | `**4c. Trefoil--cinquefoil ($\mathfrak{u}$-$\mathfrak{b}$)**` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `appendix-transfer-matrices/tm-knot-pairs.md:110` | `$c = 1, d = 0$. Thus $T_{\mathfrak{u}\mathfrak{b}}(q) = T_{pp}(q)$.` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `appendix-transfer-matrices/tm-notation-table3-data.md:4` | `([up quark](#def:up-quark)); its rows give the torus knot of its lepton` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `appendix-transfer-matrices/tm-notation-table3-data.md:12` | `\| Up quark $\mathfrak{u}$ (partner) \| $T_{2,3}$ \| $\mathfrak{u}^{\sigma}$ \| $T_{2,3}^{\sigma}$ \|` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `braids-and-knots/knot-notation-convention.md:1` | `Particles in this framework are identified with their knots. The notation is $\mathfrak{K}_x^{\pm}$, where $x$…` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `brings-surface/cohomological-embedding-table2-data.md:5` | `\| $H^{1,0}$ \| $1$ \| $1$ \| $\tau(2,3)$ (trefoil) \| $e^- / e^+$; on divisor: $\mathfrak{u}/\mathfrak{d}$ \|` | B | 'τ(2,3) (trefoil) … on divisor: u/d' reads the quarks as the trefoil on the exceptional divisor |
| `information-theory/jet-planck-particle-spectrum.md:17` | `Both appear at the same Planck step. The cubic jet produces both chiralities simultaneously. The same trefoil …` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `information-theory/jet-planck-particle-spectrum.md:20` | `The figure-eight knot $4_1$ has crossing number $4$ and is the first hyperbolic knot. It is amphichiral, so th…` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `information-theory/jet-planck-steps-table1-data.md:6` | `\| 3 \| cubic \| 3 \| $3_1$ \| **Electron** $e^-$, **up** $u$ \| **Positron** $e^+$, **down** $u^{\sigma}$ \| …` | B | table lists **up** u / **down** under knot 3₁ as particles; whole table assigns quarks to torus knots (also rows 7, 10-12) — rewrite needs a decision on the jet-step spectrum |
| `information-theory/jet-planck-steps-table1-data.md:7` | `\| 3 \| cubic \| 3 \| $3_1^{\sigma}$ \| **Positron** $e^+$, **down** $d$ \| **Electron** $e^-$, $d^{\sigma}$ \…` | B | same table, down quark under 3₁^σ |
| `information-theory/jet-planck-steps-table1-data.md:10` | `\| 5 \| quintic \| 5 \| $5_1$ \| **Muon** $\mu^-$, **charm** $c$ \| $\mu^+$, $c^{\sigma}$ \| Cinquefoil; chira…` | B | charm under 5₁ (quark as torus knot) |
| `information-theory/jet-planck-steps-table1-data.md:11` | `\| 5 \| quintic \| 5 \| $5_1^{\sigma}$ \| **Antimuon** $\mu^+$, **strange** $s$ \| $\mu^-$, $s^{\sigma}$ \| Mi…` | B | strange under 5₁^σ |
| `information-theory/jet-planck-steps-table1-data.md:12` | `\| 7 \| septic \| 7 \| $7_1$ \| **Tau** $\tau^-$, **bottom** $b$ \| $\tau^+$, $b^{\sigma}$ \| Third-generation…` | B | bottom under 7₁ |
| `knots-particles-confinement/atom-knot.md:16` | `- *$w_{q^Z} \in S_{n(K)}$ is the proton-quark block. It is the product of $Z$ permutations. Each permutation r…` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `knots-particles-confinement/atom-knot.md:17` | `- *$w_{\bar q^N}$ is the neutron-quark block. It consists of $N$ disjoint Borromean normal forms for $\mathfra…` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `knots-particles-confinement/categorical-neutron-properties.md:60` | `The sum vanishes, and the arithmetic is the Standard Model's. What it is **not** is a consequence of the cross…` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `knots-particles-confinement/categorical-proton.lean:10` | `orientation ('def:up-quark'); their lepton partners are T_{2,3} and its` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `knots-particles-confinement/down-quark-properties.md:2` | `The up and down quarks possess the same knot type and environment. The mass difference $\mu_{\mathfrak{d}} - \…` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `knots-particles-confinement/knot-particle-dictionary-table4-data.md:3` | `\| Up \| $\mathfrak{u}$ \| $\sigma_i$ (positive crossing) \| $\leftarrow T_{2,3}$ \| 1 \| $e^-$ \|` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `knots-particles-confinement/knot-particle-generation-table-data.md:4` | `\| $T_{2,3}$ \| Trefoil $3_1$ \| $1$ \| $3$ \| Electron (gen. 1); lepton partner of $\mathfrak{u}$, $\mathfrak…` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `knots-particles-confinement/knot-particle-generation.lean:81` | `/-- Dressed up-quark Skein mass (MeV), from CODATA nucleon masses. -/` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `knots-particles-confinement/quark-antiquark-production-reduction.md:19` | `The Hopf link operator $L_+$ transmutes the trefoil electron into a virtual crossing $\sigma_1$ plus residual …` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `knots-particles-confinement/up-quark.lean:30` | `/-- The up quark is an unknot (same underlying knot as the neutrino,` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `knots-particles-confinement/up-quark.md:8` | `*The up quark is not a distinct knot type. It is the unknot distinguished by its environment. It is threaded t…` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `lean/QOU/Archimedean/TorusKnot.lean:74` | `/-- Electron: 'e = τ(2,3)' (trefoil), the up quark's lepton partner; the up` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `lean/QOU/StandardModel/ChiralityIndependentOfCrossing.lean:99` | `'u_L' and 'u_R' are both up quarks, so by the knot-particle dictionary they` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `mass-theory/transfer-matrix-operator-properties.md:79` | `Each quark is an unknot strand of $\mathcal{B}_3$ ([up quark](#def:up-quark)); the strands are distinguished b…` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `nuclear-interactions/hydrogen-derived-nf.md:7` | `3(\gamma\gamma) \xrightarrow{\text{pair prod.}} (\mathfrak{u}_1, \mathfrak{u}_2, \mathfrak{d}_3) + (\bar{\math…` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `observations/building-block-knots-table1-data.md:5` | `\| Left trefoil \| $T_{2,3}$ \| $3_1$ \| $1$ \| $3$ \| ● \| $e^-$ (electron); lepton partner of $\mathfrak{u}$…` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `observations/building-block-knots-table7-data.md:8` | `\| $u,d$ (quarks) \| $T_{2,3}$ \| $3$ \| $0$ \| $3q$ \| $3\mathfrak{E}_{\times}$ \| (bound; see below) \|` | B | row 'u,d (quarks) | T_{2,3} | 3 | 0 | 3q' gives quarks the trefoil and its crossing energy 3q — a number |
| `observations/hopf-diquark.lean:46` | `\| .up => 3 -- T_{2,3} trefoil` | B | def Flavor.crossingCount: .up => 3 '-- T_{2,3} trefoil' — a Lean definition |
| `observations/hopf-diquark.lean:47` | `\| .down => 3 -- mirror T_{2,3}` | B | same def, .down => 3 |
| `observations/hopf-diquark.lean:48` | `\| .strange => 5 -- mirror T_{2,5} cinquefoil` | B | same def, .strange => 5 |
| `observations/hydrogen-knot-structure-table1-data.md:3` | `\| $\nu_r$ \| Unknot $K_{0_1}$ \| 1 \| Up quark (color $r$) \|` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `observations/hydrogen-knot-structure-table1-data.md:4` | `\| $\nu_g$ \| Unknot $K_{0_1}$ \| 1 \| Up quark (color $g$) \|` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `observations/mass-comparison-table-table1-data.md:4` | `\| $e^-$ \| $T_{2,3}$ \| $\mathcal{S}_{\mathfrak{u}\mathfrak{u}}(q) / 3$ (input) \| $0.511$ \| $0.51100$ \| CO…` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `observations/strangelet-crossing-energy-proof.md:1` | `*Proof.* (1) The up quark occupies a color tube with positive orientation ($+2/3$ charge). The down and strang…` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `observations/strangelet-crossing-energy.md:28` | `> The arrow is the [knot-particle dictionary](#tbl:knot-particle-dictionary-table4-data)'s **lepton-descent** …` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `observations/strangelet-intro.md:1` | `In the lepton-partner reading of the quark sector ([knot–particle dictionary](#rem:knot-particle-dictionary)),…` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `observations/strangelet-witten-stability.md:20` | `\| Up $\mathfrak{u}$ \| $T_{2,3}$ \| $-q^{-4} + q^{-3} + q^{-1}$ \| $0.973$ \|` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `observations/time-reversal-energy-barrier.md:13` | `The proton is a [Borromean baryon](#def:borromean-baryon): $\mathfrak{p} = [\mathfrak{u}, \mathfrak{u}, \mathf…` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `observations/time-reversal-energy-barrier.md:31` | `The neutron decay $\mathfrak{n} \to \mathfrak{p} + e^- + \bar{\nu}_e^{\sigma}$ changes the crossing orientatio…` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `predicted-spectra/antineutrino-knot.md:11` | `In $\beta^-$ decay, the $L_0^{-}$ smoothing of the $\mathfrak{d} \to \mathfrak{u}$ crossing change yields the …` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `predicted-spectra/electron-knot.lean:10` | `It is the lepton partner of the up quark, which is an unknot localized` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `predicted-spectra/electron-knot.md:7` | `It is the lepton partner of the [up quark](#def:up-quark) in the [knot–particle dictionary](#rem:knot-particle…` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `predicted-spectra/knot-formula-table-table2-data.md:8` | `\| Up quark \| $\mathfrak{u}$ \| unknot strand, $\sigma_i$ (partner $T_{2,3}$) \| $0$ \| $0$ \|` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `predicted-spectra/knot-formula-table-table4-data.md:3` | `\| Proton \| $\mathfrak{p}$ \| $[\mathfrak{u}, \mathfrak{u}, \mathfrak{d}]_p \oplus \mathcal{L}_H$ \|` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `predicted-spectra/knot-formula-table-table4-data.md:4` | `\| Neutron \| $\mathfrak{n}$ \| $[\mathfrak{u}, \mathfrak{d}, \mathfrak{d}]_p \oplus \mathcal{L}_H$ \|` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `predicted-spectra/knot-formula-table-table4-data.md:5` | `\| $\pi^+$ \| \| $\mathfrak{u} \oplus \mathfrak{d}^{\sigma}$ \|` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `predicted-spectra/knot-formula-table-table4-data.md:6` | `\| $\pi^0$ \| \| $(\mathfrak{u} \oplus \mathfrak{u}^{\sigma} + \mathfrak{d} \oplus \mathfrak{d}^{\sigma})/\!\s…` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `predicted-spectra/knot-formula-table-table4-data.md:7` | `\| $K^+$ \| \| $\mathfrak{u} \oplus \mathfrak{s}^{\sigma}$ \|` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `predicted-spectra/knot-formula-table-table4-data.md:8` | `\| $\Lambda$ \| \| $[\mathfrak{u}, \mathfrak{d}, \mathfrak{s}]_p \oplus \mathcal{L}_H$ \|` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `predicted-spectra/knot-formula-table-table4-data.md:9` | `\| $\Sigma^+$ \| \| $[\mathfrak{u}, \mathfrak{u}, \mathfrak{s}]_p \oplus \mathcal{L}_H$ \|` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `predicted-spectra/knot-formula-table.md:8` | `The up and down quarks are not independent generators. Each is an unknot strand of the Borromean braid $\mathc…` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `predicted-spectra/knot-formula-table.md:11` | `\mathfrak{u} \leftarrow T_{2,3}, \qquad` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `predicted-spectra/knot-formula-table.md:23` | `\mathfrak{p} = [\mathfrak{u}, \mathfrak{u}, \mathfrak{d}]_p \oplus \mathcal{L}_H,` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `predicted-spectra/knot-formula-table.md:25` | `\mathfrak{n} = [\mathfrak{u}, \mathfrak{d}, \mathfrak{d}]_p \oplus \mathcal{L}_H.` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `predicted-spectra/linking-relations-table-table1-data.md:3` | `\| $T_{2,3}$ \| $T_{2,3}$ \| $T_{2,3} \oplus T_{2,3}$ \| $2$ \| lepton-partner pair of $\mathfrak{u}\mathfrak{…` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `predicted-spectra/linking-relations-table-table1-data.md:4` | `\| $T_{2,3}$ \| $T_{2,3}^{\sigma}$ \| $T_{2,3} \oplus T_{2,3}^{\sigma}$ \| $2$ \| lepton-partner pair of $\mat…` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `predicted-spectra/linking-relations-table-table1-data.md:8` | `\| $T_{2,3}$ \| $T_{2,5}$ \| $T_{2,3} \oplus T_{2,5}$ \| $2$ \| lepton-partner pair of $\mathfrak{u}\mathfrak{…` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `predicted-spectra/linking-relations-table-table1-data.md:9` | `\| $T_{2,3}$ \| $T_{2,5}^{\sigma}$ \| $T_{2,3} \oplus T_{2,5}^{\sigma}$ \| $2$ \| lepton-partner pair of $\mat…` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `predicted-spectra/linking-relations-table-table2-data.md:9` | `\| $T_{2,3} \oplus T_{2,3}$ \| Skein at crossing \| $4_1$ \| lepton-partner pair of $\mathfrak{u}\mathfrak{u}$…` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `predicted-spectra/linking-relations-table-table5-data.md:3` | `\| $\mathfrak{d} \to \mathfrak{u}$ in $\mathfrak{n}$ \| $L_0^{-}$ \| $T_{2,3} \sqcup T_{1,0}^{\sigma}$ \| $e^-…` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `predicted-spectra/linking-relations-table-table5-data.md:4` | `\| $\mathfrak{u} \to \mathfrak{d}$ in $\mathfrak{p}$ \| $L_0^{+}$ \| $T_{2,3}^{\sigma} \sqcup T_{1,0}$ \| $e^+…` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `predicted-spectra/linking-relations-table-table5-data.md:5` | `\| $\mathfrak{s} \to \mathfrak{u}$ in $\Lambda$ \| $L_0^{-}$ \| $T_{2,3} \sqcup T_{1,0}^{\sigma}$ \| $e^- + \n…` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `predicted-spectra/nuclear-spin-parity-proof.md:2` | `Each nucleon—proton $\mathfrak{p} = \mathcal{B}_3(\mathfrak{u}, \mathfrak{u}, \mathfrak{d})$ or neutron $\math…` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `predicted-spectra/q-chromaticity.md:38` | `An individual quark is an unknot strand carrying one crossing letter within a single color tube; the trefoil $…` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `predicted-spectra/torus-knot-prime-powers.md:16` | `\| $1$ \| $T_{3,2} = T_{2,3}$ (trefoil $3_1$) \| $1$ \| $3$ \| Yes \| Electron $e^-$ (lepton partner of $\math…` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `predicted-spectra/torus-knot-prime-powers.md:31` | `The trefoil is the unique generator at the intersection of the $m = 2$ (leptonic) and $m = 3$ (quark) families…` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `predicted-spectra/torus-knot-prime-powers.md:65` | `- $k = 1$: $T_{3,2}$ = trefoil. Lightest matter (the electron, lepton partner of the up quark).` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `predicted-spectra/unmapped-torus-knots.md:14` | `- $T_{2,3}$: electron $e^-$; lepton partner of the up quark $\mathfrak{u}$ (genus 1)` | D | quark as unknot strand / lepton-partner label / no knot-type claim |
| `predicted-spectra/unmapped-torus-knots.md:27` | `\| $T_{2,3}$ \| $3$ \| $1$ \| Matter (electron; partner of the up quark) \|` | D | quark as unknot strand / lepton-partner label / no knot-type claim |

## 5. Q_β: derived from γγ; 0.3254 MeV is Q_β, not m_n − m_p

Spellings searched: `Q_β`, `Q_{\beta}`, `Q_beta`, `QBeta`, `qbeta`, `Q-value` beside
`m_n − m_p` (several dash spellings), `Δ_pn`, `\Delta_{pn}`, "neutron-proton mass
difference/splitting" or `0.3254`. Also `0.325`, "weight split", `T³` / `T^3`, `flavour`
beside the n–p splitting.

**No stale site found.** Both places that state the scored cell
(`observations/mass-comparison-table.md:39`,
`nuclear-interactions/neutron-qvalue-symbolic.md:61-69`) call 0.3254 MeV the scored Q_β.
They derive `m_n − m_p = Q_β + m_e ≈ 0.8364` MeV from it, which follows the ruling. The
other hits are the kinematic identity `Q_β = m_n − m_p − m_e` or dashboards that list
`Q_β` and `Δ_pn` as separate rows. The "flavour split" in `MarkovBondRule`,
`FlavourSplitNormalisation` and similar files is `Δm/M_N` (`prop:flavor-split-substrate`),
a different object.

The γγ *derivation* half of the ruling was not audited. It concerns compute routes, which
are in open PRs #8681, #8693, #8696 and #8707.

### Sites

| site (path under `folio/quantum-observable-universe/`, line at `bccf522bb5d`) | quoted phrase | class | action |
|---|---|---|---|
| `knots-particles-confinement/delta-skein-substrate-identity.lean:35` | `Conventional CODATA identity Q_β = m_n − m_p − m_e gives` | D | CODATA kinematic identity Q_β = m_n − m_p − m_e |
| `knots-particles-confinement/delta-skein-substrate-identity.lean:36` | `(m_n − m_p) / m_e = (Q_β + m_e) / m_e. -/` | D | CODATA kinematic identity Q_β = m_n − m_p − m_e |
| `knots-particles-confinement/delta-skein-substrate-identity.lean:52` | `Combined with CODATA 'm_n − m_p = Q_β + m_e', this yields the` | D | CODATA kinematic identity Q_β = m_n − m_p − m_e |
| `lean/QOU/BraidKnot/IsotopeRecord.lean:62` | `\| CAL_3 -- Q_β(neutron) = m_n - m_p - m_e` | D | Q_β = m_n − m_p − m_e is the kinematic identity, not the scored cell (aside: labelled CAL_3; Q_β is the CAL-2 proxy) |
| `lean/QOU/Observations/L2_100x_SharedRoot.lean:31` | `'Q_β', 'm_n', 'Δ_pn' all derive from the same Path-C chain` | D | lists Q_β and Δ_pn as separate observables |
| `lean/QOU/OptionE/CrystalDeltaLambdaScaffold.lean:36` | `The current L2 100× dashboard has 3 failures (Q_β, m_n, Δ_pn) all` | D | lists Q_β and Δ_pn as separate observables |
| `lean/QOU/OptionE/CrystalDeltaLambdaScaffold.lean:162` | `shared-root observables (Q_β, m_n, Δ_pn). -/` | D | lists Q_β and Δ_pn as separate observables |
| `lean/QOU/QBeta/MeasurementLimitedFloor.lean:5` | `misses (Q_beta, m_n, Delta_pn via c_3; m_p, m_mu via q_0) are gated on the` | D | lists Q_β and Δ_pn as separate observables |

## Asides found on the way (not among the five rulings; nothing changed)

1. **`L_± = σ₀σ₁, σ₁σ₀` is labelled "Hopf link" in many places, but its closure on three
   strands is the unknot.** `σ₀σ₁` permutes the strands by a 3-cycle, so it closes to one
   component (`ElectronWordCandidates.numCycles_permOf_of_even` allows 1 or 3). Markov
   destabilisation gives `σ₀ ∈ B₂`, whose closure is the unknot. Examples:
   - `appendix-knot-operations-archimedean/particle-nf-table-table-data.md` rows `L_±`
     "Hopf `T(2,2)`";
   - `nuclear-interactions/nucleon-nf-observability.md:18`;
   - `QBeta/QBetaZeta4ResidueRefutation.lean:173`;
   - `BraidKnot/DeltaLambdaSignRule.lean:450`;
   - `mass-theory/qbeta-odd-carrier-hopf-cubic.md:43`.

   Together with ruling 1 this produces a sharper collision: the corpus now calls both
   `e⁻ = σ₀σ₁σ₀` (correctly) and `L_±` (incorrectly) "the Hopf link". This needs an owner
   decision on naming. It was not grepped exhaustively.
2. **`BraidKnot/IsotopeRecord.lean:62`** labels `CAL_3` as `Q_β(neutron) = m_n − m_p −
   m_e`. Under the 2026-06-26 calibration ruling, CAL-3 is `𝔇_π` (proxy `m_π`), and `Q_β`
   is the CAL-2 proxy.


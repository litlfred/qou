# Retired corpus labels cited in `computations/` docstrings — the record (2026-10-11)

**26 corpus labels are cited in `computations/` producer docstrings and resolve
to no content block anywhere in `folio/`.** This document is where those
citations now point. It exists so that a reader following a reference in a
producer lands on the decision that retired the block, rather than on nothing.

Measured with
[`computations/audits/docstring_label_carrier_audit.py`](../../computations/audits/docstring_label_carrier_audit.py)
(**489** distinct labels cited across **862** files; **26** dead, **58**
citations). The audit is wired **blocking** in
[`scripts/precision-gates.sh`](../../scripts/precision-gates.sh) as a draining
ratchet. Bean `qou-3kni`; the surface was unmeasured before #7586, where the
bean's own sample of *"three dead labels in two files"* turned out to understate
it **8×**.

## Why the labels live here and not in the docstrings

The producers that cited these labels no longer name them. That is deliberate
and it is the point of this document: a bare `prop:…` string in a docstring is a
pointer to nothing, whereas a path into this file is a pointer to the record.
Each docstring now cites this document and its section.

It also makes the gate drainable. The audit scans `computations/**/*.py`
docstrings only, so it **cannot distinguish citing a dead label from documenting
that one is dead** — a producer explaining a retired label in prose *raises* the
count, which is how a citation fix once moved it 25 → 26. Moving the label
strings into `docs/`, which the audit does not scan, resolves that: the record
is complete and the count falls.

## The three groups, and why the distinction matters

Commit archeology over all 26 (pickaxe `git log --all -S'"<label>"' -- '*.ts'`,
plus a tree read at `0763606e4f^`) splits them three ways, and the remedy
differs per group:

| group | n | citations | what happened | content recoverable? |
|---|---:|---:|---|---|
| **A** | 10 | 40 | demoted to `_deprecated/` | yes, at `0763606e4f^` |
| **B** | 9 | 11 | deleted outright, never demoted | yes, from the deleting commit's parent |
| **C** | 7 | 7 | never existed as a `.ts` label at all | no — there is nothing to recover |

🛑 **An earlier account of this population had two groups (12 / 8).** That
partition does not reproduce: there are three groups, and **group B is the one
neither remedy covered** — its blocks existed and their content is recoverable,
but they never went to `_deprecated/`, so neither "record it in an audit doc"
nor "remove the citation" is quite right for them. They are recorded here with
their deleting commit, which is the pointer a reader actually needs.

🛑 **`_deprecated/` is no longer on `main`** (removed 2026-10-10; it survives on
branch `cat/cat-harness/fsh-guts`). Every path below is therefore
**commit-pinned**. A pinned path outlives any branch and cannot be broken by a
later move, which is why it is preferred here over a branch reference.

## A — demoted to `_deprecated/` (10 labels, 40 citations)

Demoted by `61c039faab` (batch3d: 7 internal-negative + empirical-fit blocks),
`3987845811` (batch3e: 25 cross-referenced internal-negative), `8ed2344cc4`
(batch3c: 24 thimble/PL/SW) and `94ae918ad0` (2 falsified conjectures) — then
untracked wholesale by `0763606e4f`, whose subject mentions only the
agent-scratch dirs and not `_deprecated/`.

### `prop:li2q-phiq-bar-symmetrization` {#a-li2q-phiq-bar-symmetrization}

- **Was:** `_deprecated/internal-negatives-batch2/li2q-phiq-bar-symmetrization.md`
- **Recover:** `git show 0763606e4f^:_deprecated/internal-negatives-batch2/li2q-phiq-bar-symmetrization.md`
- **Stated:** **Proposition ($\mathrm{Li}_2^q$ as bar-anti-symmetrization of Faddeev $\Phi_q$, rescaled by $h/2$).**

### `prop:constit-factor-tau-M-proton-identity` {#a-constit-factor-tau-m-proton-identity}

- **Was:** `_deprecated/internal-negatives/constit-factor-tau-M-proton-identity.md`
- **Recover:** `git show 0763606e4f^:_deprecated/internal-negatives/constit-factor-tau-M-proton-identity.md`
- **Stated:** **Proposition (Constit-side per-Z step factor = $\mathrm{tr}_M^3(\mathcal{B}_p)$).**

### `conj:delta-lambda-categorical-closure` {#a-delta-lambda-categorical-closure}

- **Was:** `_deprecated/thimble-content/delta-lambda-categorical-closure.md`
- **Recover:** `git show 0763606e4f^:_deprecated/thimble-content/delta-lambda-categorical-closure.md`
- **Stated:** **Conjecture (per-partition $\Delta_\lambda(K)$ as block algebraic residue).**

### `prop:mass-formula-iterative-lp-dual` {#a-mass-formula-iterative-lp-dual}

- **Was:** `_deprecated/internal-negatives-batch2/mass-formula-iterative-lp-dual.md`
- **Recover:** `git show 0763606e4f^:_deprecated/internal-negatives-batch2/mass-formula-iterative-lp-dual.md`
- **Stated:** **Proposition (LP-dual characterisation of the QOU mass formula).** *Let $\varrho \in H_n(R, q)$ be a quantum-observable knot (QOU braid representative of a hadronic state) of strand count $n = 3A$, and let $J^\bullet \subset H_n(R, q)$ be the

### `conj:constit-factor-2q-minus-1` {#a-constit-factor-2q-minus-1}

- **Was:** `_deprecated/internal-negatives/constit-factor-2q-minus-1.md`
- **Recover:** `git show 0763606e4f^:_deprecated/internal-negatives/constit-factor-2q-minus-1.md`
- **Stated:** **Conjecture (Constit-side per-Z step factor in canonical-atom Markov trace).**

### `conj:denominator-zeros-as-sw-critical-points` {#a-denominator-zeros-as-sw-critical-points}

- **Was:** `_deprecated/thimble-content/denominator-zeros-as-sw-critical-points.md`
- **Recover:** `git show 0763606e4f^:_deprecated/thimble-content/denominator-zeros-as-sw-critical-points.md`
- **Stated:** **Conjecture (Denominator zeros = SW critical points).** *Let $\Phi_n(x; q_0)$ be the $q$-Pochhammer partial product ([q-Pochhammer partial product](#def:q-pochhammer-partial-product)) attached to a Hecke normal form word at GB-depth $n$, and let

### `conj:lambda-scale-bring-bloch-identity` {#a-lambda-scale-bring-bloch-identity}

- **Was:** `_deprecated/internal-negatives-batch2/lambda-scale-bring-bloch-identity.md`
- **Recover:** `git show 0763606e4f^:_deprecated/internal-negatives-batch2/lambda-scale-bring-bloch-identity.md`
- **Stated:** **Conjecture (categorical identity for the per-knot scale factor $\lambda_K^{\mathrm{scale}}$, status revised 2026-05-22).**

### `conj:shell-correction-term-seven` {#a-shell-correction-term-seven}

- **Was:** `_deprecated/internal-negatives-batch2/shell-correction-term-seven.md`
- **Recover:** `git show 0763606e4f^:_deprecated/internal-negatives-batch2/shell-correction-term-seven.md`
- **Stated:** The paper's unified six-term mass formula ([unified knot mass](#thm:knot-mass-formula-unified)) covers Hecke-algebraic content — descended trace, brane towers, Frobenius co-Casimir, chirality, and higher-stratum residues — but under-predicts isotope masses for $A \geq 5$ by $\sim 10\%$.

### `conj:alpha-cosh-h-z-step-correction` {#a-alpha-cosh-h-z-step-correction}

- **Was:** `_deprecated/internal-negatives/alpha-cosh-h-z-step-correction.md`
- **Recover:** `git show 0763606e4f^:_deprecated/internal-negatives/alpha-cosh-h-z-step-correction.md`
- **Stated:** **Conjecture (Per-Z step factor in the Δ_λ closure form).**

### `conj:n-sym-symmetric-channel-normalization` {#a-n-sym-symmetric-channel-normalization}

- **Was:** `_deprecated/internal-negatives/n-sym-symmetric-channel-normalization.md`
- **Recover:** `git show 0763606e4f^:_deprecated/internal-negatives/n-sym-symmetric-channel-normalization.md`
- **Stated:** **Conjecture (symmetric-channel Plancherel normalization).** *The closed-form expression for $N_v$ in [`conj:weak-spectral-completeness`](#conj:weak-spectral-completeness) takes the form*

## B — deleted outright (9 labels, 11 citations)

These never went to `_deprecated/`. The content is recoverable from the
deleting commit's parent, and that commit's subject is usually the reason.

| label | deleted in | the deleting commit's subject | recover |
|---|---|---|---|
| `conj:pl-jsj-mass-integration-equivalence` | `f86ea9d7ac` | content(thimble): demote def:picard-lefschetz-thimble + delete redundant | `git show f86ea9d7ac^ -- '**/pl-jsj-mass-integration-equivalence.md'` |
| `prop:q-schur-y-lambda-closed-form` | `edf658ff19` | fix(crossref): resolve fatal undefined references | `git show edf658ff19^ -- '**/q-schur-y-lambda-closed-form.md'` |
| `conj:chirality-ribbon-frobenius` | `e8086e521f` | cut 9 exploratory/falsified probe blocks from paper | `git show e8086e521f^ -- '**/chirality-ribbon-frobenius.md'` |
| `conj:magic-shell-stabilization` | `3af08b4a9a` | fix(validate): repair main-side CI breakage — 330 → 0 errors | `git show 3af08b4a9a^ -- '**/magic-shell-stabilization.md'` |
| `conj:sdp-rank-collapse-magic-shell` | `f8fbcc5ce3` | algebraic-refactor: cleanup — remove 3 deprecated conjectures + cherry-p | `git show f8fbcc5ce3^ -- '**/sdp-rank-collapse-magic-shell.md'` |
| `prop:b-over-a-spectral-decomposition` | `c703e576b5` | content+compute: delete stale b-over-a-spectral-decomposition + v3 artif | `git show c703e576b5^ -- '**/b-over-a-spectral-decomposition.md'` |
| `prop:free-config-chi-lr-equivalence` | `44abba3fc8` | consolidate(props): demote lr-tensor-character-bridge → corollary, delet | `git show 44abba3fc8^ -- '**/free-config-chi-lr-equivalence.md'` |
| `rem:per-partition-k-lambda-rule` | `690458d6b0` | content(mass): remove per-partition-k-lambda-rule refuted table; audit-d | `git show 690458d6b0^ -- '**/per-partition-k-lambda-rule.md'` |
| `rem:q-integer-mass-table` | `d47319404b` | excise appendix-atomic-mass-calculations (redundant to recursive knot-pa | `git show d47319404b^ -- '**/q-integer-mass-table.md'` |

Three are worth a note. `c703e576b5` deleted both the block **and** its
compute, recording that the formula *"is NOT the canonical formula. v3 was
attacking the wrong target."* `44abba3fc8` removed a child block whose
**parent** `prop:hecke-branching-trace-decomposition` is live, so that
citation is redirected to the parent rather than here. And `690458d6b0`
removed the `rem:` spelling of the `k_λ` rule, whose record is
[`2026-06-17-refuted-ansatz-lemmas.md`](2026-06-17-refuted-ansatz-lemmas.md)
— that is where its citations point, not here.

## C — never existed as a `.ts` label (7 labels, 7 citations)

Pickaxe over all history (`git log --all -S'"<label>"' -- '*.ts'`) returns
**nothing** for each of these, and no file named for the stem exists at
`0763606e4f^` or on `main`. So there is no block, no content to recover, and
nothing for a citation to point at. The citations are removed rather than
redirected.

- `prop:cosh-sinh-q-bridge`
- `prop:frobenius-co-casimir-master`
- `prop:option-e-binding-energy`
- `prop:per-partition-k-lambda-rule`
- `prop:proton-mass-frobenius-co-casimir`
- `prop:proven-unwired-regression-2026-05-25`
- `rem:mass-endomorphism-tower-adjacency-audit`

🛑 **`prop:per-partition-k-lambda-rule` is the one trap in this group.** The
label string never existed — but the **content** did, under the `rem:`
spelling in group B, and its record is in
[`2026-06-17-refuted-ansatz-lemmas.md`](2026-06-17-refuted-ansatz-lemmas.md).
So its citations are **redirected there, not removed**: a blanket "group C
→ delete" would have thrown away a live pointer. The two spellings differing
only in prefix is why the three-way split has to be read per label and not
per group.

## D — carried only by a deprecated witness filename (2 labels, 4 citations; added 2026-10-12)

Found when #7586 was merged with `main`. The carrier audit counts any tracked
path containing the label's stem as a carrier, so these two were "alive" only
through `computations/_deprecated/{hopf-jones-c3,kashiwara-jones-c4}-categorical.witness.json`.
Neither ever had a `.ts` block. `6333715860` (fsh-guts cut-over, bean `qou-6u3n`)
removed `computations/_deprecated/` from `main`, and the ratchet went 0 -> 2.
Disposed of per the owner's 2026-10-12 group-B ruling (point at the removal commit).

| label | carried by | removed in | recover |
|---|---|---|---|
| `prop:hopf-jones-c3-categorical` | `computations/_deprecated/hopf-jones-c3-categorical.witness.json` | `6333715860` | `git show 6333715860^:computations/_deprecated/hopf-jones-c3-categorical.witness.json`, or the `cat/cat-harness/fsh-guts` branch |
| `prop:kashiwara-jones-c4-categorical` | `computations/_deprecated/kashiwara-jones-c4-categorical.witness.json` | `6333715860` | same, `kashiwara-jones-c4-categorical.witness.json` |

Cited from `computations/sweeps/paper_six_term_isotope_sweep.py` (docstrings of
the N=4 chain and `q_beta_for_source`). That docstring also calls `c_3`/`c_4`
"categorically derived (no empirical fit)"; the AGENTS.md `c_k` banners scope
that ladder as convention-C and its rungs as near-matches, so the claim is
stale — recorded here, not edited, as it is outside this re-pointing.

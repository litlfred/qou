# Owner-gated bean triage — the veto ledger

**Started:** 2026-09-05 · **Bean:** `qou-fs4r` · **Mode:** owner chose *"triage +
propose a default for each; I veto rather than choose"* (Q2 option 3, 2026-09-05).

**How to use this:** read the **DEFAULT** column. Anything you do not veto, I
apply. Reply with the bean IDs you want changed — e.g. *"veto qou-zdz5, qou-agvb"*.

**One adjustment I made to the option you chose, and why.** Where a default would
land a **physics or convention claim**, I do **not** propose one. Those are marked
**NO DEFAULT** and get their options laid out instead. Silence-as-assent is
efficient for mechanics and is exactly how a wrong physics ruling gets laundered
into the corpus — which is the risk you accepted the rest of this trade for, not
one to spend on the claims themselves.

---

## The count was wrong three times. Here is the method.

I quoted **51**, then **67**, then **81**. All three were keyword scans over bean
prose with different patterns, and none is authoritative on its own.

Split properly, the **81** in-progress beans matching any owner-phrase are:

| | count | meaning |
|---|---:|---|
| **PENDING** | **33** | a live ask — "needs an owner decision", "still needs the owner's call", "author's call" |
| HISTORICAL ONLY | 18 | a *past* ruling being cited — "by owner decision", "per owner instruction", "Owner ruling 2026-08-15" |
| (pending, also citing history) | 3 | counted in PENDING |

The remaining 30 of the 81 matched only the looser patterns of the earlier scans.

**So the real backlog is 33, and 18 of the apparent backlog was you being quoted
back to yourself.** That is the single most useful thing this triage produced and
it cost one grep — the earlier counts conflated a pending ask with a citation of a
settled one.

---

## Pass 1 — classification

`A` mechanical (default proposed) · `B` physics/convention (**NO DEFAULT**) ·
`C` stale or already answered (default: close)

### Class A — mechanical, default proposed, veto to change

| bean | the ask | **DEFAULT** |
|---|---|---|
| `9h6x` | lake-cache archive truncated; left open "for the author to close" | **close it** — infra task, nothing downstream reads it |
| `qou-agvb` | witness provenance spelled three ways (`scriptFile`/`computation`/`producer`); a canonical spelling is proposed | **adopt the proposed spelling**, migrate readers; reversible, no number moves |
| `qou-jvav` | a resolver crash is fixed; whether to add an appendix section is separate | **do not add the appendix**; keep the crash fix |
| `qou-pwut` | 87 root-level QA writers bypass `qa-agent-entry.ts` | **no-op** — leave them; a refactor of that size needs its own justification |
| `qou-7yj0` | ten trivially-inhabited `BorromeanQuark` classes | **follow the bean's own standing recommendation: touch neither file** |
| `qou-52i4` (part) | seed the lake-cache orphan branch | **seed it** — pure infra (the `would_shrink()` half is separate, below) |

### Class B — physics or convention. NO DEFAULT. Options in pass 2.

`gm4q` · `qou-1jw9` · `qou-2tuv` · `qou-48is` · `qou-8na1` · `qou-aemx` ·
`qou-c66b` · `qou-cds1` · `qou-d7h1` · `qou-goc9` · `qou-hey2` · `qou-im4m` ·
`qou-imkb` · `qou-r4ya` · `qou-t7mt` · `qou-w1g8` · `t7qv`

**Two of these are already in front of you from another route:**

- **`qou-goc9`** — *"which nucleon NF is canonical for the Q_beta counit chain?"*
  This is **the same question as Q4** in today's analysis (chain `A−1` vs complete
  graph `C(A,2)`). Answer it once, both close.
- **`qou-cds1`** — the `c_k` ladder re-derivation under convention D. It is not a
  judgement so much as **authorisation to spend**: the bean says it needs your go,
  and it is a large compute.

### Class C — provisionally stale; default is to close

| bean | why | **DEFAULT** |
|---|---|---|
| `qou-gwe9` | its subject — "Copilot review does not arrive" — was **corrected on `main` 2026-08-30**: reviews do arrive and are quota-rationed | **close**, superseded by the correction |
| `qou-324i` | its own text says *"Measurement settles it"*, not an owner call | **reclassify as agent-actionable**, remove from this queue |

### Not yet classified (pass 2)

`dgpc` · `qou-58zw` · `qou-9xla` · `qou-e9pp` · `qou-octr` · `qou-qflp` ·
`qou-r765` · `qou-zdz5` · `qou-zzwm` · `qou-52i4` (the `would_shrink()` half)

**`qou-zzwm` is flagged now rather than left to pass 2**: it reports that the
C→D excision left **published accuracy figures** behind. If that is right it is a
correctness defect in reader-facing numbers, not a preference — it should not sit
in a veto queue at all. Verifying it is the first item of pass 2.

---

## Pass 2 — the remaining 9, and a pattern

### 🛑 Four more are FALSE POSITIVES — the ask was already answered, inside the bean

This is the pass-2 headline, and it is the same shape as the 18 historical-only
hits: **a bean says it needs the owner, then resolves the question further down and
never updates the line at the top.** A keyword scan reads the stale sentence.

| bean | the stated ask | why it is not pending |
|---|---|---|
| `qou-zzwm` | *"either the dashboard records the frame it inherited, or the ladder is re-derived under D"* | **the first branch was taken.** Verified live: `per-observable-100x-status.witness.json` now carries `convention_frame_qbeta`, `reproducible_under_canonical_convention`, and explicit text naming the C frame and the 2026-08-15 ruling. The figures are no longer published bare. Live remainder is `qou-cds1`, already its own bean. |
| `qou-zdz5` | Λ vs Cl₂ wrong forms, 54 sites | the bean's own text: *"a name is not revising a finding, so no ruling was needed. **Had** any site carried a wrong value feeding a conclusion, that **would have been** the owner's call."* Conditional, and the condition was **not met**. |
| `qou-52i4` | the `would_shrink()` guard blocking a cache reseed | *"the 4459-vs-7268 obstacle predicted above is **not actually enforced**"* — the guard is skipped because the incumbent branch records no counts. Moot. |
| `qou-e9pp` | a producer requesting the muon anchor that `q_parameter` refuses | **answered by the owner ruling of 2026-08-30**: proton unless (E1) an explicit proton-vs-muon comparison or (E2) the ideal CAL-1/2/3 layer. This producer is neither. |

**So of 33 "pending", 4 were already decided.** Combined with the 18
historical-only, **22 of the original 81 were noise from the same root cause** —
a stale sentence outliving the work that answered it.

### Class A additions — default proposed, veto to change

| bean | the ask | **DEFAULT** |
|---|---|---|
| `qou-58zw` | 11 witnesses: regenerate (destroys recorded analysis, **including a retraction**) vs restore producing code from history | **restore the producing code; do not regenerate.** The conservative choice preserves evidence; a regenerated witness cannot be un-regenerated |
| `qou-9xla` | 178 actionable sites; the bean says *"should probably be sequenced, not swept"* | **no-op now** — do not start; a sweep of that size needs its own sequencing plan first |
| `qou-qflp` | 74 witnesses at a value that is neither canonical pin | **no new bulk action; fold into `qou-3f7a`**, which already scopes exactly this drain. AGENTS.md warns specifically against bulk re-pinning |
| `qou-r765` | a two-line signature change to classes predating the work | **do not change the signature.** It is one rung; wait for a rung that needs it |

### Class B additions — physics or claim change, NO DEFAULT

| bean | why it is not defaultable |
|---|---|
| `dgpc` | bundles a **`status: "verified"` downgrade** on two blocks with an AME re-point. Downgrading a verified block is a claim change |
| `qou-octr` | *"adding the missing hypotheses to each context class — a claim change"*. Its own words |

---

## Where the 33 landed

| class | count | meaning |
|---|---:|---|
| **A — default proposed** | **10** | veto any you want changed; silence applies them |
| **B — NO DEFAULT** | **19** | physics / convention / claim change; options in pass 3 |
| **C — not actually pending** | **6** | 2 from pass 1, 4 from pass 2; default is to close or reclassify |

**Class A, the full veto list:** `9h6x` `qou-agvb` `qou-jvav` `qou-pwut`
`qou-7yj0` `qou-52i4` `qou-58zw` `qou-9xla` `qou-qflp` `qou-r765`

**Class C, proposed closed:** `qou-gwe9` `qou-324i` `qou-zzwm` `qou-zdz5`
`qou-52i4`(guard half) `qou-e9pp`

---

## The finding that outlives this triage

**22 of 81 apparent owner-asks were stale sentences, not open questions** — 18
citing a past ruling, 4 answered inside their own bean. The queue was ~27 %
noise, and every one of those would have cost a round-trip to a physically-
disabled author.

The cheap fix is a convention, not a tool: **when a bean answers its own owner-ask,
edit the asking sentence** rather than appending the answer below it. A grep sees
the first sentence.

## Pass 3 — the 19 Class B collapse to 7 questions, and one already has its answer measured

The point of this pass is **not** 19 write-ups. It is that several beans are the
same question wearing different names, and one of them already carries the
measurement the others are waiting for.

---

### 🔴 CLUSTER 1 — the inter-nucleon interface topology. **FOUR beans, ONE question, and the data already exists.**

**Beans:** `qou-goc9` · `qou-im4m` · `t7qv` · plus **Q4 of today's analysis**.

**The question:** does a nucleus wire its nucleons as a **linear chain** (`A−1`
interfaces, what `atom_braid_word_3A` builds) or **all pairs** (`C(A,2)`, what
`build_atom_nf` / `atom_gen_chains` build)?

**`t7qv` RESULT 4 already measured it** (AME read-only, no fit):

| model | 2H/3He | 3H/3He |
|---|---|---|
| chain (adjacent) | 0.50000 (+73.5 %) | 1.17024 (+6.5 %) |
| **all pairs** | **0.40361 (+40.0 %)** | 1.20327 (+9.5 %) |
| EXPERIMENT | 0.28823 | 1.09896 |

All-pairs nearly **halves** the A-scaling error and costs ~3 points on the mirror.

**🛑 And `t7qv` RESULT 5 says NEITHER IS RIGHT.** Solving each ratio for a single
distance-2 weight gives `f = +2.030134` from A-scaling and `f = −0.696951` from
the mirror — wildly inconsistent, one negative. **A one-parameter falloff is
refuted outright.** Per-type rates would be 2 unknowns against 2 ratios: exactly
determined, i.e. a fit with zero predictive content at this size.

**So the honest statement is: all-pairs is the better of two topologies that are
both wrong.** Anyone quoting RESULT 4 without RESULT 5 is quoting a preference
between refuted options as if it were a result.

**What this cluster needs from you** is not "pick one". It is a ruling on
**whether the two builders may keep disagreeing** while the real topology is
open. Today they do, silently, and one of them reaches the paper
(`demand-stability.ts` → all-pairs) while the other reaches the binding numbers
(`binding_canonical` → chain).

---

### 🔴 CLUSTER 2 — `qou-1jw9` is not a preference. It reports a **fourth calibration**.

Flagging this the way `qou-zzwm` was flagged, and this one **survived the check**.

The bean reports a molecular-observable calibration: `0.687012518457808 ×
27.296143240836667 × 0.23879110765149733 = 4.478000 eV`, H₂'s **measured** bond
energy — where the same witness's own `H2_cross_check` records the uncalibrated
`18.75279 eV` (4.19× too large), and `4.478 / 18.753 = 0.23879` **exactly**.

Under the standing **🟥 NO FITTING, EXCEPT CAL-1/2/3** directive that is not a
judgement call about taste — it is a discipline violation to adjudicate. Two
further defects ride along: `E_hartree_eV = 27.296143` vs CODATA `27.211386`
(**+0.31 %**, so not the Hartree), and the witness **contradicts its own content
block** on which of σ/π carries the largest `|V|`.

**🛑 CORRECTION, same session — I over-escalated this, and it is the third time.**

Verified rather than read, the way `qou-zzwm` should have taught me the first time:

- the producer `co-molecular-binding.py` is in **`_deprecated/`**;
- its witness is **absent from the tree** — the block's own prose says so;
- the content block's machine-readable `computation:` link points to a
  **different, live** producer (`co_bond_order_active_set.py`), not this one;
- and the block **already documents the `4.478 / 18.753` ratio in its own prose**,
  as a caveat, at `co-triple-bond-energy.md:29`.

So it is a **disclosed, deprecated artifact**, not a live undisclosed fit. The
NO-FITTING directive is not being violated in the live chain.

**What is actually left** is a content call of ordinary size: should a block keep
quoting a number derived from a retired, calibrated producer whose witness no
longer exists? That is Class B, and it is **not** the urgent escalation I made it.

---

### CLUSTER 3 — convention-D re-derivation. `qou-cds1` · `qou-2tuv`

Not judgements so much as **authorisation to spend** plus one scope call.
`qou-cds1` says in its own words *"still needs the owner's go: the actual D-frame
re-derivation"* — a large compute, and the 2026-08-30 bar-weight prune established
the obstruction is the **offset, not z**, so a z-swap is invalid. `qou-2tuv` asks
whether the binding channel may use CAL-3 as an acknowledged anchor — and flags
that **two scales are live in one table on different channels today**, which is
the part that is not a preference.

### ~~CLUSTER 4 — Lean class/axiom shape. `qou-t7mt` · `qou-w1g8` · `qou-octr`~~ ✅ **RESOLVED 2026-09-05 — none of the three needs an owner ruling**

**🛑 The paragraph this replaces was mine and was wrong on its central claim.**
It read: *"All three are 'change a class signature / add missing hypotheses',
which is a **claim change**. `qou-octr` proves 8 of 8 context-class sorries are
**unclosable** in their current form, so this cluster is not optional work — the
current forms cannot be discharged."* I quoted that "8 of 8" three times in
reports before checking it. Checked, all three deflate:

**`qou-octr` — scope discharged; the sorries do not exist.** All eight
declarations are **sorry-free today**. The naive check disagrees, in the
direction that misleads: `grep '\bsorry\b'` over the eight returns **21 hits
and zero are proof terms** — every one is inside a docstring or comment, in
prose *about* `sorry`, because these files argue at length about why a `sorry`
would be unsound. Tool: [`scripts/lean-sorry-count.py`](../../scripts/lean-sorry-count.py)
(strips nested block and line comments, prints `real / raw`, exits 1 on a real
one). Two of the eight also read "decl not found" on a first pass — one a
`timeout 30` recursive grep silently expiring, one a rename the bean itself
records.

They were fixed two ways, and only four honestly:

| | decls | how |
|---|---|---|
| **derived** | `mass_categorical_descent`, `finite_cascade_depth_of_cutoff`, `neutron_proton_splitting`, `skein_mass_from_linking` | splitting a finite sum along a decidable centre predicate; logs of a dissipation cutoff; pinned numerics with the exact-equality conjunct demoted to a tolerance per §7ab; demotion to a named `Prop` with a derived specialisation and a standing counterexample |
| **projected** | `volume_perturbation`, `parity_regime_selection`, `lp_dual_stability`, `confinement_frobenius_reciprocity` | each conclusion conjunct is verbatim one class field; proof term is `ctx.field` or `⟨ctx.f₁, …⟩` |

The second group is this bean's own defect **inverted** — it diagnosed *"the
class carries too little"*, and the fix moved four classes to carrying *exactly
the conclusion* (§3b-cond item 5). But per §3b a **disclosed** projection is
compliant and the undisclosed population is already epic `qou-5p7n`; measured,
`parity_regime_selection` discloses, `volume_perturbation` half-discloses, and
`lp_dual_stability` / `confinement_frobenius_reciprocity` carry none — those two
belong in that epic's bare bucket, not here.

*One* genuinely new thing came out of it: `proof-no-self-assuming-projection`
**could not see `volume_perturbation`**, the cleanest projection of the four,
because the class field spells `QOU.QInteger.qIntBalZ` while the theorem spells
`qIntSym`, a file-local reducible `abbrev` for that head. Closed by
`fileHeadAliases` in `content/pipeline/lean-vacuity-axiom-audit.ts`; whole-corpus
before/after is exactly one new hit and no other line changed.

**`qou-t7mt` — its Option 1 was already applied, in full.**
`frobenius-hopf-substrate.md` now opens *"Let $\mathbf{C}$ be a **monoidal**
category"*, states axiom 4 via `coev` + both snake identities with no `A^\vee`,
and says in axiom 5 that `(ev, coev)` *"exhibits $A$ as its own dual"*. Line 21
carries the bean's own argument (*"Duals are required of $A$ only, not of
$\mathbf{C}$"*). The single surviving `A^\vee` is at line 23 and is the
**disclosure of the change**, not a residue.

**`qou-w1g8` — its prerequisite question is answered by the paper.** The bean
holds `Σ p_b = 𝟙` behind *"does the paper's R-linear phrasing already imply
Preadditive?"*. `def:quantum-universe` item 1 **asserts** *"an $R$-linear braided
monoidal category $\mathbf{C}$ over a commutative ring $R$"* — an axiom, not a
defined-but-unasserted predicate — and `def:rigid-monoidal-category:31` defines
$R$-linear as *"every hom-set is an $R$-module and composition is
$R$-bilinear"*, which is Mathlib `Preadditive` plus an $R$-action
(`CategoryTheory.Linear R C` is *declared* `[Preadditive C]`). So adding the
instance does not change what a quantum universe is — the Lean is weaker than
the paper and the fix is claim-**alignment**. Agent-actionable; off the
owner-gated queue, still open as work.

### ~~CLUSTER 5 — notation. `qou-d7h1`~~ ✅ **RESOLVED 2026-09-05 — already ruled, no decision needed**

**The fifth already-answered item.** The bean says the `SU(3)_C`/`SU(3)_F`
collision "needs an owner convention decision". That decision landed
**2026-09-03** in `afec87d506` (bean `qou-gght`), with a 28-site sweep — **eight
days after** this bean's last update. `notation-collisions.md` now rules: bare
`SU(3)` only for statements true of any `SU(3)`; otherwise `SU(3)_c` (colour) or
`SU(3)_f` (flavour), roman lowercase — *because eightfold-open-problems item 4
asks whether the two are the same, and a shared glyph presupposes an answer*.
That is precisely the reasoning the bean wanted.

**`qou-d7h1`'s medium-term work is unblocked and agent-actionable.**

Compliance measured: 16 canonical `_c`, 19 canonical `_f`, 6 declared-legacy
(explicitly not swept), **45 bare across 22 files** — of which **20 are in
`appendix-standard-model/`** and are the SM gauge triple `SU(3)×SU(2)×U(1)`, i.e.
the ruling's own carve-out.

**One genuinely new, small question surfaced.** `q-deformed-nuclear-models-comparison.md`
uses **Elliott's `SU(3)`** (3 sites, `\cite{elliott1958}`) — the harmonic-oscillator
shell-model symmetry, a **third** group the register does not name. It is
disambiguated today by the adjacent word "Elliott", the same mechanism the
register accepts for `\zeta(s)` vs `\zeta_n`. **Proposed, not applied** (a register
change is a convention claim): one line in `notation-collisions.md` recording it,
so a future sweep does not "correct" those 3 sites into `_c` or `_f`.

### CLUSTER 6 — `qou-aemx`. ✅ **Checked for staleness: it is GENUINELY OPEN, and well framed.**

I flagged this as possibly stale. **It is not** — and that matters, because five
other items were, and the run of them was starting to read as "the queue is
noise". It is not. This one moved *sharper*, not resolved.

**What advanced.** The bean's own later entry withdraws its earlier *"nothing in
the corpus argues for one prefactor"* and finds an exact identity:
`8 = Vol(𝓑₃)/G` — the Borromean rings `L6a4`, this framework's **nucleon** knot,
`Vol = 2·V_oct = 8G`, machine-checked to 30 digits, residual exactly 0. Already
load-bearing in the nucleon row of `fundamental-knots-operator-basis` and in the
binding scale `α = m_e·8G`. The live `.lean` carried the **weaker** reading
(`dim su(3) = gluon octet`, self-described as post-hoc) while the corpus held the
exact one and did not cite it.

**What that does NOT settle**, per the bean's own four points:

1. the identity fixes the `8`, **not the power of `q`** multiplying it — `Vol/G`
   and `q²·Vol/G` are not excluded;
2. **the cross-sector gap, load-bearing and unaddressed**: why should a *nucleon*
   knot's volume set a coefficient in an *electromagnetic* coupling? The bean
   pursued this and reports it "does not close; it sharpens" — the identity is
   **not generic**, holding for only 2 of 9 corpus/standard hyperbolic knots;
3. **genericity unmoved**: κ ∈ [8.474, 9.265] still admits the integer 9 at
   33 ppb, so `8q` is *in range, not forced*;
4. a chronology the bean initially missed: `45·[3]_q` **replaced**
   `q·[9]_q·[10]_q` (which had needed an unidentifiable `1.6`), and the latter was
   then revived with a derived Gram κ. **Production compute uses the superseded
   prefactor.**

**The decision, stated plainly:** does the revival supersede the supersession —
i.e. does `q·[9]_q·[10]_q` with a derived Gram κ reinstate over `45·[3]_q`?

| option | what it means | cost | risk | commits to |
|---|---|---|---|---|
| **a. Reinstate `q·[9]_q·[10]_q`** | production moves to the revived form | producer + witness + the `.lean` docstring | the cross-sector gap is *unexplained*, and κ's range admits 9 — reinstating on an unexplained identity is the numerology shape the anti-fit discipline guards against | an EM coefficient set by a nucleon volume, with no mechanism |
| **b. Keep `45·[3]_q`** | status quo; production keeps the later form | zero | leaves the `.lean` citing the weaker of two available readings | nothing |
| **c. Neither, until the cross-sector gap closes** | record both, wire neither as canonical | small — a scope note on the `.lean` | slower | nothing; keeps the question honest |

**My recommendation, marked as judgement: (c).** The `8` identity is real and
exact, but a *nucleon* volume setting an *electromagnetic* coefficient with no
mechanism, holding for only 2 of 9 knots, and against a κ range that admits the
integer 9 — that is a coincidence with a good number, not a derivation. Under the
standing NO-FITTING directive, "accuracy is not evidence of correctness here".

**Default if you say nothing:** (b), the status quo — production keeps
`45·[3]_q` and nothing moves.

### CLUSTER 7 — one-off content/model calls. ⚠️ **RE-TRIAGED 2026-09-05: 6 of 8 are NOT owner decisions**

Two closed as already-answered, four reclassified off the queue as ordinary
agent work, two genuinely remain. **The queue was inflated by misclassification
as well as by staleness** — that is a second inflation mechanism this triage had
not separated, and it is the larger one here.

| bean | verdict 2026-09-05 |
|---|---|
| `qou-8na1` | ✅ **CLOSED — owner ruled today.** `1b26c6d28d` (*"O2 (owner ruling): say WHICH program, and stop calling `1/[k]_q!` an LP dual"*) put the consequence into the block: *"by strong duality $y_0^\ast = 0$. Any quantity recovered by dividing by $y_0^\ast$ is undefined"* (line 19) and *"…it is not $y_0^\ast$, which is $0$"* (line 36). |
| `qou-hey2` | ✅ **CLOSED — superseded** by `qou-8bxv` / [`2026-09-05-two-skein-normalisations-are-live.md`](../audits/2026-09-05-two-skein-normalisations-are-live.md), which proves the two skein relations are not rescalings. This bean's *argument* is retracted (it evaluated an invariant-level relation on operator eigenvalues — arity conflation); its conclusion survives, and the one claim false under **either** convention — `feynman-eigenbasis.md:29`, *"is simply the characteristic equation of the braiding evaluated under the categorical trace"* — is fixed. Measured **1 of 20** files carried it; the other 19 are correct and must not be swept. |
| `qou-r4ya` | ↩︎ **Not a ruling.** It proposes running the theta-limit machinery and already carries its own scope correction. Open research, in scope for all under the 2026-07-11 reversal. |
| `qou-48is` | ↩︎ **Not a ruling.** It establishes a *gap* (the orbit identity does not license the cross-species ordering; the stated reason is a cost property). Same subject as **Cluster 1** — merge it there. |
| `dgpc` | ↩︎ **Not a ruling.** A Tier-C drain queue with per-family counts and recorded progress. No decision in it. |
| `qou-imkb` | ↩︎ **Not a ruling — a live defect.** Re-verified: `probe_sdp_canonical_paper_formula.py` and its witness are **0 files on disk** and **0 commits** in this clone, and the raising site is still live at `paper_six_term_isotope_sweep.py:185`. The error message instructs a user to run something that has never existed. |
| `gm4q` | 🔴 **GENUINELY OPEN** — and it already ships a full options doc with a recommendation ([`2026-09-04-binding-law-options-decision-frame.md`](../audits/2026-09-04-binding-law-options-decision-frame.md), probe 10/10). The ask is *"adopt Option B, the additive law, or say why not"*. |
| `qou-c66b` | 🔴 **GENUINELY OPEN** — editing a conjecture block's stated obstacle. The measurement is decisive (in `Q_β/m_e = |q² − 2q − 1|·(q+1)/(2q³)` the modulus wraps **one** factor, so the projection is not total), but whether the block's *"no mass observable can detect Im(q)"* is thereby wrong turns on whether a decay Q-value counts as one — a framing call. |

Original pass-3 text, kept for the record:



`gm4q` (**already has a full options doc with a recommendation**:
`docs/audits/2026-09-04-binding-law-options-decision-frame.md`, probe 10/10 — the
ask is "adopt Option B, the additive law, or say why not") · `qou-48is` (ordering:
the **rename** is free and honest, the **fix** moves witnesses) · `qou-8na1`
(content consequence of `y₀* = 0`) · `qou-c66b` (edit the conjecture block) ·
`qou-hey2` (normalising a convention moves published numbers; 0.136 % inside the
half-life prefactor) · `qou-imkb` (what "Model B" means) · `qou-r4ya`
(Friedrichs-vs-Krein framing) · `dgpc` (a `status: "verified"` downgrade)

---

## 🛑 The meta-finding: I made the same error the beans make

Three times this triage I escalated on a bean's own words and the check deflated
it — `qou-zzwm` (already fixed), `qou-zdz5` (conditional, condition unmet), and now
`qou-1jw9` (deprecated and disclosed). That is the **same root cause** as the 22
stale sentences: a bean states urgency at the top, the situation moves, and
nothing updates the claim.

**The reusable rule: a bean is a lead, never a finding.** It earns the same
treatment AGENTS.md already prescribes for a source file's `## Status` note —
the corpus is the source of truth, and the corpus here means the live code, the
live witness, and the block's `computation:` link, not its prose.

I applied that rule to my own claims all session and kept suspending it for
someone else's bean.

## What pass 3 changes

- **19 beans → 7 clusters.** Cluster 1 alone retires four asks with one ruling.
- **Two items should leave the veto queue entirely**: `qou-1jw9` (a fourth
  calibration — a discipline question, not a preference) and Cluster 1's core
  (a measured result exists; what is missing is a ruling on the *inconsistency*).
- **`gm4q` is decision-ready** — options, pros/cons and a recommendation already
  written up in its own audit doc.

## Status

- **Pass 1** — 33 pending split from 18 historical-only.
- **Pass 2** — 4 more false positives; A/B/C = 10 / 19 / 6.
- **Pass 4 (2026-09-05)** — Cluster 4 RESOLVED: all three beans deflate on
  checking. `qou-octr`'s scope is discharged (its eight sorries no longer
  exist; the naive grep says 21 and every one is prose), `qou-t7mt`'s Option 1
  was already applied in full, and `qou-w1g8`'s prerequisite question is
  answered by `def:quantum-universe` axiom 1. That takes the already-answered
  count from five to **eight**, and Clusters 5, 4 and 6 are now closed —
  leaving **1, 3 and 7** genuinely open.
- **Pass 3** — the 19 collapse to 7 clusters; `t7qv` already carries Cluster 1's
  measurement; `qou-1jw9` escalated out of the queue.
- **Remaining** — nothing further is triageable without your rulings. The queue is
  drained to decisions.

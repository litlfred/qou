# PR #6233 (orphaned FormB probe) adjudication + `qou-cds1` state of play

**Date:** 2026-09-14 · **Beans:** `qou-cds1` (S1), `qou-pdix` (the S1 blocker)
· **Branch:** `claude/cds1-formb-adjudication-2026-09-13` · **PR:** #7276
· **Scope: (a) throughout.** No `c_k` value is proposed, no route is wired, no
bean is closed. Two corpus corrections are recorded in §6, one of them to a
claim of my own made earlier in this same session.

## Scope

Two linked questions.

1. **PR #6233** preserves two files found *untracked* in a working tree on
   2026-08-30, provenance recorded as unknown:
   `computations/qbeta/qbeta_block_resolved_formB_probe.py` and its witness.
   Neither is on `main`. The preserving author claimed **no** verification
   beyond `ast.parse`, and asked for exactly the review below.

2. **Bean `qou-cds1`** — re-derive the Q_β `c_k` ladder under convention D.
   What is done, what is blocking, and does the #6233 probe advance it.

---

## 1. Verdict on #6233 — CLOSE UNMERGED

**The probe is sound. It should still not land.** Those are not in tension, and
keeping them apart is the whole adjudication: every technical check passes, and
the reason to close is that the result is *already in the corpus* and the
decision not to land the file *was already taken* — on 2026-08-29, one day
before the PR was opened.

This is the PR's own **outcome 1** ("a sibling's in-flight work that leaked into
this container … this PR closes unmerged"), with outcome 3's disposition for the
branch (kept as the record, per the never-delete-branches rule).

---

## 2. Provenance — RESOLVED, contrary to the PR title

The PR says *"provenance UNKNOWN"* and *"I do **not** know who wrote it or when
it entered this container."* It is recoverable, and the answer was inside the
witness the PR was carrying.

The witness names its own commit:

```
"commitSha": "db4beedfa0c951d25eef23bbab53da5c1f0465b9"
"computedAt": "2026-08-19T20:36:47.287459+00:00"
```

That object resolves in this clone:

```
$ git log --format="%H%n%ci%n%s" -1 db4beedfa0c951d25eef23bbab53da5c1f0465b9
db4beedfa0c951d25eef23bbab53da5c1f0465b9
2026-08-19 20:30:31 +0000
branch: qou-cds1 — fold the Wenzl two-row cap into the D decay correction

$ git branch -r --contains db4beedfa0c951d25eef23bbab53da5c1f0465b9
  origin/claude/qbeta-f-coordinate-2026-08-19
```

So the witness was computed **6 minutes after** a commit whose subject is the
probe's exact subject, on a single containing branch — and that branch is the
one the PR body itself guessed (*"on-topic for a sibling's branch
(`origin/claude/qbeta-f-coordinate-2026-08-19`)"*). The guess was right and was
checkable.

**Why the PR's own search missed it.** It ran
`git log --all -- computations/qbeta/qbeta_block_resolved_formB_probe.py`, which
is empty — correctly, since the file was never committed anywhere:

```
$ git log --all --oneline --diff-filter=A -- "computations/qbeta/*formB*" \
      "computations/qbeta/*block_resolved*" "computations/qbeta/*block-resolved*"
a9ce25bbb0 preserve: an ORPHANED qou-cds1 probe found untracked ...
```

(the one hit is #6233's own commit). A path-keyed history search cannot find an
uncommitted file; the witness's `commitSha` field can. Confirmed from the other
side: `git ls-tree -r origin/claude/qbeta-f-coordinate-2026-08-19` carries no
`formB` / `block-resolved` path either.

**And the corpus says so in words.** Bean `qou-cds1`, entry dated
**2026-08-29** (lines 2425–2510 of
`.beans/qou-cds1--s1-science-re-derive-the-qbeta-ck-ladder-under-d-n.md`):

> **The probe was never committed.** It lived on
> `claude/qbeta-f-coordinate-2026-08-19` as an uncommitted file and is not being
> landed: the route is settled, and a witness for a pruned class is maintenance
> surface with no consumer. The argument above is ten lines to reproduce from
> this text.
>
> **That agent is off this bean.** No claim held; the takeover stands.

**The non-landing was a decision, not an oversight, and it predates the PR by a
day.** #6233 was opened 2026-08-30T14:07Z.

This is corpus-grep **path 6** doing precisely what AGENTS.md says it does: the
conclusion sits in a bean and nowhere else reachable by paths 1–5.

---

## 3. The probe verifies clean — every check the PR asked for

### 3.1 It runs, and all three assertions reproduce

```
$ PYTHONPATH=computations:tools/qou-substrate/python:tools/pyhecke/python \
    python3 -u computations/qbeta/qbeta_block_resolved_formB_probe.py
...
  SYMBOLIC — the identity this probe rests on
    sum_l  y_l . chi_l(sigma)  ==  z_D   exactly : True
    sum_l  f^l . y_l           ==  1     exactly : True
✓ Witness: qbeta-block-resolved-formB.witness.json  (3 assertions, all passed)
=== EXIT 0 ===
```

`markov_parameter_is_the_block_mean_symbolically`,
`sign_block_weight_vanishes_under_D` and `block_resolved_differs_from_mean_form`
all reproduce. Log: `/tmp/.../formB-rerun.log`.

### 3.2 The numbers reproduce byte-identically, across different libraries

Fresh witness vs the one committed in #6233, comparing every field with the
ephemeral/provenance set masked:

```
non-ephemeral fields compared : 67
DIFFERING                     : 4
```

and **all four differences are fields ABSENT in the committed witness and
present in the fresh one** — `/q0Anchor`, `/q0Value`, `/invocation/argv[0]`,
`/invocation/reproduce`. Not one recorded numeric value moved, to the last of
60 digits.

That is a stronger result than it looks, because the environments differ:

| | committed witness | this re-run |
|---|---|---|
| mpmath | 1.4.1 | **1.3.0** |
| sympy | 1.12 | **1.14.0** |
| numpy / scipy | 2.4.6 / 1.17.1 | **absent** |
| python | 3.11.15 | 3.11.15 |

So the payload is reproducible *and* insensitive to the two libraries it
actually uses. (`numpy`/`scipy` are absent here and are not imported by the
probe or its cone — their absence changes nothing, which the identical output
confirms rather than assumes.)

### 3.3 Convention — D, verified BY VALUE not by shape

AGENTS.md records that every convention detector is blind to some spelling, so
this was checked by evaluating the bindings rather than matching their source:

```
q0 (proton pin)     = 1.109978582751380807591669
z_C = sqrt(q)/(q+1) = 0.49932033418369445241
z_D = q^3/(q^2+1)   = 0.6126880371464652516

INDEPENDENT symbolic re-derivation of the probe's claim:
  sum_l y_l chi_l = q**3/(q**2 + 1)
  equals q^3/(q^2+1) (z_D)?   True
  equals sqrt(q)/(q+1) (z_C)? False
  sum_l f^l y_l = 1  (normalised? True)

D helper: z = 0.6126880371464652516   |z - z_D| = 0.0          -> convention D
C helper: z = 0.49932033418369445241  |z - z_C| = 4.52784e-72  -> convention C
```

The primary object is **canonical convention D, exactly**. Convention C appears
only through `y_lambda_at_q0_mpmath_convention_C_HISTORICAL` — a
self-announcing, explicitly-named historical function used as the second arm of
a labelled two-arm comparison, which the convention-C audit classes as
*deliberate*, not as a leak. **No convention defect.**

I re-derived the D weight set independently (`(q⁴+1)/(q²+1)²`, `q²/(q²+1)²`, `0`
against characters `q`, `h`, `−1/q`) rather than trusting the probe's own
sympy: `Σ y_λ χ_λ = q³/(q²+1)` and `Σ f^λ y_λ = 1`, both exact over ℚ(q).

### 3.4 q₀ pin — proton, no layer straddle

The probe takes `q_at()` from `qou_substrate.constants` **directly**, i.e. the
package layer, which is the compliant route under the 2026-08-07 owner
directive (experimental/proton default for all compute). It is not routed
through `q_parameter`, so it cannot pick up an `ideal_muon` classification — and
it could not have one anyway, the stem being absent from
`computations/q0_anchor_manifest.json` (19 `ideal_muon` / 914 `physical_proton`
/ 15 `ambiguous` entries, none matching).

**No straddle.** Both weight helpers are evaluated at the *same* `q0`, and the
only other inputs are CODATA scalars. This is the shape the μ₃ Fréchet incident
warns about and the probe does not have it.

### 3.5 Precision — clean

| check | result |
|---|---|
| `set_compute_dps()` at module level | ✓ line 94 |
| `statistics` / `math` aggregation over floats | **none** |
| `mpf(<float literal>)` | **none** |
| `float()` in arithmetic | **none** |
| `float()` total | 4, **all display-only inside f-strings** (lines 225, 258, 261, 263) |
| CODATA inputs float64? | **no** — `M_E_MEV` and `Q_BETA_MEV` are already `mpf` |
| witness serialization | all values via `_precision.fmt` |

The four `float()` calls are the form AGENTS.md permits ("only inside an
f-string for display"); each converts an already-`mpf` result *after* the
arithmetic, never before. The rule's stated preference for `mp.nstr` would be a
style improvement, not a defect.

`scripts/precision-gates.sh --changed` exits 1 — and **not because of this
probe**:

```
$ grep -n "block-resolved\|block_resolved\|formB" <gates output>
(probe/witness appears NOWHERE in the precision-gates output)
```

Every RED belongs to the 11 contended audit witnesses that the gate scripts
themselves regenerate, on a tree the gate reports as *"518 behind
origin/main"* — the exact false-positive class the script's own footer
describes (bean `qou-v0t8`), which is why it prints
`DO NOT COMMIT THESE. Revert them: git checkout -- computations/`. Reverted;
tree clean. **The probe contributes zero precision-gate red.**

### 3.6 `_path_bridge` bootstrap — correct order

The probe inserts both parent directories on `sys.path` *before*
`import _path_bridge`, which is the documented USAGE. It does **not** carry the
`qou-0e1t` defect (an `import _path_bridge` preceding the bootstrap, invisible
to a `PYTHONPATH`-equipped runner).

---

## 4. Why it should nonetheless close

### 4.1 Its results are already in the corpus, to the digit

The 2026-08-29 `qou-cds1` entry contains the probe's entire content: the Form B
integrand `g(ζ) := ln(1 + ζh)/ζ`, the weights `p_λ := f^λ y_λ`, the Jensen
framing, the exact `Σ y_λ χ_λ = z_D` identity, the convex-hull class argument,
and the numbers. Byte-for-byte against the witness and against my re-run:

| quantity | bean (2026-08-29) | witness / re-run |
|---|---|---|
| D hull | `[0.786985113907, 0.865697506066]` | identical |
| C hull | `[0.786985113907, 0.969606940981]` | identical |
| D rel. (mean / full / logonly) | `+5.2549e-02  +5.5708e-02  +1.4436e-02` | identical |
| C rel. (mean / full / logonly) | `+6.3990e-02  +6.7785e-02  +8.2005e-03` | identical |

The bean also scopes the finding more carefully than the probe's own stdout
does — see §6.2.

### 4.2 Its headline justification has gone stale

The probe's docstring and the PR both rest on one claim: that it does *"verbatim,
the step bean `qou-cds1` names as **NOT folded in yet**"*. That was true when
written. It is not true now:

```
$ git log --format="%h %ci %s" --diff-filter=A -- \
    content/quantum-observable-universe/lean/QOU/QBeta/PhaseBlockResolution.lean
87bf883793 2026-09-07 21:39:42 +0300 ...
```

`QOU/QBeta/PhaseBlockResolution.lean` (132 lines) plus
`qbeta_phase_block_resolution_probe.py` (18/18) landed **2026-09-07** — 19 days
after the witness was computed, 8 after the PR opened — and fold the cap in at
the block level, on this very bean. Its `chi_two_one_delta_eq_zero` proves
`χ^{(2,1)}(Δ) = 0` over a generic `[CommRing R]`, hence that the eigenphase is
blind to the 2-dimensional block **in every convention**, no Markov parameter
entering.

The route the probe travels was closed separately the day the PR opened:
[`2026-08-30-cds1-two-row-cap-admissible-set-exhausted.md`](2026-08-30-cds1-two-row-cap-admissible-set-exhausted.md)
shows the cap's admissible set is exactly `{z = q, z_D}` (proved complete,
`ConventionDAdmissibleRoots.lean`) with both members excluded — `z = q`
structurally, since `α = (z−1)h/2 < 0` forces `z < 1` while `q > 1`.

### 4.3 Defects it would carry in if landed

None of these are reasons to reject the *mathematics*; they are reasons the
artifact is not landable as-is.

1. **The witness is self-stale on arrival.** Its recorded `scriptHash` does not
   match the probe committed beside it, by the repo's own
   `witness.file_content_hash` (SHA-256 of the UTF-8 text, 12-hex prefix):

   ```
   witness scriptHash              = 4013966f9db8
   committed probe, text mode      = 2c5858506560
   committed probe, binary         = 2c5858506560   (no CR; 16003 chars / 16025 bytes)
   ```

   So the committed file is **not** the file that produced the committed
   witness, and `witness_dependency_drift.py` — which keys self-staleness on
   `scriptHash` alone — would flag it from the moment it merged and could never
   go green without a re-run. I **cannot** classify the intervening edit:
   the producing version was never committed anywhere, so there is nothing to
   `ast.unparse`-normalise it against. What I *can* say is that whatever
   changed was numerically inert, since the committed file reproduces all 67
   recorded values exactly (§3.2).

2. **Missing the anchor stamp the audits read.** The committed witness has no
   top-level `q0Anchor` / `q0Value`; it carries only a hand-written payload
   field `data.q0_anchor`. `q0_anchor_consistency_audit.py` and the muon-pin
   gates read the top-level keys, so as committed the witness is
   unclassifiable to them. **This is not a builder-age excuse** — `q0Anchor`
   stamping was added 2026-07-18 (`b503ff4256`) and `git show
   db4beedfa0…:tools/qou-substrate/python/qou_substrate/witness.py` has 22
   occurrences of it, so the mechanism existed a month before the witness was
   written and simply did not fire. A re-run supplies both fields
   automatically, as §3.2 shows.

3. **The headline result is not machine-readable.** The probe's actual
   contribution is the hull verdict — *is the target reachable at all?* — and
   that boolean is printed to stdout and **not** recorded as an assertion. The
   three assertions that *are* recorded are structural
   (`…is_the_block_mean_symbolically`, `…vanishes_under_D`,
   `…differs_from_mean_form`), and the third is close to unfalsifiable: it
   asserts that two separately-computed 60-digit numbers are unequal. The hull
   bounds reach the witness as `data`, but nothing adjudicates them.

4. **The sweep line understates its own result** — see §6.2.

---

## 5. `qou-cds1` — state of play

**Status `in-progress`.** AGENTS.md's claim that it is blocked on the phase
`qou-pdix` is **verified**, from both ends.

### 5.1 The base is settled; the blocker is the phase

Bean `qou-cds1`, latest substantive entry (line 8065, 2026-09-08):

> **BASE SETTLED by owner ruling (qou-99qc): ε := tr_M at z_D.** The D-frame
> ladder is to be re-derived on the z_D base (0.4447004 MeV, −43.157 %).
> Structural c₂ = −1 remains the self-consistency check; **the blocker is still
> the N=1 phase (qou-pdix)**. No z-swap of the C ladder
> (`decayLadder_zC_threeRow_ne_zero`).

And from `qou-pdix`'s own body: *"Parent: qou-cds1 (tranche S1). **This is the
S1 blocker.**"*

Bean statuses as measured: `qou-cds1` in-progress, `qou-pdix` in-progress,
`qou-99qc` todo, `qou-iagg` todo, `qou-06wh` in-progress, `qou-ughq` todo,
`qou-54g5` todo.

*(Aside, not this audit's subject: the `0.4447004 MeV / −43.157 %` figure in
that entry is the 2026-09-08 order-zero-`E₀` cell and has since been superseded
twice — tower-summed `E₀`, then the `nuc11_interleaved` element. AGENTS.md
carries the correction; quote the dashboard witness, not either text.)*

### 5.2 What `qou-pdix` needs

**A derivation of the eigenphase α.** The `c_k` *tail* is settled — `tail_common`
proves `z` reaches the ladder only through the N=1 phase, so `c₂`…`c₅` are
phase-blind. There is nothing to port from convention C, because the C carrier
is **proved vacuous**: `QOU.Interactions.TransferMatrixEigenphase` is documented
as axiomatising a spectrum on `V_{(2,1)}` and its two fields encode none of it
(`−2 ≤ 2cos ≤ 2`, `cos x = cos(−x)` — true of every real), formalised as
`QOU.QBeta.EigenphaseCarrier.carrier_is_trivial : … ↔ True` (sorry-free).

**Routes closed — do not re-run:**

| # | route | status |
|---|---|---|
| 1 | substitute `z_D` into `α = (z−1)h/2` | pruned — 23 % against a ±1.1e-5 rad window |
| 2 | exact Form-A/Form-B bridge instead of its `O(h)` truncation | refuted, scope-(a) — 530 % (C) / 456 % (D) vs 0.04 % / 23 % |
| 3 | `M = λ·ρ(braid word)` in the seminormal rep | **excluded, scope-(b)** — every character lies in `ℤ[q,q⁻¹]` while `cos` of a non-constant algebraic function is not; `det ρ(σᵢ^±) = −1` blocks the scalar rescue |
| 4 | KZ / Kohno–Drinfeld holonomy | **closed** — real generator spectrum gives `cosh a ≥ 1`, and the required factor is `0.998399 < 1` (`HolonomySpectrumSignObstruction.lean`, 6 theorems, sorry-free) |
| 5 | two-row cap in the `α = (z−1)h/2` form | **closed** — admissible set proved to be exactly `{q, z_D}`; `z = q` excluded structurally by sign |

**Survivors:** a non-scalar (q-dependent, non-rational) normalisation, and an
`M_β` outside the braid image. Both are named in route 3's own scope note.

**The gap has been reshaped, and this is the part most likely to be missed.**
`qou-pdix`'s 2026-09-04 entry establishes that ellipticity is *free* at `|q| = 1`
(where `ln q = iθ` exactly, so `det A = +θ² > 0`) and *impossible* at real `q`.
So the previously-recorded frontier — "find a generator elliptic at real `q`" —
asks for what the proved argument forbids. What is actually open is **the
bridge**: a fibre-level object at `|q| = 1` whose archimedean evaluation lands at
`|q₀| = 1.10998`, an **11.0 % gap in modulus**. That is the fibre-vs-observable
structure AGENTS.md's Im(q) banner names.

Its 2026-09-12 route triage (explicitly "not a new result"): **A** Habiro
ring / roots of unity (best structural fit, risks circularity — the Habiro
construction is part of what `qou-cds1` waits on); **B** Faddeev quantum
dilogarithm / modular double (cheapest formalize-first step; Lean assets already
exist — `FaddeevRatioPeriodic.lean`, `FaddeevSolutionSet.lean`,
`FaddeevPhiBRealIntegral.lean`) — *that bean's own recorded recommendation,
marked as judgement*; **C** Stokes / resurgence; **D** two evaluation points —
**flagged as the trap**, a second anchor being a fourth calibration under
CAL-1/2/3.

Two traps `qou-pdix` restates so they are not re-run as results: `θ =
arccos(target)` reproduces any sub-unit target *tautologically*; and
`qou-c66b`'s `∂Im(Q_β)/∂Im(q) ≈ 3.418` rests on a complex extension of `Q_β`
that is the recording agent's, not the corpus's.

**Downstream:** `qou-iagg` (the second dashboard re-score) waits on `qou-cds1`.
The dashboard's Q_β / m_n / Δ_pn rows are base-only precisely because no ladder
exists on an admissible base.

### 5.3 Does #6233 advance `qou-cds1`? **No.**

Three independent reasons, any one sufficient:

1. **Its content is already recorded** in the bean, to the digit (§4.1), with
   the disposition "not being landed" already taken (§2).
2. **It attacks a class the bean already prunes.** The hull argument *is* the
   bean's own 2026-08-29 exclusion.
3. **It cannot reach the blocker, by construction.** The blocker is the
   eigenphase α, and the probe's entire premise is to *route around* the
   phase — "at the Wedderburn decomposition instead of through the phase
   alpha". The class it routes to is the one the hull excludes. So a *sound*
   result here removes a route; it supplies no α.

There is a genuine cross-check worth keeping, and it is a consistency note
rather than progress. Restating the hull as a correction factor `F = Q/Q_A`:

```
F_required            = 0.99832524167325    (< 1)
F at hull lower edge  = 1.004261219055      (>= 1)
F at hull upper edge  = 1.1047050540249
```

The required factor is **below 1** and the whole block-resolved class sits
**above 1** — structurally the same obstruction as
`HolonomySpectrumSignObstruction.lean`'s `cosh a ≥ 1 > 0.998399`, reached
through convexity instead of through a real spectrum. Two different arguments
landing on "the correction has to be sub-unit and this class is not" is a useful
corroboration of both.

---

## 6. Corrections

### 6.1 A misattributed block in bean `qou-cds1`

Its 2026-08-29 entry says:

> The lower edge is identical in the two frames because it is set by the same
> block, `(2,1)`, which both retain.

**The lower edge is set by `(3,)`, the symmetric block — not `(2,1)`.** Measured,
per-block `E₀·g(ζ_λ)` in MeV at the proton pin:

```
convention D   live blocks ['(3,)', '(2, 1)']
          (3,)  0.78698511390658
        (2, 1)  0.86569750606623
    -> lower edge set by (3,), upper edge by (2, 1)

convention C   live blocks ['(3,)', '(2, 1)', '(1, 1, 1)']
          (3,)  0.78698511390658
        (2, 1)  0.86569750606623
     (1, 1, 1)  0.96960694098131
    -> lower edge set by (3,), upper edge by (1, 1, 1)
```

**The conclusion is unaffected** — the two lower edges *are* identical, and for
the reason given, that the edge-setting block is retained in both frames. Only
the block's name is wrong. Worth fixing because the surrounding argument is
about which blocks the D cap annihilates, and `(2,1)` versus `(3,)` is exactly
the distinction in play: the cap removes `(1,1,1)`, which is the block setting
C's *upper* edge, which is why the two hulls differ at the top and agree at the
bottom.

### 6.2 A claim of my own, made earlier in this session, that was wrong

On first reading the probe's sweep line —

```
---- q-sweep, +-2% around q0 (41 points, D weights) ----
  points with Q_codata inside the hull : 18/41
```

— I recorded that "the exclusion is anchor-local, not structural in q," and
that the probe's stdout over-claimed by stating the exclusion without a
q-scope caveat. **The finer scan says the opposite, and the over-claim runs the
other way.**

```
band +/- 2.0000%   inside hull: 18/41
band +/- 0.2000%   inside hull:  0/41
band +/- 0.0100%   inside hull:  0/41

THRESHOLD: smallest |dq/q| at which the target enters the hull
  q above q0: flips at |dq/q| = 0.0023658152 = 0.2366%
  q below q0: still excluded at 5% — no flip in range
```

All 18 "inside" points sit far out in the band. The exclusion is **one-sided**
(nothing below `q₀` within ±5 %) and holds until `q` is raised by **0.2366 %** —
against a μ–p substrate tension of 11.5 ppb (`1.15e-8` relative), i.e. it
survives a displacement roughly **2×10⁵ times** any live anchor ambiguity.

So the exclusion is robust at the anchor, and **the probe's `18/41` line
understates its own result**: printed without the band structure it reads as
"~44 % of the time this is not excluded", when the correct reading is "excluded
throughout any physically meaningful neighbourhood of `q₀`". A reader taking
that line at face value would think the prune fragile. That is the reporting
defect (§4.3 item 4) — the opposite of the one I first wrote down.

The bean's own scoping is the accurate one and needs no change: scope-(b) for
the convexity invariant, scope-(a) for the physics "since the hull is evaluated
numerically at one anchor and the per-block `1/ζ` normalisation is an
assumption the corpus does not derive." The second clause — an *underived
normalisation*, not anchor fragility — is the load-bearing caveat, and it
stands.

---

## 7. Corpus-grep checklist (AGENTS.md §Before declaring "open")

Run before any statement above that an item is open or that the probe is
novel.

| path | surface | result |
|---|---|---|
| **0** | `corpus_search` (MCP) | 🛑 **NOT RUN — UNAVAILABLE this session.** The `paper-assistant` MCP server failed to connect (`ENOENT … start-folio-assistant.sh`), as did `lean-lsp`, `openalex-paper-search` and `paper-search-mcp`. This is a connection failure, not a missing capability. Paths 1–6 are greps and share the blind spot path 0 exists to cover — prior work phrased in different words. **Every "novel"/"open" statement here is therefore weaker than it would be with path 0, and should be re-checked when the server is reachable.** |
| 1 | `docs/audits/` | **HITS.** `2026-09-04-cds1-ladder-phase-has-no-derivation.md` (on `origin/main`), `2026-08-30-cds1-two-row-cap-admissible-set-exhausted.md`, `2026-05-11-q-beta-form-A-vs-form-B-canonical-choice.md`, `2026-08-24-h4-form-ab-frozen-record.md` |
| 2 | `content/` | **HITS.** `QOU/QBeta/PhaseBlockResolution.lean` (decisive — §4.2), `QOU/BraidKnot/A3OperatorCombinerMagnitude.lean`, `mass-theory/lp-dual-scaling-conjecture.{md,ts}` |
| 3 | `computations/` | **HITS.** `qbeta_phase_block_resolution_probe.py` (18/18), `qbeta_alpha_commutator_floor_probe.py` (22/22), `qbeta_d_frame_tl_quotient_phase_probe.py`, `qbeta_class_b_nonsigndefinite_bond_probe.py`, `qbeta_ladder_alpha_provenance_probe.py` (5/5) |
| 4 | `docs/coordination/` | hits, none on point: `1ppb.md`, `option-e.md`, `convention-slip-registry.json` |
| 5 | `library/` — INDEX.md, `summary.json`, `sections/`, **`ocr/`** | **HITS, none used above.** `arxiv-math-9806163v1` *Weights of Markov traces on Hecke algebras*, `arxiv-0911.4494v2` *The geometry of Markov traces*, `arxiv-1403.4021v2` (BMW), `arxiv-2507.19896v1` (Jucys–Murphy). All four tiers walked, `ocr/` included (empty for this topic). These are the *weights* literature — relevant to `qou-pdix`'s surviving non-scalar-normalisation route, cited here as available rather than used. |
| 6 | `.beans/` | **DECISIVE.** `qou-cds1` lines 2425–2510 carry the probe's whole result and its non-landing decision (§2, §4.1). Also `qou-pdix`, `qou-ughq` (todo — `H_2` block-resolve fallback), `qou-06wh`, `qou-54g5`, `qou-99qc`, `qou-iagg`. |

**Nothing is declared open in this document that was not already open in the
corpus.** The two open items named — `qou-cds1` and its blocker `qou-pdix` — are
open per their own `in-progress` beans, and no bean is closed or re-statused
here. Per AGENTS.md §13a, `qou-pdix`'s subject is an open derivation and must
not be closed while it stands.

---

## 8. Recommendation

**Judgement, not a finding.** Close **#6233 unmerged**, leaving the branch as
the record.

The mathematics is sound and reproduces exactly; that is worth saying in the
closing note, because "closed" should not read as "junk" — the preserving
author did the right thing by labelling it rather than folding it into
unrelated work, and the probe's substance was already absorbed into
`qou-cds1` before the PR existed. What would be gained by landing it is a
witness for a pruned class with no consumer, carrying a `scriptHash` that can
never go green and an anchor stamp the audits cannot read. What would be lost
by closing it is nothing: the bean says the argument is *"ten lines to reproduce
from this text"*, and this document adds the re-run, the provenance and the
robustness threshold to that record.

**Not recommended, and not done here:** re-running the probe and committing the
refreshed witness to make it landable. That would reverse a decision the arc's
owning agent recorded deliberately, on an arc this session does not hold.

The two probe files were staged into this worktree only to be executed, and
have been left untracked and uncommitted.

## Scope

Scope-(a) throughout. No `c_k` value is proposed. No route is wired. No
truncation order, branch or element is selected. The one scope-(b) statement
relied on is the convex-hull class exclusion, whose invariant (convexity) is
cited and which is the bean's, not this document's. The two corrections in §6
are factual and derived from the corpus plus the measurements shown; neither
changes a published number.

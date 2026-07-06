# P0.1 wall-violation sweep — 2026-05-02

**Pair**: [`2026-05-01-math-framework-deep-audit.md`](2026-05-01-math-framework-deep-audit.md)
§4 (strict-archimedean-wall) + [`2026-05-01-math-framework-workplan.md`](2026-05-01-math-framework-workplan.md)
P0.1.

**Branch**: `claude/tier-4-math-audit-EkI7a`

## Sweep methodology

[`computations/sweeps/wall_violations_sweep.py`](../../computations/sweeps/wall_violations_sweep.py)
greps every `*-proof.md` under
`content/quantum-observable-universe/` for Archimedean / hyperbolic-
volume markers (Mostow, Gromov, Thurston, hyperbolic Vol(K), SnapPy,
Kashaev, Murakami–Murakami, volume conjecture).  Each match is
heuristically triaged as one of:

- **`proof-input`** (likely violation): marker appears with
  derivation-step language ("by Mostow rigidity", "gives Vol(K) =").
- **`tau-image`** (allowed): marker appears under explicit τ-image /
  Archimedean realization framing.
- **`context-only`** (allowed): marker appears in motivational /
  introductory prose without being a proof step.

Triage is conservative; the triage column is the input to manual
review, not a verdict.

Output: [`computations/sweeps/wall-violations-sweep.witness.json`](../../computations/sweeps/wall-violations-sweep.witness.json).

## Sweep result (149 proof files)

Initial sweep (before P0.2 recast):

| Triage label | Count |
|--------------|------:|
| `proof-input` (likely violation) | 5 |
| `tau-image` (allowed) | 2 |
| `context-only` (allowed) | 17 |
| **Files with at least one hit** | 6 / 149 |

After P0.2 recast (the algebraic version of the mass formula
[`prop:topological-mass-formula-algebraic`](../../content/quantum-observable-universe/braids-and-knots/topological-mass-formula-algebraic.md)
landed and the two real-violation proofs now cite it):

| Triage label | Count |
|--------------|------:|
| `proof-input` (false-positive only — see triage #1) | 3 |
| `tau-image` (allowed) | 2 |
| `context-only` (allowed) | 25 |
| **Files with at least one hit** | 6 / 149 |

The 3 remaining `proof-input` hits all land in
[`atom-knot-mass-derivation-proof.md`](../../content/quantum-observable-universe/braids-and-knots/atom-knot-mass-derivation-proof.md)
and are false positives (already correctly framed as
"Post-Archimedean naming, borrowed, not part of derivation"); see
triage #1 below for the explanation.

After P0.1 heuristic refinement (2026-05-02): the sweep script now
recognises the `### Post-Archimedean naming` / "borrowed, not part
of derivation" disclaimers via section-header context and inline
phrase matching, reclassifying the 3 false-positive hits as
`tau-image` (allowed):

| Triage label | Count |
|--------------|------:|
| `proof-input` (likely violation) | **0** |
| `tau-image` (allowed, includes the 3 reclassified hits) | 16 |
| `context-only` (allowed) | 14 |
| **Files with at least one hit** | 6 / 149 |

🟢 **All 149 proof blocks now triage clean.** No proof-input hits;
the 16 + 14 allowed hits are correctly recognised as τ-side
naming or context-only references.

## Manual triage of `proof-input` hits

### 1. `atom-knot-mass-derivation-proof.md` (3 hits) — 🟢 false positive

Context:

```
### Post-Archimedean naming (borrowed, not part of derivation)

If $K = \widehat{T_w}$ is hyperbolic then by the volume conjecture
\cite{kashaev1997,murakami-murakami2001} the asymptotic ...
```

The proof explicitly puts the volume-conjecture / Mostow / Gromov
references under a **"Post-Archimedean naming (borrowed, not part
of derivation)"** subheading. The surrounding prose closes with:

> This is **borrowed, conventional, and used only as naming**. The
> QOU mass identity above does not depend on the volume conjecture
> in any way: it is a finite-sum categorical statement, terminated
> by the Archimedean functor.

This is the **canonical correct framing** per audit §4 — the
Archimedean labels are τ-image naming, not derivation inputs. The
sweep heuristic over-flagged because the localised text "by the
volume conjecture" matches `proof-input`-style language even though
the sectioning makes the framing explicit. **No action required.**

The triage heuristic in `wall_violations_sweep.py` could be refined
to recognise the "Post-Archimedean naming" / "borrowed, not part of
derivation" header pattern; tracked as a follow-up enhancement
rather than blocking on this audit.

### 2. `local-substrate-q-proof.md` (1 hit) — ✅ resolved by P0.2

Initial context (real wall violation):

```
[topological mass formula](#prop:topological-mass-formula) gives
$m_\mu / m_e = \mathrm{Vol}(4_1) / \hbar_q^{2}$ with
$\hbar_q = 1 - q^{-1}$ ...
```

Used hyperbolic volume $\mathrm{Vol}(4_1) \approx 2.0299$ as a
numerical derivation input — flagged as a wall violation per
audit §4·B.

**Fix landed (commit on this branch)**: the proof now cites
[`prop:topological-mass-formula-algebraic`](../../content/quantum-observable-universe/braids-and-knots/topological-mass-formula-algebraic.md)
and routes through $\Phi_1(4_1) = \tau_{\mathrm{arch}}(\mathrm{Vol}_q(4_1))$
with the Archimedean value entering only as the final
$\tau_{\mathrm{arch}}$-specialised step. Resulting prose:

> The **algebraic** topological mass formula gives the mass ratio
> at the level of $\mathbb{Q}(q)$ as $m_\mu / m_e = \Phi_1(4_1) /
> \hbar_q^{2}$, where $\Phi_1(4_1) = \tau_{\mathrm{arch}}(\mathrm{Vol}_q(4_1))$.
> The Archimedean form of the same identity is the specialisation
> under $\tau_{\mathrm{arch}}$ … as **τ-side naming** (not as a
> derivation step).

Re-running the sweep confirms zero `proof-input` hits in this
file post-fix.

### 3. `skein-mass-relation-proof.md` (1 hit) — ✅ resolved by P0.2

Same pattern as #2: the proof now routes through
$\Phi_1(4_1) = \tau_{\mathrm{arch}}(\mathrm{Vol}_q(4_1))$ via
[`prop:topological-mass-formula-algebraic`](../../content/quantum-observable-universe/braids-and-knots/topological-mass-formula-algebraic.md)
with the Archimedean value entering only as the final
$\tau_{\mathrm{arch}}$-specialised step. Re-running the sweep
confirms zero `proof-input` hits in this file post-fix.

## `tau-image` hits (2 — allowed)

The two `tau-image` hits are in
[`mass-identity-su2-proof.md`](../../content/quantum-observable-universe/lifting-and-descent/mass-identity-su2-proof.md):
both occur in an explicit "Archimedean realization" subsection that
identifies the mass identity at $q = 1$ with the Mostow-rigid
hyperbolic structure on $\mathrm{SU}(2)$. This is correct τ-side
framing per audit §4. **No action required.**

## `context-only` hits (17 — allowed)

The 17 `context-only` hits span 5 files (varying counts), all
matching the volume / Mostow / hyperbolic markers in motivational
prose, citation lists, or intro paragraphs without being part of
a derivation step. **No action required.**

## Summary

| Severity | Count | Notes |
|----------|------:|-------|
| 🟢 False positive (correctly framed) | 3 | `atom-knot-mass-derivation-proof.md` — explicit "borrowed, not part of derivation" |
| 🔴 Real wall violation | 2 | `local-substrate-q-proof.md` and `skein-mass-relation-proof.md` — both use $\mathrm{Vol}(4_1)$ as a numerical derivation input |
| 🟢 `tau-image` (allowed) | 2 | Explicit τ-side framing |
| 🟢 `context-only` (allowed) | 17 | Motivational prose / citations |

**Net audit result.** Of 149 proof blocks, **2 real wall
violations** were identified, both **resolved by the P0.2 recast
on this branch**:
[`prop:topological-mass-formula-algebraic`](../../content/quantum-observable-universe/braids-and-knots/topological-mass-formula-algebraic.md)
states the mass identity in $\mathbb{Q}(q)$ via
$\Phi_1 = \tau_{\mathrm{arch}}(\mathrm{Vol}_q)$, with the
Archimedean form recovered as a $\tau_{\mathrm{arch}}$-
specialisation; the two affected proofs now cite the algebraic
version with τ-side naming as the final numerical step. The
post-fix sweep records:

- 5 → **3 `proof-input` hits**, all in
  [`atom-knot-mass-derivation-proof.md`](../../content/quantum-observable-universe/braids-and-knots/atom-knot-mass-derivation-proof.md)
  (the false-positive cluster — see triage #1; **no action
  required**).
- 17 → 25 `context-only` hits (the recast adds explanatory prose
  that mentions Archimedean / volume language; all in
  context-only triage).
- 2 `tau-image` hits unchanged.

🟢 **All real wall violations cleared.** P0.1 + P0.2 closure is
complete on this branch.

## Reproducibility

```bash
python3 computations/sweeps/wall_violations_sweep.py
# → computations/sweeps/wall-violations-sweep.witness.json
```

The sweep is deterministic given the file set; rerun after any
proof-block edit to confirm no new violations.

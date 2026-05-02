# P0.1 wall-violation sweep — 2026-05-02

**Pair**: [`2026-05-01-math-framework-deep-audit.md`](2026-05-01-math-framework-deep-audit.md)
§4 (strict-archimedean-wall) + [`2026-05-01-math-framework-workplan.md`](2026-05-01-math-framework-workplan.md)
P0.1.

**Branch**: `claude/tier-4-math-audit-EkI7a`

## Sweep methodology

[`folio-assistant/computations/wall_violations_sweep.py`](../../folio-assistant/computations/wall_violations_sweep.py)
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

Output: [`folio-assistant/computations/wall-violations-sweep.witness.json`](../../folio-assistant/computations/wall-violations-sweep.witness.json).

## Sweep result (149 proof files)

| Triage label | Count |
|--------------|------:|
| `proof-input` (likely violation) | 5 |
| `tau-image` (allowed) | 2 |
| `context-only` (allowed) | 17 |
| **Files with at least one hit** | 6 / 149 |

The 5 `proof-input` hits land in 3 files. Manual triage below.

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

### 2. `local-substrate-q-proof.md` (1 hit) — 🔴 real wall violation

Context:

```
[topological mass formula](#prop:topological-mass-formula) gives
$m_\mu / m_e = \mathrm{Vol}(4_1) / \hbar_q^{2}$ with
$\hbar_q = 1 - q^{-1}$ ...
```

Uses **hyperbolic volume of the figure-eight knot**
$\mathrm{Vol}(4_1) \approx 2.0299$ as a numerical input to derive
the mass ratio $m_\mu / m_e$. This is the wall risk flagged in
audit §4·B: the proof should use
[`def:algebraic-quantum-volume`](../../content/quantum-observable-universe/braids-and-knots/algebraic-quantum-volume.md)'s
$\mathrm{Vol}_q(4_1)$ instead, with the Archimedean value being a
specialisation under $\tau_{\mathrm{arch}}$ rather than a
derivation input.

**Fix path**: requires workplan **P0.2** (land
algebraic-quantum-volume recast). Once `prop:topological-mass-formula`
is restated to use $\mathrm{Vol}_q$, this proof becomes
algebraic-side throughout with the $\tau_{\mathrm{arch}}$
specialisation as the final numerical step.

### 3. `skein-mass-relation-proof.md` (1 hit) — 🔴 real wall violation

Context:

```
the lepton--electron *ratio* eliminates the overall mass scale and
gives $m_\mu / m_e = \mathrm{Vol}(4_1) / \hbar_q^{2}$.  Substituting
$\hbar_q = 1 - q^{-1}$ and the CODATA value ...
```

Same pattern as #2: $\mathrm{Vol}(4_1)$ used as numerical
derivation input. Same fix path (P0.2 recast).

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

**Net audit result.** Of 149 proof blocks, **2 are real wall
violations**, both blocked on workplan **P0.2** (algebraic-quantum-
volume recast). Once P0.2 lands, the standard fix is to replace
$\mathrm{Vol}(4_1)$ with $\mathrm{Vol}_q(4_1)$ in both proofs, with
the Archimedean specialisation appearing only as the final
numerical step. The remaining 22 hits across 4 other files are
either correctly framed (post-Archimedean naming, τ-image, or
context-only).

## Reproducibility

```bash
python3 folio-assistant/computations/wall_violations_sweep.py
# → folio-assistant/computations/wall-violations-sweep.witness.json
```

The sweep is deterministic given the file set; rerun after any
proof-block edit to confirm no new violations.

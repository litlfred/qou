> **DEPRECATED on 2026-05-24.** Workplan / status snapshot / investigation result / closure-attempt that has been integrated into main or superseded by a later resolution. Original audit preserved here for historical record. See [`docs/audits/INDEX.md`](../INDEX.md) for the tranche rationale.

# A.3 v2 result — shell-aware level-1 (Manhattan distance to magic) FAILED to close spread

**Pair:** [`per_braid_tower_shell_aware.py`](../../computations/per_braid_tower_shell_aware.py)
+ witness [`2026-05-02-shell-aware-level-1.witness.json`](2026-05-02-shell-aware-level-1.witness.json).

The cal/m_e structure audit
([`2026-05-02-cal-spread-structure.md`](2026-05-02-cal-spread-structure.md))
identified 4He as the doubly-magic outlier driving the 1.06%
spread. A.3 v2 attempted a shell-aware level-1 correction:

$$
  m_{\mathrm{total}}(Z, N) = m^{(0)}(Z, N) \cdot \bigl(1 - \varepsilon \cdot e^{-d(Z, N)/\mathrm{scale}}\bigr)
$$

where $d(Z, N) = \min_{Z^*, N^* \in \mathrm{MAGIC}} (|Z-Z^*| + |N-N^*|)$
is the Manhattan distance to the closest magic shell-pair, and
$\varepsilon$ is fitted on 4He. **Test of universality**: same
$\varepsilon$ applied to all atoms — does it close the spread?

## Result: NO

| | Level-0 only | Shell-aware ($\varepsilon = 1.46\%$ on 4He) |
|---|---:|---:|
| Mean cal/m_e | 0.987 | 0.997 |
| Spread % | **1.06%** | **1.19%** (worse) |

The mean shifted toward 1.0 (good — that's just absorbed by $E_0$
calibration), but the **spread got slightly worse**.

### Per-atom

| atom | $A$ | $d$ | shell_factor | level-0 cal/m_e | shell-aware cal/m_e |
|------|----:|----:|-------------:|----------------:|--------------------:|
| D | 2 | 2 | 0.607 | 0.99181 | **1.00069** |
| 3He | 3 | 1 | 0.779 | 0.98997 | **1.00139** |
| 3H | 3 | 1 | 0.779 | 0.99016 | **1.00158** |
| 4He | 4 | 0 | 1.000 | 0.98536 | **1.00000** (anchor) |
| 6Li | 6 | 2 | 0.607 | 0.98732 | 0.99616 |
| 7Li | 7 | 3 | 0.472 | 0.98701 | 0.99388 |
| 9Be | 9 | 5 | 0.287 | 0.98570 | 0.98985 |
| 12C | 12 | 4 | 0.368 | 0.98438 | 0.98971 |
| 16O | 16 | 0 | 1.000 | 0.98376 | 0.99838 |
| 40Ca | 40 | 0 | 1.000 | 0.98133 | 0.99591 |

## What went wrong

1. **Light atoms (D, 3He, 3H) overshoot.** They get a substantial
   correction (shell_factor 0.6–0.78) because they're "close to"
   magic 4He. But these atoms are **sub-saturated**, in the
   building-up region BEFORE 4He — they shouldn't get a binding
   enhancement based on proximity.
2. **Magic atoms cluster but don't all need the same $\varepsilon$.**
   Fitting on 4He gives $\varepsilon = 1.46\%$. Applying that to
   16O leaves it at 0.998 (slightly under-corrected). Applying
   to 40Ca leaves it at 0.996 (more under-corrected). The
   shell binding fraction does NOT scale uniformly across the
   magic ladder.
3. **Manhattan distance is the wrong metric.** Real shell binding
   correlates with shell-index *occupation*, not euclidean-style
   distance. 7Li (Z=3, N=4) is closer to 4He than 9Be (Z=4, N=5)
   in $d(Z,N)$, but its actual shell occupation profile is
   different.

## Why the original audit was right but this implementation isn't

The cal-spread audit's claim — "spread driven by 4He, fix is
shell-aware level-1" — remains correct in spirit. What this v2
implementation got wrong is **the form of the shell factor**.

The actual shell-correction physics involves:

- **Shell occupancy** (how filled is each major shell at $Z, N$),
  not raw distance.
- **Pairing** (proton-proton vs proton-neutron vs neutron-neutron
  pair-binding asymmetries).
- **Symmetry / asymmetry energy** ($|N - Z|$ effects from the
  semi-empirical mass formula).

A simple multiplicative $1 - \varepsilon \cdot \mathrm{shell\_factor}$
collapses all of these into one knob; it's mathematically too
restrictive to capture the actual structure.

## What would work

Three candidate next steps:

1. **Use BB-stratification properly.** PR #500's
   `optimised_magic_verifier.py` checks LR-fusion compatibility
   on shell-pair indices $(i_Z, i_N) \in \{1, \dots, 7\}^2$ with
   $|i_Z - i_N| \leq 1$ (Δi ≤ 1 rule). The shell-correction at
   $(Z, N)$ should depend on whether $(Z, N)$ saturates a
   shell-pair $(i_Z, i_N)$, NOT just euclidean distance to a
   magic atom.
2. **Per-Wedderburn-block enrichment.** Instead of a global
   multiplicative factor, sum shell contributions from each
   Wedderburn block $\lambda \vdash 3A$ that has BB-stratum-
   saturated structure. Closed shells happen because more
   $\lambda$'s contribute non-trivially.
3. **SEMF-style decomposition.** Add a Wigner–Bethe asymmetry
   term ($\propto (N-Z)^2/A$) and pairing term ($\propto
   \delta(\mathrm{parity})$) to capture the structural variables
   the Manhattan metric misses.

Option (2) is the most aligned with the categorical framework
and could be implemented as a level-1 jet contribution that
sums over BB-saturated $\lambda$'s.

## Status

**A.3 v2 (Manhattan-distance shell_factor): negative result —
spread got slightly worse.** The hypothesis was right (shell
structure IS the relevant variable), but the implementation
form was too crude. The real fix needs LR-compatibility-based
shell occupancy or per-Wedderburn-block BB-saturation
counting, not a multiplicative distance penalty.

A.3 v3 should pursue option (1) or (2) above.
